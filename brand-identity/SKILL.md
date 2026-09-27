---
name: brand-identity
description: >
  Turn a project's context and brand story (plus an existing logo, if there is one) into a finished
  visual brand identity: logo lockup, color system, type pairing, motifs drawn from the mark, examples
  of it all in use, and a brand kit (logo SVGs, CSS/JSON tokens, a one-page guide). Built for engineers
  and founders without brand-design skills who still want products that look deliberate. Use this
  whenever someone asks for a brand, brand identity, brand board, visual identity, style guide, look
  and feel, color palette plus fonts, or "make this look good" for a new product, startup or landing
  page. Also use it when they share a logo and ask what to pair with it, or say things like "I'm not a
  designer but I want this to feel premium", even if they never say the word "brand".
---

# Brand identity

Get from "here's what we're building and why" to a finished brand board in **two rounds of feedback, not ten**. Most wasted iterations come from the same few mistakes: generic fonts, a header face too artistic to work as a header, a wordmark whose weight doesn't match the mark, thick motif lines that compete with the text, an accent color that quietly took over, and motifs with no clear job. This skill heads those off up front.

The deliverable is a **brand board**: one HTML page generated from a `brand.json` file by `scripts/build.py`, plus a **brand kit** folder. Read `assets/example-brand.json` before writing a brand.json; it's a complete worked example and doubles as the schema.

## 0. Intake: ask once, then work

You need these. Ask for anything missing in a single message, and suggest defaults so the user can simply say yes.

1. **Project context:** what it is, who it's for, where the brand will appear (landing page, app, CLI, deck).
2. **Brand story:** the feeling, the metaphor, the origin of the name. This drives everything else, so if it's thin, ask two or three sharp questions rather than guessing.
3. **Logo:** an SVG if possible (a PNG works for analysis only). If there's no logo, see "No logo" below.
4. **Taste signals:** products or brands they admire, and anything they hate. Even a single reference, like "Teenage Engineering", is worth a lot.
5. **Hard constraints:** colors they're attached to, free fonts only (the default), light or dark first.

## 1. Words before pixels

Draft the words first, because the board needs real copy and wrong copy poisons feedback on the visuals.

- **Brand line:** one sentence with the brand's promise, such as "Build what's in your head. Kraddle holds the rest."
- **Hero headline:** name the pain in the user's own words, not the product's internal model. Test it by asking whether the target user has literally said or thought this. Avoid internal jargon (the user corrected "decision" to "what I wanted") and avoid "we solve X".
- **Voice:** three do's and three don'ts.

Show the lines briefly and move on. Don't hold up the visuals for a perfect headline.

## 2. Read the mark

With a logo: follow the "Read the mark first" checklist in `references/motifs.md` (symmetry, construction, characteristic gesture, ends, weight). Write two or three sentences on how the mark tells the story. Users love hearing a true insight about their own logo, such as "it's one shape and its twin, holding each other", and that insight becomes the motif system.

**Don't alter the user's mark.** Rounding its ends, thinning it or redrawing it are suggestions for their designer; label them that way. A stroke-weight control is fine, because the geometry stays the same.

**No logo:** propose 2–3 simple marks built from the story's metaphor, using basic SVG primitives (strokes, arcs, rectangles), each with one line of reasoning. Mark them clearly as placeholders for a designer. Alternatively, offer a wordmark-only direction, where the name set heavy in the mono or header face does the work. Pick marks with rotational symmetry or a repeatable gesture, because they give you free motifs.

## 3. Round one: three directions in one board

Write `brand.json` with **three directions** that differ in feel, not just in hex values. For example: warm and crafted, industrial and precise, dark and technical. Each direction gets:

- **Fonts:** a header, body and mono face (plus an optional readout face) from `references/fonts.md`. Uncommon but functional. Check real weight ranges.
- **Colors:** a light and a dark palette with the same *roles*: paper, surface, ink, graphite, line, **primary** (the lead color for buttons and key moments), **accent** (a small secondary color). Decide deliberately which color leads. If the user's favorite is orange, orange is the primary; don't let the secondary color creep into buttons. Each direction also gets a proportion mix (for example paper 64, ink 16, primary 6, accent 1).
- **Radius** and button radius.
- `recommended: true` on your pick, with one line on why.

Shared across directions: the story, the mark, the wordmark settings, logo rules, and motifs (`include` built-ins plus 1–3 `custom` motifs drawn from the mark's gesture).

Build and check:

```bash
python scripts/build.py board brand.json board.html               # for publishing as an Artifact
python scripts/build.py board brand.json board.html --standalone  # for opening locally
```

`build.py` validates the JSON and refuses common mistakes. If an Artifact or preview tool is available, publish or open the board, look at it once, fix what's visibly broken, and share the link. Otherwise give the user the local file path.

## 4. Collect feedback in a structured way

Ask for reactions on five things at once. It's the fastest route to convergence:

1. **Mark and lockup:** does the name's weight match the mark? Keep the ends as they are?
2. **Fonts:** keep or replace the header, body and mono separately. Users often love the mono and body but not the header.
3. **Color:** which color leads? Is the accent too loud?
4. **Motifs:** keep, drop, or "don't understand where it goes".
5. **Overall feel:** which direction, or which mix.

Read their answer literally and generalize from it. "Too artistic" means the header needs to be more functional; "too popular" means uncommon picks; "the line is too thick" applies to every motif in context, not just the one they mentioned.

## 5. Round two: converge

Collapse to **one direction** built from their picks. If the mark weight is in question, show one or two stroke weights; for a mono wordmark, set the name one weight step lighter than looks right on paper. Show any alternatives side by side on the same page rather than in another round. Drop every motif they didn't like, and show the survivors in real layouts: a hero background, a loader inside a button, a quote, a footer band.

Stop iterating once the user says it's right. Polish they didn't ask for costs them tokens.

## 6. Deliver

1. The final board: publish it (Artifact) if possible, and also write a standalone copy into the project.
2. The brand kit: `python scripts/build.py kit brand.json <project>/brand` produces `logo/` (mark, icons and lockups in ink and paper), `tokens.css` (`--b-*` variables, light and dark, font import), `tokens.json` and `README.md`. Save `brand.json` alongside it so the brand can be rebuilt or extended later.
3. Mention that the lockup SVGs use live text and should be converted to outlines before print.
4. Offer a Figma export only if a Figma connection exists. Confirm whose account it is and which team to use before creating anything.

## Taste rules (why they matter)

- **Uncommon over trendy.** Users recognize Inter or Space Grotesk even when they can't name them, and the brand reads as a template.
- **Functional header.** A header font that fights the page is worse than a plain one.
- **Weight harmony.** The eye catches a mismatch between mark and wordmark instantly, even when the user can't explain what's wrong.
- **Blocky can be good.** Square, solid geometry reads as reliable. Don't soften a mark to make it "friendlier" unless asked.
- **Color with meaning.** Give each color a job (primary for action and key moments, accent for one semantic state). Show a proportion bar so nothing quietly takes over.
- **Motifs recede.** Thin, faint and small in context, with one accent each. The mark and headline carry the page.
- **Avoid the AI-generated look:** purple gradients, cream plus terracotta with a serif, glassmorphism, emoji section markers, rounded-everything, a lone neon pop on black.
- **Dark mode is designed, not inverted.** The template handles both themes from the two palettes; keep contrast legible in both.

## Files

- `assets/board-template.html`: the board renderer. Don't edit it per project; everything goes in brand.json.
- `assets/example-brand.json`: a complete example (Kraddle) showing every field.
- `scripts/build.py`: `board` and `kit` commands, plus validation.
- `references/fonts.md`: font roles, the overused list, uncommon picks by role, pairing rules.
- `references/motifs.md`: how to read a mark, the motif catalogue, rules for keeping motifs subtle.
