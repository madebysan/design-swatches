---
version: alpha
name: "Arcade"
description: "Crisp Blueprint on White Canvas. Clean surfaces frame sharp typography and a singular, vibrant blue, like a detailed architectural plan on a clear white sheet, accented by a distinct highlight."

colors:
  background: "#ffffff"
  surface: "#2142e7"
  surface-elevated: "#f5f5f5"
  ink: "#111111"
  ink-muted: "#4b5563"
  primary: "#111827"
  on-primary: "#ffffff"
  border: "#f9fafb"
  focus-ring: "#111827"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 33px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  4xl: 96px

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 16px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.background}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    borderColor: "{colors.focus-ring}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  badge:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
---

# Arcade Design System

## Overview

Arcade's homepage reads like a precision instrument — pure white canvas (`#ffffff`), graphite-near-black type (`#111827`), and a single saturated Arcade Blue (`#2142e7`) that does all the action work. The visual identity prioritizes clarity and directness without going sterile. Subtle, layered shadows and one decorative dark gradient for the hero give the system tactile dimensionality, so even with a tightly disciplined palette the page feels grounded rather than flat.

The typographic system is single-face: **Inter** carries every role from 64px display down to 12px caption, with **Balig Script** held in reserve for occasional decorative brand moments. Display sizes use aggressive negative letter-spacing (`-1.6px` at 64px, `-0.96px` at 48px, `-0.36px` at 36px) — the standard tightening-at-scale convention applied with discipline. Below the heading line, tracking returns to normal and Inter's natural rhythm carries.

The signature move is the elevation system. Arcade publishes one of the most layered shadow stacks in this corpus — six inset/outer layers per element on cards, with both shadow color and inset highlight rgba values calibrated to give buttons a tactile, lift-from-the-page feel. This is the architectural-blueprint reference made literal: every interactive surface has weight, every CTA looks press-able. Combine that with the polarized radius system (`12px` buttons, `16px` inputs and cards, `72px` for large action chrome) and Arcade reads as composed, technical, and craft-conscious.

**Key Characteristics:**
- White (`#ffffff`) canvas with Whisper Gray (`#f9fafb`) for subtle differentiation
- Arcade Blue (`#2142e7`) reserved exclusively for primary CTAs and active states
- Graphite Text (`#111827`) — near-black with cool blue undertone, never pure black
- Single-face Inter typography from 64px display to 12px caption
- Aggressive negative tracking on headings: `-1.6px` at 64px down to `-0.36px` at 36px
- Polarized radius vocabulary: `12px` buttons, `16px` cards/inputs, `72px` large action shells
- Multi-layer shadow stacks (6+ rgba layers) for tactile button and card elevation
- Inset highlight technique on elevated panels (`rgba(255, 255, 255, 0.06) inset`)
- Dark gradient hero (`#111827` → `#2142e7`) as the brand's only large color moment
- Generous `96px` section gap and `48px` card padding
- 1304px max-width — slightly wider than the typical 1280

## Colors

### Background Surfaces
- **Canvas White** (`#ffffff`): Primary page background.
- **Whisper Gray** (`#f9fafb`): Subtle background for UI elements and section differentiation.
- **Dark Gradient Base** (`#111827`): Base color for the hero gradient.

### Text & Content
- **Graphite Text** (`#111827`): Primary text — headings and body. Near-black with cool blue undertone.
- **Slate Text** (`#4b5563`): Secondary body text.
- **Silver Text** (`#374151`): Decorative text for navigation and links.
- **Steel Accent** (`#70747d`): Subtle secondary text and ghost button labels.

### Brand & Accent
- **Arcade Blue** (`#2142e7`): Primary brand color — CTAs, active states, gradient accent.
- **Deep Blue Shadow** (`#182fa5`): Darker shade used for primary button border-shadow technique.

### Border & Divider
- **Outline Ash** (`#e5e7eb`): Primary border color for buttons, inputs, and subtle dividers.

## Typography

### Font Families
- **Inter** (substitute: system-ui, sans-serif): The primary typeface for all text content from headings to body. Strong legibility supports an efficient, clear communication style. Heavier weights (600, 700) reserved for key titles; lighter weights (400, 500) serve body and secondary information.
- **Balig Script** (substitute: cursive): A decorative script font used sparingly for unique brand-specific elements or signatures. Contrasts with Inter's utilitarianism for occasional personality moments.

### Hierarchy

| Role | Font | Size | Line Height | Letter Spacing |
|------|------|------|-------------|----------------|
| Display | Inter | 64px | 1.07 | -1.6px |
| Heading Large | Inter | 48px | 1.17 | -0.96px |
| Heading | Inter | 36px | 1.25 | -0.36px |
| Heading Small | Inter | 24px | 1.33 | -0.48px |
| Subheading | Inter | 18px | 1.56 | normal |
| Body | Inter | 16px | 1.50 | normal |
| Body Small | Inter | 14px | 1.43 | normal |
| Caption | Inter | 12px | 1.50 | normal |

### Principles
- **Single-face system**: Inter handles every typographic role. Hierarchy comes from size, weight, and tracking — never face changes (Balig Script is reserved for special-case brand decoration).
- **Negative tracking proportional to size**: -1.6px at 64px, -0.96px at 48px, -0.48px at 24px. Below 24px, spacing returns to normal.
- **Three-weight system for Inter**: 400 (body, captions), 500 (UI labels, navigation, status chips), 600/700 (headings, key titles). No light weights at display sizes.
- **Balig Script as accent only**: The cursive face appears for signature-like brand moments. It never carries information that needs to be readable at a glance.

## Layout

### Spacing System
- **elementGap**: `8px` — small inline spacing
- **sectionGap**: `96px` — generous vertical breathing between sections
- **cardPadding**: `48px` — distinctly spacious card interiors

### Border Radius Scale
- **buttons / nav items**: `12px`
- **cards / inputs**: `16px`
- **status chips**: `8px`
- **decorative elements**: `24px`
- **large action shells**: `72px`

### Grid
- Max content width: `1304px` — slightly wider than the typical 1280
- Hero: full-width gradient with centered content stack and integrated input
- Content sections: alternating text-stack-with-visual-below or two-column splits
- 96px section gap maintains scannable rhythm without dividers

### Layout & Composition
The site uses a centered max-width layout (`1304px`) for most content, conveying order and focus. The hero breaks this slightly with a full-width gradient background, contrasted with a centered text block and the action input field. Sections maintain consistent `96px` vertical spacing with alternating arrangements: text-with-visual-below or two-column text+visual splits. The sticky nav carries branding, links, and prominent CTAs. The composition balances generous whitespace with information density, supported by the elevated card system for visual organization.

## Elevation & Depth

| Level | Hex / Treatment | Name | Purpose |
|-------|-----------------|------|---------|
| 0 | `#ffffff` | Canvas White | Page background |
| 1 | `#f9fafb` | Whisper Gray | Subtle background, card backgrounds |
| 2 | Subtle UI shadow stack | Subtle UI Element | Inline elements with light depth |
| 3 | Button shadow (normal) | Button (Normal) | Standard interactive buttons |
| 4 | Button shadow (hover) | Button (Hover/Focus) | Interactive lift on hover |
| 5 | Primary button + Deep Blue Shadow border | Primary Button | CTA emphasis with brand-color border-shadow |
| 6 | Card multi-layer + inset highlight | Elevated Panel | Featured cards with tactile depth |

**Shadow Philosophy**: Arcade is one of the more elevation-heavy systems in light-mode SaaS. Where most light-mode designs use single shadows, Arcade stacks 5–6 rgba layers per element, mixing outer shadows at multiple offsets (32px / 16px / 8px / 4px / 2px) with inset white highlights (`rgba(255, 255, 255, 0.06) inset`) to suggest a slight bevel. The signature primary button uses Deep Blue Shadow (`#182fa5`) as its 1px border-shadow — a brand-tinted ring that makes the CTA feel pressed-in rather than floating. The cumulative effect is tactile and architectural: every elevated element looks like a real material with weight and a defined edge.

## Shapes

The complete radius scale is declared in the `rounded:` token block above.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Hard-edged brand moments and flush layouts |
| `sm` | 4px | Small controls and tight UI details |
| `md` | 8px | Inputs and compact interface elements |
| `lg` | 16px | Cards and larger containers |
| `pill` | 9999px | CTAs, chips, and rounded badges |

## Components

### Buttons

**Primary Action**
- Background: Arcade Blue (`#2142e7`)
- Text: White (`#ffffff`)
- Radius: `12px`
- Padding: `10px 16px`
- Font: Inter, 16px, weight 500
- Shadow: multi-layer with Deep Blue Shadow (`#182fa5`) border-shadow:
  `rgba(17, 24, 39, 0.04) 0px 32px 32px 0px, rgba(17, 24, 39, 0.04) 0px 16px 16px 0px, rgba(17, 24, 39, 0.04) 0px 8px 8px 0px, rgba(17, 24, 39, 0.04) 0px 4px 4px -2px, rgba(17, 24, 39, 0.04) 0px 2px 2px -1px, rgb(24, 47, 165) 0px 0px 0px 1px`

**Secondary (Outlined)**
- Background: Canvas White (`#ffffff`)
- Text: Graphite Text (`#111827`)
- Border: `1px solid #e5e7eb` (Outline Ash)
- Radius: `12px`
- Padding: `10px 16px`
- Shadow (normal): `rgba(17, 24, 39, 0.04) 0px 32px 32px 0px, rgba(17, 24, 39, 0.04) 0px 16px 16px 0px, rgba(17, 24, 39, 0.04) 0px 8px 8px 0px, rgba(17, 24, 39, 0.04) 0px 4px 4px -2px, rgba(17, 24, 39, 0.04) 0px 2px 2px -1px, rgba(17, 24, 39, 0.16) 0px 0px 0px 1px`
- Shadow (hover): same stack but at `0.05` alpha and `0.1` border-shadow

**Ghost Button**
- Background: transparent
- Text: Steel Accent (`#70747d`)
- No visible border
- Radius: `12px`
- Padding: `10px 16px`
- Font: Inter, 16px, weight 500
- Use: Navigation, tertiary actions

### Inputs

**Action Input Field**
- Background: Canvas White (`#ffffff`)
- Border: `1px solid #e5e7eb` (Outline Ash)
- Text: Graphite Text (`#111827`)
- Radius: `16px`
- Padding: `16px` left, `114px` right (room for integrated submit button)
- Use: Hero input with embedded action button

**Text Input Field**
- Background: transparent
- Text: Graphite Text (`#111827`)
- Radius: `0px`
- Minimal padding
- Use: Simpler, integrated-text input

### Cards

**Elevated Panel**
- Background: Canvas White (`#ffffff`) or Whisper Gray (`#f9fafb`)
- Radius: `16px`
- Padding: `48px`
- Shadow: multi-layer with inset highlight
  `rgba(17, 24, 39, 0.2) 0px 8px 8px 0px, rgba(17, 24, 39, 0.1) 0px 4px 4px 0px, rgba(17, 24, 39, 0.1) 0px 2px 2px 0px, rgba(17, 24, 39, 0.1) 0px 0px 0px 1px, rgba(255, 255, 255, 0.06) 0px 0px 0px 1px inset, rgba(255, 255, 255, 0.06) 0px 1px 0px 0px inset`

**Subtle UI Card**
- Background: Whisper Gray (`#f9fafb`)
- Radius: `16px`
- Padding: `48px`
- Shadow: layered with `0.03` and `0.12` alpha values
  `rgba(17, 24, 39, 0.12) 0px 0px 0px 1px, rgba(17, 24, 39, 0.03) 0px 2px 2px -2px, rgba(17, 24, 39, 0.03) 0px 4px 4px 0px, rgba(17, 24, 39, 0.03) 0px 8px 8px 0px, rgba(17, 24, 39, 0.03) 0px 16px 16px 0px`

**Feature Card (Flat)**
- Background: transparent
- No border, no shadow
- Radius: `0px`
- Padding: `0px`
- Use: Visual segmentation of content without imposing visual boundaries

### Badges

**Status Chip**
- Background: Whisper Gray (`#f9fafb`)
- Text: Graphite Text (`#111827`)
- Radius: `8px`
- Padding: `4px 8px`
- Font: Inter, 14px, weight 500

### Navigation
- Sticky top bar
- Links: Silver Text (`#374151`) default, Graphite (`#111827`) or Arcade Blue (`#2142e7`) on hover/active
- Interactive regions: `12px` radius
- Inter, 16px, weight 500

## Do's and Don'ts

### Do
- Prioritize Inter for all text elements, leveraging weights 400–700. Reserve Balig Script for highly decorative brand elements only — never for information.
- Use Canvas White (`#ffffff`) as the base background, with Whisper Gray (`#f9fafb`) for subtle differentiation.
- Apply Arcade Blue (`#2142e7`) exclusively to primary CTAs and active states.
- Utilize border radii of `12px` for buttons and nav items, `16px` for inputs and cards.
- Apply aggressive negative letter-spacing on display sizes — `-1.6px` at 64px, scaling proportionally down.
- Use multi-layer shadow stacks for elevated elements — depth comes from layering, not from single heavy shadows.
- Apply the Deep Blue Shadow (`#182fa5`) border-shadow technique on primary buttons for the brand-tinted ring.
- Use the `rgba(255, 255, 255, 0.06) inset` highlight on top-tier elevated panels for the bevel effect.

### Don't
- Do not introduce new vibrant colors outside the Arcade Blue palette; controlled color is part of the architectural feel.
- Avoid sharp corners or harsh transitions — leverage the established radii (`12px`, `16px`, `24px`, `72px`).
- Do not use dark backgrounds for general body text sections; preserve the light composition for readability.
- Refrain from excessive gradient backgrounds. Limit them to the hero or distinct banners.
- Do not deviate from the typography scale and letter-spacing values; specific tracking is part of the brand voice.
- Avoid arbitrary padding values; stick to the defined scale (`4`, `8`, `10`, `12`, `16`, `24`, `32`, `40`, `48`).
- Do not replace multi-layer shadow stacks with single shadows — the layered build is the system's signature depth move.

---

## Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | Single column, display drops to ~36px, section gap reduces |
| md | `768px+` | Two-column text+visual layouts engage |
| lg | `1024px+` | Card grids, full nav with CTAs visible |
| xl | `1280px+` | Max-width container caps at `1304px` |

### Touch Targets
- Buttons: `10px 16px` padding yields ~40px touch height
- Action input: `16px` horizontal padding plus integrated button needs at least `48px` total height
- Status chips: `4px 8px` padding suits inline labels but not primary touch targets

### Collapsing Strategy
- Display: 64px → 48px → 36px on mobile; tracking scales proportionally
- Two-column text+visual layouts collapse to stacked single column
- Section gap: `96px` → `64px` → `48px` on mobile
- Card padding tightens from `48px` to `24px` at small mobile sizes
- Action input field stacks the button below at narrow widths
- Multi-layer shadows simplify on low-power devices to preserve performance

---

## Agent Prompt Guide

### Quick Color Reference
- Text (Primary): `#111827` (Graphite Text)
- Text (Secondary): `#4b5563` (Slate Text)
- Background (Primary): `#ffffff` (Canvas White)
- Background (Subtle): `#f9fafb` (Whisper Gray)
- CTA Button: `#2142e7` (Arcade Blue)
- Border (Neutral): `#e5e7eb` (Outline Ash)
- Primary Button Border-Shadow: `#182fa5` (Deep Blue Shadow)

### Example Component Prompts
1. **Hero Section**: Full-width background gradient `linear-gradient(rgb(17,24,39), rgba(30,43,72,0.9))`. Centered headline "Your product story, built by AI in minutes." in Inter, 64px, weight 700, color `#111827`, letter-spacing `-1.6px`. Subheading "Create beautiful, on-brand demos..." in Inter, 20px, weight 400, color `#4b5563`. Below: Action Input Field with Canvas White background, Outline Ash border, `72px` radius, integrated Arcade Blue submit button.
2. **Primary Button**: Arcade Blue (`#2142e7`) background, white text, `12px` radius, `10px 16px` padding. Inter, 16px, weight 500. Shadow: `rgba(17, 24, 39, 0.04) 0px 32px 32px 0px, rgba(17, 24, 39, 0.04) 0px 16px 16px 0px, rgba(17, 24, 39, 0.04) 0px 8px 8px 0px, rgba(17, 24, 39, 0.04) 0px 4px 4px -2px, rgba(17, 24, 39, 0.04) 0px 2px 2px -1px, rgb(24, 47, 165) 0px 0px 0px 1px`.
3. **Feature Testimonial Card**: Whisper Gray (`#f9fafb`) background, `16px` radius, `48px` padding. Main text "Arcade makes every format effortless." in Inter, 36px, weight 600, `#111827`, letter-spacing `-0.36px`. Shadow: `rgba(17, 24, 39, 0.12) 0px 0px 0px 1px, rgba(17, 24, 39, 0.03) 0px 2px 2px -2px, rgba(17, 24, 39, 0.03) 0px 4px 4px 0px, rgba(17, 24, 39, 0.03) 0px 8px 8px 0px, rgba(17, 24, 39, 0.03) 0px 16px 16px 0px`.
4. **Ghost Nav Button**: transparent background, Steel Accent (`#70747d`) text, no border, `12px` radius, `10px 16px` padding. Inter, 16px, weight 500. Text: "Talk to sales".
5. **Status Chip**: Whisper Gray (`#f9fafb`) background, Graphite Text (`#111827`) text, `8px` radius, `4px 8px` padding. Inter, 14px, weight 500.

### Iteration Guide
1. White canvas, near-black graphite text, single Arcade Blue accent — that's the structural baseline.
2. Single-face Inter handles every role; Balig Script is decoration only.
3. Polarized radius vocabulary: `12px` buttons, `16px` cards/inputs, `72px` large action shells.
4. Multi-layer shadow stacks (5–6 rgba layers) for tactile elevation — never single shadows on elevated elements.
5. Primary button gets the Deep Blue Shadow (`#182fa5`) border-shadow ring — the brand-tinted CTA signature.
6. Inset white highlight (`rgba(255, 255, 255, 0.06) inset`) on top-tier panels creates the bevel effect.
