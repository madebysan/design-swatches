<h1 align="center">Design Swatches</h1>
<p align="center">Portable visual identity for AI coding agents.</p>
<p align="center"><a href="https://designmd.santiagoalonso.com"><strong>Try it live →</strong></a></p>

![Design Swatches gallery](screenshot.png)

![Sanity design swatch in dark mode](screenshot-detail.png)

---

## What this is

A corpus of 98 DESIGN.md files, one per real company, all in the same 9-section format. Plus a browsable gallery and the Claude Code skill that generated them.

AI coding agents produce generic UIs unless you hand them a detailed design system reference. Most design systems live locked inside Figma, Storybook, or tokens JSON, none of which paste cleanly into an LLM chat. DESIGN.md is the pasteable form: 9 sections of prose + tokens that describe a brand's visual identity well enough for an agent to rebuild a believable interface.

## What's inside

```
design-swatches/
├── getdesign-corpus/    # 98 DESIGN.md files (~250–550 lines each)
├── explorer/            # Browsable visual catalog of all 98
│   ├── index.html       # Filterable gallery (search, light/dark, by category & style)
│   └── bentos/          # One HTML "swatch" per brand
└── skill/design-md/     # Claude Code skill that generates new DESIGN.md files
```

## The skill

`skill/design-md/` is a Claude Code skill that produces a DESIGN.md from any URL. Point it at your own company's site:

```bash
cp -R skill/design-md ~/.claude/skills/
```

Then in any Claude Code session:

```
/design-md https://your-company.com
```

The skill pulls raw design tokens via [dembrandt](https://github.com/dembrandt/dembrandt), then uses Claude with 1–3 corpus files as voice references to write a structured 9-section DESIGN.md. The result drops into any agent context. Future prototypes built in that session land closer to your brand on the first try.

### How this relates to dembrandt

Dembrandt already has a `--design-md` flag that outputs a DESIGN.md directly. What this project adds is the corpus (98 files in a consistent format, written with a specific interpretive voice) and the prompting that produces new files in that same voice. Dembrandt is the scraper layer. It tells you `#f36458` appears 12 times. This layer is what calls that coral Sanity's singular brand accent, reserved for CTAs, and flips to electric blue on hover. Raw tokens in, AI-usable design brief out.

## The explorer

98 DESIGN.md files is a lot of text to scan. The explorer renders each one back into a visible "design swatch", hero typography, color palette, button variants, icon system, type specimens, so you can see the format's output side-by-side at scale. The 9-section format works across Ferrari, Notion, A24, Mercury Weather, and Claude. Wildly different visual priorities, same format.

The explorer is for reference, not for copying. The brands catalogued here describe public corporate visual identities and remain owned by their companies. Use them as voice references for your own DESIGN.md, not as something to lift into a product.

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

The last section is the payload: copy-paste prompts an AI agent can use directly to build on-brand UI.

## Credits

- Token extraction via [dembrandt](https://github.com/dembrandt/dembrandt)
- Most corpus files bootstrapped from VoltAgent's [getdesign.md](https://getdesign.md) CLI
- Iconify CDN for the icon previews in the explorer

## License

The toolkit (skill, explorer, scripts) is [MIT](LICENSE). The DESIGN.md files describe public brand identities and remain owned by their respective companies. Catalogued here as references, not for redistribution or product use.

---

Made by [santiagoalonso.com](https://santiagoalonso.com)
