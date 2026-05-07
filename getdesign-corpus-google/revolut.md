---
version: alpha
name: Revolut
description: Stadium-scale fintech confidence — Aeonik Pro at 136px weight 500, near-black + white binary canvas, universal pill buttons with generous padding, and zero shadows.

colors:
  # Primary
  background: "#ffffff"
  ink: "#191c1f"
  surface-light: "#f4f4f4"
  on-primary: "#ffffff"

  # Brand / Interactive
  primary: "#494fdf"
  accent-action: "#4f55f1"
  accent-blue: "#376cd5"

  # Semantic
  danger: "#e23b4a"
  deep-pink: "#e61e49"
  warning: "#ec7e00"
  yellow: "#b09000"
  teal: "#00a87e"
  light-green: "#428619"
  green-text: "#006400"
  light-blue: "#007bc2"
  brown: "#936d62"
  red-text: "#8b0000"

  # Neutrals
  text-secondary: "#505a63"
  text-muted: "#8d969e"
  border: "#c9c9cd"

  # Ghost-on-dark surface (opaque approx)
  ghost-on-dark: "#3a3d40"  # was rgba(244,244,244,0.1) over ink — flatten for hex

typography:
  display-mega:
    fontFamily: "Aeonik Pro, Arial, sans-serif"
    fontSize: 136px
    fontWeight: 500
    lineHeight: 1.00
    letterSpacing: -2.72px
  display-hero:
    fontFamily: "Aeonik Pro, Arial, sans-serif"
    fontSize: 80px
    fontWeight: 500
    lineHeight: 1.00
    letterSpacing: -0.8px
  section-heading:
    fontFamily: "Aeonik Pro, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.21
    letterSpacing: -0.48px
  sub-heading:
    fontFamily: "Aeonik Pro, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: -0.4px
  card-title:
    fontFamily: "Aeonik Pro, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.19
    letterSpacing: -0.32px
  feature-title:
    fontFamily: "Aeonik Pro, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  nav-ui:
    fontFamily: "Aeonik Pro, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: -0.09px
  body:
    fontFamily: "Inter, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0.24px
  body-semibold:
    fontFamily: "Inter, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.50
    letterSpacing: 0.16px
  body-bold-link:
    fontFamily: "Inter, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.50
    letterSpacing: 0.24px

spacing:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 14px
  xl: 16px
  2xl: 20px
  3xl: 24px
  4xl: 32px
  5xl: 40px
  6xl: 48px
  7xl: 80px
  8xl: 120px

rounded:
  md: 12px
  lg: 20px
  pill: 9999px

components:
  # Buttons (universal pill)
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-ui}"
    rounded: "{rounded.pill}"
    padding: 14px 32px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-ui}"
    rounded: "{rounded.pill}"
    padding: 14px 34px
  button-outlined:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-ui}"
    rounded: "{rounded.pill}"
    padding: 14px 32px
  button-ghost-on-dark:
    backgroundColor: "{colors.ghost-on-dark}"
    textColor: "{colors.surface-light}"
    typography: "{typography.nav-ui}"
    rounded: "{rounded.pill}"
    padding: 14px 32px

  # Cards
  card:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-small:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 16px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-ui}"
    padding: 16px 24px
  nav-link:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-ui}"
    padding: 8px 12px

  # Inputs
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 14px 16px

  # Surface light alt
  surface-secondary:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 32px

  # Semantic text/badges (product surface)
  text-danger:
    backgroundColor: "{colors.background}"
    textColor: "{colors.danger}"
    typography: "{typography.body}"
  text-deep-pink:
    backgroundColor: "{colors.background}"
    textColor: "{colors.deep-pink}"
    typography: "{typography.body}"
  text-warning:
    backgroundColor: "{colors.background}"
    textColor: "{colors.warning}"
    typography: "{typography.body}"
  text-yellow:
    backgroundColor: "{colors.background}"
    textColor: "{colors.yellow}"
    typography: "{typography.body}"
  text-teal:
    backgroundColor: "{colors.background}"
    textColor: "{colors.teal}"
    typography: "{typography.body}"
  text-light-green:
    backgroundColor: "{colors.background}"
    textColor: "{colors.light-green}"
    typography: "{typography.body}"
  text-green:
    backgroundColor: "{colors.background}"
    textColor: "{colors.green-text}"
    typography: "{typography.body}"
  text-light-blue:
    backgroundColor: "{colors.background}"
    textColor: "{colors.light-blue}"
    typography: "{typography.body}"
  text-brown:
    backgroundColor: "{colors.background}"
    textColor: "{colors.brown}"
    typography: "{typography.body}"
  text-red:
    backgroundColor: "{colors.background}"
    textColor: "{colors.red-text}"
    typography: "{typography.body}"
  text-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.body}"
  text-muted:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-muted}"
    typography: "{typography.body}"

  # Brand tokens
  text-primary-brand:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.body-bold-link}"
  text-action:
    backgroundColor: "{colors.background}"
    textColor: "{colors.accent-action}"
    typography: "{typography.body-semibold}"
  text-link:
    backgroundColor: "{colors.background}"
    textColor: "{colors.accent-blue}"
    typography: "{typography.body}"

  # Border rule
  border-rule:
    backgroundColor: "{colors.border}"
    rounded: "{rounded.md}"
    padding: 0px
---

# Revolut Design System

## Overview

Revolut's website is fintech confidence distilled into pixels — a design system that communicates "your money is in capable hands" through massive typography, generous whitespace, and a disciplined neutral palette. The visual language is built on Aeonik Pro, a geometric grotesque that creates billboard-scale headlines at 136px with weight 500 and aggressive negative tracking (-2.72px). This isn't subtle branding; it's fintech at stadium scale.

The color system is built on a comprehensive `--rui-*` (Revolut UI) token architecture with semantic naming for every state: danger (`{colors.danger}`), warning (`{colors.warning}`), teal (`{colors.teal}`), blue (`{colors.primary}`), deep-pink (`{colors.deep-pink}`), and more. But the marketing surface itself is remarkably restrained — near-black (`{colors.ink}`) and pure white (`{colors.background}`) dominate, with the colorful semantic tokens reserved for the product interface, not the marketing page.

What distinguishes Revolut is its pill-everything button system. Every button uses 9999px radius — primary dark (`{colors.ink}`), secondary light (`{colors.surface-light}`), outlined (transparent + 2px solid), and ghost on dark. The padding is generous (14px 32–34px), creating large, confident touch targets. Combined with Inter for body text at various weights and positive letter-spacing (0.16px–0.24px), the result is a design that feels both premium and accessible — banking for the modern era.

**Key Characteristics:**
- Aeonik Pro display at 136px weight 500 — billboard-scale fintech headlines
- Near-black (`{colors.ink}`) + white binary with comprehensive `--rui-*` semantic tokens
- Universal pill buttons (9999px radius) with generous padding (14px 32px)
- Inter for body text with positive letter-spacing (0.16px–0.24px)
- Rich semantic color system: blue, teal, pink, yellow, green, brown, danger, warning
- Zero shadows detected — depth through color contrast only
- Tight display line-heights (1.00) with relaxed body (1.50–1.56)

## Colors

### Primary
- **Revolut Dark** (`{colors.ink}`): Primary dark surface, button background, near-black text.
- **Pure White** (`{colors.background}`): Primary light surface.
- **Light Surface** (`{colors.surface-light}`): Secondary button background, subtle surface.

### Brand / Interactive
- **Revolut Blue** (`{colors.primary}`): Primary brand blue.
- **Action Blue** (`{colors.accent-action}`): Header accent.
- **Blue Text** (`{colors.accent-blue}`): Link blue.

### Semantic
- **Danger Red** (`{colors.danger}`): Error/destructive.
- **Deep Pink** (`{colors.deep-pink}`): Critical accent.
- **Warning Orange** (`{colors.warning}`): Warning states.
- **Yellow** (`{colors.yellow}`): Attention.
- **Teal** (`{colors.teal}`): Success/positive.
- **Light Green** (`{colors.light-green}`): Secondary success.
- **Green Text** (`{colors.green-text}`): Green text.
- **Light Blue** (`{colors.light-blue}`): Informational.
- **Brown** (`{colors.brown}`): Warm neutral accent.
- **Red Text** (`{colors.red-text}`): Dark red text.

### Neutral Scale
- **Mid Slate** (`{colors.text-secondary}`): Secondary text.
- **Cool Gray** (`{colors.text-muted}`): Muted text, tertiary.
- **Gray Tone** (`{colors.border}`): Borders/dividers.

## Typography

### Font Families
- **Display**: `Aeonik Pro` — geometric grotesque, no detected fallbacks.
- **Body / UI**: `Inter` — standard system sans.
- **Fallback**: `Arial` for specific button contexts.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-mega}`, `{typography.body}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-mega` | 136px Aeonik Pro 500 — stadium-scale hero |
| `display-hero` | 80px — primary hero |
| `section-heading` | 48px — feature sections |
| `sub-heading` | 40px — sub-sections |
| `card-title` | 32px — card headings |
| `feature-title` | 24px regular — light headings |
| `nav-ui` | 20px — navigation, buttons |
| `body-large` | 18px Inter — introductions |
| `body` | 16px Inter — standard reading |
| `body-semibold` | 16px Inter 600 — emphasized |
| `body-bold-link` | 16px Inter 700 — bold links |

### Principles
- **Weight 500 as display default**: Aeonik Pro uses medium (500) for ALL headings — no bold. This creates authority through size and tracking, not weight.
- **Billboard tracking**: -2.72px at 136px is extremely compressed — text designed to be read at a glance, like airport signage.
- **Positive tracking on body**: Inter uses +0.16px to +0.24px, creating airy, well-spaced reading text that contrasts with the compressed headings.

## Layout

### Spacing System
Base unit is **8px**. Large section spacing 80–120px (`7xl`–`8xl`).

### Grid
- Centered max-width container
- Generous side margins
- Section alternation between dark and light

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Everything — Revolut uses zero shadows |
| Focus | `0 0 0 0.125rem` ring | Accessibility focus |

**Shadow Philosophy**: Revolut uses ZERO shadows. Depth comes entirely from the dark/light section contrast and the generous whitespace between elements.

## Shapes

| Token | Value | Use |
|---|---|---|
| `md` | 12px | Navigation, small buttons |
| `lg` | 20px | Feature cards |
| `pill` | 9999px | All buttons |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly rather than reconstructing them.

### Buttons
- **`button-primary`** — Dark pill (`{colors.ink}`), white text, 14px 32px padding. Hover: opacity 0.85.
- **`button-secondary`** — Light pill (`{colors.surface-light}`), black text, 14px 34px padding.
- **`button-outlined`** — Transparent fill, 2px solid dark border.
- **`button-ghost-on-dark`** — Translucent surface on dark with light text and 2px border.

### Cards
- **`card`** — 20px radius for feature cards.
- **`card-small`** — 12px radius for small containers.
- No shadows — flat surfaces with color contrast.

### Navigation
- **`nav-bar`** — Aeonik Pro 20px weight 500. Clean header.
- **`nav-link`** — Pill CTAs right-aligned.

### Inputs
- **`input`** — Standard surface input with 12px radius.

### Surfaces
- **`surface-secondary`** — Light alternate surface.

### Semantic Text Tokens
- **`text-danger`** / **`text-warning`** / **`text-teal`** / **`text-yellow`** / **`text-green`** / **`text-light-green`** / **`text-light-blue`** / **`text-brown`** / **`text-red`** / **`text-deep-pink`** / **`text-secondary`** / **`text-muted`** — Comprehensive semantic text colors for product surfaces.

### Brand Tokens
- **`text-primary-brand`** — Revolut Blue text.
- **`text-action`** — Action accent text.
- **`text-link`** — Standard link color.

## Do's and Don'ts

### Do
- Use Aeonik Pro weight 500 for all display headings
- Apply 9999px radius to all buttons — pill shape is universal
- Use generous button padding (14px 32px)
- Keep the palette to near-black + white for marketing surfaces
- Apply positive letter-spacing on Inter body text

### Don't
- Don't use shadows — Revolut is flat by design
- Don't use bold (700) for Aeonik Pro headings — 500 is the weight
- Don't use small buttons — the generous padding is intentional
- Don't apply semantic colors to marketing surfaces — they're for the product

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile Small | <400px | Compact, single column |
| Mobile | 400–720px | Standard mobile |
| Tablet | 720–1024px | 2-column layouts |
| Desktop | 1024–1280px | Standard desktop |
| Large | 1280–1920px | Full layout |

## Agent Prompt Guide

### Quick Color Reference
- Dark: Revolut Dark (`{colors.ink}`)
- Light: White (`{colors.background}`)
- Surface: Light (`{colors.surface-light}`)
- Blue: Revolut Blue (`{colors.primary}`)
- Danger: Red (`{colors.danger}`)
- Success: Teal (`{colors.teal}`)

### Example Component Prompts
- "Create a hero: white background. Headline at 136px Aeonik Pro weight 500, line-height 1.00, letter-spacing -2.72px, `{colors.ink}` text. Dark pill CTA (`{colors.ink}`, 9999px, 14px 32px). Outlined pill secondary (transparent, 2px solid `{colors.ink}`)."
- "Build a pill button: `{colors.ink}` background, white text, 9999px radius, 14px 32px padding, 20px Aeonik Pro weight 500. Hover: opacity 0.85."

### Iteration Guide
1. Aeonik Pro 500 for headings — never bold
2. All buttons are pills (9999px) with generous padding
3. Zero shadows — flat is the Revolut identity
4. Near-black + white for marketing, semantic colors for product
