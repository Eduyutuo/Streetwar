#!/usr/bin/env python3
"""
scripts/generate_flow_nanobanana_data.py
=============================================================================
Generador Oficial de Datos Normalizados para Flow Workstation (45 Modelos)
=============================================================================
- Escaneo estricto 1:1 cruzado con SNKRS (1).xlsx y _source_data/fotos (Grupos A a G)
- Nombres de carpetas reales: {Nombre_Carpeta_Real}
- Nombres de archivos normalizados: {Nombre_Carpeta_Real}_{01_lateral...08_outsole}.webp
- Prompts para Cuadrícula 4x2 Maestra (EN/ES, Texto y JSON, Modos A y B)
- 8 Prompts Individuales (1:1 WebP sobre fondo blanco #FFFFFF, EN/ES, Modos A y B)
- Generación de miniaturas WebP ordenadas determinísticamente por ángulo
"""

import os
import sys
import json
import re
from PIL import Image, ImageOps
from concurrent.futures import ThreadPoolExecutor

sys.path.append(os.path.dirname(__file__))
from snkrs_mapping import load_snkrs_mapping, normalize_sku, clean_model_name

CANONICAL_PANELS = [
    ('01', '01_lateral', '01 | LATERAL', '90-degree lateral outer profile, toe pointing LEFT', 'perfil lateral externo a 90°, puntera apuntando a la IZQUIERDA (toe pointing LEFT)'),
    ('02', '02_medial', '02 | MEDIAL', '90-degree medial inner profile, toe pointing RIGHT', 'perfil medial interno a 90°, puntera apuntando a la DERECHA (toe pointing RIGHT)'),
    ('03', '03_3-4_front', '03 | 3/4 FRONT', '45-degree three-quarter front perspective, toe pointing bottom-LEFT', 'perspectiva 3/4 frontal-lateral a 45°, puntera apuntando abajo-IZQUIERDA (toe pointing bottom-LEFT)'),
    ('04', '04_3-4_rear', '04 | 3/4 REAR', '135-degree three-quarter rear perspective, heel on left and toe pointing RIGHT', 'perspectiva 3/4 trasera a 135°, talón a la izquierda y puntera apuntando a la DERECHA (heel on left, toe pointing RIGHT)'),
    ('05', '05_front', '05 | FRONT', 'direct straight front eye-level view', 'vista frontal directa a nivel de ojo'),
    ('06', '06_rear', '06 | REAR', 'direct rear heel counter view', 'vista trasera directa del contrafuerte del talón'),
    ('07', '07_top_down', '07 | TOP-DOWN', 'horizontal direct overhead top-down flat lay view, heel on left and toe pointing RIGHT', 'vista cenital horizontal directa desde arriba, talón a la izquierda y puntera apuntando a la DERECHA (toe pointing RIGHT)'),
    ('08', '08_outsole', '08 | OUTSOLE', 'horizontal direct bottom outsole rubber tread view, heel on left and toe pointing RIGHT', 'vista inferior horizontal de la suela de goma con patrón de tracción, talón a la izquierda y puntera apuntando a la DERECHA (toe pointing RIGHT)')
]

def sanitize_filename(filename):
    name, _ = os.path.splitext(filename)
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)

def sort_product_photos(file_list):
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
        if fn.startswith('img_'):
            # Orden de cámara en sesiones D-G: 0=lateral, 1=rear, 2=medial, 3=front, último=top-down
            if index_in_order == 1:
                return (
                    f"Image {index_in_order} ({filename}): outer lateral profile of THIS sneaker -> replicate directly for panel [01 | LATERAL]",
                    f"Imagen {index_in_order} ({filename}): perfil lateral externo exacto de ESTA zapatilla -> replicar directamente en [01 | LATERAL]",
                    '01'
                )
            elif index_in_order == 2:
                return (
                    f"Image {index_in_order} ({filename}): direct rear heel counter view of THIS sneaker -> use directly for panel [06 | REAR]",
                    f"Imagen {index_in_order} ({filename}): vista trasera directa del contrafuerte del talón de ESTA zapatilla -> usar en [06 | REAR]",
                    '06'
                )
            elif index_in_order == 3:
                return (
                    f"Image {index_in_order} ({filename}): inner medial profile of THIS sneaker -> replicate directly for panel [02 | MEDIAL]",
                    f"Imagen {index_in_order} ({filename}): perfil medial interior exacto de ESTA zapatilla -> replicar directamente en [02 | MEDIAL]",
                    '02'
                )
            elif index_in_order == 4:
                return (
                    f"Image {index_in_order} ({filename}): direct front eye-level view of THIS single sneaker -> use directly for panel [05 | FRONT]",
                    f"Imagen {index_in_order} ({filename}): vista frontal directa de ESTA zapatilla -> usar en [05 | FRONT]",
                    '05'
                )
            else:
                return (
                    f"Image {index_in_order} ({filename}): overhead top-down / upper detail view of THIS sneaker -> use for panel [07 | TOP-DOWN]",
                    f"Imagen {index_in_order} ({filename}): vista cenital superior de ESTA zapatilla -> usar para [07 | TOP-DOWN]",
                    '07'
                )
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

MISPLACED_SHIFT_PREFIXES = ('IMG_0264', 'IMG_0269', 'IMG_0275', 'IMG_0280')

def find_primary_photo_for_angle(angle_code, sorted_files):
    """Encuentra la foto física que mejor corresponde al ángulo canónico."""
    fn_map = {
        '01_lateral': ['01-lateral', 'official-01'],
        '02_medial': ['02-medial', 'official-05'],
        '03_3-4_front': ['03-3-4-front', '03-frontal-3-4', '02-frontal-3-4'],
        '04_3-4_rear': ['04-3-4-rear', '03-trasera-3-4'],
        '05_front': ['05-front', 'official-03'],
        '06_rear': ['06-rear', '03-trasera', 'official-06'],
        '07_top_down': ['07-top-down', '04-superior', 'official-04'],
        '08_outsole': ['08-outsole', 'suela']
    }
    targets = fn_map.get(angle_code, [])
    for f in sorted_files:
        f_low = f.lower()
        for t in targets:
            if t in f_low and 'zoom' not in f_low:
                return f
    # Orden real de cámara IMG_: 0=lateral, 1=rear, 2=medial, 3=front, último=top-down
    img_clean = [f for f in sorted_files if f.lower().startswith('img_') and not f.upper().startswith(MISPLACED_SHIFT_PREFIXES)]
    if img_clean:
        idx_map = {
            '01_lateral': 0,
            '06_rear': 1 if len(img_clean) > 1 else None,
            '02_medial': 2 if len(img_clean) > 2 else None,
            '05_front': 3 if len(img_clean) > 3 else None,
            '07_top_down': (len(img_clean) - 1) if len(img_clean) >= 5 else None,
        }
        idx = idx_map.get(angle_code)
        if idx is not None and idx < len(img_clean):
            return img_clean[idx]
    return None

def build_8_individual_prompts(name, sku, group, real_folder, sorted_files, is_space_jam=False):
    """
    Construye los 8 prompts individuales (1:1 WebP sobre fondo blanco #FFFFFF)
    en EN y ES para los modos A y B.
    """
    context_files_str = ", ".join(sorted_files)
    
    if is_space_jam:
        anti_contam_en = (
            f"STRICT PRODUCT IDENTITY: Render ONLY the authentic Air Jordan 9 Retro OG \"Space Jam\" (SKU: {sku}). "
            "Replicate the exact black and white leather/durabuck silhouette, red Jumpman logos, round laces, and distinct sole. "
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
            "NEVER copy or blend features from Air Jordan 9 Space Jam or any other shoe."
        )
        anti_contam_es = (
            f"IDENTIDAD ESTRICTA DEL PRODUCTO: Renderizar ÚNICAMENTE la zapatilla auténtica {name} (SKU: {sku}, {group}). "
            "Replicar con fidelidad la silueta exacta, paleta de colores, paneles, materiales, costuras y logotipos mostrados en las fotos de referencia adjuntas. "
            "RESTRICCIÓN NEGATIVA: NO sustituir por ningún otro modelo ni silueta de calzado. "
            "NUNCA copiar ni mezclar características de las Air Jordan 9 Space Jam ni de ningún otro modelo ajeno."
        )

    cards_by_mode = {'mode_a': {'EN': [], 'ES': []}, 'mode_b': {'EN': [], 'ES': []}}

    for mode in ['mode_a', 'mode_b']:
        for code, angle_slug, angle_label, desc_en, desc_es in CANONICAL_PANELS:
            primary_file = find_primary_photo_for_angle(angle_slug, sorted_files)
            is_synth = primary_file is None
            
            # Ajustar descripción para 05 y 06 según modo
            if angle_slug == '05_front':
                if mode == 'mode_a':
                    shot_en = "matching pair of authentic sneakers standing side-by-side, left shoe direct front eye-level view, right shoe direct rear heel view, centered"
                    shot_es = "par de zapatillas auténticas lado a lado, zapatilla izquierda en vista frontal directa a nivel de ojo, zapatilla derecha en vista trasera directa, centradas"
                else:
                    shot_en = "single authentic sneaker in direct straight front eye-level view showing symmetrical toe box, tongue, and laces, centered"
                    shot_es = "una sola zapatilla auténtica en vista frontal directa a nivel de ojo mostrando simetría de puntera, lengüeta y cordones, centrada"
            elif angle_slug == '06_rear':
                if mode == 'mode_a':
                    shot_en = "matching pair of authentic sneakers standing side-by-side, dual direct rear heel views showing both heel counters and back branding, centered"
                    shot_es = "par de zapatillas auténticas lado a lado, doble vista trasera directa mostrando ambos contrafuertes del talón y marcas posteriores, centradas"
                else:
                    shot_en = "single authentic sneaker in direct straight rear heel counter view showing heel badge, collar, and sole width, centered"
                    shot_es = "una sola zapatilla auténtica en vista trasera directa del contrafuerte del talón mostrando insignia posterior, cuello y ancho de entresuela, centrada"
            else:
                shot_en = f"single authentic sneaker, {desc_en}, centered"
                shot_es = f"una sola zapatilla auténtica, {desc_es}, centrada"

            ref_file_name = f"{angle_slug.replace('_', '-')}.webp"
            ref_image_path = f"output_catalog/REFERENCIA/{ref_file_name}"

            role_spec_en = (
                f"INPUT IMAGES ROLES SPECIFICATION:\n"
                f"1. PRODUCT REFERENCE PHOTOS (Images 1 to {len(sorted_files)}: [{context_files_str}]):\n"
                f"   - SOLE source of design, sneaker silhouette, exact colorway, leather/suede/mesh materials, stitch patterns, logos, laces, and sole tread of {name} (SKU: {sku}, {group}).\n"
                f"2. CAMERA POSE & ANGLE GUIDE (LAST Image: 'output_catalog/REFERENCIA/{ref_file_name}'):\n"
                f"   - SOLE source of camera perspective angle, framing scale, position on pure white #FFFFFF canvas, and ground contact shadow.\n\n"
                f"CRITICAL: NEVER copy the shoe model, colors, or Jordan 9 Space Jam design from the LAST image (REFERENCIA). Use the REFERENCIA image strictly as a camera angle, framing, and white-studio pose guide ONLY. Render 100% the sneaker shown in the product reference photos."
            )

            role_spec_es = (
                f"ESPECIFICACIÓN DE ROLES DE IMÁGENES SUBIDAS:\n"
                f"1. FOTOS REALES DEL PRODUCTO (Imágenes 1 a {len(sorted_files)}: [{context_files_str}]):\n"
                f"   - Fuente ÚNICA de diseño, silueta de zapatilla, paleta exacta de colores, materiales (cuero/gamuza/malla), costuras, logotipos, cordones y patrón de suela de {name} (SKU: {sku}, {group}).\n"
                f"2. IMAGEN GUÍA DE ÁNGULO Y CÁMARA (ÚLTIMA Imagen: 'output_catalog/REFERENCIA/{ref_file_name}'):\n"
                f"   - Fuente ÚNICA de ángulo de cámara, perspectiva geométrica, escala de encuadre, posición sobre el lienzo blanco #FFFFFF y sombra en el suelo.\n\n"
                f"CRITICAL: NEVER copy the shoe model, colors, or Jordan 9 Space Jam design from the LAST image (REFERENCIA). Use the REFERENCIA image strictly as a camera angle, framing, and white-studio pose guide ONLY. Render 100% the sneaker shown in the product reference photos."
            )

            prompt_en = (
                f"Commercial e-commerce studio product photograph of {shot_en} ({name}, SKU: {sku}, {group}).\n\n"
                f"{role_spec_en}\n\n"
                f"{anti_contam_en}\n\n"
                "IMAGE CONSTRAINTS:\n"
                "- Exact 1:1 square aspect ratio.\n"
                "- Seamless solid pure white background (#FFFFFF).\n"
                "- High-end 5500K daylight dual-softbox commercial studio illumination.\n"
                "- f/8 edge-to-edge sharpness with generous white margins around the footwear.\n"
                "- Subtle grounded contact shadow on floor, zero floating artifacts.\n"
                "- Clean output: NO text, NO labels, NO watermark, NO borders, NO grid lines."
            )

            prompt_es = (
                f"Fotografía de producto comercial e-commerce de {shot_es} ({name}, SKU: {sku}, {group}).\n\n"
                f"{role_spec_es}\n\n"
                f"{anti_contam_es}\n\n"
                "RESTRICCIONES DE IMAGEN:\n"
                "- Relación de aspecto cuadrada exacta 1:1.\n"
                "- Fondo blanco puro sólido sin costuras (#FFFFFF).\n"
                "- Iluminación comercial de estudio balanceada dual-softbox a 5500K luz día neutra.\n"
                "- Nitidez de borde a borde f/8 con generoso margen blanco alrededor del calzado.\n"
                "- Sombra sutil de contacto en el piso perfectamente aterrizada, cero artefactos flotantes.\n"
                "- Salida limpia: CERO texto, CERO etiquetas, CERO marcas de agua, CERO bordes, CERO líneas de cuadrícula."
            )

            expected_fn = f"{real_folder}_{angle_slug}.webp"

            card_data = {
                'code': code,
                'slug': angle_slug,
                'label': angle_label,
                'expected_filename': expected_fn,
                'primary_file': primary_file or "Sintetizar en 3D (Sin foto física)",
                'ref_image_path': ref_image_path,
                'ref_file_name': ref_file_name,
                'is_synthesis': is_synth,
                'prompt_en': prompt_en,
                'prompt_es': prompt_es
            }
            cards_by_mode[mode]['EN'].append(card_data)
            cards_by_mode[mode]['ES'].append(card_data)

    return cards_by_mode

def build_bilingual_prompts(name, sku, group, real_folder, files, is_space_jam=False):
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

    folder_origin = f"_source_data/fotos/{group}/{real_folder}"

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

    prompts = {'EN': {}, 'ES': {}}

    for mode in ['mode_a', 'mode_b']:
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

        json_obj_en = {
            "task": "ecommerce_4k_sneaker_contact_sheet",
            "product": {
                "name": name,
                "sku": sku,
                "group": group,
                "source_folder": folder_origin,
                "real_folder_name": real_folder,
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

        json_obj_es = {
            "tarea": "hoja_de_contacto_ecommerce_calzado_4k",
            "producto": {
                "nombre": name,
                "sku": sku,
                "grupo": group,
                "carpeta_fuente": folder_origin,
                "nombre_carpeta_real": real_folder,
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
    print("AUDITORÍA Y GENERADOR DE PROMPTS FLOW (CRUCE OFICIAL SNKRS (1).xlsx)")
    print("=" * 80)

    products, sku_map, f_map = load_snkrs_mapping()
    print(f"✅ Mapeo 1:1 cargado: {len(products)} modelos validados.")
    print(f"\n{'#':<3} | {'Grupo':<8} | {'SKU':<12} | {'Nombre Modelo':<36} | {'Carpeta Real Exacta':<36} | {'Fotos':<5}")
    print("-" * 115)

    catalog = []
    thumb_tasks = []

    for item in products:
        idx = item['index']
        group = item['group']
        sku = item['sku']
        name = item['name']
        real_folder = item['folder']
        fpath = item['folder_path']

        # Listar y ordenar fotos determinísticamente (excluyendo fotos desplazadas de otro modelo)
        all_files = [
            f for f in os.listdir(fpath)
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))
            and not f.upper().startswith(MISPLACED_SHIFT_PREFIXES)
        ]
        sorted_files = sort_product_photos(all_files)
        img_count = len(sorted_files)

        if img_count == 0:
            raise RuntimeError(f"ERROR: La carpeta {fpath} no tiene fotos!")

        print(f"{idx+1:<3} | {group:<8} | {sku:<12} | {name[:35]:<36} | {real_folder[:35]:<36} | {img_count:<5}")

        sku_preview_dir = os.path.join('dist', 'assets', 'source-previews', sku)
        os.makedirs(sku_preview_dir, exist_ok=True)

        real_photos = []
        image_items = []
        for i, fn in enumerate(sorted_files, 1):
            clean_fn = sanitize_filename(fn)
            webp_name = f"{i:02d}_{clean_fn}.webp"
            dst_path = os.path.join(sku_preview_dir, webp_name)
            src_path = os.path.join(fpath, fn)
            rel_web_path = f"assets/source-previews/{sku}/{webp_name}"
            real_photos.append(rel_web_path)
            thumb_tasks.append((src_path, dst_path))
            image_items.append({
                'order': i,
                'filename': fn,
                'label': f"Image {i}: {fn}",
                'web_path': rel_web_path
            })

        is_space_jam = (idx == 0 or sku == 'IX6180-100')
        
        # 1. Prompts Cuadrícula 4x2
        grid_prompts, map_en, map_es, missing = build_bilingual_prompts(name, sku, group, real_folder, sorted_files, is_space_jam)
        
        # 2. Prompts 8 Individuales (1:1 WebP)
        individual_prompts = build_8_individual_prompts(name, sku, group, real_folder, sorted_files, is_space_jam)

        catalog.append({
            'index': idx,
            'index_display': idx + 1,
            'sku': sku,
            'rawSku': item['raw_code'],
            'name': name,
            'group': group,
            'product_dir': real_folder,
            'real_folder': real_folder,
            'full_path': fpath.replace('\\', '/'),
            'image_count': img_count,
            'image_files': sorted_files,
            'image_items': image_items,
            'real_photos': real_photos,
            'preview_primary': real_photos[0] if real_photos else f"assets/2-norm-std/{sku}/01-lateral.webp",
            'reference_mapping_en': map_en,
            'reference_mapping_es': map_es,
            'missing_angles': missing,
            'prompts': grid_prompts,
            'prompts_individual': individual_prompts,
            'prompt_text': grid_prompts['EN']['mode_b']['text'],
            'prompt_json': grid_prompts['EN']['mode_b']['json']
        })

    print("-" * 115)
    print(f"Procesando {len(thumb_tasks)} miniaturas WebP...")
    with ThreadPoolExecutor(max_workers=8) as executor:
        list(executor.map(process_thumbnail, thumb_tasks))

    out_js = os.path.join('dist', 'js', 'flow_nanobanana_data.js')
    data_payload = {
        'generated_at': '2026-11-24',
        'source_directory': '_source_data/fotos',
        'total_products': len(catalog),
        'groups': ['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D', 'Grupo E', 'Grupo F', 'Grupo G'],
        'catalog': catalog
    }

    with open(out_js, 'w', encoding='utf-8') as f:
        f.write("// Datos Oficiales Normalizados para Flow Workstation (45 Modelos)\n")
        f.write("const flowNanobananaData = ")
        json.dump(data_payload, f, indent=2, ensure_ascii=False)
        f.write(";\n")

    print(f"Archivo dist/js/flow_nanobanana_data.js generado con éxito!")

if __name__ == '__main__':
    main()
