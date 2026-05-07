---
version: alpha
name: "Pentagram"
description: "Monochrome editorial rigour — Plain typeface, full-bleed imagery, and zero decoration as design philosophy"

colors:
  background: "#ffffff"
  surface: "#767676"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#222222"
  primary: "#1a1a1a"
  on-primary: "#ffffff"
  border: "#8c8c8c"
  focus-ring: "#1a1a1a"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Plain, ui-sans-serif, system-ui, sans-serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Plain, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Plain, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Plain, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Plain, ui-sans-serif, system-ui, sans-serif"
    fontSize: 21px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Plain, ui-sans-serif, system-ui, sans-serif"
    fontSize: 19px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Plain, ui-sans-serif, system-ui, sans-serif"
    fontSize: 19px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Plain, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
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

# Pentagram Design System

## Overview

Pentagram's website is the rarest of things: a design firm's digital presence that practices exactly what it preaches. The page opens on a pure white canvas (`#ffffff`) with a full-bleed hero image consuming nearly the entire viewport — no padding, no border-radius, no frame. The photography is allowed to breathe at its own scale, and only the faintest of captions sit at the lower-left like a museum wall label. The overall impression is of a very expensive monograph laid open on a white reading table: confident, unhurried, and absolutely certain it doesn't need to try.

The typeface is Plain — a grotesk that lives up to its name without being anonymous. At display sizes (52px), it runs at weight 400 with tight negative letter-spacing (`-1.04px`) and a claustrophobically compressed line-height of 1.05. These are not headlines designed to comfort; they are statements. The `"case"` OpenType feature is enabled on all display text, which adjusts case-sensitive punctuation and spacing — a precision detail that signals the system was built by people who notice such things. At 32px the tracking relaxes fractionally to `-0.32px`, and the line-height opens to 1.20. Below 20px, tracking normalises and the `"kern"` feature takes over from `"case"`, governing the more intimate typographic relationships of body text and captions.

What most distinguishes Pentagram's system is its chromatic restraint. Five hexes carry the entire page: near-black `#1a1a1a`, pure white `#ffffff`, and three grades of grey — `#767676`, `#8c8c8c`, and the secondary dark `#222222`. There is no accent colour. No blue CTA. No brand orange lurking in the hover state. The dark section (`#222222` background with white text) serves as the only meaningful surface shift, creating a quiet drama when the page crosses from gallery white to editorial dark. Every interactive affordance — the pill carousel dots, the filter badges, the section-crossing underlines — is expressed in the same achromatic language. The work provides all the colour.

**Key Characteristics:**
- Plain typeface with `"case"` OpenType feature on display text and `"kern"` on body — the invisible typographic detail that separates this from a generic grotesk site
- Weight 400 as the headline weight — no bold anywhere in display hierarchy; authority through proportion, not mass
- Negative letter-spacing scaling with size: `-1.04px` at 52px, `-0.32px` at 32px, relaxing to normal below 20px
- Near-black `#1a1a1a` for all primary text — not pure black, a fractional warm lift
- Five-hex monochrome palette — the work supplies all chromatic interest; the UI provides none
- Full-bleed hero imagery with zero border-radius — the frame IS the viewport
- Carousel dot navigation rendered as 18×18px circles at `9999px` radius — the only curved form in the system
- Shadow-free elevation system — depth is communicated through surface colour contrast alone
- `4px` border-radius as the sole interior radius — used on badges, filter chips, and modal overlays only
- Underline-on-dark as the primary link affordance: `text-decoration: underline 1px` on white links, reverting on hover

## Colors

### Primary Brand
- **Pentagram Black** (`#1a1a1a`): The primary text and heading color — near-black with a barely perceptible warmth. Used for all body copy, nav links, section headings, and the wordmark logotype. Count of 2,266 in the extraction — this is the dominant chromatic decision.

### Brand Accent
- **Pure Black** (`#000000`): Reserved for maximum-contrast moments — the thematic button overlay at 30% opacity, dark border treatments, and the full inky presence of dark interactive controls. A step below `#1a1a1a` in warmth, used for graphic rather than typographic purposes.

### Text Scale
- **Primary Text** (`#1a1a1a`): All headings, navigation, body copy, and link defaults on light surfaces.
- **Secondary Text / Muted** (`#767676`): Captions, metadata, image credits, and de-emphasized labels. At 49.64% lightness (LCH) — comfortably WCAG AA compliant on white.
- **Tertiary Text** (`#8c8c8c`): The semantic primary from the extraction — used for the softest annotation tier, footnotes, and form placeholder states.
- **Dark Section Text** (`#ffffff`): All text on the dark `#222222` editorial panels. Links use `underline 1px` in this context, removing it on hover.

### Surface & Backgrounds
- **Canvas White** (`#ffffff`): The primary page background — pure, no warm or cool tint. The default state for all content panels, the nav strip, and project cards.
- **Editorial Dark** (`#222222`): The dark surface used for "Our Future is the Ultimate Project" and analogous editorial sections. Not pure black — a deliberate step back from maximum contrast, creating a slightly warmer, print-like dark field.
- **Transparent Light Overlay** (`rgba(0, 0, 0, 0.07)`): Used as the background for filter badges and secondary interactive chips on the light canvas — a barely-there tinted surface that reads as "selected" or "available" without introducing colour.
- **Transparent Dark Overlay** (`rgba(255, 255, 255, 0.12)`): Used for the `btn--secondary` ghost button on dark sections — a frosted-glass-adjacent approach that maintains legibility over dark imagery.

### Borders
- **Dark Article Border** (`rgb(51, 51, 51)`): Top-edge `1px solid` border on article cards — separates list items in the work grid without visible weight.
- **Input Underline** (`#1a1a1a`): Bottom-only `1px solid` border on newsletter email inputs — the sole form border treatment.
- **Form Border** (`#8c8c8c`): Full form container bottom border — the muted separator for form regions.

### Shadows
- Pentagram uses **no shadows**. Zero entries in the extracted shadow array. Depth is entirely achieved through surface colour contrast and spatial layout.

### Debug / Development
- **Grid Column Debug** (`rgba(127, 255, 255, 0.25)`): The `--grid-column-bg` CSS variable — a development-only cyan overlay for column visualisation. Not present in production rendering.

## Typography

### Font Family
- **Primary**: `Plain`, with fallback: `Arial`, `sans-serif`
- **Monospace**: None — Plain handles all typographic registers including UI chrome
- **OpenType Features**: `"case"` on all display and navigation text (52px, 32px, 16px contexts); `"kern"` on all body, link, and caption text (19px, 13px contexts). These two features are mutually exclusive by size tier — never combined.

*Note: Plain is a commercial typeface. Söhne or Neue Haas Grotesk Display serve as the closest substitute for implementations requiring a web-licensed equivalent. The hint notes Söhne-class grotesk, which is accurate to the visual character.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Features | Notes |
|------|------|------|--------|-------------|----------------|----------|-------|
| Display Hero | Plain | 52px (3.25rem) | 400 | 1.05 (very tight) | -1.04px | "case" | Maximum size — homepage editorial statements |
| Section Heading | Plain | 32px (2.00rem) | 400 | 1.20 (tight) | -0.32px | "case" | Feature section anchors, dark panel headings |
| Interactive Heading | Plain | 32px (2.00rem) | 400 | 1.88 (relaxed) | -0.32px | "case" | Filter button / dropdown display size — generous leading for interactive context |
| Sub-heading / Card | Plain | 19px (1.19rem) | 500 | 1.32 | normal | "kern" | Project card titles, partner names |
| Body / Link Primary | Plain | 19px (1.19rem) | 400 | 1.32 | normal | "kern" | Standard body text, project descriptions |
| Nav Link | Plain | 19px (1.19rem) | 500 | 1.32 | normal | "kern" | Top navigation links — weight 500 distinguishes from body |
| Button / UI Action | Plain | 19px (1.19rem) | 400–500 | 0 (leading-none) | normal | "kern" | Icon-adjacent button labels — 0 line-height for precise vertical control |
| UI Label | Plain | 16px (1.00rem) | 500 | 1.25 | normal | "case" | Section labels, category markers, filter headings |
| UI Text / Small Link | Plain | 16px (1.00rem) | 400 | 1.25 | normal | "case" | Breadcrumbs, secondary nav text, form labels |
| Caption | Plain | 13px (0.81rem) | 400 | 1.25 | normal | "case" | Image credits, hero slide captions, metadata |
| Small Link | Plain | 13px (0.81rem) | 400 | 1.25 | normal | "case" | Archive links, footer links |

### Principles
- **Weight 400 at display sizes is the philosophical stance**: Pentagram uses regular weight for all its largest text. The 52px headline is not bold — it doesn't need to be. This is a firm whose reputation precedes any typographic emphasis. The weight 500 appears only at 19px for card titles and navigation — where UI legibility demands a fractional step up.
- **"case" vs "kern" as a size-based split**: Larger text (52px, 32px, 16px) enables `"case"` — the OpenType feature for case-sensitive punctuation spacing. Smaller text (19px, 13px) enables `"kern"` — standard kerning pairs. This two-feature system mirrors print typesetting conventions where display type and text type are treated as distinct disciplines.
- **Negative tracking tightens with size, stops cold**: From `-1.04px` at 52px to `-0.32px` at 32px, then nothing. Below 20px, Plain runs at normal tracking. There is no micro-tracking applied to captions or labels — the system trusts the typeface's own kerning below 20px.
- **Line-height as pacing control**: The 1.05 display line-height creates stacked headlines that nearly touch. At 32px it opens to 1.20. At 19px body it relaxes to 1.32. The progression is tight-to-comfortable, never airy — this is not a system that believes in generous body text spacing.
- **Single typeface, total discipline**: Plain handles every role without a secondary or mono companion. No code typeface, no serif for pull quotes, no display script for accent moments. The monofamily approach reinforces the editorial mono style tag.

## Layout

### Spacing System
- **Base unit**: 8px
- **Scale in use**: 3px, 4px, 6px, 7px, 8px, 12px, 16px, 18px, 22px, 24px, 32px, 48px, 64px, 70px, 96px, 124px
- **Notable density**: The scale uses 4px (count: 276) and 8px (count: 309) as the dominant micro-spacing values — button padding, gap between grid items, and internal card padding all resolve to these two values
- **Macro spacing**: 48px, 64px, 96px, and 124px govern section-level breathing room — generous but not maximalist
- **Edge case**: 557.656px appears once — a calculated pixel value from a responsive constraint, likely a hero image height or sidebar calculation

### Grid & Container
- **Max content width**: Approximately 1600–1920px at the largest breakpoint — the hero is full-bleed; container content sits within 1040–1600px
- **Hero section**: Full-bleed, zero padding, no border-radius — the image IS the container
- **Work grid**: Multi-column card grid (estimated 3–4 columns at desktop) with top-rule article separators
- **Dark editorial panel**: 100% viewport width — breaks the column grid intentionally
- **Carousel**: Full-width with dot navigation aligned bottom-right

### Whitespace Philosophy
- **Work as the breathing room**: Pentagram does not pad the page with decorative whitespace. The space is provided by the work itself — full-bleed imagery creates vast areas of visual interest that function as rest, not decoration.
- **Tight typography in generous space**: Small text (13–16px captions) inside large imagery zones creates a deliberate scale tension — the museum-label effect.
- **Section breaks are surface changes, not gaps**: The transition from white canvas to dark `#222222` panel is not preceded by margin — the sections collide directly. The colour shift IS the break.
- **Grid discipline over gestural layout**: The card grid is rigorous. Article borders (top-rule only) create horizontal rhythm. Columns align strictly. There are no rotated or angled elements anywhere.

### Border Radius Scale
- **None (0px)**: All content cards, images, editorial panels, inputs, and the nav strip — the overwhelming default
- **Micro (4px)**: Filter badges, interactive chips, modal overlays, and the ghost/thematic buttons — used exclusively on interactive chrome elements, never on content
- **Modal (8px)**: Dialog and overlay containers — the softest structural radius
- **Pill (9999px)**: Carousel dot navigation exclusively — the only curved form in the interface

## Elevation & Depth

| Level | Box Shadow Value | Use Case |
|-------|-----------------|----------|
| Flat (Level 0) | `none` | Everything — images, cards, panels, navigation, buttons |
| Surface Shift (Level 1) | Background change only: `#ffffff` → `rgba(0,0,0,0.07)` | Filter chips and secondary buttons — depth through opacity tint |
| Dark Section (Level 2) | Background change only: `#ffffff` → `#222222` | Editorial dark panels — maximum contrast without shadow |
| Focus Ring (Level 3) | `outline: transparent solid 2px` (accessible placeholder) | Keyboard focus on interactive elements — outline-based, not shadow |

Pentagram's shadow philosophy is its most radical design statement: there are none. Zero shadows extracted from the entire page. Elevation is communicated exclusively through surface colour relationships — the near-invisible `rgba(0,0,0,0.07)` tint against white reads as "above" without any physical lift. The dark editorial section reads as "other" by surface identity alone. This approach demands that the layout be spatially unambiguous without depth cues — and it succeeds because the grid discipline and full-bleed photography provide sufficient visual hierarchy.

The only "shadows" in the system are implicit: dark photography creates its own depth field, and the darkened backdrop imagery behind the hero carousel creates an atmospheric foreground/background separation through photographic tonal contrast.

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

**Carousel Navigation Dot (Primary Interactive)**
- Background: `#ffffff` (light) or `#000000` (dark/selected)
- Size: 18×18px
- Radius: `9999px` (perfect circle)
- Border: `0px solid #1a1a1a` (border-present but width-0 — hover likely introduces visible border)
- Opacity: `0.5` at rest (dimmed), `1.0` on active slide
- Font: Plain 19px weight 400 (accessible label only — visually icon-free)
- Outline: `#1a1a1a none 3px` (focus state ready)
- Use: Slide position indicators in the hero carousel — the only `9999px` radius elements in the system

**Filter / Taxonomy Badge Button**
- Background: `rgba(0, 0, 0, 0.07)` — near-invisible tinted surface
- Text: `rgba(0, 0, 0, 0.56)` — muted near-black
- Padding: `4px 8px`
- Radius: `4px`
- Border: `0px solid rgba(0, 0, 0, 0.56)`
- Font: Plain 13px weight 400, `"case"` feature
- Use: Discipline and sector filter pills ("Brand Identity", "Arts & Culture")

**Interactive Filter Chip (Active/Dark)**
- Background: `rgba(0, 0, 0, 0.07)`
- Text: `#1a1a1a`
- Padding: `6px 8px`
- Radius: `4px`
- Border: `0px solid #1a1a1a`
- Font: Plain 19px weight 500, `"kern"` feature, `leading-[0]`
- Focus: `outline: transparent solid 2px`
- Use: Active-state filter controls — larger tap target than the muted badge variant

**Ghost Dark (on dark sections)**
- Background: `rgba(255, 255, 255, 0.12)` — frosted white
- Text: `#ffffff`
- Padding: `7px 8px 7px 12px` (asymmetric — icon-right layout)
- Radius: `4px`
- Border: `0px solid #ffffff`
- Font: Plain 16px weight 400, `"case"` feature
- Outline: `#ffffff none 3px`
- Use: Secondary CTAs overlaid on dark editorial sections (`btn--secondary`)

**Thematic Overlay Button**
- Background: `#000000`
- Text: `#ffffff`
- Padding: `7px 0px`
- Radius: `4px`
- Border: `0px solid #ffffff`
- Opacity: `0.3` at rest — heavily muted, appears as a ghost presence over dark imagery
- Font: Plain 16px weight 400, `"case"` feature
- Use: Thematic slide controls within the hero carousel (`thematic__btn`)

### Cards

**Project / Work Card**
- Background: `#ffffff`
- Border: `1px solid rgb(51, 51, 51)` — top edge only (`border-width: 1px 0px 0px`)
- Radius: `0px` — sharp rectangular, no rounding on content cards
- Shadow: none
- Layout: full-width image above, title + caption below the top rule
- Title: Plain 19px weight 500, `#1a1a1a`, `"kern"`
- Caption: Plain 13px weight 400, `#767676`, `"case"`
- Padding: 8px top, 24px bottom (estimated from spacing scale)
- Hover: no visual card state — the image or link itself registers the interaction

**Editorial Dark Panel**
- Background: `#222222`
- Text: `#ffffff` (heading), `#ffffff` at reduced opacity (body)
- No border, no radius, no shadow
- Headline: Plain 52px weight 400, `"case"`, letter-spacing `-1.04px`, line-height 1.05
- Body: Plain 19px weight 400, `"kern"`, line-height 1.32
- Full-width section break — extends edge-to-edge
- Padding: 64–96px vertical (from spacing scale)

### Inputs & Forms

**Newsletter Email Input**
- Background: `#222222` (dark section context)
- Text: `#ffffff`
- Border: bottom-only — `0px none #ffffff` at default, transitions on focus
- Radius: `0px` — completely flat
- Padding: `0px` — flush input, no internal padding
- Focus color: `#1a1a1a` — text shifts to near-black on focus (surface/context change)
- Focus outline: `transparent solid 2px`
- Placeholder: `#8c8c8c`

**Form Container Bottom Rule**
- Border: bottom `1px solid #8c8c8c` — separates form fields on the light canvas
- The only visible form structure; no box, no panel background

### Navigation

**Primary Horizontal Nav**
- Background: `#ffffff` (sticky white strip)
- Wordmark: Plain logotype (`Pentagram`) left-aligned — SVG, 103×20px
- Links: Plain 19px weight 500, `#1a1a1a`, `"kern"`, no underline
- Link hover: no explicit hover state extracted — likely a subtle opacity shift
- Right chrome: Work, About, News, Contact, Archive (text links) + Search icon
- No radius, no border, no shadow on the nav container itself
- Position: sticky top, no backdrop blur — clean white strip

**Carousel Caption (Hero)**
- Text: `#ffffff` (on dark imagery)
- Position: lower-left of hero image
- Size: Plain 13px weight 400, `"case"`
- Project title line: underline default (`text-decoration: underline 1px`), removes on hover
- Two-line treatment: project name (larger) + description (smaller, muted)

### Links

**Dark-Surface Link**
- Color: `#1a1a1a`
- Decoration: none at default
- Hover: none (decoration removed)
- Weight: 500 for navigation, 400 for inline

**Light-Surface White Link**
- Color: `#ffffff`
- Decoration: `underline 1px` — always underlined as primary affordance on dark
- Hover: underline removed — a subtle inversion of convention

**Muted / Meta Link**
- Color: `#8c8c8c`
- Decoration: none
- Weight: 400
- Use: Archive entries, footnote links, de-emphasized navigation

## Do's and Don'ts

**Do:**
- Use Plain weight 400 for all display and heading text — never weight 700 or even 600 at large sizes
- Enable `font-feature-settings: "case"` on all text at 16px and above; switch to `"kern"` at 19px body and below
- Apply negative letter-spacing proportionally: `-1.04px` at 52px, `-0.32px` at 32px, none below 20px
- Use `#1a1a1a` for primary text — not `#000000`, the fractional warmth is intentional
- Restrict border-radius to `4px` for interactive chrome elements only; use `0px` on all content surfaces
- Apply the top-rule only (`border-top: 1px solid rgb(51,51,51)`) for card separation — never full-border cards
- Use the dark `#222222` section as the sole surface contrast — make the transition a direct collision, no margin buffer
- Let photography provide all chromatic interest — never introduce a non-neutral accent color in UI chrome
- Underline white links on dark surfaces as the primary affordance; remove underline on hover (inverse of convention)

**Don't:**
- Don't introduce any brand accent color — no blue CTA, no warm highlight, no hover colour. The system is monochrome.
- Don't add box shadows to cards, buttons, panels, or navigation — the shadow array is empty by design
- Don't round content card corners — `0px` radius on all project imagery and editorial containers
- Don't use the pill (`9999px`) radius for anything other than carousel navigation dots
- Don't introduce a secondary typeface — Plain handles every typographic register without backup
- Don't set body line-height above 1.32 — this is not a generous, literary reading system; it is an editorial one
- Don't use positive letter-spacing on display text — all tracking at 20px+ is negative or neutral
- Don't use the `"case"` and `"kern"` features simultaneously on the same text element — they govern different size tiers
- Don't pad the hero image — full-bleed means full-bleed, edge-to-edge with zero border-radius
- Don't use `rgba(0,0,0,0.07)` tint for anything other than interactive filter/chip states — it is not a general card background

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Small Mobile | <470px | Single column, hero image compresses, nav collapses, 52px → ~28px heading |
| Mobile | 470–569px | Single column, carousel dot nav visible, minimal chrome |
| Mobile Wide | 570–598px | Slightly wider single column |
| Tablet Small | 600–665px | 2-column work grid begins, nav expands |
| Tablet | 666–754px | Standard 2-column grid |
| Tablet Large | 755–799px | Wider 2-column or early 3-column |
| Desktop Small | 800–979px | 3-column work grid, full nav visible |
| Desktop | 980–1039px | Full layout, hero at larger scale |
| Desktop Wide | 1040–1599px | Standard desktop — full hero, 3–4 column grid, all nav links |
| Large Desktop | 1600–1727px | Maximum grid columns, hero photography at cinematic scale |
| Ultra Wide | 1728–1799px | Extended content areas |
| Cinema | 1800–1920px+ | Maximum breakpoint — hero imagery at full quality, widest grid |

Pentagram ships an unusually dense breakpoint list (17 breakpoints) — reflecting the pixel-precision demanded by full-bleed hero imagery and multi-column project grids across a broad range of screen widths.

### Touch Targets
- Navigation links: 19px text with adequate surrounding padding — estimated 44px tap height
- Carousel dots: 18×18px visual but should have 44px touch area via padding
- Filter chips: 4–6px padding — compact; mobile variants should expand to 44px minimum

### Collapsing Strategy
- **Navigation**: Horizontal text links collapse to hamburger or icon strip on mobile
- **Hero carousel**: Maintains full-bleed at all breakpoints; caption text reduces in size
- **Work grid**: 4-column → 3-column → 2-column → 1-column across breakpoints
- **Display heading**: 52px desktop → approximately 28–32px on mobile, weight 400 maintained throughout
- **Dark editorial panel**: Maintains full-width at all breakpoints; internal text scales down
- **Section spacing**: 96px → 48px → 24px at mobile — preserves editorial rhythm proportionally
- **Carousel dots**: Remain visible at all sizes; dot count and positioning adjust

### Image Behavior
- Hero imagery: full-bleed, `object-fit: cover`, no radius at any breakpoint
- Work cards: images maintain aspect ratio within column width
- No art direction swaps — same images serve all breakpoints
- Caption overlays on dark sections maintain legibility through photography composition (dark backgrounds in frame), not CSS scrims

---

## Agent Prompt Guide

### Quick Reference
- Primary CTA: there is none — the system has no chromatic accent button
- Page Background: `#ffffff`
- Primary Text: `#1a1a1a`
- Secondary Text: `#767676`
- Tertiary / Placeholder: `#8c8c8c`
- Dark Section Background: `#222222`
- Dark Section Text: `#ffffff`
- Filter Chip Background: `rgba(0, 0, 0, 0.07)`
- Ghost Button (dark): `rgba(255, 255, 255, 0.12)` background
- Border (top-rule card): `1px solid rgb(51, 51, 51)` — top only
- All shadows: none

### Example Component Prompts
- "Create a hero section with a full-bleed editorial photograph — no border-radius, no padding, edge-to-edge. Overlay a caption at the lower-left: project name in Plain 19px weight 500, `#ffffff`, `text-decoration: underline 1px` that removes on hover; tagline below in Plain 13px weight 400, `#ffffff`, `"case"` feature. At lower-right, 8–12 carousel navigation dots: 18×18px circles, `9999px` radius, white fill, `opacity: 0.5` at rest, `1.0` active."
- "Design a project card for a work grid: zero border-radius, no shadow, no visible box. Top edge rule: `border-top: 1px solid rgb(51, 51, 51)`. Full-width image above. Below the rule: project title in Plain 19px weight 500, `#1a1a1a`, `font-feature-settings: 'kern'`, followed by discipline label in Plain 13px weight 400, `#767676`, `font-feature-settings: 'case'`. Padding: 8px top, 24px bottom."
- "Build a dark editorial section — full-width `#222222` background, 96px vertical padding. Headline: Plain 52px weight 400, `#ffffff`, `line-height: 1.05`, `letter-spacing: -1.04px`, `font-feature-settings: 'case'`. Body paragraph below: Plain 19px weight 400, `#ffffff`, `line-height: 1.32`, `font-feature-settings: 'kern'`. No decorative elements, no dividers, no accent color."
- "Create a discipline filter row — a horizontal list of filter chips. Each chip: background `rgba(0, 0, 0, 0.07)`, text `rgba(0, 0, 0, 0.56)`, Plain 13px weight 400 `'case'`, padding `4px 8px`, `border-radius: 4px`, no border, no shadow. Active chip upgrades to: text `#1a1a1a`, weight 500, padding `6px 8px`, same surface. Chips render at 19px in the dropdown display view with `line-height: 0`."
- "Design a top navigation bar — white background `#ffffff`, no border, no shadow. Left: Pentagram wordmark SVG in `#1a1a1a`. Right: text links (Work, About, News, Contact, Archive) in Plain 19px weight 500, `#1a1a1a`, `font-feature-settings: 'kern'`, no underline, spaced with 24–32px gaps. Final item: search icon (no label). Sticky positioning, full viewport width."

### Iteration Guide
1. Start with the surface, not the component — `#ffffff` or `#222222` determines everything else; the two surfaces never blur into intermediate grays
2. Apply `font-feature-settings: "case"` at 16px and above; switch to `"kern"` below — this determines the typographic register of the element
3. Negative letter-spacing is mandatory on display text: `-1.04px` at 52px, `-0.32px` at 32px. Do not leave tracking at 0 for headings.
4. Weight 400 for display, weight 500 for navigation and card titles — nothing heavier appears in this system
5. The only radius allowed on content is `0px`. Apply `4px` only to filter chips, modal overlays, and button chrome. Apply `9999px` only to carousel dots.
6. If you are tempted to add a colored accent — a blue link, a red hover, an orange badge — resist it. Find the achromatic solution.
7. Top-rule only on cards (`border-top: 1px solid rgb(51,51,51)`) — never a full card box border
8. Underline white links on dark surfaces; remove it on hover. On light surfaces, no underline by default.
9. Full-bleed imagery means zero padding, zero margin, zero border-radius on the image container — it touches all four edges
10. When in doubt, remove — this system communicates through subtraction, not addition
