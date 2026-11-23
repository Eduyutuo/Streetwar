import os, glob, json, re
from PIL import Image

with open('dist/js/flow_nanobanana_data.js', 'r', encoding='utf-8') as f:
    data = json.loads(re.search(r'const flowNanobananaData = ({.*?});\s*$', f.read(), re.DOTALL).group(1))

catalog = data['catalog']

already_done = [d for d in glob.glob('output_catalog/*/*') if len(os.listdir(d)) >= 16]
already_done_skus = set(os.path.basename(d) for d in already_done)
print(f"Already done SKUs ({len(already_done_skus)}):", already_done_skus)

remaining = [item for item in catalog if item['sku'] not in already_done_skus]
print(f"Remaining SKUs to generate: {len(remaining)}")

for item in remaining[:5]:
    sku = item['sku']
    raw_p = os.path.join('dist/assets/1-orig-raw', sku)
    std_p = os.path.join('dist/assets/2-norm-std', sku)
    raw_files = sorted(os.listdir(raw_p)) if os.path.exists(raw_p) else []
    std_files = sorted(os.listdir(std_p)) if os.path.exists(std_p) else []
    print(f"\nSKU {sku} ({item['group']}):")
    print(f"  raw ({len(raw_files)}): {raw_files}")
    print(f"  std ({len(std_files)}): {std_files}")
