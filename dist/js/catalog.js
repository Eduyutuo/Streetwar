const pages=[
  ['novedades.html','novedades'],
  ['hombre.html','hombre'],
  ['mujer.html','mujer'],
  ['ninos.html','ninos'],
  ['marcas.html','marcas'],
  ['ofertas.html','ofertas'],
  ['lanzamientos.html','lanzamientos'],
  ['editorial.html','editorial'],
  ['tiendas.html','tiendas']
];

const current=location.pathname.split('/').pop()||'index.html';
const searchQuery=(new URLSearchParams(location.search).get('q')||'').replace(/[&<>"]/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[char]));

function renderHeaderAndFooter(){
  const t = (window.RITMO_I18N && window.RITMO_I18N.getT()) || {
    promoBar: 'CATÁLOGO DE ZAPATILLAS ACTUALIZADO ✦ JORDAN Y NIKE',
    searchPlaceholder: 'BUSCAR EN EL CATÁLOGO',
    nav: { novedades: 'NOVEDADES', hombre: 'HOMBRE', mujer: 'MUJER', ninos: 'NIÑOS', marcas: 'MARCAS', ofertas: 'OFERTAS', lanzamientos: 'LANZAMIENTOS', editorial: 'EDITORIAL', tiendas: '⌖ TIENDAS' },
    footer: { store: 'TIENDA', help: 'AYUDA', shipping: 'Envíos y devoluciones', contact: 'Contacto', stores: 'Tiendas', copy: '© 2026 LIL DAVID / RITMO — DEMO CONCEPT' },
    catalog: { toast: 'AÑADIDO A TU LISTA ✓' }
  };
  const currentLang = (window.RITMO_I18N && window.RITMO_I18N.getLang()) || 'es';

  const siteHeader = document.querySelector('#site-header');
  if(siteHeader){
    siteHeader.innerHTML=`
      <div class="promo">${t.promoBar}</div>
      <header class="shop-head">
        <div class="head-row">
          <a class="logo" href="index.html" aria-label="Lil David, inicio"><img src="assets/LOGO.svg" alt="Lil David"></a>
          <div class="head-right-group">
            <div class="lang-toggle-wrap header-lang" role="group" aria-label="Idioma / Language">
              <button type="button" class="lang-btn ${currentLang==='es'?'active':''}" data-lang-btn="es" title="Español" aria-label="Español">
                <img src="assets/idioma/ES.webp" alt="ES" class="lang-flag">
                <span class="lang-code">ES</span>
              </button>
              <button type="button" class="lang-btn ${currentLang==='en'?'active':''}" data-lang-btn="en" title="English" aria-label="English">
                <img src="assets/idioma/EN.webp" alt="EN" class="lang-flag">
                <span class="lang-code">EN</span>
              </button>
            </div>
            <form class="head-search" role="search" action="novedades.html">
              <label class="sr-only" for="catalog-search">${t.searchPlaceholder}</label>
              <input id="catalog-search" name="q" type="search" autocomplete="off" placeholder="${t.searchPlaceholder}" value="${searchQuery}">
              <button type="submit" aria-label="Buscar">⌕</button>
            </form>
          </div>
        </div>
        <nav class="shop-nav">
          <div class="shop-nav-links">
            ${pages.map(([u,key])=>`<a href="${u}" class="${current===u?'active':''}">${t.nav[key]||key.toUpperCase()}</a>`).join('')}
          </div>
          <div class="lang-toggle-wrap nav-lang" role="group" aria-label="Idioma / Language">
            <button type="button" class="lang-btn ${currentLang==='es'?'active':''}" data-lang-btn="es" title="Español" aria-label="Español">
              <img src="assets/idioma/ES.webp" alt="ES" class="lang-flag">
              <span class="lang-code">ES</span>
            </button>
            <button type="button" class="lang-btn ${currentLang==='en'?'active':''}" data-lang-btn="en" title="English" aria-label="English">
              <img src="assets/idioma/EN.webp" alt="EN" class="lang-flag">
              <span class="lang-code">EN</span>
            </button>
          </div>
        </nav>
      </header>`;
  }

  const siteFooter = document.querySelector('#site-footer');
  if(siteFooter){
    siteFooter.innerHTML=`
      <footer class="footer">
        <a class="footer-logo" href="index.html" aria-label="Lil David, inicio"><img src="assets/LOGO.svg" alt="Lil David"></a>
        <div>
          <h3>${t.footer.store}</h3>
          <a href="novedades.html">${t.nav.novedades}</a>
          <a href="hombre.html">${t.nav.hombre}</a>
          <a href="mujer.html">${t.nav.mujer}</a>
          <a href="ninos.html">${t.nav.ninos}</a>
        </div>
        <div>
          <h3>${t.footer.help}</h3>
          <a href="tiendas.html">${t.footer.stores}</a>
          <a href="#">${t.footer.shipping}</a>
          <a href="#">${t.footer.contact}</a>
        </div>
        <small>${t.footer.copy}</small>
      </footer>
      <div class="toast">${t.catalog.toast}</div>`;
  }

  // Attach language toggle listeners
  document.querySelectorAll('[data-lang-btn]').forEach(btn => {
    btn.addEventListener('click', () => {
      const targetLang = btn.dataset.langBtn;
      if (window.RITMO_I18N) {
        window.RITMO_I18N.setLanguage(targetLang);
      }
    });
  });
}

// Initial render
renderHeaderAndFooter();

// Re-render when language changes
window.addEventListener('languagechange', () => {
  renderHeaderAndFooter();
});

document.querySelectorAll('.heart').forEach(btn=>btn.addEventListener('click',()=>{const t=document.querySelector('.toast');t.classList.add('show');setTimeout(()=>t.classList.remove('show'),1800)}));
document.querySelectorAll('.filter-bar button').forEach(btn=>btn.addEventListener('click',()=>{btn.parentElement.querySelectorAll('button').forEach(x=>x.classList.remove('active'));btn.classList.add('active')}));

// Inject search and shadow styles if not present
if(!document.querySelector('link[href*="product-shadows.css"]')){
  const productShadows=document.createElement('link');productShadows.rel='stylesheet';productShadows.href='css/product-shadows.css?v=20261111';document.head.append(productShadows);
}
if(!document.querySelector('link[href*="i18n.css"]')){
  const i18nCss=document.createElement('link');i18nCss.rel='stylesheet';i18nCss.href='css/i18n.css?v=20261117-left';document.head.append(i18nCss);
}
if(!document.querySelector('link[href*="card-style.css"]')){
  const cardCss=document.createElement('link');cardCss.rel='stylesheet';cardCss.href='css/card-style.css?v=20261117-static';document.head.append(cardCss);
}
if(!document.querySelector('link[href*="brand-filter.css"]')){
  const brandCss=document.createElement('link');brandCss.rel='stylesheet';brandCss.href='css/brand-filter.css?v=20261117';document.head.append(brandCss);
}
if(!document.querySelector('script[src*="search.js"]')){
  const searchScript=document.createElement('script');searchScript.src='js/search.js?v=20261117';document.head.append(searchScript);
}
