(function() {
  const STORAGE_KEY = 'ritmo_catalog_lang';

  // Supported languages: 'en' and 'es'
  const translations = {
    es: {
      code: 'ES',
      currency: 'PEN',
      currencySymbol: 'S/',
      exchangeRate: 1, // 1 USD = 3.75 PEN approx
      promoBar: 'CATÁLOGO DE ZAPATILLAS ACTUALIZADO ✦ JORDAN Y NIKE',
      searchPlaceholder: 'BUSCAR EN EL CATÁLOGO',
      nav: {
        novedades: 'NOVEDADES',
        hombre: 'HOMBRE',
        mujer: 'MUJER',
        ninos: 'NIÑOS',
        marcas: 'MARCAS',
        ofertas: 'OFERTAS',
        lanzamientos: 'LANZAMIENTOS',
        editorial: 'EDITORIAL',
        tiendas: '⌖ TIENDAS'
      },
      filters: {
        all: 'VER TODO',
        exclusive: 'EXCLUSIVAS',
        kids: 'NIÑO',
        men: 'HOMBRE',
        women: 'MUJER',
        adult: 'ADULTO',
        accessories: 'ACCESORIOS · PRÓXIMAMENTE',
        shirts: 'POLOS · PRÓXIMAMENTE',
        airJordan: 'AIR JORDAN',
        airForce1: 'AIR FORCE 1',
        airMax: 'AIR MAX',
        basketball: 'BASKETBALL'
      },
      catalog: {
        title: 'CATÁLOGO',
        kicker: 'COLECCIÓN 2026 · EXCLUSIVAS',
        intro: 'Explora las siluetas exclusivas o encuentra calzado seleccionado para hombre y mujer.',
        countSuffix: 'MODELOS',
        featured: 'DESTACADO',
        forMen: 'PARA HOMBRE',
        forWomen: 'PARA MUJER',
        unisex: 'UNISEX',
        viewDetails: 'VER DETALLES →',
        emptySearch: 'No encontramos modelos con esa búsqueda. Prueba con Jordan, Nike, Air Max o una talla.',
        sizes: 'Tallas:',
        inquire: 'CONSULTAR',
        toast: 'AÑADIDO A TU LISTA ✓'
      },
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
        referentialImage: 'IMAGEN REFERENCIAL DEL MODELO',
        notes: [
          { num: '01', title: 'PRODUCTO', text: 'Zapatillas importadas seleccionadas para el catálogo Streetwar 2026.' },
          { num: '02', title: 'TALLAS', text: 'La disponibilidad se presenta en talla EU. Selecciona una talla antes de comprar.' },
          { num: '03', title: 'COMPRA DIRECTA', text: 'Tu pedido se envía a un asesor de Streetwar por WhatsApp con el modelo y la talla elegida.' }
        ]
      },
      footer: {
        store: 'TIENDA',
        help: 'AYUDA',
        shipping: 'Envíos y devoluciones',
        contact: 'Contacto',
        stores: 'Tiendas',
        copy: '© 2026 LIL DAVID / RITMO — CONCEPTO DE DEMOSTRACIÓN'
      },
      whatsapp: {
        support: 'SOPORTE WHATSAPP',
        usaLabel: 'USA (Drop & Direct)',
        peLabel: 'Perú (Local)',
        defaultMsg: 'Hola Streetwar, quiero consultar por una zapatilla.',
        orderMsg: (name, size, price, category) => 
          `Hola Streetwar, quiero comprar este modelo:\n\n*${name}*\n${size ? `Talla: *EU ${size}*` : 'Talla: *Por confirmar*'}\nPrecio: *${price}*\nCategoría: ${category}\n\n¿Está disponible?`
      }
    },
    en: {
      code: 'EN',
      currency: 'USD',
      currencySymbol: '$',
      exchangeRate: 0.27, // 1 PEN ≈ 0.27 USD
      promoBar: 'UPDATED SNEAKER CATALOG ✦ JORDAN & NIKE EXCLUSIVES',
      searchPlaceholder: 'SEARCH CATALOG',
      nav: {
        novedades: 'NEW RELEASES',
        hombre: 'MEN',
        mujer: 'WOMEN',
        ninos: 'KIDS',
        marcas: 'BRANDS',
        ofertas: 'SALE',
        lanzamientos: 'DROPS',
        editorial: 'LOOKBOOK',
        tiendas: '⌖ STORES'
      },
      filters: {
        all: 'VIEW ALL',
        exclusive: 'EXCLUSIVES',
        kids: 'KIDS',
        men: 'MEN',
        women: 'WOMEN',
        adult: 'ADULTS',
        accessories: 'ACCESSORIES · COMING SOON',
        shirts: 'TEES · COMING SOON',
        airJordan: 'AIR JORDAN',
        airForce1: 'AIR FORCE 1',
        airMax: 'AIR MAX',
        basketball: 'BASKETBALL'
      },
      catalog: {
        title: 'CATALOG',
        kicker: '2026 COLLECTION · EXCLUSIVES',
        intro: 'Explore exclusive streetwear silhouettes or find selected footwear for men and women.',
        countSuffix: 'MODELS',
        featured: 'FEATURED',
        forMen: 'MEN',
        forWomen: 'WOMEN',
        unisex: 'UNISEX',
        viewDetails: 'VIEW DETAILS →',
        emptySearch: 'No models found matching that search. Try Jordan, Nike, Air Max or a size.',
        sizes: 'Sizes:',
        inquire: 'INQUIRE',
        toast: 'ADDED TO YOUR LIST ✓'
      },
      detail: {
        breadcrumb: 'HOME / CATALOG / DETAIL',
        availableForOrder: 'Available for order',
        authTitle: 'STREETWAR',
        authText: 'Selected release for our 2026 catalog',
        audienceLabel: 'THIS MODEL IS',
        unisexSub: 'Designed for men & women',
        genderSub: 'According to Streetwar inventory',
        selectSize: 'SELECT YOUR SIZE',
        euSize: 'EU SIZE',
        sizesInInventory: 'Listed inventory sizes:',
        sizesPending: 'Sizes to be confirmed. Contact us to check availability.',
        btnSelectSize: 'SELECT A SIZE',
        btnInquire: 'CHECK AVAILABILITY',
        btnBuyWhatsApp: 'BUY VIA WHATSAPP · EU',
        whatsappNote: 'Choose Contact 1 (USA) or Contact 2 (PE) on the WhatsApp radar.',
        benefit1Title: 'Direct Support',
        benefit1Text: 'Confirm stock, shipping and payment with an advisor.',
        benefit2Title: 'Order Prepared',
        benefit2Text: 'We will send the model, price and selected size.',
        productDetails: 'PRODUCT DETAILS',
        brand: 'BRAND',
        silhouette: 'SILHOUETTE',
        model: 'MODEL',
        code: 'SKU / CODE',
        backToCatalog: '← BACK TO CATALOG',
        alsoLike: 'YOU MIGHT ALSO LIKE',
        moreLikeThis: 'MORE LIKE THIS',
        seeAll: 'VIEW ALL',
        viewCount: 'MODEL SHOTS',
        referentialImage: 'REFERENTIAL MODEL IMAGE',
        notes: [
          { num: '01', title: 'PRODUCT', text: 'Imported sneakers selected for the Streetwar 2026 catalog.' },
          { num: '02', title: 'SIZING', text: 'Availability is displayed in EU sizing. Please select a size before ordering.' },
          { num: '03', title: 'DIRECT ORDER', text: 'Your order connects directly to a Streetwar specialist via WhatsApp.' }
        ]
      },
      footer: {
        store: 'STORE',
        help: 'HELP',
        shipping: 'Shipping & Returns',
        contact: 'Contact',
        stores: 'Stores',
        copy: '© 2026 LIL DAVID / RITMO — DEMO CONCEPT'
      },
      whatsapp: {
        support: 'WHATSAPP SUPPORT',
        usaLabel: 'USA (Direct Orders)',
        peLabel: 'Peru (Local Stock)',
        defaultMsg: 'Hello Streetwar, I want to inquire about a sneaker model.',
        orderMsg: (name, size, price, category) => 
          `Hello Streetwar, I want to buy this model:\n\n*${name}*\n${size ? `Size: *EU ${size}*` : 'Size: *To be confirmed*'}\nPrice: *${price}*\nCategory: ${category}\n\nIs it currently available?`
      }
    }
  };

  // Get current language from localStorage or default to 'es'
  let currentLang = 'es';
  try {
    if (typeof localStorage !== 'undefined') {
      currentLang = localStorage.getItem(STORAGE_KEY) || 'es';
    }
  } catch (e) {
    currentLang = 'es';
  }
  if (!translations[currentLang]) currentLang = 'es';

  function getLang() {
    return currentLang;
  }

  function getT() {
    return translations[currentLang];
  }

  function formatPrice(penValue) {
    if (penValue === null || penValue === undefined) {
      return getT().catalog.inquire;
    }
    if (currentLang === 'en') {
      const usd = Math.round(penValue * 0.27);
      return `$ ${usd.toLocaleString('en-US')}`;
    }
    return `S/ ${penValue.toLocaleString('es-PE')}`;
  }

  function setLanguage(lang) {
    if (!translations[lang] || lang === currentLang) return;
    currentLang = lang;
    try {
      if (typeof localStorage !== 'undefined') {
        localStorage.setItem(STORAGE_KEY, lang);
      }
    } catch (e) {}
    window.dispatchEvent(new CustomEvent('languagechange', { detail: { lang } }));
  }

  window.RITMO_I18N = {
    getLang,
    getT,
    setLanguage,
    formatPrice,
    translations
  };
})();
