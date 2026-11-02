(()=>{
  const WHATSAPP_NUMBER='51999999999';
  const normalize=value=>value.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
  const escapeHtml=value=>String(value).replace(/[&<>"]/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[char]));
  const init=()=>{
    if(typeof inventory==='undefined'){setTimeout(init,40);return}
    document.querySelectorAll('form[role="search"]').forEach(form=>{
      if(form.dataset.liveSearch)return;
      form.dataset.liveSearch='ready';
      const input=form.querySelector('input[type="search"]');
      if(!input)return;
      const results=document.createElement('div');
      results.className='live-search-results';
      results.setAttribute('role','listbox');
      form.append(results);
      const close=()=>{results.innerHTML='';results.classList.remove('open')};
      const render=()=>{
        const query=input.value.trim();
        if(!query){close();return}
        const terms=normalize(query).split(/\s+/).filter(Boolean);
        const found=inventory.filter(product=>terms.every(term=>normalize(`${product.name} ${product.category} ${product.audience} ${product.sizes}`).includes(term))).slice(0,6);
        results.innerHTML=found.length?found.map(product=>{
          const id=inventory.indexOf(product);
          return `<a role="option" href="producto.html?id=${id}"><img src="assets/${product.image}?v=20261102-search" alt=""><span><strong>${escapeHtml(product.name)}</strong><small>${escapeHtml(product.category)} · ${escapeHtml(product.audience)} · ${escapeHtml(product.sizes)} EU</small></span><b>S/ ${product.price.toLocaleString('es-PE')}</b></a>`;
        }).join(''):`<p>No encontramos resultados para “${escapeHtml(query)}”.</p>`;
        results.classList.add('open');
      };
      input.addEventListener('input',render);
      input.addEventListener('focus',render);
      input.addEventListener('keydown',event=>{if(event.key==='Escape'){close();input.blur()}});
      document.addEventListener('click',event=>{if(!form.contains(event.target))close()});
    });
    if(!document.querySelector('.whatsapp-float')){
      const whatsapp=document.createElement('a');
      whatsapp.className='whatsapp-float';
      whatsapp.href=`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent('Hola Streetwar, quiero consultar por una zapatilla.')}`;
      whatsapp.target='_blank';
      whatsapp.rel='noopener';
      whatsapp.setAttribute('aria-label','Consultar por WhatsApp');
      whatsapp.title='Comprar por WhatsApp';
      whatsapp.innerHTML='<img src="assets/icono-whastapp.png" alt=""><span>WHATSAPP</span>';
      document.body.append(whatsapp);
    }
  };
  init();
})();
