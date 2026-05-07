---
version: alpha
name: "Rivian"
description: "Token-first design system reference for Rivian."

colors:
  background: "#ffffff"
  surface: "#ffac00"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#f6f6f6"
  primary: "#1f2121"
  on-primary: "#ffffff"
  border: "#f2f2f2"
  focus-ring: "#1f2121"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 88px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 61px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 44px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
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

# Rivian Design System

## Overview

Rivian's website is an expedition magazine rendered as an EV configurator. Where most automakers default to studio renders on white seamless paper, Rivian shoots its trucks on actual roads — leaf-dappled suburban streets, alpine switchbacks, desert washes — and lets the photograph do the heavy work. The interface around the photography is unusually quiet: a custom display typeface called `Adventure`, a deep near-black slate (`#1F2121`) for primary text, and a single saturated golden-yellow (`#FFAC00`) reserved almost exclusively for the primary CTA. The result is an outdoor magazine aesthetic that feels closer to Filson or Patagonia than to Tesla or Lucid.

The signature move is the **pill-shaped golden CTA** in the top-right of the navigation. While the rest of the system runs in restrained near-black and warm off-whites, that one button — labeled "Order now" or "Reserve" — glows in `#FFAC00` and locks attention immediately. Rivian uses this color the way a magazine uses a single die-cut sticker: rare, high-saturation, unmissable. The same yellow shows up sparingly on accent moments (vehicle wheel detailing, badge highlights, focus states) but never dilutes — it remains the brand's stamp of action.

Compositionally, Rivian leans hard into **photo-led storytelling with editorial captions**. Hero sections are full-bleed environmental photography (a couple loading an R1S in a driveway, a truck on a coastal road, a Quad-Motor charging at a Rivian Adventure Network station) overlaid with a small left-aligned text block: a tight headline in `Adventure`, two lines of body copy, and one or two pill buttons. There are no decorative gradients, no scrim overlays softening the imagery — the photograph is presented honestly, and text is positioned where it has natural negative space to land. Below the hero, the page runs through alternating dark and light sections, generous white space, and oversized Adventure-typeset model names (R1T, R1S) that act as chapter dividers.

**Key Characteristics:**
- Custom `Adventure` display typeface for all hero and section headings — geometric, slightly humanist, unmistakable
- Saturated golden-yellow (`#FFAC00`) reserved for the primary "Order now" CTA — the stamp of the system
- Deep slate near-black (`#1F2121`) for primary text — softer than pure `#000` but still high-contrast
- Warm off-white canvases (`#F2F2F2`, `#F6F6F6`) alternating with full-bleed environmental photography
- Photo-led hero compositions with no scrims or gradient overlays — trust in the image
- Pill-shaped (fully rounded) CTAs sit alongside square content cards — soft action, hard structure
- Oversized model-name typography (R1T, R1S) as chapter markers between sections
- Outdoor / expedition photography style — cars in lived environments, never floating in studios

## Colors

### Primary
- **Rivian Slate** (`#1F2121`): Primary text, headings, body copy, dark-section backgrounds. A near-black with a slight green-gray undertone — never pure `#000`.
- **Rivian Bone** (`#F6F6F6`): Default page canvas. A warm off-white that reads as natural paper rather than screen.
- **Rivian Mist** (`#F2F2F2`): Slightly cooler off-white used for alternate sections, card surfaces, and panel backgrounds.

### Brand Accent
- **Rivian Yellow** (`#FFAC00`): The signature golden-yellow — applied to the primary "Order now" CTA, occasional badge highlights, focus indicators, and decorative micro-moments. The only saturated color in the system.
- **Rivian Ember** (`#E84826`): A warm orange-red used for occasional alerts, sale tags, and high-attention status moments. Used sparingly.

### Neutrals & Text
- **Slate Primary** (`#1F2121`): All primary text — headings, body, nav links, button labels on light surfaces.
- **Slate Deep** (`#151515`): Deepest near-black for full-bleed dark sections and footer surfaces.
- **Carbon** (`#212121`): A near-twin to slate, used on dark cards and overlay panels.
- **Graphite** (`#333333`): Secondary text, captions, metadata on light surfaces.
- **Stone** (`#606060`): Tertiary text, fine print, disabled states.

### Surface & Borders
- **Surface Bone** (`#F6F6F6`): Default panel background — matches page canvas.
- **Surface Mist** (`#F2F2F2`): Alternate panel background for tonal sectioning.
- **Surface Carbon** (`#252826`): Dark card and panel surface — used on inverted sections.
- **Border Hairline** (`rgba(31, 33, 33, 0.12)`): Subtle dividers between content rows.

### Atmospheric / Photographic
- **Sky Pale** (`#77AFD8`): Soft blue extracted from atmospheric photography — used for occasional informational icons and ambient highlights.
- **Slate Steel** (`#8BA8BD`): Cool blue-gray for infographic accents, charging-network maps, and quiet UI moments.
- **Stone Tan** (`#BC9C8A`): Warm desert-tone accent for occasional landscape callouts.
- **Forest** (`#629B5C`): A muted green pulled from environmental photography — used for trail/route indicators.

### Gradient System
- Rivian is **gradient-free on chrome**. The system relies on solid-color relationships and the photographic backdrops carry all the chromatic richness. The only "gradients" in the experience are the natural ones inside the photography itself.

## Typography

### Font Family
- **Display**: `Adventure`, with fallback: `HelveticaNeue`, `Helvetica Neue`, `Helvetica`, `Arial`, `sans-serif`
- **Editorial / Serif Moments**: `Canela` — used sparingly for occasional editorial pull-quotes and brand-storytelling moments
- **OpenType Features**: Standard ligatures, with tabular figures enabled inside specs tables

*Note: `Adventure` is Rivian's custom commercial display typeface. For external implementations, `Söhne` (geometric humanist), `Inter` (web-safe), or `GT America` serve as close substitutes. `Canela` is from Commercial Type — `Canela Deck` is the most accessible licensable variant.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero (Model Name) | Adventure | 88px (8.8rem) | 500 | 1.00 (88px) | -0.02em | Model name chapter dividers (R1T, R1S) |
| Display Large | Adventure | 64px (6.4rem) | 500 | 1.06 (6.8rem) | -0.02em | Primary section heroes |
| Display | Adventure | 52px (5.2rem) | 500 | 1.07 (5.6rem) | -0.02em | Feature section titles |
| Section Heading | Adventure | 44px (4.4rem) | 500 | 1.09 (4.8rem) | -0.02em | Sub-section heads |
| Sub-heading Large | Adventure | 36px (3.6rem) | 500 | 1.11 (4rem) | -0.01em | Card titles, feature heads |
| Sub-heading | Adventure | 32px (3.2rem) | 500 | 1.06 (3.4rem) | -0.01em | Smaller section heads |
| Sub-heading Small | Adventure | 24px (2.4rem) | 500–600 | 1.17 (2.8rem) | normal | Card headings, callouts |
| Body Large | Adventure | 18px (1.8rem) | 400 | 1.44 (2.6rem) | normal | Intro paragraphs, hero descriptions |
| Body | Adventure | 16px (1.6rem) | 400 | 1.50 (2.4rem) | normal | Standard reading text |
| Body Small | Adventure | 14px (1.4rem) | 400 | 1.43 (2rem) | normal | Captions, secondary descriptions |
| Nav Link | Adventure | 16px (1.6rem) | 500 | 1.00 | normal | Top navigation links |
| Button UI | Adventure | 16px (1.6rem) | 500–600 | 1.00 | normal | Pill button labels, CTAs |
| Caption | Adventure | 12px | 400 | 1.33 | normal | Disclaimers, fine print |

### Principles
- **Adventure as the brand voice**: The custom typeface carries the entire identity. Every display, heading, and body line runs in Adventure — there is no separate body family.
- **Weight 500 as the heading default**: Headings live at weight 500, never 700/bold. Rivian's hierarchy comes from size and tracking, not weight.
- **Tight negative tracking on display**: Letter-spacing tightens to `-0.02em` at 36px+ display sizes. Below 24px, tracking returns to normal for readability.
- **Generous line-height on body**: Body copy runs at 1.44–1.50 line-height — deliberately airy, reflecting the editorial pacing of the visual system.
- **Title case for headlines**: "Designed for adventure", "Keep exploring" — sentence-case or title-case rather than uppercase. The lone uppercase moment is button micro-labels and legal chrome.
- **Oversized model names**: R1T and R1S appear at 88px+ as visual punctuation between sections — the type itself is the brand signal.

## Layout

### Spacing System
- Base unit: 8px
- Scale: 4px, 6px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px
- Notable: Most spacing aligns to 8px. The `gap: 6px` exception appears only in tight inline UI (badge clusters, icon+label pairs).

### Grid & Container
- Max content width: 1440px outer, 1280px inner content
- Hero: full-bleed photography with overlaid text block left-aligned, max-width 480–560px
- Feature sections: 12-column grid; commonly used as 2-column (image + copy) or 3-column (feature triads)
- Full-bleed dark sections alternate with off-white canvases for chapter-like rhythm
- Photography routinely breaks the container for cinematic effect

### Whitespace Philosophy
- **Editorial pacing**: Major sections separated by 96–128px on desktop, 48–64px on mobile
- **Hero breathing room**: Hero text blocks sit with 64–96px of vertical air above and below
- **Tonal sectioning**: Off-white sections alternate with full-bleed dark or imagery sections — creating chapter breaks without decorative dividers
- **Copy density**: Body paragraphs run at 1.50 line-height with 24px paragraph spacing — closer to magazine layout than typical web density

### Border Radius Scale
- Sharp small (`8px`): Content cards, form inputs, image crops
- Soft medium (`16px`): Feature panels, larger cards, modal dialogs
- Pill (`9999px`): All buttons, all badges, all status indicators
- No large mid-range radii: Rivian doesn't use 24–48px radii. The system reads as "pill or panel" — fully round or gently soft.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, body text, structural containers |
| Surface (Level 1) | `0 1px 2px rgba(0,0,0,0.04)` | Default cards on light surfaces |
| Lifted (Level 2) | `0 4px 16px rgba(0,0,0,0.06)` | Hovered cards, dropdown menus |
| Floating (Level 3) | `0 12px 32px rgba(0,0,0,0.10)` | Modal dialogs, full-screen overlays |
| Focus Ring | `0 0 0 3px rgba(255, 172, 0, 0.24)` | Keyboard focus on interactive elements |

**Shadow Philosophy**: Rivian uses depth sparingly. Most sections rely on tonal contrast (off-white vs. dark slate vs. photography) rather than drop shadows. When elevation is needed, shadows stay soft and low-spread — never dramatic. The signature elevation cue is actually the **photographic backdrop** itself: when a button or card sits over a real-world image, the inherent depth of the photo provides all the dimensionality the composition needs.

### Decorative Depth
- Cards on photography use a subtle backdrop-blur (`backdrop-filter: blur(20px)`) plus 70% opacity background to maintain legibility without disrupting the image
- Inverted dark cards on light pages use no shadow — just the tonal jump
- Focus states ring in yellow `#FFAC00` at 24% opacity — high-visibility for keyboard users without breaking the chrome

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

**Primary Yellow Pill**
- Background: Rivian Yellow (`#FFAC00`)
- Text: Rivian Slate (`#1F2121`)
- Padding: 12px 24px
- Radius: `9999px` (fully rounded pill)
- Border: none
- Shadow: none — the saturation does the work
- Font: 16px Adventure weight 500–600
- Hover: brightness `0.96`, translate `0 -1px` for subtle lift
- Use: Primary CTA only — "Order now", "Reserve", "Shop"

**Slate Pill**
- Background: Rivian Slate (`#1F2121`)
- Text: Pure White (`#FFFFFF`)
- Padding: 12px 24px
- Radius: `9999px`
- Hover: background shifts to `#333333`
- Use: Secondary primary CTA — "Build your R1S", "Learn more" on light backgrounds

**Outline Pill**
- Background: transparent
- Text: Rivian Slate (`#1F2121`) on light, `#FFFFFF` on dark
- Border: `1px solid currentColor`
- Radius: `9999px`
- Padding: 12px 24px
- Hover: fills with current color, inverts text
- Use: Tertiary actions, "View offers", inline secondary CTAs over imagery

**Inverted White Pill**
- Background: Pure White (`#FFFFFF`)
- Text: Rivian Slate (`#1F2121`)
- Radius: `9999px`
- Use: Primary CTA when overlaid on dark photography (where yellow would clash)

### Cards & Containers
- Background: `#F6F6F6` or `#F2F2F2` on light sections; `#252826` or `#1F2121` on dark sections
- Border: none — cards rely on tonal contrast and generous padding
- Radius: `8px` for content cards, `16px` for feature panels, `9999px` for buttons only
- Shadow: rarely used — when present, very soft `0 2px 16px rgba(0,0,0,0.06)` for subtle elevation
- Internal padding: 24–48px depending on density; feature cards run 48–64px

### Badges / Tags / Pills
**Yellow Stamp Badge**
- Background: Rivian Yellow (`#FFAC00`)
- Text: Rivian Slate (`#1F2121`)
- Padding: 4px 10px
- Radius: `9999px`
- Font: 12px Adventure weight 500
- Use: "Limited time", "New", emphasis tags on offer panels

**Outline Badge**
- Background: transparent
- Text: current color
- Border: `1px solid currentColor`
- Radius: `9999px`
- Padding: 4px 10px
- Use: Category markers, "Quad-Motor", "Adventure Package"

### Inputs & Forms
- Background: `#FFFFFF` on light surfaces, `#252826` on dark
- Border: `1px solid rgba(31, 33, 33, 0.16)`
- Radius: `8px`
- Font: 16px Adventure weight 400
- Text color: `#1F2121`
- Focus: border shifts to `#FFAC00`, soft ring `0 0 0 3px rgba(255, 172, 0, 0.24)`
- Padding: 14px 16px

### Navigation
- Top nav: horizontal bar over a transparent or off-white background, left-aligned wordmark logo, center-aligned model/category links (Vehicles, Charging, Technology, Discover, Gear Shop), right-aligned yellow "Order now" pill CTA
- Hover menus: full-width drop panels with multi-column layouts — vehicle thumbnails, accessory categories, technology subsections
- Links: Adventure 16px weight 500, color `#1F2121` on light / `#FFFFFF` on dark
- Hover: underline animates from left to right under the link
- Sticky behavior: nav stays fixed during scroll; background fades from transparent to `#F6F6F6` once user scrolls past hero

### Decorative Elements

**Full-Bleed Environmental Photography**
- Hero photographs run edge-to-edge with no scrim, vignette, or gradient overlay
- Text overlays (small headline + 2-line body + pill CTA) sit in natural negative space within the composition
- Photography style: real environments, golden-hour lighting, lived-in mise-en-scène, no studio cyclorama

**Oversized Model Wordmarks**
- "R1T" and "R1S" rendered at 88–120px in Adventure weight 500 act as chapter dividers
- Often paired with a small subtitle ("Adventure SUV", "All-electric truck") in 16px body weight

## Do's and Don'ts

### Do
- Use Adventure for every display, heading, and body size — it's the entire voice
- Reserve `#FFAC00` for the primary CTA and rare emphasis — one or two applications per screen maximum
- Lead with full-bleed environmental photography — real places, real light, real lived-in scenes
- Use pill (`9999px`) radius for every button — sharp-cornered buttons break the brand
- Keep heading weight at 500 — never bold
- Pair tight letter-spacing (`-0.02em`) with generous line-height (`1.50` body) — type contrast through tracking and air
- Alternate off-white sections (`#F6F6F6`, `#F2F2F2`) with full-bleed dark or photographic sections for chapter pacing
- Let the photograph carry the emotion — the chrome stays quiet
- Use oversized model names (R1T, R1S) at 88px+ as visual punctuation between sections
- Use `#1F2121` slate near-black for primary text — softer and warmer than `#000`

### Don't
- Don't use pure `#000` for primary text — Rivian Slate (`#1F2121`) is the correct near-black
- Don't introduce gradient scrims or vignettes over photography — the image stands alone
- Don't square-corner buttons — pill (`9999px`) radius is non-negotiable for actions
- Don't mid-range radius (24–48px) — the system is binary: small panel radius or full pill
- Don't saturate the yellow — `#FFAC00` is a stamp, never a wash; never use it for full backgrounds
- Don't introduce a second display typeface — Adventure carries everything
- Don't use weight 700 on Adventure — 500 is the ceiling for headings, 600 for emphasized CTA labels
- Don't shoot product on cyclorama / seamless white — environmental photography is the brand
- Don't use uppercase for headlines — sentence-case or title-case is the convention
- Don't pile drop shadows for depth — Rivian uses tonal contrast and photography for dimensionality

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero type drops to 36–44px |
| Mobile | 375–767px | Single-column, 44–52px hero, stacked CTAs |
| Tablet | 768–1023px | 2-column grids begin, 56–64px hero |
| Desktop | 1024–1439px | Full multi-column layouts, 72–80px hero |
| Large Desktop | ≥1440px | Maximum type scale (88px+ display), 1280px content container |

### Touch Targets
- Primary pill CTAs: min 44px tap height, 24px horizontal padding on mobile
- Nav links: 48px tap area with 12–16px label padding
- Tertiary outline pills: 40px tap height minimum

### Collapsing Strategy
- **Nav**: Horizontal link bar collapses to hamburger menu on mobile; full-screen overlay menu with vehicle thumbnails on open. Yellow "Order now" pill remains visible at all breakpoints.
- **Hero**: 88px → 64px → 52px → 44px progressive scaling across breakpoints, weight 500 maintained throughout
- **Feature sections**: 2-column image+copy collapses to stacked image-on-top, copy-below
- **Photography**: Full-bleed treatment preserved; aspect ratio shifts from 16:9 to 4:3 or 1:1 on narrow viewports for vertical compositions
- **Section spacing**: 128px desktop → 64px tablet → 48px mobile — reduces but maintains editorial pacing
- **Letter-spacing**: Tracking stays proportionally tight at all breakpoints

### Image Behavior
- Environmental photography maintains full-bleed treatment on mobile
- Art direction adapts: landscape compositions on desktop swap for portrait crops on mobile
- Vehicle hero shots reframe to keep the truck centered on narrow screens
- Adventure Network maps simplify to key markers only on small viewports

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Rivian Yellow (`#FFAC00`)
- Page Background: Rivian Bone (`#F6F6F6`)
- Alt Background: Rivian Mist (`#F2F2F2`)
- Primary Text: Rivian Slate (`#1F2121`)
- Dark Surface: Slate Deep (`#151515`) or Carbon (`#212121`)
- Inverted Text: Pure White (`#FFFFFF`)
- Focus Ring: `0 0 0 3px rgba(255, 172, 0, 0.24)`
- Subtle Border: `rgba(31, 33, 33, 0.12)`

### Example Component Prompts
- "Create a hero section with a full-bleed environmental photograph (no scrim or gradient overlay). Overlay a left-aligned text block at 480px max-width: headline at 64px Adventure weight 500, line-height 1.06, letter-spacing -0.02em, color `#FFFFFF`. Below the headline, two lines of body copy at 18px Adventure weight 400, line-height 1.44. Add a Rivian Yellow (`#FFAC00`) pill CTA — `9999px` radius, 12px 24px padding, 16px Adventure weight 500–600, text color `#1F2121`."
- "Design a feature card on `#F6F6F6` with `16px` border-radius, no border, soft shadow `0 4px 16px rgba(0,0,0,0.06)` on hover. Title in Adventure 36px weight 500, letter-spacing `-0.01em`. Body in Adventure 16px weight 400, line-height 1.50. Internal padding 48px."
- "Build an alternating page section: off-white canvas at `#F6F6F6` followed by a full-bleed dark section at `#1F2121` with environmental photography. Each section gets 96–128px vertical padding. Between sections, place an oversized model name 'R1T' at 88px Adventure weight 500 as a chapter divider, color `#1F2121` on light, `#FFFFFF` on dark."
- "Create a top navigation bar — transparent background that fades to `#F6F6F6` on scroll. Left-aligned Rivian wordmark logo, center-aligned 5 nav links (Vehicles, Charging, Technology, Discover, Gear Shop) at 16px Adventure weight 500 color `#1F2121`. Right-aligned yellow pill CTA labeled 'Order now' at `#FFAC00` background with `#1F2121` text, `9999px` radius, 12px 24px padding."
- "Design an outline pill badge — transparent background, `1px solid #1F2121`, `9999px` radius, 12px Adventure weight 500 text in `#1F2121`, padding 4px 10px. Use for category markers like 'Quad-Motor' or 'Adventure Package'."

### Iteration Guide
1. Default to Adventure typeface for everything — display, heading, body. No second family unless using Canela for an editorial pull-quote moment.
2. Use weight 500 for headings, weight 400 for body, weight 500–600 for button labels. Never weight 700.
3. Keep button radius at `9999px` — fully rounded pills only. Square buttons break the brand.
4. Yellow `#FFAC00` is sacred — one primary CTA per screen, plus rare badge moments. Never use it as a background fill or wash.
5. Lead every page section with environmental photography — real places, golden-hour light, lived-in scenes. No studio renders.
6. Negative letter-spacing scales with size: `-0.02em` at 36px+, `-0.01em` at 24–32px, normal at body.
7. Pair tight tracking on display with generous body line-height (1.44–1.50) — the brand's editorial breath.
8. Slate near-black `#1F2121` is the correct primary text color, not `#000`. The slight green-gray undertone is the brand.
9. Sections alternate between off-white (`#F6F6F6`) and full-bleed photographic/dark — let tonal contrast pace the page, not decorative dividers.
10. Trust the photograph. Don't add scrims, vignettes, or gradient overlays — Rivian's confidence is in the image.
