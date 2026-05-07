---
version: alpha
name: Figma
description: Design tool that designed itself — variable font figmaSans with unusual weight stops, strict black-and-white interface chrome, vibrant gradient hero, pill-and-circle button geometry, dashed focus outlines.

colors:
  # Primary binary
  ink: "#000000"
  background: "#ffffff"
  primary: "#000000"
  on-primary: "#ffffff"

  # Surfaces
  surface: "#ffffff"

  # Glass / overlay (opaque approximations)
  glass-dark: "#ebebeb"     # opaque approx of rgba(0,0,0,0.08) over white — Google format requires hex
  glass-light: "#3a3a3a"    # opaque approx of rgba(255,255,255,0.16) over black

  # Hero gradient stops (vibrant multi-stop)
  gradient-green: "#54f068"
  gradient-yellow: "#fbe24c"
  gradient-purple: "#5a32f2"
  gradient-pink: "#ff5fbb"

typography:
  display-hero:
    fontFamily: "figmaSans, figmaSans Fallback, SF Pro Display, system-ui, helvetica"
    fontSize: 86px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -1.72px
  section-heading:
    fontFamily: "figmaSans, figmaSans Fallback, SF Pro Display, system-ui, helvetica"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.10
    letterSpacing: -0.96px
  sub-heading:
    fontFamily: "figmaSans, figmaSans Fallback, SF Pro Display, system-ui, helvetica"
    fontSize: 26px
    fontWeight: 540
    lineHeight: 1.35
    letterSpacing: -0.26px
  sub-heading-light:
    fontFamily: "figmaSans, figmaSans Fallback, SF Pro Display, system-ui, helvetica"
    fontSize: 26px
    fontWeight: 340
    lineHeight: 1.35
    letterSpacing: -0.26px
  feature-title:
    fontFamily: "figmaSans, figmaSans Fallback, SF Pro Display, system-ui, helvetica"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.45
    letterSpacing: 0px
  body-large:
    fontFamily: "figmaSans, figmaSans Fallback, SF Pro Display, system-ui, helvetica"
    fontSize: 20px
    fontWeight: 450
    lineHeight: 1.40
    letterSpacing: -0.14px
  body:
    fontFamily: "figmaSans, figmaSans Fallback, SF Pro Display, system-ui, helvetica"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: -0.14px
  body-light:
    fontFamily: "figmaSans, figmaSans Fallback, SF Pro Display, system-ui, helvetica"
    fontSize: 18px
    fontWeight: 320
    lineHeight: 1.45
    letterSpacing: -0.26px
  mono-label:
    fontFamily: "figmaMono, figmaMono Fallback, SF Mono, menlo, monospace"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 0.54px
  mono-small:
    fontFamily: "figmaMono, figmaMono Fallback, SF Mono, menlo, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: 0.6px

spacing:
  micro: 1px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 40px
  4xl: 48px

rounded:
  none: 0px
  xs: 2px
  sm: 6px
  md: 8px
  pill: 50px
  full: 9999px

components:
  button-black-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 18px

  button-white-pill:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 18px

  button-glass-dark:
    backgroundColor: "{colors.glass-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.full}"
    padding: 8px 8px

  button-glass-light:
    backgroundColor: "{colors.glass-light}"
    textColor: "{colors.background}"
    typography: "{typography.body}"
    rounded: "{rounded.full}"
    padding: 8px 8px

  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 24px

  card-small:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: 16px

  product-tab:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-large}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  product-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-large}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 16px 24px

  hero-gradient-section:
    backgroundColor: "{colors.gradient-purple}"
    textColor: "{colors.background}"
    typography: "{typography.display-hero}"
    padding: 48px

  mono-section-label:
    textColor: "{colors.ink}"
    typography: "{typography.mono-label}"
    padding: 0px
---

# Figma Design System

## Overview

Figma's interface is the design tool that designed itself — a masterclass in typographic sophistication where a custom variable font (figmaSans) modulates between razor-thin (weight 320) and bold (weight 700) with stops at unusual intermediates (330, 340, 450, 480, 540) that most type systems never explore. This granular weight control gives every text element a precisely calibrated visual weight, creating hierarchy through micro-differences rather than the blunt instrument of "regular vs bold."

The page presents a fascinating duality: the interface chrome is strictly black-and-white (literally only `{colors.ink}` and `{colors.background}` detected as colors), while the hero section and product showcases explode with vibrant multi-color gradients — electric greens (`{colors.gradient-green}`), bright yellows (`{colors.gradient-yellow}`), deep purples (`{colors.gradient-purple}`), hot pinks (`{colors.gradient-pink}`). This separation means the design system itself is colorless, treating the product's colorful output as the hero content. Figma's marketing page is essentially a white gallery wall displaying colorful art.

What makes Figma distinctive beyond the variable font is its circle-and-pill geometry. Buttons use `{rounded.pill}` (50px) or full-circle (`{rounded.full}`) for icon buttons, creating an organic, tool-palette-like feel. The dashed-outline focus indicator (`dashed 2px`) is a deliberate design choice that echoes selection handles in the Figma editor itself — the website's UI language references the product's UI language.

**Key Characteristics:**
- Custom variable font (figmaSans) with unusual weight stops: 320, 330, 340, 450, 480, 540, 700
- Strictly black-and-white interface chrome — color exists only in product content
- figmaMono for uppercase technical labels with wide letter-spacing
- Pill (`{rounded.pill}`) and circular (`{rounded.full}`) button geometry
- Dashed focus outlines echoing Figma's editor selection handles
- Vibrant multi-color hero gradients (green, yellow, purple, pink)
- OpenType `"kern"` feature enabled globally
- Negative letter-spacing throughout — even body text at -0.14px to -0.26px

## Colors

### Primary
- **Pure Black** (`{colors.ink}`): All text, all solid buttons, all borders. The sole "color" of the interface.
- **Pure White** (`{colors.background}`): All backgrounds, white buttons, text on dark surfaces.

*Note: Figma's marketing site uses ONLY these two colors for its interface layer. All vibrant colors appear exclusively in product screenshots, hero gradients, and embedded content.*

### Surface & Background
- **Pure White** (`{colors.surface}`): Primary page background and card surfaces.
- **Glass Dark** (`{colors.glass-dark}`): Subtle dark overlay for secondary circular buttons and glass effects.
- **Glass Light** (`{colors.glass-light}`): Frosted glass overlay for buttons on dark/colored surfaces.

### Gradient System
- **Hero Gradient**: A vibrant multi-stop gradient using electric green (`{colors.gradient-green}`), bright yellow (`{colors.gradient-yellow}`), deep purple (`{colors.gradient-purple}`), and hot pink (`{colors.gradient-pink}`). This gradient is the visual signature of the hero section — it represents the creative possibilities of the tool.
- **Product Section Gradients**: Individual product areas (Design, Dev Mode, Prototyping) may use distinct color themes in their showcases.

## Typography

### Font Family
- **Primary**: `figmaSans`, with fallbacks: `figmaSans Fallback, SF Pro Display, system-ui, helvetica`
- **Monospace / Labels**: `figmaMono`, with fallbacks: `figmaMono Fallback, SF Mono, menlo`

### Hierarchy

| Token | Use |
|---|---|
| `display-hero` | 86px figmaSans 400 with -1.72px tracking — maximum impact |
| `section-heading` | 64px weight 400, -0.96px tracking |
| `sub-heading` | 26px weight 540 — emphasized section text |
| `sub-heading-light` | 26px weight 340 — light-weight section text |
| `feature-title` | 24px weight 700 — bold card headings |
| `body-large` | 20px weight 450 — descriptions, intros |
| `body` | 16px weight 400 — standard body, nav, buttons |
| `body-light` | 18px weight 320 — light-weight body text |
| `mono-label` | 18px figmaMono uppercase with 0.54px tracking |
| `mono-small` | 12px figmaMono uppercase with 0.6px tracking |

### Principles
- **Variable font precision**: figmaSans uses weights that most systems never touch — 320, 330, 340, 450, 480, 540. This creates hierarchy through subtle weight differences rather than dramatic jumps.
- **Light as the base**: Most body text uses 320–340 (lighter than typical 400 "regular"), creating an ethereal, airy reading experience.
- **Kern everywhere**: Every text element enables OpenType `"kern"` feature — kerning is not optional, it's structural.
- **Negative tracking by default**: Even body text uses -0.1px to -0.26px letter-spacing. Display text compresses further to -0.96px and -1.72px.
- **Mono for structure**: figmaMono in uppercase with positive letter-spacing (0.54px–0.6px) creates technical signpost labels.

## Layout

### Spacing System
Base unit is **8px**. Scale lives in YAML — `micro` (1px) through `4xl` (48px).

### Grid & Container
- Max container width: up to 1920px
- Hero: full-width gradient with centered content
- Product sections: alternating showcases
- Footer: dark full-width section
- Responsive from 559px to 1920px

### Whitespace Philosophy
- **Gallery-like pacing**: Generous spacing lets each product section breathe as its own exhibit.
- **Color sections as visual breathing**: The gradient hero and product showcases provide chromatic relief between the monochrome interface sections.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Page background, most text |
| Surface (Level 1) | White card on gradient/dark section | Cards, product showcases |
| Elevated (Level 2) | Subtle shadow | Floating cards, hover states |

**Shadow Philosophy**: Figma uses shadows sparingly. The primary depth mechanisms are **background contrast** (white content on colorful/dark sections) and the inherent dimensionality of the product screenshots themselves.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `xs` | 2px | Small link elements |
| `sm` | 6px | Small containers, dividers |
| `md` | 8px | Cards, images, dialogs |
| `pill` | 50px | Tab buttons, CTAs |
| `full` | 9999px | Icon buttons, circular elements |

## Components

The complete component spec lives in YAML.

### Buttons
- **`button-black-pill`** — Pill-shaped solid black, white text, maximum emphasis.
- **`button-white-pill`** — Pill-shaped white, black text — standard CTA on dark/colored surfaces.
- **`button-glass-dark`** — Subtle dark overlay for circular icon buttons on light surfaces.
- **`button-glass-light`** — Frosted glass overlay for circular icon buttons on dark/colored surfaces.

### Cards
- **`card`** — Standard 24px-padded card, `{rounded.md}` radius.
- **`card-small`** — Tighter card with `{rounded.sm}` radius.

### Product Tabs
- **`product-tab`** / **`product-tab-active`** — Pill-shaped horizontal tabs (50px radius). Active tab uses inverted black-on-white treatment.

### Navigation
- **`nav-bar`** — Clean horizontal nav on white. Logo, pill tabs, black pill CTA right-aligned.

### Hero
- **`hero-gradient-section`** — Full-width vibrant multi-color gradient background with white display headline overlay.

### Mono Labels
- **`mono-section-label`** — figmaMono 18px uppercase technical label.

**Dashed Focus Indicators**: All interactive elements use `dashed 2px` outline on focus — references the selection handles in the Figma editor. A meta-design choice connecting website and product.

## Do's and Don'ts

### Do
- Use figmaSans with precise variable weights (320–540) — the granular weight control IS the design
- Keep the interface strictly black-and-white — color comes from product content only
- Use pill (`{rounded.pill}`) and circular (`{rounded.full}`) geometry for all interactive elements
- Apply dashed 2px focus outlines — the signature accessibility pattern
- Enable `"kern"` feature on all text
- Use figmaMono in uppercase with positive letter-spacing for labels
- Apply negative letter-spacing throughout (-0.1px to -1.72px)

### Don't
- Don't add interface colors — the monochrome palette is absolute
- Don't use standard font weights (400, 500, 600, 700) — use the variable font's unique stops (320, 330, 340, 450, 480, 540)
- Don't use sharp corners on buttons — pill and circular geometry only
- Don't use solid focus outlines — dashed is the signature
- Don't increase body font weight above 450 — the light-weight aesthetic is core
- Don't use positive letter-spacing on body text — it's always negative

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Small Mobile | <560px | Compact layout, stacked |
| Tablet | 560–768px | Minor adjustments |
| Small Desktop | 768–960px | 2-column layouts |
| Desktop | 960–1280px | Standard layout |
| Large Desktop | 1280–1440px | Expanded |
| Ultra-wide | 1440–1920px | Maximum width |

### Collapsing Strategy
- Hero text: 86px → 64px → 48px
- Product tabs: horizontal scroll on mobile
- Feature sections: stacked single column
- Footer: multi-column → stacked

---

## Agent Prompt Guide

### Quick Color Reference
- Everything: "Pure Black (`{colors.ink}`)" and "Pure White (`{colors.background}`)"
- Glass Dark: "`{colors.glass-dark}`"
- Glass Light: "`{colors.glass-light}`"

### Example Component Prompts
- "Create a hero on a vibrant multi-color gradient (green `{colors.gradient-green}`, yellow `{colors.gradient-yellow}`, purple `{colors.gradient-purple}`, pink `{colors.gradient-pink}`). Headline at 86px figmaSans weight 400, line-height 1.0, letter-spacing -1.72px. White text. White pill CTA button (`{rounded.pill}` radius, 8px 18px padding)."
- "Design a product tab bar with pill-shaped buttons (`{rounded.pill}` radius). Active: Black bg, white text. Inactive: transparent, black text. figmaSans at 20px weight 480."
- "Build a section label: figmaMono 18px, uppercase, letter-spacing 0.54px, black text. Kern enabled."
- "Create body text at 20px figmaSans weight 330, line-height 1.40, letter-spacing -0.14px. Pure Black on white."

### Iteration Guide
1. Use variable font weight stops precisely: 320, 330, 340, 450, 480, 540, 700
2. Interface is always black + white — never add colors to chrome
3. Dashed focus outlines, not solid
4. Letter-spacing is always negative on body, always positive on mono labels
5. Pill (`{rounded.pill}`) for buttons/tabs, circle (`{rounded.full}`) for icon buttons
