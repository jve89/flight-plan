# Pattern: scroll choreography (transformation)

**Message:** "Our product turns A into B." Approved in Complai variant A (law text becomes a
task list), see the johan-design-dna example `complai-proef.html`.

## Choreography (desktop, pinned, scrub 0.4–0.8)
1. Input alone and centered (raw, overwhelming): e.g. a panel of law articles.
2. Highlight what matters (marker sweep on key phrases, the rest dims to ~0.32).
3. Input moves aside; the output builds next to it (items arrive one by one).
4. Resolution: progress ring fills, statuses flip to done.
5. Hold buffer.
Captions change per phase (crossfade, 8px movement).

Centering the input: `x = (sceneWidth + gap) / 4` moves the left column to the center of a
two-column grid; animate back to 0. Use a function value with `invalidateOnRefresh: true`.

## Mobile
No pin; stack input above output; scrub each phase over its own element so it still reverses.

## Pitfalls
- Marker highlights via `background-size` from `0% 100%` to `100% 100%` with
  `box-decoration-break: clone` so multi-line highlights look right.
- Keep the output readable at every scroll position: no half-faded text as an end state.
