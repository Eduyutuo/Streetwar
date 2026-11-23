import os
import shutil
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import subprocess

def test_synthetic_grid():
    print("\n--- 🧪 TEST SINTÉTICO: GENERANDO CUADRÍCULA 4x2 CON LÍNEAS 1PX Y ETIQUETAS ---")
    os.makedirs('scratch', exist_ok=True)
    synth_path = 'scratch/test_grid_4x2.png'
    
    # Crear imagen 4x2 de 2048x2048 (4 filas x 2 cols, cada celda 512x1024)
    # o 1024x1024 (cada celda 256x512)
    w, h = 1024, 1024
    img = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Dibujar líneas divisorias de 1px en gris oscuro (#404040 = 64,64,64)
    cols, rows = 2, 4
    cell_w, cell_h = w // cols, h // rows
    
    # Línea vertical
    draw.line([(cell_w, 0), (cell_w, h)], fill=(64, 64, 64), width=1)
    # Líneas horizontales
    for r in range(1, rows):
        draw.line([(0, r * cell_h), (w, r * cell_h)], fill=(64, 64, 64), width=1)
        
    labels = [
        "01 | LATERAL", "02 | MEDIAL",
        "03 | 3/4 FRONT", "04 | 3/4 REAR",
        "05 | FRONT", "06 | REAR",
        "07 | TOP-DOWN", "08 | OUTSOLE"
    ]
    
    # Dibujar etiqueta y una silueta simulada en cada celda
    for idx, label in enumerate(labels):
        r = idx // cols
        c = idx % cols
        x0 = c * cell_w
        y0 = r * cell_h
        
        # Etiqueta en esquina superior izquierda
        draw.text((x0 + 15, y0 + 12), label, fill=(30, 30, 30))
        
        # Silueta irregular de calzado simulado (con varios colores para probar no-borrado)
        cx = x0 + cell_w // 2
        cy = y0 + cell_h // 2 + 10
        # Suela
        draw.rectangle([cx - 140, cy + 30, cx + 130, cy + 50], fill=(220, 50, 50))
        # Cuerpo
        draw.ellipse([cx - 120, cy - 40, cx + 100, cy + 35], fill=(40, 80, 160))
        # Lengüeta / cuello que sube hacia la izquierda pero no toca la etiqueta
        draw.polygon([(cx - 70, cy - 30), (cx - 40, cy - 70), (cx - 10, cy - 30)], fill=(240, 240, 240)) # blanco casi puro
        # Cordones oscuros
        draw.line([(cx - 35, cy - 50), (cx - 20, cy - 40)], fill=(20, 20, 20), width=3)
        
    img.save(synth_path)
    print(f"Cuadrícula sintética guardada en: {synth_path} ({img.size})")
    
    # Ejecutar split_grid_angles.py
    out_dir = './output_catalog/test_verify'
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
        
    cmd = [
        'python', 'scripts/split_grid_angles.py',
        synth_path,
        '--sku', 'TEST-001',
        '--group', 'Grupo_A',
        '--size', '1024',
        '--format', 'webp',
        '--output-dir', out_dir
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print("ERROR:", res.stderr)
        return False
        
    # Verificar los 8 WebPs
    panel_names = [
        "01_lateral", "02_medial", "03_3-4_front", "04_3-4_rear",
        "05_front", "06_rear", "07_top_down", "08_outsole"
    ]
    target_folder = os.path.join(out_dir, 'Grupo_A', 'TEST-001')
    assert os.path.isdir(target_folder), f"Target folder {target_folder} does not exist"
    
    for p_name in panel_names:
        fn = os.path.join(target_folder, f"TEST-001_{p_name}.webp")
        assert os.path.exists(fn), f"File {fn} does not exist"
        im = Image.open(fn)
        assert im.size == (1024, 1024), f"Wrong size {im.size} for {fn}"
        arr = np.array(im)
        # Esquinas deben ser #FFFFFF puro
        assert list(arr[0, 0]) == [255, 255, 255], f"Top-left corner not white in {fn}"
        assert list(arr[0, 1023]) == [255, 255, 255], f"Top-right corner not white in {fn}"
        assert list(arr[1023, 0]) == [255, 255, 255], f"Bottom-left corner not white in {fn}"
        assert list(arr[1023, 1023]) == [255, 255, 255], f"Bottom-right corner not white in {fn}"
        # Zona superior izquierda (donde estaba la etiqueta) debe estar limpia (blanca)
        assert np.all(arr[0:60, 0:120] == 255), f"Label area not clean in {fn}"
        print(f"  ✓ {p_name}.webp: Dimensiones exactas 1024x1024, fondo #FFFFFF puro, sin etiquetas.")
        
    print("\n✅ TODAS LAS COMPROBACIONES DE VERIFICACIÓN PASARON CON ÉXITO.")
    return True

if __name__ == '__main__':
    test_synthetic_grid()
