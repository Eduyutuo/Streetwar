/* Número peruano de demostración. Reemplazar por el WhatsApp real sin + ni espacios. */
const WHATSAPP_NUMBER='51999999999';
const detailRoot=document.querySelector('#product-detail');

const expandSizes=label=>{
  const sizes=[];
  label.split('/').map(part=>part.trim()).forEach(part=>{
    const range=part.match(/^(\d+(?:\.\d+)?)\s*[–-]\s*(\d+(?:\.\d+)?)$/);
    if(range){
      const start=Number(range[1]);
      const end=Number(range[2]);
      const step=Number.isInteger(start)&&Number.isInteger(end)?1:.5;
      for(let size=start;size<=end;size+=step)sizes.push(String(size));
    }else if(part){sizes.push(part)}
  });
  return [...new Set(sizes)];
};

const brandFor=product=>product.name.toLowerCase().includes('nike')?'Nike':'Jordan';
const descriptionFor=product=>`${product.name} combina una silueta urbana con una construcción pensada para uso diario. Este modelo forma parte del inventario Streetwar 2026 y está disponible para ${product.audience.toLowerCase()} en las tallas indicadas.`;

if(detailRoot){
  const requested=Number(new URLSearchParams(location.search).get('id'));
  const id=Number.isInteger(requested)&&requested>=0&&requested<inventory.length?requested:0;
  const product=inventory[id];
  const sizes=expandSizes(product.sizes);
  const brand=brandFor(product);
  document.title=`${product.name} — Streetwar`;
  detailRoot.innerHTML=`
    <div class="detail-gallery">
      <div class="detail-thumbs" aria-label="Galería del producto">
        <button class="thumb active" type="button" data-view="contain" aria-label="Vista completa"><img src="assets/${product.image}?v=20261030-whatsapp" alt=""></button>
        <button class="thumb" type="button" data-view="zoom" aria-label="Vista ampliada"><img src="assets/${product.image}?v=20261030-whatsapp" alt=""></button>
        <button class="thumb" type="button" data-view="detail" aria-label="Detalle lateral"><img src="assets/${product.image}?v=20261030-whatsapp" alt=""></button>
      </div>
      <div class="detail-main" data-main-view="contain">
        <span class="detail-tag">STREETWAR SELECT</span>
        <img src="assets/${product.image}?v=20261030-whatsapp" alt="${product.name}">
        <small>IMAGEN REFERENCIAL DEL MODELO</small>
      </div>
    </div>
    <div class="detail-info">
      <p class="kicker">INICIO / ZAPATILLAS / ${brand.toUpperCase()}</p>
      <h1>${product.name}</h1>
      <p class="detail-audience">${product.category} · ${product.audience}</p>
      <strong class="detail-price">${money(product.price)}</strong>
      <p class="availability"><span></span> Disponible para pedido</p>
      <div class="auth-card"><strong>STREETWAR</strong><span>Producto seleccionado para nuestro catálogo 2026</span></div>
      <div class="detail-rule"></div>
      <div class="size-heading"><h2>SELECCIONA TU TALLA</h2><span>TALLA EU</span></div>
      <div class="size-grid">${sizes.map(size=>`<button type="button" data-size="${size}" aria-pressed="false">EU ${size}</button>`).join('')}</div>
      <p class="size-copy">Tallas registradas en inventario: <strong>${product.sizes}</strong></p>
      <button class="detail-add whatsapp-buy" type="button" disabled>SELECCIONA UNA TALLA</button>
      <p class="whatsapp-note">La compra se coordina directamente por WhatsApp. Número de demostración.</p>
      <div class="purchase-benefits"><p><b>✓</b><span><strong>Atención directa</strong>Confirma stock, entrega y forma de pago con un asesor.</span></p><p><b>✓</b><span><strong>Pedido preparado</strong>Enviaremos el modelo, precio y talla elegida.</span></p></div>
      <div class="product-facts">
        <h2>DETALLES DEL PRODUCTO</h2>
        <p>${descriptionFor(product)}</p>
        <dl><div><dt>MARCA</dt><dd>${brand}</dd></div><div><dt>SILUETA</dt><dd>${product.category}</dd></div><div><dt>MODELO</dt><dd>${product.name}</dd></div><div><dt>TALLAS</dt><dd>${product.sizes} EU</dd></div><div><dt>PÚBLICO</dt><dd>${product.audience}</dd></div></dl>
      </div>
      <a class="back-catalog" href="novedades.html">← VOLVER AL CATÁLOGO</a>
    </div>`;

  let selected='';
  const addButton=detailRoot.querySelector('.detail-add');
  detailRoot.querySelectorAll('[data-size]').forEach(button=>button.addEventListener('click',()=>{
    detailRoot.querySelectorAll('[data-size]').forEach(option=>{option.classList.remove('selected');option.setAttribute('aria-pressed','false')});
    button.classList.add('selected');
    button.setAttribute('aria-pressed','true');
    selected=button.dataset.size;
    addButton.disabled=false;
    addButton.textContent=`COMPRAR POR WHATSAPP · EU ${selected}`;
  }));
  detailRoot.querySelectorAll('[data-view]').forEach(button=>button.addEventListener('click',()=>{
    detailRoot.querySelectorAll('[data-view]').forEach(option=>option.classList.remove('active'));
    button.classList.add('active');
    detailRoot.querySelector('.detail-main').dataset.mainView=button.dataset.view;
  }));
  addButton.addEventListener('click',()=>{
    const message=`Hola Streetwar, quiero comprar este modelo:\n\n*${product.name}*\nTalla: *EU ${selected}*\nPrecio: *${money(product.price)}*\nCategoría: ${product.category}\n\n¿Está disponible?`;
    window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`,'_blank','noopener');
  });

  const relatedRoot=document.querySelector('#related-products');
  const related=inventory.map((item,index)=>({item,index})).filter(entry=>entry.index!==id&&(entry.item.category===product.category||brandFor(entry.item)===brand)).slice(0,6);
  relatedRoot.innerHTML=related.map(({item,index})=>`<article><a href="producto.html?id=${index}"><div><img src="assets/${item.image}?v=20261030-whatsapp" alt="${item.name}" loading="lazy"></div><h3>${item.name}</h3><p>${item.sizes} EU</p><strong>${money(item.price)}</strong></a></article>`).join('');
}
