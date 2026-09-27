#!/usr/bin/env python3
"""Build a brand board and a brand kit from one brand.json.

  python build.py board brand.json out.html [--standalone]
      Inject brand.json into the board template. Use --standalone for a file that opens
      directly in a browser (adds doctype/head/body). Without it, the output is ready to
      publish as an Artifact (which adds its own skeleton).

  python build.py kit brand.json out_dir [--direction ID]
      Write logo SVGs, tokens.css, tokens.json and README.md for one direction
      (default: the first, or the one marked "recommended").

Only the standard library is used.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, '..', 'assets', 'board-template.html')


def load(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def check(b):
    """Catch the mistakes that silently break the board."""
    errs = []
    for k in ('name', 'brandLine', 'hero', 'mark', 'wordmark', 'directions'):
        if k not in b:
            errs.append(f'missing "{k}"')
    m = b.get('mark', {})
    if 'viewBox' not in m or 'svg' not in m:
        errs.append('mark needs "viewBox" and "svg" (inner markup)')
    elif 'currentColor' not in m['svg']:
        errs.append('mark.svg must paint with currentColor so it can switch between ink and paper')
    if re.search(r'(fill|stroke)="var\(', m.get('svg', '')):
        errs.append('mark.svg uses var() in an SVG attribute; use style="fill:var(--x)" instead')
    for d in b.get('directions', []):
        for k in ('id', 'name', 'fonts', 'colors'):
            if k not in d:
                errs.append(f'direction {d.get("id", "?")}: missing "{k}"')
        for mode in ('light', 'dark'):
            c = d.get('colors', {}).get(mode, {})
            for k in ('paper', 'surface', 'ink', 'graphite', 'line', 'primary', 'onPrimary', 'primaryTint', 'accent', 'accentTint'):
                if k not in c:
                    errs.append(f'direction {d.get("id")}: colors.{mode}.{k} missing')
        for k in ('header', 'body', 'mono'):
            if k not in d.get('fonts', {}):
                errs.append(f'direction {d.get("id")}: fonts.{k} missing')
    for c in (b.get('motifs') or {}).get('custom', []):
        if re.search(r'(fill|stroke)="var\(', c.get('svg', '')):
            errs.append(f'motif {c.get("name")}: var() inside an SVG attribute; move it into style=""')
    if errs:
        sys.exit('brand.json problems:\n  - ' + '\n  - '.join(errs))


def pick(b, did):
    ds = b['directions']
    if did:
        for d in ds:
            if d['id'] == did:
                return d
        sys.exit(f'no direction "{did}"')
    return next((d for d in ds if d.get('recommended')), ds[0])


def board(src, out, standalone):
    b = load(src)
    check(b)
    with open(TEMPLATE, encoding='utf-8') as f:
        t = f.read()
    t = re.sub(r'<!--.*?-->\s*', '', t, count=1, flags=re.S)
    data = json.dumps(b, ensure_ascii=False).replace('</', '<\\/')
    t = t.replace('/*BRAND_JSON*/', data).replace('__TITLE__', b.get('title') or f"{b['name'].capitalize()} Brand Board")
    if standalone:
        head, rest = t.split('<script id="brand"', 1)
        t = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
             '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
             + head + '</head>\n<body>\n<script id="brand"' + rest + '\n</body>\n</html>\n')
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(t)
    print('board ->', out)


def kit(src, out, did):
    b = load(src)
    check(b)
    d = pick(b, did)
    L, D = d['colors']['light'], d['colors']['dark']
    m, wm = b['mark'], b['wordmark']
    vx, vy, vw, vh = [float(x) for x in re.split(r'[\s,]+', m['viewBox'].strip())]
    os.makedirs(os.path.join(out, 'logo'), exist_ok=True)

    def paint(color):
        return m['svg'].replace('currentColor', color)

    def mark(color, bg=None, pad=0.18):
        s = max(vw, vh) * (1 + 2 * pad)
        x0, y0 = vx + vw / 2 - s / 2, vy + vh / 2 - s / 2
        rect = f'<rect x="{x0:.2f}" y="{y0:.2f}" width="{s:.2f}" height="{s:.2f}" fill="{bg}"/>' if bg else ''
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="{x0:.2f} {y0:.2f} {s:.2f} {s:.2f}">'
                f'{rect}{paint(color)}</svg>\n')

    wf = d['fonts'].get('wordmark') or d['fonts'][wm.get('role', 'mono')]
    fs = 100.0
    mh = float(str(wm.get('markHeight', '0.82em')).replace('em', '')) * fs
    gap = float(str(wm.get('gap', '0.32em')).replace('em', '')) * fs
    k = mh / vh
    mwid = vw * k
    textw = len(b['name']) * 0.62 * fs

    def lockup(color):
        w, h = mwid + gap + textw, fs * 1.2
        tr = wm.get('tracking', '-0.04em')
        ls = float(tr.replace('em', '')) * fs if tr.endswith('em') else 0
        name = b['name'].lower() if wm.get('transform') == 'lowercase' else b['name']
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.2f} {h:.2f}">'
                f'<g transform="translate(0 {h/2 - mh/2:.2f}) scale({k:.5f}) translate({-vx} {-vy})">{paint(color)}</g>'
                f'<text x="{mwid + gap:.2f}" y="{h/2 + 0.36*fs:.2f}" fill="{color}" font-family="{wf["family"]}, monospace" '
                f'font-weight="{wm.get("weight", 700)}" font-size="{fs:.0f}" letter-spacing="{ls:.1f}">{name}</text></svg>\n')

    n = b['name'].lower()
    files = {
        f'{n}-mark-ink.svg': mark(L['ink']),
        f'{n}-mark-paper.svg': mark(L['paper']),
        f'{n}-icon-ink.svg': mark(L['paper'], L['ink']),
        f'{n}-icon-paper.svg': mark(L['ink'], L['paper']),
        f'{n}-lockup-ink.svg': lockup(L['ink']),
        f'{n}-lockup-paper.svg': lockup(L['paper']),
    }
    for fn, c in files.items():
        with open(os.path.join(out, 'logo', fn), 'w', encoding='utf-8') as f:
            f.write(c)

    fonts = {r: d['fonts'][r]['family'] for r in ('header', 'body', 'mono', 'readout') if r in d['fonts']}
    tokens = {'name': b['name'], 'direction': d['id'], 'color': {'light': L, 'dark': D}, 'font': fonts,
              'wordmark': wm, 'radius': d.get('radius', '0px'), 'mix': d.get('mix')}
    with open(os.path.join(out, 'tokens.json'), 'w', encoding='utf-8') as f:
        json.dump(tokens, f, indent=2, ensure_ascii=False)
        f.write('\n')

    kebab = lambda s: re.sub(r'([A-Z])', lambda x: '-' + x.group(1).lower(), s)
    block = lambda c, ind: ''.join(f'{ind}--b-{kebab(k)}: {v};\n' for k, v in c.items())
    gf = [d['fonts'][r]['google'] for r in ('header', 'body', 'mono', 'readout') if r in d['fonts'] and d['fonts'][r].get('google')]
    stacks = {'serif': 'Georgia, serif', 'sans': "'Helvetica Neue', Arial, sans-serif", 'mono': 'ui-monospace, Consolas, monospace'}
    fontvars = ''.join(f"  --b-font-{r}: '{d['fonts'][r]['family']}', {stacks[d['fonts'][r].get('fallback', 'sans')]};\n"
                       for r in ('header', 'body', 'mono', 'readout') if r in d['fonts'])
    css = (f"/* {b['name']} brand tokens ({d['name']}) */\n"
           + (f"@import url('https://fonts.googleapis.com/css2?{'&'.join('family=' + g for g in gf)}&display=swap');\n\n" if gf else '')
           + ':root {\n' + block(L, '  ') + fontvars + f"  --b-radius: {d.get('radius', '0px')};\n}}\n\n"
           + '@media (prefers-color-scheme: dark) {\n  :root:not([data-theme="light"]) {\n' + block(D, '    ') + '  }\n}\n\n'
           + ':root[data-theme="dark"] {\n' + block(D, '  ') + '}\n')
    with open(os.path.join(out, 'tokens.css'), 'w', encoding='utf-8') as f:
        f.write(css)

    rules = '\n'.join(f'- {x}' for x in b.get('logoRules', []))
    rows = '\n'.join(f'| {k} | `{L[k]}` | `{D[k]}` |' for k in L)
    readme = f"""# {b['name']} brand

Open the brand board HTML for the full identity. Direction: **{d['name']}**.

## Mark
{b.get('markNote', '')}

{rules}

Lockup: name in {wf['family']} {wm.get('weight', 700)}, mark height {wm.get('markHeight', '0.82em')}, gap {wm.get('gap', '0.32em')}.
The lockup SVGs use live text; convert it to outlines before sending them anywhere the font isn't installed.

## Color
| Token | Light | Dark |
| --- | --- | --- |
{rows}

## Type
""" + '\n'.join(f'- {r.capitalize()}: {fam}' for r, fam in fonts.items()) + """

## Files
- `logo/`: mark, app icons and lockups in ink and paper.
- `tokens.css`: CSS variables (`--b-*`), light and dark, with the font import.
- `tokens.json`: the same values for other tools.
"""
    with open(os.path.join(out, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme)
    print('kit ->', out, sorted(os.listdir(os.path.join(out, 'logo'))))


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) < 3 or a[0] not in ('board', 'kit'):
        sys.exit(__doc__)
    if a[0] == 'board':
        board(a[1], a[2], '--standalone' in a)
    else:
        did = a[a.index('--direction') + 1] if '--direction' in a else None
        kit(a[1], a[2], did)
