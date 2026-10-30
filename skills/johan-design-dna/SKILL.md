---
name: "johan-design-dna"
description: Johan's personal visual design DNA for websites. Use this skill for ANY website, landing page, homepage, marketing site, hero section, redesign or web page Johan asks Claude to build, design, mock up or improve, in any stack (Astro, React, plain HTML, Claude artifacts). Also use it when he asks to make a site "mooier", "moderner", "strakker", more professional, or says a page looks bad, generic or cluttered, and when reviewing or critiquing a site's look. Trigger words include website, site, landing page, homepage, hero, header, navbar, redesign, webdesign, "bouw een website", "maak een pagina", "ziet er niet mooi uit". Use it even when he does not mention design explicitly, because if the output is a web page someone will look at, this skill applies.
---

# Johan's Design DNA

Johan builds websites with Claude but does not trust his own visual judgement. He wants
every site to look modern, calm and premium without having to explain his taste again.
This skill is that explanation. Read it fully before planning any page.

His taste was calibrated on real sites. He likes: lendavhollandlane.ee and
drone-approval-support.pages.dev (his own), airhub.app (former employer), proven-saas.com,
tryholo.ai, penpot.app. He disliked the old complai-eu.nl (cluttered, generic, dated).
A reference implementation that he approved is in `examples/complai-proef.html`:
three hero variants (dark choreography, light infographic, 3D object) sharing one DNA.

## The core idea: defaults, not dogma

Every website has a different subject, and the subject decides a lot. A zoo can be loud,
an antique furniture shop can use an italic serif. So the rules come in three tiers:

1. **Craft rules**: always apply. They are about quality, not taste.
2. **Johan's defaults**: his personal preference and the starting point, not a rulebook.
   Use them unless the subject or Johan's own request calls for something else. Deviations
   are normal design choices, never a conflict: name them openly, never hide them (see
   tier 2 for how).
3. **Project variables**: decided per project in the intake.

## Tier 1: Craft rules (always)

- **Every visual is a deliberate choice, never filler.** Preferably it shows or explains
  something: a product demo, a transformation, a real photo or video of the work, data that
  builds up. A visual may also simply be beautiful (an atmospheric 3D object, a brand moment
  in the hero) as long as it is chosen on purpose and adds to the feel of the page. What is
  never OK: a meaningless image in a slot that should explain. Lesson from the old Complai
  site: the "how it works" image said nothing and was replaced by a scroll animation showing
  the product turning law text into tasks. If a purely aesthetic visual could also explain
  something, suggest that once; don't block it or reject it as "decoration".
- **One memorable thing per page section.** Spend boldness in one place, keep the rest
  quiet. No clouds of floating badges, chips and stats around a hero visual.
- **Short hero copy.** Headline plus one or two sentences. A six-line hero paragraph is
  always wrong.
- **Load a real webfont.** Never rely on the system font stack alone: on a Mac it shows
  SF Pro, on Windows Segoe UI, on Linux something worse. The site must look the same for
  every visitor.
- **Design mobile separately for anything visual.** Infographics and 3D scenes need their
  own mobile composition (e.g. a wide flow diagram becomes vertical, a horizontal card
  fan becomes a vertical cascade). Scaling a desktop diagram down until the text is 9px
  is a failure.
- **Overlap follows reading direction.** When elements overlap, the readable part
  (usually the left-aligned title) must stay visible.
- **No template section stack.** Do not default to "4 pain cards, 3 steps, 9 feature grid,
  comparison table, 4 pricing tiers, FAQ". Choose sections from the content.
- **Accessibility floor.** Contrast 4.5:1 for body text, visible keyboard focus, real
  buttons and links, `prefers-reduced-motion` respected (show final states, no pinning).
- **Look before delivering.** Screenshot desktop (1440×900) and mobile (390×844) at
  several scroll positions, fix what is wrong, then deliver. See `checklist.md`.

## Tier 2: Johan's defaults (starting point, not rules)

**Johan's request is his approval.** When he explicitly asks for something, or points at a
reference site and wants an element from it, build it. Mention in one line that it differs
from his default ("Dit wijkt af van je default: split hero"), then continue. Never frame it
as "your DNA or this, you must choose".

**Deviations you propose yourself** go into the design plan as normal choices, one line each
with the reason ("Afwijkingen: split hero, omdat…"). Johan approves the plan as a whole; do
not stop for each item separately.

**Everything must feel current.** The test for any layout or element is not "is it on the
list" but "does this look like a modern, premium site in this year, done well?"

| Area | Default |
|---|---|
| Typeface | **Inter**, loaded as webfont, one family for everything |
| Headlines | Weight 800, letter-spacing about -0.045em, line-height about 1.02, `text-wrap: balance`. Weight contrast between two sentences (300 + 800) is a welcome variation |
| Header | Floating glass **pill** navbar, detached from the top edge. Details in `reference/header.md` |
| Hero layout | **Centered**: headline, one or two sentences, primary + ghost button, small reassurance line, then the hero media below or behind |
| Usually avoid | **Text left + image right split hero**: often looks dated and template-like. Fine when done well and in a current way (strong composition, media that shows something, generous space, e.g. Holo). **One italic or differently colored accent word in a headline**: a common AI-template tell. **All-caps eyebrow labels** and **monospace data labels**: tech cosplay when used as decoration; fine for genuinely technical content. **Arrows appended to button text**: often a template tell; fine when it fits the design. Each of these is a default, not a ban |
| Color | One accent color plus neutrals, on light or dark. Accent chosen from the subject |
| Energy | Level 1, calm (see `reference/energy-levels.md`) |
| Stack | Astro for marketing sites; GSAP + ScrollTrigger, Lenis, Three.js for motion and 3D (see `reference/stack.md`) |

How to note deviations, in Johan's language (Dutch), inside the design plan:

> Afwijkingen van je defaults:
> - Klassieke serif met cursief in plaats van Inter: past beter bij antieke meubelen.
> - Split hero, zoals bij Holo (jouw verzoek).

## Tier 3: Project variables (intake)

Before planning, make sure these are known. Ask only what the conversation does not
already answer, all in one short message:

1. **Site type**: which archetype (see `reference/layout-archetypes.md`).
2. **Theme**: dark or light. Both are equal and neither is a deviation; the subject decides.
   "One accent plus neutrals" works on both.
3. **Energy level**: 1 calm (default), 2 lively, 3 exuberant.
4. **Hero media**: looped video, choreographed scroll scene, explanatory infographic,
   3D object, product demo. Several roads lead to Rome; pick what shows the subject best
   (see `reference/hero-patterns.md`).

Also ask whether real assets exist (video footage, photos, product screenshots). Real
assets beat invented ones; never fake photos of work that has not happened.

## Workflow

1. **Intake**: tier 3 questions (skip what is known).
2. **Design plan** (short, in the reply): 4–6 named hex colors, type roles, a one-line
   layout concept per section with an ASCII wireframe for the hero, the one memorable
   thing, and any tier 2 deviations as normal choices (requested ones noted, own ones with a reason). Check the plan against
   `reference/anti-patterns.md` before building.
3. **Build**: tokens first (`tokens/tokens.css` is the starting point), then header,
   hero, sections. Johan executes in his own repo: return complete files, never fragments,
   and ask for the current version of a file before changing it.
4. **Review loop**: screenshots on desktop and mobile, compare against `checklist.md`,
   fix, repeat. Mention what you fixed in one or two lines.
5. **Deliver**: the page plus a short note on which defaults were used and which
   deviations were requested or agreed.

## Reference files (read when relevant)

- `tokens/tokens.css`: base tokens plus a dark and a light theme. Start every project here.
- `reference/header.md`: the pill navbar with full HTML/CSS/JS, including mobile menu.
- `reference/typography.md`: type scale, weights, tracking, variation rules.
- `reference/layout-archetypes.md`: section structures per site type.
- `reference/hero-patterns.md`: the hero media options and when to use each.
- `reference/energy-levels.md`: what changes between calm, lively and exuberant.
- `reference/anti-patterns.md`: what made the old Complai site fail, plus generic AI tells.
- `reference/stack.md`: Astro, GSAP, Lenis, Three.js setup and hard-won technical lessons.
- `checklist.md`: the pre-delivery review.
- `examples/complai-proef.html`: approved reference implementation of all three hero types.

Related skills (planned, may not exist yet): a motion & infographics skill for scroll
choreography and animated diagrams, and a 3D pipeline skill for procedural models. If
they exist, use them for the hero media; this skill stays in charge of the overall look.
