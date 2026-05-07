---
version: alpha
name: Mistral AI
description: Sun-drenched warm-spectrum design — golden amber gradients, billboard-scale Arial display typography, sharp architectural corners, multi-layer amber-tinted shadows that bathe elements in golden hour light.

colors:
  # Primary brand
  primary: "#fa520f"
  mistral-orange: "#fa520f"
  mistral-flame: "#fb6424"
  block-orange: "#ff8105"

  # Sunshine scale
  sunshine-900: "#ff8a00"
  sunshine-700: "#ffa110"
  sunshine-500: "#ffb83e"
  sunshine-300: "#ffd06a"
  block-gold: "#ffe295"
  bright-yellow: "#ffd900"

  # Surface
  background: "#fffaeb"
  surface: "#fff0c2"
  surface-bright: "#ffffff"
  surface-dark: "#1f1f1f"
  ink: "#1f1f1f"

  # Text
  text-secondary: "#3d3d3d"   # was hsl(0,0%,24%)

  # Inverted
  on-primary: "#ffffff"
  on-dark: "#ffffff"

  # Form
  input-border: "#e5e5e7"     # was hsl(240,5.9%,90%)

  # Overlays (opaque approximations)
  white-overlay: "#fafaf2"   # was oklab(1,0,0 / 0.088) — flattened over warm ivory
  ghost-overlay: "#1a1a1a"   # was oklab(0,0,0 / 0.1)

  # Warm golden shadow (the signature multi-layer)
  shadow-golden: "#e6dccd"   # was rgba(127,99,21,0.12) — flattened over warm ivory
  shadow-golden-soft: "#ede5d8" # was rgba(127,99,21,0.10)
  shadow-golden-faint: "#f3ede1" # was rgba(127,99,21,0.06)

typography:
  display-hero:
    fontFamily: "Arial, ui-sans-serif, system-ui, sans-serif"
    fontSize: 82px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -2.05px
  section-heading:
    fontFamily: "Arial, ui-sans-serif, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: 0px
  sub-heading-large:
    fontFamily: "Arial, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: 0px
  sub-heading:
    fontFamily: "Arial, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0px
  card-title:
    fontFamily: "Arial, ui-sans-serif, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0px
  feature-title:
    fontFamily: "Arial, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  body:
    fontFamily: "Arial, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button:
    fontFamily: "Arial, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-uppercase:
    fontFamily: "Arial, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.8px
  caption:
    fontFamily: "Arial, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  sm-plus: 10px
  md: 12px
  md-plus: 16px
  lg: 20px
  xl: 24px
  2xl: 32px
  3xl: 40px
  4xl: 48px
  5xl: 64px
  6xl: 80px
  7xl: 100px

rounded:
  none: 0px
  sm: 4px
  md: 8px

components:
  # Buttons
  button-primary:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 12px 24px
  button-cream:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 12px 24px
  button-ghost:
    backgroundColor: "{colors.ghost-overlay}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 12px 24px
  button-text:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: 8px 0px

  # Cards
  card-ivory:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.card-title}"
    rounded: "{rounded.none}"
    padding: 32px
  card-cream:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.card-title}"
    rounded: "{rounded.none}"
    padding: 32px
  card-elevated:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.card-title}"
    rounded: "{rounded.none}"
    padding: 32px

  # Inputs
  input:
    backgroundColor: "{colors.surface-bright}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 16px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    padding: 16px 24px

  # Block identity tile (one segment of the gradient row)
  block-tile-yellow:
    backgroundColor: "{colors.bright-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 24px
  block-tile-amber:
    backgroundColor: "{colors.sunshine-700}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 24px
  block-tile-orange:
    backgroundColor: "{colors.mistral-orange}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    padding: 24px

  # Footer
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    padding: 80px 24px
---

# Mistral AI Design System

## Overview

Mistral AI's interface is a sun-drenched landscape rendered in code — a warm, bold, unapologetically European design that trades the typical blue-screen AI aesthetic for golden amber, burnt orange, and the feeling of late-afternoon light in southern France. Every surface glows with warmth: backgrounds fade from pale cream (`{colors.background}`) to deep amber, shadows carry golden undertones, and the brand's signature orange (`{colors.primary}`) burns through the page like a signal fire.

The design language is maximalist in its warmth but minimalist in its structure. Huge display headlines (82px) crash into the viewport with aggressive negative tracking (-2.05px), creating text blocks that feel like billboards or protest posters — declarations rather than descriptions. The typography uses Arial (likely a custom font with Arial as fallback) at extreme sizes, creating a raw, unadorned voice that says "we build frontier AI" with no decoration needed.

What makes Mistral distinctive is the complete commitment to a warm color temperature. The signature "block" identity — a gradient system flowing from bright yellow (`{colors.bright-yellow}`) through amber (`{colors.sunshine-700}`) to burnt orange (`{colors.mistral-orange}`) — creates a visual identity that's immediately recognizable. Even the shadows are warm, using amber-tinted blacks instead of cool grays. Combined with dramatic landscape photography in golden tones, the design feels less like a tech company and more like a European luxury brand that happens to build language models.

**Key Characteristics:**
- Golden-amber color universe: every tone from pale cream (`{colors.background}`) to burnt orange (`{colors.primary}`)
- Massive display typography (82px) with aggressive negative letter-spacing (-2.05px)
- Warm golden shadow system using amber-tinted approximations (`{colors.shadow-golden}`)
- The Mistral "M" block identity — a gradient from yellow to orange
- Dramatic landscape photography in warm golden tones
- Uppercase typography used strategically for section labels and CTAs
- Near-zero border-radius — sharp, architectural geometry
- French-European confidence: bold, warm, declarative

## Colors

### Primary
- **Mistral Orange** (`{colors.mistral-orange}`): Core brand color — vivid saturated orange-red that anchors the identity. Used for primary emphasis, brand block, highest-signal moments.
- **Mistral Flame** (`{colors.mistral-flame}`): Slightly warmer/lighter brand orange variant for secondary brand moments and hover states.
- **Block Orange** (`{colors.block-orange}`): Pure orange used in the gradient block system — warmer and less red than Mistral Orange.

### Secondary & Accent
- **Sunshine 900** (`{colors.sunshine-900}`): Deep golden amber — strongest sunshine accent.
- **Sunshine 700** (`{colors.sunshine-700}`): Core sunshine accent for backgrounds and interactive elements.
- **Sunshine 500** (`{colors.sunshine-500}`): Balanced warmth for mid-level emphasis.
- **Sunshine 300** (`{colors.sunshine-300}`): Subtle warm tints, secondary backgrounds.
- **Block Gold** (`{colors.block-gold}`): Soft background accents.
- **Bright Yellow** (`{colors.bright-yellow}`): Brightest tone in the gradient — top of the block identity.

### Surface & Background
- **Warm Ivory** (`{colors.background}`): Lightest page background — barely tinted with warmth.
- **Cream** (`{colors.surface}`): Primary warm surface and secondary button background.
- **Pure White** (`{colors.surface-bright}`): Maximum-contrast popovers and overlays.
- **Mistral Black** (`{colors.surface-dark}`): Primary dark surface for buttons, text, dark sections.

### Neutrals & Text
- **Mistral Black** (`{colors.ink}`): Primary text — a near-black that's warmer than pure `#000000`.
- **Black Tint** (`{colors.text-secondary}`): Medium dark gray for secondary text on light backgrounds (was `hsl(0, 0%, 24%)`).
- **Pure White** (`{colors.on-dark}`): Text on dark surfaces and CTA labels.

### Semantic & Form
- **Input Border** (`{colors.input-border}`): Cool-tinted light gray for form borders — one of the few cool tones (was `hsl(240, 5.9%, 90%)`).
- **White Overlay** (`{colors.white-overlay}`): Semi-transparent white for frosted-glass effects (was `oklab(1, 0, 0 / 0.088–0.1)`).

### Gradient System
- **Mistral Block Gradient**: Yellow (`{colors.bright-yellow}`) → Gold (`{colors.block-gold}`) → Amber (`{colors.sunshine-700}`) → Orange (`{colors.block-orange}`) → Flame (`{colors.mistral-flame}`) → Mistral Orange (`{colors.mistral-orange}`).
- **Golden Landscape Wash**: Photography and backgrounds use warm amber overlays creating a consistent golden temperature.
- **Warm Shadow Cascade**: Multi-layered golden shadows (`{colors.shadow-golden}`, `{colors.shadow-golden-soft}`, `{colors.shadow-golden-faint}`) building depth with amber-tinted transparency.

## Typography

### Font Family
- **Primary**: Likely a custom font (Font Source) with `Arial` as fallback, plus extended stack: `ui-sans-serif, system-ui, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji`.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference each role via tokens.

| Token | Use |
|---|---|
| `display-hero` | Maximum impact, billboard scale (82px) |
| `section-heading` | Feature section anchors (56px) |
| `sub-heading-large` | Secondary section titles (48px) |
| `sub-heading` | Card headings, feature names (32px) |
| `card-title` | Mid-level headings (30px) |
| `feature-title` | Small headings (24px) |
| `body` | Standard body text (16px) |
| `button` | Button labels |
| `button-uppercase` | Uppercase CTA labels (formal European signage feel) |
| `caption` | Metadata, secondary links (14px) |

### Principles
- **Single weight, maximum impact**: The entire system uses weight 400 — even at 82px. Size alone carries authority.
- **Ultra-tight at scale**: Line-heights of 0.95–1.00 at display sizes create text blocks where ascenders nearly touch descenders from the line above — dense, poster-like composition.
- **Aggressive tracking on display**: -2.05px letter-spacing at 82px compresses the hero text into a monolithic block.
- **Uppercase as emphasis**: Strategic `text-transform: uppercase` on button labels and section markers creates a formal, European signage quality.
- **No weight variation**: Hierarchy comes from size and color, never weight.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit `{spacing.sm}` (8px). Section spacing is generous (`{spacing.6xl}`–`{spacing.7xl}`).

### Grid & Container
- Max container width: approximately 1280px, centered
- Hero: full-width with massive typography overlaying warm backgrounds
- Feature sections: wide-format layouts with dramatic imagery
- Card grids: 2–3 column layouts

### Whitespace Philosophy
- **Bold declarations**: Huge headlines surrounded by generous whitespace create billboard-like impact.
- **Warm void**: Empty space itself feels warm because the backgrounds are tinted ivory/cream rather than pure white.
- **Photography as space-filler**: Large landscape images serve double duty as content and decorative whitespace.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Page backgrounds, text blocks |
| Golden Float (Level 1) | 5-layer warm shadow cascade using `{colors.shadow-golden}`, `{colors.shadow-golden-soft}`, `{colors.shadow-golden-faint}` | Feature cards, product showcases, elevated content |

**Shadow Philosophy**: Mistral uses a single but extraordinarily complex shadow — **five cascading layers** of amber-tinted shadow that build from a close 16px offset to a distant 400px offset. The result is a rich, warm, "golden hour" lighting effect that makes elevated elements look like they're bathed in afternoon sunlight. This is the most distinctive shadow system in any major AI brand.

## Shapes

The system is essentially **flat-cornered**: sharp, architectural geometry as a counterpoint to the warm color universe.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Default — sharp corners on cards, buttons, blocks, the entire system |
| `sm` | 4px | Rare softening on inline chrome |
| `md` | 8px | Optional soft surfaces (rare) |

The decision to keep radius near-zero is what gives Mistral its tension between soft warm color and hard mechanical geometry.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (e.g. `{components.button-primary}`, `{components.card-elevated}`) rather than reconstructing them.

### Buttons
- **`button-primary`** — Mistral Black surface with white text, sharp corners, 12px padding. The primary action — dark on warm.
- **`button-cream`** — Cream (`{colors.surface}`) surface with `{colors.ink}` text. Warm inviting secondary CTA.
- **`button-ghost`** — Slight dark overlay tint, `{colors.ink}` text. Secondary/de-emphasized.
- **`button-text`** — Transparent text-link button with top-only padding for tertiary nav.

### Cards
- **`card-ivory`** / **`card-cream`** — Flat warm-surface cards, sharp corners, generous interior padding.
- **`card-elevated`** — Same as cream but pair with the 5-layer golden shadow cascade for the signature "floating in golden light" effect.

### Inputs
- **`input`** — White surface, `{colors.input-border}` outline, sharp corners. The lone cool element in the system.

### Navigation
- **`nav-bar`** — Transparent (or warm-ivory) overlay above the warm hero. Logo left, links and CTA right. Minimal, wide-spaced.

### Block Identity
- **`block-tile-yellow`** / **`block-tile-amber`** / **`block-tile-orange`** — segments of the Mistral block gradient row (yellow → amber → burnt orange). Sharp corners, no gaps. The visual DNA of the brand.

### Footer
- **`footer`** — Mistral Black surface with white text, generous padding. Often pairs with a warm gradient transition from amber into the dark — a "sunset" effect ending the page.

## Do's and Don'ts

### Do
- Use the warm color spectrum exclusively: ivory, cream, amber, gold, orange
- Keep display typography at 82px+ with -2.05px letter-spacing for hero sections
- Use the Mistral block gradient (yellow → amber → orange) for brand moments
- Apply warm golden shadows (amber-tinted) for elevated elements
- Use Mistral Black (`{colors.ink}`) for text — never pure `#000000`
- Keep font weight at 400 throughout — let size and color carry hierarchy
- Use sharp, architectural corners — `{rounded.none}`
- Apply uppercase on button labels and section markers for European formality
- Use warm landscape photography with golden color grading

### Don't
- Don't introduce cool colors (blue, green, purple) — the palette is exclusively warm
- Don't use bold (700+) weight — 400 is the only weight
- Don't round corners — the sharp geometry is intentional
- Don't use cool-toned shadows — shadows must carry amber warmth
- Don't use pure white as a page background — always warm-tinted (`{colors.background}` minimum)
- Don't reduce hero text below 48px on desktop — the billboard scale is core
- Don't use more than 2 font weights — size variation replaces weight variation
- Don't add gradients outside the warm spectrum — no blue-to-purple, no cool transitions
- Don't use generic gray for text — even neutrals should be warm-tinted

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, stacked everything, hero text reduces to ~32px |
| Tablet | 640–768px | Minor layout adjustments |
| Small Desktop | 768–1024px | 2-column layouts begin |
| Desktop | 1024–1280px | Full layout with maximum typography scale |

### Touch Targets
- Buttons use generous padding (12px minimum)
- Navigation elements adequately spaced
- Cards serve as large touch targets

### Collapsing Strategy
- **Navigation**: Collapses to hamburger on mobile
- **Hero text**: 82px → 56px → 48px → 32px progressive scaling
- **Feature sections**: Multi-column → stacked
- **Photography**: Scales proportionally, may crop on mobile
- **Block identity**: Scales down proportionally

### Image Behavior
- Landscape photography scales proportionally
- Warm color grading maintained at all sizes
- Block gradient elements resize fluidly
- No art direction changes — same warm composition at all sizes

---

## Agent Prompt Guide

### Quick Color Reference
- Brand Orange: "Mistral Orange (#fa520f)"
- Page Background: "Warm Ivory (#fffaeb)"
- Warm Surface: "Cream (#fff0c2)"
- Primary Text: "Mistral Black (#1f1f1f)"
- Sunshine Amber: "Sunshine 700 (#ffa110)"
- Bright Gold: "Bright Yellow (#ffd900)"
- Text on Dark: "Pure White (#ffffff)"

### Example Component Prompts
- "Create a hero section on Warm Ivory (#fffaeb) with a massive headline at 82px Arial weight 400, line-height 1.0, letter-spacing -2.05px. Mistral Black (#1f1f1f) text. Add a dark solid CTA button (#1f1f1f bg, white text, 12px padding, sharp corners) and a cream secondary button (#fff0c2 bg)."
- "Design a feature card on Cream (#fff0c2) with sharp corners (no border-radius). Apply the golden shadow system: rgba(127, 99, 21, 0.12) -8px 16px 39px as the primary layer. Title at 32px weight 400, body at 16px."
- "Build the Mistral block identity: a row of colored blocks from Bright Yellow (#ffd900) through Sunshine 700 (#ffa110) to Mistral Orange (#fa520f). Sharp corners, no gaps."
- "Create a dark footer section on Mistral Black (#1f1f1f) with Pure White (#ffffff) text. Footer links at 14px. Add a warm gradient from Sunshine 700 (#ffa110) at the top fading to Mistral Black."

### Iteration Guide
1. Keep the warm temperature — "shift toward amber" not "shift toward gray"
2. Use size for hierarchy — 82px → 56px → 48px → 32px → 24px → 16px
3. Never add border-radius — sharp corners only
4. Shadows are always warm: "golden shadow with amber tones"
5. Font weight is always 400 — describe emphasis through size and color
