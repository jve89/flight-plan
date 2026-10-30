# Pattern: drawing diagram

**Message:** "Here is how the logic flows." Approved in Complai variant B (AI use, risk level,
documents). Columns of nodes; connecting paths draw; counters update as connections land;
outcome nodes get a check.

## Choreography
1. Input nodes appear (stagger, slight x offset).
2. Paths from inputs to categories draw (`stroke-dashoffset` from length to 0); category
   counters rise.
3. Paths from categories to outcomes draw; outcome nodes slide in; checks pop.
Desktop: pinned + scrub. Mobile: see below.

## Mobile (mandatory, separate composition)
A three-column SVG scaled to a phone has ~9px text: a failure (seen in the Complai proof).
Build a vertical version instead: inputs on top, categories in the middle, outcomes at the
bottom, paths running downward, all text ≥ 13px. Two SVGs (`.flow-wide`, `.flow-tall`) swapped
with CSS is fine; animate whichever is visible via `gsap.matchMedia`.

## Pitfalls
- `stroke-linecap: butt` on paths that start at zero length, or round caps leave stray dots.
- Shorten labels instead of shrinking type; leave room for check icons at the end of nodes.
- `getTotalLength()` after fonts load if paths depend on text positions.
