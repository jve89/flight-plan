# Pattern: video layers (AirHub hero)

**Message:** "This is our product / our work, in context."
**Needs:** real footage or a screen recording, plus a schematic UI card that shows what the product does.

## Choreography (desktop, pinned, scrub 0.4)
1. Video large and centered under the hero text (peeks into the first viewport).
2. Video shrinks to the left half; a schematic card fades in on the right.
3. Card rows complete one by one (ticks, values).
4. Video and card swap sides; the last row completes; status badge flips (Draft to Submitted).
5. Hold buffer (~20% of the timeline) so step 4 is finished before the pin releases.
Captions under the stage change per phase.

## Mobile and tablet portrait
No pin. Video full width (16:9), card below it. The card rows are scrubbed by scroll
(`start: "top 85%"`, `end: "bottom 55%"`, `scrub: 0.4`) so they also reverse.

## Reverse
Scrubbed: everything runs backwards, badge flips back to Draft.

## Skeleton
```css
@media (min-width:900px){
  .layers{position:relative;height:min(62vh,600px)}
  .vframe{position:absolute;top:0;left:0;width:100%;height:100%}
  .card{position:absolute;top:50%;left:54%;width:46%;transform:translateY(-50%)}
}
```
```js
mm.add("(min-width: 900px)", () => {
  gsap.set(card, { autoAlpha: 0, xPercent: 12 });
  const tl = gsap.timeline({ defaults:{ease:"none"}, scrollTrigger:{
    trigger: stage, start:"top top", end:"+=3200", pin:true, scrub:0.4, anticipatePin:1, invalidateOnRefresh:true }});
  tl.to(vframe, { width:"50%", top:"7%", height:"86%", duration:1, ease:"power2.inOut" }, 0.2)
    .to(card, { autoAlpha:1, xPercent:0, duration:0.6 }, 0.75);
  rows.forEach((row, i) => tl.to(row, { autoAlpha:1, duration:0.12 }, 1.35 + i*0.22));
  tl.to(vframe, { left:"50%", duration:1, ease:"power2.inOut" }, 2.6)
    .to(card, { left:"0%", duration:1, ease:"power2.inOut" }, 2.6)
    .to({}, { duration: 0.9 });            // hold buffer
});
```

## Pitfalls
- Without the hold buffer, a fast scroller sees the section release with half the rows done
  (Johan saw exactly this in the first version of the lab).
- Video must be muted, `playsinline`, with a poster, or iOS will not autoplay it.
- Card values marked "illustrative" when they are examples.
