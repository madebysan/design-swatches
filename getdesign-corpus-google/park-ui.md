---
version: alpha
name: Park UI
description: Tokens-first framework-agnostic design system built on Radix Themes scales, Outfit at weight 700, with `4px` workhorse radii and dual-layer shadow definition.

colors:
  # Canvas
  background: "#fcfcfc"
  surface: "#ffffff"

  # Neutral scale (Radix neutral)
  neutral-1: "#fcfcfc"
  neutral-2: "#f9f9f9"
  neutral-3: "#f0f0f0"
  neutral-6: "#d9d9d9"
  neutral-8: "#8d8d8d"
  neutral-9: "#8f8f8f"
  neutral-11: "#646464"
  neutral-12: "#202020"

  # Ink
  ink: "#202020"
  ink-inverted: "#ffffff"
  text-secondary: "#646464"
  text-muted: "#8d8d8d"

  # Brand / primary (neutral-solid)
  primary: "#000000"
  on-primary: "#ffffff"

  # Accent scales (selectable per theme)
  jade-9: "#29a383"
  indigo-6: "#c1d0ff"
  ruby-9: "#e93d82"
  crimson-9: "#e93d82"

  # Translucent fills flattened
  subtle-bg: "#f0f0f0"  # was rgba(0,0,0,0.06) — flattened over white
  subtle-bg-hover: "#e6e6e6"  # was rgba(0,0,0,0.1) — flattened
  violet-tint: "#ededfd"  # was rgba(68,0,238,0.06) — flattened
  amber-hover: "#ffeba1"  # was rgba(255,212,0,0.39) — flattened

  # Borders
  border: "#d9d9d9"

  # Shadow tints
  shadow-soft: "#d9d9d9"  # was rgba(0,0,0,0.15) — flattened approx
  shadow-hairline: "#cdcdcd"  # was rgba(0,0,0,0.19) — flattened approx

typography:
  display:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1.2px
  h1:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.96px
  h2:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0px
  h3:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0px
  body-large:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0px
  caption:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  code:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px

rounded:
  none: 0px
  sm: 2px
  md: 4px
  lg: 6px
  pill: 9999px

components:
  # Solid primary button
  button-solid:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 0px 12px

  # Subtle button
  button-subtle:
    backgroundColor: "{colors.subtle-bg}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 0px 12px
  button-subtle-hover:
    backgroundColor: "{colors.subtle-bg-hover}"
    textColor: "{colors.ink}"

  # Outline button
  button-outline:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 0px 12px

  # Ghost button
  button-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 0px 12px

  # Card
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 0px 12px

  # Badge
  badge:
    backgroundColor: "{colors.subtle-bg}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: 2px 8px

  # Dropdown / menu
  menu:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 8px

  # Switch (track)
  switch:
    backgroundColor: "{colors.neutral-6}"
    rounded: "{rounded.pill}"
    padding: 2px
---

# Park UI Design System

## Overview

Park UI is the design system for the agentic era — three-framework-compatible (React, Solid, Vue), tokens-first, aggressively neutral. The homepage is a showroom of components on a pure white canvas (`{colors.surface}`) with near-black text (`{colors.ink}`) and zero brand color in the chrome. This is the "Radix Themes with muscle" aesthetic — crisp borders, `4px` radii, Outfit display type, and a philosophy that the design system IS the tokens, not the components.

Typography is **Outfit** across the board — the same geometric sans-serif DaisyUI uses, but at weight 700 for display (not 900) with `-1.2px` letter-spacing. The 20px+ type uses weight 600 or 400 exclusively — no in-between weights, no weight 500. This two-weight simplicity is deliberate: Park UI wants components to compose cleanly, which means typography must be predictable.

The defining technical choice is Park UI's **595 CSS variables**. The scan found a massive token vocabulary — every Radix color scale (12 tones × 14 hues × light + dark + alpha), every spacing value, every radius, every elevation — all defined as custom properties. Components reference tokens like `--colors-neutral-solid-bg` or `--colors-jade-9`, never hex. This is the Radix Themes token system adopted wholesale into Panda CSS.

**Key Characteristics:**
- Outfit typeface, weight 700 at display — geometric, clean
- `4px` dominant radius — tighter than DaisyUI, consistent with Radix
- Built on Ark UI (headless primitives) + Panda CSS (compile-time CSS)
- 595 CSS variables — Radix Themes scale wholesale
- Framework-agnostic: React, Solid, Vue from one source
- Neutral-first palette (gray/black/white) — accent via Radix hues (jade, violet, ruby)
- No custom brand color — you bring your own
- Pill buttons absent — Park UI uses `{rounded.md}` even on buttons

## Colors

Park UI ships the full **Radix Themes** palette — 14 color scales (gray, mauve, slate, sage, olive, sand, red, orange, amber, yellow, green, teal, jade, cyan, blue, indigo, violet, purple, plum, pink, crimson, ruby, tomato, brown, bronze, gold) each with 12 steps (1-12) in both light + dark + alpha variants.

### Core Neutral (default theme)
- **Neutral 1** (`{colors.neutral-1}`): Page background.
- **Neutral 2** (`{colors.neutral-2}`): Subtle surface.
- **Neutral 3** (`{colors.neutral-3}`): Element background.
- **Neutral 6** (`{colors.neutral-6}`): Strong border.
- **Neutral 8** (`{colors.neutral-8}`): Subtle text, muted foreground.
- **Neutral 9** (`{colors.neutral-9}`): Solid backgrounds, badges.
- **Neutral 11** (`{colors.neutral-11}`): Secondary text.
- **Neutral 12** (`{colors.neutral-12}`): Primary text — near-black.

### Solid Role
- **Neutral Solid BG** (`{colors.primary}`): Primary buttons, active indicators.

### Accent Scales (examples — selectable per theme)
- **Jade 9** (`{colors.jade-9}`): Green accent.
- **Indigo 6** (`{colors.indigo-6}`): Light indigo border.
- **Ruby 9** (`{colors.ruby-9}`): Destructive accent (if theme is ruby).
- **Crimson 9** (`{colors.crimson-9}`): Alternative destructive hue.
- **Violet Tint** (`{colors.violet-tint}`): Flattened approx of 6% violet alpha for subtle tints.
- **Amber Hover** (`{colors.amber-hover}`): Flattened approx of 39% amber for warning hovers.

## Typography

### Font Family
- **Primary**: `Outfit`, fallback: `ui-sans-serif, system-ui, sans-serif`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, monospace`
- Park UI uses only ONE typeface family across the entire system — Outfit everywhere except code blocks.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display` | Hero, billboard headlines |
| `h1` | Page titles |
| `h2` | Section titles |
| `h3` | Sub-section heads, card titles |
| `body-large` | Lead paragraphs |
| `body` | Standard reading text |
| `button` | Button labels |
| `caption` | Small metadata |
| `code` | Inline code, snippets |

### Principles
- **Two-weight system**: 400 for body, 600 for UI text and headings, 700 for display — no 500, no 800, no in-between.
- **Outfit everywhere**: Park UI commits to Outfit throughout — only code blocks use ui-monospace.
- **Conservative tracking**: Letter-spacing stays at `-1.2px` max — less aggressive than Stripe or shadcn.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 4px with `xl` (24px) the dominant value.

### Grid & Container
- 12-column Tailwind/Panda grid
- `xl` section padding
- `lg` gutter gap

### Whitespace Philosophy
Park UI uses generous-but-controlled spacing — more breathing room than shadcn (which sits at 4-10px workhorses) but tighter than Material (which sits at 24-48px). The scale is calibrated for component-showroom layouts.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow | Page background |
| Subtle | `0 1px 2px {colors.shadow-soft}, 0 0 1px {colors.shadow-hairline}` | Card at rest (dual hairline) |
| Hover | `0 4px 8px {colors.shadow-soft}` | Card hover |
| Elevated | `0 8px 16px {colors.shadow-soft}` | Popovers, dropdowns |

**Shadow Philosophy**: Park UI follows Radix Themes' dual-layer shadow pattern — a soft outer shadow for atmospheric depth + a `1px` near-shadow for crisp edge definition. This prevents fuzzy-edged cards while keeping the lift soft.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Edge-to-edge sections |
| `sm` | 2px | Small inline elements, kbd |
| `md` | 4px | Buttons, inputs, badges — the workhorse |
| `lg` | 6px | Cards, dropdowns |
| `pill` | 9999px | Avatars, switches, the occasional pill |

The 4px radius is the Park UI rhythm — never pill, never sharp.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly.

### Buttons
- **`button-solid`** — Black fill, white text, 4px radius. The default CTA.
- **`button-subtle`** — Translucent neutral fill (`{colors.subtle-bg}`).
- **`button-outline`** — White surface with `1px solid {colors.border}`.
- **`button-ghost`** — Transparent on default, `{colors.subtle-bg}` on hover.

### Cards
- **`card`** — White surface, hairline border, 6px radius, dual-layer shadow.

### Inputs
- **`input`** — White surface with hairline border, 4px radius, 36px height. Focus brings a 2px outline-offset.

### Badges & Menus
- **`badge`** — 4px radius (not pill), translucent neutral fill, caption type.
- **`menu`** — White surface, 6px radius, popover-grade shadow.

### Switch
- **`switch`** — 32x16 pill track with 12px white thumb.

## Do's and Don'ts

### Do
- Use Radix color tokens — never hardcoded hex
- Default to `{rounded.md}` (4px) for buttons/inputs, `{rounded.lg}` (6px) for cards
- Use the two-weight Outfit system (400 body, 600 UI/headings)
- Apply dual-layer shadows — outer glow + 1px inner definition
- Pick one accent scale per theme (jade, violet, ruby) — don't mix

### Don't
- Don't use pill radius (`{rounded.pill}`) on buttons — Park UI is `4px`
- Don't use weight 500 — it's not in the two-weight system
- Don't mix multiple accent scales in one theme — disruptive
- Don't override individual tokens — swap the scale at the `[data-theme]` level
- Don't use vibrant color combinations — Park UI is neutral-first

---

## Responsive Behavior

*(Preserved from original 9-section format — Google's parser keeps unknown sections.)*

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| sm | `640px+` | 2-column card grids |
| md | `768px+` | 3-column features |
| lg | `1024px+` | Full desktop, docs sidebar |
| xl | `1280px+` | Max-width applies |

### Touch Targets
- Buttons: `36px` minimum (height via Radix sizing)
- Icon buttons: `36px × 36px`

### Collapsing Strategy
- Hero: 60px → 40px → 32px
- Sidebar: visible → collapsible → drawer
- Cards: 3-col → 2-col → stacked

---

## Agent Prompt Guide

*(Preserved from original 9-section format — the copy-paste payload section.)*

### Quick Color Reference (default neutral theme)
- Background: `{colors.background}` (neutral-1)
- Surface: `{colors.surface}`
- Text: `{colors.ink}` (neutral-12)
- Muted text: `{colors.text-secondary}` (neutral-11)
- Border: `{colors.border}` (neutral-6)
- Primary solid: `{colors.primary}`

### Example Component Prompts
- "Create a hero: white bg. Headline at 60px Outfit weight 700, letter-spacing -1.2px, line-height 1.10, color `{colors.ink}`. Subtitle at 20px Outfit weight 400 color `{colors.text-secondary}`. Solid button: `{colors.primary}` bg, white text, 4px radius, 0 24px padding, 36px height, 14px Outfit weight 600."
- "Design a card: white bg, 1px solid `{colors.border}`, 6px radius, 24px padding, dual-layer shadow `{colors.shadow-soft}`. Title at 24px Outfit weight 600. Body at 16px weight 400 color `{colors.text-secondary}`."
- "Build a subtle button: `{colors.subtle-bg}` bg, `{colors.ink}` text, 4px radius, 0 12px padding, 36px height, 14px Outfit weight 600. Hover: `{colors.subtle-bg-hover}`."

### Iteration Guide
1. Radix tokens are the source of truth — never hardcode colors
2. `4px` radius for interactive elements, `6px` for containers — the Park UI rhythm
3. Two-weight typography (400/600) — resist weight 500
4. Dual-layer shadows (outer + 1px inner) — keeps card edges crisp
5. Pick ONE accent scale per theme — neutral + jade, neutral + violet, never both
6. Button height is always `36px` — sized through Radix's size scale
