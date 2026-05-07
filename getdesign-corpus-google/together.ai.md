---
version: alpha
name: Together AI
description: Pastel-gradient enterprise AI — soft pink/blue/lavender hero washes, midnight-blue dark sections, "The Future" display with aggressive negative tracking, PP Neue Montreal Mono uppercase labels, sharp 4–8px geometry.

colors:
  # Canvas
  background: "#ffffff"
  surface: "#ffffff"
  surface-dark: "#010120"
  ink: "#000000"
  ink-inverted: "#ffffff"

  # Brand accents — used in illustrations only
  primary: "#ef2cc1"
  secondary: "#fc4c02"
  accent-lavender: "#bdbbff"

  # On-color
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  on-surface-dark: "#ffffff"

  # Borders + glass (opaque approximations)
  border: "#ebebeb"           # was rgba(0,0,0,.08) — flattened over white
  border-dark: "#1f1f3a"      # was rgba(255,255,255,.12) — flattened over #010120
  glass-light: "#e0e0e0"      # was rgba(255,255,255,.12) on dark
  glass-dark-tint: "#ebebeb"  # was rgba(0,0,0,.08) on light
  badge-tint: "#f5f5f5"       # was rgba(0,0,0,.04) — flattened over white

  # Tinted shadow — distinctive midnight blue
  shadow-blue: "#cccce6"      # was rgba(1,1,32,.1) — flattened over white

typography:
  display:
    fontFamily: "The Future, Arial, sans-serif"
    fontSize: 64px
    fontWeight: 500
    lineHeight: 1.10
    letterSpacing: -1.92px
  section-heading:
    fontFamily: "The Future, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: -0.8px
  sub-heading:
    fontFamily: "The Future, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.42px
  feature-title:
    fontFamily: "The Future, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.22px
  body-large:
    fontFamily: "The Future, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.18px
  body:
    fontFamily: "The Future, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.16px
  button-ui:
    fontFamily: "The Future, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.16px
  caption:
    fontFamily: "The Future, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  mono-label:
    fontFamily: "PP Neue Montreal Mono, Georgia, serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.00
    letterSpacing: 0.08px
  mono-small:
    fontFamily: "PP Neue Montreal Mono, Georgia, serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.00
    letterSpacing: 0.055px
  mono-micro:
    fontFamily: "PP Neue Montreal Mono, Georgia, serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0.05px

spacing:
  micro: 1px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 80px
  5xl: 120px

rounded:
  none: 0px
  sm: 4px
  md: 8px
  pill: 9999px

components:
  # Dark solid CTA — primary on light surfaces
  button-primary:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 8px 16px

  # Glass button — for dark sections
  button-glass:
    backgroundColor: "{colors.glass-light}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 8px 16px

  # Outlined light — secondary on light
  button-outlined:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    borderColor: "{colors.border}"

  # Card — light
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 24px
    borderColor: "{colors.border}"

  # Card — dark variant for research
  card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-surface-dark}"
    rounded: "{rounded.md}"
    padding: 24px
    borderColor: "{colors.border-dark}"

  # Stats card — large display numbers
  card-stats:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.display}"
    rounded: "{rounded.md}"
    padding: 32px

  # Badge / tag
  badge:
    backgroundColor: "{colors.badge-tint}"
    textColor: "{colors.ink}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
    borderColor: "{colors.border}"

  # Badge on dark
  badge-dark:
    backgroundColor: "{colors.glass-light}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
    borderColor: "{colors.border-dark}"

  # Top nav
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 16px 24px

  # Mono section label
  section-label:
    textColor: "{colors.ink}"
    typography: "{typography.mono-small}"

  # Input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    borderColor: "{colors.border}"
---

# Together AI Design System

## Overview

Together AI's interface is a pastel-gradient dreamscape built for enterprise AI infrastructure — a design that somehow makes GPU clusters and model inference feel light, airy, and optimistic. The hero section blooms with soft pink-blue-lavender gradients and abstract, painterly illustrations that evoke clouds and flight, establishing a visual metaphor for the "AI-Native Cloud" proposition. Against this softness, the typography cuts through with precision: "The Future" display font at 64px with aggressive negative tracking (-1.92px) creates dense, authoritative headline blocks.

The design straddles two worlds: a bright, white-canvas light side where pastel gradients and stats cards create an approachable platform overview, and a dark midnight-blue universe (`{colors.surface-dark}` — not gray-black but a deep midnight blue) where research papers and technical content live. This dual-world approach elegantly separates the "business" messaging (light, friendly, stat-driven) from the "research" messaging (dark, serious, academic).

What makes Together AI distinctive is its type system. "The Future" handles all display and body text with a geometric modernist aesthetic, while "PP Neue Montreal Mono" provides uppercase labels with meticulous letter-spacing — creating a "technical infrastructure company with taste" personality. The brand accents — magenta (`{colors.primary}`) and orange (`{colors.secondary}`) — appear sparingly in gradients and illustrations, never polluting the clean UI.

**Key Characteristics:**
- Soft pastel gradients (pink, blue, lavender) against pure white canvas
- Deep midnight blue (`{colors.surface-dark}`) for dark/research sections — not gray-black
- Custom "The Future" font with aggressive negative letter-spacing throughout
- PP Neue Montreal Mono for uppercase technical labels
- Sharp geometry (`{rounded.sm}`, `{rounded.md}`) — not rounded, not pill
- Magenta + orange brand accents in illustrations only
- Lavender (`{colors.accent-lavender}`) as a soft secondary accent
- Enterprise stats prominently displayed (2x, 60%, 90%)
- Dark-blue-tinted shadows

## Colors

### Primary
- **Brand Magenta** (`{colors.primary}`): The primary brand accent — vivid pink-magenta in gradient illustrations and the highest-signal moments. Never UI chrome.
- **Brand Orange** (`{colors.secondary}`): Secondary brand accent — vivid orange for gradient endpoints.
- **Dark Blue** (`{colors.surface-dark}`): Primary dark surface — deep midnight blue-black for research, footer, dark containers. Distinctly blue, not gray.

### Secondary & Accent
- **Soft Lavender** (`{colors.accent-lavender}`): Gentle blue-violet for subtle accents and soft UI highlights.

### Surface & Background
- **Pure White** (`{colors.background}`): Primary light-section page background.
- **Dark Blue** (`{colors.surface-dark}`): Dark-section backgrounds — research, footer, technical content.
- **Glass Light** (`{colors.glass-light}`): Frosted glass button backgrounds on dark sections.
- **Glass Dark Tint** (`{colors.glass-dark-tint}`): Subtle tinted surfaces on light sections.

### Neutrals & Text
- **Pure Black** (`{colors.ink}`): Primary text on light surfaces.
- **Pure White** (`{colors.ink-inverted}`): Primary text on dark surfaces.
- **Border Light** (`{colors.border}`): Borders and subtle containment on light surfaces.
- **Border Dark** (`{colors.border-dark}`): Borders and containment on dark surfaces.

### Gradient System
- **Pastel Cloud Gradient**: Soft pink → lavender → soft blue gradients in hero illustrations. Abstract painterly forms — clouds, feathers, flowing shapes.
- **Hero Gradient**: Soft pastel tints layered over white, creating a dawn-like atmospheric effect.

## Typography

### Font Family
- **Primary**: `The Future`, with fallback: `Arial`
- **Monospace / Labels**: `PP Neue Montreal Mono`, with fallback: `Georgia`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display}`, `{typography.body}`, etc.).

| Token | Use |
|---|---|
| `display` | 64px hero — maximum impact, dense blocks |
| `section-heading` | Feature section titles |
| `sub-heading` | Card headings |
| `feature-title` | Small feature headings |
| `body-large` | Descriptions, sections |
| `body` | Standard body, nav |
| `button-ui` | Button labels |
| `caption` | Metadata, descriptions |
| `mono-label` | Uppercase section labels |
| `mono-small` | Small uppercase tags — navigational signposts |
| `mono-micro` | Smallest uppercase labels |

### Principles
- **Negative tracking everywhere**: Every "The Future" size uses negative letter-spacing (-0.16px to -1.92px) — consistently tight and modern.
- **Mono for structure**: PP Neue Montreal Mono in uppercase with positive letter-spacing creates technical "label" moments.
- **Weight 500 as emphasis**: 400 (regular) and 500 (medium) only — no bold.
- **Tight line-heights throughout**: Even body text uses 1.25–1.30 — denser than typical, information-rich feel.

## Layout

### Spacing System
The complete scale lives in the `spacing:` token block above. Base unit is 8px. Section vertical spacing is generous (`{spacing.4xl}`–`{spacing.5xl}`).

### Grid & Container
- Max container width: approximately 1200px, centered
- Hero: centered with pastel gradient background
- Feature sections: multi-column card grids
- Stats: horizontal row of metric cards
- Research: dark full-width section

### Whitespace Philosophy
- **Optimistic breathing room**: Generous spacing between sections makes enterprise AI infrastructure feel accessible.
- **Dual atmosphere**: Light sections breathe with whitespace; dark sections are denser with content.
- **Stats as visual anchors**: Large numbers with small captions create natural focal points.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Page background, text blocks |
| Contained (Level 1) | `1px solid {colors.border}` (light) or `{colors.border-dark}` (dark) | Cards, badges, containers |
| Elevated (Level 2) | `0 4px 10px {colors.shadow-blue}` | Feature cards, hover states |
| Dark Zone (Level 3) | `{colors.surface-dark}` full-width background | Research, footer, technical sections |

**Shadow Philosophy**: Together AI uses a single, distinctive shadow — tinted with midnight blue (`{colors.shadow-blue}`) rather than generic black. This gives elevated elements a subtle blue-ish cast that ties them to the brand's midnight-blue dark mode.

## Shapes

The system is deliberately restrained — no pills, no generous rounding. The sharp geometry contrasts with the soft pastel gradients.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `sm` | 4px | Buttons, badges, tags, small interactive elements — primary radius |
| `md` | 8px | Larger containers, feature cards |
| `pill` | 9999px | Reserved (avatars only, rare) |

## Components

The full component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card}`).

### Buttons
- **`button-primary`** — Dark Blue solid, white text, sharp `{rounded.sm}`. Primary CTA on light surfaces.
- **`button-glass`** — Frosted glass over dark sections, white text.
- **`button-outlined`** — Transparent with border, black text. Secondary on light.

### Cards & Containers
- **`card`** — White surface with `{colors.border}` 1px hairline, `{rounded.md}` radius.
- **`card-dark`** — Midnight blue surface with `{colors.border-dark}` border. Research/dark zones.
- **`card-stats`** — Large display number cards (64px, weight 500) with caption beneath.

### Badges / Tags
- **`badge`** — Small tinted surface with border, mono uppercase label, 2×8px padding.
- **`badge-dark`** — Glass tint on dark sections.

### Navigation
- **`nav-bar`** — Clean horizontal nav on white. Logo + wordmark; links + dark CTA right.

### Mono Section Labels
- **`section-label`** — Used as navigational signposts. Technical, structured feel.

### Image Treatment
- Abstract pastel gradient illustrations (cloud/feather forms)
- Product UI screenshots on dark/light surfaces
- Team photos in editorial style
- Research paper cards with dark backgrounds

### Distinctive Components
- **Stats Bar**: Large metrics (2x, 60%, 90%) in bold display numbers with short captions.
- **Research Section**: Dark Blue background, white text, paper thumbnails — distinct "academic" zone.
- **Large Footer Logo**: "together" wordmark at massive scale in dark footer — brand-statement closing.

## Do's and Don'ts

### Do
- Use pastel gradients (pink/blue/lavender) for hero illustrations and decorative backgrounds
- Use Dark Blue (`{colors.surface-dark}`) for dark sections — never generic gray-black
- Apply negative letter-spacing on all "The Future" text (scaled by size)
- Use PP Neue Montreal Mono in uppercase for section labels
- Keep border-radius sharp (`{rounded.sm}`) for badges and interactive elements
- Use the dark-blue-tinted shadow for elevation
- Maintain the light/dark section duality
- Show enterprise stats prominently with large display numbers

### Don't
- Don't use Brand Magenta or Brand Orange as UI colors — they're for illustrations only
- Don't use pill-shaped or generously rounded corners — geometry is sharp
- Don't use generic gray-black for dark sections — always Dark Blue
- Don't use positive letter-spacing on "The Future" — always negative
- Don't use bold (700+) weight — 400–500 is the full range
- Don't use warm-toned shadows — always midnight-blue-tinted
- Don't reduce section spacing below 48px — open feeling is core
- Don't mix in additional typefaces — "The Future" + PP Neue Montreal Mono is the pair

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <479px | Compact layout, stacked everything |
| Large Mobile | 479–767px | Single column, hamburger nav |
| Tablet | 768–991px | 2-column grids begin |
| Desktop | 992px+ | Full multi-column layout |

### Touch Targets
- Buttons with adequate padding
- Card surfaces as touch targets
- Navigation links at comfortable 16px

### Collapsing Strategy
- Navigation: collapses to hamburger on mobile
- Hero text: 64px → 40px → 28px progressive scaling
- Stats bar: horizontal → stacked vertical
- Feature grids: multi-column → single column
- Research section: cards stack vertically

### Image Behavior
- Pastel illustrations scale proportionally
- Product screenshots maintain aspect ratio
- Team photos scale within containers

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Text (light): Pure Black `{colors.ink}`
- Primary Text (dark): Pure White `{colors.ink-inverted}`
- Page Background: Pure White `{colors.background}`
- Dark Surface: Dark Blue `{colors.surface-dark}`
- Brand Accent 1: Brand Magenta `{colors.primary}`
- Brand Accent 2: Brand Orange `{colors.secondary}`
- Soft Accent: Soft Lavender `{colors.accent-lavender}`
- Border (light): `{colors.border}`

### Example Component Prompts
- "Create a hero section on white with soft pastel gradients (pink → lavender → blue). Headline at 64px 'The Future' weight 500, line-height 1.10, letter-spacing -1.92px. Pure Black text. Include a dark blue CTA button (`{colors.surface-dark}`, 4px radius)."
- "Design a stats card: large display number (64px, weight 500) with a small caption below (14px). White background, 8px radius, midnight-blue-tinted shadow."
- "Build a section label: PP Neue Montreal Mono, 11px, weight 500, uppercase, letter-spacing 0.055px. Black text on light, white on dark."
- "Create a dark research section: Dark Blue (`{colors.surface-dark}`) background. White text, section heading at 40px 'The Future' weight 500, letter-spacing -0.8px. Cards with `{colors.border-dark}` border."
- "Design a badge: 4px radius, light tinted background, 1px solid `{colors.border}`, 'The Future' 16px text. Padding: 2px 8px."

### Iteration Guide
1. Always specify negative letter-spacing for "The Future" — scaled by size
2. Dark sections use `{colors.surface-dark}` (midnight blue), never generic black
3. Shadows are always midnight-blue-tinted
4. Mono labels are always uppercase with positive letter-spacing
5. Keep radius sharp (`{rounded.sm}` or `{rounded.md}`) — no pills, no generous rounding
6. Pastel gradients are for decoration, not UI chrome
