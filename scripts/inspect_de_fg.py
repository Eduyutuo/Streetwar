import os

for f in ['_source_data/fotos_DE/Grupo D', '_source_data/fotos_DE/Grupo E', '_source_data/fotos_FG/Grupo F', '_source_data/fotos_FG/Grupo G']:
    if os.path.exists(f):
        print("===", f, "===")
        for d in sorted(os.listdir(f)):
            sub = os.path.join(f, d)
            if os.path.isdir(sub):
                print(f"  {d}:", sorted(os.listdir(sub)))
