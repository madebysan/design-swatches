---
version: alpha
name: IBM
description: Carbon Design System distilled — enterprise authority through methodical rigor, IBM Plex Sans light at display, IBM Blue 60 as the singular accent, sharp 0px corners, and depth via background-color layering.

colors:
  # Base
  background: "#ffffff"
  surface: "#f4f4f4"
  surface-elevated: "#e0e0e0"
  ink: "#161616"
  on-primary: "#ffffff"

  # Brand accent — IBM Blue 60
  primary: "#0f62fe"
  primary-hover: "#0353e9"
  primary-active: "#002d9c"
  primary-tint: "#edf5ff"

  # Gray scale (Carbon Gray family)
  gray-90: "#262626"
  gray-80: "#393939"
  gray-70: "#525252"
  gray-60: "#6f6f6f"
  gray-50: "#8d8d8d"
  gray-30: "#c6c6c6"
  gray-20: "#e0e0e0"
  gray-10: "#f4f4f4"
  gray-10-hover: "#e8e8e8"

  # Semantic / status
  danger: "#da1e28"
  danger-hover: "#b81921"
  success: "#24a148"
  warning: "#f1c21b"

  # Borders / dividers
  border: "#c6c6c6"
  border-subtle: "#e0e0e0"

  # Focus
  focus: "#0f62fe"
  focus-inset: "#ffffff"

  # Shadow approximation (opaque)
  shadow-raised: "#999999"  # was rgba(0,0,0,0.3) — Google format requires hex

typography:
  display-01:
    fontFamily: "IBM Plex Sans, Helvetica Neue, Arial, sans-serif"
    fontSize: 60px
    fontWeight: 300
    lineHeight: 1.17
    letterSpacing: 0px
  display-02:
    fontFamily: "IBM Plex Sans, Helvetica Neue, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.17
    letterSpacing: 0px
  heading-01:
    fontFamily: "IBM Plex Sans, Helvetica Neue, Arial, sans-serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.19
    letterSpacing: 0px
  heading-02:
    fontFamily: "IBM Plex Sans, Helvetica Neue, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0px
  heading-03:
    fontFamily: "IBM Plex Sans, Helvetica Neue, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  heading-04:
    fontFamily: "IBM Plex Sans, Helvetica Neue, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0px
  body-long-01:
    fontFamily: "IBM Plex Sans, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  body-long-02:
    fontFamily: "IBM Plex Sans, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.50
    letterSpacing: 0px
  body-short-01:
    fontFamily: "IBM Plex Sans, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0.16px
  body-short-02:
    fontFamily: "IBM Plex Sans, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.16px
  caption-01:
    fontFamily: "IBM Plex Sans, Helvetica Neue, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.32px
  code-01:
    fontFamily: "IBM Plex Mono, Menlo, Courier, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0.16px
  code-02:
    fontFamily: "IBM Plex Mono, Menlo, Courier, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
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
  5xl: 96px
  6xl: 160px

rounded:
  none: 0px
  sm: 2px
  pill: 24px
  circle: 9999px

components:
  # Primary button
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-short-02}"
    rounded: "{rounded.none}"
    padding: 14px 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"

  # Secondary button (gray)
  button-secondary:
    backgroundColor: "{colors.gray-80}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-short-02}"
    rounded: "{rounded.none}"
    padding: 14px 16px
  button-secondary-hover:
    backgroundColor: "{colors.gray-70}"
    textColor: "{colors.on-primary}"

  # Tertiary (ghost outlined blue)
  button-tertiary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.body-short-02}"
    rounded: "{rounded.none}"
    padding: 14px 16px

  # Ghost link-style
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.body-short-02}"
    rounded: "{rounded.none}"
    padding: 14px 16px
  button-ghost-hover:
    backgroundColor: "{colors.gray-10-hover}"
    textColor: "{colors.primary}"

  # Danger button
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-short-02}"
    rounded: "{rounded.none}"
    padding: 14px 16px
  button-danger-hover:
    backgroundColor: "{colors.danger-hover}"
    textColor: "{colors.on-primary}"

  # Card / tile
  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.none}"
    padding: 16px
  tile:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
    padding: 16px
  tile-hover:
    backgroundColor: "{colors.gray-10-hover}"

  # Form input — bottom-border only
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-long-01}"
    rounded: "{rounded.none}"
    padding: 0px 16px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"

  # Top navigation (dark masthead)
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.gray-30}"
    typography: "{typography.body-short-01}"
    padding: 0px 16px
  nav-link-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"

  # Tag / label — pill exception
  tag:
    backgroundColor: "{colors.primary-tint}"
    textColor: "{colors.primary}"
    typography: "{typography.caption-01}"
    rounded: "{rounded.pill}"
    padding: 4px 8px

  # Notification banner
  banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-short-01}"
    rounded: "{rounded.none}"
    padding: 12px 16px
---

# IBM Design System

## Overview

IBM's website is the digital embodiment of enterprise authority built on the Carbon Design System — a design language so methodically structured it reads like an engineering specification rendered as a webpage. The page operates on a stark duality: a bright white (`{colors.background}`) canvas with near-black (`{colors.ink}`) text, punctuated by a single, unwavering accent — IBM Blue 60 (`{colors.primary}`). This isn't playful tech-startup minimalism; it's corporate precision distilled into pixels. Every element exists within Carbon's rigid 2× grid, every color maps to a semantic token, every spacing value snaps to the 8px base unit.

The IBM Plex type family is the system's backbone. IBM Plex Sans at light weight (300) for display headlines creates an unexpectedly airy, almost delicate quality at large sizes — a deliberate counterpoint to IBM's corporate gravity. At body sizes, regular weight (400) with 0.16px letter-spacing on 14px captions introduces the meticulous micro-tracking that makes Carbon text feel engineered rather than designed. IBM Plex Mono serves code, data, and technical labels, completing the family trinity alongside the rarely-surfaced IBM Plex Serif.

What defines IBM's visual identity beyond monochrome-plus-blue is the reliance on Carbon's component token system. Every interactive state maps to a CSS custom property prefixed with `--cds-` (Carbon Design System). Buttons don't have hardcoded colors; they reference `--cds-button-primary`, `--cds-button-primary-hover`, `--cds-button-primary-active`. This tokenized architecture means the entire visual layer is a thin skin over a deeply systematic foundation — the design equivalent of a well-typed API.

**Key Characteristics:**
- IBM Plex Sans at weight 300 (Light) for display — corporate gravitas through typographic restraint
- IBM Plex Mono for code and technical content with consistent 0.16px letter-spacing at small sizes
- Single accent color: IBM Blue 60 (`{colors.primary}`) — every interactive element, every CTA, every link
- Carbon token system (`--cds-*`) driving all semantic colors, enabling theme-switching at the variable level
- 8px spacing grid with strict adherence — no arbitrary values, everything aligns
- Flat, borderless cards on `{colors.surface}` Gray 10 surface — depth through background-color layering, not shadows
- Bottom-border inputs (not boxed) — the signature Carbon form pattern
- 0px border-radius on primary buttons — unapologetically rectangular, no softening

## Colors

### Primary
- **IBM Blue 60** (`{colors.primary}`): The singular interactive color. Primary buttons, links, focus states, active indicators. The only chromatic hue in the core UI palette.
- **White** (`{colors.background}`): Page background, card surfaces, button text on blue.
- **Gray 100** (`{colors.ink}`): Primary text, headings, dark surface backgrounds, nav bar, footer.

### Neutral Scale (Gray Family)
Carbon's gray scale runs in 10-step increments. Surfaces shift through Gray 10, 20, and 30 to imply elevation; text uses Gray 70 for secondary copy and Gray 60 for placeholders and disabled labels.
- `{colors.gray-90}` — secondary dark surfaces
- `{colors.gray-80}` — tertiary dark, secondary button bg
- `{colors.gray-70}` — secondary text, helper text
- `{colors.gray-60}` — placeholder, disabled text
- `{colors.gray-50}` — disabled icons, muted labels
- `{colors.gray-30}` — borders, divider lines, input bottom-borders
- `{colors.gray-20}` — subtle borders, card outlines
- `{colors.gray-10}` — secondary surface background, tile fill
- `{colors.gray-10-hover}` — hover state for Gray 10 surfaces

### Interactive
- `{colors.primary}` — primary CTA, links, focus
- `{colors.primary-hover}` — link/button hover
- `{colors.primary-active}` — active/pressed
- `{colors.primary-tint}` — selected row, tag fill

### Status
- **Error** (`{colors.danger}`)
- **Success** (`{colors.success}`)
- **Warning** (`{colors.warning}`)
- **Info** (`{colors.primary}`)

## Typography

### Font Family
- **Primary**: `IBM Plex Sans`, fallbacks `Helvetica Neue, Arial, sans-serif`
- **Monospace**: `IBM Plex Mono`, fallbacks `Menlo, Courier, monospace`
- **Serif** (limited use): `IBM Plex Serif`, for editorial/expressive contexts

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens (`{typography.display-01}`, `{typography.body-long-01}`) directly.

| Token | Use |
|---|---|
| `display-01` | Maximum impact — hero, light weight for elegance |
| `display-02` | Secondary hero, responsive fallback |
| `heading-01` | Expressive heading |
| `heading-02` | Section headings |
| `heading-03` | Sub-section titles |
| `heading-04` | Card titles, feature headers |
| `body-long-01` | Standard reading text |
| `body-long-02` | Emphasized body, labels |
| `body-short-01` | Compact body, captions |
| `body-short-02` | Bold captions, nav items |
| `caption-01` | Metadata, timestamps |
| `code-01` | Inline code, terminal |
| `code-02` | Code blocks |

### Principles
- **Light weight at display sizes**: Carbon's expressive set uses weight 300 at 42px+. Content speaks with corporate authority while letterforms whisper with typographic lightness.
- **Micro-tracking at small sizes**: 0.16px at 14px and 0.32px at 12px — Carbon's secret weapon for legibility at compact sizes.
- **Three functional weights**: 300 (display/expressive), 400 (body/reading), 600 (emphasis/UI labels). Weight 700 is intentionally absent.
- **Productive vs. Expressive**: Productive sets use tighter line-heights (1.29) for dense UI; expressive sets breathe more (1.40–1.50).

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is **8px** (Carbon's 2× grid). The scale runs `micro` (2px) and `xs` (4px) for fine adjustments, then snaps cleanly to 8/16/24/32 multiples.

### Grid & Container
- 16-column grid (Carbon's 2× grid system)
- Max content width: 1584px (max breakpoint)
- Column gutters: 32px (16px on mobile)
- Margin: 16px (mobile), 32px (tablet+)

### Whitespace Philosophy
- **Functional density**: Carbon favors productive density over expansive whitespace, reflecting IBM's enterprise DNA.
- **Background-color zoning**: Sections separate via alternating background colors (white → gray 10 → white) rather than vast vertical padding.
- **Consistent 48px rhythm**: Major section transitions use `3xl` vertical spacing. Hero sections may use `5xl`.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, `{colors.background}` background | Default page surface |
| Layer 01 | No shadow, `{colors.surface}` background | Cards, tiles, alternating sections |
| Layer 02 | No shadow, `{colors.surface-elevated}` background | Elevated panels within Layer 01 |
| Raised | `0 2px 6px {colors.shadow-raised}` | Dropdowns, tooltips, overflow menus |
| Overlay | `0 2px 6px {colors.shadow-raised}` + dark scrim | Modal dialogs, side panels |
| Focus | `2px solid {colors.focus}` inset + `1px solid {colors.focus-inset}` | Keyboard focus ring |
| Bottom-border | `2px solid {colors.ink}` on bottom edge | Active input, active tab indicator |

**Shadow Philosophy**: Carbon is deliberately shadow-averse. Depth comes from background-color layering — stacking surfaces of progressively darker grays rather than adding box-shadows. This print-inspired aesthetic communicates hierarchy through value rather than simulated light. Shadows are reserved for floating elements (dropdowns, tooltips, modals).

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Buttons, inputs, tiles, cards — the dominant treatment |
| `sm` | 2px | Occasional micro-rounding on small interactive elements |
| `pill` | 24px | Tags / labels (the sole non-zero exception) |
| `circle` | 9999px | Avatar circles, icon containers |

Carbon is fundamentally rectangular. The 24px tag/label pill is the only place rounding appears in the core component set.

## Components

The complete component spec lives in the `components:` token block above. Reference components directly (`{components.button-primary}`, `{components.tile}`).

### Buttons
- **`button-primary`** — IBM Blue 60 fill, white text, sharp 0px corners, 48px default height with asymmetric padding for trailing icons.
- **`button-secondary`** — Gray 80 fill, secondary actions on light surfaces.
- **`button-tertiary`** — outlined blue ghost.
- **`button-ghost`** — link-style, transparent until hover.
- **`button-danger`** — Red 60 fill for destructive actions.

### Cards & Tiles
- **`card`** — flat white surface, 0px radius, no shadow.
- **`tile`** — Gray 10 surface, hovers to `{colors.gray-10-hover}`. Separation comes from background-color shifts, not shadows.

### Inputs
- **`input`** — Gray 10 fill, 0px radius, 40px default height, bottom-border-only treatment. Bottom border activates to Gray 100; focus shifts the border to Blue 60; error to Red 60.

### Navigation
- **`nav-bar`** — full-width Gray 100 masthead, 48px height, IBM 8-bar logo white left-aligned, links at 14px Gray 30, hover/active to white.

### Tag
- **`tag`** — Blue 10 background with Blue 60 text, 24px pill radius — the system's single rounded exception.

### Banner
- **`banner`** — full-width notification bar, Blue 60 (or Gray 100) background, white text.

## Do's and Don'ts

### Do
- Use IBM Plex Sans at weight 300 for display sizes (42px+) — the lightness is intentional
- Apply 0.16px letter-spacing on 14px body text and 0.32px on 12px captions
- Use 0px border-radius on buttons, inputs, cards, and tiles — rectangles are the system
- Reference `--cds-*` token names when implementing
- Use background-color layering (white → gray 10 → gray 20) for depth instead of shadows
- Use bottom-border (not box) for input field indicators
- Maintain the 48px default button height and asymmetric padding for icon accommodation
- Apply Blue 60 (`{colors.primary}`) as the sole accent — one blue to rule them all

### Don't
- Don't round button corners — 0px radius is the Carbon identity
- Don't use shadows on cards or tiles — flatness is the point
- Don't introduce additional accent colors — IBM's system is monochromatic + blue
- Don't use weight 700 (Bold) — the scale stops at 600 (Semibold)
- Don't add letter-spacing to display-size text — tracking is only for 14px and below
- Don't box inputs with full borders — Carbon inputs use bottom-border only
- Don't use gradient backgrounds — IBM's surfaces are flat, solid colors
- Don't deviate from the 8px spacing grid

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Small (sm) | 320px | Single column, hamburger nav, 16px margins |
| Medium (md) | 672px | 2-column grids begin, expanded content |
| Large (lg) | 1056px | Full navigation visible, 3–4 column grids |
| X-Large (xlg) | 1312px | Maximum content density, wide layouts |
| Max | 1584px | Maximum content width, centered with margins |

### Touch Targets
- Button height: 48px default, minimum 40px (compact)
- Navigation links: 48px row height for touch
- Input height: 40px default, 48px large
- Icon buttons: 48px square touch target
- Mobile menu items: full-width 48px rows

### Collapsing Strategy
- Hero: 60px display → 42px → 32px heading as viewport narrows
- Navigation: full horizontal masthead → hamburger with slide-out panel
- Grid: 4-column → 2-column → single column
- Tiles/cards: horizontal grid → vertical stack
- Footer: multi-column link groups → stacked single column
- Section padding: 48px → 32px → 16px

### Image Behavior
- Responsive images with `max-width: 100%`
- Product illustrations scale proportionally
- Hero images may shift from side-by-side to stacked below
- Data visualizations maintain aspect ratio with horizontal scroll on mobile

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: IBM Blue 60 (`{colors.primary}`)
- Background: White (`{colors.background}`)
- Heading text: Gray 100 (`{colors.ink}`)
- Body text: Gray 100 (`{colors.ink}`)
- Secondary text: Gray 70 (`{colors.gray-70}`)
- Surface/Card: Gray 10 (`{colors.surface}`)
- Border: Gray 30 (`{colors.border}`)
- Link: Blue 60 (`{colors.primary}`)
- Link hover: Blue 70 (`{colors.primary-hover}`)
- Focus ring: Blue 60 (`{colors.focus}`)
- Error: Red 60 (`{colors.danger}`)
- Success: Green 50 (`{colors.success}`)

### Example Component Prompts
- "Create a hero section on white background. Headline at 60px IBM Plex Sans weight 300, line-height 1.17, color `{colors.ink}`. Subtitle at 16px weight 400, line-height 1.50, color `{colors.gray-70}`, max-width 640px. Blue CTA button (`{colors.primary}` background, white text, 0px border-radius, 48px height, 14px 63px 14px 15px padding)."
- "Design a card tile: `{colors.surface}` background, 0px border-radius, 16px padding. Title at 20px IBM Plex Sans weight 600, line-height 1.40, color `{colors.ink}`. Body at 14px weight 400, letter-spacing 0.16px, line-height 1.29, color `{colors.gray-70}`. Hover: background shifts to `{colors.gray-10-hover}`."
- "Build a form field: `{colors.surface}` background, 0px border-radius, 40px height, 16px horizontal padding. Label above at 12px weight 400, letter-spacing 0.32px, color `{colors.gray-70}`. Bottom-border: 2px solid transparent default, 2px solid `{colors.focus}` on focus."
- "Create a dark navigation bar: `{colors.ink}` background, 48px height. IBM logo white left-aligned. Links at 14px IBM Plex Sans weight 400, color `{colors.gray-30}`. Hover: white text. Active: white with 2px bottom border."
- "Build a tag component: `{colors.primary-tint}` background, `{colors.primary}` text, 4px 8px padding, 24px border-radius, 12px IBM Plex Sans weight 400."

### Iteration Guide
1. Always use 0px border-radius on buttons, inputs, and cards — this is non-negotiable in Carbon
2. Letter-spacing only at small sizes: 0.16px at 14px, 0.32px at 12px — never on display text
3. Three weights: 300 (display), 400 (body), 600 (emphasis) — no bold
4. Blue 60 is the only accent color — do not introduce secondary accent hues
5. Depth comes from background-color layering, not shadows
6. Inputs have bottom-border only, never fully boxed
7. Use `--cds-` prefix for token naming to stay Carbon-compatible
8. 48px is the universal interactive element height
