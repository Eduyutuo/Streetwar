import os, glob

dirs = glob.glob('_source_data/**/01_*', recursive=True)
print("Sample product dirs in _source_data:", dirs[:5])
if dirs:
    for f in os.listdir(dirs[0])[:6]:
        print(" ", f)
