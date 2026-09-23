#!/usr/bin/env python3
"""Render the static profile headers: python3 scripts/render-header.py."""

from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, Liberation Mono, monospace"
MARK = (
    r"   ____  ______",
    r"  / __ \/ ____/",
    r" / / / / /_",
    r"/ /_/ / __/",
    r"\____/_/",
)
FIELDS = (
    ("Name", "Oskar Freye"),
    ("Home", "Dortmund, Germany"),
    ("Building", "draht / fr3n"),
    ("OS", "macOS + Arch"),
    ("Editor", "Neovim"),
    ("Code", "TypeScript, Go, Elixir"),
    ("", "Rust, Lua, Python, Dart"),
)
THEMES = {
    "dark": {
        "background": "oklch(0.18 0.008 165)",
        "text": "oklch(0.91 0.012 100)",
        "muted": "oklch(0.68 0.010 165)",
        "accent": "oklch(0.80 0.12 160)",
        "mark": "oklch(0.80 0.11 80)",
    },
    "light": {
        "background": "oklch(0.977 0.006 165)",
        "text": "oklch(0.28 0.014 165)",
        "muted": "oklch(0.46 0.015 165)",
        "accent": "oklch(0.38 0.09 160)",
        "mark": "oklch(0.42 0.09 70)",
    },
}
SWATCHES = (
    "oklch(0.34 0.015 165)",
    "oklch(0.67 0.15 25)",
    "oklch(0.76 0.12 160)",
    "oklch(0.80 0.11 80)",
    "oklch(0.70 0.12 250)",
    "oklch(0.72 0.12 325)",
    "oklch(0.80 0.09 205)",
    "oklch(0.91 0.012 100)",
)


def text(x, y, content, color, size, weight=400):
    return (
        f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" '
        f'font-weight="{weight}" xml:space="preserve">{escape(content)}</text>'
    )


def render(theme, mobile):
    colors = THEMES[theme]
    width, height = (360, 360) if mobile else (800, 320)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
        '<title id="title">Oskar Freye / neofetch</title>',
        '<desc id="description">Oskar Freye in Dortmund, Germany. Building draht and fr3n. '
        'Neovim on macOS and Arch. TypeScript, Go, Elixir, Rust, Lua, Python, and Dart.</desc>',
        f'<rect width="{width}" height="{height}" rx="6" fill="{colors["background"]}"/>',
        f'<g font-family="{FONT}">',
    ]
    if mobile:
        for index, line in enumerate(MARK):
            parts.append(text(16, 32 + index * 13, line, colors['mark'], 10.5))
        parts.extend([
            text(132, 39, 'oskar@freye', colors['accent'], 19, 600),
            text(132, 65, 'Oskar Freye', colors['text'], 15.5),
            text(20, 119, '$ neofetch', colors['muted'], 13),
        ])
        rows = FIELDS[1:]
        label_x, value_x, start_y, row_height = 20, 112, 153, 26
        label_size, value_size = 13, 15.5
        palette_x, palette_y, swatch_width = 112, 319, 23
    else:
        parts.append(text(30, 38, '$ neofetch', colors['muted'], 14))
        for index, line in enumerate(MARK):
            parts.append(text(27, 99 + index * 28, line, colors['mark'], 22))
        parts.extend([
            text(252, 42, 'oskar@freye', colors['accent'], 24, 600),
            text(252, 62, '----------------------------', colors['muted'], 14),
        ])
        rows = FIELDS
        label_x, value_x, start_y, row_height = 252, 370, 92, 27
        label_size, value_size = 15, 18
        palette_x, palette_y, swatch_width = 370, 286, 24

    for index, (label, value) in enumerate(rows):
        y = start_y + index * row_height
        if label:
            parts.append(text(label_x, y, label, colors['accent'], label_size, 600))
        parts.append(text(value_x, y, value, colors['text'], value_size))

    parts.append('</g>')
    parts.append('<g aria-hidden="true">')
    for index, color in enumerate(SWATCHES):
        parts.append(
            f'<rect x="{palette_x + index * swatch_width}" y="{palette_y}" '
            f'width="{swatch_width}" height="14" fill="{color}"/>'
        )
    parts.extend(['</g>', '</svg>', ''])
    return '\n'.join(parts)


def main():
    assets = ROOT / 'assets'
    assets.mkdir(exist_ok=True)
    for theme in THEMES:
        for mobile in (False, True):
            suffix = '-mobile' if mobile else ''
            target = assets / f'neofetch-{theme}{suffix}.svg'
            target.write_text(render(theme, mobile), encoding='utf-8')
            print(target.relative_to(ROOT))


if __name__ == '__main__':
    main()
