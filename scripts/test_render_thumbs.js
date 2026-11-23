const fs = require('fs');

global.window = {};
eval(fs.readFileSync('dist/js/source-link-photos.js', 'utf8').replace('const sourceLinkPhotos =', 'global.sourceLinkPhotos ='));
eval(fs.readFileSync('dist/js/galleries.js', 'utf8').replace('const galleries =', 'global.galleries ='));

const id = 0;
const product = { name: 'Air Jordan 9 Retro OG "Space Jam"', image: 'productos/IX6180-100/01-lateral.webp' };
const gallery = (typeof global.sourceLinkPhotos !== 'undefined' && global.sourceLinkPhotos[id]?.length)
  ? global.sourceLinkPhotos[id].slice(0, 8)
  : (typeof global.galleries !== 'undefined' && global.galleries[id]?.length 
      ? global.galleries[id].slice(0, 8) 
      : [product.image]);

const galleryIndex = 0;
const thumbsHtml = gallery.map((image,index)=>
  `<button class="thumb ${index===galleryIndex?'active':''}" type="button" data-gallery-index="${index}" aria-label="Ver imagen ${index+1}"><img src="assets/${image}?v=20261102-clean" alt="Vista ${index+1} de ${product.name}"></button>`
).join('');

console.log('<div class="detail-thumbs" aria-label="Galería del producto">\n  ' + thumbsHtml + '\n</div>');
