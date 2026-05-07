---
version: alpha
name: "BlackRock"
description: "Fort serif system at three weights, ink-black on white with a single ember-orange CTA accent, sharp 0px corners and 4px below-nav rule."

colors:
  background: "#ffffff"
  surface: "#005eb8"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#616161"
  primary: "#ff4713"
  on-primary: "#ffffff"
  border: "#3860be"
  focus-ring: "#ff4713"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "FortExtraBold, ui-sans-serif, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "FortExtraBold, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "FortExtraBold, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "FortExtraBold, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "FortExtraBold, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "FortExtraBold, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "FortExtraBold, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "FortExtraBold, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
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

# BlackRock Design System

## Overview

BlackRock's website is what an asset-management firm worth more than the GDP of most nations chooses to look like, and the answer is "less than you would expect." The page sits on pure white (`#ffffff`) with deep ink-black headlines (`#000000`) — 706 instances of pure black across the page versus 638 of pure white — and a single ember-orange accent (`#ff4713`) that lives on column-header strokes and feature-link arrows. Where Goldman Sachs reaches for navy and Schwab reaches for institutional blue, BlackRock has chosen the most editorial palette in finance: black ink on white sheet with a precise hand-drawn orange. The composition reads less like a corporate site and more like an institutional letter — the asset manager's equivalent of a Federal Reserve press release.

The defining typographic move is the **three-weight Fort serif system**. `FortExtraBold` carries the largest display moments (hero heads at 56px / 40px / 24px), `FortBold` handles tertiary headings and primary buttons (32px / 20px / 16px), and `FortBook` (the regular weight) carries every body line, every link, and every long-form paragraph. The serif itself is custom — a contemporary transitional with crisp ascenders and a tight x-height — and it does almost all the talking. Where most financial sites use a sans for chrome and a serif for headlines, BlackRock pushes the serif into the body and the buttons too, falling back to Arial only for utility metadata and disclaimer text. The result is a page that reads like a print annual report: dense, authoritative, and unwilling to chase contemporary fintech aesthetics.

What separates BlackRock from every other heritage asset manager is the **commitment to editorial sharpness**. Buttons have `0px` border-radius (the entire system caps at 2–4px for legal/cookie chrome). The single below-the-nav rule is a `4px solid #000` horizontal band that announces "this is a structural break, not decoration." The `1px hairline` border colour for cards is also pure black — not a softened grey, not a hairline neutral, but full ink. Shadows are conservative single-layer drops (`rgba(112, 112, 112, 0.5) 0px 0px 12px 0px` for elevated content). Where modern fintech has migrated toward soft elevation and rounded corners, BlackRock holds the print-document line: ink, paper, and the absence of decoration.

**Key Characteristics:**
- Three-weight Fort serif system: FortExtraBold (display), FortBold (headings/buttons), FortBook (body)
- Pure white canvas (`#ffffff`) — institutional sheet white, never cream
- Pure black headlines (`#000000`) — ink, not softened off-black
- Single chromatic accent: ember orange (`#ff4713`) used 38 times across column-header strokes and feature-link arrows
- Editorial-blue link colour (`#005eb8`) for off-site references and cross-document hyperlinks
- `0px` border-radius on primary buttons, with `2px` reserved for "Keep exploring" / "Close" mid-tier CTAs
- 1px solid black borders (12 confirmed instances) — full ink hairlines, never softened grey
- 4px solid black below-nav rule — the system's single bold structural device
- Serif buttons (`FortBold` 16px weight 800) — financial-document authority on every CTA
- Conservative shadow scale: ambient 12px-blur drops only, never tinted
- 8px workhorse spacing (283 uses) with 4px / 6px sub-grid for tight chrome

## Colors

### Primary
- **Ink Black** (`#000000`): All headlines, body type, primary borders, button backgrounds. Pure black — the institution refuses to soften the ink. Used 706 times across the page.
- **Sheet White** (`#ffffff`): Page background, button text on dark CTAs, inverse text. Crisp institutional white. Used 638 times.

### Brand Accent
- **Ember Orange** (`#ff4713`): The single chromatic note in the system — confirmed at high confidence in the column-header context with 38 instances. Used for column-header strokes, feature-link arrows ("Keep exploring →"), and editorial accent moments. Reads as an institutional highlighter — used so rarely that it functions as a wax-seal punctuation. The brand's chromatic identity lives almost entirely in this one orange.

### Editorial Link
- **Document Blue** (`#005eb8`): The system's hyperlink colour for off-site references, document downloads, and cross-publication links. 40 instances confirmed. Reads as a Bloomberg / Federal-Reserve-style editorial blue — never decorative, always functional.
- **Hover Blue** (`#3860be`): Hover-state shift for blue links — a softer indigo step.

### Neutrals & Text
- **Ink Black** (`#000000`): All primary headlines and body text without exception.
- **Slate Caption** (`#616161`): Secondary metadata, footer attribution, fine-print captions.
- **Disclosure Grey** (`#c1c6c8`): Top-rule borders on `<main>` content separators.
- **Disabled / Hairline** (`#979797`): Form input hairline borders, divider strokes.
- **Border Light** (`#d8d8d8`): Cookie-banner and overlay element borders (third-party origin).
- **Border Pale** (`#bbbbbb`): Tertiary button outline colour for the lightest hierarchy.

### Surface & Borders
- **Page Surface** (`#ffffff`): Default canvas — always.
- **Solid Hairline** (`1px solid #000`): The primary structural border colour — appears 12 times across `<button>` elements and 11 times across `<div>` / `<li>` elements as bottom-only rules. BlackRock prefers full ink over softened greys.
- **Bottom Rule** (`0px 0px 1px solid #000`): Bottom-border-only treatment used on list items and section dividers.
- **Left Rule** (`0px 0px 0px 1px solid #000`): Left-border-only treatment used on quote panels and editorial pull-outs.
- **Compound Frame** (`0px 1px 1px solid #000`): Three-sided border (right, bottom, left) for editorial card moments.
- **Heavy Bottom Rule** (`0px 0px 4px solid #000`): The signature structural separator — appears below the primary navigation. Five confirmed uses across `<nav>` / `<ul>` elements.
- **Inverse White Border** (`1px solid #ffffff`): Used on dark hero panels for outlined buttons against `#161616` surfaces.

### Shadow Colors
- **Card Drop** (`rgba(112, 112, 112, 0.5) 0px 0px 12px 0px`): The most-used shadow (12 instances) — a soft mid-grey ambient drop with 12px blur and zero offset. Used on elevated cards and CTA-hover states.
- **Soft Drop** (`rgba(12, 13, 14, 0.2) 0px 2px 2px 0px`): Compact shadow for tight chrome elevation.
- **Wide Drop** (`rgba(0, 0, 0, 0.2) 0px 0px 18px 0px`): Modal-overlay-grade ambient shadow.
- **Direction Drop** (`rgb(153, 153, 153) 0px 2px 10px -3px`): Standard card-hover shadow with slight downward offset.

### Gradient System
- BlackRock is **gradient-free in core brand chrome**. Surface colour is solid white, solid black, or solid orange — never blended. The only gradients that ship are standard scrim treatments over hero photography (`transparent → #000000`) to anchor white text on full-bleed imagery — never on buttons, cards, or structural surfaces.

## Typography

### Font Family
- **Display Heavy**: `FortExtraBold`, weight 400 (the fontface itself carries the heaviness), fallback `Arial`. The hero-and-section-front display weight — sets every page-front headline and primary section opener.
- **Display / Heading Bold**: `FortBold`, weight 400–800, fallback `Arial`. Tertiary headings, primary button labels, and emphasis in body. Where `FortExtraBold` reads as page-front, `FortBold` reads as in-document chapter mark.
- **Body / Reading**: `FortBook`, weight 400, fallback `Arial`. The reading face — carries every paragraph, every long-form description, every form-field label.
- **Utility / Disclaimer**: `Arial`, weights 400/600/700, fallback `Helvetica`. The fall-through face for cookie-banner copy, legal disclaimer text, third-party widget chrome.
- **Iconography**: `Font Awesome 5 Pro` and `Font Awesome 5 Brands` — the inline icon system at weights 400/900.
- **OpenType Features**: Standard ligatures only. No stylistic alternates, no opticals — the type's institutional gravity is in the default character set.

*Note: Fort is a custom commercial typeface from Sharp Type Co commissioned for BlackRock — there is no public fallback that captures the exact letterforms. For external implementations, `Lyon Display` or `Untitled Serif` from Klim approximates the editorial weight; `Crimson Pro` or `Source Serif 4` works as a free substitute. Arial fallback is acceptable for utility chrome.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | FortExtraBold | 56px (3.50rem) | 400 | 1.14 | normal | Page-front hero headline — homepage / section opener |
| Display Large | FortExtraBold | 40px (2.50rem) | 400 | 1.20 | normal | Section heroes, page introductions |
| Section Heading | FortBold | 32px (2.00rem) | 700 | 1.00 | normal | Major in-page section heads |
| Sub-Heading Heavy | FortExtraBold | 24px (1.50rem) | 400 | 1.33 | normal | Tertiary headings, callout heads |
| Sub-Heading Bold | FortBold | 24px (1.50rem) | 400 | 1.50 | normal | Card titles, secondary heads |
| Editorial Lead | FortBook | 24px (1.50rem) | 400 | 1.33 | 1px | Editorial intro paragraphs with `1px` letter-spacing |
| Standard Heading | FortExtraBold | 20px (1.25rem) | 700 | 1.40 | normal | Card heads, secondary headings |
| Standard Heading Body | FortBook | 20px (1.25rem) | 400 | 1.50 | normal | Sub-headings in body context |
| Link Bold | FortBold | 20px (1.25rem) | 400 | 1.20 | normal | Featured editorial links |
| Sub-Heading Small | FortExtraBold | 18px (1.13rem) | 400 | 1.33 | normal | Compact section heads |
| Body | FortBook | 16px (1.00rem) | 400 | 1.50 | normal | Standard reading text |
| Body Bold | FortBold | 16px (1.00rem) | 400 | 1.50 | normal | Emphasized body, list items |
| Editorial Heading | FortExtraBold | 16px (1.00rem) | 400 | 1.38 | normal | Inline editorial heads |
| Button Heavy | FortBold | 16px (1.00rem) | 800 | 1.50 | normal | Primary CTA button label — serif at extra-bold |
| Caption | FortBook | 14px (0.88rem) | 400 | 1.00–1.50 | normal | Image captions, metadata |
| Tabular Caption | Arial | 14.4px | 400 | 2.64 | 0.144px | Tabular financial data with explicit tracking |
| Footer / Disclosure | FortBook | 12px (0.75rem) | 400 | 1.67 | normal | Fine print, legal disclosure |
| Footer Eyebrow | FortExtraBold | 12px (0.75rem) | 400 | 1.67 | normal | UPPERCASE footer category labels |

### Principles
- **Three Fort weights, no italic, no bold sans**: FortExtraBold for display, FortBold for headings and buttons, FortBook for body. The system rotates between these three weights and never reaches for a sans-serif on primary chrome.
- **Buttons are serifs**: Primary CTAs use FortBold at weight 800 — financial-document authority on every "Keep exploring", "Subscribe", "Download". Where modern fintech uses a clean sans for buttons, BlackRock makes the button itself a piece of editorial typography.
- **Pure black headlines**: No softening to `#222` or `#161616` for headings. The institution publishes in ink.
- **Tight display line-height**: FortExtraBold at 56px runs `1.14`, at 40px runs `1.20` — institutional-tight, not airy. Headlines are dense graphic blocks, not paragraphs.
- **Generous body line-height**: FortBook body at 16px runs `1.50` — long-form reading comfort, the inverse of display tightness.
- **Tabular data uses Arial**: Charts, fund-data tables, and tabular financial displays drop to Arial at 14.4px / `0.144px` letter-spacing — the editorial Fort gives way to the workhorse sans for numerical density.
- **No tracking on Fort**: The Fort family runs at default letter-spacing across nearly every role. The exception is `1px` tracking on 24px FortBook editorial leads.

## Layout

### Spacing System
- Base unit: `8px` (with `4px` and `6px` sub-grid for tight chrome)
- Scale: `1px, 2px, 4px, 6px, 8px, 12px, 16px, 24px, 32px, 40px, 80px, 96px, 128px`
- Notable: `8px` is the dominant value (283 instances) — the system's true workhorse. `6px` (133), `16px` (102), and `4px` (100) carry the secondary load. `40px` (33), `32px` (26), `24px` (44) handle component-internal spacing. `96px` (11) and `128px` (7) are the section-level macro values. The scale is dense at the small end (every 2px from 4–12) reflecting the institution's precision-oriented financial UI.

### Grid & Container
- Max content width: ~`1200px–1440px` for editorial / homepage; `720px` for long-form article reading column
- Hero: full-bleed photography or full-bleed `#161616` cinematic block with FortExtraBold headline overlay
- Section content: 3-column or 4-column card grids on desktop with hairline separators
- Article reading column: ~`640–720px` max — narrow, magazine-style for long-form comfort
- Frequent dark `#161616` panels for cinematic features alternating with white reading sections

### Whitespace Philosophy
- **Editorial pacing**: Each major section gets 96–128px of vertical air. The page reads as a print research note, not a stacked landing page.
- **Reading column air**: FortBook body at 16px / 1.50 line-height with 16–24px paragraph spacing — denser than blog convention, looser than print. Tuned for screens read like documents.
- **Hero breathing room**: FortExtraBold headlines at 56px get 48–64px of air above and 32px below. The masthead always gets its own band.
- **No filler**: Empty rails are left empty. The grid does not invent content to balance itself.

### Border Radius Scale
- Sharp (`0px`): Default for primary buttons, cards, inputs, image containers — the institutional rectangle
- Slight (`1px`, `2px`): Reserved for "Keep exploring" / "Close" mid-tier CTAs and cookie-banner chrome (third-party origin); `2px` appears 18 times, the most-used non-zero radius
- Mini-rounded (`3px`, `4px`): One-off micro-radius on pop-up dialog buttons (low confidence)
- Slight Plus (`17px–32px`): Filter Cookie List, search-pill chrome (third-party origin) — never first-party brand
- Pill (`50px`, `46px`): Cookie-banner search and close pills (third-party)
- Circular (`50%`): Search and close icon circles (third-party origin)

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text, standard surfaces |
| Hairline (Level 1) | `1px solid #000` | Card edges, dividers, button outlines |
| Heavy Rule (Level 2) | `4px solid #000` | Below-nav structural separator (single use) |
| Compound Border (Level 3) | `0px 1px 1px solid #000` | Editorial pull-out cards with three-sided frame |
| Inverted Block (Level 4) | `#161616` background panel | Cinematic features — depth via tonal shift |
| Card Drop (Level 5) | `rgba(112, 112, 112, 0.5) 0px 0px 12px 0px` | Hover state on primary CTAs and elevated cards |
| Modal Drop (Level 6) | `rgba(0, 0, 0, 0.2) 0px 0px 18px 0px` | Modal overlay elevation |
| Focus Ring | `box-shadow: rgb(0, 0, 0) 0px 0px 0px 2px inset` + `outline: 1px solid #000` | Keyboard focus on inputs and CTAs |

**Shadow Philosophy**: BlackRock's shadow system is consciously editorial. The default state of every surface is flat — the page reads as a print document, not a UI. Where elevation needs to communicate, the system uses 1px hairlines, 4px heavy rules, or `#161616` tonal blocks rather than blurred ambient shadows. The single soft shadow that does appear (`rgba(112, 112, 112, 0.5) 0px 0px 12px 0px`) is reserved for primary CTA hover states and a small set of elevated cards — and even then it has zero offset, reading as ambient illumination rather than directional lift. Where Stripe leans into multi-layer blue-tinted shadows for premium gravity, BlackRock holds the print line: ink, paper, and the absence of decoration.

### Decorative Depth
- The `#161616` dark hero block is the system's only true "elevation" — it functions as a chapter shift via tonal contrast
- 1px solid black hairlines do double duty as both rules and structural elevation
- The 4px below-nav rule is the system's signature structural device, communicating "navigation ends here" without any other treatment
- Ember Orange appears as a 1–2px column stroke — chromatic accent acting as decorative depth

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

**Primary Ink CTA**
- Background: Ink Black (`#000000`)
- Text: Sheet White (`#ffffff`)
- Padding: `12px 24px`
- Radius: `0px`
- Border: `1px solid #000`
- Shadow: `none` at rest
- Font: 16px FortBold weight 800
- Hover: background goes white, text shifts to Document Blue (`#2285f7`), border softens to `#e7e9ec`, shadow appears (`rgba(112, 112, 112, 0.5) 0px 0px 12px 0px`), opacity drops to `0.6`, transform `translateY(-20%)` lifts the button
- Active: background `#2c6415` (deep institutional green for pressed state), border softens further
- Focus: background goes turquoise (`#1eaedb`), `box-shadow: rgb(0, 0, 0) 0px 0px 0px 2px inset` provides inset focus ring
- Use: Primary CTA — "Keep exploring", "Subscribe", "Download Prospectus"

**Outlined Inverse (on dark hero)**
- Background: `#161616` (slightly warmer than pure black for hero panel surfaces)
- Text: Sheet White (`#ffffff`)
- Padding: `12px 24px`
- Radius: `2px`
- Border: `1px solid #ffffff`
- Font: 16px FortBold weight 400
- Hover: background goes turquoise (`#1eaedb`), border `1px solid #003eff`
- Use: CTAs on `#161616` cinematic hero panels

**Tertiary "Close" / Compact**
- Background: Ink Black (`#000000`)
- Text: Sheet White (`#ffffff`)
- Padding: `8px 11px`
- Radius: `0px`
- Border: `0px none` — borderless ink block
- Font: 20px FontAwesome at weight 900 (icon-only)
- Hover: background goes turquoise (`#1eaedb`), border `1px solid #003eff`, ambient shadow appears
- Use: Modal close, toolbar utility actions

**Inverse White-Field**
- Background: Sheet White (`#ffffff`)
- Text: Ink Black (`#000000`)
- Padding: `0px`
- Radius: `0px`
- Border: `0px none`
- Font: 13.33px FortBook weight 400
- Hover: same turquoise treatment as primary
- Use: Compact in-card text actions

### Cards & Containers

**Article Card**
- Background: Sheet White (`#ffffff`)
- Border: `1px solid #000` for outlined editorial moments, often only top/bottom (`1px 0 0 0`) for feed-style separation
- Radius: `0px`
- Shadow: `none` at rest
- Padding: `24px–40px` internal — generous editorial padding
- Internal: image (full-width or 4:3), FortExtraBold headline, FortBook dek, "Keep exploring →" link in FortBold

**Compound-Border Editorial Card**
- Background: Sheet White (`#ffffff`)
- Border: `0px 1px 1px solid #000` — three-sided frame (right, bottom, left)
- Radius: `0px`
- Padding: `32px`
- Use: Long-form editorial pull-outs, opinion-piece panels

**Dark Hero Panel**
- Background: `#161616`
- Text: `#ffffff` headline (FortExtraBold), `#e5e5e5` body (FortBook)
- Radius: `0px`
- Padding: `64px 48px`
- Border: none
- Use: Cinematic feature heroes — quarterly outlook, market commentary

### Badges / Tags / Pills

**Status Indicator**
- Background: `transparent`
- Text: Document Blue (`#005eb8`) for informational, `#000` for neutral
- Padding: `0px`
- Font: 12–14px FortExtraBold UPPERCASE
- Use: "MARKET COMMENTARY", "OUTLOOK 2026" — typographic-only category markers

**Compact Pill (rare, third-party)**
- Background: Sheet White (`#ffffff`)
- Border: `1px solid #000`
- Padding: `4px 12px`
- Radius: `2px`
- Font: 12px FortBook weight 400
- Use: Filter chips, category tags on fund-explorer pages

### Inputs & Forms

**Search / Standard Input**
- Background: Sheet White (`#ffffff`)
- Border: `0px` default — input sits inside a parent container with `1px solid #000` carrying the visible border
- Radius: `0px`
- Padding: `0px`
- Font: FortBook 16px weight 400, color `#000`
- Focus: parent shifts to `1px solid #000`, `box-shadow: rgb(0, 0, 0) 0px 0px 0px 2px inset` adds inset focus ring, `outline: 1px solid #000`
- Use: Search input, fund lookup, newsletter email

**Email Newsletter (with parent border)**
- Parent container: `1px solid #000`, `0px` radius
- Input inside: transparent, no own border
- Submit button flush-attached, no gap

### Navigation

- Top utility strip: white background, FortExtraBold UPPERCASE category links at 12px, footer-style category headers
- Primary nav: white background with the BlackRock wordmark (152x22 SVG) anchored top-left, never resized below 22px height
- Primary nav links: 14px FortBook weight 700, color `#000`, with `4px solid #000` heavy bottom-rule separating the nav from the page content
- Hover: color shifts to Document Blue (`#005eb8`), no underline change
- Sticky behaviour: full nav stack remains fixed on scroll
- Mobile: hamburger reveals full-screen white overlay with stacked FortExtraBold UPPERCASE category names

### Decorative Elements

**Heavy Black Below-Nav Rule**
- `0px 0px 4px solid #000` — the system's single bold structural device
- Appears beneath the primary navigation, separating chrome from content
- Five confirmed uses across `<nav>` / `<ul>` elements

**1px Black Editorial Hairlines**
- `1px solid #000` borders carry all card and divider structure
- 12 confirmed instances on `<button>` elements, 11 on `<div>` / `<li>` for bottom-rules
- Pure ink, not softened grey — the institution prefers full hairlines

**Ember Orange Column Strokes**
- Ember Orange (`#ff4713`) appears on column-header strokes and feature-link arrows
- Acts as an editorial highlighter — used so rarely it reads as institutional emphasis
- 38 confirmed uses, all in column-header context

**Document Blue Hyperlinks**
- Document Blue (`#005eb8`) for off-site links and cross-document references
- 40 confirmed instances — the system's only chromatic accent in body type
- Inline hyperlinks underlined by default, hover removes underline and shifts to `#3860be`

## Do's and Don'ts

### Do
- Use FortExtraBold for hero display, FortBold for headings and buttons, FortBook for body — the three-weight serif system is the institution's voice
- Set primary buttons in FortBold weight 800 — serif buttons are the brand's signature
- Use pure black (`#000000`) for headlines and body — no softened off-blacks
- Use pure white (`#ffffff`) as the canvas — institutional sheet white, never cream
- Reserve Ember Orange (`#ff4713`) for column-header strokes and feature-link arrows — its rarity is its institutional weight
- Use Document Blue (`#005eb8`) for hyperlinks and cross-document references — the editorial blue of financial publishing
- Use 1px solid black borders (`1px solid #000`) for primary card edges — full ink, never softened grey
- Apply the 4px solid black below-nav rule as the system's single bold structural separator
- Keep border-radius at `0px` for primary buttons and cards — the institutional rectangle
- Set body line-height to `1.50` for long-form reading comfort against tight `1.14–1.20` display
- Drop to Arial at 14.4px / `0.144px` tracking for tabular financial data — the workhorse for numerical density
- Use the dark `#161616` panel for cinematic features — the system's chapter break

### Don't
- Don't use a sans-serif on primary headlines or buttons — Fort serif is non-negotiable
- Don't use bold body Fort for emphasis — keep body at FortBook weight 400
- Don't introduce drop shadows on primary chrome — flat is the institutional default
- Don't soften pure black to off-black — the institution publishes in ink
- Don't introduce a second saturated colour to compete with Ember Orange — the single accent is the point
- Don't use pill-shaped buttons or rounded cards — `0px` radius is the brand's tactile signature (mid-tier CTAs at 2px are the only exception)
- Don't crowd display line-height below `1.10` or stretch body line-height above `1.55`
- Don't use Document Blue (`#005eb8`) on body type — only inline hyperlinks
- Don't introduce gradient fills on cards or buttons — solid ink, solid orange, solid white only
- Don't replace the 4px below-nav rule with a softer hairline — the heavy rule is the structural signature
- Don't use Ember Orange as a button fill — it's a column-stroke and arrow accent only
- Don't pair Fort with another serif — the three-weight monoculture carries the institution

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero scales to 32px FortExtraBold, body 16px FortBook maintained |
| Mobile | 375–767px | Single-column, hero 40px, hamburger nav, hero photography full-bleed |
| Tablet | 768–1023px | 2-column feed grid, hero 48px |
| Desktop | 1024–1279px | 3-column feed grid, hero 56px FortExtraBold, full primary nav with 4px rule |
| Large Desktop | ≥1280px | Maximum scale, 1440px container, full editorial spacing |
| XL Desktop | ≥1480px | Editorial spread mode, 96–128px section padding |

### Touch Targets
- Primary CTAs: 12px vertical padding × 2 plus 16px line-height produces ~40–44px tap height — at the smaller end of comfortable
- Nav links: 14px FortBook with 16–24px padding
- Editorial cards: full-card tappable with FortExtraBold headline as the visual affordance
- Form inputs: minimum 44px tap-comfortable height via parent `1px solid #000` container

### Collapsing Strategy
- **Nav**: Horizontal nav with 4px below-rule collapses to hamburger drawer below 768px; drawer reveals stacked FortExtraBold UPPERCASE section names
- **Feed grid**: 3-column → 2-column → single column; 1px hairline dividers persist at all widths
- **Article column**: Reading column maintains ~640–720px max even on large desktop — the line measure is sacred
- **Display type**: FortExtraBold 56px → 40px → 32px progressive scaling; weight 400 maintained throughout
- **Dark hero panels**: Maintain `#161616` background; padding compresses 64px → 32px on mobile
- **Section spacing**: 96–128px desktop → 32–48px mobile while preserving editorial rhythm

### Image Behavior
- Photography full-bleed within the article column, occasionally breaking out for cinematic features
- Editorial card imagery maintains 4:3 or 16:9 aspect ratio across breakpoints
- Image captions in FortBook 14px, color `#616161`, no background tint
- No art-direction shifts between breakpoints — same composition adapts proportionally

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Text / Background Inversion: Ink Black (`#000000`)
- Page Background: Sheet White (`#ffffff`)
- Cinematic Hero Background: `#161616`
- Brand Accent: Ember Orange (`#ff4713`)
- Hyperlink: Document Blue (`#005eb8`)
- Hyperlink Hover: `#3860be`
- Caption / Footer Text: `#616161`
- Hairline Border: `#000000` (pure ink, not softened grey)
- Below-Nav Rule: `4px solid #000`

### Quick Type Reference
- Display hero: FortExtraBold 56px / 1.14 line-height / weight 400
- Section heading: FortBold 32px / 1.00 line-height / weight 700
- Body reading: FortBook 16px / 1.50 line-height / weight 400
- Button label: FortBold 16px / weight 800
- Caption: FortBook 14px
- Tabular financial data: Arial 14.4px / `0.144px` letter-spacing

### Example Component Prompts
- "Create a BlackRock-style hero on `#ffffff` with a 56px FortExtraBold weight 400 headline, line-height 1.14, color `#000000`. Sub-deck in 24px FortBook weight 400 line-height 1.33, letter-spacing 1px, color `#000`. Primary CTA: `#000` background, `#fff` text, `0px` radius, `1px solid #000` border, padding `12px 24px`, 16px FortBold weight 800 — 'Keep exploring'. On hover, background goes white, text shifts to `#2285f7`, ambient shadow `rgba(112, 112, 112, 0.5) 0px 0px 12px 0px` appears."
- "Build a long-form article opener: full-bleed photo above the fold, then a centered 720px reading column on `#ffffff`. Headline at 40px FortExtraBold weight 400 line-height 1.20, color `#000`. Dek at 24px FortBook weight 400 line-height 1.33 letter-spacing 1px. Body at 16px FortBook line-height 1.50, paragraphs separated by 16px."
- "Design a navigation: white sticky header with the BlackRock wordmark left-aligned. Nav links in 14px FortBook weight 700 color `#000`, hover shifts to `#005eb8`. Below the nav, a `4px solid #000` rule announces the navigation boundary."
- "Create a cinematic dark feature panel: `#161616` background, 64px padding, FortExtraBold 48px white headline at line-height 1.20, FortBook 18px white body, 'Read more →' link in white with Ember Orange (`#ff4713`) arrow. Outlined inverse button: `transparent` bg, `1px solid #fff` border, `2px` radius, 16px FortBold weight 400 white label."
- "Build a fund-data table: white surface, headers in 12px FortExtraBold UPPERCASE color `#000`, body cells in Arial 14.4px weight 400 color `#000`, letter-spacing `0.144px`, line-height 2.64. Column rules in `1px solid #000` (full ink). Header row separated from body by `4px solid #000` rule. Ember Orange (`#ff4713`) marker on the active column header."
- "Design an editorial pull-out card: white background, `0px 1px 1px solid #000` three-sided border, `0px` radius, 32px internal padding. Headline in 24px FortExtraBold, body in 16px FortBook line-height 1.50, 'Keep exploring →' link in 16px FortBold with Ember Orange arrow."

### Iteration Guide
1. Default to the three-weight Fort serif system: FortExtraBold (display), FortBold (heads + buttons), FortBook (body). No sans on primary chrome.
2. Use pure black (`#000000`) for headlines and pure white (`#ffffff`) for canvas — institutional ink on institutional paper, no softening.
3. Reserve Ember Orange (`#ff4713`) for column-header strokes and feature-link arrows. Never on body, never as a button fill.
4. Use Document Blue (`#005eb8`) for inline hyperlinks only — never on body, never as a brand accent.
5. Border-radius is `0px` for primary buttons and cards; `2px` for "Keep exploring" / "Close" mid-tier CTAs only.
6. Set primary CTA labels in FortBold weight 800 — serif buttons are the brand's signature.
7. Use 1px solid black hairlines (`1px solid #000`) for borders — full ink, never softened grey.
8. Apply the 4px solid black below-nav rule as the system's single bold structural separator.
9. Drop to Arial at 14.4px / `0.144px` letter-spacing for tabular financial data — the workhorse for numerical density.
10. Use the dark `#161616` panel for cinematic features — the system's chapter break and only true elevation.
