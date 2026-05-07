---
version: alpha
name: "Eataly"
description: "Trattoria gold pills on cream, Libre Baskerville italic display, photo-led pasta-aisle chrome."

colors:
  background: "#ffffff"
  surface: "#333333"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#c9a973"
  primary: "#f8ae00"
  on-primary: "#ffffff"
  border: "#1976d2"
  focus-ring: "#f8ae00"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Libre Baskerville, ui-sans-serif, system-ui, sans-serif"
    fontSize: 70px
    fontWeight: 300
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Libre Baskerville, ui-sans-serif, system-ui, sans-serif"
    fontSize: 49px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Libre Baskerville, ui-sans-serif, system-ui, sans-serif"
    fontSize: 42px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Libre Baskerville, ui-sans-serif, system-ui, sans-serif"
    fontSize: 29px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Libre Baskerville, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Libre Baskerville, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Libre Baskerville, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Libre Baskerville, ui-sans-serif, system-ui, sans-serif"
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

# Eataly Design System

## Overview

Eataly's site is an Italian food market translated into a digital storefront. The page sits on pure white (`#ffffff`) with deep ink (`#000000`) for primary text and a warm slate (`#333333`) for secondary copy, but the entire chromatic identity hinges on a single saturated accent — Trattoria Gold (`#f8ae00`), the egg-yolk amber that fills primary CTAs, anchor banners, and family-recipe-card flags. That gold, paired with Libre Baskerville (a humanist transitional serif) running across every headline and section title at weights 300–400, is what makes an Eataly page feel like a trattoria menu rather than a grocery e-commerce template.

The signature typographic move is **Libre Baskerville at large display sizes with positive letter-spacing**. The face appears at 70px / 4.38rem with `2px` tracking on hero headlines, then steps down through 42px, 36px, 30px, and 22px — always with positive letter-spacing (`0.63–2px`), always sentence-case or capitalized, never UPPERCASE. The face's calligraphic character (open apertures, slight italic inflection on hero copy) carries the warmth that a slab serif would render too rigid; Libre Baskerville is the printerly counterpart to Italian-American family-restaurant signage.

The third defining trait is the **gold pill button** — a `30px`-radius CTA filled with `#f8ae00` and a `2px solid #f8ae00` border, white text at 15px weight 500, that on hover flips to `rgba(0, 0, 0, 0.04)` ghost-fill with `#333` text and a warm orange shadow `rgba(199, 91, 18, 0.4) 0 6px 16px`. The translation of the gold from solid fill to glow-cast is the brand's interactive signature: a button that doesn't just react, it warms up. Pair with `0 2px 10px` soft drop shadows on cards (the most-used shadow in the system, 120 occurrences) and a tertiary cobalt-blue (`#1976d2`) for inline product links, and the entire chrome reads as warm-Italian commerce — pasta-aisle warmth, gold-trim chrome, photographic abundance.

**Key Characteristics:**
- Trattoria Gold accent (`#f8ae00`) — primary CTA fill, banner highlights, family-card flags
- Pure white (`#ffffff`) page canvas — never tinted, photography supplies the warmth
- Pure black (`#000000`) primary text and warm slate (`#333333`) for secondary copy
- Libre Baskerville across the system at weights 300/400 — humanist transitional serif
- Positive letter-spacing on display (`0.63–2px`) — printerly trattoria signage register
- Gold pill button radius (`30px`) — full-pill primary CTAs
- Family-recipe italic feel — Libre Baskerville's soft humanist character
- Cobalt blue inline link (`#1976d2`) — Material-Design-tinged secondary accent
- Wine-warm orange shadow (`rgba(199, 91, 18, 0.4) 0 6px 16px`) on CTA hover
- Soft `0 2px 10px` drop shadows on cards — the system's elevation default
- Cream-trim accent (`#c9a973`) — gilded-frame counterpoint to the gold pills
- Hairline gray (`#9b9b9b` / `#737373`) for footer columns and metadata
- Photo-led product chrome — abundance imagery, market-stall presence

## Colors

### Primary Brand
- **Trattoria Gold** (`#f8ae00`): The brand-defining warm amber. Egg-yolk gold used on every primary CTA fill, banner accent, family-recipe flag, and Eataly nameplate. So definitional that the system loses its trattoria identity without it.
- **Pure Black** (`#000000`): Primary text colour, deepest type weight on white, masthead text. Used at `rgba(0, 0, 0, 0.87)` for body copy — Material-Design-tinged near-black.
- **Pure White** (`#ffffff`): Page canvas — committed pure white, never tinted, never warmed.

### Brand Accent / Secondary
- **Wine-Warm Cream** (`#c9a973`): Tertiary accent — the gilded-frame trim, used on framed editorial blocks and historical Eataly heritage sections.
- **Stone Gray** (`#737373`): Footer column heads and link colour — Bootstrap-rooted neutral.
- **Soft Gray** (`#9b9b9b`): Footer top items, logo image overlays, hairline metadata.
- **Cobalt Blue** (`#1976d2`): Material-Design link blue — used for inline product links, account / cart utility links, pre-header callouts.

### Neutrals & Text
- **Headline Black** (`rgba(0, 0, 0, 0.87)`): Material-tinged primary text colour — softer than pure black for editorial readability.
- **Warm Slate** (`#333333`): Secondary text, navigation labels, hover-state CTA text — the system's second-most-frequent colour (628 occurrences).
- **Stone Body** (`#737373`): Tertiary text, footer columns, byline metadata — third most-frequent (548 occurrences).
- **Soft Gray** (`#9b9b9b`): Disabled-state text, ancillary captions, logo backdrops.
- **Hairline Cream** (`#c9a973`): Decorative accent stops on heritage and history sections.

### Surface & Borders
- **Page Surface** (`#ffffff`): Default panel background.
- **Pre-header Bar** (`#000000`): The dark utility bar above the masthead — pure black with `#f8ae00` callout text.
- **Cream Surface** (`#faf8f5`) /* estimated */: Alternate-section warm surface, inferred from heritage / family-history blocks.

### Functional / State
- **Trattoria Gold** (`#f8ae00`): Primary CTA fill, banner highlights, premium-content flags, "MEMBER" badges.
- **Cobalt Link Blue** (`#1976d2`): Inline product links, utility links, focus-state highlights.
- **Hover Slate** (`rgba(0, 0, 0, 0.04)`): Ghost-fill on CTA hover state — barely-there darkening.
- **Hover Slate Text** (`#333333`): Text colour on CTA hover.
- **Focus Ring Blue** (`blue` / `#197cae`): Keyboard-focus outline `2px solid` ring.

### Shadow / Atmospheric
- **Card Drop** (`rgba(0, 0, 0, 0.1) 0px 2px 10px 0px`): The system's signature elevation — applied to product cards and panels (120 occurrences, the most-used shadow).
- **Card Drop Stronger** (`rgba(0, 0, 0, 0.16) 0px 2px 10px 0px`): Secondary card lift for featured tiles (30 occurrences).
- **Sticky Bar** (`rgba(0, 0, 0, 0.11) 0px -2px 20px 0px, rgba(0, 0, 0, 0.2) -1px 0px 4px 0px`): Cart sticky-bar elevation at viewport bottom.
- **Wine Warmth** (`rgba(199, 91, 18, 0.4) 0px 6px 16px`): The brand's hot orange glow — applied to CTA hover state. The single most-defining decorative shadow.
- **Sage-Pine Drop** (`rgba(23, 73, 77, 0.15) 0px 20px 30px 0px`): Editorial feature lift, cooler counterpoint to the wine glow.
- **Crisp Card** (`rgba(0, 0, 0, 0.25) 0px 1px 4px 0px`): Tighter elevation on compact tiles.

### Gradient System
- Eataly is **functionally gradient-free in chrome**. Photography does the gradient work — pasta-on-marble, sunset-on-Bologna-rooftop, espresso-pour gradients all live inside imagery. The single decorative gradient that surfaces is a `transparent → rgba(0,0,0,0.5)` linear-bottom scrim used to anchor white captions over food photography.

## Typography

### Font Family
- **Display & Body**: `Libre Baskerville`, with fallback `system-ui, Georgia, serif`. A humanist transitional serif (open-source, Google Fonts), used across hero headlines, section titles, body copy, and product names. The system's typographic backbone.
- **OpenType Features**: Standard ligatures, lining numerals on prices and historical dates, italic for editorial pivots.

*Note: Libre Baskerville is open-source and freely available via Google Fonts — no licensing concerns. The face is genuinely the working display font on the live site, not a substitute.*

*For a more refined alternative consistent with the trattoria register: **GT Super Display**, **PP Editorial New**, or **Domaine Display**. Avoid display slab serifs (Roboto Slab, Arvo) — they break the family-recipe warmth.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero Display Light | Libre Baskerville | 70px (4.38rem) | 300 | 1.20 /* estimated */ | 2px | Trattoria-signage display, often italic |
| Hero Display Regular | Libre Baskerville | 70px (4.38rem) | 400 | 1.20 /* estimated */ | 2px | Bolder hero variant |
| Section Title | Libre Baskerville | 42px (2.63rem) | 400 | 1.20 /* estimated */ | 1.43px | Section openers |
| H1 | Libre Baskerville | 36px (2.25rem) | 400 | 1.20 /* estimated */ | 1.03px | Page-level titles, category landing |
| H1 Secondary | Libre Baskerville | 36px (2.25rem) | 400 | 1.20 /* estimated */ | 0.8px | Tighter H1 variant |
| H2 | Libre Baskerville | 30px (1.88rem) | 400 | 1.20 /* estimated */ | 1.03px | Sub-sections inside categories |
| H3 Light | Libre Baskerville | 22px (1.38rem) | 300 | 1.50 | 0.63px | Card titles, italic-leaning |
| H3 Regular | Libre Baskerville | 22px (1.38rem) | 400 | 1.40 | 0.63px | Card titles, sturdier variant |
| H4 | Libre Baskerville | 22px (1.38rem) | 400 | 1.40 | 0.63px | Editorial subsection heads |
| Lead Body | Libre Baskerville | 20px (1.25rem) | 400 | 1.05 | 0.2px | Lead paragraphs, hero decks |
| Body | Libre Baskerville | 16px (1.00rem) | 400 | 1.50 /* estimated */ | normal | Default reading copy /* estimated */ |
| Button Label | system-ui / sans | 15px (0.94rem) | 500 | 1.00 | normal | Primary CTA labels |
| Caption / Metadata | system-ui / sans | 13–14px | 400 | 1.40 | normal | Bylines, prices, footer copy /* estimated */ |
| Pre-header Disclaimer | system-ui / sans | 13px /* estimated */ | 400 | 1.40 | normal | Top utility bar text in `#f8ae00` |

### Principles
- **One serif across the system**: Libre Baskerville carries every headline, section title, body, and editorial pivot. There is no second face. Discipline comes from weight (300 / 400) and letter-spacing (`0.2–2px`).
- **Positive tracking is the trattoria signature**: Libre Baskerville always has positive letter-spacing on display (`0.63–2px`). The face's native metrics are tightened for body but always opened for display.
- **No bold weights on display**: The heaviest display weight is 400 (regular). Light 300 appears for editorial italic-leaning hero copy. No 700-weight headlines anywhere in the system — calm-confidence display, not aggressive.
- **Sentence case throughout**: Hero headlines and section titles use sentence case or title case. UPPERCASE is reserved for occasional buttons and pre-header utility text in gold.
- **Buttons drop the serif**: Primary CTA labels at 15px weight 500 use a sans-serif (system-ui or implied Material sans). The serif sells; the sans transacts.

## Layout

### Spacing System
- Base unit: 4px (with 8px and 16px as the rhythm increments)
- Scale: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px /* estimated mid-range */
- Notable: Eataly's grid uses warm magazine-pacing spacing — section padding lives at 48–96px on desktop, tightening to 24–48px on mobile.

### Grid & Container
- Max content width: 1280–1440px on desktop product grids
- Hero: full-width photograph, text overlay positioned via 12-column grid (centred or left-aligned)
- Product grid: 4-up desktop, 2-up tablet, 1-up mobile — 16–24px gutters
- Footer: 4–5-column dense link grid in stone-gray (`#737373`) with logo glyph

### Whitespace Philosophy
- **Photographic abundance over chrome density**: Eataly leads with full-bleed food photography (pasta on marble, espresso pour, market stalls). The chrome stays out of the way.
- **Trattoria warmth via gold pills, not gradients**: The single chromatic moment of warmth is the gold CTA — the rest of the chrome stays in pure white and warm-slate neutrals.
- **Cards float, don't sit**: Soft `0 2px 10px` shadows lift product cards just enough to feel curated without becoming SaaS-y.

### Border Radius Scale
- Sharp (`0px`): Default for full-bleed photography, masthead, footer
- Subtle (`2px`–`3px`): Tags, inputs, product cards
- Soft (`5px`): Modal corners, occasional secondary CTAs
- Mid (`14px`–`19px`): Search-pill inputs, expand toggles
- Pill (`20px`–`30px`): Primary CTAs, mini action buttons, full-pill action chrome
- Larger Pill (`40px`): Newsletter-capture inputs (`0px 40px 40px 0px` asymmetric variant)
- Circle (`50%`): Carousel arrows, social icons, avatar dots
- Stretch (`100%`): Spanned buttons inside fixed-width containers

## Elevation & Depth

| Level | Box Shadow | Use Case |
|-------|-----------|---------|
| Flat (Level 0) | `none` | Page canvas, masthead, body content |
| Card Drop (Level 1) | `rgba(0, 0, 0, 0.1) 0px 2px 10px 0px` | Default product cards (most-used, 120 occurrences) |
| Card Drop Strong (Level 2) | `rgba(0, 0, 0, 0.16) 0px 2px 10px 0px` | Featured tiles, hover lift |
| Crisp Tile (Level 3) | `rgba(0, 0, 0, 0.25) 0px 1px 4px 0px` | Compact tile elevation |
| Wine Warmth (Level 4) | `rgba(199, 91, 18, 0.4) 0px 6px 16px` | The brand's hot orange glow — CTA hover signature |
| Sage-Pine Lift (Level 5) | `rgba(23, 73, 77, 0.15) 0px 20px 30px 0px` | Editorial feature elevation, cooler counterpoint |
| Sticky Cart Bar (Level 6) | `rgba(0, 0, 0, 0.11) 0px -2px 20px 0px, rgba(0, 0, 0, 0.2) -1px 0px 4px 0px` | Persistent cart-bar at viewport bottom |
| Modal Dialog (Level 7) | `rgba(0, 0, 0, 0.2) 0px 11px 15px -7px, rgba(0, 0, 0, 0.14) 0px 24px 38px 3px, rgba(0, 0, 0, 0.12) 0px 9px 46px 8px` | Material-Design-tinged modal stack |

**Shadow Philosophy**: Eataly treats elevation the way a market stall does — every product has its own halo, but the halos are warm, not clinical. The signature wine-warm glow (`rgba(199, 91, 18, 0.4) 0 6px 16px`) on CTA hover is the brand's interactive thumbprint: the gold doesn't just hover, it warms. Default cards use the soft `0 2px 10px` drop that 120 different elements share — a quiet, consistent lift that lets photography stay primary. Modal stacks reach Material-Design-tinged complexity, but only at the edges of the system.

### Decorative Depth
- The wine-warm glow is the only chromatic shadow in the system — every other shadow is neutral black at low opacity
- Sage-pine green shadow (`rgba(23, 73, 77, 0.15)`) appears on heritage / countryside editorial features as a cooler counterpoint
- Hover states combine `translateY(-1px)` lift with shadow darkening — the card "rises" toward the viewer

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

**Primary Trattoria Gold Pill**
- Background: Trattoria Gold (`#f8ae00`)
- Text: Pure White (`#ffffff`)
- Padding: `0px 20px` (with implied min-height ~44px from the pill structure)
- Border: `2px solid #f8ae00`
- Border-radius: `20px` — full pill on standard CTAs, `30px` on hero CTAs
- Box-shadow: `none` at rest
- Font: 15px sans (system-ui) weight 500, sentence case
- Hover: background `rgba(0, 0, 0, 0.04)` (ghost), text `#333`, shadow `rgba(199, 91, 18, 0.4) 0 6px 16px`, transform `translateY(-1px)` — wine-warm glow rises
- Active: outline `none`, transform `translateY(0px)` — settles back
- Focus: outline `none`, color `#ffffff`
- Use: Primary CTAs — "Shop Now", "Order Online", "Reserve Table"

**Outline Carousel Arrow**
- Background: `transparent`
- Color: Material-tinged near-black (`rgba(0, 0, 0, 0.87)`)
- Padding: `0px`
- Border: `2px solid #333`
- Border-radius: `50%` — full circle
- Transform: `matrix(-1, 0, 0, -1, 0, 0)` (icon rotation)
- Hover: outline none
- Focus: outline `blue solid 2px`
- Use: Carousel navigation arrows on featured product carousels

**Mini Action Button**
- Background: Trattoria Gold (`#f8ae00`)
- Text: Material near-black (`rgba(0, 0, 0, 0.87)`)
- Padding: `2px`
- Border: `0px none`
- Border-radius: `30px` — full pill
- Font: 16px weight 500
- Use: Compact action toggles ("Add", "View"), in-card CTAs

### Cards & Containers

**Product Card**
- Background: Pure White (`#ffffff`)
- Border: `none`
- Border-radius: `3px` — subtle modern rounding
- Box-shadow: `rgba(0, 0, 0, 0.1) 0px 2px 10px 0px` — the system's default elevation
- Internal padding: 0 around image, 16px around text block, 12px between rows
- Hover: shadow deepens to `rgba(0, 0, 0, 0.16) 0px 2px 10px 0px`, optional `translateY(-2px)` lift

**Editorial / Family-Recipe Card**
- Background: Pure White (`#ffffff`)
- Border: optional `1px solid #c9a973` (cream gilded frame) on heritage content
- Border-radius: `3px`
- Box-shadow: `rgba(0, 0, 0, 0.1) 0px 2px 10px 0px`
- Padding: 24–32px
- Use: Family recipe cards, heritage editorial blocks

### Badges / Tags / Pills

**"MEMBER" / "PREMIUM" Gold Flag**
- Background: Trattoria Gold (`#f8ae00`)
- Text: Pure White (`#ffffff`) or Material near-black
- Padding: `4px 12px`
- Border-radius: `2px`–`30px` depending on variant (sharp tag or full pill)
- Font: 12px sans weight 500–700 UPPERCASE
- Use: Eataly Club / Premium content flags

**"ITALIANO" Cobalt Tag**
- Background: Cobalt Blue (`#1976d2`)
- Text: Pure White (`#ffffff`)
- Padding: `4px 8px`
- Border-radius: `2px`
- Font: 12px sans weight 500
- Use: Origin / region tags on product tiles

**Cream Heritage Frame**
- Background: `transparent`
- Border: `1px solid #c9a973`
- Padding: `4px 12px`
- Border-radius: `2px`
- Font: 14px Libre Baskerville italic
- Use: Heritage / "Since 2007" frames

### Inputs & Forms
- Background: Pure White (`#ffffff`)
- Border: `1px solid #ced4da` /* estimated */ default
- Border-radius: `2px` for compact inputs, `40px` for newsletter-capture pill inputs
- Font: 16px sans (system-ui) weight 400 /* estimated */
- Text colour: Material near-black (`rgba(0, 0, 0, 0.87)`)
- Padding: `12px 16px` /* estimated */
- Focus: outline `blue solid 2px`
- Placeholder: Stone Gray (`#737373`) /* estimated */

### Navigation

**Pre-header Utility Bar**
- Background: Pure Black (`#000000`)
- Text: Trattoria Gold (`#f8ae00`) for promo callouts, white for utility links
- Height: ~32px
- Font: 13px sans weight 400 /* estimated */ — promo / shipping / club callouts

**Primary Nav Bar**
- Background: Pure White (`#ffffff`)
- Height: 64–80px
- Logo: Eataly wordmark, ~120–160px wide, left-aligned or centred
- Categories: "Shop · Restaurants · Classes · Events · Stores · About" — 14–15px sans (system-ui) weight 500, `#333` text, sentence case
- Right cluster: search icon, account icon, bag icon (gold-pill bg)
- Hover: subtle underline appears below text, optional gold-pill highlight on active item

### Inline Editorial Links
- Color: Cobalt Blue (`#1976d2`)
- Text-decoration: `underline` on hover
- Font: inherits from body
- Use: Inline product links, heritage links, store-finder callouts

## Do's and Don'ts

### Do
- Use Trattoria Gold (`#f8ae00`) on primary CTAs and brand accents — the egg-yolk amber that makes a page feel Italian
- Run Libre Baskerville at 22–70px with positive letter-spacing (`0.63–2px`) for editorial display
- Default to `20px`–`30px` pill border-radius on primary CTAs — full-pill trattoria signage
- Use `2px solid #f8ae00` border on gold pills — the gilded-edge contract
- Apply the wine-warm shadow (`rgba(199, 91, 18, 0.4) 0 6px 16px`) on CTA hover — the brand's interactive signature
- Use `0 2px 10px rgba(0, 0, 0, 0.1)` as the default card elevation
- Run body copy in Libre Baskerville regular with `1.50` line-height for editorial readability
- Pair gold CTAs with cobalt blue (`#1976d2`) inline links — Material-tinged secondary accent
- Keep section padding generous (48–96px desktop) — magazine pacing, market-stall breath
- Reserve cream (`#c9a973`) for heritage / family-history frames — gilded counterpoint

### Don't
- Don't soften the gold to amber-orange — `#f8ae00` is the brand contract
- Don't apply UPPERCASE to Libre Baskerville at display sizes — sentence case or title case only, with positive letter-spacing
- Don't introduce a second display face — Libre Baskerville carries every headline
- Don't use cool-blue shadows on CTA hover — wine-warm orange is the brand contract
- Don't crowd the gold pills with mid-range radii (`8–12px`) — full-pill or sharp, nothing in between
- Don't bold display headlines — weight 400 with positive letter-spacing is the calm-confidence move
- Don't replace the cobalt link blue with the brand gold — gold is the action contract, blue is the navigation contract
- Don't apply drop shadows to gold pills at rest — the elevation appears only on hover
- Don't use Material-Design-tinged modal shadows on regular cards — the deep three-layer shadow is reserved for modals only
- Don't strip the `2px solid #f8ae00` border from gold pills — the gilded edge is the chrome contract

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero type drops to 36–42px, 1-up product grid |
| Mobile | 375–599px | Single-column, 42–48px hero, hamburger nav |
| Mobile Wide | 600–767px | Optional 2-up tile, 48px hero |
| Tablet | 768–1023px | 2-up product grid, 48–60px hero, partial inline nav |
| Desktop | 1024–1279px | 4-up product grid, full inline nav, 60–70px hero |
| Large | 1280–1903px | Maximum 1280px container, 70px hero, full editorial spacing |
| XL | ≥1920px | Wider container, increased gutters, 70px hero stays |

### Touch Targets
- Primary gold pills: min 44px tap height, 20–24px horizontal padding on mobile
- Carousel arrows: 44px tap area at all breakpoints
- Nav links collapse into a full-screen hamburger menu under 1024px

### Collapsing Strategy
- **Nav**: Horizontal categories collapse to hamburger under 1024px; pre-header bar remains visible
- **Hero**: 70px → 60px → 48px → 42px → 36px progressive scaling, weight stays at 300/400 throughout
- **Product grid**: 4-up → 2-up → 1-up with maintained aspect ratios
- **Photography**: Hero photographs preserve their full-bleed treatment at every breakpoint
- **Footer**: 4-column link grid collapses to accordion sections, logo glyph centres on mobile

### Image Behavior
- Hero photography uses art-directed crops at mobile (often a tighter detail-crop of the same scene)
- Product imagery maintains square or 4:3 aspect ratio at all breakpoints
- Recipe / family-card imagery preserves photographic abundance — pasta-on-marble, espresso-pour, market-stall density

---

## Agent Prompt Guide

### Quick Reference
- Brand Accent: Trattoria Gold (`#f8ae00`)
- Page Background: Pure White (`#ffffff`)
- Primary Text: Pure Black (`#000000`) / Material near-black `rgba(0, 0, 0, 0.87)`
- Secondary Text: Warm Slate (`#333333`)
- Display Font: Libre Baskerville 22–70px with positive letter-spacing (`0.63–2px`)
- Body Font: Libre Baskerville regular / system-ui sans for buttons
- Primary CTA: Gold (`#f8ae00`) bg, white text, `2px solid #f8ae00` border, `20–30px` pill radius
- Card Shadow: `rgba(0, 0, 0, 0.1) 0 2px 10px 0`
- Wine-Warm Hover Shadow: `rgba(199, 91, 18, 0.4) 0 6px 16px`
- Inline Link: Cobalt Blue (`#1976d2`)
- Heritage Frame: Cream (`#c9a973`)

### Example Component Prompts
- "Create an Eataly hero on `#ffffff` with a full-bleed pasta-on-marble photograph. Overlay a 70px Libre Baskerville weight 300 italic headline with `2px` letter-spacing in `#000000`, left-aligned. Below, a 20px Libre Baskerville weight 400 deck with `0.2px` letter-spacing. Pair with a primary gold CTA — `#f8ae00` bg, `2px solid #f8ae00` border, white 15px sans weight 500 label, `0px 20px` padding, `30px` border-radius. On hover the CTA flips to `rgba(0, 0, 0, 0.04)` ghost-fill with `#333` text and a `rgba(199, 91, 18, 0.4) 0 6px 16px` wine-warm shadow."
- "Build a 4-up product grid on `#ffffff`. Each card has `3px` radius, no border, `rgba(0, 0, 0, 0.1) 0 2px 10px 0` default shadow. Inside: square product photograph, then 22px Libre Baskerville weight 300 product name in `#000` with `0.63px` letter-spacing, then a 16px Libre Baskerville price. Add a Trattoria Gold (`#f8ae00`) 12px UPPERCASE 'PREMIUM' flag in the top-left of premium items, `4px 12px` padding, `2px` radius."
- "Design a primary nav bar — pure white background, 80px height, 1px bottom border. Eataly wordmark left at 140px wide. Pre-header above it: `#000000` band, 32px height, gold (`#f8ae00`) promo text. Category links centred at 14px sans weight 500 in `#333`, sentence case. On hover, gold underline appears."
- "Create a family-recipe card — pure white bg, `1px solid #c9a973` cream border (heritage frame), `3px` radius, `rgba(0, 0, 0, 0.1) 0 2px 10px 0` shadow. Inside: 22px Libre Baskerville weight 400 italic title in `#000` with `0.63px` letter-spacing, 16px Libre Baskerville body in `#333` at line-height `1.50`, and a gold pill 'View Recipe' CTA at the bottom."
- "Design a sticky cart-bar — fixed at viewport bottom, full-width, white background, `rgba(0, 0, 0, 0.11) 0px -2px 20px 0px, rgba(0, 0, 0, 0.2) -1px 0px 4px 0px` shadow. Inside: cart preview thumbnails on left, total price in 18px Libre Baskerville weight 400 in `#000`, gold pill 'Checkout' CTA on right at `#f8ae00` bg, white text, `30px` radius."

### Iteration Guide
1. Default to pure white (`#ffffff`) page background — never tinted, photography supplies all warmth.
2. Trattoria Gold (`#f8ae00`) is the brand-action contract — primary CTAs, premium flags, brand glyph only.
3. Libre Baskerville is the only display face — across hero, section titles, body, editorial. No second face.
4. Positive letter-spacing on display (`0.63–2px`) — the trattoria signage register.
5. Sentence case or title case throughout — UPPERCASE reserved for occasional buttons and pre-header gold callouts.
6. Border-radius is wide-ranged: sharp `0px` photography, subtle `2–3px` cards / inputs, full-pill `20–30px` CTAs, circle `50%` carousel arrows.
7. Default card elevation is `0 2px 10px rgba(0, 0, 0, 0.1)` — soft, warm, market-stall lift.
8. Wine-warm orange shadow (`rgba(199, 91, 18, 0.4) 0 6px 16px`) on CTA hover — the brand's interactive thumbprint.
9. Cobalt blue (`#1976d2`) for inline editorial / utility links — Material-Design-tinged secondary accent. Never gold.
10. Cream (`#c9a973`) for heritage and family-history frames — gilded counterpoint to the gold pills, used sparingly.
