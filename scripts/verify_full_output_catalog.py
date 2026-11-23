import os, glob
from PIL import Image

groups = sorted(os.listdir('output_catalog'))
total_skus = 0
total_webp = 0
total_png = 0
dimension_mismatches = 0
non_white_corners = 0

print("==========================================")
print("AUDITING OUTPUT CATALOG (45 MODELS)")
print("==========================================")

for g in groups:
    gp = os.path.join('output_catalog', g)
    if not os.path.isdir(gp):
        continue
    skus = sorted(os.listdir(gp))
    print(f"\n[{g}] ({len(skus)} SKUs):")
    for sku in skus:
        sp = os.path.join(gp, sku)
        files = os.listdir(sp)
        webps = [f for f in files if f.endswith('.webp')]
        pngs = [f for f in files if f.endswith('.png')]
        total_skus += 1
        total_webp += len(webps)
        total_png += len(pngs)
        
        # Test sample file: 01_lateral
        sample_fn = f"{sku}_01_lateral.webp"
        sample_path = os.path.join(sp, sample_fn)
        if os.path.exists(sample_path):
            with Image.open(sample_path) as im:
                if im.size != (1024, 1024):
                    dimension_mismatches += 1
                    print(f"  Warning {sku}: size is {im.size} != (1024, 1024)")
                # check top-left pixel
                rgb = im.convert('RGB')
                tl = rgb.getpixel((5, 5))
                if tl != (255, 255, 255):
                    non_white_corners += 1
                    print(f"  Warning {sku}: corner pixel is {tl} != (255, 255, 255)")
        else:
            print(f"  Missing {sample_fn} in {sku}!")

print("\n==========================================")
print(f"TOTAL SKUs VERIFIED: {total_skus}/45")
print(f"TOTAL WEBP FILES: {total_webp} (expected 360)")
print(f"TOTAL PNG FILES: {total_png} (expected 360)")
print(f"TOTAL IMAGES GENERATED: {total_webp + total_png} (expected 720)")
print(f"DIMENSION MISMATCHES: {dimension_mismatches}")
print(f"NON-WHITE CORNERS: {non_white_corners}")
print("==========================================")
