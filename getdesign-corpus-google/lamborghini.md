---
version: alpha
name: Lamborghini
description: Cathedral of darkness — true black canvas, Lamborghini Gold as the singular accent, custom LamboType uppercase at extreme scales, sharp 0px corners, and depth via surface-color layering.

colors:
  # Base
  background: "#000000"
  surface: "#202020"
  surface-deep: "#181818"
  ink: "#ffffff"
  on-primary: "#000000"

  # Brand — Lamborghini Gold
  primary: "#ffc000"
  primary-hover: "#917300"
  primary-light: "#ffce3e"

  # Accent
  cyan: "#29abe2"
  link-blue: "#3860be"
  teal: "#1eaedb"

  # Light surfaces (rare, white-mode sections)
  surface-light: "#f8f8f8"
  surface-mist: "#e6e6e6"

  # Neutrals (achromatic gray scale)
  smoke: "#f5f5f5"
  graphite: "#494949"
  ash: "#7d7d7d"
  steel: "#969696"
  slate: "#666666"
  iron: "#555555"
  shadow-gray: "#313131"

  # Borders / overlay (opaque approximations)
  overlay-dark: "#000000"  # rgba(0,0,0,0.7) flattens to near-black on dark
  border-faint: "#333333"  # was rgba(0,0,0,0.5) on dark — opaque approx

typography:
  hero-display:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 120px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: 0px
  display-2:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 80px
    fontWeight: 400
    lineHeight: 1.13
    letterSpacing: 0px
  section-title:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 54px
    fontWeight: 400
    lineHeight: 1.19
    letterSpacing: 0px
  sub-section:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0px
  feature-heading:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 27px
    fontWeight: 400
    lineHeight: 1.37
    letterSpacing: 0px
  card-title:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 0px
  body-large:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0px
  body:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button-large:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button-standard:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0.2px
  caption:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: -0.42px
  label:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.83
    letterSpacing: 0.96px
  micro:
    fontFamily: "LamboType, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0.225px

spacing:
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 40px
  4xl: 48px
  5xl: 56px

rounded:
  none: 0px
  sm: 1px
  micro: 2px
  toggle: 20px

components:
  # Gold Accent CTA — primary action
  button-gold:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-large}"
    rounded: "{rounded.none}"
    padding: 24px 24px
  button-gold-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"

  # Transparent ghost — secondary on dark
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-standard}"
    rounded: "{rounded.none}"
    padding: 16px 16px
  button-ghost-hover:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.ink}"

  # White filled — light-mode CTA
  button-white:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    typography: "{typography.button-large}"
    rounded: "{rounded.none}"
    padding: 16px 24px

  # Black filled — inverted CTA on light
  button-black:
    backgroundColor: "{colors.background}"
    textColor: "{colors.surface}"
    typography: "{typography.button-large}"
    rounded: "{rounded.none}"
    padding: 16px 24px

  # Gray neutral — subtle action
  button-gray:
    backgroundColor: "{colors.steel}"
    textColor: "{colors.surface}"
    typography: "{typography.button-standard}"
    rounded: "{rounded.none}"
    padding: 12px 16px

  # Card / container on charcoal
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
    padding: 32px

  # Card on absolute black
  card-black:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.none}"
    padding: 32px

  # Switch — the sole rounded element
  switch:
    backgroundColor: "{colors.surface-mist}"
    rounded: "{rounded.toggle}"
    size: 40px

  # Badge / tag
  badge:
    backgroundColor: "{colors.steel}"
    textColor: "{colors.ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.micro}"
    padding: 8px 8px

  # Navigation bar — transparent over black
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-standard}"
    padding: 16px 24px
---

# Lamborghini Design System

## Overview

Lamborghini's website is a cathedral of darkness — a digital stage where jet-black surfaces stretch infinitely and every element emerges from the void like a machine under a spotlight. The page is almost entirely black. Not dark gray, not near-black — true, uncompromising black (`{colors.background}`) that saturates the viewport and refuses to yield. Into this abyss, white type and Lamborghini Gold (`{colors.primary}`) are deployed with surgical precision, creating a visual language that feels like walking through a nighttime motorsport event where every surface absorbs light except the things that matter.

The hero is a full-viewport video — dark, cinematic, immersive — showing event footage or vehicle reveals with the Lamborghini bull logo floating ethereally above. The navigation is minimal: a centered bull logo, a "MENU" hamburger on the left, and search/bookmark icons on the right, all rendered in white against the black canvas. There are no borders, no visible nav containers, no background color on the header — just white marks floating in darkness. The overall mood is nocturnal luxury: exclusive, theatrical, and deliberately intimidating.

Typography is the voice of this darkness. LamboType — a custom Neo-Grotesk typeface created by Character Type and design agency Strichpunkt — is used for everything from 120px uppercase display headlines to 10px micro labels. Its distinctive 12° angled terminals are inspired by the aerodynamic lines of Lamborghini's super sports cars, and its proportions range from Normal to Ultracompressed width. Headlines SHOUT in uppercase at enormous scales with tight line-heights (0.92 at 120px), creating dense blocks of text that feel stamped from steel. The typeface carries hexagonal geometric DNA — constructed from hexagons, three-armed stars, and circles — that echoes throughout the interface.

**Key Characteristics:**
- True black (`{colors.background}`) dominant surfaces with white and gold as the only relief colors
- LamboType custom Neo-Grotesk font with 12° angled terminals
- Lamborghini Gold (`{colors.primary}`) as the sole accent — used exclusively for primary CTAs
- All-uppercase display typography at extreme scales (120px, 80px, 54px) with tight line-heights
- Full-viewport video heroes with cinematic event/vehicle content
- Zero border-radius on buttons — sharp, angular, uncompromising rectangles
- Hexagonal motifs in UI elements echoing brand geometry
- Bootstrap grid system + Element Plus/UI 68 components underneath
- Transparent ghost buttons with white borders as the secondary CTA pattern

## Colors

### Primary
- **Lamborghini Gold** (`{colors.primary}`): The signature accent — used exclusively for primary action buttons. The only chromatic color in the entire interface.
- **Pure White** (`{colors.ink}`): Primary text on dark surfaces, logo rendering, nav elements.

### Secondary & Accent
- **Dark Gold** (`{colors.primary-hover}`): Hover/pressed state for gold buttons
- **Gold Text** (`{colors.primary-light}`): Inline text accents and highlighted labels
- **Cyan Pulse** (`{colors.cyan}`): Informational accent and interactive element highlight
- **Link Blue** (`{colors.link-blue}`): Link hover states across all text colors

### Surface
- **Absolute Black** (`{colors.background}`): The dominant surface
- **Charcoal** (`{colors.surface}`): Elevated dark surface — primary "dark gray" for cards, panels
- **Dark Iron** (`{colors.surface-deep}`): Subtle surface variant — barely distinguishable from black
- **Near White** (`{colors.surface-light}`): Rare light surface for white-mode sections
- **Mist** (`{colors.surface-mist}`): Light gray for secondary light-mode containers

### Neutrals & Text
- **Pure White** (`{colors.ink}`): Primary text on dark backgrounds
- **Smoke** (`{colors.smoke}`): Secondary text on dark
- **Graphite** (`{colors.graphite}`): Dark gray text on light surfaces
- **Ash** (`{colors.ash}`): Mid-range gray for muted text
- **Steel** (`{colors.steel}`): Lighter gray for disabled text
- **Slate** (`{colors.slate}`), **Iron** (`{colors.iron}`), **Shadow** (`{colors.shadow-gray}`): mid/dark variants

### Gradient System
No explicit gradients in the color palette — the dark-to-light progression is achieved through surface layering: `{colors.background}` → `{colors.surface-deep}` → `{colors.surface}` → `{colors.graphite}` → `{colors.ash}`.

## Typography

### Font Family
- **Display & UI**: `LamboType`, Roboto, Helvetica Neue, Arial — custom Neo-Grotesk for Lamborghini's 2024 brand refresh. Available in widths from Normal to Ultracompressed and weights from Light (300) to Black. Features 12° angled terminals inspired by aerodynamic car geometry.
- **Fallback/UI**: `Open Sans` for some button/form contexts as system fallback
- **No italic variants** — the brand voice is always upright

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens (`{typography.hero-display}`, `{typography.body}`) directly.

| Token | Use |
|---|---|
| `hero-display` | 120px uppercase — maximum impact |
| `display-2` | 80px uppercase — major section titles |
| `section-title` | 54px uppercase |
| `sub-section` | 40px uppercase |
| `feature-heading` | 27px uppercase |
| `card-title` | 24px |
| `body-large` | 18px primary body |
| `body` | 16px standard body |
| `button-large` | 16px gold CTA buttons |
| `button-standard` | 14px ghost button labels |
| `caption` | 14px uppercase with negative tracking |
| `label` | 12px uppercase badge/micro label |
| `micro` | 10px uppercase smallest text |

### Principles
- **ALL-CAPS is the default voice** for display and feature headings — a shouting, commanding tone matching the brand's aggression.
- **Extreme scale range**: from 120px heroes to 10px micro labels — a 12:1 ratio.
- **Tight line-heights at scale**: 0.92–1.19 at display sizes, creating dense compressed blocks.
- **Weight 400 dominates** — the typeface is so distinctive it doesn't need weight variation.
- **Negative tracking on captions** (-0.42px) creates a compressed, technical aesthetic.
- **Single typeface discipline**: LamboType handles everything.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is **8px**, with the scale running from `xs` (2px) through `5xl` (56px).

### Grid & Container
- **Framework**: Bootstrap grid (container + row + col)
- **Max width**: 1440px (largest breakpoint)
- **Columns**: Standard 12-column Bootstrap grid
- **Full-bleed**: Hero sections break out to fill viewport edge-to-edge

### Whitespace Philosophy
Lamborghini uses darkness as whitespace. The generous black expanses between content blocks serve the same function as white space in a light design — creating breathing room that elevates each element to the status of exhibit. A model name floating in the middle of a black viewport has the same visual weight as a gallery piece on a white wall. The absence of color IS the design.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 (Abyss) | `{colors.background}` flat | Page background, deepest layer |
| Level 1 (Surface) | `{colors.surface-deep}` or `{colors.surface}` | Cards, elevated sections |
| Level 2 (Overlay) | `{colors.overlay-dark}` at high opacity | Modal backdrops, video dimming |
| Level 3 (Fog) | `{colors.border-faint}` | Lighter overlays, hover states |

### Shadow Philosophy
Lamborghini achieves depth through surface color layering rather than shadows. On a black canvas, traditional drop shadows are invisible — instead, the system creates elevation by shifting from absolute black to progressively lighter dark grays. This "darkness gradient" approach means that elevated elements are literally lighter than their surroundings, inverting the traditional shadow model.

### Decorative Depth
- Full-bleed video provides atmospheric depth through cinematic lighting
- The hexagonal pause button floats with a thin white outline stroke
- Progress bars at hero section bottoms create a subtle horizon line
- No gradients, glows, or blur effects on UI elements — the photography provides all visual richness

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Default for everything — buttons, cards, containers, images |
| `sm` | 1px | Subtle span elements |
| `micro` | 2px | Badges, close buttons, cookie elements |
| `toggle` | 20px | Toggle switches only — the sole rounded element |

The system is fundamentally rectangular. The 20px toggle radius is the only place rounding appears.

## Components

The complete component spec lives in the `components:` token block above. Reference components directly (`{components.button-gold}`, `{components.card}`).

### Buttons
All buttons use **zero border-radius** — sharp, angular rectangles echoing the aggressive lines of Lamborghini vehicles.

- **`button-gold`** — Lamborghini Gold fill, black text, 24px padding, the primary action.
- **`button-ghost`** — transparent fill, white border, white text — secondary on dark.
- **`button-white`** — white fill, charcoal text — light-mode primary.
- **`button-black`** — black fill, charcoal text — inverted CTA on light.
- **`button-gray`** — steel gray fill — subtle action.

### Cards
- **`card`** — charcoal surface, sharp corners, 32px padding.
- **`card-black`** — pure black variant for deep sections.

### Switch
- **`switch`** — 20px radius, the only rounded element in the system.

### Badge / Tag
- **`badge`** — steel gray fill, white text, 2px micro radius, tiny metallic pill.

### Navigation
- **`nav-bar`** — transparent over absolute black, centered bull logo, "MENU" hamburger left, search + bookmarks right. No visible borders or shadows — elements float in darkness.

## Do's and Don'ts

### Do
- Use absolute black (`{colors.background}`) as the primary background — never dark gray as a substitute
- Apply Lamborghini Gold (`{colors.primary}`) exclusively for primary CTA buttons
- Set all display headings in uppercase with LamboType — the brand voice is always SHOUTING
- Use zero border-radius on buttons and cards — sharp angles are non-negotiable
- Maintain tight line-heights (0.92–1.19) on display type
- Use the transparent ghost button as the secondary CTA on dark backgrounds
- Let full-viewport video/photography carry emotional weight — UI is infrastructure, not decoration
- Reserve hexagonal geometry for UI icons and the video control button
- Use weight 400 (regular) for headlines
- Keep the gray palette achromatic — all neutrals are pure gray

### Don't
- Don't introduce additional accent colors beyond gold — the monochrome-plus-gold system is sacred
- Don't apply border-radius to buttons or cards — curved edges contradict the angular vehicle aesthetic
- Don't use LamboType in italic or decorative styles
- Don't add gradients to buttons or surfaces — depth comes from surface layering
- Don't use light backgrounds as the primary canvas — darkness is the default state
- Don't mix lowercase into display headings
- Don't add hover animations with scale or translate — interactions should be color-only
- Don't use Open Sans for display text — LamboType must handle all visible typography
- Don't apply shadows to elements — on a black canvas, shadows are meaningless

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile Small | <425px | Single column, reduced type scale, stacked buttons |
| Mobile | 425–576px | Single column, hamburger nav, hero text ~40px |
| Tablet Small | 576–768px | 2-column grid begins, padding adjusts |
| Tablet | 768–1024px | 2-column layout, expanded hero, vehicle cards side-by-side |
| Desktop | 1024–1280px | Full navigation, 3+ column grids, display text at 80px |
| Desktop Large | 1280–1440px | Full layout, hero at 120px |
| Wide | >1440px | Content centered, margins expand |

### Touch Targets
- Gold CTA buttons: 48px+ minimum height with 24px padding
- Ghost buttons: 48px+ with 16px padding
- Hamburger menu: large touch target (~48px square)
- Hexagonal pause button: approximately 48px diameter

### Collapsing Strategy
- **Navigation**: Always hamburger-based — no horizontal nav expansion on any breakpoint
- **Hero video**: Maintains full-viewport height across all breakpoints
- **Display type**: Scales from 120px (desktop) → 80px (tablet) → 54px/40px (mobile)
- **Button layout**: Side-by-side on desktop, stacks vertically on mobile
- **Grid columns**: 3-column → 2-column → 1-column progression
- **Section spacing**: Reduces from 56px → 40px → 24px vertical padding

### Image Behavior
- Hero videos use `object-fit: cover` to maintain cinematic framing
- Vehicle images scale within containers with maintained aspect ratios
- Background images darken at edges to maintain text contrast on all viewports

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: "Lamborghini Gold (`{colors.primary}`)"
- Background: "Absolute Black (`{colors.background}`)"
- Surface: "Charcoal (`{colors.surface}`)"
- Heading text: "Pure White (`{colors.ink}`)"
- Body text: "Ash (`{colors.ash}`)"
- Link hover: "Link Blue (`{colors.link-blue}`)"
- Accent: "Cyan Pulse (`{colors.cyan}`)"

### Example Component Prompts
- "Create a hero section with a full-viewport black background, the model name 'TEMERARIO' in LamboType at 120px uppercase weight 400 white text with 0.92 line-height, centered vertically, with a Lamborghini Gold (`{colors.primary}`) 'Discover More' button below — sharp corners, 0px radius, 24px padding, black text"
- "Design a transparent ghost button with 1px solid white border at 50% opacity, white text at 14px uppercase with 0.2px letter-spacing, padding 16px, on a black background — hover state changes to Teal Action (`{colors.teal}`) background"
- "Build a navigation bar with zero visible background on absolute black, a centered bull logo, 'MENU' text label with hamburger icon on the left, and search + bookmark icons on the right — all in white, sticky position"
- "Create a news card grid on charcoal (`{colors.surface}`) background with white headlines at 27px uppercase, body text in `{colors.ash}` at 16px, and a white underlined 'Read More' link that turns `{colors.link-blue}` on hover"
- "Design a section divider using a 1px solid bottom border in `{colors.surface}` on a black canvas — the elevation difference is purely through surface color shift, not shadow"

### Iteration Guide
1. Focus on ONE component at a time — Lamborghini's system is extreme and every element must feel aggressive
2. Reference specific color names AND hex codes — the palette has only about 5 active colors
3. Use natural language descriptions alongside specific measurements
4. Describe the desired "feel" — "floating in total darkness" communicates the black canvas
5. Remember that UPPERCASE IS THE DEFAULT — if text isn't uppercase at display sizes, it probably should be
