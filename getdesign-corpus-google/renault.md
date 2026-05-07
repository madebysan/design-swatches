---
version: alpha
name: Renault
description: French automotive design at showroom scale — solid black/white canvas, Renault Yellow super-primary CTA, NouvelR with 28-degree radical r, zero-radius buttons, and chessboard light/dark alternation.

colors:
  # Primary
  background: "#FFFFFF"
  surface-dark: "#000000"
  surface-charcoal: "#222222"
  surface-light: "#F2F2F2"

  # Brand
  primary: "#EFDF00"
  primary-soft: "#F8EB4C"

  # Interactive
  accent-blue: "#1883FD"

  # Neutrals & Text
  ink: "#000000"
  ink-inverted: "#FFFFFF"
  text-muted: "#D9D9D6"
  border: "#D1D1D1"

  # Semantic
  success: "#8DC572"
  error: "#BE6464"
  warning: "#F0AD4E"
  info: "#337AB7"

  # Promo gradient overlay (opaque approx)
  overlay-dark: "#000000"  # was rgba(0,0,0,0.6) — flatten for hex compliance

typography:
  hero-title:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: 0px
  section-heading:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: 0px
  card-heading:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: 0px
  sub-heading:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: 0px
  module-title:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 21.92px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0px
  content-title:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: 0px
  ui-heading:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 19.2px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0px
  emphasis:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0px
  body-heading:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.40
    letterSpacing: 0px
  body:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  body-bold:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.57
    letterSpacing: 0px
  button-label:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 14.4px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0.144px
  nav-link:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.50
    letterSpacing: 0px
  caption:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 12.8px
    fontWeight: 400
    lineHeight: 1.10
    letterSpacing: 0px
  small-label:
    fontFamily: "NouvelR, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0px

spacing:
  micro: 1px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  2xl: 24px
  3xl: 32px
  4xl: 40px

rounded:
  none: 0px
  sharp: 2px
  sm: 3px
  md: 4px
  pill: 50px
  full: 9999px

components:
  # Buttons (zero radius signature)
  button-super:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.button-label}"
    rounded: "{rounded.none}"
    padding: 10px 15px
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.button-label}"
    rounded: "{rounded.none}"
    padding: 10px 15px
  button-primary-inverted:
    backgroundColor: "{colors.ink-inverted}"
    textColor: "{colors.ink}"
    typography: "{typography.button-label}"
    rounded: "{rounded.none}"
    padding: 10px 15px
  button-ghost-light:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-label}"
    rounded: "{rounded.none}"
    padding: 10px 15px
  button-ghost-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.button-label}"
    rounded: "{rounded.none}"
    padding: 10px 15px

  # Text link
  text-link:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 0px
  text-link-hover:
    textColor: "{colors.accent-blue}"

  # Cards (PromoCard)
  promo-card-light:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 0px
  promo-card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink-inverted}"
    rounded: "{rounded.none}"
    padding: 0px
  vehicle-card:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 16px

  # Inputs (pill shape — only place pill is allowed)
  search-input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 6px 35px 6px 15px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.accent-blue}"

  # Charcoal surface for footer/dark text-heavy
  surface-charcoal-block:
    backgroundColor: "{colors.surface-charcoal}"
    textColor: "{colors.ink-inverted}"
    rounded: "{rounded.none}"
    padding: 32px

  # Light alt surface
  surface-light-block:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 32px

  # Status text
  text-muted:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-muted}"
    typography: "{typography.caption}"
    padding: 0px
  border-rule:
    backgroundColor: "{colors.border}"
    rounded: "{rounded.none}"
    padding: 0px

  # Semantic text states
  text-success:
    backgroundColor: "{colors.background}"
    textColor: "{colors.success}"
    typography: "{typography.body}"
    padding: 0px
  text-error:
    backgroundColor: "{colors.background}"
    textColor: "{colors.error}"
    typography: "{typography.body}"
    padding: 0px
  text-warning:
    backgroundColor: "{colors.background}"
    textColor: "{colors.warning}"
    typography: "{typography.body}"
    padding: 0px
  text-info:
    backgroundColor: "{colors.background}"
    textColor: "{colors.info}"
    typography: "{typography.body}"
    padding: 0px

  # Soft yellow hover alternate
  button-super-hover:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-label}"
    rounded: "{rounded.none}"
    padding: 10px 15px

  # Overlay (decorative)
  promo-card-overlay:
    backgroundColor: "{colors.overlay-dark}"
    rounded: "{rounded.none}"
    padding: 0px
---

# Renault Design System

## Overview

Renault's website is a disciplined digital showroom that balances French automotive elegance with bold, forward-leaning energy — a departure from the monochromatic austerity of German or Italian luxury brands. The page opens with a full-screen hero that leans on clean solid backgrounds — deep black or pure white — behind dramatically lit vehicle photography, with Renault Yellow (`{colors.primary}`) landing as a single, high-intensity accent on the primary CTA. The expressiveness comes from restraint: confident NouvelR typography, a strict black-and-white CTA framework, zero-radius buttons, and yellow used as a signal rather than an atmosphere. The effect is a showroom that feels engineered rather than theatrical.

The layout follows a card-based editorial rhythm. Below the hero, content is organized into a grid of PromoCards — each a full-bleed photographic panel with a subtle dark gradient overlay at top used purely to keep heading text legible over imagery. These cards alternate between light and dark modes: white editorial panels with black text sit beside black `is-alternative-mode` sections with white text, creating a chessboard-like visual cadence. The grid is generous — large card formats dominate, giving each vehicle or campaign its own visual territory. The lower sections shift to a fully dark canvas (Absolute Black backgrounds) for the E-Tech electric and technology showcases, establishing a deliberate mood shift: electrification lives in darkness, tradition in light.

Typography is unified under NouvelR — a proprietary geometric sans-serif designed by Black[Foundry] exclusively for Renault's rebrand. The typeface features a distinctive "radical r" with a terminal cut at 28 degrees to echo the Renault diamond logo's angles. Available in 6 weights from Light to Extrabold, the site primarily uses Bold (700) for headings and Regular (400) for body. Display headlines run large — 56px/0.95 line-height for hero titles, creating dense, impactful text blocks that sit tight against each other. The font supports Latin, Greek, Cyrillic, Hebrew, Arabic, and Korean, reflecting Renault's global market reach. All text rendering feels precise and engineered, with the geometric proportions lending a sense of modernity that aligns with Renault's electric-first brand positioning.

**Key Characteristics:**
- Full-screen hero carousel with clean solid backgrounds (pure black or pure white) behind dramatically lit vehicle photography
- NouvelR proprietary typeface with 28-degree "radical r" cut matching the diamond logo geometry
- Renault Yellow (`{colors.primary}`) as the super-primary accent — used sparingly for highest-priority CTAs
- Zero border-radius on all buttons — sharp rectangular forms expressing precision engineering
- Card-based editorial grid with full-bleed photography and dark gradient overlays
- Binary black/white CTA system: primary (black bg/white text) and ghost (transparent/white border)
- PromoCard dark-mode alternation creating a chessboard rhythm between light and dark sections
- PrimeReact (21 components) + Element Plus (19 components) powering interactive elements
- Link hover state in Renault Blue (`{colors.accent-blue}`) — the sole chromatic interaction color

## Colors

### Primary
- **Renault Yellow** (`{colors.primary}`): The brand's signature Pantone — a vivid, saturated yellow used for super-primary CTAs and the highest-priority action buttons. Carries the energy of the diamond logo.
- **Absolute Black** (`{colors.surface-dark}`): Primary button background, heading text on light surfaces, and the dominant dark section surface.
- **Pure White** (`{colors.background}`): Primary surface for editorial content, inverted button backgrounds, hero text color, and the dominant light-mode canvas.

### Secondary & Accent
- **Soft Yellow** (`{colors.primary-soft}`): Lighter, warmer variant of Renault Yellow — used for hover/pressed states on yellow CTAs.
- **Renault Blue** (`{colors.accent-blue}`): Link hover color across all link variants.
- **Warm Gray** (`{colors.text-muted}`): Subtle warm neutral used for disabled states, inactive UI elements, and soft borders.

### Surface & Background
- **Pure White** (`{colors.background}`): Page background, light editorial sections, navigation bar, and footer.
- **Absolute Black** (`{colors.surface-dark}`): Hero backgrounds, PromoCard dark-mode sections, and E-Tech showcase areas.
- **Charcoal** (`{colors.surface-charcoal}`): Secondary dark surface for text-heavy dark sections.
- **Pale Silver** (`{colors.surface-light}`): Subtle alternate light surface for section differentiation.

### Neutrals & Text
- **Absolute Black** (`{colors.ink}`): Primary heading and body text on light surfaces — Renault uses true black rather than near-black.
- **Pure White** (`{colors.ink-inverted}`): Primary text on dark surfaces.
- **Warm Gray** (`{colors.text-muted}`): Tertiary text, metadata, and subdued labels.
- **Border Gray** (`{colors.border}`): Input field borders and subtle separators.

### Semantic & Accent
- **Success Green** (`{colors.success}`): Positive status indicators and confirmation messages.
- **Error Rose** (`{colors.error}`): Form validation errors and warning states.
- **Warning Amber** (`{colors.warning}`): Cautionary alerts and attention-requiring states.
- **Info Blue** (`{colors.info}`): Informational callouts and neutral status messaging.

### Gradient System
- **Hero**: No decorative gradients — hero backgrounds are clean solids that let vehicle photography and the yellow CTA do the chromatic work.
- **PromoCard Overlay**: A dark top-of-card overlay applied strictly as a legibility aid for heading text over photography.
- No flat CSS gradients on UI surfaces — depth comes from photographic treatment, the black/white alternation, and the single yellow accent.

## Typography

### Font Family
- **NouvelR**: The sole typeface. A proprietary geometric sans-serif designed by Black[Foundry] for Renault's 2021+ rebrand. Features a distinctive "radical r" with a 28-degree terminal cut matching the diamond logo angle. Available in 6 weights, supports 6 writing systems. Fallback: `sans-serif`.
- **No secondary typeface**: Unlike Ferrari or Lamborghini, Renault uses a single font family for all text — headings, body, buttons, captions, and navigation.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.hero-title}`, `{typography.body}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `hero-title` | NouvelR Bold 56px — full-bleed hero |
| `section-heading` | NouvelR Bold 40px — PromoCard headings |
| `card-heading` | NouvelR Bold 32px — medium-scale cards |
| `sub-heading` | NouvelR Bold 24px — section sub-titles |
| `module-title` | NouvelR Semibold 21.92px — component headings |
| `content-title` | NouvelR Bold 20px — smaller section titles |
| `ui-heading` | NouvelR Semibold 19.2px — card UI headings |
| `emphasis` | NouvelR Bold 18px — emphasized inline text |
| `body-heading` | NouvelR Bold 16px — paragraph-level headings |
| `body` | NouvelR Regular 14px — paragraph content |
| `body-bold` | NouvelR Bold 14px — emphasized body |
| `button-label` | NouvelR Bold 14.4px — primary buttons |
| `nav-link` | NouvelR Bold 13px — navigation, footer |
| `caption` | NouvelR Regular 12.8px — small descriptive |
| `small-label` | NouvelR Bold 12px — labels and tags |

### Principles
- **Single-family discipline**: NouvelR handles everything from 56px hero headlines to small legal captions — the font's geometric precision allows it to scale across this extreme range without losing character.
- **Bold-default headings**: Weight 700 dominates the heading hierarchy. Renault's Bold weight creates a more assertive, energetic reading experience.
- **Ultra-tight display line-heights**: 0.95 line-height on hero and section headings — the lines nearly collide, creating a compressed, punchy typographic texture.
- **28-degree radical r**: The typeface's signature detail — the lowercase "r" terminal is cut at precisely 28 degrees to mirror the Renault diamond logo, embedding brand identity into every word.

## Layout

### Spacing System
Base unit is **8px**. Button padding 10px 15px, consistent across button variants. Section padding `3xl`–`4xl` between major content blocks. Minimum interactive size 46px.

### Grid & Container
- Max width: 1440px (largest defined breakpoint)
- Hero: Full-bleed, edge-to-edge, viewport-height
- PromoCard grid: 2-up and 3-up layouts with mixed card sizes
- Vehicle range: Horizontal scrollable card row or grid
- Footer: Multi-column layout on white background

### Whitespace Philosophy
Renault uses whitespace moderately — more generously than Ferrari but less extremely than Tesla. The card-based layout means content is organized into defined containers rather than floating in void. The visual breathing room comes primarily from large card formats and the full-bleed hero carousel. The alternation between light and dark sections also creates perceived whitespace — the mode switch itself acts as a visual separator.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 (Flat) | No shadow | Default for PromoCards, buttons, most containers |
| Level 1 (Soft) | `rgba(0,0,0,0.2) 0px 4px 8px` | Card hover states, subtle lift |
| Level 2 (Medium) | `rgba(0,0,0,0.2) 0px 0px 18px` | Floating UI elements, dropdowns |
| Level 3 (Layered) | Compound shadow (tight dark + wider purple-tinted) | Elevated cards and modals |
| Level 4 (Deep) | `rgba(0,0,0,0.15) 0px 40px 80px` | Large floating panels, configurator overlays |
| Level 5 (Directional) | `rgba(0,0,0,0.2) 5px 5px 8px` | Offset directional shadow |
| Level 6 (Ambient) | Warm gray glow | Highlighted elements |

**Shadow Philosophy**: Renault uses a richer shadow system than Ferrari or Tesla — seven distinct shadow tokens reflecting a more layered, dimensional interface. The shadows progress from subtle 4px hover lifts to dramatic 80px deep panels.

### Decorative Depth
- **Hero photography**: The primary decorative depth element — dramatically lit vehicle renders on solid black or white create atmosphere without chromatic gradients.
- **PromoCard overlays**: Top-fading dark overlay creates depth within cards through transparency, used as a legibility tool rather than an aesthetic one.
- **No blur effects** on UI elements.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | All buttons, PromoCards, most containers — the zero-radius default |
| `sharp` | 2px | Small UI elements (region controls) |
| `sm` | 3px | Content panels |
| `md` | 4px | Labels and tag elements |
| `pill` | 50px | Search/input fields |
| `full` | 9999px | Reserved circular elements |

The system is binary: zero-radius rectangles for actions and surfaces, pill (50px) reserved for search inputs and filter chips. There are no mid-range radii on action elements.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly rather than reconstructing them.

### Buttons
Renault's buttons are sharp-edged rectangles with zero border-radius — the industrial precision of a pressed metal body panel.

- **`button-super`** — The highest-emphasis CTA. Renault Yellow background, black text. Used for primary conversion actions (configure, buy now).
- **`button-primary`** — The default action button. Black background, white text on light surfaces.
- **`button-primary-inverted`** — White fill, black text on dark backgrounds.
- **`button-ghost-light`** — Transparent on white with black border and text.
- **`button-ghost-dark`** — Transparent on black with white border and text.
- **`button-super-hover`** — Soft Yellow hover state.

### Text Links
- **`text-link`** — Inline navigation, no border, no background.
- **`text-link-hover`** — Color shifts to Renault Blue (`{colors.accent-blue}`).

### Cards & Containers
- **`promo-card-light`** — Editorial content card with full-bleed photography and dark overlay at top.
- **`promo-card-dark`** — Cinematic card on Absolute Black with white text and inverted CTAs.
- **`vehicle-card`** — Vehicle showcase, transparent background, vehicle image above name/price/spec.

### Inputs & Forms
- **`search-input`** — Pill-shaped (50px radius) with white background, 1px border. The unusual deviation from the zero-radius button system.

### Navigation
- **`nav-bar`** — White background, no shadow at rest. Renault diamond logo centered/left.
- **`nav-link`** — NouvelR 13px weight 700, black text. Hover: Renault Blue.

### Surfaces
- **`surface-charcoal-block`** — Dark text-heavy block for footer sub-regions.
- **`surface-light-block`** — Subtle alternate light section surface.

### Status / Semantic
- **`text-success`** / **`text-error`** / **`text-warning`** / **`text-info`** — Semantic text colors reserved for form states only, not decoration.

## Do's and Don'ts

### Do
- Use Renault Yellow (`{colors.primary}`) exclusively for super-primary CTAs — it carries the full weight of the diamond logo's identity
- Maintain zero border-radius on all buttons — sharp edges are non-negotiable
- Use NouvelR Bold (700) as the default heading weight
- Apply the dark gradient overlay on PromoCards to ensure text legibility over photography
- Keep hero line-heights ultra-tight (0.95) for display text
- Alternate between black and white sections to create the signature chessboard rhythm
- Use `{colors.accent-blue}` consistently for all link hover states
- Set minimum interactive size at 46×46px for all buttons
- Reserve pill-shaped radius (50px) exclusively for search inputs and filter elements — never for buttons
- Use the PromoCard gradient overlay on every card that has text over photography

### Don't
- Don't apply Renault Yellow as a background color for sections — it's a CTA signal, not an atmosphere color
- Don't add border-radius to buttons — the zero-radius rectangle is a core brand marker
- Don't use any typeface besides NouvelR — the single-family discipline is a brand pillar
- Don't mix multiple chromatic accent colors in a single section — the palette is monochrome-plus-yellow
- Don't soften heading weights to 400 or 500 — NouvelR Bold is the brand voice
- Don't add decorative borders to PromoCards or content containers — separation comes from background color alternation
- Don't use the semantic colors (Success Green, Error Rose) for decorative purposes — they're reserved for form states
- Don't apply the 56px hero size to anything below the fold
- Don't create rounded-pill buttons — pill shapes are reserved for inputs
- Don't use flat CSS gradients on UI surfaces — the only acceptable gradient is the top-of-card dark overlay

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile Small | ≤425px | Single-column, full-width cards, hero text scales to ~32px, stacked CTAs, hamburger nav |
| Mobile | 426–640px | Single-column, slightly larger cards, hero text at 32–40px |
| Tablet Small | 641–768px | 2-column PromoCard grid begins, hero maintains full-width |
| Tablet | 769–896px | Full 2-column layout, vehicle range shows 2–3 cards |
| Desktop Small | 897–1024px | Navigation fully expanded, hero at 56px, 2-up card grid |
| Desktop | 1025–1280px | Full layout, 3-up card grid, generous whitespace |
| Large Desktop | 1281–1440px | Maximum content width, centered container |

### Touch Targets
- All buttons: minimum 46×46px — exceeds WCAG AAA 44×44px requirement
- Search input pill: adequate touch target with 50px border-radius
- Navigation links: NouvelR 13px with adequate spacing between items
- Carousel navigation: large arrow targets at viewport edges

### Collapsing Strategy
- **Navigation**: Full horizontal nav collapses to Renault diamond logo + hamburger menu on mobile
- **Hero carousel**: Full-width at all breakpoints, headline scales from 56px (desktop) to ~32px (mobile)
- **PromoCard grid**: 3-up → 2-up → single-column as viewport narrows
- **Vehicle range**: Horizontal scroll maintained at all sizes
- **CTA pairs**: Side-by-side buttons stack vertically on mobile
- **Footer**: Multi-column collapses to single-column accordion on mobile

### Image Behavior
- Hero images: full-bleed at all breakpoints with `object-fit: cover`
- PromoCard images: responsive within card containers, gradient overlay scales proportionally
- Vehicle images: transparent-background renders scale proportionally within grid cells
- Art direction: mobile may crop to tighter vehicle views, reducing environmental context

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA (Super): Renault Yellow (`{colors.primary}`)
- Primary CTA (Default): Absolute Black (`{colors.ink}`)
- Background Light: Pure White (`{colors.background}`)
- Background Dark: Absolute Black (`{colors.surface-dark}`)
- Secondary Dark: Charcoal (`{colors.surface-charcoal}`)
- Heading text (light bg): Absolute Black (`{colors.ink}`)
- Body text: Absolute Black (`{colors.ink}`)
- Link Hover: Renault Blue (`{colors.accent-blue}`)
- Border: Pale Silver (`{colors.surface-light}`)
- Semantic Error: Error Rose (`{colors.error}`)

### Example Component Prompts
- "Create a hero section with a solid Absolute Black background, a centered vehicle image, a NouvelR Bold headline at 56px with 0.95 line-height in white, a Renault Yellow super-primary button 'Configure', and a Ghost button (transparent bg, white border, white text, 0px radius) 'Learn More'"
- "Design a PromoCard with a full-bleed photography background, a dark gradient overlay (top to transparent at 40%), a NouvelR Bold 40px white heading, a 14px body text line in white, and a Primary inverted button (white bg, black text, 0px radius, 10px 15px padding)"
- "Build a vehicle range grid with 3 columns on white background, each card showing a transparent-background car render above a NouvelR Bold 24px model name in black, a 14px price caption, and a ghost button (black border, black text, 0px radius) labeled 'Configure'"
- "Create a dark E-Tech section on Absolute Black with a NouvelR Bold 40px white heading 'E-Tech electric powertrain', a 14px subtitle in white, and a Renault Yellow super-primary button with black text, 0px radius, and 10px 15px padding"
- "Design a search input as a pill-shaped field (50px border-radius) with white background, 1px solid `{colors.border}` border, NouvelR 12.8px text, 6px 35px 6px 15px padding, and a search icon positioned inside the right padding area"

### Iteration Guide
1. Focus on ONE component at a time — Renault's system has clear component boundaries (PromoCard, VehicleRangeCard, CTA variants)
2. Reference specific color names and hex codes — the palette is small but each color has a precise function
3. Use natural language descriptions — "sharp zero-radius rectangle" conveys intent better than "border-radius: 0"
4. Describe the desired "feel" alongside specific measurements — "assertive automotive energy" communicates the NouvelR Bold heading personality better than "font-weight: 700"
5. Always check whether a section should be light or dark — the chessboard alternation is a core pattern
6. Reserve Renault Yellow for ONE button per screen — if yellow appears in more than one CTA, the hierarchy collapses
