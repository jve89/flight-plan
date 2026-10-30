# Typography

## Default: Inter, one family

Inter is the standard because it is the closest cross-platform match to SF Pro, which is what
Johan saw on his Mac when he fell in love with his own sites (they used the system font stack,
so Windows and Linux visitors saw something else). Always load it as a webfont.

- Astro: self-host with `@fontsource-variable/inter` (no third-party request, no layout shift).
- Prototypes/artifacts: Google Fonts `family=Inter:wght@300..800&display=swap`.

## Scale and settings (from approved sites)

| Role | Size | Weight | Tracking | Line-height |
|---|---|---|---|---|
| Hero h1 | `clamp(2.55rem, 1.5rem + 4.7vw, 5.3rem)` | 800 | -0.045em | 1.02 |
| Section h2 | `clamp(1.9rem, 1.3rem + 2.6vw, 3.25rem)` | 800 | -0.035em | 1.15 |
| h3 / card title | ~1.1–1.375rem | 650–700 | -0.015em | 1.2 |
| Lead | `clamp(1.05rem, 1rem + .35vw, 1.25rem)` | 400 | normal | 1.55 |
| Body | 1rem | 400 | normal | 1.6 |
| Nav / UI | .88–.95rem | 500–650 | -0.01em | 1.2 |
| Small print | .8–.86rem | 400–500 | normal | 1.5 |

Rules that make Inter look premium instead of generic:
- Big type needs tight tracking. Inter at 80px with default tracking looks loose and cheap.
- `text-wrap: balance` on headlines so no single word dangles on the last line.
- Keep hero lines short: max about 15 characters per em-width line (`max-width: 15ch` works).
- Line length for body text under 70 characters.
- Sentence case everywhere. No all-caps labels.

## Allowed variation within the default

Johan explicitly likes variation as long as it stays tight and modern:
- **Weight contrast between two sentences**: first sentence weight 300, second weight 800
  (approved in Complai variant B). Use it on whole sentences, not on a single word.
- Different hero sizes per site, mixed sentence lengths, a single huge number with a small label
  when the number truly is the message.

## Tier 2 items: ask first

- **A different typeface.** Fine when the subject asks for it: an exuberant zoo or festival site
  may get a playful display face for headlines (Inter stays for body and UI); an antique furniture
  or wine site may suit a classic serif. Propose it with one sentence of reasoning.
- **Italic or color-accented single words in headlines.** Johan dislikes this pattern in general
  (his friend overuses it), but it can fit editorial, luxury or heritage subjects. Ask.
- **Monospace labels.** Only for genuinely technical content (code, terminal output), never as
  "tech decoration".
