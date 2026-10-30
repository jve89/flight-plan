# Anti-patterns

Check the design plan against this list before building. Items marked **(craft)** are always wrong.
Items marked **(default)** are Johan's taste: usually avoid them, but they are fine when Johan asks
for them or when they are done well in a current way. Name the deviation; don't block it.

## What made the old complai-eu.nl fail (his own words: "veel te druk", "zo 2010")

| Problem | Why it fails | Instead |
|---|---|---|
| Four typefaces (Bricolage Grotesque, Instrument Sans, Inter, JetBrains Mono) **(craft)** | No typographic identity; quirky display face fights the clean look | One family (Inter) |
| Full-width flat header bar **(default)** | Feels like a template | Floating pill header |
| Text left, generic dashboard right **(default)** | Dated, generic split layout, and the visual said nothing | Centered hero with media that demonstrates, or a split hero done in a current way with media that shows something |
| Hero paragraph of six lines **(craft)** | Nobody reads it; the hero loses focus | One or two sentences |
| Four floating badges around the hero visual **(craft)** | Visual noise, "AI template" look | Zero to three trust chips, in a row, above or below |
| Blue + mint highlighter + coral + red **(default at level 1)** | Restless | One accent + neutrals |
| Monospace tags everywhere ("Art. 4", status chips) **(default)** | Tech cosplay | Regular weight labels in sentence case |
| Standard section stack: 4 pain cards, 3 steps, 9-feature grid, comparison table, 4 pricing tiers, FAQ **(craft)** | Generic; every AI-built SaaS page looks like this | Sections chosen from the content, each with one job |
| A decorative image in the "how it works" slot **(craft)** | Says nothing | A scroll animation that shows the product doing its work |

## Generic AI-generated design tells

Avoid unless the subject truly asks for it:
- Cream background + serif display + terracotta accent.
- Near-black with one acid-green or vermilion accent.
- Everything chopped into identical rounded cards with the same soft grey shadow.
- Gradient washes and glowing blobs as decoration.
- ALL-CAPS tracked eyebrow above every heading.
- Meta strings joined with middle dots ("A · B · C"), labels like "WORD — fragment".
- "→" appended to every button and link.
- Fade-and-slide-up on every section and hover lift on every card (motion everywhere = no motion).
- Numbered markers (01/02/03) on content that is not a sequence.
- Invented statistics, fake testimonials, fake logos, stock photos pretending to be the client's work.

## Technical anti-patterns (learned in testing)

- System font stack only: the site looks different on every OS. **(craft)**
- Desktop infographic scaled down on mobile until text is ~9px. **(craft)**
- ScrollTriggers created before pinned sections they depend on: their positions ignore pin spacing.
- Animated SVG paths with round caps starting at length zero: a stray dot appears.
- A CSS rule like `.parent span { display:block }` silently overriding a component's own
  `display:grid` (specificity). Scope child selectors with classes.
