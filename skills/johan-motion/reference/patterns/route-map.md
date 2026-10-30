# Pattern: route map

**Message:** "Movement through space": a route, an area, a coverage zone, a delivery path.

## Build
Stylised SVG map (no tiles, no remote images): muted blocks for land use, a river, roads.
One route path (visible, dotted). A marker (drone, vehicle) that follows the route with
GSAP MotionPathPlugin. Optional nested volumes around the route: the same path drawn with
increasing `stroke-width`, round caps and joins, low-opacity colors.

## Choreography (desktop, pinned, scrub 0.4, end "+=2600")
1. Map visible, route empty.
2. Route draws while the marker travels along it.
3. Volumes grow outward one by one; their labels appear with leader lines.
4. Hold buffer.

## Mobile
No pin; the same timeline scrubbed over the section (`start: "top 80%"`, `end: "bottom 45%"`).
Labels inside the SVG become unreadable when scaled down, so hide them and show an HTML legend
under the map (legend is visible on all devices).

## Skeleton
```js
gsap.registerPlugin(MotionPathPlugin);
line.style.strokeDasharray = L + " " + L; line.style.strokeDashoffset = L;
tl.to(line, { strokeDashoffset: 0, duration: 1.2 }, 0)
  .to(marker, { motionPath: { path: "#route-line", align: "#route-line", alignOrigin: [.5,.5] }, duration: 1.2 }, 0);
volumes.forEach((v, i) => tl.to(v, { attr: { "stroke-width": W[i] }, duration: .55, ease: "power2.out" }, 1.35 + i*.4));
tl.to({}, { duration: .9 });
```

## Pitfalls
- `motionPath` must point at a **rendered** path, not one inside `<defs>`: alignment fails and
  the marker disappears (found in testing).
- Animate volumes with `attr: { "stroke-width" }`; scaling a group distorts the stroke.
