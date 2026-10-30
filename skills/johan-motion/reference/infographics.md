# Infographics that stay readable

- **SVG with real text**, not images of text. Use the site font (`font-family` on the SVG or via CSS).
- **Design at one size per composition**: a wide desktop composition and a tall mobile one.
  Minimum rendered text size on mobile: 13px. Compute: rendered = font-size × (rendered width / viewBox width).
- **Fewer, shorter labels** beat smaller type. Move secondary text to an HTML legend or caption.
- **Lines**: 1.5–2 px, `butt` caps when animated from zero; color by category at ~0.45–0.75 opacity.
- **Nodes**: rounded rects (rx 14–16), 1px border in the line color, white or raised fill.
- **Color for categories** differs in lightness too; never meaning by hue alone.
- **One focal result** per infographic (the highlighted cell, the final document, the check).
- **Grids of data** (density maps, matrices) built in JS from data, not hand-placed.
- **Accessibility**: `role="img"` + `aria-label` describing the conclusion, or a real table
  (`role="table"`) when the content is tabular.
- Label example values "illustrative"; never invent statistics.
