# The pill header

Johan's signature element, present on every site he likes (his own sites, AirHub, Holo).
This is a tier 2 default: keep it unless Johan asks for something else or a deviation is agreed.

## Anatomy

- Floats: detached from the top edge (`top: 1rem`), max width = content wrap, centered.
- Fully rounded (`border-radius: 999px`), glass fill with `backdrop-filter: blur(18px) saturate(140%)`,
  1px light border. Solid fallback when `backdrop-filter` is unsupported.
- Left: brand wordmark in weight 800, letter-spacing -0.035em. A logo mark is fine if the brand has one.
- Then 3–6 links, `.9rem`, weight 500, muted color; ink on hover and for the current page.
- Right: optional secondary link (Inloggen, language switch), then **one** accent CTA pill.
- Mobile (< 1000px or whenever links do not fit): links collapse into a round toggle that opens a
  rounded panel below the pill. The CTA stays visible; shorten its label if needed.
- Sticky (`position: sticky; top: 0`), or `fixed` (`.is-overlay`) over a full-bleed video/3D hero.
- Light themes get the same pill with white glass. Never a full-width flat bar.

## Code (framework-free; port to an Astro component as-is)

```html
<header class="site-header">
  <nav class="pill" aria-label="Hoofdmenu">
    <a class="brand" href="/">Merknaam</a>
    <ul class="pill-links">
      <li><a href="/diensten" aria-current="page">Diensten</a></li>
      <li><a href="/prijzen">Prijzen</a></li>
      <li><a href="/over">Over ons</a></li>
      <li><a href="/contact">Contact</a></li>
    </ul>
    <div class="pill-actions">
      <a class="pill-secondary" href="/login">Inloggen</a>
      <a class="btn btn-primary btn-sm" href="/contact">Vraag een offerte aan</a>
      <button class="pill-toggle" type="button" aria-expanded="false" aria-controls="pill-panel" aria-label="Menu openen">
        <span class="bars" aria-hidden="true"></span>
      </button>
    </div>
    <div class="pill-panel" id="pill-panel" hidden>
      <ul>
        <li><a href="/diensten">Diensten</a></li>
        <li><a href="/prijzen">Prijzen</a></li>
        <li><a href="/over">Over ons</a></li>
        <li><a href="/contact">Contact</a></li>
        <li><a href="/login">Inloggen</a></li>
      </ul>
    </div>
  </nav>
</header>
```

```css
.site-header{position:sticky;top:0;z-index:60;padding:1rem var(--gutter) 0}
.site-header.is-overlay{position:fixed;inset-inline:0}
.pill{position:relative;max-width:var(--wrap);margin:0 auto;display:flex;align-items:center;gap:1.5rem;
  padding:.45rem .45rem .45rem 1.35rem;border-radius:var(--r-pill);
  background:var(--raised);border:1px solid var(--glass-line)}
@supports (backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px)){
  .pill{background:var(--glass);-webkit-backdrop-filter:blur(18px) saturate(140%);backdrop-filter:blur(18px) saturate(140%)}
}
.brand{font-weight:800;letter-spacing:-.035em;font-size:1.12rem;color:var(--ink);text-decoration:none;white-space:nowrap}
.pill-links{display:flex;gap:1.6rem;list-style:none;margin:0 0 0 .75rem;padding:0}
.pill-links a{color:var(--muted);font-size:.9rem;font-weight:500;text-decoration:none;transition:color .15s}
.pill-links a:hover,.pill-links a[aria-current=page]{color:var(--ink)}
.pill-actions{margin-left:auto;display:flex;align-items:center;gap:.35rem}
.pill-secondary{color:var(--ink-2);font-size:.9rem;font-weight:500;padding:.5rem .85rem;text-decoration:none}
.pill-secondary:hover{color:var(--ink)}
.pill-toggle{display:none;width:40px;height:40px;border-radius:50%;border:1px solid var(--glass-line);
  background:transparent;color:var(--ink);cursor:pointer;place-items:center}
.pill-toggle .bars{position:relative}
.pill-toggle .bars,.pill-toggle .bars::before,.pill-toggle .bars::after{display:block;width:16px;height:2px;border-radius:2px;background:currentColor}
.pill-toggle .bars::before,.pill-toggle .bars::after{content:"";position:absolute;left:0}
.pill-toggle .bars::before{top:-5px}.pill-toggle .bars::after{top:5px}
.pill-toggle[aria-expanded=true]{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.pill-panel{position:absolute;top:calc(100% + .5rem);inset-inline:0;padding:1rem;border-radius:var(--r-card);
  background:var(--panel);border:1px solid var(--line);box-shadow:var(--shadow-panel);max-height:calc(100dvh - 7rem);overflow-y:auto}
.pill-panel ul{list-style:none;margin:0;padding:0;display:grid}
.pill-panel a{display:block;padding:.75rem 1rem;border-radius:var(--r-sm);color:var(--ink-2);font-weight:500;text-decoration:none}
.pill-panel a:hover{color:var(--ink);background:var(--accent-soft)}
@media (max-width:999px){
  .pill-links,.pill-secondary{display:none}
  .pill-toggle{display:grid}
}
@media (max-width:420px){ .pill{gap:.75rem;padding-left:1.1rem} .brand{font-size:1rem} }
```

```js
const t = document.querySelector('.pill-toggle'), p = document.getElementById('pill-panel');
t?.addEventListener('click', () => {
  const open = t.getAttribute('aria-expanded') === 'true';
  t.setAttribute('aria-expanded', String(!open));
  t.setAttribute('aria-label', open ? 'Menu openen' : 'Menu sluiten');
  p.hidden = open;
});
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && p && !p.hidden) { t.click(); t.focus(); }
});
```
