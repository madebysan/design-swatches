---
version: alpha
name: Arc Browser
description: Cream-paper canvas, electric Arc Blue at full-bleed scale, restrained 2–3-color gradient mesh atmosphere, frosted glass panels, and Marlin Soft SQ display typography.

colors:
  # Surfaces — paper-warm canvas
  background: "#fffcec"
  background-warm: "#fffadd"
  surface: "#ffffff"

  # Brand blues
  primary: "#3139fb"
  primary-deep: "#2702c2"
  brand-dark: "#000354"

  # Ink + text
  ink: "#000000"
  ink-inverted: "#ffffff"
  on-background: "#000000"
  on-surface: "#000000"
  on-primary: "#ffffff"
  text-secondary: "#595959"  # was rgba(0,0,0,0.65) — flattened over cream
  text-placeholder: "#696969"

  # Mesh blooms — restrained pastels
  mesh-peach: "#f5e4d8"
  mesh-butter: "#f6ecd2"
  mesh-mint: "#dce8df"
  mesh-violet: "#e3dcf2"

  # Muted accents — one per surface
  accent-coral: "#d86a73"
  accent-salmon: "#e8c8b8"
  accent-olive: "#cfd8a8"
  accent-periwinkle: "#c8cadc"
  accent-pink-pop: "#f25e6b"
  accent-red: "#d64050"

  # Teal scale
  teal-1: "#00eae7"
  teal-3: "#00a39f"
  teal-7: "#003828"

  # Interactive
  focus-ring: "#96c4ff"
  hover-overlay: "#8b89c1"  # was rgba(23,3,148,0.5) — flattened over cream

  # Glass + borders (opaque approximations)
  glass-cream: "#faf6e3"  # was rgba(255,252,236,0.6) — flattened over white
  glass-dark: "#1a2057"  # was rgba(0,3,84,0.35) — flattened over white
  border-soft: "#ebebeb"  # was rgba(0,0,0,0.08) — flattened over cream
  border-tinted: "#d6d8fc"  # was rgba(49,57,251,0.2) — flattened
  shadow-soft: "#e6e6e6"  # was rgba(0,0,0,0.1) — flattened

typography:
  hero-display:
    fontFamily: "Marlin Soft SQ, Marlin, -apple-system, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: 45.5px
    fontWeight: 700
    lineHeight: 0.93
    letterSpacing: -1.82px
  display-large:
    fontFamily: "Marlin Soft SQ, Marlin, -apple-system, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 0.97
    letterSpacing: -1.6px
  display-mid:
    fontFamily: "Exposure VAR, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.72px
  heading:
    fontFamily: "Marlin, Marlin Soft SQ, -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 0.97
    letterSpacing: -1.6px
  editorial-large:
    fontFamily: "ABC Oracle, Helvetica, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0px
  editorial:
    fontFamily: "ABC Oracle, Helvetica, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0px
  ui-heading:
    fontFamily: "InterVariable, Inter, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  link-strong:
    fontFamily: "InterVariable, Inter, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Marlin, Marlin Soft SQ, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  nav-link:
    fontFamily: "Marlin Soft SQ, Marlin, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  meta:
    fontFamily: "Marlin Soft SQ, Marlin, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: -0.28px
  button-ui:
    fontFamily: "-apple-system, system-ui, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 2.07
    letterSpacing: -0.14px
  micro-link:
    fontFamily: "InterVariable, Inter, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.4px

spacing:
  micro: 3px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 72px
  4xl: 80px
  5xl: 128px
  6xl: 160px

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 10px
  lg: 12px
  xl: 22px
  pill: 9999px

components:
  # Sticky cream nav with subtle blur
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.md}"
    padding: 16px 24px

  # Primary solid button on cream
  button-primary:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.md}"
    padding: 8px 20px

  # Inverse button on Arc Blue
  button-inverse:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-deep}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.md}"
    padding: 8px 20px

  # Glass button on gradient mesh
  button-glass:
    backgroundColor: "{colors.glass-cream}"
    textColor: "{colors.brand-dark}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.xl}"
    padding: 8px 20px

  # Mesh-blend CTA — replaces rainbow conic
  button-mesh:
    backgroundColor: "{colors.mesh-violet}"
    textColor: "{colors.brand-dark}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.xl}"
    padding: 8px 20px

  # Card — standard
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 24px

  # Comfortable card
  card-comfortable:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px

  # Hero / featured glass card
  card-featured:
    backgroundColor: "{colors.glass-cream}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 32px

  # Glass sidebar panel
  panel-glass:
    backgroundColor: "{colors.glass-cream}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 16px

  # Dark glass panel
  panel-glass-dark:
    backgroundColor: "{colors.glass-dark}"
    textColor: "{colors.ink-inverted}"
    rounded: "{rounded.lg}"
    padding: 16px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"

  # Tab pill
  tab:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.ui-heading}"
    rounded: "{rounded.sm}"
    padding: 6px 12px

  # Pin square (one accent color per pin)
  pin:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.brand-dark}"
    typography: "{typography.meta}"
    rounded: "{rounded.sm}"
    padding: 4px 8px

  # Neutral badge
  badge-neutral:
    backgroundColor: "{colors.background-warm}"
    textColor: "{colors.brand-dark}"
    typography: "{typography.meta}"
    rounded: "{rounded.sm}"
    padding: 2px 10px

  # Pop badge
  badge-pop:
    backgroundColor: "{colors.accent-pink-pop}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.meta}"
    rounded: "{rounded.sm}"
    padding: 2px 10px
---

# Arc Browser Design System

## Overview

Arc's website is not a browser's landing page — it's a manifesto printed on paper-warm cream, torn open by a bright electric blue, and lit from behind by a soft gradient mesh that hums quietly while you read. The background is an unmistakable off-white (`{colors.background}`) — not clinical white, not iOS gray, but a faintly butter-tinted parchment that immediately separates Arc from every Chromium clone on earth. Over this warm canvas, the brand lays a saturated ultramarine (`{colors.primary}`) that refuses to behave like a corporate accent: it fills entire sections, gets used as a full-bleed background, carries the wordmark, and frames product screenshots like a movie poster.

The second defining gesture is the **gradient mesh** — the muted cloud that sits behind every hero. Desaturated peach, mint, butter, and pale violet blur into each other at 40–60% of a full pastel's saturation, creating an atmospheric halo that looks like sunrise diffused through frosted glass rather than a crayon box. Over the mesh, the UI sits on **frosted glass panels** — translucent sidebars, blurred command bars, peek windows that dim the page behind them — giving the product a physicality competitors don't attempt.

What makes Arc feel *different* from every other browser site is the collision of opposites held in one system: the cream paper warmth against the digital electric blue, the hushed mesh atmosphere against the hard geometric buttons, the occasional muted coral against the rigorous Marlin Soft SQ typography. Arc is crafted playfulness held in check.

**Key Characteristics:**
- Cream off-white canvas (`{colors.background}`) — paper-warm, never sterile
- Electric Arc Blue (`{colors.primary}`) as full-bleed hero color, not just an accent stamp
- **Restrained mesh gradients** (muted peach + mint + butter + violet) as atmospheric halos — 40–60% less saturated than a pure pastel
- **Frosted glass** sidebars, peek panels, command bars — `backdrop-filter: blur()` with translucent fills
- Marlin Soft SQ for display, Marlin for UI, InterVariable for body — a three-font wardrobe
- Generous rounded corners (`{rounded.sm}`–`{rounded.xl}`) — playful but never infantile
- Soft black shadows — diffused, never harsh
- A quiet accent tier (muted coral, soft sky, pale olive) used sparingly

## Colors

### Primary
- **Arc Blue** (`{colors.primary}`): The signature. Full-bleed hero backgrounds, wordmark, primary CTAs, pin indicators.
- **Deep Arc Blue** (`{colors.primary-deep}`): Solid button fills on cream surfaces, link text on light backgrounds.
- **Paper Cream** (`{colors.background}`): The canvas. Warm off-white that sits between `#fff` and a true butter.
- **Paper Cream Warm** (`{colors.background-warm}`): A slightly more saturated cream for stacked sections and inset cards.

### Brand Deep
- **Brand Dark Blue** (`{colors.brand-dark}`): The near-black brand navy. Used for dark sections, headers on cream.
- **Pure Black** (`{colors.ink}`): Body text, headings on cream. Arc doesn't dilute its black.
- **Secondary Ink** (`{colors.text-secondary}`): Secondary text on cream when full black is too heavy.

### Gradient Mesh (the atmosphere, restrained)
- **Mesh Peach** (`{colors.mesh-peach}`): Upper-left bloom — dusty, warm, barely coral.
- **Mesh Butter** (`{colors.mesh-butter}`): Central warm diffusion — muted sunrise note.
- **Mesh Mint** (`{colors.mesh-mint}`): Lower cool bloom — closer to sage.
- **Mesh Violet** (`{colors.mesh-violet}`): Upper-right pale lavender, balancing the warms.

### Accents (used sparingly — one per surface)
- **Muted Coral** (`{colors.accent-coral}`): Badges, notification dots, occasional pin.
- **Arc Salmon** (`{colors.accent-salmon}`): Muted peach companion for cards.
- **Pale Olive** (`{colors.accent-olive}`): Soft highlighter green, success-adjacent.
- **Pale Periwinkle** (`{colors.accent-periwinkle}`): Low-emphasis chips and muted surfaces.
- **Pink Pop** (`{colors.accent-pink-pop}`): Student-campaign energy — high-pop notification.
- **Brand Red** (`{colors.accent-red}`): Alerts only.

> Deliberately retired: the full rainbow conic gradient. Real Arc surfaces now carry Arc Blue or a 2–3 color mesh blend.

### Secondary (Teals)
- **Teal 1** (`{colors.teal-1}`): Vivid aqua, used for highlight rings and electric decorative moments.
- **Teal 3** (`{colors.teal-3}`): Mid-teal for icons and illustrations.
- **Teal 7** (`{colors.teal-7}`): Deep forest teal for dark sections.

### Interactive
- **Focus Outline** (`{colors.focus-ring}`): System focus ring — soft sky blue.
- **Arc Blue Hover** (`{colors.hover-overlay}`): Translucent deep blue for hover overlays.

### Glass & Surface
- **Glass White** (`{colors.glass-cream}`): Frosted cream — the default glass fill for panels over gradients.
- **Glass Dark** (`{colors.glass-dark}`): Frosted brand-navy for glass panels over light imagery.
- **Border Soft** (`{colors.border-soft}`): Hairline dividers, barely visible.
- **Border Tinted** (`{colors.border-tinted}`): Arc-blue-tinted borders on interactive cards.

## Typography

### Font Family
- **Display**: `Marlin Soft SQ` / `Marlin` — geometric, soft-squared, architectural. Fallback: `-apple-system, system-ui, Segoe UI, Roboto`.
- **Body/UI**: `InterVariable` / `Inter` — workhorse for nav, UI, links, body copy at 17px and below.
- **Accent Serif**: `ABC Oracle` — bookish serif for editorial moments. Fallback: `Helvetica`.
- **Display Variable**: `Exposure VAR` — variable display used at mid-sizes (36px). Fallback: `Helvetica`.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Use those tokens directly.

| Token | Use |
|---|---|
| `hero-display` | Super-tight leading, near-overlap heroes |
| `display-large` | Section intros |
| `display-mid` | Expressive variable headings |
| `heading` | Feature blocks |
| `editorial-large` / `editorial` | Serif pull quotes, link moments |
| `ui-heading` | Card titles, nav |
| `link-strong` | Emphasized inline links |
| `body` | General UI copy |
| `nav-link` | Primary nav items |
| `meta` | Caption/label copy |
| `button-ui` | System-font buttons for native feel |
| `micro-link` | Uppercase tracking for chrome labels |

### Principles
- **Marlin Soft SQ is the voice**: The soft-squared geometric sans is Arc's typographic fingerprint. Used at 700 for all display.
- **Ultra-tight display leading (0.93–0.97)**: Display text nearly overlaps vertically — compressed, intentional.
- **Negative letter-spacing scales with size**: -1.82px at 45px, -1.6px at 40px, -0.28px at 14px.
- **ABC Oracle as the editorial comma**: Used sparingly for quotes; never for UI.
- **Three families, no more**: Display (Marlin), Body (Inter), Editorial accent (Oracle).

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

`lg` (24px) is the workhorse rhythm unit. `sm` (8px) is the micro-tick.

### Grid & Container
- Max content width: ~1080–1200px, centered
- Hero: centered single column, headline + subhead + CTAs, product screenshot below
- Full-bleed Arc Blue sections alternate with cream sections — a cream/blue cadence that defines the page rhythm

### Whitespace Philosophy
- **Generous around product, tight around type**: Arc gives screenshots cathedral-like space, then compresses headline typography into dense architectural blocks.
- **Section as set-piece**: Each scroll section is a distinct environment.
- **Color as spacing**: A switch from cream to Arc Blue does more work than 120px of whitespace.

## Elevation & Depth

Arc's depth system is built on the **interaction of glass, gradient, and soft drop shadow** — three physical layers that together create dimensionality.

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (0) | No shadow | Page text, inline elements |
| Ambient (1) | Subtle 8px soft drop using `{colors.shadow-soft}` | Hover hints, subtle lift |
| Standard (2) | 5px+5px drop using `{colors.shadow-soft}` | Buttons, cards — signature soft drop |
| Floating (3) | 12px+40px wide drop | Glass panels, peek windows, command bar |
| Deep (4) | 24px+60px ambient | Modals over gradient mesh |
| Ring (focus) | `0 0 0 3px {colors.focus-ring}` | Keyboard focus — soft sky halo |

### The Glass Recipe
Arc's frosted-glass panels follow a five-step stack:
1. **Colored ground**: Arc Blue, gradient mesh, or dark navy.
2. **Translucent fill**: `{colors.glass-cream}` or `{colors.glass-dark}`.
3. **Backdrop filter**: `backdrop-filter: blur(20px) saturate(1.8)` — the saturation bump keeps colors vibrant.
4. **Inner top-edge highlight**: `box-shadow: inset 0 1px 0` white-60 — simulates light catching the rim.
5. **Outer soft drop**: 12px+40px shadow.

### Gradient Mesh Halo
Behind hero content, Arc layers four overlapping soft radial gradients of `{colors.mesh-peach}`, `{colors.mesh-violet}`, `{colors.mesh-mint}`, and `{colors.mesh-butter}` over a cream base. The gradient is never animated on-scroll — it's a still atmosphere, not a light show.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Edge cases |
| `xs` | 4px | Smallest interactive (tight badges, inline chips) |
| `sm` | 8px | Standard — tabs, cards, inputs, pins |
| `md` | 10px | Comfortable — buttons, primary interactive |
| `lg` | 12px | Panels, nested glass surfaces |
| `xl` | 22px | Hero pills, Little Arc, featured glass chips |
| `pill` | 9999px | Reserved — Arc avoids full-pill rectangles |

Arc never goes full-pill for rectangles, but `{rounded.xl}` (22px) gets close for special moments.

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Deep Arc Blue solid on cream
- **`button-inverse`** — White on Arc Blue full-bleed sections
- **`button-glass`** — Frosted cream over gradient mesh
- **`button-mesh`** — 2–3-color mesh blend; replaces the retired rainbow conic

### Cards & Containers
- **`card`** — White on cream, `{rounded.sm}`
- **`card-comfortable`** — `{rounded.md}` for primary interactive
- **`card-featured`** — Glass cream, `{rounded.xl}` for hero/featured

### Glass Panels
- **`panel-glass`** — Cream glass for sidebars, peek windows, command bars
- **`panel-glass-dark`** — Dark navy glass for panels over light imagery

### Pins, Tabs, and Little Arc
- **`tab`** — 8px radius, 2px Arc blue border when active
- **`pin`** — 8px radius square with one muted accent color (coral, olive, periwinkle, salmon)
- **Little Arc** — 22px-radius floating glass chip with a 2–3 color mesh blend

### Inputs & Forms
**`input`** — White or glass background, hairline border, `{rounded.md}`. Focus uses `{colors.primary}` 1px border + soft sky outer ring.

### Badges
- **`badge-neutral`** — Warm cream background, brand-dark text
- **`badge-pop`** — Pink pop background for student-campaign energy

### Navigation
**`nav-bar`** — Sticky cream background with subtle blur. Marlin Soft SQ 16px weight 700 for nav links. Right-aligned blue CTA.

## Do's and Don'ts

### Do
- Use **restrained gradient meshes** behind hero moments — atmospheric, not flat
- **Layer glass carefully**: colored ground + translucent fill + backdrop-blur + inner highlight + soft drop. All five, every time.
- Use Arc Blue (`{colors.primary}`) at full-bleed scale — as a section background, not just as a button
- Pair cream (`{colors.background}`) with black text — the warmth is the brand
- Use Marlin Soft SQ at weight 700 with tight negative letter-spacing for display
- Reach for a **2–3 color mesh blend** (not a full rainbow) on celebratory moments
- Use `{rounded.sm}`–`{rounded.xl}` radii — playful but architectural
- Let the gradient mesh breathe with `backdrop-filter: blur()` on any overlaid panel

### Don't
- **Don't use the full conic rainbow anymore** — pick 2–3 adjacent mesh hues and blend them
- **Don't use solid single-color fills for hero moments** — always have a gradient mesh or Arc Blue background
- Don't let the mesh hit full-pastel saturation — keep it 40–60% off the pure tone
- Don't flatten the glass — skip `backdrop-filter` and the panels look like PowerPoint rectangles
- Don't use cool gray for surfaces — the base is cream, warmth matters
- Don't use pill-shaped buttons for rectangles — Arc stays in 8–22px range
- Don't use harsh dark shadows — Arc's drops are soft and black-based
- Don't use serif-only heroes — Marlin Soft SQ is the display voice; ABC Oracle is a guest
- Don't forget the **saturation boost** on glass — `saturate(1.8)` keeps the gradient vibrant through frost

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Hero headline 32px, single column, mesh gradient simplifies to 2 blooms |
| Tablet | 640–1024px | 2-column grids, glass panels shrink, gradient stays atmospheric |
| Desktop | 1024–1280px | Full layout, 3-column feature grids, full mesh |
| XL | >1280px | Centered content, broader cream/blue margins |

### Touch Targets
- Buttons: 36px+ tall
- Nav links generously spaced with 24px gutters
- Glass chips and pins are 22px+ hit areas

### Collapsing Strategy
- Hero: 45.5px Marlin Soft SQ → 32px on mobile, weight 700 maintained
- Full-bleed Arc Blue sections stay full-bleed on all sizes
- Gradient mesh: 5 blooms on desktop → 2–3 blooms on mobile
- Glass panels: `backdrop-filter` reduces blur radius on mobile (20px → 12px)
- Product screenshots: horizontal scroll on mobile when UI detail is critical

### Image Behavior
- Product screenshots maintain soft drop shadow at all sizes
- Mesh elements scale proportionally, never tile
- Little Arc illustration: 22px radius, sits at consistent scale across breakpoints

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Deep Arc Blue (`{colors.primary-deep}`) on cream, or White on Arc Blue
- Hero background: Arc Blue (`{colors.primary}`) full-bleed, or cream + gradient mesh
- Background: Paper Cream (`{colors.background}`)
- Heading: Pure Black (`{colors.ink}`) on cream, White on blue
- Body: Pure Black (`{colors.ink}`) or `{colors.text-secondary}`
- Brand Dark: `{colors.brand-dark}`
- Link: `{colors.primary-deep}` on cream
- Focus ring: `{colors.focus-ring}` (soft sky)
- Pop accent: `{colors.accent-pink-pop}`
- Mesh blooms: peach (`{colors.mesh-peach}`), butter (`{colors.mesh-butter}`), mint (`{colors.mesh-mint}`), violet (`{colors.mesh-violet}`)
- Mesh blend (replaces rainbow): linear `{colors.mesh-violet} → {colors.mesh-peach} → {colors.mesh-butter}` at ~115deg
- Muted coral accent: `{colors.accent-coral}` (use sparingly)

### Example Component Prompts
- "Create an Arc hero: cream background (`{colors.background}`). Behind the headline, layer four restrained radial gradients — peach (`{colors.mesh-peach}`) at 18% 28%, violet (`{colors.mesh-violet}`) at 82% 18%, mint (`{colors.mesh-mint}`) at 75% 85%, butter (`{colors.mesh-butter}`) at 25% 82%, all fading to transparent. Apply `filter: saturate(0.85)` on the mesh layer. Headline in Marlin Soft SQ 45.5px weight 700, line-height 0.93, letter-spacing -1.82px, color `{colors.ink}`. Primary CTA: deep Arc Blue `{colors.primary-deep}`, white text, `{rounded.md}` radius."
- "Design a glass sidebar panel: translucent cream fill `{colors.glass-cream}`, `backdrop-filter: blur(20px) saturate(1.8)`, inner top highlight, outer drop shadow, `{rounded.lg}` radius. Sits over an Arc Blue or gradient mesh ground."
- "Full-bleed Arc section: `{colors.primary}` background, white Marlin Soft SQ 40px weight 700 headline, letter-spacing -1.6px. White pill CTA button (`{colors.surface}` bg, `{colors.primary-deep}` text, `{rounded.md}` radius) inverse-style."
- "Mesh blend CTA (replaces rainbow): linear gradient `{colors.mesh-violet} → {colors.mesh-peach} → {colors.mesh-butter}`, `{rounded.xl}` radius, brand-dark text (`{colors.brand-dark}`), 1px white-50 border."
- "Product screenshot treatment: sit the image on cream with a soft mesh halo behind it. `{rounded.lg}` on the image, soft drop shadow plus a wide ambient secondary."

### Iteration Guide
1. **Always start with cream** (`{colors.background}`) as the base — white is wrong, gray is wrong, only paper is right.
2. **Heroes need atmosphere** — either a full-bleed Arc Blue or a gradient mesh. Never flat white.
3. **Glass needs all five layers**: ground + fill + blur + saturate + inner highlight + outer drop.
4. **Marlin Soft SQ 700 with -1.6px+ tracking** is the display voice.
5. **Radius stays 8–22px** — no pills for rectangles, no sharp corners for interactive.
6. **Shadows are soft and black-based**. Arc doesn't use blue-tinted shadows.
7. **Section cadence: cream → Arc Blue → cream → navy** — alternate rooms.
8. **Muted accents** are the secondary layer — use them for tabs, pins, badges, never for primary CTAs. One color per surface.
9. **The mesh is a mood, not a graphic.** If it looks like a paint swatch, pull saturation down.
