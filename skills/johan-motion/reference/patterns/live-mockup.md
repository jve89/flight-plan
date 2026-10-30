# Pattern: live product mockup

**Message:** "See how easy it is to use."
A real-looking interface built in HTML (not a screenshot) where an animated cursor fills it in
and the result appears. Feels like a demo video, but crisp, light, translatable and editable.

## Behaviour
Mini story: plays once when 60% in view, stays finished, with a "Play again" button.
Do not replay on every pass.

## Build
- The mockup uses real buttons/inputs (accessible), styled like the product.
- Cursor: small SVG arrow, absolutely positioned inside the mockup, `pointer-events: none`.
- Target positions are computed at play time (`getBoundingClientRect` relative to the mockup),
  so the animation survives layout changes and different devices.
- Click = cursor scale .82 for 80 ms + the option gets its selected class.
- Result panel slides up (desktop: over the bottom of the form; mobile: below it).

```js
const pos = el => { const d = demo.getBoundingClientRect(), r = el.getBoundingClientRect();
  return { x: r.left - d.left + r.width*.55, y: r.top - d.top + r.height*.55 }; };
picks.forEach(p => {
  tl.to(cursor, { x: () => pos(p).x, y: () => pos(p).y, duration: .7, ease: "power2.inOut" })
    .to(cursor, { scale: .82, duration: .08 }).add(() => p.classList.add("sel"))
    .to(cursor, { scale: 1, duration: .12 });
});
```

## Pitfalls
- Function-based values (`x: () => ...`) so positions are measured when the step runs.
- Kill the previous timeline before replaying.
- Reduced motion: show the completed state directly, hide the replay button.
