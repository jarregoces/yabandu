#!/usr/bin/env python3
"""
Build script — inyecta partials/header.html y partials/footer.html
dentro de cada página HTML, marcando el link de navegación activo
según el atributo data-page de cada <body>.

Uso: editar partials/header.html o partials/footer.html y volver a
correr:  python3 build.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
PAGES = [
    "index.html",
    "desarrollo-web.html",
    "embudos-de-venta.html",
    "automatizacion-ia.html",
    "politica-de-privacidad.html",
    "terminos-de-servicio.html",
]

header_src = (ROOT / "partials" / "header.html").read_text(encoding="utf-8")
footer_src = (ROOT / "partials" / "footer.html").read_text(encoding="utf-8")

for name in PAGES:
    path = ROOT / name
    html = path.read_text(encoding="utf-8")

    m = re.search(r'data-page="([^"]+)"', html)
    page = m.group(1) if m else None

    header = header_src
    if page:
        header = re.sub(
            rf'(<a[^>]*data-nav="{re.escape(page)}"[^>]*)>',
            r'\1 class="active">',
            header
        )

    html = re.sub(r'<header id="site-header"></header>', header.strip(), html, count=1)
    html = re.sub(r'<footer id="site-footer"></footer>', footer_src.strip(), html, count=1)

    path.write_text(html, encoding="utf-8")
    print(f"  ✓ {name} (nav activo: {page})")

print("Listo — header y footer inyectados en todas las páginas.")
