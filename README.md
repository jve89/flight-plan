# Flight Plan

Johan's skill system: from a problem worth solving to a business that is found and valued.

## Status: v1.0.0, the baseline

This repository holds exact, unchanged copies of the seven skills that were installed in Claude on 30 October 2026. Nothing has been modified. Every later change starts from here.

| Folder | What it is |
| --- | --- |
| `skills/build-machine` | Build method: prototype first, then spec, then gated phases |
| `skills/business-opportunity-evaluator` | Idea evaluation with a build path |
| `skills/compliance-document-architect` | Compliance documents (operations manuals, SORA) |
| `skills/johan-design-dna` | Visual design DNA for websites |
| `skills/johan-motion` | Motion, scroll animation and infographics |
| `skills/johan-3d` | Blender to glTF to Three.js pipeline |
| `skills/saas-architect` | Architecture-first design for software |

`BASELINE-MANIFEST.txt` holds a SHA-256 fingerprint of every baseline file. To check that nothing in the baseline changed, run this in the repository folder:

```
shasum -a 256 -c BASELINE-MANIFEST.txt
```

## Rules for changing skills

1. The baseline (tag `v1.0.0`) is never edited. A change is a new commit and a new version.
2. Before a skill changes, list its rules and lessons, and record how it answers three test questions.
3. One change per version, with a line in `CHANGELOG.md` that names the problem it fixes.
4. A rule leaves a skill only with a destination ("moved to ...") or a reason ("removed because ...").
5. An installed skill is replaced only after the new version passes the same three test questions.

The design of the full system is in the Flight Plan blueprint (private document).
