import os
from PIL import Image

skus = ['IO2076-100', 'IR1968-133', '323419-164', '553560-081', 'IM4026-100', 'AQ9214-012']

for sku in skus:
    raw_p = os.path.join('dist/assets/1-orig-raw', sku)
    files = sorted(os.listdir(raw_p))
    print(f"\nSKU {sku} has {len(files)} files:")
    for f in files:
        im = Image.open(os.path.join(raw_p, f))
        print(f"  {f}: size={im.size}, ratio={im.width/im.height:.2f}")
