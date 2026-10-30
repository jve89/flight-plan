---
name: "johan-motion"
description: Johan's motion and infographics system for websites. Use this skill whenever a web page needs movement, scroll animation, animated infographics, scroll-linked video, a choreographed hero, an animated product demo, animated diagrams, maps or charts, or any "interactive" or "moving" visual, in any stack (Astro, React, plain HTML, Claude artifacts). Also use it when Johan says a page should feel more alive, modern or premium, mentions sites like Holo or AirHub, or uses words like animatie, beweging, scroll-animatie, infographic, interactief, "laat het bewegen". Works together with the johan-design-dna skill, which owns the overall look; this skill owns how things move. Includes a mandatory test script for desktop, tablet and mobile.
---

# Johan's Motion System

Motion on Johan's sites works best when it **shows or explains something that a still image
cannot**: a transformation, a process, a sequence in time, a product working, data building up.
Motion can also be purely atmospheric, as long as it is calm and deliberate. What breaks the
calm, premium look he loves is restless motion: many things moving at once, everywhere, for no
reason. If atmospheric motion could also explain something, suggest that once; don't block it.

His references: tryholo.ai (scroll animations, heavy use of pre-rendered product videos),
airhub.app (hero where video layers move while a schematic app animates in the middle).
An approved showcase of six patterns is in `examples/motion-lab-source.html`
(Drone Approval Support content; the drone wording is filler, the motion is what was approved).

Always also apply the **johan-design-dna** skill for the look. This skill decides motion only.

## Core principles

1. **Meaning first.** Pick the pattern from the message, not from what looks impressive.
2. **Two or three big motion moments per page, maximum.** Everything else stays still or
   uses only subtle reveals. The lab shows six patterns because it is a showcase; no real page
   should stack them all.
3. **Scroll is time.** Scroll-linked animation must be readable at any scroll position and
   must run backwards when the visitor scrolls back (see the reversibility table).
4. **Every pinned section finishes before it releases.** Add a hold buffer at the end of every
   pinned timeline (about 20% of its length) so the animation is complete before the page moves on.
5. **Each device gets its own composition.** Desktop pins and choreographs; mobile usually
   un-pins, stacks and simplifies. Tablet portrait follows mobile, tablet landscape follows desktop.
6. **Reduced motion shows the final state.** No pinning, no scrubbing, no autoplay; everything
   readable and complete.
7. **Test before delivering.** Run `scripts/motion_test.py` (see Testing). Static screenshots
   at fixed scroll positions miss the real bugs; continuous scrolling finds them.

## Reversibility (scrolling back)

| Kind of motion | Scrolling back | Implementation | Examples |
|---|---|---|---|
| Tied to scroll position | Runs backwards exactly, frame by frame | `scrub: 0.4` timeline, pinned on desktop, unpinned scrub on mobile | Video layers, scroll video, map, choreography |
| Build-up on entering view | Plays forward on enter, reverses when the visitor scrolls back above it | `toggleActions: "play none none reverse"` | Matrix, counters, charts, card reveals |
| Mini story | Plays once and stays finished; offers a replay button | `once: true` + replay control | Live product demo |

## Choosing a pattern

| The message is... | Pattern | File |
|---|---|---|
| "Our product turns A into B" | Scroll choreography | `reference/patterns/choreography.md` |
| "This is our product, in context" | Video layers (AirHub hero) | `reference/patterns/video-layers.md` |
| "Watch a real process step by step" | Scroll-linked video | `reference/patterns/scrub-video.md` |
| "It works in N steps" | Sticky steps (text + changing visual) | `reference/patterns/sticky-steps.md` |
| "Here is how the logic flows" | Drawing diagram | `reference/patterns/drawing-diagram.md` |
| "Movement through space / a route / an area" | Route map | `reference/patterns/route-map.md` |
| "These numbers / this table / this matrix matter" | Data that builds | `reference/patterns/data-builds.md` |
| "See how easy it is to use" | Live product mockup | `reference/patterns/live-mockup.md` |

Fit per site type (combine with the energy level from johan-design-dna):

| Site type | Strongest patterns | Keep it sparse |
|---|---|---|
| Tech / SaaS | Live mockup, choreography, video layers | Most patterns fit; showing the product is the sale |
| Consultancy / expertise | Sticky steps, drawing diagram, data that builds | Video layers only with real footage |
| Local service business | Looped hero video, scroll-linked video | One strong real-footage moment is enough |
| Exuberant (zoo, festival) | Not yet in the library: parallax, playful transitions | Add patterns when such a project arrives, then update this skill |

Text left + visual right is fine inside sections (sticky steps); only in the hero is it a
johan-design-dna default to avoid.

## Three production methods

Top sites combine these. Choose per element:

1. **Code animation** (GSAP + SVG/HTML): diagrams, choreography, counters, mockups. Fully
   controllable, crisp, light. Default for explaining logic.
2. **Video as a building block**: real footage, screen recordings of a product, pre-rendered
   3D loops. This is where much of Holo's and AirHub's quality comes from. See `reference/video.md`.
3. **Real-time 3D** (Three.js): see the johan-design-dna hero patterns and, when it exists,
   the 3D pipeline skill.

## Workflow

1. **Message map**: list the page's sections and write the one thing each must make clear.
   Mark which two or three get a big motion moment; the rest get at most subtle reveals.
2. **Pattern choice** per moment from the table above. Note the production method and whether
   real assets (footage, screen recordings) exist; ask Johan for them before inventing.
3. **Choreography script** for each big moment, in the reply: phases, what moves, captions,
   desktop vs mobile behavior, reverse behavior. Keep it short.
4. **Build** with the stack in `reference/timing.md` and the pattern files. Johan executes in
   his own repo: return complete files, never fragments.
5. **Test** with `scripts/motion_test.py` on all four devices, slow and fast, cold load. Fix and
   re-run until everything passes, then look at the screenshots it saves.
6. **Deliver** with a two-line note: which patterns, and what the test caught and fixed.

## Testing (mandatory)

`scripts/motion_test.py` (Python + Playwright) does what a real visitor does:
- **Cold load**: starts scrolling before the page has fully loaded, which exposes position bugs
  caused by late fonts, video or images.
- **Continuous wheel scrolling**, slow and fast, down through the page and back up to the top.
- **Four devices**: desktop 1440×900, tablet landscape 1180×820, tablet portrait 820×1180,
  mobile 390×844.
- **Checks every ScrollTrigger automatically**: after scrolling past a trigger, its animation
  must be complete; after scrolling back above it, it must be reset (except `once` triggers).
- Saves screenshots at the start, middle and end of every pinned section per device.
- Reports console errors.

Usage: `python3 scripts/motion_test.py path/to/page.html` (or a URL). It needs GSAP and
ScrollTrigger exposed as globals (true for the CDN build; in Astro expose them in dev with
`window.gsap = gsap; window.ScrollTrigger = ScrollTrigger`).

A full run (4 devices × 2 speeds) takes several minutes. Where commands have a time limit,
run it per device (`--devices desktop --speeds fast`, then the others). Passing checks do not
replace looking: open the saved screenshots of every pinned section on every device.

Software-rendered 3D is slow in headless Chromium: expect longer waits there.

## Reference files

- `reference/patterns/*.md`: one file per pattern: when, choreography, desktop/mobile/reverse
  behavior, code skeleton, pitfalls.
- `reference/timing.md`: stack, easing, durations, scrub values, buffers, glue code, refresh rules.
- `reference/video.md`: footage, screen recordings, encoding, frame sequences, embedding.
- `reference/infographics.md`: building SVG diagrams that stay readable, mobile compositions.
- `reference/performance.md`: keeping it smooth on phones and laptops.
- `scripts/motion_test.py`: the test.
- `scripts/embed_media.py`: injects video and frame sequences into an artifact page as data URIs.
- `examples/motion-lab-source.html`: approved showcase, readable source. Media are placeholders
  (`__VIDEO__`, `__POSTER__`, `__FRAMES__`): see `reference/video.md` for how they were made.
