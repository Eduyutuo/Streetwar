const galleries={"0":["galleries/1-1.jpg","galleries/1-2.jpg","galleries/1-3.jpg","galleries/1-4.jpg","galleries/1-5.jpg"],"1":["galleries/2-1.jpg","galleries/2-2.jpg","galleries/2-3.jpg","galleries/2-4.jpg","galleries/2-5.jpg","galleries/2-6.jpg"],"7":["galleries/8-1.webp","galleries/8-2.webp","galleries/8-3.webp","galleries/8-4.webp","galleries/8-5.webp","galleries/8-6.webp"],"11":["galleries/12-1.jpg","galleries/12-2.jpg","galleries/12-3.jpg","galleries/12-4.jpg","galleries/12-5.jpg","galleries/12-6.jpg"],"14":["galleries/15-1.jpg","galleries/15-2.jpg","galleries/15-3.jpg","galleries/15-4.jpg","galleries/15-5.jpg","galleries/15-6.jpg"],"21":["galleries/22-1.webp","galleries/22-2.webp","galleries/22-3.webp","galleries/22-4.webp","galleries/22-5.webp","galleries/22-6.webp"],"22":["products/diamond-turf-hq.png","galleries/23-2.webp","galleries/23-3.webp","galleries/23-4.jpeg","galleries/23-5.webp","galleries/23-6.webp"],"24":["galleries/25-1.png","galleries/25-2.png","galleries/25-3.png","galleries/25-4.png","galleries/25-5.png","galleries/25-6.png"],"25":["galleries/26-1.webp","galleries/26-2.jpg","galleries/26-3.webp","galleries/26-4.webp","galleries/26-5.png"],"32":["galleries/33-1.png","galleries/33-2.png","galleries/33-3.png","galleries/33-4.png"]};
galleries[16]=["products/tour-yellow-main.webp","products/tour-yellow-angle-2.jpg","products/tour-yellow-angle-3.jpg"];
galleries[2]=["products/max-aura-official-1.jpg","products/max-aura-official-2.jpg","products/max-aura-official-3.jpg","products/max-aura-official-4.jpg","products/max-aura-official-5.jpg"];
// La fuente de la galería 2 incluyó prendas ajenas al modelo; usamos la foto HQ del producto.
delete galleries[1];
// Cinco ángulos reales por modelo, sin prendas ni imágenes repetidas.
galleries[4]=["products/flight-legacy-2.jpg","products/flight-legacy-3.jpg","products/flight-legacy-4.jpg","products/flight-legacy-5.jpg","products/flight-legacy-1.jpg"];
galleries[6]=["products/air-max-correlate-1.png","products/air-max-correlate-2.png","products/air-max-correlate-3.png","products/air-max-correlate-4.png","products/air-max-correlate-5.png"];
galleries[7]=["products/son-of-mars-1.png","products/son-of-mars-2.png","products/son-of-mars-3.png","products/son-of-mars-4.png","products/son-of-mars-5.png"];
galleries[3]=["hq/product-3.webp","generated/air-max-95-pink-brown-angle-2.png"];
galleries[1]=["generated/jordan-3-green-white-red/angle-1.png","generated/jordan-3-green-white-red/angle-2.png","generated/jordan-3-green-white-red/angle-3.png","generated/jordan-3-green-white-red/angle-4.png","generated/jordan-3-green-white-red/angle-5.png"];
// Cinco ángulos distintos, generados desde la referencia de cada modelo y separados para la galería.
for(let index=0;index<inventory.length;index+=1){galleries[index]=Array.from({length:5},(_,angle)=>`generated/product-${index}/angle-${angle+1}.png`);}

// Tomas reales, en el orden de cada modelo recibido.
Object.entries(catalogPhotos).forEach(([index,photos])=>{
  galleries[Number(index)]=photos.map(photo=>`catalog-photos/${photo}`);
});
