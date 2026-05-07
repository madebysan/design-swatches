---
version: alpha
name: AlignUI
description: Figma-first SaaS component system with Inter Variable weight 550, odd-numbered radii (5/7/9/11/13px), and dual-layer subtle elevation.

colors:
  # Surface
  background: "#ffffff"
  surface: "#ffffff"
  surface-muted: "#f7f7f7"
  surface-secondary: "#f2f2f2"

  # Ink + neutral scale
  ink: "#0a0a0a"
  ink-inverted: "#ffffff"
  text-secondary: "#2e2e2e"
  text-emphasis: "#3d3d3d"
  text-muted: "#525252"
  text-tertiary: "#707070"
  text-disabled: "#8f8f8f"
  text-placeholder: "#b8b8b8"

  on-background: "#0a0a0a"
  on-surface: "#0a0a0a"
  on-primary: "#ffffff"

  # Brand
  primary: "#335cff"
  primary-tint: "#e1e9ff"
  accent: "#f05023"

  # Semantic
  success: "#1fc16b"
  warning: "#f9c700"
  error: "#e5404c"

  # Borders
  border: "#ebebeb"
  border-strong: "#3d3d3d"

  # Focus + shadow
  focus-ring: "#99adff"  # was rgba(51,92,255,0.5) — flattened over white
  focus-ring-soft: "#ccd5ff"  # was rgba(51,92,255,0.2) — flattened
  shadow-near: "#f5f5f5"  # was rgba(0,0,0,0.04)
  shadow-edge: "#ededed"  # was rgba(61,61,61,0.12)
  shadow-soft: "#e6e6e6"  # was rgba(61,61,61,0.1)

typography:
  display-hero:
    fontFamily: "Inter Variable, Inter, system-ui, sans-serif"
    fontSize: 80px
    fontWeight: 550
    lineHeight: 1.05
    letterSpacing: -2.8px
  display-large:
    fontFamily: "Inter Variable, Inter, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 550
    lineHeight: 1.1
    letterSpacing: -1.344px
  heading-1:
    fontFamily: "Inter Variable, Inter, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 550
    lineHeight: 1.15
    letterSpacing: -0.8px
  heading-2:
    fontFamily: "Inter Variable, Inter, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 550
    lineHeight: 1.2
    letterSpacing: -0.896px
  heading-3:
    fontFamily: "Inter Variable, Inter, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 550
    lineHeight: 1.25
    letterSpacing: -0.56px
  heading-sub:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0px
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  label-medium:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: -0.084px
  label-mono:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: -0.084px
  caption:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0px

spacing:
  micro: 3px
  xs: 4px
  sm: 8px
  md: 10px
  lg: 12px
  xl: 16px
  2xl: 24px
  3xl: 32px
  4xl: 48px

rounded:
  none: 0px
  badge: 5px
  sm: 7px
  md: 9px
  lg: 11px
  xl: 13px
  pill-soft: 18px
  pill: 9999px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.label-medium}"
    padding: 16px 24px

  # Primary button — black on white
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-medium}"
    rounded: "{rounded.md}"
    padding: 8px 14px
  button-primary-hover:
    backgroundColor: "{colors.text-secondary}"

  # Outline button
  button-outline:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.label-medium}"
    rounded: "{rounded.md}"
    padding: 8px 14px

  # Secondary subtle button
  button-secondary:
    backgroundColor: "{colors.surface-secondary}"
    textColor: "{colors.text-tertiary}"
    typography: "{typography.label-medium}"
    rounded: "{rounded.sm}"
    padding: 8px 14px

  # Brand-accent CTA — used for hero brand moments
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-medium}"
    rounded: "{rounded.md}"
    padding: 8px 14px

  # Card
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Featured card (deeper radius)
  card-featured:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 32px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.label-medium}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"

  # Badge — odd small radius, not pill
  badge:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.badge}"
    padding: 2px 8px

  # Soft tinted alert/badge
  badge-tint:
    backgroundColor: "{colors.primary-tint}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.badge}"
    padding: 2px 8px

  # Status badges
  badge-success:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.badge}"
    padding: 2px 8px
  badge-warning:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.warning}"
    typography: "{typography.caption}"
    rounded: "{rounded.badge}"
    padding: 2px 8px
  badge-error:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.error}"
    typography: "{typography.caption}"
    rounded: "{rounded.badge}"
    padding: 2px 8px

  # Switch / toggle
  switch:
    backgroundColor: "{colors.surface-secondary}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: 2px

  # Dropdown / popover
  popover:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 16px

  # Modal
  modal:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 32px
---

# AlignUI Design System

## Overview

AlignUI is the design system that was designed in Figma first and then ported to code with unusual fidelity. The homepage announces its ambition: an 80px hero at Inter Variable **weight 550** (a non-integer weight, available only because it's a variable font) with `-2.8px` letter-spacing — a combination that reads simultaneously as neutral SaaS and as engineered. The palette is a carefully calibrated gray scale (`{colors.border}`, `{colors.text-secondary}`, `{colors.text-tertiary}`) with a **single saturated accent** — a warm orange-red (`{colors.accent}`) — that appears sparingly as the brand anchor.

Typography is the core differentiator. AlignUI uses three font variants: `__interVar` (Inter Variable at custom weights 550), `__Inter` (standard Inter at 400/500), and `__GeistMono` for technical labels. The variable-weight 550 is the defining choice — it sits between medium and semibold, giving display type a confident presence without the blockiness of weight 600.

The component vocabulary is unusually dense: radii at `5px`, `7px`, `9px`, `11px`, `13px` — odd-number values spaced 2px apart — the scan found 30 elements at `9px` radius. This creates a radius scale with much finer granularity than shadcn's `8/10/12/14` or Material's `4/8/16/24`, enabling components that look calibrated rather than pre-built.

**Key Characteristics:**
- Inter Variable at weight 550 — the non-standard display weight that IS the brand
- Neutral gray scale (`{colors.border}`, `{colors.text-secondary}`, `{colors.text-tertiary}`) with saturated orange (`{colors.accent}`) accent
- Odd-numbered radii (`5, 7, 9, 11, 13px`) — 2px granularity, calibrated feel
- Subtle dual-layer shadows — crisp 1px near-shadow + soft outer
- Geist Mono for technical labels at 14px weight 500 with `-0.084px` tracking
- Figma-first: design tokens are exported from Figma, not added after
- Focus ring color `{colors.focus-ring}` — saturated indigo, high-visibility

## Colors

### Neutral Scale
- **Neutral 950** (`{colors.ink}`): Primary text, headings.
- **Neutral 800** (`{colors.text-secondary}`): Secondary text (696 occurrences).
- **Neutral 700** (`{colors.text-emphasis}`): Emphasized body text.
- **Neutral 600** (`{colors.text-muted}`): Muted body.
- **Neutral 500** (`{colors.text-tertiary}`): Secondary muted text (97 occurrences).
- **Neutral 400** (`{colors.text-disabled}`): Disabled text.
- **Neutral 300** (`{colors.text-placeholder}`): Placeholders (126 occurrences).
- **Neutral 100** (`{colors.border}`): Primary border color (2,417 occurrences — by far the most-used color).
- **Neutral 50** (`{colors.surface-muted}`): Muted surface.
- **White** (`{colors.surface}`): Base canvas.

### Brand
- **Accent Orange** (`{colors.accent}`): Singular brand anchor — 48 occurrences. Used on hero accent, focused link state, brand moment.
- **Primary Blue** (`{colors.primary}`): Interactive elements, focus rings.
- **Accent Light** (`{colors.primary-tint}`): Subtle primary background tint.

### Semantic States
- **Success** (`{colors.success}`): Confirmation badges.
- **Warning** (`{colors.warning}`): Caution states.
- **Error** (`{colors.error}`): Destructive actions.

## Typography

### Font Family
- **Display**: `Inter Variable` (variable font with custom weight axis — 550 is the signature).
- **Body / UI**: `Inter` (standard weights 400, 500).
- **Monospace**: `Geist Mono` (for technical labels).

### Hierarchy

The complete type scale lives in the `typography:` token block above. Use those tokens directly via reference.

| Token | Use |
|---|---|
| `display-hero` | Hero — 80px, Inter Variable weight 550 |
| `display-large` | Large display — 48px |
| `heading-1` | Page titles — 40px |
| `heading-2` | Section heads — 32px |
| `heading-3` | Sub-section heads — 28px |
| `heading-sub` | UI sub-heads — 20px Inter weight 500 |
| `body` | Standard body — 16px Inter weight 400 |
| `label-medium` | Button labels, UI text — 14px Inter weight 500 |
| `label-mono` | Technical labels — 14px Geist Mono |
| `caption` | Captions — 11px Geist Mono |

### Principles
- **Weight 550 is unique**: Only accessible through Inter Variable's weight axis. This is AlignUI's most defensible typographic choice.
- **Mixed-weight within display**: Inter Var 550 for hero/display, Inter 500 for UI chrome, Inter 400 for body.
- **Letter-spacing micro-adjustments**: The `-0.084px` tracking on 14px labels is deliberate — barely perceptible but affects rendering rhythm.
- **Geist Mono at 14px/11px**: Both caption sizes use the same font family — the size differentiates.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 4px.

Dominant values: `xs` (4px — 55 uses), `sm` (8px — 22), `lg` (12px — 20), `md` (10px — 17), `micro` (3px — 16). The `micro` use is unusual — AlignUI calibrates spacing at micro-intervals.

### Grid
- 12-column with `2xl` (24px) gutters
- Max content width: `1280px`
- Sidebar layouts: `256px` sidebar + content

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | None | Background |
| Level 1 | Subtle 1px soft drop using `{colors.shadow-near}` | Card rest |
| Level 2 | Crisp 0.5px near + 1px edge ring using `{colors.shadow-edge}` | Card with visible edge |
| Level 3 | Soft 12px+24px atmospheric using `{colors.shadow-soft}` | Popover, dropdown |
| Level 4 | Wide 20px+40px ambient | Modal |

**Shadow Philosophy**: AlignUI uses dual-layer shadows where the first layer is a crisp `0.5px` or `1px` near-shadow for edge definition and the second is a soft atmospheric outer shadow. The slight half-pixel values suggest Figma-native design.

## Shapes

The radius scale is **odd-numbered** with 2px granularity — calibrated, not pre-built.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Edge cases |
| `badge` | 5px | Badges (21 uses) |
| `sm` | 7px | Small buttons, chips (15 uses) |
| `md` | 9px | Default buttons, inputs (30 uses — workhorse) |
| `lg` | 11px | Cards (8 uses) |
| `xl` | 13px | Featured cards (5 uses) |
| `pill-soft` | 18px | Pills, avatars |
| `pill` | 9999px | Switches |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Black bg, white text, `{rounded.md}` (9px) radius
- **`button-outline`** — White bg, hairline border, black text
- **`button-secondary`** — Soft gray bg, muted text, `{rounded.sm}` (7px) — odd value for distinction
- **`button-accent`** — Orange brand-moment CTA

### Cards
- **`card`** — White, hairline border, `{rounded.lg}` (11px), 24px padding, very subtle shadow
- **`card-featured`** — `{rounded.xl}` (13px), 32px padding

### Inputs
**`input`** — White bg, hairline border, `{rounded.md}` (9px), 8px × 12px padding. Focus uses `{colors.primary}` 2px border + `{colors.focus-ring-soft}` outer ring.

### Badges
- **`badge`** — `{rounded.badge}` (5px) — distinctive small rectangle, not pill
- **`badge-tint`** / **`badge-success`** / **`badge-warning`** / **`badge-error`** — Semantic variants

### Focus Ring (system-wide)
`{colors.focus-ring}` — indigo blue at 50% alpha (flattened). 2px thickness with 2px offset — accessibility-compliant, high-visibility.

## Do's and Don'ts

### Do
- Use Inter Variable at weight 550 for display — the variable font is the brand
- Use the odd-number radius scale (`{rounded.badge}/{rounded.sm}/{rounded.md}/{rounded.lg}/{rounded.xl}`) — calibrated, intentional
- Apply the `-0.084px` tracking on small UI text (14px labels)
- Pair Inter with Geist Mono for captions — don't mix with other monos
- Use subtle dual-layer shadows — a crisp 1px + soft outer
- Reserve the orange accent (`{colors.accent}`) for brand-moment use only

### Don't
- Don't use Inter at weight 500 for display — AlignUI is specifically 550
- Don't use even-number radii (`4, 8, 12`) — the odd-numbers are the signature
- Don't use dark mode without regenerating all tokens — AlignUI's palette is light-first
- Don't use pill radius on buttons — stays `{rounded.md}` (9px)
- Don't skip the focus ring — the saturated indigo is a brand element

---

## Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | Single column, sidebar drawer |
| md | `768px+` | 2-column grids |
| lg | `1024px+` | Full desktop |
| xl | `1280px+` | Max-width |

### Touch Targets
- Buttons: `36px+` minimum height
- Tappable list items: `44px` minimum

### Collapsing Strategy
- Hero: 80px → 48px → 32px, weight 550 maintained
- Nav: horizontal → hamburger drawer
- Sidebar: visible → collapsible → overlay
- Cards: multi-col → stacked, `{rounded.lg}` (11px) maintained

---

## Agent Prompt Guide

### Quick Color Reference
- Background: `{colors.background}`
- Text: `{colors.ink}` (primary), `{colors.text-tertiary}` (muted)
- Border: `{colors.border}`
- Surface: `{colors.surface-muted}`
- Primary: `{colors.primary}`
- Accent: `{colors.accent}`
- Focus: `{colors.focus-ring}`

### Example Component Prompts
- "Create a hero: white bg. Headline at 80px Inter Variable weight 550, letter-spacing -2.8px, line-height 1.05, color `{colors.ink}`. Subtitle 20px Inter weight 500 color `{colors.text-tertiary}`. Primary button: `{colors.ink}` bg, white text, `{rounded.md}` radius, 8px 14px padding, 14px Inter weight 500 tracking -0.084px."
- "Design a card: white bg, 1px solid `{colors.border}`, `{rounded.lg}` (11px) radius, 24px padding, subtle box-shadow with `{colors.shadow-near}` tint. Title 24px Inter Variable weight 550 letter-spacing -0.48px. Body 14px Inter weight 400 tracking -0.084px color `{colors.text-tertiary}`."
- "Build a focus ring on any interactive element: 2px solid `{colors.primary}` with 2px offset, `{colors.focus-ring-soft}` secondary ring. Must be perceivable on light backgrounds."

### Iteration Guide
1. Weight 550 on Inter Variable is the display signature — no substitutes
2. Odd-number radii (`5/7/9/11/13`) — resist rounding to even numbers
3. `-0.084px` tracking on 14px UI labels — micro-calibration
4. Dual-layer shadows with `0.5-1px` inner + soft outer
5. Orange (`{colors.accent}`) is a brand-moment color — reserve for accent surfaces
6. Focus rings are saturated indigo — accessibility as an aesthetic commitment
