#!/usr/bin/env python3
"""
scripts/color_lock.py
=============================================================================
Fase 1: Anclaje de Fotos Reales HD + Candado Cromático CIELAB + Métricas QA
=============================================================================
Provee utilidades reutilizables para:
  1. Cargar los 45 productos desde dist/js/flow_nanobanana_data.js (sin depender de openpyxl).
  2. Detectar las fotos reales 2K en _source_data/fotos-HD/{Grupo}/{Carpeta}/.
  3. Extraer siluetas limpias RGBA con rembg sin dañar suelas blancas.
  4. Aplicar acabado de estudio local sutil (claridad + balance tonal) manteniendo fidelidad.
  5. Transferir y bloquear el espacio de color CIELAB desde la foto real hacia imágenes
     generadas/editadas por IA (evita cambios de colorway, saturación o tintes).
  6. Medir fidelidad cromática (Delta E) y geométrica (IoU de silueta normalizada).
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)
for p in (CURRENT_DIR, PROJECT_DIR):
    if p not in sys.path:
        sys.path.insert(0, p)

from reference_metrics import align_and_canvas


def detect_source_hd_photos(folder_path: str) -> Dict[str, str]:
    """
    Detecta fotos reales por ángulo canónico en _source_data/fotos-HD (o fotos/),
    descartando variantes zoom/detail/copia. Compatible con nombres 01-..08- y IMG_XXXX.
    """
    if not os.path.exists(folder_path):
        return {}
    files = sorted(f for f in os.listdir(folder_path) if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")))
    if not files:
        return {}

    detected: Dict[str, str] = {}
    has_named = any(f.lower().startswith(("01-", "02-", "03-", "04-", "05-", "06-", "07-", "08-")) for f in files)
    if has_named:
        patterns = {
            "01_lateral": ["01-lateral"],
            "02_medial": ["02-medial"],
            "03_3-4_front": ["03-3-4-front", "03-frontal-3-4", "02-frontal-3-4"],
            "04_3-4_rear": ["04-3-4-rear", "03-trasera-3-4"],
            "05_front": ["05-front"],
            "06_rear": ["06-rear", "03-trasera"],
            "07_top_down": ["07-top-down", "04-superior"],
            "08_outsole": ["08-outsole", "suela"],
        }
        for slug, prefixes in patterns.items():
            cands = [f for f in files if any(p in f.lower() for p in prefixes)]
            if cands:
                clean = [c for c in cands if not any(bad in c.lower() for bad in ("zoom", "detail", "copia"))]
                detected[slug] = os.path.join(folder_path, clean[0] if clean else cands[0])
    elif any(f.upper().startswith("IMG_") for f in files):
        misplaced = ("IMG_0264", "IMG_0269", "IMG_0275", "IMG_0280")
        img_files = [f for f in files if f.upper().startswith("IMG_") and not f.upper().startswith(misplaced)]
        img_map = {
            "01_lateral": 0,
            "06_rear": 1 if len(img_files) > 1 else None,
            "02_medial": 2 if len(img_files) > 2 else None,
            "05_front": 3 if len(img_files) > 3 else None,
            "07_top_down": (len(img_files) - 1) if len(img_files) >= 5 else None,
        }
        for slug, idx in img_map.items():
            if idx is not None and idx < len(img_files):
                detected[slug] = os.path.join(folder_path, img_files[idx])
    return detected


CANONICAL_STUDIO_SLUGS = [
    ("01_lateral", "01-lateral.webp"),
    ("02_medial", "02-medial.webp"),
    ("03_3-4_front", "03-3-4-front.webp"),
    ("04_3-4_rear", "04-3-4-rear.webp"),
    ("05_front", "05-front.webp"),
    ("06_rear", "06-rear.webp"),
    ("07_top_down", "07-top-down.webp"),
    ("08_outsole", "08-outsole.webp"),
]


def load_catalog_metadata(
    data_js_path: str = os.path.join(PROJECT_DIR, "dist", "js", "flow_nanobanana_data.js")
) -> List[Dict]:
    """Lee el catálogo maestro de 45 modelos desde flow_nanobanana_data.js."""
    with open(data_js_path, "r", encoding="utf-8") as f:
        raw = f.read()
    m = re.search(r"const flowNanobananaData = (\{.*?\});\s*$", raw, re.DOTALL)
    if not m:
        raise RuntimeError(f"No se pudo parsear flowNanobananaData en {data_js_path}")
    data = json.loads(m.group(1))
    return data["catalog"]


def get_hd_source_map(product_item: Dict) -> Dict[str, str]:
    """Retorna mapa {angle_slug: abs_path} con las fotos reales HD disponibles."""
    hd_dir = os.path.join(
        PROJECT_DIR, "_source_data", "fotos-HD", product_item["group"], product_item["product_dir"]
    )
    detected = detect_source_hd_photos(hd_dir)
    # Fallback a _source_data/fotos si no existiera en fotos-HD
    if not detected:
        raw_dir = os.path.join(
            PROJECT_DIR, "_source_data", "fotos", product_item["group"], product_item["product_dir"]
        )
        detected = detect_source_hd_photos(raw_dir)
    return detected


def extract_clean_rgba(
    img_or_path,
    rembg_session=None,
    use_rembg: bool = True,
    alpha_threshold: int = 20,
) -> Image.Image:
    """
    Extrae un recorte RGBA limpio de la zapatilla sin halo gris ni recorte de suela blanca.
    Si use_rembg=False y el fondo es blanco puro, usa detección conectada a bordes.
    """
    if isinstance(img_or_path, (str, Path)):
        im = Image.open(img_or_path)
    else:
        im = img_or_path.copy()

    arr = np.array(im.convert("RGBA"))
    if arr.shape[2] == 4 and np.any(arr[:, :, 3] < 245):
        rgba = Image.fromarray(arr, mode="RGBA")
    elif use_rembg:
        import rembg

        sess = rembg_session or rembg.new_session("u2net")
        rgba = rembg.remove(im.convert("RGB"), session=sess).convert("RGBA")
    else:
        rgb = np.array(im.convert("RGB"))
        h, w, _ = rgb.shape
        near_white = ((rgb[:, :, 0] >= 246) & (rgb[:, :, 1] >= 246) & (rgb[:, :, 2] >= 246)).astype(np.uint8)
        num_labels, labels = cv2.connectedComponents(near_white)
        border_labels = set(labels[0, :].tolist() + labels[h - 1, :].tolist() + labels[:, 0].tolist() + labels[:, w - 1].tolist())
        bg_mask = np.isin(labels, list(border_labels - {0}))
        alpha = np.where(bg_mask, 0, 255).astype(np.uint8)
        rgba = Image.fromarray(np.dstack([rgb, alpha]), mode="RGBA")

    # Suavizado ligero de borde alfa para evitar dientes o halo oscuro
    out_arr = np.array(rgba)
    alpha = out_arr[:, :, 3]
    alpha = np.where(alpha < alpha_threshold, 0, alpha).astype(np.uint8)
    # Descontaminar borde semitransparente cercano a blanco/gris
    edge = (alpha > 0) & (alpha < 220)
    if np.any(edge):
        alpha[edge] = np.clip((alpha[edge].astype(np.float32) - alpha_threshold) * 1.15, 0, 255).astype(np.uint8)
    out_arr[:, :, 3] = alpha
    return Image.fromarray(out_arr, mode="RGBA")


def extract_studio_whitebg_rgba(
    img_or_path,
    rembg_session=None,
    bg_white_thresh: int = 243,
    angle_slug: str = "",
) -> Image.Image:
    """
    Extracción precisa para imágenes de estudio sobre blanco puro (#FFFFFF):
    Usa flood-fill desde los bordes para NO recortar nunca cuero blanco ni crear halos
    en pasadores negros, y usa rembg únicamente como guía en la franja inferior del piso
    (y componentes sueltos) para eliminar la sombra de contacto.
    """
    im = Image.open(img_or_path) if isinstance(img_or_path, (str, Path)) else img_or_path
    rgb = np.array(im.convert("RGB"))
    h, w, _ = rgb.shape

    near_white = (
        (rgb[:, :, 0] >= bg_white_thresh)
        & (rgb[:, :, 1] >= bg_white_thresh)
        & (rgb[:, :, 2] >= bg_white_thresh)
    ).astype(np.uint8)
    _, labels = cv2.connectedComponents(near_white)
    border_labels = set(
        labels[0, :].tolist()
        + labels[h - 1, :].tolist()
        + labels[:, 0].tolist()
        + labels[:, w - 1].tolist()
    )
    flood_fg = ~np.isin(labels, list(border_labels - {0}))

    # Quedarse con el componente principal más grande del zapato
    n_fg, fg_labels, stats, _ = cv2.connectedComponentsWithStats(flood_fg.astype(np.uint8))
    if n_fg > 1:
        areas = stats[1:, cv2.CC_STAT_AREA]
        main_lbl = 1 + int(np.argmax(areas))
        flood_fg = fg_labels == main_lbl

    # Usar rembg solo para limpiar sombra de piso abajo o halo externo en cenital/suela
    if rembg_session is not None:
        import rembg

        rembg_alpha = np.array(rembg.remove(im.convert("RGB"), session=rembg_session))[:, :, 3]
        rembg_mask = rembg_alpha > 110
        ys = np.where(flood_fg)[0]
        if len(ys):
            y0, y1 = int(ys.min()), int(ys.max())
            if angle_slug in ("07_top_down", "08_outsole"):
                # En vista cenital/suela, rembg dilatado 10px conserva todo el zapato y corta sombra externa
                k_dil = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21, 21))
                rembg_loose = cv2.dilate(rembg_mask.astype(np.uint8), k_dil) > 0
                flood_fg = flood_fg & rembg_loose
            else:
                # En vistas laterales/front/rear: en 85% superior mandar flood_fg (0 mordidas en blanco),
                # en 15% inferior cercano al suelo limpiar sombra gris con rembg + oscuridad real
                floor_y = y0 + int((y1 - y0) * 0.85)
                bottom_zone = np.zeros_like(flood_fg)
                bottom_zone[floor_y:, :] = True
                k_bot = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
                rembg_bot = cv2.dilate(rembg_mask.astype(np.uint8), k_bot) > 0
                flood_fg = np.where(bottom_zone, flood_fg & rembg_bot, flood_fg)

    alpha = np.where(flood_fg, 255, 0).astype(np.uint8)
    return Image.fromarray(np.dstack([rgb, alpha]), mode="RGBA")


def crop_rgba_tight(rgba: Image.Image, pad: int = 8) -> Image.Image:
    """Recorta al bounding box de la silueta con un margen seguro."""
    arr = np.array(rgba.convert("RGBA"))
    ys, xs = np.where(arr[:, :, 3] > 20)
    if len(xs) == 0:
        return rgba
    x0 = max(0, int(xs.min()) - pad)
    y0 = max(0, int(ys.min()) - pad)
    x1 = min(rgba.width, int(xs.max()) + 1 + pad)
    y1 = min(rgba.height, int(ys.max()) + 1 + pad)
    return rgba.crop((x0, y0, x1, y1))


def rgba_on_white(rgba: Image.Image, size: Optional[int] = None) -> Image.Image:
    """Compone una imagen RGBA sobre blanco puro #FFFFFF (opcionalmente centrada en cuadro)."""
    im = rgba.convert("RGBA")
    if size is not None:
        im.thumbnail((size, size), Image.Resampling.LANCZOS)
        canvas = Image.new("RGBA", (size, size), (255, 255, 255, 255))
        canvas.alpha_composite(im, ((size - im.width) // 2, (size - im.height) // 2))
        return canvas.convert("RGB")
    bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
    bg.alpha_composite(im)
    return bg.convert("RGB")


def enhance_studio_lighting_local(rgba: Image.Image) -> Image.Image:
    """
    Aplica limpieza tonal y micro-nitidez de estudio solo dentro de la silueta
    preservando intactos el matiz (hue) y el balance de blancos del par real.
    """
    arr = np.array(rgba.convert("RGBA"))
    rgb = arr[:, :, :3]
    alpha = arr[:, :, 3]
    fg = alpha > 40
    if not np.any(fg):
        return rgba

    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB).astype(np.float32)
    L = lab[:, :, 0]
    clahe = cv2.createCLAHE(clipLimit=1.25, tileGridSize=(8, 8))
    L_clahe = clahe.apply(L.astype(np.uint8)).astype(np.float32)

    # Mezcla conservadora (35% CLAHE) para ganar detalle en cuero/malla sin lavar negros ni quemar blancos
    lab[:, :, 0] = np.where(fg, 0.68 * L + 0.32 * L_clahe, L)
    enhanced_rgb = cv2.cvtColor(np.clip(lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2RGB)

    # Micro-nitidez controlada solo en píxeles del producto
    pil_rgb = Image.fromarray(enhanced_rgb)
    sharp_rgb = np.array(pil_rgb.filter(ImageFilter.UnsharpMask(radius=1.1, percent=65, threshold=4)))
    out_rgb = np.where(fg[:, :, None], sharp_rgb, rgb)
    return Image.fromarray(np.dstack([out_rgb, alpha]), mode="RGBA")


def _fg_pixels_lab(rgba: Image.Image, alpha_min: int = 150) -> Tuple[np.ndarray, np.ndarray]:
    arr = np.array(rgba.convert("RGBA"))
    mask = arr[:, :, 3] >= alpha_min
    lab = cv2.cvtColor(arr[:, :, :3], cv2.COLOR_RGB2LAB).astype(np.float32)
    return lab, mask


def lock_colors_lab(
    target_rgba: Image.Image,
    ref_rgba: Image.Image,
    strength_l: float = 0.55,
    strength_ab: float = 0.90,
) -> Image.Image:
    """
    Candado cromático CIELAB: alinea la distribución de color de `target_rgba`
    (imagen editada/generada por IA) con la paleta real de `ref_rgba`.
    Usa igualación por cuantiles en a* y b* y alineación suave en L*, protegiendo
    zonas neutras (blanco/negro puro) contra tintes artificiales.
    """
    tgt_arr = np.array(target_rgba.convert("RGBA"))
    tgt_lab, tgt_mask = _fg_pixels_lab(target_rgba, alpha_min=60)
    ref_lab, ref_mask = _fg_pixels_lab(ref_rgba, alpha_min=150)

    if tgt_mask.sum() < 100 or ref_mask.sum() < 100:
        return target_rgba

    out_lab = tgt_lab.copy()
    quantiles = np.linspace(0, 100, 101)

    for ch, strength in ((0, strength_l), (1, strength_ab), (2, strength_ab)):
        src_vals = tgt_lab[:, :, ch][tgt_mask]
        ref_vals = ref_lab[:, :, ch][ref_mask]
        src_q = np.percentile(src_vals, quantiles)
        ref_q = np.percentile(ref_vals, quantiles)
        mapped = np.interp(src_vals, src_q, ref_q)

        # Proteger blancos/negros neutros de tintes en canales a* y b*
        if ch in (1, 2):
            a_c = tgt_lab[:, :, 1][tgt_mask] - 128.0
            b_c = tgt_lab[:, :, 2][tgt_mask] - 128.0
            chroma = np.sqrt(a_c * a_c + b_c * b_c)
            # Si ambos son casi neutros, reducir transferencia cromática agresiva
            neutral_weight = np.clip((chroma - 2.0) / 10.0, 0.35, 1.0)
            blended = src_vals + (mapped - src_vals) * (strength * neutral_weight)
        else:
            blended = src_vals + (mapped - src_vals) * strength

        ch_plane = out_lab[:, :, ch]
        ch_plane[tgt_mask] = np.clip(blended, 0, 255)
        out_lab[:, :, ch] = ch_plane

    locked_rgb = cv2.cvtColor(np.clip(out_lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2RGB)
    locked_rgb = np.where(tgt_arr[:, :, 3:4] > 10, locked_rgb, 255)
    return Image.fromarray(np.dstack([locked_rgb, tgt_arr[:, :, 3]]), mode="RGBA")


def _normalized_mask(rgba: Image.Image, box_size: int = 256) -> np.ndarray:
    tight = crop_rgba_tight(rgba, pad=0)
    mask = (np.array(tight.resize((box_size, box_size), Image.Resampling.BILINEAR))[:, :, 3] > 100)
    return mask


def evaluate_fidelity(
    gen_rgba: Image.Image,
    ref_rgba: Image.Image,
    same_angle: bool = True,
) -> Dict:
    """
    Calcula métricas de control de calidad entre la imagen generada y la referencia real:
      - delta_e_palette: distancia cromática CIELAB entre percentiles de color (p10..p90).
      - silhouette_iou: IoU de silueta normalizada (cuando es el mismo ángulo).
    """
    gen_lab, gen_mask = _fg_pixels_lab(gen_rgba, alpha_min=128)
    ref_lab, ref_mask = _fg_pixels_lab(ref_rgba, alpha_min=128)

    if gen_mask.sum() < 50 or ref_mask.sum() < 50:
        return {"delta_e_palette": 99.0, "silhouette_iou": 0.0, "passed": False}

    qs = np.linspace(10, 90, 17)
    diffs_sq = np.zeros_like(qs)
    for ch, scale in ((0, 100.0 / 255.0), (1, 1.0), (2, 1.0)):
        gq = np.percentile(gen_lab[:, :, ch][gen_mask], qs) * scale
        rq = np.percentile(ref_lab[:, :, ch][ref_mask], qs) * scale
        diffs_sq += (gq - rq) ** 2
    delta_e = float(np.mean(np.sqrt(diffs_sq)))

    iou = None
    if same_angle:
        m1 = _normalized_mask(gen_rgba)
        m2 = _normalized_mask(ref_rgba)
        inter = float(np.logical_and(m1, m2).sum())
        union = float(np.logical_or(m1, m2).sum())
        iou = inter / union if union > 0 else 0.0

    passed = delta_e <= 6.5 and (iou is None or iou >= 0.80)
    return {
        "delta_e_palette": round(delta_e, 2),
        "silhouette_iou": round(iou, 3) if iou is not None else None,
        "passed": passed,
    }


def standardize_studio_angle(rgba: Image.Image, angle_slug: str, size: int = 1024) -> Image.Image:
    """Alinea la toma al estándar milimétrico de output_catalog/REFERENCIA/."""
    return align_and_canvas(rgba, angle_slug=angle_slug, target_size=size)


if __name__ == "__main__":
    catalog = load_catalog_metadata()
    print(f"Catálogo cargado: {len(catalog)} productos.")
    sample = catalog[0]
    hd_map = get_hd_source_map(sample)
    print(f"Ejemplo {sample['sku']} ({sample['name']}): {sorted(hd_map.keys())}")
