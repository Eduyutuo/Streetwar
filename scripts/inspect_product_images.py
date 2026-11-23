import json
import os

with open('dist/js/flow_nanobanana_data.js', 'r', encoding='utf-8') as f:
    c = f.read().strip()[len('const flowNanobananaData = '):]
    if c.endswith(';'): c = c[:-1]
    data = json.loads(c)

catalog = data['catalog']
for p in catalog:
    p_path = p['full_disk_path']
    fls = sorted([f for f in os.listdir(p_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))])
    print(f"{p['sku']:<12} | {p['group']:<8} | {len(fls)} files: {fls}")
