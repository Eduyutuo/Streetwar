import os, glob

folders = []
for p in ['_source_data/fotos_ABC', '_source_data/fotos_DE', '_source_data/fotos_FG']:
    if os.path.exists(p):
        for root, dirs, files in os.walk(p):
            for d in dirs:
                if d.startswith(('01_', '02_', '03_', '04_', '05_', '06_', '07_')):
                    folders.append(os.path.join(root, d))

print(f"Total product folders found: {len(folders)}")
for folder in folders[:10]:
    flist = os.listdir(folder)
    print(f"\n{folder}:")
    print("  files:", flist)
