// ============================================================================
// STREETWAR 3D & 360° INTERACTIVO
// ============================================================================
// Método 1 (Visor 360° Turntable por ángulos + Tilt + Zoom): todos los modelos del catálogo
// Método 2 (3D Real .GLB Multi-Vista): id 0 (IX6180-100) y id 14 (IW2872-700)
// ============================================================================

window.STREETWAR_3D_DEMO = {
  method2_glb: {
    0:  { label: 'MÉTODO 2 · 3D REAL (.GLB)', sku: 'IX6180-100', model: 'assets/models/IX6180-100.glb' },
    14: { label: 'MÉTODO 2 · 3D REAL (.GLB)', sku: 'IW2872-700', model: 'assets/models/IW2872-700.glb' }
  },

  isSpinEnabled(pIndex) {
    return !this.method2_glb[pIndex];
  },

  getSortRank(pIndex) {
    const order = [0, 14];
    const pos = order.indexOf(Number(pIndex));
    return pos === -1 ? 999 : pos;
  },

  getCardBadge(pIndex) {
    if (this.method2_glb[pIndex]) {
      return '<span class="badge-3d-demo badge-3d-glb">3D GLB</span>';
    }
    return '<span class="badge-3d-demo badge-3d-360">360°</span>';
  },

  initTiltCards() {
    // Método 3 desactivado: se usan únicamente Método 1 (360° catálogo) y Método 2 (.GLB en 2 modelos)
  },

  // ── MÉTODO 2: Visor 3D Real (.GLB) con <model-viewer> ──
  ensureModelViewerScript() {
    if (document.querySelector('script[data-model-viewer-lib]')) return;
    const s = document.createElement('script');
    s.type = 'module';
    s.src = 'https://ajax.googleapis.com/ajax/libs/model-viewer/3.5.0/model-viewer.min.js';
    s.dataset.modelViewerLib = '1';
    s.onerror = () => {
      const fallback = document.createElement('script');
      fallback.type = 'module';
      fallback.src = 'https://cdn.jsdelivr.net/npm/@google/model-viewer@3.5.0/dist/model-viewer.min.js';
      document.head.appendChild(fallback);
    };
    document.head.appendChild(s);
  },

  loadGlbUrlForProtocol(sku, modelPath) {
    if (location.protocol !== 'file:') {
      return Promise.resolve(`${modelPath}?v=20261126-hy3d`);
    }
    return new Promise((resolve, reject) => {
      const makeBlobUrl = b64 => {
        const bin = atob(b64);
        const bytes = new Uint8Array(bin.length);
        for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
        return URL.createObjectURL(new Blob([bytes], { type: 'model/gltf-binary' }));
      };
      if (window.__GLB_B64 && window.__GLB_B64[sku]) {
        resolve(makeBlobUrl(window.__GLB_B64[sku]));
        return;
      }
      const sc = document.createElement('script');
      sc.src = `${modelPath}.js?v=20261126-hy3d`;
      sc.onload = () => {
        if (window.__GLB_B64 && window.__GLB_B64[sku]) {
          resolve(makeBlobUrl(window.__GLB_B64[sku]));
        } else {
          reject(new Error('No GLB data'));
        }
      };
      sc.onerror = () => reject(new Error('Failed loading GLB script'));
      document.head.appendChild(sc);
    });
  },

  mountDetailExperience(detailRoot, id, product, gallery) {
    const isGlb = Boolean(this.method2_glb[id]);
    const hasMultiView = Array.isArray(gallery) && gallery.length > 1;
    if (!isGlb && !hasMultiView) return;

    const mainBox = detailRoot.querySelector('.detail-main');
    const galleryBox = detailRoot.querySelector('.detail-gallery');
    if (!mainBox || !galleryBox) return;
    mainBox.classList.add('has-3d-demo');

    // Preserve original photo HTML inside a wrapper so user can toggle back and forth
    const photoWrap = document.createElement('div');
    photoWrap.className = 'detail-photo-fallback';
    photoWrap.style.width = '100%';
    photoWrap.style.height = '100%';
    photoWrap.style.position = 'relative';
    photoWrap.style.display = 'none';
    while (mainBox.firstChild) {
      photoWrap.appendChild(mainBox.firstChild);
    }

    const modeBar = document.createElement('div');
    modeBar.className = 'detail-mode-bar';
    const pillLabel = isGlb ? this.method2_glb[id].label : 'MÉTODO 1 · 360° FOTOS';

    modeBar.innerHTML = `
      <span class="detail-mode-pill ${isGlb ? 'is-glb' : ''}">${pillLabel}</span>
      <div class="detail-mode-tabs" role="tablist">
        ${isGlb ? `<button type="button" class="active" data-view-mode="glb">🧊 3D Real (.GLB)</button>` : ''}
        ${hasMultiView ? `<button type="button" class="${isGlb ? '' : 'active'}" data-view-mode="spin">🔄 360°</button>` : ''}
        <button type="button" data-view-mode="photos">📷 Fotos (${gallery.length})</button>
      </div>
    `;

    const glbContainer = document.createElement('div');
    glbContainer.className = 'detail-interactive-stage-wrap';
    glbContainer.style.width = '100%';
    glbContainer.style.display = isGlb ? 'block' : 'none';

    const spinContainer = document.createElement('div');
    spinContainer.className = 'detail-interactive-stage-wrap';
    spinContainer.style.width = '100%';
    spinContainer.style.display = isGlb ? 'none' : 'block';

    mainBox.appendChild(modeBar);
    if (isGlb) mainBox.appendChild(glbContainer);
    if (hasMultiView) mainBox.appendChild(spinContainer);
    mainBox.appendChild(photoWrap);

    if (isGlb) {
      const meta = this.method2_glb[id];
      this.ensureModelViewerScript();
      glbContainer.innerHTML = `
        <div class="detail-glb-stage">
          <span class="glb-status" data-glb-status>Cargando modelo 3D...</span>
          <model-viewer
            id="streetwar-model-viewer"
            alt="Modelo 3D interactivo de ${product.name}"
            poster="assets/${gallery[0]}?v=20261125-output-catalog"
            camera-controls
            touch-action="none"
            auto-rotate
            auto-rotate-delay="200"
            rotation-per-second="30deg"
            shadow-intensity="0.95"
            shadow-softness="0.8"
            exposure="1.0"
            interaction-prompt="auto"
            camera-orbit="35deg 75deg 110%"
            min-camera-orbit="auto auto 65%"
            max-camera-orbit="auto auto 170%">
          </model-viewer>
          <div class="glb-toolbar">
            <span class="glb-hint">Arrastra para rotar 360° · Rueda para zoom</span>
            <div class="glb-actions">
              <button type="button" class="glb-btn active" data-glb-autorotate>↻ Auto-giro</button>
              <button type="button" class="glb-btn" data-glb-reset>⌖ Centrar</button>
            </div>
          </div>
        </div>
      `;

      const mv = glbContainer.querySelector('model-viewer');
      const statusEl = glbContainer.querySelector('[data-glb-status]');
      const btnAuto = glbContainer.querySelector('[data-glb-autorotate]');
      const btnReset = glbContainer.querySelector('[data-glb-reset]');

      mv?.addEventListener('load', () => {
        statusEl?.classList.add('is-hidden');
      });
      mv?.addEventListener('error', () => {
        if (statusEl) {
          statusEl.textContent = 'No se pudo cargar el modelo .GLB';
          statusEl.classList.remove('is-hidden');
        }
      });

      this.loadGlbUrlForProtocol(meta.sku, meta.model)
        .then(url => {
          if (mv) mv.src = url;
        })
        .catch(() => {
          if (statusEl) {
            statusEl.textContent = 'Abre el sitio con servidor local o GitHub Pages para ver el .GLB';
          }
        });

      btnAuto?.addEventListener('click', () => {
        if (!mv) return;
        const on = mv.hasAttribute('auto-rotate');
        if (on) {
          mv.removeAttribute('auto-rotate');
          btnAuto.classList.remove('active');
        } else {
          mv.setAttribute('auto-rotate', '');
          btnAuto.classList.add('active');
        }
      });
      btnReset?.addEventListener('click', () => {
        if (!mv) return;
        mv.cameraOrbit = '35deg 75deg 110%';
        mv.fieldOfView = 'auto';
      });
    }

    if (hasMultiView) {
      this._mountSpin360(spinContainer, product, gallery);
    }

    const tabs = modeBar.querySelectorAll('[data-view-mode]');
    const setMode = mode => {
      tabs.forEach(t => t.classList.toggle('active', t.dataset.viewMode === mode));
      glbContainer.style.display = mode === 'glb' ? 'block' : 'none';
      spinContainer.style.display = mode === 'spin' ? 'block' : 'none';
      photoWrap.style.display = mode === 'photos' ? 'block' : 'none';
    };
    tabs.forEach(t => t.addEventListener('click', () => setMode(t.dataset.viewMode)));

    detailRoot.querySelectorAll('[data-gallery-index]').forEach(btn => {
      btn.addEventListener('click', () => {
        setMode('photos');
      });
    });
  },

  // ── MÉTODO 1: Visor Interactivo 360° Turntable por ángulos + Tilt + Zoom ──
  _mountSpin360(container, product, gallery) {
    const orbitOrder = [
      { key: '01-lateral', label: 'Lateral (0°)' },
      { key: '03-3-4-front', label: '3/4 Frontal (45°)' },
      { key: '05-front', label: 'Frontal (90°)' },
      { key: '02-medial', label: 'Medial (180°)' },
      { key: '04-3-4-rear', label: '3/4 Trasera (225°)' },
      { key: '06-rear', label: 'Talón / Trasera (270°)' }
    ];
    const orbitSlides = [];
    orbitOrder.forEach(slot => {
      const match = gallery.find(p => p.includes(slot.key));
      if (match) orbitSlides.push({ src: `assets/${match}?v=20261125-output-catalog`, label: slot.label });
    });
    if (!orbitSlides.length) {
      gallery.forEach((p, idx) => orbitSlides.push({ src: `assets/${p}?v=20261125-output-catalog`, label: `Ángulo ${idx + 1}` }));
    }

    const topSlide = gallery.find(p => p.includes('07-top-down'));
    const botSlide = gallery.find(p => p.includes('08-outsole'));

    const allSlides = [...orbitSlides];
    const topIdx = topSlide ? (allSlides.push({ src: `assets/${topSlide}?v=20261125-output-catalog`, label: 'Vista Superior' }) - 1) : -1;
    const botIdx = botSlide ? (allSlides.push({ src: `assets/${botSlide}?v=20261125-output-catalog`, label: 'Vista Suela' }) - 1) : -1;

    container.innerHTML = `
      <div class="detail-spin360-stage">
        <div class="spin360-vertical-strip">
          ${topIdx >= 0 ? `<button type="button" class="glb-btn" data-spin-jump="${topIdx}">⬆ Arriba</button>` : ''}
          <button type="button" class="glb-btn active" data-spin-jump="0">↔ 360°</button>
          ${botIdx >= 0 ? `<button type="button" class="glb-btn" data-spin-jump="${botIdx}">⬇ Suela</button>` : ''}
        </div>
        <div class="spin360-card">
          ${allSlides.map((s, i) => `<img src="${s.src}" alt="${product.name} - ${s.label}" class="${i === 0 ? 'active' : ''}">`).join('')}
        </div>
        <div class="spin360-hud">
          <span class="spin360-angle-label">${allSlides[0].label} · Arrastra ↔</span>
          <div class="spin360-controls">
            <button type="button" class="glb-btn" data-spin-auto>▶ Auto 360°</button>
            <button type="button" class="glb-btn" data-spin-zoom>🔍 Zoom</button>
          </div>
        </div>
      </div>
    `;

    const stage = container.querySelector('.detail-spin360-stage');
    const card = container.querySelector('.spin360-card');
    const imgs = Array.from(card.querySelectorAll('img'));
    const labelEl = container.querySelector('.spin360-angle-label');
    const btnAuto = container.querySelector('[data-spin-auto]');
    const btnZoom = container.querySelector('[data-spin-zoom]');
    const jumpBtns = Array.from(container.querySelectorAll('[data-spin-jump]'));

    let orbitIdx = 0;
    let activeIdx = 0;
    let zoomScale = 1;
    let autoTimer = null;
    let dragging = false;
    let startX = 0;
    let startY = 0;
    let accumX = 0;

    const showSlide = idx => {
      activeIdx = idx;
      imgs.forEach((im, i) => im.classList.toggle('active', i === idx));
      labelEl.textContent = `${allSlides[idx].label} · Arrastra ↔`;
      jumpBtns.forEach(b => {
        const j = Number(b.dataset.spinJump);
        const isOrbitBtn = j === 0 && idx < orbitSlides.length;
        b.classList.toggle('active', j === idx || isOrbitBtn);
      });
    };

    const stepOrbit = delta => {
      orbitIdx = (orbitIdx + delta + orbitSlides.length) % orbitSlides.length;
      showSlide(orbitIdx);
    };

    const stopAuto = () => {
      if (autoTimer) {
        clearInterval(autoTimer);
        autoTimer = null;
        btnAuto.classList.remove('active');
        btnAuto.textContent = '▶ Auto 360°';
      }
    };

    btnAuto.addEventListener('click', () => {
      if (autoTimer) {
        stopAuto();
      } else {
        btnAuto.classList.add('active');
        btnAuto.textContent = '⏸ Pausar';
        autoTimer = setInterval(() => stepOrbit(1), 650);
      }
    });

    btnZoom.addEventListener('click', () => {
      zoomScale = zoomScale === 1 ? 1.55 : 1;
      btnZoom.classList.toggle('active', zoomScale > 1);
      card.style.transform = `scale(${zoomScale})`;
    });

    jumpBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        stopAuto();
        const j = Number(btn.dataset.spinJump);
        if (j < orbitSlides.length) orbitIdx = j;
        showSlide(j);
      });
    });

    stage.addEventListener('pointerdown', e => {
      if (e.target.closest('button')) return;
      stopAuto();
      dragging = true;
      startX = e.clientX;
      startY = e.clientY;
      accumX = 0;
      stage.classList.add('is-dragging');
      stage.setPointerCapture(e.pointerId);
    });

    stage.addEventListener('pointermove', e => {
      const rect = stage.getBoundingClientRect();
      const nx = (e.clientX - rect.left) / rect.width - 0.5;
      const ny = (e.clientY - rect.top) / rect.height - 0.5;
      const rY = nx * 14;
      const rX = -ny * 10;
      card.style.transform = `scale(${zoomScale}) rotateX(${rX.toFixed(1)}deg) rotateY(${rY.toFixed(1)}deg)`;

      if (!dragging) return;
      const dx = e.clientX - startX;
      const dy = e.clientY - startY;
      accumX += dx;
      startX = e.clientX;

      if (Math.abs(accumX) >= 42) {
        stepOrbit(accumX > 0 ? 1 : -1);
        accumX = 0;
      } else if (dy < -70 && topIdx >= 0 && activeIdx !== topIdx) {
        showSlide(topIdx);
      } else if (dy > 70 && botIdx >= 0 && activeIdx !== botIdx) {
        showSlide(botIdx);
      }
    });

    const endDrag = () => {
      dragging = false;
      stage.classList.remove('is-dragging');
      card.style.transform = `scale(${zoomScale})`;
    };
    stage.addEventListener('pointerup', endDrag);
    stage.addEventListener('pointercancel', endDrag);
    stage.addEventListener('pointerleave', () => {
      if (!dragging) card.style.transform = `scale(${zoomScale})`;
    });
  }
};
