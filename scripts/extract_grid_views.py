#!/usr/bin/env python3
"""
scripts/extract_grid_views.py
=============================================================================
Extrae las 8 vistas RGBA limpias (sin etiquetas, sin bordes de grilla y sin
sombra de piso) desde una hoja de contacto 4x2 (1K, 2K o 4K).
Maneja automáticamente celdas con doble zapatilla (05 | FRONT y 06 | REAR en
el formato "Plantilla Maestra — Pares") quedándose solo con la zapatilla
izquierda correspondiente.
"""

import argparse
import os
import sys
from typing import Dict, Optional

import cv2
import numpy as np
from PIL import Image

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)
for p in (CURRENT_DIR, PROJECT_DIR):
    if p not in sys.path:
        sys.path.insert(0, p)

from split_grid_angles import PANEL_NAMES_8, clean_background_compression, clean_label_connected_components
from color_lock import extract_studio_whitebg_rgba


def _keep_primary_shoe_if_pair(cell_rgb: Image.Image, angle_slug: str) -> Image.Image:
    """
    Si una celda (ej. 05_front o 06_rear) contiene dos zapatillas lado a lado
    separadas por un pasillo blanco central, recorta únicamente la zapatilla izquierda.
    """
    if angle_slug not in ("05_front", "06_rear"):
        return cell_rgb

    arr = np.array(cell_rgb.convert("RGB"))
    h, w, _ = arr.shape
    non_white = np.any(arr < 242, axis=2)

    # Ignorar franja superior donde podría quedar rastro de borde
    col_hits = non_white[int(h * 0.12) : int(h * 0.92), :].sum(axis=0)
    # Buscar un valle blanco claro en el tercio central (35%..65% del ancho)
    x_start = int(w * 0.35)
    x_end = int(w * 0.65)
    center_hits = col_hits[x_start:x_end]
    if len(center_hits) == 0:
        return cell_rgb

    min_hits = int(center_hits.min())
    left_mass = int(col_hits[:x_start].sum())
    right_mass = int(col_hits[x_end:].sum())

    # Solo dividir si ambos lados tienen masa sustancial (>15% del menor) y hay pasillo casi vacío en medio
    if min_hits <= max(2, int(h * 0.015)) and left_mass > 500 and right_mass > 500:
        valley_rel = int(np.argmin(center_hits))
        split_x = x_start + valley_rel
        # Verificar que exista una banda de al menos 6 px casi vacía
        zero_cols = np.where(center_hits <= max(2, int(h * 0.015)))[0]
        if len(zero_cols) >= 6:
            split_x = x_start + int(np.median(zero_cols))
            return cell_rgb.crop((0, 0, split_x, h))

    return cell_rgb


def extract_8_views_from_grid(
    grid_path: str,
    out_rgba_dir: Optional[str] = None,
    rembg_session=None,
) -> Dict[str, Image.Image]:
    """
    Corta una cuadrícula 4x2 en sus 8 paneles, limpia etiquetas/bordes y extrae
    recortes RGBA sin sombra de piso listos para reconstrucción y proyección 3D.
    """
    grid_im = Image.open(grid_path).convert("RGB")
    gw, gh = grid_im.size
    cell_w = gw / 2.0
    cell_h = gh / 4.0

    # Recorte de margen interno seguro (1.8%) para eliminar líneas divisorias de 1-2px
    trim_x = max(4, int(cell_w * 0.018))
    trim_y = max(4, int(cell_h * 0.018))

    if rembg_session is None:
        import rembg

        rembg_session = rembg.new_session("u2net")

    if out_rgba_dir:
        os.makedirs(out_rgba_dir, exist_ok=True)

    views: Dict[str, Image.Image] = {}
    for idx, slug in enumerate(PANEL_NAMES_8):
        row = idx // 2
        col = idx % 2
        x0 = int(round(col * cell_w)) + trim_x
        y0 = int(round(row * cell_h)) + trim_y
        x1 = int(round((col + 1) * cell_w)) - trim_x
        y1 = int(round((row + 1) * cell_h)) - trim_y

        panel = grid_im.crop((x0, y0, x1, y1))
        arr = np.array(panel)
        clean_label_connected_components(arr, max_y_ratio=0.16, max_x_ratio=0.40)
        clean_background_compression(arr, threshold=244)
        clean_panel = Image.fromarray(arr, mode="RGB")

        # Si 05_front o 06_rear trae par lado a lado, conservar solo la zapatilla izquierda
        single_panel = _keep_primary_shoe_if_pair(clean_panel, slug)

        # Extraer RGBA preservando cuero blanco y pasadores negros sin mordidas de rembg
        rgba = extract_studio_whitebg_rgba(single_panel, rembg_session=rembg_session, angle_slug=slug)
        views[slug] = rgba

        if out_rgba_dir:
            rgba.save(os.path.join(out_rgba_dir, f"{slug}.png"))

    return views


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extrae 8 vistas RGBA limpias desde un grid 4x2.")
    parser.add_argument("grid_path", help="Ruta al archivo de cuadrícula 4x2.")
    parser.add_argument("--out-dir", required=True, help="Carpeta destino para los 8 PNG RGBA.")
    args = parser.parse_args()

    res = extract_8_views_from_grid(args.grid_path, out_rgba_dir=args.out_dir)
    print(f"Extraídas {len(res)} vistas RGBA en {args.out_dir}: {sorted(res.keys())}")
