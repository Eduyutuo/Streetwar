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

if(detailRoot){
  const requested=Number(new URLSearchParams(location.search).get('id'));
  const id=Number.isInteger(requested)&&requested>=0&&requested<inventory.length?requested:0;
  const product=inventory[id];
  const sizes=expandSizes(product.sizes);
  document.title=`${product.name} — Streetwar`;
  detailRoot.innerHTML=`
    <div class="detail-gallery">
      <div class="detail-main"><img src="assets/${product.image}?v=20261030-detail" alt="${product.name}"></div>
      <div class="detail-side">
        <div class="detail-tile"><img src="assets/${product.image}?v=20261030-detail" alt="Vista de ${product.name}"></div>
        <div class="detail-color"><span>${product.group}</span><strong>${product.category}</strong><small>CATÁLOGO STREETWAR 2026</small></div>
      </div>
    </div>
    <div class="detail-info">
      <p class="kicker">GRUPO ${product.group} / ${product.category.toUpperCase()}</p>
      <h1>${product.name}</h1>
      <p class="detail-audience">${product.audience} · Producto importado</p>
      <strong class="detail-price">${money(product.price)}</strong>
      <div class="detail-rule"></div>
      <div class="size-heading"><h2>SELECCIONA TU TALLA</h2><span>TALLA EU</span></div>
      <div class="size-grid">${sizes.map(size=>`<button type="button" data-size="${size}" aria-pressed="false">${size}</button>`).join('')}</div>
      <p class="size-copy">Tallas disponibles: <strong>${product.sizes}</strong></p>
      <button class="detail-add" type="button" disabled>SELECCIONA UNA TALLA</button>
      <div class="detail-accordion">
        <details open><summary>INFORMACIÓN DEL PRODUCTO</summary><p>${product.name}, de la categoría ${product.category}. Disponible para ${product.audience.toLowerCase()} en las tallas indicadas.</p></details>
        <details><summary>PRECIO Y DISPONIBILIDAD</summary><p>Precio de catálogo: ${money(product.price)}. La disponibilidad final se confirma al realizar el pedido.</p></details>
        <details><summary>CAMBIOS Y CUIDADO</summary><p>Conserva el producto sin uso y su empaque. Limpia suavemente con un paño húmedo; no uses lavadora.</p></details>
      </div>
      <a class="back-catalog" href="novedades.html">← VOLVER AL CATÁLOGO</a>
    </div>`;

  let selected='';
  const addButton=detailRoot.querySelector('.detail-add');
  detailRoot.querySelectorAll('[data-size]').forEach(button=>button.addEventListener('click',()=>{
    detailRoot.querySelectorAll('[data-size]').forEach(option=>{
      option.classList.remove('selected');
      option.setAttribute('aria-pressed','false');
    });
    button.classList.add('selected');
    button.setAttribute('aria-pressed','true');
    selected=button.dataset.size;
    addButton.disabled=false;
    addButton.textContent=`AGREGAR TALLA ${selected}`;
  }));
  addButton.addEventListener('click',()=>{
    addButton.textContent=`AÑADIDO · TALLA ${selected} ✓`;
    const toast=document.querySelector('.toast');
    if(toast){toast.textContent=`${product.name} · Talla ${selected}`;toast.classList.add('show');setTimeout(()=>toast.classList.remove('show'),2200)}
  });
}
