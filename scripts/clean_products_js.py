import re

with open('dist/js/products.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    # Remove .png in initial inventory
    if i < 48:
        line = re.sub(r"image:'[^']*\.png'", "image:''", line)
    
    # Clean 511417-136 note
    if '511417-136' in line and 'Poner fondo blanco.' in line:
        line = line.replace('Poner fondo blanco.', '')
        
    # Skip legacy lines setting .png images
    if any(k in line for k in [
        'const cardPrimaryImages',
        'Object.entries(cardPrimaryImages)',
        'generated/product-',
        'air-max-correlate-1.png',
        'son-of-mars-1.png',
        'jordan-3-green-white-red'
    ]):
        continue
        
    new_lines.append(line)

with open('dist/js/products.js', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('dist/js/products.js successfully cleaned of PNG references!')
