"""
Generador Maestro de Prompts para Flow / Nano Banana 2.1
Soporta:
- Tomas individuales (6 u 8 ángulos canónicos)
- Hojas de contacto / Grids combinados (Grid 2x3 de 6 tomas o Grid 2x4 de 8 tomas)
- Hojas en pares (1x2) o tríos (1x3)
"""

import json
import os

# 8 Ángulos canónicos organizados lógicamente
ANGLES_8 = [
    {
        "slot": 1,
        "code": "01-lateral-exterior",
        "name": "Perfil Lateral Exterior (90°)",
        "grid_pos": "Fila 1, Columna 1 (Top-Left)",
        "prompt_desc": "Panel 1: Strict 90-degree lateral side profile view, toe box pointing horizontally directly to the LEFT.",
        "details": "Clear exterior brand Swoosh/Jumpman logo, upper stitch lines, full midsole and outsole profile."
    },
    {
        "slot": 2,
        "code": "02-frontal-3-4",
        "name": "Perspectiva 3/4 Frontal (45°)",
        "grid_pos": "Fila 1, Columna 2 (Top-Center)",
        "prompt_desc": "Panel 2: Three-quarter (3/4) perspective front-quarter view, angled toward the LEFT.",
        "details": "Showing front toe box volume, lacing eyestay curvature, and outer lateral panel simultaneously."
    },
    {
        "slot": 3,
        "code": "03-frontal-directa",
        "name": "Frontal Directa (0°)",
        "grid_pos": "Fila 1, Columna 3",
        "prompt_desc": "Panel 3: Direct straight-on front eye-level view at 0 degrees, perfectly centered.",
        "details": "Symmetrical rounded toe cap, neat lace rows, and tongue brand label."
    },
    {
        "slot": 4,
        "code": "04-posterior-talon",
        "name": "Posterior / Talón (180°)",
        "grid_pos": "Fila 1, Columna 4 o Fila 2",
        "prompt_desc": "Panel 4: Direct 180-degree rear heel view from behind, centered and vertical.",
        "details": "Authentic heel counter branding badge (Nike Air / Jumpman), heel pull tab, and outsole tread wrap."
    },
    {
        "slot": 5,
        "code": "05-trasera-3-4",
        "name": "Perspectiva 3/4 Trasera (135°)",
        "grid_pos": "Fila 2, Columna 1",
        "prompt_desc": "Panel 5: Three-quarter (3/4) rear perspective view facing away toward the left.",
        "details": "Ankle collar padding thickness, heel counter shape, and outer rear midsole curvature."
    },
    {
        "slot": 6,
        "code": "06-lateral-interior",
        "name": "Perfil Lateral Interior / Medial (90°)",
        "grid_pos": "Fila 2, Columna 2",
        "prompt_desc": "Panel 6: Strict 90-degree medial inner side profile view, toe pointing horizontally to the LEFT.",
        "details": "Inner foot arch support, medial panel textures, and inner midsole geometry."
    },
    {
        "slot": 7,
        "code": "07-cenital-superior",
        "name": "Cenital / Superior (90° Top-Down)",
        "grid_pos": "Fila 2, Columna 3",
        "prompt_desc": "Panel 7: Direct 90-degree top-down flat lay view looking straight down.",
        "details": "Symmetrical eyelets, tied laces, collar opening, and printed footbed insole logo."
    },
    {
        "slot": 8,
        "code": "08-suela-inferior",
        "name": "Suela Inferior / Outsole (90° Bottom-Up)",
        "grid_pos": "Fila 2, Columna 4",
        "prompt_desc": "Panel 8: Direct 90-degree flat outsole bottom tread view looking directly at the sole.",
        "details": "Complete rubber traction pattern, pivot points, flex grooves, and embossed sole branding."
    }
]

STUDIO_COMMON = (
    "Pure solid seamless white background (#FFFFFF). Uniform high-end commercial studio lighting, "
    "balanced softbox illumination at 5500K neutral daylight, razor-sharp focus across all angles, "
    "subtle grounded contact shadows on the floor. 8k resolution e-commerce product catalog standard, "
    "zero floating artifacts, zero background clutter."
)

NEGATIVE_PROMPT = (
    "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, "
    "colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, "
    "dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
)

def clean_name(name):
    return name.replace('“', '"').replace('”', '"').replace('’', "'")

def build_all_prompts():
    with open('dist/js/assigned_angles.json', 'r', encoding='utf-8') as f:
        assigned = json.load(f)

    catalog = []
    
    for item in assigned:
        idx = item['index']
        sku = item['sku']
        raw_name = clean_name(item['name'])
        
        # 1. Prompts individuales (8 ángulos)
        individual_angles = []
        for a in ANGLES_8:
            prompt_ind = (
                f"Commercial footwear catalog studio photography of authentic sneaker {raw_name}, SKU: {sku}. "
                f"{a['prompt_desc']} {a['details']} {STUDIO_COMMON}"
            )
            individual_angles.append({
                "slot": a["slot"],
                "code": a["code"],
                "name": a["name"],
                "prompt": prompt_ind
            })
            
        # 2. Grid de 6 Ángulos (Múltiplo de 2 y 3 -> Matriz 2x3 o 3x2)
        grid_6_desc = (
            f"Commercial e-commerce studio contact sheet grid showing exactly 6 distinct clean photographic panels of the authentic sneaker {raw_name}, SKU: {sku}, "
            f"arranged in a neat 2-row by 3-column (2x3) grid on a pure solid white background (#FFFFFF). "
            f"Row 1: [Panel 1: 90-degree lateral side profile pointing LEFT], [Panel 2: 3/4 perspective front-quarter facing LEFT], [Panel 3: direct straight front view]. "
            f"Row 2: [Panel 4: direct rear heel view], [Panel 5: 90-degree medial inner side profile pointing LEFT], [Panel 6: direct overhead top-down flat lay view]. "
            f"Identical sneaker colorway, identical softbox lighting, even spacing between panels. {STUDIO_COMMON}"
        )

        # 3. Grid de 8 Ángulos (Múltiplo de 2 y 4 -> Matriz 2x4)
        grid_8_desc = (
            f"Commercial e-commerce studio contact sheet grid showing exactly 8 distinct clean photographic panels of the authentic sneaker {raw_name}, SKU: {sku}, "
            f"arranged in a neat 2-row by 4-column (2x4) grid on a pure solid white background (#FFFFFF). "
            f"Row 1: [Panel 1: 90-degree lateral profile pointing LEFT], [Panel 2: 3/4 perspective front-quarter facing LEFT], [Panel 3: direct straight front view], [Panel 4: direct rear heel view]. "
            f"Row 2: [Panel 5: 3/4 rear perspective facing LEFT], [Panel 6: 90-degree medial inner side profile pointing LEFT], [Panel 7: direct overhead top-down view], [Panel 8: direct bottom outsole tread view]. "
            f"Identical sneaker colorway, identical softbox studio lighting, clean thin white gutters between panels. {STUDIO_COMMON}"
        )

        # 4. Grupo de 2 (Dúo 1x2: Lateral + 3/4 Frontal)
        duo_1_desc = (
            f"Commercial e-commerce dual-panel product sheet showing 2 views of the authentic sneaker {raw_name}, SKU: {sku}, "
            f"side-by-side in 1 row by 2 columns (1x2) on pure white background (#FFFFFF). "
            f"Left: 90-degree lateral side profile view pointing LEFT. "
            f"Right: 3/4 perspective front-quarter view pointing LEFT. "
            f"Identical lighting, grounded soft shadows. {STUDIO_COMMON}"
        )

        # 5. Grupo de 3 (Trío 1x3: Lateral + Trasera + Cenital)
        trio_1_desc = (
            f"Commercial e-commerce tri-panel product sheet showing 3 views of the authentic sneaker {raw_name}, SKU: {sku}, "
            f"side-by-side in 1 row by 3 columns (1x3) on pure white background (#FFFFFF). "
            f"Panel 1 (Left): 90-degree lateral side profile pointing LEFT. "
            f"Panel 2 (Center): Direct 180-degree rear heel view. "
            f"Panel 3 (Right): Direct 90-degree overhead top-down view. "
            f"Identical materials, uniform softbox lighting. {STUDIO_COMMON}"
        )

        catalog.append({
            "index": idx,
            "sku": sku,
            "name": raw_name,
            # Ruta relativa limpia desde dist/
            "primary_ref": f"assets/2-norm-std/{sku}/01-lateral.webp",
            "individual_angles": individual_angles,
            "grids": {
                "grid_6": {
                    "title": "Grid 2x3 (6 Ángulos en 1 Imagen)",
                    "layout": "2x3",
                    "multiplo": "Múltiplo de 2 y 3 (2 filas x 3 columnas)",
                    "prompt": grid_6_desc
                },
                "grid_8": {
                    "title": "Grid 2x4 (8 Ángulos en 1 Imagen)",
                    "layout": "2x4",
                    "multiplo": "Múltiplo de 2 y 4 (2 filas x 4 columnas)",
                    "prompt": grid_8_desc
                },
                "duo_1x2": {
                    "title": "Dúo 1x2 (2 Ángulos: Lateral + 3/4 Frontal)",
                    "layout": "1x2",
                    "multiplo": "Múltiplo de 2 (1 fila x 2 columnas)",
                    "prompt": duo_1_desc
                },
                "trio_1x3": {
                    "title": "Trío 1x3 (3 Ángulos: Lateral + Trasera + Cenital)",
                    "layout": "1x3",
                    "multiplo": "Múltiplo de 3 (1 fila x 3 columnas)",
                    "prompt": trio_1_desc
                }
            }
        })

    return catalog

def export_all():
    catalog = build_all_prompts()
    
    # 1. Guardar JSON
    json_path = 'dist/flow_prompts_catalog.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({
            "angles_meta": ANGLES_8,
            "negative_prompt": NEGATIVE_PROMPT,
            "total_products": len(catalog),
            "catalog": catalog
        }, f, indent=2, ensure_ascii=False)
    print(f"Exportado JSON: {json_path}")
    
    # 2. Guardar JS para el visor
    js_path = 'dist/js/flow_prompts.js'
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write("const flowCatalogData = " + json.dumps({
            "angles_meta": ANGLES_8,
            "negative_prompt": NEGATIVE_PROMPT,
            "catalog": catalog
        }, indent=2, ensure_ascii=False) + ";\n")
    print(f"Exportado JS: {js_path}")
    
    # 3. Actualizar Markdown
    md_path = 'docs/GUIA_PROMPTS_FLOW_CATALOGO.md'
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# Guía de Prompts para Flow y Nano Banana 2.1 (Grids de 6 y 8 Ángulos)\n\n")
        f.write("Esta guía permite generar hojas de contacto combinadas en **grids de múltiplos de 2 y 3** (2x3, 2x4, 1x2, 1x3) ")
        f.write("para cortarlas automáticamente con `scripts/split_grid_angles.py`.\n\n")
        f.write("### 🚫 Negative Prompt Común\n```text\n" + NEGATIVE_PROMPT + "\n```\n\n---\n\n")
        
        for p in catalog:
            f.write(f"## [{p['index']:02d}] {p['sku']} — {p['name']}\n\n")
            f.write(f"**Referencia Primaria:** `{p['primary_ref']}`\n\n")
            
            f.write("### 🔲 Prompts para Hojas de Contacto / Grids Combinados:\n\n")
            f.write(f"**1. {p['grids']['grid_6']['title']}** ({p['grids']['grid_6']['multiplo']})\n")
            f.write("```text\n" + p['grids']['grid_6']['prompt'] + "\n```\n\n")
            
            f.write(f"**2. {p['grids']['grid_8']['title']}** ({p['grids']['grid_8']['multiplo']})\n")
            f.write("```text\n" + p['grids']['grid_8']['prompt'] + "\n```\n\n")
            
            f.write(f"**3. {p['grids']['duo_1x2']['title']}**\n")
            f.write("```text\n" + p['grids']['duo_1x2']['prompt'] + "\n```\n\n")
            
            f.write(f"**4. {p['grids']['trio_1x3']['title']}**\n")
            f.write("```text\n" + p['grids']['trio_1x3']['prompt'] + "\n```\n\n")
            f.write("---\n\n")
            
    print(f"Exportada Guía Markdown: {md_path}")

if __name__ == '__main__':
    export_all()
