"""
Script de Corte Automático para Hojas de Contacto de Nano Banana 2.1
Soporta exactamente las distribuciones de 8 paneles:
- 4x2 (4 filas x 2 columnas, como en la imagen generada de Nano Banana)
- 2x4 (2 filas x 4 columnas)
- Limpia automáticamente las marcas de texto (01 | LATERAL, etc.)
- Estandariza a 1200x1200px con fondo blanco puro #FFFFFF, centrado y 10% padding.
"""

import os
import argparse
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

PANEL_LABELS_8 = [
    "01-lateral",
    "02-medial",
    "03-3-4-front",
    "04-3-4-rear",
    "05-front",
    "06-rear",
    "07-top-down",
    "08-outsole"
]

def standardize_crop(cropped_img, target_size=1200, padding_pct=0.10):
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

def split_nanobanana_grid(image_path, sku, output_dir=None, layout='4x2'):
    if not os.path.exists(image_path):
        print(f"Error: No existe el archivo {image_path}")
        return []

    im = Image.open(image_path)
    w, h = im.size
    
    parts = layout.lower().split('x')
    rows, cols = int(parts[0]), int(parts[1])

    if output_dir is None:
        output_dir = os.path.join('dist/assets/cortes-flow', sku)
    os.makedirs(output_dir, exist_ok=True)

    cell_w = w / cols
    cell_h = h / rows
    
    print(f"\n=======================================================")
    print(f"Cortando Grid Nano Banana: {image_path}")
    print(f"SKU: {sku} | Dimensiones: {w}x{h} px | Layout: {rows} filas x {cols} columnas")
    print(f"Carpeta destino: {output_dir}")
    print(f"=======================================================")

    saved_paths = []
    idx = 0
    
    for r in range(rows):
        for c in range(cols):
            if idx >= len(PANEL_LABELS_8):
                break
                
            x0 = int(c * cell_w)
            y0 = int(r * cell_h)
            x1 = int((c + 1) * cell_w)
            y1 = int((r + 1) * cell_h)
            
            cell = im.crop((x0, y0, x1, y1))
            
            # Limpiar marca de agua / etiqueta en la esquina superior izquierda si existe
            cell_arr = np.array(cell.convert('RGB'))
            cell_arr[:35, :160] = 255
            cleaned_cell = Image.fromarray(cell_arr)
            
            standardized = standardize_crop(cleaned_cell, target_size=1200)
            
            filename = f"{PANEL_LABELS_8[idx]}.webp"
            out_file = os.path.join(output_dir, filename)
            standardized.save(out_file, 'WEBP', quality=95)
            
            print(f"  [{idx+1}/8] Guardado: {filename} (Fila {r+1}, Col {c+1})")
            saved_paths.append(out_file)
            idx += 1

    print(f"\n¡Éxito! Se cortaron y normalizaron las 8 tomas a 1200x1200px con fondo blanco puro.")
    return saved_paths

def main():
    parser = argparse.ArgumentParser(description="Cortador oficial de cuadrículas de Nano Banana 2.1")
    parser.add_argument('image', help='Ruta de la imagen descargada de Flow / Nano Banana')
    parser.add_argument('--sku', required=True, help='SKU del producto (ej: IX6180-100)')
    parser.add_argument('--layout', default='4x2', choices=['4x2', '2x4'], help='Distribución de paneles (por defecto: 4x2)')
    parser.add_argument('--out', default=None, help='Directorio de salida personalizado')

    args = parser.parse_args()
    split_nanobanana_grid(args.image, args.sku, args.out, args.layout)

if __name__ == '__main__':
    main()
