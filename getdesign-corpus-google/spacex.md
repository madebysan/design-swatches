---
version: alpha
name: SpaceX
description: Cinematic aerospace exhibition — pure black canvas, full-viewport photography, D-DIN industrial type universally uppercased with positive letter-spacing, single ghost button, zero shadows or containers.

colors:
  # Canvas
  background: "#000000"

  # Spectral white (slight blue-violet tint, not pure)
  ink: "#f0f0fa"
  on-primary: "#f0f0fa"

  # Primary CTA = ghost button surface
  primary: "#181820"  # opaque approx of rgba(240,240,250,0.1) over #000 — Google format requires hex
  primary-border: "#54555f"  # opaque approx of rgba(240,240,250,0.35) over #000 — Google format requires hex

  # Hover white
  ink-hover: "#ffffff"

  # Dark photographic overlay (for text legibility)
  overlay: "#000000"

typography:
  display-hero:
    fontFamily: "D-DIN-Bold, D-DIN, Arial, Verdana, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.96px
  body:
    fontFamily: "D-DIN, Arial, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  nav-link-bold:
    fontFamily: "D-DIN, Arial, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 0.94
    letterSpacing: 1.17px
  nav-link:
    fontFamily: "D-DIN, Arial, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 2.0
    letterSpacing: 0px
  caption-bold:
    fontFamily: "D-DIN, Arial, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 0.94
    letterSpacing: 1.17px
  caption:
    fontFamily: "D-DIN, Arial, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  micro:
    fontFamily: "D-DIN, Arial, Verdana, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 0.94
    letterSpacing: 1px

spacing:
  xxs: 3px
  xs: 5px
  sm: 12px
  md: 15px
  lg: 18px
  xl: 20px
  2xl: 24px
  3xl: 30px

rounded:
  none: 0px
  xs: 4px
  pill: 32px

components:
  # Ghost button — the only interactive element in the system
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.pill}"
    padding: 18px 18px
  button-primary-hover:
    backgroundColor: "{colors.primary-border}"
    textColor: "{colors.ink-hover}"

  # Top navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link-bold}"
    padding: 20px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link-bold}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.ink-hover}"
---

# SpaceX Design System

## Overview

SpaceX's website is a full-screen cinematic experience that treats aerospace engineering like a film — every section is a scene, every photograph is a frame, and the interface disappears entirely behind the imagery. The design is pure black (`{colors.background}`) with photography of rockets, space, and planets occupying 100% of the viewport. Text overlays sit directly on these photographs with no background panels, cards, or containers — just type on image, bold and unapologetic.

The typography system uses D-DIN, an industrial geometric typeface with DIN heritage (the German industrial standard). The defining characteristic is that virtually ALL text is uppercase with positive letter-spacing (`0.96px`–`1.17px`), creating a military/aerospace labeling system where every word feels stenciled onto a spacecraft hull. D-DIN-Bold at 48px with uppercase and `0.96px` tracking for the hero creates headlines that feel like mission briefing titles. Even body text at 16px maintains the uppercase/tracked treatment at smaller scales.

What makes SpaceX distinctive is its radical minimalism: no shadows, no borders (except one ghost button border), no color (only black and a spectral near-white `{colors.ink}`), no cards, no grids. The only visual element is photography + text. The ghost button (`{colors.primary}` background) with 32px radius is the sole interactive element — barely visible, floating over the imagery like a heads-up display. This isn't a design system in the traditional sense — it's a photographic exhibition with a type system and a single button.

**Key Characteristics:**
- Pure black canvas with full-viewport cinematic photography — the interface is invisible
- D-DIN / D-DIN-Bold — industrial DIN-heritage typeface
- Universal uppercase + positive letter-spacing (`0.96px`–`1.17px`) — aerospace stencil aesthetic
- Near-white spectral text (`{colors.ink}`) — not pure white, a slight blue-violet tint
- Zero shadows, zero cards, zero containers — text on image only
- Single ghost button: `{colors.primary}` surface with `{colors.primary-border}` border
- Full-viewport sections — each section is a cinematic "scene"
- No decorative elements — every pixel serves the photography

## Colors

### Primary
- **Space Black** (`{colors.background}`): Page background, the void of space.
- **Spectral White** (`{colors.ink}`): Text color — not pure white, a slight blue-violet tint that mimics starlight.

### Interactive
- **Ghost Surface** (`{colors.primary}`): Button background — opaque approximation of the original 10%-opacity overlay.
- **Ghost Border** (`{colors.primary-border}`): Button border — opaque approximation of the original 35%-opacity spectral border.
- **Hover White** (`{colors.ink-hover}`): Link hover state — full white.

### Gradient
- **Dark Overlay** (`{colors.overlay}`): Gradient overlay applied at partial opacity in CSS over photographs to ensure text legibility (the canvas color itself is reused for the overlay tint).

## Typography

### Font Family
- **Display**: `D-DIN-Bold` — bold industrial geometric
- **Body / UI**: `D-DIN`, fallback `Arial, Verdana`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`).

| Token | Use |
|---|---|
| `display-hero` | Hero mission-briefing headline (48px uppercase) |
| `body` | Standard reading text (16px) |
| `nav-link-bold` | Bold uppercase nav (13px) |
| `nav-link` | Light uppercase nav (12px) |
| `caption-bold` | Emphasized uppercase caption (13px) |
| `caption` | Light uppercase caption (12px) |
| `micro` | Tiny stencil labels (10px) |

### Principles
- **Universal uppercase**: Nearly every text element uses `text-transform: uppercase` — a systematic military/aerospace voice.
- **Positive letter-spacing as identity**: `0.96px` on display, `1.17px` on nav — wide tracking creates the stenciled, industrial feel that connects to DIN's heritage as a German engineering standard.
- **Two weights, strict hierarchy**: D-DIN-Bold (700) for headlines and nav emphasis, D-DIN (400) for body. No medium or semibold weights exist.
- **Tight line-heights**: 0.94–1.00 across most text — compressed, efficient, mission-critical.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px but the scale is intentionally minimal — spacing is not the organizing principle; photography is.

### Grid & Container
- No traditional grid — each section is a full-viewport cinematic frame
- Text is positioned absolutely or with generous padding over imagery
- Left-aligned text blocks on photography backgrounds
- No max-width container — content bleeds to viewport edges

### Whitespace Philosophy
- **Photography IS the whitespace**: Empty space is never empty — it's filled with the dark expanse of space, the curve of a planet, or the flame of a rocket engine.
- **Vertical pacing through viewport**: Each section is exactly one viewport tall, creating a rhythmic scroll where each "page" reveals a new scene.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Photography (Level 0) | Full-viewport imagery | Background layer — always present |
| Overlay (Level 1) | Dark gradient tinted `{colors.overlay}` (partial opacity in CSS) | Text legibility layer over photography |
| Text (Level 2) | Spectral white text, no shadow | Content layer — text floats directly on image |
| Ghost (Level 3) | `{colors.primary}` surface | Barely-visible interactive layer |

**Shadow Philosophy**: SpaceX uses ZERO shadows. In a design built entirely on photography, shadows are meaningless — every surface is already a photograph with natural lighting. Depth comes from the photographic content itself: the receding curvature of Earth, the diminishing trail of a rocket, the atmospheric haze around Mars.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Default for full-bleed imagery and text overlays |
| `xs` | 4px | Small dividers, utility elements |
| `pill` | 32px | Ghost buttons — the only rounded element |

## Components

The complete component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.nav-bar}`).

### Buttons
- **`button-primary`** — The Ghost button. Barely visible `{colors.primary}` surface with `1px solid {colors.primary-border}` border, `{rounded.pill}` corners, 18px padding. The only button variant — used for "LEARN MORE" CTAs over photography.

### Cards & Containers
**None.** SpaceX does not use cards, panels, or containers. All content is text directly on full-viewport photographs. The absence of containers IS the design.

### Inputs & Forms
Not present on the homepage. The site is purely presentational.

### Navigation
Transparent overlay nav on photography. D-DIN 13px weight 700, uppercase, `1.17px` tracking, spectral white text. SpaceX wordmark at 147×19px. Mobile collapses to hamburger.

### Image Treatment
- Full-viewport (100vh) photography sections
- Professional aerospace photography: rockets, Mars, space
- Dark gradient overlays for text legibility
- Each section = one full-screen photograph with text overlay
- No border radius, no frames — edge-to-edge imagery

## Do's and Don'ts

### Do
- Use full-viewport photography as the primary design element — every section is a scene
- Apply uppercase + positive letter-spacing to ALL text — the aerospace stencil voice
- Use D-DIN exclusively — no other fonts exist in the system
- Keep the color palette to black + spectral white (`{colors.ink}`) only
- Use ghost buttons (`{colors.primary}`) as the sole interactive element
- Apply dark gradient overlays for text legibility on photographs
- Let photography carry the emotional weight — the type system is functional, not expressive

### Don't
- Don't add cards, panels, or containers — text sits directly on photography
- Don't use shadows — they have no meaning in a photographic context
- Don't introduce colors — the palette is strictly achromatic with spectral tint
- Don't use sentence case — everything is uppercase
- Don't use negative letter-spacing — all tracking is positive (`0.96px`–`1.17px`)
- Don't reduce photography to thumbnails — every image is full-viewport
- Don't add decorative elements (icons, badges, dividers) — the design is photography + type + one button

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <600px | Stacked, reduced padding, smaller type |
| Tablet Small | 600–960px | Adjusted layout |
| Tablet | 960–1280px | Standard scaling |
| Desktop | 1280–1350px | Full layout |
| Large Desktop | 1350–1500px | Expanded |
| Ultra-wide | >1500px | Maximum viewport |

### Touch Targets
- Ghost buttons: 18px padding provides adequate touch area
- Navigation links: uppercase with generous letter-spacing aids readability

### Collapsing Strategy
- Photography: maintains full-viewport at all sizes, content repositions
- Hero text: 48px → scales down proportionally
- Navigation: horizontal → hamburger
- Text blocks: reposition but maintain overlay-on-photography pattern
- Full-viewport sections maintained on mobile

### Image Behavior
- Edge-to-edge photography at all viewport sizes
- `background-size: cover` with center focus
- Dark overlay gradients adapt to content position
- No art direction changes — same photographs, responsive positioning

---

## Agent Prompt Guide

### Quick Color Reference
- Background: Space Black (`{colors.background}`)
- Text: Spectral White (`{colors.ink}`)
- Button background: Ghost (`{colors.primary}`)
- Button border: Ghost Border (`{colors.primary-border}`)
- Overlay: Dark gradient tinted `{colors.overlay}` (partial opacity in CSS)

### Example Component Prompts
- "Create a full-viewport hero: background-image covering 100vh, dark gradient overlay (~50% black). Headline at 48px D-DIN-Bold, uppercase, letter-spacing 0.96px, spectral white (`{colors.ink}`) text. Ghost CTA button: `{colors.primary}` bg, 1px solid `{colors.primary-border}` border, 32px radius, 18px padding."
- "Design a navigation: transparent over photography. D-DIN 13px weight 700, uppercase, letter-spacing 1.17px, spectral white text. SpaceX wordmark left-aligned."
- "Build a content section: full-viewport height, background photography with dark overlay. Left-aligned text block with 48px D-DIN-Bold uppercase heading, 16px D-DIN body text, and ghost button below."
- "Create a micro label: D-DIN 10px, uppercase, letter-spacing 1px, spectral white, line-height 0.94."

### Iteration Guide
1. Start with photography — the image IS the design
2. All text is uppercase with positive letter-spacing — no exceptions
3. Only two colors: black and spectral white (`{colors.ink}`)
4. Ghost buttons are the only interactive element — transparent, spectral-bordered
5. Zero shadows, zero cards, zero decorative elements
6. Every section is full-viewport (100vh) — cinematic pacing
