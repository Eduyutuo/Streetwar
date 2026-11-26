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
const descriptionFor=product=>{
  const lang = (window.RITMO_I18N && window.RITMO_I18N.getLang()) || 'es';
  if (lang === 'en') {
    return `${product.name} blends iconic street style with premium materials engineered for daily wear. This release is part of the Streetwar 2026 catalog and is available for ${product.audience.toLowerCase()} in selected sizes.`;
  }
  return `${product.name} combina una silueta urbana con una construcción pensada para uso diario. Este modelo forma parte del inventario Streetwar 2026 y está disponible para ${product.audience.toLowerCase()} en las tallas indicadas.`;
};

if(detailRoot){
  const requested=Number(new URLSearchParams(location.search).get('id'));
  const id=Number.isInteger(requested)&&requested>=0&&requested<inventory.length?requested:0;
  const product=inventory[id];
  detailRoot.dataset.productId=id;
  const sizes=expandSizes(product.sizes);
  const hasListedSizes=sizes.length>0;
  const brand=brandFor(product);

  const getT = () => (window.RITMO_I18N && window.RITMO_I18N.getT()) || {
    detail: {
      breadcrumb: 'INICIO / CATÁLOGO / DETALLE',
      availableForOrder: 'Disponible para pedido',
      authTitle: 'STREETWAR',
      authText: 'Producto seleccionado para nuestro catálogo 2026',
      audienceLabel: 'ESTE MODELO ES',
      unisexSub: 'Diseñado para mujer y hombre',
      genderSub: 'Según el inventario Streetwar',
      selectSize: 'SELECCIONA TU TALLA',
      euSize: 'TALLA EU',
      sizesInInventory: 'Tallas registradas en inventario:',
      sizesPending: 'Tallas por confirmar. Escríbenos para consultar disponibilidad.',
      btnSelectSize: 'SELECCIONA UNA TALLA',
      btnInquire: 'CONSULTAR DISPONIBILIDAD',
      btnBuyWhatsApp: 'COMPRAR POR WHATSAPP · EU',
      whatsappNote: 'Elige Contacto 1 (USA) o Contacto 2 (PE) en el radar de WhatsApp.',
      benefit1Title: 'Atención directa',
      benefit1Text: 'Confirma stock, entrega y forma de pago con un asesor.',
      benefit2Title: 'Pedido preparado',
      benefit2Text: 'Enviaremos el modelo, precio y talla elegida.',
      productDetails: 'DETALLES DEL PRODUCTO',
      brand: 'MARCA',
      silhouette: 'SILUETA',
      model: 'MODELO',
      code: 'CÓDIGO',
      backToCatalog: '← VOLVER AL CATÁLOGO',
      alsoLike: 'TAMBIÉN TE PUEDE GUSTAR',
      moreLikeThis: 'MÁS COMO ESTO',
      seeAll: 'VER TODO',
      viewCount: 'TOMAS DEL MODELO',
      referentialImage: 'IMAGEN REFERENCIAL DEL MODELO'
    },
    whatsapp: {
      orderMsg: (name, size, price, cat) => `Hola Streetwar, quiero comprar este modelo:\n\n*${name}*\n${size?`Talla: *EU ${size}*`:'Talla: *Por confirmar*'}\nPrecio: *${price}*\nCategoría: ${cat}\n\n¿Está disponible?`
    }
  };

  const gallery = (typeof sourceLinkPhotos !== 'undefined' && sourceLinkPhotos[id]?.length)
    ? sourceLinkPhotos[id].slice(0, 8)
    : (typeof galleries !== 'undefined' && galleries[id]?.length 
        ? galleries[id].slice(0, 8) 
        : [product.image]);
  let selected='';
  let galleryIndex=0;

  function renderDetailView() {
    const t = getT();
    const money = window.RITMO_I18N ? window.RITMO_I18N.formatPrice : (p => `S/ ${p.toLocaleString('es-PE')}`);
    const audienceLabel = product.audience==='Mujer' ? (t.detail.audienceLabel === 'THIS MODEL IS' ? 'WOMEN' : 'PARA MUJER') : product.audience==='Hombre' ? (t.detail.audienceLabel === 'THIS MODEL IS' ? 'MEN' : 'PARA HOMBRE') : 'UNISEX';

    document.title=`${product.name} — Streetwar`;

    const breadcrumbEl = document.querySelector('.breadcrumb');
    if (breadcrumbEl) {
      breadcrumbEl.innerHTML = `<a href="novedades.html">${t.detail.breadcrumb.split('/')[0]} / ${t.detail.breadcrumb.split('/')[1]}</a> / ${t.detail.breadcrumb.split('/')[2]}`;
    }

    detailRoot.innerHTML=`
      <div class="detail-gallery">
        <div class="detail-thumbs" aria-label="Galería del producto">
          ${gallery.map((image,index)=>`<button class="thumb ${index===galleryIndex?'active':''}" type="button" data-gallery-index="${index}" aria-label="Ver imagen ${index+1}"><img src="assets/${image}?v=20261125-output-catalog" alt="Vista ${index+1} de ${product.name}"></button>`).join('')}
        </div>
        <div class="detail-main">
          <span class="detail-tag">STREETWAR SELECT</span>
          <img data-main-image src="assets/${gallery[galleryIndex]}?v=20261125-output-catalog" alt="Vista 1 de ${product.name}">
          ${gallery.length>1?'<div class="gallery-controls"><button type="button" data-gallery-nav="previous" aria-label="Imagen anterior">‹</button><button type="button" data-gallery-nav="next" aria-label="Imagen siguiente">›</button></div>':''}
          <small>${gallery.length>1?`${gallery.length} ${t.detail.viewCount}`:t.detail.referentialImage}</small>
        </div>
      </div>
      <div class="detail-info">
        <p class="kicker">HOME / SNEAKERS / ${brand.toUpperCase()}</p>
        <h1>${product.name}</h1>
        <p class="detail-audience">${product.category} · ${product.audience}</p>
        <strong class="detail-price">${money(product.price)}</strong>
        <p class="availability"><span></span> ${t.detail.availableForOrder}</p>
        <div class="auth-card"><strong>${t.detail.authTitle}</strong><span>${t.detail.authText}</span></div>
        <div class="detail-rule"></div>
        <div class="audience-card"><span>${t.detail.audienceLabel}</span><strong>${audienceLabel}</strong><small>${product.audience==='Unisex'?t.detail.unisexSub:t.detail.genderSub}</small></div>
        ${hasListedSizes?`<div class="size-heading"><h2>${t.detail.selectSize}</h2><span>${t.detail.euSize}</span></div><div class="size-grid">${sizes.map(size=>`<button type="button" data-size="${size}" class="${selected===size?'selected':''}" aria-pressed="${selected===size?'true':'false'}">EU ${size}</button>`).join('')}</div><p class="size-copy">${t.detail.sizesInInventory} <strong>${product.sizes}</strong></p>`:`<p class="size-copy">${t.detail.sizesPending}</p>`}
        <button class="detail-add whatsapp-buy" type="button" ${hasListedSizes && !selected ?'disabled':''}>${selected ? `${t.detail.btnBuyWhatsApp} ${selected}` : (hasListedSizes ? t.detail.btnSelectSize : t.detail.btnInquire)}</button>
        <p class="whatsapp-note">${t.detail.whatsappNote}</p>
        <div class="purchase-benefits">
          <p><b>✓</b><span><strong>${t.detail.benefit1Title}</strong>${t.detail.benefit1Text}</span></p>
          <p><b>✓</b><span><strong>${t.detail.benefit2Title}</strong>${t.detail.benefit2Text}</span></p>
        </div>
        <div class="product-facts">
          <h2>${t.detail.productDetails}</h2>
          <p>${descriptionFor(product)}</p>
          <dl>
            <div><dt>${t.detail.brand}</dt><dd>${brand}</dd></div>
            <div><dt>${t.detail.silhouette}</dt><dd>${product.category}</dd></div>
            <div><dt>${t.detail.model}</dt><dd>${product.name}</dd></div>
            ${product.sku?`<div><dt>${t.detail.code}</dt><dd>${product.sku}</dd></div>`:''}
            <div><dt>${t.detail.euSize}</dt><dd>${product.sizes} EU</dd></div>
          </dl>
        </div>
        <a class="back-catalog" href="novedades.html">${t.detail.backToCatalog}</a>
      </div>`;

    const addButton=detailRoot.querySelector('.detail-add');
    detailRoot.querySelectorAll('[data-size]').forEach(button=>button.addEventListener('click',()=>{
      detailRoot.querySelectorAll('[data-size]').forEach(option=>{option.classList.remove('selected');option.setAttribute('aria-pressed','false')});
      button.classList.add('selected');
      button.setAttribute('aria-pressed','true');
      selected=button.dataset.size;
      addButton.disabled=false;
      addButton.textContent=`${t.detail.btnBuyWhatsApp} ${selected}`;
    }));

    const mainImage=detailRoot.querySelector('[data-main-image]');
    const showGalleryImage=index=>{
      galleryIndex=(index+gallery.length)%gallery.length;
      mainImage.src=`assets/${gallery[galleryIndex]}?v=20261125-output-catalog`;
      mainImage.alt=`Vista ${galleryIndex+1} de ${product.name}`;
      detailRoot.querySelectorAll('[data-gallery-index]').forEach(button=>button.classList.toggle('active',Number(button.dataset.galleryIndex)===galleryIndex));
    };
    detailRoot.querySelectorAll('[data-gallery-index]').forEach(button=>button.addEventListener('click',()=>showGalleryImage(Number(button.dataset.galleryIndex))));
    detailRoot.querySelectorAll('[data-gallery-nav]').forEach(button=>button.addEventListener('click',()=>showGalleryImage(galleryIndex+(button.dataset.galleryNav==='next'?1:-1))));

    addButton.addEventListener('click',()=>{
      const moneyText = money(product.price);
      const message = t.whatsapp.orderMsg(product.name, selected, moneyText, product.category);
      window.dispatchEvent(new CustomEvent('open-whatsapp-picker',{detail:{message}}));
    });

    // Related section translations
    const relatedHeading = document.querySelector('.related-heading');
    if (relatedHeading) {
      relatedHeading.querySelector('.kicker').textContent = t.detail.alsoLike;
      relatedHeading.querySelector('h2').textContent = t.detail.moreLikeThis;
      relatedHeading.querySelector('a').textContent = t.detail.seeAll;
    }

    const relatedRoot=document.querySelector('#related-products');
    if (relatedRoot) {
      const related=inventory.map((item,index)=>({item,index})).filter(entry=>entry.index!==id&&(entry.item.category===product.category||brandFor(entry.item)===brand)).slice(0,6);
      relatedRoot.innerHTML=related.map(({item,index})=>`<article><a href="producto.html?id=${index}"><div><img src="assets/${item.image}?v=20261030-whatsapp" alt="${item.name}" loading="lazy"></div><h3>${item.name}</h3><p>${item.sizes} EU</p><strong>${money(item.price)}</strong></a></article>`).join('');
    }

    // Detail notes below
    const detailNotes = document.querySelector('.detail-notes');
    if (detailNotes && t.detail.notes) {
      detailNotes.innerHTML = t.detail.notes.map(n => `<article><span>${n.num}</span><h3>${n.title}</h3><p>${n.text}</p></article>`).join('');
    }
  }

  renderDetailView();
  window.addEventListener('languagechange', () => {
    renderDetailView();
  });
}
