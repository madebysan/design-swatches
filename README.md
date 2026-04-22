# designmd

A design-system exploration toolkit built around the **DESIGN.md** format — portable visual identity for AI coding agents.

**The problem:** AI coding agents produce generic-looking UIs unless you hand them a detailed design system reference.

**What's here:** an 81-brand corpus of real-company DESIGN.md files, a visual explorer for browsing them, and the `/design-md` skill for generating new ones from any URL.

![Design Swatches gallery](screenshot.png)

---

## What's inside

```
designmd/
├── README.md
├── getdesign-corpus/          # 81 real-company DESIGN.md files
├── explorer/                  # Visual catalog of all 81 brands
│   ├── index.html             # Gallery — search, filter, light/dark
│   ├── bentos/                # One HTML "design swatch" per brand
│   └── thumbnails/            # PNG previews for the gallery
└── skill/
    └── design-md/             # The skill that generated the corpus
        ├── SKILL.md
        └── references/
            ├── template.md         # 9-section DESIGN.md template
            └── corpus-pointer.md   # How to use the corpus as exemplars
```

---

## The explorer

Open `explorer/index.html` in your browser. You'll see 81 brand "design swatches" — one per real company — that you can search, filter (by category or style), and toggle between light/dark. Each swatch shows:

- Hero typography personality + CTA language
- 8 brand colors with names and hex
- Typography specimens (display, heading, body, caption with actual specs)
- 3 button variants
- Icon system (Lucide, Solar, Material Symbols, etc. via Iconify)
- Card, form, FAQ, shadow samples
- Link to the full DESIGN.md

Brands cover: tech (Stripe, Linear, Vercel, Notion, Figma, Claude), luxury autos (Ferrari, Lamborghini, Bugatti, BMW, Tesla), retail (Apple, Nike, Starbucks, Airbnb), media (Wired, The Verge, A24, Spotify), AI labs (Cohere, ElevenLabs, Mistral, Anthropic), finance (Mastercard, Revolut, Binance, Coinbase, Wise), dev tools (Warp, Raycast, HashiCorp, Supabase), craft tools (Things, Arc, Fey, Granola, Ivory, Mercury Weather), and more.

---

## The corpus

`getdesign-corpus/` holds 81 DESIGN.md files, each a 250–550-line document following a consistent 9-section template:

1. Visual Theme & Atmosphere
2. Color Palette & Roles
3. Typography Rules
4. Component Stylings
5. Layout Principles
6. Depth & Elevation
7. Do's and Don'ts
8. Responsive Behavior
9. Agent Prompt Guide

Most come from VoltAgent's [getdesign.md](https://getdesign.md) CLI. The rest were generated locally with [dembrandt](https://github.com/dembrandt/dembrandt) for token extraction + Claude for the prose.

---

## The skill

`skill/design-md/` is the Claude Code skill that produces a new DESIGN.md from any URL. To use it locally:

```bash
cp -R skill/design-md ~/.claude/skills/
```

Then in any Claude Code session: `/design-md https://example.com` — it scrapes tokens, picks 1-3 corpus exemplars to match style, and writes a 9-section DESIGN.md.

## License

[MIT](LICENSE)

---

Made by [santiagoalonso.com](https://santiagoalonso.com)
