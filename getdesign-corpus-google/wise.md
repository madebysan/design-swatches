---
version: alpha
name: Wise
description: Bold, confident fintech — warm off-white canvas with near-black text, lime-green Wise accent, Wise Sans at weight 900 with 0.85 line-height, pill buttons with scale(1.05) hover.

colors:
  # Primary brand
  background: "#ffffff"
  surface: "#ffffff"
  ink: "#0e0f0c"
  primary: "#9fe870"          # Wise Green
  on-primary: "#163300"       # Dark Green button text
  primary-container: "#e2f6d5"  # Light Mint
  primary-hover: "#cdffad"     # Pastel Green

  # Semantic
  success: "#054d28"
  danger: "#d03238"
  warning: "#ffd11a"
  info-tint: "#d6f0fb"        # was rgba(56,200,255,0.10) — flattened
  bright-orange: "#ffc091"

  # Neutral
  warm-dark: "#454745"
  gray: "#868685"
  light-surface: "#e8ebe6"

  # Borders & rings
  border: "#dbdcd9"           # was rgba(14,15,12,0.12) — flattened
  border-focus: "#868685"

  # Subtle nav hover
  nav-hover: "#e8f4dd"        # was rgba(211,242,192,0.4) — flattened

  # Subtle secondary fill
  subtle-fill: "#e3e9dc"      # was rgba(22,51,0,0.08) — flattened

typography:
  display-mega:
    fontFamily: "Wise Sans, Inter, sans-serif"
    fontSize: 126px
    fontWeight: 900
    lineHeight: 0.85
    letterSpacing: 0px
    fontFeature: "calt"
  display-hero:
    fontFamily: "Wise Sans, Inter, sans-serif"
    fontSize: 96px
    fontWeight: 900
    lineHeight: 0.85
    letterSpacing: 0px
    fontFeature: "calt"
  section-heading:
    fontFamily: "Wise Sans, Inter, sans-serif"
    fontSize: 64px
    fontWeight: 900
    lineHeight: 0.85
    letterSpacing: 0px
    fontFeature: "calt"
  sub-heading:
    fontFamily: "Wise Sans, Inter, sans-serif"
    fontSize: 40px
    fontWeight: 900
    lineHeight: 0.85
    letterSpacing: 0px
    fontFeature: "calt"
  alt-heading:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 78px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -2.34px
    fontFeature: "calt"
  card-title:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: -0.39px
    fontFeature: "calt"
  feature-title:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.396px
    fontFeature: "calt"
  body:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.44
    letterSpacing: 0.18px
    fontFeature: "calt"
  body-semibold:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: -0.108px
    fontFeature: "calt"
  button-ui:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: -0.108px
    fontFeature: "calt"
  caption:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.084px
    fontFeature: "calt"
  small:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.084px
    fontFeature: "calt"

spacing:
  hairline: 1px
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px

rounded:
  micro: 2px
  sm: 10px
  card: 16px
  md: 20px
  lg: 30px
  section: 40px
  mega: 1000px
  pill: 9999px

components:
  # Buttons
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 5px 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"

  button-secondary:
    backgroundColor: "{colors.subtle-fill}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  # Cards
  card-small:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: 16px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-large:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.section}"
    padding: 32px
  card-accent:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Inputs
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"

  # Navigation
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-semibold}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-semibold}"
    padding: 8px 16px
  nav-link-hover:
    backgroundColor: "{colors.nav-hover}"
    textColor: "{colors.ink}"

  # Badge
  badge-mint:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.on-primary}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: 2px 8px

  # Stat / display
  stat-display:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.section-heading}"
    padding: 0px

  # Semantic states (referenced by color)
  alert-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  alert-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  alert-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  alert-info:
    backgroundColor: "{colors.info-tint}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
---

# Wise Design System

## Overview

Wise's website is a bold, confident fintech platform that communicates "money without borders" through massive typography and a distinctive lime-green accent. The design operates on a warm off-white canvas with near-black text (`{colors.ink}`) and a signature Wise Green (`{colors.primary}`) — a fresh, lime-bright color that feels alive and optimistic, unlike the corporate blues of traditional banking.

The typography uses Wise Sans — a proprietary font used at extreme weight 900 (black) for display headings with a remarkably tight line-height of 0.85 and OpenType `"calt"` (contextual alternates). At 126px, the text is so dense it feels like a protest sign — bold, urgent, and impossible to ignore. Inter serves as the body font with weight 600 as the default for emphasis, creating a consistently confident voice.

What distinguishes Wise is its green-on-white-on-black material palette. Lime Green (`{colors.primary}`) appears on buttons with dark green text (`{colors.on-primary}`), creating a nature-inspired CTA that feels fresh. Hover states use `scale(1.05)` expansion rather than color changes — buttons physically grow on interaction. The border-radius system uses 9999px for buttons (pill), 30px–40px for cards, and the shadow system is minimal — just subtle ring shadows.

**Key Characteristics:**
- Wise Sans at weight 900, 0.85 line-height — billboard-scale bold headlines
- Lime Green (`{colors.primary}`) accent with dark green text (`{colors.on-primary}`) — nature-inspired fintech
- Inter body at weight 600 as default — confident, not light
- Near-black (`{colors.ink}`) primary with warm green undertone
- Scale(1.05) hover animations — buttons physically grow
- OpenType `"calt"` on all text
- Pill buttons (9999px) and large rounded cards (30px–40px)
- Semantic color system with comprehensive state management

## Colors

### Primary Brand
- **Near Black** (`{colors.ink}`): Primary text, background for dark sections.
- **Wise Green** (`{colors.primary}`): Primary CTA button, brand accent.
- **Dark Green** (`{colors.on-primary}`): Button text on green, deep green accent.
- **Light Mint** (`{colors.primary-container}`): Soft green surface, badge backgrounds.
- **Pastel Green** (`{colors.primary-hover}`): Hover accent.

### Semantic
- **Positive Green** (`{colors.success}`): Success.
- **Danger Red** (`{colors.danger}`): Error/destructive.
- **Warning Yellow** (`{colors.warning}`): Warnings.
- **Info Cyan** (`{colors.info-tint}`): Information tint.
- **Bright Orange** (`{colors.bright-orange}`): Warm accent.

### Neutral
- **Warm Dark** (`{colors.warm-dark}`): Secondary text, borders.
- **Gray** (`{colors.gray}`): Muted text, tertiary.
- **Light Surface** (`{colors.light-surface}`): Subtle green-tinted light surface.

## Typography

### Font Families
- **Display**: Wise Sans, fallback Inter — OpenType `"calt"` enabled
- **Body / UI**: Inter, fallbacks Helvetica, Arial

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-mega` | 126px Wise Sans 900 — billboard-scale |
| `display-hero` | 96px Wise Sans 900 — hero |
| `section-heading` | 64px Wise Sans 900 — section heads |
| `sub-heading` | 40px Wise Sans 900 — sub-section heads |
| `alt-heading` | 78px Inter 600 — alternate heading |
| `card-title` | 26px Inter 600 |
| `feature-title` | 22px Inter 600 |
| `body` | 18px Inter 400 |
| `body-semibold` | 18px Inter 600 — default body emphasis |
| `button-ui` | 18px Inter 600 |
| `caption` | 14px Inter 400 |
| `small` | 12px Inter 400 |

### Principles
- **Weight 900 as identity**: Wise Sans Black (900) is used exclusively for display — the heaviest weight in any analyzed system. It creates text that feels stamped, pressed, physical.
- **0.85 line-height**: The tightest display line-height analyzed. Letters overlap vertically, creating dense, billboard-like text blocks.
- **"calt" everywhere**: Contextual alternates enabled on ALL text — both Wise Sans and Inter.
- **Weight 600 as body default**: Inter Semibold is the standard reading weight — confident, not light.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

### Grid & Container
- Hero: full-width with massive Wise Sans display
- 2-column feature blocks
- Pill CTAs right-aligned
- Generous section padding

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Default |
| Ring (Level 1) | `1px solid {colors.border}` | Card borders |
| Inset (Level 2) | `1px solid {colors.border-focus}` inset | Input focus |

**Shadow Philosophy**: Wise uses minimal shadows — ring shadows only. Depth comes from the bold green accent against the neutral canvas.

## Shapes

| Token | Value | Use |
|---|---|---|
| `micro` | 2px | Links, inputs |
| `sm` | 10px | Comboboxes, inputs |
| `card` | 16px | Small cards, buttons, radio |
| `md` | 20px | Links, medium cards |
| `lg` | 30px | Feature cards |
| `section` | 40px | Tables, large cards |
| `mega` | 1000px | Presentation elements |
| `pill` | 9999px | All buttons, images |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Wise Green pill (`9999px` radius), Dark Green text, padding 5px 16px. Hover: `scale(1.05)`. Active: `scale(0.95)`.
- **`button-secondary`** — subtle dark-green-tinted pill, ink text. Same scale hover/active behavior.

### Cards
- 1px solid `{colors.border}` ring border
- Radii: 16px (small), 30px (medium), 40px (large)
- Subtle ring shadow only

### Navigation
- Green-tinted hover background
- Clean header with Wise wordmark
- Pill CTAs right-aligned

## Do's and Don'ts

### Do
- Use Wise Sans weight 900 for display — the extreme boldness IS the brand
- Apply line-height 0.85 on Wise Sans display — ultra-tight is intentional
- Use Lime Green (`{colors.primary}`) for primary CTAs with Dark Green (`{colors.on-primary}`) text
- Apply `scale(1.05)` hover and `scale(0.95)` active on buttons
- Enable `"calt"` on all text
- Use Inter weight 600 as the body default

### Don't
- Don't use light font weights for Wise Sans — only 900
- Don't relax the 0.85 line-height on display — the density is the identity
- Don't use the Wise Green as background for large surfaces — it's for buttons and accents
- Don't skip the scale animation on buttons
- Don't use traditional shadows — ring shadows only

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <576px | Single column |
| Tablet | 576–992px | 2-column |
| Desktop | 992–1440px | Full layout |
| Large | >1440px | Expanded |

---

## Agent Prompt Guide

### Quick Color Reference
- Text: Near Black (`{colors.ink}`)
- Background: White (`{colors.background}` / off-white)
- Accent: Wise Green (`{colors.primary}`)
- Button text: Dark Green (`{colors.on-primary}`)
- Secondary: Gray (`{colors.gray}`)

### Example Component Prompts
- "Create hero: white background. Headline at 96px Wise Sans weight 900, line-height 0.85, 'calt' enabled, `{colors.ink}` text. Green pill CTA (`{colors.primary}`, 9999px radius, 5px 16px padding, `{colors.on-primary}` text). Hover: scale(1.05)."
- "Build a card: 30px radius, 1px solid `{colors.border}`. Title at 22px Inter weight 600, body at 18px weight 400."

### Iteration Guide
1. Wise Sans 900 at 0.85 line-height — the extreme weight IS the brand
2. Lime Green for buttons only — dark green text on green background
3. Scale animations (1.05 hover, 0.95 active) on all interactive elements
4. "calt" on everything — contextual alternates are mandatory
5. Inter 600 for body — confident reading weight
