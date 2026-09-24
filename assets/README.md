# Profile images

The profile loads these files from this repository, not a remote image-generation service.

## Neofetch header

Edit the profile fields and colors in `scripts/render-header.py`, then run:

```sh
python3 scripts/render-header.py
```

The script writes light and dark SVGs in desktop and mobile layouts. The main README selects a variant with `<picture>`. Keep the header's alt text in sync with its fields.

## Social buttons

The same `python3 scripts/render-header.py` command writes light and dark variants of the Website, X, YouTube, and Instagram buttons. Colors and typography match the Neofetch header. Each image is 136 × 56 pixels, including transparent spacing, so the four links wrap into two rows on small screens.

The buttons are ordinary image links, so keyboard navigation and focus styling remain GitHub-native. GitHub does not allow custom link CSS in a README; the SVGs intentionally contain no hover scripts or animation.

Brand icons in `assets/icons/` come from [Simple Icons](https://github.com/simple-icons/simple-icons), distributed under [CC0 1.0](https://github.com/simple-icons/simple-icons/blob/develop/LICENSE.md). Their paths are embedded into the generated buttons, with no remote icon requests. Brand names and marks remain the property of their respective owners.

## Project previews

`projects.webp` contains public website screenshots captured on 2026-09-22. From left to right:

- Kintura: https://kintura.xyz
- GymGeist: https://freye.tech/gymgeist
- The Airlock: https://theairlock.space

Each screenshot was captured at 1440 × 1050, resized to 480 × 350, and placed side by side. The WebP is a static visual preview; the project descriptions and links remain ordinary text in the main README. It contains no private application screens or repository content.
