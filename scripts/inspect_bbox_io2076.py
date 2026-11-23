import os, numpy as np
from PIL import Image

def analyze_img(path):
    im = Image.open(path).convert('RGB')
    arr = np.array(im)
    # find non-white bbox
    mask = np.any(arr < 240, axis=2)
    if not np.any(mask):
        return "empty"
    y_idx, x_idx = np.where(mask)
    ymin, ymax = y_idx.min(), y_idx.max()
    xmin, xmax = x_idx.min(), x_idx.max()
    w = xmax - xmin
    h = ymax - ymin
    aspect = w / h
    return f"bbox aspect {aspect:.2f} (w={w}, h={h})"

for i in range(1, 9):
    fn = f"official-{i:02d}.jpg"
    p = os.path.join("dist/assets/1-orig-raw/IO2076-100", fn)
    print(fn, analyze_img(p))
