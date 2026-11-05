import fs from 'node:fs/promises';
import path from 'node:path';
import vm from 'node:vm';
import {createHash} from 'node:crypto';

const root=path.resolve(process.cwd());
const productsPath=path.join(root,'dist','products.js');
const assetRoot=path.join(root,'dist','assets','source-links');
const userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130 Safari/537.36';
const start=Math.max(0,Number(process.argv.find(value=>value.startsWith('--start='))?.split('=')[1]||0));
const end=Math.min(45,Number(process.argv.find(value=>value.startsWith('--end='))?.split('=')[1]||45));

const context={
  document:{dispatchEvent(){},querySelector(){return null},querySelectorAll(){return []}},
  Event:function Event(){}, URLSearchParams, location:{search:''}
};
vm.createContext(context);
vm.runInContext(`${await fs.readFile(productsPath,'utf8')};this.catalogItems=inventory;`,context);
const products=context.catalogItems.map((product,index)=>({index,...product}));
const selectedProducts=products.slice(start,end);

const attributes=tag=>Object.fromEntries([...tag.matchAll(/([\w:-]+)\s*=\s*(["'])(.*?)\2/g)].map(([,name,,value])=>[name.toLowerCase(),value]));
const absolute=(value,base)=>{try{return new URL(value.replaceAll('&amp;','&'),base).href}catch{return null}};
const useful=url=>url&&/^https?:/i.test(url)&&!/\.(svg|gif)(?:\?|$)/i.test(url)&&!/logo|icon|favicon|placeholder/i.test(url);
const unique=items=>[...new Set(items.filter(useful))];

function imageUrls(html,source){
  const meta=[];
  for(const tag of html.match(/<meta\b[^>]*>/gi)||[]){
    const attr=attributes(tag);
    const key=(attr.property||attr.name||'').toLowerCase();
    if(['og:image','og:image:secure_url','twitter:image','twitter:image:src'].includes(key))meta.push(absolute(attr.content,source));
  }
  const schema=[];
  for(const script of html.match(/<script[^>]*type=["']application\/ld\+json["'][^>]*>[\s\S]*?<\/script>/gi)||[]){
    const text=script.replace(/^.*?>/,'').replace(/<\/script>$/i,'').trim();
    try{
      const visit=value=>{
        if(Array.isArray(value))return value.forEach(visit);
        if(value&&typeof value==='object'){
          const images=value.image||value.images;
          if(Array.isArray(images))images.forEach(image=>schema.push(absolute(typeof image==='string'?image:image?.url,source)));
          else if(images)schema.push(absolute(typeof images==='string'?images:images?.url,source));
          if(value['@graph'])visit(value['@graph']);
        }
      };
      visit(JSON.parse(text));
    }catch{}
  }
  const pageImages=[];
  for(const tag of html.match(/<(?:img|source)\b[^>]*>/gi)||[]){
    const attr=attributes(tag);
    for(const candidate of [attr['data-zoom-image'],attr['data-src'],attr.src,attr.srcset?.split(',').at(-1)?.trim().split(/\s+/)[0]])pageImages.push(absolute(candidate,source));
  }
  const productImages=unique([...meta,...schema]);
  // Solo usamos imágenes declaradas por la ficha del producto. Si la página
  // no las declara, recurrimos a sus imágenes visibles como último recurso.
  return (productImages.length?productImages:unique(pageImages)).slice(0,8);
}

function exclusions(note,count){
  const omit=new Set();
  const lower=(note||'').toLowerCase();
  if(lower.includes('séptima'))omit.add(6);
  if(lower.includes('segunda'))omit.add(1);
  if(lower.includes('última imagen'))omit.add(count-1);
  const match=lower.match(/últimas\s+(\d+)\s+imágenes/);
  if(match)for(let i=Math.max(0,count-Number(match[1]));i<count;i++)omit.add(i);
  if(lower.includes('dos últimas')){omit.add(count-1);omit.add(count-2)}
  return omit;
}

function extension(contentType,url){
  if(contentType.includes('png'))return 'png';
  if(contentType.includes('webp'))return 'webp';
  if(contentType.includes('avif'))return 'avif';
  const found=new URL(url).pathname.match(/\.(jpe?g|png|webp|avif)$/i)?.[1];
  return found?.replace('jpeg','jpg')||'jpg';
}

async function download(product){
  if(!product.source)return {index:product.index,sku:product.sku,status:'missing-source',images:[]};
  const response=await fetch(product.source,{headers:{'user-agent':userAgent,'accept':'text/html,application/xhtml+xml'}});
  if(!response.ok)throw new Error(`page ${response.status}`);
  const urls=imageUrls(await response.text(),response.url);
  const omit=exclusions(product.note,urls.length);
  const dir=path.join(assetRoot,product.sku||`product-${product.index}`);
  await fs.rm(dir,{recursive:true,force:true});
  await fs.mkdir(dir,{recursive:true});
  const images=[];
  const hashes=new Set();
  for(let position=0;position<urls.length;position++){
    if(omit.has(position))continue;
    try{
      const image=await fetch(urls[position],{headers:{'user-agent':userAgent,'referer':response.url,'accept':'image/avif,image/webp,image/apng,image/*,*/*;q=0.8'}});
      if(!image.ok)continue;
      const type=image.headers.get('content-type')||'';
      if(!type.startsWith('image/'))continue;
      const bytes=Buffer.from(await image.arrayBuffer());
      // Evita iconos, respuestas de error disfrazadas de imagen y duplicados.
      if(bytes.length<15_000)continue;
      const hash=createHash('sha256').update(bytes).digest('hex');
      if(hashes.has(hash))continue;
      hashes.add(hash);
      const file=`${String(images.length+1).padStart(2,'0')}.${extension(type,urls[position])}`;
      await fs.writeFile(path.join(dir,file),bytes);
      images.push(`source-links/${product.sku||`product-${product.index}`}/${file}`);
    }catch{}
  }
  return {index:product.index,sku:product.sku,status:images.length?'ok':'no-downloadable-images',images,source:response.url};
}

const results=[];
for(let offset=0;offset<selectedProducts.length;offset+=3){
  results.push(...await Promise.all(selectedProducts.slice(offset,offset+3).map(async product=>{
    try{return await download(product)}catch(error){return {index:product.index,sku:product.sku,status:`error: ${error.message}`,images:[]}}
  })));
}
results.sort((a,b)=>a.index-b.index);
const sourceMap={};
for(const product of products){
  const sku=product.sku||`product-${product.index}`;
  try{
    const files=(await fs.readdir(path.join(assetRoot,sku))).filter(file=>/\.(jpe?g|png|webp|avif)$/i.test(file)).sort();
    if(files.length)sourceMap[product.index]=files.map(file=>`source-links/${sku}/${file}`);
  }catch{}
}
await fs.writeFile(path.join(assetRoot,`manifest-${start}-${end}.json`),JSON.stringify(results,null,2));
await fs.writeFile(path.join(root,'dist','source-link-photos.js'),`// Generado desde los enlaces de SNKRS (1).xlsx.\nconst sourceLinkPhotos=${JSON.stringify(sourceMap,null,2)};\n`);
console.table(results.map(result=>({index:result.index+1,sku:result.sku,status:result.status,images:result.images.length})));
