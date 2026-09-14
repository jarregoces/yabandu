// Yabandú — menú móvil, FAQ y scroll reveal.
// El header y el footer ya vienen escritos directamente en cada
// página (ver build.py) — este script ya no depende de fetch().

function setupMobileMenu() {
  const menuBtn = document.querySelector('.menu-btn');
  const navLinks = document.querySelector('.nav-links');
  if (menuBtn && navLinks) {
    menuBtn.addEventListener('click', () => {
      navLinks.classList.toggle('mobile-open');
    });
  }
}

function setupFaqAccordion() {
  document.querySelectorAll('.faq-item').forEach(item => {
    const q = item.querySelector('.faq-q');
    const a = item.querySelector('.faq-a');
    if (!q || !a) return;
    q.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(o => {
        if (o !== item) { o.classList.remove('open'); o.querySelector('.faq-a').style.maxHeight = null; }
      });
      if (isOpen) {
        item.classList.remove('open');
        a.style.maxHeight = null;
      } else {
        item.classList.add('open');
        a.style.maxHeight = a.scrollHeight + 'px';
      }
    });
  });
}

function setupScrollReveal() {
  const items = document.querySelectorAll('.reveal');
  if (!items.length) return;
  if (!('IntersectionObserver' in window)) {
    items.forEach(el => el.classList.add('in'));
    return;
  }
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
  items.forEach(el => io.observe(el));
}

// Envía un evento a Google Tag Manager (dataLayer) cada vez que
// alguien hace clic en un CTA o en el botón flotante de WhatsApp,
// para poder medir conversiones desde GTM / GA4 / los pixels.
function setupWhatsAppTracking() {
  window.dataLayer = window.dataLayer || [];
  document.querySelectorAll('a[href^="https://wa.me/"]').forEach(link => {
    link.addEventListener('click', () => {
      window.dataLayer.push({
        event: 'whatsapp_click',
        wa_source: link.getAttribute('data-wa') || 'link'
      });
    });
  });
}

document.addEventListener('DOMContentLoaded', () => {
  setupMobileMenu();
  setupFaqAccordion();
  setupScrollReveal();
  setupWhatsAppTracking();
});
