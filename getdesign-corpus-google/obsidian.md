---
version: alpha
name: "Obsidian"
description: "Token-first design system reference for Obsidian."

colors:
  background: "#ffffff"
  surface: "#a882ff"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#7c5cff"
  primary: "#0f0f0f"
  on-primary: "#ffffff"
  border: "#1f1f1f"
  focus-ring: "#0f0f0f"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 33px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  4xl: 96px

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 16px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.background}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    borderColor: "{colors.focus-ring}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  badge:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
---

# Obsidian Design System

## Overview

Obsidian's website is a researcher's notebook rendered in software: a dark canvas, a single saturated purple, and product imagery that puts the knowledge graph and markdown editor at the center of every story. The page opens on near-black (`#0F0F0F`) — not the trendy off-charcoal of contemporary developer tools, but a deliberate "vault interior" black that lets the violet accent (`#a882ff`) and the bright graph-node visualizations carry the entire visual hierarchy. Where most knowledge tools chase Notion's airy whiteboard aesthetic, Obsidian leans into the opposite frame: lights off, focus on, your own private workspace.

The brand voice is indie-craft software through and through. There's no marketing photography, no founder portraits, no abstract gradients filling negative space. Instead, the page is laid out like a feature tour — every section is anchored by a real screenshot of the app, often with the file pane, editor, and graph view all visible at once. The signature purple (`#a882ff`) appears as a soft glow on the diamond logo, as the active-link accent, and as the highlight color inside the syntax-highlighted markdown previews. It functions less as a brand stamp and more as an interior light source — purple is what you see when you're inside the vault.

Typography is Inter throughout, set in a tight functional hierarchy with confident sans-serif headlines (`Sharpen your thinking.`, `Spark ideas.`, `Sync securely.`). Display sizes run heavy (semibold to bold) — a deliberate counterweight to the lightness of the surrounding space. The headline-as-imperative pattern (verb + period) gives the page a documentation rhythm rather than a marketing one. Every section's title reads like a chapter heading in a manual, which is exactly the audience self-image Obsidian is selling: you are someone who reads manuals, who likes systems, who builds.

**Key Characteristics:**
- Near-black canvas (`#0F0F0F`) — vault-interior dark, not generic charcoal
- Single saturated purple accent (`#a882ff`) used as logo glow, links, and code-token color
- Inter throughout at semibold-to-bold display weights — confident, technical, no tricks
- Product screenshots embedded directly into layout — graph view, editor, file tree all visible
- Knowledge-graph imagery as the signature decorative element — radial node clusters
- Tight feature-tour rhythm — each section is title + screenshot + 2-line caption
- Soft purple glow on icons and graph nodes — atmospheric without being a gradient
- No founder photos, no testimonial portraits — the app IS the hero

## Colors

### Primary
- **Vault Black** (`#0F0F0F`): Page canvas. The defining surface — every section sits on this. Reads as "inside the app at night."
- **Surface Charcoal** (`#1F1F1F`): Card and panel backgrounds. One step up from canvas, used for feature tiles, code blocks, and screenshot frames.
- **Pure White** (`#ffffff`): Primary heading and body text on dark surfaces. High contrast — Obsidian does not soften its primary text.

### Brand Accent
- **Obsidian Purple** (`#a882ff`): The signature color — used for the diamond logo gradient, link highlights, code-token strings, active states, and hero CTA backgrounds. Lavender-leaning, never magenta.
- **Deep Violet** (`hsl(258, 88%, 66%)` / `#7c5cff`): The CTA fill — a darker, more saturated cousin of the lavender, used on primary buttons ("Get Obsidian", "Download", "Sign up").
- **Purple Glow** (`rgba(168, 130, 255, 0.15)`): Soft halo behind the diamond logo and around active graph nodes.

### Syntax / Semantic Palette
Obsidian's markdown rendering uses a full retro-tooling palette inside code and tag previews — these read as decorative accents rather than UI states.
- **Code Yellow** (`#e0de71`): Function tokens, headings in markdown previews
- **Code Green** (`#44cf6e`): Strings, success states
- **Code Red** (`#fb464c`): Operators, danger states, delete actions
- **Code Pink** (`#fa99cd`): Keywords, special tokens
- **Code Cyan** (`#53dfdd`): Properties, links in editor preview
- **Code Orange** (`#e9973f`): Important markers, warnings
- **Code Blue** (`#027aff`): External links, system blue

### Neutrals & Text
- **Pure White** (`#ffffff`): Headlines, body text on dark
- **Text Muted** (`rgba(255, 255, 255, 0.65)`): Secondary copy, captions, feature subtitles
- **Text Faint** (`rgba(255, 255, 255, 0.35)`): Tertiary text — code comments, footer microcopy, timestamps

### Surface & Borders
- **Border Faint** (`rgba(255, 255, 255, 0.08)`): Default 1px hairlines on cards and section dividers
- **Border Visible** (`rgba(255, 255, 255, 0.16)`): Hover-state borders, input outlines
- **Border Active** (`rgba(168, 130, 255, 0.4)`): Focus rings and active-card outlines

### Semantic States
- **Success** (`#16a34a` text on `rgba(34, 197, 94, 0.1)` fill): Confirmation toasts
- **Danger** (`#dc2626` text on `rgba(239, 68, 68, 0.1)` fill): Destructive actions, errors

### Gradient System
- **Logo Gradient**: Purple-to-violet diamond fill (`#a882ff` → `#7c5cff`) with a soft inner glow
- **Hero Backdrop**: Subtle radial gradient from `rgba(168, 130, 255, 0.06)` at hero center fading to pure `#0F0F0F` at edges — creates the "ambient lamp" feel without ever reading as a marketing gradient

## Typography

### Font Family
- **Primary**: `Inter`, with system fallback: `ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Roboto, "Helvetica Neue", Arial, sans-serif`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace` — used for code blocks, syntax previews, and terminal-style microcopy
- **OpenType Features**: Standard tabular numerals on pricing tables and version numbers; `cv11` (single-story `a`) optional for a more technical reading

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Inter | 64px (4.00rem) | 700 | 1.05 | -0.02em | "Sharpen your thinking." opener |
| Display Section | Inter | 48px (3.00rem) | 700 | 1.10 | -0.02em | "Spark ideas.", "Sync securely.", "Publish instantly." |
| Display Small | Inter | 36px (2.25rem) | 700 | 1.15 | -0.015em | Sub-section heads in feature tours |
| Heading L | Inter | 28px (1.75rem) | 600 | 1.20 | -0.01em | Card titles, pricing tier names |
| Heading M | Inter | 22px (1.375rem) | 600 | 1.25 | -0.01em | Feature tile heads |
| Heading S | Inter | 18px (1.125rem) | 600 | 1.30 | normal | Sub-feature labels, list headings |
| Body Large | Inter | 18px (1.125rem) | 400 | 1.55 | normal | Hero tagline, intro paragraphs |
| Body | Inter | 16px (1.00rem) | 400 | 1.55 | normal | Standard reading copy, FAQ answers |
| Body Small | Inter | 14px (0.875rem) | 400 | 1.50 | normal | Captions, feature descriptions, footer text |
| Nav Link | Inter | 15px (0.9375rem) | 500 | 1.00 | normal | Top-nav items |
| Button | Inter | 15px (0.9375rem) | 600 | 1.00 | normal | Primary and secondary CTAs |
| Caption | Inter | 13px (0.8125rem) | 500 | 1.40 | 0.01em | Micro-labels, "Free without limits" eyebrows |
| Code Inline | JetBrains Mono / SF Mono | 14px (0.875rem) | 400 | 1.50 | normal | Inline code, file paths, hotkeys |

### Principles
- **Bold display, regular body**: Headlines run at 700 weight to anchor each section against the dark canvas. Body copy stays at 400 — there is no mid-weight body voice. The contrast between heavy heading and light body creates the "manual chapter" rhythm.
- **Verb-period headlines**: Section heads are imperative-mood single sentences ending with a period. Cape uses lightness as confidence; Obsidian uses declarative structure as confidence.
- **Tight negative tracking on display**: -0.02em at hero, scaling to -0.01em at heading sizes. Body returns to normal tracking for readability at 16px and below.
- **Inter as the workhorse**: One typeface across every weight and size. No display alternative, no specialty cuts. Discipline is the brand voice — Inter at the right weight does every job.
- **Monospace as decoration**: Obsidian leans into mono type for hotkeys, file paths, frontmatter examples, and "Made for typists" microcopy. Mono signals the technical-craft audience without screaming it.

## Layout

### Spacing System
- Base unit: 4px
- Scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128px
- Notable: tight inside cards (12–24px) and generous between sections (96–128px). The contrast lets each feature section read as its own chapter.

### Grid & Container
- Max content width: 1200px centered
- Hero: full-width with centered content, max text column 720px
- Feature grid: 2-column on desktop (large tiles), 3-column on plugin/theme grids (small tiles)
- Screenshot sections: text + screenshot in 2-column split, screenshot frequently overflows its column for emphasis
- Footer: 5-column link grid + brand strip

### Whitespace Philosophy
- **Manual-chapter pacing**: Each major feature gets a full section with 96–128px above and below. Within sections, copy stays tight (16–24px between paragraphs) — like a well-typeset page.
- **Screenshot-led rhythm**: Sections lead with the screenshot, followed by 1–2 sentences of caption. Text never carries a section alone; the product image does.
- **No decorative breathing room**: Unlike Cape's editorial-magazine pacing, Obsidian fills space with product detail. Whitespace is structural, not atmospheric.

### Border Radius Scale
- Sharp (0px): full-bleed sections, dividers
- Small (4px): inline pills, tag chips
- Medium (8px): buttons, inputs, small cards
- Large (12px): feature tiles, screenshot frames, modal sheets
- Pill (9999px): status badges, avatar crops
- Mid-range (16–24px) avoided — Obsidian stays in the 8/12 zone for software-tool consistency

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text, hero typography |
| Hairline (Level 1) | `1px solid rgba(255,255,255,0.08)` | Default card borders, section dividers |
| Card Lift (Level 2) | `1px solid rgba(255,255,255,0.16)` (no shadow) | Hover state on feature tiles |
| Screenshot Drop (Level 3) | `0 24px 64px rgba(0,0,0,0.5)` | Hero product screenshots, only |
| Purple Halo (Level 4) | `0 0 0 3px rgba(168,130,255,0.25)` + glow | Focus rings on inputs, active CTA states |
| Logo Glow (Level 5) | `0 0 60px rgba(168,130,255,0.2)` radial | Diamond logo, marquee graph nodes — atmospheric only |

**Shadow Philosophy**: Obsidian's depth system is binary — most elements sit flat against the canvas with only a hairline border for definition, while a small set of marquee elements (the hero screenshot, the diamond logo, focused inputs) get a soft purple-tinted glow. The signal is "ambient lamp inside a dark room" rather than Material's stacked-paper elevation. There are no neutral drop shadows — every shadow is either pure black (for screenshot lift) or purple-tinted (for state).

### Decorative Depth
- Glow effects pair with the diamond logo and graph-node visualizations to create an "internal light source" feeling
- Hairline borders do most of the structural work — depth comes from contrast (`#1F1F1F` cards on `#0F0F0F` canvas), not lift
- Avoid adding mid-level shadows; Obsidian's system is flat-or-glow, no in-between

## Shapes

The complete radius scale is declared in the `rounded:` token block above.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Hard-edged brand moments and flush layouts |
| `sm` | 4px | Small controls and tight UI details |
| `md` | 8px | Inputs and compact interface elements |
| `lg` | 16px | Cards and larger containers |
| `pill` | 9999px | CTAs, chips, and rounded badges |

## Components

### Buttons

**Primary Violet**
- Background: Deep Violet (`#7c5cff`)
- Text: Pure White (`#ffffff`)
- Padding: 12px 20px standard, 14px 24px large
- Radius: `8px`
- Border: none
- Shadow: `0 1px 2px rgba(0,0,0,0.3), 0 0 0 1px rgba(168,130,255,0.2)` — subtle ring suggests glow
- Font: Inter 15px weight 600
- Hover: background lightens to `#8c6dff`, shadow grows to `0 0 0 3px rgba(168,130,255,0.25)`
- Use: Primary CTA — "Get Obsidian for Windows", "Download now", "Sign up"

**Ghost / Secondary**
- Background: transparent
- Text: Pure White (`#ffffff`)
- Border: `1px solid rgba(255,255,255,0.16)`
- Radius: `8px`
- Padding: 12px 20px
- Hover: border brightens to `rgba(255,255,255,0.32)`, background fills to `rgba(255,255,255,0.04)`
- Use: "More platforms", "Learn more", secondary CTAs alongside primary

**Tertiary Link**
- Background: none
- Text: Obsidian Purple (`#a882ff`)
- Underline: appears on hover only
- Use: "Read documentation", inline "Learn more" links inside paragraph copy

### Cards & Containers

**Feature Tile**
- Background: Surface Charcoal (`#1F1F1F`)
- Border: `1px solid rgba(255,255,255,0.08)`
- Radius: `12px`
- Padding: 24px–32px
- Shadow: none — depth comes from the background contrast against `#0F0F0F`
- Hover: border brightens to `rgba(255,255,255,0.16)`, no movement
- Use: feature grid tiles ("Links", "Graph", "Canvas", "Plugins", "Themes")

**Screenshot Frame**
- Background: Surface Charcoal (`#1F1F1F`)
- Border: `1px solid rgba(255,255,255,0.06)`
- Radius: `12px`
- Padding: 0 — screenshot bleeds to frame edge
- Shadow: `0 24px 64px rgba(0,0,0,0.5)` — heavy ambient lift on hero screenshots only
- Use: every product screenshot in the page (editor, graph, canvas, sync UI)

### Badges / Tags / Pills

**Eyebrow Label**
- Background: transparent
- Text: Obsidian Purple (`#a882ff`)
- Font: Inter 13px weight 500, `letter-spacing: 0.06em`, often uppercase
- Use: section eyebrows ("FREE WITHOUT LIMITS", "WHAT'S NEW")

**Status Pill**
- Background: `rgba(168,130,255,0.12)`
- Text: Obsidian Purple (`#a882ff`)
- Padding: 4px 10px
- Radius: `9999px`
- Font: Inter 12px weight 500
- Use: "New", "Beta", version flags

### Inputs & Forms
- Background: Surface Charcoal (`#1F1F1F`)
- Border: `1px solid rgba(255,255,255,0.12)`
- Radius: `8px`
- Padding: 10px 14px
- Font: Inter 15px weight 400, color `#ffffff`
- Placeholder: `rgba(255,255,255,0.35)`
- Focus: border shifts to `#a882ff`, plus `0 0 0 3px rgba(168,130,255,0.25)` halo
- Use: search, email signup, settings inputs in Sync/Publish flows

### Navigation
- Top nav: horizontal dark bar matching `#0F0F0F` canvas, 60px height (90px before scroll), left-aligned diamond logo + wordmark, right-aligned "Download", "Pricing", "Sync", "Publish", "Enterprise"
- Links: Inter 15px weight 500, `rgba(255,255,255,0.75)` default
- Hover: text brightens to pure white (`#ffffff`)
- Active: text shifts to Obsidian Purple (`#a882ff`)
- Sticky behavior: sticks to top, height collapses from 90px → 60px on scroll
- Mobile: collapses to hamburger; menu opens as full-screen panel on `#0F0F0F`

### Decorative Elements

**Knowledge Graph Cluster**
- Radial node-and-edge SVG rendered in Obsidian Purple (`#a882ff`) on `#0F0F0F`
- Nodes: small filled circles 4–10px diameter, sized by importance
- Edges: 1px hairlines at `rgba(168,130,255,0.4)`
- Optional soft glow halo (`rgba(168,130,255,0.15)`) on hub nodes
- Use: hero illustration, plugin/canvas section accents — the signature visual metaphor

**Diamond Logo Glow**
- Purple-to-violet gradient fill (`#a882ff` → `#7c5cff`)
- Radial halo `rgba(168,130,255,0.2)` at 60px blur behind logo
- Always paired with the wordmark "Obsidian" in Inter weight 600
- Used in nav, footer, hero diamond accent block

**Grain Overlay**
- Subtle PNG noise grain at low opacity over hero backgrounds — adds analog texture without being a "paper" treatment
- Sourced from `--grain` CSS variable (data URI)

## Do's and Don'ts

### Do
- Use `#0F0F0F` for the page canvas — vault-interior black, not generic charcoal
- Apply Obsidian Purple (`#a882ff`) sparingly — logo, links, code highlights, focus states
- Use Inter at weight 700 for display headlines — bold confidence is the brand voice
- Pair every feature section with a real product screenshot — the app is the hero
- Use Surface Charcoal (`#1F1F1F`) for cards and tiles — one step up from canvas
- End section headlines with a period — declarative manual-chapter rhythm
- Use 1px hairline borders (`rgba(255,255,255,0.08)`) instead of drop shadows for card definition
- Embed knowledge-graph visualizations as decorative accents — purple nodes on dark
- Use monospace type for hotkeys, file paths, and technical microcopy
- Keep eyebrow labels uppercase with `0.06em` letter-spacing in Obsidian Purple

### Don't
- Don't use pure black (`#000000`) for the canvas — `#0F0F0F` reads warmer and more "interior"
- Don't introduce a second brand color — purple is the only chromatic accent
- Don't use light/airy hero illustrations — Obsidian's hero is always a dense product screenshot
- Don't apply mid-range border radius (16–24px) — stick to 8px or 12px
- Don't use Material-style stacked drop shadows — depth comes from glow or hairline only
- Don't soften body text below `rgba(255,255,255,0.65)` for primary copy — readability first
- Don't lighten display weight below 600 — Obsidian's headlines are bold by design
- Don't use stock photography or founder portraits — the page is product imagery only
- Don't add gradient washes to backgrounds — purple glows are atmospheric, not decorative gradients
- Don't break the monochrome+purple system with secondary accent colors outside the syntax palette

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero drops to 36px, screenshots stack |
| Mobile | 375–640px | Single-column, 40–48px hero, full-width buttons |
| Tablet | 640–1024px | 2-column feature grids appear, 48–56px hero |
| Desktop | 1024–1280px | Full multi-column layouts, 56–64px hero |
| Large Desktop | ≥1280px | Maximum scale (64px hero), 1200px max container |

### Touch Targets
- Primary CTAs: minimum 44px tap height, full-width on mobile
- Nav links: 48px tap height on mobile menu, 36px desktop
- Card tiles: entire tile is tappable, not just the link

### Collapsing Strategy
- **Nav**: Horizontal links collapse to hamburger below 1024px; menu opens as full-screen panel on `#0F0F0F` with stacked Inter 18px weight 500 links
- **Hero**: 64px → 48px → 36px progressive scale; tagline drops to 16px, CTAs stack vertically
- **Feature grid**: 2-column → 1-column at 768px; 3-column plugin grid → 2-column → 1-column
- **Screenshots**: text + screenshot side-by-side becomes screenshot-on-top, text-below at 768px
- **Section spacing**: 128px desktop → 64px mobile — preserves chapter-pacing feel
- **Footer**: 5-column → 2-column at 768px → 1-column at 480px

### Image Behavior
- Product screenshots maintain native aspect ratio at all breakpoints (no cropping)
- Knowledge-graph SVGs simplify on mobile — fewer visible nodes, no edge labels
- Diamond logo scales but never becomes an icon-only mark
- Screenshot frames maintain 12px radius and 1px hairline border across all sizes

---

## Agent Prompt Guide

### Quick Color Reference
- Page Background: Vault Black (`#0F0F0F`)
- Card Background: Surface Charcoal (`#1F1F1F`)
- Primary Text: Pure White (`#ffffff`)
- Muted Text: `rgba(255,255,255,0.65)`
- Brand Accent: Obsidian Purple (`#a882ff`)
- Primary CTA Fill: Deep Violet (`#7c5cff`)
- Hairline Border: `rgba(255,255,255,0.08)`
- Focus Halo: `0 0 0 3px rgba(168,130,255,0.25)`
- Screenshot Drop: `0 24px 64px rgba(0,0,0,0.5)`

### Example Component Prompts
- "Create a dark hero on `#0F0F0F` with a 64px Inter weight 700 headline ending with a period (`Sharpen your thinking.`), 18px weight 400 tagline in `rgba(255,255,255,0.65)`. Add a primary CTA filled `#7c5cff`, 8px radius, white text Inter 15px weight 600, plus a ghost secondary with `1px solid rgba(255,255,255,0.16)` border."
- "Build a feature tile on `#1F1F1F` with `1px solid rgba(255,255,255,0.08)` border, 12px radius, 32px padding. Title in Inter 22px weight 600 white, body in 16px weight 400 muted white. Add a small purple icon (`#a882ff`) in the top-left."
- "Render a knowledge graph illustration: 12–20 small filled purple circles (`#a882ff`) at 4–10px diameter, connected by 1px hairlines at `rgba(168,130,255,0.4)`, on a `#0F0F0F` background. Add a soft `rgba(168,130,255,0.15)` glow behind the central hub node."
- "Design a screenshot frame: 12px radius, `1px solid rgba(255,255,255,0.06)` border, `0 24px 64px rgba(0,0,0,0.5)` drop shadow on `#0F0F0F` canvas. Screenshot bleeds to frame edge with no inner padding."
- "Create an eyebrow label: uppercase Inter 13px weight 500, `letter-spacing: 0.06em`, color `#a882ff`, no background, sitting 12px above its section headline."
- "Build a status pill — `rgba(168,130,255,0.12)` background, `#a882ff` text, Inter 12px weight 500, `9999px` radius, 4px 10px padding."

### Iteration Guide
1. Default to `#0F0F0F` page canvas — never pure black, never charcoal-gray
2. Inter weight 700 for all display headlines, weight 400 for body — no mid-weight body voice
3. Obsidian Purple (`#a882ff`) is sacred — logo, links, code highlights, focus only. Never fill large surfaces with it.
4. Card definition through `1px solid rgba(255,255,255,0.08)` hairlines, not drop shadows
5. Real product screenshots anchor every feature section — no abstract illustrations
6. Border radius: 8px for buttons/inputs, 12px for tiles/frames, never 16–24px
7. Section headlines end with a period — `Spark ideas.`, `Sync securely.`, `Publish instantly.`
8. Glow effects are purple-tinted only — neutral drop shadows are reserved for screenshots
9. Pair monospace type with hotkeys, file paths, frontmatter — signals the technical-craft audience
10. Vertical pacing: 96–128px between sections, 16–24px inside paragraphs — manual-chapter rhythm
