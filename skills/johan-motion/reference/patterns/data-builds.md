# Pattern: data that builds

**Message:** "These numbers, this table, this matrix matter."
Charts that grow, counters that count, a matrix that fills and then highlights one answer.

## Behaviour
Plays when 70% into view; reverses when the visitor scrolls back above it:
`toggleActions: "play none none reverse"`.

Matrix example (lab, SORA SAIL matrix):
1. Cells cascade in (`stagger: { each: .035, grid: [rows, cols] }`, scale .85 to 1).
2. Highlight the row, then the column, then ring the intersecting cell.
3. Result chips fade in next to it.

Class changes inside a timeline must also undo on reverse:
```js
const tl = gsap.timeline({ scrollTrigger: { trigger: mx, start: "top 70%", toggleActions: "play none none reverse" } });
tl.to(cells, { autoAlpha: 1, scale: 1, duration: .4, stagger: { each: .035, grid: [6,4] } })
  .add(() => rowHead.classList.toggle("hl", !tl.reversed()), "+=.2")
  .add(() => colHead.classList.toggle("hl", !tl.reversed()), "+=.35")
  .add(() => hit.classList.toggle("hit", !tl.reversed()), "+=.35");
```

## Rules
- Real data only. No invented statistics; example values are labelled "illustrative".
- Numbers in tabular figures (`font-variant-numeric: tabular-nums`).
- Color scales must differ in lightness, not only hue; check text contrast on every step.
- Keep the build under ~2 s; testers and visitors should not wait.
- On a light section, the pill header switches to light glass (see `../timing.md`).
