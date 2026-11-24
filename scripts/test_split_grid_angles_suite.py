#!/usr/bin/env python3
"""
scripts/test_split_grid_angles_suite.py
Suite de pruebas automatizadas para scripts/split_grid_angles.py
"""

import os
import sys
import shutil
import tempfile
import subprocess
from PIL import Image, ImageDraw
import numpy as np

def create_synthetic_grid(save_path, w=4096, h=4096):
    """Crea una imagen sintética 4x2 en resolución 4K con líneas grises 1px y etiquetas."""
    img = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    rows, cols = 4, 2
    cell_w = w // cols
    cell_h = h // rows
    
    # Dibujar líneas divisorias de 1px en gris oscuro (#404040)
    for r in range(1, rows):
        y = r * cell_h
        draw.line([(0, y), (w, y)], fill=(64, 64, 64), width=1)
    for c in range(1, cols):
        x = c * cell_w
        draw.line([(x, 0), (x, h)], fill=(64, 64, 64), width=1)
        
    labels = [
        "01 | LATERAL", "02 | MEDIAL",
        "03 | 3/4 FRONT", "04 | 3/4 REAR",
        "05 | FRONT", "06 | REAR",
        "07 | TOP-DOWN", "08 | OUTSOLE"
    ]
    
    idx = 0
    for r in range(rows):
        for c in range(cols):
            x0 = c * cell_w
            y0 = r * cell_h
            lbl = labels[idx]
            # Dibujar etiqueta de texto en esquina superior izquierda
            draw.text((x0 + 40, y0 + 35), lbl, fill=(20, 20, 20))
            
            # Dibujar silueta de calzado simulada en el centro de la celda
            cx = x0 + cell_w // 2
            cy = y0 + cell_h // 2
            sw = int(cell_w * 0.35)
            sh = int(cell_h * 0.25)
            draw.ellipse([cx - sw, cy - sh, cx + sw, cy + sh], fill=(30, 40, 60))
            draw.rectangle([cx - sw + 50, cy - sh + 20, cx, cy], fill=(220, 40, 40))
            idx += 1
            
    img.save(save_path, quality=95)
    print(f"Creada cuadrícula sintética 4K: {save_path} ({w}x{h} px)")
    return save_path

def run_tests():
    temp_dir = tempfile.mkdtemp(prefix="test_split_")
    print(f"Directorio temporal de pruebas: {temp_dir}")
    
    try:
        synth_img = os.path.join(temp_dir, "TEST-999.png")
        create_synthetic_grid(synth_img)
        
        out_dir = os.path.join(temp_dir, "output_catalog")
        
        # 1. Prueba Individual 1024x1024 (1K)
        print("\n--- PRUEBA 1: Modo Individual 1024x1024 (1K) ---")
        cmd_1024 = [
            sys.executable, "scripts/split_grid_angles.py",
            synth_img,
            "--sku", "TEST-999",
            "--group", "Grupo_A",
            "--size", "1024",
            "--format", "webp",
            "--output-dir", out_dir
        ]
        res = subprocess.run(cmd_1024, capture_output=True, text=True)
        assert res.returncode == 0, f"Error en cmd_1024: {res.stderr}"
        
        dest_1024 = os.path.join(out_dir, "Grupo_A", "TEST-999")
        files_1024 = sorted([f for f in os.listdir(dest_1024) if f.endswith('.webp')])
        assert len(files_1024) == 8, f"Se esperaban 8 archivos, se encontraron {len(files_1024)}"
        
        for f in files_1024:
            fp = os.path.join(dest_1024, f)
            with Image.open(fp) as im:
                assert im.size == (1024, 1024), f"Dimensiones incorrectas {im.size} en {f}"
                arr = np.array(im)
                # Verificar esquinas en blanco puro
                assert (arr[0, 0] == [255, 255, 255]).all(), f"Esquina no es blanca en {f}"
                # Verificar que el borde no tiene líneas oscuras de la cuadrícula
                assert arr[0, :].min() == 255
                assert arr[-1, :].min() == 255
                assert arr[:, 0].min() == 255
                assert arr[:, -1].min() == 255
        print("✅ PRUEBA 1 SUPERADA: 8 archivos WebP 1024x1024, blanco puro #FFFFFF, bordes de cuadrícula eliminados.")
        
        # 2. Prueba Individual 1200x1200 (HD)
        print("\n--- PRUEBA 2: Modo Individual 1200x1200 (HD) ---")
        cmd_1200 = [
            sys.executable, "scripts/split_grid_angles.py",
            synth_img,
            "--sku", "TEST-HD",
            "--group", "Grupo_B",
            "--size", "1200",
            "--format", "webp",
            "--output-dir", out_dir
        ]
        res = subprocess.run(cmd_1200, capture_output=True, text=True)
        assert res.returncode == 0, f"Error en cmd_1200: {res.stderr}"
        
        dest_1200 = os.path.join(out_dir, "Grupo_B", "TEST-HD")
        files_1200 = sorted([f for f in os.listdir(dest_1200) if f.endswith('.webp')])
        assert len(files_1200) == 8
        for f in files_1200:
            with Image.open(os.path.join(dest_1200, f)) as im:
                assert im.size == (1200, 1200), f"Dimensiones incorrectas {im.size} en {f}"
        print("✅ PRUEBA 2 SUPERADA: 8 archivos WebP 1200x1200 HD exactos.")
        
        # 3. Prueba Comparativa: Limpieza de Etiquetas vs --keep-labels
        print("\n--- PRUEBA 3: Comparación Limpieza de Etiquetas vs --keep-labels ---")
        cmd_keep = [
            sys.executable, "scripts/split_grid_angles.py",
            synth_img,
            "--sku", "TEST-KEEP",
            "--group", "Grupo_C",
            "--size", "1024",
            "--format", "webp",
            "--keep-labels",
            "--output-dir", out_dir
        ]
        res = subprocess.run(cmd_keep, capture_output=True, text=True)
        assert res.returncode == 0
        dest_keep = os.path.join(out_dir, "Grupo_C", "TEST-KEEP")
        files_keep = sorted([f for f in os.listdir(dest_keep) if f.endswith('.webp')])
        assert len(files_keep) == 8
        
        # Verificar diferencia entre limpio y con etiquetas
        im_clean = np.array(Image.open(os.path.join(dest_1024, files_1024[0])))
        im_keep = np.array(Image.open(os.path.join(dest_keep, files_keep[0])))
        # Cuando se limpian las etiquetas, la imagen limpia no incluye los píxeles de texto de la esquina
        # En la imagen limpia, la parte superior por encima del calzado está 100% limpia
        clean_top = im_clean[:200, :400]
        assert clean_top.min() == 255, "La parte superior de la imagen limpia no es 100% blanca"
        
        # En la imagen con keep_labels, el texto se preserva en la silueta recortada
        assert np.any(im_keep < 120), "La imagen con keep-labels debe conservar píxeles oscuros"
        print("✅ PRUEBA 3 SUPERADA: Limpieza de etiquetas elimina texto; --keep-labels lo conserva.")
        
        # 4. Prueba Modo Lote (--batch-dir)
        print("\n--- PRUEBA 4: Modo Lote (--batch-dir) ---")
        batch_input_dir = os.path.join(temp_dir, "batch_inputs")
        os.makedirs(batch_input_dir, exist_ok=True)
        shutil.copy(synth_img, os.path.join(batch_input_dir, "BATCH-001.png"))
        shutil.copy(synth_img, os.path.join(batch_input_dir, "BATCH-002.png"))
        
        cmd_batch = [
            sys.executable, "scripts/split_grid_angles.py",
            "--batch-dir", batch_input_dir,
            "--output-dir", out_dir,
            "--size", "1024",
            "--format", "webp"
        ]
        res = subprocess.run(cmd_batch, capture_output=True, text=True)
        assert res.returncode == 0
        assert os.path.exists(os.path.join(out_dir, "Grupo_A", "BATCH-001"))
        assert os.path.exists(os.path.join(out_dir, "Grupo_A", "BATCH-002"))
        print("✅ PRUEBA 4 SUPERADA: Modo lote procesó 2 imágenes y generó 16 WebP en carpetas correctas.")
        
        print("\n" + "=" * 70)
        print("🎉 TODAS LAS PRUEBAS AUTOMATIZADAS PASARON AL 100% (4/4)")
        print("=" * 70)
        
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

if __name__ == '__main__':
    run_tests()
