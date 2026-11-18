"""
Script de Corte Automático de Grids / Hojas de Contacto de Calzado
Soporta:
- Grids de 6 ángulos: 2x3 (2 filas, 3 columnas) o 3x2 (3 filas, 2 columnas)
- Grids de 8 ángulos: 2x4 (2 filas, 4 columnas) o 4x2 (4 filas, 2 columnas)
- Tiras de 2 ángulos: 1x2
- Tiras de 3 ángulos: 1x3

Cada panel cortado se:
1. Aísla de la celda de la cuadrícula.
2. Centra en un lienzo cuadrado uniforme de 1200x1200px.
3. Aplica fondo blanco puro #FFFFFF.
4. Aplica padding del 10% (la zapatilla ocupa 80% máximo).
5. Guarda en formato WebP optimizado con nomenclatura estandarizada.
"""

import os
import argparse
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# Nombres canónicos para los cortes según cantidad de tomas
NAMES_6 = [
    "01-lateral-exterior",
    "02-frontal-3-4",
    "03-frontal-directa",
    "04-posterior-talon",
    "05-lateral-interior",
    "06-cenital-superior"
]

NAMES_8 = [
    "01-lateral-exterior",
    "02-frontal-3-4",
    "03-frontal-directa",
    "04-posterior-talon",
    "05-trasera-3-4",
    "06-lateral-interior",
    "07-cenital-superior",
    "08-suela-inferior"
]

NAMES_4 = [
    "01-lateral-exterior",
    "02-frontal-3-4",
    "03-posterior-talon",
    "04-cenital-superior"
]

NAMES_2 = [
    "01-lateral-exterior",
    "02-frontal-3-4"
]

NAMES_3 = [
    "01-lateral-exterior",
    "02-posterior-talon",
    "03-cenital-superior"
]

def standardize_crop(cropped_img, target_size=1200, padding_pct=0.10):
    """
    Toma un recorte individual, detecta su bounding box real,
    lo centra sobre lienzo blanco 1200x1200px con padding 10% y sombra suave.
    """
    img_rgba = cropped_img.convert('RGBA')
    arr = np.array(img_rgba)
    
    # Máscara de silueta
    if arr.shape[2] == 4 and np.any(arr[:, :, 3] < 250):
        mask = arr[:, :, 3] > 20
    else:
        mask = np.any(arr[:, :, :3] < 242, axis=2)
        
    if np.any(mask):
        y_idx, x_idx = np.where(mask)
        ymin, ymax = y_idx.min(), y_idx.max()
        xmin, xmax = x_idx.min(), x_idx.max()
        shoe = img_rgba.crop((xmin, ymin, xmax + 1, ymax + 1))
    else:
        shoe = img_rgba
        
    cw, ch = shoe.size
    max_dim = int(target_size * (1.0 - 2 * padding_pct)) # 960 px
    scale = min(max_dim / cw, max_dim / ch)
    nw = max(1, int(cw * scale))
    nh = max(1, int(ch * scale))
    
    resized = shoe.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', (target_size, target_size), (255, 255, 255, 255))
    
    pos_x = (target_size - nw) // 2
    pos_y = (target_size - nh) // 2
    
    # Sombra suave de contacto
    shadow = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(shadow)
    sw = int(nw * 0.85)
    sh = max(16, int(nh * 0.08))
    sx0 = (target_size - sw) // 2
    sy0 = pos_y + nh - int(sh * 0.55)
    draw.ellipse([sx0, sy0, sx0 + sw, sy0 + sh], fill=(25, 25, 25, 38))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=10))
    
    canvas.alpha_composite(shadow)
    canvas.alpha_composite(resized, (pos_x, pos_y))
    return canvas.convert('RGB')

def split_grid(image_path, sku, output_dir=None, layout=None):
    """
    Corta una imagen de grid en sus paneles correspondientes.
    layout puede ser: '2x3', '3x2', '2x4', '4x2', '1x2', '1x3' o None (auto-detectar).
    """
    if not os.path.exists(image_path):
        print(f"Error: No existe el archivo {image_path}")
        return []

    im = Image.open(image_path)
    w, h = im.size
    aspect = w / h
    
    # Auto-detección de layout si no se especifica
    if layout is None:
        if 1.4 <= aspect <= 1.6: # aprox 3:2 (ej. 3 cols x 2 rows)
            rows, cols = 2, 3
        elif 1.9 <= aspect <= 2.2: # aprox 2:1 (ej. 4 cols x 2 rows)
            rows, cols = 2, 4
        elif 1.8 <= aspect <= 2.2 and h < w/1.8: # 1 row x 2 cols
            rows, cols = 1, 2
        elif 2.8 <= aspect <= 3.3: # 1 row x 3 cols
            rows, cols = 1, 3
        elif 0.9 <= aspect <= 1.1: # Cuadrado 2x2
            rows, cols = 2, 2
        else:
            # Por defecto asumir 2 filas x 3 columnas
            rows, cols = 2, 3
    else:
        parts = layout.lower().split('x')
        rows, cols = int(parts[0]), int(parts[1])

    total_panels = rows * cols
    if total_panels == 6:
        names = NAMES_6
    elif total_panels == 8:
        names = NAMES_8
    elif total_panels == 4:
        names = NAMES_4
    elif total_panels == 2:
        names = NAMES_2
    elif total_panels == 3:
        names = NAMES_3
    else:
        names = [f"{i+1:02d}-angulo" for i in range(total_panels)]

    if output_dir is None:
        output_dir = os.path.join('dist/assets/cortes-flow', sku)
    os.makedirs(output_dir, exist_ok=True)

    cell_w = w / cols
    cell_h = h / rows
    
    print(f"\n=======================================================")
    print(f"Procesando Grid: {image_path}")
    print(f"SKU: {sku} | Dimensiones: {w}x{h} px | Layout: {rows} filas x {cols} columnas ({total_panels} paneles)")
    print(f"Carpeta destino: {output_dir}")
    print(f"=======================================================")

    saved_paths = []
    panel_idx = 0
    
    for r in range(rows):
        for c in range(cols):
            if panel_idx >= len(names):
                break
                
            x0 = int(c * cell_w)
            y0 = int(r * cell_h)
            x1 = int((c + 1) * cell_w)
            y1 = int((r + 1) * cell_h)
            
            cell_crop = im.crop((x0, y0, x1, y1))
            standardized = standardize_crop(cell_crop, target_size=1200)
            
            filename = f"{names[panel_idx]}.webp"
            out_file = os.path.join(output_dir, filename)
            standardized.save(out_file, 'WEBP', quality=92)
            
            print(f"  [{panel_idx+1}/{total_panels}] Guardado: {filename} (Fila {r+1}, Col {c+1})")
            saved_paths.append(out_file)
            panel_idx += 1

    print(f"\nÉxito: Se cortaron y normalizaron {len(saved_paths)} tomas a 1200x1200px en {output_dir}")
    return saved_paths

def main():
    parser = argparse.ArgumentParser(description="Script para cortar y estandarizar hojas de contacto de Flow/Nano Banana")
    parser.add_argument('image', help='Ruta de la imagen de grid generada por Flow (ej: uploads/grid_jordan.png)')
    parser.add_argument('--sku', required=True, help='SKU del producto (ej: IX6180-100 o HF7054-012)')
    parser.add_argument('--layout', default=None, choices=['2x3', '3x2', '2x4', '4x2', '1x2', '1x3'], help='Distribución de filas y columnas (por defecto: auto-detectar)')
    parser.add_argument('--out', default=None, help='Directorio de salida personalizado')

    args = parser.parse_args()
    split_grid(args.image, args.sku, args.out, args.layout)

if __name__ == '__main__':
    main()
