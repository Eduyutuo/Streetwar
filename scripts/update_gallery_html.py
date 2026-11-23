import json, re

with open('dist/js/flow_nanobanana_data.js', 'r', encoding='utf-8') as f:
    data = json.loads(re.search(r'const flowNanobananaData = ({.*?});\s*$', f.read(), re.DOTALL).group(1))

catalog = data['catalog']
models_js = []
for item in catalog:
    models_js.append({
        'sku': item['sku'],
        'group': item['group'].replace(' ', '_'),
        'groupLabel': item['group'],
        'name': item['name'],
        'colorway': item.get('colorway', ''),
        'origin': item.get('folderOrigin', item['sku'])
    })

models_json_str = json.dumps(models_js, indent=2, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visor de Resultados — 8 Tomas Normalizadas (Catálogo Completo 45 Modelos)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #090d16;
      --card-bg: #111827;
      --border: #1f293d;
      --accent: #38bdf8;
      --accent-green: #10b981;
      --accent-purple: #a855f7;
      --text: #f3f4f6;
      --text-muted: #9ca3af;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: 'Plus Jakarta Sans', sans-serif;
      padding: 24px;
      min-height: 100vh;
    }}
    .container {{
      max-width: 1540px;
      margin: 0 auto;
    }}
    header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      padding-bottom: 20px;
      border-bottom: 1px solid var(--border);
      margin-bottom: 20px;
    }}
    h1 {{
      font-size: 22px;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .badge {{
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-green);
      border: 1px solid rgba(16, 185, 129, 0.3);
      font-size: 13px;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 20px;
    }}
    
    /* Filtro de Grupos */
    .filter-tabs {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 10px;
      margin-bottom: 14px;
    }}
    .tab-btn {{
      background: #111827;
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}
    .tab-btn:hover {{ background: #1e293b; color: #fff; }}
    .tab-btn.active {{
      background: var(--accent);
      color: #090d16;
      border-color: var(--accent);
    }}
    
    /* Selector de Modelos */
    .selector-bar {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 14px;
      margin-bottom: 20px;
    }}
    .model-btn {{
      background: #111827;
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .model-btn:hover {{
      background: #172033;
      color: #fff;
    }}
    .model-btn.active {{
      background: var(--accent);
      color: #090d16;
      border-color: var(--accent);
      font-weight: 800;
    }}

    /* Card info del modelo activo */
    .model-info-banner {{
      background: #131c2e;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px 20px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}
    .model-info-left h2 {{
      font-size: 18px;
      font-weight: 800;
      color: #fff;
    }}
    .model-info-left p {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 4px;
    }}
    .model-info-tags {{
      display: flex;
      gap: 10px;
    }}
    .model-tag {{
      background: #0f172a;
      border: 1px solid var(--border);
      font-size: 12px;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: 6px;
      color: var(--accent);
    }}

    /* Grid de 8 tomas */
    .angles-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
    }}
    @media (max-width: 1200px) {{
      .angles-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 640px) {{
      .angles-grid {{ grid-template-columns: 1fr; }}
    }}

    .angle-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: transform 0.15s ease, border-color 0.15s ease;
    }}
    .angle-card:hover {{
      transform: translateY(-2px);
      border-color: var(--accent);
    }}
    .angle-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
    }}
    .angle-tag {{
      background: #1e293b;
      color: var(--accent);
      padding: 2px 8px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
    }}
    .img-box {{
      width: 100%;
      aspect-ratio: 1 / 1;
      background: #ffffff;
      border-radius: 8px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      position: relative;
    }}
    .img-box img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      transition: transform 0.2s ease;
    }}
    .img-box:hover img {{
      transform: scale(1.04);
    }}
    .angle-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-muted);
    }}

    /* Modal */
    .modal {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 100;
      padding: 20px;
    }}
    .modal.show {{
      display: flex;
    }}
    .modal-content {{
      background: #111827;
      border: 1px solid var(--border);
      border-radius: 14px;
      max-width: 900px;
      width: 100%;
      overflow: hidden;
      box-shadow: 0 25px 50px -12px rgba(0,0,0,0.7);
    }}
    .modal-content img {{
      width: 100%;
      aspect-ratio: 1 / 1;
      object-fit: contain;
      background: #ffffff;
      display: block;
    }}
    .modal-footer {{
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 14px;
      font-weight: 600;
    }}
    .btn-close {{
      background: #374151;
      color: #fff;
      border: none;
      padding: 8px 16px;
      border-radius: 6px;
      font-weight: 700;
      cursor: pointer;
    }}
    .btn-close:hover {{
      background: #4b5563;
    }}
  </style>
</head>
<body>

<div class="container">
  <header>
    <div>
      <h1>👟 Galería de Tomas Normalizadas (Catálogo Completo 45 Modelos)</h1>
      <p style="color:var(--text-muted); font-size:13px; margin-top:4px;">
        8 Tomas canónicas (<code>01 | LATERAL</code> a <code>08 | OUTSOLE</code>) a <strong>1024×1024 px</strong> sobre fondo blanco puro <strong>#FFFFFF</strong>, auto-centradas con fill-ratio 82%.
      </p>
    </div>
    <div class="badge" id="catalog-count-badge">✅ 45 Modelos Normalizados (360 Tomas)</div>
  </header>

  <!-- Filtro por Grupos A-G -->
  <div class="filter-tabs" id="group-tabs">
    <!-- Renderizado dinámicamente -->
  </div>

  <!-- Selector de Modelos con scroll horizontal -->
  <div class="selector-bar" id="model-bar">
    <!-- Renderizado dinámicamente -->
  </div>

  <!-- Banner con datos del modelo actual -->
  <div class="model-info-banner" id="model-banner">
    <!-- Renderizado dinámicamente -->
  </div>

  <!-- Cuadrícula 4x2 de las 8 tomas -->
  <div class="angles-grid" id="angles-grid">
    <!-- Renderizado dinámicamente -->
  </div>
</div>

<!-- Modal para inspeccionar en alta resolución -->
<div class="modal" id="modal" onclick="closeModal()">
  <div class="modal-content" onclick="event.stopPropagation()">
    <img id="modal-img" src="" alt="Zoom">
    <div class="modal-footer">
      <span id="modal-title">Detalle del Ángulo</span>
      <div style="display:flex; gap:10px;">
        <a id="modal-download" href="" target="_blank" class="btn-close" style="text-decoration:none; display:inline-block;">Abrir Original</a>
        <button class="btn-close" onclick="closeModal()">Cerrar</button>
      </div>
    </div>
  </div>
</div>

<script>
  const allModels = {models_json_str};

  const groups = ['TODOS', 'Grupo A', 'Grupo B', 'Grupo C', 'Grupo D', 'Grupo E', 'Grupo F', 'Grupo G'];
  let currentGroup = 'TODOS';
  let currentSku = allModels[0].sku;

  const panelDefs = [
    {{ code: '01_lateral', label: '01 | LATERAL', desc: 'Perfil Lateral Exterior (Puntera Izquierda)' }},
    {{ code: '02_medial', label: '02 | MEDIAL', desc: 'Perfil Medial Interior (Puntera Derecha)' }},
    {{ code: '03_3-4_front', label: '03 | 3/4 FRONT', desc: 'Perspectiva 3/4 Frontal (Punta Abajo-Izq)' }},
    {{ code: '04_3-4_rear', label: '04 | 3/4 REAR', desc: 'Perspectiva 3/4 Trasera (Talón Izq, Punta Der)' }},
    {{ code: '05_front', label: '05 | FRONT', desc: 'Vista Frontal Directa' }},
    {{ code: '06_rear', label: '06 | REAR', desc: 'Vista Posterior Talón' }},
    {{ code: '07_top_down', label: '07 | TOP-DOWN', desc: 'Vista Cenital Superior (Horizontal)' }},
    {{ code: '08_outsole', label: '08 | OUTSOLE', desc: 'Vista Suela Inferior (Horizontal)' }}
  ];

  function renderGroupTabs() {{
    const tabs = document.getElementById('group-tabs');
    tabs.innerHTML = '';
    groups.forEach(g => {{
      const btn = document.createElement('button');
      btn.className = `tab-btn ${{g === currentGroup ? 'active' : ''}}`;
      const count = g === 'TODOS' ? allModels.length : allModels.filter(m => m.groupLabel === g).length;
      btn.textContent = `${{g}} (${{count}})`;
      btn.onclick = () => {{
        currentGroup = g;
        const visible = getVisibleModels();
        if (visible.length && !visible.find(m => m.sku === currentSku)) {{
          currentSku = visible[0].sku;
        }}
        renderGroupTabs();
        renderBar();
        renderAngles();
      }};
      tabs.appendChild(btn);
    }});
  }}

  function getVisibleModels() {{
    if (currentGroup === 'TODOS') return allModels;
    return allModels.filter(m => m.groupLabel === currentGroup);
  }}

  function renderBar() {{
    const bar = document.getElementById('model-bar');
    bar.innerHTML = '';
    const visible = getVisibleModels();

    visible.forEach(m => {{
      const btn = document.createElement('button');
      btn.className = `model-btn ${{m.sku === currentSku ? 'active' : ''}}`;
      const shortName = m.name.length > 28 ? m.name.substring(0, 26) + '...' : m.name;
      btn.innerHTML = `<span>👟</span> <strong>${{m.sku}}</strong> &bull; ${{shortName}}`;
      btn.onclick = () => {{
        currentSku = m.sku;
        renderBar();
        renderAngles();
      }};
      bar.appendChild(btn);
    }});
  }}

  function renderAngles() {{
    const m = allModels.find(x => x.sku === currentSku) || allModels[0];
    
    // Update banner
    const banner = document.getElementById('model-banner');
    banner.innerHTML = `
      <div class="model-info-left">
        <h2>${{m.sku}} &bull; ${{m.name}}</h2>
        <p>${{m.groupLabel}} &bull; Colorway: ${{m.colorway || 'Original'}} &bull; Origen: <code>${{m.origin}}</code></p>
      </div>
      <div class="model-info-tags">
        <span class="model-tag">${{m.groupLabel}}</span>
        <span class="model-tag">1024×1024 px 1K</span>
        <span class="model-tag">WebP / PNG</span>
      </div>
    `;

    const grid = document.getElementById('angles-grid');
    grid.innerHTML = '';

    panelDefs.forEach(p => {{
      const imgPath = `../output_catalog/${{m.group}}/${{m.sku}}/${{m.sku}}_${{p.code}}.webp`;
      const fallbackPng = `../output_catalog/${{m.group}}/${{m.sku}}/${{m.sku}}_${{p.code}}.png`;
      const card = document.createElement('div');
      card.className = 'angle-card';
      card.innerHTML = `
        <div class="angle-header">
          <span>${{p.desc}}</span>
          <span class="angle-tag">${{p.label}}</span>
        </div>
        <div class="img-box" onclick="openModal('${{imgPath}}', '${{m.sku}} - ${{p.label}}')" title="Clic para ampliar">
          <img src="${{imgPath}}" alt="${{p.label}}" onerror="this.src='${{fallbackPng}}'">
        </div>
        <div class="angle-meta">
          <span>1024×1024 px</span>
          <span style="color:var(--accent-green);">#FFFFFF Puro</span>
        </div>
      `;
      grid.appendChild(card);
    }});
  }}

  function openModal(src, title) {{
    document.getElementById('modal-img').src = src;
    document.getElementById('modal-download').href = src;
    document.getElementById('modal-title').textContent = title;
    document.getElementById('modal').classList.add('show');
  }}

  function closeModal() {{
    document.getElementById('modal').classList.remove('show');
  }}

  renderGroupTabs();
  renderBar();
  renderAngles();
</script>
</body>
</html>
'''

with open('dist/resultados_cortes.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Updated dist/resultados_cortes.html with all 45 models and group filters!")
