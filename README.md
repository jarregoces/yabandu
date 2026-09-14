# Yabandú — sitio web

Sitio estático (HTML + CSS + JS vanilla) de la agencia Yabandú:
desarrollo web, embudos de adquisición y automatizaciones con IA.

## Estructura

```
index.html                 Landing principal
desarrollo-web.html        Servicio 1
embudos-de-venta.html      Servicio 2
automatizacion-ia.html     Servicio 3
politica-de-privacidad.html
terminos-de-servicio.html
css/styles.css             Sistema visual
js/script.js               Menú, FAQ, scroll reveal, tracking WhatsApp
img/                       Imágenes locales
partials/                  Fragmentos header/footer (ver build.py)
sitemap.xml · robots.txt · llms.txt
```

## Medición — Google Tag Manager

Cada página incluye el contenedor de **Google Tag Manager** (`GTM-NNZVVCL7`),
desde el que se administran GA4 y los pixels (Meta, TikTok, etc.) sin tocar
el código. El snippet está en las 6 páginas: el `<script>` en el `<head>` y
el `<noscript>` justo tras `<body>`.

Al hacer clic en cualquier CTA de WhatsApp o en el botón flotante se envía
el evento `whatsapp_click` a `dataLayer`, listo para configurarse como
conversión en GTM/GA4/pixels.

## WhatsApp

Todos los CTAs principales y un botón flotante apuntan a
`https://wa.me/573215767930` con un mensaje predefinido.

## Desarrollo local

```bash
python3 -m http.server 8000   # abrir http://localhost:8000
```
