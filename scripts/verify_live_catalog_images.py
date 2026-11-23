import os
from PIL import Image

base_dir = 'dist/assets/productos'
folders = sorted(os.listdir(base_dir))
print(f"Total product folders in {base_dir}: {len(folders)}")

all_1024 = True
checked_count = 0

for folder in folders:
    fp = os.path.join(base_dir, folder)
    if not os.path.isdir(fp):
        continue
    files = [f for f in os.listdir(fp) if f.endswith('.webp')]
    for fn in ['01-lateral.webp', '02-medial.webp', '03-3-4-front.webp', '04-3-4-rear.webp', '05-front.webp', '06-rear.webp', '07-top-down.webp', '08-outsole.webp']:
        img_p = os.path.join(fp, fn)
        if not os.path.exists(img_p):
            print(f"Missing {fn} in {folder}")
            all_1024 = False
        else:
            with Image.open(img_p) as im:
                checked_count += 1
                if im.size != (1024, 1024):
                    print(f"BAD SIZE: {folder}/{fn} is {im.size}")
                    all_1024 = False

print(f"Total canonical WebP images verified in live catalog: {checked_count}")
print(f"Are all 1024x1024 px identical? {all_1024}")
