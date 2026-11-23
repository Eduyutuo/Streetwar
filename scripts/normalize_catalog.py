import json
import re

with open('dist/js/assigned_angles.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

def clean_name(n):
    return n.replace('“', '"').replace('”', '"').replace('’', "'").replace('Spam Jam', 'Space Jam')

def norm_sku(s):
    return re.sub(r'[\s_]+', '-', str(s).strip().upper())

modified = 0
for it in items:
    raw = it.get('rawSku', it.get('sku', ''))
    norm = norm_sku(raw)
    cname = clean_name(it['name'])
    if norm != it.get('sku') or cname != it['name'] or 'rawSku' not in it:
        modified += 1
    it['rawSku'] = raw
    it['sku'] = norm
    it['name'] = cname

print(f"Items normalized: {modified} of {len(items)}")

with open('dist/js/assigned_angles.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

js_content = "const assignedAngles = " + json.dumps(items, indent=2, ensure_ascii=False) + ";\n"
with open('dist/js/assigned_angles.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updated dist/js/assigned_angles.json and dist/js/assigned_angles.js successfully.")
