#!/usr/bin/env python3
"""
scripts/generate_pbr_3d.py
=============================================================================
Fases 3, 4 y 5: Geometría Hunyuan3D-2mv + Proyección Multi-Vista Directa 2K
               + Síntesis de Mapas PBR (Normal & Roughness) + QA Visual
=============================================================================
Mejoras clave respecto a generate_hunyuan_mv_3d.py:
  1. No desecha 5 de las 6 vistas en el texturizado: proyecta directamente
     las 6 vistas limpias 2K sobre las UV de la malla usando MeshRender.back_project
     en las cámaras verificadas (elev=0 azim=0/90/180/270 y elev=±89.5).
  2. Alinea automáticamente cada recorte RGBA al bounding box real de la silueta 3D
     renderizada en ese ángulo (y prueba rotaciones 0/90/180/270 en top-down/outsole
     para asegurar coincidencia exacta de puntera y talón).
  3. Usa uv_inpaint solo en zonas ocluidas (entre cordones/ojales/interior cuello),
     conservando intactos los logotipos reales (Jumpman, "23", Swoosh, costuras).
  4. Genera Normal Map 2K y Metallic-Roughness Map 2K para dar relieve físico al
     cuero, malla y suela dentro de <model-viewer>.
  5. Exporta .glb + .glb.js y renderiza hoja de QA 2x3 para inspección visual.
"""

import argparse
import base64
import gc
import io
import json
import os
import sys
import time
from typing import Dict, List, Optional, Tuple

import cv2
import numpy as np
import pygltflib
import torch
import torch.nn.functional as F
import trimesh
from PIL import Image, ImageDraw

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)
for p in (CURRENT_DIR, PROJECT_DIR):
    if p not in sys.path:
        sys.path.insert(0, p)

sys.path.insert(0, os.path.abspath(os.path.join(PROJECT_DIR, "scratch", "Hunyuan3D-2")))

import huggingface_hub.file_download as hf_fd

hf_fd.are_symlinks_supported = lambda *args, **kwargs: False

from hy3dgen.texgen.differentiable_renderer.mesh_render import MeshRender
from hy3dgen.texgen.utils.uv_warp_utils import mesh_uv_wrap

from color_lock import extract_clean_rgba, load_catalog_metadata
from extract_grid_views import extract_8_views_from_grid

# Mapeo verificado experimentalmente contra MeshRender.render_normal / get_mv_matrix:
# azim=0 -> lateral (toe LEFT), azim=90 -> rear heel, azim=180 -> medial (toe RIGHT),
# azim=270 -> front toe, elev=+89.5 -> top-down, elev=-89.5 -> outsole.
# (slug, web_fn, elev, azim, weight, allow_rot, angle_thres)
CAMERA_VIEW_CONFIG = [
    ("01_lateral", "01-lateral.webp", 0.0, 0.0, 1.00, False, 56.0),
    ("06_rear", "06-rear.webp", 0.0, 90.0, 0.90, False, 52.0),
    ("02_medial", "02-medial.webp", 0.0, 180.0, 1.00, False, 56.0),
    ("05_front", "05-front.webp", 0.0, 270.0, 1.00, False, 64.0),
    ("07_top_down", "07-top-down.webp", 89.5, 0.0, 1.40, True, 60.0),
    ("08_outsole", "08-outsole.webp", -89.5, 0.0, 0.95, True, 60.0),
]


def resolve_rgba_views(sku: str, rembg_session=None, grid_path: Optional[str] = None) -> Dict[str, Image.Image]:
    """
    Carga vistas RGBA limpias desde --grid (si se indica), o priorizando
    scratch/pilot_work/studio_rgba/{sku}/ y dist/assets/productos/{sku}/.
    """
    if grid_path:
        grid_cache = os.path.join(PROJECT_DIR, "scratch", "pilot_work", "grid_rgba", sku)
        print(f"[{sku}] Extrayendo 8 vistas limpias desde grid: {grid_path}", flush=True)
        return extract_8_views_from_grid(grid_path, out_rgba_dir=grid_cache, rembg_session=rembg_session)

    studio_dir = os.path.join(PROJECT_DIR, "scratch", "pilot_work", "studio_rgba", sku)
    prod_dir = os.path.join(PROJECT_DIR, "dist", "assets", "productos", sku)
    cache_dir = os.path.join(PROJECT_DIR, "scratch", "pilot_work", "proj_rgba_cache", sku)
    os.makedirs(cache_dir, exist_ok=True)

    views: Dict[str, Image.Image] = {}
    for slug, web_fn, _, _, _, _, _ in CAMERA_VIEW_CONFIG:
        p_studio = os.path.join(studio_dir, f"{slug}.png")
        p_cache = os.path.join(cache_dir, f"{slug}.png")
        p_prod = os.path.join(prod_dir, web_fn)

        if os.path.exists(p_studio):
            views[slug] = Image.open(p_studio).convert("RGBA")
        elif os.path.exists(p_cache):
            views[slug] = Image.open(p_cache).convert("RGBA")
        elif os.path.exists(p_prod):
            rgba = extract_clean_rgba(p_prod, rembg_session=rembg_session, use_rembg=True)
            rgba.save(p_cache)
            views[slug] = rgba
    return views


def get_hy3d_geometry_locked_base(
    sku: str,
    mesh: trimesh.Trimesh,
    ref_rgba: Image.Image,
    tag: str = "",
) -> Tuple[trimesh.Trimesh, Image.Image]:
    """
    Genera (y cachea) una textura base 2K bloqueada exactamente a la geometría 3D usando
    Hunyuan3DPaintPipeline. Esto garantiza que los relieves de los pasadores y las curvas
    del tope frontal queden 100% alineados sin bordes blancos ni huecos.
    """
    suffix = f"_{tag}" if tag else ""
    base_dir = os.path.join(PROJECT_DIR, "scratch", "pilot_work", "hy3d_base")
    os.makedirs(base_dir, exist_ok=True)
    base_glb = os.path.join(base_dir, f"{sku}{suffix}_base.glb")
    base_tex_png = os.path.join(base_dir, f"{sku}{suffix}_base.png")

    if os.path.exists(base_glb) and os.path.exists(base_tex_png):
        m = trimesh.load(base_glb)
        if isinstance(m, trimesh.Scene):
            m = m.to_geometry()
        if isinstance(m.visual, trimesh.visual.TextureVisuals) and getattr(m.visual, "uv", None) is not None:
            print(f"[{sku}] Reutilizando base geométrica HunyuanPaint cacheada...", flush=True)
            return m, Image.open(base_tex_png).convert("RGB")

    from hy3dgen.texgen import Hunyuan3DPaintPipeline

    print(f"[{sku}] Generando textura base alineada a geometría (Hunyuan3DPaintPipeline)...", flush=True)
    paint_pipe = Hunyuan3DPaintPipeline.from_pretrained(
        "tencent/Hunyuan3D-2",
        subfolder="hunyuan3d-paint-v2-0-turbo",
    )
    paint_pipe.enable_model_cpu_offload()
    try:
        paint_pipe.models["delight_model"].pipeline.enable_attention_slicing()
        paint_pipe.models["delight_model"].pipeline.vae.enable_slicing()
        paint_pipe.models["multiview_model"].pipeline.enable_attention_slicing()
        paint_pipe.models["multiview_model"].pipeline.vae.enable_slicing()
    except Exception:
        pass

    textured_mesh = paint_pipe(mesh.copy(), image=ref_rgba.convert("RGBA"))
    base_img = getattr(textured_mesh.visual.material, "image", None) or getattr(
        textured_mesh.visual.material, "baseColorTexture", None
    )
    base_img = base_img.convert("RGB")
    base_img.save(base_tex_png)

    uvs = np.asarray(textured_mesh.visual.uv, dtype=np.float32)
    textured_mesh.visual = trimesh.visual.TextureVisuals(uv=uvs)
    textured_mesh.export(base_glb)

    del paint_pipe
    gc.collect()
    torch.cuda.empty_cache()
    return textured_mesh, base_img


def load_or_generate_uv_mesh(
    sku: str,
    views: Dict[str, Image.Image],
    regen_shape: bool = False,
    max_faces: int = 55000,
    tag: str = "",
) -> trimesh.Trimesh:
    """Carga la malla blanca cacheada o genera geometría nueva con Hunyuan3D-2mv, luego aplica UV unwrap."""
    suffix = f"_{tag}" if tag else ""
    white_path = os.path.join(PROJECT_DIR, "scratch", "hy3d_tmp", f"{sku}{suffix}_white.glb")
    uv_cache_path = os.path.join(PROJECT_DIR, "scratch", "pilot_work", "uv_meshes", f"{sku}{suffix}_uv.glb")
    os.makedirs(os.path.dirname(uv_cache_path), exist_ok=True)

    if os.path.exists(uv_cache_path) and not regen_shape:
        m = trimesh.load(uv_cache_path)
        if isinstance(m, trimesh.Scene):
            m = m.to_geometry()
        if isinstance(m.visual, trimesh.visual.TextureVisuals) and getattr(m.visual, "uv", None) is not None:
            print(f"[{sku}] Reutilizando malla UV cacheada ({len(m.faces)} tris)", flush=True)
            return m

    if regen_shape or not os.path.exists(white_path):
        from hy3dgen.shapegen import (
            DegenerateFaceRemover,
            FaceReducer,
            FloaterRemover,
            Hunyuan3DDiTFlowMatchingPipeline,
        )

        print(f"[{sku}] Generando geometría base con Hunyuan3D-2mv...", flush=True)
        shape_pipe = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained(
            "tencent/Hunyuan3D-2mv",
            subfolder="hunyuan3d-dit-v2-mv",
            variant="fp16",
            device="cpu",
            dtype=torch.float16,
        )
        shape_pipe.components = {
            "conditioner": shape_pipe.conditioner,
            "model": shape_pipe.model,
            "vae": shape_pipe.vae,
        }
        shape_pipe.enable_model_cpu_offload(device="cuda")
        shape_pipe.device = torch.device("cuda")

        mv_in = {
            "front": views["01_lateral"],
            "left": views["05_front"],
            "back": views["02_medial"],
            "right": views["06_rear"],
        }
        mesh = shape_pipe(
            image=mv_in,
            num_inference_steps=38,
            octree_resolution=320,
            num_chunks=12000,
            generator=torch.manual_seed(42),
            output_type="trimesh",
        )[0]
        mesh = FloaterRemover()(mesh)
        mesh = DegenerateFaceRemover()(mesh)
        mesh = FaceReducer()(mesh, max_facenum=max_faces)
        os.makedirs(os.path.dirname(white_path), exist_ok=True)
        mesh.export(white_path)
        del shape_pipe
        gc.collect()
        torch.cuda.empty_cache()
    else:
        mesh = trimesh.load(white_path)
        if isinstance(mesh, trimesh.Scene):
            mesh = mesh.to_geometry()

    # Suavizado Taubin conservador de volumen para quitar crestas dentadas en pasadores antes del UV
    if hasattr(trimesh, "smoothing") and hasattr(trimesh.smoothing, "filter_taubin"):
        mesh = trimesh.smoothing.filter_taubin(mesh, lamb=0.45, nu=-0.46, iterations=4)

    print(f"[{sku}] Parametrizando UVs con xatlas ({len(mesh.faces)} tris)...", flush=True)
    mesh = mesh_uv_wrap(mesh)
    uvs = np.asarray(mesh.visual.uv, dtype=np.float32)
    mesh.visual = trimesh.visual.TextureVisuals(uv=uvs)
    mesh.export(uv_cache_path)
    return mesh


def _tight_rgba_crop(rgba: Image.Image) -> Image.Image:
    arr = np.array(rgba.convert("RGBA"))
    ys, xs = np.where(arr[:, :, 3] > 24)
    if len(xs) == 0:
        return rgba
    return rgba.crop((int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1))


def _voronoi_color_bleed(rgb: np.ndarray, alpha: np.ndarray) -> np.ndarray:
    """
    Rellena TODOS los píxeles fuera de la máscara interior pura del zapato usando el color
    del píxel válido más cercano (Voronoi vía distanceTransformWithLabels).
    Evita que queden píxeles negros [0,0,0] o halos blancos alrededor de pasadores y puntera.
    """
    raw_mask = (alpha > 210).astype(np.uint8)
    erode_k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    core_mask = cv2.erode(raw_mask, erode_k)
    if core_mask.sum() < 100:
        core_mask = raw_mask

    inv = (1 - core_mask).astype(np.uint8)
    if inv.sum() == 0 or core_mask.sum() == 0:
        return rgb

    _, labels = cv2.distanceTransformWithLabels(inv, cv2.DIST_L2, 5, labelType=cv2.DIST_LABEL_PIXEL)
    # Mapear etiqueta -> coordenada (y, x) del píxel válido más cercano
    fg_ys, fg_xs = np.where(core_mask > 0)
    # En OpenCV, labels en píxeles de fondo apuntan al índice 1..N en orden de escaneo donde inv==0
    out = rgb.copy()
    bg_ys, bg_xs = np.where(inv > 0)
    lbl_vals = labels[bg_ys, bg_xs] - 1
    lbl_vals = np.clip(lbl_vals, 0, len(fg_ys) - 1)
    out[bg_ys, bg_xs] = rgb[fg_ys[lbl_vals], fg_xs[lbl_vals]]
    return out


def align_photo_to_mesh_silhouette(
    mr: MeshRender,
    rgba_photo: Image.Image,
    elev: float,
    azim: float,
    res: int = 2048,
    allow_rotations: bool = False,
) -> Tuple[Image.Image, float]:
    """
    Renderiza la silueta exacta de la malla 3D en (elev, azim), encuentra la mejor
    orientación y refina (dx, dy, sx, sy) por IoU de silueta, rellenando el exterior
    con Voronoi color-bleed sin premultiplicar alfa (cero bordes negros).
    """
    normal_np = mr.render_normal(elev, azim, resolution=res, return_type="np")
    mesh_mask = np.any(normal_np < 0.985, axis=-1)
    ys, xs = np.where(mesh_mask)
    if len(xs) < 100:
        return Image.new("RGB", (res, res), (255, 255, 255)), 0.0

    mx0, mx1 = int(xs.min()), int(xs.max())
    my0, my1 = int(ys.min()), int(ys.max())
    mw, mh = mx1 - mx0 + 1, my1 - my0 + 1

    base_crop = _tight_rgba_crop(rgba_photo)
    candidates = [base_crop]
    if allow_rotations:
        candidates = [
            base_crop,
            base_crop.rotate(90, expand=True),
            base_crop.rotate(180, expand=True),
            base_crop.rotate(270, expand=True),
            base_crop.transpose(Image.Transpose.FLIP_LEFT_RIGHT),
            base_crop.transpose(Image.Transpose.FLIP_LEFT_RIGHT).rotate(180, expand=True),
        ]

    # Buscar orientación ganadora a resolución rápida (256px)
    probe = min(256, res)
    scale_p = probe / float(res)
    mesh_p = cv2.resize(mesh_mask.astype(np.uint8), (probe, probe), interpolation=cv2.INTER_NEAREST) > 0
    pmx0, pmx1 = int(mx0 * scale_p), int(mx1 * scale_p)
    pmy0, pmy1 = int(my0 * scale_p), int(my1 * scale_p)
    pmw, pmh = max(4, pmx1 - pmx0 + 1), max(4, pmy1 - pmy0 + 1)

    best_iou = -1.0
    best_cand = candidates[0]
    best_affine = (0.0, 0.0, 1.0, 1.0)  # dx_frac, dy_frac, sx, sy

    for cand in candidates:
        c_arr = np.array(cand.convert("RGBA"))
        c_mask = (c_arr[:, :, 3] > 100).astype(np.uint8)
        p_mask = cv2.resize(c_mask, (pmw, pmh), interpolation=cv2.INTER_NEAREST) > 0
        canvas_p = np.zeros((probe, probe), dtype=bool)
        canvas_p[pmy0 : pmy0 + pmh, pmx0 : pmx0 + pmw] = p_mask
        inter = float(np.logical_and(canvas_p, mesh_p).sum())
        union = float(np.logical_or(canvas_p, mesh_p).sum())
        iou = inter / union if union > 0 else 0.0
        if iou > best_iou:
            best_iou = iou
            best_cand = cand

    # Refinamiento fino de desplazamiento y escala (±4%) sobre la orientación ganadora
    win_arr = np.array(best_cand.convert("RGBA"))
    win_mask = (win_arr[:, :, 3] > 100).astype(np.uint8)
    for sx in (0.97, 1.0, 1.03, 1.06):
        for sy in (0.97, 1.0, 1.03):
            tw, th = max(4, int(round(pmw * sx))), max(4, int(round(pmh * sy)))
            rm = cv2.resize(win_mask, (tw, th), interpolation=cv2.INTER_NEAREST) > 0
            for dx in (-0.025, 0.0, 0.025):
                for dy in (-0.02, 0.0, 0.02):
                    ox = pmx0 + (pmw - tw) // 2 + int(round(dx * pmw))
                    oy = pmy0 + (pmh - th) // 2 + int(round(dy * pmh))
                    x_dst0, y_dst0 = max(0, ox), max(0, oy)
                    x_dst1, y_dst1 = min(probe, ox + tw), min(probe, oy + th)
                    x_src0, y_src0 = x_dst0 - ox, y_dst0 - oy
                    x_src1, y_src1 = x_src0 + (x_dst1 - x_dst0), y_src0 + (y_dst1 - y_dst0)
                    if x_dst1 <= x_dst0 or y_dst1 <= y_dst0:
                        continue
                    test_m = np.zeros((probe, probe), dtype=bool)
                    test_m[y_dst0:y_dst1, x_dst0:x_dst1] = rm[y_src0:y_src1, x_src0:x_src1]
                    inter = float(np.logical_and(test_m, mesh_p).sum())
                    union = float(np.logical_or(test_m, mesh_p).sum())
                    iou = inter / union if union > 0 else 0.0
                    if iou > best_iou:
                        best_iou = iou
                        best_affine = (dx, dy, sx, sy)

    # Aplicar transformación óptima a resolución completa SIN premultiplicar alfa sobre RGB
    dx, dy, sx, sy = best_affine
    fw = max(8, int(round(mw * sx)))
    fh = max(8, int(round(mh * sy)))
    rgb_clean = _voronoi_color_bleed(win_arr[:, :, :3], win_arr[:, :, 3])
    rgb_resized = cv2.resize(rgb_clean, (fw, fh), interpolation=cv2.INTER_LANCZOS4)
    alpha_resized = cv2.resize(win_arr[:, :, 3], (fw, fh), interpolation=cv2.INTER_LINEAR)

    # Colocar en lienzo completo res x res y re-aplicar Voronoi bleed global para eliminar cualquier borde
    canvas_rgb = np.zeros((res, res, 3), dtype=np.uint8)
    canvas_alpha = np.zeros((res, res), dtype=np.uint8)
    ox = mx0 + (mw - fw) // 2 + int(round(dx * mw))
    oy = my0 + (mh - fh) // 2 + int(round(dy * mh))

    xd0, yd0 = max(0, ox), max(0, oy)
    xd1, yd1 = min(res, ox + fw), min(res, oy + fh)
    xs0, ys0 = xd0 - ox, yd0 - oy
    xs1, ys1 = xs0 + (xd1 - xd0), ys0 + (yd1 - yd0)
    if xd1 > xd0 and yd1 > yd0:
        canvas_rgb[yd0:yd1, xd0:xd1] = rgb_resized[ys0:ys1, xs0:xs1]
        canvas_alpha[yd0:yd1, xd0:xd1] = alpha_resized[ys0:ys1, xs0:xs1]

    final_rgb = _voronoi_color_bleed(canvas_rgb, canvas_alpha)
    return Image.fromarray(final_rgb, mode="RGB"), best_iou


def synthesize_pbr_maps(albedo_pil: Image.Image, uv_valid_mask: np.ndarray) -> Tuple[Image.Image, Image.Image]:
    """
    Genera mapas PBR 2K (Normal Map + Metallic-Roughness Map) a partir de la textura Albedo 2K:
      - Normal Map: relieve multi-escala (costuras, granulado del cuero, malla, suela).
      - Metallic-Roughness (glTF): canal G = roughness, canal B = metallic, canal R = 255.
    """
    rgb = np.array(albedo_pil.convert("RGB")).astype(np.float32) / 255.0
    gray = cv2.cvtColor((rgb * 255).astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32) / 255.0

    # Extraer detalle de alta/media frecuencia filtrando ruido de pixel
    smooth_base = cv2.GaussianBlur(gray, (3, 3), 0.7)
    detail_broad = cv2.GaussianBlur(gray, (9, 9), 2.0)
    height_field = 0.65 * smooth_base + 0.35 * (smooth_base - detail_broad + 0.5)

    gx = cv2.Scharr(height_field, cv2.CV_32F, 1, 0) / 32.0
    gy = cv2.Scharr(height_field, cv2.CV_32F, 0, 1) / 32.0

    strength = 2.6
    nx = -gx * strength
    ny = -gy * strength
    nz = np.ones_like(nx)
    norm = np.sqrt(nx * nx + ny * ny + nz * nz) + 1e-8
    nx /= norm
    ny /= norm
    nz /= norm

    normal_rgb = np.stack([(nx * 0.5 + 0.5), (ny * 0.5 + 0.5), (nz * 0.5 + 0.5)], axis=-1)
    # En márgenes fuera de UV, mantener normal plana neutra [128, 128, 255]
    valid = uv_valid_mask.astype(bool)
    normal_rgb[~valid] = np.array([0.5, 0.5, 1.0], dtype=np.float32)
    normal_pil = Image.fromarray(np.clip(normal_rgb * 255.0, 0, 255).astype(np.uint8), mode="RGB")

    # Roughness adaptativo: zonas muy oscuras brillantes / acentos satinados ~0.35-0.48,
    # blancos de cuero ~0.58-0.68, texturas con alto relieve micro-rugoso ~0.78-0.88.
    grad_mag = np.sqrt(gx * gx + gy * gy)
    local_roughness = 0.62 + 0.16 * np.clip(grad_mag * 8.0, 0.0, 1.0) - 0.18 * np.clip(1.0 - gray * 1.4, 0.0, 1.0)
    local_roughness = cv2.GaussianBlur(np.clip(local_roughness, 0.28, 0.90), (5, 5), 1.0)

    rough_u8 = np.clip(local_roughness * 255.0, 0, 255).astype(np.uint8)
    metal_u8 = np.full_like(rough_u8, 10, dtype=np.uint8)  # ~0.04 dieléctrico realista
    occ_u8 = np.full_like(rough_u8, 255, dtype=np.uint8)
    mr_pil = Image.fromarray(np.stack([occ_u8, rough_u8, metal_u8], axis=-1), mode="RGB")

    return normal_pil, mr_pil


def compress_glb_pbr_textures(glb_bytes: bytes, jpeg_quality: int = 92) -> bytes:
    """
    Re-codifica baseColorTexture y metallicRoughnessTexture dentro del GLB de PNG a JPEG
    (estándar glTF 2.0 core) preservando normalTexture en PNG para evitar artefactos
    en normales y reduciendo el peso total de ~7-8 MB a ~2.5-3.2 MB.
    """
    gltf = pygltflib.GLTF2.load_from_bytes(glb_bytes)
    if not gltf.images or not gltf.buffers:
        return glb_bytes

    blob = bytearray(gltf.binary_blob())

    # Identificar índices de imágenes usadas como normalTexture para conservarlas en PNG
    normal_img_idxs = set()
    for mat in gltf.materials:
        if mat.normalTexture is not None:
            tex_idx = mat.normalTexture.index
            if tex_idx is not None and tex_idx < len(gltf.textures):
                src = gltf.textures[tex_idx].source
                if src is not None:
                    normal_img_idxs.add(src)

    # Extraer geometría/accesores fuera de las bufferViews de imágenes intactas
    img_bv_map = {img.bufferView: idx for idx, img in enumerate(gltf.images) if img.bufferView is not None}

    new_blob = bytearray()
    for bv_idx, bv in enumerate(gltf.bufferViews):
        offset = bv.byteOffset or 0
        chunk = bytes(blob[offset : offset + bv.byteLength])

        if bv_idx in img_bv_map and img_bv_map[bv_idx] not in normal_img_idxs:
            img_obj = gltf.images[img_bv_map[bv_idx]]
            pil_im = Image.open(io.BytesIO(chunk)).convert("RGB")
            jbuf = io.BytesIO()
            pil_im.save(jbuf, format="JPEG", quality=jpeg_quality, optimize=True)
            chunk = jbuf.getvalue()
            img_obj.mimeType = "image/jpeg"

        # Alinear cada bufferView a múltiplo de 4 bytes según especificación glTF 2.0
        while len(new_blob) % 4 != 0:
            new_blob.append(0)
        bv.byteOffset = len(new_blob)
        bv.byteLength = len(chunk)
        new_blob.extend(chunk)

    while len(new_blob) % 4 != 0:
        new_blob.append(0)

    gltf.buffers[0].byteLength = len(new_blob)
    gltf.set_binary_blob(bytes(new_blob))
    return b"".join(gltf.save_to_bytes())


def render_textured_cr(mr: MeshRender, elev: float, azim: float, res: int = 512) -> Image.Image:
    """Renderiza una vista con custom_rasterizer muestreando mr.tex (evita bug de glctx en MeshRender.render)."""
    _, pos_clip = mr.get_pos_from_mvp(elev, azim, None, None)
    rast_out, _ = mr.raster_rasterize(pos_clip, mr.pos_idx, resolution=[res, res])
    uv, _ = mr.raster_interpolate(mr.vtx_uv[None, ...], rast_out, mr.uv_idx)
    vis = torch.clamp(rast_out[0, ..., -1:], 0, 1)
    grid = uv * 2.0 - 1.0
    tex_chw = mr.tex.permute(2, 0, 1).unsqueeze(0)
    sampled = F.grid_sample(tex_chw, grid, mode="bilinear", padding_mode="border", align_corners=False)
    rgb = sampled[0].permute(1, 2, 0) * vis + (1.0 - vis)
    return Image.fromarray((rgb.clamp(0, 1).cpu().numpy() * 255).astype(np.uint8))


def solve_diagonal_camera_pose(
    mr: MeshRender,
    rgba_photo: Image.Image,
    slug: str,
    probe_res: int = 256,
) -> Tuple[float, float, float]:
    """
    Encuentra el ángulo exacto (elev, azim) de una vista 3/4 comparando silueta
    y coincidencia de color contra la malla ya proyectada con vistas ortogonales.
    """
    if slug == "03_3-4_front":
        azim_candidates = [305.0, 315.0, 325.0, 215.0, 225.0, 235.0]
    else:  # 04_3-4_rear
        azim_candidates = [125.0, 135.0, 145.0, 35.0, 45.0, 55.0]
    elev_candidates = [8.0, 14.0, 20.0]

    crop = _tight_rgba_crop(rgba_photo)
    best_score = -999.0
    best_pose = (12.0, azim_candidates[1], 0.0)

    for elev in elev_candidates:
        for azim in azim_candidates:
            normal_np = mr.render_normal(elev, azim, resolution=probe_res, return_type="np")
            mesh_mask = np.any(normal_np < 0.985, axis=-1)
            ys, xs = np.where(mesh_mask)
            if len(xs) < 100:
                continue
            mx0, mx1 = int(xs.min()), int(xs.max())
            my0, my1 = int(ys.min()), int(ys.max())
            mw, mh = mx1 - mx0 + 1, my1 - my0 + 1

            resized = crop.resize((mw, mh), Image.Resampling.LANCZOS)
            r_arr = np.array(resized)
            p_mask = r_arr[:, :, 3] > 60
            m_roi = mesh_mask[my0 : my1 + 1, mx0 : mx1 + 1]

            inter_m = np.logical_and(p_mask, m_roi)
            union_m = np.logical_or(p_mask, m_roi)
            iou = float(inter_m.sum()) / float(union_m.sum()) if union_m.sum() > 0 else 0.0

            # Comparar color en la intersección contra el render actual de las vistas ortogonales
            rendered = np.array(render_textured_cr(mr, elev, azim, res=probe_res))[my0 : my1 + 1, mx0 : mx1 + 1]
            if inter_m.sum() > 50:
                mae = float(np.abs(rendered[inter_m].astype(np.float32) - r_arr[:, :, :3][inter_m].astype(np.float32)).mean() / 255.0)
            else:
                mae = 1.0

            score = 0.55 * iou + 0.45 * (1.0 - mae)
            if score > best_score:
                best_score = score
                best_pose = (elev, azim, iou)

    return best_pose


def blend_projected_views(proj_textures: List[torch.Tensor], proj_cos_maps: List[torch.Tensor]) -> Tuple[torch.Tensor, torch.Tensor]:
    """Combina todas las proyecciones ponderadas por coseno sin descartar vistas 3/4 diagonales."""
    num = torch.zeros_like(proj_textures[0])
    den = torch.zeros_like(proj_cos_maps[0])
    for tex_v, cos_v in zip(proj_textures, proj_cos_maps):
        num += tex_v * cos_v
        den += cos_v
    baked = num / torch.clamp(den, min=1e-8)
    return baked, den > 1e-6


def _compute_zone_masks_in_uv(
    mr: MeshRender, mesh: Optional[trimesh.Trimesh] = None
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Calcula pesos suaves [0..1] directamente sobre vértices 3D y los rasteriza a UV vía
    uv_feature_map (cero desenfoque a través de costuras/islas UV pequeñas como pasadores):
      - lace_uv: corredor central de pasadores/empeine.
      - front_uv: extremo delantero de la puntera negra.
      - rear_tab_uv: trabilla trasera del talón.
      - ridge_uv: relieve/protrusión geométrica local 3D (detecta cordones físicos sobre lengüeta plana).
    Note: en Hunyuan3D camera_utils, el eje +Z apunta hacia la suela (z_max) y -Z arriba (z_min).
    """
    v = mr.vtx_pos
    v_fwd = (v[:, 0] - v[:, 0].min()) / torch.clamp(v[:, 0].max() - v[:, 0].min(), min=1e-5)
    v_side = v[:, 1].abs() / v[:, 1].abs().max().clamp(min=1e-5)
    v_h = (v[:, 2].max() - v[:, 2]) / torch.clamp(v[:, 2].max() - v[:, 2].min(), min=1e-5)

    lace_v = (
        torch.clamp((v_h - 0.22) / 0.08, 0.0, 1.0)
        * torch.clamp((0.88 - v_h) / 0.08, 0.0, 1.0)
        * torch.clamp((0.68 - v_side) / 0.14, 0.0, 1.0)
        * torch.clamp((v_fwd - 0.26) / 0.10, 0.0, 1.0)
        * torch.clamp((0.76 - v_fwd) / 0.10, 0.0, 1.0)
    )

    front_v = (
        torch.clamp((v_fwd - 0.77) / 0.09, 0.0, 1.0)
        * torch.clamp((v_h - 0.04) / 0.05, 0.0, 1.0)
        * torch.clamp((0.36 - v_h) / 0.08, 0.0, 1.0)
    )

    rear_tab_v = (
        torch.clamp((0.24 - v_fwd) / 0.08, 0.0, 1.0)
        * torch.clamp((v_h - 0.70) / 0.08, 0.0, 1.0)
        * torch.clamp((0.48 - v_side) / 0.12, 0.0, 1.0)
    )

    if mesh is not None and len(mesh.vertices) == len(v) and hasattr(trimesh, "smoothing"):
        sm_mesh = mesh.copy()
        trimesh.smoothing.filter_laplacian(sm_mesh, lamb=0.5, iterations=18)
        disp = np.asarray(mesh.vertices, dtype=np.float32) - np.asarray(sm_mesh.vertices, dtype=np.float32)
        vnorm = np.asarray(mesh.vertex_normals, dtype=np.float32)
        ridge_np = np.sum(disp * vnorm, axis=-1)
        r_scale = float(np.percentile(np.abs(ridge_np), 97) + 1e-6)
        ridge_v = torch.from_numpy(ridge_np / r_scale).float().to(mr.device)
    else:
        ridge_v = torch.zeros_like(lace_v)

    uv_feats = mr.uv_feature_map(torch.stack([lace_v, front_v, rear_tab_v, ridge_v], dim=-1), bg=None)
    return (
        uv_feats[:, :, 0:1].clamp(0.0, 1.0),
        uv_feats[:, :, 1:2].clamp(0.0, 1.0),
        uv_feats[:, :, 2:3].clamp(0.0, 1.0),
        uv_feats[:, :, 3:4],
    )


def build_pbr_glb_for_sku(
    sku: str,
    out_dir: str,
    tex_size: int = 2048,
    regen_shape: bool = False,
    rembg_session=None,
    grid_path: Optional[str] = None,
    use_hy3d_base: bool = True,
):
    t0 = time.time()
    views = resolve_rgba_views(sku, rembg_session=rembg_session, grid_path=grid_path)
    if not all(k in views for k in ("01_lateral", "02_medial", "05_front", "06_rear")):
        raise RuntimeError(f"[{sku}] Faltan vistas ortogonales mínimas para 3D (encontradas: {sorted(views.keys())})")

    tag = "grid" if grid_path else ""
    mesh = load_or_generate_uv_mesh(
        sku,
        views,
        regen_shape=regen_shape,
        max_faces=55000,
        tag=tag,
    )

    base_tex_pil = None
    if use_hy3d_base:
        mesh, base_tex_pil = get_hy3d_geometry_locked_base(sku, mesh, views["01_lateral"], tag=tag)

    mr = MeshRender(default_resolution=tex_size, texture_size=tex_size)
    # Evitar que MeshRender borre 17px alrededor de cada pasador en 2048px
    mr.bake_unreliable_kernel_size = 1
    mr.load_mesh(mesh)

    lace_w_uv, front_w_uv, rear_tab_uv, ridge_uv = _compute_zone_masks_in_uv(mr, mesh=mesh)
    lace_bool_uv = lace_w_uv > 0.25

    proj_textures = []
    proj_cos_maps = []
    ious = {}

    for slug, _, elev, azim, weight, allow_rot, thres in CAMERA_VIEW_CONFIG:
        if slug not in views:
            print(f"[{sku}] Aviso: vista {slug} no disponible, omitiendo proyección directa.", flush=True)
            continue
        mr.bake_angle_thres = thres
        aligned_rgb, iou = align_photo_to_mesh_silhouette(
            mr, views[slug], elev=elev, azim=azim, res=tex_size, allow_rotations=allow_rot
        )
        ious[slug] = round(iou, 3)
        print(f"[{sku}] Proyectando {slug} (elev={elev}, azim={azim}, thres={thres}°, silhouette_IoU={iou:.3f})...", flush=True)
        tex_v, cos_v, _ = mr.back_project(aligned_rgb, elev=elev, azim=azim)
        cos_weighted = weight * (cos_v ** 4.0)
        # En 05_front, evitar que la vista plana cruce pasadores físicos con la lengüeta blanca
        if slug == "05_front":
            cos_weighted = torch.where(lace_bool_uv, cos_weighted * 0.02, cos_weighted)
        proj_textures.append(tex_v)
        proj_cos_maps.append(cos_weighted)

    baked_tex, trust_mask = blend_projected_views(proj_textures, proj_cos_maps)

    # Si tenemos vistas 3/4 (03_3-4_front / 04_3-4_rear), llenar únicamente esquinas diagonales sin pisar pasadores
    diag_views = [s for s in ("03_3-4_front", "04_3-4_rear") if s in views]
    if diag_views:
        mr.set_texture(baked_tex.clamp(0, 1))
        mr.bake_angle_thres = 54.0
        for dslug in diag_views:
            delev, dazim, diou = solve_diagonal_camera_pose(mr, views[dslug], dslug)
            aligned_rgb, iou = align_photo_to_mesh_silhouette(
                mr, views[dslug], elev=delev, azim=dazim, res=tex_size, allow_rotations=False
            )
            ious[dslug] = round(iou, 3)
            print(f"[{sku}] Proyectando {dslug} (elev={delev}, azim={dazim}, silhouette_IoU={iou:.3f})...", flush=True)
            tex_d, cos_d, _ = mr.back_project(aligned_rgb, elev=delev, azim=dazim)
            w_d = 0.40 * (cos_d ** 5.0)
            if dslug == "03_3-4_front":
                w_d = torch.where(lace_bool_uv, w_d * 0.05, w_d)
            proj_textures.append(tex_d)
            proj_cos_maps.append(w_d)
        baked_tex, trust_mask = blend_projected_views(proj_textures, proj_cos_maps)

    trust_np = trust_mask.squeeze(-1).cpu().numpy()
    coverage_pct = float(trust_np.mean() * 100.0)
    print(f"[{sku}] Cobertura UV directa de vistas reales/estudio: {coverage_pct:.1f}%", flush=True)

    if base_tex_pil is not None:
        base_np = np.array(base_tex_pil.resize((tex_size, tex_size), Image.Resampling.LANCZOS)).astype(np.float32) / 255.0
        baked_np = baked_tex.clamp(0, 1).cpu().numpy()

        # Igualar blancos de base_np suavemente contra baked_np SIN levantar los negros oscuros
        bluma = base_np.mean(axis=-1, keepdims=True)
        baked_luma = baked_np.mean(axis=-1)
        valid_w = trust_np & (bluma.squeeze(-1) > 0.65) & (baked_luma > 0.65)
        if np.any(valid_w):
            src_w = float(np.median(base_np[valid_w]))
            ref_w = float(np.median(baked_np[valid_w]))
            hi_t = np.clip((bluma - 0.35) / 0.35, 0.0, 1.0)
            base_bal = np.clip(base_np * (1.0 + hi_t * ((ref_w / max(src_w, 1e-4)) - 1.0)), 0.0, 1.0)
        else:
            base_bal = base_np

        merged_np = np.where(trust_np[..., None], baked_np, base_bal)

        # Limpiar brillo alucinado en caras internas no vistas de la trabilla del talón
        rt_np = rear_tab_uv.squeeze(-1).cpu().numpy()
        rt_obs = trust_np & (rt_np > 0.5)
        if np.any(rt_obs):
            rt_col = np.median(baked_np[rt_obs], axis=0)
            rt_miss = (~trust_np) & (rt_np > 0.35)
            merged_np[rt_miss] = merged_np[rt_miss] * (1.0 - 0.85 * rt_np[rt_miss, None]) + rt_col * (0.85 * rt_np[rt_miss, None])

        # Refinar cordones 3D sobresalientes dentro del corredor de pasadores según su color real
        lw_np = lace_w_uv.squeeze(-1).cpu().numpy()
        r_np = ridge_uv.squeeze(-1).cpu().numpy()
        bl_bal = base_bal.mean(axis=-1)
        lace_src = base_bal.copy()
        cord_sample = (lw_np > 0.45) & (r_np > 0.14)
        if np.any(cord_sample):
            is_dark_laces = float(np.median(bl_bal[cord_sample])) < 0.45
            if is_dark_laces:
                dark_target = float(np.clip(np.percentile(bl_bal[cord_sample], 22), 0.025, 0.065))
                cord_w = np.clip((r_np - 0.09) / 0.13, 0.0, 1.0) * (bl_bal < 0.88) * lw_np
                lace_src = lace_src * (1.0 - 0.90 * cord_w[..., None]) + dark_target * (0.90 * cord_w[..., None])
            # Mantener valles planos de lengüeta blanca nítidos con foto real 07_top_down
            valley_w = (r_np < 0.03).astype(np.float32) * (bl_bal > 0.42) * (baked_luma > 0.74) * trust_np * lw_np
            lace_src = lace_src * (1.0 - 0.65 * valley_w[..., None]) + baked_np * (0.65 * valley_w[..., None])

        # Usar gradientes continuos por vértice 3D (cero desenfoque sobre islas UV pequeñas)
        ga = torch.maximum(lace_w_uv, front_w_uv).cpu().numpy().astype(np.float32)
        zone_src = np.where((lace_w_uv > front_w_uv).cpu().numpy(), lace_src, base_bal)
        merged_np = merged_np * (1.0 - ga) + zone_src * ga
        albedo_pil = Image.fromarray(np.clip(merged_np * 255.0, 0, 255).astype(np.uint8), mode="RGB")
    else:
        mask_u8 = (trust_np * 255).astype(np.uint8)
        inpainted_np = mr.uv_inpaint(baked_tex, mask_u8)
        albedo_pil = Image.fromarray(inpainted_np.astype(np.uint8), mode="RGB")

    # Síntesis de mapas PBR 2K
    albedo_arr = np.array(albedo_pil)
    normal_pil, mr_pil = synthesize_pbr_maps(albedo_pil, uv_valid_mask=(albedo_arr.sum(axis=-1) > 10))

    # Guardar hoja QA 2x3 antes de exportar
    mr.set_texture(albedo_pil)
    qa_sheet = Image.new("RGB", (512 * 3, 512 * 2), (255, 255, 255))
    draw = ImageDraw.Draw(qa_sheet)
    for idx, (slug, _, elev, azim, _, _, _) in enumerate(CAMERA_VIEW_CONFIG):
        shot = render_textured_cr(mr, elev, azim, res=512)
        x, y = (idx % 3) * 512, (idx // 3) * 512
        qa_sheet.paste(shot, (x, y))
        draw.text((x + 12, y + 12), f"{sku} | {slug}", fill=(220, 20, 20))

    qa_dir = os.path.join(PROJECT_DIR, "scratch", "pilot_approval")
    os.makedirs(qa_dir, exist_ok=True)
    qa_path = os.path.join(qa_dir, f"{sku}_3d_qa.png")
    qa_sheet.save(qa_path)

    out_mesh = mesh.copy()
    uvs = np.asarray(out_mesh.visual.uv, dtype=np.float32)
    bounds = out_mesh.bounds
    out_mesh.apply_translation(-(bounds[0] + bounds[1]) / 2.0)
    extent = float((bounds[1] - bounds[0]).max())
    if extent > 0:
        out_mesh.apply_scale(0.32 / extent)

    # Redimensionar normal/roughness a 1024 para mantener peso web ágil (~3-5 MB) manteniendo albedo 2K
    pbr_half = max(1024, tex_size // 2)
    normal_export = normal_pil.resize((pbr_half, pbr_half), Image.Resampling.LANCZOS) if tex_size > 1024 else normal_pil
    mr_export = mr_pil.resize((pbr_half, pbr_half), Image.Resampling.LANCZOS) if tex_size > 1024 else mr_pil

    pbr_mat = trimesh.visual.texture.PBRMaterial(
        name=f"{sku}_pbr",
        baseColorTexture=albedo_pil,
        normalTexture=normal_export,
        metallicRoughnessTexture=mr_export,
        metallicFactor=0.04,
        roughnessFactor=1.0,
        normalScale=0.85,
        doubleSided=True,
    )
    out_mesh.visual = trimesh.visual.TextureVisuals(uv=uvs, material=pbr_mat)

    os.makedirs(out_dir, exist_ok=True)
    out_glb = os.path.join(out_dir, f"{sku}.glb")
    glb_bytes = compress_glb_pbr_textures(out_mesh.export(file_type="glb"), jpeg_quality=92)
    with open(out_glb, "wb") as f:
        f.write(glb_bytes)

    b64 = base64.b64encode(glb_bytes).decode("ascii")
    with open(out_glb + ".js", "w", encoding="utf-8") as f:
        f.write(f'window.__GLB_B64=window.__GLB_B64||{{}};window.__GLB_B64["{sku}"]="{b64}";\n')

    # Verificación rápida del GLB exportado
    verify = trimesh.load(out_glb)
    vmesh = verify.to_geometry() if isinstance(verify, trimesh.Scene) else verify
    vmat = vmesh.visual.material
    has_norm = getattr(vmat, "normalTexture", None) is not None
    has_mr = getattr(vmat, "metallicRoughnessTexture", None) is not None
    dt = time.time() - t0
    print(
        f"[{sku}] GLB PBR guardado ({len(glb_bytes)/1024/1024:.2f} MB, tris={len(vmesh.faces)}, "
        f"normal={has_norm}, roughness={has_mr}) en {dt:.1f}s -> {out_glb}",
        flush=True,
    )
    print(f"[{sku}] QA render -> {qa_path}", flush=True)
    gc.collect()
    torch.cuda.empty_cache()
    return {"sku": sku, "glb": out_glb, "qa_render": qa_path, "size_mb": round(len(glb_bytes) / 1048576, 2), "ious": ious}


def main():
    parser = argparse.ArgumentParser(description="Genera modelos 3D .GLB PBR multi-vista proyectados en 2K.")
    parser.add_argument("--skus", nargs="+", help="SKUs específicos a construir.")
    parser.add_argument("--approved-json", help="Ruta a approved_skus.json descargado del tablero.")
    parser.add_argument("--all", action="store_true", help="Procesar los 45 SKUs del catálogo.")
    parser.add_argument("--out-dir", default=os.path.join(PROJECT_DIR, "scratch", "pilot_3d_out"), help="Carpeta de salida .glb.")
    parser.add_argument("--deploy", action="store_true", help="Escribir directamente en dist/assets/models/.")
    parser.add_argument("--regen-shape", action="store_true", help="Regenerar malla base aunque exista cache.")
    parser.add_argument("--no-hy3d-base", action="store_true", help="Desactivar base geométrica HunyuanPaint (solo inpaint UV).")
    parser.add_argument("--grid", help="Ruta a una cuadrícula 4x2 (ej. Resultado A/...) para reconstruir desde 8 vistas limpias.")
    parser.add_argument("--tex-size", type=int, default=2048, help="Resolución de textura PBR (default 2048).")
    args = parser.parse_args()

    out_dir = os.path.join(PROJECT_DIR, "dist", "assets", "models") if args.deploy else args.out_dir

    if args.skus:
        skus = args.skus
    elif args.approved_json:
        with open(args.approved_json, "r", encoding="utf-8") as f:
            skus = json.load(f).get("approved_skus", [])
    elif args.all:
        skus = [item["sku"] for item in load_catalog_metadata()]
    else:
        skus = ["IX6180-100"]

    import rembg

    rembg_sess = rembg.new_session("u2net")
    results = []
    for sku in skus:
        results.append(
            build_pbr_glb_for_sku(
                sku,
                out_dir=out_dir,
                tex_size=args.tex_size,
                regen_shape=args.regen_shape,
                rembg_session=rembg_sess,
                grid_path=args.grid if len(skus) == 1 else None,
                use_hy3d_base=not args.no_hy3d_base,
            )
        )

    print("\nResumen 3D PBR:", json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
