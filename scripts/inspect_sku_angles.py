import os
from PIL import Image

sku = "IO2076-100"
raw_p = os.path.join("dist/assets/1-orig-raw", sku)
for f in sorted(os.listdir(raw_p)):
    p = os.path.join(raw_p, f)
    im = Image.open(p)
    print(f, im.size, im.mode)
