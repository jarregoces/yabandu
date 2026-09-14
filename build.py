#!/usr/bin/env python3
"""
Sincroniza el header y el footer de todas las páginas.

Edita partials/header.html o partials/footer.html y ejecuta:

    python3 build.py

El script reemplaza el bloque <header>...</header> y <footer>...</footer>
de cada página por el contenido de los partials.

Tokens disponibles dentro de los partials:
  {HOME}  -> "" en index.html, "index.html" en el resto (para los anclajes)
  {WA}    -> enlace de WhatsApp con el mensaje por defecto
"""
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent
WA_NUMBER = "573215767930"
WA_MSG = "Hola Yabandú, quiero saber cómo llenar mi agenda de citas."
WA_LINK = f"https://wa.me/{WA_NUMBER}?text={quote(WA_MSG)}"

PAGES = [
    "index.html",
    "desarrollo-web.html",
    "embudos-de-venta.html",
    "automatizacion-ia.html",
    "politica-de-privacidad.html",
    "terminos-de-servicio.html",
]

header_src = (ROOT / "partials" / "header.html").read_text(encoding="utf-8").strip()
footer_src = (ROOT / "partials" / "footer.html").read_text(encoding="utf-8").strip()


def render(tpl: str, page: str) -> str:
    home = "" if page == "index.html" else "index.html"
    return tpl.replace("{HOME}", home).replace("{WA}", WA_LINK)


for name in PAGES:
    path = ROOT / name
    if not path.exists():
        print(f"  ! {name} no existe, se omite")
        continue

    html = path.read_text(encoding="utf-8")
    original = html

    html, n_h = re.subn(
        r"<header>.*?</header>",
        lambda _: render(header_src, name),
        html, count=1, flags=re.S,
    )
    html, n_f = re.subn(
        r"<footer>.*?</footer>",
        lambda _: render(footer_src, name),
        html, count=1, flags=re.S,
    )

    if not n_h or not n_f:
        print(f"  ! {name}: header={n_h} footer={n_f} — revisar la marcación")

    if html != original:
        path.write_text(html, encoding="utf-8")
        print(f"  ✓ {name} actualizado")
    else:
        print(f"  = {name} sin cambios")

print("Listo — header y footer sincronizados.")
