# Motifs

A motif is a graphic element that repeats across every surface the brand appears on. Good motifs come **from the mark's own geometry**, so the whole system feels drawn by one hand. Every motif needs a **meaning** (what it says about the product) and a **place** (where it goes on a page). Without both, users call it "bland" or "I don't get where this goes", even when it looks nice.

## Read the mark first

Before inventing anything, write down:
- **Symmetry.** Rotational order (does it land on itself after 180°? 90°?) and mirror axes. Rotational symmetry gives a free loading animation: turn by 360/order and it lands on itself.
- **Construction.** Is it several identical parts? Can it be split into halves that frame something?
- **The characteristic gesture.** A step, a curve, a joint, a corner, a dot. Take its exact path data and reuse it at other scales. Don't redraw it by eye.
- **Stroke vs fill, and the ends.** Square, round or cut. Never change these on the user's mark; offer them as a suggestion for the designer.
- **Weight.** Stroke thickness relative to the mark's height. Motifs used in context should be much lighter than the mark.

## Catalogue (built into the template unless marked "custom")

| Motif | Needs | Means | Goes |
| --- | --- | --- | --- |
| Turn | rotational symmetry | turns and lands on itself: stability | loaders, "thinking" states |
| Turn, step by step | rotational symmetry | progress that ends where it started | onboarding, how-it-works steps, dividers |
| Dot mark | any mark | the mark as a dot-matrix readout | faint hero backgrounds, share cards, merch |
| Tile | any mark | the mark repeated, one in the primary color | footer bands, packaging, slides, swag |
| Readout | a readout font | status as hardware display | counters, status bars, launch numbers |
| Brackets (custom) | mark splits into halves | halves pulled apart to hold a line | pull quotes, the one sentence to remember |
| Joint dots (custom) | a characteristic stroke | the gesture alone in dot matrix | badges, empty states |
| Nest (custom) | a dip/curve gesture | layers holding layers, the important thing at the centre | "how it works", depth |

Motifs that tested badly in the Kraddle session: heavy lines running through a page ("path"), line fields with one highlighted line ("current"), and stairs or pulses with no clear meaning. The common problems were **lines too thick** (they fight the text), **one saturated line ruining an otherwise quiet pattern**, and **no stated place**.

## Rules that keep motifs working

- **Text leads, motifs recede.** Inside real layouts, draw motifs faint (the `line2` token), thin (2–4px strokes in context), or small. Save full weight for the motif's own showcase tile.
- **One accent per motif.** A single orange tile, one dot run, one frame. Never a whole line in the accent color.
- **The logo stays ink or paper.** Motifs may use the primary color; the logo never does.
- **Show every motif in use:** a hero background, a loader inside a button, a quote framed by brackets, a footer band. Users judge motifs in context, not in isolation.

## Custom motif snippets (brand.json `motifs.custom[].svg`)

Write the SVG as a string. Paint with `currentColor` or `style="fill:var(--primary)"`. Don't write `fill="var(--x)"` in an attribute: var() in presentation attributes isn't reliable. For halves, keep the mark's original coordinates and wrap them in `<g transform="translate(..) scale(..)">`. To reuse a gesture at another scale, take its path commands and multiply every coordinate by the scale factor in JS or Python while writing the JSON.
