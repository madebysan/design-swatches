---
version: alpha
name: Runway
description: Cinematic film-production design — full-bleed photography as primary UI, single typeface (abcNormal) for everything, cool-gray dark palette, zero shadows, and uppercase navigation labels.

colors:
  # Primary
  background-dark: "#000000"
  background-deep: "#030303"
  surface-dark: "#1a1a1a"
  background-light: "#ffffff"
  surface-near-white: "#fefefe"
  surface-cool-cloud: "#e9ecf2"

  # Text / Ink
  ink: "#ffffff"
  ink-light-bg: "#404040"
  ink-near-charcoal: "#3f3f3f"

  # Neutrals
  text-cool-slate: "#767d88"
  text-mid-slate: "#7d848e"
  text-muted: "#a7a7a7"
  text-cool-silver: "#c9ccd1"
  text-light-silver: "#d0d4d4"
  text-tailwind-gray: "#6b7280"
  text-dark-link: "#0c0c0c"
  text-footer: "#999999"

  # Borders
  border-dark: "#27272a"

typography:
  display-hero:
    fontFamily: "abcNormal, abcNormal Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -1.2px
  section-heading:
    fontFamily: "abcNormal, abcNormal Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -1px
  sub-heading:
    fontFamily: "abcNormal, abcNormal Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -0.9px
  card-title:
    fontFamily: "abcNormal, abcNormal Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: 0px
  feature-title:
    fontFamily: "abcNormal, abcNormal Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: 0px
  body:
    fontFamily: "abcNormal, abcNormal Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.16px
  body-emphasis:
    fontFamily: "abcNormal, abcNormal Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0px
  caption:
    fontFamily: "abcNormal, abcNormal Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  caption-uppercase:
    fontFamily: "abcNormal, abcNormal Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.35px
  small:
    fontFamily: "abcNormal, abcNormal Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.16px
  micro:
    fontFamily: "abcNormal, abcNormal Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 450
    lineHeight: 1.30
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 28px
  4xl: 32px
  5xl: 48px
  6xl: 64px
  7xl: 78px

rounded:
  sharp: 4px
  sm: 6px
  md: 8px
  lg: 16px

components:
  # Buttons
  button-primary:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sharp}"
    padding: 12px 20px
  button-secondary:
    backgroundColor: "{colors.background-light}"
    textColor: "{colors.ink-light-bg}"
    typography: "{typography.caption}"
    rounded: "{rounded.sharp}"
    padding: 12px 20px

  # Cards
  card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  card-deep:
    backgroundColor: "{colors.background-deep}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  card-light:
    backgroundColor: "{colors.surface-near-white}"
    textColor: "{colors.ink-light-bg}"
    rounded: "{rounded.md}"
    padding: 24px
  card-alert:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Surfaces
  hero-dark:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.display-hero}"
    padding: 48px
  section-light:
    backgroundColor: "{colors.surface-cool-cloud}"
    textColor: "{colors.ink-light-bg}"
    rounded: "{rounded.md}"
    padding: 48px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 16px 24px
  nav-link:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 8px 12px

  # Labels
  label-uppercase:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.text-cool-slate}"
    typography: "{typography.caption-uppercase}"
    padding: 0px
  label-micro:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.text-cool-slate}"
    typography: "{typography.micro}"
    padding: 0px

  # Text variants
  text-secondary:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.text-cool-slate}"
    typography: "{typography.body}"
  text-tertiary:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.text-mid-slate}"
    typography: "{typography.body}"
  text-muted:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.text-muted}"
    typography: "{typography.small}"
  text-charcoal:
    backgroundColor: "{colors.background-light}"
    textColor: "{colors.ink-near-charcoal}"
    typography: "{typography.body}"
  text-tailwind:
    backgroundColor: "{colors.background-light}"
    textColor: "{colors.text-tailwind-gray}"
    typography: "{typography.caption}"
  text-link-dark:
    backgroundColor: "{colors.background-light}"
    textColor: "{colors.text-dark-link}"
    typography: "{typography.body-emphasis}"
  text-footer:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.text-footer}"
    typography: "{typography.small}"

  # Borders
  border-rule:
    backgroundColor: "{colors.border-dark}"
    rounded: "{rounded.sharp}"
    padding: 0px
  border-light-rule:
    backgroundColor: "{colors.text-cool-silver}"
    rounded: "{rounded.sharp}"
    padding: 0px
  border-light-rule-alt:
    backgroundColor: "{colors.text-light-silver}"
    rounded: "{rounded.sharp}"
    padding: 0px
---

# Runway Design System

## Overview

Runway's interface is a cinematic reel brought to life as a website — a dark, editorial, film-production-grade design where full-bleed photography and video ARE the primary UI elements. This is not a typical tech product page; it's a visual manifesto for AI-powered creativity. Every section feels like a frame from a film: dramatic lighting, sweeping landscapes, and intimate human moments captured in high-quality imagery that dominates the viewport.

The design language is built on a single typeface — abcNormal — a clean, geometric sans-serif that handles everything from 48px display headlines to 11px uppercase labels. This single-font commitment creates an extreme typographic uniformity that lets the visual content speak louder than the text. Headlines use tight line-heights (1.0) with negative letter-spacing (-0.9px to -1.2px), creating compressed text blocks that feel like film titles rather than marketing copy.

What makes Runway distinctive is its complete commitment to visual content as design. Rather than illustrating features with icons or diagrams, Runway shows actual AI-generated and AI-enhanced imagery — cars driving through cinematic landscapes, artistic portraits, architectural renders. The interface itself retreats into near-invisibility: minimal borders, zero shadows, subtle cool-gray text, and a dark palette that puts maximum focus on the photography.

**Key Characteristics:**
- Cinematic full-bleed photography and video as primary UI elements
- Single typeface system: abcNormal for everything from display to micro labels
- Dark-dominant palette with cool-toned neutrals (`{colors.text-cool-slate}`, `{colors.text-mid-slate}`)
- Zero shadows, minimal borders — the interface is intentionally invisible
- Tight display typography (line-height 1.0) with negative tracking (-0.9px to -1.2px)
- Uppercase labels with positive letter-spacing for navigational structure
- Weight 450 (unusual intermediate) for small uppercase text — precision craft
- Editorial magazine layout with mixed-size image grids

## Colors

### Primary
- **Runway Black** (`{colors.background-dark}`): The primary page background and maximum-emphasis text.
- **Deep Black** (`{colors.background-deep}`): A near-imperceptible variant for layered dark surfaces.
- **Dark Surface** (`{colors.surface-dark}`): Card backgrounds and elevated dark containers.
- **Pure White** (`{colors.background-light}`): Primary text on dark surfaces and light-section backgrounds.

### Surface & Background
- **Near White** (`{colors.surface-near-white}`): The lightest surface — barely distinguishable from pure white.
- **Cool Cloud** (`{colors.surface-cool-cloud}`): Light section backgrounds with a cool blue-gray tint.
- **Border Dark** (`{colors.border-dark}`): The single dark-mode border color — barely visible containment.

### Neutrals & Text
- **Charcoal** (`{colors.ink-light-bg}`): Primary body text on light surfaces and secondary text.
- **Near Charcoal** (`{colors.ink-near-charcoal}`): Slightly lighter variant for dark-section secondary text.
- **Cool Slate** (`{colors.text-cool-slate}`): Secondary body text — a distinctly blue-gray cool neutral.
- **Mid Slate** (`{colors.text-mid-slate}`): Tertiary text, metadata descriptions.
- **Muted Gray** (`{colors.text-muted}`): De-emphasized content, timestamps.
- **Cool Silver** (`{colors.text-cool-silver}`): Light borders and dividers.
- **Light Silver** (`{colors.text-light-silver}`): The lightest border/divider variant.
- **Tailwind Gray** (`{colors.text-tailwind-gray}`): Standard Tailwind neutral for supplementary text.
- **Dark Link** (`{colors.text-dark-link}`): Darkest link text — nearly black.
- **Footer Gray** (`{colors.text-footer}`): Footer links and deeply muted content.

### Gradient System
- **None in the interface.** Visual richness comes entirely from photographic content — AI-generated and enhanced imagery provides all the color and gradient the design needs. The interface itself is intentionally colorless.

## Typography

### Font Family
- **Universal**: `abcNormal`, with fallback: `abcNormal Fallback`.

*Note: abcNormal is a custom geometric sans-serif. For external implementations, Inter or DM Sans serve as close substitutes.*

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | 48px abcNormal — film-title presence |
| `section-heading` | 40px — feature section titles |
| `sub-heading` | 36px — secondary section markers |
| `card-title` | 24px — article and card headings |
| `feature-title` | 20px — small headings |
| `body` | 16px — standard body, nav links |
| `body-emphasis` | 16px weight 600 — emphasized text |
| `caption` | 14px medium — metadata |
| `caption-uppercase` | 14px weight 600 uppercase with tracking — navigational signposts |
| `small` | 13px — compact descriptions |
| `micro` | 11px weight 450 — uppercase tags, tiny labels (precision intermediate) |

### Principles
- **One typeface, complete expression**: abcNormal handles every text role. The design achieves variety through size, weight, case, and letter-spacing rather than font-family switching.
- **Tight everywhere**: Nearly every size uses line-height 1.0–1.30 — even body text is relatively compressed.
- **Weight 450 — the precision detail**: Some small uppercase labels use weight 450, an uncommon intermediate between regular (400) and medium (500). Micro-craft signals typographic sophistication.
- **Negative tracking as default**: Even body text uses -0.16px to -0.26px letter-spacing.
- **Uppercase as structure**: Labels at 14px and 11px use `text-transform: uppercase` with positive letter-spacing (0.35px) to create navigational signposts that contrast with the tight lowercase text.

## Layout

### Spacing System
Base unit is **8px**. Section vertical spacing generous (48–78px). Component gaps 16–24px.

### Grid & Container
- Max container width: up to 1600px (cinema-wide)
- Hero: full-viewport, edge-to-edge
- Content sections: centered with generous margins
- Image grids: asymmetric, magazine-style mixed sizes
- Footer: full-width dark section

### Whitespace Philosophy
- **Cinema-grade breathing**: Large vertical gaps between sections create a scrolling experience that feels like watching scenes change.
- **Images replace whitespace**: Where other sites use empty space, Runway fills it with photography. The visual content IS the breathing room.
- **Editorial grid asymmetry**: The image grid uses intentionally varied sizes — large hero images paired with smaller supporting images, creating visual rhythm.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Everything — the dominant state |
| Bordered (Level 1) | `1px solid {colors.border-dark}` | Alert containers only |
| Dark Section (Level 2) | Dark bg with light text | Hero, features, footer |
| Light Section (Level 3) | White/Cool Cloud bg with dark text | Content sections, research |

**Shadow Philosophy**: Runway uses **zero shadows**. This is a film-production design decision — in cinema, depth comes from lighting, focus, and composition, not drop shadows. The interface mirrors this philosophy: depth is communicated through dark/light section alternation, photographic depth-of-field, and overlay transparency — never through CSS box-shadow.

## Shapes

| Token | Value | Use |
|---|---|---|
| `sharp` | 4px | Buttons, small interactive elements |
| `sm` | 6px | Links, small containers |
| `md` | 8px | Standard containers, image cards |
| `lg` | 16px | Alert-style containers, featured elements |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly rather than reconstructing them.

### Buttons
- **`button-primary`** — Dark surface with white text, 4px radius, 14px weight 600.
- **`button-secondary`** — White surface with charcoal text on light sections.
- The button design is extremely restrained — no heavy fills or borders.

### Cards & Containers
- **`card-dark`** / **`card-deep`** — Dark surfaces with barely-visible 1px border, 8px radius.
- **`card-light`** — Near-white surface for light-section content.
- **`card-alert`** — 16px radius for alert-style containers.
- Cards are primarily photographic — the image IS the card.

### Surfaces
- **`hero-dark`** — Full-viewport image or video with text overlay. The image is always cinematic quality.
- **`section-light`** — Cool Cloud background for light editorial sections.

### Navigation
- **`nav-bar`** — Minimal horizontal nav, transparent over hero content.
- **`nav-link`** — abcNormal at 16px, weight 400–600. Hover: text shifts to white or higher opacity.

### Labels
- **`label-uppercase`** — 14px caption uppercase with 0.35px tracking, Cool Slate text. Navigational signposts.
- **`label-micro`** — 11px weight 450 uppercase for category tags.

### Text Variants
- **`text-secondary`** / **`text-tertiary`** / **`text-muted`** — Cool slate hierarchy for body content on dark surfaces.
- **`text-charcoal`** / **`text-tailwind`** / **`text-link-dark`** — Light-section text variants.
- **`text-footer`** — Footer-specific muted gray.

### Borders
- **`border-rule`** — Dark-mode hairline.
- **`border-light-rule`** / **`border-light-rule-alt`** — Light-section dividers.

### Distinctive Components

**Cinematic Hero** — Full-viewport image or video with text overlay. Headline in 48px abcNormal, white on dark imagery.

**Research Article Cards** — Photographic thumbnails with article titles. Mixed-size grid layout (large feature + smaller supporting).

**Trust Bar** — Company logos in monochrome, horizontal layout with generous spacing.

**Mission Statement** — On a dark background with white text, the emotional close — artistic and philosophical.

## Do's and Don'ts

### Do
- Use full-bleed cinematic photography as the primary visual element
- Use abcNormal for all text — maintain the single-typeface commitment
- Keep display line-heights at 1.0 with negative letter-spacing for film-title density
- Use the cool-gray neutral palette (`{colors.text-cool-slate}`, `{colors.text-mid-slate}`) for secondary text
- Maintain zero shadows — depth comes from photography and section backgrounds
- Use uppercase with letter-spacing for navigational labels (14px, 0.35px spacing)
- Apply small border-radius (4–8px) — the design is NOT pill-shaped
- Let visual content (photos, videos) dominate — the UI should be invisible
- Use weight 450 for micro labels — the precision matters

### Don't
- Don't add decorative colors to the interface — the only color comes from photography
- Don't use heavy borders or shadows — the interface must be nearly invisible
- Don't use pill-shaped radius — Runway's geometry is subtly rounded, not circular
- Don't use bold (700+) weight — 400–600 is the full range, with 450 as a precision tool
- Don't compete with the visual content — text overlays should be minimal and restrained
- Don't use gradient backgrounds in the interface — gradients exist only in photography
- Don't use more than one typeface — abcNormal handles everything
- Don't use body line-height above 1.50 — the tight, editorial feel is core
- Don't reduce image quality — cinematic photography IS the design

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <640px | Single column, stacked images, reduced hero text |
| Tablet | 640–768px | 2-column image grids begin |
| Small Desktop | 768–1024px | Standard layout |
| Desktop | 1024–1280px | Full layout, expanded hero |
| Large Desktop | 1280–1600px | Maximum cinema-width container |

### Touch Targets
- Navigation links at comfortable 16px
- Article cards serve as large touch targets
- Buttons at 14px weight 600 with adequate padding

### Collapsing Strategy
- **Navigation**: Collapses to hamburger on mobile
- **Hero**: Full-bleed maintained, text scales down
- **Image grids**: Multi-column → 2-column → single column
- **Research articles**: Feature-size cards → stacked full-width
- **Trust logos**: Horizontal scroll or reduced grid

### Image Behavior
- Cinematic images scale proportionally
- Full-bleed hero maintained across all sizes
- Image grids reflow to fewer columns
- Video content maintains aspect ratio

## Agent Prompt Guide

### Quick Color Reference
- Background Dark: Runway Black (`{colors.background-dark}`)
- Background Light: Pure White (`{colors.background-light}`)
- Primary Text Dark: Charcoal (`{colors.ink-light-bg}`)
- Secondary Text: Cool Slate (`{colors.text-cool-slate}`)
- Muted Text: Muted Gray (`{colors.text-muted}`)
- Light Border: Cool Silver (`{colors.text-cool-silver}`)
- Dark Border: Border Dark (`{colors.border-dark}`)
- Card Surface: Dark Surface (`{colors.surface-dark}`)

### Example Component Prompts
- "Create a cinematic hero section: full-bleed dark background with a cinematic image overlay. Headline at 48px abcNormal weight 400, line-height 1.0, letter-spacing -1.2px in white. Minimal text below in Cool Slate (`{colors.text-cool-slate}`) at 16px."
- "Design a research article grid: one large card (50% width) with a cinematic image and 24px title, next to two smaller cards stacked. All images with 8px border-radius. Titles in white (dark bg) or Charcoal (`{colors.ink-light-bg}`, light bg)."
- "Build a section label: 14px abcNormal weight 500, uppercase, letter-spacing 0.35px in Cool Slate (`{colors.text-cool-slate}`). No border, no background."
- "Create a trust bar: company logos in monochrome, horizontal layout with generous spacing. On dark background with white/gray logo treatments."
- "Design a mission statement section: Runway Black background, white text at 36px abcNormal, line-height 1.0, letter-spacing -0.9px. Centered, with generous vertical padding."

### Iteration Guide
1. Visual content first — always include cinematic photography
2. Use abcNormal for everything — specify size and weight, never change the font
3. Keep the interface invisible — no heavy borders, no shadows, no bright colors
4. Use the cool slate grays (`{colors.text-cool-slate}`, `{colors.text-mid-slate}`) for secondary text — not warm grays
5. Uppercase labels need letter-spacing (0.35px) — never tight uppercase
6. Dark sections should be truly dark (`{colors.background-dark}` or `{colors.surface-dark}`) — no medium grays as surfaces
