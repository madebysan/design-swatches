---
version: alpha
name: "Bandcamp"
description: "Token-first design system reference for Bandcamp."

colors:
  background: "#ffffff"
  surface: "#222222"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#f8f8f8"
  primary: "#ffffff"
  on-primary: "#ffffff"
  border: "#0cacd7"
  focus-ring: "#ffffff"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Helvetica Neue, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Helvetica Neue, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Helvetica Neue, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Helvetica Neue, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Helvetica Neue, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Helvetica Neue, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Helvetica Neue, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Helvetica Neue, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  4xl: 96px

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 16px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.background}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    borderColor: "{colors.focus-ring}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  badge:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
---

# Bandcamp Design System

## Overview

Bandcamp's site is a museum of pre-Material-Design web design — a 2010-era marketplace that has refused, on principle, to be redesigned into Spotify. The page opens on pure white (`#ffffff`) with near-black text (`#222222`), dense album-cover grids stacked at 100×100px and 300×300px, and a single signature turquoise (`#0cacd7`) doing the work that an entire color system would do on a modern site. There is no hero illustration, no animated gradient, no scroll-jacked storytelling. The homepage is a directory: latest releases, genre tags, editorial picks, the fan feed. It looks like a record-store wall, and that is the point — the design is in service of music discovery, not brand storytelling.

The defining aesthetic is **functionality-first density**. Where contemporary sites use 80–120px of vertical rhythm between sections, Bandcamp uses 24–36px. Where modern marketplaces hide metadata behind progressive disclosure, Bandcamp surfaces it: artist name, album name, location, genre tag, time-since-release, all visible in the album card chrome. The 16px Helvetica Neue body sits at weight 400 on white, links are underlined and tinted with `--bc-link-color: #222` (yes, links default to dark with underline — Bandcamp predates the "links should be blue" web), and the turquoise accent is reserved for hover/focus rings, the play button, and the wordmark logo carrying its iconic vinyl-disc dot.

What distinguishes Bandcamp most is its **anti-redesign discipline**. The "Buy Digital Album" button is still a 4px-radius rectangle with a 1px solid border — the same button pattern from 2008, preserved because it works. Album-cover grids fill the viewport edge-to-edge with 1px gutters between thumbnails, treating each cover as a tile in a contact sheet rather than a card with its own shadow. The system feels editorial in the print sense: rigid grid, no decoration, type and image carrying everything. It's the rare modern site that reads as an artifact rather than a campaign.

**Key Characteristics:**
- Helvetica Neue weights 400 and 500 throughout — no display typeface, no custom font, no variable axis
- Pure white (`#ffffff`) page canvas with near-black (`#222222`) text — maximum contrast, zero softening
- Signature Bandcamp Turquoise (`#0cacd7`) for the wordmark, focus outlines, primary play affordances
- Underlined dark links (`#222` underlined) — links predate the "blue link" convention and stay dark on purpose
- Dense album-cover grids — 100×100, 200×200, 300×300 thumbnails packed with 1px gutters
- 4px and 16px border-radius — sharp UI surfaces with mid-radius hover cards, plus 50% circular play buttons
- 32px vertical button padding, 0px horizontal default — buttons stretch as wide as their content needs
- Compact spacing (5.5–12px) for chrome, generous (64–105px) only for genre showcase strips

## Colors

### Primary
- **Bandcamp Ink** (`#222222`): Primary text, headings, link color, button fills. Near-black, never pure black — softer than `#000` but still high-contrast.
- **Pure White** (`#ffffff`): Page background, card surfaces, button text on dark fills, the negative space holding the album grid.
- **Bandcamp Turquoise** (`#0cacd7`): The signature accent — wordmark logo, focus outlines, play-button glow, hover-state link tint. The single chromatic color in the system.

### Secondary
- **Off-White Surface** (`#f8f8f8`): Subtle panel background — used for sidebar shading, alternating-row backgrounds, hover-state surfaces. The 2nd most-used color after ink and white.
- **Editorial Mint** (`#ecf3f4`): The pale turquoise canvas behind the logo and editorial banners — a desaturated tint of the brand turquoise, used as a soft chromatic surface.

### Neutrals & Text
- **Bandcamp Ink** (`#222222`): Primary text, default link color, headings.
- **Mid Gray** (`#5d5d5d`): Secondary text — metadata, byline credits, "released by" annotations.
- **Caption Gray** (`#767676`): Tertiary text — timestamps, fan counts, micro-metadata.
- **Disabled Gray** (`#949494`): Disabled UI elements, muted controls in dark mode.
- **Hover Surface Tint** (`rgba(34, 34, 34, 0.08)`): Subtle dark wash applied to row hovers and search-input fills.
- **Page Text Secondary** (`rgba(34, 34, 34, 0.72)`): Lower-weight body text, label text in forms.

### Surface & Borders
- **Border Gray** (`#333333`): 1px solid borders on outline buttons (the "Buy" button family).
- **Default Border** (`#222222`): 1px solid borders on filled buttons and primary surfaces.
- **Soft Border** (`#888888`): Subtle dividers between content blocks.
- **Hairline** (`rgba(34, 34, 34, 0.08)`): 1px nav-bar bottom border — almost invisible.
- **Card Outline** (`rgba(34, 34, 34, 0.16)`): Light card borders on the fan-discovery feed.

### Status & Highlight
- **Highlight Yellow** (`#fce097`): Mark/highlight color — used for `<mark>` text in search results and editorial annotations. The only warm color in the system.
- **Error Red** (`#e50a0a`): Form error text, validation messages.

### Gradient System
- Bandcamp is **gradient-free**. The system uses solid color blocks, 1px borders, and the turquoise/white contrast to do all heavy lifting. The only "gradient" is the implicit one created by overlaying `rgba(34,34,34,0.08)` hover tints over white surfaces.

## Typography

### Font Family
- **Primary**: `Helvetica Neue`, fallback: `Arial`, `sans-serif`
- **Monospace / Technical**: Not used — Bandcamp does not have monospace UI text
- **Custom Display**: None. The wordmark is the only custom typography on the site, and it lives as an SVG logo.

*Note: Helvetica Neue is the system default Bandcamp leans on for its "this is a 2010-era web app" feel. For external implementations, Inter at weight 400/500 substitutes well. Avoid custom display faces — the workhorse-grotesk feel is the brand.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Heading | Helvetica Neue | 32px (2.00rem) | 500 | 1.40 | normal | Page-title H1 — "Discover", "Music", section heads |
| Section Heading | Helvetica Neue | 24px (1.50rem) | 500 | 1.50 | normal | Sub-section heads — "new releases", "fan favorites" |
| Sub-heading | Helvetica Neue | 16px (1.00rem) | 500 | 1.50 | normal | Card titles, album names |
| Sub-heading Bold | Helvetica Neue | 16px (1.00rem) | 700 | 1.50 | normal | Emphasized track titles, "now playing" labels |
| Eyebrow Label | Helvetica Neue | 16px (1.00rem) | 400 | 1.50 | 0.64px | Uppercase eyebrow — genre tags above album strips |
| Body | Helvetica Neue | 16px (1.00rem) | 400 | 1.50 | normal | Standard reading text, link copy |
| Button Label Lg | Helvetica Neue | 16px (1.00rem) | 500 | 1.00 | normal | Primary buttons — "Buy Digital Album", "Sign Up" |
| Body Small | Helvetica Neue | 14px (0.88rem) | 400 | 1.57 | normal | Album metadata, byline copy |
| Body Small Bold | Helvetica Neue | 14px (0.88rem) | 500 | 1.57 | normal | Album/track titles within compact rows |
| Button Label Sm | Helvetica Neue | 14px (0.88rem) | 400–500 | 1.00 | normal | Compact buttons — "play", "share", language picker |
| Caption | Helvetica Neue | 12.8px (0.80rem) | 400 | 1.88 | normal | Metadata footer text, "released by" annotations |
| Caption Small | Helvetica Neue | 12px (0.75rem) | 400 | 1.67 | normal | Track counts, time-since labels, micro-metadata |
| Caption Bold | Helvetica Neue | 12px (0.75rem) | 700 | 1.67 | normal | Emphasized small labels — fan counts, "supported by" |
| Micro Link | Helvetica Neue | 11px (0.69rem) | 400 | 1.82 | normal | Footer links, legal copy |

### Principles
- **Two weights only**: 400 and 500 carry 95% of the system. 700 appears sparingly for emphasis. There is no light weight, no display weight, no italics outside of editorial album-name treatments.
- **No letter-spacing on body**: All body and heading text runs at normal tracking. The only `letter-spacing` value (`0.64px`) is reserved for uppercase eyebrow labels — and even there it's a quiet 4% of the size.
- **Line-height varies by role, not size**: Headings run tight (1.40–1.50), body runs loose (1.50–1.88), and button labels are mechanical (1.00 — labels never wrap). The system distinguishes "reading" from "labeling" through line-height.
- **No display sizes**: 32px is the maximum heading size. Bandcamp does not do hero typography. The album covers are the hero.
- **Underlined links by default**: Links are `#222` with `text-decoration: underline` — a deliberate inheritance of pre-2010 web conventions. On hover, the underline stays and the color shifts to turquoise.

## Layout

### Spacing System
- Base unit: 8px nominal — but Bandcamp uses sub-grid values heavily (1px, 2px, 5.5px, 7.2px, 11px) for compact UI
- Scale: 1px, 2px, 5.5px, 7.2px, 8px, 10px, 11px, 12px, 16px, 20px, 24px, 36px, 64px, 100px, 105.6px
- Notable: The scale skews compact. Most spacing values land between 5–12px (chrome, gutters, padding). Generous values (64px+) only appear in genre-showcase strip spacing. Mid-range values (32–48px) are used sparingly — Bandcamp packs density.

### Grid & Container
- Max content width: ~1200px for primary content rails
- Album-cover grids: 4–6 columns desktop, 3 columns tablet, 2 columns mobile
- Discovery feed: dense alternating rows of album thumbnail (left) + metadata block (right) at ~120–150px row height
- Sidebar layouts: 240px sidebar + main content at 1024px breakpoint and up
- Full-bleed sections: rare — used only for editorial banner moments and the new-releases hero strip

### Whitespace Philosophy
- **Density-first**: Each section gets minimal vertical breathing room — 24–36px between major sections, 8–16px between rows within a section. The page is meant to feel like a record store wall, not a magazine spread.
- **Image-anchored rhythm**: Sections are paced by album-cover grids. The covers ARE the rhythm — a 6×6 grid of 200×200 thumbnails creates 36 visual beats with no need for decorative dividers.
- **No chapter breaks**: Bandcamp does not alternate light/dark sections. The page is uniformly white from top to bottom, with content blocks separated by hairline borders or simple section labels.

### Border Radius Scale
- Sharp (0px): Album-cover grid tiles, full-item buttons, dense list rows — the workhorse for image-heavy surfaces
- Compact (3–4px): Buttons, inputs, badges — the workhorse UI radius
- Mid (16px): Editorial discovery cards, fan-feed cards, pill-shaped tags
- Pill (50%): Circular play buttons, bundle badges, avatar crops
- No mid-large radii: Bandcamp does not use 6, 8, or 12px values. The system clusters around 4 and 16, with circles at 50%.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text, default cards, album-cover grid tiles |
| Hairline (Level 1) | `1px solid rgba(34, 34, 34, 0.08)` | Nav bottom border, section dividers, list-row separators |
| Outlined (Level 2) | `1px solid #222` or `1px solid rgba(34, 34, 34, 0.16)` | Buttons, inputs, outlined cards |
| Subtle Lift (Level 3) | `rgba(0, 0, 0, 0.1) 0px 1px 1px 0px` | Hover state on cards, dropdown panels |
| Focus Ring (Level 4) | `3px solid #0cacd7` outline | Keyboard focus on all interactive elements |

**Shadow Philosophy**: Bandcamp's depth system is essentially flat. The site predates the soft-shadow Material Design era and never adopted it. Where modern marketplaces use 4–8 elevation levels with progressively diffused shadows, Bandcamp uses a single 1px hairline shadow on hover and a 3px turquoise outline on focus — that's it. The visual layering comes from the 1px borders and the turquoise focus ring, not from blur radii. This is intentional: shadows would soften the editorial-print feel that Bandcamp guards.

### Decorative Depth
- The signature `3px solid #0cacd7` focus outline is the loudest depth signal in the system — a turquoise glow that announces "this element is focused" in the most direct way possible
- Inset borders (`2px inset #222`) appear on iframe embeds for the player widget — a deliberately retro 90s-window-chrome inset that signals "this is an embedded object, not part of the page"
- No ambient or glow effects on hover — the 1px shadow is the maximum lift the system permits

## Shapes

The complete radius scale is declared in the `rounded:` token block above.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Hard-edged brand moments and flush layouts |
| `sm` | 4px | Small controls and tight UI details |
| `md` | 8px | Inputs and compact interface elements |
| `lg` | 16px | Cards and larger containers |
| `pill` | 9999px | CTAs, chips, and rounded badges |

## Components

### Buttons

**Primary Filled (Ink)**
- Background: Bandcamp Ink (`#222222`)
- Text: Pure White (`#ffffff`)
- Padding: `0px 32px` (vertical sizing comes from line-height)
- Radius: `4px`
- Border: `1px solid #222222`
- Shadow: `none`
- Outline (focus): `3px solid #0cacd7`
- Font: 16px Helvetica Neue weight 500
- Use: Primary CTA — "Buy Digital Album", "Sign Up", "Follow Artist"

**Outline (Ghost)**
- Background: `transparent`
- Text: Bandcamp Ink (`#222222`)
- Padding: `0px 32px`
- Radius: `4px`
- Border: `1px solid #222222`
- Outline (focus): `3px solid #0cacd7`
- Font: 16px Helvetica Neue weight 500
- Use: Secondary CTA — "Wishlist", "Share", "Add to Cart"

**Compact Outline (Sm)**
- Background: `transparent`
- Text: Pure White (`#ffffff`) on dark, `#222` on light
- Padding: `0px 10px`
- Radius: `4px`
- Border: `1px solid #ffffff` (on dark) or `1px solid #222` (on light)
- Font: 14px Helvetica Neue weight 400
- Use: Dark-mode chrome buttons — language picker, currency selector, secondary nav

**Full-Item Button (Bare)**
- Background: Bandcamp Ink (`#222222`)
- Text: Pure White (`#ffffff`)
- Padding: `0px`, Radius: `0px`, Border: `0`
- Use: Full-row clickable areas in dense lists — entire row becomes the button

**Search Field Button (Inline Icon)**
- Background: `rgba(34, 34, 34, 0.08)`
- Text: White on dark, ink on light
- Padding: `0px 8px`
- Radius: `4px`
- Use: Inline search controls, language picker dropdowns

### Cards & Containers
- Background: `#ffffff` (default) or `#f8f8f8` (alternating rows)
- Border: `1px solid rgba(34, 34, 34, 0.16)` for outlined cards; `0` for grid-cell album covers
- Radius: `16px` for editorial discovery cards; `0px` for tiled album-cover grids; `4px` for compact components
- Shadow: `rgba(0, 0, 0, 0.1) 0px 1px 1px 0px` — a barely-there 1px lift on hover. No drop shadows on default state.
- Internal padding: tight — 8–16px for grid cells, 24–36px for editorial discovery cards

### Badges / Tags / Pills

**Filled Pill (Tag)**
- Background: Bandcamp Ink (`#222222`)
- Text: Pure White (`#ffffff`)
- Padding: `1px 16px`
- Radius: `16px` (fully pill-rounded)
- Border: `1px solid #222222`
- Font: 12px Helvetica Neue weight 400
- Use: Genre tags, format tags ("vinyl", "cassette"), filter chips

**Mid Gray Pill**
- Background: `#333333`
- Text: Pure White (`#ffffff`)
- Padding: `1px 16px`, Radius: `16px`
- Font: 16px Helvetica Neue weight 400
- Use: Larger filter chips on detail pages

**Bundle Badge (Circular)**
- Background: Pure White (`#ffffff`)
- Text: Bandcamp Ink (`#222222`)
- Border: `1px solid #888888`
- Radius: `50%`
- Font: ~7.6px weight 400
- Use: Tiny count indicators on bundle/merch thumbnails

### Inputs & Forms

**Search Input**
- Background: `rgba(34, 34, 34, 0.08)` — subtle dark wash on white
- Text: Bandcamp Ink (`#222222`)
- Border: `0`
- Radius: `3px`
- Padding: `5px 10px 5px 38px` (left padding accommodates search icon)
- Outline (focus): `3px solid #0cacd7`

**Email Input**
- Background: `rgba(255, 255, 255, 0.16)` (semi-transparent on dark)
- Text: Bandcamp Ink (`#222222`)
- Border: `1px solid rgba(34, 34, 34, 0.72)`
- Radius: `3px`
- Padding: `5px 10px`
- Outline (focus): `3px solid #0cacd7`

**Textarea**
- Background: `#ffffff`
- Border: `1px solid #c1c1c1`
- Padding: 8–12px
- Font: 14px Helvetica Neue weight 400

### Navigation
- Top nav: white bar, ~48px tall, left-aligned wordmark logo (turquoise dot + dark text), center search input, right-aligned account/cart links
- Bottom border: `1px solid rgba(34, 34, 34, 0.08)` — almost invisible hairline
- Links: 16px Helvetica Neue weight 400, color `#222`, no underline in nav (underline is reserved for body links)
- Hover: link color shifts to turquoise `#0cacd7`, no underline appears
- Sticky: nav remains fixed on scroll, content scrolls beneath

### Decorative Elements

**Album Cover Grid Tile**
- Square aspect (1:1), edge-to-edge in container with 1px gutters
- Sizes: 100×100 (compact), 200×200 (default), 300×300 (featured)
- No border, no shadow, no radius — the cover image IS the surface
- Hover: subtle play-button overlay appears centered, with turquoise glow

**Play Button (Circular)**
- Background: Bandcamp Ink (`#222222`) or Pure White (`#ffffff`)
- Radius: `50%`
- Size: 24–48px depending on context
- Triangle icon centered, in turquoise (`#0cacd7`) on white, or white on dark
- Hover: turquoise outline glow `3px solid #0cacd7`

**Wordmark Logo**
- SVG, 120×19px proportions
- Dark text "bandcamp" with the dot above the "i" replaced by a turquoise (`#0cacd7`) vinyl disc
- Sits on the editorial mint background (`#ecf3f4`) in nav, or pure white in body content

## Do's and Don'ts

### Do
- Use Helvetica Neue weights 400 and 500 for everything — the workhorse-grotesk feel is the brand
- Apply Bandcamp Turquoise (`#0cacd7`) only to focus states, the wordmark, play affordances, and link hovers
- Use 4px radius for buttons and inputs, 16px radius for editorial cards, 50% for circles, 0px for image grids
- Underline body links by default — links stay dark (`#222`) underlined, hover shifts to turquoise
- Pack density on listing pages — 24–36px between sections, 8–16px between rows
- Use the 3px solid turquoise outline for keyboard focus on every interactive element
- Use the 1px hairline shadow `rgba(0, 0, 0, 0.1) 0px 1px 1px 0px` for subtle hover lift on cards
- Use uppercase eyebrow labels with `letter-spacing: 0.64px` for genre tags above strips
- Treat album covers as the hero — let them fill the grid edge-to-edge with 1px gutters

### Don't
- Don't introduce light weight (300) or display weight (700+ display-size) — the system is 400/500 only
- Don't use blue (`#0066cc` or similar) for links — Bandcamp links are `#222` underlined, not "web blue"
- Don't add gradient fills, animated gradients, or glassmorphism — the system is solid-color flat
- Don't use blurred drop shadows for elevation — the system is flat with 1px hairlines
- Don't add hero illustrations or animated backgrounds — album covers carry all visual interest
- Don't use pure black (`#000`) for text — always `#222`, slightly softer
- Don't introduce new chromatic colors — turquoise is the only chromatic, plus yellow `#fce097` for highlights only
- Don't redesign the buttons. Seriously. The 4px-radius outline button is sacred — it's been the same since 2008
- Don't space sections with 80px+ vertical padding — Bandcamp is dense, not editorial-airy

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <650px | Single-column album list, 2-col cover grid, stacked nav |
| Tablet | 650–1000px | 3-column cover grid, condensed nav, sidebar collapses |
| Desktop | 1000–1280px | 4-column cover grid, full nav with search, sidebar appears |
| Large Desktop | ≥1280px | 5–6 column cover grid, max content width 1200px, full discovery layout |

### Touch Targets
- Primary buttons: min 36px tap height (vertical padding from line-height)
- Album cover tiles: minimum 100×100 on mobile, 200×200+ on desktop
- Nav links: 44px tap area enforced through padding
- Play buttons: 48px circle on touch, 32px on desktop hover

### Collapsing Strategy
- **Nav**: Horizontal nav bar collapses to hamburger on mobile; account/cart icons remain visible
- **Album grids**: 6-col → 4-col → 3-col → 2-col progression across breakpoints
- **Sidebar**: Genre/discovery sidebar disappears below 1000px, accessible via filter sheet
- **Cards**: Editorial discovery cards stack vertically on mobile, with metadata moving below cover
- **Section spacing**: 36px desktop → 24px mobile — already tight, gets tighter
- **Type scale**: 32px → 24px → 20px progressive heading scale, weights preserved

### Image Behavior
- Album covers maintain 1:1 aspect at all sizes — never cropped, never letterboxed
- Cover thumbnails preload at 100×100 and lazy-load full-resolution on hover/scroll
- Hero album of the day: full-width banner on desktop, square cover on mobile
- No art direction changes — same square covers everywhere, just different sizes

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Text: Bandcamp Ink (`#222222`)
- Page Background: Pure White (`#ffffff`)
- Brand Accent: Bandcamp Turquoise (`#0cacd7`)
- Surface Tint: Off-White (`#f8f8f8`)
- Logo Background: Editorial Mint (`#ecf3f4`)
- Secondary Text: Mid Gray (`#5d5d5d`)
- Caption Text: Caption Gray (`#767676`)
- Border: `#222222` or `rgba(34, 34, 34, 0.16)`
- Highlight: Yellow (`#fce097`)
- Error: Red (`#e50a0a`)
- Focus Outline: `3px solid #0cacd7`

### Example Component Prompts
- "Create a primary button on white background — 16px Helvetica Neue weight 500, white text on `#222` fill, `4px` border-radius, `1px solid #222` border, `0px 32px` padding. On focus, add `3px solid #0cacd7` outline."
- "Build an album-cover grid — 6 columns at desktop, square 200×200 thumbnails, 1px gutters, no border-radius on the tiles, no shadow. Hover: overlay a 48px circular play button (`#222` fill, white triangle, `3px solid #0cacd7` outline glow) centered on the cover."
- "Design a fan-discovery card — `#ffffff` background, `1px solid rgba(34, 34, 34, 0.16)` border, `16px` border-radius, 24px internal padding. Album title in 16px Helvetica Neue weight 500 `#222`, artist name in 14px weight 400 `#5d5d5d`, genre pill below in `#222` fill with white 12px text, `16px` pill radius."
- "Create a search input — `rgba(34, 34, 34, 0.08)` background, no border, `3px` border-radius, `5px 10px 5px 38px` padding (38px left for search icon). Focus state: `3px solid #0cacd7` outline."
- "Build the nav bar — white background, `1px solid rgba(34, 34, 34, 0.08)` bottom border, ~48px tall. Wordmark logo on the left (turquoise dot, dark text) on `#ecf3f4` mint background. Center search input. Right-aligned account links — 16px Helvetica Neue weight 400 `#222`, no underline. Hover shifts color to `#0cacd7`."
- "Style body links as `#222` with `text-decoration: underline`. On hover, color shifts to `#0cacd7`, underline stays. This is the Bandcamp link convention — do not use blue."

### Iteration Guide
1. Default to Helvetica Neue weight 400 for body, 500 for headings/buttons. No light, no display weights.
2. Page is white (`#ffffff`), text is `#222222` — never softer, never pure black.
3. Turquoise (`#0cacd7`) is sacred — only on focus rings, the wordmark, play affordances, and link hover.
4. Border-radius is binary-ish: 4px for UI chrome, 16px for editorial cards, 50% for circles, 0px for image grids.
5. Links are `#222` with underline. Do not introduce blue links — that breaks the Bandcamp convention.
6. Pack density: 24–36px between sections, 8–16px between rows. Avoid 80px+ section spacing.
7. Use the 3px turquoise outline for keyboard focus on every interactive element — never remove it.
8. Album covers are the hero. Let them fill grids edge-to-edge with 1px gutters and no chrome.
9. Shadows are flat — `0 1px 1px 0 rgba(0,0,0,0.1)` is the maximum elevation. No blurred drop shadows.
10. When in doubt, ask: "would this fit on Bandcamp circa 2012?" If yes, ship it. If it screams "redesigned in 2024," reconsider.
