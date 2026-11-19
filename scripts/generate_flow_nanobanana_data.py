import os
import json
import re
from PIL import Image, ImageOps
from concurrent.futures import ThreadPoolExecutor

base = '_source_data'
top_folders = [
    ('fotos_ABC', ['Grupo A', 'Grupo B', 'Grupo C']),
    ('fotos_DE', ['Grupo D', 'Grupo E']),
    ('fotos_FG', ['Grupo F', 'Grupo G'])
]

with open('dist/js/assigned_angles.json', 'r', encoding='utf-8') as f:
    assigned = json.load(f)

def clean_name(name):
    return name.replace('“', '"').replace('”', '"').replace('’', "'")

def sanitize_filename(filename):
    name, _ = os.path.splitext(filename)
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)

# Tareas para generar previews optimizados de las fotos reales
tasks = []
catalog = []
sku_idx = 0

REF_MASTER = 'Air Jordan 9 Retro OG "Space Jam"'

for top, groups in top_folders:
    for g in groups:
        g_path = os.path.join(base, top, g)
        if os.path.exists(g_path):
            prod_dirs = sorted([d for d in os.listdir(g_path) if os.path.isdir(os.path.join(g_path, d))])
            for pdir in prod_dirs:
                pdir_full = os.path.join(g_path, pdir)
                files = sorted([f for f in os.listdir(pdir_full) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))])
                
                matched = assigned[sku_idx] if sku_idx < len(assigned) else None
                sku = matched['sku'] if matched else f"SKU-{sku_idx}"
                name = clean_name(matched['name'] if matched else pdir)
                
                img_count = len(files)
                
                # Previews locales reales dentro de dist/assets/source-previews/{sku}
                sku_preview_dir = os.path.join('dist', 'assets', 'source-previews', sku)
                os.makedirs(sku_preview_dir, exist_ok=True)
                
                real_photos = []
                for i, f in enumerate(files):
                    clean_fn = sanitize_filename(f)
                    webp_name = f"{i+1:02d}_{clean_fn}.webp"
                    dst_path = os.path.join(sku_preview_dir, webp_name)
                    src_path = os.path.join(pdir_full, f)
                    rel_web_path = f"assets/source-previews/{sku}/{webp_name}"
                    real_photos.append(rel_web_path)
                    tasks.append((src_path, dst_path))
                
                preview_primary = real_photos[0] if real_photos else f"assets/2-norm-std/{sku}/01-lateral.webp"
                
                # Generar prompt de texto adaptativo
                prompt_text = (
                    f'Commercial e-commerce studio contact sheet grid showing exactly 8 distinct clean photographic panels of the authentic sneaker {name}, SKU: {sku}. '
                    f'Synthesized from the {img_count} input reference photos provided, matching the exact 4-row by 2-column layout and camera angles of reference image "{REF_MASTER}". '
                    f'Row 1: [01 | LATERAL: 90-degree lateral profile pointing LEFT], [02 | MEDIAL: 90-degree medial inner side profile pointing LEFT]. '
                    f'Row 2: [03 | 3/4 FRONT: three-quarter perspective front-quarter facing LEFT], [04 | 3/4 REAR: three-quarter rear perspective facing LEFT]. '
                    f'Row 3: [05 | FRONT: direct straight front eye-level view], [06 | REAR: direct rear heel counter view]. '
                    f'Row 4: [07 | TOP-DOWN: direct overhead flat lay view], [08 | OUTSOLE: direct bottom outsole tread view]. '
                    f'Synthesize the 3D geometry seamlessly using all {img_count} multi-angle reference photos to reconstruct complete 360-degree colorway and textures. '
                    f'Pure solid seamless white background (#FFFFFF). Uniform high-end commercial studio lighting, balanced softbox illumination at 5500K neutral daylight, '
                    f'razor-sharp focus across all 8 panels, subtle grounded floor contact shadows, zero floating artifacts, 8k resolution e-commerce product catalog standard.'
                )
                
                # Generar JSON adaptativo
                prompt_json = {
                    "task": "commercial_footwear_catalog_contact_sheet_8_panels",
                    "reference_composition_image": REF_MASTER,
                    "multi_view_reference_inputs": {
                        "source_photos_count": img_count,
                        "description": f"Use all {img_count} uploaded reference photos to reconstruct 360-degree materials, colorway, and logos",
                        "folder_origin": f"{top}/{g}/{pdir}"
                    },
                    "product": {
                        "name": name,
                        "sku": sku,
                        "authentic": True
                    },
                    "grid_layout": {
                        "total_panels": 8,
                        "distribution": "4_rows_by_2_columns",
                        "reference_match": f"replicate_exact_grid_and_angles_from_{REF_MASTER}",
                        "background": "#FFFFFF",
                        "gutters": "clean_thin_white_lines"
                    },
                    "panels_distribution": [
                        {"row": 1, "col": 1, "label": "01 | LATERAL", "view": "90-degree lateral outer profile pointing LEFT"},
                        {"row": 1, "col": 2, "label": "02 | MEDIAL", "view": "90-degree medial inner side profile pointing LEFT"},
                        {"row": 2, "col": 1, "label": "03 | 3/4 FRONT", "view": "45-degree 3/4 perspective front-quarter facing LEFT"},
                        {"row": 2, "col": 2, "label": "04 | 3/4 REAR", "view": "135-degree 3/4 rear perspective facing LEFT"},
                        {"row": 3, "col": 1, "label": "05 | FRONT", "view": "direct straight front eye-level view centered"},
                        {"row": 3, "col": 2, "label": "06 | REAR", "view": "direct rear heel counter view centered"},
                        {"row": 4, "col": 1, "label": "07 | TOP-DOWN", "view": "direct overhead top-down flat lay view"},
                        {"row": 4, "col": 2, "label": "08 | OUTSOLE", "view": "direct bottom outsole rubber tread view"}
                    ],
                    "environment": {
                        "lighting": "dual_softbox_5500k_neutral_daylight",
                        "focus": "razor_sharp_edge_to_edge_f8",
                        "floor_shadow": "subtle_grounded_contact_shadow",
                        "quality": "8k_resolution_e_commerce_catalog_standard_zero_artifacts"
                    }
                }
                
                catalog.append({
                    "index": sku_idx,
                    "sku": sku,
                    "name": name,
                    "top_folder": top,
                    "group": g,
                    "prod_dir": pdir,
                    "full_disk_path": f"C:/Users/eduar/Documents/CATALOGO/_source_data/{top}/{g}/{pdir}",
                    "image_count": img_count,
                    "image_files": files,
                    "preview_primary": preview_primary,
                    "real_photos": real_photos,
                    "ref_master_image": "assets/Air Jordan 9 Retro OG Space Jam.jpg",
                    "ref_master_name": REF_MASTER,
                    "prompt_text": prompt_text,
                    "prompt_json": json.dumps(prompt_json, indent=2),
                    "split_command": f'python scripts/split_grid_angles.py "tu_imagen.jpg" --sku {sku} --layout 4x2'
                })
                
                sku_idx += 1

# Procesar imágenes en paralelo
def convert_worker(item):
    src, dst = item
    if os.path.exists(dst):
        return
    try:
        with Image.open(src) as im:
            im = ImageOps.exif_transpose(im)
            im.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
            im.save(dst, 'WEBP', quality=85)
    except Exception as e:
        print(f"Error procesando {src}: {e}")

print(f"Generando {len(tasks)} previews de fotos reales desde _source_data...")
with ThreadPoolExecutor(max_workers=8) as ex:
    list(ex.map(convert_worker, tasks))

# Guardar JS
js_content = "const flowNanobananaData = " + json.dumps({
    "total_products": len(catalog),
    "ref_master": REF_MASTER,
    "catalog": catalog
}, indent=2, ensure_ascii=False) + ";\n"

with open('dist/js/flow_nanobanana_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Generado dist/js/flow_nanobanana_data.js con {len(catalog)} productos y {len(tasks)} fotos reales de inventario.")
