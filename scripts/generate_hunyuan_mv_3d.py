import os
import re
import sys
import gc
import json
import time
import base64
import argparse
import numpy as np
import torch
import trimesh
from PIL import Image
import huggingface_hub.file_download as hf_fd

hf_fd.are_symlinks_supported = lambda *args, **kwargs: False

sys.path.insert(0, os.path.abspath("scratch/Hunyuan3D-2"))

from hy3dgen.rembg import BackgroundRemover
from hy3dgen.shapegen import (
    Hunyuan3DDiTFlowMatchingPipeline,
    FloaterRemover,
    DegenerateFaceRemover,
    FaceReducer,
)
from hy3dgen.texgen import Hunyuan3DPaintPipeline


def load_rgba_cached(sku, view_name, path, cache_dir, get_rembg):
    os.makedirs(cache_dir, exist_ok=True)
    cpath = os.path.join(cache_dir, f"{sku}_{view_name}.png")
    if os.path.exists(cpath):
        print(f"[prep] Using cached RGBA {sku}/{view_name}", flush=True)
        return Image.open(cpath).convert("RGBA")
    print(f"[prep] Removing background {sku}/{view_name}...", flush=True)
    im = Image.open(path)
    if im.mode != "RGBA" or np.array(im)[:, :, 3].min() == 255:
        im = get_rembg()(im.convert("RGB"))
    im.save(cpath)
    return im


def load_all_targets_from_galleries():
    with open("dist/js/galleries.js", "r", encoding="utf-8") as f:
        raw = f.read()
    obj = json.loads(re.search(r"const galleries\s*=\s*(\{[\s\S]*?\});", raw).group(1))
    targets = []
    seen = set()
    for idx in sorted(obj.keys(), key=lambda x: int(x)):
        first = obj[idx][0]  # e.g. "productos/IX6180-100/01-lateral.webp"
        sku = first.split("/")[1]
        if sku in seen:
            continue
        seen.add(sku)
        targets.append((sku, f"dist/assets/productos/{sku}", f"dist/assets/models/{sku}.glb"))
    return targets


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Generate GLBs for all 45 SKUs in galleries.js")
    args = parser.parse_args()

    os.makedirs("scratch/hy3d_tmp", exist_ok=True)
    rembg_holder = [None]

    def get_rembg():
        if rembg_holder[0] is None:
            print("[prep] Initializing rembg session...", flush=True)
            rembg_holder[0] = BackgroundRemover()
        return rembg_holder[0]

    if args.all:
        all_targets = load_all_targets_from_galleries()
    else:
        all_targets = [
            ("IX6180-100", "dist/assets/productos/IX6180-100", "dist/assets/models/IX6180-100.glb"),
            ("IW2872-700", "dist/assets/productos/IW2872-700", "dist/assets/models/IW2872-700.glb"),
        ]

    targets = [
        t for t in all_targets
        if not (os.path.exists(t[2]) and os.path.exists(t[2] + ".js"))
    ]
    print(f"Total targets: {len(all_targets)} | Already done: {len(all_targets) - len(targets)} | Pending: {len(targets)}", flush=True)
    if not targets:
        print("All targets already generated!", flush=True)
        return

    # Map studio views consistently around the shoe so lateral (rich side view) is azim=0 ("front"):
    # Looking from azim=0: shoe toe points LEFT ->
    #   90° clockwise (left view) sees TOE (05-front)
    #   180° (back view) sees MEDIAL (02-medial)
    #   270° (right view) sees HEEL (06-rear)
    view_files = {
        "front": "01-lateral.webp",
        "left": "05-front.webp",
        "back": "02-medial.webp",
        "right": "06-rear.webp",
    }
    rgba_cache_dir = "scratch/hy3d_tmp/rgba"
    for sku, pdir, _ in targets:
        for vname, fname in view_files.items():
            im = load_rgba_cached(sku, vname, os.path.join(pdir, fname), rgba_cache_dir, get_rembg)
            im.close()
    rembg_holder[0] = None
    gc.collect()

    def get_mv_images(sku):
        return {
            vname: Image.open(os.path.join(rgba_cache_dir, f"{sku}_{vname}.png")).convert("RGBA")
            for vname in view_files
        }

    # ── STAGE 1: Multi-View Shape Generation (Hunyuan3D-2mv) ──
    white_paths = {sku: f"scratch/hy3d_tmp/{sku}_white.glb" for sku, _, _ in targets}
    missing_white = [sku for sku, _, _ in targets if not os.path.exists(white_paths[sku])]
    if missing_white:
        print("Loading Hunyuan3D-2mv shape pipeline...", flush=True)
        t_s = time.time()
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
        print(f"Shape pipeline ready in {time.time() - t_s:.1f}s", flush=True)

        floater_rm = FloaterRemover()
        degen_rm = DegenerateFaceRemover()
        face_red = FaceReducer()

        for sku in missing_white:
            t0 = time.time()
            print(f"[{sku}] Generating multi-view 3D shape...", flush=True)
            mesh = shape_pipe(
                image=get_mv_images(sku),
                num_inference_steps=35,
                octree_resolution=300,
                num_chunks=12000,
                generator=torch.manual_seed(42),
                output_type="trimesh",
            )[0]
            shape_pipe.maybe_free_model_hooks()
            shape_pipe.device = torch.device("cuda")
            mesh = floater_rm(mesh)
            mesh = degen_rm(mesh)
            mesh = face_red(mesh, max_facenum=40000)

            wpath = white_paths[sku]
            mesh.export(wpath)
            print(f"[{sku}] Shape saved ({len(mesh.faces)} tris) in {time.time() - t0:.1f}s -> {wpath}", flush=True)

        del shape_pipe
        gc.collect()
        torch.cuda.empty_cache()
    else:
        print("Reusing cached white meshes from scratch/hy3d_tmp/", flush=True)

    # ── STAGE 2: Texture Painting (Hunyuan3DPaintPipeline) ──
    print("Loading Hunyuan3DPaintPipeline (turbo)...", flush=True)
    t_p = time.time()
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
    except Exception as exc:
        print("Note enabling slicing:", exc, flush=True)
    print(f"Paint pipeline ready in {time.time() - t_p:.1f}s", flush=True)

    for idx, (sku, _, out_glb) in enumerate(targets, 1):
        t0 = time.time()
        print(f"[{idx}/{len(targets)} {sku}] Painting 2K UV texture...", flush=True)
        mesh = trimesh.load(white_paths[sku])
        if isinstance(mesh, trimesh.Scene):
            mesh = mesh.to_geometry()

        front_img = Image.open(os.path.join(rgba_cache_dir, f"{sku}_front.png")).convert("RGBA")
        textured_mesh = paint_pipe(mesh, image=front_img)
        front_img.close()

        raw_tpath = f"scratch/hy3d_tmp/{sku}_textured_raw.glb"
        textured_mesh.export(raw_tpath)
        print(f"[{sku}] Saved raw textured mesh -> {raw_tpath}", flush=True)

        # Center & normalize scale to ~0.32m for consistent <model-viewer> framing
        bounds = textured_mesh.bounds
        textured_mesh.apply_translation(-(bounds[0] + bounds[1]) / 2.0)
        extent = float((bounds[1] - bounds[0]).max())
        if extent > 0:
            textured_mesh.apply_scale(0.32 / extent)

        os.makedirs(os.path.dirname(out_glb), exist_ok=True)
        glb_bytes = textured_mesh.export(file_type="glb")
        with open(out_glb, "wb") as f:
            f.write(glb_bytes)

        b64 = base64.b64encode(glb_bytes).decode("ascii")
        with open(out_glb + ".js", "w", encoding="utf-8") as f:
            f.write(f'window.__GLB_B64=window.__GLB_B64||{{}};window.__GLB_B64["{sku}"]="{b64}";\n')

        print(f"[{sku}] Textured GLB saved ({len(glb_bytes)/1024:.1f} KB) in {time.time() - t0:.1f}s -> {out_glb}", flush=True)
        gc.collect()
        torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
