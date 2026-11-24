#!/usr/bin/env python3
"""
scripts/generate_flow_nanobanana_data.py
=============================================================================
Generador Oficial de Datos Normalizados para Flow Workstation (45 Modelos)
=============================================================================
- Escaneo estricto 1:1 desde: _source_data/fotos (Grupos A hasta G)
- 45 modelos verificados con tabla de auditoría en consola
- Mapeo dinámico de imágenes de referencia por ángulo (EN / ES, Texto y JSON)
- Síntesis explícita de ángulos faltantes y eliminación total de contaminación Space Jam
- Generación de miniaturas WebP ordenadas determinísticamente por ángulo
"""

import os
import json
import re
from PIL import Image, ImageOps
from concurrent.futures import ThreadPoolExecutor

BASE_FOTOS = os.path.join('_source_data', 'fotos')

GROUPS = [
    'Grupo A',
    'Grupo B',
    'Grupo C',
    'Grupo D',
    'Grupo E',
    'Grupo F',
    'Grupo G'
]

CANONICAL_PANELS = [
    ('01', '01 | LATERAL', '90-degree lateral outer profile, toe pointing LEFT', 'perfil lateral externo a 90°, puntera apuntando a la IZQUIERDA (toe pointing LEFT)'),
    ('02', '02 | MEDIAL', '90-degree medial inner profile, toe pointing RIGHT', 'perfil medial interno a 90°, puntera apuntando a la DERECHA (toe pointing RIGHT)'),
    ('03', '03 | 3/4 FRONT', '45-degree three-quarter front perspective, toe pointing bottom-LEFT', 'perspectiva 3/4 frontal-lateral a 45°, puntera apuntando abajo-IZQUIERDA (toe pointing bottom-LEFT)'),
    ('04', '04 | 3/4 REAR', '135-degree three-quarter rear perspective, heel on left and toe pointing RIGHT', 'perspectiva 3/4 trasera a 135°, talón a la izquierda y puntera apuntando a la DERECHA (heel on left, toe pointing RIGHT)'),
    ('05', '05 | FRONT', 'direct straight front eye-level view', 'vista frontal directa a nivel de ojo'),
    ('06', '06 | REAR', 'direct rear heel counter view', 'vista trasera directa del contrafuerte del talón'),
    ('07', '07 | TOP-DOWN', 'horizontal direct overhead top-down flat lay view, heel on left and toe pointing RIGHT', 'vista cenital horizontal directa desde arriba, talón a la izquierda y puntera apuntando a la DERECHA (toe pointing RIGHT)'),
    ('08', '08 | OUTSOLE', 'horizontal direct bottom outsole rubber tread view, heel on left and toe pointing RIGHT', 'vista inferior horizontal de la suela de goma con patrón de tracción, talón a la izquierda y puntera apuntando a la DERECHA (toe pointing RIGHT)')
]

def clean_name(name):
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

def sort_product_photos(file_list):
    """
    Ordena determinísticamente las fotos por prefijo de ángulo (01-, 02-, etc.),
    luego tomas zoom/detalle, y finalmente cualquier foto extra sin prefijo.
    """
    def sort_key(fn):
        fn_low = fn.lower()
        m = re.match(r'^(\d{2})[-_]', fn_low)
        if m:
            prefix_num = int(m.group(1))
            is_zoom = 1 if 'zoom' in fn_low or 'detail' in fn_low else 0
            return (0, prefix_num, is_zoom, fn_low)
        else:
            return (1, 99, 0, fn_low)
    return sorted(file_list, key=sort_key)

def map_file_to_panel_role(filename, index_in_order, is_first_product=False):
    """
    Asigna a cada archivo un rol explícito en inglés y español para el bloque REFERENCE IMAGE MAPPING.
    """
    fn = filename.lower()
    
    if fn.startswith('01-lateral') or 'official-01' in fn:
        if 'zoom' in fn or 'detail' in fn:
            return (
                f"Image {index_in_order} ({filename}): close-up outer lateral stitching, texture and logo details -> preserve faithfully across all panels",
                f"Imagen {index_in_order} ({filename}): detalles en primer plano de textura, costuras y logotipo lateral -> preservar fielmente en todos los paneles",
                '01-detail'
            )
        return (
            f"Image {index_in_order} ({filename}): exact outer lateral profile of THIS sneaker -> replicate directly for panel [01 | LATERAL]",
            f"Imagen {index_in_order} ({filename}): perfil lateral exterior exacto de ESTA zapatilla -> replicar directamente en el panel [01 | LATERAL]",
            '01'
        )
    elif fn.startswith('02-medial') or 'official-05' in fn:
        return (
            f"Image {index_in_order} ({filename}): exact inner medial profile of THIS sneaker -> replicate directly for panel [02 | MEDIAL]",
            f"Imagen {index_in_order} ({filename}): perfil medial interior exacto de ESTA zapatilla -> replicar directamente en el panel [02 | MEDIAL]",
            '02'
        )
    elif fn.startswith('03-3-4-front') or fn.startswith('03-frontal-3-4') or fn.startswith('02-frontal-3-4'):
        return (
            f"Image {index_in_order} ({filename}): exact three-quarter front perspective of THIS sneaker -> replicate directly for panel [03 | 3/4 FRONT]",
            f"Imagen {index_in_order} ({filename}): perspectiva 3/4 frontal exacta de ESTA zapatilla -> replicar directamente en el panel [03 | 3/4 FRONT]",
            '03'
        )
    elif fn.startswith('04-3-4-rear') or fn.startswith('03-trasera-3-4'):
        return (
            f"Image {index_in_order} ({filename}): exact three-quarter rear perspective of THIS sneaker -> replicate directly for panel [04 | 3/4 REAR]",
            f"Imagen {index_in_order} ({filename}): perspectiva 3/4 trasera exacta de ESTA zapatilla -> replicar directamente en el panel [04 | 3/4 REAR]",
            '04'
        )
    elif fn.startswith('05-front') or 'official-03' in fn:
        return (
            f"Image {index_in_order} ({filename}): exact front eye-level view of THIS sneaker -> use directly for panel [05 | FRONT]",
            f"Imagen {index_in_order} ({filename}): vista frontal directa a nivel de ojo de ESTA zapatilla -> usar directamente para el panel [05 | FRONT]",
            '05'
        )
    elif fn.startswith('06-rear') or 'official-06' in fn or fn.startswith('03-trasera'):
        return (
            f"Image {index_in_order} ({filename}): exact rear heel counter and back branding of THIS sneaker -> use directly for panel [06 | REAR]",
            f"Imagen {index_in_order} ({filename}): vista trasera del contrafuerte del talón y logotipo posterior de ESTA zapatilla -> usar directamente para el panel [06 | REAR]",
            '06'
        )
    elif fn.startswith('07-top-down') or 'official-04' in fn or fn.startswith('04-superior'):
        return (
            f"Image {index_in_order} ({filename}): exact overhead top-down flat lay view of THIS sneaker -> use directly for panel [07 | TOP-DOWN]",
            f"Imagen {index_in_order} ({filename}): vista cenital aérea directa de ESTA zapatilla -> usar directamente para el panel [07 | TOP-DOWN]",
            '07'
        )
    elif fn.startswith('08-outsole') or 'suela' in fn:
        return (
            f"Image {index_in_order} ({filename}): exact outsole tread pattern and rubber colors of THIS sneaker -> use directly for panel [08 | OUTSOLE]",
            f"Imagen {index_in_order} ({filename}): patrón exacto de tracción y colores de suela de ESTA zapatilla -> usar directamente para el panel [08 | OUTSOLE]",
            '08'
        )
    else:
        # Fotos genéricas estilo IMG_0159
        if index_in_order == 1:
            return (
                f"Image {index_in_order} ({filename}): lateral profile perspective of THIS sneaker -> guide for panel [01 | LATERAL]",
                f"Imagen {index_in_order} ({filename}): perspectiva de perfil lateral de ESTA zapatilla -> guía para panel [01 | LATERAL]",
                '01'
            )
        elif index_in_order == 2:
            return (
                f"Image {index_in_order} ({filename}): medial/quarter view of THIS sneaker -> guide for panel [02 | MEDIAL]",
                f"Imagen {index_in_order} ({filename}): perspectiva medial/tres cuartos de ESTA zapatilla -> guía para panel [02 | MEDIAL]",
                '02'
            )
        else:
            return (
                f"Image {index_in_order} ({filename}): authentic colorway, materials, embroidery and shape of THIS sneaker -> preserve across all 8 panels",
                f"Imagen {index_in_order} ({filename}): colorway auténtico, materiales, bordados y forma de ESTA zapatilla -> preservar en los 8 paneles",
                'aux'
            )

def build_bilingual_prompts(name, sku, group, pdir, files, is_space_jam=False):
    """
    Construye los prompts en EN y ES (Texto Plano y JSON) para Mode A y Mode B,
    con mapeo dinámico de imágenes, ángulos faltantes y estrictas reglas anti-contaminación.
    """
    img_count = len(files)
    mapped_panels = set()
    mappings_en = []
    mappings_es = []
    
    for idx, f in enumerate(files, 1):
        en_str, es_str, panel_code = map_file_to_panel_role(f, idx, is_space_jam)
        mappings_en.append(en_str)
        mappings_es.append(es_str)
        if panel_code in ['01', '02', '03', '04', '05', '06', '07', '08']:
            mapped_panels.add(panel_code)

    all_panels = {'01', '02', '03', '04', '05', '06', '07', '08'}
    missing_codes = sorted(list(all_panels - mapped_panels))
    
    panel_names_map = {
        '01': '[01 | LATERAL]',
        '02': '[02 | MEDIAL]',
        '03': '[03 | 3/4 FRONT]',
        '04': '[04 | 3/4 REAR]',
        '05': '[05 | FRONT]',
        '06': '[06 | REAR]',
        '07': '[07 | TOP-DOWN]',
        '08': '[08 | OUTSOLE]'
    }
    missing_str_en = ", ".join([panel_names_map[c] for c in missing_codes]) if missing_codes else "None (all 8 primary angles covered by reference photos)"
    missing_str_es = ", ".join([panel_names_map[c] for c in missing_codes]) if missing_codes else "Ninguno (todos los 8 ángulos cubiertos por las fotos de referencia)"

    folder_origin = f"_source_data/fotos/{group}/{pdir}"

    # Reglas anti-contaminación
    if is_space_jam:
        anti_contam_en = (
            f"STRICT PRODUCT IDENTITY: Render ONLY the authentic Air Jordan 9 Retro OG \"Space Jam\" (SKU: {sku}). "
            "Replicate the exact black and white leather/durabuck silhouette, red Jumpman logos, round laces, and distinct outsole traction. "
            "NEGATIVE CONSTRAINTS: Do NOT substitute any other sneaker model or silhouette."
        )
        anti_contam_es = (
            f"IDENTIDAD ESTRICTA DEL PRODUCTO: Renderizar ÚNICAMENTE las Air Jordan 9 Retro OG \"Space Jam\" auténticas (SKU: {sku}). "
            "Replicar con fidelidad la silueta de cuero y durabuck blanco/negro, logotipos Jumpman rojos y suela característica. "
            "RESTRICCIÓN NEGATIVA: NO sustituir por ningún otro modelo de zapatilla."
        )
    else:
        anti_contam_en = (
            f"STRICT PRODUCT IDENTITY: Render ONLY the authentic {name} (SKU: {sku}, {group}). "
            "Replicate the exact sneaker silhouette, colorway, panelling, materials, stitching lines, and brand markings shown in the provided reference photos. "
            "NEGATIVE CONSTRAINTS: Do NOT substitute any other sneaker model or silhouette. "
            "NEVER copy or blend features from Air Jordan 9 Space Jam or any other shoe. "
            f"Maintain the authentic identity of THIS sneaker ({name}) across all 8 panels without cross-model contamination."
        )
        anti_contam_es = (
            f"IDENTIDAD ESTRICTA DEL PRODUCTO: Renderizar ÚNICAMENTE la zapatilla auténtica {name} (SKU: {sku}, {group}). "
            "Replicar con fidelidad la silueta exacta, paleta de colores, paneles, materiales, costuras y logotipos mostrados en las fotos de referencia adjuntas. "
            "RESTRICCIÓN NEGATIVA: NO sustituir por ningún otro modelo ni silueta de calzado. "
            "NUNCA copiar ni mezclar características de las Air Jordan 9 Space Jam ni de ningún otro modelo ajeno. "
            f"Mantener la identidad auténtica de ESTA zapatilla ({name}) en los 8 paneles sin contaminación entre modelos."
        )

    mapping_block_en = "REFERENCE IMAGE MAPPING:\n" + "\n".join(f"- {m}" for m in mappings_en)
    mapping_block_es = "MAPEO DE IMÁGENES DE REFERENCIA:\n" + "\n".join(f"- {m}" for m in mappings_es)

    synth_block_en = f"MISSING ANGLES TO SYNTHESIZE 3D: {missing_str_en}. Accurately synthesize these perspective angles by projecting the 3D geometry, materials, and colorway observed in the reference photos, maintaining 100% architectural fidelity."
    synth_block_es = f"ÁNGULOS FALTANTES A SINTETIZAR EN 3D: {missing_str_es}. Sintetizar con precisión 3D estas perspectivas proyectando la geometría, materiales y colorway observados en las fotos de referencia, manteniendo 100% fidelidad de diseño."

    prompts = {
        'EN': {},
        'ES': {}
    }

    for mode in ['mode_a', 'mode_b']:
        # Mode A: Pares | Mode B: 1 Zapatilla
        if mode == 'mode_a':
            row3_en = "Row 3: [05 | FRONT: pair side-by-side (left shoe direct front eye-level view, right shoe direct rear heel view), centered], [06 | REAR: pair side-by-side (dual direct rear heel views showing both heel counters), centered]."
            row3_es = "Fila 3: [05 | FRONT: par lado a lado (izquierda vista frontal directa a nivel de ojo, derecha vista trasera directa), centrado], [06 | REAR: par lado a lado (doble vista trasera mostrando ambos contrafuertes del talón), centrado]."
            view_05_json_en = "pair side-by-side (left shoe direct front eye-level view, right shoe direct rear heel view), centered"
            view_06_json_en = "pair side-by-side (dual direct rear heel views showing both heel counters), centered"
            view_05_json_es = "par lado a lado (izquierda vista frontal directa a nivel de ojo, derecha vista trasera directa), centrado"
            view_06_json_es = "par lado a lado (doble vista trasera mostrando ambos contrafuertes del talón), centrado"
        else:
            row3_en = "Row 3: [05 | FRONT: single sneaker direct straight front eye-level view, perfectly centered], [06 | REAR: single sneaker direct rear heel counter view, perfectly centered]."
            row3_es = "Fila 3: [05 | FRONT: 1 sola zapatilla en vista frontal directa a nivel de ojo, perfectamente centrada], [06 | REAR: 1 sola zapatilla en vista trasera directa del contrafuerte del talón, perfectamente centrada]."
            view_05_json_en = "single sneaker direct straight front eye-level view, perfectly centered"
            view_06_json_en = "single sneaker direct rear heel counter view, perfectly centered"
            view_05_json_es = "1 sola zapatilla en vista frontal directa a nivel de ojo, perfectamente centrada"
            view_06_json_es = "1 sola zapatilla en vista trasera directa del contrafuerte del talón, perfectamente centrada"

        # EN Text
        text_en = (
            f"Commercial e-commerce studio contact sheet grid showing exactly 8 distinct clean photographic panels of the authentic sneaker {name}, SKU: {sku}, {group}.\n\n"
            f"{anti_contam_en}\n\n"
            f"{mapping_block_en}\n\n"
            f"{synth_block_en}\n\n"
            "LAYOUT SPECIFICATIONS:\n"
            "Master generation in 4K resolution (1:1 aspect ratio), divided by thin 1px dark-gray divider lines (#333333) on a seamless pure solid white #FFFFFF background, with generous uniform white margins in each cell ensuring the sneaker never touches borders or labels. Upper-left corner of each cell displays discrete technical label:\n"
            "Row 1: [01 | LATERAL: 90-degree lateral outer profile, toe pointing LEFT], [02 | MEDIAL: 90-degree medial inner profile, toe pointing RIGHT].\n"
            "Row 2: [03 | 3/4 FRONT: 45-degree three-quarter front perspective, toe pointing bottom-LEFT], [04 | 3/4 REAR: 135-degree three-quarter rear perspective, heel on left and toe pointing RIGHT].\n"
            f"{row3_en}\n"
            "Row 4: [07 | TOP-DOWN: horizontal direct overhead top-down flat lay view, heel on left and toe pointing RIGHT], [08 | OUTSOLE: horizontal direct bottom outsole rubber tread view, heel on left and toe pointing RIGHT].\n\n"
            "LIGHTING & ENVIRONMENT:\n"
            "Pure solid seamless white background (#FFFFFF). Uniform high-end commercial studio lighting, balanced dual-softbox illumination at 5500K neutral daylight, edge-to-edge f/8 sharpness across all 8 panels, subtle grounded contact floor shadow, zero floating artifacts, master 4K e-commerce product catalog standard."
        )

        # ES Text
        text_es = (
            f"Hoja de contacto de estudio fotográfico comercial e-commerce que muestra exactamente 8 paneles limpios de la zapatilla auténtica {name}, SKU: {sku}, {group}.\n\n"
            f"{anti_contam_es}\n\n"
            f"{mapping_block_es}\n\n"
            f"{synth_block_es}\n\n"
            "ESPECIFICACIONES DE CUADRÍCULA:\n"
            "Generación maestra en resolución 4K (relación de aspecto 1:1), dividida por líneas divisorias finas de 1px en gris oscuro (#333333) sobre fondo blanco puro #FFFFFF sin costuras, con margen blanco amplio y uniforme en cada celda para asegurar que el calzado nunca toque bordes ni etiquetas. Esquina superior izquierda de cada celda con etiqueta técnica discreta en mayúsculas:\n"
            "Fila 1: [01 | LATERAL: perfil lateral externo a 90°, puntera apuntando a la IZQUIERDA (toe pointing LEFT)], [02 | MEDIAL: perfil medial interno a 90°, puntera apuntando a la DERECHA (toe pointing RIGHT)].\n"
            "Fila 2: [03 | 3/4 FRONT: perspectiva 3/4 frontal-lateral a 45°, puntera apuntando abajo-IZQUIERDA (toe pointing bottom-LEFT)], [04 | 3/4 REAR: perspectiva 3/4 trasera a 135°, talón a la izquierda y puntera apuntando a la DERECHA (heel on left, toe pointing RIGHT)].\n"
            f"{row3_es}\n"
            "Fila 4: [07 | TOP-DOWN: vista cenital horizontal directa desde arriba, talón a la izquierda y puntera apuntando a la DERECHA (toe pointing RIGHT)], [08 | OUTSOLE: vista inferior horizontal de la suela de goma con patrón de tracción, talón a la izquierda y puntera apuntando a la DERECHA (toe pointing RIGHT)].\n\n"
            "ILUMINACIÓN Y ENTORNO:\n"
            "Fondo blanco puro sin costuras (#FFFFFF). Iluminación comercial de estudio balanceada con difusor dual-softbox a 5500K luz día neutra, nitidez de borde a borde f/8 en los 8 paneles, sombra sutil de contacto en el piso perfectamente aterrizada, cero artefactos flotantes, estándar de catálogo e-commerce en resolución maestra 4K."
        )

        # EN JSON
        json_obj_en = {
            "task": "ecommerce_4k_sneaker_contact_sheet",
            "product": {
                "name": name,
                "sku": sku,
                "group": group,
                "source_folder": folder_origin,
                "input_reference_images_count": img_count
            },
            "strict_product_identity": anti_contam_en,
            "reference_image_mapping": mappings_en,
            "missing_angles_to_synthesize": missing_str_en,
            "grid_layout": {
                "rows": 4,
                "columns": 2,
                "total_panels": 8,
                "aspect_ratio": "1:1",
                "master_resolution": "4K",
                "background": "#FFFFFF",
                "divider_lines": "thin_1px_dark_gray_#333333",
                "cell_margins": "wide_uniform_white_no_border_touch",
                "labels": "upper_left_discrete_uppercase",
                "view_mode_05_06": "mode_a_pairs_master_template" if mode == "mode_a" else "mode_b_ecommerce_single_sneaker"
            },
            "panel_distribution": [
                {"row": 1, "column": 1, "label": "01 | LATERAL", "view": "90-degree lateral outer profile, toe pointing LEFT"},
                {"row": 1, "column": 2, "label": "02 | MEDIAL", "view": "90-degree medial inner profile, toe pointing RIGHT"},
                {"row": 2, "column": 1, "label": "03 | 3/4 FRONT", "view": "45-degree three-quarter front perspective, toe pointing bottom-LEFT"},
                {"row": 2, "column": 2, "label": "04 | 3/4 REAR", "view": "135-degree three-quarter rear perspective, heel on left and toe pointing RIGHT"},
                {"row": 3, "column": 1, "label": "05 | FRONT", "view": view_05_json_en},
                {"row": 3, "column": 2, "label": "06 | REAR", "view": view_06_json_en},
                {"row": 4, "column": 1, "label": "07 | TOP-DOWN", "view": "horizontal direct overhead top-down flat lay view, heel on left and toe pointing RIGHT"},
                {"row": 4, "column": 2, "label": "08 | OUTSOLE", "view": "horizontal direct bottom outsole rubber tread view, heel on left and toe pointing RIGHT"}
            ],
            "environment": {
                "lighting": "dual_softbox_5500k_neutral_daylight",
                "sharpness": "edge_to_edge_f8",
                "floor_shadow": "subtle_grounded_contact_shadow",
                "quality": "master_4k_catalog_standard_zero_artifacts"
            }
        }

        # ES JSON
        json_obj_es = {
            "tarea": "hoja_de_contacto_ecommerce_calzado_4k",
            "producto": {
                "nombre": name,
                "sku": sku,
                "grupo": group,
                "carpeta_fuente": folder_origin,
                "cantidad_fotos_referencia": img_count
            },
            "identidad_estricta_producto": anti_contam_es,
            "mapeo_imagenes_referencia": mappings_es,
            "angulos_faltantes_a_sintetizar": missing_str_es,
            "especificaciones_cuadricula": {
                "filas": 4,
                "columnas": 2,
                "total_paneles": 8,
                "relacion_aspecto": "1:1",
                "resolucion_maestra": "4K",
                "fondo": "#FFFFFF",
                "lineas_divisorias": "lineas_finas_1px_gris_oscuro_#333333",
                "margen_celdas": "margen_blanco_amplio_uniforme_sin_colision_bordes_etiquetas",
                "etiquetas": "esquina_superior_izquierda_discreta_mayusculas",
                "modo_vistas_05_06": "modo_a_plantilla_maestra_pares" if mode == "mode_a" else "modo_b_ecommerce_una_zapatilla"
            },
            "distribucion_paneles": [
                {"fila": 1, "columna": 1, "etiqueta": "01 | LATERAL", "vista": "perfil lateral externo a 90°, puntera apuntando a la IZQUIERDA (toe pointing LEFT)"},
                {"fila": 1, "columna": 2, "etiqueta": "02 | MEDIAL", "vista": "perfil medial interno a 90°, puntera apuntando a la DERECHA (toe pointing RIGHT)"},
                {"fila": 2, "columna": 1, "etiqueta": "03 | 3/4 FRONT", "vista": "perspectiva 3/4 frontal-lateral a 45°, puntera apuntando abajo-IZQUIERDA (toe pointing bottom-LEFT)"},
                {"fila": 2, "columna": 2, "etiqueta": "04 | 3/4 REAR", "vista": "perspectiva 3/4 trasera a 135°, talón a la izquierda y puntera apuntando a la DERECHA (heel on left, toe pointing RIGHT)"},
                {"fila": 3, "columna": 1, "etiqueta": "05 | FRONT", "vista": view_05_json_es},
                {"fila": 3, "columna": 2, "etiqueta": "06 | REAR", "vista": view_06_json_es},
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

        prompts['EN'][mode] = {
            'text': text_en,
            'json': json.dumps(json_obj_en, indent=2, ensure_ascii=False)
        }
        prompts['ES'][mode] = {
            'text': text_es,
            'json': json.dumps(json_obj_es, indent=2, ensure_ascii=False)
        }

    return prompts, mappings_en, mappings_es, missing_codes

def process_thumbnail(args):
    src, dst = args
    if os.path.exists(dst):
        return
    try:
        im = Image.open(src)
        im = ImageOps.exif_transpose(im)
        im = im.convert('RGB')
        im.thumbnail((600, 600), Image.Resampling.LANCZOS)
        im.save(dst, 'WEBP', quality=88, method=6)
    except Exception as e:
        print(f"Error optimizando preview {src}: {e}")

def main():
    print("=" * 80)
    print("AUDITORÍA Y NORMALIZACIÓN: ESCANEANDO _source_data/fotos (GRUPOS A HASTA G)")
    print("=" * 80)

    with open('dist/js/assigned_angles.json', 'r', encoding='utf-8') as f:
        assigned_list = json.load(f)

    # 1. Recolectar todas las carpetas reales estrictamente en _source_data/fotos
    scanned_items = []
    
    for g in GROUPS:
        g_path = os.path.join(BASE_FOTOS, g)
        if not os.path.exists(g_path):
            raise RuntimeError(f"ERROR CRÍTICO: La carpeta requerida {g_path} no existe en disco!")
        
        # Listar carpetas de producto (ignorar 'resultado', 'ref', etc.)
        pdirs = sorted([
            d for d in os.listdir(g_path)
            if os.path.isdir(os.path.join(g_path, d)) and not d.lower().startswith(('resultado', 'ref'))
        ])
        
        for pd in pdirs:
            scanned_items.append((g, pd, os.path.join(g_path, pd)))

    if len(scanned_items) != 45:
        raise RuntimeError(f"ERROR: Se esperaban 45 modelos en _source_data/fotos, pero se encontraron {len(scanned_items)}!")

    print(f"\n{'#':<3} | {'Grupo':<8} | {'SKU':<12} | {'Nombre Modelo':<36} | {'Carpeta Exacta':<36} | {'Fotos':<5} | Archivos")
    print("-" * 140)

    catalog = []
    thumb_tasks = []

    for idx, (group, pdir, pdir_full) in enumerate(scanned_items):
        matched = assigned_list[idx] if idx < len(assigned_list) else None
        if not matched:
            raise RuntimeError(f"Desfase en índice {idx} al emparejar con assigned_angles.json!")

        raw_sku = matched.get('rawSku', matched.get('sku', f'SKU-{idx+1}'))
        norm_sku = normalize_sku(matched.get('sku', raw_sku))
        name = clean_name(matched.get('name', pdir))

        # Listar y ordenar fotos determinísticamente
        all_files = [f for f in os.listdir(pdir_full) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))]
        sorted_files = sort_product_photos(all_files)
        img_count = len(sorted_files)

        if img_count == 0:
            raise RuntimeError(f"ERROR: La carpeta {pdir_full} no tiene fotos!")

        # Tabla de auditoría
        first_few = ", ".join(sorted_files[:3]) + (f" (+{img_count-3})" if img_count > 3 else "")
        print(f"{idx+1:<3} | {group:<8} | {norm_sku:<12} | {name[:35]:<36} | {pdir[:35]:<36} | {img_count:<5} | {first_few}")

        # Directorio de previews optimizados
        sku_preview_dir = os.path.join('dist', 'assets', 'source-previews', norm_sku)
        os.makedirs(sku_preview_dir, exist_ok=True)

        real_photos = []
        image_items = []
        for i, fn in enumerate(sorted_files, 1):
            clean_fn = sanitize_filename(fn)
            webp_name = f"{i:02d}_{clean_fn}.webp"
            dst_path = os.path.join(sku_preview_dir, webp_name)
            src_path = os.path.join(pdir_full, fn)
            rel_web_path = f"assets/source-previews/{norm_sku}/{webp_name}"
            real_photos.append(rel_web_path)
            thumb_tasks.append((src_path, dst_path))
            image_items.append({
                'order': i,
                'filename': fn,
                'label': f"Image {i}: {fn}",
                'web_path': rel_web_path
            })

        is_space_jam = (idx == 0 or norm_sku == 'IX6180-100')
        bilingual_prompts, map_en, map_es, missing = build_bilingual_prompts(name, norm_sku, group, pdir, sorted_files, is_space_jam)

        catalog.append({
            'index': idx,
            'index_display': idx + 1,
            'sku': norm_sku,
            'rawSku': raw_sku,
            'name': name,
            'group': group,
            'top_folder': 'fotos',
            'product_dir': pdir,
            'full_path': f"C:/Users/eduar/Documents/CATALOGO/_source_data/fotos/{group}/{pdir}",
            'image_count': img_count,
            'image_files': sorted_files,
            'image_items': image_items,
            'real_photos': real_photos,
            'preview_primary': real_photos[0] if real_photos else f"assets/2-norm-std/{norm_sku}/01-lateral.webp",
            'reference_mapping_en': map_en,
            'reference_mapping_es': map_es,
            'missing_angles': missing,
            'prompts': bilingual_prompts,
            'prompt_text': bilingual_prompts['EN']['mode_a']['text'],
            'prompt_json': bilingual_prompts['EN']['mode_a']['json']
        })

    print("-" * 140)
    print(f"Total modelos auditados exitosamente: {len(catalog)} / 45.")

    print(f"\nGenerando {len(thumb_tasks)} miniaturas WebP optimizadas en paralelo...")
    with ThreadPoolExecutor(max_workers=8) as executor:
        list(executor.map(process_thumbnail, thumb_tasks))
    print("Todas las miniaturas WebP fueron generadas exitosamente.")

    # Guardar dist/js/flow_nanobanana_data.js
    out_js = os.path.join('dist', 'js', 'flow_nanobanana_data.js')
    data_payload = {
        'generated_at': '2026-11-24',
        'source_directory': '_source_data/fotos',
        'total_products': len(catalog),
        'groups': GROUPS,
        'catalog': catalog
    }

    with open(out_js, 'w', encoding='utf-8') as f:
        f.write("// Datos Oficiales Normalizados para Flow Workstation (45 Modelos)\n")
        f.write("const flowNanobananaData = ")
        json.dump(data_payload, f, indent=2, ensure_ascii=False)
        f.write(";\n")

    print(f"\nArchivo generado exitosamente: {out_js}")
    print("=" * 80)

if __name__ == '__main__':
    main()
