---
version: alpha
name: BMW
description: Automotive engineering made visual — alternating dark hero photography and white content sections, BMWTypeNextLatin Light uppercase display, zero radius corners, single BMW Blue interactive accent.

colors:
  # Surface
  background: "#ffffff"
  background-dark: "#262626"
  surface: "#ffffff"

  # Brand blues
  primary: "#1c69d4"
  primary-focus: "#0653b6"

  # Ink + text
  ink: "#262626"
  ink-inverted: "#ffffff"
  text-meta: "#757575"
  text-muted: "#bbbbbb"

  on-background: "#262626"
  on-surface: "#262626"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

  # Borders
  border: "#bbbbbb"

typography:
  display-hero:
    fontFamily: "BMWTypeNextLatin Light, BMWTypeNextLatin, Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo, sans-serif"
    fontSize: 60px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0px
  heading-section:
    fontFamily: "BMWTypeNextLatin, Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0px
  nav-emphasis:
    fontFamily: "BMWTypeNextLatin, Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo, sans-serif"
    fontSize: 18px
    fontWeight: 900
    lineHeight: 1.3
    letterSpacing: 0px
  body:
    fontFamily: "BMWTypeNextLatin, Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0px
  button-bold:
    fontFamily: "BMWTypeNextLatin, Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0px
  button-ui:
    fontFamily: "BMWTypeNextLatin, Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0px

spacing:
  micro: 1px
  xs: 5px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 40px
  4xl: 56px
  5xl: 60px

rounded:
  none: 0px

components:
  # Top navigation — dark surface
  nav-bar:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-emphasis}"
    rounded: "{rounded.none}"
    padding: 16px 32px

  nav-link:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-emphasis}"
    rounded: "{rounded.none}"
    padding: 8px 16px

  # Primary button — bold
  button-primary:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-bold}"
    rounded: "{rounded.none}"
    padding: 12px 24px

  # Standard button — regular weight
  button-default:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.none}"
    padding: 12px 24px

  # Accent / interactive button — BMW Blue
  button-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-bold}"
    rounded: "{rounded.none}"
    padding: 12px 24px
  button-accent-focus:
    backgroundColor: "{colors.primary-focus}"
    textColor: "{colors.on-primary}"

  # Card
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 32px

  card-dark:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    padding: 32px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"

  # Hero section — full-bleed dark
  hero-section:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-hero}"
    rounded: "{rounded.none}"
    padding: 60px 32px

  # Meta info text block
  meta-block:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-meta}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 8px 0
---

# BMW Design System

## Overview

BMW's website is automotive engineering made visual — a design system that communicates precision, performance, and German industrial confidence. The page alternates between deep dark hero sections (featuring full-bleed automotive photography) and clean white content areas, creating a cinematic rhythm reminiscent of a luxury car showroom where vehicles are lit against darkness. The BMW CI2020 design language defines every element.

The typography is built on BMWTypeNextLatin — a proprietary typeface in two variants: BMWTypeNextLatin Light (weight 300) for massive uppercase display headings, and BMWTypeNextLatin Regular for body and UI text. The 60px uppercase headline at weight 300 is the defining typographic gesture — light-weight type that whispers authority rather than shouting it. The fallback stack includes Helvetica and Japanese fonts (Hiragino, Meiryo), reflecting BMW's global presence.

What makes BMW distinctive is its CSS variable-driven theming system. Context-aware variables (`--site-context-highlight-color: {colors.primary}`, `--site-context-focus-color: {colors.primary-focus}`, `--site-context-metainfo-color: {colors.text-meta}`) suggest a design system built for multi-brand, multi-context deployment. The blue highlight color (`{colors.primary}`) is BMW's signature blue — used sparingly for interactive elements and focus states, never decoratively. Zero border-radius — BMW's design is angular, sharp-cornered, and uncompromisingly geometric.

**Key Characteristics:**
- BMWTypeNextLatin Light (weight 300) uppercase for display — whispered authority
- BMW Blue (`{colors.primary}`) as singular accent — used only for interactive elements
- Zero border-radius — angular, sharp-cornered, industrial geometry
- Dark hero photography + white content sections — showroom lighting rhythm
- CSS variable-driven theming: `--site-context-*` tokens for brand flexibility
- Weight 900 for navigation emphasis — extreme contrast with 300 display
- Tight line-heights (1.15–1.30) throughout — compressed, efficient, German engineering
- Full-bleed automotive photography as primary visual content

## Colors

### Primary Brand
- **Pure White** (`{colors.surface}`): Primary surface, card backgrounds. `--site-context-theme-color`.
- **BMW Blue** (`{colors.primary}`): `--site-context-highlight-color`, primary interactive accent.
- **BMW Focus Blue** (`{colors.primary-focus}`): `--site-context-focus-color`, keyboard focus and active states.

### Neutral Scale
- **Near Black** (`{colors.ink}`): Primary text on light surfaces, dark link text, dark hero backgrounds.
- **Meta Gray** (`{colors.text-meta}`): `--site-context-metainfo-color`, secondary text, metadata.
- **Silver** (`{colors.text-muted}`): Tertiary text, muted links, footer elements.

### Interactive States
- All links hover to white (`{colors.ink-inverted}`) — suggesting primarily dark-surface navigation
- Text links use underline: none on hover — clean interaction

### Shadows
- Minimal shadow system — depth through photography and dark/light section contrast

## Typography

### Font Families
- **Display Light**: `BMWTypeNextLatin Light`, fallbacks: `Helvetica, Arial, Hiragino Kaku Gothic ProN, Hiragino Sans, Meiryo`
- **Body / UI**: `BMWTypeNextLatin`, same fallback stack

### Hierarchy

The complete type scale lives in the `typography:` token block above. Use those tokens directly.

| Token | Use |
|---|---|
| `display-hero` | 60px uppercase Light weight 300 — monumental display |
| `heading-section` | Major section titles (32px) |
| `nav-emphasis` | Navigation bold items — weight 900 |
| `body` | Standard body text |
| `button-bold` | CTA buttons — weight 700 |
| `button-ui` | Standard buttons — weight 400 |

### Principles
- **Light display, heavy navigation**: Weight 300 for hero headlines creates whispered elegance; weight 900 for navigation creates stark authority. This extreme weight contrast (300 vs 900) is the signature typographic tension.
- **Universal uppercase display**: The 60px hero is always uppercase — creating a monumental, architectural quality.
- **Tight everything**: Line-heights from 1.15 to 1.30 across the entire system. Nothing breathes — every line is compressed, efficient, German-engineered.
- **Single font family**: BMWTypeNextLatin handles everything from 60px display to 16px body — unity through one typeface at different weights.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

### Grid & Container
- Full-width hero photography
- Centered content sections
- Footer: multi-column link grid

### Whitespace Philosophy
- **Showroom pacing**: Dark hero sections with generous padding create the feeling of walking through a showroom where each vehicle is spotlit.
- **Compressed content**: Body text areas use tight line-heights and compact spacing — information-dense, no waste.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Photography (Level 0) | Full-bleed dark imagery | Hero backgrounds |
| Flat (Level 1) | White surface, no shadow | Content sections |
| Focus (Accessibility) | `{colors.primary-focus}` outline | Focus states |

**Shadow Philosophy**: BMW uses virtually no shadows. Depth is created entirely through the contrast between dark photographic sections and white content sections — the automotive lighting does the elevation work.

## Shapes

The system has **no border-radius**. Every element is a precise rectangle.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Default for **everything** — buttons, cards, panels, inputs, dialogs, images |

Zero radius is the BMW identity. This is the most angular design system in the corpus.

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Dark fill with bold weight 700 text, sharp corners
- **`button-default`** — White surface, regular weight, sharp corners
- **`button-accent`** — BMW Blue accent for interactive moments

### Cards & Containers
- **`card`** — White, no border-radius, sharp rectangle
- **`card-dark`** — Dark surface for hero/feature sections

### Navigation
**`nav-bar`** — Dark background, BMWTypeNextLatin 18px weight 900 white nav links. BMW logo 54×54px. Hover remains white, no underline.

### Image Treatment
- Full-bleed automotive photography
- Dark cinematic lighting
- Edge-to-edge hero images
- Car photography as primary visual content

### Hero Section
**`hero-section`** — Dark background, full-bleed automotive photo, 60px uppercase BMWTypeNextLatin Light over it.

## Do's and Don'ts

### Do
- Use BMWTypeNextLatin Light (300) uppercase for all display headings
- Keep ALL corners sharp (`{rounded.none}`) — angular geometry is non-negotiable
- Use BMW Blue (`{colors.primary}`) only for interactive elements — never decoratively
- Apply weight 900 for navigation emphasis — the extreme weight contrast is intentional
- Use full-bleed automotive photography for hero sections
- Keep line-heights tight (1.15–1.30) throughout
- Use `--site-context-*` CSS variables for theming

### Don't
- Don't round corners — `{rounded.none}` is the BMW identity
- Don't use BMW Blue for backgrounds or large surfaces — it's an accent only
- Don't use medium font weights (500–600) — the system uses 300, 400, 700, 900 extremes
- Don't add decorative elements — the photography and typography carry everything
- Don't use relaxed line-heights — BMW text is always compressed
- Don't lighten the dark hero sections — the contrast with white IS the design

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Minimum supported |
| Mobile | 375–480px | Single column |
| Mobile Large | 480–640px | Slight adjustments |
| Tablet Small | 640–768px | 2-column begins |
| Tablet | 768–920px | Standard tablet |
| Desktop Small | 920–1024px | Desktop layout begins |
| Desktop | 1024–1280px | Standard desktop |
| Large Desktop | 1280–1440px | Expanded |
| Ultra-wide | 1440–1600px | Maximum layout |

### Collapsing Strategy
- Hero: 60px → scales down, maintains uppercase
- Navigation: horizontal → hamburger
- Photography: full-bleed maintained at all sizes
- Content sections: stack vertically
- Footer: multi-column → stacked

---

## Agent Prompt Guide

### Quick Color Reference
- Background: Pure White (`{colors.surface}`)
- Text: Near Black (`{colors.ink}`)
- Secondary text: Meta Gray (`{colors.text-meta}`)
- Accent: BMW Blue (`{colors.primary}`)
- Focus: BMW Focus Blue (`{colors.primary-focus}`)
- Muted: Silver (`{colors.text-muted}`)

### Example Component Prompts
- "Create a hero: full-width dark automotive photography background. Heading at 60px BMWTypeNextLatin Light weight 300, uppercase, line-height 1.30, white text. `{rounded.none}` everywhere."
- "Design navigation: dark background. BMWTypeNextLatin 18px weight 900 for links, white text. BMW logo 54x54. Sharp rectangular layout."
- "Build a button: 16px BMWTypeNextLatin weight 700, line-height 1.20. Sharp corners (`{rounded.none}`). White bottom border on dark surface."
- "Create content section: white background. Heading at 32px weight 400, line-height 1.30, `{colors.ink}`. Body at 16px weight 400, line-height 1.15."

### Iteration Guide
1. Zero border-radius — every corner is sharp, no exceptions
2. Weight extremes: 300 (display), 400 (body), 700 (buttons), 900 (nav)
3. BMW Blue (`{colors.primary}`) for interactive only — never as background or decoration
4. Photography carries emotion — the UI is pure precision
5. Tight line-heights everywhere — 1.15 to 1.30 is the range
