import os
import json
import struct
import io
import base64
import numpy as np
from PIL import Image
from scipy import ndimage
from skimage import measure


def extract_clean_crop(img_path):
    """Load studio image on white background, remove floor shadow, return tight RGB + dilated RGB + mask."""
    im = Image.open(img_path).convert('RGB')
    arr = np.array(im)

    max_c = arr.max(axis=2)
    min_c = arr.min(axis=2)
    chroma = max_c.astype(np.int16) - min_c.astype(np.int16)
    fg = (min_c < 228) | (chroma > 14)

    labeled, num = ndimage.label(fg)
    if num > 0:
        sizes = np.bincount(labeled.ravel())
        sizes[0] = 0
        fg = labeled == sizes.argmax()

    fg = ndimage.binary_fill_holes(fg)

    ys, xs = np.where(fg)
    if len(ys) == 0:
        raise ValueError(f"Empty foreground in {img_path}")
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())

    # Trim pale gray floor shadow rows at the bottom
    while y1 > y0 + 20:
        row_mask = fg[y1, x0:x1 + 1]
        if not np.any(row_mask):
            y1 -= 1
            continue
        row_rgb = arr[y1, x0:x1 + 1][row_mask]
        row_luma = row_rgb.mean()
        row_chroma = (row_rgb.max(axis=1) - row_rgb.min(axis=1)).mean()
        if row_luma > 212 and row_chroma < 10:
            fg[y1, :] = False
            y1 -= 1
        else:
            break

    ys, xs = np.where(fg)
    ty0, ty1 = int(ys.min()), int(ys.max())
    tx0, tx1 = int(xs.min()), int(xs.max())

    rgb = np.ascontiguousarray(arr[ty0:ty1 + 1, tx0:tx1 + 1])
    mask = np.ascontiguousarray(fg[ty0:ty1 + 1, tx0:tx1 + 1])

    # Dilate foreground colors outward into background so UV sampling never hits white halo
    _, indices = ndimage.distance_transform_edt(~mask, return_indices=True)
    rgb_dilated = rgb[indices[0], indices[1]]

    return {'rgb': rgb_dilated, 'mask': mask}


def detect_toe_left(mask):
    """For side profiles: toe is shorter vertically than ankle/heel."""
    h, w = mask.shape
    sw = max(4, int(w * 0.16))
    ly = np.where(np.any(mask[:, :sw], axis=1))[0]
    ry = np.where(np.any(mask[:, w - sw:], axis=1))[0]
    lh = (ly.max() - ly.min()) if len(ly) else h
    rh = (ry.max() - ry.min()) if len(ry) else h
    return lh <= rh


def rotate_view(view, k):
    return {
        'rgb': np.ascontiguousarray(np.rot90(view['rgb'], k)),
        'mask': np.ascontiguousarray(np.rot90(view['mask'], k)),
    }


def flip_lr_view(view):
    return {
        'rgb': np.ascontiguousarray(np.fliplr(view['rgb'])),
        'mask': np.ascontiguousarray(np.fliplr(view['mask'])),
    }


def sample_mask_grid(mask, u_grid, v_grid):
    h, w = mask.shape
    ix = np.clip(np.round(u_grid * (w - 1)).astype(np.int32), 0, w - 1)
    iy = np.clip(np.round(v_grid * (h - 1)).astype(np.int32), 0, h - 1)
    return mask[iy, ix]


def build_glb_from_6views(sku, prod_dir, out_glb_path, nx=96, ny=66, nz=44):
    """Reconstruct a textured 3D sneaker .glb from 6 orthographic product views."""
    views_raw = {
        'lateral': extract_clean_crop(os.path.join(prod_dir, '01-lateral.webp')),
        'medial': extract_clean_crop(os.path.join(prod_dir, '02-medial.webp')),
        'front': extract_clean_crop(os.path.join(prod_dir, '05-front.webp')),
        'rear': extract_clean_crop(os.path.join(prod_dir, '06-rear.webp')),
        'top': extract_clean_crop(os.path.join(prod_dir, '07-top-down.webp')),
        'bottom': extract_clean_crop(os.path.join(prod_dir, '08-outsole.webp')),
    }

    if not detect_toe_left(views_raw['lateral']['mask']):
        views_raw['lateral'] = flip_lr_view(views_raw['lateral'])
    if detect_toe_left(views_raw['medial']['mask']):
        views_raw['medial'] = flip_lr_view(views_raw['medial'])

    # Proportions normalized to length = 1.0
    lat_h, lat_w = views_raw['lateral']['mask'].shape
    fr_h, fr_w = views_raw['front']['mask'].shape
    lx = 1.0
    ly = float(lat_h) / float(lat_w)
    lz = min(0.46, max(0.32, float(fr_w) / float(fr_h) * ly))

    xs = np.linspace(-0.04, 1.04, nx)  # 0=toe, 1=heel
    ys = np.linspace(-0.04, 1.04, ny)  # 0=bottom, 1=top
    zs = np.linspace(-0.04, 1.04, nz)  # 0=medial, 1=lateral
    X, Y, Z = np.meshgrid(xs, ys, zs, indexing='ij')
    in_bounds = (X >= 0) & (X <= 1) & (Y >= 0) & (Y <= 1) & (Z >= 0) & (Z <= 1)

    m_lat = sample_mask_grid(views_raw['lateral']['mask'], X, 1.0 - Y)
    m_med = sample_mask_grid(views_raw['medial']['mask'], 1.0 - X, 1.0 - Y)
    m_fr = sample_mask_grid(views_raw['front']['mask'], Z, 1.0 - Y)
    m_rr = sample_mask_grid(views_raw['rear']['mask'], 1.0 - Z, 1.0 - Y)
    side_hull = in_bounds & m_lat & m_med & m_fr & m_rr

    # Pick horizontal orientation for top & bottom using forefoot > heel width,
    # and pick Z-mirror that maximizes 3D hull intersection (left vs right shoe).
    def orient_plan_view(raw_view, want_toe_right, u_expr, name):
        base = rotate_view(raw_view, 1) if raw_view['mask'].shape[0] > raw_view['mask'].shape[1] else raw_view
        m = base['mask']
        h, w = m.shape
        left_w = m[:, int(w * 0.12):int(w * 0.32)].sum(axis=0).mean()
        right_w = m[:, int(w * 0.68):int(w * 0.88)].sum(axis=0).mean()
        toe_is_right = right_w >= left_w
        if toe_is_right != want_toe_right:
            base = rotate_view(base, 2)

        best = None
        for flip_v in (False, True):
            v_grid = Z if flip_v else (1.0 - Z)
            m_plan = sample_mask_grid(base['mask'], u_expr, v_grid)
            score = int((side_hull & m_plan).sum())
            if best is None or score > best[0]:
                best = (score, flip_v, base, m_plan)
        print(f"  [{sku}] {name}: want_toe_right={want_toe_right}, score={best[0]}, flip_z={best[1]}")
        return best[2], best[3], best[1]

    top_view, m_top, top_flip_z = orient_plan_view(views_raw['top'], True, 1.0 - X, 'top')
    bot_view, m_bot, bot_flip_z = orient_plan_view(views_raw['bottom'], False, X, 'bottom')

    occ = (side_hull & m_top & m_bot).astype(np.float32)
    occ_smooth = ndimage.gaussian_filter(occ, sigma=0.9)
    verts, faces, normals, _ = measure.marching_cubes(occ_smooth, level=0.45)
    # marching_cubes returns inward-wound faces for solid-positive volumes; flip winding to outward CCW
    faces = faces[:, [0, 2, 1]]

    vx = np.interp(verts[:, 0], np.arange(nx), xs)
    vy = np.interp(verts[:, 1], np.arange(ny), ys)
    vz = np.interp(verts[:, 2], np.arange(nz), zs)

    scale = 0.30
    pos = np.column_stack([
        (vx - 0.5) * lx * scale,
        (vy - 0.5) * ly * scale,
        (vz - 0.5) * lz * scale,
    ]).astype(np.float32)

    nrm = np.column_stack([
        normals[:, 0] / (lx * nx),
        normals[:, 1] / (ly * ny),
        normals[:, 2] / (lz * nz),
    ]).astype(np.float32)
    nrm = nrm / np.maximum(np.linalg.norm(nrm, axis=1, keepdims=True), 1e-8)

    tile = 512
    atlas = Image.new('RGB', (tile * 3, tile * 2), (255, 255, 255))
    cam_defs = [
        ('lateral', views_raw['lateral']['rgb'], (0.0, 0.0, 1.0), (0, 0)),
        ('medial', views_raw['medial']['rgb'], (0.0, 0.0, -1.0), (1, 0)),
        ('front', views_raw['front']['rgb'], (-1.0, 0.0, 0.0), (2, 0)),
        ('rear', views_raw['rear']['rgb'], (1.0, 0.0, 0.0), (0, 1)),
        ('top', top_view['rgb'], (0.0, 1.0, 0.0), (1, 1)),
        ('bottom', bot_view['rgb'], (0.0, -1.0, 0.0), (2, 1)),
    ]

    for _, rgb_arr, _, (tx, ty) in cam_defs:
        pil_tile = Image.fromarray(rgb_arr).resize((tile, tile), Image.Resampling.LANCZOS)
        atlas.paste(pil_tile, (tx * tile, ty * tile))

    tri_pos = pos[faces]
    tri_nrm = nrm[faces]
    tri_vx = vx[faces]
    tri_vy = vy[faces]
    tri_vz = vz[faces]

    e1 = tri_pos[:, 1] - tri_pos[:, 0]
    e2 = tri_pos[:, 2] - tri_pos[:, 0]
    fnrm = np.cross(e1, e2)
    fnrm = fnrm / np.maximum(np.linalg.norm(fnrm, axis=1, keepdims=True), 1e-8)

    cam_dirs = np.array([c[2] for c in cam_defs], dtype=np.float32)
    best_cam = np.argmax(fnrm @ cam_dirs.T, axis=1)

    u_all = np.zeros((len(faces), 3), dtype=np.float32)
    v_all = np.zeros((len(faces), 3), dtype=np.float32)

    m0 = best_cam == 0
    u_all[m0], v_all[m0] = tri_vx[m0], 1.0 - tri_vy[m0]
    m1 = best_cam == 1
    u_all[m1], v_all[m1] = 1.0 - tri_vx[m1], 1.0 - tri_vy[m1]
    m2 = best_cam == 2
    u_all[m2], v_all[m2] = tri_vz[m2], 1.0 - tri_vy[m2]
    m3 = best_cam == 3
    u_all[m3], v_all[m3] = 1.0 - tri_vz[m3], 1.0 - tri_vy[m3]
    m4 = best_cam == 4
    u_all[m4], v_all[m4] = 1.0 - tri_vx[m4], (tri_vz[m4] if top_flip_z else (1.0 - tri_vz[m4]))
    m5 = best_cam == 5
    u_all[m5], v_all[m5] = tri_vx[m5], (tri_vz[m5] if bot_flip_z else (1.0 - tri_vz[m5]))

    u_all = np.clip(u_all, 0.004, 0.996)
    v_all = np.clip(v_all, 0.004, 0.996)

    tile_xy = np.array([c[3] for c in cam_defs], dtype=np.float32)
    atlas_u = (tile_xy[best_cam, 0][:, None] + u_all) / 3.0
    atlas_v = (tile_xy[best_cam, 1][:, None] + v_all) / 2.0

    flat_pos = tri_pos.reshape(-1, 3).astype(np.float32)
    flat_nrm = tri_nrm.reshape(-1, 3).astype(np.float32)
    flat_uv = np.stack([atlas_u.reshape(-1), atlas_v.reshape(-1)], axis=1).astype(np.float32)

    tex_buf = io.BytesIO()
    atlas.save(tex_buf, format='JPEG', quality=88, optimize=True)
    tex_bytes = tex_buf.getvalue()

    def pad4(b):
        rem = len(b) % 4
        return b + (b'\x00' * (4 - rem) if rem else b'')

    pos_bytes = flat_pos.tobytes()
    nrm_bytes = flat_nrm.tobytes()
    uv_bytes = flat_uv.tobytes()

    pos_p, nrm_p, uv_p, tex_p = pad4(pos_bytes), pad4(nrm_bytes), pad4(uv_bytes), pad4(tex_bytes)
    off_pos = 0
    off_nrm = len(pos_p)
    off_uv = off_nrm + len(nrm_p)
    off_tex = off_uv + len(uv_p)
    bin_blob = pos_p + nrm_p + uv_p + tex_p

    pmin = flat_pos.min(axis=0).tolist()
    pmax = flat_pos.max(axis=0).tolist()
    vcount = len(flat_pos)

    gltf = {
        "asset": {"version": "2.0", "generator": "Streetwar-6View-VisualHull"},
        "scene": 0,
        "scenes": [{"nodes": [0]}],
        "nodes": [{"mesh": 0, "name": sku}],
        "meshes": [{"primitives": [{"attributes": {"POSITION": 0, "NORMAL": 1, "TEXCOORD_0": 2}, "material": 0}]}],
        "materials": [{
            "name": f"{sku}_mat",
            "pbrMetallicRoughness": {"baseColorTexture": {"index": 0}, "metallicFactor": 0.04, "roughnessFactor": 0.72},
            "doubleSided": True,
        }],
        "textures": [{"sampler": 0, "source": 0}],
        "samplers": [{"magFilter": 9729, "minFilter": 9987, "wrapS": 33071, "wrapT": 33071}],
        "images": [{"bufferView": 3, "mimeType": "image/jpeg"}],
        "buffers": [{"byteLength": len(bin_blob)}],
        "bufferViews": [
            {"buffer": 0, "byteOffset": off_pos, "byteLength": len(pos_bytes), "target": 34962},
            {"buffer": 0, "byteOffset": off_nrm, "byteLength": len(nrm_bytes), "target": 34962},
            {"buffer": 0, "byteOffset": off_uv, "byteLength": len(uv_bytes), "target": 34962},
            {"buffer": 0, "byteOffset": off_tex, "byteLength": len(tex_bytes)},
        ],
        "accessors": [
            {"bufferView": 0, "componentType": 5126, "count": vcount, "type": "VEC3", "min": pmin, "max": pmax},
            {"bufferView": 1, "componentType": 5126, "count": vcount, "type": "VEC3"},
            {"bufferView": 2, "componentType": 5126, "count": vcount, "type": "VEC2"},
        ],
    }

    json_bytes = json.dumps(gltf, separators=(',', ':')).encode('utf-8')
    if len(json_bytes) % 4:
        json_bytes += b' ' * (4 - len(json_bytes) % 4)

    total_len = 12 + 8 + len(json_bytes) + 8 + len(bin_blob)
    os.makedirs(os.path.dirname(out_glb_path), exist_ok=True)
    with open(out_glb_path, 'wb') as f:
        f.write(struct.pack('<III', 0x46546C67, 2, total_len))
        f.write(struct.pack('<II', len(json_bytes), 0x4E4F534A))
        f.write(json_bytes)
        f.write(struct.pack('<II', len(bin_blob), 0x004E4942))
        f.write(bin_blob)

    # Also write .glb.js wrapper so file:// protocol can load via Blob URL without CORS errors
    with open(out_glb_path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('ascii')
    js_path = out_glb_path + '.js'
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(f'window.__GLB_B64=window.__GLB_B64||{{}};window.__GLB_B64["{sku}"]="{b64}";\n')

    return len(faces), len(flat_pos), os.path.getsize(out_glb_path)


if __name__ == '__main__':
    targets = [
        ('IX6180-100', 'dist/assets/productos/IX6180-100', 'dist/assets/models/IX6180-100.glb'),
        ('IW2872-700', 'dist/assets/productos/IW2872-700', 'dist/assets/models/IW2872-700.glb'),
    ]
    for sku, pdir, out_p in targets:
        f_cnt, v_cnt, size_b = build_glb_from_6views(sku, pdir, out_p)
        print(f"{sku}: {f_cnt} tris, {v_cnt} verts, {size_b/1024:.1f} KB -> {out_p}")
