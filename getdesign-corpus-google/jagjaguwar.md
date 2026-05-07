---
version: alpha
name: "Jagjaguwar"
description: "Futura PT uppercase masthead over OCR-B monospace catalogue type, near-monochrome ink-on-cream, zero-radius rectangles."

colors:
  background: "#ffffff"
  surface: "#f5f5f5"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#666666"
  primary: "#231f20"
  on-primary: "#ffffff"
  border: "#d9d9d9"
  focus-ring: "#231f20"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "futura-pt, ui-sans-serif, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "futura-pt, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "futura-pt, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "futura-pt, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "futura-pt, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "futura-pt, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "futura-pt, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "futura-pt, ui-sans-serif, system-ui, sans-serif"
    fontSize: 13px
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

# Jagjaguwar Design System

## Overview

Jagjaguwar's website is the digital extension of an oatmeal-sleeve LP cover — a Bloomington, Indiana indie-folk label (Bon Iver, Sharon Van Etten, Angel Olsen) that has refused, for over thirty years, to dress like a tech company. The page sits on pure white (`#ffffff`) with deep ink-grey type (`#231f20`) and almost no other colour anywhere — 941 of the page's text instances run in this single warm near-black, 796 use pure black for hairline rules, and 553 use white. That's the entire palette. There is no brand red, no accent blue, no hero block. The chromatic richness lives entirely in the album artwork; the surrounding chrome stays as quiet as a record store wall painted matte off-white in 1994.

The defining typographic move is a two-face contract: **futura-pt** (uppercase, weight 700 for the masthead and weight 500 for navigation/links) does the announcement, and **ocr-b-std** (a 1965 ISO-standard machine-readable monospace) handles every catalogue entry, every track listing, every release-date eyebrow. Where every other indie label site has migrated toward a generic Helvetica or sans-grotesk, Jagjaguwar holds the line with two specific historical references: Paul Renner's geometric futura set in `2px` letter-spacing UPPERCASE for the wordmark and section openers, and OCR-B (designed by Adrian Frutiger for the European Computer Manufacturers Association) for the catalogue numbers, release notes, and tracklists. The pairing reads as a record label that has handed the design to an obsessive archivist rather than a brand agency.

What separates Jagjaguwar from every other indie label is the **commitment to letterpress austerity**. Buttons have `0px` radius (and there are barely any buttons — the catalogue is mostly text-and-image links). Borders are `1px solid #231f20` hairlines that run beneath every navigation link. Shadows do not exist anywhere in the system — the dembrandt extraction confirms zero shadow declarations. The page reads as a printed catalogue insert from a vinyl LP — type-only, hand-set, monochrome ink on uncoated cream. The label trusts the album covers (each LP sleeve carrying its own visual identity from its own designer or photographer) to carry every chromatic moment, and the chrome stays as out-of-the-way as humanly possible.

**Key Characteristics:**
- Pure white canvas (`#ffffff`) — uncoated paper, never warm cream
- Deep ink-grey body (`#231f20`) — softened from pure black, easier on long-form catalogue reading
- Two-face contract: `futura-pt` for masthead/nav, `ocr-b-std` for catalogue / track listings
- UPPERCASE futura-pt at weight 700 for the masthead, weight 500 for navigation links
- OCR-B monospace for catalogue meta — release dates, track numbers, "JAG" SKU codes
- `0px` border-radius across the entire system — letterpress-rectangular by conviction
- Zero drop shadows, zero gradients — the page is genuinely flat
- 1px solid hairlines (`#231f20`) under nav links and around editorial frames
- Album artwork is the only chromatic element — the chrome surrounds it, never competes
- 162px section spacing scale — generous magazine-spread breathing room

## Colors

### Primary
- **Jag Ink** (`#231f20`): The workhorse — used 941 times across the page. All body type, headings, navigation links, masthead, and primary borders. A warm near-black with a slight sepia undertone that reads as printed ink rather than digital text.
- **True Black** (`#000000`): Used 796 times for hairline rules and structural separators. Slightly cooler than Jag Ink — deployed where mechanical precision is needed (table rules, divider lines).
- **Pure White** (`#ffffff`): Page background, used 553 times. Crisp uncoated-paper white, never tinted warm. Also serves as the inverted text colour on the rare occasions ink panels invert.

### Brand Accent
- Jagjaguwar is **chromatically restrained to monochrome** in core brand chrome. The dembrandt extraction returned only `#231f20` as a confirmed palette colour with `medium` confidence on hover/focus states. There is no signature brand red, blue, or yellow in the chrome — the chromatic richness lives entirely in the album-cover thumbnails on the catalogue page.

### Hover / Focus
- **Hover Ink** (`#231f20` over `#ffffff` background swap): Links and nav items hover by inverting — the link background fills with ink and the text becomes white. No colour change.
- **Inverse Hover** (`#ffffff` text over `#231f20`): On dark sections (rare), hover lifts the text toward pure white from a slightly muted state.

### Neutrals & Text
- **Jag Ink** (`#231f20`): All primary text without exception.
- **Inverse Text** (`#ffffff`): Text colour on inverted nav drawers and tour-date hover states.

### Surface & Borders
- **Page Surface** (`#ffffff`): Default canvas — the only surface in active use.
- **Solid Hairline Border** (`1px solid #231f20`): The system's primary structural device — appears 82 times across `<a>` elements as bottom-border underlines for nav and catalogue links.
- **Vertical Rule** (`0px 115px 0px 0px solid #000000`): A right-side vertical divider used once on the primary `<nav>` element to separate the masthead from the catalogue grid.

### Shadow System
- **Zero shadows.** The dembrandt extraction returned an empty shadows array — Jagjaguwar declares no `box-shadow` anywhere on the page. Depth is communicated entirely through 1px hairlines and surface alternation between white and (rarely) ink panels.

### Gradient System
- Jagjaguwar is **gradient-free**. Every colour application is solid. The system's richness comes entirely from the album-cover photography that the chrome surrounds — never from layered colour transitions.

## Typography

### Font Family
- **Display / Masthead**: `futura-pt`, weight 500 / 700, sourced from Adobe Fonts (`adobeFonts: true`). Paul Renner's 1927 geometric grotesk, used UPPERCASE for the masthead and section openers. Carries the brand's modernist authority.
- **Catalogue / Body**: `ocr-b-std`, weight 400. Adrian Frutiger's 1965 machine-readable monospace designed for European optical character recognition. Used for every release listing, track number, tour-date entry, and meta line.
- **OpenType Features**: Standard ligatures only. No stylistic alternates, no opticals — the type's character carries the work.

*Note: futura-pt is a commercial typeface from URW (via Adobe Fonts subscription); ocr-b-std is a commercial typeface from URW. For external implementations, `Futura PT` substitutes are `Futura Std`, `Avenir Next`, or open-source `Hanken Grotesk` for futura; `OCR-B` substitutes are `IBM Plex Mono`, `Courier Prime`, or `JetBrains Mono` for the monospace catalogue role. The geometric-vs-monospace contrast must be preserved when substituting.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Display Hero / Masthead | futura-pt | 40px (2.50rem) | 700 | normal | normal | UPPERCASE | "JAGJAGUWAR" wordmark / hero header |
| Display Lite | futura-pt | 40px (2.50rem) | 500 | normal | normal | UPPERCASE | Section heads at masthead scale |
| Section Heading | futura-pt | 32px (2.00rem) | 700 | normal | normal | none | Sub-section titles |
| Display Sub | futura-pt | 18.72px (1.17rem) | 700 | normal | normal | UPPERCASE | "Releases", "Tour Dates" eyebrow heads |
| Primary Link / Nav | futura-pt | 20px (1.25rem) | 500 | normal | normal | none | Primary navigation, large links |
| Nav Link UPPER | futura-pt | 16px (1.00rem) | 500 | normal | normal | UPPERCASE | Top-level nav uppercase variant |
| Section Title (sentence) | futura-pt | 16px (1.00rem) | 500 | 1.50 | normal | UPPERCASE | Mid-page section headings with leading |
| Heading Bold | futura-pt | 16px (1.00rem) | 700 | normal | normal | UPPERCASE | Bold meta heads |
| Catalogue Body | ocr-b-std | 16px (1.00rem) | 400 | normal | normal | none | Standard catalogue / release body |
| Catalogue UPPER | ocr-b-std | 16px (1.00rem) | 400 | normal | normal | UPPERCASE | Track titles, release names |
| Catalogue Link | ocr-b-std | 16px (1.00rem) | 400 | normal | normal | UPPERCASE | Catalogue hyperlinks, "Listen" / "Buy" |
| Button Label | ocr-b-std | 16px (1.00rem) | 400 | normal | normal | UPPERCASE | Primary button labels |

### Principles
- **Two-face contract, three operative voices**: futura-pt 700 UPPERCASE for the masthead, futura-pt 500 for navigation, ocr-b-std for catalogue and meta. The roles do not trade.
- **UPPERCASE for futura-pt display**: The masthead and section headers run uppercase exclusively. The geometric letterforms read as architectural lettering, and the uppercase set carries the institutional voice.
- **Sentence case for catalogue body**: ocr-b-std runs in mixed-case for prose body, UPPERCASE for track titles and "Listen" / "Buy" links. The monospace's character lives in either case.
- **No bold weights below 700**: futura-pt at 500 (Medium) is the navigational weight; 700 (Bold) is reserved for the masthead and major section heads. There is no light or extra-bold anywhere.
- **No tracking adjustments**: Both faces use default letter-spacing — the typefaces' native spacing carries the work. No negative tracking on display, no wide tracking on UI.
- **One body weight**: ocr-b-std runs at weight 400 across every catalogue and meta context. The face's monospace rhythm is uniform.

## Layout

### Spacing System
- Base unit: `5–8px` for tight UI, with strong reliance on `10`, `18.72`, and `20`
- Scale: `5px, 8px, 10px, 15px, 16px, 18.72px, 20px, 21.6px, 30px, 54px, 57.6px, 81px, 162px, 216px, 460.8px`
- Notable: The `162px` value (41 instances) is the dominant section-spacing macro — it appears as the standard distance between major catalogue sections. The `18.72px` (42 uses) handles meta-row gutters. The unusual `5px` and `10px` densities at the small end suggest a 5px-rooted micro grid for tight catalogue chrome. `460.8px` is the editorial column width for press-release prose.

### Grid & Container
- Max content width: ~`1200px–1280px` for the catalogue grid
- Hero: full-bleed featured release block with carousel pagination
- Feature sections: 3-column or 4-column album-cover grids with consistent `162px` section-break spacing
- Press / editorial: single-column layout at ~460px reading column width
- Footer: 3-column nav with futura-pt UPPERCASE category headers and ocr-b-std link bodies

### Whitespace Philosophy
- **Magazine-spread breathing**: 162px between major sections is unusually generous for an e-commerce catalogue. Pages feel like printed liner notes, not dashboards.
- **Album-cover anchored**: The catalogue grid uses album artwork as the visual anchor and surrounds each tile with quiet whitespace. The chrome supports the artwork.
- **Centred composition for editorial**: Press-release prose and "About the Label" text run in narrow centred columns at ~460px max — magazine-style line measure for long-form reading.
- **No filler**: Empty rails are left empty. The grid does not invent content to balance itself.

### Border Radius Scale
- Sharp (`0px`): Default for every element across the entire system. Buttons, cards, inputs, image containers — all rectangular.
- The dembrandt extraction returned an empty `borderRadius.values` array — Jagjaguwar declares no rounded corners anywhere. The system is binary: rectangular only.
- Pill / Circle: Reserved exclusively for any social-icon avatars in the footer (third-party), not first-party brand chrome.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text, structural blocks |
| Hairline (Level 1) | `1px solid #231f20` | Link underlines, framed editorial blocks |
| Inverted Block (Level 2) | `#231f20` background panel | Nav hover state — links invert with white text on ink |
| Vertical Rule (Level 3) | `0px 115px 0px 0px solid #000000` | Masthead-to-catalogue separator (single-use structural rule) |

**Shadow Philosophy**: Jagjaguwar has no drop shadows. Anywhere. The dembrandt extraction confirms zero shadow declarations across the page — even modal overlays and floating elements (when they appear) avoid blur effects in favour of solid ink fills. Depth is communicated through three things: **hairline borders** (1px solid `#231f20`), **typography contrast** (futura-pt vs ocr-b-std as visual layering), and **album artwork density** (the cover photography carries all visual weight). The system is consciously print — paper has no shadow, only ink and the absence of ink. When an element needs to feel "interactive", it gets a hairline underline. When a section needs gravity, it inverts to ink. There is no ambient elevation, no atmospheric blur, no neumorphic surface anywhere in the system.

### Decorative Depth
- The album artwork itself provides all chromatic and visual depth — the surrounding chrome stays flat
- Hairline underlines do double duty as both rule and link affordance
- The futura-pt vs ocr-b-std contrast acts as typographic layering — the geometric face reads as "front", the monospace reads as "annotation"

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

**Primary Ink Block**
- Background: Jag Ink (`#231f20`)
- Text: `transparent` (default state — the button is a typographic mark)
- Padding: `10px 48px`
- Radius: `0px`
- Border: `0px none rgba(0, 0, 0, 0)` — borderless ink block
- Shadow: `none`
- Font: ocr-b-std at 16px weight 400, UPPERCASE
- Outline: `rgba(0, 0, 0, 0) none 3px` — focus reserved for tab navigation
- Hover: text remains transparent; opacity stays at 1
- Transform: `matrix(1, 0, 0, 1, 0, -240)` — used by the slick carousel for absolute positioning on hero rotation
- Use: Carousel navigation arrows, hero CTA blocks (the system uses few traditional buttons)

**Outlined Catalogue Link (de facto button)**
- Background: `transparent` or `#ffffff`
- Text: Jag Ink (`#231f20`)
- Padding: text-only — `0px`
- Radius: `0px`
- Border-bottom: `1px solid #231f20` — the underline IS the button affordance
- Font: futura-pt or ocr-b-std at 16–20px weight 400–500, often UPPERCASE
- Hover: link text inverts — background fills with ink, text becomes white
- Use: "BUY", "LISTEN", "MORE INFO" — the catalogue's primary affordance is the underlined uppercase link

### Cards & Containers

**Album Cover Tile**
- Background: `#ffffff`
- Border: `0px` default
- Radius: `0px`
- Shadow: `none`
- Internal padding: minimal — image fills the tile
- Below image: artist name in futura-pt UPPERCASE at 16px weight 700, album title in ocr-b-std at 16px weight 400, JAG catalogue number in ocr-b-std

**Editorial Block**
- Background: `#ffffff`
- Border: `1px solid #231f20` for occasional framed editorial moments
- Radius: `0px`
- Padding: 20–60px internal
- Use: Press-page features, "About the Label" prose

### Badges / Tags / Pills

**Catalogue Number Tag (typographic)**
- Background: `transparent`
- Text: Jag Ink (`#231f20`)
- Font: ocr-b-std at 16px weight 400 — "JAG345" style SKU
- No fill, no border — pure typographic marker
- Use: Release SKU codes, "JAG[number]" identifiers

**Genre / Format Mark**
- Background: `transparent`
- Text: Jag Ink (`#231f20`)
- Font: ocr-b-std at 16px weight 400, UPPERCASE
- No chip, no border — adjacent to the album title with a `·` separator
- Use: "LP / CD / DIGITAL", "FOLK / EXPERIMENTAL"

### Inputs & Forms

- The dembrandt extraction returned no input declarations from the catalogue page — Jagjaguwar's primary site is a browse-and-listen catalogue rather than a form-heavy storefront. When inputs do appear (newsletter signup in the footer), they should follow:
  - Background: `transparent`
  - Border: `0px 0px 1px solid #231f20` — bottom-border only, sketchbook-style
  - Radius: `0px`
  - Padding: `8px 0px`
  - Font: ocr-b-std at 16px weight 400
  - Focus: full `1px solid #231f20` border replaces underline; no glow

### Navigation

- Top masthead: white background, futura-pt UPPERCASE wordmark "JAGJAGUWAR" at 40px weight 700, centered or left-aligned
- Primary nav: futura-pt at 20px weight 500, sentence case for first-letter caps, link colour `#231f20`
- Top-utility links (smaller): futura-pt at 16px weight 500 UPPERCASE
- Hover: nav links display `1px solid #231f20` underline (82 instances detected in extraction); some links invert (text becomes white on ink hover)
- Vertical separator: `0px 115px 0px 0px solid #000000` right-edge rule on the masthead nav block
- Mobile: hamburger drawer with full-screen overlay on white, links stacked vertically

### Decorative Elements

**Hairline Underline System**
- `1px solid #231f20` appearing 82 times — the system's primary structural device
- Used as a bottom-border on every navigation link, catalogue link, and inline affordance
- Functions as both visual rule and affordance indicator — the underline IS the link's "button-ness"

**Letterpress-Style Typographic Marks**
- "JAG" catalogue numbers in ocr-b-std act as decorative typographic marks throughout the catalogue
- The monospace-vs-geometric contrast is the entire decorative system

**Album Artwork as Decoration**
- Each LP cover thumbnail is its own decorative element — designed by the artist or commissioned designer for that release
- The chrome stays mute so the artwork can carry the chromatic and visual richness

## Do's and Don'ts

### Do
- Use pure white (`#ffffff`) as the page canvas — uncoated paper, never warm cream
- Set all body and meta type in Jag Ink (`#231f20`) — softer than pure black, easier on long-form catalogue reading
- Pair futura-pt UPPERCASE (display / nav) with ocr-b-std monospace (catalogue / meta) — every screen should show this contrast
- Use futura-pt at weight 700 for the masthead, weight 500 for navigation
- Use ocr-b-std at weight 400 for every catalogue entry, track title, release date, and "JAG" SKU number
- Set link affordances with a `1px solid #231f20` bottom-border — the underline is the button
- Keep border-radius at `0px` for every element — the system is rectangular by conviction
- Use hover-by-inversion: nav links fill with ink and text becomes white on hover
- Reserve all chromatic richness for album-cover artwork — let the LP sleeves carry every colour moment
- Use `162px` section spacing for major catalogue breaks — generous magazine-spread breathing
- Run editorial / press prose in narrow ~460px columns for magazine-style line measure

### Don't
- Don't introduce a brand accent colour — the system is genuinely monochrome and the album artwork carries the colour
- Don't use pure black (`#000000`) for body type — Jag Ink (`#231f20`) is warmer and reads as ink rather than digital text
- Don't add drop shadows anywhere — the system is consciously flat
- Don't introduce gradients on surfaces or buttons — solid ink fills only
- Don't use rounded corners on any element — `0px` radius is the brand's tactile signature
- Don't replace ocr-b-std with a generic monospace like Courier — the OCR-B character set is the catalogue voice
- Don't replace futura-pt with a humanist sans like Inter — the geometric grotesk is the institutional voice
- Don't pair futura-pt with another sans — its singular display role is non-negotiable
- Don't crowd line-height on display text — let futura-pt's natural metrics carry the masthead
- Don't lowercase the masthead — futura-pt UPPERCASE at weight 700 is the wordmark's only legal setting
- Don't add chips, fills, or borders to catalogue tags — typographic-only marks separated by `·`
- Don't use a warm off-white canvas — pure white preserves the printed-catalogue feel

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <600px | Single-column catalogue grid, hamburger nav, masthead scales to ~24–32px |
| Tablet | 600–1024px | 2-column album grid, primary nav still collapsed |
| Desktop | ≥1024px | Full horizontal nav, 3 or 4-column album grid, full editorial spacing |

### Touch Targets
- Catalogue links: 16px ocr-b-std with `8–10px` vertical padding produces ~32–40px tap height — at the smaller end of comfortable, acceptable for catalogue browsing
- Nav links: 20px futura-pt with hairline underline produces ~28–36px tap zones — extended on mobile via padding for thumb-friendly drawer
- Album-cover tiles: entire tile is tappable, including the meta below

### Collapsing Strategy
- **Nav**: Horizontal nav row collapses to hamburger drawer below 600px; full-screen white overlay on open with stacked futura-pt UPPERCASE links
- **Masthead**: Centred / left-aligned wordmark scales from 40px → 32px → 24px progressively
- **Catalogue grid**: 4-up desktop → 3-up tablet → 2-up mobile, gutters stay proportionally generous
- **Editorial columns**: 460px reading column tightens on mobile but ocr-b-std body stays at 16px — the catalogue never bumps body size for small viewports
- **Section spacing**: 162px desktop → 80px tablet → 40px mobile — compresses but preserves magazine rhythm

### Image Behavior
- Album artwork maintains its native aspect ratio (typically square for vinyl LPs, occasionally 12x12 / 7x7 for singles)
- No art-direction shifts between breakpoints — same composition adapts proportionally
- Artwork is never cropped, never overlaid with text, never given a tint — the cover is sacrosanct

---

## Agent Prompt Guide

### Quick Color Reference
- Page Background: Pure White (`#ffffff`)
- Primary Text / Borders: Jag Ink (`#231f20`)
- Mechanical Hairlines: True Black (`#000000`)
- Inverse Text: Pure White (`#ffffff`)
- No accent colours — the system is mono

### Quick Type Reference
- Masthead: futura-pt 40px / weight 700 / UPPERCASE / `#231f20`
- Nav primary: futura-pt 20px / weight 500 / `#231f20`
- Nav UPPER: futura-pt 16px / weight 500 / UPPERCASE
- Catalogue body / track titles: ocr-b-std 16px / weight 400 / often UPPERCASE
- Section heading: futura-pt 32px / weight 700

### Example Component Prompts
- "Create a Jagjaguwar-style masthead on `#ffffff` with the wordmark in futura-pt 40px weight 700 UPPERCASE, color `#231f20`. Below: horizontal nav in futura-pt 20px weight 500 with `#231f20` color and `1px solid #231f20` bottom-border on hover. Right-aligned utility links in futura-pt 16px weight 500 UPPERCASE."
- "Build a catalogue tile: album cover image at top with no border, no radius, no shadow. Below: artist name in futura-pt 16px weight 700 UPPERCASE, album title in ocr-b-std 16px weight 400 UPPERCASE, JAG catalogue number in ocr-b-std 16px weight 400, format/genre tags in ocr-b-std 16px weight 400 UPPERCASE separated by `·`. Color throughout: `#231f20`. No card border."
- "Design a 'Listen / Buy' link affordance: text in ocr-b-std 16px weight 400 UPPERCASE, color `#231f20`, with `1px solid #231f20` bottom-border. On hover, fill background with `#231f20` and invert text to `#ffffff`. Padding: 4px 0px."
- "Create a press-release editorial layout: ~460px centered column on `#ffffff`. Section title in futura-pt 32px weight 700 UPPERCASE, color `#231f20`. Body in ocr-b-std 16px weight 400, line-height 1.50. Inline links: futura-pt 16px weight 500 with `1px solid #231f20` underline."
- "Build a tour-date listing: ocr-b-std 16px weight 400 UPPERCASE in `#231f20` with date · venue · city · ticket-link layout, separated by `·`. Each row separated by a `162px` vertical gap on desktop, `40px` on mobile. Ticket link gets `1px solid #231f20` bottom-border."

### Iteration Guide
1. Default to pure white (`#ffffff`) canvas and Jag Ink (`#231f20`) text — never deviate to cream or pure black
2. Pair futura-pt UPPERCASE (display) with ocr-b-std monospace (catalogue) on every screen — this is the brand
3. futura-pt at weight 700 is the masthead; weight 500 is the nav. Reserve 700 for the wordmark and major section heads.
4. ocr-b-std runs at weight 400 universally — track titles, release dates, JAG numbers, prose body
5. UPPERCASE is the default for futura-pt display and ocr-b-std catalogue links — sentence case only for prose body
6. Border-radius is `0px` everywhere. The system is rectangular by conviction.
7. Use `1px solid #231f20` bottom-border as the link affordance — the underline IS the "button"
8. Hover by inversion: link backgrounds fill with `#231f20` and text becomes `#ffffff`
9. No shadows. No gradients. No accent colours. The album artwork carries everything chromatic.
10. Use `162px` section spacing for major catalogue breaks; `460px` reading column for editorial prose
