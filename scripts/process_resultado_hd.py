#!/usr/bin/env python3
"""
scripts/process_resultado_hd.py
=============================================================================
Procesa y genera el catálogo final en ALTA DEFINICIÓN (2048x2048 PNG)
para TODOS los 45 modelos bajo:
  RESULTADO/{Grupo}/{Nombre_Carpeta_Real}/

Estándar de calidad:
- Estándar Maestro: output_catalog/REFERENCIA-HD (2048x2048 PNG)
- Fondo: Blanco puro #FFFFFF
- Sombra de contacto suave en base (grounded baseline calibrada a ~1475-1503 px)
- Vistas cenitales (07_top_down, 08_outsole) centradas armónicamente
- 8 tomas canónicas EXACTAS y DISTINTAS por modelo (01-lateral.png a 08-outsole.png)
- Cero duplicados ni fotos repetidas: detección y descarte estricto de duplicados
=============================================================================
"""

import os
import sys
import time
import json
from pathlib import Path
from PIL import Image, ImageOps
import numpy as np

# Configurar sys.path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)
for p in [CURRENT_DIR, PROJECT_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)

from reference_metrics import align_and_canvas, compute_reference_metrics
from snkrs_mapping import load_snkrs_mapping

try:
    import rembg
    REMBG_AVAILABLE = True
except ImportError:
    REMBG_AVAILABLE = False
    print("Warning: rembg not installed!")

FOTOS_HD_BASE = os.path.join(PROJECT_DIR, "_source_data", "fotos-HD")
REF_HD_DIR = os.path.join(PROJECT_DIR, "output_catalog", "REFERENCIA-HD")
OUTPUT_RESULTADO = os.path.join(PROJECT_DIR, "RESULTADO")

CANONICAL_ANGLES = [
    ("01_lateral", "01-lateral.png"),
    ("02_medial", "02-medial.png"),
    ("03_3-4_front", "03-3-4-front.png"),
    ("04_3-4_rear", "04-3-4-rear.png"),
    ("05_front", "05-front.png"),
    ("06_rear", "06-rear.png"),
    ("07_top_down", "07-top-down.png"),
    ("08_outsole", "08-outsole.png"),
]

def clean_stray_root_files():
    """Limpia archivos sueltos en el directorio raíz de RESULTADO."""
    if os.path.exists(OUTPUT_RESULTADO):
        for item in os.listdir(OUTPUT_RESULTADO):
            item_path = os.path.join(OUTPUT_RESULTADO, item)
            if os.path.isfile(item_path):
                try:
                    os.remove(item_path)
                except Exception:
                    pass

def detect_source_hd_photos(folder_path):
    """
    Detecta y mapea las fotos reales en fotos-HD para cada ángulo canónico,
    descartando duplicados, variantes de zoom y copias.
    """
    if not os.path.exists(folder_path):
        return {}
    
    files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    if not files:
        return {}

    detected = {}
    has_named = any(f.lower().startswith(('01-', '02-', '03-', '04-', '05-', '06-', '07-', '08-')) for f in files)

    if has_named:
        patterns = {
            '01_lateral': ['01-lateral'],
            '02_medial': ['02-medial'],
            '03_3-4_front': ['03-3-4-front', '03-frontal-3-4', '02-frontal-3-4'],
            '04_3-4_rear': ['04-3-4-rear', '03-trasera-3-4'],
            '05_front': ['05-front'],
            '06_rear': ['06-rear', '03-trasera'],
            '07_top_down': ['07-top-down', '04-superior'],
            '08_outsole': ['08-outsole', 'suela']
        }
        for slug, prefixes in patterns.items():
            candidates = []
            for f in files:
                f_low = f.lower()
                for p in prefixes:
                    if p in f_low:
                        candidates.append(f)
                        break
            if candidates:
                # Filtrar estrictamente zoom, detail, copia
                clean_cands = [c for c in candidates if 'zoom' not in c.lower() and 'detail' not in c.lower() and 'copia' not in c.lower()]
                chosen = clean_cands[0] if clean_cands else candidates[0]
                detected[slug] = os.path.join(folder_path, chosen)

    elif any(f.upper().startswith('IMG_') for f in files):
        # Excluir fotos top-down del modelo anterior que quedaron en la carpeta siguiente (Grupo G)
        misplaced_prefixes = ('IMG_0264', 'IMG_0269', 'IMG_0275', 'IMG_0280')
        img_files = [f for f in files if f.upper().startswith('IMG_') and not f.upper().startswith(misplaced_prefixes)]
        # Orden real en sesión fotográfica D-G: 0=lateral, 1=rear, 2=medial, 3=front, último=top-down
        img_map = {
            '01_lateral': 0,
            '06_rear': 1 if len(img_files) > 1 else None,
            '02_medial': 2 if len(img_files) > 2 else None,
            '05_front': 3 if len(img_files) > 3 else None,
            '07_top_down': (len(img_files) - 1) if len(img_files) >= 5 else None,
        }
        for slug, idx in img_map.items():
            if idx is not None and idx < len(img_files):
                detected[slug] = os.path.join(folder_path, img_files[idx])

        # Mapa cruzado exacto para los top-down desplazados en F/06 y Grupo G
        folder_name = os.path.basename(folder_path)
        cross_top_down = {
            '06_Air_Jordan_1_Low_Banned': os.path.join(FOTOS_HD_BASE, 'Grupo G', '01_Jordan_Negro_Elephant_Print', 'IMG_0264.png'),
            '01_Jordan_Negro_Elephant_Print': os.path.join(FOTOS_HD_BASE, 'Grupo G', '02_Jordan_Gris_Negro', 'IMG_0269.png'),
            '02_Jordan_Gris_Negro': os.path.join(FOTOS_HD_BASE, 'Grupo G', '03_Nike_Air_Force_1_Negro', 'IMG_0275.png'),
            '03_Nike_Air_Force_1_Negro': os.path.join(FOTOS_HD_BASE, 'Grupo G', '04_Nike_Air_Force_1_Azul_Marino', 'IMG_0280.png'),
        }
        if folder_name in cross_top_down and os.path.exists(cross_top_down[folder_name]):
            detected['07_top_down'] = cross_top_down[folder_name]

    return detected

def get_fallback_angle(group, folder_name, sku, angle_slug):
    """
    Busca fuente confiable para ángulos no fotografiados en la sesión real
    (típicamente 03-3-4-front, 04-3-4-rear, 08-outsole) desde las carpetas
    maestras calibradas (output_catalog, cortes-flow o dist/assets).
    """
    candidates = [
        # 1. output_catalog/{group}/{folder_name}/{folder_name}_{angle_slug}.webp
        os.path.join(PROJECT_DIR, "output_catalog", group, folder_name, f"{folder_name}_{angle_slug}.webp"),
        # 2. cortes-flow/{sku}/{angle_slug}.webp / .jpg
        os.path.join(PROJECT_DIR, "dist", "assets", "cortes-flow", sku, f"{angle_slug.replace('_', '-')}.webp"),
        os.path.join(PROJECT_DIR, "dist", "assets", "cortes-flow", sku, f"{angle_slug.replace('_', '-')}.jpg"),
        # 3. output_catalog/{group_u}/{sku}/{sku}_{angle_slug}.webp
        os.path.join(PROJECT_DIR, "output_catalog", group.replace(" ", "_"), sku, f"{sku}_{angle_slug}.webp"),
        # 4. dist/assets/2-norm-std/{sku}/{angle}.webp
        os.path.join(PROJECT_DIR, "dist", "assets", "2-norm-std", sku, f"{angle_slug.replace('_', '-')}.webp"),
    ]
    
    for c in candidates:
        if os.path.exists(c) and os.path.getsize(c) > 2000:
            return c
    return None

def process_all_products(force=False, target_angles=None):
    t0 = time.time()
    mapping_list, sku_map, folder_map = load_snkrs_mapping()
    clean_stray_root_files()
    
    angles_filter = [slug for slug, _ in CANONICAL_ANGLES if (target_angles is None or slug in target_angles)]

    print("=" * 80)
    print("👟 INICIANDO PIPELINE DE PRODUCCIÓN HD (2048x2048 PNG)")
    print(f"Estándar Maestro: {REF_HD_DIR}")
    print(f"Directorio Destino: {OUTPUT_RESULTADO}")
    print(f"Ángulos a procesar: {angles_filter}")
    print(f"Total productos en catálogo: {len(mapping_list)}")
    print("=" * 80)

    # Precalcular y cachear métricas maestras HD
    metrics_hd = compute_reference_metrics(REF_HD_DIR)
    
    # Crear sesión rembg compartida
    session = rembg.new_session("u2net") if REMBG_AVAILABLE else None

    total_images_generated = 0
    total_images_skipped = 0
    total_products_completed = 0
    
    for item in mapping_list:
        idx = item['index'] + 1
        sku = item['sku']
        group = item['group']
        folder = item['folder']
        name = item['name']

        target_dir = os.path.join(OUTPUT_RESULTADO, group, folder)
        os.makedirs(target_dir, exist_ok=True)

        source_hd_folder = os.path.join(FOTOS_HD_BASE, group, folder)
        real_photos = detect_source_hd_photos(source_hd_folder)

        print(f"\n[#{idx:02d}] {group} | {sku} | {folder}")

        product_angles_ready = 0

        for slug, filename in CANONICAL_ANGLES:
            target_path = os.path.join(target_dir, filename)

            # Si este ángulo no está en el filtro de ejecución, saltar
            if target_angles is not None and slug not in target_angles:
                if os.path.exists(target_path):
                    product_angles_ready += 1
                continue

            # Si ya existe y no forzamos reescritura
            if os.path.exists(target_path) and not force and os.path.getsize(target_path) > 10000:
                total_images_skipped += 1
                product_angles_ready += 1
                continue

            src_img_path = real_photos.get(slug)
            is_from_real_photo = src_img_path is not None

            if not is_from_real_photo:
                # Buscar fuente de respaldo de alta fidelidad
                src_img_path = get_fallback_angle(group, folder, sku, slug)

            if not src_img_path:
                print(f"  ⚠️ Sin fuente disponible para {slug} ({filename})")
                continue

            try:
                # 1. Cargar imagen origen
                with Image.open(src_img_path) as im:
                    im = ImageOps.exif_transpose(im)
                    if im.mode not in ("RGB", "RGBA"):
                        im = im.convert("RGB")
                    
                    # 2. Aislar producto eliminando fondo
                    # Optimización: Reducir a 1600px para rembg preservando máxima fidelidad visual
                    w, h = im.size
                    max_d = max(w, h)
                    if max_d > 1600:
                        ratio = 1600.0 / max_d
                        im_small = im.resize((int(round(w * ratio)), int(round(h * ratio))), Image.Resampling.LANCZOS)
                    else:
                        im_small = im

                    rgba = rembg.remove(im_small, session=session)

                # 3. Calibrar encuadre, escala, baseline y sombra con REFERENCIA-HD a 2048x2048
                calibrated = align_and_canvas(
                    rgba_image=rgba,
                    angle_slug=slug,
                    target_size=2048,
                    ref_dir=REF_HD_DIR
                )

                # 4. Guardar en PNG 2048x2048 (RGB)
                calibrated.save(target_path, format="PNG", compress_level=4)
                total_images_generated += 1
                product_angles_ready += 1
                origin_tag = "FOTO-HD REAL" if is_from_real_photo else f"CALIBRADO ({os.path.basename(src_img_path)})"
                print(f"  ✨ {filename:17s} -> 2048x2048 OK [{origin_tag}]")

            except Exception as e:
                print(f"  ❌ Error procesando {slug}: {e}")

        if product_angles_ready == 8:
            total_products_completed += 1
            print(f"  ✅ Producto Completo: 8/8 tomas canónicas HD en {target_dir}")
        else:
            print(f"  ⏳ Producto con {product_angles_ready}/8 tomas")

    t1 = time.time()
    print("\n" + "=" * 80)
    print("📊 RESUMEN FINAL DEL PROCESAMIENTO HD:")
    print(f"  • Tiempo total transcurrido       : {t1 - t0:.2f} segundos")
    print(f"  • Productos 100% completos (8/8)  : {total_products_completed} de 45")
    print(f"  • Imágenes generadas ahora        : {total_images_generated}")
    print(f"  • Imágenes ya existentes          : {total_images_skipped}")
    print(f"  • Total imágenes en RESULTADO     : {total_images_generated + total_images_skipped} (esperadas: 360)")
    print("=" * 80)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Procesador HD para RESULTADO/")
    parser.add_argument("--force", action="store_true", help="Forzar reescritura de imágenes existentes")
    parser.add_argument("--angles", type=str, default=None, help="Lista separada por comas de ángulos a procesar (ej. 05_front,06_rear,07_top_down)")
    args = parser.parse_args()

    target_angles = [a.strip() for a in args.angles.split(",")] if args.angles else None
    process_all_products(force=args.force, target_angles=target_angles)
