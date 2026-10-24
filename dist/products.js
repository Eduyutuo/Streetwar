const inventory = [
  ['Air Jordan 1 High OG "Royal"','Air Jordan 1','unisex','product-sneaker.png'],
  ['Air Jordan 1 Retro High OG "Shattered Backboard"','Air Jordan 1','unisex','product-sneaker.png'],
  ['Air Jordan 1 Mid SE Black/Gold/Pink','Air Jordan 1','women','editorial-woman.png'],
  ['Air Jordan 3 Retro "True Blue" (White/Blue)','Air Jordan 3','unisex','campaign-men.png'],
  ['Air Jordan 3 Retro GS "Spring Flowers"','Air Jordan 3','kids','campaign-kids.png'],
  ['Air Jordan 3 Retro Green/White/Red','Air Jordan 3','unisex','campaign-men.png'],
  ['Air Jordan 4 Retro x J Balvin "Amazonas"','Air Jordan 4','unisex','hero-ritmo.png'],
  ['Air Jordan 4 Retro "Tour Yellow" (Lightning)','Air Jordan 4','unisex','hero-ritmo.png'],
  ['Air Jordan 6 Retro "Oreo"','Air Jordan 6','unisex','campaign-accessories.png'],
  ['Air Jordan 9 Retro "Space Jam"','Air Jordan 9','unisex','campaign-accessories.png'],
  ['Air Jordan 12 Retro "Bucks"','Air Jordan 12','unisex','campaign-men.png'],
  ['Air Jordan Access "Black Gym Red"','Jordan Hybrid / Otros','unisex','product-sneaker.png'],
  ['Jordan Max Aura Black/White','Jordan Hybrid / Otros','unisex','product-sneaker.png'],
  ['Jordan Max Aura Black/Black/Gym Red','Jordan Hybrid / Otros','unisex','campaign-men.png'],
  ['Jordan Son of Mars Low — White/Red/Black','Jordan Hybrid / Otros','unisex','campaign-men.png'],
  ["Nike Air Force 1 '07 Black/White/Orange Peel",'Nike Air Force 1','unisex','product-sneaker.png'],
  ["Nike Air Force 1 '07 WNBA 30th Anniversary",'Nike Air Force 1','women','editorial-woman.png'],
  ["Nike Air Force 1 '07 LV8 \"Mexico\"",'Nike Air Force 1','unisex','product-sneaker.png'],
  ['Nike Air Max Bolt (Mujer)','Nike Air Max','women','editorial-woman.png'],
  ['Nike Air Max Correlate White/New Green/Bright Mango/Black','Nike Air Max','unisex','product-sneaker.png'],
  ['Nike Air Max Correlate Black/White/Grey','Nike Air Max','unisex','product-sneaker.png'],
  ['Nike Air Max 95 White/Pink/Brown','Nike Air Max','women','editorial-woman.png'],
  ['Nike Air Max Command PRM "Light Taupe"','Nike Air Max','unisex','product-sneaker.png'],
  ['Nike Air Diamond Turf II "Royals"','Nike Diamond / DT / Griffey','men','campaign-men.png'],
  ["Nike Air DT Max '96 Low White/Metallic",'Nike Diamond / DT / Griffey','men','campaign-men.png'],
  ['Nike Air Griffey Max 1','Nike Diamond / DT / Griffey','men','campaign-men.png'],
  ['Nike Zoom LeBron NXXT Gen "Black Wolf Grey"','Nike Basketball / Performance','men','campaign-accessories.png'],
  ['Nike Flight Legacy "Black/White"','Nike Basketball / Performance','men','campaign-accessories.png']
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
    grid.innerHTML = items.map((p, i) => `<article class="product" data-category="${p[1]}"><div class="product-media shoe"><img src="assets/${p[3]}?v=20261023-inventory" alt="Imagen editorial de zapatillas Jordan"><span class="pill">${i < 4 ? 'DESTACADO' : p[1].toUpperCase()}</span><button class="heart" aria-label="Guardar producto" style="border:0;background:none">♡</button></div><h3>${p[0]}</h3><p>${p[1]} · Talla y stock: consultar</p><strong>Precio por confirmar</strong></article>`).join('');
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
