import os
import shutil
import json
import re
from PIL import Image

CANONICAL_ANGLES = [
    ('01_lateral', '01-lateral.webp'),
    ('02_medial', '02-medial.webp'),
    ('03_3-4_front', '03-3-4-front.webp'),
    ('04_3-4_rear', '04-3-4-rear.webp'),
    ('05_front', '05-front.webp'),
    ('06_rear', '06-rear.webp'),
    ('07_top_down', '07-top-down.webp'),
    ('08_outsole', '08-outsole.webp')
]

# Verified filename overrides for folders in output_catalog whose filenames
# do not follow the standard "{product_dir}_{angle}.{ext}" pattern.
ANGLE_OVERRIDES = {
    'IR0519-101': {
        '07_top_down': 'Sneaker_product_photography_stud\u2026_e3c039a3.jpg',
    },
    'IR1968-133': {
        '04_3-4_rear': '03_Nike_Air_Force_1_WNBA_08_outsole.jpg',
        '07_top_down': '03_Nike_Air_Force_1_WNBA_04_3-4_rear .jpg',
        '08_outsole': '03_Nike_Air_Force_1_WNBA_08_outsole.webp',
    },
    'CT3839-100': {
        '04_3-4_rear': 'Sneaker_product_photograph_in_st\u2026_a08552df.jpg',
    },
    'II0599-600': {
        '04_3-4_rear': 'Sneaker_product_photography_stud\u2026_c54669af.jpg',
    },
}


def resolve_angle_source(src_dir, sku, product_dir, angle_code):
    """Resolve the best matching image file in output_catalog for an angle."""
    override_fn = ANGLE_OVERRIDES.get(sku, {}).get(angle_code)
    if override_fn:
        override_path = os.path.join(src_dir, override_fn)
        if os.path.exists(override_path):
            return override_path

    if not os.path.isdir(src_dir):
        return None

    files = os.listdir(src_dir)
    prefix = f"{product_dir}_{angle_code}"
    matches = [fn for fn in files if fn.startswith(prefix)]
    if not matches:
        return None

    # Prefer newer .jpg/.jpeg studio renders over older .webp when both exist.
    matches.sort(key=lambda fn: (0 if fn.lower().endswith(('.jpg', '.jpeg')) else 1, fn))
    return os.path.join(src_dir, matches[0])


def safe_copy(src_file, dst_file):
    """Copy file atomically via a temporary sibling to avoid Windows lock errors."""
    tmp_file = dst_file + '.tmp'
    shutil.copyfile(src_file, tmp_file)
    os.replace(tmp_file, dst_file)


def write_webp(src_file, dst_file, target_size=(1024, 1024)):
    """Copy WebP directly or convert JPG/PNG to standardized WebP."""
    with Image.open(src_file) as im:
        size_ok = im.size == target_size
        if src_file.lower().endswith('.webp'):
            safe_copy(src_file, dst_file)
        else:
            tmp_file = dst_file + '.tmp'
            im.convert('RGB').save(tmp_file, 'WEBP', quality=92, method=6)
            os.replace(tmp_file, dst_file)
        return im.size, size_ok


def deploy():
    with open('dist/js/flow_nanobanana_data.js', 'r', encoding='utf-8') as f:
        data = json.loads(re.search(r'const flowNanobananaData = ({.*?});\s*$', f.read(), re.DOTALL).group(1))

    catalog = data['catalog']
    print(f"Deploying images from output_catalog (Grupo A..G) for {len(catalog)} products...")

    target_size = (1024, 1024)
    deployed_files = 0
    size_checks = 0
    size_errors = 0

    source_link_photos = {}
    new_galleries = {}

    for i, item in enumerate(catalog):
        sku = item['sku']
        group = item['group']
        product_dir = item['product_dir']
        src_dir = os.path.join('output_catalog', group, product_dir)
        dst_dir = os.path.join('dist', 'assets', 'productos', sku)
        norm_dir = os.path.join('dist', 'assets', '2-norm-std', sku)

        # Reset dst_dir so it only holds the canonical .webp angles (no old or duplicate files)
        if os.path.isdir(dst_dir):
            shutil.rmtree(dst_dir)
        os.makedirs(dst_dir, exist_ok=True)
        os.makedirs(norm_dir, exist_ok=True)

        product_photo_list = []

        for code, standard_fn in CANONICAL_ANGLES:
            src_file = resolve_angle_source(src_dir, sku, product_dir, code)
            if not src_file:
                print(f"INFO: No {code} for {sku} ({group}/{product_dir})")
                continue

            dst_standard = os.path.join(dst_dir, standard_fn)
            im_size, size_ok = write_webp(src_file, dst_standard, target_size)
            size_checks += 1
            if not size_ok:
                print(f"ERROR: Image {src_file} size {im_size} != {target_size}!")
                size_errors += 1

            # Keep norm_dir synced for comparador-rutas.html
            safe_copy(dst_standard, os.path.join(norm_dir, standard_fn))
            if code == '03_3-4_front':
                safe_copy(dst_standard, os.path.join(norm_dir, '02-frontal-3-4.webp'))
            elif code == '06_rear':
                safe_copy(dst_standard, os.path.join(norm_dir, '03-trasera.webp'))
            elif code == '07_top_down':
                safe_copy(dst_standard, os.path.join(norm_dir, '04-superior.webp'))

            product_photo_list.append(f"productos/{sku}/{standard_fn}")
            deployed_files += 1

        source_link_photos[str(i)] = product_photo_list
        new_galleries[str(i)] = product_photo_list

    slp_js = "// Catálogo desde output_catalog (Grupo A..G): ángulos estandarizados 1024x1024 px WebP\n"
    slp_js += "const sourceLinkPhotos = " + json.dumps(source_link_photos, indent=2) + ";\n"
    with open('dist/js/source-link-photos.js', 'w', encoding='utf-8') as f:
        f.write(slp_js)
    print("Updated dist/js/source-link-photos.js!")

    gal_js = "// Galerías desde output_catalog (Grupo A..G): ángulos estandarizados 1024x1024 px WebP\n"
    gal_js += "const galleries = " + json.dumps(new_galleries, indent=2) + ";\n"
    with open('dist/js/galleries.js', 'w', encoding='utf-8') as f:
        f.write(gal_js)
    print("Updated dist/js/galleries.js!")

    print("\n==========================================")
    print("DEPLOYMENT SUMMARY:")
    print(f"Products Deployed: {len(catalog)} / 45")
    print(f"WebP Views Deployed: {deployed_files}")
    print(f"Size Verifications: {size_checks} checked")
    print(f"Size Errors: {size_errors}")
    print("==========================================")


if __name__ == '__main__':
    deploy()
