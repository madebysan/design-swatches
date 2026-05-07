---
version: alpha
name: Coinbase
description: Trustworthy crypto platform aesthetic — Coinbase Blue (#0052ff) on white-and-near-black canvas, four-font proprietary family (Display, Sans, Text, Icons), 56px-radius pill CTAs, alternating white and #0a0b0d sections.

colors:
  # Primary canvas + ink
  background: "#ffffff"
  surface: "#ffffff"
  surface-subtle: "#f7f7f7"      # opaque approx of rgba(247,247,247,0.88) — Google format requires hex
  surface-cool: "#eef0f3"        # Cool Gray Surface (secondary button bg)
  surface-dark: "#0a0b0d"        # Dark section background
  surface-card-dark: "#282b31"   # Dark Card
  ink: "#0a0b0d"                 # Near Black
  ink-pure: "#000000"
  ink-inverted: "#ffffff"

  # Brand accent
  primary: "#0052ff"             # Coinbase Blue
  primary-hover: "#578bfa"        # Hover Blue
  primary-link: "#0667d0"         # Link Blue
  primary-muted: "#5b616e"        # Muted Blue (border)

  # Text states
  on-background: "#0a0b0d"
  on-surface: "#0a0b0d"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

  # Borders
  border: "#5b616e"

typography:
  display-hero:
    fontFamily: "CoinbaseDisplay, ui-sans-serif, system-ui, sans-serif"
    fontSize: 80px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  display-secondary:
    fontFamily: "CoinbaseDisplay, ui-sans-serif, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  display-third:
    fontFamily: "CoinbaseDisplay, ui-sans-serif, system-ui, sans-serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  section-heading:
    fontFamily: "CoinbaseSans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.11
    letterSpacing: 0px
  card-title:
    fontFamily: "CoinbaseSans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.13
    letterSpacing: 0px
  feature-title:
    fontFamily: "CoinbaseSans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0px
  body-bold:
    fontFamily: "CoinbaseSans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.50
    letterSpacing: 0px
  body-semibold:
    fontFamily: "CoinbaseSans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0px
  body:
    fontFamily: "CoinbaseText, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0px
  body-small:
    fontFamily: "CoinbaseText, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button:
    fontFamily: "CoinbaseSans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0.16px
  caption:
    fontFamily: "CoinbaseSans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.50
    letterSpacing: 0px
  small:
    fontFamily: "CoinbaseSans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0px

spacing:
  micro: 1px
  2xs: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px

rounded:
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
  2xl: 24px
  3xl: 32px
  4xl: 40px
  pill: 56px
  full: 9999px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-semibold}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-semibold}"
    padding: 8px 12px

  # Primary pill CTA — 56px radius signature
  button-primary:
    backgroundColor: "{colors.surface-cool}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 14px 24px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"

  # Dark pill button
  button-dark:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 14px 24px
  button-dark-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"

  # Blue bordered
  button-bordered:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 14px 24px

  # Full pill
  button-full-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.full}"
    padding: 14px 24px

  # Card
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-feature:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.2xl}"
    padding: 32px
  card-large:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.4xl}"
    padding: 48px

  # Dark section
  section-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-secondary}"
    padding: 64px

  # Dark card
  card-dark:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-small}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"

  # Article link / small card
  link-article:
    backgroundColor: "{colors.surface-subtle}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
---

# Coinbase Design System

## Overview

Coinbase's website is a clean, trustworthy crypto platform that communicates financial reliability through a blue-and-white binary palette. The design uses Coinbase Blue (`{colors.primary}`) — a deep, saturated blue — as the singular brand accent against white and near-black surfaces. The proprietary font family includes CoinbaseDisplay for hero headlines, CoinbaseSans for UI text, CoinbaseText for body reading, and CoinbaseIcons for iconography — a comprehensive four-font system.

The button system uses a distinctive 56px radius for pill-shaped CTAs with hover transitions to a lighter blue (`{colors.primary-hover}`). The design alternates between white content sections and dark (`{colors.surface-dark}`, `{colors.surface-card-dark}`) feature sections, creating a professional, financial-grade interface.

The interaction model is restrained: blue is functional only — used for CTAs, links, and brand moments, never decoratively. Display headlines run at ultra-tight 1.00 line-height that compresses CoinbaseDisplay into commanding, financial-statement-grade text blocks. The result is a system that feels built for fiduciary trust: the chrome is quiet, the type is firm, and the only color on the page is the blue you press to act.

**Key Characteristics:**
- Coinbase Blue (`{colors.primary}`) as singular brand accent
- Four-font proprietary family: Display, Sans, Text, Icons
- 56px radius pill buttons with blue hover transition
- Near-black (`{colors.surface-dark}`) dark sections + white light sections
- 1.00 line-height on display headings — ultra-tight
- Cool gray secondary surface (`{colors.surface-cool}`) with blue tint
- Lowercase button labels on some CTAs — unusual but distinctive

## Colors

### Primary
- **Coinbase Blue** (`{colors.primary}`): Primary brand, links, CTA borders.
- **Pure White** (`{colors.background}`): Primary light surface.
- **Near Black** (`{colors.ink}`): Text, dark section backgrounds.
- **Cool Gray Surface** (`{colors.surface-cool}`): Secondary button background.

### Interactive
- **Hover Blue** (`{colors.primary-hover}`): Button hover background.
- **Link Blue** (`{colors.primary-link}`): Secondary link color.
- **Muted Blue** (`{colors.primary-muted}`): Border color.

### Surface
- **Dark Card** (`{colors.surface-card-dark}`): Dark button/card backgrounds.
- **Light Surface** (`{colors.surface-subtle}`): Subtle surface.
- **Dark Section** (`{colors.surface-dark}`): Dark feature sections.

### Text
- Primary on light: `{colors.ink}`
- Primary on dark: `{colors.on-dark}`

## Typography

### Font Families
- **Display**: `CoinbaseDisplay` — hero headlines
- **UI / Sans**: `CoinbaseSans` — buttons, headings, nav
- **Body**: `CoinbaseText` — reading text
- **Icons**: `CoinbaseIcons` — icon font

The complete type scale lives in the `typography:` token block above.

| Token | Use |
|---|---|
| `display-hero` | 80px CoinbaseDisplay max impact |
| `display-secondary` | 64px sub-hero |
| `display-third` | 52px third-tier display |
| `section-heading` | 36px CoinbaseSans feature section |
| `card-title` | 32px card heading |
| `feature-title` | 18px feature emphasis (weight 600) |
| `body-bold` | 16px strong body (weight 700) |
| `body-semibold` | 16px button/nav (weight 600) |
| `body` | 18px CoinbaseText reading |
| `body-small` | 16px secondary reading |
| `button` | 16px button label with +0.16px tracking |
| `caption` | 14px metadata |
| `small` | 13px tags |

### Principles
- **Display ultra-tight at 1.00 line-height** — financial statement gravitas.
- **Functional blue only** — `{colors.primary}` is the action color, never decorative.
- **Pill CTAs at 56px radius** — the signature interaction shape.
- **Four typefaces, three voices**: Display for hero, Sans for UI, Text for reading.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px. Scale: 1, 4, 6, 8, 12, 16, 24, 32, 48px.

### Grid & Container
- Max width: ~1200px content
- Hero: full-width with massive Display type
- Feature sections alternate dark and light environments
- Trust bars: horizontal logo strip

### Whitespace Philosophy
- Crisp, financial pacing — generous gaps between sections
- Dark/light alternation creates chapter-like reading rhythm
- Type-led composition: headline + CTA + supporting media

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Page canvas, text |
| Bordered (Level 1) | 1px solid `{colors.primary-muted}` at low opacity | Cards, subtle containment |
| Surface Contrast (Level 2) | Background change (white → snow → dark) | Section transitions |

**Shadow Philosophy**: Coinbase has a minimal shadow system — depth comes from color contrast between dark and light sections, not from elevation rendering. The brand prefers visible structural clarity over atmospheric lift.

## Shapes

| Token | Value | Use |
|---|---|---|
| `sm` | 4px | Article links, small cards |
| `md` | 8px | Inputs, small cards |
| `lg` | 12px | Cards, menus |
| `xl` | 16px | Cards, menus |
| `2xl` | 24px | Feature containers |
| `3xl` | 32px | Feature containers |
| `4xl` | 40px | Large buttons/containers |
| `pill` | 56px | Primary CTAs — the Coinbase pill |
| `full` | 9999px | Maximum pill |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — 56px radius pill, cool gray fill, dark text. Hover shifts to `{colors.primary-hover}`.
- **`button-dark`** — Dark card fill, white text — for use on light sections.
- **`button-bordered`** — White fill, blue border, blue text — secondary CTA.
- **`button-full-pill`** — Full 9999px pill with brand blue fill.

### Cards & Containers
- **`card`** — Standard 12px-radius card on white.
- **`card-feature`** — 24px radius for feature containers.
- **`card-large`** — 40px radius for the largest feature blocks.
- **`card-dark`** — Dark variant with `{colors.surface-card-dark}` fill.

### Sections
- **`section-dark`** — Full-width near-black band with display type.

### Inputs
- **`input`** — White fill, near-black text, 8px radius, blue focus border.

### Article Links
- **`link-article`** — Compact subtle-surface link card.

## Do's and Don'ts

### Do
- Use Coinbase Blue (`{colors.primary}`) for primary interactive elements only
- Apply 56px radius for all CTA buttons
- Use CoinbaseDisplay for hero headings only
- Alternate dark (`{colors.surface-dark}`) and white sections for chapter pacing
- Use CoinbaseSans for buttons, nav, headings; CoinbaseText for body reading
- Maintain 1.00 line-height on display headings — tight is the brand
- Hover states transition to `{colors.primary-hover}` — never opacity drops

### Don't
- Don't use the blue decoratively — it's functional only
- Don't use sharp corners on CTAs — 56px radius minimum
- Don't mix CoinbaseDisplay into body or button text
- Don't introduce additional accent colors
- Don't reduce display line-height below 1.00 or above 1.20

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile Small | <400px | Single column, compressed type |
| Mobile | 400–576px | Single column, hamburger nav |
| Small Tablet | 576–640px | Slight grid expansion |
| Tablet | 640–768px | 2-column begins |
| Tablet Large | 768–896px | Multi-column feature grids |
| Desktop | 896–1280px | Full layout |
| Large Desktop | 1280–1440px | Maximum content width |
| Ultra-Wide | 1440–1600px | Container caps |

### Touch Targets
- Pill CTAs at 14px+ vertical padding hit ~44px touch height
- Nav links generously spaced
- Mobile CTAs full-width

### Collapsing Strategy
- **Hero**: 80px → 64px → 52px → 36px progressive
- **Sections**: dark/light alternation maintained at all sizes
- **Navigation**: full → hamburger
- **Feature grids**: multi-column → 2-column → stacked

### Image Behavior
- Product screenshots scale within rounded containers
- Trust logo bars reflow to multi-row
- Display type retains 1.00 line-height across breakpoints

---

## Agent Prompt Guide

### Quick Color Reference
- Brand: Coinbase Blue `{colors.primary}`
- Background: White `{colors.background}`
- Dark surface: `{colors.surface-dark}`
- Secondary surface: `{colors.surface-cool}`
- Hover: `{colors.primary-hover}`
- Text: `{colors.ink}`

### Example Component Prompts
- "Create hero: white background. CoinbaseDisplay 80px, line-height 1.00. Pill CTA (`{colors.surface-cool}`, 56px radius). Hover: `{colors.primary-hover}`."
- "Build dark section: `{colors.surface-dark}` background. CoinbaseDisplay 64px white text. Blue accent link (`{colors.primary}`)."
- "Design a card: `{colors.surface}` background, 12px radius, 1px border `{colors.primary-muted}` at low opacity. Title at 32px CoinbaseSans weight 400."
- "Create a primary pill button at 56px radius: `{colors.surface-cool}` bg, `{colors.ink}` text in CoinbaseSans 16px weight 600 with +0.16px letter-spacing. Hover: `{colors.primary-hover}` bg with white text."

### Iteration Guide
1. Pill radius is non-negotiable on CTAs — 56px minimum
2. Blue is functional only — never as decoration
3. Display at 1.00 line-height — financial statement gravitas
4. Alternate dark/light sections for chapter pacing
5. Four-font discipline: Display for hero, Sans for UI, Text for reading
