import os

p_dir = os.path.join('dist', 'assets', 'productos')
exact_8 = {
    '01-lateral.webp',
    '02-medial.webp',
    '03-3-4-front.webp',
    '04-3-4-rear.webp',
    '05-front.webp',
    '06-rear.webp',
    '07-top-down.webp',
    '08-outsole.webp'
}

deleted_count = 0
kept_count = 0

for folder in sorted(os.listdir(p_dir)):
    fpath = os.path.join(p_dir, folder)
    if not os.path.isdir(fpath):
        continue
    
    files = os.listdir(fpath)
    for f in files:
        fp = os.path.join(fpath, f)
        if f not in exact_8:
            os.remove(fp)
            deleted_count += 1
        else:
            kept_count += 1

print(f'Done! Deleted {deleted_count} non-canonical files across all product folders.')
print(f'Total canonical files remaining: {kept_count} (Expected: 45 x 8 = 360)')
