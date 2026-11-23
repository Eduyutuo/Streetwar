import os
from PIL import Image

def describe_sku(sku):
    raw_p = os.path.join('dist/assets/1-orig-raw', sku)
    files = sorted(os.listdir(raw_p))
    print(f"=== {sku} ===")
    for f in files:
        im = Image.open(os.path.join(raw_p, f))
        print(f"  {f}: size={im.size}")

describe_sku('IO2076-100')
describe_sku('323419-164')
describe_sku('AR4430-101')
