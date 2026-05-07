---
version: alpha
name: Airtable
description: Enterprise-friendly sophisticated-simplicity system — white canvas, deep navy text, Airtable Blue CTA accent, Haas typography with positive letter-spacing, blue-tinted multi-layer elevation.

colors:
  # Surface + canvas
  background: "#ffffff"
  surface: "#ffffff"
  surface-light: "#f8fafc"
  surface-spotlight: "#f9fcff"  # was rgba(249,252,255,0.97) — flattened

  # Ink + text
  ink: "#181d26"
  ink-inverted: "#ffffff"
  text-secondary: "#333333"
  text-weak: "#525a6b"  # was rgba(4,14,32,0.69) — flattened over white
  text-secondary-active: "#252b35"  # was rgba(7,12,20,0.82) — flattened

  on-background: "#181d26"
  on-surface: "#181d26"
  on-primary: "#ffffff"

  # Brand accent
  primary: "#1b61c9"
  primary-mid: "#254fad"

  # Semantic
  success: "#006400"

  # Borders
  border: "#e0e2e6"

  # Shadow tints (opaque approximations)
  shadow-tint: "#dce5f3"  # was rgba(45,127,249,0.28) — flattened
  shadow-soft: "#f4f6f9"  # was rgba(15,48,106,0.05) — flattened

typography:
  display-hero:
    fontFamily: "Haas, -apple-system, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0px
  display-bold:
    fontFamily: "Haas Groot Disp, Haas, -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.5
    letterSpacing: 0px
  heading-section:
    fontFamily: "Haas, -apple-system, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0px
  heading-sub:
    fontFamily: "Haas, -apple-system, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0px
  card-title:
    fontFamily: "Haas, -apple-system, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.12px
  feature:
    fontFamily: "Haas, -apple-system, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  body-large:
    fontFamily: "Haas, -apple-system, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.18px
  body:
    fontFamily: "Haas, -apple-system, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.12px
  button-ui:
    fontFamily: "Haas, -apple-system, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08px
  caption:
    fontFamily: "Haas, -apple-system, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.18px

spacing:
  micro: 1px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px

rounded:
  none: 0px
  xs: 2px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  pill: 9999px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    padding: 16px 24px

  # Primary CTA — Airtable Blue
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.md}"
    padding: 16px 24px
  button-primary-hover:
    backgroundColor: "{colors.primary-mid}"
    textColor: "{colors.on-primary}"

  # White outline button
  button-white:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.md}"
    padding: 16px 24px

  # Cookie / sharp utility button
  button-sharp:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.xs}"
    padding: 12px 16px

  # Card
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px

  card-section:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 32px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px

  # Soft elevated panel
  panel-elevated:
    backgroundColor: "{colors.surface-spotlight}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Success indicator
  badge-success:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: 4px 8px
---

# Airtable Design System

## Overview

Airtable's website is a clean, enterprise-friendly platform that communicates "sophisticated simplicity" through a white canvas (`{colors.background}`) with deep navy text (`{colors.ink}`) and Airtable Blue (`{colors.primary}`) as the primary interactive accent. The Haas font family (display + text variants) creates a Swiss-precision typography system with positive letter-spacing throughout — every text size carries `0.08px`–`0.28px` tracking, an unusual choice that gives the prose a slight aerated quality and reads as "grown-up enterprise" rather than consumer-friendly.

The interactive language is **Airtable Blue** (`{colors.primary}`) — used for CTAs, links, and inline emphasis — paired with a signature blue-tinted multi-layer drop shadow that gives white surfaces a subtle elevated lift without the harshness of pure-black shadows. The 12px corner radius on buttons and 16–32px on cards establishes a soft-but-precise corner vocabulary that matches the Swiss-precision typographic feel.

**Key Characteristics:**
- White canvas with deep navy text (`{colors.ink}`)
- Airtable Blue (`{colors.primary}`) as primary CTA and link color
- Haas + Haas Groot Disp dual font system
- Positive letter-spacing on body text (`0.08px`–`0.28px`)
- 12px radius buttons, 16px–32px for cards
- Multi-layer blue-tinted shadow with `{colors.shadow-tint}` warmth
- Semantic theme tokens: `--theme_*` CSS variable naming

## Colors

### Primary
- **Deep Navy** (`{colors.ink}`): Primary text — used for ~95% of headings and body
- **Airtable Blue** (`{colors.primary}`): CTA buttons, links, inline emphasis
- **White** (`{colors.surface}`): Primary surface
- **Spotlight** (`{colors.surface-spotlight}`): Elevated panel surfaces

### Semantic
- **Success Green** (`{colors.success}`): Success state text
- **Weak Text** (`{colors.text-weak}`): De-emphasized body text
- **Secondary Active** (`{colors.text-secondary-active}`): Active/pressed secondary button text

### Neutral
- **Dark Gray** (`{colors.text-secondary}`): Secondary text
- **Mid Blue** (`{colors.primary-mid}`): Link/accent blue variant
- **Border** (`{colors.border}`): Card borders
- **Light Surface** (`{colors.surface-light}`): Subtle surface for sectioned backgrounds

### Shadows
- **Blue-tinted Drop** (`{colors.shadow-tint}`): Multi-layer drop shadow with subtle blue warmth — the system's signature elevation
- **Soft Ambient** (`{colors.shadow-soft}`): Wide soft glow used on featured cards

## Typography

### Font Families
- **Primary**: `Haas`, fallbacks: `-apple-system, system-ui, Segoe UI, Roboto`
- **Display**: `Haas Groot Disp`, fallback: `Haas`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Use those tokens directly via reference rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | Hero headings — 48px regular weight |
| `display-bold` | Heaviest display moments — 48px weight 900 in Groot Disp |
| `heading-section` | Section heads (40px) |
| `heading-sub` | Sub-section heads (32px) |
| `card-title` | Card titles, mid-tier headings |
| `feature` | Feature copy, emphasized statements |
| `body-large` | Standard body copy at 18px |
| `body` | Mid-weight 16px body |
| `button-ui` | Button labels, UI chrome |
| `caption` | Metadata, fine print |

### Principles
- **Positive tracking everywhere**: Body text carries `0.08px`–`0.28px` letter-spacing — atypical for sans-serif systems and gives prose an aerated, premium quality.
- **Dual-family precision**: Haas for nearly all text; Haas Groot Disp reserved for heavy display-weight (900) hero moments.
- **Weight 400–500 for content, 900 for display drama**: Mid-weights for everything readable; weight 900 reserved for display.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px with `xs` (4px) used for tight UI chrome.

The scale runs `micro` (1px) for hairlines, `xs`–`md` for chrome, and `xl`–`3xl` for section breathing.

### Grid & Container
- 12-column grid
- Generous gutters for enterprise content density
- Section padding: `2xl`–`3xl` between major sections

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, body text |
| Hairline (Level 1) | 1px solid `{colors.border}` | Card and divider edges |
| Blue-tint Lift (Level 2) | Multi-layer drop with `{colors.shadow-tint}` warmth | Card lift, dropdown menus, modals — the signature shadow |
| Soft Ambient (Level 3) | Wide ~20px blur using `{colors.shadow-soft}` | Featured cards, hero panels |

**Shadow Philosophy**: Airtable layers four shadows of varying opacity into a single perceived "lift" — a hairline, two soft blurs, and a slight blue-tint that warms the white surface above. The blue tint is the brand-aware detail that distinguishes this from generic Material/iOS shadow defaults.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Edge cases |
| `xs` | 2px | Cookie consent, sharp utility chrome |
| `md` | 12px | Buttons, inputs — workhorse radius |
| `lg` | 16px | Cards |
| `xl` | 24px | Section containers, hero blocks |
| `2xl` | 32px | Large containers, feature panels |
| `pill` | 9999px | Avatar, circular indicators |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Airtable Blue background, white text, `{rounded.md}` (12px) radius, 16px × 24px padding
- **`button-white`** — White surface, deep navy text, 12px radius, hairline border
- **`button-sharp`** — `{colors.primary}` with `{rounded.xs}` (2px) radius — used for cookie consent and tight utility chrome

### Cards
- **`card`** — White, hairline gray border, 16px radius, 24px padding
- **`card-section`** — Light surface tint, 24px radius, 32px padding
- **`panel-elevated`** — Spotlight surface, multi-layer blue shadow

### Inputs
**`input`** — Standard Haas styling, white surface, 12px radius. Focus state shifts border to `{colors.primary}`.

### Badges
**`badge-success`** — Light surface with success green text.

## Do's and Don'ts

### Do
- Use Airtable Blue (`{colors.primary}`) for primary CTAs and links — never decorative
- Apply Haas with positive letter-spacing (0.08–0.28px) throughout
- Use 12px radius for buttons, 16–32px for cards — gentle but precise
- Pair white surfaces with the blue-tinted multi-layer shadow for elevation
- Use `--theme_*` CSS variable naming for thematic tokens

### Don't
- Don't skip positive letter-spacing — it's the system's hidden polish
- Don't use heavy black shadows — the blue-tinted multi-layer lift is the signature
- Don't override Haas with a different display face — the dual-family system is enterprise-precise
- Don't use sharp radius (2px) on standard buttons — reserve it for cookie/utility chrome only

---

## Responsive Behavior

Breakpoints: 425–1664px across approximately 23 breakpoints. The system reflows densely across enterprise viewports, maintaining 12-column grid and gutter consistency.

| Name | Width | Notes |
|------|-------|-------|
| Mobile | <425px | Single-column, condensed nav |
| Tablet | 425–800px | 2-column grid, sticky CTA |
| Laptop | 800–1280px | 3–4 column grid |
| Desktop | 1280–1664px | Full multi-column |
| Wide Desktop | ≥1664px | Maximum container width |

### Touch Targets
Standard 44×44px on all interactive elements. Buttons maintain ~48px height across breakpoints.

### Collapsing Strategy
- **Nav**: Horizontal links collapse to hamburger drawer below tablet
- **Hero type**: 48px → 36px → 28px progressive scaling
- **Card grids**: 4-col → 2-col → 1-col across breakpoints
- **Section spacing**: `3xl` desktop → `xl` mobile

---

## Agent Prompt Guide

### Quick Color Reference
- Text: Deep Navy (`{colors.ink}`)
- CTA: Airtable Blue (`{colors.primary}`)
- Background: White (`{colors.background}`)
- Border: Hairline Gray (`{colors.border}`)
- Subsurface: Light (`{colors.surface-light}`)
- Success: Green (`{colors.success}`)

### Example Component Prompts
- "Create a primary CTA button: Airtable Blue (`{colors.primary}`) background, white Haas 16px weight 500 label with `0.08px` letter-spacing, 16px × 24px padding, 12px border-radius, no shadow."
- "Design a feature card: white background, 1px solid `{colors.border}` border, 16px border-radius, 24px padding, multi-layer blue-tinted drop shadow with `{colors.shadow-tint}` warmth. Title in Haas 24px weight 400 with `0.12px` letter-spacing."
- "Build a hero section on white canvas: headline in Haas 48px weight 400 with `0.0px` letter-spacing in Deep Navy (`{colors.ink}`); subtitle in Haas 18px weight 400 with `0.18px` letter-spacing. Place a `button-primary` CTA below."

### Iteration Guide
1. Always include positive letter-spacing on body text — it's the brand's signature aerated quality
2. Apply Airtable Blue (`{colors.primary}`) only to CTAs and links — never decorative
3. Use 12px radius for buttons, 16–32px for cards
4. Layer the blue-tinted shadow on white surfaces — never use plain black drop shadows
5. Use Haas for everything; Haas Groot Disp only for weight 900 display drama
