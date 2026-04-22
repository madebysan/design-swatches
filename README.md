<h1 align="center">Design Swatches</h1>
<p align="center">Portable visual identity for AI coding agents.</p>
<p align="center"><a href="https://designmd-gamma.vercel.app"><strong>Try it live →</strong></a></p>

![Design Swatches gallery](screenshot.png)

![Sanity design swatch in dark mode](screenshot-detail.png)

---

## The premise

If you work at a company and you want an AI coding agent to ship prototypes that *look like your product*, you have to hand it your design system. Most design systems live locked inside Figma libraries, Storybook instances, or design-tokens JSON — none of which paste cleanly into a chat with an LLM.

This is a research project to test how far you can push **design systems → markdown**: can the visual identity of a brand (colors, typography, components, depth, motion personality) be captured well enough in a single 9-section text file that an AI agent can rebuild a believable interface from it alone?

So far the answer is: **mostly yes**, with some compression. The 81-brand explorer in this repo exists to prove it.

## The skill

The actual product here is `skill/design-md/` — a Claude Code skill that produces a DESIGN.md from any URL. The intended use is on your own company's site:

```bash
cp -R skill/design-md ~/.claude/skills/
```

Then in any Claude Code session:

```
/design-md https://your-company.com
```

The skill scrapes design tokens via [dembrandt](https://github.com/dembrandt/dembrandt), picks 1–3 reference examples from the corpus to match the visual category, and writes a 9-section DESIGN.md you can drop into any agent context. Future prototypes built in that session land closer to your brand on the first try.

## The proof

Generating a DESIGN.md for one company doesn't tell you whether the format actually works. So the corpus has 81 examples — wildly different visual languages, all captured in the same template — and an explorer that lets you see them side-by-side.

```
design-swatches/
├── getdesign-corpus/    # 81 DESIGN.md files (~250–550 lines each)
└── explorer/            # Browsable visual catalog of all 81
    ├── index.html       # Filterable gallery (search, light/dark, by category & style)
    └── bentos/          # One HTML "swatch" per brand — colors, type, components
```

The explorer is **proof**, not a swipe file. The brands catalogued here describe public corporate visual identities and remain owned by their respective companies. If you find one inspiring, use it as a voice reference for your own DESIGN.md — not as something to copy literally into a product. That's why this repo is private.

## What's in a DESIGN.md

Each file follows the same 9-section structure:

1. Visual Theme & Atmosphere
2. Color Palette & Roles
3. Typography Rules
4. Component Stylings
5. Layout Principles
6. Depth & Elevation
7. Do's and Don'ts
8. Responsive Behavior
9. Agent Prompt Guide

The last section is the payload — copy-paste prompts an AI agent can use directly to build on-brand UI.

## Credits

- Most corpus files come from VoltAgent's [getdesign.md](https://getdesign.md) CLI
- Token extraction via [dembrandt](https://github.com/dembrandt/dembrandt)
- Iconify CDN for the icon previews

## License

The toolkit (skill, explorer, scripts) is [MIT](LICENSE). The DESIGN.md files describe public brand identities and remain owned by their respective companies — catalogued here for format research, not for redistribution or product use.

---

Made by [santiagoalonso.com](https://santiagoalonso.com)
