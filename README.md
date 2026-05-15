<h1>Design Swatches</h1>

<p>Portable visual identity for AI coding agents.<br>
183-brand Google design.md corpus with a browsable explorer and a Claude Code skill.</p>

<p>
  <img src="https://img.shields.io/badge/JavaScript-f7df1e" alt="JavaScript">
  <img src="https://img.shields.io/badge/HTML-e34f26" alt="HTML">
  <img src="https://img.shields.io/badge/YAML-cb171e" alt="YAML">
</p>

<p><a href="https://designmd.santiagoalonso.com">Live site</a></p>

![Design Swatches gallery](screenshot.png)

A corpus of 183 DESIGN.md files, one per real company, converted to Google's token-first `design.md` format. Plus a browsable gallery and the Claude Code skill that generated them.

The premise: AI coding agents produce generic UIs unless you hand them a detailed design system reference. Most design systems live locked inside Figma, Storybook, or tokens JSON, none of which paste cleanly into an LLM chat. DESIGN.md is the pasteable form: structured tokens plus prose that describe a brand's visual identity well enough for an agent to rebuild a believable interface from it alone.

![Sanity design swatch in dark mode](screenshot-detail.png)

## What's inside

```
design-swatches/
├── getdesign-corpus-google/   # 183 DESIGN.md files in Google design.md format (YAML + markdown, lint-validated)
├── getdesign-corpus/          # legacy prose-only corpus, kept as source/reference
├── explorer/                  # Browsable visual catalog of 167 rendered swatches
│   ├── index.html             # Filterable gallery (search, light/dark, by category & style)
│   └── bentos/                # One HTML "swatch" per rendered brand
└── skill/design-md/           # Claude Code skill that generates new DESIGN.md files
```

## The skill

`skill/design-md/` is a Claude Code skill that produces a DESIGN.md from any URL. The intended use is on your own company's site:

```bash
cp -R skill/design-md ~/.claude/skills/
```

Then in any Claude Code session:

```
/design-md https://your-company.com
```

The skill pulls raw design tokens via [dembrandt](https://github.com/dembrandt/dembrandt), then uses Claude with 1–3 corpus files as voice references to write a structured DESIGN.md in [Google's official `design.md` format](https://github.com/google-labs-code/design.md): YAML token block plus markdown rationale, validated with `npx @google/design.md lint`. The result drops cleanly into any agent context, and the tokens can be exported downstream.

### How this relates to dembrandt

Dembrandt already has a `--design-md` flag that outputs a DESIGN.md directly. What this project adds on top is the **corpus** (183 files in a consistent Google-compatible format, written with a specific interpretive voice) and the **exemplar-based prompting** that produces new files in that same voice. Dembrandt is the scraper layer. It tells you `#f36458` appears 12 times. This layer is what calls that coral Sanity's singular brand accent, reserved for CTAs, and flips to electric blue on hover. Raw tokens in, AI-usable design brief out.

## The explorer

183 DESIGN.md files is a lot of text to scan. The explorer renders 167 of them back into visible "design swatches": hero typography, color palette, button variants, icon system, type specimens. That it holds across Ferrari, Notion, A24, Mercury Weather, and Claude, with wildly different visual priorities, is the evidence that the format is doing real work.

The explorer is for reference, not for copying. The brands catalogued here describe public corporate visual identities and remain owned by their companies. Use them as voice references for your own DESIGN.md — not as something to lift into a product. That's why this repo is private.

## What's in a DESIGN.md

Each Google-format file has two layers:

**YAML front matter** (machine-readable tokens):
- `colors` — opaque 6-digit hex, organized by role
- `typography` — named tokens with fontFamily, fontSize, fontWeight, lineHeight, letterSpacing
- `spacing` — brand-appropriate scale
- `rounded` — radius scale
- `components` — variants with token references like `{colors.primary}`

**Markdown body**:
1. Overview
2. Colors
3. Typography
4. Layout
5. Elevation & Depth
6. Shapes
7. Components
8. Do's and Don'ts
9. Responsive Behavior
10. Agent Prompt Guide

The Agent Prompt Guide is the payload: copy-paste prompts an AI agent can use directly to build on-brand UI.

## Credits

- Token extraction via [dembrandt](https://github.com/dembrandt/dembrandt)
- Format spec: [Google's `design.md`](https://github.com/google-labs-code/design.md)
- Most corpus files bootstrapped from VoltAgent's [getdesign.md](https://getdesign.md) CLI
- Iconify CDN for the icon previews in the explorer

## License

The toolkit (skill, explorer, scripts) is [MIT](LICENSE). The DESIGN.md files describe public brand identities and remain owned by their respective companies — catalogued here as references, not for redistribution or product use.

---

Made by [santiagoalonso.com](https://santiagoalonso.com)
