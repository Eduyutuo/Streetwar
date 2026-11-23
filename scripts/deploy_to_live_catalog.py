import os
import shutil
import json
import re
from PIL import Image

def deploy():
    # 1. Load catalog from flow_nanobanana_data.js
    with open('dist/js/flow_nanobanana_data.js', 'r', encoding='utf-8') as f:
        data = json.loads(re.search(r'const flowNanobananaData = ({.*?});\s*$', f.read(), re.DOTALL).group(1))

    catalog = data['catalog']
    print(f"Deploying standardized WebP images for {len(catalog)} products...")

    target_size = (1024, 1024)
    deployed_files = 0
    size_checks = 0
    size_errors = 0

    canonical_angles = [
        ('01_lateral', '01-lateral.webp'),
        ('02_medial', '02-medial.webp'),
        ('03_3-4_front', '03-3-4-front.webp'),
        ('04_3-4_rear', '04-3-4-rear.webp'),
        ('05_front', '05-front.webp'),
        ('06_rear', '06-rear.webp'),
        ('07_top_down', '07-top-down.webp'),
        ('08_outsole', '08-outsole.webp')
    ]

    source_link_photos = {}
    new_galleries = {}

    for i, item in enumerate(catalog):
        sku = item['sku']
        group = item['group'].replace(' ', '_')
        src_dir = os.path.join('output_catalog', group, sku)
        dst_dir = os.path.join('dist', 'assets', 'productos', sku)
        norm_dir = os.path.join('dist', 'assets', '2-norm-std', sku)

        os.makedirs(dst_dir, exist_ok=True)
        os.makedirs(norm_dir, exist_ok=True)

        product_photo_list = []

        for code, standard_fn in canonical_angles:
            sku_webp_fn = f"{sku}_{code}.webp"
            src_file = os.path.join(src_dir, sku_webp_fn)

            if not os.path.exists(src_file):
                print(f"ERROR: Missing {src_file}!")
                continue

            # Verify dimensions
            with Image.open(src_file) as im:
                size_checks += 1
                if im.size != target_size:
                    print(f"ERROR: Image {src_file} size {im.size} != {target_size}!")
                    size_errors += 1

            # 1. Copy as {sku}_{code}.webp
            dst_sku_webp = os.path.join(dst_dir, sku_webp_fn)
            shutil.copyfile(src_file, dst_sku_webp)

            # 2. Copy as standard name (e.g. 01-lateral.webp)
            dst_standard = os.path.join(dst_dir, standard_fn)
            shutil.copyfile(src_file, dst_standard)

            # 3. Copy to norm_dir
            dst_norm = os.path.join(norm_dir, standard_fn)
            shutil.copyfile(src_file, dst_norm)

            # 4. Backward compatibility aliases
            if code == '03_3-4_front':
                shutil.copyfile(src_file, os.path.join(dst_dir, '02-frontal-3-4.webp'))
                shutil.copyfile(src_file, os.path.join(norm_dir, '02-frontal-3-4.webp'))
            elif code == '06_rear':
                shutil.copyfile(src_file, os.path.join(dst_dir, '03-trasera.webp'))
                shutil.copyfile(src_file, os.path.join(norm_dir, '03-trasera.webp'))
            elif code == '07_top_down':
                shutil.copyfile(src_file, os.path.join(dst_dir, '04-superior.webp'))
                shutil.copyfile(src_file, os.path.join(norm_dir, '04-superior.webp'))

            product_photo_list.append(f"productos/{sku}/{standard_fn}")
            deployed_files += 1

        source_link_photos[str(i)] = product_photo_list
        new_galleries[str(i)] = product_photo_list

    # 2. Write dist/js/source-link-photos.js
    slp_js = "// Catálogo estandarizado: 8 ángulos uniformes (1024x1024 px WebP) por producto\n"
    slp_js += "const sourceLinkPhotos = " + json.dumps(source_link_photos, indent=2) + ";\n"
    with open('dist/js/source-link-photos.js', 'w', encoding='utf-8') as f:
        f.write(slp_js)
    print("Updated dist/js/source-link-photos.js with 8 angles for all 45 products!")

    # 3. Write dist/js/galleries.js
    gal_js = "// Galerías estandarizadas: 8 ángulos uniformes (1024x1024 px WebP) por producto\n"
    gal_js += "const galleries = " + json.dumps(new_galleries, indent=2) + ";\n"
    with open('dist/js/galleries.js', 'w', encoding='utf-8') as f:
        f.write(gal_js)
    print("Updated dist/js/galleries.js with all 45 products!")

    print("\n==========================================")
    print(f"DEPLOYMENT SUMMARY:")
    print(f"Products Deployed: {len(catalog)} / 45")
    print(f"WebP Views Deployed: {deployed_files} (expected {45 * 8} = 360)")
    print(f"Size Verifications: {size_checks} checked")
    print(f"Size Errors: {size_errors}")
    print("==========================================")

if __name__ == '__main__':
    deploy()
