import json
import os
import re

with open('dist/js/assigned_angles.json', 'r', encoding='utf-8') as f:
    assigned = json.load(f)

def clean_name(name):
    c = name.replace('“', '"').replace('”', '"').replace('’', "'")
    c = c.replace('Spam Jam', 'Space Jam')
    return c.strip()

def normalize_sku(sku_str):
    return re.sub(r'[\s_]+', '-', str(sku_str).strip().upper())

catalog_data = []
REF_IMAGE_NAME = 'Air Jordan 9 Retro OG "Space Jam"'

for item in assigned:
    idx = item['index']
    sku = normalize_sku(item['sku'])
    name = clean_name(item['name'])
    
    # 1. TEXTO PLANO REFERENCIANDO LA IMAGEN FIJA
    prompt_text = (
        f'Commercial e-commerce studio contact sheet grid showing exactly 8 distinct clean photographic panels of the authentic sneaker {name}, SKU: {sku}. '
        f'Matching the exact 4-row by 2-column layout and camera angles of reference image "{REF_IMAGE_NAME}". '
        f'Master generation in 4K resolution (1:1 aspect ratio), divided by thin 1px dark-gray divider lines on a seamless pure white #FFFFFF background, with generous uniform white margins in each cell ensuring the sneaker never touches borders or labels. Upper-left corner of each cell displays discrete technical label: '
        f'Row 1: [01 | LATERAL: 90-degree lateral outer profile, toe pointing LEFT], [02 | MEDIAL: 90-degree medial inner profile, toe pointing RIGHT]. '
        f'Row 2: [03 | 3/4 FRONT: 45-degree three-quarter front perspective, toe pointing bottom-LEFT], [04 | 3/4 REAR: 135-degree three-quarter rear perspective, heel on left and toe pointing RIGHT]. '
        f'Row 3: [05 | FRONT: pair side-by-side (left shoe direct front eye-level view, right shoe direct rear heel view), centered], [06 | REAR: pair side-by-side (dual direct rear heel views showing both heel counters), centered]. '
        f'Row 4: [07 | TOP-DOWN: horizontal direct overhead top-down flat lay view, heel on left and toe pointing RIGHT], [08 | OUTSOLE: horizontal direct bottom outsole rubber tread view, heel on left and toe pointing RIGHT]. '
        f'Identical sneaker colorway and materials across all 8 panels, seamless solid pure white background (#FFFFFF), '
        f'balanced softbox studio lighting at 5500K neutral daylight, subtle grounded floor contact shadows, razor-sharp edge-to-edge f/8 focus, master 4K resolution e-commerce standard.'
    )

    # 2. JSON OPTIMIZADO Y PERFECCIONADO
    prompt_json = {
        "task": "commercial_footwear_catalog_contact_sheet_8_panels",
        "master_resolution": "4K_uhd_1_to_1_aspect_ratio",
        "reference_composition_image": REF_IMAGE_NAME,
        "product": {
            "name": name,
            "sku": sku,
            "authentic": True
        },
        "grid_layout": {
            "total_panels": 8,
            "distribution": "4_rows_by_2_columns",
            "aspect_ratio": "1:1",
            "reference_match": f"replicate_exact_grid_and_angles_from_{REF_IMAGE_NAME}",
            "background": "#FFFFFF",
            "dividers": "thin_1px_dark_gray_divider_lines",
            "cell_margins": "generous_uniform_white_padding_zero_border_or_label_overlap",
            "labels": "discrete_uppercase_top_left_corner"
        },
        "panels_distribution": [
            {"row": 1, "col": 1, "label": "01 | LATERAL", "view": "90-degree lateral outer profile, toe pointing LEFT"},
            {"row": 1, "col": 2, "label": "02 | MEDIAL", "view": "90-degree medial inner profile, toe pointing RIGHT"},
            {"row": 2, "col": 1, "label": "03 | 3/4 FRONT", "view": "45-degree 3/4 perspective front-quarter facing bottom-LEFT"},
            {"row": 2, "col": 2, "label": "04 | 3/4 REAR", "view": "135-degree 3/4 rear perspective, heel on left and toe pointing RIGHT"},
            {"row": 3, "col": 1, "label": "05 | FRONT", "view": "pair side-by-side (left shoe direct front eye-level view, right shoe direct rear heel view), centered"},
            {"row": 3, "col": 2, "label": "06 | REAR", "view": "pair side-by-side (dual direct rear heel views showing both heel counters), centered"},
            {"row": 4, "col": 1, "label": "07 | TOP-DOWN", "view": "horizontal direct overhead top-down flat lay view, heel on left and toe pointing RIGHT"},
            {"row": 4, "col": 2, "label": "08 | OUTSOLE", "view": "horizontal direct bottom outsole rubber tread view, heel on left and toe pointing RIGHT"}
        ],
        "environment": {
            "lighting": "dual_softbox_5500k_neutral_daylight",
            "focus": "razor_sharp_edge_to_edge_f8",
            "floor_shadow": "subtle_grounded_contact_shadow",
            "quality": "master_4k_resolution_e_commerce_catalog_standard_zero_artifacts"
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
        "split_command": f'python scripts/split_grid_angles.py "{sku}.png" --sku {sku} --layout 4x2 --size 1024 --format webp'
    })

js_content = "const nanoBananaCatalog = " + json.dumps(catalog_data, indent=2, ensure_ascii=False) + ";\n"
with open('dist/js/nanobanana_prompts.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Exportado correctamente con referencia fija a {REF_IMAGE_NAME}: dist/js/nanobanana_prompts.js")
