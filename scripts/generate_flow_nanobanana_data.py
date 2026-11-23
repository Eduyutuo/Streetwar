#!/usr/bin/env python3
"""
scripts/generate_flow_nanobanana_data.py
=============================================================================
Generador de Datos Normalizados para Flow Workstation (45 Modelos, Grupos A-G)
=============================================================================
Genera dist/js/flow_nanobanana_data.js con:
  - Catálogo normalizado de 45 modelos auditados (Grupos A a G).
  - SKUs normalizados en mayúsculas con guiones y campo rawSku.
  - Corrección de nombres (ej. "Space Jam" en IX6180-100).
  - Prompts en 2 idiomas (EN / ES) para ambos modos de vistas 05/06:
      * Modo A: Plantilla Maestra — Pares (Side-by-side)
      * Modo B: E-Commerce — 1 Zapatilla (Individual)
  - Previews WebP optimizados de todas las fotos de inventario reales.
"""

import os
import json
import re
from PIL import Image, ImageOps
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = '_source_data'
REF_MASTER = 'Air Jordan 9 Retro OG "Space Jam"'

TOP_FOLDERS = [
    ('fotos_ABC', ['Grupo A', 'Grupo B', 'Grupo C']),
    ('fotos_DE', ['Grupo D', 'Grupo E']),
    ('fotos_FG', ['Grupo F', 'Grupo G'])
]

with open('dist/js/assigned_angles.json', 'r', encoding='utf-8') as f:
    assigned_list = json.load(f)

def clean_name(name):
    """Normaliza nombres eliminando comillas tipográficas y corrigiendo typos."""
    c = name.replace('“', '"').replace('”', '"').replace('’', "'")
    c = c.replace('Spam Jam', 'Space Jam')
    return c.strip()

def sanitize_filename(filename):
    name, _ = os.path.splitext(filename)
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)

def normalize_sku(sku_str):
    if not sku_str:
        return ""
    return re.sub(r'[\s_]+', '-', str(sku_str).strip().upper())

def build_prompt_text(name, sku, group, top_folder, prod_dir, img_count, lang='en', mode='mode_a'):
    folder_origin = f"{top_folder}/{group}/{prod_dir}"
    if lang == 'en':
        row3 = (
            "Row 3: [05 | FRONT: pair side-by-side (left shoe direct front eye-level view, right shoe direct rear heel view), centered], "
            "[06 | REAR: pair side-by-side (dual direct rear heel views showing both heel counters), centered]."
            if mode == 'mode_a' else
            "Row 3: [05 | FRONT: single sneaker direct straight front eye-level view, perfectly centered], "
            "[06 | REAR: single sneaker direct rear heel counter view, perfectly centered]."
        )
        return (
            f'Commercial e-commerce studio contact sheet grid showing exactly 8 distinct clean photographic panels of the authentic sneaker {name}, SKU: {sku}, {group}. '
            f'Synthesized from the {img_count} input reference photos provided from "{folder_origin}", matching the exact 4-row by 2-column layout and camera angles of reference image "{REF_MASTER}". '
            f'Master generation in 4K resolution (1:1 aspect ratio), divided by thin 1px dark-gray divider lines on a seamless pure white #FFFFFF background, with generous uniform white margins in each cell ensuring the sneaker never touches borders or labels. Upper-left corner of each cell displays discrete technical label: '
            f'Row 1: [01 | LATERAL: 90-degree lateral outer profile, toe pointing LEFT], [02 | MEDIAL: 90-degree medial inner profile, toe pointing RIGHT]. '
            f'Row 2: [03 | 3/4 FRONT: 45-degree three-quarter front perspective, toe pointing bottom-LEFT], [04 | 3/4 REAR: 135-degree three-quarter rear perspective, heel on left and toe pointing RIGHT]. '
            f'{row3} '
            f'Row 4: [07 | TOP-DOWN: horizontal direct overhead top-down flat lay view, heel on left and toe pointing RIGHT], [08 | OUTSOLE: horizontal direct bottom outsole rubber tread view, heel on left and toe pointing RIGHT]. '
            f'Synthesize complete 3D geometry seamlessly using all {img_count} multi-angle reference photos to reconstruct authentic 360-degree colorway, stitch lines, textures, and logos. '
            f'Pure solid seamless white background (#FFFFFF). Uniform high-end commercial studio lighting, balanced dual-softbox illumination at 5500K neutral daylight, '
            f'edge-to-edge f/8 sharpness across all 8 panels, subtle grounded contact floor shadow, zero floating artifacts, master 4K e-commerce product catalog standard.'
        )
    else: # Spanish
        row3_es = (
            "Fila 3: [05 | FRONT: par lado a lado (izquierda vista frontal directa a nivel de ojo, derecha vista trasera directa), centrado], "
            "[06 | REAR: par lado a lado (doble vista trasera mostrando ambos contrafuertes del talón), centrado]."
            if mode == 'mode_a' else
            "Fila 3: [05 | FRONT: 1 sola zapatilla en vista frontal directa a nivel de ojo, perfectamente centrada], "
            "[06 | REAR: 1 sola zapatilla en vista trasera directa del contrafuerte del talón, perfectamente centrada]."
        )
        return (
            f'Hoja de contacto de estudio fotográfico comercial e-commerce que muestra exactamente 8 paneles limpios de la zapatilla auténtica {name}, SKU: {sku}, {group}. '
            f'Sintetizada a partir de las {img_count} fotos de referencia provistas desde "{folder_origin}", replicando con exactitud la cuadrícula de 4 filas × 2 columnas y los ángulos de cámara de la imagen maestra de referencia "{REF_MASTER}". '
            f'Generación maestra en resolución 4K (relación de aspecto 1:1), dividida por líneas divisorias finas de 1px en gris oscuro sobre fondo blanco puro #FFFFFF sin costuras, con margen blanco amplio y uniforme en cada celda para asegurar que el calzado nunca toque bordes ni etiquetas. Esquina superior izquierda de cada celda con etiqueta técnica en mayúsculas: '
            f'Fila 1: [01 | LATERAL: perfil lateral externo a 90°, puntera apuntando a la IZQUIERDA (toe pointing LEFT)], [02 | MEDIAL: perfil medial interno a 90°, puntera apuntando a la DERECHA (toe pointing RIGHT)]. '
            f'Fila 2: [03 | 3/4 FRONT: perspectiva 3/4 frontal-lateral a 45°, puntera apuntando abajo-IZQUIERDA (toe pointing bottom-LEFT)], [04 | 3/4 REAR: perspectiva 3/4 trasera a 135°, talón a la izquierda y puntera apuntando a la DERECHA (heel on left, toe pointing RIGHT)]. '
            f'{row3_es} '
            f'Fila 4: [07 | TOP-DOWN: vista cenital horizontal directa desde arriba, talón a la izquierda y puntera apuntando a la DERECHA (toe pointing RIGHT)], [08 | OUTSOLE: vista inferior horizontal de la suela de goma con patrón de tracción, talón a la izquierda y puntera apuntando a la DERECHA (toe pointing RIGHT)]. '
            f'Reconstrucción 3D fidedigna de materiales originales, colorway, costuras y logotipos en 360 grados según todas las {img_count} fotos reales de referencia. '
            f'Fondo blanco puro sin costuras (#FFFFFF). Iluminación comercial de estudio balanceada con difusor dual-softbox a 5500K luz día neutra, '
            f'nitidez de borde a borde f/8 en los 8 paneles, sombra sutil de contacto en el piso perfectamente aterrizada, cero artefactos flotantes, estándar de catálogo e-commerce en resolución maestra 4K.'
        )

def build_prompt_json(name, sku, group, top_folder, prod_dir, img_count, lang='en', mode='mode_a'):
    folder_origin = f"{top_folder}/{group}/{prod_dir}"
    if lang == 'en':
        view_05 = "pair side-by-side (left shoe direct front eye-level view, right shoe direct rear heel view), centered" if mode == "mode_a" else "single sneaker direct straight front eye-level view, perfectly centered"
        view_06 = "pair side-by-side (dual direct rear heel views showing both heel counters), centered" if mode == "mode_a" else "single sneaker direct rear heel counter view, perfectly centered"
        return {
            "task": "commercial_footwear_catalog_contact_sheet_8_panels",
            "master_resolution": "4K_uhd_1_to_1_aspect_ratio",
            "reference_composition_image": REF_MASTER,
            "multi_view_reference_inputs": {
                "source_photos_count": img_count,
                "description": f"Use all {img_count} uploaded reference photos to reconstruct 360-degree authentic materials, colorway, and logos",
                "folder_origin": folder_origin,
                "group": group
            },
            "product": {
                "name": name,
                "sku": sku,
                "group": group,
                "authentic": True
            },
            "grid_layout": {
                "total_panels": 8,
                "distribution": "4_rows_by_2_columns",
                "aspect_ratio": "1:1",
                "reference_match": f"replicate_exact_grid_and_angles_from_{REF_MASTER}",
                "background": "#FFFFFF",
                "dividers": "thin_1px_dark_gray_divider_lines",
                "cell_margins": "generous_uniform_white_padding_zero_border_or_label_overlap",
                "labels": "discrete_uppercase_top_left_corner",
                "view_mode_05_06": "mode_a_master_pairs" if mode == "mode_a" else "mode_b_ecommerce_single"
            },
            "panels_distribution": [
                {"row": 1, "col": 1, "label": "01 | LATERAL", "view": "90-degree lateral outer profile, toe pointing LEFT"},
                {"row": 1, "col": 2, "label": "02 | MEDIAL", "view": "90-degree medial inner profile, toe pointing RIGHT"},
                {"row": 2, "col": 1, "label": "03 | 3/4 FRONT", "view": "45-degree three-quarter front perspective, toe pointing bottom-LEFT"},
                {"row": 2, "col": 2, "label": "04 | 3/4 REAR", "view": "135-degree three-quarter rear perspective, heel on left and toe pointing RIGHT"},
                {"row": 3, "col": 1, "label": "05 | FRONT", "view": view_05},
                {"row": 3, "col": 2, "label": "06 | REAR", "view": view_06},
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
    else: # Spanish
        view_05_es = "par lado a lado (izquierda vista frontal directa a nivel de ojo, derecha vista trasera directa), centrado" if mode == "mode_a" else "1 sola zapatilla en vista frontal directa a nivel de ojo, perfectamente centrada"
        view_06_es = "par lado a lado (doble vista trasera mostrando ambos contrafuertes del talón), centrado" if mode == "mode_a" else "1 sola zapatilla en vista trasera directa del contrafuerte del talón, perfectamente centrada"
        return {
            "tarea": "hoja_contacto_catalogo_calzado_comercial_8_paneles",
            "resolucion_maestra": "4K_uhd_relacion_aspecto_1_a_1",
            "imagen_referencia_composicion": REF_MASTER,
            "entradas_referencia_multiples": {
                "cantidad_fotos_origen": img_count,
                "descripcion": f"Utilizar todas las {img_count} fotos de referencia provistas para reconstruir materiales originales, colorway y logotipos en 360 grados",
                "carpeta_origen": folder_origin,
                "grupo": group
            },
            "producto": {
                "nombre": name,
                "sku": sku,
                "grupo": group,
                "autentico": True
            },
            "diseno_cuadricula": {
                "total_paneles": 8,
                "distribucion": "4_filas_por_2_columnas",
                "relacion_aspecto": "1:1",
                "referencia_maestra": f"replicar_exactamente_cuadricula_y_angulos_de_{REF_MASTER}",
                "fondo": "#FFFFFF",
                "lineas_divisorias": "lineas_finas_1px_gris_oscuro",
                "margen_celdas": "margen_blanco_amplio_uniforme_sin_colision_bordes_etiquetas",
                "etiquetas": "esquina_superior_izquierda_discreta_mayusculas",
                "modo_vistas_05_06": "modo_a_plantilla_maestra_pares" if mode == "mode_a" else "modo_b_ecommerce_una_zapatilla"
            },
            "distribucion_paneles": [
                {"fila": 1, "columna": 1, "etiqueta": "01 | LATERAL", "vista": "perfil lateral externo a 90°, puntera apuntando a la IZQUIERDA (toe pointing LEFT)"},
                {"fila": 1, "columna": 2, "etiqueta": "02 | MEDIAL", "vista": "perfil medial interno a 90°, puntera apuntando a la DERECHA (toe pointing RIGHT)"},
                {"fila": 2, "columna": 1, "etiqueta": "03 | 3/4 FRONT", "vista": "perspectiva 3/4 frontal-lateral a 45°, puntera apuntando abajo-IZQUIERDA (toe pointing bottom-LEFT)"},
                {"fila": 2, "columna": 2, "etiqueta": "04 | 3/4 REAR", "vista": "perspectiva 3/4 trasera a 135°, talón a la izquierda y puntera apuntando a la DERECHA (heel on left, toe pointing RIGHT)"},
                {"fila": 3, "columna": 1, "etiqueta": "05 | FRONT", "vista": view_05_es},
                {"fila": 3, "columna": 2, "etiqueta": "06 | REAR", "vista": view_06_es},
                {"fila": 4, "columna": 1, "etiqueta": "07 | TOP-DOWN", "vista": "vista cenital horizontal directa desde arriba, talón a la izquierda y puntera apuntando a la DERECHA (toe pointing RIGHT)"},
                {"fila": 4, "columna": 2, "etiqueta": "08 | OUTSOLE", "vista": "vista inferior horizontal de la suela de goma con patrón de tracción, talón a la izquierda y puntera apuntando a la DERECHA (toe pointing RIGHT)"}
            ],
            "entorno": {
                "iluminacion": "dual_softbox_5500k_luz_dia_neutra",
                "enfoque": "nitidez_borde_a_borde_f8",
                "sombra_piso": "sombra_sutil_contacto_aterrizada",
                "calidad": "resolucion_maestra_4k_estandar_catalogo_ecommerce_cero_artefactos"
            }
        }

tasks = []
catalog = []
sku_idx = 0

print("🔍 Escaneando estructura de _source_data (Grupos A a G)...")
for top, groups in TOP_FOLDERS:
    for g in groups:
        g_path = os.path.join(BASE_DIR, top, g)
        if not os.path.exists(g_path):
            continue
            
        # Filtrar estrictamente carpetas de producto (ignorar 'resultado', 'ref', etc.)
        prod_dirs = sorted([
            d for d in os.listdir(g_path)
            if os.path.isdir(os.path.join(g_path, d)) and not d.lower().startswith(('resultado', 'ref'))
        ])
        
        print(f"  • {top} / {g}: {len(prod_dirs)} productos detectados.")
        
        for pdir in prod_dirs:
            pdir_full = os.path.join(g_path, pdir)
            files = sorted([f for f in os.listdir(pdir_full) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))])
            
            matched = assigned_list[sku_idx] if sku_idx < len(assigned_list) else None
            raw_sku = matched.get('rawSku', matched.get('sku', f'SKU-{sku_idx}')) if matched else f"SKU-{sku_idx}"
            norm_sku = normalize_sku(matched.get('sku', raw_sku) if matched else raw_sku)
            name = clean_name(matched.get('name', pdir) if matched else pdir)
            img_count = len(files)
            
            # Directorio de previews optimizados
            sku_preview_dir = os.path.join('dist', 'assets', 'source-previews', norm_sku)
            os.makedirs(sku_preview_dir, exist_ok=True)
            
            real_photos = []
            for i, f in enumerate(files):
                clean_fn = sanitize_filename(f)
                webp_name = f"{i+1:02d}_{clean_fn}.webp"
                dst_path = os.path.join(sku_preview_dir, webp_name)
                src_path = os.path.join(pdir_full, f)
                rel_web_path = f"assets/source-previews/{norm_sku}/{webp_name}"
                real_photos.append(rel_web_path)
                tasks.append((src_path, dst_path))
                
            preview_primary = real_photos[0] if real_photos else f"assets/2-norm-std/{norm_sku}/01-lateral.webp"
            
            # Prompts dinámicos EN y ES para ambos modos
            prompt_en_a = build_prompt_text(name, norm_sku, g, top, pdir, img_count, 'en', 'mode_a')
            prompt_en_b = build_prompt_text(name, norm_sku, g, top, pdir, img_count, 'en', 'mode_b')
            prompt_es_a = build_prompt_text(name, norm_sku, g, top, pdir, img_count, 'es', 'mode_a')
            prompt_es_b = build_prompt_text(name, norm_sku, g, top, pdir, img_count, 'es', 'mode_b')
            
            json_en_a = build_prompt_json(name, norm_sku, g, top, pdir, img_count, 'en', 'mode_a')
            json_en_b = build_prompt_json(name, norm_sku, g, top, pdir, img_count, 'en', 'mode_b')
            json_es_a = build_prompt_json(name, norm_sku, g, top, pdir, img_count, 'es', 'mode_a')
            json_es_b = build_prompt_json(name, norm_sku, g, top, pdir, img_count, 'es', 'mode_b')
            
            safe_group = g.replace(' ', '_')
            
            catalog.append({
                "index": sku_idx,
                "sku": norm_sku,
                "rawSku": raw_sku,
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
                "prompts": {
                    "EN": {
                        "mode_a": {
                            "text": prompt_en_a,
                            "json": json.dumps(json_en_a, indent=2)
                        },
                        "mode_b": {
                            "text": prompt_en_b,
                            "json": json.dumps(json_en_b, indent=2)
                        }
                    },
                    "ES": {
                        "mode_a": {
                            "text": prompt_es_a,
                            "json": json.dumps(json_es_a, indent=2, ensure_ascii=False)
                        },
                        "mode_b": {
                            "text": prompt_es_b,
                            "json": json.dumps(json_es_b, indent=2, ensure_ascii=False)
                        }
                    }
                },
                # Prompts por defecto activos (EN, mode_a)
                "prompt_text": prompt_en_a,
                "prompt_json": json.dumps(json_en_a, indent=2),
                "split_command": f'python scripts/split_grid_angles.py "{norm_sku}.png" --sku {norm_sku} --group {safe_group} --size 1024 --format webp'
            })
            
            sku_idx += 1

print(f"\n📦 Total de productos catalogados: {len(catalog)}")

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
        print(f"Error procesando preview {src}: {e}")

print(f"⚡ Verificando/generando {len(tasks)} previews de fotos reales en WebP...")
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

print(f"✅ Generado exitosamente 'dist/js/flow_nanobanana_data.js' con {len(catalog)} productos.")
