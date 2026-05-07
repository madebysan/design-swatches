---
version: alpha
name: Atlassian Design System
description: Enterprise SaaS vocabulary for Jira/Confluence/Trello/Bitbucket — Atlassian Sans variable-font weight 653, semantic ds-token naming, electric blue brand, dual-layer shadows, and accessibility-first defaults.

colors:
  # Surface
  background: "#ffffff"
  surface: "#ffffff"
  surface-muted: "#f8f9fa"

  # Brand
  primary: "#1868db"
  brand-boldest: "#1c2b42"
  brand-subtlest: "#e8f1ff"
  brand-subtlest-hovered: "#cfe1fd"
  brand-pressed: "#adcbfb"

  # Neutral scale
  ink: "#101214"
  ink-inverted: "#ffffff"
  text-secondary: "#1e1f21"
  text-label: "#44546f"
  text-muted: "#505258"
  text-disabled: "#7d818a"
  text-placeholder: "#b3b9c4"

  on-background: "#101214"
  on-surface: "#101214"
  on-primary: "#ffffff"

  # Borders
  border: "#dcdfe4"

  # Accent (sub-brand)
  saffron: "#fca700"
  green: "#6a9a23"
  magenta: "#af59e1"
  purple: "#af5eff"
  orange: "#e06c00"
  teal: "#206a83"
  blue-bolder: "#123263"

  # Semantic
  danger: "#ae2e24"
  warning-text: "#9e4c00"

  # Shadow tints (opaque approximations of rgba(30,31,33,…))
  shadow-near: "#cccccc"  # was rgba(30,31,33,0.31) — flattened
  shadow-soft: "#dadbdc"  # was rgba(30,31,33,0.25) — flattened
  shadow-medium: "#e8e9eb"  # was rgba(30,31,33,0.15) — flattened
  shadow-modal: "#ebebeb"  # was rgba(0,0,0,0.09) — flattened

typography:
  display-giant:
    fontFamily: "Atlassian Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: 112px
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: 0px
  display-hero:
    fontFamily: "Atlassian Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: 68px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: 0px
  display-large:
    fontFamily: "Atlassian Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0px
  display-charlie:
    fontFamily: "Charlie Display, Atlassian Sans, -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 653
    lineHeight: 1.15
    letterSpacing: 0px
  heading-1:
    fontFamily: "Atlassian Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: 40px
    fontWeight: 653
    lineHeight: 1.15
    letterSpacing: 0px
  heading-2:
    fontFamily: "Atlassian Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  heading-3:
    fontFamily: "Atlassian Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0px
  body-large:
    fontFamily: "Atlassian Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Atlassian Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  caption:
    fontFamily: "Atlassian Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px

spacing:
  micro: 2px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  2xl: 24px
  3xl: 32px

rounded:
  none: 0px
  xs: 2px
  badge: 3px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 28px
  pill: 9999px

components:
  # Top app bar / nav
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 24px

  # Primary CTA — brand blue
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-primary-hover:
    backgroundColor: "{colors.blue-bolder}"
    textColor: "{colors.on-primary}"

  # Subtle button
  button-subtle:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.text-label}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-subtle-hover:
    backgroundColor: "{colors.border}"
    textColor: "{colors.text-label}"

  # Link button
  button-link:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 4px 8px

  # Danger button
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 8px 16px

  # Card
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px

  # Featured marketing card
  card-marketing:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 32px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"

  # Status badges — distinctive 3px radius
  badge:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.text-label}"
    typography: "{typography.caption}"
    rounded: "{rounded.badge}"
    padding: 2px 8px
  badge-success:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.green}"
    typography: "{typography.caption}"
    rounded: "{rounded.badge}"
    padding: 2px 8px
  badge-warning:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.warning-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.badge}"
    padding: 2px 8px
  badge-danger:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.danger}"
    typography: "{typography.caption}"
    rounded: "{rounded.badge}"
    padding: 2px 8px
  badge-in-progress:
    backgroundColor: "{colors.brand-subtlest}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.badge}"
    padding: 2px 8px
  badge-done:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.purple}"
    typography: "{typography.caption}"
    rounded: "{rounded.badge}"
    padding: 2px 8px

  # Toolbar icon button
  button-icon:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.badge}"
    size: 32px

  # Dropdown / popover
  popover:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 16px

  # Modal dialog
  modal:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 32px
---

# Atlassian Design System

## Overview

The Atlassian Design System is the enterprise design vocabulary that powers Jira, Confluence, Trello, and Bitbucket — four products serving 250,000+ organizations, with a design system that has to stay consistent across 30 years of product evolution. The homepage opens on a clean white canvas (`{colors.background}`) with near-black text (`{colors.ink}`) and an **unmistakable blue** (`{colors.primary}`) — Atlassian's primary brand color, applied sparingly but with authority. This is enterprise SaaS perfected: precise, accessible, boringly consistent in the best possible way.

Typography uses Atlassian's **custom typeface — Atlassian Sans** — with a secondary **Charlie Display** for marketing headlines and **Atlassian Mono** for code. The sans uses an unusual weight 653 (variable-font custom axis) for the display tier, along with more conventional 500/700. The 653 weight is between semibold (600) and bold (700), giving display type a distinct confidence without shouting.

The defining differentiator is Atlassian's **semantic token vocabulary** — 24+ design tokens found in the CSS scan, named with precise intent: `--ds-background-brand-subtlest-hovered`, `--ds-text-accent-teal`, `--ds-background-brand-boldest`. Each token encodes role + intensity + state. This is enterprise design systems done right — tokens that describe purpose, not appearance.

**Key Characteristics:**
- Atlassian Sans (custom typeface) with weight 653 as a variable-font signature
- Electric blue brand (`{colors.primary}`) applied sparingly as primary accent
- Rich palette of sub-brand accent colors (saffron, teal, purple, magenta, orange)
- `4px` / `8px` dominant radii — conservative, enterprise-appropriate
- Semantic token naming (`ds-background-brand-subtlest-hovered`)
- Dual-layer shadow system for precise elevation
- Accessibility-first: WCAG AAA compliance by default
- Design-for-scale: Jira alone has 1,000+ distinct UI views

## Colors

### Brand
- **Brand Blue** (`{colors.primary}`): Primary brand color — 426 occurrences. CTAs, links, active states.
- **Brand Boldest** (`{colors.brand-boldest}`): Deep navy for dark brand surfaces.
- **Brand Subtlest** (`{colors.brand-subtlest}`): Pale blue tint for hover states.
- **Brand Subtlest Hovered** (`{colors.brand-subtlest-hovered}`): Slightly stronger hover tint.
- **Brand Pressed** (`{colors.brand-pressed}`): Active press state.

### Neutral Scale
- **Neutral 900** (`{colors.ink}`): Primary text, strongest emphasis.
- **Neutral 800** (`{colors.text-secondary}`): Dark text.
- **Neutral 700** (`{colors.text-label}`): Label text.
- **Neutral 600** (`{colors.text-muted}`): Secondary text — 146 occurrences.
- **Neutral 400** (`{colors.text-disabled}`): Muted text.
- **Neutral 300** (`{colors.text-placeholder}`): Placeholders, disabled.
- **Neutral 200** (`{colors.border}`): Default borders.
- **Neutral 100** (`{colors.surface-muted}`): Muted surface.
- **Neutral 0** (`{colors.surface}`): Base canvas.

### Accent (sub-brand colors)
- **Saffron** (`{colors.saffron}`): Highlighting warnings.
- **Grass Green** (`{colors.green}`): Success states (44 occurrences).
- **Magenta** (`{colors.magenta}`): Status indicators (27 occurrences).
- **Purple** (`{colors.purple}`): Beta features, new indicators.
- **Orange** (`{colors.orange}`): Warnings.
- **Teal** (`{colors.teal}`): Info states.
- **Blue Bolder** (`{colors.blue-bolder}`): Deep blue for accent-blue text.

### Semantic
- **Danger** (`{colors.danger}`): Destructive.
- **Warning** (`{colors.warning-text}`): Warning text.

## Typography

### Font Family
- **Primary**: `Atlassian Sans` — variable font with weight axis including 475, 500, 653, 700.
- **Display**: `Charlie Display` — used for marketing hero moments only.
- **Monospace**: `Atlassian Mono` — custom mono for code.
- Fallback stack: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Use those tokens directly.

| Token | Use |
|---|---|
| `display-giant` | Marketing-only — 112px |
| `display-hero` | Marketing hero — 68px |
| `display-large` | Marketing large display — 44px |
| `display-charlie` | Charlie Display marketing — 32px weight 653 |
| `heading-1` | App page titles — 40px weight 653 |
| `heading-2` | Section heads — 28px weight 500 |
| `heading-3` | Sub-section heads — 24px |
| `body-large` | Body paragraphs — 16px |
| `body` | Standard reading text — 14px |
| `caption` | Code, technical labels — Atlassian Mono |

### Principles
- **Weight 653 is unique**: Available via Atlassian Sans's variable font weight axis. Sits between semibold and bold for display authority.
- **No letter-spacing**: Atlassian explicitly keeps tracking at normal across all sizes — generous and accessible.
- **Charlie Display for marketing only**: H2/H3 inside app UI uses Atlassian Sans; Charlie appears only on marketing pages.
- **Atlassian Mono for code**: Distinct from typical Mono Sans or JetBrains Mono — branded consistency.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 4px (Atlassian's `grid` token).

Dominant values: `md` (8px — 55 uses), `xl` (16px — 18), `lg` (12px — 14), `2xl` (24px — 7), `sm` (6px — 20). Token names: `space.100` (8px), `space.200` (16px), `space.400` (32px).

### Grid
- Atlassian's `Grid` primitive with `gap`, `alignItems`, `justifyContent` props
- App layout: persistent 56px left rail + 240px nav panel + content
- Marketing: 12-column with `2xl` gutter, max `1200px`

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | None | Background |
| Level 1 | Crisp 1px hairline + soft 1px+1px drop using `{colors.shadow-soft}` | Card rest |
| Level 2 | 4px+8px medium drop using `{colors.shadow-medium}` | Card hover, menu |
| Level 3 | 8px+12px wide drop using `{colors.shadow-medium}` | Dropdown, popover |
| Level 4 | 40px+20px+20px atmospheric using `{colors.shadow-modal}` | Modal dialogs (unusual spread value) |

**Shadow Philosophy**: Atlassian uses dual-layer shadows with a `0 0 1px` near-shadow for crisp edge definition + a softer far-shadow for depth. The `{colors.shadow-near}` neutral near-black photographs consistently across brand contexts. Deep shadow uses unusual spread that creates an atmospheric modal effect.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Flat sections |
| `xs` | 2px | Inline elements, tiny chrome (26 uses) |
| `badge` | 3px | Badges (distinctive — not pill, not rounded) |
| `sm` | 4px | Buttons, inputs — workhorse (16 uses) |
| `md` | 8px | Cards, dropdowns (9 uses) |
| `lg` | 16px | Featured callouts |
| `xl` | 28px | Marketing hero cards |
| `pill` | 9999px | Reserved — Atlassian rarely uses pill |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Brand blue, white text, `{rounded.sm}` (4px), Atlassian Sans weight 500. Focus is 2px inset.
- **`button-subtle`** — Soft gray, label-text color, hover deepens to border gray.
- **`button-link`** — Transparent with brand blue text.
- **`button-danger`** — Danger red with white text.

### Cards
- **`card`** — White, hairline border, `{rounded.md}` (8px), 24px padding, dual-layer shadow.
- **`card-marketing`** — `{rounded.xl}` (28px) for hero/marketing moments.

### Inputs
**`input`** — White bg, hairline border, `{rounded.sm}`, 8px × 12px padding. Focus uses 2px brand-blue inset.

### Badges
Distinctive `{rounded.badge}` (3px) — not pill, not rounded. Variants: `badge-success` / `-warning` / `-danger` / `-in-progress` / `-done`.

### Toolbars / Nav
- **`nav-bar`** — White bg, hairline bottom border, 48-56px height
- **`button-icon`** — 32×32px with `{rounded.badge}` hover state

## Do's and Don'ts

### Do
- Use semantic tokens (`--ds-background-brand-subtlest-hovered`) — not hex
- Default to `{rounded.sm}` (4px) radius for buttons/inputs, `{rounded.md}` (8px) for cards
- Use Atlassian Sans weight 653 for display/H1 (variable-font weight axis)
- Reserve Charlie Display for marketing-hero moments only
- Use the rich accent palette (saffron, magenta, teal, purple) for status indicators
- Apply dual-layer shadows — crisp 1px + soft atmospheric

### Don't
- Don't use pill radius on buttons — stays `{rounded.sm}` in app UI
- Don't hardcode brand blue — use the `ds-` tokens
- Don't mix Atlassian Mono with other mono fonts — brand consistency matters
- Don't use tight letter-spacing — Atlassian is normal-tracked at all sizes
- Don't use generic weight 600 for display — the variable-axis 653 is specific

---

## Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<600px` | Left rail becomes bottom bar, nav panel slides up |
| Tablet | `600-1024px` | Left rail visible, nav panel toggles |
| Desktop | `1024-1280px` | Full app layout, rail + nav + content |
| Large | `>1280px` | Max content width applied |

### Touch Targets
- Buttons: `32-36px` minimum height
- Icon buttons in toolbars: `32px × 32px`
- Tappable rows: `44px` minimum

### Collapsing Strategy
- Display: 112px → 68px → 44px across breakpoints
- Left rail: persistent → collapsible → bottom nav
- Sidebars: multi-panel → single panel → overlay drawer
- Tables: horizontal scroll with sticky first column

---

## Agent Prompt Guide

### Quick Color Reference
- Brand Blue: `{colors.primary}`
- Brand Boldest: `{colors.brand-boldest}`
- Foreground: `{colors.ink}`
- Muted FG: `{colors.text-muted}`
- Border: `{colors.border}`
- Background: `{colors.background}`
- Success: `{colors.green}`
- Warning: `{colors.saffron}`
- Danger: `{colors.danger}`

### Example Component Prompts
- "Create a primary button: `{colors.primary}` bg, white text, `{rounded.sm}` radius, 8px 16px padding, 14px Atlassian Sans weight 500. Hover: `{colors.blue-bolder}` (darker). Focus: 2px inset `{colors.primary}` ring."
- "Design a card: white bg, 1px solid `{colors.border}`, `{rounded.md}` radius, 24px padding, dual-layer box-shadow with `{colors.shadow-soft}` and `{colors.shadow-near}` tints. Title at 20px Atlassian Sans weight 500 color `{colors.ink}`."
- "Build a status badge: `{rounded.badge}` (3px, not pill), 2px 8px padding, 12px Atlassian Sans weight 500. Success: subtle green. In progress: `{colors.brand-subtlest}` bg, `{colors.primary}` text."

### Iteration Guide
1. Tokens, not hex — always use the `ds-` semantic names
2. `{rounded.sm}` for interactive, `{rounded.md}` for cards, `{rounded.badge}` for badges — the enterprise rhythm
3. Weight 653 (variable axis) is the display signature — 500/700 for body
4. Dual-layer shadows with `1px` inner + soft outer
5. Brand blue (`{colors.primary}`) is primary; reserve sub-brand accents for status
6. Accessibility is structural — never skip focus rings, contrast is AAA by default
