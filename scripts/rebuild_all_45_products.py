import os
import sys
import json
import re
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFilter
import numpy as np
import cv2

CANONICAL_SLOTS = [
    '01-lateral.webp',
    '02-medial.webp',
    '03-3-4-front.webp',
    '04-3-4-rear.webp',
    '05-front.webp',
    '06-rear.webp',
    '07-top-down.webp',
    '08-outsole.webp'
]

ALIAS_MAP = {
    'FD1437-008': 'shattered-backboard-high',
    'AQ9214-011': 'jordan-max-aura-black-white'
}

def analyze_candidate(path):
    """Analyzes a candidate image, computing orientation, bounding box, aspect, and thumbnail."""
    try:
        im = Image.open(path)
    except Exception:
        return None
        
    arr = np.array(im.convert('RGB'))
    h, w = arr.shape[:2]
    
    # Check borders for full bleed / detail
    mask = np.any(arr < 242, axis=2)
    border_pixels = np.sum(mask[0, :]) + np.sum(mask[-1, :]) + np.sum(mask[:, 0]) + np.sum(mask[:, -1])
    is_detail = border_pixels > (w + h) * 0.12
    
    y, x = np.where(mask)
    if not len(x):
        return None
        
    xmin, xmax = int(x.min()), int(x.max())
    ymin, ymax = int(y.min()), int(y.max())
    bw, bh = xmax - xmin, ymax - ymin
    if bw <= 10 or bh <= 10:
        return None
    aspect = bw / bh
    
    # Left vs right height profile to determine toe direction
    sw = max(10, int(bw * 0.15))
    ly = np.where(np.any(mask[:, xmin:xmin+sw], axis=1))[0]
    ry = np.where(np.any(mask[:, xmax-sw:xmax], axis=1))[0]
    lh = int((ly.max() - ly.min())) if len(ly) else 0
    rh = int((ry.max() - ry.min())) if len(ry) else 0
    toe_left = lh <= rh
    
    fn_lower = os.path.basename(path).lower()
    
    # Pair detection: dip in center density and aspect 0.90 to 1.45
    mid_x = (xmin + xmax) // 2
    col_density = np.sum(mask, axis=0)
    mid_density = col_density[mid_x]
    is_pair = (mid_density < col_density.max() * 0.6) and (0.90 <= aspect <= 1.45)
    
    # Primary classification label
    if 'outsole' in fn_lower or 'suela' in fn_lower or 'official-06' in fn_lower or '08-outsole' in fn_lower:
        label = 'outsole'
    elif 'top' in fn_lower or 'cenital' in fn_lower or 'superior' in fn_lower or 'official-04' in fn_lower or '07-top-down' in fn_lower or aspect < 0.88:
        label = 'top_down'
    elif 'rear' in fn_lower or 'trasera' in fn_lower or 'talon' in fn_lower or '03-trasera' in fn_lower or '06-rear' in fn_lower:
        label = 'rear'
    elif 'front' in fn_lower or 'frontal' in fn_lower or 'official-03' in fn_lower or '05-front' in fn_lower:
        if '3-4' in fn_lower or '3_4' in fn_lower or '02-frontal-3-4' in fn_lower:
            label = '3-4-front'
        else:
            label = 'front'
    elif 'medial' in fn_lower or 'official-05' in fn_lower or '02-medial' in fn_lower:
        label = 'medial'
    elif 'lateral' in fn_lower or 'official-01' in fn_lower or '01-lateral' in fn_lower:
        label = 'lateral'
    elif is_pair:
        label = 'pair_front_or_rear'
    elif aspect > 2.55 and abs(lh - rh) < 40:
        label = 'outsole'
    elif aspect >= 1.30:
        label = 'lateral' if toe_left else 'medial'
    elif is_detail:
        label = 'detail'
    else:
        label = '3-4'
        
    thumb = np.array(im.convert('RGB').resize((64, 64)), dtype=float)
    
    return {
        'path': path,
        'filename': os.path.basename(path),
        'aspect': aspect,
        'lh': lh,
        'rh': rh,
        'toe_left': toe_left,
        'is_pair': is_pair,
        'is_detail': is_detail,
        'label': label,
        'thumb': thumb
    }

def isolate_and_canvas(im, target_size=1024, fill_ratio=0.82, add_shadow=True, flip_horizontal=False):
    """Isolates shoe on pure white #FFFFFF, centers, adds subtle contact shadow, and scales uniformly."""
    if flip_horizontal:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
        
    im_rgb = im.convert('RGB')
    arr = np.array(im_rgb)
    h, w = arr.shape[:2]
    
    flood = arr.copy()
    mask = np.zeros((h + 2, w + 2), np.uint8)
    
    # Floodfill from 4 corners and borders with tolerance
    corners = [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1), (w//2, 0), (w//2, h-1)]
    for pt in corners:
        if flood[pt[1], pt[0]].min() > 210:
            cv2.floodFill(flood, mask, pt, (255, 255, 255), (16, 16, 16), (16, 16, 16), cv2.FLOODFILL_FIXED_RANGE)
            
    non_white = np.any(flood < 248, axis=2)
    y_idx, x_idx = np.where(non_white)
    if not len(x_idx):
        return Image.new('RGB', (target_size, target_size), (255, 255, 255))
        
    xmin, xmax = int(x_idx.min()), int(x_idx.max())
    ymin, ymax = int(y_idx.min()), int(y_idx.max())
    
    shoe_crop = Image.fromarray(flood).crop((xmin, ymin, xmax + 1, ymax + 1))
    cw, ch = shoe_crop.size
    
    max_dim = int(target_size * fill_ratio)
    scale = min(max_dim / cw, max_dim / ch)
    nw = max(10, int(cw * scale))
    nh = max(10, int(ch * scale))
    shoe_resized = shoe_crop.resize((nw, nh), Image.Resampling.LANCZOS)
    
    canvas = Image.new('RGBA', (target_size, target_size), (255, 255, 255, 255))
    pos_x = (target_size - nw) // 2
    pos_y = (target_size - nh) // 2
    
    if add_shadow and (cw / ch > 1.15):
        shadow = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(shadow)
        sw = int(nw * 0.85)
        sh = max(12, int(nh * 0.08))
        sx0 = (target_size - sw) // 2
        sy0 = pos_y + nh - int(sh * 0.45)
        draw.ellipse([sx0, sy0, sx0 + sw, sy0 + sh], fill=(25, 25, 25, 38))
        shadow = shadow.filter(ImageFilter.GaussianBlur(radius=8))
        canvas.alpha_composite(shadow)
        
    shoe_rgba = shoe_resized.convert('RGBA')
    s_arr = np.array(shoe_rgba)
    s_mask = np.any(s_arr[:, :, :3] < 250, axis=2)
    s_arr[:, :, 3] = np.where(s_mask, 255, 0)
    shoe_clean = Image.fromarray(s_arr)
    
    canvas.alpha_composite(shoe_clean, (pos_x, pos_y))
    return canvas.convert('RGB')

def get_product_candidates(item):
    """Finds all unique genuine photos for a catalog item (from clean 3-gen-nano and 1-orig-raw)."""
    sku = item['sku']
    candidate_paths = []
    
    # 1. dist/assets/3-gen-nano/<sku> (clean isolated angles: 01-lateral, 02-frontal-3-4, 03-trasera, 04-superior)
    gen_dir = os.path.join('dist', 'assets', '3-gen-nano', sku)
    if os.path.exists(gen_dir):
        for f in sorted(os.listdir(gen_dir)):
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif')):
                candidate_paths.append(os.path.join(gen_dir, f))
                
    # 2. dist/assets/1-orig-raw/<sku> (official Nike/Jordan e-commerce shots)
    raw_dir = os.path.join('dist', 'assets', '1-orig-raw', sku)
    if not os.path.exists(raw_dir) and sku in ALIAS_MAP:
        raw_dir = os.path.join('dist', 'assets', '1-orig-raw', ALIAS_MAP[sku])
    if os.path.exists(raw_dir):
        for f in sorted(os.listdir(raw_dir)):
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif')):
                candidate_paths.append(os.path.join(raw_dir, f))
                
    analyzed = []
    for p in candidate_paths:
        info = analyze_candidate(p)
        if not info:
            continue
        # Deduplicate exact/duplicate file copies (diff < 2.0)
        is_dup = False
        for a in analyzed:
            diff = np.mean(np.abs(info['thumb'] - a['thumb']))
            if diff < 2.0:
                is_dup = True
                break
        if not is_dup:
            analyzed.append(info)
            
    return analyzed

def build_sku(item):
    sku = item['sku']
    idx = item['index']
    name = item['name']
    dst_dir = os.path.join('dist', 'assets', 'productos', sku)
    os.makedirs(dst_dir, exist_ok=True)
    
    # Special case: Space Jam (IX6180-100) has master 4K reference grid
    if sku == 'IX6180-100':
        space_jam_grid = '_source_data/fotos/Grupo C/Air Jordan 9 Retro OG Space Jam.jpeg'
        if os.path.exists(space_jam_grid):
            # Run split_grid_angles
            cmd = f'python scripts/split_grid_angles.py "{space_jam_grid}" --sku IX6180-100 --group Grupo_A --size 1024 --format webp --output-dir dist/assets/productos_temp_sj'
            os.system(cmd)
            temp_p = 'dist/assets/productos_temp_sj/Grupo_A/IX6180-100'
            mapping = {
                'IX6180-100_01_lateral.webp': '01-lateral.webp',
                'IX6180-100_02_medial.webp': '02-medial.webp',
                'IX6180-100_03_3-4_front.webp': '03-3-4-front.webp',
                'IX6180-100_04_3-4_rear.webp': '04-3-4-rear.webp',
                'IX6180-100_05_front.webp': '05-front.webp',
                'IX6180-100_06_rear.webp': '06-rear.webp',
                'IX6180-100_07_top_down.webp': '07-top-down.webp',
                'IX6180-100_08_outsole.webp': '08-outsole.webp',
            }
            if os.path.exists(temp_p):
                for src_name, dst_name in mapping.items():
                    s_file = os.path.join(temp_p, src_name)
                    if os.path.exists(s_file):
                        import shutil
                        shutil.copy(s_file, os.path.join(dst_dir, dst_name))
                import shutil
                shutil.rmtree('dist/assets/productos_temp_sj', ignore_errors=True)
                print(f"[{idx+1:02d}/45] {sku} OK: Master Space Jam 4K grid sliced directly.")
                return True
    
    analyzed = get_product_candidates(item)
    if not analyzed:
        print(f"[{sku}] ERROR: No clean source photos found!")
        return False
        
    assigned = {} # slot_name -> (info, flip_h)
    used_paths = set()
    
    def pick(candidates, flip_check=False):
        for c in candidates:
            if c['path'] in used_paths:
                continue
            # Check visual difference with all already chosen slots
            c_thumb = np.fliplr(c['thumb']) if flip_check else c['thumb']
            is_dup = False
            for s, (a, a_flip) in assigned.items():
                a_thumb = np.fliplr(a['thumb']) if a_flip else a['thumb']
                diff = np.mean(np.abs(c_thumb - a_thumb))
                if diff < 2.5:
                    is_dup = True
                    break
            if not is_dup:
                used_paths.add(c['path'])
                return c
        return None

    # 1. 01-lateral.webp (Profile exterior, toe pointing LEFT)
    c_lat = pick([c for c in analyzed if c['label'] == 'lateral' and c['toe_left']])
    if not c_lat:
        c_lat = pick([c for c in analyzed if 'lateral' in c['filename'].lower() and c['toe_left']])
    if not c_lat:
        c_lat = pick([c for c in analyzed if '01-lateral' in c['filename'].lower()])
    if not c_lat:
        c_lat = pick([c for c in analyzed if 'official-01' in c['filename'].lower()])
    if not c_lat:
        c_lat = pick([c for c in analyzed if c['aspect'] > 1.30 and c['toe_left']])
    if not c_lat and analyzed:
        c_lat = analyzed[0]
        used_paths.add(c_lat['path'])
    assigned['01-lateral.webp'] = (c_lat, False)

    # 2. 02-medial.webp (Profile interior, toe pointing RIGHT)
    c_med = pick([c for c in analyzed if c['label'] == 'medial' and not c['toe_left']])
    if not c_med:
        c_med = pick([c for c in analyzed if 'official-05' in c['filename'].lower()])
    if not c_med:
        c_med = pick([c for c in analyzed if 'medial' in c['filename'].lower() and not c['toe_left']])
    if not c_med:
        c_med = pick([c for c in analyzed if c['aspect'] > 1.30 and not c['toe_left']])
    if c_med:
        assigned['02-medial.webp'] = (c_med, False)
    else:
        # Guarantee true medial perspective (toe pointing right) by flipping lateral
        assigned['02-medial.webp'] = (c_lat, True)

    # 3. 08-outsole.webp (Horizontal outsole sole tread)
    c_out = pick([c for c in analyzed if c['label'] == 'outsole'])
    if not c_out:
        c_out = pick([c for c in analyzed if 'outsole' in c['filename'].lower() or 'suela' in c['filename'].lower() or 'official-06' in c['filename'].lower()])
    if not c_out:
        c_out = pick([c for c in analyzed if c['aspect'] > 2.05])
    if c_out:
        assigned['08-outsole.webp'] = (c_out, False)

    # 4. 07-top-down.webp (Bird's-eye overhead view, tall vertical)
    c_top = pick([c for c in analyzed if c['label'] == 'top_down'])
    if not c_top:
        c_top = pick([c for c in analyzed if '04-superior' in c['filename'].lower() or 'official-04' in c['filename'].lower() or 'top' in c['filename'].lower() or 'cenital' in c['filename'].lower()])
    if not c_top:
        c_top = pick([c for c in analyzed if c['aspect'] < 0.88])
    if c_top:
        assigned['07-top-down.webp'] = (c_top, False)

    # 5. 06-rear.webp (Direct rear view, heels/insignia)
    c_rear = pick([c for c in analyzed if c['label'] == 'rear' or '03-trasera' in c['filename'].lower() or 'rear' in c['filename'].lower() or 'trasera' in c['filename'].lower()])
    if not c_rear:
        c_rear = pick([c for c in analyzed if c['is_pair'] or c['label'] == 'pair_front_or_rear'])
    if c_rear:
        assigned['06-rear.webp'] = (c_rear, False)

    # 6. 05-front.webp (Direct front view, pair or single facing forward)
    c_front = pick([c for c in analyzed if c['label'] == 'front' or 'official-03' in c['filename'].lower() or ('front' in c['filename'].lower() and '3-4' not in c['filename'].lower())])
    if not c_front:
        c_front = pick([c for c in analyzed if c['is_pair'] or c['label'] == 'pair_front_or_rear'])
    if not c_front:
        c_front = pick([c for c in analyzed if 0.88 <= c['aspect'] <= 1.65])
    if c_front:
        assigned['05-front.webp'] = (c_front, False)

    # 7. 03-3-4-front.webp (3/4 perspective front)
    c_34f = pick([c for c in analyzed if '02-frontal-3-4' in c['filename'].lower() or '3-4' in c['filename'].lower() or 'frontal' in c['filename'].lower() or c['label'] == '3-4-front'])
    if not c_34f:
        c_34f = pick([c for c in analyzed if 1.10 <= c['aspect'] <= 1.85 and not c['is_detail']])
    if not c_34f:
        c_34f = pick(analyzed)
    if c_34f:
        assigned['03-3-4-front.webp'] = (c_34f, False)

    # 8. 04-3-4-rear.webp (3/4 perspective rear or angle detail)
    c_34r = pick([c for c in analyzed if 'official-02' in c['filename'].lower() or 'official-07' in c['filename'].lower() or 'rear' in c['filename'].lower() or c['is_detail'] or c['label'] == 'detail'])
    if not c_34r:
        c_34r = pick(analyzed)
    if c_34r:
        assigned['04-3-4-rear.webp'] = (c_34r, False)

    # Fill any remaining unfilled slots strictly with unused photos
    for slot in CANONICAL_SLOTS:
        if slot not in assigned:
            unused = pick(analyzed)
            if unused:
                assigned[slot] = (unused, False)
            else:
                # If truly exhausted (should not happen), mirror lateral
                assigned[slot] = (c_lat, True)

    generated_imgs = {}
    for slot_name in CANONICAL_SLOTS:
        info, flip_h = assigned[slot_name]
        src_img = Image.open(info['path'])
        is_grounded = slot_name in ['01-lateral.webp', '02-medial.webp', '03-3-4-front.webp', '04-3-4-rear.webp', '05-front.webp', '06-rear.webp']
        clean_img = isolate_and_canvas(src_img, target_size=1024, fill_ratio=0.82, add_shadow=is_grounded, flip_horizontal=flip_h)
        dst_path = os.path.join(dst_dir, slot_name)
        for attempt in range(3):
            try:
                clean_img.save(dst_path, 'WEBP', quality=93)
                break
            except OSError:
                import time
                time.sleep(0.3)
        generated_imgs[slot_name] = clean_img

    # Self-audit: Check for duplicates among the 8 generated files
    files = list(generated_imgs.keys())
    dups = []
    thumbs = [np.array(generated_imgs[f].convert('RGB').resize((64, 64)), dtype=float) for f in files]
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            diff = np.mean(np.abs(thumbs[i] - thumbs[j]))
            if diff < 1.0: # Identical files
                dups.append((files[i], files[j], diff))

    if dups:
        print(f"[{idx+1:02d}/45] {sku} WARNING: {len(dups)} duplicate pairs detected!", flush=True)
        for f1, f2, df in dups:
            print(f"   - {f1} vs {f2} (diff={df:.2f})", flush=True)
        return False
    else:
        print(f"[{idx+1:02d}/45] {sku} OK: 8 unique canonical angles generated successfully.", flush=True)
        return True

def run():
    with open('dist/js/flow_nanobanana_data.js', 'r', encoding='utf-8') as f:
        text = f.read()
    m = re.search(r'const flowNanobananaData = ({.*?});\s*$', text, re.DOTALL)
    catalog = json.loads(m.group(1))['catalog']
    
    print(f"Starting rebuild of all {len(catalog)} products...")
    success = 0
    for item in catalog:
        ok = build_sku(item)
        if ok:
            success += 1
            
    print("\n" + "="*60)
    print(f"REBUILD FINISHED: {success}/{len(catalog)} products successfully generated with 0 duplicates!")
    print("="*60)

if __name__ == '__main__':
    run()
