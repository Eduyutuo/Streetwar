import os, glob, json, re
from PIL import Image
import numpy as np

with open('dist/js/flow_nanobanana_data.js', 'r', encoding='utf-8') as f:
    data = json.loads(re.search(r'const flowNanobananaData = ({.*?});\s*$', f.read(), re.DOTALL).group(1))

catalog = data['catalog']
already_done = [d for d in glob.glob('output_catalog/*/*') if len(os.listdir(d)) >= 16]
already_done_skus = set(os.path.basename(d) for d in already_done)

remaining = [item for item in catalog if item['sku'] not in already_done_skus]
print(f"Total remaining SKUs: {len(remaining)}")

for item in remaining:
    sku = item['sku']
    raw_p = os.path.join('dist/assets/1-orig-raw', sku)
    if not os.path.exists(raw_p):
        print(f"SKU {sku} has no 1-orig-raw dir")
        continue
    files = sorted(os.listdir(raw_p))
    print(f"\n[{item['group']}] {sku} ({len(files)} files):")
    for f in files:
        fp = os.path.join(raw_p, f)
        try:
            im = Image.open(fp)
            print(f"   {f:<25} {im.size} {im.format}")
        except Exception as e:
            print(f"   {f:<25} ERROR: {e}")
