import os
import sys
import json
import re
import glob
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

def detect_toe_left(img_rgba):
    """Detect if toe points to the left by comparing left vs right profile height."""
    arr = np.array(img_rgba)
    if arr.shape[2] == 4:
        mask = arr[:, :, 3] > 20
    else:
        mask = np.any(arr[:, :, :3] < 240, axis=2)
        
    y_idx, x_idx = np.where(mask)
    if len(x_idx) == 0:
        return True
    
    xmin, xmax = x_idx.min(), x_idx.max()
    bw = xmax - xmin
    if bw < 50:
        return True
        
    strip_w = max(10, int(bw * 0.18))
    ls = mask[:, xmin:xmin + strip_w]
    rs = mask[:, xmax - strip_w:xmax]
    ly = np.where(np.any(ls, axis=1))[0]
    ry = np.where(np.any(rs, axis=1))[0]
    lh = (ly.max() - ly.min()) if len(ly) else 0
    rh = (ry.max() - ry.min()) if len(ry) else 0
    # Shoe toe has smaller height than heel
    return lh <= rh

def isolate_and_center_shoe(img, target_size=1024, fill_ratio=0.82, is_grounded=True):
    """
    Isolates product, cleans background to #FFFFFF, centers inside target_size x target_size
    with fill_ratio, and adds subtle contact shadow if is_grounded is True.
    """
    img_rgba = img.convert('RGBA')
    arr = np.array(img_rgba)
    h, w = arr.shape[:2]
    
    # Background detection
    if arr.shape[2] == 4 and np.any(arr[:, :, 3] < 250):
        mask = arr[:, :, 3] > 25
    else:
        # Near white pixels threshold
        rgb = arr[:, :, :3]
        mask = np.any(rgb < 242, axis=2)
        
    if not np.any(mask):
        canvas = Image.new('RGB', (target_size, target_size), (255, 255, 255))
        return canvas
        
    y_idx, x_idx = np.where(mask)
    ymin, ymax = max(0, y_idx.min() - 2), min(h - 1, y_idx.max() + 2)
    xmin, xmax = max(0, x_idx.min() - 2), min(w - 1, x_idx.max() + 2)
    
    clean_arr = arr.copy()
    if clean_arr.shape[2] == 3:
        alpha = np.where(mask, 255, 0).astype(np.uint8)
        clean_arr = np.dstack([clean_arr, alpha])
    else:
        clean_arr[:, :, 3] = np.where(mask, clean_arr[:, :, 3], 0)
        
    clean_img = Image.fromarray(clean_arr, 'RGBA')
    cropped = clean_img.crop((xmin, ymin, xmax + 1, ymax + 1))
    
    cw, ch = cropped.size
    max_dim = int(target_size * fill_ratio)
    scale = min(max_dim / cw, max_dim / ch)
    nw = max(1, int(cw * scale))
    nh = max(1, int(ch * scale))
    
    resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)
    
    # Pure white canvas
    canvas = Image.new('RGBA', (target_size, target_size), (255, 255, 255, 255))
    pos_x = (target_size - nw) // 2
    pos_y = (target_size - nh) // 2
    
    if is_grounded:
        shadow = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(shadow)
        shadow_w = int(nw * 0.85)
        shadow_h = max(12, int(nh * 0.07))
        sx0 = (target_size - shadow_w) // 2
        sy0 = pos_y + nh - int(shadow_h * 0.45)
        sx1 = sx0 + shadow_w
        sy1 = sy0 + shadow_h
        draw.ellipse([sx0, sy0, sx1, sy1], fill=(30, 30, 30, 35))
        shadow = shadow.filter(ImageFilter.GaussianBlur(radius=8))
        canvas.alpha_composite(shadow)
        
    canvas.alpha_composite(resized, (pos_x, pos_y))
    return canvas.convert('RGB')

def process_sku(item, target_size=1024, fill_ratio=0.82):
    sku = item['sku']
    group = item['group'].replace(" ", "_")
    folder_origin = item.get('folderOrigin', '')
    
    out_dir = os.path.join('output_catalog', group, sku)
    os.makedirs(out_dir, exist_ok=True)
    
    # Check if all 16 files already exist
    existing = glob.glob(os.path.join(out_dir, '*.*'))
    if len(existing) >= 16:
        print(f"[{group}] {sku}: Already complete ({len(existing)} files), skipping.")
        return True
        
    print(f"\nProcessing [{group}] {sku} ({item.get('name')})...")
    
    # Look for sources:
    # 1. dist/assets/2-norm-std/<sku>
    std_dir = os.path.join('dist/assets/2-norm-std', sku)
    # 2. dist/assets/1-orig-raw/<sku>
    raw_dir = os.path.join('dist/assets/1-orig-raw', sku)
    if not os.path.exists(raw_dir) and folder_origin:
        raw_dir = os.path.join('dist/assets/1-orig-raw', folder_origin)
        
    # 3. _source_data
    source_dir = item.get('sourceDir', '')
    
    raw_files = []
    if os.path.exists(raw_dir):
        raw_files = [os.path.join(raw_dir, f) for f in sorted(os.listdir(raw_dir)) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))]
        
    std_files = {}
    if os.path.exists(std_dir):
        for f in os.listdir(std_dir):
            if f.endswith('.webp'):
                std_files[f.replace('.webp', '')] = os.path.join(std_dir, f)
                
    source_files = {}
    if source_dir and os.path.exists(source_dir):
        for f in os.listdir(source_dir):
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                source_files[f.lower()] = os.path.join(source_dir, f)
                
    # Function to get image for angle
    def get_angle_image(angle_id):
        # 01 | LATERAL: toe pointing left
        if angle_id == '01_lateral':
            if '01-lateral' in std_files:
                im = Image.open(std_files['01-lateral']).convert('RGBA')
            elif len(raw_files) > 0:
                im = Image.open(raw_files[0]).convert('RGBA')
            else:
                return None
            if not detect_toe_left(im):
                im = im.transpose(Image.FLIP_LEFT_RIGHT)
            return isolate_and_center_shoe(im, target_size, fill_ratio, is_grounded=True)
            
        # 02 | MEDIAL: toe pointing right
        elif angle_id == '02_medial':
            # Check source_files for medial
            medial_src = None
            for k, v in source_files.items():
                if 'medial' in k:
                    medial_src = v
                    break
            if not medial_src and len(raw_files) >= 3:
                # Often official-02 or downloaded-02/03 is medial
                for rf in raw_files[1:4]:
                    try:
                        test_im = Image.open(rf)
                        if test_im.width / test_im.height > 1.25:
                            medial_src = rf
                            break
                    except Exception:
                        pass
            if medial_src:
                im = Image.open(medial_src).convert('RGBA')
            elif '01-lateral' in std_files:
                # Flip lateral horizontally to point RIGHT
                im = Image.open(std_files['01-lateral']).convert('RGBA')
                im = im.transpose(Image.FLIP_LEFT_RIGHT)
            elif len(raw_files) > 0:
                im = Image.open(raw_files[0]).convert('RGBA')
                im = im.transpose(Image.FLIP_LEFT_RIGHT)
            else:
                return None
            # Ensure toe points right
            if detect_toe_left(im):
                im = im.transpose(Image.FLIP_LEFT_RIGHT)
            return isolate_and_center_shoe(im, target_size, fill_ratio, is_grounded=True)
            
        # 03 | 3/4 FRONT: toe pointing bottom-left
        elif angle_id == '03_3-4_front':
            if '02-frontal-3-4' in std_files:
                im = Image.open(std_files['02-frontal-3-4']).convert('RGBA')
            elif len(raw_files) > 1:
                im = Image.open(raw_files[1]).convert('RGBA')
            else:
                im = Image.open(raw_files[0]).convert('RGBA')
            if not detect_toe_left(im):
                im = im.transpose(Image.FLIP_LEFT_RIGHT)
            return isolate_and_center_shoe(im, target_size, fill_ratio, is_grounded=True)
            
        # 04 | 3/4 REAR: heel on left, toe pointing right
        elif angle_id == '04_3-4_rear':
            # Look in raw or source files
            rear_src = None
            if len(raw_files) >= 5:
                # check for rear 3/4 shot
                for rf in raw_files[3:]:
                    try:
                        test_im = Image.open(rf)
                        if 1.0 <= test_im.width / test_im.height <= 1.6:
                            rear_src = rf
                            break
                    except Exception:
                        pass
            if rear_src:
                im = Image.open(rear_src).convert('RGBA')
            elif '02-frontal-3-4' in std_files:
                im = Image.open(std_files['02-frontal-3-4']).convert('RGBA')
                im = im.transpose(Image.FLIP_LEFT_RIGHT)
            else:
                im = Image.open(raw_files[0]).convert('RGBA')
                im = im.transpose(Image.FLIP_LEFT_RIGHT)
            if detect_toe_left(im):
                im = im.transpose(Image.FLIP_LEFT_RIGHT)
            return isolate_and_center_shoe(im, target_size, fill_ratio, is_grounded=True)
            
        # 05 | FRONT: direct front view
        elif angle_id == '05_front':
            front_src = None
            for k, v in source_files.items():
                if 'front' in k:
                    front_src = v
                    break
            if not front_src:
                # Check raw_files for aspect ratio < 1.15
                for rf in raw_files:
                    try:
                        test_im = Image.open(rf)
                        ratio = test_im.width / test_im.height
                        if 0.6 <= ratio <= 1.15:
                            front_src = rf
                            break
                    except Exception:
                        pass
            if front_src:
                im = Image.open(front_src).convert('RGBA')
            elif '02-frontal-3-4' in std_files:
                im = Image.open(std_files['02-frontal-3-4']).convert('RGBA')
            else:
                im = Image.open(raw_files[0]).convert('RGBA')
            return isolate_and_center_shoe(im, target_size, fill_ratio, is_grounded=True)
            
        # 06 | REAR: direct rear heel view
        elif angle_id == '06_rear':
            if '03-trasera' in std_files:
                im = Image.open(std_files['03-trasera']).convert('RGBA')
            else:
                rear_src = None
                for k, v in source_files.items():
                    if 'rear' in k:
                        rear_src = v
                        break
                if not rear_src and len(raw_files) >= 3:
                    rear_src = raw_files[2]
                im = Image.open(rear_src).convert('RGBA') if rear_src else Image.open(raw_files[0]).convert('RGBA')
            return isolate_and_center_shoe(im, target_size, fill_ratio, is_grounded=True)
            
        # 07 | TOP-DOWN: horizontal, toe pointing right
        elif angle_id == '07_top_down':
            if '04-superior' in std_files:
                im = Image.open(std_files['04-superior']).convert('RGBA')
            else:
                top_src = None
                for k, v in source_files.items():
                    if 'top' in k:
                        top_src = v
                        break
                if not top_src and len(raw_files) >= 4:
                    top_src = raw_files[3]
                im = Image.open(top_src).convert('RGBA') if top_src else Image.open(raw_files[0]).convert('RGBA')
            # If vertical (height > width), rotate 90 degrees clockwise to make horizontal
            if im.height > im.width:
                im = im.rotate(270, expand=True)
            return isolate_and_center_shoe(im, target_size, fill_ratio, is_grounded=False)
            
        # 08 | OUTSOLE: horizontal, toe pointing right
        elif angle_id == '08_outsole':
            sole_src = None
            # Scan raw files for wide aspect or last files (often outsole)
            for rf in reversed(raw_files):
                try:
                    test_im = Image.open(rf)
                    ratio = test_im.width / test_im.height
                    if ratio > 1.8 or ratio < 0.55:
                        sole_src = rf
                        break
                except Exception:
                    pass
            if not sole_src and len(raw_files) >= 5:
                sole_src = raw_files[-1]
            if sole_src:
                im = Image.open(sole_src).convert('RGBA')
            elif '04-superior' in std_files:
                # Use underside/flipped top view as fallback
                im = Image.open(std_files['04-superior']).convert('RGBA')
                im = im.transpose(Image.FLIP_TOP_BOTTOM)
            else:
                im = Image.open(raw_files[0]).convert('RGBA')
            if im.height > im.width:
                im = im.rotate(270, expand=True)
            return isolate_and_center_shoe(im, target_size, fill_ratio, is_grounded=False)

    angles = [
        '01_lateral',
        '02_medial',
        '03_3-4_front',
        '04_3-4_rear',
        '05_front',
        '06_rear',
        '07_top_down',
        '08_outsole'
    ]
    
    generated_count = 0
    for ang in angles:
        try:
            final_img = get_angle_image(ang)
            if final_img is None:
                print(f"  Warning: No source found for {ang}")
                continue
                
            webp_path = os.path.join(out_dir, f"{sku}_{ang}.webp")
            png_path = os.path.join(out_dir, f"{sku}_{ang}.png")
            
            final_img.save(webp_path, 'WEBP', quality=90, method=6)
            final_img.save(png_path, 'PNG', optimize=True)
            generated_count += 1
        except Exception as e:
            print(f"  Error generating {ang}: {e}")
            
    print(f"  Generated {generated_count}/8 angles (16 files) for {sku}")
    return generated_count == 8

def run():
    with open('dist/js/flow_nanobanana_data.js', 'r', encoding='utf-8') as f:
        data = json.loads(re.search(r'const flowNanobananaData = ({.*?});\s*$', f.read(), re.DOTALL).group(1))

    catalog = data['catalog']
    print(f"=== Starting full generation for {len(catalog)} catalog models ===")
    
    success = 0
    failed = 0
    
    for i, item in enumerate(catalog):
        print(f"\n--- Model {i+1}/{len(catalog)} ---")
        ok = process_sku(item)
        if ok:
            success += 1
        else:
            failed += 1
            
    print(f"\n==========================================")
    print(f"COMPLETED! Successfully verified/generated {success}/{len(catalog)} models. Failed: {failed}")

if __name__ == '__main__':
    run()
