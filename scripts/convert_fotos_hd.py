"""
scripts/convert_fotos_hd.py
Convierte todas las fotos de _source_data/fotos a PNG a resolución 2K (máximo 2048px en su lado más largo,
respetando orientación EXIF y relación de aspecto) y las guarda organizadas en _source_data/fotos-HD.
"""

import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageOps

SRC_BASE = r"C:\Users\eduar\Documents\CATALOGO\_source_data\fotos"
DST_BASE = r"C:\Users\eduar\Documents\CATALOGO\_source_data\fotos-HD"

def process_file(task):
    src_path, dst_path = task
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    try:
        with Image.open(src_path) as img:
            # Corregir orientación según EXIF (ej. fotos tomadas en vertical)
            img = ImageOps.exif_transpose(img)
            
            # Asegurar modo RGB
            if img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGB")
                
            w, h = img.size
            max_side = max(w, h)
            if max_side != 2048:
                ratio = 2048.0 / max_side
                new_w = int(round(w * ratio))
                new_h = int(round(h * ratio))
                img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            
            img.save(dst_path, format="PNG", compress_level=4)
        return True, src_path, dst_path, img.size
    except Exception as e:
        return False, src_path, dst_path, str(e)

def main():
    t0 = time.time()
    tasks = []
    for root, dirs, files in os.walk(SRC_BASE):
        for f in files:
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                src_path = os.path.join(root, f)
                rel_path = os.path.relpath(src_path, SRC_BASE)
                base_name = os.path.splitext(rel_path)[0]
                dst_path = os.path.join(DST_BASE, f"{base_name}.png")
                tasks.append((src_path, dst_path))

    total = len(tasks)
    print(f"Iniciando conversión de {total} imágenes...")

    success = 0
    errors = []
    # 8 workers es óptimo en I/O + Pillow
    with ThreadPoolExecutor(max_workers=8) as executor:
        for ok, s, d, info in executor.map(process_file, tasks):
            if ok:
                success += 1
                if success % 25 == 0 or success == total:
                    print(f"Progreso: {success}/{total} convertidas...")
            else:
                errors.append((s, info))

    t1 = time.time()
    print(f"\nFinalizado en {t1 - t0:.2f} segundos.")
    print(f"Exitosas: {success}/{total}")
    if errors:
        print(f"Errores ({len(errors)}):")
        for s, err in errors:
            print(f"  {s}: {err}")
    else:
        print("Todas las imagenes se procesaron correctamente sin errores.")

if __name__ == "__main__":
    main()
