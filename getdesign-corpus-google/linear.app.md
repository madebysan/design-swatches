---
version: alpha
name: Linear
description: Dark-mode-first issue tracker — near-black canvas, Inter Variable with weight 510 signature, aggressive negative tracking, brand indigo-violet accent, semi-transparent white borders, and luminance-stacked depth.

colors:
  # Surfaces (luminance-stacked dark)
  background: "#08090a"
  background-deep: "#010102"
  surface: "#0f1011"
  surface-elevated: "#191a1b"
  surface-hover: "#28282c"

  # Ink (text scale)
  ink: "#f7f8f8"
  ink-secondary: "#d0d6e0"
  ink-tertiary: "#8a8f98"
  ink-quaternary: "#62666d"
  ink-muted: "#e2e4e7"

  # Brand & accent
  primary: "#5e6ad2"
  accent: "#7170ff"
  accent-hover: "#828fff"
  security-lavender: "#7a7fad"

  # Status
  success: "#27a644"
  emerald: "#10b981"

  # Solid borders
  border: "#23252a"
  border-secondary: "#34343a"
  border-tertiary: "#3e3e44"
  line-tint: "#141516"
  line-tertiary: "#18191a"

  # Semi-transparent white borders (opaque approximations on dark)
  border-subtle: "#1a1c1e"  # was rgba(255,255,255,0.05) on #08090a — Google format requires hex
  border-standard: "#212224"  # was rgba(255,255,255,0.08) on #08090a — Google format requires hex

  # Surface tints (opaque approximations)
  surface-tint-1: "#0d0e10"  # was rgba(255,255,255,0.02) — Google format requires hex
  surface-tint-2: "#131416"  # was rgba(255,255,255,0.04) — Google format requires hex
  surface-tint-3: "#16181a"  # was rgba(255,255,255,0.05) — Google format requires hex

  # Light mode
  background-light: "#f7f8f8"
  surface-light: "#f3f4f5"
  surface-light-alt: "#f5f6f7"
  border-light: "#d0d6e0"
  border-light-alt: "#e6e6e6"
  surface-pure: "#ffffff"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "Inter Variable, SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 510
    lineHeight: 1.00
    letterSpacing: -1.584px
    fontFeature: "'cv01', 'ss03'"
  display-large:
    fontFamily: "Inter Variable, SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 510
    lineHeight: 1.00
    letterSpacing: -1.408px
    fontFeature: "'cv01', 'ss03'"
  display:
    fontFamily: "Inter Variable, SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 510
    lineHeight: 1.00
    letterSpacing: -1.056px
    fontFeature: "'cv01', 'ss03'"
  heading-1:
    fontFamily: "Inter Variable, SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.13
    letterSpacing: -0.704px
    fontFeature: "'cv01', 'ss03'"
  heading-2:
    fontFamily: "Inter Variable, SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: -0.288px
    fontFeature: "'cv01', 'ss03'"
  heading-3:
    fontFamily: "Inter Variable, SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 590
    lineHeight: 1.33
    letterSpacing: -0.24px
    fontFeature: "'cv01', 'ss03'"
  body-large:
    fontFamily: "Inter Variable, SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: -0.165px
    fontFeature: "'cv01', 'ss03'"
  body:
    fontFamily: "Inter Variable, SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
    fontFeature: "'cv01', 'ss03'"
  body-medium:
    fontFamily: "Inter Variable, SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 510
    lineHeight: 1.50
    letterSpacing: 0px
    fontFeature: "'cv01', 'ss03'"
  small:
    fontFamily: "Inter Variable, SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: -0.165px
    fontFeature: "'cv01', 'ss03'"
  caption:
    fontFamily: "Inter Variable, SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 510
    lineHeight: 1.50
    letterSpacing: -0.13px
    fontFeature: "'cv01', 'ss03'"
  label:
    fontFamily: "Inter Variable, SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 510
    lineHeight: 1.40
    letterSpacing: 0px
    fontFeature: "'cv01', 'ss03'"
  micro:
    fontFamily: "Inter Variable, SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 510
    lineHeight: 1.50
    letterSpacing: -0.15px
    fontFeature: "'cv01', 'ss03'"
  mono-body:
    fontFamily: "Berkeley Mono, ui-monospace, SF Mono, Menlo, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  mono-label:
    fontFamily: "Berkeley Mono, ui-monospace, SF Mono, Menlo, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 48px
  5xl: 80px

rounded:
  none: 0px
  micro: 2px
  sm: 4px
  md: 6px
  card: 8px
  panel: 12px
  large: 22px
  pill: 9999px
  circle: 9999px

components:
  # Ghost button (default Linear button)
  button-ghost:
    backgroundColor: "{colors.surface-tint-1}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 6px 12px

  # Subtle button — toolbar / contextual
  button-subtle:
    backgroundColor: "{colors.surface-tint-2}"
    textColor: "{colors.ink-secondary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 0px 6px

  # Primary brand button
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 8px 16px
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.on-primary}"

  # Icon button — circular
  button-icon:
    backgroundColor: "{colors.surface-tint-2}"
    textColor: "{colors.ink}"
    rounded: "{rounded.circle}"
    size: 32px

  # Pill button — filter chip
  button-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-secondary}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 0px 10px

  # Toolbar button
  button-toolbar:
    backgroundColor: "{colors.surface-tint-3}"
    textColor: "{colors.ink-quaternary}"
    typography: "{typography.label}"
    rounded: "{rounded.micro}"
    padding: 0px 6px

  # Card
  card:
    backgroundColor: "{colors.surface-tint-1}"
    rounded: "{rounded.card}"
    padding: 24px
  card-featured:
    backgroundColor: "{colors.surface-tint-2}"
    rounded: "{rounded.panel}"
    padding: 32px

  # Text area
  input:
    backgroundColor: "{colors.surface-tint-1}"
    textColor: "{colors.ink-secondary}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 14px

  # Search input
  input-search:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 1px 32px

  # Success status pill (small dot)
  badge-success:
    backgroundColor: "{colors.emerald}"
    textColor: "{colors.ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.circle}"

  # Neutral pill — tag / category
  badge-neutral:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-secondary}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 0px 10px

  # Subtle inline badge
  badge-subtle:
    backgroundColor: "{colors.surface-tint-3}"
    textColor: "{colors.ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.micro}"
    padding: 0px 8px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-secondary}"
    typography: "{typography.caption}"
    padding: 16px 24px
---

# Linear Design System

## Overview

Linear's website is a masterclass in dark-mode-first product design — a near-black canvas (`{colors.background}`) where content emerges from darkness like starlight. The overall impression is one of extreme precision engineering: every element exists in a carefully calibrated hierarchy of luminance, from barely-visible borders to soft, luminous text (`{colors.ink}`). This is not a dark theme applied to a light design — it is darkness as the native medium, where information density is managed through subtle gradations of white opacity rather than color variation.

The typography system is built entirely on Inter Variable with OpenType features `"cv01"` and `"ss03"` enabled globally, giving the typeface a cleaner, more geometric character. Inter is used at a remarkable range of weights — from 300 (light body) through 510 (medium, Linear's signature weight) to 590 (semibold emphasis). The 510 weight is particularly distinctive: it sits between regular and medium, creating a subtle emphasis that doesn't shout. At display sizes (72px, 64px, 48px), Inter uses aggressive negative letter-spacing (-1.584px to -1.056px), creating compressed, authoritative headlines that feel engineered rather than designed. Berkeley Mono serves as the monospace companion for code and technical labels.

The color system is almost entirely achromatic — dark backgrounds with white/gray text — punctuated by a single brand accent: Linear's signature indigo-violet (`{colors.primary}` for backgrounds, `{colors.accent}` for interactive accents). This accent color is used sparingly and intentionally, appearing only on CTAs, active states, and brand elements. The border system uses ultra-thin, semi-transparent white borders that create structure without visual noise, like wireframes drawn in moonlight.

**Key Characteristics:**
- Dark-mode-native: `{colors.background}` marketing background, `{colors.surface}` panel background, `{colors.surface-elevated}` elevated surfaces
- Inter Variable with `"cv01", "ss03"` globally — geometric alternates for a cleaner aesthetic
- Signature weight 510 (between regular and medium) for most UI text
- Aggressive negative letter-spacing at display sizes (-1.584px at 72px, -1.056px at 48px)
- Brand indigo-violet: `{colors.primary}` (bg) / `{colors.accent}` (accent) / `{colors.accent-hover}` (hover) — the only chromatic color in the system
- Semi-transparent white borders throughout (`{colors.border-subtle}` / `{colors.border-standard}` opaque approximations)
- Button backgrounds at near-zero opacity tints
- Multi-layered shadows with inset variants for depth on dark surfaces
- Radix UI primitives as the component foundation
- Success green (`{colors.success}`, `{colors.emerald}`) used only for status indicators

## Colors

### Background Surfaces
- **Marketing Black** (`{colors.background-deep}` / `{colors.background}`): The deepest background — canvas for hero sections.
- **Panel Dark** (`{colors.surface}`): Sidebar and panel backgrounds.
- **Level 3 Surface** (`{colors.surface-elevated}`): Elevated surface areas, card backgrounds, dropdowns.
- **Secondary Surface** (`{colors.surface-hover}`): Lightest dark surface — hover states.

### Text & Content
- **Primary Text** (`{colors.ink}`): Near-white with a barely-warm cast.
- **Secondary Text** (`{colors.ink-secondary}`): Cool silver-gray for body text.
- **Tertiary Text** (`{colors.ink-tertiary}`): Muted gray for placeholders, metadata.
- **Quaternary Text** (`{colors.ink-quaternary}`): The most subdued text — timestamps, disabled.

### Brand & Accent
- **Brand Indigo** (`{colors.primary}`): Primary brand — CTA buttons, brand marks.
- **Accent Violet** (`{colors.accent}`): Brighter variant for interactive elements.
- **Accent Hover** (`{colors.accent-hover}`): Lighter, more saturated for hover.
- **Security Lavender** (`{colors.security-lavender}`): Muted indigo for security UI.

### Status
- **Green** (`{colors.success}`) — primary success
- **Emerald** (`{colors.emerald}`) — pill badges, completion

### Border & Divider
- **Border Primary** (`{colors.border}`) — solid dark border for prominent separations
- **Border Secondary/Tertiary** (`{colors.border-secondary}`, `{colors.border-tertiary}`) — variant solid borders
- **Border Subtle/Standard** (`{colors.border-subtle}`, `{colors.border-standard}`) — semi-transparent white approximations
- **Line Tint/Tertiary** (`{colors.line-tint}`, `{colors.line-tertiary}`) — nearly invisible dividers

### Light Mode Neutrals
- `{colors.background-light}` page background, `{colors.surface-light}` / `{colors.surface-light-alt}` subtle surface tinting, `{colors.border-light}` visible border, `{colors.surface-pure}` card surfaces.

## Typography

### Font Family
- **Primary**: `Inter Variable`, fallbacks `SF Pro Display, -apple-system, system-ui, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue`
- **Monospace**: `Berkeley Mono`, fallbacks `ui-monospace, SF Mono, Menlo`
- **OpenType Features**: `"cv01", "ss03"` enabled globally — single-story 'a' and adjusted letterforms for a cleaner geometric appearance.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens (`{typography.display-xl}`, `{typography.body}`) directly.

| Token | Use |
|---|---|
| `display-xl` | 72px hero headlines |
| `display-large` | 64px secondary hero |
| `display` | 48px section headlines |
| `heading-1` | 32px major section titles |
| `heading-2` | 24px sub-section headings |
| `heading-3` | 20px feature titles, card headers (weight 590) |
| `body-large` | 18px introduction text |
| `body` | 16px standard reading text |
| `body-medium` | 16px navigation, labels |
| `small` | 15px secondary body |
| `caption` | 13px metadata |
| `label` | 12px button text, small labels |
| `micro` | 10px tiny labels |
| `mono-body` | Berkeley Mono 14px |
| `mono-label` | Berkeley Mono 12px |

### Principles
- **510 is the signature weight**: between regular (400) and medium (500). Subtle emphasis without heaviness.
- **Compression at scale**: progressively tighter letter-spacing from -1.584px at 72px down through display sizes; relaxes toward normal below 24px.
- **OpenType as identity**: `"cv01", "ss03"` aren't decorative — they transform Inter into Linear's distinctive typeface.
- **Three-tier weight system**: 400 (reading), 510 (emphasis/UI), 590 (strong emphasis). Weight 300 appears only in deliberately de-emphasized contexts.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is **8px**, with intermediate values (7px, 11px) suggesting micro-adjustments for optical alignment.

### Grid & Container
- Max content width: ~1200px
- Hero: centered single-column with generous vertical padding
- Feature sections: 2–3 column grids
- Full-width dark sections with internal max-width constraints

### Whitespace Philosophy
- **Darkness as space**: empty space isn't white — it's absence. The near-black background IS the whitespace.
- **Compressed headlines, expanded surroundings**: 72px display with -1.584px tracking is dense and compressed, but sits within vast dark padding.
- **Section isolation**: each feature section is separated by generous vertical padding (`5xl`+) with no visible dividers.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, `{colors.background-deep}` | Page background, deepest canvas |
| Subtle (Level 1) | `0 1px 0 {colors.border-subtle}` | Toolbar buttons, micro-elevation |
| Surface (Level 2) | `{colors.surface-tint-3}` bg + `1px solid {colors.border-standard}` | Cards, input fields, containers |
| Inset (Level 2b) | `0 0 12px {colors.background-deep} inset` | Recessed panels, inner shadows |
| Ring (Level 3) | `0 0 0 1px {colors.background-deep}` | Border-as-shadow technique |
| Elevated (Level 4) | `0 2px 4px {colors.background-deep}` | Floating elements, dropdowns |

**Shadow Philosophy**: On dark surfaces, traditional shadows (dark on dark) are nearly invisible. Linear solves this by using semi-transparent white borders as the primary depth indicator. Elevation is communicated through background luminance steps — each level slightly increases the white opacity of the surface (`{colors.surface-tint-1}` → `{colors.surface-tint-2}` → `{colors.surface-tint-3}`), creating a subtle stacking effect. The inset shadow technique creates a unique "sunken" effect for recessed panels.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Sharp inline elements (rare) |
| `micro` | 2px | Inline badges, toolbar buttons, subtle tags |
| `sm` | 4px | Small containers, list items |
| `md` | 6px | Buttons, inputs, functional elements |
| `card` | 8px | Cards, dropdowns, popovers |
| `panel` | 12px | Panels, featured cards, section containers |
| `large` | 22px | Large panel elements |
| `pill` | 9999px | Chips, filter pills, status tags |
| `circle` | 9999px | Icon buttons, avatars, status dots |

## Components

The complete component spec lives in the `components:` token block above. Reference components directly (`{components.button-primary}`, `{components.card}`).

### Buttons
- **`button-ghost`** — default Linear button: ultra-low-opacity background, near-white text, 6px radius, 1px subtle border.
- **`button-subtle`** — toolbar/contextual.
- **`button-primary`** — brand indigo, white text — the canonical CTA.
- **`button-icon`** — circular, surface-tinted.
- **`button-pill`** — filter chip, full pill, transparent background.
- **`button-toolbar`** — small 2px-radius toolbar action.

### Cards
- **`card`** — surface-tinted background, semi-transparent border, 8px radius.
- **`card-featured`** — slightly more lifted background, 12px radius.

### Inputs
- **`input`** — text area, 12px×14px padding, 6px radius.
- **`input-search`** — icon-aware compact search.

### Badges
- **`badge-success`** — emerald circular dot for status.
- **`badge-neutral`** — full pill with transparent background and 1px border.
- **`badge-subtle`** — micro-radius inline label.

### Navigation
- **`nav-bar`** — dark sticky header on near-black; 13–14px weight 510 links in `{colors.ink-secondary}`, hover lightens to `{colors.ink}`. Brand indigo CTA right-aligned. Mobile collapses to hamburger.

## Do's and Don'ts

### Do
- Use Inter Variable with `"cv01", "ss03"` on ALL text
- Use weight 510 as your default emphasis weight
- Apply aggressive negative letter-spacing at display sizes (-1.584px at 72px, -1.056px at 48px)
- Build on near-black backgrounds — `{colors.background}` for marketing, `{colors.surface}` for panels, `{colors.surface-elevated}` for elevated surfaces
- Use semi-transparent white borders (`{colors.border-subtle}` / `{colors.border-standard}` approximations) instead of solid dark borders
- Keep button backgrounds nearly transparent
- Reserve brand indigo (`{colors.primary}` / `{colors.accent}`) for primary CTAs and interactive accents only
- Use `{colors.ink}` for primary text — not pure `#ffffff`
- Apply the luminance stacking model: deeper = darker bg, elevated = slightly lighter bg

### Don't
- Don't use pure white as primary text
- Don't use solid colored backgrounds for buttons — transparency is the system
- Don't apply the brand indigo decoratively
- Don't use positive letter-spacing on display text
- Don't use visible/opaque borders on dark backgrounds
- Don't skip the OpenType features — without them, it's generic Inter, not Linear's Inter
- Don't use weight 700 (bold) — Linear's maximum weight is 590
- Don't introduce warm colors into the UI chrome
- Don't use drop shadows for elevation on dark surfaces — use background luminance stepping

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile Small | <600px | Single column, compact padding |
| Mobile | 600–640px | Standard mobile layout |
| Tablet | 640–768px | Two-column grids begin |
| Desktop Small | 768–1024px | Full card grids, expanded padding |
| Desktop | 1024–1280px | Standard desktop, full navigation |
| Large Desktop | >1280px | Full layout, generous margins |

### Touch Targets
- Buttons use comfortable padding with 6px radius minimum
- Navigation links at 13–14px with adequate spacing
- Pill tags have 10px horizontal padding for touch accessibility
- Icon buttons at 50% radius ensure circular, easy-to-tap targets
- Search trigger is prominently placed with generous hit area

### Collapsing Strategy
- Hero: 72px → 48px → 32px display text, tracking adjusts proportionally
- Navigation: horizontal links + CTAs → hamburger menu at 768px
- Feature cards: 3-column → 2-column → single column stacked
- Product screenshots: maintain aspect ratio, may reduce padding
- Changelog: timeline maintains single-column through all sizes
- Footer: multi-column → stacked single column
- Section spacing: 80px+ → 48px on mobile

### Image Behavior
- Dashboard screenshots maintain border treatment at all sizes
- Hero visuals simplify on mobile (fewer floating UI elements)
- Product screenshots use responsive sizing with consistent radius
- Dark background ensures screenshots blend naturally at any viewport

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Brand Indigo (`{colors.primary}`)
- Page Background: Marketing Black (`{colors.background}`)
- Panel Background: Panel Dark (`{colors.surface}`)
- Surface: Level 3 (`{colors.surface-elevated}`)
- Heading text: Primary White (`{colors.ink}`)
- Body text: Silver Gray (`{colors.ink-secondary}`)
- Muted text: Tertiary Gray (`{colors.ink-tertiary}`)
- Subtle text: Quaternary Gray (`{colors.ink-quaternary}`)
- Accent: Violet (`{colors.accent}`)
- Accent Hover: Light Violet (`{colors.accent-hover}`)
- Border (default): `{colors.border-standard}`
- Border (subtle): `{colors.border-subtle}`

### Example Component Prompts
- "Create a hero section on `{colors.background}`. Headline at 48px Inter Variable weight 510, line-height 1.00, letter-spacing -1.056px, color `{colors.ink}`, font-feature-settings `'cv01', 'ss03'`. Subtitle at 18px weight 400, line-height 1.60, color `{colors.ink-tertiary}`. Brand CTA button (`{colors.primary}`, 6px radius, 8px 16px padding) and ghost button."
- "Design a card on dark background: `{colors.surface-tint-1}` background, 1px solid `{colors.border-standard}` border, 8px radius. Title at 20px Inter Variable weight 590, letter-spacing -0.24px, color `{colors.ink}`. Body at 15px weight 400, color `{colors.ink-tertiary}`."
- "Build a pill badge: transparent background, `{colors.ink-secondary}` text, 9999px radius, 0px 10px padding, 1px solid `{colors.border}` border, 12px Inter Variable weight 510."
- "Create navigation: dark sticky header on `{colors.surface}`. Inter Variable 13px weight 510 for links, `{colors.ink-secondary}` text. Brand indigo CTA `{colors.primary}` right-aligned with 6px radius."
- "Design a command palette: `{colors.surface-elevated}` background, 1px solid `{colors.border-standard}` border, 12px radius. Input at 16px Inter Variable weight 400, `{colors.ink}` text."

### Iteration Guide
1. Always set font-feature-settings `"cv01", "ss03"` on all Inter text — non-negotiable
2. Letter-spacing scales with font size: -1.584px at 72px, -1.056px at 48px, -0.704px at 32px, normal below 16px
3. Three weights: 400 (read), 510 (emphasize/navigate), 590 (announce)
4. Surface elevation via background opacity — never solid backgrounds on dark
5. Brand indigo (`{colors.primary}` / `{colors.accent}`) is the only chromatic color
6. Borders are always semi-transparent white, never solid dark colors on dark backgrounds
7. Berkeley Mono for any code or technical content, Inter Variable for everything else
