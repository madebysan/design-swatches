---
version: alpha
name: "Blue Bottle Coffee"
description: "Espresso ink on paper white, ABC Marfa serif caps, sharp 0px buttons, modernist single-origin chrome."

colors:
  background: "#ffffff"
  surface: "#333333"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#999999"
  primary: "#006fff"
  on-primary: "#ffffff"
  border: "#6c6864"
  focus-ring: "#006fff"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "ABC Marfa, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "ABC Marfa, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "ABC Marfa, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "ABC Marfa, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "ABC Marfa, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "ABC Marfa, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "ABC Marfa, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "ABC Marfa, ui-sans-serif, system-ui, sans-serif"
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

# Blue Bottle Coffee Design System

## Overview

Blue Bottle's site is third-wave specialty coffee rendered as a digital object. The page sits on pure white (`#ffffff`) with deep espresso ink (`#333333`) for body copy, and the entire system is built on a relationship between two custom typefaces from ABC Dinamo — ABC Marfa (a humanist serif used at uppercase display sizes with `1.6–2.4px` letter-spacing) and ABC Diatype (a precise neo-grotesk used everywhere else). Imagery is sparse and product-led, navigation is whisper-quiet at 14–16px Diatype, and entire screens unfold with nothing but a centred Marfa caps headline, a paragraph of dense Diatype body, and one plain rectangular button. There is no chrome here. No gradients announce themselves, no shadows lift cards, and the only colour that consistently surfaces beyond the espresso-and-paper neutrals is the iconic Blue Bottle blue (`#006fff`) — a single saturated note used for the bottle mark and select inline links.

The signature typographic move is **Marfa caps with positive tracking**. ABC Marfa Regular at 16–24px set in UPPERCASE with `1.6px` letter-spacing reads as letterpress signage — the typographic register of a single-origin coffee bag, not a startup landing page. Pair that with ABC Diatype at 16px regular for body, sentence-case throughout, and the system reads as a quietly designed cookbook rather than a tech product.

The third defining trait is **near-zero visual noise**. Border radius defaults to `0` for buttons and inputs (the system has effectively one CSS-tokened radius — `4px` — and only one input uses it). Box-shadows are absent except for a single subtle drop on carousel arrows (`rgba(28, 29, 33, 0.12) 0px 0px 18px`). Imagery sits centred in generous negative space, products photographed against sage-green and kraft-cream backdrops. The aesthetic is modernist letterpress restraint translated into pixels — exactly the editorial register that built Aesop and Kinfolk before it, applied to a coffee roaster who treats single-origin sourcing the way an art gallery treats provenance.

**Key Characteristics:**
- Paper white canvas (`#ffffff`) — never tinted, never warm-shifted
- Espresso ink (`#333333`) — softer than pure black for editorial body copy
- Dual-typeface contract — ABC Marfa serif for display caps, ABC Diatype grotesk for everything else
- Sharp `0px` border-radius on buttons and chrome — letterpress rectangles, never pills
- ABC Marfa caps with `1.6px`–`2.4px` positive letter-spacing — single-origin signage register
- Sentence-case Diatype throughout body, navigation, and most CTAs (UPPERCASE saved for accents)
- Blue Bottle Blue (`#006fff`) — the brand glyph and select link colour, used sparingly
- No drop shadows on chrome — the system is flat, paper-like, modernist
- Generous whitespace between sections — magazine pacing, never commerce-page tightness
- Hairline `2px` border on featured carousel arrows in `rgba(255, 255, 255, 0.5)` — barely-there
- No CSS gradients on UI — surfaces are flat tinted paper
- Centred composition for hero and editorial moments — typography as still-life

## Colors

### Primary Brand
- **Blue Bottle Blue** (`#006fff`): The single saturated brand note — used for the iconic bottle mark, select inline links, and editorial-link emphasis. So rare in chrome that it reads as a stamp. (Estimated based on brand identity; the dembrandt extraction surfaced predominantly neutral palette with `--tw-ring-color` `rgba(59,130,246,.5)` confirming the brand-blue family.)
- **Espresso Ink** (`#333333`): Primary text, primary button background, headline ink. Slightly softened from pure black for long-form editorial readability.
- **Pure White** (`#ffffff`): Page canvas — committed pure white, never off-white tinted.

### Brand Accent / Secondary
- **Tan / Kraft** (`#6c6864`): Editorial muted text on cream-and-sage backdrops — the warm gray that pairs with kraft-paper photography.
- **True Black** (`#000000`): Used as inverse text on light surfaces and as the deepest ink on key brand surfaces.
- **Tw Ring Blue** (`rgba(59,130,246,.5)`): Tailwind-default focus ring colour — confirms the system uses Tailwind under the hood with the brand-blue family at 50% opacity.

### Neutrals & Text
- **Espresso Ink** (`#333333`): Primary headlines and body text — the system's most-frequent text colour (144 occurrences).
- **Warm Stone** (`#6c6864`): Secondary text on editorial pages, captions, byline metadata — warm-tinted gray for tonal continuity with kraft photography.
- **True Black** (`#000000`): Reserved for inverse states and the rare on-light heavyweight emphasis.
- *Estimated stops below were not surfaced in the dembrandt scan but are implied by the modernist neo-grotesk system; treat as design-direction guides.*
- **Mid Gray** (`#999999`) /* estimated */: Disabled-state text, placeholder text.
- **Hairline Gray** (`#e5e5e5`) /* estimated */: Section dividers, table borders.
- **Surface Cream** (`#faf8f5`) /* estimated */: Alternate-section background, banner panels — implied by kraft / sage product photography.

### Surface & Borders
- **Page Surface** (`#ffffff`): Default panel background, matches canvas.
- **Espresso Surface** (`#333333`): Footer background and inverse hero blocks. Paper-white type sits on top.
- **Kraft Surface** (`#faf8f5`) /* estimated */: Alternate-section warm surface, used sparingly.

### Functional / State
- **Tw Ring Blue** (`rgba(59, 130, 246, 0.5)`): Default keyboard-focus ring, applied via Tailwind utility.
- **Focus Outline** (`#197cae`): Solid `2px` focus outline applied to primary buttons (extracted from button focus state).
- **Inline Link Blue** (`#006fff`): Editorial link colour, brand glyph fill.

### Shadow / Atmospheric
- **Carousel Lift** (`rgba(28, 29, 33, 0.12) 0px 0px 18px 0px, rgba(28, 29, 33, 0.06) 0px 6px 6px 0px`): The single decorative drop in the system, applied to white carousel arrows on photographic backdrops.
- **Soft Drop** (`rgba(0, 0, 0, 0.1) 0px 4px 6px -1px`): Tailwind default shadow, used rarely on featured-product callouts.
- **Sharp Drop** (`rgba(0, 0, 0, 0.2) 0px 4px 4px 0px`): Carousel hover-state shadow, slightly punchier on engagement.

### Gradient System
- Blue Bottle is **functionally gradient-free**. Surfaces are flat tinted paper. The closest the system gets to a gradient is the tonal range inside product photography (kraft sleeve to sage backdrop, espresso pour to porcelain cup) — never CSS gradients on UI surfaces.

## Typography

### Font Family
- **Display / Editorial**: `ABC Marfa Regular`, with fallback `ui-serif, Georgia, Cambria, Times New Roman, Times, serif`. A humanist serif from ABC Dinamo, used at uppercase display sizes for section openers and editorial heads. Carries the brand voice.
- **Primary UI / Body**: `ABC Diatype Regular`, with fallback `ui-sans-serif, system-ui, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji`. The neo-grotesk that handles every transactional surface.
- **OpenType Features**: Standard ligatures, lining numerals on prices and brew temperatures.

*Note: Both faces are commercially licensed from ABC Dinamo. For external implementations: **ABC Marfa** can be substituted with **PP Eiko**, **GT Alpina**, or **Söhne Schmal**; **ABC Diatype** can be substituted with **Inter**, **Söhne**, or **GT America**. Avoid Helvetica or Arial — they break the third-wave editorial register.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display / Hero Title | ABC Marfa Regular | 24px (1.50rem) | 400 | 1.33 | 1.6px | UPPERCASE — section openers, "Browse our coffees" |
| Display Light | ABC Marfa Regular | 24px (1.50rem) | 200 | 1.25 | 2.4px | UPPERCASE — alternate light-weight display variant |
| Section Subhead | ABC Marfa Regular | 16px (1.00rem) | 400 | 1.38 | 1.6px | UPPERCASE — section labels above body content |
| H1 (UI variant) | ABC Diatype Regular | 18px (1.13rem) | 400 | 1.33 | normal | Page-level H1 in transactional flows |
| Product Tile Title | ABC Diatype Regular | 16px (1.00rem) | 400 | 1.25 | 0.4px | Product card name, sentence case |
| Body | ABC Diatype Regular | 16px (1.00rem) | 400 | 1.50 | normal | Default reading copy |
| Body Tight | ABC Diatype Regular | 16px (1.00rem) | 400 | 1.38 | normal | Compact body, footer copy |
| Button Label | ABC Diatype Regular | 16px (1.00rem) | 400 | 1.50 | normal | Primary CTA labels — sentence case default |
| Button Caps | ABC Diatype Regular | 16px (1.00rem) | 400 | 1.00 | normal | UPPERCASE button variant — section CTAs |
| Caption / Byline | ABC Diatype Regular | 14px (0.88rem) | 400 | 1.43 | normal | Bylines, timestamps, meta-labels |
| Caption Caps | ABC Diatype Regular | 14px (0.88rem) | 400 | 1.43 | normal | UPPERCASE caption variant — eyebrows above body |

### Principles
- **Two-typeface contract**: ABC Marfa for editorial display caps only; ABC Diatype for everything that takes user input or sells a product. The serif sets tone, the grotesk sells.
- **Marfa always UPPERCASE with positive tracking**: Marfa never appears in mixed case. Always `text-transform: uppercase` with `1.6–2.4px` letter-spacing. This is the brand's typographic signature — single-origin signage register.
- **Sentence case Diatype everywhere**: Buttons, navigation, body copy, captions, and product names all use sentence case. UPPERCASE is reserved for Marfa display moments and rare eyebrow accents.
- **No bold weights**: The heaviest weight in use is 400 (regular). Marfa Light (200) appears as an alternate display variant. There is no 700 anywhere in the design system. Emphasis comes from typeface contrast (serif vs grotesk) and tracking (`1.6–2.4px` on caps), not weight escalation.
- **Body line-height generous**: Body Diatype runs at `1.50`, display Marfa caps run at `1.25–1.38` — the brand never crushes line-height for density.

## Layout

### Spacing System
- Base unit: 4px (with 8px and 16px as the rhythm increments)
- Scale: 4px, 8px, 12px, 16px, 20px, 24px, 32px, 36px, 48px, 64px, 80px, 96px, 128px /* estimated mid-range */
- Notable: Blue Bottle's grid uses generous magazine-pacing spacing — section padding lives at 64–128px on desktop and tightens to 32–64px on mobile. Padding `36px` on the primary button is unusually generous for an e-commerce CTA.

### Grid & Container
- Max content width: 1280–1440px /* estimated */ on product grids and editorial columns
- Hero: full-width with centred content stack — Marfa eyebrow caps, body Diatype paragraph, single CTA
- Section content: alternating between full-width imagery and centred 600–720px text columns
- Product grid: 3-up or 4-up desktop, 2-up tablet, 1-up mobile — 16–24px gutters
- Footer: dense link grid with bottle glyph left-aligned, social icons right-aligned

### Whitespace Philosophy
- **Editorial breathing**: Each section gets generous vertical padding — 64–128px between major content blocks. Blue Bottle pages feel like book chapters, not landing-page sections.
- **Centre-anchored composition**: Display content (Marfa caps, hero captions, key paragraphs) sits centred with symmetric whitespace.
- **Image isolation**: Product photography and editorial imagery sit with significant negative space surrounding them — kraft sleeves and sage cups breathe.
- **Quiet chrome**: Navigation, footer, and utility elements use no shadows and minimal borders — the system trusts whitespace over chrome.

### Border Radius Scale
- Sharp (`0`): Default for buttons, inputs, cards, modals — the workhorse radius and the brand's tactile signature
- Slight (`4px`): Reserved for one tokenised input field — the only mid-range radius in the system
- Pill (`50%`): Reserved for circular icon buttons, avatars, social mark dots
- No mid-range: Blue Bottle does not use 8–24px radii. The system reads either letterpress-sharp or fully circular.

## Elevation & Depth

| Level | Box Shadow | Use Case |
|-------|-----------|---------|
| Flat (Level 0) | `none` | Default state for nearly every surface — page canvas, cards, modals at rest |
| Soft Drop (Level 1) | `rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px` | Featured product callouts (rare) |
| Carousel Lift (Level 2) | `rgba(28, 29, 33, 0.12) 0px 0px 18px 0px, rgba(28, 29, 33, 0.06) 0px 6px 6px 0px` | Carousel arrows on photographic backdrops |
| Sharp Drop (Level 3) | `rgba(0, 0, 0, 0.2) 0px 4px 4px 0px` | Hover state on carousel arrows |
| Focus Outline (Level 4) | `outline: 2px solid #197cae` | Keyboard-focus on primary buttons |

**Shadow Philosophy**: Blue Bottle's elevation is editorial, not architectural. The default state of every surface is flat — there is no ambient elevation in the system. The two shadows that do exist live exclusively on white carousel-arrow chrome floating over photographic backdrops, where they're functional rather than decorative. The aesthetic is letterpress restraint: cards stay on the paper, buttons stay on the paper, the page IS the paper. Where competitor coffee retailers lean into soft elevation to imply premium, Blue Bottle achieves the opposite by refusing to lift anything off the page.

### Decorative Depth
- Carousel arrows do double duty as shadow holders — when they sit over photography, the soft drop helps them read against busy backdrops without breaking the flatness elsewhere on the page
- Hover states on buttons use background colour shifts (espresso flips to white, white fills to espresso) rather than shadow blooms
- No glows, no inner highlights, no neumorphic treatments

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

**Primary (Espresso)**
- Background: Espresso Ink (`#333333`)
- Text: Pure White (`#ffffff`)
- Padding: `12px 36px`
- Border: `0px solid #ffffff`
- Border-radius: `0px` — letterpress rectangle
- Box-shadow: `none`
- Font: 16px ABC Diatype Regular weight 400, sentence case default
- Hover: background stays `#333333`, optional underline appears on label
- Focus: outline `2px solid #197cae`
- Use: Primary CTAs — "Add to cart", "Continue", "Subscribe"

**Inverse (White on Photo)**
- Background: Pure White (`#ffffff`)
- Text: Pure Black (`#000000`)
- Padding: `12px 20px`
- Border: `0px solid #000000`
- Border-radius: `0px`
- Hover: background fills to Espresso (`#333333`), text inverts to white
- Focus: outline `2px solid #197cae`
- Use: Inverse CTAs sitting over photography or coloured surfaces

**Outline (Photo Carousel Arrow)**
- Background: Pure White (`#ffffff`)
- Color: Pure White (`#ffffff`) — icon-only, no text
- Border: `2px solid rgba(255, 255, 255, 0.5)`
- Border-radius: `0px`
- Box-shadow: `rgba(28, 29, 33, 0.12) 0px 0px 18px 0px, rgba(28, 29, 33, 0.06) 0px 6px 6px 0px`
- Hover: shadow deepens to `rgba(28, 29, 33, 0.2) 0px 0px 18px, rgba(28, 29, 33, 0.1) 0px 6px 6px`
- Use: Carousel navigation arrows on photographic carousels

**Ghost / Inline Link**
- Background: `transparent`
- Text: Espresso (`#333333`) or Blue Bottle Blue (`#006fff`) for editorial links
- Border-bottom: `1px solid currentColor` on hover
- Font: 14–16px ABC Diatype Regular weight 400
- Padding: 0 (inline)
- Use: Tertiary actions — "Learn more", inline editorial links

### Cards & Containers

**Product Card**
- Background: Pure White (`#ffffff`) on default sections; warm-cream (`#faf8f5`) /* estimated */ on alternate sections
- Border: `0` default — Blue Bottle trusts whitespace, not strokes
- Border-radius: `0px` — letterpress rectangle
- Box-shadow: `none` — cards are always flat
- Internal padding: 0 around image, 16–24px around text block, 12px between rows

**Editorial Block**
- Background: Pure White (`#ffffff`)
- Border: `0`
- Border-radius: `0`
- Padding: 64–96px section padding — magazine pacing
- Centred composition: Marfa eyebrow caps, body Diatype, single CTA

### Badges / Tags / Pills

**Eyebrow / Section Marker**
- Color: Espresso (`#333333`) or Warm Stone (`#6c6864`)
- Background: `transparent`
- Padding: 0 (inline)
- Font: 14px ABC Diatype Regular weight 400 UPPERCASE — no chip background, just typography
- Use: Section markers above body content

**Marfa Caps Caption**
- Color: Espresso (`#333333`)
- Background: `transparent`
- Padding: 0 (inline)
- Font: 16px ABC Marfa Regular weight 400 UPPERCASE with `1.6px` letter-spacing
- Use: Editorial section openers, product family labels

### Inputs & Forms
- Background: Pure White (`#ffffff`)
- Text colour: Espresso (`#333333`)
- Border: `1px solid` /* estimated `#e5e5e5` from system */
- Border-radius: `0` default; `4px` on the single input that uses CSS-tokened radius
- Font: 16px ABC Diatype Regular weight 400
- Padding: `12px 16px` /* estimated */
- Focus: outline `2px solid #197cae`, ring `rgba(59, 130, 246, 0.5)`
- Placeholder: /* estimated `#999999` */

### Navigation

**Top Nav Bar**
- Background: Pure White (`#ffffff`)
- Height: 64–80px
- Logo: Blue Bottle bottle glyph + wordmark, ~140–180px wide, left-aligned
- Categories: "Coffee · Equipment · Subscriptions · Gifts · Cafes · Stories" — 14px ABC Diatype Regular sentence case
- Right cluster: search icon, account icon, bag icon
- Hover: subtle underline appears below link text — no colour change
- Border-bottom: `0` or hairline `1px solid #e5e5e5` /* estimated */

### Decorative Elements

**Centred Composition**: hero blocks, section titles, and editorial paragraphs centred with text columns rarely exceeding ~640px — preserves reading rhythm and lets photography breathe.

**Wordmark Treatment**: Blue Bottle bottle glyph in solid Blue Bottle Blue (`#006fff`), set against pure white. The mark is the brand's only saturated chromatic moment in the chrome.

## Do's and Don'ts

### Do
- Use ABC Marfa (or substitute serif) only for editorial display caps with `1.6–2.4px` positive letter-spacing — never for body copy or UI
- Use ABC Diatype (or Inter / Söhne substitute) for everything transactional — buttons, body, captions, navigation
- Default to sentence case for every label, button, and navigation item — UPPERCASE reserved for Marfa display moments
- Use `#ffffff` (pure white) as the page canvas — never tinted, never warm-shifted
- Keep border-radius at `0` for buttons and inputs — letterpress rectangles
- Run body type at 16px Diatype regular with `1.50` line-height — magazine readability
- Reserve Blue Bottle Blue (`#006fff`) for the bottle glyph and select inline links — its rarity is its power
- Centre editorial composition by default — typography as still-life
- Use 64–128px section padding on desktop — book-chapter pacing
- Pair Marfa caps eyebrows above Diatype body for editorial pacing

### Don't
- Don't use bold weights — the design system caps at regular (400) with Marfa Light (200) as the alternate
- Don't apply UPPERCASE to UI text — sentence case is the Diatype contract
- Don't add drop shadows for elevation — flat is the default and the brand
- Don't use off-white (`#fffef2` / cream) for the page background — Blue Bottle commits to pure `#ffffff`
- Don't introduce gradients on surfaces or buttons — solid-tint only
- Don't enlarge Marfa caps above ~24px — the system stays restrained, never display-loud
- Don't crowd line-height below `1.50` for body — density without breath is the wrong kind of dense
- Don't use Blue Bottle Blue decoratively — every appearance must be functional
- Don't pair Marfa with a second serif — its singular role is non-negotiable
- Don't add rounded corners to buttons — sharp `0` radius is the brand's tactile signature

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, accordion footer, hamburger nav |
| Mobile | 375–767px | Single-column, primary nav still collapsed |
| Tablet | 768–1023px | 2-column grids begin, partial inline nav |
| Desktop | 1024–1279px | Full horizontal nav, multi-column product grids |
| Large | ≥1280px | Maximum container width, full editorial spacing |

### Touch Targets
- Primary buttons: min `44px` tap height via `12px 36px` padding × 2
- Nav links: `1rem` vertical padding for thumb-friendly tap zones in mobile drawer
- Form inputs: minimum `12px` vertical padding for tap-comfortable height
- Product tiles: entire card is tappable, not just the title

### Collapsing Strategy
- **Nav**: Horizontal row collapses to hamburger drawer; full-screen overlay on open with white background
- **Hero**: Centred composition stacks tighter on mobile; hero image scales but caption sequence stays the same
- **Footer**: column nav collapses to vertical accordion on mobile
- **Product grids**: 4-up desktop → 2-up mobile, gutters scale proportionally
- **Editorial text columns**: Max-width tightens on mobile; body remains 16px — Blue Bottle never bumps body size on small viewports
- **Section spacing**: 64–128px desktop reduces to 32–64px mobile while preserving editorial rhythm

### Image Behavior
- Product imagery maintains square or 5:4 aspect ratio across breakpoints
- Editorial photography uses padding-percent containers to lock aspect ratios
- Hero compositions reorder: Marfa caps eyebrow → headline → body → button stack stays vertical on every viewport
- The Blue Bottle glyph scales but never simplifies to a single bottle silhouette — always full mark

---

## Agent Prompt Guide

### Quick Reference
- Page Background: Pure White (`#ffffff`)
- Primary Text: Espresso Ink (`#333333`)
- Brand Glyph: Blue Bottle Blue (`#006fff`)
- Primary Button: `#333333` background, `#ffffff` text, `0px` radius
- Display Font: ABC Marfa Regular UPPERCASE with `1.6–2.4px` letter-spacing
- Body Font: ABC Diatype Regular 16px / `1.50` line-height
- Focus Outline: `2px solid #197cae`
- Section Padding: 64–128px desktop

### Example Component Prompts
- "Create a Blue Bottle hero on `#ffffff` with centred composition: 16px ABC Marfa Regular UPPERCASE eyebrow with `1.6px` letter-spacing in `#333`, 24px ABC Marfa Regular UPPERCASE headline with `1.6px` letter-spacing at line-height `1.33`, 16px ABC Diatype Regular body at line-height `1.50` in `#333`, and one primary button — `#333` bg, `#ffffff` text, `0px` radius, 16px ABC Diatype Regular weight 400, `12px 36px` padding."
- "Design a product tile on `#ffffff` with `0px` radius, no border, no shadow. Square product photograph at top against kraft-cream backdrop. Below: 14px ABC Diatype Regular UPPERCASE eyebrow ('SINGLE ORIGIN') in `#6c6864`, 16px ABC Diatype Regular weight 400 product name in `#333` (line-height `1.25`, `0.4px` letter-spacing), and a 14px ABC Diatype Regular price."
- "Create a primary CTA — `#333` background, `#ffffff` text, 16px ABC Diatype Regular weight 400, `12px 36px` padding, `0px` radius, sentence case ('Add to cart'). On hover, background stays `#333` with optional label underline. On focus, outline `2px solid #197cae`."
- "Design a section eyebrow — 16px ABC Marfa Regular UPPERCASE with `1.6px` letter-spacing in `#333`, sitting above a 24px ABC Marfa Regular UPPERCASE headline (also `1.6px` letter-spacing). Below: 16px ABC Diatype Regular body in `#333` at line-height `1.50`, max-width 640px, centred."
- "Create a carousel arrow — pure white background, `2px solid rgba(255, 255, 255, 0.5)` border, `0px` radius, icon-only. Apply `rgba(28, 29, 33, 0.12) 0px 0px 18px 0px, rgba(28, 29, 33, 0.06) 0px 6px 6px 0px` shadow so the white arrow reads against busy photographic backdrops."

### Iteration Guide
1. Default to two typefaces only: ABC Marfa for editorial UPPERCASE display, ABC Diatype for everything else. No exceptions.
2. Marfa is always UPPERCASE with `1.6–2.4px` positive letter-spacing. Mixed-case Marfa breaks the brand.
3. Diatype is always sentence case for body, navigation, buttons, and captions. UPPERCASE Diatype is reserved for rare eyebrow accents only.
4. Border-radius is binary: `0` for buttons / inputs / cards, `50%` for circular elements. No mid-range.
5. The page is pure white (`#ffffff`), committed. Espresso Ink (`#333`) is the primary text colour, softer than pure black.
6. Buttons are letterpress rectangles — `0px` radius, espresso bg, white text, `12px 36px` padding. Sharp.
7. Drop shadows do not exist in this system except the carousel-arrow exception. Use whitespace and typography for hierarchy.
8. Blue Bottle Blue (`#006fff`) is sacred — bottle glyph and select inline links only.
9. Centre editorial composition by default; left-align only when working inside dense product grids or forms.
10. Section padding stays generous (64–128px desktop) — pages should feel like book chapters, not stacked components.
