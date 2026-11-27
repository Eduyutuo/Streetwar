#!/usr/bin/env python3
r"""
scripts/pilot_2d_pipeline.py
=============================================================================
Fase 1 & 2: Mejora IA con Referencia Real (deAPI) + Candado Cromático CIELAB
            + Tablero Interactivo de Aprobación (preview_aprobacion.html)
=============================================================================
Flujo:
  1. Toma las fotos reales 2K de _source_data/fotos-HD/{Grupo}/{Carpeta}/.
  2. Limpia el fondo con rembg sin dañar suelas blancas.
  3. Según --engine:
     - auto / deapi-qwen / deapi-klein: envía las fotos reales como referencia
       a deAPI (/api/v2/images/edits) con prompts de estudio 5500K y bloquea el
       color en espacio CIELAB (color_lock.py) contra la foto real.
     - local: aplica acabado de estudio local + candado CIELAB sin consumir API
       (útil para pruebas en seco o mientras se activan créditos).
  4. Guarda recortes RGBA limpios (para proyección 3D exacta) y WebP 1024x1024
     sobre #FFFFFF alineados con reference_metrics.py.
  5. Genera scratch/pilot_approval/preview_aprobacion.html para aprobar fotos.

Uso:
  .\.venv_hy3d\Scripts\python.exe scripts/pilot_2d_pipeline.py --engine local
  .\.venv_hy3d\Scripts\python.exe scripts/pilot_2d_pipeline.py --engine auto --skus IX6180-100 IO2076-100 CT3839-100
"""

import argparse
import base64
import io
import json
import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import requests
from PIL import Image

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)
for p in (CURRENT_DIR, PROJECT_DIR):
    if p not in sys.path:
        sys.path.insert(0, p)

from color_lock import (
    CANONICAL_STUDIO_SLUGS,
    enhance_studio_lighting_local,
    evaluate_fidelity,
    extract_clean_rgba,
    get_hd_source_map,
    load_catalog_metadata,
    lock_colors_lab,
    rgba_on_white,
    standardize_studio_angle,
)

DEFAULT_PILOT_SKUS = ["IX6180-100", "IO2076-100", "CT3839-100"]
DEAPI_BASE = "https://api.deapi.ai"

ANGLE_PROMPTS = {
    "01_lateral": (
        "Commercial e-commerce studio photograph of the exact same sneaker shown in the reference photo. "
        "Strict 90-degree outer lateral side profile view, toe pointing horizontally LEFT. "
        "Preserve exact colors, materials, leather grain, mesh weave, stitching, and brand logos unchanged. "
        "Seamless pure solid white #FFFFFF background, balanced 5500K softbox studio lighting, crisp f/8 focus, zero extra objects."
    ),
    "02_medial": (
        "Commercial e-commerce studio photograph of the exact same sneaker shown in the reference photo. "
        "Strict 90-degree inner medial side profile view, toe pointing horizontally RIGHT. "
        "Preserve exact colors, materials, stitching, midsole, and logos unchanged. "
        "Seamless pure solid white #FFFFFF background, balanced 5500K softbox studio lighting, crisp f/8 focus."
    ),
    "03_3-4_front": (
        "Commercial e-commerce studio photograph of the exact same sneaker shown in the reference photos. "
        "Three-quarter (3/4) front perspective view angled toward bottom-LEFT showing both toe box and outer lateral profile. "
        "Preserve exact colorway, materials, laces, midsole, and logos from the reference sneaker. "
        "Seamless pure solid white #FFFFFF background, balanced 5500K softbox studio lighting."
    ),
    "04_3-4_rear": (
        "Commercial e-commerce studio photograph of the exact same sneaker shown in the reference photos. "
        "Three-quarter (3/4) rear perspective view angled toward RIGHT showing heel counter and lateral profile. "
        "Preserve exact colorway, materials, heel badge, and sole geometry from the reference sneaker. "
        "Seamless pure solid white #FFFFFF background, balanced 5500K softbox studio lighting."
    ),
    "05_front": (
        "Commercial e-commerce studio photograph of the exact same sneaker shown in the reference photo. "
        "Direct straight-on eye-level front toe view, perfectly centered and upright. "
        "Preserve exact toe box shape, lace pattern, tongue logo, and colorway unchanged. "
        "Seamless pure solid white #FFFFFF background, balanced 5500K softbox studio lighting."
    ),
    "06_rear": (
        "Commercial e-commerce studio photograph of the exact same sneaker shown in the reference photo. "
        "Direct 180-degree rear heel view, perfectly centered and upright. "
        "Preserve exact heel counter shape, heel branding/numbers/logos, pull tab, and sole colors unchanged. "
        "Seamless pure solid white #FFFFFF background, balanced 5500K softbox studio lighting."
    ),
    "07_top_down": (
        "Commercial e-commerce studio photograph of the exact same sneaker shown in the reference photo. "
        "Direct 90-degree overhead top-down flat lay view, heel on left and toe pointing RIGHT. "
        "Preserve exact lacing, tongue, collar lining, and colors unchanged. "
        "Seamless pure solid white #FFFFFF background, uniform 5500K studio lighting."
    ),
    "08_outsole": (
        "Commercial e-commerce studio photograph of the exact same sneaker shown in the reference photos. "
        "Direct 90-degree flat bottom outsole rubber tread view, heel on left and toe pointing RIGHT, showing only the flat sole without floor shadow. "
        "Match exact midsole/outsole colorway and brand traction pattern of the reference sneaker. "
        "Seamless pure solid white #FFFFFF background, crisp f/8 studio focus."
    ),
}

NEGATIVE_PROMPT = (
    "changed colors, wrong colorway, distorted logos, misspelled text, warped sole, "
    "colored background, gray wall, table, human feet, hands, mannequin, blurry, lowres, plastic sheen"
)


class DeApiBalanceError(RuntimeError):
    """Error específico cuando la cuenta de deAPI no tiene saldo activo."""


def load_deapi_key(env_path: str = os.path.join(PROJECT_DIR, ".env")) -> str:
    """Lee DEAPI_API_KEY desde entorno o .env (soporta línea con o sin clave=)."""
    key = os.environ.get("DEAPI_API_KEY", "").strip()
    if key:
        return key
    if not os.path.exists(env_path):
        raise RuntimeError(f"No se encontró {env_path} ni la variable DEAPI_API_KEY.")
    with open(env_path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip() and not l.strip().startswith("#")]
    for line in lines:
        if line.startswith("DEAPI_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    if len(lines) == 1 and "=" not in lines[0]:
        return lines[0]
    raise RuntimeError("DEAPI_API_KEY no definida en .env")


class DeApiEditClient:
    """Cliente REST v2 para /api/v2/images/edits con control automático de rate limit (1 RPM)."""

    def __init__(self, api_key: str, min_interval_sec: float = 62.0):
        self.api_key = api_key
        self.min_interval_sec = min_interval_sec
        self.last_submit_ts = 0.0
        self.headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}

    def _wait_rate_limit(self):
        elapsed = time.time() - self.last_submit_ts
        if self.last_submit_ts > 0 and elapsed < self.min_interval_sec:
            wait = self.min_interval_sec - elapsed
            print(f"  [deAPI] Esperando {wait:.1f}s por límite de 1 petición/minuto (tier Basic)...", flush=True)
            time.sleep(wait)

    def edit(
        self,
        prompt: str,
        ref_images: List[Image.Image],
        model: str = "QwenImageEdit_Plus_NF4",
        width: int = 1024,
        height: int = 1024,
        steps: Optional[int] = None,
        seed: int = 42,
    ) -> Image.Image:
        if not ref_images:
            raise ValueError("Se requiere al menos una imagen de referencia.")

        if model == "QwenImageEdit_Plus_NF4":
            ref_images = ref_images[:1]
            width = min(width, 1024)
            height = min(height, 1024)
            steps = steps or 32
        else:
            ref_images = ref_images[:3]
            width = min(max(width, 256), 1536)
            height = min(max(height, 256), 1536)
            steps = 4 if model == "Flux_2_Klein_4B_BF16" else (steps or 25)

        files = []
        field_name = "image" if len(ref_images) == 1 else "images[]"
        for idx, im in enumerate(ref_images):
            buf = io.BytesIO()
            im.convert("RGB").save(buf, format="PNG")
            buf.seek(0)
            files.append((field_name, (f"ref_{idx}.png", buf, "image/png")))

        data = {
            "model": model,
            "prompt": prompt,
            "width": str(width),
            "height": str(height),
            "steps": str(steps),
            "seed": str(seed),
        }
        if model == "QwenImageEdit_Plus_NF4":
            data["negative_prompt"] = NEGATIVE_PROMPT

        for attempt in range(3):
            self._wait_rate_limit()
            # Rebobinar buffers en reintentos
            for _, (_, buf, _) in files:
                buf.seek(0)

            self.last_submit_ts = time.time()
            resp = requests.post(
                f"{DEAPI_BASE}/api/v2/images/edits",
                headers=self.headers,
                data=data,
                files=files,
                timeout=60,
            )

            if resp.status_code == 422:
                payload = resp.json()
                if payload.get("code") == "insufficient_balance":
                    raise DeApiBalanceError(
                        "Saldo insuficiente en deAPI ($0). Verifica tu correo en https://app.deapi.ai "
                        "para activar los $5 de crédito gratuito o recarga saldo."
                    )
                raise RuntimeError(f"deAPI 422 validation error: {resp.text}")

            if resp.status_code == 429:
                retry_after = float(resp.headers.get("Retry-After", "62"))
                print(f"  [deAPI] 429 Rate Limit, esperando {retry_after:.0f}s...", flush=True)
                time.sleep(retry_after + 1.0)
                continue

            if resp.status_code != 200:
                raise RuntimeError(f"deAPI HTTP {resp.status_code}: {resp.text[:300]}")

            req_id = resp.json()["data"]["request_id"]
            rem_day = resp.headers.get("X-RateLimit-Daily-Remaining", "?")
            print(f"  [deAPI] Job {req_id} enviado ({model}, cuota diaria restante: {rem_day})", flush=True)
            return self._poll_result(req_id)

        raise RuntimeError("Se agotaron reintentos en deAPI por rate limit.")

    def _poll_result(self, req_id: str, timeout_sec: int = 180) -> Image.Image:
        t0 = time.time()
        while time.time() - t0 < timeout_sec:
            time.sleep(2.5)
            r = requests.get(f"{DEAPI_BASE}/api/v2/jobs/{req_id}", headers=self.headers, timeout=30)
            if r.status_code != 200:
                continue
            jdata = r.json().get("data", {})
            st = jdata.get("status")
            if st == "done":
                img_bytes = requests.get(jdata["result_url"], timeout=60).content
                return Image.open(io.BytesIO(img_bytes)).convert("RGB")
            if st == "error":
                raise RuntimeError(f"Job {req_id} falló: {jdata}")
        raise TimeoutError(f"Timeout esperando job {req_id}")


def _pil_to_data_uri(path: str, thumb: int = 320) -> str:
    if not path or not os.path.exists(path):
        return ""
    im = Image.open(path).convert("RGB")
    im.thumbnail((thumb, thumb), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="WEBP", quality=86)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/webp;base64,{b64}"


def build_approval_html(records: List[Dict], out_html: str):
    """Genera tablero visual local para que el usuario apruebe o rechace las fotos 2D."""
    cards_html = []
    for rec in records:
        sku = rec["sku"]
        name = rec["name"]
        group = rec["group"]
        angle_rows = []
        for ang in rec["angles"]:
            real_b64 = _pil_to_data_uri(ang.get("real_preview"))
            ai_b64 = _pil_to_data_uri(ang.get("studio_web"))
            qa = ang.get("qa", {})
            de = qa.get("delta_e_palette", "-")
            iou = qa.get("silhouette_iou")
            iou_txt = f"IoU: {iou:.2f}" if iou is not None else "Ángulo sintetizado"
            badge_cls = "ok" if qa.get("passed", True) else "warn"
            src_tag = "Real HD + Estudio" if ang["has_real"] else f"IA ({ang['source_mode']})"
            angle_rows.append(
                f"""
                <div class="angle-card" data-sku="{sku}" data-angle="{ang['slug']}">
                  <div class="angle-head">
                    <strong>{ang['slug']}</strong>
                    <span class="badge {badge_cls}">ΔE {de} · {iou_txt}</span>
                  </div>
                  <div class="pair">
                    <div class="slot">
                      <span class="cap">Real HD ({'Base' if ang['has_real'] else 'Ref Lateral'})</span>
                      {'<img src="' + real_b64 + '">' if real_b64 else '<div class="empty">Sin foto real de este ángulo</div>'}
                    </div>
                    <div class="slot">
                      <span class="cap">{src_tag}</span>
                      <img src="{ai_b64}">
                    </div>
                  </div>
                  <div class="angle-actions">
                    <label><input type="checkbox" class="reject-angle" value="{ang['slug']}"> Rechazar ángulo</label>
                  </div>
                </div>"""
            )
        cards_html.append(
            f"""
            <section class="sku-block" id="sku-{sku}">
              <div class="sku-header">
                <div>
                  <h2>{sku} — {name}</h2>
                  <p>{group} · {len(rec['angles'])} vistas listas para 3D PBR</p>
                </div>
                <div class="sku-decision">
                  <button type="button" class="btn-approve is-selected" onclick="setSkuDecision('{sku}', true, this)">✅ Aprobar para 3D</button>
                  <button type="button" class="btn-reject" onclick="setSkuDecision('{sku}', false, this)">❌ Rechazar / Corregir</button>
                </div>
              </div>
              <div class="angles-grid">{''.join(angle_rows)}</div>
            </section>"""
        )

    skus_init = json.dumps({r["sku"]: True for r in records})
    html = f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Tablero de Aprobación 2D -> 3D PBR (Piloto)</title>
  <style>
    body {{ font-family: Inter, system-ui, sans-serif; background: #f4f1ea; color: #111; margin: 0; padding: 24px; }}
    .topbar {{ position: sticky; top: 0; z-index: 20; background: #111; color: #fff; padding: 16px 20px; border-radius: 12px; display: flex; justify-content: space-between; align-items: center; gap: 16px; margin-bottom: 24px; }}
    .topbar h1 {{ margin: 0; font-size: 18px; }}
    .topbar p {{ margin: 4px 0 0; font-size: 13px; color: #ccc; }}
    .btn-export {{ background: #c7ff16; color: #111; border: 0; font-weight: 800; padding: 10px 16px; border-radius: 8px; cursor: pointer; }}
    .sku-block {{ background: #fff; border: 1px solid #cbc8c0; border-radius: 14px; padding: 18px; margin-bottom: 24px; }}
    .sku-header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eceae4; padding-bottom: 12px; margin-bottom: 16px; flex-wrap: wrap; gap: 12px; }}
    .sku-header h2 {{ margin: 0; font-size: 18px; }}
    .sku-header p {{ margin: 4px 0 0; font-size: 13px; color: #555; }}
    .sku-decision button {{ padding: 8px 14px; border-radius: 8px; border: 1px solid #ccc; background: #f8f8f8; cursor: pointer; font-weight: 700; margin-left: 6px; }}
    .btn-approve.is-selected {{ background: #c7ff16; border-color: #111; }}
    .btn-reject.is-selected {{ background: #ff5b2b; color: #fff; border-color: #111; }}
    .angles-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 14px; }}
    .angle-card {{ border: 1px solid #e2dfd7; border-radius: 10px; padding: 10px; background: #faf9f6; }}
    .angle-head {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; font-size: 13px; }}
    .badge {{ padding: 2px 8px; border-radius: 999px; font-size: 11px; font-weight: 700; }}
    .badge.ok {{ background: #dcfce7; color: #166534; }}
    .badge.warn {{ background: #fef3c7; color: #92400e; }}
    .pair {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
    .slot {{ background: #fff; border: 1px solid #e5e5e5; border-radius: 8px; padding: 6px; text-align: center; }}
    .slot .cap {{ display: block; font-size: 11px; color: #666; margin-bottom: 4px; }}
    .slot img {{ width: 100%; height: 150px; object-fit: contain; background: #fff; }}
    .empty {{ height: 150px; display: flex; align-items: center; justify-content: center; font-size: 12px; color: #999; }}
    .angle-actions {{ margin-top: 8px; font-size: 12px; color: #444; }}
  </style>
</head>
<body>
  <div class="topbar">
    <div>
      <h1>Tablero de Aprobación 2D → 3D PBR</h1>
      <p>Revisa colores y logotipos frente a la foto real antes de reconstruir el .GLB ultradetallado.</p>
    </div>
    <button class="btn-export" onclick="exportSelection()">Descargar approved_skus.json</button>
  </div>
  {''.join(cards_html)}
  <script>
    const decisions = {skus_init};
    function setSkuDecision(sku, ok, btn) {{
      decisions[sku] = ok;
      const box = btn.parentElement;
      box.querySelectorAll('button').forEach(b => b.classList.remove('is-selected'));
      btn.classList.add('is-selected');
    }}
    function exportSelection() {{
      const rejectedAngles = {{}};
      document.querySelectorAll('.reject-angle:checked').forEach(cb => {{
        const card = cb.closest('.angle-card');
        const sku = card.dataset.sku;
        rejectedAngles[sku] = rejectedAngles[sku] || [];
        rejectedAngles[sku].push(cb.value);
      }});
      const payload = {{
        approved_skus: Object.keys(decisions).filter(k => decisions[k]),
        rejected_skus: Object.keys(decisions).filter(k => !decisions[k]),
        rejected_angles: rejectedAngles
      }};
      const blob = new Blob([JSON.stringify(payload, null, 2)], {{type: 'application/json'}});
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'approved_skus.json';
      a.click();
    }}
  </script>
</body>
</html>"""
    os.makedirs(os.path.dirname(out_html), exist_ok=True)
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(html)


def run_pilot_2d(skus: List[str], engine: str = "auto", size: int = 1024, include_3_4: bool = False):
    catalog = load_catalog_metadata()
    sku_map = {item["sku"]: item for item in catalog}
    missing = [s for s in skus if s not in sku_map]
    if missing:
        raise ValueError(f"SKUs no encontrados en catálogo: {missing}")

    client = None
    if engine != "local":
        client = DeApiEditClient(load_deapi_key())

    import rembg

    rembg_sess = rembg.new_session("u2net")

    # Ángulos requeridos para 3D PBR completo (6 ortogonales) + opcionales 3/4
    target_angles = [a for a in CANONICAL_STUDIO_SLUGS if include_3_4 or a[0] not in ("03_3-4_front", "04_3-4_rear")]
    approval_records = []

    for sku in skus:
        item = sku_map[sku]
        print(f"\n=== [{sku}] {item['name']} ({item['group']}) ===", flush=True)
        hd_sources = get_hd_source_map(item)
        print(f"  Fotos reales HD detectadas: {sorted(hd_sources.keys())}", flush=True)

        rgba_real_dir = os.path.join(PROJECT_DIR, "scratch", "pilot_work", "real_rgba", sku)
        rgba_studio_dir = os.path.join(PROJECT_DIR, "scratch", "pilot_work", "studio_rgba", sku)
        web_studio_dir = os.path.join(PROJECT_DIR, "scratch", "pilot_work", "studio_web", sku)
        real_preview_dir = os.path.join(PROJECT_DIR, "scratch", "pilot_work", "real_preview", sku)
        for d in (rgba_real_dir, rgba_studio_dir, web_studio_dir, real_preview_dir):
            os.makedirs(d, exist_ok=True)

        # 1. Extraer recortes RGBA limpios de las fotos reales HD
        real_rgba_map: Dict[str, Image.Image] = {}
        for slug, src_path in hd_sources.items():
            cache_p = os.path.join(rgba_real_dir, f"{slug}.png")
            if os.path.exists(cache_p):
                real_rgba_map[slug] = Image.open(cache_p).convert("RGBA")
            else:
                rgba = extract_clean_rgba(src_path, rembg_session=rembg_sess, use_rembg=True)
                rgba.save(cache_p)
                real_rgba_map[slug] = rgba
            prev_p = os.path.join(real_preview_dir, f"{slug}.webp")
            if not os.path.exists(prev_p):
                rgba_on_white(real_rgba_map[slug], size=512).save(prev_p, "WEBP", quality=88)

        anchor_ref = real_rgba_map.get("01_lateral") or next(iter(real_rgba_map.values()))
        sku_angles_record = []

        for slug, web_fn in target_angles:
            out_rgba_p = os.path.join(rgba_studio_dir, f"{slug}.png")
            out_web_p = os.path.join(web_studio_dir, web_fn)
            has_real = slug in real_rgba_map
            ref_for_angle = real_rgba_map.get(slug, anchor_ref)

            if os.path.exists(out_rgba_p) and os.path.exists(out_web_p):
                studio_rgba = Image.open(out_rgba_p).convert("RGBA")
                src_mode = "cached"
            elif engine == "local":
                if has_real:
                    studio_rgba = enhance_studio_lighting_local(real_rgba_map[slug])
                    src_mode = "local-hd-studio"
                else:
                    # Fallback limpio al catálogo existente si falta en fotos-HD, bloqueando color con lateral real
                    existing_p = os.path.join(PROJECT_DIR, "dist", "assets", "productos", sku, web_fn)
                    if os.path.exists(existing_p):
                        raw_ex = extract_clean_rgba(existing_p, rembg_session=rembg_sess, use_rembg=True)
                        # En suela (08_outsole) preservar luminosidad propia (0.0) para no manchar suelas blancas
                        s_l = 0.0 if slug == "08_outsole" else 0.35
                        s_ab = 0.65 if slug == "08_outsole" else 0.88
                        studio_rgba = lock_colors_lab(raw_ex, anchor_ref, strength_l=s_l, strength_ab=s_ab)
                        src_mode = "catalog-color-locked"
                    else:
                        print(f"  [!] Sin fuente local para {slug}, omitido.")
                        continue
            else:
                # Pipeline con deAPI
                if has_real:
                    model_slug = "Flux_2_Klein_4B_BF16" if engine == "deapi-klein" else "QwenImageEdit_Plus_NF4"
                    refs_in = [rgba_on_white(real_rgba_map[slug], size=1024)]
                else:
                    model_slug = "QwenImageEdit_Plus_NF4" if engine == "deapi-qwen" else "Flux_2_Klein_4B_BF16"
                    refs_list = [
                        real_rgba_map.get("01_lateral"),
                        real_rgba_map.get("05_front"),
                        real_rgba_map.get("06_rear"),
                    ]
                    refs_in = [rgba_on_white(r, size=1024) for r in refs_list if r is not None] or [rgba_on_white(anchor_ref, 1024)]

                edited_rgb = client.edit(
                    prompt=ANGLE_PROMPTS[slug],
                    ref_images=refs_in,
                    model=model_slug,
                    width=1024,
                    height=1024,
                    seed=42,
                )
                edited_rgba = extract_clean_rgba(edited_rgb, rembg_session=rembg_sess, use_rembg=True)
                studio_rgba = lock_colors_lab(edited_rgba, ref_for_angle, strength_l=0.55, strength_ab=0.92)
                src_mode = model_slug

            qa = evaluate_fidelity(studio_rgba, ref_for_angle, same_angle=has_real)
            # Guardia automática: si la IA deformó la silueta de una foto real existente (IoU < 0.78),
            # revertir a la silueta real mejorada localmente para no corromper el 3D.
            if has_real and qa["silhouette_iou"] is not None and qa["silhouette_iou"] < 0.78 and engine != "local":
                print(f"  [guardia] {slug} IoU={qa['silhouette_iou']} bajo -> usando real HD mejorada.", flush=True)
                studio_rgba = enhance_studio_lighting_local(real_rgba_map[slug])
                qa = evaluate_fidelity(studio_rgba, ref_for_angle, same_angle=True)
                src_mode += "+fallback-real"

            studio_rgba.save(out_rgba_p)
            web_img = standardize_studio_angle(studio_rgba, slug, size=size)
            web_img.save(out_web_p, "WEBP", quality=92, method=6)
            print(f"  [{slug}] listo ({src_mode}) -> ΔE={qa['delta_e_palette']}, IoU={qa['silhouette_iou']}", flush=True)

            real_prev = os.path.join(real_preview_dir, f"{slug}.webp")
            if not os.path.exists(real_prev):
                real_prev = os.path.join(real_preview_dir, "01_lateral.webp")

            sku_angles_record.append(
                {
                    "slug": slug,
                    "has_real": has_real,
                    "source_mode": src_mode,
                    "studio_rgba": out_rgba_p,
                    "studio_web": out_web_p,
                    "real_preview": real_prev,
                    "qa": qa,
                }
            )

        approval_records.append(
            {
                "sku": sku,
                "name": item["name"],
                "group": item["group"],
                "angles": sku_angles_record,
            }
        )

    out_html = os.path.join(PROJECT_DIR, "scratch", "pilot_approval", "preview_aprobacion.html")
    build_approval_html(approval_records, out_html)
    meta_json = os.path.join(PROJECT_DIR, "scratch", "pilot_approval", "pilot_2d_manifest.json")
    with open(meta_json, "w", encoding="utf-8") as f:
        json.dump(approval_records, f, indent=2, ensure_ascii=False)
    print(f"\nTablero de aprobación generado en: {out_html}", flush=True)


def main():
    parser = argparse.ArgumentParser(description="Pipeline 2D con candado de color y tablero de aprobación.")
    parser.add_argument("--skus", nargs="+", default=DEFAULT_PILOT_SKUS, help="Lista de SKUs del piloto.")
    parser.add_argument(
        "--engine",
        choices=["auto", "deapi-qwen", "deapi-klein", "local"],
        default="auto",
        help="Motor 2D: auto (deAPI Qwen+Klein), deapi-qwen, deapi-klein o local.",
    )
    parser.add_argument("--size", type=int, default=1024, help="Tamaño WebP de catálogo (default 1024).")
    parser.add_argument("--include-3-4", action="store_true", help="Incluir también vistas 3/4 en el lote.")
    args = parser.parse_args()

    try:
        run_pilot_2d(skus=args.skus, engine=args.engine, size=args.size, include_3_4=args.include_3_4)
    except DeApiBalanceError as exc:
        print(f"\n[BLOQUEO DE SALDO DEAPI] {exc}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
