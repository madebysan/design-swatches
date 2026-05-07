---
version: alpha
name: Webflow
description: Visually rich tool-forward platform — clean white canvas, Webflow Blue accent, rich secondary palette (purple/pink/green/orange/yellow/red), conservative 4–8px radii, multi-layer cascading shadows.

colors:
  # Primary
  background: "#ffffff"
  surface: "#ffffff"
  ink: "#080808"
  on-background: "#080808"
  on-surface: "#080808"

  # Brand
  primary: "#146ef5"
  primary-light: "#3b89ff"
  primary-dark: "#006acc"
  primary-hover: "#0055d4"
  on-primary: "#ffffff"

  # Secondary accents
  secondary-purple: "#7a3dff"
  secondary-pink: "#ed52cb"
  secondary-green: "#00d722"
  secondary-orange: "#ff6b00"
  secondary-yellow: "#ffae13"
  secondary-red: "#ee1d36"

  # Neutrals
  gray-800: "#222222"
  gray-700: "#363636"
  gray-300: "#ababab"
  mid-gray: "#5a5a5a"
  border: "#d8d8d8"
  border-hover: "#898989"

  # Shadow tints (opaque approximations of multi-layer cascade)
  shadow-soft: "#e6e6e6"   # was rgba(0,0,0,0.09) layer — flattened
  shadow-mid: "#d4d4d4"    # was rgba(0,0,0,0.08) layer — flattened
  shadow-low: "#f0f0f0"    # was rgba(0,0,0,0.04) layer — flattened

typography:
  display-hero:
    fontFamily: "WF Visual Sans Variable, Arial, sans-serif"
    fontSize: 80px
    fontWeight: 600
    lineHeight: 1.04
    letterSpacing: -0.8px
  section-heading:
    fontFamily: "WF Visual Sans Variable, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.04
    letterSpacing: 0px
  sub-heading:
    fontFamily: "WF Visual Sans Variable, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0px
  feature-title:
    fontFamily: "WF Visual Sans Variable, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0px
  body-large:
    fontFamily: "WF Visual Sans Variable, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px
  body:
    fontFamily: "WF Visual Sans Variable, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: -0.16px
  button-ui:
    fontFamily: "WF Visual Sans Variable, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: -0.16px
  uppercase-label:
    fontFamily: "WF Visual Sans Variable, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1.5px
  caption:
    fontFamily: "WF Visual Sans Variable, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  badge-uppercase:
    fontFamily: "WF Visual Sans Variable, Arial, sans-serif"
    fontSize: 12.8px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0px
  micro-uppercase:
    fontFamily: "WF Visual Sans Variable, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
  code:
    fontFamily: "Inconsolata, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px

spacing:
  micro: 1px
  fractional-1: 2.4px
  fractional-2: 3.2px
  xs: 4px
  fractional-3: 5.6px
  sm: 6px
  fractional-4: 7.2px
  md: 8px
  fractional-5: 9.6px
  lg: 12px
  xl: 16px
  2xl: 24px

rounded:
  micro: 2px
  sm: 4px
  md: 8px
  pill: 9999px

components:
  # Buttons
  button-transparent:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 12px 20px

  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 12px 20px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"

  button-circle:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: 16px

  badge-blue:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-uppercase}"
    rounded: "{rounded.sm}"
    padding: 4px 8px

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 24px

  card-featured:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 32px

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
    typography: "{typography.button-ui}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    padding: 8px 12px

  # Secondary swatches as badges
  badge-purple:
    backgroundColor: "{colors.secondary-purple}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-green:
    backgroundColor: "{colors.secondary-green}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
---

# Webflow Design System

## Overview

Webflow's website is a visually rich, tool-forward platform that communicates "design without code" through clean white surfaces, the signature Webflow Blue (`{colors.primary}`), and a rich secondary color palette (purple, pink, green, orange, yellow, red). The custom WF Visual Sans Variable font creates a confident, precise typographic system with weight 600 for display and 500 for body.

The system runs on a white canvas (`{colors.background}`) with near-black (`{colors.ink}`) text — high contrast, sharp, and unapologetically clean. Where most "design tool" sites lean into experimental chaos, Webflow leans into *engineered* clarity: precise weight progressions, conservative 4–8px radii, multi-layer cascading shadows for realistic elevation, and a translate(6px) hover animation that subtly suggests responsiveness without theatrics.

The secondary palette — purple, pink, green, orange, yellow, red — appears in illustrations, demo screens, and accent cards rather than primary chrome. This gives Webflow the vibrancy of a creative platform while keeping primary CTAs disciplined to Webflow Blue.

**Key Characteristics:**
- White canvas with near-black (`{colors.ink}`) text
- Webflow Blue (`{colors.primary}`) as primary brand + interactive color
- WF Visual Sans Variable — custom variable font with weight 500–600
- Rich secondary palette: purple, pink, green, orange, yellow, red
- Conservative 4px–8px border-radius — sharp, not rounded
- Multi-layer shadow stacks (5-layer cascading shadows)
- Uppercase labels: 10px–15px, weight 500–600, wide letter-spacing (0.6px–1.5px)
- translate(6px) hover animation on buttons

## Colors

### Primary
- **Near Black** (`{colors.ink}`): Primary text on white surfaces.
- **Webflow Blue** (`{colors.primary}`): Primary CTA and links.
- **Blue 400** (`{colors.primary-light}`): Lighter interactive blue.
- **Blue 300** (`{colors.primary-dark}`): Darker blue variant.
- **Button Hover Blue** (`{colors.primary-hover}`): Pressed/hover state.

### Secondary Accents
- **Purple** (`{colors.secondary-purple}`)
- **Pink** (`{colors.secondary-pink}`)
- **Green** (`{colors.secondary-green}`)
- **Orange** (`{colors.secondary-orange}`)
- **Yellow** (`{colors.secondary-yellow}`)
- **Red** (`{colors.secondary-red}`)

### Neutrals
- **Gray 800** (`{colors.gray-800}`): Dark secondary text
- **Gray 700** (`{colors.gray-700}`): Mid text
- **Gray 300** (`{colors.gray-300}`): Muted text, placeholder
- **Mid Gray** (`{colors.mid-gray}`): Link text
- **Border Gray** (`{colors.border}`): Borders, dividers
- **Border Hover** (`{colors.border-hover}`): Hover border

### Shadows
- **5-layer cascade** approximated by `{colors.shadow-soft}`, `{colors.shadow-mid}`, `{colors.shadow-low}` — fading offsets from soft to deep create realistic elevation.

## Typography

### Font Family
- **Display & Body**: WF Visual Sans Variable, fallback Arial, sans-serif
- **Code**: Inconsolata (monospace companion)

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-hero` | Hero headlines, 80px weight 600 |
| `section-heading` | Section heads, 56px weight 600 |
| `sub-heading` | Sub-section heads, 32px weight 500 |
| `feature-title` | Feature card titles, 24px |
| `body-large` | Lead body text, 20px |
| `body` | Standard body, 16px |
| `button-ui` | Button labels, 16px weight 500 |
| `uppercase-label` | Uppercase section labels, 15px with 1.5px tracking |
| `caption` | Captions, metadata |
| `badge-uppercase` | Uppercase badges, 12.8px weight 600 |
| `micro-uppercase` | Micro overlines, 10px |
| `code` | Inconsolata monospace |

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Webflow uses a fractional scale (1px, 2.4px, 3.2px, 4px, 5.6px, 6px, 7.2px, 8px, 9.6px, 12px, 16px, 24px) — unusually granular for fine UI tuning.

### Grid & Container
- Max content width: ~1280px, centered
- Multi-column feature grids (2–3 columns) with cascading shadow cards
- Full-bleed hero sections with white canvas

### Whitespace Philosophy
- Generous breathing room between sections
- Cards use cascading shadows to lift them off the white canvas
- Translate(6px) hover provides physical responsiveness

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Default text on canvas |
| Bordered (Level 1) | `1px solid {colors.border}` | Standard cards, inputs |
| Cascade Soft (Level 2) | layered soft shadows using `{colors.shadow-low}` and `{colors.shadow-mid}` | Hover states, secondary elevation |
| Cascade Deep (Level 3) | full 5-layer cascading shadow stack | Hero feature cards, modals |

**Shadow Philosophy**: Webflow uses a 5-layer cascading shadow stack to create realistic, atmospheric elevation. Each layer adds an offset and blur — the result is a soft, photographic shadow that feels lifted but not floating. This is the most distinctive depth treatment in the system.

## Shapes

| Token | Value | Use |
|---|---|---|
| `micro` | 2px | Tight inline elements |
| `sm` | 4px | Buttons, tags, small cards |
| `md` | 8px | Standard cards, featured containers |
| `pill` | 9999px | Circular icon buttons, pill badges |

Conservative 4–8px radii are core to Webflow's "engineered clarity" aesthetic. Round only what should be round.

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Webflow Blue with translate(6px) hover.
- **`button-transparent`** — text-only with translate(6px) hover.
- **`button-circle`** — circular icon button with white surface.

### Cards
- **`card`** — `1px solid {colors.border}`, 4px radius.
- **`card-featured`** — 8px radius with cascading shadow.

### Badges
- **`badge-blue`** — Webflow Blue accent badge.
- **`badge-purple`**, **`badge-green`** — secondary palette badges for category tags.

### Inputs
Standard rectangular inputs with sand-gray border, 4px radius. Focus shifts border to Webflow Blue.

## Do's and Don'ts

### Do
- Use WF Visual Sans Variable at 500–600 weight
- Webflow Blue (`{colors.primary}`) for primary CTAs and links
- 4–8px radius — conservative, sharp
- translate(6px) hover for primary buttons
- Cascading 5-layer shadows for realistic elevation
- Uppercase labels with 0.6px–1.5px letter-spacing
- Use the secondary palette (purple, pink, green, orange, yellow, red) for category accents and illustrations

### Don't
- Round beyond 8px for functional elements
- Use secondary colors on primary CTAs — primary is Webflow Blue
- Skip the translate(6px) hover animation
- Use generic single-layer shadows where the cascading stack belongs

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <479px | Single column, hamburger nav |
| Mobile Large | 479–768px | Slight horizontal breathing |
| Tablet | 768–992px | 2-column grids begin |
| Desktop | >992px | Full multi-column layout |

### Touch Targets
- Buttons: 12px 20px padding ensures comfortable touch
- Translate(6px) hover does not interfere with touch
- Minimum tap target: 44px

### Collapsing Strategy
- Hero text: 80px → 56px → 40px progressive scaling
- Feature grids: 3-col → 2-col → 1-col
- Section padding reduces proportionally
- Cards stack vertically on mobile

---

## Agent Prompt Guide

### Quick Color Reference
- Text: Near Black (`{colors.ink}`)
- CTA: Webflow Blue (`{colors.primary}`)
- Background: White (`{colors.background}`)
- Border: Border Gray (`{colors.border}`)
- Secondary: Purple (`{colors.secondary-purple}`), Pink (`{colors.secondary-pink}`), Green (`{colors.secondary-green}`)

### Example Component Prompts
- "Create a hero on white background with WF Visual Sans Variable 80px weight 600 in `{colors.ink}`, line-height 1.04, letter-spacing -0.8px. Webflow Blue (`{colors.primary}`) primary CTA, 4px radius, translate(6px) on hover."
- "Design a feature card on white surface with `1px solid {colors.border}` border, 8px radius, and a 5-layer cascading shadow stack. Title 24px weight 600, body 16px weight 400."
- "Build an uppercase section label at 15px weight 500 with 1.5px letter-spacing in `{colors.gray-700}`."

### Iteration Guide
1. Webflow Blue (`{colors.primary}`) is the primary brand color — keep CTAs disciplined to it
2. Secondary palette is for illustrations and category accents only
3. Use cascading 5-layer shadows for real elevation
4. translate(6px) on hover is non-negotiable for primary buttons
5. Conservative 4–8px radii throughout
