const inventory=[
{group:'A',category:'Jordan Retro 9',name:'Air Jordan 9 Retro OG “Space Jam”',sizes:'36–38 / 40–42',price:1200,audience:'Unisex',image:'real/jordan-9.webp',source:'https://www.nike.com/mx/launch/t/air-jordan-9-retro-og-white-and-black'},
{group:'A',category:'Jordan Retro 3',name:'Air Jordan 3 Green / White / Red',sizes:'36–41',price:790,audience:'Unisex',image:'galleries/2-1.jpg',source:'https://www.nike.com/launch/t/air-jordan-3-hall-of-fame'},
{group:'A',category:'Jordan Hybrid / Otros',name:'Jordan Max Aura Black / Black / Gym Red',sizes:'39–42',price:685,audience:'Hombre',image:'products/max-aura-black-gym-red.jpg',source:'https://novelship.com/air-jordan-max-aura-black-infrared'},
{group:'A',category:'Nike Air Max',name:'Nike Air Max 95 White / Pink / Brown',sizes:'37–39',price:695,audience:'Mujer',image:'real/air-max-95.webp',source:'https://stockx.com/es-us/nike-air-max-95-cuban-link-velvet-brown-w'},
{group:'A',category:'Nike Flight Legacy',name:'Nike Flight Legacy Black / White',sizes:'39–41',price:500,audience:'Hombre',image:'real/flight-legacy.webp',source:'https://stockx.com/nike-flight-legacy-black-white'},
{group:'A',category:'Nike Air Max',name:'Nike Air Max Command Premium Light Taupe',sizes:'40–42',price:695,audience:'Hombre',image:'products/air-max-command-hq.png',source:'https://www.nike.com/jp/en/t/air-max-command-womens-shoes-JfvPvR'},
{group:'A',category:'Nike Air Max',name:'Nike Air Max Correlate Black / White / Grey',sizes:'36–41',price:450,audience:'Unisex',image:'products/air-max-correlate-black-grey.png',source:'https://www.nike.com/il/t/air-max-correlate-shoes-sZmWR6'},
{group:'B',category:'Jordan Hybrid / Otros',name:'Jordan Son of Mars Low White / Red / Black',sizes:'39–41',price:700,audience:'Hombre',image:'real/son-of-mars.webp',source:'https://www.shopwss.com/products/580603_101'},
{group:'B',category:'Nike Air Force 1',name:'Nike Air Force 1 ’07 Black / White / Orange Peel',sizes:'36–38 / 39–42',price:584,audience:'Unisex',image:'products/air-force-1-orange-peel.png',source:'https://www.nike.com/es/t/air-force-1-07-zapatillas-hombre-CcXoUHU9/IX6731-010'},
{group:'B',category:'Nike Air Force 1',name:'Nike Air Force 1 ’07 WNBA 30th Anniversary',sizes:'36–40',price:595,audience:'Unisex',image:'products/air-force-1-wnba.png',source:'https://www.nike.com/w/complete-the-wnba-fan-look-shoes-4cbgmzom6bzy7ok'},
{group:'B',category:'Nike Air Force 1',name:'Nike Air Force 1 ’07 LV8 “Mexico”',sizes:'39–41',price:595,audience:'Hombre',image:'products/air-force-1-mexico.png',source:'https://www.nike.com/mx/t/tenis-para-hombre-nike-air-force-1-07-lv8-mkYmss6V'},
{group:'B',category:'Nike Diamond / DT / Griffey',name:'Nike Air Griffey Max 1',sizes:'39–42',price:650,audience:'Hombre',image:'real/griffey-max-1.webp',source:'https://www.shiekh.com/nike-air-griffey-max-1-white-black-fresh-water.html'},
{group:'B',category:'Air Jordan 1 Low',name:'Air Jordan 1 Low Summit White / Black',sizes:'36–42',price:584,audience:'Unisex',image:'products/jordan-1-low-summit-white.png',source:'https://www.nike.com/mx/w/air-jordan-1-low-260d2z37eefz4foky'},
{group:'B',category:'Nike Air Force 1',name:'Nike Air Force 1 Blanco / Negro',sizes:'37–40',price:413,audience:'Mujer',image:'products/air-force-1-white-black.jpeg',source:'https://www.nike.com/mx/w/air-force-1-1ef98z2eqihz5sj3yzom6b'},
{group:'C',category:'Jordan Retro 4',name:'Air Jordan 4 x J Balvin “Amazonas”',sizes:'40–42',price:1300,audience:'Hombre',image:'real/jordan-4-amazonas.webp',source:'https://www.nike.com/mx/launch/t/air-jordan-4-j-balvin-amazonas'},
{group:'C',category:'Jordan Retro 1',name:'Air Jordan 1 High OG “Shattered Backboard”',sizes:'39–42',price:740,audience:'Hombre',image:'products/jordan-1-shattered-backboard.webp',source:'https://www.nike.com/mx/w/air-jordan-1-zapatillas-aj85gzy7ok'},
{group:'C',category:'Jordan Retro 4',name:'Air Jordan 4 Retro “Tour Yellow”',sizes:'36–38 / 40–42',price:1100,audience:'Unisex',image:'products/jordan-4-tour-yellow.png',source:'https://www.nike.com/mx/w/jordan-jordan-4-37eefz6ymx6zcsxjzy7ok'},
{group:'C',category:'Jordan Hybrid / Otros',name:'Jordan Max Aura Black / White',sizes:'39–42',price:685,audience:'Hombre',image:'products/max-aura-black-white.png',source:'https://novelship.com/air-jordan-max-aura-black-infrared'},
{group:'C',category:'Jordan Retro 1',name:'Air Jordan 1 Mid SE Black / Gold / Pink',sizes:'35–38',price:514,audience:'Mujer',image:'products/jordan-1-mid-pinksicle.jpg',source:'https://www.nike.com/mx/w/air-jordan-1-zapatillas-aj85gzy7ok'},
{group:'C',category:'Jordan Retro 3',name:'Air Jordan 3 Retro GS “Spring Flowers”',sizes:'35–39',price:617,audience:'Mujer',image:'products/jordan-3-spring-flowers.png',source:'https://www.nike.com/mx/w/jordan-calzado-37eefz98pddzj5jwzy7ok'},
{group:'C',category:'Nike Air Max',name:'Nike Air Max Correlate White / New Green / Bright Mango / Black',sizes:'35–38',price:583,audience:'Mujer',image:'products/air-max-correlate-mango.png',source:'https://www.nike.com/il/t/air-max-correlate-shoes-sZmWR6'},
{group:'D',category:'Jordan 6 Rings',name:'Jordan 6 Rings White / University Red / Black',sizes:'36–38 / 39–42',price:686,audience:'Unisex',image:'real/jordan-6-rings.webp',source:'https://www.shoepalace.com/products/jordan-322992-164-6-rings-mens-basketball-shoes-white-varsity-red-black'},
{group:'D',category:'Nike Diamond / DT / Griffey',name:'Nike Air Diamond Turf II',sizes:'36–38 / 39–42',price:583,audience:'Unisex',image:'real/diamond-turf.webp',source:'https://www.dtlr.com/products/nike-air-diamond-turf-ii-prime-red-mf-red-hq2631-600'},
{group:'D',category:'Nike Diamond / DT / Griffey',name:'Nike Air DT Max ’96 Low White / Metallic',sizes:'36–42',price:686,audience:'Unisex',image:'products/air-dt-max-96-low.webp',source:'https://www.nike.com/mx/w/calzado-1v79xz3r09wz9hh0lzy7ok'},
{group:'D',category:'Nike Basketball / Performance',name:'Nike Zoom LeBron NXXT Gen “Black Wolf Grey”',sizes:'40 / 40.5',price:630,audience:'Hombre',image:'galleries/25-1.png',source:'https://www.nike.com/t/lebron-nxxt-gen-basketball-shoes-55g4w1/DR8784-004'},
{group:'D',category:'Jordan Hybrid / Otros',name:'Air Jordan Access “Black Gym Red”',sizes:'40–42',price:583,audience:'Hombre',image:'real/jordan-access.webp',source:'https://item.rakuten.co.jp/limited-edt/ar3762-001/'},
{group:'D',category:'Nike Air Force 1',name:'Nike Air Force 1 ’07 Light British Tan / Sail / Hemp / Metallic Gold',sizes:'36–39',price:685,audience:'Mujer',image:'products/air-force-1-light-british-tan.webp',source:'https://www.nike.com/mx/w/air-force-1-1ef98z2eqihz5sj3yzom6b'},
{group:'D',category:'Nike Air Max',name:'Nike Air Max Bolt',sizes:'36–39',price:411,audience:'Mujer',image:'products/air-max-bolt.png',source:'https://www.nike.com/mx/w/calzado-1v79xz3r09wz9hh0lzy7ok'},
{group:'E',category:'Jordan Hybrid / Otros',name:'Jordan Lift Off White / Black / Wolf Grey',sizes:'40–42',price:650,audience:'Hombre',image:'real/jordan-lift-off.webp',source:'https://stockx.com/air-jordan-lift-off-white'},
{group:'E',category:'Jordan Retro 3',name:'Air Jordan 3 “Pure Money” White / Metallic Silver',sizes:'36–40',price:650,audience:'Unisex',image:'products/jordan-3-pure-money.webp',source:'https://www.nike.com/mx/w/jordan-calzado-37eefz98pddzj5jwzy7ok'},
{group:'E',category:'Air Jordan 1 Low',name:'Air Jordan 1 Low “Shattered Backboard Alternate”',sizes:'36–41',price:584,audience:'Unisex',image:'galleries/31-1.webp',source:'https://www.topsandbottomsusa.com/products/jordan-mens-air-jordan-1-low-shattered-backboard-alternate-shoes-553558-081'},
{group:'E',category:'Air Jordan 1 Low',name:'Air Jordan 1 Low “Inner Beast”',sizes:'35–37',price:514,audience:'Mujer',image:'products/jordan-1-inner-beast.png',source:'https://www.nike.com/mx/w/air-jordan-1-low-260d2z37eefz4foky'},
{group:'E',category:'Nike Basketball',name:'Nike LeBron Witness 9',sizes:'40–41',price:360,audience:'Hombre',image:'galleries/33-1.png',source:'https://www.nike.com/t/lebron-witness-9-basketball-shoes-h9SkAFPT'},
{group:'E',category:'Nike Air Force 1',name:'Nike Air Force 1 Rust Pink / Metallic Red',sizes:'36–38',price:446,audience:'Mujer',image:'products/air-force-1-rust-pink.webp',source:'https://www.nike.com/w/complete-the-wnba-fan-look-shoes-4cbgmzom6bzy7ok'},
{group:'E',category:'Nike Shox',name:'Nike Shox R4 College Grey / Volt',sizes:'35–38',price:514,audience:'Unisex',image:'products/shox-r4-college-grey.jpg',source:'https://www.nike.com/mx/w/calzado-1v79xz3r09wz9hh0lzy7ok'},
{group:'F',category:'Jordan Retro 5',name:'Halloween',sizes:'36–38 / 39–41',price:null,audience:'Unisex',image:'',sku:'HQ7980-001',source:'http://nike.com.pe/air-jordan-5-retro-haloween-zapatillas-para-hombre/hq7978-001/11112211015.html',note:'No tomar en cuenta la última imagen. Poner fondo blanco.'},
{group:'F',category:'Jordan Retro 4',name:'Flight Club',sizes:'36–38 / 40–43',price:null,audience:'Unisex',image:'',sku:'IM4026-100',source:'https://www.ebay.com/itm/287072006055',note:'No tomar en cuenta las últimas 4 imágenes.'},
{group:'F',category:'Jordan Retro 4',name:'She’s A Star',sizes:'36–37.5 / 36–38',price:null,audience:'Mujer',image:'',sku:'IO2829-600',source:'https://thesolesupplier.co.uk/release-dates/nike/air-jordan-4/air-jordan-4-retro-gs-shes-a-star/',note:''},
{group:'F',category:'Jordan 1',name:'Air Jordan 1 Mid SE Black / Opti Yellow / Silver',sizes:'36–38',price:null,audience:'Mujer',image:'',sku:'IV6811-001',source:'https://www.bbbranded.com/products/y-air-jordan-1-mid-se-iv6811-001',note:''},
{group:'F',category:'Jordan Hybrid / Otros',name:'Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black',sizes:'39–41',price:null,audience:'Hombre',image:'',sku:'IR0519-600',source:'https://www.nike.com.pe/air-jordan-4-retro-zapatillas-para-hombre/fq8138-600/11084881021.html',note:''},
{group:'F',category:'Air Jordan 1 Low',name:'Retro Low OG “Banned”',sizes:'36–38 / 37–38',price:null,audience:'Unisex',image:'',sku:'IW6277-001',source:'https://www.shiekh.com/jordan-grade-school-air-jordan-1-low-og-black-red-iw6277-001.html',note:''},
{group:'F',category:'Jordan Hybrid / Otros',name:'Jordan Son Of Mars Low Black / University Red',sizes:'39–42',price:null,audience:'Hombre',image:'',sku:'IR0519-003',source:'https://www.kickscrew.com/products/gs-air-jordan-son-of-mars-low-black-university-red-ir0519-003',note:''},
{group:'G',category:'Jordan Hybrid / Otros',name:'Jordan Max Aura Cool Grey / Gym Red / Black / White',sizes:'38–40',price:null,audience:'Hombre',image:'',sku:'AQ9214-012',source:'https://zapatos.es/p/zapatos-nike-jordan-max-aura-gs-aq9214-012-cool-grey-gym-red-black-white',note:''},
{group:'G',category:'Nike Force 1',name:'Nike Force 1 ’07 Premium Flowers',sizes:'36–39',price:null,audience:'Mujer',image:'',sku:'IB6644-001',source:'https://skstore.eu/en/nike-air-force-1-07-premium-black-shoes.html',note:''},
{group:'G',category:'Nike Force 1',name:'Obsidiana / Azul Difuso / Perla Suave / Aluminio',sizes:'36–39',price:null,audience:'Mujer',image:'',sku:'IM6969-451',source:'https://www.nike.com/us/es/t/tenis-para-ninos-grandes-nike-air-force-1-3JNSvS/IM6969-451',note:'Poner fondo blanco.'}
];
// Códigos, enlaces y observaciones tomados exclusivamente de SNKRS (1).xlsx.
const spreadsheetMetadata=[
  ['IX6180-100','https://samtabak.com/products/gs-air-jordan-9-retro-og-space-jam-ix6180-100',''],
  ['IO2076-100','https://samtabak.com/products/gs-air-jordan-3-retro-play-your-way-io2076-100',''],
  ['AQ9214-006','https://novelship.com/es-us/air-jordan-max-aura-black-gym-red-gs',''],
  ['HF7054-012','https://www.footy.com/p/nike-air-max-95-older-kids-shoes-grey/694a2a0f4f62009b36685a23/',''],
  ['BQ4212-002','https://www.goat.com/sneakers/flight-legacy-black-white-bq4212-002',''],
  ['694862-200','https://www.n-sport.net/lifestyle-patike/muske-patike-nike-air-max-command-20.html',''],
  ['511416-011','https://articulo.mercadolibre.com.pe/MPE-655050748-zapatillas-nike-air-max-correlate-black-white-511416-011--_JM',''],
  ['IR0519-101','https://www.nike.com.pe/jordan-son-of-mars-low-zapatillas-para-hombre/580603-101/11084738017.html','No tomar en cuenta la séptima ni la última imagen.'],
  ['IQ0205-100','https://www.nike.com/us/es/t/tenis-para-ninos-grandes-nike-air-force-1-XfzEDzQ5/IQ0205-100','Poner fondo blanco.'],
  ['IR1968-133','https://www.kickscrew.com/products/wmns-nike-air-force-1-low-wnba-30th-anniversary-ir1968-133',''],
  ['IR5896-030','https://www.headquarterstore.com/es/products/nike-air-force-1-mexico-ir5896-030',''],
  ['IV6222-410','https://reynoldsandsons.com/products/nike-air-griffey-max-1-hbcu-swingman-gs-iv6222-410',''],
  ['553560-045','https://simple.ripley.com.pe/zapatillas-nike-air-jordan-1-low-553560-045-ninos-pmp20001533854',''],
  ['CT3839-100','https://simple.ripley.com.pe/zapatillas-hombre-nike-urbanas-blanco-dh2987-101-court-vis-2025280147540','No tomar en cuenta las dos últimas imágenes.'],
  ['IW2872-700','https://cityjeans.com/products/mens-air-jordan-4-retro-x-j-balvin-amazonas-lemonade-multicolor-iw2872-700-iw2872-700',''],
  ['FD1437-008','https://www.futurevisions.pe/futurevisions-pe/product/80200745/zap-dz5485-201-air-jordan-1-re/80200765','No tomar en cuenta la segunda ni la última imagen.'],
  ['408452-102','https://cityjeans.com/products/big-kids-air-jordan-4-retro-tour-yellow-white-tour-yellow-dark-blue-grey-black-408452-102-408452-102',''],
  ['AQ9214-011','https://www.zakcret.gr/en/jordan-max-aura-aq9214-011-leyko-mayro',''],
  ['II1254-001','https://thesolesupplier.co.uk/release-dates/nike/air-jordan-1/air-jordan-1-mid-se-gs-world-tour-multi/',''],
  ['II0599-600','https://www.sneakersnstuff.com/products/jordan-air-jordan-3-retro-spring-flowers-big-kids-gs-ii0599-600','Poner fondo blanco.'],
  ['511417-136','https://www.nike.com.pe/nike-air-max-correlate-zapatillas-para-mujer/511417-136/10677147014.html','Poner fondo blanco.'],
  ['323419-164','https://www.kickscrew.com/products/gs-air-jordan-6-rings-white-varsity-red-black-323419-164',''],
  ['IR4727-100','https://www.bbbranded.com/products/y-nike-air-diamond-turf-ii-ir4727-100',''],
  ['IR4714-100','https://www.shiekh.com/nike-grade-school-air-dt-max-96-low-white-metallic-silver-white-ir4714-100.html','Poner fondo blanco. No tomar en cuenta la última imagen.'],
  ['DR8784-005','https://articulo.mercadolibre.com.pe/MPE-655104518-zapatillas-nike-zoom-lebron-nxxt-gen-urbano-dr8784-005--_JM','Poner fondo blanco.'],
  ['AR3762-001','https://tiendamia.com.pe/p/amz/b07slnlp6g/nike-zapatillas-hombre-air-force-1-07-lv8-zapatos',''],
  ['IV5197-201','http://bbbranded.com/products/w-nike-air-force-1-07-iv5197-201',''],
  ['CU4152-101','https://articulo.mercadolibre.com.pe/MPE-621254943-zapatilla-nike-air-max-bolt-urbano-original-cu4152101--_JM','Poner fondo blanco.'],
  ['AR4430-101','https://pe.ebay.com/b/Jordan-Lift-Off-White-Grey/15709/bn_7117641379',''],
  ['DM0967-111','https://noirfonce.eu/es-es/products/air-jordan-3-retro-pure-money-dm0967-111',''],
  ['553560-081','https://www.shiekh.com/jordan-grade-school-air-jordan-1-low-black-starfish-white-sail-553560-081.html',''],
  ['HV4775-001','https://www.kickscrew.com/products/gs-air-jordan-1-low-inner-beast-hv4775-001',''],
  ['HQ8034-700','https://www.nike.com.pe/lebron-witness%C2%A09-zapatillas-de-basquet/hq8034-700/11058724019.html','Poner fondo blanco.'],
  ['IQ0213-685','https://www.nike.com/t/air-force-1-big-kids-shoes-XfzEDzQ5/IQ0213-685','Poner fondo blanco.'],
  ['CW2626-008','https://www.footlocker.com/product/~/W2626008.html','Poner fondo blanco.']
];
spreadsheetMetadata.forEach(([sku,source,note],index)=>Object.assign(inventory[index],{sku,source,note}));
// La tarjeta y la ficha comienzan con la misma primera toma del modelo.
const cardPrimaryImages={0:'galleries/1-1.jpg',1:'galleries/2-1.jpg',7:'galleries/8-1.webp',11:'galleries/12-1.jpg',14:'galleries/15-1.jpg',21:'galleries/22-1.webp',22:'products/diamond-turf-hq.png',24:'galleries/25-1.png',25:'galleries/26-1.webp',30:'real/aj1-low-shattered.webp',32:'galleries/33-1.png'};
Object.entries(cardPrimaryImages).forEach(([index,image])=>{inventory[Number(index)].image=image});
// Todas las tarjetas cargan una versión de alta resolución del mismo ángulo principal.
inventory.forEach((product,index)=>{product.image=`hq/product-${index}.webp`});
inventory[7].image='real/son-of-mars.webp';
inventory[2].image='products/max-aura-official-1.jpg';
inventory[16].image='products/tour-yellow-main.webp';
inventory[4].image='products/flight-legacy-2.jpg';
inventory[6].image='products/air-max-correlate-1.png';
inventory[7].image='products/son-of-mars-1.png';
inventory[1].image='generated/jordan-3-green-white-red/angle-1.png';
// Todas las tarjetas del catálogo usan la primera toma generada sobre fondo blanco.
for(let index=0;index<inventory.length;index+=1){inventory[index].image=`generated/product-${index}/angle-1.png`;}

// Fotografías originales recibidas. La primera toma de cada conjunto se usa
// también como imagen principal en las tarjetas del catálogo.
const catalogPhotos={
  0:['IMG_0046.jpeg','IMG_0047.jpeg','IMG_0048.jpeg','IMG_0049.jpeg','IMG_0051.jpeg','IMG_0052.jpeg'],
  1:['IMG_0053.jpeg','IMG_0054.jpeg','IMG_0055.jpeg','IMG_0056.jpeg','IMG_0057.jpeg'],
  2:['IMG_0058.jpeg','IMG_0059.jpeg','IMG_0060.jpeg','IMG_0061.jpeg','IMG_0062.jpeg'],
  3:['IMG_0063.jpeg','IMG_0064.jpeg','IMG_0065.jpeg','IMG_0066.jpeg','IMG_0067.jpeg'],
  4:['IMG_0068.jpeg','IMG_0069.jpeg','IMG_0070.jpeg','IMG_0071.jpeg','IMG_0072.jpeg'],
  5:['IMG_0073.jpeg','IMG_0074.jpeg','IMG_0075.jpeg','IMG_0076.jpeg','IMG_0077.jpeg','IMG_0078.jpeg'],
  6:['IMG_0079.jpeg','IMG_0080.jpeg','IMG_0081.jpeg','IMG_0082.jpeg','IMG_0083.jpeg'],
  7:['IMG_0084.jpeg','IMG_0085.jpeg','IMG_0086.jpeg','IMG_0087.jpeg','IMG_0088.jpeg'],
  8:['IMG_0089.jpeg','IMG_0090.jpeg','IMG_0091.jpeg','IMG_0092.jpeg','IMG_0093.jpeg'],
  9:['IMG_0094.jpeg','IMG_0095.jpeg','IMG_0096.jpeg','IMG_0097.jpeg','IMG_0098.jpeg'],
  10:['IMG_0099.jpeg','IMG_0100.jpeg','IMG_0101.jpeg','IMG_0102.jpeg','IMG_0103.jpeg'],
  11:['IMG_0104.jpeg','IMG_0105.jpeg','IMG_0106.jpeg','IMG_0107.jpeg','IMG_0108.jpeg','IMG_0109.jpeg'],
  12:['IMG_0110.jpeg','IMG_0111.jpeg','IMG_0112.jpeg','IMG_0113.jpeg','IMG_0114.jpeg'],
  13:['IMG_0115.jpeg','IMG_0116.jpeg','IMG_0117.jpeg','IMG_0118.jpeg','IMG_0119.jpeg'],
  14:['IMG_0120.jpeg','IMG_0121.jpeg','IMG_0122.jpeg','IMG_0123.jpeg','IMG_0124.jpeg','IMG_0125.jpeg'],
  15:['IMG_0126.jpeg','IMG_0127.jpeg','IMG_0128.jpeg','IMG_0129.jpeg','IMG_0130.jpeg','IMG_0131.jpeg'],
  16:['IMG_0132.jpeg','IMG_0133.jpeg','IMG_0134.jpeg','IMG_0135.jpeg','IMG_0136.jpeg','IMG_0137.jpeg'],
  17:['IMG_0138.jpeg','IMG_0139.jpeg','IMG_0140.jpeg','IMG_0141.jpeg','IMG_0142.jpeg'],
  18:['IMG_0143.jpeg','IMG_0144.jpeg','IMG_0145.jpeg','IMG_0146.jpeg','IMG_0147.jpeg'],
  19:['IMG_0148.jpeg','IMG_0149.jpeg','IMG_0150.jpeg','IMG_0151.jpeg'],
  20:['IMG_0153.jpeg','IMG_0154.jpeg','IMG_0155.jpeg','IMG_0156.jpeg','IMG_0157.jpeg','IMG_0158.jpeg'],
  21:['IMG_0159.jpeg','IMG_0160.jpeg','IMG_0161.jpeg','IMG_0162.jpeg','IMG_0163.jpeg','IMG_0164.jpeg'],
  22:['IMG_0165.jpeg','IMG_0166.jpeg','IMG_0167.jpeg','IMG_0168.jpeg','IMG_0169.jpeg'],
  23:['IMG_0170.jpeg','IMG_0171.jpeg','IMG_0172.jpeg','IMG_0173.jpeg','IMG_0174.jpeg'],
  24:['IMG_0175.jpeg','IMG_0176.jpeg','IMG_0177.jpeg','IMG_0178.jpeg','IMG_0179.jpeg','IMG_0180.jpeg'],
  25:['IMG_0181.jpeg','IMG_0182.jpeg','IMG_0183.jpeg','IMG_0184.jpeg','IMG_0185.jpeg'],
  26:['IMG_0186.jpeg','IMG_0187.jpeg','IMG_0188.jpeg','IMG_0189.jpeg','IMG_0190.jpeg'],
  27:['IMG_0191.jpeg','IMG_0192.jpeg','IMG_0193.jpeg','IMG_0194.jpeg','IMG_0195.jpeg'],
  28:['IMG_0196.jpeg','IMG_0197.jpeg','IMG_0198.jpeg','IMG_0199.jpeg','IMG_0200.jpeg'],
  29:['IMG_0201.jpeg','IMG_0202.jpeg','IMG_0203.jpeg','IMG_0204.jpeg','IMG_0205.jpeg'],
  30:['IMG_0206.jpeg','IMG_0207.jpeg','IMG_0208.jpeg','IMG_0209.jpeg','IMG_0210.jpeg'],
  31:['IMG_0211.jpeg','IMG_0212.jpeg','IMG_0213.jpeg','IMG_0214.jpeg','IMG_0215.jpeg'],
  32:['IMG_0216.jpeg','IMG_0217.jpeg','IMG_0218.jpeg','IMG_0219.jpeg','IMG_0220.jpeg'],
  33:['IMG_0221.jpeg','IMG_0222.jpeg','IMG_0223.jpeg','IMG_0224.jpeg','IMG_0225.jpeg'],
  34:['IMG_0226.jpeg','IMG_0227.jpeg','IMG_0228.jpeg','IMG_0229.jpeg','IMG_0230.jpeg'],
  35:['IMG_0231.jpeg','IMG_0232.jpeg','IMG_0233.jpeg','IMG_0234.jpeg','IMG_0235.jpeg','IMG_0236.jpeg'],
  36:['IMG_0237.jpeg','IMG_0238.jpeg','IMG_0239.jpeg','IMG_0240.jpeg','IMG_0241.jpeg'],
  37:['IMG_0242.jpeg','IMG_0243.jpeg','IMG_0244.jpeg','IMG_0245.jpeg','IMG_0246.jpeg','IMG_0247.jpeg'],
  38:['IMG_0248.jpeg','IMG_0249.jpeg','IMG_0250.jpeg','IMG_0251.jpeg','IMG_0252.jpeg'],
  39:['IMG_0253.jpeg','IMG_0254.jpeg','IMG_0255.jpeg','IMG_0256.jpeg','IMG_0257.jpeg','IMG_0258.jpeg'],
  40:['IMG_0259.jpeg','IMG_0260.jpeg','IMG_0261.jpeg','IMG_0262.jpeg','IMG_0263.jpeg','IMG_0264.jpeg'],
  41:['IMG_0265.jpeg','IMG_0266.jpeg','IMG_0267.jpeg','IMG_0268.jpeg','IMG_0269.jpeg'],
  42:['IMG_0270.jpeg','IMG_0272.jpeg','IMG_0273.jpeg','IMG_0274.jpeg','IMG_0275.jpeg'],
  43:['IMG_0276.jpeg','IMG_0277.jpeg','IMG_0278.jpeg','IMG_0279.jpeg','IMG_0280.jpeg'],
  44:['IMG_0281.jpeg','IMG_0282.jpeg','IMG_0283.jpeg','IMG_0284.jpeg','IMG_0285.jpeg','IMG_0286.jpeg']
};
const catalogPhotoPath=photo=>{
  const number=Number((photo.match(/IMG_(\d{4})/)||[])[1]);
  const group=number<=83?'A':number<=119?'B':number<=158?'C':number<=195?'D':number<=230?'E':number<=269?'F':'G';
  return `galleries/Grupo ${group}/${photo}`;
};
Object.entries(catalogPhotos).forEach(([index,photos])=>{
  inventory[Number(index)].image=catalogPhotoPath(photos[0]);
});
if(typeof sourceLinkPhotos!=='undefined'){
  Object.entries(sourceLinkPhotos).forEach(([index,photos])=>{
    if(photos.length)inventory[Number(index)].image=photos[0];
  });
}
const sets={default:inventory,men:inventory.filter(p=>p.audience!=='Mujer'),women:inventory.filter(p=>p.audience!=='Hombre'),kids:inventory.filter(p=>p.name.includes('GS')),sale:inventory.filter(p=>p.price!==null).sort((a,b)=>a.price-b.price).slice(0,8)};
const money=value=>value===null?'CONSULTAR':`S/ ${value.toLocaleString('es-PE')}`;
const detailUrl=p=>`producto.html?id=${inventory.indexOf(p)}`;
document.dispatchEvent(new Event('inventoryready'));
const grid=document.querySelector('[data-products]');
if(grid){const key=grid.dataset.products||'default';const products=sets[key]||sets.default;const count=key==='default'?document.querySelector('.shop-section .title-row h1'):document.querySelector('.shop-section .title-row p');const query=(new URLSearchParams(location.search).get('q')||'').trim();const render=items=>{if(count)count.textContent=`${items.length} MODELOS`;grid.innerHTML=items.length?items.map((p,i)=>`<article class="product" data-category="${p.category}"><a class="product-media shoe" href="${detailUrl(p)}"><img src="assets/${p.image}?v=20261102-clean" alt="${p.name}" loading="lazy"><span class="pill">${i<4?'DESTACADO':p.category.toUpperCase()}</span><span class="audience-pill">${p.audience==='Unisex'?'UNISEX':`PARA ${p.audience.toUpperCase()}`}</span><span class="source-badge">VER DETALLES →</span></a><button class="heart" aria-label="Guardar producto" style="border:0;background:none">♡</button><h3><a href="${detailUrl(p)}">${p.name}</a></h3><p>${p.category} · ${p.audience}</p><p class="product-sizes">Tallas: ${p.sizes}</p><strong>${money(p.price)}</strong></article>`).join(''):'<p class="search-empty">No encontramos modelos con esa búsqueda. Prueba con Jordan, Nike, Air Max o una talla.</p>';document.querySelectorAll('.heart').forEach(btn=>btn.addEventListener('click',()=>{const toast=document.querySelector('.toast');toast.classList.add('show');setTimeout(()=>toast.classList.remove('show'),1800)}))};const normalized=value=>value.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();if(query){const terms=normalized(query).split(/\s+/).filter(Boolean);const found=products.filter(product=>terms.every(term=>normalized(`${product.name} ${product.category} ${product.audience} ${product.sizes}`).includes(term)));const row=document.querySelector('.shop-section .title-row');if(row){const note=document.createElement('p');note.className='search-result-note';note.innerHTML=`Resultados para <strong>“${query.replace(/[<>&]/g,char=>({'<':'&lt;','>':'&gt;','&':'&amp;'}[char]))}”</strong>`;row.after(note)}render(found)}else render(products);document.querySelectorAll('.filter-bar button[data-filter]').forEach(btn=>btn.addEventListener('click',()=>{btn.parentElement.querySelectorAll('button').forEach(x=>x.classList.remove('active'));btn.classList.add('active');const filter=btn.dataset.filter;const matches=p=>filter==='Air Jordan'?p.category.includes('Jordan'):p.category.includes(filter);render(filter==='all'?products:products.filter(matches))}))}
