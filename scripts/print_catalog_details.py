import json, re

with open('dist/js/flow_nanobanana_data.js', 'r', encoding='utf-8') as f:
    data = json.loads(re.search(r'const flowNanobananaData = ({.*?});\s*$', f.read(), re.DOTALL).group(1))

catalog = data['catalog']
for i, item in enumerate(catalog):
    print(f"{i+1:02d}. SKU: {item['sku']:<15} Group: {item['group']:<10} Folder: {str(item.get('folderOrigin')):<25} RawSKU: {str(item.get('rawSku'))}")
