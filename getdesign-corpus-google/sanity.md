---
version: alpha
name: Sanity
description: Nocturnal command-center aesthetic for a structured-content platform — near-black canvas, waldenburgNormal with extreme negative tracking, achromatic gray ramp, and coral-red plus electric-blue accents.

colors:
  # Canvas + surfaces
  background: "#0b0b0b"
  surface: "#212121"
  surface-elevated: "#353535"
  surface-inverted: "#ffffff"
  surface-light: "#ededed"

  # Ink
  ink: "#ffffff"
  ink-muted: "#b9b9b9"
  ink-subtle: "#797979"
  ink-on-light: "#0b0b0b"
  ink-on-light-muted: "#212121"

  # Brand accent — coral red CTA
  primary: "#f36458"
  on-primary: "#ffffff"

  # Universal interactive / hover
  interactive: "#0052ef"
  on-interactive: "#ffffff"
  interactive-light: "#55beff"
  interactive-pale: "#afe3ff"
  focus-ring: "#0052ef"
  focus-tint: "#072227"  # focus background shift on inputs

  # Vivid accents
  accent-green: "#19d600"  # sRGB fallback for display-p3 neon green
  accent-magenta: "#f500ff"  # sRGB fallback for display-p3 magenta

  # Semantic
  error: "#dd0000"
  success: "#37cd84"

  # Borders
  border-dark: "#0b0b0b"
  border-subtle: "#212121"
  border-medium: "#353535"
  border-light: "#ffffff"
  border-orange: "#ff5500"  # sRGB fallback for display-p3 orange

  # Pure black for max-contrast moments
  black: "#000000"

typography:
  display-hero:
    fontFamily: "waldenburgNormal, ui-sans-serif, system-ui, sans-serif"
    fontSize: 112px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -4.48px
  hero-secondary:
    fontFamily: "waldenburgNormal, ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -2.88px
  heading-section:
    fontFamily: "waldenburgNormal, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -1.68px
  heading-large:
    fontFamily: "waldenburgNormal, ui-sans-serif, system-ui, sans-serif"
    fontSize: 38px
    fontWeight: 400
    lineHeight: 1.10
    letterSpacing: -1.14px
  heading-medium:
    fontFamily: "waldenburgNormal, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 425
    lineHeight: 1.24
    letterSpacing: -0.32px
  heading-small:
    fontFamily: "waldenburgNormal, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 425
    lineHeight: 1.24
    letterSpacing: -0.24px
  subheading:
    fontFamily: "waldenburgNormal, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 425
    lineHeight: 1.13
    letterSpacing: -0.2px
  body-large:
    fontFamily: "waldenburgNormal, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.18px
  body:
    fontFamily: "waldenburgNormal, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-small:
    fontFamily: "waldenburgNormal, ui-sans-serif, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.15px
  caption:
    fontFamily: "waldenburgNormal, ui-sans-serif, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: -0.13px
  caption-small:
    fontFamily: "waldenburgNormal, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.12px
  micro-label:
    fontFamily: "waldenburgNormal, ui-sans-serif, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0
  code-body:
    fontFamily: "IBM Plex Mono, ui-monospace, monospace"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  code-caption:
    fontFamily: "IBM Plex Mono, ui-monospace, monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

spacing:
  hairline: 1px
  micro: 2px
  xxs: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px
  5xl: 96px
  6xl: 120px

rounded:
  none: 0px
  xs: 3px
  sm: 5px
  md: 6px
  lg: 12px
  pill: 99999px

components:
  # Primary CTA — coral pill
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  button-primary-hover:
    backgroundColor: "{colors.interactive}"
    textColor: "{colors.on-interactive}"

  # Dark secondary pill
  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 12px
  button-secondary-hover:
    backgroundColor: "{colors.interactive}"
    textColor: "{colors.on-interactive}"

  # Light outlined pill
  button-outlined:
    backgroundColor: "{colors.surface-inverted}"
    textColor: "{colors.ink-on-light}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 8px
  button-outlined-hover:
    backgroundColor: "{colors.interactive}"
    textColor: "{colors.on-interactive}"

  # Ghost / subtle
  button-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 0px 12px
  button-ghost-hover:
    backgroundColor: "{colors.interactive}"
    textColor: "{colors.on-interactive}"

  # Uppercase label button (tab-like)
  button-label:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.sm}"
    padding: 4px 8px

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  card-feature:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 32px

  # Inputs
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.focus-tint}"
    textColor: "{colors.ink}"

  # Search
  input-search:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: 0px 12px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    padding: 12px 24px
  nav-link:
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.interactive}"

  # Badges
  badge-light:
    backgroundColor: "{colors.surface-inverted}"
    textColor: "{colors.ink-on-light}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 8px
  badge-dark:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 8px
---

# Sanity Design System

## Overview

Sanity's website is a developer-content platform rendered as a nocturnal command center — dark, precise, and deeply structured. The entire experience sits on a near-black canvas (`{colors.background}`) that reads less like a "dark mode toggle" and more like the natural state of a tool built for people who live in terminals. Where most CMS marketing pages reach for friendly pastels and soft illustration, Sanity leans into the gravity of its own product: structured content deserves a structured stage.

The signature typographic voice is waldenburgNormal — a distinctive, slightly geometric sans-serif with tight negative letter-spacing (`-0.32px` to `-4.48px` at display sizes) that gives headlines a compressed, engineered quality. At 112px hero scale with `-4.48px` tracking, the type feels almost machined — like precision-cut steel letterforms. This is paired with IBM Plex Mono for code and technical labels, creating a dual-register voice: editorial authority meets developer credibility.

What makes Sanity distinctive is the interplay between its monochromatic dark palette and vivid, saturated accent punctuation. The neutral scale runs from pure black through a tightly controlled gray ramp (`{colors.background}` → `{colors.surface}` → `{colors.surface-elevated}` → `{colors.ink-subtle}` → `{colors.ink-muted}` → `{colors.surface-light}` → `{colors.surface-inverted}`) with no warm or cool bias — just pure achromatic precision. Against this disciplined backdrop, neon green (`{colors.accent-green}`) and electric blue (`{colors.interactive}`) land with the impact of signal lights in a dark control room. The coral-red CTA (`{colors.primary}`) provides the only warm touch in an otherwise cool system.

**Key Characteristics:**
- Near-black canvas (`{colors.background}`) as the default, natural environment — not a dark "mode" but the primary identity
- waldenburgNormal with extreme negative tracking at display sizes, creating a precision-engineered typographic voice
- Pure achromatic gray scale — no warm or cool undertones, pure neutral discipline
- Vivid accent punctuation: neon green, electric blue (`{colors.interactive}`), and coral-red (`{colors.primary}`) against the dark field
- Pill-shaped primary buttons (`{rounded.pill}`) contrasting with subtle rounded rectangles (`{rounded.xs}`–`{rounded.md}`) for secondary actions
- IBM Plex Mono as the technical counterweight to the editorial display face
- Full-bleed dark sections with content contained in measured max-width containers
- Hover states that shift to electric blue (`{colors.interactive}`) across all interactive elements — a consistent "activation" signal

## Colors

### Primary Brand
- **Sanity Black** (`{colors.background}`): The primary canvas and dominant surface color. Not pure black but close enough to feel absolute. The foundation of the entire visual identity.
- **Pure Black** (`{colors.black}`): Used for maximum-contrast moments, deep overlays, and certain border accents.
- **Sanity Red** (`{colors.primary}`): The primary CTA and brand accent — a warm coral-red used for "Get Started" buttons and primary conversion points.

### Accent & Interactive
- **Electric Blue** (`{colors.interactive}`): The universal hover/active state color across the entire system. Buttons, links, and interactive elements all shift to this blue on hover. Also used for focus rings.
- **Light Blue** (`{colors.interactive-light}` / `{colors.interactive-pale}`): Secondary blue variants used for accent backgrounds, badges, and dimmed blue surfaces.
- **Neon Green** (`{colors.accent-green}`): A vivid green used for success states and premium feature highlights (sRGB fallback for the original wide-gamut display-p3 value).
- **Accent Magenta** (`{colors.accent-magenta}`): A vivid magenta for specialized accent moments (sRGB fallback for the original wide-gamut display-p3 value).

### Surface & Background
- **Near Black** (`{colors.background}`): Default page background and primary surface.
- **Dark Gray** (`{colors.surface}`): Elevated surface color for cards, secondary containers, input backgrounds, and subtle layering above the base canvas.
- **Medium Dark** (`{colors.surface-elevated}`): Tertiary surface and border color for creating depth between dark layers.
- **Pure White** (`{colors.surface-inverted}`): Used for inverted sections, light-on-dark text, and specific button surfaces.
- **Light Gray** (`{colors.surface-light}`): Light surface for inverted/light sections and subtle background tints.

### Neutrals & Text
- **White** (`{colors.ink}`): Primary text color on dark surfaces, maximum legibility.
- **Silver** (`{colors.ink-muted}`): Secondary text, body copy on dark surfaces, muted descriptions, and placeholder text.
- **Medium Gray** (`{colors.ink-subtle}`): Tertiary text, metadata, timestamps, and de-emphasized content.
- **Charcoal** (`{colors.ink-on-light-muted}`): Text on light/inverted surfaces.
- **Near Black Text** (`{colors.ink-on-light}`): Primary text on white/light button surfaces.

### Semantic
- **Error Red** (`{colors.error}`): Destructive actions, validation errors, and critical warnings.
- **Success Green** (`{colors.success}`): Privacy/compliance indicator green.
- **Focus Ring Blue** (`{colors.focus-ring}`): Focus ring color, matching the interactive blue.

### Borders
- **Dark Border** (`{colors.border-dark}`): Primary border on dark containers — barely visible, maintaining minimal containment.
- **Subtle Border** (`{colors.border-subtle}`): Standard border for inputs, textareas, and card edges on dark surfaces.
- **Medium Border** (`{colors.border-medium}`): More visible borders for emphasized containment and dividers.
- **Light Border** (`{colors.border-light}`): Border on inverted/light elements or buttons needing contrast separation.
- **Orange Border** (`{colors.border-orange}`): Special accent border for highlighted/featured elements (sRGB fallback for the original wide-gamut display-p3 value).

## Typography

### Font Family
- **Display / Body / UI**: `waldenburgNormal`, fallback `ui-sans-serif, system-ui`
- **Code / Technical**: `IBM Plex Mono`, fallback `ui-monospace`

*Note: waldenburgNormal is a custom typeface. For external implementations, use Inter or Space Grotesk as the sans substitute (geometric, slightly condensed feel). IBM Plex Mono is available on Google Fonts.*

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | Maximum impact hero statements (112px) |
| `hero-secondary` | Large section headers (72px) |
| `heading-section` | Primary section anchors (48px) |
| `heading-large` | Feature section titles (38px) |
| `heading-medium` | Card titles, subsection headers (32px) |
| `heading-small` | Smaller feature headings (24px) |
| `subheading` | Sub-section markers (20px) |
| `body-large` | Intro paragraphs, descriptions (18px) |
| `body` | Standard reading text (16px) |
| `body-small` | Compact body text (15px) |
| `caption` | Metadata, descriptions, tags (13px) |
| `caption-small` | Footnotes, timestamps (12px) |
| `micro-label` | Uppercase labels, tiny badges (11px) |
| `code-body` | Code blocks, technical content |
| `code-caption` | Inline code, small technical labels |

### Principles
- **Extreme negative tracking at scale**: Display headings at 72px+ use aggressive negative letter-spacing (`-2.88px` to `-4.48px`), creating a tight engineered quality.
- **Single font, multiple registers**: waldenburgNormal handles both editorial display and functional UI text. The weight range is narrow (400–425 for most, 500–600 only for tiny labels).
- **OpenType feature control**: Display sizes use `"cv01", "cv11", "cv12", "cv13", "ss07"`; body uses `"calt" 0` to fine-tune character alternates.
- **Tight headings, relaxed body**: Headings use 1.00–1.24 line-height; body breathes at 1.50.
- **Uppercase for technical labels**: IBM Plex Mono captions and small labels frequently use uppercase with tight line-heights, creating a "system readout" aesthetic.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

The scale runs from `hairline` (1px) for border-like gaps up through `6xl` (120px) for hero vertical padding. Within sections spacing stays tight (`lg`–`2xl`); between sections spacing breathes wide (`4xl`–`6xl`).

### Grid & Container
- Max content width: ~1440px
- Page gutter: 32px on desktop, 16px on mobile
- Content sections use full-bleed backgrounds with centered, max-width content
- Multi-column layouts: 2–3 columns on desktop, single column on mobile
- Card grids use CSS Grid with `lg`–`xl` gaps

### Whitespace Philosophy
Sanity uses aggressive vertical spacing between sections (`4xl`–`6xl`) to create breathing room on the dark canvas. Within sections, spacing is tighter (`lg`–`2xl`), creating dense information clusters separated by generous voids. This rhythm gives the page a "slides" quality — each section feels like its own focused frame.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Default state for most elements — dark surfaces create depth through color alone |
| Subtle (Level 1) | `0 0 0 1px {colors.border-subtle}` | Border-like ring for minimal containment |
| Focus (Level 2) | `0 0 0 2px {colors.focus-ring}` | Focus ring for inputs and interactive elements |
| Overlay (Level 3) | Backdrop blur + semi-transparent dark | Navigation overlay, modal backgrounds |

**Shadow Philosophy**: Sanity's depth system is almost entirely **colorimetric** rather than shadow-based. Elevation is communicated through surface color shifts: `{colors.background}` (ground) → `{colors.surface}` (elevated) → `{colors.surface-elevated}` (prominent) → `{colors.surface-inverted}` (inverted/highest). The few shadows that exist are ring-based (`0 0 0 Npx`) or blur-based, not offset shadows. Border-based containment serves as the primary spatial separator. The system avoids "floating card" aesthetics — everything feels mounted to the surface rather than hovering above it.

## Shapes

The system jumps from small radii directly to a full pill — no mid-range values.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Hard-edge containers (rare in this system) |
| `xs` | 3px | Inputs, textareas, subtle rounding |
| `sm` | 5px | Secondary buttons, small cards, tags |
| `md` | 6px | Standard cards, containers |
| `lg` | 12px | Large cards, feature containers, forms |
| `pill` | 99999px | Primary buttons, badges, nav pills |

Sanity does not use radii between 13px and 99998px. The jump from `lg` (12px) to `pill` is intentional — there's no middle ground.

## Components

The complete component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card}`) rather than reconstructing values.

### Buttons
- **`button-primary`** — Coral-red full pill. The signature CTA. Hovers to electric blue.
- **`button-secondary`** — Near-black pill with silver text. Hovers to electric blue.
- **`button-outlined`** — White pill with black text and `1px` `{colors.ink-on-light}` border. Hovers to electric blue.
- **`button-ghost`** — Dark gray rectangle with subtle `{rounded.sm}` corners. Hovers to electric blue.
- **`button-label`** — Tab-like uppercase 11px label, weight 600, transparent or dark background.

### Cards
- **`card`** — Standard `{colors.surface}` card with `{rounded.md}` corners and a hairline `{colors.border-medium}` border. White titles, silver body.
- **`card-feature`** — Full-bleed feature card on `{colors.background}` with `{rounded.lg}` corners, `32px` padding, and overlaid imagery/text.

### Inputs
- **`input`** — Near-black background, silver text, hairline `{colors.border-subtle}` border, `{rounded.xs}` corners. Focus shifts background to `{colors.focus-tint}` with a 2px `{colors.focus-ring}` ring.
- **`input-search`** — Same surface and ink but flush horizontal padding only.

### Navigation
Top nav: `{colors.background}` with backdrop blur, left-aligned wordmark, silver `{typography.body}` links that hover to electric blue, right-aligned coral-red pill CTA, hairline `{colors.border-subtle}` bottom border.

Footer: same dark canvas, multi-column link grid; section headers in 13px IBM Plex Mono uppercase white.

### Badges
- **`badge-light`** — White pill with near-black text, used for neutral subtle tags.
- **`badge-dark`** — Near-black pill with white text, used for filled neutral tags.

## Do's and Don'ts

### Do
- Use the achromatic gray scale as the foundation — maintain pure neutral discipline with no warm/cool tinting
- Apply Electric Blue (`{colors.interactive}`) consistently as the universal hover/active state across all interactive elements
- Use extreme negative letter-spacing (`-2px` to `-4.48px`) on display headings 48px and above
- Keep primary CTAs as full-pill shapes (`{rounded.pill}`) with the coral-red (`{colors.primary}`)
- Use IBM Plex Mono uppercase for technical labels, tags, and system metadata
- Communicate depth through surface color (dark-to-light) rather than shadows
- Maintain generous vertical section spacing (`4xl`–`6xl`) on the dark canvas
- Apply OpenType feature settings (`"cv01", "cv11", "cv12", "cv13", "ss07"`) for display typography

### Don't
- Don't introduce warm or cool color tints to the neutral scale — Sanity's grays are pure achromatic
- Don't use drop shadows for elevation — dark interfaces demand colorimetric depth
- Don't apply border-radius between 13px and 99998px — the system jumps from `lg` (12px) directly to `pill`
- Don't mix the coral-red CTA with the electric blue interactive color in the same element
- Don't use heavy font weights (700+) — the system maxes out at 600 and only for 11px uppercase labels
- Don't place light text on light surfaces or dark text on dark surfaces without checking gray-on-gray contrast
- Don't use offset box-shadows — ring shadows or border-based containment only
- Don't break the tight line-height on headings — 1.00–1.24 is the range, never 1.5+ for display

---

## Responsive Behavior

### Breakpoints

| Name | Width | Behavior |
|------|-------|----------|
| Desktop XL | >= 1640px | Full layout, maximum content width |
| Desktop | >= 1440px | Standard desktop layout |
| Desktop Compact | >= 1200px | Slightly condensed desktop |
| Laptop | >= 1100px | Reduced column widths |
| Tablet Landscape | >= 960px | 2-column layouts begin collapsing |
| Tablet | >= 768px | Transition zone, some elements stack |
| Mobile Large | >= 720px | Near-tablet layout |
| Mobile | >= 480px | Single-column, stacked layout |
| Mobile Small | >= 376px | Minimum supported width |

### Collapsing Strategy
- **Navigation**: Horizontal links collapse to hamburger menu below 768px
- **Hero typography**: Scales from 112px → 72px → 48px → 38px across breakpoints, maintaining tight letter-spacing ratios
- **Grid layouts**: 3-column → 2-column at ~960px, single-column below 768px
- **Card grids**: Horizontal scrolling on mobile instead of wrapping (preserving card aspect ratios)
- **Section spacing**: Vertical padding reduces by ~40% on mobile (120px → 64px → 48px)
- **Button sizing**: CTA pills maintain padding but reduce font size; ghost buttons stay fixed
- **Code blocks**: Horizontal scroll with preserved monospace formatting

### Mobile-Specific Adjustments
- Full-bleed sections extend edge-to-edge with 16px internal gutters
- Touch targets: minimum 44px for all interactive elements
- Heading letter-spacing relaxes slightly at mobile sizes (less aggressive negative tracking)
- Image containers switch from fixed aspect ratios to full-width with auto height

---

## Agent Prompt Guide

### Quick Color Reference
- Background: `{colors.background}` (near-black canvas)
- Surface: `{colors.surface}` (elevated cards/containers)
- Border: `{colors.border-medium}` (visible) / `{colors.border-subtle}` (subtle)
- Text Primary: `{colors.ink}` (white on dark)
- Text Secondary: `{colors.ink-muted}` (silver on dark)
- Text Tertiary: `{colors.ink-subtle}` (medium gray)
- CTA: `{colors.primary}` (coral-red)
- Interactive: `{colors.interactive}` (electric blue, all hovers)
- Success: `{colors.accent-green}`
- Error: `{colors.error}`
- Light Surface: `{colors.surface-light}` / `{colors.surface-inverted}` (inverted sections)

### Example Prompts

**Landing page section:**
"Create a feature section with a near-black (`{colors.background}`) background. Use a 48px heading in waldenburgNormal with `-1.68px` letter-spacing, white text. Below it, 16px body text in `{colors.ink-muted}` with 1.50 line-height. Include a coral-red (`{colors.primary}`) pill button with white text and a secondary dark (`{colors.background}`) pill button with `{colors.ink-muted}` text. Both buttons hover to `{colors.interactive}` blue."

**Card grid:**
"Build a 3-column card grid on a `{colors.background}` background. Each card has a `{colors.surface}` surface, 1px solid `{colors.border-medium}` border, 6px border-radius, and 24px padding. Card titles are 24px white with `-0.24px` letter-spacing. Body text is 13px `{colors.ink-muted}`. Add a 13px IBM Plex Mono uppercase tag in `{colors.ink-subtle}` at the top of each card."

**Form section:**
"Design a contact form on a `{colors.background}` background. Inputs have `{colors.background}` background, 1px solid `{colors.border-subtle}` border, 3px border-radius, 8px 12px padding, and `{colors.ink-muted}` placeholder text. Focus state shows a 2px blue (`{colors.focus-ring}`) ring. Submit button is a full-width coral-red (`{colors.primary}`) pill. Include a 13px `{colors.ink-subtle}` helper text below each field."

**Navigation bar:**
"Create a sticky top navigation on `{colors.background}` with backdrop blur. Left: brand text in 15px white. Center/right: nav links in 16px `{colors.ink-muted}` that hover to blue. Far right: a coral-red (`{colors.primary}`) pill CTA button. Bottom border: 1px solid `{colors.border-subtle}`."

### Iteration Guide
1. **Start dark**: Begin with `{colors.background}` background, `{colors.ink}` primary text, `{colors.ink-muted}` secondary text
2. **Add structure**: Use `{colors.surface}` surfaces and `{colors.border-medium}` borders for containment — no shadows
3. **Apply typography**: waldenburgNormal (or Inter as a fallback) with tight letter-spacing on headings, 1.50 line-height on body
4. **Color punctuation**: Add `{colors.primary}` for CTAs and `{colors.interactive}` for all hover/interactive states
5. **Refine spacing**: 8px base unit, `xl`–`2xl` within sections, `4xl`–`6xl` between sections
6. **Technical details**: Add IBM Plex Mono uppercase labels for tags and metadata
7. **Polish**: Ensure all interactive elements hover to `{colors.interactive}`, all buttons are pills or subtle `{rounded.sm}` radius, borders are hairline (1px)
