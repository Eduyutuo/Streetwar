(()=>{
  const WHATSAPP_CONTACTS=[
    {label:'Contacto 1',number:'13017933122',display:'+1 301 793 3122'},
    {label:'Contacto 2',number:'51940640679',display:'+51 940 640 679'}
  ];
  const defaultMessage='Hola Streetwar, quiero consultar por una zapatilla.';
  const openContact=(number,message)=>window.open(`https://wa.me/${number}?text=${encodeURIComponent(message||defaultMessage)}`,'_blank','noopener');
  const openPicker=message=>{
    const radar=document.querySelector('.whatsapp-radar');
    if(!radar)return;
    radar.dataset.message=message||defaultMessage;
    radar.classList.add('is-open');
    radar.querySelector('.whatsapp-radar-toggle')?.focus();
  };
  window.openWhatsAppPicker=openPicker;
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
    if(!document.querySelector('.whatsapp-radar')){
      const radar=document.createElement('div');
      radar.className='whatsapp-radar';
      radar.dataset.message=defaultMessage;
      radar.innerHTML=`<div class="whatsapp-radar-menu" aria-label="Contactos de WhatsApp"><b>SOPORTE WHATSAPP</b>${WHATSAPP_CONTACTS.map(contact=>`<button type="button" data-whatsapp-number="${contact.number}"><strong>${contact.label}</strong><small>${contact.display}</small></button>`).join('')}</div><button class="whatsapp-radar-toggle" type="button" aria-label="Elegir contacto de WhatsApp" aria-expanded="false"><img src="assets/icono-whastapp.png" alt=""><span>WHATSAPP</span></button>`;
      radar.querySelector('.whatsapp-radar-toggle').addEventListener('click',()=>{
        const open=radar.classList.toggle('is-open');
        radar.querySelector('.whatsapp-radar-toggle').setAttribute('aria-expanded',String(open));
      });
      radar.querySelectorAll('[data-whatsapp-number]').forEach(button=>button.addEventListener('click',()=>openContact(button.dataset.whatsappNumber,radar.dataset.message)));
      document.addEventListener('click',event=>{if(!radar.contains(event.target)){radar.classList.remove('is-open');radar.querySelector('.whatsapp-radar-toggle').setAttribute('aria-expanded','false')}});
      document.body.append(radar);
    }
    window.addEventListener('open-whatsapp-picker',event=>openPicker(event.detail?.message));
  };
  init();
})();
