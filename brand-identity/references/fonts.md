# Choosing fonts

Engineers ask for "unique", then reject fonts that are loud. What they usually want is **uncommon but functional**: a face they haven't seen on ten other product sites, which still does its job quietly. Each role has a different job.

## Roles

- **Header.** Carries personality, but has to work as a headline, not as a poster. If it looks like it belongs on an album cover or a wedding invitation, it's too artistic. A good test is to set a full sentence, not one word, at 44px.
- **Body.** Readable at 16–18px for paragraphs. Friendly and quiet. Needs at least 400 and 600 or 700.
- **Mono.** The product's "system voice": logs, status, file paths, the agent talking. For developer products this role often ends up carrying the brand, and the wordmark is often set in it.
- **Readout** (optional). A dot-matrix or pixel face for counters and status, like a display on hardware. Used sparingly.

## Overused right now (avoid unless the user asks)

Inter, Inter Tight, Space Grotesk, Space Mono, Geist, Geist Mono, Manrope, Poppins, DM Sans, DM Mono, Plus Jakarta Sans, Outfit, Sora, Satoshi, General Sans, Bricolage Grotesque, Instrument Sans, Instrument Serif, Fraunces, Newsreader, Playfair Display, IBM Plex (reads as IBM), Archivo, Chivo, Syne, Unbounded. JetBrains Mono is common but well liked, so it's an acceptable fallback mono.

## Uncommon picks by role (all on Google Fonts)

Verify each is still available and check its real weight range before using it: a single-weight font set bold gets fake-bolded by the browser and looks broken.

**Header, serif:** Young Serif (warm and chunky, single weight 400), Hedvig Letters Serif (sharp, single weight), Gloock (high contrast, single weight), Petrona, Libre Caslon Display.
**Header, sans:** Host Grotesk (300–800), Schibsted Grotesk (400–900, dense and serious), Geologica (100–900, technical), Radio Canada Big (400–700), Encode Sans with wdth ~112 (wide and hardware-like), Sofia Sans (narrow and efficient), Atkinson Hyperlegible Next (200–800, distinctive), Rethink Sans, Funnel Display (300–800, cut-in shapes), Anybody (wdth 50–150; only at extreme width for a hardware look, since wide caps can feel "too display").
**Body:** Afacad (400–700, humanist), SUSE (100–800), Funnel Sans, Onest, Gantari, Hanken Grotesk (a little common), Hedvig Letters Sans (400 only, so it can't be bolded).
**Mono:** Azeret Mono (100–900, calm and open; heavy weights make a strong wordmark), Martian Mono (wide, interface-oriented), Kode Mono (400–700, squarish, lots of character), Spline Sans Mono, Fragment Mono, Reddit Mono, Sometype Mono.
**Readout:** Doto (dot matrix, 100–900), Handjet (modular), Workbench, DotGothic16.

## Pairing rules

- Contrast the header and body in one dimension only: serif vs sans, or wide vs normal. Don't vary everything at once.
- The mono should share the product's temperament. A calm product gets Azeret; a gritty product gets Kode.
- Keep it to three families (plus an optional readout face). Using one family for both header and body is fine for disciplined, industrial directions.
- **Wordmark weight has to match the mark's visual weight.** Compare the mark's stroke thickness with the letter stems at the lockup size. A heavy mark next to a regular-weight name reads as a mismatch and makes people uneasy even when they can't say why. For mono wordmarks, one weight step lighter than a "matched" guess usually looks equal, because mono letters are denser. Single-weight serifs only match a mark at one stroke thickness.

## How to show fonts on the board

Large "Aa", the family name set in the font itself, the full alphabet, the available weights, and a real sentence from the product. Label each card HEADER, BODY or MONO. If the roles aren't labelled clearly, users say "I don't see any header font" even when it's on the page.

For the final choice, a header shortlist helps: 6–8 cards, each showing the same real headline plus the wordmark plus a mono line, with switches for the mono and for light or dark.
