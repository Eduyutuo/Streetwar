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
    
    # 1. JSON 2x2 (Lienzo 1:1)
    j_2x2 = {
        "task": "commercial_footwear_catalog_quad_sheet",
        "product": {
            "name": name,
            "sku": sku,
            "authentic": True
        },
        "layout": {
            "type": "2x2_grid_contact_sheet",
            "aspect_ratio": "1:1",
            "background_color": "#FFFFFF",
            "panels": {
                "top_left": "90-degree lateral outer profile, toe pointing LEFT",
                "top_right": "45-degree 3/4 perspective front-quarter, facing LEFT",
                "bottom_left": "180-degree direct rear heel counter, centered",
                "bottom_right": "90-degree overhead top-down flat lay view, laces and tongue"
            }
        },
        "lighting": "neutral_softbox_5500k_studio",
        "camera": "85mm_lens_f8_sharp_focus",
        "output": "razor_sharp_focus_pure_white_background_subtle_contact_shadow"
    }

    # 2. JSON 1x3 (Lienzo 16:9 / 4:3)
    j_1x3 = {
        "style": "professional_sneaker_catalog",
        "shoe": name,
        "sku": sku,
        "composition": "horizontal_triptych_three_equal_panels",
        "aspect_ratio": "16:9_or_4:3",
        "background": "seamless_solid_pure_white_#FFFFFF",
        "views_left_to_right": [
            "Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT",
            "Panel 2: direct 180-degree rear heel branding badge centered",
            "Panel 3: direct 90-degree overhead top-down view showing laces and tongue"
        ],
        "render_quality": "8k_resolution_sharp_textures_dual_softbox_lighting"
    }

    # 3. TEXTO 2x2 (Lienzo 1:1)
    t_2x2 = (
        f"Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker {name}, SKU: {sku}. "
        f"Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). "
        f"Top-left panel: strict 90-degree lateral outer profile pointing LEFT. "
        f"Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. "
        f"Bottom-left panel: direct 180-degree rear heel view centered. "
        f"Bottom-right panel: direct 90-degree overhead top-down flat lay view. "
        f"Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, "
        f"razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
    )

    # 4. TEXTO 1x3 (Lienzo 16:9)
    t_1x3 = (
        f"Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker {name}, SKU: {sku} "
        f"on a pure solid white background (#FFFFFF). "
        f"Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. "
        f"Panel 2 (center): direct 180-degree rear heel counter view with branding badge. "
        f"Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. "
        f"Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
    )

    # 5. NEGATIVE PROMPT COMÚN
    neg_prompt = (
        "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, "
        "colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, "
        "dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
    )

    catalog_data.append({
        "index": idx,
        "sku": sku,
        "name": name,
        "primary_ref": f"assets/2-norm-std/{sku}/01-lateral.webp",
        "formats": {
            "json_2x2": {
                "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
                "ratio": "1:1",
                "tag": "JSON • 1:1 Cuadrado",
                "layout": "2x2",
                "angles_count": 4,
                "split_cmd": f'python scripts/split_grid_angles.py "imagen_descargada.png" --sku {sku} --layout 2x2',
                "prompt": json.dumps(j_2x2, indent=2)
            },
            "json_1x3": {
                "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
                "ratio": "16:9 o 4:3",
                "tag": "JSON • 16:9 / 4:3 Horizontal",
                "layout": "1x3",
                "angles_count": 3,
                "split_cmd": f'python scripts/split_grid_angles.py "imagen_descargada.png" --sku {sku} --layout 1x3',
                "prompt": json.dumps(j_1x3, indent=2)
            },
            "text_2x2": {
                "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
                "ratio": "1:1",
                "tag": "Texto • 1:1 Cuadrado",
                "layout": "2x2",
                "angles_count": 4,
                "split_cmd": f'python scripts/split_grid_angles.py "imagen_descargada.png" --sku {sku} --layout 2x2',
                "prompt": t_2x2
            },
            "text_1x3": {
                "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
                "ratio": "16:9",
                "tag": "Texto • 16:9 Horizontal",
                "layout": "1x3",
                "angles_count": 3,
                "split_cmd": f'python scripts/split_grid_angles.py "imagen_descargada.png" --sku {sku} --layout 1x3',
                "prompt": t_1x3
            }
        },
        "negative_prompt": neg_prompt
    })

# Exportar JS
js_content = "const nanoBananaCatalog = " + json.dumps(catalog_data, indent=2, ensure_ascii=False) + ";\n"
with open('dist/js/nanobanana_prompts.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Exportado con éxito: dist/js/nanobanana_prompts.js con {len(catalog_data)} productos")
