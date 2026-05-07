---
version: alpha
name: Replicate
description: Developer playground at festival scale — orange-red-magenta gradient hero, massive 128px display type, exclusive 9999px pill geometry, dotted-underline links, and high-contrast black-and-white energy.

colors:
  # Primary
  background: "#ffffff"
  surface-near-white: "#fcfcfc"
  ink: "#202020"
  ink-pure: "#000000"
  on-dark: "#fcfcfc"

  # Brand
  primary: "#ea2804"
  primary-warm: "#dd4425"

  # Status / Semantic
  success: "#2b9a66"

  # Code surface
  code-bg: "#24292e"

  # Neutrals
  text-secondary: "#646464"
  text-emphasis: "#4e4e4e"
  text-tertiary: "#8d8d8d"
  text-muted: "#bbbbbb"

  # Frosted glass (opaque approx for hex compliance)
  glass-tint: "#e8e8e8"  # was rgba(255,255,255,0.1) — flatten for Google format

typography:
  display-mega:
    fontFamily: "rb-freigeist-neue, ui-sans-serif, system-ui, sans-serif"
    fontSize: 128px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0px
  display-hero:
    fontFamily: "rb-freigeist-neue, ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: -1.8px
  section-heading:
    fontFamily: "rb-freigeist-neue, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0px
  sub-heading:
    fontFamily: "rb-freigeist-neue, ui-sans-serif, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0px
  sub-heading-sans:
    fontFamily: "basier-square, ui-sans-serif, system-ui, sans-serif"
    fontSize: 38.4px
    fontWeight: 400
    lineHeight: 0.83
    letterSpacing: 0px
  feature-title:
    fontFamily: "basier-square, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.56
    letterSpacing: 0px
  body-large:
    fontFamily: "basier-square, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  body:
    fontFamily: "basier-square, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button:
    fontFamily: "basier-square, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.50
    letterSpacing: 0px
  caption:
    fontFamily: "basier-square, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  small-tag:
    fontFamily: "basier-square, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  code:
    fontFamily: "jetbrains-mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px

spacing:
  micro: 1px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px
  5xl: 96px
  6xl: 160px

rounded:
  pill: 9999px

components:
  # Buttons (everything is pill)
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  button-outline:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  button-glass:
    backgroundColor: "{colors.glass-tint}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 6px 28px

  # Cards & containers
  card:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: 16px
  card-featured:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    rounded: "{rounded.pill}"
    padding: 16px

  # Inputs
  input:
    backgroundColor: "{colors.glass-tint}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 6px 28px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    padding: 16px 24px
  nav-link:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.text-muted}"

  # Status badges
  badge-status:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 12px

  # Code blocks
  code-block:
    backgroundColor: "{colors.code-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.code}"
    rounded: "{rounded.pill}"
    padding: 16px 24px

  # Manifesto / dark hero
  manifesto:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-mega}"
    padding: 96px

  # Tag
  tag:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.small-tag}"
    rounded: "{rounded.pill}"
    padding: 2px 10px

  # Text emphasis variants
  text-emphasis:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-emphasis}"
    typography: "{typography.body}"
  text-tertiary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-tertiary}"
    typography: "{typography.caption}"

  # Pure-black emphasis surface
  surface-pure-black:
    backgroundColor: "{colors.ink-pure}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.pill}"
    padding: 24px

  # Near-white surface
  surface-light:
    backgroundColor: "{colors.surface-near-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: 16px

  # Brand-warm border button
  button-warm:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary-warm}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
---

# Replicate Design System

## Overview

Replicate's interface is a developer playground crackling with creative energy — a bold, high-contrast design that feels more like a music festival poster than a typical API platform. The hero section explodes with a vibrant orange-red-magenta gradient that immediately signals "this is where AI models come alive," while the body of the page grounds itself in a clean white canvas where code snippets and model galleries take center stage.

The design personality is defined by two extreme choices: **massive display typography** (up to 128px) using the custom rb-freigeist-neue face, and **exclusively pill-shaped geometry** (9999px radius on everything). The display font is thick, bold, and confident — its heavy weight at enormous sizes creates text that feels like it's shouting with joy rather than whispering authority. Combined with basier-square for body text (a clean geometric sans) and JetBrains Mono for code, the system serves developers who want power and playfulness in equal measure.

What makes Replicate distinctive is its community-powered energy. The model gallery with AI-generated images, the dotted-underline links, the green status badges, and the "Imagine what you can build" closing manifesto all create a space that feels alive and participatory — not a corporate product page but a launchpad for creative developers.

**Key Characteristics:**
- Explosive orange-red-magenta gradient hero (`{colors.primary}` brand anchor)
- Massive display typography (128px) in heavy rb-freigeist-neue
- Exclusively pill-shaped geometry: 9999px radius on EVERYTHING
- High-contrast black (`{colors.ink}`) and white palette with red brand accent
- Developer-community energy: model galleries, code examples, dotted-underline links
- Green status badges (`{colors.success}`) for live/operational indicators
- Bold/heavy font weights (600–700) creating maximum typographic impact
- Playful closing manifesto: "Imagine what you can build."

## Colors

### Primary
- **Replicate Dark** (`{colors.ink}`): The primary text color and dark surface — a near-black that's the anchor of all text and borders. Slightly warmer than pure black.
- **Replicate Red** (`{colors.primary}`): The core brand color — a vivid, saturated orange-red used in the hero gradient, accent borders, and high-signal moments.
- **Secondary Red** (`{colors.primary-warm}`): A slightly warmer variant for button borders and link hover states.

### Secondary & Accent
- **Status Green** (`{colors.success}`): Badge/pill background for "running" or operational status indicators.
- **GitHub Dark** (`{colors.code-bg}`): A blue-tinted dark used for code block backgrounds.

### Surface & Background
- **Pure White** (`{colors.background}`): The primary page body background.
- **Near White** (`{colors.surface-near-white}`): Button text on dark surfaces and the lightest content.
- **Glass Tint** (`{colors.glass-tint}`): Semi-transparent surface for inputs and frosted glass buttons.
- **Hero Gradient**: A dramatic orange → red → magenta → pink gradient for the hero section.

### Neutrals & Text
- **Medium Gray** (`{colors.text-secondary}`): Secondary body text and de-emphasized content.
- **Warm Gray** (`{colors.text-emphasis}`): Emphasized secondary text.
- **Mid Silver** (`{colors.text-tertiary}`): Tertiary text, footnotes.
- **Light Silver** (`{colors.text-muted}`): Dotted-underline link decoration color, muted metadata.
- **Pure Black** (`{colors.ink-pure}`): Maximum-emphasis borders and occasional text.

### Gradient System
- **Hero Blaze**: A dramatic multi-stop gradient flowing through orange → red → magenta → hot pink. The most visually dominant element on the page.
- **Dark Sections**: Deep dark sections with white/near-white text provide contrast against the white body.

## Typography

### Font Family
- **Display**: `rb-freigeist-neue`, with fallbacks: `ui-sans-serif, system-ui`.
- **Body / UI**: `basier-square`, with fallbacks: `ui-sans-serif, system-ui`.
- **Code**: `jetbrains-mono`, with fallbacks: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New`.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-mega}`, `{typography.body}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-mega` | 128px — the closing manifesto |
| `display-hero` | 72px — hero section headline |
| `section-heading` | 48px — feature section titles |
| `sub-heading` | 30px — card headings |
| `sub-heading-sans` | 38.4px sans — large body headings |
| `feature-title` | 18px — small section titles |
| `body-large` | 20px — intro paragraphs |
| `body` | 16px — standard text, buttons |
| `button` | 16px semibold — buttons |
| `caption` | 14px — metadata, descriptions |
| `small-tag` | 12px — tags (lowercase transform) |
| `code` | 14px JetBrains Mono — code |

### Principles
- **Heavy display, light body**: rb-freigeist-neue at 700 weight creates thundering headlines, while basier-square at 400 handles body text with quiet efficiency. The contrast is extreme and intentional.
- **128px is a real size**: The closing manifesto "Imagine what you can build." uses 128px — bigger than most mobile screens.
- **Negative tracking on hero**: -1.8px letter-spacing at 72px creates dense, impactful hero text.
- **Lowercase tags**: 12px basier-square uses `text-transform: lowercase` — an unusual choice that creates a casual, developer-friendly vibe.
- **Weight 600 as emphasis**: When basier-square needs emphasis, it uses 600 (semibold) — never bold (700), which is reserved for rb-freigeist-neue display text.

## Layout

### Spacing System
Base unit is **8px**. Section vertical spacing is generous (`5xl`–`6xl`, 96–160px). Button padding varies widely (0–28px asymmetric).

### Grid & Container
- Fluid width with responsive constraints
- Hero: full-width gradient with centered content
- Model gallery: multi-column responsive grid
- Feature sections: mixed layouts
- Code examples: contained dark blocks

### Whitespace Philosophy
- **Bold and generous**: Massive spacing between sections (up to 160px+) creates distinct zones.
- **Dense within galleries**: Model images are tightly packed in the grid for browsable density.
- **The gradient IS the whitespace**: The hero gradient section occupies significant vertical space as a colored void.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | White body, text blocks |
| Bordered (Level 1) | `1px solid {colors.ink}` | Cards, buttons, containers |
| Accent Border (Level 2) | `1px solid {colors.primary}` | Featured/highlighted items |
| Gradient Hero (Level 3) | Full-width blaze gradient | Hero section, maximum visual impact |
| Dark Section (Level 4) | Dark bg with light text | Manifesto, footer, feature sections |

**Shadow Philosophy**: Replicate relies on **borders and background color** for depth rather than shadows. The `1px solid {colors.ink}` border is the primary containment mechanism. The dramatic gradient hero and dark/light section alternation provide all the depth the design needs.

## Shapes

| Token | Value | Use |
|---|---|---|
| `pill` | 9999px | Everything — buttons, images, badges, containers |

The pill (9999px) is the ONLY radius in the system. Everything interactive, every image, every badge, every label, every container uses 9999px. This is the most extreme pill-radius commitment in any major tech brand.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly rather than reconstructing them.

### Buttons
- **`button-dark`** — Replicate Dark bg, near-white text, pill shape. Maximum emphasis.
- **`button-outline`** — White bg, dark text, dark border, pill. Clean secondary actions.
- **`button-glass`** — Frosted glass surface with light silver border, asymmetric padding for icon/search layouts.
- **`button-warm`** — Warm-red text variant.

### Cards & Containers
- **`card`** — White surface, 1px dark border for prominent containment.
- **`card-featured`** — Brand red accent for highlighted/featured items.
- **`surface-pure-black`** — Maximum-contrast black panel.
- **`surface-light`** — Near-white alt surface.

### Inputs & Forms
- **`input`** — Frosted glass surface with subtle border, search-bar style padding.

### Navigation
- **`nav-bar`** — Clean horizontal nav on white. Logo: Replicate wordmark in dark.
- **`nav-link`** — Dark text with dotted underline on hover.
- **`nav-link-hover`** — Text shifts to muted on hover.

### Status & Tags
- **`badge-status`** — Status Green pill with white text for operational indicators.
- **`tag`** — Pill tag with muted secondary text.

### Code Blocks
- **`code-block`** — Dark `{colors.code-bg}` surface, JetBrains Mono, white text, pill container.

### Manifesto
- **`manifesto`** — Dark surface with 128px display-mega type. The emotional climax of the page.

### Distinctive Patterns

**Model Gallery Grid** — Horizontal scrolling or grid of AI-generated images, each in a pill-shaped container, with model names and run counts.

**Dotted Underline Links** — Links use `text-decoration: underline dotted {colors.text-muted}` — a distinctive, developer-notebook aesthetic.

## Do's and Don'ts

### Do
- Use pill-shaped (9999px) radius on EVERYTHING — buttons, images, badges, containers
- Use rb-freigeist-neue at weight 700 for display text — go big (72px+) or go home
- Use the orange-red brand gradient for hero sections
- Use Replicate Dark (`{colors.ink}`) as the primary dark — not pure black
- Apply dotted underline decoration on text links (`{colors.text-muted}`)
- Use Status Green (`{colors.success}`) for operational/success badges
- Keep body text in basier-square at 400–600 weight
- Use JetBrains Mono for all code content
- Create a "manifesto" section with 128px type for emotional impact

### Don't
- Don't use any border-radius other than 9999px — the pill system is absolute
- Don't use the brand red (`{colors.primary}`) as a surface/background color — it's for gradients and accent borders
- Don't reduce display text below 48px on desktop — the heavy display font needs size to breathe
- Don't use light/thin font weights on rb-freigeist-neue — 600–700 is the range
- Don't use solid underlines on links — dotted is the signature
- Don't add drop shadows — depth comes from borders and background color
- Don't use warm neutrals — the gray scale is purely neutral
- Don't skip the code examples — they're primary content, not decoration
- Don't make the hero gradient subtle — it should be BOLD and vibrant

## Responsive Behavior

### Breakpoints
*No explicit breakpoints detected — likely using fluid/container-query responsive system.*

### Touch Targets
- Pill buttons with generous padding
- Gallery images as large touch targets
- Navigation adequately spaced

### Collapsing Strategy
- **Hero text**: 128px → 72px → 48px progressive scaling
- **Model gallery**: Grid reduces columns
- **Navigation**: Collapses to hamburger
- **Manifesto**: Scales down but maintains impact

### Image Behavior
- AI-generated images scale within pill containers
- Gallery reflows to fewer columns on narrow screens
- Hero gradient maintained at all sizes

## Agent Prompt Guide

### Quick Color Reference
- Primary Text: Replicate Dark (`{colors.ink}`)
- Page Background: Pure White (`{colors.background}`)
- Brand Accent: Replicate Red (`{colors.primary}`)
- Secondary Text: Medium Gray (`{colors.text-secondary}`)
- Muted/Decoration: Light Silver (`{colors.text-muted}`)
- Status: Status Green (`{colors.success}`)
- Dark Surface: Replicate Dark (`{colors.ink}`)

### Example Component Prompts
- "Create a hero section with a vibrant orange-red-magenta gradient background. Headline at 72px rb-freigeist-neue weight 700, white text, -1.8px letter-spacing. Include a dark pill CTA button and a white outlined pill button."
- "Design a model card with pill-shaped (9999px) image container, model name at 16px basier-square weight 600, run count at 14px in Medium Gray. Border: 1px solid `{colors.ink}`."
- "Build a status badge: pill-shaped (9999px), Status Green (`{colors.success}`) background, white text at 14px basier-square."
- "Create a manifesto section on Replicate Dark (`{colors.ink}`) with 'Imagine what you can build.' at 128px rb-freigeist-neue weight 700, white text. Embed small AI-generated images between the words."
- "Design a code block: dark background (`{colors.code-bg}`), JetBrains Mono at 14px, white text. Pill-shaped container."

### Iteration Guide
1. Everything is pill-shaped — never specify any other border-radius
2. Display text is HEAVY — weight 700, sizes 48px+
3. Links use dotted underline (`{colors.text-muted}`) — never solid
4. The gradient hero is the visual anchor — make it bold
5. Use basier-square for body, rb-freigeist-neue for display, JetBrains Mono for code
