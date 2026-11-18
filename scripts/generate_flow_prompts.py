"""
Generador Maestro de Prompts para Flow (Midjourney, ComfyUI, FLUX, SDXL)
Crea prompts específicos para 7 perspectivas canónicas de catálogo de e-commerce
para cada uno de los 45 productos.
"""

import json
import os

# Definición técnica de los 7 ángulos canónicos de e-commerce
PERSPECTIVES = [
    {
        "id": "toma-1-lateral-exterior",
        "number": 1,
        "name": "Perfil Lateral Exterior (90°)",
        "tag": "90° Lateral Exterior",
        "description": "Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.",
        "angle_spec": "Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole.",
        "details_focus": "Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line."
    },
    {
        "id": "toma-2-frontal-3-4",
        "number": 2,
        "name": "Perspectiva 3/4 Frontal (45°)",
        "tag": "3/4 Frontal Perspectiva",
        "description": "Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.",
        "angle_spec": "Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle.",
        "details_focus": "Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously."
    },
    {
        "id": "toma-3-frontal-directa",
        "number": 3,
        "name": "Frontal Directa (0°)",
        "tag": "Frontal Directa 0°",
        "description": "Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.",
        "angle_spec": "Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker.",
        "details_focus": "Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings."
    },
    {
        "id": "toma-4-posterior-talon",
        "number": 4,
        "name": "Posterior / Talón (180°)",
        "tag": "Posterior Talón 180°",
        "description": "Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.",
        "angle_spec": "Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level.",
        "details_focus": "Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap."
    },
    {
        "id": "toma-5-trasera-3-4",
        "number": 5,
        "name": "Perspectiva 3/4 Trasera (135°)",
        "tag": "3/4 Trasera Exterior",
        "description": "Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.",
        "angle_spec": "Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front.",
        "details_focus": "Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective."
    },
    {
        "id": "toma-6-lateral-interior",
        "number": 6,
        "name": "Perfil Lateral Interior / Medial (90°)",
        "tag": "90° Lateral Interior (Medial)",
        "description": "Muestra el lado interno del pie, soporte del arco y patrón medial.",
        "angle_spec": "Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level.",
        "details_focus": "Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting."
    },
    {
        "id": "toma-7-cenital-superior",
        "number": 7,
        "name": "Cenital / Superior (90° Top-Down)",
        "tag": "Cenital Superior 90°",
        "description": "Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.",
        "angle_spec": "Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left.",
        "details_focus": "Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo."
    }
]

# Entorno de estudio, iluminación y calidad uniforme para consistencia comercial
STUDIO_ENVIRONMENT = (
    "Pure solid seamless white background (#FFFFFF), clean commercial studio environment. "
    "Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. "
    "Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. "
    "Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. "
    "8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions."
)

NEGATIVE_PROMPT = (
    "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, "
    "colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, "
    "dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
)

# Parámetros técnicos recomendados para Flow / Stable Diffusion / Midjourney
FLOW_RECOMMENDED_SETTINGS = {
    "aspect_ratio": "1:1 (Square 1200x1200px / 1024x1024px)",
    "sampler": "Euler a / DPM++ 2M Karras",
    "steps": 30,
    "cfg_scale": 7.0,
    "denoising_strength_img2img": 0.45,
    "image_weight_reference": 1.8,
    "seed_mode": "Fixed Seed per product to maintain identical materials across all 7 angles"
}

def clean_name(name):
    return name.replace('“', '"').replace('”', '"').replace('’', "'")

def build_catalog_prompts():
    with open('dist/js/assigned_angles.json', 'r', encoding='utf-8') as f:
        assigned = json.load(f)

    catalog = []
    
    for item in assigned:
        idx = item['index']
        sku = item['sku']
        raw_name = clean_name(item['name'])
        folder = item.get('folder', sku)
        
        # Generar prompts para los 7 ángulos
        angles_data = []
        for p in PERSPECTIVES:
            prompt_flat = (
                f"Commercial footwear catalog studio photography of authentic sneaker {raw_name}, SKU: {sku}. "
                f"{p['angle_spec']} {p['details_focus']} "
                f"{STUDIO_ENVIRONMENT}"
            )
            
            prompt_tags = (
                f"footwear product photography, {raw_name}, {sku}, {p['tag']}, "
                f"{p['angle_spec']}, {p['details_focus']}, "
                f"pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, "
                f"85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog"
            )
            
            angles_data.append({
                "number": p["number"],
                "id": p["id"],
                "name": p["name"],
                "tag": p["tag"],
                "description": p["description"],
                "prompt_natural": prompt_flat,
                "prompt_tags": prompt_tags,
                "negative_prompt": NEGATIVE_PROMPT,
                "ref_image_recommended": f"dist/assets/2-norm-std/{sku}/01-lateral.webp" if p["number"] in (1, 2, 5, 6) else f"dist/assets/2-norm-std/{sku}/02-frontal-3-4.webp"
            })
            
        catalog.append({
            "index": idx,
            "sku": sku,
            "name": raw_name,
            "folder": folder,
            "primary_ref": f"dist/assets/2-norm-std/{sku}/01-lateral.webp",
            "angles": angles_data
        })
        
    return catalog

def export_all():
    catalog = build_catalog_prompts()
    
    # 1. Guardar JSON
    json_path = 'dist/flow_prompts_catalog.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({
            "settings": FLOW_RECOMMENDED_SETTINGS,
            "perspectives_meta": PERSPECTIVES,
            "total_products": len(catalog),
            "catalog": catalog
        }, f, indent=2, ensure_ascii=False)
    print(f"Exportado JSON: {json_path}")
    
    # 2. Guardar JS estático para el visor web
    js_path = 'dist/js/flow_prompts.js'
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write("const flowCatalogData = " + json.dumps({
            "settings": FLOW_RECOMMENDED_SETTINGS,
            "perspectives_meta": PERSPECTIVES,
            "catalog": catalog
        }, indent=2, ensure_ascii=False) + ";\n")
    print(f"Exportado JS: {js_path}")
    
    # 3. Guardar Guía Markdown de Referencia
    md_path = 'docs/GUIA_PROMPTS_FLOW_CATALOGO.md'
    os.makedirs('docs', exist_ok=True)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# Guía de Prompts para Generación en Flow (7 Ángulos Canónicos)\n\n")
        f.write("Guía estructurada con prompts listos para copiar y pegar en herramientas de generación de imágenes (Flow, Midjourney, ComfyUI, FLUX).\n\n")
        f.write("## ⚙️ Configuración Recomendada en Flow\n\n")
        f.write(f"- **Relación de Aspecto (Aspect Ratio):** `{FLOW_RECOMMENDED_SETTINGS['aspect_ratio']}`\n")
        f.write(f"- **Muestreador (Sampler):** `{FLOW_RECOMMENDED_SETTINGS['sampler']}`\n")
        f.write(f"- **Pasos (Steps):** `{FLOW_RECOMMENDED_SETTINGS['steps']}`\n")
        f.write(f"- **CFG Scale:** `{FLOW_RECOMMENDED_SETTINGS['cfg_scale']}`\n")
        f.write(f"- **Denoising Strength (Img2Img):** `{FLOW_RECOMMENDED_SETTINGS['denoising_strength_img2img']}`\n")
        f.write(f"- **Image Weight (Referencia):** `{FLOW_RECOMMENDED_SETTINGS['image_weight_reference']}`\n")
        f.write(f"- **Consistencia de Semilla:** `{FLOW_RECOMMENDED_SETTINGS['seed_mode']}`\n\n")
        f.write("### 🚫 Negative Prompt Común\n```text\n" + NEGATIVE_PROMPT + "\n```\n\n")
        f.write("---\n\n")
        f.write("## 👟 Catálogo de Modelos (45 Productos × 7 Ángulos)\n\n")
        
        for item in catalog:
            f.write(f"### [{item['index']:02d}] {item['sku']} — {item['name']}\n\n")
            f.write(f"**Foto de Referencia Primaria recomendada:** `{item['primary_ref']}`\n\n")
            for a in item['angles']:
                f.write(f"#### Ángulo {a['number']}: {a['name']}\n")
                f.write(f"*{a['description']}*\n\n")
                f.write("**Prompt en Lenguaje Natural (Recomendado):**\n")
                f.write("```text\n" + a['prompt_natural'] + "\n```\n\n")
                f.write("**Variante en Tags (Para Stable Diffusion / ComfyUI):**\n")
                f.write("```text\n" + a['prompt_tags'] + "\n```\n\n")
            f.write("---\n\n")
            
    print(f"Exportada Guía Markdown: {md_path}")

if __name__ == '__main__':
    export_all()
