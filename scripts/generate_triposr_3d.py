import os
import sys
import json
import struct
import base64
import subprocess
import tempfile
import time
import numpy as np
import torch
import trimesh
from PIL import Image
from skimage import color as skcolor

sys.path.insert(0, os.path.abspath("scratch/TripoSR"))
from tsr.system import TSR
from tsr.utils import to_gradio_3d_orientation, resize_foreground


def segment_with_rembg(img_path):
    """Segment shoe foreground cleanly with rembg in global Python."""
    try:
        import rembg
        im = Image.open(img_path).convert("RGBA")
        return rembg.remove(im)
    except ImportError:
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tf:
            tmp_out = tf.name
        try:
            code = (
                "import rembg; from PIL import Image; "
                f"im = Image.open({img_path!r}).convert('RGBA'); "
                f"rembg.remove(im).save({tmp_out!r})"
            )
            subprocess.run(["python", "-c", code], check=True)
            return Image.open(tmp_out).convert("RGBA").copy()
        finally:
            if os.path.exists(tmp_out):
                os.remove(tmp_out)


def prepare_triposr_input(img_path, fg_ratio=0.84, size=512):
    """Return 512x512 gray-background TripoSR input + raw foreground sRGB pixels [N, 3] for color calibration."""
    rgba_im = segment_with_rembg(img_path)
    fg_im = resize_foreground(rgba_im, fg_ratio)
    arr = np.array(fg_im).astype(np.float32) / 255.0
    fg_mask = arr[:, :, 3] > 0.85
    fg_pixels = arr[fg_mask][:, :3]

    rgb = arr[:, :, :3] * arr[:, :, 3:4] + (1.0 - arr[:, :, 3:4]) * 0.5
    pil_rgb = Image.fromarray((rgb * 255.0).astype(np.uint8))
    if pil_rgb.size != (size, size):
        pil_rgb = pil_rgb.resize((size, size), Image.Resampling.LANCZOS)
    return pil_rgb, fg_pixels


def match_lab_color_stats(pred_srgb, ref_fg_srgb, strength=0.75):
    """Softly match TripoSR vertex color L*a*b* mean/std to the reference photo's foreground palette."""
    pred_lab = skcolor.rgb2lab(np.clip(pred_srgb, 0.0, 1.0)[None, :, :])[0]
    ref_lab = skcolor.rgb2lab(np.clip(ref_fg_srgb, 0.0, 1.0)[None, :, :])[0]

    p_mean, p_std = pred_lab.mean(axis=0), np.maximum(pred_lab.std(axis=0), 1e-4)
    r_mean, r_std = ref_lab.mean(axis=0), np.maximum(ref_lab.std(axis=0), 1e-4)

    # Keep luminance shift gentle while accurately matching chroma (a*, b*) and contrast
    matched_lab = (pred_lab - p_mean) * (r_std / p_std) + r_mean
    blended_lab = pred_lab * (1.0 - strength) + matched_lab * strength
    blended_lab[:, 0] = np.clip(blended_lab[:, 0], 0.0, 100.0)
    blended_lab[:, 1:] = np.clip(blended_lab[:, 1:], -128.0, 127.0)

    out_rgb = skcolor.lab2rgb(blended_lab[None, :, :])[0]
    return np.clip(out_rgb, 0.0, 1.0).astype(np.float32)


def srgb_to_linear(c):
    c = np.clip(c, 0.0, 1.0)
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4).astype(np.float32)


def export_clean_glb(mesh, srgb_colors, out_glb_path, sku):
    pos = np.asarray(mesh.vertices, dtype=np.float32)
    faces = np.asarray(mesh.faces, dtype=np.uint32).reshape(-1)
    nrm = np.asarray(mesh.vertex_normals, dtype=np.float32)

    vc_lin = srgb_to_linear(srgb_colors)
    vc_rgba = np.column_stack([vc_lin, np.ones(len(vc_lin), dtype=np.float32)]).astype(np.float32)

    def pad4(b):
        rem = len(b) % 4
        return b + (b"\x00" * (4 - rem) if rem else b"")

    pos_b, nrm_b, col_b, idx_b = pos.tobytes(), nrm.tobytes(), vc_rgba.tobytes(), faces.tobytes()
    pos_p, nrm_p, col_p, idx_p = pad4(pos_b), pad4(nrm_b), pad4(col_b), pad4(idx_b)
    off_pos, off_nrm = 0, len(pos_p)
    off_col = off_nrm + len(nrm_p)
    off_idx = off_col + len(col_p)
    bin_blob = pos_p + nrm_p + col_p + idx_p

    gltf = {
        "asset": {"version": "2.0", "generator": "Streetwar-TripoSR-Polished"},
        "scene": 0,
        "scenes": [{"nodes": [0]}],
        "nodes": [{"mesh": 0, "name": sku}],
        "meshes": [{"primitives": [{"attributes": {"POSITION": 0, "NORMAL": 1, "COLOR_0": 2}, "indices": 3, "material": 0}]}],
        "materials": [{
            "name": f"{sku}_mat",
            "pbrMetallicRoughness": {"baseColorFactor": [1.0, 1.0, 1.0, 1.0], "metallicFactor": 0.02, "roughnessFactor": 0.80},
        }],
        "buffers": [{"byteLength": len(bin_blob)}],
        "bufferViews": [
            {"buffer": 0, "byteOffset": off_pos, "byteLength": len(pos_b), "target": 34962},
            {"buffer": 0, "byteOffset": off_nrm, "byteLength": len(nrm_b), "target": 34962},
            {"buffer": 0, "byteOffset": off_col, "byteLength": len(col_b), "target": 34962},
            {"buffer": 0, "byteOffset": off_idx, "byteLength": len(idx_b), "target": 34963},
        ],
        "accessors": [
            {"bufferView": 0, "componentType": 5126, "count": len(pos), "type": "VEC3",
             "min": pos.min(axis=0).tolist(), "max": pos.max(axis=0).tolist()},
            {"bufferView": 1, "componentType": 5126, "count": len(pos), "type": "VEC3"},
            {"bufferView": 2, "componentType": 5126, "count": len(pos), "type": "VEC4"},
            {"bufferView": 3, "componentType": 5125, "count": len(faces), "type": "SCALAR"},
        ],
    }

    json_bytes = json.dumps(gltf, separators=(",", ":")).encode("utf-8")
    if len(json_bytes) % 4:
        json_bytes += b" " * (4 - len(json_bytes) % 4)
    total_len = 12 + 8 + len(json_bytes) + 8 + len(bin_blob)
    os.makedirs(os.path.dirname(out_glb_path), exist_ok=True)
    with open(out_glb_path, "wb") as f:
        f.write(struct.pack("<III", 0x46546C67, 2, total_len))
        f.write(struct.pack("<II", len(json_bytes), 0x4E4F534A))
        f.write(json_bytes)
        f.write(struct.pack("<II", len(bin_blob), 0x004E4942))
        f.write(bin_blob)
    return total_len


def main():
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print(f"Running Smooth TripoSR on {device}", flush=True)
    model = TSR.from_pretrained("stabilityai/TripoSR", config_name="config.yaml", weight_name="model.ckpt")
    model.renderer.set_chunk_size(8192)
    model.to(device)

    targets = [
        ("IX6180-100", "dist/assets/productos/IX6180-100/03-3-4-front.webp", "dist/assets/models/IX6180-100.glb"),
        ("IW2872-700", "dist/assets/productos/IW2872-700/03-3-4-front.webp", "dist/assets/models/IW2872-700.glb"),
    ]

    for sku, img_path, out_glb in targets:
        t0 = time.time()
        inp, ref_fg = prepare_triposr_input(img_path)
        with torch.no_grad():
            scene_codes = model([inp], device=device)
            meshes = model.extract_mesh(scene_codes, has_vertex_color=False, resolution=288, threshold=25.0)

        mesh = meshes[0]
        parts = mesh.split(only_watertight=False)
        if len(parts) > 1:
            mesh = max(parts, key=lambda m: len(m.faces))

        # Taubin smooth BEFORE querying TripoSR colors so vertex normals & colors are silky-smooth
        trimesh.smoothing.filter_taubin(mesh, lamb=0.5, nu=-0.53, iterations=14)

        v_query = torch.from_numpy(np.asarray(mesh.vertices, dtype=np.float32)).to(device)
        with torch.no_grad():
            pred_srgb = model.renderer.query_triplane(model.decoder, v_query, scene_codes[0])["color"].cpu().numpy()

        calibrated_srgb = match_lab_color_stats(pred_srgb, ref_fg, strength=0.75)

        mesh = to_gradio_3d_orientation(mesh)
        bounds = mesh.bounds
        mesh.apply_translation(-(bounds[0] + bounds[1]) / 2.0)
        extent = float((bounds[1] - bounds[0]).max())
        if extent > 0:
            mesh.apply_scale(0.32 / extent)
        mesh.fix_normals()

        glb_size = export_clean_glb(mesh, calibrated_srgb, out_glb, sku)
        with open(out_glb, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        with open(out_glb + ".js", "w", encoding="utf-8") as f:
            f.write(f'window.__GLB_B64=window.__GLB_B64||{{}};window.__GLB_B64["{sku}"]="{b64}";\n')

        print(f"Generated {sku}: {len(mesh.faces)} tris, {len(mesh.vertices)} verts, {glb_size/1024:.1f} KB in {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
