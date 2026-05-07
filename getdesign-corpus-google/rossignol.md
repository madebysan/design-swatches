---
version: alpha
name: "Rossignol"
description: "Alpine ski-patrol catalog with mountain-rouge accents, condensed Gotham caps, and 10px button radii."

colors:
  background: "#ffffff"
  surface: "#212529"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#242f48"
  primary: "#ef212b"
  on-primary: "#ffffff"
  border: "#ced4da"
  focus-ring: "#ef212b"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Gotham, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Gotham, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Gotham, ui-sans-serif, system-ui, sans-serif"
    fontSize: 42px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Gotham, ui-sans-serif, system-ui, sans-serif"
    fontSize: 29px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Gotham, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Gotham, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Gotham, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Gotham, ui-sans-serif, system-ui, sans-serif"
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

# Rossignol Design System

## Overview

Rossignol's site reads like a printed expedition catalog that someone tightened up for the web without losing the alpine grit. The page sits on pure white (`#ffffff`) with deep slate ink (`#212529`) for body copy, and the entire chrome falls back to grayscale until a single chromatic moment — the rooster-rouge `#ef212b` — appears on a sale badge, a ski-patrol logo, or the rare CTA hover. The typography is Gotham across the board (`gotham`, `GothamBook`, `GothamMedium`, `GothamBold` — same family, four weights, no second face), often pushed into 1.6px tracked uppercase for buttons and section labels. That uppercase Gotham at 16–24px with letter-spacing — paired with a generous `10px` button radius — is the move that makes a Rossignol page feel like ski-patrol gear rather than a sportswear e-commerce template.

Photography does the loudest work: full-bleed alpine action shots, racers carving powder, gear hung against snow-blue gradients, helmets photographed like industrial objects. Where most ski-brand sites lean into glassy sapphire gradients and chrome-blue overlays, Rossignol stays committed to a **paper-white canvas** with photography supplying every saturated note. The chrome itself stays in pure neutrals — Gotham caps over white, hairline `1px` borders in `#ced4da`, and shadows that cast warm-brown (`rgba(43, 36, 25, 0.4)`) rather than cold-blue, like sun on a wood porch rather than fluorescent on a showroom floor.

The third defining trait is the **paratroop button**: deep navy fill (`#242f48`), white Gotham label uppercase, `10px` radius, no border, that flips on hover to white background with a `2px solid #242f48` outline and a soft `0 0 15px rgba(0,0,0,0.1)` halo. It's an action button shaped like a piece of kit — corners rounded enough to read as tactile, bold enough to read across a 30px viewport, and the warm shadow keeps it from feeling clinical.

**Key Characteristics:**
- Paper white canvas (`#ffffff`) — never tinted, photography supplies the warmth
- Deep slate ink (`#212529`) for body copy, true black (`#000000`) for primary buttons
- Single Gotham family across four weights — `gotham` / `GothamBook` / `GothamMedium` / `GothamBold`
- Patrol Red brand accent (`#ef212b`) — sale states, ski-patrol logo, hover-state highlights
- Navy CTA fill (`#242f48`) — the secondary "kit" button color
- `10px` border-radius on buttons and dialogs — the brand's tactile signature
- 1.6px tracked uppercase on display buttons (`text-transform: uppercase`, `letter-spacing: 1.6px`)
- Warm-brown shadows (`rgba(43, 36, 25, 0.4) 0 3px 5px`) — sun-on-wood, not fluorescent
- 1px hairline borders in `#ced4da` — Bootstrap-rooted gray for dividers
- Bootstrap grid underneath (4-up product layout, 1260px / 1440px container caps)
- Rare orange-amber sun glow (`#fcb900`) appears as focus background in select buttons
- Full-bleed alpine action photography — racers, patrol, gear, never studio

## Colors

### Primary Brand
- **Patrol Red** (`#ef212b`): The single chromatic anchor. The rooster-rouge of the Rossignol mark — used on sale prices, "On Sale" badges, the ski-patrol logo, and primary-link emphasis. So rare in chrome that it reads as a stamp.
- **Slate Ink** (`#212529`): Default text color across body, navigation, and product names — Bootstrap `gray-900`. Slightly softened from pure black for editorial readability.
- **True Black** (`#000000`): Primary CTA background, full-bleed dark scrims, ski-patrol logo black-out variant.

### Brand Accent / Secondary
- **Patrol Navy** (`#242f48`): Secondary CTA fill, hover-outline color — the "kit" navy that anchors most of the chrome on category pages.
- **Sky Blue** (`#00a1e0`): Skin primary color (CSS var `--skin-primary-color-1`) — used for product-config selectors, link emphasis on dark backgrounds, and ski-resort wayfinding.
- **Light Blue** (`#467bd2`): Tertiary blue accent — found on info banners and resort-status indicators.
- **Cobalt Blue** (`#3156bc`): Form-validation success indicator, occasional brand-secondary accent.
- **Patrol Green** (`#59dd92`): Success-state indicator for cart confirmations and stock badges. Used sparingly.
- **Sun Amber** (`#fcb900`): Focus-state background on certain CTAs — appears as a high-vis flash when a button is keyboard-focused.

### Neutrals & Text
- **Slate Ink** (`#212529`): Primary headlines and body text.
- **Charcoal Gray** (`#333333`): Secondary text, paragraph copy alternative — Bootstrap `gray-8`.
- **Mid Gray** (`#444444`): Tertiary text and link color in default state — Bootstrap `gray-6`.
- **Body Gray** (`#666666`): Captions, metadata, breadcrumbs — Bootstrap `gray-5`.
- **Quiet Gray** (`#949494`): Disabled-state text, placeholder text, ancillary captions.
- **Soft Gray** (`#999999`): Divider text on alternate surfaces — Bootstrap `slightly-darker-gray`.
- **Hairline Gray** (`#ced4da`): The default 1px border — used between product tiles, in form-field outlines, and below headers.
- **Cool Gray** (`#cccccc`): Secondary divider color — Bootstrap `gray-3`.
- **Faint Gray** (`#eeeeee`): Ghost-fill on alternate-row tables — Bootstrap `gray-2`.

### Surface & Borders
- **Page Surface** (`#ffffff`): Default page canvas — committed pure white, never tinted.
- **Input Surface** (`#f6f6f6`): Newsletter and email-capture input fills — barely-warm gray.
- **Hairline Border** (`#ced4da`): Dropdown borders, table dividers, search-pill outline.
- **Black Underline** (`#000000`): Solid 1px bottom-border used as section ribs on dark-mode editorial blocks.

### Functional / State
- **Sale Red** (`#ef212b`): Sale prices, "WEB SPECIAL" badges, end-of-season markdowns. Pairs with strikethrough on original price.
- **Validation Green** (`#59dd92`): "Added to bag" confirmation, stock-available indicators.
- **Error Red** (`#ff0000`): Pure red reserved for inline form errors only — distinct from the brand patrol red.

### Shadow / Atmospheric
- **Warm Brown Shadow** (`rgba(43, 36, 25, 0.4)`): The brand's signature elevation tint — used on lift-out panels and hero overlays, casts sun-on-wood warmth.
- **Soft Drop** (`rgba(0, 0, 0, 0.35) 2px 2px 3px -1px`): Image-card lift on the catalog grid.
- **Halo** (`rgba(0, 0, 0, 0.1) 0 0 15px`): Hover halo around the navy CTA — the alpine glow.

### Gradient System
- Rossignol is **near gradient-free in chrome**. Photography does the gradient work — sky-to-snow tonal shifts inside hero imagery do the lifting that CSS gradients do elsewhere. The single decorative gradient that surfaces is a `transparent → rgba(0,0,0,0.5)` linear-bottom scrim used to anchor white captions over alpine photography.

## Typography

### Font Family
- **Display & Body**: `gotham`, with capitalization variants `GothamBook` (regular), `GothamMedium` (500), `GothamBold` (700). Single-family discipline across every typographic role.
- **Fallback Stack**: `Arial, Helvetica, sans-serif`
- **System Fallback**: `-apple-system` for utility chrome and Apple-platform-tailored copy
- **OpenType Features**: Standard ligatures, lining numerals on prices and ski-resort altitudes

*Note: Gotham is a licensed face from Hoefler & Co. For external implementations, **Inter**, **Söhne**, or **Proxima Nova** are the closest workmanlike-geometric substitutes. Avoid display-trend geometrics like Avenir or Futura — they break the catalog feel.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero Display | gotham | 48px (3.00rem) | 400 | 1.20 | -3.6px | Alpine hero headlines, full-bleed photo overlays |
| Hero Display Bold | GothamBook | 36.8px (2.30rem) | 700 | 1.00 | normal | Heavyweight ski-race / patrol page heads |
| H1 | gotham | 36px (2.25rem) | 400 | 1.20 | -2.7px | Page-level titles, category landing heads |
| H1 Bold Link | gotham | 36px (2.25rem) | 700 | 1.00 | -2.7px | Inline mega-link callouts on hero zones |
| H1 Stat | GothamBook | 30px (1.88rem) | 700 | 1.50 | normal | Sub-section heads on resort and product pages |
| H2 | gotham | 24px (1.50rem) | 700 | 1.20 | -1.8px | Section heads inside product grids |
| H2 Caps | gotham | 24px (1.50rem) | 400 | 1.00 | normal | UPPERCASE section labels |
| H3 | gotham | 21.33px (1.33rem) | 500 | 2.00 | normal | Block-quoted feature heads |
| H4 | gotham | 20px (1.25rem) | 500 | 1.36 | normal | Spec heads on product detail |
| H5 | gotham | 18px (1.13rem) | 700 | 1.20 | -0.54px | Card titles |
| Body | gotham/GothamBook | 16px (1.00rem) | 400 | 1.50 | normal | Default reading copy, product descriptions |
| Button (primary) | Gotham | 16px (1.00rem) | 400 | 1.06 | 1.6px | UPPERCASE, the alpine-CTA signature |
| Button (compact) | GothamBold | 14px (0.88rem) | 700 | 1.21 | normal | UPPERCASE compact CTAs, "ADD TO BAG" |
| Nav Link | gotham | 14px (0.88rem) | 500 | 2.00 | normal | UPPERCASE primary nav, top categories |
| Caption (subtle) | gotham | 14px (0.88rem) | 500 | 1.50 | normal | UPPERCASE meta-labels, "NEW", "BESTSELLER" |
| Footer Link | gotham | 13px (0.81rem) | 700 | 1.15 | normal | UPPERCASE footer nav and column heads |
| Resort Caption | gotham | 13px (0.81rem) | 300 | 1.50 | normal | Capitalize — resort names, altitude labels |
| Microcopy | gotham | 12px (0.75rem) | 400 | 1.50 | normal | Default microcopy line — fine print |
| Footer Microcopy | Gotham | 11px (0.69rem) | 700 | 1.91 | 1.1px | UPPERCASE legal labels, copyright |

### Principles
- **One family, four weights**: Gotham across every role. There is no second face. Discipline comes from weight (`400` / `500` / `700`) and tracking (`-3.6px` to `+1.6px`), not from typeface mixing.
- **Caps + tracking is the brand fingerprint**: Buttons, nav, footer heads, and section labels run `text-transform: uppercase` with `letter-spacing: 1.1–1.6px`. Lowercase Gotham reads as informal; uppercase Gotham reads as ski-patrol.
- **Negative tracking on display, positive on caps**: Hero display sits at `-3.6px` to `-1.8px` for tight alpine presence; uppercase chrome opens out to `+1.1px` to `+1.6px` for legibility on small UI.
- **Bold is functional, not decorative**: 700-weight Gotham appears on H5, footer heads, sale prices, and compact CTAs. The hero stays at 400 — the brand earns its bigness through size, not weight.
- **Body line-height is generous (1.50)**: Catalog copy runs open and readable; only display caps drop to 1.00–1.20 for tight alpine presence.

## Layout

### Spacing System
- Base unit: 4px (with 8px and 16px as the rhythm increments for components)
- Scale: 1px, 4px, 7.5px, 8px, 10px, 12px, 15px, 16px, 20px, 24px, 32px, 40px
- Notable: The most-used spacing value is 16px (268 occurrences) — Rossignol's grid is rooted on a strict 16px rhythm. Section padding lives at 24–40px on desktop and collapses to 16–20px on mobile.

### Grid & Container
- Max content width: 1260–1440px on category and product pages
- Hero: full-width photograph, text overlay positioned via 12-column Bootstrap grid (typically left-aligned columns 2–6)
- Product grid: 4-up desktop, 2-up tablet, 1-up mobile — generous 16–24px gutters
- Footer: 4–5-column dense link grid with rooster wordmark left-aligned, social icons right-aligned

### Whitespace Philosophy
- **Catalog density on commerce, expedition pacing on stories**: Product grids run tight at 16–24px between tiles; editorial story pages give 64–96px between sections.
- **Photography as the visual structure**: Full-bleed alpine imagery does the work that decorative dividers do elsewhere. Pages read as photo → grid → photo → grid.
- **Quiet chrome, loud photography**: Navigation, footer, and utility elements use thin 1px borders in `#ced4da` and warm-brown shadows. The interface stays out of the way of the alpine work.

### Border Radius Scale
- Sharp (`0px`): Default for product photography, full-bleed imagery, story cards
- Subtle (`2px`): Sale and feature badges
- Compact (`3px`): Search pills, form inputs, dropdowns
- Tactile (`10px`): The signature button radius — primary CTAs, dialogs, newsletter inputs
- Pill (`50%`): Color swatches, carousel arrows, social icons

## Elevation & Depth

| Level | Box Shadow | Use Case |
|-------|-----------|---------|
| Flat (Level 0) | `none` | Page canvas, default product cards, body content |
| Hairline (Level 1) | `1px solid #ced4da` | Product grid boundaries, footer separators, table dividers |
| Warm Lift (Level 2) | `rgba(43, 36, 25, 0.4) 0 3px 5px 0` | Featured product tiles, sun-on-wood lift |
| Modal (Level 3) | `rgba(0, 0, 0, 0.06) 0 1px 6px 0, rgba(0, 0, 0, 0.16) 0 2px 32px 0` | Cart drawer, modal dialogs, mega-menu panels |
| Halo (Level 4) | `rgba(0, 0, 0, 0.1) 0 0 15px 0` | CTA hover state — the alpine glow around active buttons |
| Photo Scrim (Level 5) | `linear-gradient(180deg, transparent 60%, rgba(0,0,0,0.25) 100%)` | Hero photographic CTAs needing legibility |

**Shadow Philosophy**: Rossignol treats elevation the way an outdoor catalog does — sparingly, and warm when it does appear. The signature warm-brown shadow tint (`rgba(43, 36, 25, 0.4)`) keeps the system from feeling clinical: shadows cast sun-on-wood, not fluorescent-on-glass. Hover halos use neutral black at low opacity, but lift shadows on featured tiles always carry the warm brown. The result is a system that feels expedition-warm, not e-commerce-cold.

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

**Primary Black**
- Background: True Black (`#000000`)
- Text: Pure White (`#ffffff`)
- Padding: `13.5px 32px`
- Border: `0px none`
- Border-radius: `10px` — the brand's tactile signature
- Box-shadow: `none` at rest
- Font: 16px Gotham weight 700, mixed case allowed but UPPERCASE preferred with `1.6px` tracking
- Hover: background flips to `#ffffff`, text becomes Patrol Navy (`#242f48`), border becomes `2px solid #242f48`, shadow `rgba(0, 0, 0, 0.1) 0 0 15px 0` — the alpine halo
- Active: background `#ffffff`, text `#3d3d3d`, border `2px solid #3d3d3d`, opacity `0.6`
- Focus: background `#ffdd00` (sun amber), text inherits, inset shadow `rgba(0, 0, 0, 0.1) 0 0 0 999px inset` — high-vis keyboard state
- Use: Primary CTAs — "ADD TO BAG", "SHOP NOW", "EXPLORE THE RANGE"

**Patrol Navy**
- Background: Patrol Navy (`#242f48`)
- Text: Pure White (`#ffffff`)
- Padding: `10px 32px`
- Border-radius: `0px` (sharp variant for compact inline CTAs)
- Border: `0px none`
- Hover: background `#ffffff`, text `#242f48`, border `2px solid #242f48`, halo shadow
- Use: Secondary CTAs in alpine zones — "VIEW ALL", "READ THE STORY"

**Ghost / Underlined Link**
- Background: `transparent`
- Text: Slate Ink (`#212529`) or Mid Gray (`#444444`)
- Padding: `12px 0`
- Border: `1px solid transparent` default, `2px solid #242f48` on hover
- Border-radius: `0px`
- Font: 14px GothamBold weight 700 UPPERCASE, `1.2px` tracking
- Hover: text shifts to Patrol Navy (`#242f48`), inline `2px solid` border appears
- Use: Tertiary actions — "Learn More", "View Specs", inline editorial links

**Search Field (Inline Button)**
- Background: Pure White (`#ffffff`)
- Text: Slate Ink (`#212529`)
- Padding: `4px 4px 4px 32px`
- Border: `1px solid #ced4da`
- Border-radius: `3px`
- Focus: border `1px solid #707070`, outline `2px solid #70b3ff`, inset white shadow

**Round Carousel Arrow**
- Background: `rgba(0, 0, 0, 0.2)` default
- Color: transparent text (icon-only)
- Border-radius: `50%`
- Hover: background `#ffffff`, text becomes Patrol Navy, `2px solid #242f48` border, halo shadow

### Cards & Containers

**Product Card**
- Background: Pure White (`#ffffff`)
- Border: `1px solid #ced4da` only at grid boundaries — none on the card itself
- Border-radius: `0px` for the photograph, `0px` for the wrapper
- Box-shadow: `none` at rest, optional warm-brown lift `rgba(43, 36, 25, 0.4) 0 3px 5px 0` on featured tiles
- Internal padding: 0 around image, 12px above name, 4px between name and price
- Hover: subtle 1.02× image scale within fixed crop, name underline appears

**Modal / Dialog**
- Background: Pure White (`#ffffff`)
- Border-radius: `10px` — matches the primary CTA radius for kit-tactile feel
- Box-shadow: `rgba(0, 0, 0, 0.06) 0 1px 6px 0, rgba(0, 0, 0, 0.16) 0 2px 32px 0` — soft expedition lift
- Padding: 24px–40px

### Badges / Tags / Pills

**Sale Badge**
- Background: Patrol Red (`#ef212b`)
- Text: Pure White (`#ffffff`)
- Padding: `4px 8px`
- Border-radius: `2px`
- Font: 11px Gotham weight 700 UPPERCASE, `1.1px` tracking
- Use: Sale flag in upper-left of product cards

**"NEW" / "BESTSELLER" Badge**
- Background: Patrol Navy (`#242f48`) or `transparent` with border
- Text: Pure White (`#ffffff`)
- Padding: `4px 10px`
- Border-radius: `2px`
- Font: 11px Gotham weight 500 UPPERCASE, `1.1px` tracking

**Color Swatch Dot**
- Size: 16px × 16px (selectable), 12px × 12px (count indicator)
- Border-radius: `50%`
- Border: `1px solid #ced4da` default, `1px solid #000000` on selected

### Inputs & Forms
- Background: Pure White (`#ffffff`) — `#f6f6f6` on newsletter inputs
- Text color: Slate Ink (`#212529`)
- Border: `1px solid #ced4da` default
- Border-radius: `3px` for compact inputs, `10px` for newsletter capture pills
- Padding: `4px 4px 4px 32px` (compact), `10px 20px` (large)
- Font: 16px GothamBook weight 400
- Placeholder: `#949494`
- Focus: border `1px solid #707070`, outline `2px solid #70b3ff` (Bootstrap focus blue)
- Checkbox: `1px solid #707070`, `2–5px` radius, focus `2px solid #70b3ff`

### Navigation

**Top Utility Bar**
- Background: Pure White (`#ffffff`) or Slate Ink on dark editorial pages
- Height: 32px
- Font: 11–12px GothamBook weight 400
- Content: country/lang switcher, ski-resort wayfinding, account links
- Border-bottom: `1px solid #ced4da`

**Primary Nav Bar**
- Background: Pure White (`#ffffff`)
- Height: 64–80px
- Logo: Rossignol wordmark + rooster glyph, ~120–180px wide, left-aligned
- Categories: "Skis · Snowboards · Apparel · Bags · Lifestyle · Resorts · Stories" — center-aligned, 14px Gotham weight 500 UPPERCASE
- Right cluster: search pill (`#ffffff` background, `1px #ced4da` border, `3px` radius), wishlist heart, account icon, bag icon
- Hover: category underline appears 4px below text, mega-menu drops with `rgba(0, 0, 0, 0.06) 0 1px 6px` soft shadow
- Border-bottom: `1px solid #ced4da`

### Decorative Elements

**Full-bleed Alpine Photography**
- Hero, category, and editorial heroes extend edge-to-edge
- When a scrim is required, it's a soft `linear-gradient(180deg, transparent 60%, rgba(0,0,0,0.25) 100%)` from bottom — applied sparingly
- The rooster glyph appears as a solid `#ef212b` mark on patrol-red moments and as `#000000` on default chrome

## Do's and Don'ts

### Do
- Use Patrol Red (`#ef212b`) as the single chromatic accent — sale states, ski-patrol logo, hover-state emphasis
- Run Gotham at four weights (400 / 500 / 700) and lean on caps + 1.1–1.6px tracking for buttons and nav
- Default to `10px` border-radius on primary buttons and dialogs — the brand's tactile signature
- Use full-bleed alpine action photography — racers, patrol, gear in real conditions, never studio
- Cast warm-brown shadows (`rgba(43, 36, 25, 0.4)`) on featured tiles for sun-on-wood elevation
- Run hero display at 36–48px Gotham weight 400 with `-1.8px` to `-3.6px` letter-spacing
- Keep body copy at 16px Gotham regular with 1.50 line-height for catalog readability
- Reserve Patrol Navy (`#242f48`) for hover states and secondary CTAs — the "kit" navy
- Use 1px hairline borders in `#ced4da` for grid boundaries and form fields
- Treat the rooster glyph as a stamp — appears in red on accent moments, black on default chrome

### Don't
- Don't use cool-blue shadows — Rossignol's elevation is always warm-brown (`rgba(43, 36, 25, 0.4)`), never `rgba(0, 100, 200, ...)`
- Don't introduce a second typeface — Gotham across the system, no serif counterpoint, no display alternative
- Don't soften the page background to off-white — Rossignol commits to pure `#ffffff` for photographic contrast
- Don't lowercase primary CTAs — UPPERCASE Gotham with 1.6px tracking is the alpine-button signature
- Don't apply the `10px` button radius to inline form inputs — those stay at `3px` for compact density
- Don't use display-trend typography (geometric sans, condensed display, slab serifs) — Gotham is the brand
- Don't bold display headlines — weight 400 at 36–48px is the calm-confidence move
- Don't introduce mid-range radii (5–8px or 12–24px) — sharp, 2px, 3px, or 10px, nothing in between
- Don't crowd photography with overlay scrims — choose images with built-in negative space instead
- Don't use Patrol Red on primary CTAs — preserve its rarity for sale states and the rooster mark

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <320px | Single-column, hero type drops to 28–32px, 1-up product grid |
| Mobile | 320–639px | Single-column, 32–36px hero, hamburger nav, 1-up product grid |
| Mobile Wide | 640–767px | Optional 2-up tile, 36px hero |
| Tablet | 768–991px | 2-up product grid, 40–44px hero, partial inline nav |
| Desktop | 992–1199px | 4-up product grid, full inline nav, 44–48px hero |
| Large | 1200–1259px | Maximum 1260px container, full editorial spacing |
| XL | ≥1440px | 1440px container, 48px hero, 4-up grid with wider gutters |

### Touch Targets
- Primary CTAs: min 44px tap height, 24–32px horizontal padding on mobile
- Nav links collapse into a full-screen hamburger menu under 992px with 56px row heights
- Color swatch picker: 24px tap area on mobile (16px visual)
- Carousel arrows: 44px tap area at all breakpoints

### Collapsing Strategy
- **Nav**: Horizontal categories collapse to hamburger under 992px; the utility bar stays visible
- **Hero**: 48px → 40px → 36px → 32px → 28px progressive scaling, weight stays at 400 throughout
- **Product grid**: 4-up → 2-up → 1-up with maintained square aspect ratios
- **Photography**: Hero photographs preserve their full-bleed treatment at every breakpoint, with art-directed crops at mobile widths
- **Footer**: 4-column link grid collapses to accordion sections on mobile, rooster wordmark moves to centered top of footer

### Image Behavior
- Hero photography uses art-directed crops at mobile (often a tighter portrait crop of the same scene)
- Product imagery maintains square aspect ratio at all breakpoints
- Story imagery preserves full-bleed treatment but reduces intermediate margins

---

## Agent Prompt Guide

### Quick Reference
- Brand Accent: Patrol Red (`#ef212b`)
- Page Background: Pure White (`#ffffff`)
- Primary Text: Slate Ink (`#212529`)
- Primary Button: Black (`#000000`) bg, White text, `10px` radius, 1.6px-tracked uppercase
- Secondary Button: Patrol Navy (`#242f48`) bg
- Hairline Border: `#ced4da`
- Sale State: Patrol Red (`#ef212b`)
- Warm Shadow: `rgba(43, 36, 25, 0.4) 0 3px 5px 0`
- Halo: `rgba(0, 0, 0, 0.1) 0 0 15px 0`

### Example Component Prompts
- "Create a Rossignol-style hero on `#ffffff` with a full-bleed photograph of a skier carving powder. Overlay a 48px Gotham weight 400 headline with `-3.6px` letter-spacing in pure white, left-aligned at column 2 of a 12-column grid. Below, a 16px Gotham regular subhead, then a primary CTA — `#000000` background, white 16px Gotham UPPERCASE label with `1.6px` letter-spacing, `13.5px 32px` padding, `10px` border-radius. On hover the button flips to white with a `2px solid #242f48` border and a `rgba(0, 0, 0, 0.1) 0 0 15px 0` halo."
- "Build a 4-up product grid on `#ffffff`. Each card is a square photograph with `0px` radius, no shadow, no border. Below the image: 14px Gotham weight 500 product name in `#212529`, 14px Gotham weight 400 price below, then a 12px gray (`#666666`) caption '4 colors'. Add a Patrol Red (`#ef212b`) 11px Gotham weight 700 UPPERCASE 'SALE' badge with `1.1px` tracking in the top-left of any sale items, `4px 8px` padding, `2px` radius."
- "Design a primary nav bar — pure white background, 64px height, 1px bottom border (`#ced4da`). Rossignol wordmark left at 140px, category links centered at 14px Gotham weight 500 UPPERCASE, search pill (`#ced4da` border, `3px` radius) + heart + account + bag icons right-aligned. On hover, a 4px underline appears below the active category and a mega-menu panel drops with `rgba(0, 0, 0, 0.06) 0 1px 6px` soft shadow."
- "Design a featured story tile — pure white background, full-bleed alpine photograph at the top with `0px` radius, then 16px above-the-fold padding. Eyebrow: 11px Gotham weight 700 UPPERCASE with `1.1px` tracking in `#666`. Headline: 24px Gotham weight 700 in `#212529`. Below: a 14px Gotham regular dek in `#444`. Add a `rgba(43, 36, 25, 0.4) 0 3px 5px 0` warm-brown shadow on hover."
- "Create a newsletter capture — `#f6f6f6` input field, 16px Gotham weight 400 placeholder in `#949494`, `10px 20px` padding, `10px` border-radius, `1px solid transparent` border. Pair with a 16px Gotham weight 700 UPPERCASE 'SUBSCRIBE' button — `#000000` bg, white text, `10px` radius, `1.6px` tracking."

### Iteration Guide
1. Default to pure white (`#ffffff`) page background — never off-white, never warm-tinted
2. Use full-bleed alpine action photography — racers, patrol, gear in real conditions
3. Gotham across four weights (400 / 500 / 700) is the typeface — no second face, ever
4. UPPERCASE + `1.1–1.6px` tracking is the button and nav signature — lowercase reads as informal
5. Patrol Red (`#ef212b`) is the brand anchor — sale states, ski-patrol mark, and hover emphasis only
6. `10px` border-radius is the tactile signature on primary CTAs and dialogs — pair with `0–3px` on inputs and badges
7. Warm-brown shadows (`rgba(43, 36, 25, 0.4)`) for elevation, never cool-blue
8. Hero display at 36–48px Gotham weight 400 with `-1.8px` to `-3.6px` letter-spacing
9. Body copy at 16px Gotham regular with `1.50` line-height for catalog readability
10. The alpine halo (`rgba(0, 0, 0, 0.1) 0 0 15px 0`) appears on CTA hover — the brand's "kit-glow" moment
