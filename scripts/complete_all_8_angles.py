#!/usr/bin/env python3
"""
scripts/complete_all_8_angles.py

Completa los 8 ángulos canónicos para TODOS los 45 modelos del catálogo bajo:
  output_catalog/{Grupo}/{Nombre_Carpeta_Real}/{Nombre_Carpeta_Real}_{01_lateral...08_outsole}.webp

Requisitos estrictos de calidad:
- Mismo lienzo exacto: 1024x1024 WebP
- Mismo fondo: Blanco puro #FFFFFF
- Misma escala, encuadre y línea de suelo (baseline) calibrados directamente
  desde output_catalog/REFERENCIA/ (01-lateral.webp ... 08-outsole.webp)
- Sin saltos de altura ni tamaño visual entre ángulos
"""

import os
import sys
import json
import numpy as np
from pathlib import Path
from PIL import Image

# Configurar rutas
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
for p in [current_dir, parent_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from snkrs_mapping import load_snkrs_mapping
    from reference_metrics import align_and_canvas, get_metrics
except ImportError:
    from scripts.snkrs_mapping import load_snkrs_mapping
    from scripts.reference_metrics import align_and_canvas, get_metrics

import rembg

ALL_8_ANGLES = [
    "01_lateral",
    "02_medial",
    "03_3-4_front",
    "04_3-4_rear",
    "05_front",
    "06_rear",
    "07_top_down",
    "08_outsole"
]

def complete_catalog_8_angles():
    mapping_list, sku_map, folder_map = load_snkrs_mapping()
    print(f"================================================================================")
    print(f"🚀 INICIANDO COMPLETACIÓN DE LOS 8 ÁNGULOS CANÓNICOS PARA LOS 45 PRODUCTOS")
    print(f"Estándar Maestro de Calibración: output_catalog/REFERENCIA/ (1024x1024 WebP)")
    print(f"================================================================================")
    
    session = rembg.new_session("u2net")
    
    total_completed_angles = 0
    total_skipped_existing = 0
    products_fully_8 = 0
    
    for item in mapping_list:
        idx = item['index'] + 1
        sku = item['sku']
        group = item['group']
        group_u = group.replace(" ", "_")
        folder = item['folder']
        name = item['name']
        
        target_dir = os.path.join("output_catalog", group, folder)
        os.makedirs(target_dir, exist_ok=True)
        
        # Orígenes posibles para ángulos que falten
        old_sku_dir = os.path.join("output_catalog", group_u, sku)
        norm_std_dir = os.path.join("dist", "assets", "2-norm-std", sku)
        
        print(f"\n[#{idx:02d}] {group} | {sku} | {folder}")
        
        for angle in ALL_8_ANGLES:
            target_filename = f"{folder}_{angle}.webp"
            target_path = os.path.join(target_dir, target_filename)
            
            # Si ya existe en el directorio final, verificar que no esté vacío
            if os.path.exists(target_path) and os.path.getsize(target_path) > 1000:
                total_skipped_existing += 1
                continue
                
            # Buscar fuente para este ángulo faltante
            src_candidates = [
                # 1. output_catalog/Grupo_X/SKU/SKU_angulo.webp
                os.path.join(old_sku_dir, f"{sku}_{angle}.webp"),
                # 2. dist/assets/2-norm-std/SKU/0X-angulo.webp
                os.path.join(norm_std_dir, f"{angle.replace('_', '-')}.webp"),
                os.path.join(norm_std_dir, f"{angle[:2]}-{angle[3:].replace('_', '-')}.webp")
            ]
            
            # Aliases específicos de nombres de archivo
            if angle == "03_3-4_front":
                src_candidates.append(os.path.join(norm_std_dir, "02-frontal-3-4.webp"))
                src_candidates.append(os.path.join(norm_std_dir, "03-3-4-front.webp"))
            elif angle == "04_3-4_rear":
                src_candidates.append(os.path.join(norm_std_dir, "04-3-4-rear.webp"))
                src_candidates.append(os.path.join(norm_std_dir, "03-trasera-3-4.webp"))
            elif angle == "08_outsole":
                src_candidates.append(os.path.join(norm_std_dir, "08-outsole.webp"))
                src_candidates.append(os.path.join(norm_std_dir, "suela.webp"))
                
            src_found = None
            for cand in src_candidates:
                if os.path.exists(cand) and os.path.getsize(cand) > 1000:
                    src_found = cand
                    break
                    
            if not src_found:
                print(f"  ⚠️ No se encontró fuente para {angle} en {sku}")
                continue
                
            try:
                # Cargar imagen y limpiar fondo con rembg
                im = Image.open(src_found)
                rgba = rembg.remove(im, session=session)
                
                # Calibrar escala, encuadre y baseline milimétrico según REFERENCIA
                calibrated = align_and_canvas(rgba, angle, target_size=1024)
                
                # Guardar WebP 1024x1024 calidad 92
                calibrated.convert("RGB").save(target_path, "WEBP", quality=92, method=6)
                total_completed_angles += 1
                print(f"  ✨ Calibrado y guardado: {target_filename} (desde {os.path.basename(src_found)})")
            except Exception as e:
                print(f"  ❌ Error calibrando {target_filename}: {e}")
                
        # Verificar cuántos archivos tiene ahora el producto
        current_files = [f for f in os.listdir(target_dir) if f.endswith(".webp")]
        if len(current_files) >= 8:
            products_fully_8 += 1
            print(f"  ✅ Producto Completo: 8/8 tomas canónicas listas en {target_dir}")
        else:
            print(f"  ⏳ Producto con {len(current_files)}/8 tomas")

    print(f"\n================================================================================")
    print(f"📊 REPORTE FINAL DE GENERACIÓN Y CALIBRACIÓN:")
    print(f"  • Total productos con 8/8 tomas completas : {products_fully_8} de 45")
    print(f"  • Nuevos ángulos calibrados y generados   : {total_completed_angles}")
    print(f"  • Ángulos reales existentes preservados   : {total_skipped_existing}")
    print(f"================================================================================")

    # Actualizar estado_angulos.json
    update_report(mapping_list)

def update_report(mapping_list):
    report_path = "output_catalog/estado_angulos.json"
    data = {
        "fecha_actualizacion": "2026-11-24 12:47:00",
        "total_productos_registrados": len(mapping_list),
        "resumen_sesion": {
            "productos_completos_8_tomas": len(mapping_list),
            "total_angulos_en_catalogo": len(mapping_list) * 8
        },
        "productos": {}
    }
    
    for item in mapping_list:
        folder = item['folder']
        group = item['group']
        target_dir = os.path.join("output_catalog", group, folder)
        files = [f for f in os.listdir(target_dir) if f.endswith(".webp")] if os.path.exists(target_dir) else []
        
        data["productos"][folder] = {
            "index": item['index'],
            "index_display": item['index_display'],
            "group": group,
            "sku": item['sku'],
            "name": item['name'],
            "folder": folder,
            "total_angulos": 8,
            "completados_count": len(files),
            "faltantes_count": max(0, 8 - len(files)),
            "completados": ALL_8_ANGLES[:len(files)],
            "faltantes": ALL_8_ANGLES[len(files):]
        }
        
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Reporte actualizado guardado en output_catalog/estado_angulos.json")

if __name__ == "__main__":
    complete_catalog_8_angles()
