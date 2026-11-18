import json
import os

with open('dist/js/assigned_angles.json', 'r', encoding='utf-8') as f:
    assigned = json.load(f)

def clean_name(name):
    return name.replace('“', '"').replace('”', '"').replace('’', "'")

catalog_data = []

REF_IMAGE_NAME = 'Air Jordan 9 Retro OG "Space Jam"'

for item in assigned:
    idx = item['index']
    sku = item['sku']
    name = clean_name(item['name'])
    
    # 1. TEXTO PLANO REFERENCIANDO LA IMAGEN FIJA
    prompt_text = (
        f'Commercial e-commerce studio contact sheet grid showing exactly 8 distinct clean photographic panels of the authentic sneaker {name}, SKU: {sku}, '
        f'matching the exact 4-row by 2-column layout and camera angles of reference image "{REF_IMAGE_NAME}". '
        f'Row 1: [01 | LATERAL: 90-degree lateral profile pointing LEFT], [02 | MEDIAL: 90-degree medial inner side profile pointing LEFT]. '
        f'Row 2: [03 | 3/4 FRONT: three-quarter perspective front-quarter facing LEFT], [04 | 3/4 REAR: three-quarter rear perspective facing LEFT]. '
        f'Row 3: [05 | FRONT: direct straight front eye-level view], [06 | REAR: direct rear heel counter view]. '
        f'Row 4: [07 | TOP-DOWN: direct overhead flat lay view], [08 | OUTSOLE: direct bottom outsole tread view]. '
        f'Identical sneaker colorway and materials across all 8 panels, seamless solid pure white background (#FFFFFF), '
        f'balanced softbox studio lighting at 5500K, subtle grounded floor contact shadows, razor-sharp edge-to-edge focus, 8k resolution e-commerce standard.'
    )

    # 2. JSON OPTIMIZADO Y PERFECCIONADO
    prompt_json = {
        "task": "commercial_footwear_catalog_contact_sheet_8_panels",
        "reference_composition_image": REF_IMAGE_NAME,
        "product": {
            "name": name,
            "sku": sku,
            "authentic": True
        },
        "grid_layout": {
            "total_panels": 8,
            "distribution": "4_rows_by_2_columns",
            "reference_match": f"replicate_exact_grid_and_angles_from_{REF_IMAGE_NAME}",
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
            {"row": 4, "col": 1, "label": "07 | TOP-DOWN", "view": "direct overhead top-down flat lay view, toe pointing left/up"},
            {"row": 4, "col": 2, "label": "08 | OUTSOLE", "view": "direct bottom outsole rubber tread view"}
        ],
        "environment": {
            "lighting": "dual_softbox_5500k_neutral_daylight",
            "focus": "razor_sharp_edge_to_edge_f8",
            "floor_shadow": "subtle_grounded_contact_shadow",
            "quality": "8k_resolution_e_commerce_catalog_standard_zero_artifacts"
        }
    }

    catalog_data.append({
        "index": idx,
        "sku": sku,
        "name": name,
        "primary_ref": f"assets/2-norm-std/{sku}/01-lateral.webp",
        "grid_ref_image": "assets/Air Jordan 9 Retro OG Space Jam.jpg",
        "grid_ref_name": REF_IMAGE_NAME,
        "prompt_text": prompt_text,
        "prompt_json": json.dumps(prompt_json, indent=2),
        "split_command": f'python scripts/split_grid_angles.py "tu_imagen.jpg" --sku {sku} --layout 4x2'
    })

js_content = "const nanoBananaCatalog = " + json.dumps(catalog_data, indent=2, ensure_ascii=False) + ";\n"
with open('dist/js/nanobanana_prompts.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Exportado correctamente con referencia fija a {REF_IMAGE_NAME}: dist/js/nanobanana_prompts.js")
