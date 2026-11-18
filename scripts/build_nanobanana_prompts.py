import json
import os

with open('dist/js/assigned_angles.json', 'r', encoding='utf-8') as f:
    assigned = json.load(f)

def clean_name(name):
    return name.replace('“', '"').replace('”', '"').replace('’', "'")

catalog_data = []

for item in assigned:
    idx = item['index']
    sku = item['sku']
    name = clean_name(item['name'])
    
    # 1. TEXTO PLANO CON REFERENCIA A LA IMAGEN MAESTRA DE GRID
    prompt_text = (
        f'Commercial e-commerce studio contact sheet grid showing exactly 8 distinct clean photographic panels of the authentic sneaker {name}, SKU: {sku}, '
        f'arranged in a neat 2-row by 4-column (or 4-row by 2-column) grid on a pure solid white background (#FFFFFF), identical composition and layout to reference image "Sneaker product grid studio display". '
        f'Row 1: [Panel 1: 90-degree lateral profile pointing LEFT], [Panel 2: 3/4 perspective front-quarter facing LEFT], [Panel 3: direct straight front view], [Panel 4: direct rear heel view]. '
        f'Row 2: [Panel 5: 3/4 rear perspective facing LEFT], [Panel 6: 90-degree medial inner side profile pointing LEFT], [Panel 7: direct overhead top-down view], [Panel 8: direct bottom outsole tread view]. '
        f'Identical sneaker colorway, identical softbox studio lighting, clean thin white gutters between panels. '
        f'Pure solid seamless white background (#FFFFFF). Uniform high-end commercial studio lighting, balanced softbox illumination at 5500K neutral daylight, razor-sharp focus across all angles, subtle grounded contact shadows on the floor. 8k resolution e-commerce product catalog standard, zero floating artifacts, zero background clutter.'
    )

    # 2. JSON CON REFERENCIA A LA IMAGEN MAESTRA
    prompt_json = {
        "task": "commercial_footwear_catalog_contact_sheet_8_panels",
        "reference_composition_image": "Sneaker product grid studio display",
        "product": {
            "name": name,
            "sku": sku,
            "authentic": True
        },
        "grid_layout": {
            "total_panels": 8,
            "distribution": "matching_reference_Sneaker_product_grid_studio_display",
            "background": "#FFFFFF",
            "gutters": "clean_thin_white_lines"
        },
        "row_1_panels": [
            {"panel_1": "90-degree lateral side profile pointing LEFT"},
            {"panel_2": "3/4 perspective front-quarter facing LEFT"},
            {"panel_3": "direct straight front eye-level view"},
            {"panel_4": "direct rear heel counter view"}
        ],
        "row_2_panels": [
            {"panel_5": "3/4 rear perspective facing LEFT"},
            {"panel_6": "90-degree medial inner side profile pointing LEFT"},
            {"panel_7": "direct overhead top-down flat lay view"},
            {"panel_8": "direct bottom outsole tread view"}
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
        "grid_ref_image": "assets/sneaker-product-grid-studio-display.jpg",
        "grid_ref_name": "Sneaker product grid studio display",
        "prompt_text": prompt_text,
        "prompt_json": json.dumps(prompt_json, indent=2),
        "split_command": f'python scripts/split_grid_angles.py "tu_imagen.jpg" --sku {sku} --layout 4x2'
    })

js_content = "const nanoBananaCatalog = " + json.dumps(catalog_data, indent=2, ensure_ascii=False) + ";\n"
with open('dist/js/nanobanana_prompts.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Exportado con referencia Sneaker product grid studio display: dist/js/nanobanana_prompts.js")
