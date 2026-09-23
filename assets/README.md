# Profile images

The profile loads these files from this repository, not a remote image-generation service.

## Neofetch header

Edit the profile fields and colors in `scripts/render-header.py`, then run:

```sh
python3 scripts/render-header.py
```

The script writes light and dark SVGs in desktop and mobile layouts. The main README selects a variant with `<picture>`. Keep the header's alt text in sync with its fields.

## Project previews

`projects.webp` contains public website screenshots captured on 2026-09-22. From left to right:

- Kintura: https://kintura.xyz
- GymGeist: https://freye.tech/gymgeist
- The Airlock: https://theairlock.space

Each screenshot was captured at 1440 × 1050, resized to 480 × 350, and placed side by side. The WebP is a static visual preview; the project descriptions and links remain ordinary text in the main README. It contains no private application screens or repository content.
