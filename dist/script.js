const nav=document.querySelector('.main-nav');
document.querySelectorAll('img[src^="assets/"]').forEach(img=>{const url=new URL(img.src);url.searchParams.set('v','20261023-inventory');img.src=url.href;});
const toggle=document.querySelector('.menu-toggle');
const mega=document.querySelector('.mega-menu');
const bag=document.querySelector('.bag');
const scrim=document.querySelector('.scrim');
toggle.addEventListener('click',()=>{const open=nav.classList.toggle('open');toggle.setAttribute('aria-expanded',open);});
document.querySelectorAll('[data-menu]').forEach(btn=>btn.addEventListener('click',()=>{const open=mega.classList.toggle('open');mega.setAttribute('aria-hidden',!open);}));
function closePanels(){bag.classList.remove('open');scrim.classList.remove('open');bag.setAttribute('aria-hidden','true');mega.classList.remove('open');}
document.querySelector('.bag-button').addEventListener('click',()=>{bag.classList.add('open');scrim.classList.add('open');bag.setAttribute('aria-hidden','false');});
document.querySelector('.close').addEventListener('click',closePanels);scrim.addEventListener('click',closePanels);
document.addEventListener('keydown',e=>{if(e.key==='Escape')closePanels();});
document.querySelector('.newsletter form').addEventListener('submit',e=>{e.preventDefault();const b=e.currentTarget.querySelector('button');b.textContent='¡LISTO! ✓';});
