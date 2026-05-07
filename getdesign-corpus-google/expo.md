---
version: alpha
name: Expo
description: Luminous developer platform with cool-tinted off-white canvas, monochromatic interface, pill-shaped geometry, massive Inter display headlines with extreme negative tracking, and gallery-like spacing.

colors:
  # Primary
  ink: "#000000"
  text-primary: "#1c2024"

  # Surfaces
  background: "#f0f0f3"
  surface: "#ffffff"
  surface-dark: "#1a1a1a"
  surface-darker: "#171717"

  # Brand accent (the system has no chromatic brand color — black is the primary)
  primary: "#000000"
  on-primary: "#ffffff"

  # Links / accents
  link: "#0d74ce"
  link-legal: "#476cff"
  link-widget: "#47c2ff"
  preview-purple: "#8145b5"

  # Neutral text
  text-secondary: "#60646c"
  text-mid: "#555860"
  text-tertiary: "#b0b4ba"
  text-pewter: "#999999"
  text-light: "#cccccc"
  text-dark-slate: "#363a3f"
  text-charcoal: "#333333"

  # Semantic
  warning: "#ab6400"
  destructive: "#eb8e90"
  focus-ring: "#2547d0"

  # Borders
  border: "#e0e1e6"
  input-border: "#d9d9e0"

  # Shadow stand-ins
  shadow-soft: "#ebebec"  # opaque approx of rgba(0,0,0,0.08) — Google format requires hex
  shadow-elevated: "#e5e5e6"  # opaque approx of rgba(0,0,0,0.10)

typography:
  display-hero:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: -3px
  section-heading:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -2px
  sub-heading:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.25px
  body-large:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  body:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  button:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0px
  small:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0px
  code:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  code-small:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px

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
  5xl: 64px
  6xl: 80px
  7xl: 96px
  8xl: 144px

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 16px
  xl: 24px
  2xl: 32px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 0px 12px

  button-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 20px

  button-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 20px

  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 24px

  card-featured:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.xl}"
    padding: 32px

  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 0px 12px

  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    typography: "{typography.caption}"
    padding: 16px 24px

  status-badge:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: 4px 12px

  code-block:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    typography: "{typography.code-small}"
    rounded: "{rounded.md}"
    padding: 16px

  link:
    textColor: "{colors.link}"
    typography: "{typography.body}"
    padding: 0px
---

# Expo Design System

## Overview

Expo's interface is a luminous, confidence-radiating developer platform built on the premise that tools for building apps should feel as polished as the apps themselves. The entire experience lives on a bright, airy canvas — a cool-tinted off-white (`{colors.background}`) that gives the page a subtle technological coolness without the starkness of pure white. This is a site that breathes: enormous vertical spacing between sections creates a gallery-like pace where each feature gets its own "room."

The design language is decisively monochromatic — pure black (`{colors.ink}`) headlines against the lightest possible backgrounds, with a spectrum of cool blue-grays (`{colors.text-secondary}`, `{colors.text-tertiary}`, `{colors.text-mid}`) handling all secondary communication. Color is almost entirely absent from the interface itself; when it appears, it's reserved for product screenshots, app icons, and the React universe illustration — making the actual content burst with life against the neutral canvas.

What makes Expo distinctive is its pill-shaped geometry. Buttons, tabs, video containers, and even images use generously rounded or fully pill-shaped corners (`{rounded.xl}`–`{rounded.pill}`), creating an organic, approachable feel that contradicts the typical sharp-edged developer tool aesthetic. Combined with tight letter-spacing on massive headlines (-1.6px to -3px at 64px), the result is a design that's simultaneously premium and friendly — like an Apple product page reimagined for developers.

**Key Characteristics:**
- Luminous cool-white canvas (`{colors.background}`) with gallery-like vertical spacing
- Strictly monochromatic: pure black headlines, cool blue-gray body text, no decorative color
- Pill-shaped geometry everywhere — buttons, tabs, containers, images
- Massive display headlines (64px) with extreme negative letter-spacing (-1.6px to -3px)
- Inter as the sole typeface, used at weights 400–900 for full expressive range
- Whisper-soft shadows that barely lift elements from the surface
- Product screenshots as the only source of color in the interface

## Colors

### Primary
- **Expo Black** (`{colors.ink}`): The absolute anchor — used for primary headlines, CTA buttons, and the brand identity. Pure black on cool white creates maximum contrast without feeling aggressive.
- **Near Black** (`{colors.text-primary}`): The primary text color for body content — a barely perceptible blue-black that's softer than pure `#000` for extended reading.

### Secondary & Accent
- **Link Cobalt** (`{colors.link}`): The standard link color — a trustworthy, saturated blue that signals interactivity without competing with the monochrome hierarchy.
- **Legal Blue** (`{colors.link-legal}`): A brighter, more saturated blue for legal/footer links.
- **Widget Sky** (`{colors.link-widget}`): A light, friendly cyan-blue for widget branding elements.
- **Preview Purple** (`{colors.preview-purple}`): A rich violet used for "preview" or beta feature indicators.

### Surface & Background
- **Cloud Gray** (`{colors.background}`): The primary page background — a cool off-white with the faintest blue-violet tint.
- **Pure White** (`{colors.surface}`): Card surfaces, button backgrounds, and elevated content containers.
- **Widget Dark** (`{colors.surface-dark}`): Dark surface for dark-theme widgets and overlay elements.
- **Banner Dark** (`{colors.surface-darker}`): The darkest surface variant, used for promotional banners.

### Neutrals & Text
- **Slate Gray** (`{colors.text-secondary}`): The workhorse secondary text color.
- **Mid Slate** (`{colors.text-mid}`): Slightly darker than Slate, used for emphasized secondary text.
- **Silver** (`{colors.text-tertiary}`): Tertiary text, placeholders, and de-emphasized metadata.
- **Pewter** (`{colors.text-pewter}`): Accordion icons and deeply de-emphasized UI elements in dark contexts.
- **Light Silver** (`{colors.text-light}`): Arrow icons and decorative elements in dark contexts.
- **Dark Slate** (`{colors.text-dark-slate}`): Borders on dark surfaces, switch tracks.
- **Charcoal** (`{colors.text-charcoal}`): Dark mode switch backgrounds and deep secondary surfaces.

### Semantic & Accent
- **Warning Amber** (`{colors.warning}`): A warm, deep amber for warning states.
- **Destructive Rose** (`{colors.destructive}`): A soft pink-coral for disabled destructive actions.
- **Border Lavender** (`{colors.border}`): Standard card/container borders.
- **Input Border** (`{colors.input-border}`): Button and form element borders.
- **Dark Focus Ring** (`{colors.focus-ring}`): Deep blue for keyboard focus indicators.

### Shadow Stand-Ins
- **Whisper** (`{colors.shadow-soft}`): Approximation of the gentle 3px lift used on cards.
- **Elevated** (`{colors.shadow-elevated}`): Approximation of the standard 10px ambient drop.

The design is notably **gradient-free** in the interface layer. Visual richness comes from product screenshots, the React universe illustration, and careful shadow layering rather than color gradients.

## Typography

### Font Family
- **Primary**: `Inter`, with fallbacks: `-apple-system, system-ui`
- **Monospace**: `JetBrains Mono`, with fallback: `ui-monospace`

### Hierarchy

| Token | Use |
|---|---|
| `display-hero` | Maximum impact 64px Inter weight 700 with extreme tracking |
| `section-heading` | 48px weight 600 — feature section anchors |
| `sub-heading` | 20px weight 600 — card titles, feature names |
| `body-large` | 18px weight 400 — intro paragraphs |
| `body` | 16px weight 400 — standard text, nav links |
| `button` | 16px weight 500 — buttons |
| `caption` | 14px weight 500 — descriptions, metadata |
| `small` | 12px weight 500 — badges |
| `code` | 16px JetBrains Mono — inline code |
| `code-small` | 14px JetBrains Mono — code blocks |

### Principles
- **One typeface, full expression**: Inter is the only sans-serif, used from weight 400 (regular) through 900 (black). This gives the design a unified voice while still achieving dramatic contrast between whisper-light body text and thundering display headlines.
- **Extreme negative tracking at scale**: Headlines at 64px use -1.6px to -3px letter-spacing, creating ultra-dense text blocks that feel like logotypes.
- **Weight as hierarchy**: 700–900 for display, 600 for headings, 500 for emphasis, 400 for body. The jumps are decisive — no ambiguous in-between weights.
- **Consistent body line-height**: Nearly all body and UI text shares 1.40 line-height, creating a rhythmic vertical consistency.

## Layout

### Spacing System
Base unit is **8px**. Scale lives in YAML and runs from `micro` (1px) to `8xl` (144px). Section vertical spacing is enormous — 96–144px between major sections — supporting the gallery-like pacing.

### Grid & Container
- Max container width: ~1200–1400px, centered
- Hero: centered single-column with massive breathing room
- Feature sections: alternating layouts (image left/right, full-width showcases)
- Card grids: 2–3 column for feature highlights
- Full-width sections with contained inner content

### Whitespace Philosophy
- **Gallery-like pacing**: Each section feels like its own exhibit, surrounded by vast empty space.
- **Breathing room is the design**: The generous whitespace IS the primary design element — it communicates confidence, quality, and that each feature deserves individual attention.
- **Content islands**: Sections float as isolated "islands" in the white space, connected by scrolling rather than visual continuation.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Cloud Gray page background, inline text |
| Surface (Level 1) | White bg, no shadow | Standard white cards on Cloud Gray |
| Whisper (Level 2) | Soft `{colors.shadow-soft}` lift | Subtle card lift, hover states |
| Elevated (Level 3) | Stronger `{colors.shadow-elevated}` drop | Feature showcases, product screenshots |
| Modal (Level 4) | Dark overlay + heavy shadow | Dialogs, overlays |

**Shadow Philosophy**: Expo uses shadows as gentle whispers rather than architectural statements. The primary depth mechanism is **background color contrast** — white cards floating on Cloud Gray — rather than shadow casting. When shadows appear, they're soft, diffused, and directional (downward), creating the feeling of paper hovering millimeters above a desk.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `xs` | 4px | Small inline elements, tags |
| `sm` | 6px | Buttons, form inputs — the functional interactive radius |
| `md` | 8px | Standard content cards, containers |
| `lg` | 16px | Feature tabs, content panels |
| `xl` | 24px | Buttons, video/image containers — the signature softness |
| `2xl` | 32px | Hero CTAs, status badges, nav buttons |
| `pill` | 9999px | Primary action buttons, tags, avatars |

## Components

The complete component spec lives in YAML.

### Buttons
- **`button-primary`** — Subtly rounded white-on-border default; clean, professional, unheroic.
- **`button-pill`** — Pill-shaped white variant for hero CTAs.
- **`button-dark`** — Black pill for maximum-emphasis primary conversion CTAs.

### Cards
- **`card`** — Standard 24px-padded white card with `{rounded.md}` radius.
- **`card-featured`** — Generous 32px padding with `{rounded.xl}` for featured showcases.

### Inputs
- **`input`** — White surface with `{colors.input-border}` 1px stroke; matches `button-primary` sizing.

### Navigation
- **`nav-bar`** — Sticky horizontal nav. Logo left, links centered, dark pill CTA right.

### Status & Code
- **`status-badge`** — Pill-shaped trust pill (e.g. "All Systems Operational"). Uses `{typography.small}`.
- **`code-block`** — White-surface code panel with JetBrains Mono and `{rounded.md}`.

### Links
- **`link`** — Inline `{colors.link}` text styled as `{typography.body}`.

## Do's and Don'ts

### Do
- Use Cloud Gray (`{colors.background}`) as the page background and Pure White (`{colors.surface}`) for elevated cards
- Keep display headlines at extreme negative letter-spacing (-1.6px to -3px at 64px)
- Use pill-shaped (`{rounded.pill}`) radius for primary CTA buttons
- Reserve black (`{colors.ink}`) for headlines and primary CTAs
- Use Slate Gray (`{colors.text-secondary}`) for secondary text
- Maintain enormous vertical spacing between sections (96px+)
- Use product screenshots as the primary visual content
- Apply Inter at the full weight range (400–900)

### Don't
- Don't introduce decorative colors into the interface chrome — the monochromatic palette is intentional
- Don't use sharp corners (border-radius < 6px) on interactive elements
- Don't reduce section spacing below 64px
- Don't use heavy drop shadows
- Don't mix in additional typefaces — Inter handles everything
- Don't use letter-spacing wider than -0.25px on body text
- Don't use borders heavier than 2px
- Don't add gradients to the interface
- Don't use saturated colors outside of semantic contexts

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <640px | Single column, hamburger nav, stacked cards, hero text scales to ~36px |
| Tablet | 640–1024px | 2-column grids, condensed nav, medium hero text |
| Desktop | >1024px | Full multi-column layout, expanded nav, massive hero (64px) |

*Only one explicit breakpoint detected (640px), suggesting a fluid, container-query or min()/clamp()-based responsive system rather than fixed breakpoint snapping.*

### Touch Targets
- Buttons use generous radius (24–36px) creating large, finger-friendly surfaces
- Navigation links spaced with adequate gap
- Status badge sized for touch (36px radius)
- Minimum recommended: 44x44px

### Collapsing Strategy
- **Navigation**: Full horizontal nav with CTA collapses to hamburger on mobile
- **Feature sections**: Multi-column → stacked single column
- **Hero text**: 64px → ~36px progressive scaling
- **Device previews**: Grid → stacked/carousel
- **Cards**: Side-by-side → vertical stacking
- **Spacing**: Reduces proportionally but maintains generous rhythm

### Image Behavior
- Product screenshots scale proportionally
- Device mockups may simplify or show fewer devices on mobile
- Rounded corners maintained at all sizes
- Lazy loading for below-fold content

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA / Headlines: "Expo Black (`{colors.ink}`)"
- Page Background: "Cloud Gray (`{colors.background}`)"
- Card Surface: "Pure White (`{colors.surface}`)"
- Body Text: "Near Black (`{colors.text-primary}`)"
- Secondary Text: "Slate Gray (`{colors.text-secondary}`)"
- Borders: "Border Lavender (`{colors.border}`)"
- Links: "Link Cobalt (`{colors.link}`)"
- Tertiary Text: "Silver (`{colors.text-tertiary}`)"

### Example Component Prompts
- "Create a hero section on Cloud Gray (`{colors.background}`) with a massive headline at 64px Inter weight 700, line-height 1.10, letter-spacing -3px. Text in Expo Black (`{colors.ink}`). Below, add a subtitle in Slate Gray (`{colors.text-secondary}`) at 18px. Place a black pill-shaped CTA button (`{rounded.pill}` radius) beneath."
- "Design a feature card on Pure White (`{colors.surface}`) with a 1px solid Border Lavender (`{colors.border}`) border and comfortably rounded corners (`{rounded.md}`). Title in Near Black at 20px Inter weight 600, description in Slate Gray at 16px. Add a whisper shadow."
- "Build a navigation bar with Expo logo on the left, text links in Near Black at 14px Inter weight 500, and a black pill CTA button on the right. Background: transparent with blur backdrop."
- "Create a code block using JetBrains Mono at 14px on a Pure White surface with Border Lavender border and `{rounded.md}` radius."
- "Design a status badge pill (`{rounded.pill}`) with a green dot and 'All Systems Operational' text in Inter 12px weight 500. Background: Pure White, border: 1px solid Input Border."

### Iteration Guide
1. Focus on ONE component at a time
2. Reference specific color names — "use Slate Gray (`{colors.text-secondary}`)" not "make it gray"
3. Use radius values deliberately — `{rounded.sm}` for buttons, `{rounded.md}` for cards, `{rounded.xl}` for images, `{rounded.pill}` for pills
4. Describe the "feel" alongside measurements — "enormous breathing room with 96px section spacing"
5. Always specify Inter and the exact weight — weight contrast IS the hierarchy
6. For shadows, specify "whisper shadow" or "standard elevation" from the elevation table
7. Keep the interface monochrome — let product content be the color
