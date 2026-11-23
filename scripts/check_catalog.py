import json

with open('dist/js/assigned_angles.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, d in enumerate(data):
    print(f"{i:02d}: sku={d.get('sku')} | folder={d.get('folder')} | name={d.get('name')}")
