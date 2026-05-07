---
version: alpha
name: Carbon Design System
description: IBM's enterprise design system — sharp 0px corners everywhere, IBM Plex Sans at weight 300 display, IBM Blue (#0f62fe) as the singular interactive color, layer-based elevation instead of drop shadows, and 20-year enterprise heritage.

colors:
  # Primary canvas + ink
  background: "#ffffff"
  surface: "#ffffff"
  ink: "#161616"
  ink-inverted: "#ffffff"

  # Brand interactive
  primary: "#0f62fe"          # IBM Blue
  primary-hover: "#0353e9"
  primary-active: "#002d9c"
  secondary: "#161616"
  tertiary: "#0f62fe"

  # Layer scale (Carbon's elevation system)
  layer-01: "#f4f4f4"
  layer-02: "#ffffff"
  layer-03: "#f4f4f4"
  layer-hover: "#e0e0e0"
  layer-row-hover: "#e5e5e5"

  # Text
  on-background: "#161616"
  on-surface: "#161616"
  on-primary: "#ffffff"
  text-secondary: "#525252"
  text-placeholder: "#a8a8a8"
  text-disabled: "#c6c6c6"

  # Borders
  border: "#c6c6c6"
  border-strong: "#8d8d8d"
  border-interactive: "#0f62fe"

  # Buttons
  button-secondary-bg: "#393939"

  # Semantic
  success: "#24a148"
  warning: "#f1c21b"
  error: "#da1e28"
  info: "#4589ff"

  # Modal shadow color (opaque approx of rgba(0,0,0,0.3))
  shadow-modal: "#b3b3b3"  # was rgba(0,0,0,0.3) flattened — Google format requires hex

typography:
  display-04:
    fontFamily: "IBM Plex Sans, IBM Plex Sans Var, -apple-system, system-ui, sans-serif"
    fontSize: 92px
    fontWeight: 300
    lineHeight: 1.05
    letterSpacing: -1.8px
  display-03:
    fontFamily: "IBM Plex Sans, IBM Plex Sans Var, -apple-system, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 300
    lineHeight: 1.10
    letterSpacing: -1.44px
  display-02:
    fontFamily: "IBM Plex Sans, IBM Plex Sans Var, -apple-system, system-ui, sans-serif"
    fontSize: 54px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0px
  display-01:
    fontFamily: "IBM Plex Sans, IBM Plex Sans Var, -apple-system, system-ui, sans-serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.20
    letterSpacing: 0px
  productive-heading-04:
    fontFamily: "IBM Plex Sans, IBM Plex Sans Var, -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0px
  productive-heading-03:
    fontFamily: "IBM Plex Sans, IBM Plex Sans Var, -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  productive-heading-02:
    fontFamily: "IBM Plex Sans, IBM Plex Sans Var, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0px
  body-long:
    fontFamily: "IBM Plex Sans, IBM Plex Sans Var, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  body-short:
    fontFamily: "IBM Plex Sans, IBM Plex Sans Var, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0.16px
  label:
    fontFamily: "IBM Plex Sans, IBM Plex Sans Var, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.32px
  code-02:
    fontFamily: "IBM Plex Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0.16px
  code-01:
    fontFamily: "IBM Plex Mono, ui-monospace, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.32px

spacing:
  micro: 4px
  xs: 5px
  sm: 6px
  md: 8px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px

rounded:
  none: 0px
  notification: 2px
  circle: 9999px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-short}"
    padding: 0px 16px

  # Primary button — IBM Blue
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-short}"
    rounded: "{rounded.none}"
    padding: 0px 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"

  # Secondary
  button-secondary:
    backgroundColor: "{colors.button-secondary-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-short}"
    rounded: "{rounded.none}"
    padding: 0px 16px

  # Tertiary outlined
  button-tertiary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.body-short}"
    rounded: "{rounded.none}"
    padding: 0px 16px

  # Ghost
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.body-short}"
    rounded: "{rounded.none}"
    padding: 0px 16px

  # Danger
  button-danger:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-short}"
    rounded: "{rounded.none}"
    padding: 0px 16px

  # Tile (Carbon's card)
  tile:
    backgroundColor: "{colors.layer-01}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 16px
  tile-hover:
    backgroundColor: "{colors.layer-hover}"
    textColor: "{colors.ink}"

  # Text input — bottom border only
  input:
    backgroundColor: "{colors.layer-01}"
    textColor: "{colors.ink}"
    typography: "{typography.body-short}"
    rounded: "{rounded.none}"
    padding: 11px 16px
  input-focus:
    backgroundColor: "{colors.layer-01}"
    textColor: "{colors.ink}"
  input-error:
    backgroundColor: "{colors.layer-01}"
    textColor: "{colors.ink}"

  # Data table header
  data-table-header:
    backgroundColor: "{colors.layer-hover}"
    textColor: "{colors.ink}"
    typography: "{typography.productive-heading-02}"
    rounded: "{rounded.none}"
    padding: 11px 16px
  data-table-row-hover:
    backgroundColor: "{colors.layer-row-hover}"

  # Notification — colored left border
  notification-error:
    backgroundColor: "{colors.layer-01}"
    textColor: "{colors.ink}"
    rounded: "{rounded.notification}"
    padding: 16px
  notification-warning:
    backgroundColor: "{colors.layer-01}"
    textColor: "{colors.ink}"
    rounded: "{rounded.notification}"
    padding: 16px
  notification-success:
    backgroundColor: "{colors.layer-01}"
    textColor: "{colors.ink}"
    rounded: "{rounded.notification}"
    padding: 16px
  notification-info:
    backgroundColor: "{colors.layer-01}"
    textColor: "{colors.ink}"
    rounded: "{rounded.notification}"
    padding: 16px
---

# Carbon Design System

## Overview

Carbon is IBM's enterprise design system — the chrome that ships mainframe administration consoles, Watson dashboards, cloud platform UIs, and 40+ other products to half a million IBM employees. The homepage opens in a restrained palette: white canvas (`{colors.background}`), IBM Blue (`{colors.primary}`) as the singular interactive color, and IBM Plex Sans as the typeface. This is enterprise design with capital E — precise, structural, intentional in its refusal to be consumer-friendly.

Typography is **IBM Plex Sans** — IBM's custom variable-font family — used at weight 300 (light) for display, weight 400 for UI, weight 600 for emphasis. The weight 300 at display is a deliberate signature: where most enterprise systems lean on 600-700 for authority, Carbon chose lightness. Body text uses weight 400 with `+0.16px` tracking — a barely perceptible positive letter-spacing that opens the text for readability. IBM Plex Mono handles code and data.

The defining structural choice is **0px border-radius**. Carbon has no rounded corners. The scan found 1 instance of `2px` radius (Inline Notifications) and 1 instance of `50%` (for a "Back to Top" button) — that's it. Every button, every card, every input is **sharp-cornered**. Carbon communicates precision, engineering density, and enterprise heritage through angular geometry. Rounded corners signal consumer software; Carbon intentionally rejects that vocabulary.

**Key Characteristics:**
- Sharp corners everywhere — `{rounded.none}` radius on all interactive elements
- IBM Plex Sans (variable font) at weight 300 display, weight 400 body
- IBM Blue (`{colors.primary}`) as the singular interactive color — 45 occurrences
- Positive letter-spacing (`+0.16px`) on body — readability-first
- IBM Plex Mono for code and data tables
- Bottom-only input borders — material-inspired but simpler
- 20-year enterprise heritage — Carbon has powered IBM products since 2014
- Used across 40+ IBM products in 40+ languages — design for global scale

## Colors

### Interactive Scale
- **Interactive 01** (`{colors.primary}`): IBM Blue — primary interactive. Tier-1 CTAs.
- **Interactive 02** (`{colors.secondary}`): Near-black — secondary CTAs.
- **Interactive 03** (`{colors.tertiary}`): Tertiary interactive.
- **Hover Primary** (`{colors.primary-hover}`): Blue hover state.
- **Active Primary** (`{colors.primary-active}`): Pressed state.

### Layer Scale (Carbon's unique elevation system)
- **Background** (`{colors.background}`): Base canvas layer.
- **Layer 01** (`{colors.layer-01}`): First elevation layer — cards sit here.
- **Layer 02** (`{colors.layer-02}`): Alternating layer for nested cards.
- **Layer 03** (`{colors.layer-03}`): Deepest nested layer.
- Carbon explicitly names elevation as "layers" rather than shadows — they alternate background tints for depth, not drop shadows.

### Text
- **Text Primary** (`{colors.ink}`): Primary text.
- **Text Secondary** (`{colors.text-secondary}`): Secondary text — the dominant text color (192 occurrences).
- **Text Placeholder** (`{colors.text-placeholder}`): Placeholder.
- **Text On Color** (`{colors.on-primary}`): Text on filled surfaces.
- **Text Disabled** (`{colors.text-disabled}`): Disabled text.

### Border
- **Border Strong** (`{colors.border-strong}`): Emphasized border.
- **Border Subtle** (`{colors.border}`): Default border.
- **Border Interactive** (`{colors.border-interactive}`): Focus/interactive border.

### Semantic
- **Success** (`{colors.success}`): Success state.
- **Warning** (`{colors.warning}`): Amber caution.
- **Error** (`{colors.error}`): Critical/destructive.
- **Info** (`{colors.info}`): Info callouts.

## Typography

### Font Families
- **Primary**: `IBM Plex Sans` (variable font)
- **Monospace**: `IBM Plex Mono`
- **Serif** (editorial): `IBM Plex Serif` — used rarely, for marketing long-form
- Variable font weight axis: 100-700 available

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-04` | 92px maximum hero |
| `display-03` | 72px hero |
| `display-02` | 54px display |
| `display-01` | 42px display |
| `productive-heading-04` | 32px productive heading |
| `productive-heading-03` | 20px productive heading |
| `productive-heading-02` | 16px productive heading (weight 600) |
| `body-long` | 16px body |
| `body-short` | 14px body with +0.16px tracking |
| `label` | 12px label with +0.32px tracking |
| `code-02` | 14px code |
| `code-01` | 12px code |

### Principles
- **Weight 300 at display**: The Carbon signature. Enterprise lightness — confident without bold.
- **Positive letter-spacing at small sizes**: `+0.16px` at 14px, `+0.32px` at 12px.
- **Productive vs Expressive type**: Carbon names styles `Productive Heading 04` (for app UI) vs `Display 03` (for marketing) — same size, different weight, different tracking, different context.
- **Code is identity-forward**: IBM Plex Mono appears throughout technical documentation and data displays.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 4px (Carbon uses a `spacing-01` through `spacing-13` scale). Dominant values are 6px, 8px, and 4px. Sub-pixel values suggest density calculations for 24px grid UI.

### Grid
- 2x grid (4-4-8-12-16-24 etc.) — Carbon follows IBM's enterprise grid
- Max content widths: 1584px (max), 1312px (xlg), 1056px (lg), 672px (md)
- Nav: 48px tall top bar, 256px or 16px side nav

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Layer 01 | `{colors.layer-01}` bg on white canvas | Cards, first elevation |
| Layer 02 | `{colors.layer-02}` bg on layer-01 | Nested cards, second elevation |
| Layer 03 | `{colors.layer-03}` bg on layer-02 | Deepest nesting, third elevation |
| Modal | Soft drop shadow with `{colors.shadow-modal}` tint | Dialog only — the one drop shadow in the system |
| Notification | Subtle drop shadow | Toast, notification overlay |

**Shadow Philosophy**: Carbon uses **alternating layer backgrounds** instead of drop shadows for elevation. A card sits on Layer 01 (`{colors.layer-01}`) on a white canvas; a nested panel inside that card returns to Layer 02 (`{colors.layer-02}`) for contrast. This creates depth through tonal alternation — an enterprise-aware choice that renders identically in any printing context, doesn't rely on shadow rendering, and remains interpretable in high-contrast accessibility modes. Drop shadows appear only on modal dialogs and system-level notifications.

## Shapes

There is no radius scale in Carbon. The system uses `{rounded.none}` exclusively except for:

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Default for everything — the workhorse |
| `notification` | 2px | Reserved for Inline Notifications (single use) |
| `circle` | 9999px | Circular elements only (avatars, "Back to Top" button) |

This is Carbon's most defining visual choice — **sharp corners** as structural philosophy.

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — `{colors.primary}` bg, white text, `{rounded.none}` radius, 48px height (md), 14px IBM Plex Sans weight 400 tracking +0.16px.
- **`button-secondary`** — `{colors.button-secondary-bg}` bg, white text.
- **`button-tertiary`** — transparent, IBM Blue border + text.
- **`button-ghost`** — transparent, IBM Blue text, no border.
- **`button-danger`** — `{colors.error}` bg, white text.
- Sizes: sm (32px), md (40px), lg (48px — default), xl (64px), 2xl (80px).

### Tiles (Cards in Carbon terminology)
- **`tile`** — `{colors.layer-01}` bg (Layer 01), no border, `{rounded.none}` radius, 16px padding.
- **`tile-hover`** — Hover fills `{colors.layer-hover}` — no lift, no shadow.
- **Selectable tile**: left border thickens on selection to 4px solid `{colors.primary}`.

### Inputs
- **`input`** — `{colors.layer-01}` bg, no top/left/right borders. Bottom border only: 1px solid `{colors.border-strong}`. `{rounded.none}` radius, 11px 16px padding.
- **`input-focus`** — Focus: bottom border becomes 2px solid `{colors.primary}`, no ring.
- **`input-error`** — Error: bottom border 2px solid `{colors.error}`.

### Data Tables
- **`data-table-header`** — `{rounded.none}` radius, no border on cells (only outer container). Header: `{colors.layer-hover}` bg, `{colors.ink}` text, 14px weight 600 tracking +0.16px.
- **`data-table-row-hover`** — Hover row: `{colors.layer-row-hover}` bg.

### Notifications
- **`notification-error`**, **`notification-warning`**, **`notification-success`**, **`notification-info`** — `{rounded.notification}` (2px) radius, 16px padding, colored left border (4px) with semantic color.

## Do's and Don'ts

### Do
- Use `{rounded.none}` (0px) radius on EVERY interactive element — sharpness IS the brand
- Use IBM Plex Sans at weight 300 for display — enterprise lightness
- Apply positive letter-spacing (+0.16-0.32px) on body/caption sizes
- Use alternating layer backgrounds for elevation, not drop shadows
- Use IBM Blue (`{colors.primary}`) as the singular interactive color
- Default to bottom-only borders on inputs
- Use IBM Plex Mono for all code, data, and identifiers

### Don't
- Don't add border-radius — breaks 20 years of Carbon consistency
- Don't use weight 700 for display — Carbon caps at 600 for emphasis
- Don't use drop shadows on cards — use Layer 01/02/03 alternation
- Don't use Inter, SF Pro, or any non-IBM-Plex typeface — brand requirement
- Don't mix Carbon with Material or iOS components — the geometric language clashes
- Don't skip the accessibility audits — Carbon enforces WCAG AAA for IBM products

---

## Responsive Behavior

### Breakpoints (Carbon's grid)
| Name | Width | Max Content | Changes |
|---|---|---|---|
| sm | 320px+ | 672px | Mobile, bottom nav, single column |
| md | 672px+ | 1056px | Tablet, 2-column layout |
| lg | 1056px+ | 1312px | Desktop, side nav visible |
| xlg | 1312px+ | 1584px | Wide desktop |
| max | 1584px+ | 1584px | Max content width |

### Touch Targets
- Buttons: 40-48px height
- Data table row height: 40px (compact), 48px (default), 64px (tall)
- Icon buttons: 40px × 40px

### Collapsing Strategy
- Display: 92px → 54px → 42px across breakpoints, weight 300 maintained
- Navigation: top bar + side nav → top bar + hamburger drawer
- Data tables: horizontal scroll with sticky first column
- Cards: grid → stacked, `{rounded.none}` radius maintained

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Blue: `{colors.primary}` (IBM Blue)
- Background: `{colors.background}`
- Layer 01: `{colors.layer-01}`
- Text: `{colors.ink}` (primary), `{colors.text-secondary}` (secondary)
- Border: `{colors.border}`
- Success: `{colors.success}`
- Error: `{colors.error}`

### Example Component Prompts
- "Create a primary button: `{colors.primary}` bg, white text, 0px radius (sharp corners), 0 16px padding, 48px height, 14px IBM Plex Sans weight 400 tracking +0.16px. Hover: `{colors.primary-hover}`. Focus: 2px inset white + 4px solid `{colors.primary}` outer ring."
- "Design a Carbon tile: `{colors.layer-01}` bg (Layer 01) on white canvas, no border, 0px radius, 16px padding. Title 16px IBM Plex Sans weight 600 color `{colors.ink}`. Body 14px weight 400 tracking +0.16px color `{colors.text-secondary}`. Clickable hover: `{colors.layer-hover}` bg."
- "Build a text input: `{colors.layer-01}` bg, no top/left/right border, 1px solid `{colors.border-strong}` bottom-only border, 0px radius, 11px 16px padding. Label above at 12px weight 400 tracking +0.32px. Focus: bottom border becomes 2px solid `{colors.primary}`."

### Iteration Guide
1. Sharp corners are non-negotiable — `{rounded.none}` radius everywhere
2. IBM Plex Sans + weight 300 display = Carbon's voice
3. Positive tracking (+0.16px, +0.32px) on 14px and 12px text — readability at density
4. Layer-01/02/03 alternation replaces drop shadows
5. Bottom-only input borders — Material-inspired, not Material-copied
6. IBM Blue (`{colors.primary}`) is the only interactive color — discipline is the design
