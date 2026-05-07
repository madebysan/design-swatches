---
version: alpha
name: "Santa Maria Novella"
description: "Parchment canvas and Tesseract Display weight 200 carry eight centuries of Florentine apothecary authority"

colors:
  background: "#ffffff"
  surface: "#000000"
  surface-elevated: "#f5f5f5"
  ink: "#121212"
  ink-muted: "#f9f6f5"
  primary: "#c69967"
  on-primary: "#ffffff"
  border: "#666666"
  focus-ring: "#c69967"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Tesseract Display, ui-sans-serif, system-ui, sans-serif"
    fontSize: 54px
    fontWeight: 200
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Tesseract Display, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 200
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Tesseract Display, ui-sans-serif, system-ui, sans-serif"
    fontSize: 25px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Tesseract Display, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Tesseract Display, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Tesseract Display, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Tesseract Display, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Tesseract Display, ui-sans-serif, system-ui, sans-serif"
    fontSize: 21px
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

# Santa Maria Novella Design System

## Overview

Santa Maria Novella's website is not a shop — it is a vitrine. The page opens on a full-bleed cinematic photograph of a perfume flask, its handcrafted label lettered in the apothecary script of medieval Florence, the glass body catching warm amber light. Below, a navigation bar sits against a near-white parchment ground (`rgb(249, 246, 245)`) that feels less like a browser background and more like the uncoated paper of a herbalist's ledger. There are no gradients, no chromatic branding splashes, no hero countdown timers. The Officina's identity needs no augmentation: 800 years of continuous production in the same Florentine convent is the brand promise, and the design communicates it through material restraint and archival confidence.

The masterstroke is `Tesseract Display` — a contemporary narrow serif deployed exclusively at weight 200 for every heading from micro-caption to full-bleed hero. At 54px with letter-spacing `-1.08px` and a tight `1.05` line-height, it achieves something rare in retail typography: the letterforms read simultaneously as monumental and fragile, like hand-engraved pharmaceutical labels pressed into vellum. The uppercase transformation applied universally removes any warmth or informality. Every headline is an inscription, not an advertisement. The sans-serif workhorse `Futura PT` (with `Jost` as the web fallback) handles all functional UI text — navigation links, product labels, buttons — at weights 300–500 and measured letter-spacing of `0.162–0.648px`. The two-typeface system is a study in contrast: one voice for heritage, one for commerce, never confused.

What prevents this restraint from curdling into coldness is the photography. Every hero image is shot with the patience of a still-life painter — dramatic side-light, shallow depth of field, jewel-toned botanical props. The amber glass of the L'Iris bottle, the purple of live iris blooms breaking into frame from the right edge: these are the brand's only chromatic statements, delivered through imagery rather than UI color. The gold star rating token (`#c69967`) is the sole warm accent that escapes into the interface itself — a fitting choice, since the brand's heraldic crest features Florentine gold. Everything else is black on cream, or cream on black.

**Key Characteristics:**
- Tesseract Display at weight 200, uppercase, across all heading tiers — a lighter-than-light serif that reads as engraving
- Parchment canvas `rgb(249, 246, 245)` — distinctly warmer than white, evoking uncoated paper stock
- Hard `0px` border-radius on nearly all interactive elements — no rounding, no digital softness
- Binary button system: sharp rectangular (primary) and pill `25px` (filter/category tags) — nothing in between
- Bottom-border-only input underlines — `0px 0px 1px solid rgb(18,18,18)` — referencing handwritten ledger lines
- Near-black `rgb(18, 18, 18)` as the system foreground — not pure black, carrying a barely perceptible warmth
- Gold star accent `#c69967` — the only chromatic UI color, drawn from the brand's heraldic crest
- Scale-on-hover interactions (`scale(1.1)`) combined with grey wash `rgb(102,102,102)` — tactile, not frenetic
- Full-bleed hero photography with no text overlays or gradient scrims — imagery stands alone
- Letter-spacing consistently positive on UI text (0.162–1.08px), reinforcing the typeset precision of archival labels

## Colors

### Primary Brand
- **Apothecary Near-Black** (`#121212` / `rgb(18, 18, 18)`): The dominant foreground color for all body text, labels, borders, and icon strokes. Warmer than pure black, closer to the darkened oak of an old apothecary cabinet. Used in 3,590 occurrences — the chromatic backbone of the entire system.

### Brand Accent
- **Florentine Gold** (`#c69967`): The heraldic accent — used exclusively for product star ratings and the occasional category highlight. Drawn from the Officina's historic crest. Warm amber-gold at `lch(66.34% 34.33 72.05)`, it evokes gilt labels and pharmacy seals. The only chromatic color in the UI layer.

### Text Scale
- **Apothecary Near-Black** (`#121212`): Primary body, headings (where not inherited), nav links, prices, labels
- **Pure Black** (`#000000`): Button borders, certain button text, absolute-contrast moments
- **Medium Grey** (`#666666`): Hover states — when an element is interacted with, the near-black shifts to this desaturated grey, creating a "pressed" tactile sensation rather than a dramatic color change
- **Warm White** (`#ffffff`): Text on dark-button surfaces, inverted navigation link states

### Surface & Canvas
- **Parchment** (`rgb(249, 246, 245)` / `#f9f6f5`): Primary page background — the warmest "white" in the system, slightly rosé-tinted, evoking cream laid paper
- **Pure White** (`#ffffff`): Card surfaces, modal dialogs, email input backgrounds — the lightest surface
- **True Black** (`#000000`): Dark CTA button backgrounds, dark hero overlay sections

### Borders
- **Near-Black Rule** (`rgb(18, 18, 18)`): Standard 1px borders on forms (bottom-only `0px 0px 1px`), full borders on button tabs, and vertical dividers (`0px 0px 0px 1px`)
- **Near-Black Muted** (`rgba(18, 18, 18, 0.2)`): Horizontal list item dividers — 20% opacity creates the ghost rule of a pharmaceutical inventory list
- **Near-Black Faint** (`rgba(18, 18, 18, 0.1)`): Dialog/modal borders — barely visible containment, like a watermark
- **Near-Black Ghost** (`rgba(18, 18, 18, 0.08)`): Footer top border — the softest separation
- **Light Divider** (`rgb(204, 204, 204)`): Occasional light section separators on white surfaces

### Semantic & System
- **Star Gold** (`#c69967`): Review star ratings (jdgm system)
- **Success Mint** (`#AEE9D1`): Wishlist subscribe success background — a soft mint used by the third-party swym integration
- **Success Green** (`#00a65a`): Swym remind CTA — bright green for back-in-stock alerts
- **Error Red** (`rgb(232, 55, 55)`): Validation error states — a warm tomato red on form spans
- **Pagination Blue** (`#1d4f91`): Third-party pagination controls (jdgm reviews plugin) — the only cool blue in the system, from an external library

### Gradient System
- Santa Maria Novella is **gradient-free** in the interface. Depth and warmth come entirely from photographic imagery and the contrast between parchment surfaces and archival black type. The word "gradient" appears in class names (the `.gradient` body class) but applies to scroll behavior, not color.

## Typography

### Font Family
- **Display / Headings**: `Tesseract Display`, with fallback: `"Times New Roman"`, `serif`
- **Body / UI**: `Futura PT`, with fallback: `Jost`, `"Century Gothic"`, `sans-serif`
- **System / Third-party**: `Arial` — used only in cookie consent and framework-injected elements
- **OpenType Features**: Standard ligatures only. No stylistic sets extracted — the typefaces' native proportions carry the identity.

*Note: Tesseract Display is a commercial narrow serif. For external implementations, Cormorant Garamond Display or a narrow-cut Didot serve as visual analogues. Futura PT is standard from Adobe Fonts; Jost (Google Fonts) is the direct web substitute.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Hero Display | Tesseract Display | 54px (3.38rem) | 200 | 1.05 | -1.08px | uppercase | Maximum hero inscriptions |
| Display Large | Tesseract Display | 41.04px (2.56rem) | 200 | 1.05 | -0.8208px | uppercase | Section hero headings |
| Section Heading | Tesseract Display | 25.92px (1.62rem) | 200 | 1.30 | +0.648px | uppercase | Feature section titles — note: positive tracking at this size |
| Sub-heading | Tesseract Display | 23.76px (1.49rem) | 200 | 1.05 | -0.4752px | uppercase | Card headings, collection titles |
| Sub-heading Link | Tesseract Display | 23.76px (1.49rem) | 200 | 1.05 | -0.4752px | uppercase | Linked sub-headings (same as sub-heading) |
| Sub-heading Small | Tesseract Display | 21.6px (1.35rem) | 200 | 1.00 | -0.432px | uppercase | Smaller section markers |
| Feature Label | Tesseract Display | 19.44px (1.22rem) | 200 | 1.30 | +0.648px | uppercase | Editorial labels, caption headings |
| Nav / UI Primary | Futura PT | 17.28px (1.08rem) | 300 | 1.37 | +0.648px | none | Navigation links, primary UI text |
| Nav / UI Alt | Futura PT | 17.28px (1.08rem) | 300 | 1.80 | +0.648px | none | Dropdown / spaced UI variant |
| Button Primary | Futura PT | 16.2px (1.01rem) | 500 | 1.30 | +0.162px | uppercase | CTA button labels |
| Body / Link | Futura PT | 16.2px (1.01rem) | 300–400 | 1.20–1.80 | +0.162–0.648px | mixed | Standard body and inline links |
| Product Text | Futura PT | 16px (1.00rem) | 400 | 1.38 | +0.648px | none | Product names, descriptions |
| Small Body | Futura PT | 15.12px (0.94rem) | 300–450 | 1.06–1.50 | +0.432–1.08px | mixed | Compact body and label text |
| UI Label | Futura PT | 14.28px (0.89rem) | 300 | 1.37 | +0.648px | none | Secondary labels, metadata |
| Form Label | Futura PT | 14.04px (0.88rem) | 300–400 | 1.40–1.50 | +0.432px | mixed | Input labels, form annotations |
| Caption | Futura PT | 12.96px (0.81rem) | 300 | 1.16 | +0.3888px | uppercase | Photo captions, micro-labels |
| Micro Caption | Futura PT | 11.88px (0.74rem) | 300 | 1.20 | +0.756px | uppercase | Finest print, footnotes, timestamps |
| Micro Link | Futura PT | 12px (0.75rem) | 300 | 2.50 | +0.648px | uppercase | Micro uppercase navigation links |

### Principles
- **Weight 200 as the singular serif voice**: Every Tesseract Display heading runs at weight 200 — the lightest meaningful weight. Where apothecary brands typically reach for ornate boldness to signal heritage, Santa Maria Novella uses extreme lightness. The hairline letterforms read as hand-engraved, not desktop-printed.
- **Uppercase as inscription**: All Tesseract Display text uses `text-transform: uppercase`, universally and without exception. The system never whispers — it inscribes. This is the typographic equivalent of hand-lettering pharmaceutical labels.
- **Negative tracking at display scale, positive at label scale**: Tracking inverts across the scale. Large display (41–54px) uses negative tracking (-0.82 to -1.08px) to lock letterforms into dense monumental blocks. Medium sizes (19–25px) flip to positive tracking (+0.648px), and UI labels extend further (+0.756–1.08px) for legibility at small sizes. This inversion is the system's most sophisticated typographic decision.
- **Futura as the functional counterweight**: Futura PT's geometric precision creates visual tension against Tesseract's refined serifs — the same opposition that exists between a pharmacist's clinical handwriting and the decorative label on the bottle they fill.
- **Two weights only on sans**: Futura PT uses weight 300 for body/nav and weight 500 for uppercase CTAs. Weight 400 appears for standard inline text. This three-step range keeps the UI voice consistent and never competes with the display serif.

## Layout

### Spacing System
- Base scale: `6.48px` (the highest-frequency value at 212 occurrences) — the system's micro unit, derived from a 1.08 scale factor applied to 6px
- Scale: `1px`, `2.16px`, `5px`, `5.4px`, `6.48px`, `7.56px`, `10.8px`, `12px`, `12.96px`, `14.04px`, `16px`, `16.2px`, `17.28px`, `18.36px`, `20px`, `25.92px`
- Button padding standard: `12px 24px` (2:1 ratio)
- Section padding: estimated 40–80px between major page sections
- The 1.08 multiplier (the same used in Futura PT and Tesseract sizing) appears throughout spacing, creating a unified scale: `6 × 1.08 = 6.48`, `6.48 × 1.08 = 7`, `10 × 1.08 = 10.8`, `16 × 1.08 = 17.28`

### Grid & Container
- Max content width: approximately 1400px, centered
- Hero: full-bleed to viewport edges, photography with left-aligned overlay button
- Product grid: 3–4 column responsive grid on desktop, collapsing to 2 then 1 on mobile
- Collection sliders: full-width horizontal scrollers with filter pills above
- Footer: multi-column link grid on dark/dark-parchment background

### Whitespace Philosophy
- **Archival breathing room**: Each product photograph is given gallery-level space. Grid gutters are generous (estimated 24–32px), and the parchment background extends fully between cards rather than shrinking to tight gutters.
- **Typographic leading as structure**: The Tesseract Display headings at tight 1.00–1.05 line-height create dense inscription blocks that float within generous surrounding whitespace — the contrast between compressed type and open canvas creates visual authority.
- **Ledger rhythm**: Bottom-border-only inputs and `rgba(18,18,18,0.2)` list dividers create a horizontal-rule pattern that echoes handwritten pharmaceutical inventories — the whitespace between rules is as designed as the rules themselves.

### Border Radius Scale
- `0px`: Absolute default — all product cards, buttons, inputs, content containers, navigation. The system is rectangular.
- `8px`: Dialogs and modal containers only — the single exception where softness signals "this is an overlay, not a page element"
- `25px`: Collection filter pills — functional distinction between "this is a toggle" and "this is a button"
- `50%`: Circular elements — close buttons, cart badge counts, wishlist counters, circular image crops
- `100%`: Badge dot elements only

## Elevation & Depth

| Level | Box Shadow Value | Use Case |
|-------|-----------------|----------|
| Flat (Level 0) | `none` | Page canvas, product cards at rest, all content containers |
| Primed (Level 0.5) | `rgba(18, 18, 18, 0) 0px 4px 5px 0px` | Card baseline — zero-opacity shadow, primed for hover transition |
| Focus Ring (Level 1) | `rgba(18, 18, 18, 0) 0px 0px 0px 2.16px` | Input focus ring — primed, transitions on interaction |
| Modal Soft (Level 2) | `rgba(0,0,0,0.2) 0px 0px 12px 0px` | Dialog and modal panel depth |
| Modal Stamp (Level 2a) | `rgba(0,0,0,0.2) 1px 1px 1px 1px` | Small directional shadow on dialog containers |
| Scroll Reveal (Level 3) | `rgba(0,0,0,0.2) 0px 0px 25px 0px` | Product cards or panels revealed on hover/scroll |

**Shadow philosophy**: Santa Maria Novella's shadow system is almost entirely theatrical rather than structural. The dominant shadow pattern — `rgba(18, 18, 18, 0) 0px 4px 5px 0px` — exists at zero opacity in CSS, primed to transition visible on scroll or hover. This is a subtle performance: the depth is implied before it's revealed, like the shadow of a bottle that only becomes visible when you move closer. The system uses minimal actual elevation; instead, it relies on the contrast between the warm parchment canvas and the photographic imagery's own atmospheric depth — studio lighting does the work that box-shadows cannot.

### Decorative Depth
- Photography provides all atmospheric depth — the amber glass catching light against a grey ground plane reads as more three-dimensional than any CSS shadow system could produce
- Hard borders (`1px solid rgb(18,18,18)`) on buttons provide edge definition without shadow
- The `50%` circular close buttons use `rgba(0,0,0,0.2) 0px 0px 25px 0px` for a soft glow on modal overlays

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

**Primary Light (Shop / Discover)**
- Background: `#ffffff`
- Text: `#000000`
- Padding: `12px 24px`
- Radius: `0px` (sharp rectangular)
- Border: `1px solid rgb(0, 0, 0)`
- Box Shadow: `none`
- Font: Futura PT 16.2px, weight 500, uppercase, letter-spacing `0.162px`
- Hover: background `rgb(102, 102, 102)`, text `#ffffff`, border `1px solid rgb(34, 34, 34)`, `transform: scale(1.1)`, opacity `0.9`
- Active: background `#000000`, text `#ffffff`, outline `rgb(102, 102, 102) solid 2px`
- Use: "Discover More", primary shop CTAs on light parchment surfaces

**Primary Dark (Add to Cart / Shop Now)**
- Background: `rgb(18, 18, 18)`
- Text: `#ffffff`
- Padding: `0px 32.4px`
- Radius: `0px`
- Border: `none`
- Font: Futura PT 16.2px, weight 500, uppercase, letter-spacing `0.162px`
- Hover: background `rgba(var(--color-foreground), 0.04)`, border `1px solid rgb(34, 34, 34)`, `transform: scale(1.07)`, opacity `0.4`
- Active: `box-shadow: 0 0 0 10rem rgb(var(--color-background)) inset`, outline `rgb(102,102,102) solid 2px`
- Focus: background `rgb(102,102,102)`, outline `0.2rem solid rgba(var(--color-foreground), 0.5)`
- Use: Add to cart, primary dark-surface CTAs

**Filter Pill — Active**
- Background: `rgb(0, 0, 0)`
- Text: `rgb(255, 255, 255)`
- Padding: `12px 24px`
- Radius: `25px` (pill — the only non-zero radius on interactive elements)
- Border: `1px solid rgb(0, 0, 0)`
- Font: Futura PT 16.2px, weight 500, uppercase
- Hover: background `rgb(102, 102, 102)`, opacity `0.9`
- Use: Active category/collection filter tags

**Filter Pill — Inactive**
- Background: `rgba(0, 0, 0, 0)` (transparent)
- Text: `rgb(0, 0, 0)`
- Padding: `12px 24px`
- Radius: `25px`
- Border: `1px solid rgb(0, 0, 0)`
- Font: Futura PT 16.2px, weight 500, uppercase
- Hover: background `rgb(102, 102, 102)`, text `#ffffff`, opacity `0.9`
- Use: Inactive category filter tags — toggle with active pill above

**Parchment Surface Button (Utility)**
- Background: `rgb(249, 246, 245)`
- Text: `rgb(18, 18, 18)`
- Padding: `0px`
- Radius: `0px`
- Border: none
- Font: Futura PT 17.28px, weight 300, letter-spacing `0.648px`
- Use: Inline text-level buttons, wishlist actions, utility triggers

### Cards & Product Containers
- Background: `#ffffff` or `rgb(249, 246, 245)` depending on section context
- Border: none by default — cards are separated by spacing and photographic imagery, not frames
- Radius: `0px` — all product cards are sharp-cornered
- Shadow: `rgba(18, 18, 18, 0) 0px 4px 5px 0px` — technically present in CSS but at zero opacity (primed for hover reveal)
- Hover shadow: transitions from `0` to `rgba(0,0,0,0.2) 0px 0px 25px 0px` on elevated states
- Internal padding: generous — product imagery is full-width within its container, text follows below with 14–20px rhythm

### Inputs & Forms
**Underline Input (Default)**
- Background: `rgb(249, 246, 245)` (parchment) or `rgb(255, 255, 255)`
- Text: `rgb(18, 18, 18)` (light surfaces) or `#ffffff` (dark surfaces)
- Border: `0px 0px 1px solid rgb(18, 18, 18)` — bottom rule only, referencing the ledger line
- Radius: `0px`
- Padding: `16.2px` on search inputs
- Font: Futura PT, weight 300, 16–17px
- Focus: `borderColor: rgb(51,51,51)`, browser outline visible
- Use: Search fields, email newsletter inputs, checkout forms

**Newsletter Email (Dark Surface)**
- Background: `rgba(255, 255, 255, 0)` (transparent)
- Text: `rgb(255, 255, 255)`
- Border: bottom rule `0px 0px 1px solid rgb(255, 255, 255)` — white rule on dark
- Radius: `0px`
- Font: Futura PT, weight 300

### Navigation
- Sticky top bar on parchment `rgb(249, 246, 245)` background
- Left: Officina wordmark and heraldic crest SVG lockup
- Center: horizontal link groups (Fragrances, Skincare, Body & Hair, Home, Gifts, Our Icons, Our Story)
- Right: Language selector (EN →), search, wishlist, cart, account icons (SVG system)
- Nav links: Futura PT 17.28px weight 300, `#121212`, letter-spacing `0.648px`, no text decoration
- Active/hover: underline `0.3rem` weight — a heavy editorial rule rather than a thin underline
- No visible nav border in default state; `rgba(18,18,18,0.08)` top-border on footer
- Mobile: collapses to hamburger; mobile menu close uses `1px solid rgb(18,18,18)` top-border on the close element

### Dialogs & Modals
- Background: `#ffffff`
- Border: `1px solid rgba(18, 18, 18, 0.1)` — ghost containment
- Radius: `8px` — the only instance of meaningful rounding in the system; dialogs are softened where content surfaces are sharp
- Shadow: `rgba(0,0,0,0.2) 0px 0px 12px 0px` and `rgba(0,0,0,0.2) 1px 1px 1px 1px`
- Close button: `50%` radius circular element (close/modal class)
- "JOIN OUR WORLD" newsletter panel: white card, bottom-border email input, arrow submit button — minimal, ledger-aesthetic

### Badges & Tags
- The dembrandt extraction returns no formal badge components — the brand's editorial approach uses Tesseract Display labels and Futura PT uppercase captions as status indicators
- Cart/wishlist counts: circular badge `100%` radius, positioned over icon SVGs
- Star ratings: `#c69967` Florentine Gold — the only chromatic badge moment

### Image Treatment
- Full-bleed hero photography occupying the entire viewport on landing
- No gradient scrims, no text overlays — photography and UI exist in separate planes
- Product photography: high-contrast studio lighting, warm amber and violet tones, physical bottles, botanicals
- No lifestyle/aspirational human imagery — objects and ingredients only
- Image carousels use Swiper.js (prev/next buttons at `rgb(0,0,0)`)

## Do's and Don'ts

**Do**:
- Use Tesseract Display at weight 200 with `text-transform: uppercase` for every heading tier — the weight and case combination IS the brand voice
- Apply negative letter-spacing on large Tesseract Display (`-1.08px` at 54px) and positive tracking on small Futura PT labels (`+0.648–1.08px`) — the inversion is intentional and systematic
- Use the parchment background `rgb(249, 246, 245)` as the page canvas, never pure white `#ffffff` — the warmth is the distinction
- Reserve the `25px` pill radius exclusively for collection filter/category tags — it signals "toggle" versus "action"
- Apply bottom-border-only styling (`0px 0px 1px solid rgb(18,18,18)`) on all text inputs — the ledger line is the form aesthetic
- Let photography carry emotional and chromatic weight — UI color is monochromatic by design, imagery provides all warmth
- Use `rgb(18,18,18)` as the foreground text color rather than pure `#000000` — the near-black softness matters at body sizes
- Apply `scale(1.1)` hover transforms on buttons alongside the grey-wash `rgb(102,102,102)` — the physical "press" interaction is a signature

**Don't**:
- Don't introduce border-radius between `0px` and `25px` on any UI surface — the system is deliberately binary (sharp or pill)
- Don't use weight 400+ on Tesseract Display — weight 200 is the only sanctioned display weight; anything heavier destroys the engraved-label quality
- Don't mix lowercase Tesseract Display headings with the uppercase system — the uppercase inscription is non-negotiable
- Don't add chromatic accent colors beyond `#c69967` Florentine Gold — this is a mono-canvas system where color lives exclusively in photography
- Don't use blurred drop shadows on content cards or product imagery — flat borders and zero-opacity primed shadows are the correct approach
- Don't use positive letter-spacing on large display text — tracking above 30px should always be negative or zero
- Don't use the `25px` pill radius on primary action buttons — it's reserved for filter toggles, not conversion actions
- Don't use Futura PT at weights above 500 — the system caps the sans at medium weight to avoid competing with the display serif's visual authority

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Micro | 0–380px | Single column, minimal chrome, stacked nav elements |
| Mobile Small | 380–436px | Single column, reduced hero size |
| Mobile | 436–560px | Single column, 36–44px hero headline |
| Mobile Large | 560–749px | 1–2 column product grid, 44–48px display |
| Tablet Small | 749–768px | 2-column grid, condensed nav, 48–52px display |
| Tablet | 768–990px | 2–3 column grid, full navigation begins |
| Desktop Small | 990–1000px | Full horizontal nav, 3-column grid, 52–54px display |
| Desktop | 1000–1400px | Full layout, 4-column product grid, maximum typescale |
| Large Desktop | ≥1400px | Max container 1400px, generous lateral margins |

### Touch Targets
- Primary CTA buttons: minimum 44px height via `12px` vertical padding on 16–17px text
- Navigation icons (search, wishlist, cart, account): SVG icons with minimum 44×44px tap area
- Filter pills `25px` radius: `12px 24px` padding creates adequate touch area
- Close button (dialog): `50%` circular element — ensure minimum 32px diameter

### Collapsing Strategy
- **Navigation**: Full horizontal link bar collapses to hamburger; mobile menu opens as a full or panel overlay with `1px solid rgb(18,18,18)` close rule
- **Hero**: Full-bleed photography maintains at all breakpoints; overlay "Discover More" button shifts position from lower-left to bottom-center on mobile
- **Headline scale**: 54px hero → 41px → 25px across breakpoints, weight 200 and uppercase maintained throughout
- **Product grid**: 4-column → 3-column → 2-column → 1-column with unchanged card styling
- **Collection sliders**: Filter pills scroll horizontally on mobile rather than wrapping
- **Newsletter dialog**: Full-width on mobile (minus 16px margin each side), centered constrained width on desktop
- **Spacing**: Scale reduces proportionally — the `6.48px` micro-unit remains, larger section gaps compress from ~80px to ~40px

### Image Behavior
- Full-bleed hero photography retains its full-viewport treatment at all breakpoints using `object-fit: cover`
- Product images maintain aspect ratio within their grid cells
- No art direction changes — the same high-quality studio photography adapts via cropping
- Swiper carousels remain functional on touch with swipe gestures replacing arrow navigation

---

## Agent Prompt Guide

### Quick Reference
- Primary CTA Background: `#ffffff` (light) / `#121212` (dark)
- Primary CTA Border: `1px solid #000000`
- Page Background: `rgb(249, 246, 245)` — parchment
- Primary Text: `rgb(18, 18, 18)` — apothecary near-black
- Display Font: `Tesseract Display`, weight `200`, uppercase
- UI Font: `Futura PT` (fallback: `Jost`), weight 300–500
- Gold Accent: `#c69967` — star ratings only
- Hover Grey: `rgb(102, 102, 102)`
- Dialog/Modal Radius: `8px`
- Filter Pill Radius: `25px`
- All other radius: `0px`
- Input Border: `0px 0px 1px solid rgb(18, 18, 18)` (bottom-only)
- Button Hover Scale: `transform: scale(1.1)`

### Example Component Prompts
- "Create a hero section with a full-bleed editorial photograph as the background — no gradient scrim, no text overlay on the image. Position a standalone 'Discover More' button in the lower-left at 20% from left, 55% from top. Button: white background `#ffffff`, 1px solid black border, `0px` border-radius, padding `12px 24px`, Futura PT 16.2px weight 500 uppercase letter-spacing `0.162px`. Page canvas beneath the hero is `rgb(249, 246, 245)` parchment."
- "Design a product card on parchment background `rgb(249, 246, 245)`. No card border, no box-shadow in default state. Full-width product image above (0px radius). Below: product name in Tesseract Display 23.76px weight 200 uppercase letter-spacing `-0.4752px` color `rgb(18,18,18)`. Price in Futura PT 16px weight 400 letter-spacing `0.648px`. On hover: reveal `rgba(0,0,0,0.2) 0px 0px 25px 0px` shadow, button scales `1.1`."
- "Build a newsletter signup section on a dark `rgb(18,18,18)` background. Heading in Tesseract Display 41px weight 200 uppercase letter-spacing `-0.82px` color `#ffffff`. Below: email input with transparent background `rgba(255,255,255,0)`, white text `#ffffff`, bottom-border-only `0px 0px 1px solid #ffffff`, `0px` radius, Futura PT 17px weight 300. Submit: arrow icon button or small Futura PT uppercase button in white with `1px solid #ffffff` border, `0px` radius."
- "Create a collection filter pill bar. Each pill: padding `12px 24px`, radius `25px`, Futura PT 16.2px weight 500 uppercase letter-spacing `0.162px`. Active state: `#000000` background, `#ffffff` text, `1px solid #000000` border. Inactive state: transparent background, `#000000` text, `1px solid #000000` border. Hover both states: `rgb(102,102,102)` background, white text, `transform: scale(1.1)`, opacity `0.9`."
- "Design a 'JOIN OUR WORLD' newsletter dialog modal. White `#ffffff` background, `1px solid rgba(18,18,18,0.1)` border, `8px` border-radius, shadow `rgba(0,0,0,0.2) 0px 0px 12px 0px`. Close button: `50%` circular top-right corner. Title: Tesseract Display 25px weight 200 uppercase letter-spacing `0.648px` color `rgb(18,18,18)`. Email input: full-width, `0px` radius, bottom-border-only `0px 0px 1px solid rgb(18,18,18)`, Futura PT 16px weight 300. Submit arrow: `#000000` circle button with white arrow icon."

### Iteration Guide
1. Tesseract Display weight 200 + uppercase + negative tracking at scale: this trio is non-negotiable for every heading — change any one element and the heritage voice collapses
2. When in doubt about border-radius: use `0px`. Only escalate to `25px` for filter pills, `8px` for modal dialogs, `50%` for circular buttons/badges
3. The parchment background `rgb(249, 246, 245)` must never be replaced with pure white on page-level surfaces — the warmth is perceptible and intentional
4. Hover states always involve two simultaneous changes: `transform: scale(1.1)` AND background shift to `rgb(102, 102, 102)` — the physical-press sensation requires both
5. Letter-spacing inverts with scale: negative on large display (54px = -1.08px), positive on small labels (12px = +0.756px)
6. Chromatic color is photography's job: resist any temptation to introduce brand color in UI surfaces — the `#c69967` gold is the only exception and belongs only to star ratings
7. Input fields are always bottom-border-only (`0px 0px 1px solid ...`) — full-border inputs break the ledger-line aesthetic
8. Dark sections use `rgb(18, 18, 18)` not pure `#000000` — the same near-black warmth applies to dark surfaces as to light-surface text
