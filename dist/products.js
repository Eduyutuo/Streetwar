const inventory = [
  ['Air Jordan 1 High OG "Royal"','Air Jordan 1','unisex','jordan-1-royal-product.webp'],
  ['Air Jordan 1 Retro High OG "Shattered Backboard"','Air Jordan 1','unisex','jordan-1-royal-product.webp'],
  ['Air Jordan 1 Mid SE Black/Gold/Pink','Air Jordan 1','women','jordan-1-royal-product.webp'],
  ['Air Jordan 3 Retro "True Blue" (White/Blue)','Air Jordan 3','unisex','jordan-3-spring-flowers-product.webp'],
  ['Air Jordan 3 Retro GS "Spring Flowers"','Air Jordan 3','kids','jordan-3-spring-flowers-product.webp'],
  ['Air Jordan 3 Retro Green/White/Red','Air Jordan 3','unisex','jordan-3-spring-flowers-product.webp'],
  ['Air Jordan 4 Retro x J Balvin "Amazonas"','Air Jordan 4','unisex','jordan-4-amazonas-product.webp'],
  ['Air Jordan 4 Retro "Tour Yellow" (Lightning)','Air Jordan 4','unisex','jordan-4-amazonas-product.webp'],
  ['Air Jordan 6 Retro "Oreo"','Air Jordan 6','unisex','jordan-1-royal-product.webp'],
  ['Air Jordan 9 Retro "Space Jam"','Air Jordan 9','unisex','jordan-1-royal-product.webp'],
  ['Air Jordan 12 Retro "Bucks"','Air Jordan 12','unisex','jordan-4-amazonas-product.webp'],
  ['Air Jordan Access "Black Gym Red"','Jordan Hybrid / Otros','unisex','jordan-1-royal-product.webp'],
  ['Jordan Max Aura Black/White','Jordan Hybrid / Otros','unisex','jordan-1-royal-product.webp'],
  ['Jordan Max Aura Black/Black/Gym Red','Jordan Hybrid / Otros','unisex','jordan-4-amazonas-product.webp'],
  ['Jordan Son of Mars Low — White/Red/Black','Jordan Hybrid / Otros','unisex','jordan-4-amazonas-product.webp'],
  ["Nike Air Force 1 '07 Black/White/Orange Peel",'Nike Air Force 1','unisex','nike-air-force-air-max-product.webp'],
  ["Nike Air Force 1 '07 WNBA 30th Anniversary",'Nike Air Force 1','women','nike-air-force-air-max-product.webp'],
  ["Nike Air Force 1 '07 LV8 \"Mexico\"",'Nike Air Force 1','unisex','nike-air-force-air-max-product.webp'],
  ['Nike Air Max Bolt (Mujer)','Nike Air Max','women','nike-air-force-air-max-product.webp'],
  ['Nike Air Max Correlate White/New Green/Bright Mango/Black','Nike Air Max','unisex','nike-air-force-air-max-product.webp'],
  ['Nike Air Max Correlate Black/White/Grey','Nike Air Max','unisex','nike-air-force-air-max-product.webp'],
  ['Nike Air Max 95 White/Pink/Brown','Nike Air Max','women','nike-air-force-air-max-product.webp'],
  ['Nike Air Max Command PRM "Light Taupe"','Nike Air Max','unisex','nike-air-force-air-max-product.webp'],
  ['Nike Air Diamond Turf II "Royals"','Nike Diamond / DT / Griffey','men','nike-air-force-air-max-product.webp'],
  ["Nike Air DT Max '96 Low White/Metallic",'Nike Diamond / DT / Griffey','men','nike-air-force-air-max-product.webp'],
  ['Nike Air Griffey Max 1','Nike Diamond / DT / Griffey','men','nike-air-force-air-max-product.webp'],
  ['Nike Zoom LeBron NXXT Gen "Black Wolf Grey"','Nike Basketball / Performance','men','nike-air-force-air-max-product.webp'],
  ['Nike Flight Legacy "Black/White"','Nike Basketball / Performance','men','nike-air-force-air-max-product.webp']
];

const sets = {
  default: inventory,
  men: inventory.filter(([, , audience]) => audience !== 'women' && audience !== 'kids'),
  women: inventory.filter(([, , audience]) => audience === 'women' || audience === 'unisex').slice(0, 12),
  kids: inventory.filter(([, , audience]) => audience === 'kids'),
  sale: inventory.slice(0, 8)
};

const grid = document.querySelector('[data-products]');
if (grid) {
  const key = grid.dataset.products || 'default';
  const products = sets[key] || sets.default;
  const render = (items) => {
    grid.innerHTML = items.map((p, i) => `<article class="product" data-category="${p[1]}"><div class="product-media shoe"><img src="assets/${p[3]}?v=20261023-shoes" alt="Fotografía de zapatillas de la familia ${p[1]}"><span class="pill">${i < 4 ? 'DESTACADO' : p[1].toUpperCase()}</span><button class="heart" aria-label="Guardar producto" style="border:0;background:none">♡</button></div><h3>${p[0]}</h3><p>${p[1]} · Talla y stock: consultar</p><strong>Precio por confirmar</strong></article>`).join('');
    document.querySelectorAll('.heart').forEach(btn => btn.addEventListener('click', () => {
      const toast = document.querySelector('.toast');
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 1800);
    }));
  };
  render(products);
  document.querySelectorAll('.filter-bar button[data-filter]').forEach(btn => btn.addEventListener('click', () => {
    btn.parentElement.querySelectorAll('button').forEach(x => x.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.dataset.filter;
    render(filter === 'all' ? products : products.filter(p => p[1].includes(filter)));
  }));
}
