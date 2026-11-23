#!/usr/bin/env python3
"""
scripts/split_grid_angles.py
=============================================================================
Cortador y Normalizador Profesional de Cuadrículas Maestras de Calzado (4x2)
=============================================================================
Corta hojas de contacto en 8 tomas canónicas de resolución exacta (1K 1024x1024 o HD 1200x1200):
  01_lateral, 02_medial, 03_3-4_front, 04_3-4_rear,
  05_front, 06_rear, 07_top_down, 08_outsole

Características:
  - Elimina líneas divisorias de la cuadrícula.
  - Limpia automáticamente las etiquetas de esquina ("01 | LATERAL") sin cortar lengüetas o cuellos.
  - Limpia artefactos de compresión JPEG del fondo dejándolo en blanco puro #FFFFFF.
  - Auto-centra y ajusta el calzado proporcionalmente con fill-ratio uniforme (default 0.82).
  - Exporta directamente en formato WebP (o PNG/ambos) con compresión optimizada.
  - Soporta modo individual y modo por lote (--batch-dir).
"""

import os
import sys
import argparse
import glob
import re
from collections import deque
from PIL import Image, ImageOps
import numpy as np

PANEL_NAMES_8 = [
    "01_lateral",
    "02_medial",
    "03_3-4_front",
    "04_3-4_rear",
    "05_front",
    "06_rear",
    "07_top_down",
    "08_outsole"
]

def sanitize_folder_name(name):
    """Limpia nombres de grupo o SKU para rutas de archivo seguras."""
    if not name:
        return "General"
    cleaned = re.sub(r'[^\w\-_.]', '_', str(name).strip())
    return re.sub(r'_+', '_', cleaned)

def clean_label_connected_components(cell_arr, max_y_ratio=0.15, max_x_ratio=0.35):
    """
    Elimina etiquetas de texto ('01 | LATERAL') en la esquina superior izquierda.
    Solo borra componentes desconectados del calzado para proteger lengüeta y cuello.
    """
    h, w, _ = cell_arr.shape
    max_label_y = int(h * max_y_ratio)
    max_label_x = int(w * max_x_ratio)
    
    # Máscara de píxeles no blancos
    non_white = np.any(cell_arr < 240, axis=2)
    visited = np.zeros((h, w), dtype=bool)
    
    # Buscar componentes conectados que inicien en la zona superior izquierda
    for y in range(max_label_y):
        for x in range(max_label_x):
            if non_white[y, x] and not visited[y, x]:
                comp_pixels = []
                queue = [(y, x)]
                visited[y, x] = True
                is_label = True
                
                while queue:
                    cy, cx = queue.pop()
                    comp_pixels.append((cy, cx))
                    
                    # Si el componente se extiende más allá de la zona de etiqueta, es el zapato
                    if cy >= int(h * 0.18) or cx >= int(w * 0.45):
                        is_label = False
                        
                    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w:
                            if non_white[ny, nx] and not visited[ny, nx]:
                                visited[ny, nx] = True
                                queue.append((ny, nx))
                
                # Si es un componente aislado de tamaño modesto, borrarlo (poner en blanco puro)
                if is_label and len(comp_pixels) < (w * h * 0.05):
                    for cy, cx in comp_pixels:
                        cell_arr[cy, cx] = [255, 255, 255]

def clean_background_compression(cell_arr, threshold=244):
    """
    Convierte píxeles casi blancos (>= threshold en RGB) conectados al borde
    en blanco puro (255, 255, 255), eliminando halo de compresión JPEG sin alterar
    detalles blancos internos del calzado.
    """
    h, w, _ = cell_arr.shape
    near_white = (cell_arr[:, :, 0] >= threshold) & \
                 (cell_arr[:, :, 1] >= threshold) & \
                 (cell_arr[:, :, 2] >= threshold)
                 
    bg_connected = np.zeros((h, w), dtype=bool)
    q = deque()
    
    # Sembrar desde los 4 bordes exteriores
    for x in range(w):
        if near_white[0, x]:
            bg_connected[0, x] = True
            q.append((0, x))
        if near_white[h - 1, x]:
            bg_connected[h - 1, x] = True
            q.append((h - 1, x))
    for y in range(h):
        if near_white[y, 0] and not bg_connected[y, 0]:
            bg_connected[y, 0] = True
            q.append((y, 0))
        if near_white[y, w - 1] and not bg_connected[y, w - 1]:
            bg_connected[y, w - 1] = True
            q.append((y, w - 1))
            
    while q:
        cy, cx = q.popleft()
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < h and 0 <= nx < w:
                if not bg_connected[ny, nx] and near_white[ny, nx]:
                    bg_connected[ny, nx] = True
                    q.append((ny, nx))
                    
    cell_arr[bg_connected] = [255, 255, 255]

def process_cell(cell_img, target_w, target_h, fill_ratio=0.82, keep_labels=False):
    """
    Procesa un panel individual:
      1. Limpia etiqueta si keep_labels es False.
      2. Limpia artefactos de fondo.
      3. Encuentra bounding box del producto.
      4. Escala proporcionalmente según fill_ratio.
      5. Centra sobre lienzo blanco puro #FFFFFF de target_w x target_h.
    """
    cell_rgb = cell_img.convert('RGB')
    cell_arr = np.array(cell_rgb)
    ch, cw, _ = cell_arr.shape
    
    # Paso B: Limpieza de etiquetas
    if not keep_labels:
        clean_label_connected_components(cell_arr)
        
    # Paso C: Normalización de fondo
    clean_background_compression(cell_arr, threshold=244)
    
    # Calcular Bounding Box del calzado
    shoe_mask = np.any(cell_arr < 245, axis=2)
    ys, xs = np.where(shoe_mask)
    
    warning_msg = None
    if len(ys) < 50:
        warning_msg = "ADVERTENCIA: Panel prácticamente vacío o sin calzado detectado."
        shoe = Image.fromarray(cell_arr)
    else:
        ymin, ymax = ys.min(), ys.max()
        xmin, xmax = xs.min(), xs.max()
        
        # Verificar anomalía de bordes
        if ymin <= 2 or xmin <= 2 or ymax >= ch - 3 or xmax >= cw - 3:
            warning_msg = "AVISO: El calzado detectado toca o está muy cerca del borde del recorte."
            
        shoe = Image.fromarray(cell_arr[ymin:ymax + 1, xmin:xmax + 1])
        
    sw, sh = shoe.size
    
    # Redimensionar proporcionalmente con fill_ratio
    max_w = int(target_w * fill_ratio)
    max_h = int(target_h * fill_ratio)
    scale = min(max_w / sw, max_h / sh)
    nw = max(1, int(sw * scale))
    nh = max(1, int(sh * scale))
    
    resized_shoe = shoe.resize((nw, nh), Image.Resampling.LANCZOS)
    
    # Centrar en lienzo blanco puro #FFFFFF
    canvas = Image.new('RGB', (target_w, target_h), (255, 255, 255))
    pos_x = (target_w - nw) // 2
    pos_y = (target_h - nh) // 2
    canvas.paste(resized_shoe, (pos_x, pos_y))
    
    return canvas, warning_msg

def split_grid_image(
    image_path,
    sku,
    group="Grupo_A",
    output_dir="./output_catalog",
    layout="4x2",
    target_w=1024,
    target_h=1024,
    out_format="webp",
    quality=90,
    fill_ratio=0.82,
    keep_labels=False
):
    """
    Corta una cuadrícula 4x2 en 8 imágenes individuales normalizadas y las guarda
    en {output_dir}/{group}/{sku}/{sku}_{panel_name}.webp
    """
    if not os.path.exists(image_path):
        print(f"❌ Error: No existe el archivo de imagen '{image_path}'")
        return []
        
    try:
        im = Image.open(image_path)
        im = ImageOps.exif_transpose(im)
    except Exception as e:
        print(f"❌ Error al abrir imagen '{image_path}': {e}")
        return []
        
    w, h = im.size
    parts = layout.lower().split('x')
    rows, cols = int(parts[0]), int(parts[1])
    total_panels = rows * cols
    
    if total_panels != 8:
        print(f"⚠️ Advertencia: El layout '{layout}' define {total_panels} paneles (se esperan 8).")
        
    # Sanitizar rutas
    safe_group = sanitize_folder_name(group)
    safe_sku = sanitize_folder_name(sku).upper()
    
    dest_dir = os.path.join(output_dir, safe_group, safe_sku)
    os.makedirs(dest_dir, exist_ok=True)
    
    cell_w = w / cols
    cell_h = h / rows
    
    # Margen de seguridad para no incluir líneas divisorias oscuras (aprox 1.8%)
    margin_x = max(3, int(cell_w * 0.018))
    margin_y = max(3, int(cell_h * 0.018))
    
    print("\n" + "=" * 70)
    print(f"👟 PROCESANDO CUADRÍCULA: {os.path.basename(image_path)}")
    print(f"   • SKU: {safe_sku} | Grupo: {safe_group}")
    print(f"   • Dimensiones origen: {w}x{h} px | Layout: {rows}x{cols}")
    print(f"   • Salida objetivo: {target_w}x{target_h} px | Formato: {out_format.upper()} (Q={quality})")
    print(f"   • Fill-Ratio: {fill_ratio * 100:.0f}% | Limpieza etiquetas: {'DESACTIVADA' if keep_labels else 'ACTIVADA'}")
    print(f"   • Directorio destino: {dest_dir}")
    print("=" * 70)
    
    saved_files = []
    idx = 0
    
    for r in range(rows):
        for c in range(cols):
            if idx >= len(PANEL_NAMES_8):
                break
                
            panel_name = PANEL_NAMES_8[idx]
            
            # Coordenadas recortando líneas divisorias de borde
            x0 = int(c * cell_w) + margin_x
            y0 = int(r * cell_h) + margin_y
            x1 = int((c + 1) * cell_w) - margin_x
            y1 = int((r + 1) * cell_h) - margin_y
            
            raw_cell = im.crop((x0, y0, x1, y1))
            
            # Normalizar celda
            final_img, warn = process_cell(
                raw_cell,
                target_w=target_w,
                target_h=target_h,
                fill_ratio=fill_ratio,
                keep_labels=keep_labels
            )
            
            # Guardar archivos según formato
            base_filename = f"{safe_sku}_{panel_name}"
            
            # WebP
            if out_format in ('webp', 'both'):
                webp_path = os.path.join(dest_dir, f"{base_filename}.webp")
                final_img.save(webp_path, 'WEBP', quality=quality, method=6)
                size_kb = os.path.getsize(webp_path) / 1024
                saved_files.append(webp_path)
                status_str = f"✅ [{idx+1}/8] {base_filename}.webp ({final_img.width}x{final_img.height} px, {size_kb:.1f} KB)"
                if warn:
                    status_str += f" -> ⚠️ {warn}"
                print(f"   {status_str}")
                
            # PNG
            if out_format in ('png', 'both'):
                png_path = os.path.join(dest_dir, f"{base_filename}.png")
                final_img.save(png_path, 'PNG', optimize=True)
                size_kb = os.path.getsize(png_path) / 1024
                saved_files.append(png_path)
                if out_format == 'png':
                    status_str = f"✅ [{idx+1}/8] {base_filename}.png ({final_img.width}x{final_img.height} px, {size_kb:.1f} KB)"
                    if warn:
                        status_str += f" -> ⚠️ {warn}"
                    print(f"   {status_str}")
                    
            # JPG
            if out_format == 'jpg':
                jpg_path = os.path.join(dest_dir, f"{base_filename}.jpg")
                final_img.save(jpg_path, 'JPEG', quality=quality)
                size_kb = os.path.getsize(jpg_path) / 1024
                saved_files.append(jpg_path)
                status_str = f"✅ [{idx+1}/8] {base_filename}.jpg ({final_img.width}x{final_img.height} px, {size_kb:.1f} KB)"
                if warn:
                    status_str += f" -> ⚠️ {warn}"
                print(f"   {status_str}")
                
            idx += 1
            
    print(f"✨ Completado: {len(saved_files)} imágenes generadas exitosamente en {dest_dir}\n")
    return saved_files

def find_sku_and_group(filepath, catalog=None):
    """
    Intenta inferir el SKU y Grupo a partir de la ruta o nombre del archivo.
    """
    fn = os.path.basename(filepath)
    name_no_ext, _ = os.path.splitext(fn)
    
    # 1. Patrón SKU típico (ej. IX6180-100, AQ9214-006, 694862-200)
    sku_match = re.search(r'\b([A-Za-z0-9]{2,6}[-_ ]\d{3})\b', name_no_ext)
    inferred_sku = None
    if sku_match:
        inferred_sku = sku_match.group(1).upper().replace(' ', '-')
        
    # 2. Verificar en catálogo si está disponible
    inferred_group = "Grupo_A"
    if catalog:
        for item in catalog:
            cat_sku = item.get('sku', '').upper()
            if inferred_sku and cat_sku == inferred_sku:
                return cat_sku, item.get('group', 'Grupo_A')
            # Comparar por nombre de carpeta
            if item.get('prod_dir', '').lower() in filepath.lower():
                return cat_sku, item.get('group', 'Grupo_A')
                
    # 3. Inferir grupo desde la ruta
    grp_match = re.search(r'Grupo[-_ ]([A-Ga-g])', filepath, re.IGNORECASE)
    if grp_match:
        inferred_group = f"Grupo_{grp_match.group(1).upper()}"
        
    if not inferred_sku:
        inferred_sku = sanitize_folder_name(name_no_ext).upper()
        
    return inferred_sku, inferred_group

def run_batch(
    batch_dir,
    output_dir="./output_catalog",
    layout="4x2",
    target_w=1024,
    target_h=1024,
    out_format="webp",
    quality=90,
    fill_ratio=0.82,
    keep_labels=False,
    catalog=None
):
    """
    Escanea un directorio en busca de cuadrículas de imágenes y las procesa en lote.
    """
    if not os.path.isdir(batch_dir):
        print(f"❌ Error: La carpeta de lote '{batch_dir}' no existe.")
        return
        
    valid_exts = ('.png', '.jpg', '.jpeg', '.webp')
    images = []
    for root, _, files in os.walk(batch_dir):
        # Evitar carpetas de salida si están anidadas
        if 'output_catalog' in root or 'dist/assets/cortes-flow' in root:
            continue
        for f in files:
            if f.lower().endswith(valid_exts):
                images.append(os.path.join(root, f))
                
    images.sort()
    if not images:
        print(f"⚠️ No se encontraron imágenes válidas en '{batch_dir}'.")
        return
        
    print(f"\n🚀 MODO LOTE ACTIVADO: {len(images)} imágenes encontradas en '{batch_dir}'")
    total_processed = 0
    
    for img_path in images:
        sku, group = find_sku_and_group(img_path, catalog)
        res = split_grid_image(
            image_path=img_path,
            sku=sku,
            group=group,
            output_dir=output_dir,
            layout=layout,
            target_w=target_w,
            target_h=target_h,
            out_format=out_format,
            quality=quality,
            fill_ratio=fill_ratio,
            keep_labels=keep_labels
        )
        if res:
            total_processed += 1
            
    print("=" * 70)
    print(f"🎉 LOTE COMPLETADO: {total_processed}/{len(images)} cuadrículas procesadas con éxito.")
    print("=" * 70)

def main():
    parser = argparse.ArgumentParser(
        description="Cortador profesional y estandarizador de cuadrículas 4x2 a 8 tomas limpias en WebP/PNG."
    )
    parser.add_argument(
        'image',
        nargs='?',
        default=None,
        help="Ruta de la imagen de cuadrícula (requerida en modo individual)."
    )
    parser.add_argument(
        '--batch-dir',
        default=None,
        help="Ruta de la carpeta para procesar todas las cuadrículas en lote."
    )
    parser.add_argument(
        '--sku',
        default=None,
        help="SKU del producto (ej: IX6180-100). Si se omite, se infiere del nombre del archivo."
    )
    parser.add_argument(
        '--group',
        default="Grupo_A",
        help="Grupo del producto (ej: Grupo_A, Grupo_B, etc.). Por defecto: Grupo_A."
    )
    parser.add_argument(
        '--layout',
        default="4x2",
        choices=["4x2", "2x4"],
        help="Distribución de paneles (por defecto: 4x2)."
    )
    parser.add_argument(
        '--size',
        type=int,
        default=1024,
        help="Tamaño cuadrado final en píxeles (ej: 1024 para 1K, 1200 para HD). Por defecto: 1024."
    )
    parser.add_argument(
        '--width',
        type=int,
        default=None,
        help="Ancho personalizado en píxeles (por defecto toma el valor de --size)."
    )
    parser.add_argument(
        '--height',
        type=int,
        default=None,
        help="Alto personalizado en píxeles (por defecto toma el valor de --size)."
    )
    parser.add_argument(
        '--format',
        default="webp",
        choices=["webp", "png", "both", "jpg"],
        help="Formato de salida (por defecto: webp)."
    )
    parser.add_argument(
        '--quality',
        type=int,
        default=90,
        help="Calidad de compresión WebP/JPEG de 1 a 100 (por defecto: 90)."
    )
    parser.add_argument(
        '--fill-ratio',
        type=float,
        default=0.82,
        help="Proporción máxima del lienzo que ocupa el calzado (por defecto: 0.82 = 82%%)."
    )
    parser.add_argument(
        '--keep-labels',
        action='store_true',
        default=False,
        help="Si se activa, conserva las etiquetas de texto de esquina ('01 | LATERAL'). Por defecto se limpian."
    )
    parser.add_argument(
        '--output-dir',
        default="./output_catalog",
        help="Directorio raíz de salida (por defecto: ./output_catalog)."
    )
    
    args = parser.parse_args()
    
    target_w = args.width if args.width is not None else args.size
    target_h = args.height if args.height is not None else args.size
    
    # Cargar catálogo si existe para mejorar inferencia
    catalog = None
    catalog_path = os.path.join(os.path.dirname(__file__), "..", "dist", "js", "assigned_angles.json")
    if os.path.exists(catalog_path):
        try:
            import json
            with open(catalog_path, 'r', encoding='utf-8') as f:
                catalog = json.load(f)
        except Exception:
            pass
            
    # Modo Lote
    if args.batch_dir:
        run_batch(
            batch_dir=args.batch_dir,
            output_dir=args.output_dir,
            layout=args.layout,
            target_w=target_w,
            target_h=target_h,
            out_format=args.format,
            quality=args.quality,
            fill_ratio=args.fill_ratio,
            keep_labels=args.keep_labels,
            catalog=catalog
        )
        return
        
    # Modo Individual
    if not args.image:
        parser.print_help()
        print("\n❌ Error: Debes especificar una imagen o la opción --batch-dir.")
        sys.exit(1)
        
    sku = args.sku
    group = args.group
    if not sku:
        inferred_sku, inferred_group = find_sku_and_group(args.image, catalog)
        sku = inferred_sku
        if args.group == "Grupo_A" and inferred_group != "Grupo_A":
            group = inferred_group
            
    split_grid_image(
        image_path=args.image,
        sku=sku,
        group=group,
        output_dir=args.output_dir,
        layout=args.layout,
        target_w=target_w,
        target_h=target_h,
        out_format=args.format,
        quality=args.quality,
        fill_ratio=args.fill_ratio,
        keep_labels=args.keep_labels
    )

if __name__ == '__main__':
    main()
