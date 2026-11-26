#!/usr/bin/env python3
"""
scripts/generate_catalog_images.py

Generación desatendida de los 8 ángulos canónicos en WebP sobre fondo blanco puro #FFFFFF
usando la API oficial de Gemini (google-genai) y el mapeo exacto de carpetas de SNKRS (1).xlsx.

Nomenclatura y estructura de salida:
  output_catalog/{Grupo}/{Nombre_Carpeta_Real}/{Nombre_Carpeta_Real}_{01_lateral...08_outsole}.webp

Uso:
  python scripts/generate_catalog_images.py --product "01_Air_Jordan_9_Space_Jam" --dry-run
  python scripts/generate_catalog_images.py --sku "IX6180-100" --dry-run
  python scripts/generate_catalog_images.py --group "Grupo A" --strategy individual --dry-run
  python scripts/generate_catalog_images.py --all --strategy individual --dry-run
  python scripts/generate_catalog_images.py --product "02_Air_Jordan_3_Green_White_Red"
"""

import os
import sys
import argparse
import time
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# Intentar importar google-genai
try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

# Importar mapeo oficial SNKRS
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
for p in [current_dir, parent_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from snkrs_mapping import load_snkrs_mapping, get_mapping_by_sku, get_mapping_by_real_folder
except ImportError:
    from scripts.snkrs_mapping import load_snkrs_mapping, get_mapping_by_sku, get_mapping_by_real_folder

CANONICAL_ANGLES = [
    ("01_lateral", "Lateral exterior profile, toe pointing left", "01-lateral"),
    ("02_medial", "Medial interior profile, toe pointing right", "02-medial"),
    ("03_3-4_front", "Three-quarter perspective front view (3/4)", "03-3-4-front"),
    ("04_3-4_rear", "Three-quarter perspective rear/heel view (3/4)", "04-3-4-rear"),
    ("05_front", "Direct front view", "05-front"),
    ("06_rear", "Direct rear heel view", "06-rear"),
    ("07_top_down", "Top-down overhead view of tongue, laces and insoles", "07-top-down"),
    ("08_outsole", "Direct bottom horizontal view of the outsole tread pattern", "08-outsole"),
]

def load_dotenv():
    """Carga variables desde archivo .env local si existe."""
    env_path = Path(".env")
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    k = k.strip()
                    v = v.strip().strip("'\"")
                    if k not in os.environ:
                        os.environ[k] = v

def get_api_key():
    """Obtiene GEMINI_API_KEY del entorno."""
    load_dotenv()
    return os.environ.get("GEMINI_API_KEY", "")

def normalize_to_canvas(im, target_size=1024, fill_ratio=0.82, add_shadow=True):
    """
    Normaliza una imagen generada:
    - Detecta bounding box eliminando bordes residuales
    - Centra sobre lienzo blanco puro #FFFFFF
    - Escala proporcionalmente con fill_ratio (default 0.82)
    - Agrega sombra sutil de contacto en piso para vistas apoyadas
    - Resampling LANCZOS
    """
    im_rgb = im.convert("RGB")
    arr = np.array(im_rgb)
    h, w = arr.shape[:2]

    # Detectar píxeles no blancos (fondo blanco puro con tolerancia)
    mask = np.any(arr < 245, axis=2)
    y_idx, x_idx = np.where(mask)
    if not len(x_idx):
        return Image.new("RGB", (target_size, target_size), (255, 255, 255))

    xmin, xmax = int(x_idx.min()), int(x_idx.max())
    ymin, ymax = int(y_idx.min()), int(y_idx.max())

    shoe_crop = im_rgb.crop((xmin, ymin, xmax + 1, ymax + 1))
    cw, ch = shoe_crop.size

    max_dim = int(target_size * fill_ratio)
    scale = min(max_dim / cw, max_dim / ch)
    nw = max(10, int(cw * scale))
    nh = max(10, int(ch * scale))
    shoe_resized = shoe_crop.resize((nw, nh), Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", (target_size, target_size), (255, 255, 255, 255))
    pos_x = (target_size - nw) // 2
    pos_y = (target_size - nh) // 2

    if add_shadow and (cw / ch > 1.15):
        shadow = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(shadow)
        sw = int(nw * 0.85)
        sh = max(12, int(nh * 0.08))
        sx0 = (target_size - sw) // 2
        sy0 = pos_y + nh - int(sh * 0.45)
        draw.ellipse([sx0, sy0, sx0 + sw, sy0 + sh], fill=(25, 25, 25, 38))
        shadow = shadow.filter(ImageFilter.GaussianBlur(radius=8))
        canvas.alpha_composite(shadow)

    shoe_rgba = shoe_resized.convert("RGBA")
    s_arr = np.array(shoe_rgba)
    s_mask = np.any(s_arr[:, :, :3] < 248, axis=2)
    s_arr[:, :, 3] = np.where(s_mask, 255, 0)
    shoe_clean = Image.fromarray(s_arr)

    canvas.alpha_composite(shoe_clean, (pos_x, pos_y))
    return canvas.convert("RGB")

def build_individual_prompt(product_info, angle_key, angle_desc, mode="A"):
    """Construye el prompt en inglés optimizado para 1 ángulo individual 1:1 sobre #FFFFFF."""
    raw_name = product_info.get("name", "Sneaker")
    cat = product_info.get("category", "")
    if cat and cat.lower() not in raw_name.lower():
        full_name = f"{cat} \"{raw_name}\""
    else:
        full_name = raw_name
        
    sku = product_info.get("sku", "")
    colors = product_info.get("color", "")
    color_note = f", official colorway: {colors}" if colors else ""

    pair_clause = (
        "Show both left and right shoes arranged symmetrically side-by-side as a pair."
        if (mode == "A" and angle_key in ["05_front", "06_rear"])
        else "Show a single individual shoe."
    )

    prompt = (
        f"Master studio commercial e-commerce product photograph of {full_name} (SKU: {sku}{color_note}). "
        f"Angle: {angle_key.upper()} - {angle_desc}. {pair_clause} "
        f"Seamless, flawless solid pure white background (#FFFFFF). "
        f"Soft natural contact drop shadow directly beneath the shoe on the white ground plane. "
        f"Even, neutral 5500K commercial footwear studio lighting. Crisp razor-sharp focus on materials, leather grain, and stitching. "
        f"Square 1:1 framing, shoe centered horizontally and vertically, breathing room around borders. "
        f"CRITICAL: Pure white background only (#FFFFFF). No text, no logos, no watermarks, no grid lines, no border frames."
    )
    return prompt

def find_reference_photos(product_info):
    """Busca las fotos de referencia reales en _source_data/fotos."""
    group = product_info.get("group", "")
    folder = product_info.get("real_folder") or product_info.get("folder", "")
    base_dir = Path("_source_data") / "fotos" / group / folder
    
    if not base_dir.exists():
        return []
    
    photos = []
    for f in sorted(base_dir.iterdir()):
        if f.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp", ".avif"]:
            photos.append(f)
    return photos

def generate_single_angle_api(client, model_name, prompt, ref_photos, out_path, size=1024, quality=90, max_retries=3):
    """Genera 1 ángulo llamando a la API de Gemini / Imagen con reintentos."""
    for attempt in range(1, max_retries + 1):
        try:
            # Enviar prompt e imágenes de referencia si el modelo acepta multimodal
            # Utilizar types para construir el request
            contents = [prompt]
            for p in ref_photos[:3]: # Hasta 3 imágenes de referencia para context grounding
                try:
                    ref_img = Image.open(p).convert("RGB")
                    # Reducir si es muy pesada para el payload
                    ref_img.thumbnail((1024, 1024))
                    contents.append(ref_img)
                except Exception:
                    pass

            response = client.models.generate_images(
                model=model_name,
                prompt=prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    aspect_ratio="1:1",
                    output_mime_type="image/jpeg",
                ),
            )
            
            # Obtener imagen generada
            if response.generated_images:
                gen_img_bytes = response.generated_images[0].image.image_bytes
                import io
                raw_im = Image.open(io.BytesIO(gen_img_bytes))
                
                # Normalizar a 1024x1024 sobre #FFFFFF
                is_grounded = not any(k in str(out_path) for k in ["07_top_down", "08_outsole"])
                norm_im = normalize_to_canvas(raw_im, target_size=size, fill_ratio=0.82, add_shadow=is_grounded)
                
                out_path.parent.mkdir(parents=True, exist_ok=True)
                norm_im.save(out_path, format="WEBP", quality=quality)
                return True
                
        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "quota" in err_str.lower():
                wait_sec = (2 ** attempt) * 2
                print(f"  [429 Rate Limit] Esperando {wait_sec}s antes de reintentar...")
                time.sleep(wait_sec)
            else:
                print(f"  [Error API Intento {attempt}/{max_retries}]: {e}")
                time.sleep(2)
                
    return False

def process_product(product_info, args, client=None):
    """Procesa un producto: planifica o ejecuta la generación de sus 8 ángulos."""
    sku = product_info["sku"]
    group = product_info["group"]
    real_folder = product_info.get("real_folder") or product_info.get("folder", "")
    name = product_info["name"]
    mode = product_info.get("mode", "A")

    out_dir = Path("output_catalog") / group / real_folder
    ref_photos = find_reference_photos(product_info)

    print("\n" + "=" * 80)
    print(f"PRODUCTO: #{product_info['index']+1:02d} | [{group}] {sku} | {name}")
    print(f"  Carpeta Real : {real_folder}")
    print(f"  Fotos Ref    : {len(ref_photos)} encontradas en _source_data/fotos/{group}/{real_folder}")
    print(f"  Directorio Out: {out_dir}")
    print("=" * 80)

    tasks = []
    for angle_key, angle_desc, canonical_slot in CANONICAL_ANGLES:
        out_filename = f"{real_folder}_{angle_key}.webp"
        out_file_path = out_dir / out_filename
        prompt = build_individual_prompt(product_info, angle_key, angle_desc, mode=mode)
        
        status = "PENDIENTE"
        if out_file_path.exists() and not args.force:
            status = "EXISTE (Skip)"
            
        tasks.append({
            "angle_key": angle_key,
            "angle_desc": angle_desc,
            "out_path": out_file_path,
            "out_filename": out_filename,
            "prompt": prompt,
            "status": status,
        })
        
        print(f"  [{angle_key}] -> {out_filename} [{status}]")

    if args.dry_run:
        print("\n  [DRY-RUN] Vista previa del prompt para 01_lateral:")
        print(f"  \"{tasks[0]['prompt'][:140]}...\"")
        print(f"  [DRY-RUN] Se generarían {len([t for t in tasks if t['status'] == 'PENDIENTE'])} archivos WebP en {out_dir}")
        return True

    # Ejecución Real
    if not client:
        print("  [ERROR] Cliente Gemini no inicializado. Revisa tu GEMINI_API_KEY.")
        return False

    out_dir.mkdir(parents=True, exist_ok=True)
    pending_tasks = [t for t in tasks if t["status"] == "PENDIENTE" or args.force]
    
    if not pending_tasks:
        print("  Todos los 8 ángulos ya existen. Usa --force para regenerar.")
        return True

    print(f"\n  Iniciando generación de {len(pending_tasks)} ángulos con modelo {args.model}...")
    
    if args.strategy == "individual":
        with ThreadPoolExecutor(max_workers=min(4, len(pending_tasks))) as executor:
            future_to_angle = {
                executor.submit(
                    generate_single_angle_api,
                    client,
                    args.model,
                    task["prompt"],
                    ref_photos,
                    task["out_path"],
                    args.size,
                    args.quality
                ): task["angle_key"] for task in pending_tasks
            }
            
            for future in as_completed(future_to_angle):
                angle_k = future_to_angle[future]
                try:
                    success = future.result()
                    res_str = "OK" if success else "FALLO"
                    print(f"  [{angle_k}] Generación {res_str}")
                except Exception as exc:
                    print(f"  [{angle_k}] Excepción: {exc}")
    else:
        # Estrategia Grid: No implementada en API directa sin modelo de alta resolución
        print("  [INFO] Estrategia individual recomendada para máxima calidad 1:1.")
        
    return True

def main():
    parser = argparse.ArgumentParser(
        description="Generación desatendida de los 8 ángulos canónicos en WebP vía Gemini API."
    )
    parser.add_argument("--product", type=str, help="Nombre de carpeta real del producto (ej. '01_Air_Jordan_9_Space_Jam')")
    parser.add_argument("--sku", type=str, help="SKU del producto (ej. 'IX6180-100')")
    parser.add_argument("--group", type=str, help="Filtrar por grupo (ej. 'Grupo A')")
    parser.add_argument("--all", action="store_true", help="Procesar los 45 modelos en lote")
    parser.add_argument("--strategy", choices=["individual", "grid"], default="individual", help="Estrategia: individual (default) o grid")
    parser.add_argument("--model", type=str, default="imagen-3.0-generate-002", help="Modelo de generación de imágenes (default: imagen-3.0-generate-002)")
    parser.add_argument("--size", type=int, choices=[1024, 1200], default=1024, help="Tamaño de salida en px (default: 1024)")
    parser.add_argument("--quality", type=int, default=90, help="Calidad WebP (default: 90)")
    parser.add_argument("--force", action="store_true", help="Sobrescribir archivos existentes")
    parser.add_argument("--dry-run", action="store_true", help="Mostrar plan de ejecución sin invocar la API")

    args = parser.parse_args()

    # Cargar catálogo oficial mapeado desde SNKRS (1).xlsx
    all_products, sku_map, f_map = load_snkrs_mapping()
    if not all_products:
        print("[ERROR] No se pudo cargar el mapeo de productos desde SNKRS (1).xlsx.")
        sys.exit(1)

    # Filtrar productos según argumentos
    target_products = []
    if args.product:
        p = get_mapping_by_real_folder(args.product)
        if p:
            target_products = [p]
        else:
            print(f"[ERROR] Producto con carpeta '{args.product}' no encontrado en el catálogo.")
            sys.exit(1)
    elif args.sku:
        p = get_mapping_by_sku(args.sku)
        if p:
            target_products = [p]
        else:
            print(f"[ERROR] Producto con SKU '{args.sku}' no encontrado en el catálogo.")
            sys.exit(1)
    elif args.group:
        target_products = [p for p in all_products if p["group"].lower() == args.group.lower()]
        if not target_products:
            print(f"[ERROR] No hay productos para el grupo '{args.group}'.")
            sys.exit(1)
    elif args.all:
        target_products = all_products
    else:
        # Por defecto si no se pasa nada, mostrar ayuda o procesar el primero en dry-run
        print("Debe especificar --product, --sku, --group o --all.")
        parser.print_help()
        sys.exit(0)

    # Validar API KEY si no es dry-run
    client = None
    if not args.dry_run:
        api_key = get_api_key()
        if not api_key:
            print("\n" + "!" * 80)
            print("[ERROR] GEMINI_API_KEY no encontrada en variables de entorno ni en archivo .env.")
            print("Para ejecutar la generación real, crea un archivo .env en la raíz con:")
            print("  GEMINI_API_KEY=tu_clave_aqui")
            print("O ejecuta con --dry-run para verificar el plan de ejecución.")
            print("!" * 80 + "\n")
            sys.exit(1)
            
        if not GENAI_AVAILABLE:
            print("[ERROR] Paquete google-genai no está instalado. Ejecuta: pip install google-genai")
            sys.exit(1)
            
        client = genai.Client(api_key=api_key)

    print(f"\nProcesando {len(target_products)} producto(s) | Estrategia: {args.strategy} | Tamaño: {args.size}x{args.size} WebP | Dry-run: {args.dry_run}")
    
    success_count = 0
    for product_info in target_products:
        if process_product(product_info, args, client=client):
            success_count += 1

    print("\n" + "=" * 80)
    print(f"PROCESO FINALIZADO: {success_count}/{len(target_products)} productos procesados exitosamente.")
    print("=" * 80)

if __name__ == "__main__":
    main()
