#!/usr/bin/env python3
"""
scripts/reference_metrics.py
=============================================================================
Módulo de calibración maestro basado en output_catalog/REFERENCIA/
Calcula y aplica las métricas exactas de encuadre, escala y línea de suelo
(bottom_y_baseline) para garantizar uniformidad visual 100% en todo el catálogo.
=============================================================================
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

DEFAULT_REF_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output_catalog", "REFERENCIA")

ANGLE_FILE_MAP = {
    "01_lateral": "01-lateral.webp",
    "02_medial": "02-medial.webp",
    "03_3-4_front": "03-3-4-front.webp",
    "04_3-4_rear": "04-3-4-rear.webp",
    "05_front": "05-front.webp",
    "06_rear": "06-rear.webp",
    "07_top_down": "07-top-down.webp",
    "08_outsole": "08-outsole.webp",
}

# Cache de métricas calculadas
_CACHED_METRICS = None

def compute_reference_metrics(ref_dir=DEFAULT_REF_DIR):
    """
    Lee las 8 imágenes de output_catalog/REFERENCIA/ y calcula métricas
    normalizadas (ratios respecto al lienzo 1024x1024) para cada ángulo.
    """
    global _CACHED_METRICS
    metrics = {}
    
    if not os.path.exists(ref_dir):
        # Fallback de seguridad si no existiera la carpeta
        for slug in ANGLE_FILE_MAP:
            metrics[slug] = {
                "w_ratio": 0.72,
                "h_ratio": 0.45,
                "cx_ratio": 0.50,
                "cy_ratio": 0.50,
                "bottom_y_ratio": 0.73,
                "is_grounded": slug not in ["07_top_down", "08_outsole"],
                "target_aspect": 1.60
            }
        _CACHED_METRICS = metrics
        return metrics

    for slug, filename in ANGLE_FILE_MAP.items():
        fp = os.path.join(ref_dir, filename)
        if not os.path.exists(fp):
            # Check for .png variant (e.g. in REFERENCIA-HD)
            png_name = filename.replace(".webp", ".png")
            fp_png = os.path.join(ref_dir, png_name)
            if os.path.exists(fp_png):
                fp = fp_png
                filename = png_name
            else:
                continue
            
        im = Image.open(fp).convert("RGB")
        w_canvas, h_canvas = im.size
        arr = np.array(im)
        
        # Píxeles del producto (no blancos puros)
        mask = np.any(arr < 248, axis=2)
        y_idx, x_idx = np.where(mask)
        if not len(x_idx):
            continue
            
        xmin, xmax = int(x_idx.min()), int(x_idx.max())
        ymin, ymax = int(y_idx.min()), int(y_idx.max())
        
        bw = xmax - xmin + 1
        bh = ymax - ymin + 1
        cx = (xmin + xmax) / 2.0
        cy = (ymin + ymax) / 2.0
        bottom_y = ymax
        
        is_grounded = slug in ["01_lateral", "02_medial", "03_3-4_front", "04_3-4_rear", "05_front", "06_rear"]
        
        metrics[slug] = {
            "slug": slug,
            "filename": filename,
            "canvas_size": (w_canvas, h_canvas),
            "bbox_pixels": (xmin, ymin, xmax, ymax),
            "width_px": bw,
            "height_px": bh,
            "w_ratio": bw / w_canvas,
            "h_ratio": bh / h_canvas,
            "cx_ratio": cx / w_canvas,
            "cy_ratio": cy / h_canvas,
            "bottom_y_ratio": bottom_y / h_canvas,
            "target_aspect": bw / bh if bh > 0 else 1.0,
            "is_grounded": is_grounded
        }
        
    _CACHED_METRICS = metrics
    return metrics

def get_metrics(ref_dir=DEFAULT_REF_DIR):
    global _CACHED_METRICS
    if _CACHED_METRICS is None:
        return compute_reference_metrics(ref_dir)
    return _CACHED_METRICS

def align_and_canvas(
    rgba_image,
    angle_slug,
    target_size=1024,
    ref_dir=DEFAULT_REF_DIR
):
    """
    Ajusta una imagen con canal alfa recortada al encuadre, escala y línea de suelo
    exactos del ángulo maestro en output_catalog/REFERENCIA/.
    
    Retorna PIL.Image en modo RGB sobre lienzo blanco puro #FFFFFF.
    """
    metrics = get_metrics(ref_dir).get(angle_slug)
    
    # Obtener recorte ajustado por máscara alfa
    arr = np.array(rgba_image)
    if arr.ndim == 3 and arr.shape[2] == 4:
        alpha = arr[:, :, 3]
        y_idx, x_idx = np.where(alpha > 15)
    else:
        # Si es RGB
        mask = np.any(arr < 248, axis=2)
        y_idx, x_idx = np.where(mask)
        
    if not len(x_idx):
        return Image.new("RGB", (target_size, target_size), (255, 255, 255))
        
    xmin, xmax = int(x_idx.min()), int(x_idx.max())
    ymin, ymax = int(y_idx.min()), int(y_idx.max())
    crop = rgba_image.crop((xmin, ymin, xmax + 1, ymax + 1))
    cw, ch = crop.size
    
    if metrics:
        target_w = target_size * metrics["w_ratio"]
        target_h = target_size * metrics["h_ratio"]
        target_bottom_y = int(target_size * metrics["bottom_y_ratio"])
        target_cx = int(target_size * metrics["cx_ratio"])
        is_grounded = metrics["is_grounded"]
        
        aspect = cw / ch if ch > 0 else 1.0

        # Ajuste armónico de escala según la geometría del ángulo
        if angle_slug in ["05_front", "06_rear"]:
            if aspect < 0.95:
                # Toma frontal o trasera individual: la altura debe ser prominente (~63% del lienzo)
                # para tener la misma presencia visual y masa que el perfil lateral
                target_h_prominent = int(target_size * 0.63)
                target_w_max = int(target_size * 0.85)
                scale = min(target_w_max / cw, target_h_prominent / ch)
                target_cx = target_size // 2
            else:
                # Toma de par horizontal
                scale = min(target_w / cw, target_h / ch)

        elif angle_slug in ["07_top_down", "08_outsole"]:
            # Tomas cenitales o de suela: la dimensión mayor debe llenar ~79% del lienzo
            # ya sea que la zapatilla esté fotografiada en orientación vertical u horizontal
            target_max_dim = int(target_size * 0.79)
            scale = target_max_dim / max(cw, ch)
            target_cx = target_size // 2

        else:
            # Perfil lateral, medial y 3/4
            scale = min(target_w / cw, target_h / ch)
        
        # Permitir ajuste sutil si el aspect ratio difiere ligeramente (máx 15%)
        # para que la zapatilla tenga la misma presencia visual
        nw = max(10, int(cw * scale))
        nh = max(10, int(ch * scale))
        
        # Asegurar margen de seguridad para no salirse del lienzo
        if nw > target_size * 0.92:
            s_adj = (target_size * 0.92) / nw
            nw = int(nw * s_adj)
            nh = int(nh * s_adj)
        if nh > target_size * 0.88:
            s_adj = (target_size * 0.88) / nh
            nw = int(nw * s_adj)
            nh = int(nh * s_adj)
            
        resized = crop.resize((nw, nh), Image.Resampling.LANCZOS)
        
        canvas = Image.new("RGBA", (target_size, target_size), (255, 255, 255, 255))
        
        # Posicionamiento:
        if is_grounded:
            blur_r = max(4, int(target_size * 0.006))
            sh = max(10, int(nh * 0.075))
            sw = int(nw * 0.88)
            
            # Alinear exactamente para que la base de contacto toque target_bottom_y
            pos_y = target_bottom_y - nh - int(sh * 0.55) - blur_r
            pos_x = target_cx - (nw // 2)
            
            # Ajustar límites de seguridad verticales y horizontales
            if pos_y < int(target_size * 0.05):
                pos_y = int(target_size * 0.05)
            if pos_x < int(target_size * 0.03):
                pos_x = int(target_size * 0.03)
            elif pos_x + nw > target_size - int(target_size * 0.03):
                pos_x = target_size - nw - int(target_size * 0.03)
                
            # Sombra de contacto en la base exactamente calibrada
            shadow = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(shadow)
            sx0 = pos_x + (nw - sw) // 2
            sy0 = pos_y + nh - int(sh * 0.45)
            draw.ellipse([sx0, sy0, sx0 + sw, sy0 + sh], fill=(25, 25, 25, 38))
            shadow = shadow.filter(ImageFilter.GaussianBlur(radius=blur_r))
            canvas.alpha_composite(shadow)
        else:
            # Ungrounded (07_top_down, 08_outsole): centrado armónico perfecto en el lienzo
            pos_x = (target_size - nw) // 2
            pos_y = (target_size - nh) // 2
            
            # Límites de seguridad
            pos_x = max(int(target_size * 0.04), min(pos_x, target_size - nw - int(target_size * 0.04)))
            pos_y = max(int(target_size * 0.04), min(pos_y, target_size - nh - int(target_size * 0.04)))

        canvas.alpha_composite(resized, (pos_x, pos_y))
        return canvas.convert("RGB")
        
    else:
        # Fallback genérico centrado fill_ratio 0.82
        max_dim = int(target_size * 0.82)
        scale = min(max_dim / cw, max_dim / ch)
        nw = max(10, int(cw * scale))
        nh = max(10, int(ch * scale))
        resized = crop.resize((nw, nh), Image.Resampling.LANCZOS)
        
        canvas = Image.new("RGBA", (target_size, target_size), (255, 255, 255, 255))
        pos_x = (target_size - nw) // 2
        pos_y = (target_size - nh) // 2
        
        if angle_slug not in ["07_top_down", "08_outsole"]:
            shadow = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(shadow)
            sw = int(nw * 0.85)
            sh = max(12, int(nh * 0.08))
            sx0 = (target_size - sw) // 2
            sy0 = pos_y + nh - int(sh * 0.45)
            draw.ellipse([sx0, sy0, sx0 + sw, sy0 + sh], fill=(25, 25, 25, 38))
            shadow = shadow.filter(ImageFilter.GaussianBlur(radius=8))
            canvas.alpha_composite(shadow)
            
        canvas.alpha_composite(resized, (pos_x, pos_y))
        return canvas.convert("RGB")

def print_metrics_table(metrics=None):
    """Imprime una tabla formateada con las métricas calibradas."""
    if metrics is None:
        metrics = get_metrics()
        
    print("\n" + "=" * 90)
    print("📏 MÉTRICAS MAESTRAS CALIBRADAS DESDE output_catalog/REFERENCIA/ (Lienzo 1024x1024)")
    print("=" * 90)
    print(f"{'Ángulo (Slug)':16s} | {'Archivo Ref':17s} | {'BBox Ref (px)':22s} | {'Ancho':6s} | {'Alto':6s} | {'Baseline Y':10s} | {'Aspect':6s}")
    print("-" * 90)
    for slug, m in metrics.items():
        bbox_str = f"({m['bbox_pixels'][0]:3d},{m['bbox_pixels'][1]:3d},{m['bbox_pixels'][2]:3d},{m['bbox_pixels'][3]:3d})"
        baseline_str = f"{m['bottom_y_ratio']*1024:.0f} px ({m['bottom_y_ratio']*100:.1f}%)"
        print(f"{slug:16s} | {m['filename']:17s} | {bbox_str:22s} | {m['width_px']:4d}px | {m['height_px']:4d}px | {baseline_str:10s} | {m['target_aspect']:.2f}")
    print("=" * 90 + "\n")

if __name__ == "__main__":
    m = compute_reference_metrics()
    print_metrics_table(m)
