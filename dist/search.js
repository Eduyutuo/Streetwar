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
      whatsapp.innerHTML='<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M27.6 4.3A15.8 15.8 0 0 0 2.8 23.4L1 31l7.8-1.9A15.8 15.8 0 1 0 27.6 4.3ZM16 28.5c-2.3 0-4.5-.6-6.4-1.7l-.5-.3-4.6 1.1 1.1-4.5-.3-.5A12.5 12.5 0 1 1 16 28.5Zm6.9-9.4c-.4-.2-2.4-1.2-2.8-1.3-.4-.2-.6-.2-.9.2-.3.4-1 1.3-1.2 1.6-.2.3-.5.3-.9.1-2.3-1.1-3.8-2-5.3-4.6-.4-.7.4-.6 1.1-2 .1-.3.1-.6 0-.8-.1-.2-.9-2.2-1.3-3-.3-.8-.7-.7-.9-.7h-.8c-.3 0-.8.1-1.2.6-.4.4-1.6 1.6-1.6 3.9s1.7 4.5 2 4.8c.2.3 3.3 5 8 7 3 .9 4.1.9 5.6.8.9-.1 2.4-1 2.7-2 .3-1 .3-1.9.2-2.1-.1-.2-.4-.3-.8-.5Z"/></svg><span>WHATSAPP</span>';
      document.body.append(whatsapp);
    }
  };
  init();
})();
