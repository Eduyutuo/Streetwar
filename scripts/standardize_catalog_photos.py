import os
import sys
import json
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

def isolate_shoe(img_rgba, bg_thresh=240):
    """
    Cleans background around the shoe:
    Removes near-white backgrounds, preserving the shoe and shadows.
    """
    arr = np.array(img_rgba)
    h, w = arr.shape[:2]
    
    # If image already has a transparent alpha channel
    if arr.shape[2] == 4 and np.any(arr[:, :, 3] < 250):
        mask = arr[:, :, 3] > 20
    else:
        # Check non-white pixels
        rgb = arr[:, :, :3]
        mask = np.any(rgb < bg_thresh, axis=2)
        
    if not np.any(mask):
        return img_rgba
        
    y_idx, x_idx = np.where(mask)
    ymin, ymax = y_idx.min(), y_idx.max()
    xmin, xmax = x_idx.min(), x_idx.max()
    
    # Create clean RGBA
    clean_arr = arr.copy()
    if clean_arr.shape[2] == 3:
        alpha = np.where(mask, 255, 0).astype(np.uint8)
        clean_arr = np.dstack([clean_arr, alpha])
    else:
        # Smooth alpha mask
        clean_arr[:, :, 3] = np.where(mask, clean_arr[:, :, 3], 0)
        
    clean_img = Image.fromarray(clean_arr, 'RGBA')
    cropped = clean_img.crop((xmin, ymin, xmax + 1, ymax + 1))
    return cropped

def detect_toe_left(img_rgba):
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
    return lh <= rh

def process_image(src_path, dst_path, angle_name, target_size=1200, padding_pct=0.10):
    try:
        with Image.open(src_path) as raw:
            img_rgba = raw.convert('RGBA')
            
        cropped = isolate_shoe(img_rgba)
        
        # Enforce direction for lateral and 3/4
        if angle_name in ('01-lateral', '02-frontal-3-4'):
            if not detect_toe_left(cropped):
                cropped = cropped.transpose(Image.FLIP_LEFT_RIGHT)
                
        # Scale with 10% padding (shoe occupies 80% max dimension)
        cw, ch = cropped.size
        max_dim = int(target_size * (1.0 - 2 * padding_pct)) # 960 px
        scale = min(max_dim / cw, max_dim / ch)
        nw = max(1, int(cw * scale))
        nh = max(1, int(ch * scale))
        
        resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)
        
        # Canvas 1200x1200 pure white
        canvas = Image.new('RGBA', (target_size, target_size), (255, 255, 255, 255))
        
        pos_x = (target_size - nw) // 2
        pos_y = (target_size - nh) // 2
        
        # Grounding shadow
        shadow = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(shadow)
        
        shadow_w = int(nw * 0.85)
        shadow_h = max(16, int(nh * 0.08))
        sx0 = (target_size - shadow_w) // 2
        sy0 = pos_y + nh - int(shadow_h * 0.55)
        sx1 = sx0 + shadow_w
        sy1 = sy0 + shadow_h
        
        draw.ellipse([sx0, sy0, sx1, sy1], fill=(25, 25, 25, 40))
        shadow = shadow.filter(ImageFilter.GaussianBlur(radius=10))
        
        canvas.alpha_composite(shadow)
        canvas.alpha_composite(resized, (pos_x, pos_y))
        
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        final_rgb = canvas.convert('RGB')
        final_rgb.save(dst_path, 'WEBP', quality=92, method=6)
        return True, nw, nh
    except Exception as e:
        print(f"Error processing {src_path}: {e}")
        return False, 0, 0

def run():
    with open('scratch/assigned_angles.json', 'r', encoding='utf-8') as f:
        assigned = json.load(f)
        
    src_base = 'dist/assets/1-orig-raw'
    dst_base = 'dist/assets/2-norm-std'
    mirror_base = 'dist/assets/productos'
    
    total_processed = 0
    errors = 0
    
    new_gallery_photos = {}
    
    for item in assigned:
        idx = str(item['index'])
        sku = item['sku']
        folder = item['folder']
        tomas = item['tomas']
        
        new_gallery_photos[idx] = []
        print(f"\nProcessing [{item['index']:02d}] {sku} ({item['name']})...")
        
        for angle_name, src_file in tomas.items():
            src_fp = os.path.join(src_base, folder, src_file)
            dst_fp = os.path.join(dst_base, sku, f"{angle_name}.webp")
            mirror_fp = os.path.join(mirror_base, sku, f"{angle_name}.webp")
            rel_path = f"productos/{sku}/{angle_name}.webp"
            
            ok, nw, nh = process_image(src_fp, dst_fp, angle_name)
            if ok:
                # Mirror to productos
                os.makedirs(os.path.dirname(mirror_fp), exist_ok=True)
                with open(dst_fp, 'rb') as f_in, open(mirror_fp, 'wb') as f_out:
                    f_out.write(f_in.read())
                    
                new_gallery_photos[idx].append(rel_path)
                total_processed += 1
                print(f"  + {angle_name}.webp (from {src_file}, {nw}x{nh})")
            else:
                errors += 1
                print(f"  FAILED: {angle_name}")

    # Save gallery JS
    js_content = "// Catálogo estandarizado: 4 ángulos uniformes por producto\n"
    js_content += "const sourceLinkPhotos = " + json.dumps(new_gallery_photos, indent=2) + ";\n"
    
    with open('dist/js/source-link-photos.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    print(f"\n==========================================")
    print(f"COMPLETED! Processed {total_processed} images across {len(assigned)} products. Errors: {errors}")
    print(f"Saved gallery mapping to dist/js/source-link-photos.js")

if __name__ == '__main__':
    run()
