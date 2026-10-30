# Pattern: sticky steps (scrollytelling)

**Message:** "It works in N steps."
**Desktop:** steps as text on the left (each ~62vh tall), one sticky visual panel on the right
that changes per step. Text left + visual right is fine here (not in the hero).

## Behaviour
- The active step is full opacity, others 0.38.
- Each step has its own visual layer inside the sticky panel; layers crossfade (opacity +
  12px translate, 0.45 s). Small inner details can stagger in (CSS transition delays).
- Active step via one ScrollTrigger per step: `start: "top 55%"`, `end: "bottom 55%"`, `onToggle`.

## Mobile and tablet portrait
**Do not** use a sticky visual above scrolling text: it covers the active step's heading
(found in testing). Instead clone each visual under its own step text, show it as a normal
panel, and reveal it with a small fade when it enters.

```js
if (matchMedia("(max-width: 899px)").matches) {
  document.querySelectorAll(".sv").forEach((v, i) => {
    const c = v.cloneNode(true); c.classList.add("sv-inline", "is-active", "panel");
    c.querySelectorAll("[id]").forEach(e => e.removeAttribute("id"));
    steps[i].appendChild(c);
  });
}
```

## Reverse
State-based, so it follows the scroll position both ways automatically.

## Pitfalls
- Build generated visual content (grids, chips) before cloning.
- Create the step triggers after any pinned section above them, and refresh after fonts and
  media load, or the wrong step is active on a first (cold) visit.
- Visual text on mobile ≥ 13px: SVG diagrams designed at desktop size need larger font sizes
  or fewer labels on mobile.
