---
version: alpha
name: Intercom
description: Warm, editorial AI-first helpdesk system — warm cream canvas, off-black ink, Saans with extreme negative tracking, sharp 4px corners, and Fin Orange as the singular brand accent.

colors:
  # Base
  background: "#faf9f6"
  surface: "#ffffff"
  ink: "#111111"
  on-primary: "#ffffff"

  # Brand accent
  primary: "#ff5600"

  # Report palette (data viz)
  report-orange: "#fe4c02"
  report-blue: "#65b5ff"
  report-green: "#0bdf50"
  report-red: "#c41c1c"
  report-pink: "#ff2067"
  report-lime: "#b3e01c"
  green: "#00da00"
  deep-blue: "#0007cb"

  # Neutral scale (warm)
  black-80: "#313130"
  black-60: "#626260"
  black-50: "#7b7b78"
  content-tertiary: "#9c9fa5"
  warm-sand: "#d3cec6"

  # Borders / dividers (warm oat)
  border: "#dedbd6"

  # Hover / pressed states (opaque approximations)
  pressed-green: "#2c6415"
  border-soft: "#f1ebe2"  # was rgba via oklab — Google format requires hex

typography:
  display-hero:
    fontFamily: "Saans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 80px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -2.4px
  section-heading:
    fontFamily: "Saans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 54px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -1.6px
  sub-heading:
    fontFamily: "Saans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -1.2px
  card-title:
    fontFamily: "Saans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -0.96px
  feature-title:
    fontFamily: "Saans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -0.48px
  body-emphasis:
    fontFamily: "Saans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: -0.2px
  nav-ui:
    fontFamily: "Saans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: 0px
  body:
    fontFamily: "Saans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  body-light:
    fontFamily: "Saans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.40
    letterSpacing: 0px
  button:
    fontFamily: "Saans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button-bold:
    fontFamily: "LLMedium, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0.16px
  serif-body:
    fontFamily: "Serrif, ui-serif, Georgia, serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.40
    letterSpacing: -0.16px
  mono-label:
    fontFamily: "SaansMono, ui-monospace, monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.00
    letterSpacing: 0.6px

spacing:
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  4xl: 80px
  5xl: 96px

rounded:
  none: 0px
  sm: 4px
  md: 6px
  lg: 8px
  pill: 9999px

components:
  # Primary dark button — sharp 4px geometry
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 0px 14px
  button-primary-hover:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
  button-primary-active:
    backgroundColor: "{colors.pressed-green}"
    textColor: "{colors.surface}"

  # Outlined button
  button-outlined:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 0px 14px

  # Warm card-style button
  button-warm:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 16px

  # Card / container
  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 14px

  # Top navigation
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 16px 24px

  # Fin AI accent badge
  badge-ai:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
---

# Intercom Design System

## Overview

Intercom's website is a warm, confident customer service platform that communicates "AI-first helpdesk" through a clean, editorial design language. The page operates on a warm off-white canvas (`{colors.background}`) with off-black (`{colors.ink}`) text, creating an intimate, magazine-like reading experience. The signature Fin Orange (`{colors.primary}`) — named after Intercom's AI agent — serves as the singular vibrant accent against the warm neutral palette.

The typography uses Saans — a custom geometric sans-serif with aggressive negative letter-spacing (-2.4px at 80px, -0.48px at 24px) and a consistent 1.00 line-height across all heading sizes. This creates ultra-compressed, billboard-like headlines that feel engineered and precise. Serrif provides the serif companion for editorial moments, and SaansMono handles code and uppercase technical labels. MediumLL and LLMedium appear for specific UI contexts, creating a rich five-font ecosystem.

What distinguishes Intercom is its remarkably sharp geometry — 4px border-radius on buttons creates near-rectangular interactive elements that feel industrial and precise, contrasting with the warm surface colors. Button hover states use `scale(1.1)` expansion, creating a physical "growing" interaction. The border system uses warm oat tones (`{colors.border}`) and oklab-based opacity values for sophisticated color management.

**Key Characteristics:**
- Warm off-white canvas (`{colors.background}`) with oat-toned borders (`{colors.border}`)
- Saans font with extreme negative tracking (-2.4px at 80px) and 1.00 line-height
- Fin Orange (`{colors.primary}`) as singular brand accent
- Sharp 4px border-radius — near-rectangular buttons and elements
- Scale(1.1) hover with scale(0.85) active — physical button interaction
- SaansMono uppercase labels with wide tracking (0.6px–1.2px)
- Rich multi-color report palette (blue, green, red, pink, lime, orange)
- oklab color values for sophisticated opacity management

## Colors

### Primary
- **Off Black** (`{colors.ink}`): Primary text, button backgrounds.
- **Pure White** (`{colors.surface}`): Primary surface for cards and floating elements.
- **Warm Cream** (`{colors.background}`): Page canvas, button backgrounds, card surfaces.
- **Fin Orange** (`{colors.primary}`): Primary brand accent — reserved for AI features and product punctuation.

### Report Palette (data visualization only)
- `{colors.report-orange}` — secondary brand orange for charts
- `{colors.report-blue}`
- `{colors.report-green}`
- `{colors.report-red}`
- `{colors.report-pink}`
- `{colors.report-lime}`
- `{colors.green}`, `{colors.deep-blue}` — alternative chart accents

### Neutral Scale (Warm)
- `{colors.black-80}` — dark neutral
- `{colors.black-60}` — mid neutral
- `{colors.black-50}` — muted text
- `{colors.content-tertiary}` — tertiary content
- `{colors.warm-sand}` — light warm neutral

### Borders
- `{colors.border}` — warm oat divider
- `{colors.border-soft}` — softer interior border

## Typography

### Font Families
- **Primary**: `Saans`, fallbacks `Saans Fallback, ui-sans-serif, system-ui`
- **Serif**: `Serrif`, fallbacks `Serrif Fallback, ui-serif, Georgia`
- **Monospace**: `SaansMono`, fallbacks `SaansMono Fallback, ui-monospace`
- **UI**: `MediumLL` / `LLMedium`, fallbacks `system-ui, -apple-system`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens (`{typography.display-hero}`, `{typography.body}`) directly.

| Token | Use |
|---|---|
| `display-hero` | Maximum impact — landing hero |
| `section-heading` | Major section heads |
| `sub-heading` | Sub-sections |
| `card-title` | Card and feature titles |
| `feature-title` | Smaller feature heads |
| `body-emphasis` | Emphasized body, intro paragraphs |
| `nav-ui` | Navigation, UI text |
| `body` | Standard reading text |
| `body-light` | Lighter body text |
| `button` | Standard button labels |
| `button-bold` | LLMedium emphasis labels |
| `serif-body` | Editorial serif moments |
| `mono-label` | Uppercase technical labels |

### Principles
- **1.00 line-height across all headings** — locks display type into compressed billboard blocks.
- **Aggressive negative tracking** scales linearly with size: -2.4px at 80px, -0.48px at 24px.
- **Five-font ecosystem** — Saans for everything visible, Serrif for editorial moments, SaansMono for technical labels, MediumLL/LLMedium for specific UI contexts.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. The scale is `xs` (8px) → `5xl` (96px), with intermediate values at 12 / 16 / 24 / 32 / 48 / 64 / 80.

### Grid & Container
- Max content width: ~1280px centered
- Editorial single-column heroes pair with multi-column feature grids beneath

### Whitespace Philosophy
Intercom uses generous editorial spacing between sections (`3xl`–`5xl`) but keeps internal component padding tight (`md`–`lg`). The contrast between vast section breaks and dense component interiors creates a magazine-like reading rhythm.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Default — most surfaces sit flat on the warm canvas |
| Bordered (Level 1) | `1px solid {colors.border}` | Cards, inputs, dividers |
| Soft Border (Level 1b) | `1px solid {colors.border-soft}` | Interior containers, subtle separations |

**Shadow Philosophy**: Minimal shadows. Depth comes from warm border colors (`{colors.border}`) and subtle surface tints, not box-shadows. The warm cream canvas provides natural visual hierarchy without artificial elevation.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Sharp inline elements |
| `sm` | 4px | Buttons — the signature Intercom radius |
| `md` | 6px | Nav items, small interactive elements |
| `lg` | 8px | Cards, containers |
| `pill` | 9999px | Status indicators, AI badges, occasional pills |

The 4px button radius is the system's identity move — sharp enough to feel industrial, soft enough to avoid feeling brutalist.

## Components

The complete component spec lives in the `components:` token block above. Reference components directly (`{components.button-primary}`, `{components.card}`).

### Buttons
- **`button-primary`** — dark fill on warm cream, 4px radius, scale(1.1) hover.
- **`button-outlined`** — transparent fill with 1px ink border, same scale behavior.
- **`button-warm`** — cream surface with 1px soft border for low-emphasis actions.

### Cards
- **`card`** — warm cream surface with `{colors.border}` divider, 8px radius, no shadow.

### Inputs
- **`input`** — white surface, 4px radius, 1px warm border. Focus state shifts the border to `{colors.ink}`.

### Navigation
- **`nav-bar`** — white surface, off-black text, small 4–6px radius buttons, Fin Orange used only for AI accents.

### AI Badge
- **`badge-ai`** — Fin Orange fill, white text, small mono-label typography. The exclusive home of Fin Orange.

## Do's and Don'ts

### Do
- Use Saans with 1.00 line-height and negative tracking on all headings
- Apply 4px radius on buttons — sharp geometry is the identity
- Use Fin Orange (`{colors.primary}`) for AI/brand accent only
- Apply scale(1.1) hover on buttons
- Use warm neutrals (`{colors.background}`, `{colors.border}`)

### Don't
- Don't round buttons beyond 4px
- Don't use Fin Orange decoratively
- Don't use cool gray borders — always warm oat tones
- Don't skip the negative tracking on headings

---

## Responsive Behavior

Breakpoints: 425px, 530px, 600px, 640px, 768px, 896px

### Touch Targets
- Buttons sized for 44px minimum effective tap area through padding
- Nav links spaced for thumb-comfortable reach

### Collapsing Strategy
- Hero: 80px → 54px → 40px progressive scaling
- Section grids: 3-col → 2-col → stacked
- Negative tracking remains proportional at all sizes

---

## Agent Prompt Guide

### Quick Color Reference
- Text: Off Black (`{colors.ink}`)
- Background: Warm Cream (`{colors.background}`)
- Accent: Fin Orange (`{colors.primary}`)
- Border: Oat (`{colors.border}`)
- Muted: `{colors.black-50}`

### Example Component Prompts
- "Create hero: warm cream (`{colors.background}`) background. Saans 80px weight 400, line-height 1.00, letter-spacing -2.4px, `{colors.ink}`. Dark button (`{colors.ink}`, 4px radius). Hover: scale(1.1), white bg."
- "Build a card grid on warm cream, each card with 8px radius, 1px solid `{colors.border}`, 24px padding. Card title 32px Saans weight 400, letter-spacing -0.96px, line-height 1.00. Body 16px weight 400 line-height 1.50."
- "Add a Fin AI badge: Fin Orange (`{colors.primary}`) fill, white text in SaansMono uppercase 12px weight 500 with 0.6px tracking, 4px radius, 4px 8px padding. Reserve for AI features only."

### Iteration Guide
1. Sharp 4px is the brand — never round buttons further
2. Negative tracking scales with size — don't omit it on display type
3. Fin Orange is sacred — AI features only, never decorative
4. Warm neutrals only — no cool gray borders
5. Scale(1.1) on hover gives buttons their signature physical feel
