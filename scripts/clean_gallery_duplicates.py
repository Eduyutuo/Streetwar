import os
import json
from PIL import Image
import numpy as np

def run_deduplication():
    prod_base = 'dist/assets/productos'
    
    with open('dist/js/flow_nanobanana_data.js', 'r', encoding='utf-8') as f:
        text = f.read()
    import re
    m = re.search(r'const flowNanobananaData = ({.*?});\s*$', text, re.DOTALL)
    catalog = json.loads(m.group(1))['catalog']
    
    print(f"Auditing and deduplicating galleries for all {len(catalog)} products...")
    
    clean_galleries = {}
    total_removed = 0
    
    for item in catalog:
        idx = str(item['index'])
        sku = item['sku']
        sku_dir = os.path.join(prod_base, sku)
        
        if not os.path.exists(sku_dir):
            clean_galleries[idx] = [item['preview_primary']]
            continue
            
        canonical_order = [
            '01-lateral.webp',
            '02-medial.webp',
            '03-3-4-front.webp',
            '04-3-4-rear.webp',
            '05-front.webp',
            '06-rear.webp',
            '07-top-down.webp',
            '08-outsole.webp'
        ]
        
        existing_files = [f for f in canonical_order if os.path.exists(os.path.join(sku_dir, f))]
        
        # Space Jam (IX6180-100) is the ground-truth master with 8 unique angles from 4x2 grid
        if sku == 'IX6180-100':
            clean_galleries[idx] = [f"productos/{sku}/{f}" for f in existing_files]
            continue
            
        # For all other products, load thumbnails and detect duplicate/redundant images
        chosen_files = []
        chosen_thumbs = []
        
        for f in existing_files:
            fp = os.path.join(sku_dir, f)
            try:
                im = Image.open(fp).convert('RGB')
                arr = np.array(im)
                
                # Check bounding box & aspect
                mask = np.any(arr < 240, axis=2)
                y, x = np.where(mask)
                if not len(x):
                    continue
                xmin, xmax, ymin, ymax = x.min(), x.max(), y.min(), y.max()
                w, h = xmax - xmin, ymax - ymin
                aspect = w / h if h > 0 else 0
                
                # Toe direction
                sw = max(5, int(w * 0.15))
                ly = np.where(np.any(mask[:, xmin:xmin+sw], axis=1))[0]
                ry = np.where(np.any(mask[:, xmax-sw:xmax], axis=1))[0]
                lh = (ly.max() - ly.min()) if len(ly) else 0
                rh = (ry.max() - ry.min()) if len(ry) else 0
                toe_left = lh <= rh
                
                # Check for zoomed-in detail crops (elephant print, stitching close-up) that pretend to be a full view
                border_pixels = np.sum(mask[0, :]) + np.sum(mask[-1, :]) + np.sum(mask[:, 0]) + np.sum(mask[:, -1])
                is_crop_zoom = border_pixels > (1024 + 1024) * 0.10
                
                # Special checks for fake slots:
                # 1. If slot is 04-3-4-rear or 03-3-4-front, but it has aspect > 1.35 and toe_left == True (i.e. another lateral profile pointing left)
                if f in ['03-3-4-front.webp', '04-3-4-rear.webp'] and aspect > 1.35 and toe_left:
                    # It's a duplicate lateral profile masquerading as 3/4!
                    total_removed += 1
                    print(f"  [{sku}] Removing duplicate lateral in slot {f} (aspect={aspect:.2f}, toe_left={toe_left})")
                    continue
                    
                # 2. If slot is 03-3-4-front or 04-3-4-rear, but is a zoom crop
                if f in ['03-3-4-front.webp', '04-3-4-rear.webp'] and is_crop_zoom:
                    total_removed += 1
                    print(f"  [{sku}] Removing zoom detail crop in slot {f}")
                    continue
                    
                # 3. Visual similarity comparison with already accepted slots
                thumb = np.array(im.resize((48, 48)), dtype=float)
                is_duplicate = False
                for cf, cth in zip(chosen_files, chosen_thumbs):
                    # Compute difference focused on non-white foreground
                    fg_mask = (thumb < 240) | (cth < 240)
                    if np.any(fg_mask):
                        fg_diff = np.mean(np.abs(thumb[fg_mask] - cth[fg_mask]))
                        fg_diff_flip = np.mean(np.abs(thumb[fg_mask] - np.fliplr(cth)[fg_mask]))
                    else:
                        fg_diff = np.mean(np.abs(thumb - cth))
                        fg_diff_flip = np.mean(np.abs(thumb - np.fliplr(cth)))
                        
                    # If foreground diff < 12.0, it's visually the exact same image
                    if fg_diff < 12.0:
                        is_duplicate = True
                        total_removed += 1
                        print(f"  [{sku}] Removing {f} - identical duplicate of {cf} (fg_diff={fg_diff:.2f})")
                        break
                    # If it's a flipped version of lateral in 02-medial or elsewhere
                    if fg_diff_flip < 8.0:
                        # Artificially flipped duplicate
                        is_duplicate = True
                        total_removed += 1
                        print(f"  [{sku}] Removing {f} - artificial mirror-flip duplicate of {cf} (fg_diff_flip={fg_diff_flip:.2f})")
                        break
                        
                if not is_duplicate:
                    chosen_files.append(f)
                    chosen_thumbs.append(thumb)
                    
            except Exception as e:
                print(f"Error checking {fp}: {e}")
                
        clean_galleries[idx] = [f"productos/{sku}/{f}" for f in chosen_files]
        print(f"[{item['index']+1:02d}] {sku} ({item['name'][:30]}): {len(chosen_files)} unique clean angles: {chosen_files}")

    print("\n" + "="*80)
    print(f"DEDUPLICATION COMPLETE! Removed {total_removed} duplicate/misplaced images across catalog.")
    
    # Save to dist/js/source-link-photos.js
    js_content = "// Catálogo estandarizado: ángulos uniformes sin duplicados por producto\n"
    js_content += "const sourceLinkPhotos = " + json.dumps(clean_galleries, indent=2) + ";\n"
    with open('dist/js/source-link-photos.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    # Also sync to dist/js/galleries.js
    gal_content = "// Galerías estandarizadas: ángulos uniformes sin duplicados por producto\n"
    gal_content += "const galleries = " + json.dumps(clean_galleries, indent=2) + ";\n"
    with open('dist/js/galleries.js', 'w', encoding='utf-8') as f:
        f.write(gal_content)

    print("Updated dist/js/source-link-photos.js and dist/js/galleries.js successfully.")

if __name__ == '__main__':
    run_deduplication()
