# Pattern: scroll-linked video (Apple method)

**Message:** "Watch a real process, step by step, at your own pace."
**Needs:** real footage, 8–20 s, one continuous action.

## How
Do not scrub a `<video>` element: seeking is jerky unless every frame is a keyframe, and mobile
browsers are unreliable. Extract a frame sequence and draw it on a `<canvas>`.

- 5–8 frames per second of footage is enough (scroll provides the smoothness).
- WebP, ~960 px wide, quality ~50: about 12 KB per frame. 93 frames ≈ 1.1 MB in the lab.
- Draw with "cover" fit; resize the canvas to `clientWidth × devicePixelRatio` (max 2).
- Ease the frame index (`gsap.to(state, { f, duration: 0.25 })`) so fast scrolling looks smooth.

## Choreography
Pinned on all devices (it works well on phones too), `end: "+=2400"`. A thin progress bar and
two or three caption cards that switch at fixed progress points (e.g. 0.38 and 0.68).

## Reverse
Fully reversible by nature.

## Reduced motion
Show one representative frame and all captions stacked.

## Skeleton
```js
const imgs = FRAMES.map(src => { const i = new Image(); i.decoding = "async"; i.src = src; return i; });
let cur = -1;
function draw(i){
  const im = imgs[i]; if (!im.complete || i === cur) return; cur = i;
  const s = Math.max(canvas.width/im.naturalWidth, canvas.height/im.naturalHeight);
  const w = im.naturalWidth*s, h = im.naturalHeight*s;
  ctx.drawImage(im, (canvas.width-w)/2, (canvas.height-h)/2, w, h);
}
const st = { f: 0 };
ScrollTrigger.create({ trigger: stage, start:"top top", end:"+=2400", pin:true, scrub:true, anticipatePin:1,
  onUpdate(self){
    gsap.to(st, { f: self.progress*(imgs.length-1), duration:0.25, overwrite:true,
      onUpdate: () => draw(Math.round(st.f)) });
    bar.style.transform = `scaleX(${self.progress})`;
    setCaption(self.progress < .38 ? 0 : self.progress < .68 ? 1 : 2);
  }});
```

## Pitfalls
- Leave room at the bottom of the stage for fixed UI (a floating switcher, cookie bar) so
  captions are never covered.
- Preload: start loading frames when the section is a viewport away, not on page load, for
  long sequences.
