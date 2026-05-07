---
version: alpha
name: "Brightland"
description: "Token-first design system reference for Brightland."

colors:
  background: "#ffffff"
  surface: "#f5c518"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#e9a826"
  primary: "#fbf8f1"
  on-primary: "#ffffff"
  border: "#1f1a14"
  focus-ring: "#fbf8f1"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 50px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 25px
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
    fontSize: 20px
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

# Brightland Design System

## Overview

Brightland's website is a sun-dappled California pantry rendered as e-commerce. The page reads like a tonal still-life shoot — pastel bottles arranged on cream linen, peachy ceramics, sage produce, butter-yellow citrus — and the interface gets out of the way to let that photography breathe. The canvas is a warm off-white (`#fbf8f1`), the primary CTAs are a single saturated sunshine yellow (`#f5c518`), and the typographic voice is a contemporary high-contrast serif (`Canela`-class) for display, paired with a geometric humanist sans (`Söhne`-class) for everything functional. Where most direct-to-consumer pantry brands lean into bold sans wordmarks and clinical white, Brightland chooses warmth, restraint, and editorial pacing — a Kinfolk magazine that happens to sell olive oil.

The signature graphic device is the **sun circle** — a flat, simplified solar disc that anchors the wordmark and reappears as a decorative element across the site. It's never embellished with rays or rendered with gradients; it's a single soft yellow disc, sometimes paired with the wordmark, sometimes floating alone as a section break. The roundness echoes the bottle silhouettes (Brightland's signature is a tall, slender olive-oil bottle in pastel-tinted glass — peach for Alive, butter-cream for Awake, sage for Arise) and the rounded sans-serif typeface chosen for chrome.

What distinguishes Brightland most is its **photography-as-color-system** approach. The site doesn't impose a color palette on its imagery; the imagery sets the palette. Hero banners run in soft buttercream and pastel rose, product grids sit on warm cream, and section breaks use desaturated olive-grove greens or sandy taupes pulled directly from lifestyle photography. The result is a site that feels seasonal, edible, and tactile — the visual language of a Mediterranean cookbook rather than a tech product.

**Key Characteristics:**
- Warm cream canvas (`#fbf8f1`) — never pure white, always paper-warm
- Sunshine yellow CTAs (`#f5c518`) — the only consistently saturated color, used as a sun-stamp
- High-contrast serif display (`Canela`-class) at editorial sizes — confident but soft
- Pastel product photography drives the palette — peach, butter, sage, terracotta, sand
- Sun-circle logo as recurring visual motif — flat solid disc, never gradient
- Generous editorial whitespace — magazine pacing, not e-commerce density
- Soft rounded radius (8–12px) on cards, pill (9999px) on CTAs — friendly, not sharp
- Product photography always full-bleed or tightly framed — bottles as still-life subjects

## Colors

### Primary
- **Brightland Cream** (`#fbf8f1`): Primary page background — a warm off-white that reads as unbleached paper. The foundation everything else sits on.
- **Brightland Ink** (`#1f1a14`): Primary text and body copy — a deep warm near-black with a hint of brown, never pure `#000`.
- **Pure White** (`#ffffff`): Reserved for product cards, modal surfaces, and inverted CTA text.

### Brand Accent
- **Sunshine Yellow** (`#f5c518`): The signature accent — the sun-disc color, applied to primary "Add to Bag" CTAs, sale badges, and the wordmark's solar logo. The most saturated color in the system.
- **Honey Glow** (`#e9a826`): A deeper companion yellow used on hover states and decorative ribbons — the late-afternoon-light counterpart to the noon-sun primary.

### Pastel Photography Palette (Bottle/Lifestyle)
- **Peach Glow** (`#f4d4c2`): Alive olive oil bottle tint, warm hero backgrounds — ripe stone-fruit blush.
- **Butter Cream** (`#f0e3c1`): Awake bottle tint, gift-set photography — soft churned-butter yellow.
- **Olive Sage** (`#a8b29a`): Arise bottle tint, vinegar shoots, foliage backdrops — desaturated grove green.
- **Terracotta** (`#c97b5a`): Vinegar accents, tile/ceramic props — earthy California clay.
- **Sand Taupe** (`#d4c4a8`): Section dividers, neutral lifestyle backgrounds — sun-bleached linen.

### Neutrals & Text
- **Brightland Ink** (`#1f1a14`): All primary headings, body, nav links, and product names.
- **Soft Charcoal** (`#5c554a`): Secondary text — descriptions, metadata, breadcrumbs. A warm desaturated brown-gray.
- **Whisper Gray** (`#a89f91`): Tertiary text and disabled states — placeholder copy, helper text.
- **Hairline Cream** (`#ede5d3`): Subtle dividers and form borders — a tinted neutral that disappears into the canvas.

### Accent / Status
- **Sale Coral** (`#d8553a`): Sale price tags, urgency markers — a warm muted red, never fire-engine.
- **Badge Bestseller** (`#1f1a14`): "BESTSELLER" and "NEW" pills — ink on cream for editorial restraint.

### Gradient System
- Brightland is **near gradient-free**. The only gradient appears as a soft radial glow behind the sun-circle logo on hero moments — `radial-gradient(circle, #f5c518 0%, #fbf8f1 80%)`. Everything else is solid color sourced from photography or the primary system.

## Typography

### Font Family
- **Display (Serif)**: `Canela`, with fallback `Tiempos Headline`, `Cormorant Garamond`, `Georgia`, `serif`
- **Body / UI (Sans)**: `Söhne`, with fallback `Inter`, `Helvetica Neue`, `Arial`, `sans-serif`
- **Wordmark**: Custom `Brightland` lockup — slightly condensed serif, tracked tight, paired with sun-circle glyph
- **OpenType Features**: Old-style figures (`onum`) on prices and caption metadata; standard ligatures throughout.

*Note: `Canela` is a commercial typeface from Commercial Type. Open substitutes: `Cormorant Garamond` (Google Fonts), `EB Garamond`, or `Fraunces` for a similar high-contrast modern-serif feel. For sans, `Inter` or `IBM Plex Sans` are close to `Söhne`'s humanist warmth.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Canela | 72px (4.5rem) | 400 | 1.05 | -0.5px | Editorial hero statements ("Meet the Brightland Pantry") |
| Display Large | Canela | 56px (3.5rem) | 400 | 1.08 | -0.4px | Section heads, gift-set banners |
| Display | Canela | 44px (2.75rem) | 400 | 1.10 | -0.3px | Product detail page titles |
| Section Heading | Canela | 36px (2.25rem) | 400 | 1.15 | -0.2px | Sub-section heads, collection titles |
| Sub-heading | Canela | 28px (1.75rem) | 400 | 1.20 | -0.2px | Card titles, pull quotes |
| Sub-heading Small | Söhne | 20px (1.25rem) | 500 | 1.30 | 0 | Product card titles, list item heads |
| Body Large | Söhne | 18px (1.125rem) | 400 | 1.55 | 0 | Intro paragraphs, hero subtitles |
| Body | Söhne | 16px (1rem) | 400 | 1.55 | 0 | Standard reading, product descriptions |
| Nav Link | Söhne | 14px (0.875rem) | 500 | 1.0 | 0.02em | Top navigation labels |
| Button UI | Söhne | 14px (0.875rem) | 500 | 1.0 | 0.04em | "Add to Bag", "Shop All" — sentence case, not uppercase |
| Caption | Söhne | 13px (0.8125rem) | 400 | 1.45 | 0 | Metadata, helper text, breadcrumbs |
| Eyebrow / Tag | Söhne | 11px (0.6875rem) | 600 | 1.0 | 0.12em | "BESTSELLER", "NEW" — uppercase, wide tracking |

### Principles
- **Serif/Sans dialogue**: Canela serif handles all editorial moments (headings, hero, pull quotes); Söhne sans handles all functional content (UI, body, navigation, prices). The two never blend within a single role.
- **Soft display weights**: Canela display sizes run at weight 400 (regular) — never bold. The contrast in the typeface itself carries the editorial gravity; bolding it would feel shouty against the pastel imagery.
- **Generous body line-height**: 1.55 on all body sizes — the site reads at magazine pacing, not app density. Recipes and product descriptions need air.
- **Mixed-case CTAs**: "Add to Bag" and "Shop All" run in sentence case, not uppercase — friendlier, less commercial-pressure than typical e-commerce.
- **Eyebrow uppercase reserved**: Only the smallest tag/badge text uses uppercase, and always with wide `0.12em` tracking. Distinguishes status markers from action labels.
- **Old-style figures on prices**: `$28.00` reads with old-style numerals — softer, more pantry-cookbook than tech-startup.

## Layout

### Spacing System
- Base unit: 8px
- Scale: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px
- Notable: Brightland uses the high end of the scale liberally. Section-to-section spacing runs 96–128px on desktop; intra-section content uses 24–48px. Cramped spacing is reserved for product card metadata only.

### Grid & Container
- Max content width: 1280px for centered editorial content; 1440px for full collection grids
- Hero: full-bleed banner with text overlay or text-left/image-right two-column at 60/40 split
- Collection grid: 4 columns desktop, 2 columns tablet, 1 column mobile
- Product detail: 2 columns desktop (image gallery left at 55%, info right at 45%)
- Lifestyle modules: 4-up tile grid alternating with full-width banners
- Recipe blocks: single-column long-form with 720px max measure for body copy

### Whitespace Philosophy
- **Editorial pacing**: Each major section gets 96–128px vertical breathing room — the page reads like a magazine spread, not a Shopify default
- **Photography breathing**: Full-bleed lifestyle imagery alternates with cream-canvas content blocks — the eye rests between rich color moments
- **Text columns stay narrow**: Body copy never exceeds 720px measure, even on wide viewports — readability over fill
- **Asymmetric balance**: Hero compositions often place text left and image right with intentional left margin (96–128px) to avoid edge-locked feel

### Border Radius Scale
- Sharp (0px): Editorial banners, full-bleed hero ribbons
- Medium (8px): Form inputs, small chips, dropdowns
- Large (12px): Product cards, lifestyle tiles, image containers
- XL (16–24px): Hero feature blocks, larger banners with rounded corners
- Pill (9999px): All buttons, all badges, variant selectors — round is the action language

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body sections, full-bleed banners |
| Hairline (Level 1) | `1px solid #ede5d3` | Subtle dividers, default form borders, low-key card frames |
| Feather (Level 2) | `0 2px 8px rgba(31, 26, 20, 0.04)` | Default product card elevation |
| Soft Lift (Level 3) | `0 8px 24px rgba(31, 26, 20, 0.08)` | Hover state on cards, dropdown menus |
| Modal Halo (Level 4) | `0 16px 48px rgba(31, 26, 20, 0.16)` | Cart drawer, modal overlays, mega-menu panels |
| Sun Glow (Level 5) | `radial-gradient(circle, #f5c518 0%, transparent 80%)` at 60–120px blur | Hero sun-circle ambient glow, decorative-only |

**Shadow Philosophy**: Brightland's depth system is atmospheric and warm, not graphic. Where Cape uses hard offset rubber-stamp shadows, Brightland uses soft diffused warmth — every shadow color includes the warm-brown of the brand ink (`rgba(31, 26, 20, ...)`) instead of pure black, so elevation never feels cold or technical. The numbers stay small — 2px to 16px blur — because the canvas itself is so warm that heavy shadows would feel muddy. The system favors hairline borders over shadows for default-state structure, escalating to soft lifts only on interaction.

### Decorative Depth
- Hero sun-circle uses a subtle radial glow that bleeds into the cream canvas — the only "atmospheric" effect in the system
- Hover states on product cards use translate-Y (-2px) plus shadow growth to suggest a gentle pickup motion
- Modals and cart drawers use a 16px blur halo plus a `rgba(251, 248, 241, 0.6)` cream-tinted backdrop scrim — softer than the typical black overlay

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

**Primary Sunshine**
- Background: Sunshine Yellow (`#f5c518`)
- Text: Brightland Ink (`#1f1a14`)
- Padding: 14px 28px (standard), 12px 20px (compact)
- Radius: `9999px` (full pill)
- Border: none
- Shadow: `0 1px 2px rgba(31, 26, 20, 0.08)` — barely-there ground shadow
- Font: 14px Söhne weight 500, sentence case, letter-spacing `0.04em`
- Hover: background shifts to Honey Glow (`#e9a826`), 1px upward translate, shadow grows to `0 4px 12px rgba(31, 26, 20, 0.12)`
- Use: Primary CTA — "Add to Bag", "Shop the Collection", "Subscribe & Save"

**Ink Outline**
- Background: transparent
- Text: Brightland Ink (`#1f1a14`)
- Padding: 14px 28px
- Radius: `9999px`
- Border: `1px solid #1f1a14`
- Hover: background fills to Brightland Ink (`#1f1a14`), text inverts to cream (`#fbf8f1`)
- Use: Secondary CTAs — "Learn More", "Read Recipe", quiz/explore actions

**Cream Ghost**
- Background: Brightland Cream (`#fbf8f1`)
- Text: Brightland Ink (`#1f1a14`)
- Padding: 12px 24px
- Radius: `9999px`
- Border: `1px solid #ede5d3` (Hairline Cream)
- Use: Tertiary actions, filter chips, variant selectors

**Variant Chip (Selected)**
- Background: Brightland Ink (`#1f1a14`)
- Text: Brightland Cream (`#fbf8f1`)
- Padding: 8px 14px
- Radius: `9999px`
- Use: Active state in size/variant selectors ("8.5oz" / "Subscribe")

### Cards & Containers

**Product Card**
- Background: Pure White (`#ffffff`)
- Border: `1px solid #ede5d3` or `none` with subtle shadow
- Radius: `12px`
- Shadow: `0 2px 8px rgba(31, 26, 20, 0.04)` — feather-soft elevation
- Internal padding: 24px
- Image area: full-bleed photo at top, aspect ratio 4:5 portrait — bottle centered on pastel background
- Hover: shadow grows to `0 8px 24px rgba(31, 26, 20, 0.08)`, image scales to 1.02

**Lifestyle Tile**
- Background: photographic, no overlay
- Radius: `12px`
- Internal padding: text overlays sit at the bottom with no scrim — photography is composed for legibility
- Use: "Meet the Brightland Pantry" tiles, recipe entries

**Editorial Banner**
- Background: tinted pastel (Peach Glow, Butter Cream, or Olive Sage) at 100% solid
- Radius: `0px` or `16px` depending on placement
- Internal padding: 64px+ vertical, 48px+ horizontal
- Use: "20% Off Gift Sets" hero ribbons, seasonal promotion banners

### Badges / Tags / Pills

**Bestseller Pill**
- Background: Brightland Ink (`#1f1a14`)
- Text: Brightland Cream (`#fbf8f1`)
- Padding: 4px 10px
- Radius: `9999px`
- Font: 11px Söhne weight 600, uppercase, `0.12em` tracking
- Use: "BESTSELLER", "NEW", "LIMITED AVAILABILITY"

**Sale Pill**
- Background: Sale Coral (`#d8553a`)
- Text: Pure White (`#ffffff`)
- Padding: 4px 10px
- Radius: `9999px`
- Font: 11px Söhne weight 600, uppercase, `0.12em` tracking
- Use: "SALE", "$12 OFF" — urgency markers

**Star Rating Inline**
- Stars: 14px filled in Sunshine Yellow (`#f5c518`)
- Trailing count: 13px Söhne weight 400 in Soft Charcoal (`#5c554a`) — "(217)"
- Layout: tight inline, star-count separated by 6px

### Inputs & Forms
- Background: Pure White (`#ffffff`)
- Border: `1px solid #ede5d3` default, `1px solid #1f1a14` on focus
- Radius: `8px`
- Font: 16px Söhne weight 400
- Text color: `#1f1a14`
- Placeholder: Whisper Gray (`#a89f91`)
- Focus: border darkens, no ring — restrained, paper-form aesthetic
- Padding: 12px vertical, 16px horizontal

### Navigation
- Top nav: horizontal cream bar, centered Brightland wordmark with sun-circle, left-aligned link cluster, right-aligned cart/account icons
- Announcement ribbon: thin Sunshine Yellow strip above nav with rotating promo text in Söhne 13px weight 500
- Links: Söhne 14px weight 500, `#1f1a14`, sentence case
- Hover: text underlines with 1px Brightland Ink underline, 4px offset
- Mega menus: drop-down panels styled as mini-collection grids (image + name) rather than text lists
- Sticky behavior: nav remains fixed on scroll, ribbon hides

### Decorative Elements

**Sun Circle**
- Solid disc, Sunshine Yellow (`#f5c518`)
- Sizes: 24px (inline with wordmark), 64px (section dividers), 200px+ (hero accents)
- No rays, no gradient, no detail — a flat solar dot
- Sometimes paired with a subtle radial glow on hero treatments

**Olive Branch Illustration**
- Hand-drawn or photographed sprigs used as section ornaments
- Always desaturated sage (`#a8b29a`) on cream
- Used sparingly — never decorating CTAs or chrome

**Wavy Divider**
- A thin 1px wavy line in Hairline Cream (`#ede5d3`) used between editorial sections
- Echoes pour-of-oil motion without being literal

## Do's and Don'ts

### Do
- Use Canela (or a high-contrast modern serif) for every display and heading size — the editorial voice is non-negotiable
- Pair Canela with Söhne (or a humanist sans) for body and UI — never use serif for functional text
- Use Sunshine Yellow (`#f5c518`) on primary CTAs and the sun-circle logo — preserve its stamp quality
- Keep CTAs in sentence case — "Add to Bag", not "ADD TO BAG"
- Use pill (`9999px`) radius on every button and badge — round is the action language
- Apply soft warm shadows (`rgba(31, 26, 20, 0.04–0.16)`) — never `rgba(0, 0, 0, ...)` for depth
- Let pastel product photography drive section palettes — peach, butter, sage, terracotta
- Use the warm cream canvas (`#fbf8f1`) — it's the soul of the system
- Reserve uppercase for the smallest eyebrow/tag text only, with wide `0.12em` tracking
- Frame product imagery as still-life — full-bleed, centered, breathing room around each bottle

### Don't
- Don't use pure white (`#ffffff`) for the page background — always Brightland Cream (`#fbf8f1`)
- Don't use bold weights on Canela display — weight 400 is the ceiling; the typeface contrast carries gravity
- Don't introduce gradients beyond the sun-circle's radial glow — the system is solid-color editorial
- Don't use sharp 0-radius on buttons — they always pill (`9999px`)
- Don't apply uppercase to CTAs — sentence case is the friendlier, intentional choice
- Don't use cold shadow colors — every shadow must include the warm Ink (`#1f1a14`) base
- Don't crowd product cards — internal padding is generous (24px) and image area is full-bleed
- Don't use pure black (`#000000`) text — always the warm Brightland Ink (`#1f1a14`)
- Don't use Sale Coral (`#d8553a`) outside genuine sale/urgency moments — it breaks the pastel calm
- Don't decorate with literal sun-ray illustrations — the sun is always a flat solid disc

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero serif drops to 32–40px |
| Mobile | 375–767px | Single-column, 40–48px hero serif, stacked CTAs full-width |
| Tablet | 768–1023px | 2-column product grids, 56px hero serif, mega-menu condenses |
| Desktop | 1024–1439px | 4-column collection grids, 64–72px hero serif |
| Large Desktop | ≥1440px | Maximum type scale (72px hero), 1280px content container, 1440px grid container |

### Touch Targets
- Primary CTAs: minimum 48px tap height on mobile (14px vertical padding + 14px font)
- Variant chips: 44×44px minimum tap area even when visual size is smaller
- Nav hamburger: 44×44px tap target
- Cart icon: 44×44px with 8px hit-area padding

### Collapsing Strategy
- **Nav**: Horizontal link cluster collapses to hamburger at <1024px; full-screen drawer menu on open with serif section heads
- **Hero**: 72px → 56px → 40px → 32px progressive scaling, weight 400 maintained throughout
- **Product grid**: 4-col → 2-col → 1-col transitions at tablet and mobile breakpoints
- **Lifestyle tiles**: 4-up grid → 2×2 stack → vertical 4-stack
- **Editorial banners**: text-left/image-right two-columns reorder to stacked image-then-text on mobile
- **Section spacing**: 128px desktop → 64px tablet → 48px mobile — reduces but maintains editorial pace
- **Body measure**: 720px desktop → 100% mobile with 24px gutters

### Image Behavior
- Product imagery maintains full-bleed treatment on mobile — bottles still hero
- Lifestyle photography compresses aspect ratio rather than cropping subjects out
- No art direction changes — the same warm pastel language adapts to every viewport
- Wordmark + sun-circle scale together; sun-circle never separates as standalone icon

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Sunshine Yellow (`#f5c518`)
- CTA Hover: Honey Glow (`#e9a826`)
- Page Background: Brightland Cream (`#fbf8f1`)
- Primary Text: Brightland Ink (`#1f1a14`)
- Secondary Text: Soft Charcoal (`#5c554a`)
- Card Surface: Pure White (`#ffffff`)
- Hairline Border: Hairline Cream (`#ede5d3`)
- Sale Marker: Sale Coral (`#d8553a`)
- Pastel Photo Tints: Peach `#f4d4c2`, Butter `#f0e3c1`, Sage `#a8b29a`, Terracotta `#c97b5a`, Sand `#d4c4a8`
- Card Shadow: `0 2px 8px rgba(31, 26, 20, 0.04)` default, `0 8px 24px rgba(31, 26, 20, 0.08)` hover

### Example Component Prompts
- "Create a hero section on Brightland Cream (`#fbf8f1`) with a Canela serif headline at 72px weight 400, line-height 1.05, letter-spacing -0.5px, color `#1f1a14`. Pair with a Söhne sans subtitle at 18px weight 400. Use a Sunshine Yellow (`#f5c518`) pill CTA — 14px Söhne weight 500, sentence case, `9999px` radius, soft warm shadow `0 1px 2px rgba(31, 26, 20, 0.08)`."
- "Design a product card on Pure White (`#ffffff`) with `12px` border radius and feather shadow `0 2px 8px rgba(31, 26, 20, 0.04)`. Image area is 4:5 portrait, bottle centered on a pastel tint (Peach `#f4d4c2`, Butter `#f0e3c1`, or Sage `#a8b29a`). Title in Söhne 20px weight 500, price in Söhne 16px weight 400 with old-style figures, star rating in Sunshine Yellow `#f5c518`."
- "Build an editorial banner ribbon — solid Sunshine Yellow (`#f5c518`) strip at the top of the page, 40px tall, with rotating promo text in Söhne 13px weight 500 in Brightland Ink (`#1f1a14`)."
- "Create a 'Bestseller' pill — Brightland Ink (`#1f1a14`) background, cream (`#fbf8f1`) text, 11px Söhne weight 600 uppercase with `0.12em` tracking, `9999px` radius, padding 4px 10px."
- "Design a sun-circle logo accent — solid `#f5c518` disc at 64px diameter, no gradient, no rays, with optional radial glow `radial-gradient(circle, #f5c518 0%, transparent 80%)` at 120px blur extending behind it on hero treatments."

### Iteration Guide
1. Default to Canela (or `Cormorant Garamond` / `Fraunces` open substitutes) for every display size at weight 400 — soft serif gravity, never bold
2. Pair with Söhne (or `Inter` / `IBM Plex Sans` substitutes) for all body and UI — never mix serif into functional text
3. Keep button radius at `9999px` always — pill is the action language
4. Use sentence case for CTAs ("Add to Bag"), uppercase only for the smallest eyebrow/tag text with wide tracking
5. Sunshine Yellow (`#f5c518`) is the sun-stamp — one or two applications per screen, primarily on primary CTAs and the wordmark
6. Cream canvas (`#fbf8f1`) is non-negotiable — pure white is for cards only
7. Shadows always use the warm Ink (`rgba(31, 26, 20, ...)`) base, never pure black
8. Let pastel product photography drive secondary palette decisions — peach, butter, sage, terracotta, sand pulled from imagery
9. Maintain magazine pacing — 96–128px between major sections, 720px body measure, generous internal padding
10. The sun circle is sacred — flat solid disc, no rays, no gradients, no embellishments
