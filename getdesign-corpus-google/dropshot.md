---
version: alpha
name: "Dropshot"
description: "Token-first design system reference for Dropshot."

colors:
  background: "#ffffff"
  surface: "#0066ff"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#c8c8cc"
  primary: "#0a0a0e"
  on-primary: "#ffffff"
  border: "#9a9aa2"
  focus-ring: "#0a0a0e"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Switzer, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Switzer, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Switzer, ui-sans-serif, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Switzer, ui-sans-serif, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Switzer, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Switzer, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Switzer, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Switzer, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
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

# Dropshot Design System

## Overview

Dropshot's website is a darkroom. The entire page sits on a near-black canvas (`#0a0a0e`) with no gradients, no marketing illustrations, no colorful section breaks — just a single saturated electric blue (`#0066ff`) used as the brand stamp on the CTA, a hairline of the same blue as a slider track, and white type centered over a real product UI panel. This is a tool's tool: a browser-based app for cinematic product shots, and the marketing site is staged like a render preview, not a homepage.

The defining typographic move is **two-tone hero copy**. The H1 reads "Cinematic product shots / in your browser." — line 1 in pure white at 48px Switzer weight 400, line 2 at the same size but dropped to a muted gray (`#9a9aa2`). One sentence, two visual weights, no enthusiasm. It's a designer's voice: declarative, precise, unimpressed with itself. Below sits a 14px Switzer paragraph in `#c8c8cc` and one electric blue pill button. The hero ends. There is no second CTA, no logo cloud, no "trusted by." The product UI mockup that follows is the actual app chrome — parameter sliders, mode toggles, post-processing labels in Roboto Mono — playing the role a product photo plays on a typical SaaS site.

What sets Dropshot apart is its **chrome vocabulary**. Parameter labels (`ATMOSPHERE`, `ILLUMINATION`, `COLOUR`, `POST-PROCESSING`) are set in Roboto Mono at 9–11px, weight 500–600, uppercase, with explicit pixel tracking. Body copy is Switzer with normal tracking. The split between sans for content and mono for chrome reads like professional creative software (Resolve, Cinema 4D, After Effects) — exactly the company Dropshot wants to keep. The watermark-scale `DROPSHOT` wordmark anchored at the page bottom in barely-visible gray (`#1e1e22`-on-`#0a0a0e`) is the closing seal — not a logo flex, a credit roll.

**Key Characteristics:**
- Near-black canvas (`#0a0a0e`) — darker than `#000`-with-noise, lighter than ink black
- Switzer at weight 400 for headings, weight 500 for buttons and emphasis — never weight 700
- Two-tone hero: white H1 line followed by gray (`#9a9aa2`) H1 line at the same size
- One color: electric blue `#0066ff` — applied to the primary pill CTA, slider track, "Live" tab, focus rings
- Roboto Mono uppercase labels (9–11px, +0.36–1.1px tracking) for parameter chrome and section markers
- 100px / 999px pill radius for CTAs; 3px or 14px radius everywhere else — no mid-range
- Soft glow shadow on the CTA (`rgba(0,102,255,0.2) 0 2px 20px`) — atmospheric, not stamped
- Faded watermark wordmark at page footer — `DROPSHOT` at near-viewport scale in `#1e1e22`
- Real product UI rendered into the page as evidence — sliders, tabs, color picker, all on-brand

## Colors

### Primary
- **Dropshot Ink** (`#0a0a0e`): Page background. Deeper than dark gray, warmer than pure black — has a tiny blue undertone in OKLCH. The canvas everything else is staged against.
- **Pure White** (`#ffffff`): Primary heading text, button label color, active tab text. The high-contrast top of the type scale.
- **Electric Blue** (`#0066ff`): The single brand accent. Reserved for primary CTA pill, "Live" toggle pill, slider fills, focus halos, and the loading-bar progress indicator.

### Surface Hierarchy (Dark Stack)
- **Surface 0** (`#0a0a0e`): Page canvas
- **Surface 1** (`#111111`): Section dividers / faintly raised panels
- **Surface 2** (`#1a1a1e`): Card backgrounds, inset panels
- **Surface 3** (`#1e1e22`): Elevated controls, watermark tone
- **Surface 4** (`#2a2a30`): Border color for floating panels and inputs — the standard "outline of a control" tone

### Text Tokens
- **Text Primary** (`#ffffff`): Headings, button labels, active state text
- **Text Mid** (`#9a9aa2` — `--g-text-mid`): Secondary heading line in the two-tone hero, parameter values
- **Text Secondary** (`#8e8e96` — `--g-text-sec`): Body paragraph color, FAQ question rows, tab inactive state
- **Text Muted** (`#c8c8cc`): Hero subtitle paragraph (slightly brighter than secondary)
- **Text Tertiary** (`#5c5c64`): Footer credit, microcopy, disabled states

### Brand Accent System
- **Accent Primary** (`#0066ff`): The signature blue — solid fills for CTAs and active controls
- **Accent Tint** (`rgba(74, 158, 255, 0.06)`): Tinted background for "Live" toggle in default state — 6% blue wash on a dark surface
- **Accent Hover Tint** (`rgba(74, 158, 255, 0.08)`): Slightly more saturated tint for hover/selected states
- **Accent Border** (`#4a9eff`): The lighter blue used as a 1px hairline on selected toggles
- **Accent Glow** (`rgba(0, 102, 255, 0.2)`): The soft halo behind the primary CTA — 20px blur, 2px Y-offset

### Borders
- **Border Default** (`#2a2a30`): Standard 1px panel/control border
- **Border Subtle** (`rgba(255, 255, 255, 0.07)`): Hairline divider between rows and sections
- **Border Faint** (`rgba(255, 255, 255, 0.1)`): Slightly stronger separator on tags and pill chrome
- **Border Accent** (`#4a9eff`): Selected/active state border on toggles

### Special-Purpose Colors
- **Color Picker Demo Swatches**: Vivid demo colors appear in the swatch picker UI (`#7c3aed`, `#5b7fff`, `#fa9e9e`, `#d4d4d8`, `#18181b`). These are **demo content, not brand tokens** — never bring them into chrome.

### Gradient System
- Dropshot is **gradient-free**. The only "gradient" is the soft glow shadow on the CTA — a 20px bloom of `#0066ff` at 20% opacity. No mesh gradients, no gradient text, no gradient borders.

## Typography

### Font Family
- **Primary**: `Switzer`, fallback: `-apple-system`, `system-ui`
- **Monospace / Chrome**: `Roboto Mono` — used exclusively for UI parameter labels and uppercase markers
- **System Fallback**: `ui-sans-serif`, `system-ui`, with emoji subsets

*Switzer is a free-tier sans by Indian Type Foundry (Fontshare). It's a contemporary geometric grotesk — neutral but slightly warmer than Inter, with open apertures. Roboto Mono is Google Fonts. Both load fast and have generous weight families.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Switzer | 48px (3.00rem) | 400 | 1.10 | -0.48px | H1 — two-tone, line 1 white / line 2 gray |
| Display Tight | Switzer | 48px (3.00rem) | 400 | 1.50 | -1.44px | Pull-quote / large statement variant |
| Section Heading | Switzer | 40px (2.50rem) | 400 | 1.10 | -1px | Section heads, "Questions?" |
| Sub-heading L | Switzer | 36px (2.25rem) | 400 | 1.15 | -0.9px | Feature group titles |
| Sub-heading | Switzer | 32px (2.00rem) | 400 | 1.25 | -0.64px | Sub-sections |
| Sub-heading S | Switzer | 28px (1.75rem) | 400 | 1.40 | normal | Compact section heads |
| Body Large | Switzer | 20px (1.25rem) | 500 | 1.50 | -0.2px | Pull quotes, emphasized paragraphs |
| Body | Switzer | 17px (1.06rem) | 400 | 1.50 | normal | Standard reading text |
| Body Compact | Switzer | 15px (0.94rem) | 400–500 | 1.50 | normal | Feature descriptions |
| Body Small | Switzer | 14px (0.88rem) | 400 | 1.50–1.60 | normal | Captions, supporting copy |
| Button | Switzer | 14px (0.88rem) | 500 | 1.50 | normal | CTA pill labels (also 16px variant) |
| Caption | Switzer | 13px (0.81rem) | 400–600 | 1.50 | normal | Metadata, FAQ rows |
| Caption Small | Switzer | 12px (0.75rem) | 400 | 1.50 | normal | Microcopy, footer |
| Mono Label | Roboto Mono | 11px (0.69rem) | 600 | 1.50 | 1.1px | UPPERCASE — parameter section markers (`ATMOSPHERE`) |
| Mono Caption | Roboto Mono | 12px (0.75rem) | 400 | 1.50 | 0.48px | Inline UI values, version tags (`v1.3`) |
| Mono Tag | Roboto Mono | 9px (0.56rem) | 400 | 1.50 | 0.72px | UPPERCASE — small tab labels, mode markers |
| Mono Button | Roboto Mono | 9px (0.56rem) | 500 | 1.50 | 0.36px | UPPERCASE — chrome buttons (`FREESHOT`, `DEVICE`) |

### Principles
- **Weight 400 is the ceiling for display**: Every heading from 28px to 48px runs at weight 400. Weight 500 only appears at button and emphasis size. No weight 600 or 700 in display copy — Dropshot communicates through restraint, not boldness.
- **Two-tone hero is the signature**: H1 splits across two lines, line 1 in `#ffffff` and line 2 in `#9a9aa2`. Declarative subject, muted predicate — that's the brand voice.
- **Negative tracking scales with size**: `-1.44px` at 48px tight variant, `-0.48px` at 48px standard, `-1px` at 40px, `-0.9px` at 36px, `-0.2px` at 20px. Below 17px tracking returns to normal.
- **Chrome speaks mono, content speaks sans**: Roboto Mono is reserved for UI parameter labels, section markers, version tags. Body copy never uses mono. This split is what makes the page read as professional creative software, not generic SaaS.
- **Mono is always uppercase at chrome sizes**: At 9–11px, Roboto Mono runs uppercase with explicit pixel tracking (`0.36px` to `1.1px`). At 12px+ it can sit mixed case with tighter tracking.

## Layout

### Spacing System
- Base unit: 4px / 8px hybrid — scale visible at 4, 5, 6, 8, 14, 24, 56, 80, 120, 160
- Notable: heavy use of 5–7px micro-spacing for chrome (parameter row gaps), 24px for card padding, 80–120px for section breaks. The `14px` value is unusually frequent (radius and spacing both) — a deliberate "off-grid" mid-tone.
- Mid-range gaps (32–56px) appear sparingly. Dropshot either sits tight (chrome) or breathes wide (sections).

### Grid & Container
- Hero: left-aligned single column, max width ~720px for headline cluster
- Product UI mockup: full-bleed with generous side padding — the canvas + controls span ~1200px on desktop
- Feature row: 3-column grid below the product UI — `Multiple devices` / `Runs in a browser` / `Export 4K` over `Depth of field` / `Private by default` / `Live recording`
- FAQ: centered single column with `Questions?` heading, ~600px wide, full-width hairline dividers
- Footer: 2-row layout — copyright + email left, link list right

### Whitespace Philosophy
- **Vertical patience**: enormous blank gaps between sections (often 200–400px on desktop) — the page reads slowly on purpose
- **Hero economy**: the H1 + subtitle + CTA cluster is tight (24–32px gaps), but everything around it has room to breathe
- **Footer reveal**: the watermark wordmark only appears once you've scrolled through the entire page — the payoff for patience

### Border Radius Scale
- `3px`: Default for small controls, swatches, tabs — the workhorse "barely rounded" radius
- `6px`: Slightly softer chrome (links, inline controls)
- `14px`: Card corners, larger panel containers — the signature "soft corner"
- `100px` / `999px`: Pill CTAs, version pill, circular toggle buttons
- `50%`: Slider thumb, circular indicators
- **Avoid**: 8px, 10px, 12px, 16px — Dropshot's radius scale is intentionally non-standard. The jump from 6px to 14px is the brand.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text |
| Hairline (Level 1) | `1px solid rgba(255, 255, 255, 0.07)` | Row dividers, FAQ separators |
| Surface Step (Level 2) | Surface tone shift (`#1a1a1e` over `#0a0a0e`) | Cards, raised panels — depth via tone, not shadow |
| Bordered Panel (Level 3) | Surface tone + `1px solid #2a2a30` | Floating UI chrome, the product mockup itself |
| Brand Glow (Level 4) | `rgba(0, 102, 255, 0.2) 0 2px 20px` | Primary CTA only — the page's single bloom |
| Thumb Halo (Level 5) | `rgba(255,255,255,0.314) 0 0 10px, rgba(255,255,255,0.15) 0 0 0 2px` | Active slider thumb — focus indicator |
| Ambient Gloss (Level 6) | Multi-layer: white core + violet/blue side-lobe + tiny glow | Decorative product-shot light effect inside the app — not for marketing chrome |

**Shadow Philosophy**: Dropshot's depth is **tonal first, glow second**. Elevation comes from cycling through the dark surface stack (`#0a0a0e` → `#111111` → `#1a1a1e` → `#1e1e22`) — there's no drop shadow on cards. The single exception is the brand glow under the CTA, a soft 20px blue bloom that announces interactivity without simulating physical lift. No card ever gets a generic "0 4px 12px black" shadow — that's the SaaS-default Dropshot is rejecting.

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

**Primary Pill (Electric)**
- Background: Electric Blue (`#0066ff`)
- Text: Pure White (`#ffffff`)
- Padding: `0px 24px` (compact) or `0px 20px` (smaller)
- Height: ~40px
- Radius: `100px` (pill)
- Border: `0`
- Shadow: `rgba(0, 102, 255, 0.2) 0px 2px 20px 0px` — soft blue glow
- Outline (focus): `oklab(0.708 0 0 / 0.5) none 3px`
- Font: 14px Switzer weight 400, mixed case ("Try it for free", "Buy Dropshot")
- Use: Hero CTA, pricing CTA, navigation CTA — the only blue button on the page

**Tinted Pill (Active Toggle)**
- Background: `rgba(74, 158, 255, 0.06)` (6% blue tint over surface)
- Text: Pure White (`#ffffff`)
- Padding: `5px 10px`
- Radius: `0` for tab variant; `100px` for pill toggle variant
- Border: bottom hairline `1px solid rgba(74, 158, 255, …)` for selected-tab state
- Font: 16px Switzer weight 500
- Use: Active state of `Live` / `Image` / `Path` toggle group inside the product UI chrome

**Mono Chrome Button** (`FREESHOT`, `DEVICE` mode markers)
- Background: transparent or `rgba(74, 158, 255, 0.08)` when active; text White or `#4a9eff` when active
- Padding: `5px 0`; bottom-border only — `0 0 1px solid #4a9eff` when selected
- Font: 9px Roboto Mono weight 500, UPPERCASE, tracking `0.36px`

**Ghost Pill (Nav)** (`How it works`, `Features`, `Pricing`, `FAQ`, `Compare`, `Changelog`)
- Transparent background; text White active, `#8e8e96` inactive; radius matches surrounding pill geometry

### Cards & Containers
- Background: Surface 2 (`#1a1a1e`) for cards, Surface 1 (`#111111`) for raised panels
- Border: `1px solid #2a2a30` for default panels, `1px solid rgba(255,255,255,0.07)` for subtle dividers
- Radius: `14px` for cards, `3px` for inline controls and small tags, `100px` only for pills
- Internal padding: 24–32px for content cards; 14–16px for chrome panels
- Shadow: usually `none` — depth comes from surface tone, not blur

### Tags & Pills

**Version Pill (Hero Eyebrow)**
- Background: `rgba(255, 255, 255, 0.06)` or Surface 2
- Text: White with mono prefix — `v1.3` in Roboto Mono followed by `Ambient backgrounds, pixel grid and bokeh` in Switzer 13px
- Padding: ~6px 14px
- Radius: `999px` (pill)
- Border: `1px solid rgba(255, 255, 255, 0.1)`
- Trailing arrow icon (→) at 12px
- Use: The release-note pill above the H1 — the page's only "what's new" surface

**Inline Mono Tag**
- Background: transparent
- Text: Roboto Mono 9px weight 600, UPPERCASE, tracking `0.72px`
- Use: Parameter section markers (`ATMOSPHERE`, `ILLUMINATION`, `COLOUR`)

### Inputs & Sliders

**Slider** (all numeric controls — `Key`, `Fill`, `Rim`, `Primary Direction`)
- Track: 3–4px tall, `#222228` background with `#0066ff` fill on the left portion
- Thumb: 14px white circle, `1px solid #2a2a30`, `50%` radius
- Active glow: `rgba(255,255,255,0.314) 0 0 10px, rgba(255,255,255,0.15) 0 0 0 2px`

**Color Swatch Picker**: 14px square, `3px` radius, `1px solid #2a2a30` — vivid demo fills, never brand tokens

### Navigation
- Top bar: full-width, transparent over Ink canvas, ~60px tall
- Left: leaf-shaped Dropshot mark in white at ~24px
- Center: 6 ghost links + 1 separator dot (`#0066ff` 4px circle as decorative beat)
- Right: single Electric Blue pill CTA (`Try it for free`)
- Hover: link color shifts from `#ffffff` to `#8e8e96` (or vice versa for inactive default)
- No dropdowns except `Compare ↓` which expands a small panel

### Decorative Elements

**Watermark Wordmark**: `DROPSHOT` at near-viewport-width scale, heavy display weight, `#1e1e22` on `#0a0a0e`. Anchored to the page bottom, sometimes cropped at the viewport edge — reads as a film-credit reveal.

**Loading Bar**: centered 1px track, ~120px wide, `#0066ff` fill on `rgba(255,255,255,0.06)` background. Preserves the "this is software" feeling even before paint.

## Do's and Don'ts

### Do
- Use Switzer at weight 400 for every heading — weight 500 only appears at button-size and emphasized body
- Build the hero as **two-tone**: white H1 line followed by `#9a9aa2` H1 line at the same size
- Reserve `#0066ff` for one element per screen — the primary CTA, full stop
- Apply the soft blue glow (`rgba(0,102,255,0.2) 0 2px 20px`) **only** to the primary pill CTA
- Use Roboto Mono UPPERCASE at 9–11px with explicit pixel tracking for parameter labels and section markers
- Layer surfaces from `#0a0a0e` to `#1e1e22` for depth — no drop shadows on cards
- Use `100px` pill radius for CTAs, `14px` for cards, `3px` for chrome — skip everything in between
- Treat the product UI as the hero illustration — show real sliders, real labels, real controls
- Anchor the page footer with a near-viewport-scale `DROPSHOT` watermark in `#1e1e22`
- Let mid-range pixels (5px, 7px, 14px) appear in spacing — Dropshot isn't on a strict 8px grid

### Don't
- Don't use weight 600 or 700 on Switzer headings — the brand's quiet
- Don't use pure black (`#000000`) for the page background — it must be `#0a0a0e` (warm-cooled near-black)
- Don't add a second accent color — the system is monochrome + electric blue, period
- Don't use blurred drop shadows on cards or panels — depth is tonal
- Don't use mid-range radii (8px, 10px, 12px) — Dropshot's radius scale is binary-plus-pill
- Don't put body copy in Roboto Mono — mono is for chrome and parameter labels only
- Don't use mono in lowercase at chrome sizes — 9–11px mono is always UPPERCASE with letter-spacing
- Don't add gradient fills, glassmorphism, or noise textures — surfaces are flat color
- Don't lean on emoji or illustrated icons — small line icons (16px) at most, paired with mono labels
- Don't soften the H1 with marketing adjectives — the voice is declarative, two clauses, no exclamation

---

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, hero H1 drops to ~32–36px, stacked CTA, hide center nav (hamburger) |
| Tablet | 640–1024px | Hero stays single-column, product UI mockup shrinks proportionally, 2-column feature grid |
| Desktop | 1024–1440px | Full layout — 6-link nav, 3-column feature grid, full product UI panel |
| Large Desktop | ≥1440px | Hero left-aligned in a ~720px column, watermark wordmark spans full viewport width |

### Touch Targets
- Primary pill CTA: 40px min height, 24px horizontal padding. Nav links: 44px tap height. Slider thumbs: 14px visual but ~32px hit area on touch.

### Collapsing Strategy
- **Nav**: 6 horizontal links collapse to hamburger; blue CTA pill stays visible at top-right
- **Hero H1**: 48px → 36px → 32px progressive scaling, two-tone treatment maintained at every size
- **Product UI**: shrinks proportionally on tablet, becomes a side-scrollable card on mobile rather than collapsing parameters
- **Feature grid**: 3-col → 2-col → 1-col, mono section labels stay uppercase at every breakpoint
- **Section spacing**: 200px+ desktop → 80px mobile — compresses but preserves the "patient" pace
- **Watermark**: scales with viewport width and stays visible at the page bottom on mobile

### Image / UI Behavior
- Product UI panel maintains aspect ratio; chrome labels never reflow
- Slider tracks shorten but thumb size stays constant
- Mono parameter labels never truncate or wrap — they're treated as fixed-width chrome

---

## Agent Prompt Guide

### Quick Color Reference
- Page Background: Dropshot Ink (`#0a0a0e`)
- Primary CTA: Electric Blue (`#0066ff`)
- CTA Glow: `rgba(0, 102, 255, 0.2) 0px 2px 20px 0px`
- Heading Primary: Pure White (`#ffffff`)
- Heading Secondary (two-tone H1 line 2): `#9a9aa2`
- Body Text: `#8e8e96` (secondary) or `#c8c8cc` (subtitle)
- Card Surface: `#1a1a1e`
- Panel Border: `#2a2a30`
- Hairline Divider: `rgba(255, 255, 255, 0.07)`
- Active Tint: `rgba(74, 158, 255, 0.06)`
- Watermark Tone: `#1e1e22`

### Example Component Prompts
- "Create a hero on `#0a0a0e` with a two-tone H1 — line 1 'Cinematic product shots' in `#ffffff`, line 2 'in your browser.' in `#9a9aa2`. Both 48px Switzer weight 400, line-height 1.10, letter-spacing -0.48px. Below: a 14px Switzer body in `#c8c8cc`, then a single Electric Blue (`#0066ff`) pill CTA — 14px weight 400 white text, `100px` radius, padding `0 24px`, soft glow `rgba(0,102,255,0.2) 0 2px 20px`."
- "Build a parameter panel card — background `#1a1a1e`, `1px solid #2a2a30`, `14px` radius, internal padding 24px. Section label 'ATMOSPHERE' in Roboto Mono 11px weight 600 uppercase, letter-spacing 1.1px, color `#8e8e96`. Below: a row of swatch tags with `3px` radius and `1px solid #2a2a30`."
- "Design a horizontal slider with a 1px track in `#222228`, a `#0066ff` fill on the left portion, and a 14px white circular thumb (`#ffffff`, `1px solid #2a2a30`, `50%` radius) with a focus halo `rgba(255,255,255,0.314) 0 0 10px, rgba(255,255,255,0.15) 0 0 0 2px`."
- "Create a version pill — `999px` radius, `1px solid rgba(255,255,255,0.1)`, padding 6px 14px. Inside: 'v1.3' in Roboto Mono 12px weight 400 letter-spacing 0.48px, then a 13px Switzer label, then a 12px arrow glyph."
- "Add a footer watermark — the word 'DROPSHOT' at ~80vw font-size in `#1e1e22` on `#0a0a0e`, weight 700 grotesk, anchored to the bottom of the page, no animation."

### Iteration Guide
1. Default to Switzer weight 400 for headings — weight 500 only at button and emphasis size
2. Hero is two-tone: white line followed by `#9a9aa2` line, same size, no extra ornament
3. Electric Blue (`#0066ff`) is sacred — one CTA per screen, with the soft glow shadow
4. Layer surfaces tonally (`#0a0a0e` → `#111` → `#1a1a1e` → `#1e1e22`) — never reach for drop shadows
5. Roboto Mono UPPERCASE at 9–11px with explicit pixel tracking is the chrome voice — body stays in Switzer
6. Radius is binary-plus-pill: `3px` for chrome, `14px` for cards, `100px`/`999px` for pills. Skip 8–12px.
7. Ink (`#0a0a0e`) is the canvas — never use pure black, never use a near-white inversion
8. Show real product UI, not stock illustrations — sliders and parameter labels are the brand
9. Close the page with a near-viewport-scale watermark wordmark in `#1e1e22` — the credit roll
