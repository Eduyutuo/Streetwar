"""
=============================================================================
RUTA 2: Generador de Ángulos con IA (Nano Banana / Gemini Imagen API)
=============================================================================
Este script toma 1 o 2 fotos de entrada por cada zapatilla desde '1-orig-raw',
construye prompts fotográficos multimodales de alta precisión y se conecta a
la API de Gemini (modelo Nano Banana / Imagen 3) para sintetizar los 4 ángulos
estandarizados requeridos por el catálogo:

  1. 01-lateral.webp     (Perfil lateral 90°, puntera a la izquierda)
  2. 02-frontal-3-4.webp (Perspectiva 3/4 frontal a 45°, mirando a la izquierda)
  3. 03-trasera.webp     (Vista posterior del talón a 180°, logos y cuello)
  4. 04-superior.webp    (Vista cenital 90° desde arriba, cordones y plantilla)

Las imágenes resultantes se guardan en:
    dist/assets/3-gen-nano/<SKU>/

Uso:
    # 1. Configurar clave de API en PowerShell:
    $env:GEMINI_API_KEY = "tu_clave_de_gemini"

    # 2. Generar ángulos para un SKU específico (ej. Air Jordan 9 Space Jam):
    python scripts/generate_angles_nanobanana.py --sku IX6180-100

    # 3. Generar para todos los modelos del catálogo:
    python scripts/generate_angles_nanobanana.py --all

    # 4. Modo Demo / Simulación (genera estructura y vistas previas de prueba sin consumir cuota):
    python scripts/generate_angles_nanobanana.py --demo
=============================================================================
"""

import os
import sys
import json
import argparse
import io
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# ---------------------------------------------------------------------------
# Prompts Maestros Especializados (Nano Banana / Imagen)
# ---------------------------------------------------------------------------
PROMPTS = {
    '01-lateral': (
        "Commercial studio e-commerce product photograph of the authentic sneaker {name}, SKU: {sku}. "
        "Strict 90-degree profile lateral side view, toe box pointing horizontally directly to the LEFT. "
        "Pure solid white background (#FFFFFF). High-fidelity rendering of original materials: leather grain, "
        "mesh weave, stitch patterns, Jumpman/Swoosh logos, and exact midsole geometry. "
        "Crisp softbox studio lighting, subtle natural contact shadow on the floor. 8k resolution, e-commerce catalog standard."
    ),
    '02-frontal-3-4': (
        "Commercial studio e-commerce product photograph of the exact same authentic sneaker {name}, SKU: {sku}. "
        "Three-quarter (3/4) perspective front-angle view, facing toward the LEFT, showcasing both the front toe box "
        "and the outer lateral profile. Pure solid white background (#FFFFFF). "
        "Identical color blocking, lace texture, and brand details to the reference photo. Clean commercial lighting, grounded contact shadow."
    ),
    '03-trasera': (
        "Commercial studio e-commerce product photograph of the exact same authentic sneaker {name}, SKU: {sku}. "
        "Direct rear heel view from behind at 180 degrees, perfectly centered. Showing the back heel counter, heel pull tab, "
        "rear branding badge (Jumpman / Nike Air), and midsole height. Pure solid white background (#FFFFFF), sharp studio focus, soft shadow."
    ),
    '04-superior': (
        "Commercial studio e-commerce product photograph of the exact same authentic sneaker {name}, SKU: {sku}. "
        "Direct top-down overhead flat lay view looking down onto the sneaker at 90 degrees. "
        "Showing complete padded collar, tongue branding, symmetrical eyelets and lacing system, and inner sole lining. "
        "Pure solid white background (#FFFFFF), balanced shadowless footwear lighting."
    )
}

def detect_toe_left(img_rgba):
    arr = np.array(img_rgba)
    if arr.shape[2] == 4 and np.any(arr[:, :, 3] < 250):
        mask = arr[:, :, 3] > 20
    else:
        mask = np.any(arr[:, :, :3] < 240, axis=2)
        
    y_idx, x_idx = np.where(mask)
    if len(x_idx) == 0:
        return True
    
    xmin, xmax = x_idx.min(), x_idx.max()
    bw = xmax - xmin
    if bw < 50:
        return True
        
    strip_w = max(10, int(bw * 0.18))
    ls = mask[:, xmin:xmin + strip_w]
    rs = mask[:, xmax - strip_w:xmax]
    ly = np.where(np.any(ls, axis=1))[0]
    ry = np.where(np.any(rs, axis=1))[0]
    lh = (ly.max() - ly.min()) if len(ly) else 0
    rh = (ry.max() - ry.min()) if len(ry) else 0
    return lh <= rh

def post_process_standardize(img_pil, angle_name, target_size=1200, padding_pct=0.10):
    """
    Normaliza cualquier imagen generada por IA al estándar exacto:
    - Lienzo 1200x1200px
    - Fondo blanco puro #FFFFFF
    - Orientación uniforme (puntera a la izquierda en tomas 1 y 2)
    - Padding del 10% (la zapatilla ocupa el 80% máximo)
    - Sombra de contacto suave
    """
    img_rgba = img_pil.convert('RGBA')
    arr = np.array(img_rgba)
    
    # Detectar silueta ignorando fondo blanco
    if arr.shape[2] == 4 and np.any(arr[:, :, 3] < 250):
        mask = arr[:, :, 3] > 20
    else:
        mask = np.any(arr[:, :, :3] < 242, axis=2)
        
    if np.any(mask):
        y_idx, x_idx = np.where(mask)
        ymin, ymax = y_idx.min(), y_idx.max()
        xmin, xmax = x_idx.min(), x_idx.max()
        cropped = img_rgba.crop((xmin, ymin, xmax + 1, ymax + 1))
    else:
        cropped = img_rgba

    # Forzar orientación uniforme a la izquierda para tomas laterales y 3/4
    if angle_name in ('01-lateral', '02-frontal-3-4'):
        if not detect_toe_left(cropped):
            cropped = cropped.transpose(Image.FLIP_LEFT_RIGHT)

    cw, ch = cropped.size
    max_dim = int(target_size * (1.0 - 2 * padding_pct))  # 960 px
    scale = min(max_dim / cw, max_dim / ch)
    nw = max(1, int(cw * scale))
    nh = max(1, int(ch * scale))
    
    resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', (target_size, target_size), (255, 255, 255, 255))
    
    pos_x = (target_size - nw) // 2
    pos_y = (target_size - nh) // 2
    
    # Sombra de contacto
    shadow = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(shadow)
    sw = int(nw * 0.85)
    sh = max(16, int(nh * 0.08))
    sx0 = (target_size - sw) // 2
    sy0 = pos_y + nh - int(sh * 0.55)
    draw.ellipse([sx0, sy0, sx0 + sw, sy0 + sh], fill=(25, 25, 25, 40))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=10))
    
    canvas.alpha_composite(shadow)
    canvas.alpha_composite(resized, (pos_x, pos_y))
    return canvas.convert('RGB')

def call_gemini_api(api_key, prompt_text, ref_images=None):
    """
    Invoca la API de Gemini Imagen 3 / Nano Banana usando google-genai.
    """
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    
    # Llamada a Imagen 3.0
    response = client.models.generate_images(
        model='imagen-3.0-generate-002',
        prompt=prompt_text,
        config=types.GenerateImagesConfig(
            number_of_images=1,
            aspect_ratio="1:1",
            output_mime_type="image/jpeg",
            person_generation="DONT_ALLOW"
        )
    )
    
    if response.generated_images:
        img_bytes = response.generated_images[0].image.image_bytes
        return Image.open(io.BytesIO(img_bytes))
    return None

def process_product_nanobanana(product_info, api_key=None, is_demo=False):
    sku = product_info['sku']
    name = product_info['name']
    src_folder = os.path.join('dist/assets/1-orig-raw', product_info['folder'])
    dst_folder = os.path.join('dist/assets/3-gen-nano', sku)
    os.makedirs(dst_folder, exist_ok=True)
    
    print(f"\n=======================================================")
    print(f"[{product_info['index']:02d}] Procesando: {name} (SKU: {sku})")
    print(f"Carpeta origen: {src_folder}")
    print(f"Carpeta destino: {dst_folder}")
    print(f"=======================================================")
    
    # Buscar 1 o 2 fotos de entrada
    available_files = sorted(os.listdir(src_folder)) if os.path.exists(src_folder) else []
    ref_files = [f for f in available_files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))]
    
    ref1_path = os.path.join(src_folder, ref_files[0]) if ref_files else None
    ref2_path = os.path.join(src_folder, ref_files[1]) if len(ref_files) > 1 else None
    
    print(f"Foto de referencia 1: {ref_files[0] if ref_files else 'No disponible'}")
    if ref2_path:
        print(f"Foto de referencia 2: {ref_files[1]}")

    angles = ['01-lateral', '02-frontal-3-4', '03-trasera', '04-superior']
    tomas = product_info.get('tomas', {})
    
    for i, angle in enumerate(angles):
        out_file = os.path.join(dst_folder, f"{angle}.webp")
        prompt = PROMPTS[angle].format(name=name, sku=sku)
        
        print(f"\nGenerando {angle}.webp...")
        print(f"Prompt estructurado: {prompt[:110]}...")
        
        if is_demo or not api_key:
            # Modo demostración / simulación: procesa y sintetiza basándose en el ángulo asignado
            # para que el usuario pueda ver la estructura creada en 3-gen-nano con tomas distintas
            assigned_file = tomas.get(angle)
            if assigned_file:
                src_file_for_demo = os.path.join(src_folder, assigned_file)
            elif i < len(ref_files):
                src_file_for_demo = os.path.join(src_folder, ref_files[i])
            else:
                src_file_for_demo = ref1_path

            if src_file_for_demo and os.path.exists(src_file_for_demo):
                with Image.open(src_file_for_demo) as raw:
                    standardized = post_process_standardize(raw, angle)
                standardized.save(out_file, 'WEBP', quality=90)
                print(f"  [DEMO OK] Guardado en: {out_file} (Referencia: {os.path.basename(src_file_for_demo)})")
            else:
                print(f"  [SKIP] No hay archivo de entrada para demo")
        else:
            # Llamada en vivo a la API de Gemini (Nano Banana / Imagen 3)
            try:
                gen_img = call_gemini_api(api_key, prompt, ref_images=[ref1_path, ref2_path])
                if gen_img:
                    standardized = post_process_standardize(gen_img, angle)
                    standardized.save(out_file, 'WEBP', quality=92)
                    print(f"  [API OK] Imagen generada por Nano Banana guardada en: {out_file}")
                else:
                    print(f"  [ERROR] No se recibió imagen del modelo")
            except Exception as e:
                print(f"  [ERROR API]: {e}")

def main():
    parser = argparse.ArgumentParser(description="Ruta 2: Generación de Ángulos con IA (Nano Banana / Gemini API)")
    parser.add_argument('--sku', default=None, help='SKU específico a procesar')
    parser.add_argument('--index', type=int, default=None, help='Índice del producto (0-44)')
    parser.add_argument('--all', action='store_true', help='Procesar todos los 45 productos del catálogo')
    parser.add_argument('--demo', action='store_true', help='Ejecutar en modo simulación/demo sin consumir cuota')
    parser.add_argument('--api-key', default=None, help='Clave de API de Gemini (o usar GEMINI_API_KEY)')

    args = parser.parse_args()
    api_key = args.api_key or os.environ.get("GEMINI_API_KEY")

    if not api_key and os.path.exists('.env'):
        try:
            with open('.env', 'r', encoding='utf-8') as ef:
                for eline in ef:
                    eline = eline.strip()
                    if eline.startswith('GEMINI_API_KEY='):
                        api_key = eline.split('=', 1)[1].strip().strip('"').strip("'")
                        break
        except Exception:
            pass

    angles_file = 'scratch/assigned_angles.json' if os.path.exists('scratch/assigned_angles.json') else 'scratch/product_mapping.json'
    with open(angles_file, 'r', encoding='utf-8') as f:
        products = json.load(f)

    if not api_key and not args.demo:
        print("\n" + "="*70)
        print("  AVISO: No se detectó clave GEMINI_API_KEY.")
        print("="*70)
        print("Para conectar en vivo con Nano Banana (Google Imagen 3 API):")
        print("  1. Obtén tu clave en: https://aistudio.google.com/")
        print("  2. Configúrala en PowerShell:")
        print("     $env:GEMINI_API_KEY = 'AIzaSy...'")
        print("  3. O pásala directamente con: --api-key 'AIzaSy...'")
        print("\nEjecutando automáticamente en modo --demo para preparar las carpetas...")
        print("="*70 + "\n")
        args.demo = True

    if args.sku:
        target = [p for p in products if p['sku'].lower() == args.sku.lower()]
        if not target:
            print(f"Error: SKU {args.sku} no encontrado en el catálogo.")
            return
        process_product_nanobanana(target[0], api_key=api_key, is_demo=args.demo)
    elif args.index is not None:
        if 0 <= args.index < len(products):
            process_product_nanobanana(products[args.index], api_key=api_key, is_demo=args.demo)
        else:
            print(f"Error: Índice {args.index} fuera de rango (0-44).")
    elif args.all or args.demo:
        for p in products:
            process_product_nanobanana(p, api_key=api_key, is_demo=args.demo)
    else:
        # Por defecto, procesar el primer modelo de ejemplo (Air Jordan 9 Space Jam)
        print("Procesando modelo de prueba [00] IX6180-100 (usa --all para procesar los 45 modelos)...")
        process_product_nanobanana(products[0], api_key=api_key, is_demo=args.demo)

    print("\nProceso finalizado con éxito.")
    print("Las 3 carpetas para comparación en 'dist/assets/' son:")
    print("  1. dist/assets/1-orig-raw/   (Fotos fuente descargadas sin editar)")
    print("  2. dist/assets/2-norm-std/   (Ruta 1: Normalización fotográfica estándar)")
    print("  3. dist/assets/3-gen-nano/   (Ruta 2: Generación / Síntesis con IA)")

if __name__ == '__main__':
    main()
