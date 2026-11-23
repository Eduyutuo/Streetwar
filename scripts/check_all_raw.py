import os, json, re

with open('dist/js/flow_nanobanana_data.js', 'r', encoding='utf-8') as f:
    data = json.loads(re.search(r'const flowNanobananaData = ({.*?});\s*$', f.read(), re.DOTALL).group(1))

catalog = data['catalog']

print(f"{'SKU':<15} {'GROUP':<10} {'RAW_COUNT':<10} {'RAW_FILES'}")
print("-" * 80)
for item in catalog:
    sku = item['sku']
    raw_p = os.path.join('dist/assets/1-orig-raw', sku)
    if os.path.exists(raw_p):
        files = sorted(os.listdir(raw_p))
        print(f"{sku:<15} {item['group']:<10} {len(files):<10} {', '.join(files[:5])}{'...' if len(files) > 5 else ''}")
    else:
        print(f"{sku:<15} {item['group']:<10} NOT FOUND")
