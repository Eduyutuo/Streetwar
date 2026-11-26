"""
scripts/snkrs_mapping.py
=============================================================================
Módulo centralizado de mapeo SKU <-> Nombre_Carpeta_Real (SNKRS (1).xlsx)
=============================================================================
Cruce oficial 1:1 entre los 45 modelos del Excel SNKRS (1) y las carpetas
físicas reales en _source_data/fotos/Grupo A..G
"""

import os
import re
import openpyxl

EXCEL_PATH = os.path.join(os.path.dirname(__file__), "..", "SNKRS (1).xlsx")
FOTOS_ROOT = os.path.join(os.path.dirname(__file__), "..", "_source_data", "fotos")

GROUPS = ['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D', 'Grupo E', 'Grupo F', 'Grupo G']

def clean_model_name(name):
    if not name:
        return ""
    c = str(name).replace('“', '"').replace('”', '"').replace('’', "'")
    c = c.replace('Spam Jam', 'Space Jam')
    return c.strip()

def normalize_sku(sku_str):
    if not sku_str:
        return ""
    return re.sub(r'[\s_]+', '-', str(sku_str).strip().upper())

def load_snkrs_mapping(excel_path=EXCEL_PATH, fotos_root=FOTOS_ROOT):
    """
    Carga el Excel SNKRS (1).xlsx y lo cruza 1:1 con las carpetas físicas de _source_data/fotos.
    Retorna:
      - products: lista ordenada de los 45 modelos
      - sku_to_info: dict indexado por SKU normalizado
      - folder_to_info: dict indexado por nombre de carpeta real
    """
    wb = openpyxl.load_workbook(excel_path)
    ws = wb.active

    excel_rows = []
    current_group = None
    for r in range(1, ws.max_row + 1):
        vals = [cell.value for cell in ws[r]]
        col1 = vals[1] if len(vals) > 1 else None
        if isinstance(col1, str) and col1.strip().upper() in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            current_group = f"Grupo {col1.strip().upper()}"
            continue
        if isinstance(col1, int) and col1 <= 45 and vals[3]:
            raw_code = str(vals[8]).strip() if len(vals) > 8 and vals[8] else ''
            norm_sku = normalize_sku(raw_code)
            excel_rows.append({
                'num': col1,
                'excel_group': current_group,
                'category': str(vals[2]).strip() if vals[2] else '',
                'excel_name': clean_model_name(vals[3]),
                'raw_code': raw_code,
                'sku': norm_sku
            })

    # Escanear carpetas físicas en fotos_root
    physical_folders = []
    for g in GROUPS:
        gp = os.path.join(fotos_root, g)
        if not os.path.exists(gp):
            continue
        pdirs = sorted([d for d in os.listdir(gp) if os.path.isdir(os.path.join(gp, d)) and not d.lower().startswith(('resultado', 'ref'))])
        for pd in pdirs:
            physical_folders.append((g, pd, os.path.join(gp, pd)))

    if len(physical_folders) != 45:
        raise RuntimeError(f"Se esperaban 45 carpetas en _source_data/fotos, pero se encontraron {len(physical_folders)}")

    products = []
    sku_to_info = {}
    folder_to_info = {}

    for i in range(45):
        ex = excel_rows[i]
        fg, fdir, fpath = physical_folders[i]

        info = {
            'index': i,
            'index_display': i + 1,
            'group': fg,
            'sku': ex['sku'],
            'raw_code': ex['raw_code'],
            'name': ex['excel_name'],
            'category': ex['category'],
            'folder': fdir,
            'folder_path': fpath
        }
        products.append(info)
        sku_to_info[ex['sku']] = info
        folder_to_info[fdir] = info

    return products, sku_to_info, folder_to_info

def get_mapping_by_sku(sku):
    _, sku_map, _ = load_snkrs_mapping()
    norm = normalize_sku(sku)
    return sku_map.get(norm)

def get_mapping_by_real_folder(folder_name):
    _, _, f_map = load_snkrs_mapping()
    return f_map.get(folder_name)

if __name__ == '__main__':
    prods, sku_map, f_map = load_snkrs_mapping()
    print(f"Cargados {len(prods)} productos cruzados 1:1 exitosamente.")
    print("Muestra:", prods[0])
