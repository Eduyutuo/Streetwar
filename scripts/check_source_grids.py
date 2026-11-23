import os, glob, json, re

with open('dist/js/flow_nanobanana_data.js', 'r', encoding='utf-8') as f:
    data = json.loads(re.search(r'const flowNanobananaData = ({.*?});\s*$', f.read(), re.DOTALL).group(1))

catalog = data['catalog']

# Also check if there are grid files in _source_data
grid_files = glob.glob('_source_data/**/resultado*.*', recursive=True) + glob.glob('_source_data/**/*cuadricula*.*', recursive=True) + glob.glob('_source_data/**/*grid*.*', recursive=True) + glob.glob('**/*grid*.png', recursive=True)
print(f"Found grid files: {len(grid_files)}")
for g in grid_files[:10]:
    print("  ", g)
