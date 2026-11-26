#!/usr/bin/env python3
"""
scripts/process_real_photos_free.py
=============================================================================
Procesador local 100% gratuito e ilimitado con rembg:
Convierte las fotos reales de _source_data/fotos en imágenes de e-commerce:
- Fondo blanco puro #FFFFFF sin mesas ni paredes (rembg u2net)
- Sombra de contacto suave en la base
- Centrado automático por bounding box (fill_ratio = 0.82)
- Normalizado exacto a 1024x1024 (o 1200x1200) WebP calidad 90
- Nomenclatura oficial: output_catalog/{Grupo}/{Nombre_Carpeta_Real}/{Nombre_Carpeta_Real}_{angulo}.webp
- Reporte detallado de ángulos completados vs faltantes para Flow en output_catalog/estado_angulos.json
=============================================================================
"""

import os
import sys
import argparse
import time
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# Importar rembg
try:
    import rembg
    REMBG_AVAILABLE = True
except ImportError:
    REMBG_AVAILABLE = False

# Importar mapeo SNKRS
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
for p in [current_dir, parent_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from snkrs_mapping import load_snkrs_mapping, get_mapping_by_sku, get_mapping_by_real_folder
    from reference_metrics import align_and_canvas, get_metrics
except ImportError:
    from scripts.snkrs_mapping import load_snkrs_mapping, get_mapping_by_sku, get_mapping_by_real_folder
    from scripts.reference_metrics import align_and_canvas, get_metrics

CANONICAL_ANGLES = [
    ("01_lateral", "01-lateral", True),
    ("02_medial", "02-medial", True),
    ("03_3-4_front", "03-3-4-front", True),
    ("04_3-4_rear", "04-3-4-rear", True),
    ("05_front", "05-front", True),
    ("06_rear", "06-rear", True),
    ("07_top_down", "07-top-down", False),
    ("08_outsole", "08-outsole", False)
]

def detect_real_angles_for_folder(folder_path):
    """
    Detecta qué fotos reales de la sesión corresponden a cada ángulo canónico.
    Descarta o relega variantes -zoom si existe la versión completa.
    """
    if not os.path.exists(folder_path):
        return {}
    files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))])
    if not files:
        return {}

    detected = {}

    # 1. Grupos A, B, C y carpetas con prefijo canónico
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
                # Preferir archivo sin zoom, detalle o copia
                non_zoom = [c for c in candidates if 'zoom' not in c.lower() and 'detail' not in c.lower() and 'copia' not in c.lower()]
                chosen = non_zoom[0] if non_zoom else candidates[0]
                detected[slug] = chosen

    # 2. Grupos D, E, F, G con nombres de cámara IMG_XXXX
    # Orden real de cámara: 0=lateral, 1=rear, 2=medial, 3=front, último=top-down
    elif any(f.upper().startswith('IMG_') for f in files):
        misplaced = ('IMG_0264', 'IMG_0269', 'IMG_0275', 'IMG_0280')
        img_files = [f for f in files if f.upper().startswith('IMG_') and not f.upper().startswith(misplaced)]
        img_map = {
            '01_lateral': 0,
            '06_rear': 1 if len(img_files) > 1 else None,
            '02_medial': 2 if len(img_files) > 2 else None,
            '05_front': 3 if len(img_files) > 3 else None,
            '07_top_down': (len(img_files) - 1) if len(img_files) >= 5 else None,
        }
        for slug, idx in img_map.items():
            if idx is not None and idx < len(img_files):
                detected[slug] = img_files[idx]

    return detected

def process_single_photo(
    src_path,
    out_path,
    session,
    angle_slug="01_lateral",
    target_size=1024,
    quality=90
):
    """
    Procesa 1 foto real calibrada con output_catalog/REFERENCIA/:
    - Remueve fondo con rembg (u2net)
    - Aplica encuadre, escala armónica y línea de suelo exacta según REFERENCIA
    - Sombra de contacto calibrada en piso
    - Guarda en formato WebP con calidad configurable
    """
    im = Image.open(src_path)
    # Reducir si es excesivamente grande para acelerar rembg preservando máxima fidelidad
    if max(im.size) > 2048:
        im.thumbnail((2048, 2048), Image.Resampling.LANCZOS)
        
    rgba = rembg.remove(im, session=session)
    
    # Calibración exacta con el estándar maestro REFERENCIA
    final_rgb = align_and_canvas(
        rgba_image=rgba,
        angle_slug=angle_slug,
        target_size=target_size
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    final_rgb.save(out_path, 'WEBP', quality=quality)
    return True

    out_path.parent.mkdir(parents=True, exist_ok=True)
    final_rgb.save(out_path, 'WEBP', quality=quality)
    return True

def process_product_free(product_info, args, session=None):
    """
    Procesa un producto extrayendo y aislando todos sus ángulos reales existentes.
    Retorna un diccionario de estado con los ángulos completados y faltantes.
    """
    sku = product_info["sku"]
    group = product_info["group"]
    folder = product_info.get("real_folder") or product_info.get("folder", "")
    name = product_info["name"]
    folder_path = product_info.get("folder_path") or os.path.join("_source_data", "fotos", group, folder)

    out_dir = Path("output_catalog") / group / folder
    detected_real = detect_real_angles_for_folder(folder_path)

    completed_angles = []
    missing_angles = []
    skipped_existing = []

    print("\n" + "=" * 80)
    print(f"PRODUCTO: #{product_info['index']+1:02d} | [{group}] {sku} | {name}")
    print(f"  Carpeta Real : {folder}")
    print(f"  Fotos sesión : {len(detected_real)} identificadas de 8 posibles")
    print(f"  Destino WebP : {out_dir}")
    print("-" * 80)

    for slug, _, add_shadow in CANONICAL_ANGLES:
        out_filename = f"{folder}_{slug}.webp"
        out_file_path = out_dir / out_filename
        
        if slug in detected_real:
            src_filename = detected_real[slug]
            src_path = os.path.join(folder_path, src_filename)
            
            if out_file_path.exists() and not args.force:
                skipped_existing.append(slug)
                completed_angles.append(slug)
                print(f"  ✅ [{slug}] YA EXISTE -> {out_filename} (Omitiendo)")
            elif args.dry_run:
                completed_angles.append(slug)
                print(f"  🔍 [DRY-RUN] [{slug}] Procesaría {src_filename} -> {out_filename}")
            else:
                t0 = time.time()
                ok = process_single_photo(
                    src_path,
                    out_file_path,
                    session,
                    angle_slug=slug,
                    target_size=args.size,
                    quality=args.quality
                )
                dt = time.time() - t0
                if ok:
                    completed_angles.append(slug)
                    print(f"  ✨ [{slug}] Creado en {dt:.1f}s desde {src_filename} -> {out_filename}")
                else:
                    missing_angles.append(slug)
                    print(f"  ❌ [{slug}] Error procesando {src_filename}")
        else:
            missing_angles.append(slug)
            print(f"  ⏳ [{slug}] FALTANTE (Completar con Flow Web)")

    return {
        "index": product_info["index"],
        "index_display": product_info["index"] + 1,
        "group": group,
        "sku": sku,
        "name": name,
        "folder": folder,
        "total_angulos": 8,
        "completados_count": len(completed_angles),
        "faltantes_count": len(missing_angles),
        "completados": completed_angles,
        "faltantes": missing_angles,
        "origen_fotos": detected_real
    }

def main():
    parser = argparse.ArgumentParser(
        description="Procesador gratuito local con rembg: Aislar fotos reales en 1024x1024 WebP sobre #FFFFFF."
    )
    parser.add_argument("--product", type=str, help="Nombre de carpeta real del producto (ej. '01_Air_Jordan_9_Space_Jam')")
    parser.add_argument("--sku", type=str, help="SKU del producto (ej. 'IX6180-100')")
    parser.add_argument("--group", type=str, help="Filtrar por grupo (ej. 'Grupo A')")
    parser.add_argument("--all", action="store_true", help="Procesar los 45 modelos en lote")
    parser.add_argument("--size", type=int, choices=[1024, 1200], default=1024, help="Tamaño cuadrado en px (default: 1024)")
    parser.add_argument("--fill-ratio", type=float, default=0.82, help="Proporción del calzado en el lienzo (default: 0.82)")
    parser.add_argument("--quality", type=int, default=90, help="Calidad WebP (default: 90)")
    parser.add_argument("--force", action="store_true", help="Sobrescribir archivos existentes")
    parser.add_argument("--dry-run", action="store_true", help="Mostrar qué fotos procesaría sin ejecutar rembg")

    args = parser.parse_args()

    # Cargar catálogo mapeado ignorando la carpeta especial REFERENCIA
    all_products, sku_map, f_map = load_snkrs_mapping()
    all_products = [p for p in all_products if p.get('folder') != 'REFERENCIA' and p.get('real_folder') != 'REFERENCIA']
    if not all_products:
        print("❌ Error cargando catálogo desde SNKRS (1).xlsx.")
        sys.exit(1)

    target_products = []
    if args.product:
        p = get_mapping_by_real_folder(args.product)
        if p:
            target_products = [p]
        else:
            print(f"❌ Error: Producto '{args.product}' no encontrado.")
            sys.exit(1)
    elif args.sku:
        p = get_mapping_by_sku(args.sku)
        if p:
            target_products = [p]
        else:
            print(f"❌ Error: SKU '{args.sku}' no encontrado.")
            sys.exit(1)
    elif args.group:
        target_products = [p for p in all_products if p["group"].lower() == args.group.lower()]
        if not target_products:
            print(f"❌ Error: No hay productos en '{args.group}'.")
            sys.exit(1)
    elif args.all:
        target_products = all_products
    else:
        print("Debe especificar --product, --sku, --group o --all.")
        parser.print_help()
        sys.exit(0)

    # Validar rembg
    session = None
    if not args.dry_run:
        if not REMBG_AVAILABLE:
            print("❌ rembg no está instalado. Ejecuta: pip install rembg onnxruntime")
            sys.exit(1)
        print("⚡ Inicializando modelo rembg (u2net)...")
        t_init = time.time()
        session = rembg.new_session("u2net")
        print(f"✅ Modelo cargado en {time.time() - t_init:.2f}s.")

    print(f"\n🚀 Iniciando procesamiento local | Productos: {len(target_products)} | Tamaño: {args.size}x{args.size} WebP | Dry-run: {args.dry_run}")

    catalog_status = []
    total_reales_generados = 0
    total_faltantes_flow = 0

    for p in target_products:
        res = process_product_free(p, args, session=session)
        catalog_status.append(res)
        total_reales_generados += res["completados_count"]
        total_faltantes_flow += res["faltantes_count"]

    # Guardar / Actualizar reporte global en output_catalog/estado_angulos.json
    out_report_path = Path("output_catalog") / "estado_angulos.json"
    out_report_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Si procesamos un subconjunto, fusionar con el reporte previo si existe
    existing_report = {}
    if out_report_path.exists():
        try:
            with open(out_report_path, "r", encoding="utf-8") as f:
                existing_report = json.load(f).get("productos", {})
        except Exception:
            existing_report = {}

    for item in catalog_status:
        existing_report[item["folder"]] = item

    final_report_payload = {
        "fecha_actualizacion": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_productos_registrados": len(existing_report),
        "resumen_sesion": {
            "procesados_ahora": len(target_products),
            "angulos_listos_reales": total_reales_generados,
            "angulos_faltantes_flow": total_faltantes_flow
        },
        "productos": existing_report
    }

    with open(out_report_path, "w", encoding="utf-8") as f:
        json.dump(final_report_payload, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 80)
    print("📊 RESUMEN DE PROCESAMIENTO LOCAL GRATUITO:")
    print(f"  • Productos procesados : {len(target_products)}")
    print(f"  • Ángulos listos reales: {total_reales_generados} WebP (Fondo #FFFFFF puro, centrados, 1K)")
    print(f"  • Ángulos para Flow    : {total_faltantes_flow} ángulos faltantes")
    print(f"  • Reporte guardado en  : {out_report_path}")
    print("=" * 80)

if __name__ == "__main__":
    main()
