---
version: alpha
name: Vodafone
description: Corporate broadcast presence — single fierce Vodafone Red, monumental uppercase 800-weight display up to 144px, dual-tier button system (2px rectangles vs 60px pills), red band dividers, charcoal institutional panels.

colors:
  # Canvas + ink
  background: "#ffffff"
  surface: "#ffffff"
  surface-neutral: "#f2f2f2"
  surface-dark: "#25282b"
  ink: "#25282b"
  ink-inverted: "#ffffff"

  # Brand red — non-negotiable signature
  primary: "#e60000"
  primary-deep: "#ac1811"

  # Accent
  link-blue: "#3860be"

  # On-color
  on-primary: "#ffffff"
  on-surface-dark: "#ffffff"

  # Text hierarchy
  on-background: "#25282b"
  text-secondary: "#7e7e7e"
  text-form: "#333333"
  text-disabled: "#bebebe"

  # Borders + dividers
  border: "#25282b"
  border-subtle: "#dcdcdc"

  # Glass + opacity overlays (opaque approximations)
  glass-white: "#3a3a3a"      # was rgba(255,255,255,.1) over dark hero
  glass-translucent: "#cccccc" # was rgba(0,0,0,.05) — flattened over white
  divider-white: "#5e6164"     # was rgba(255,255,255,.25) over #25282b
  pill-white-80: "#fafafa"     # was rgba(255,255,255,.8) — flattened over white

typography:
  display-xl:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 144px
    fontWeight: 800
    lineHeight: 0.79
    letterSpacing: -1px
  display-l:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 126px
    fontWeight: 800
    lineHeight: 0.90
    letterSpacing: -1px
  display-m:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 90px
    fontWeight: 800
    lineHeight: 0.93
    letterSpacing: 0px
  display-impact:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 70px
    fontWeight: 800
    lineHeight: 1.17
    letterSpacing: -1px
  h1-light:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: 0px
  h1-bold:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.00
    letterSpacing: -1px
  h2-light:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.10
    letterSpacing: 0px
  h2-bold:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: 0px
  h3-bold:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0px
  h4-bold:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0px
  h4-light:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.42
    letterSpacing: 0px
  h5-bold:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 0px
  lead-body:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  body-large:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0px
  body-bold:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.56
    letterSpacing: 0px
  body:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0px
  label-uppercase:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 800
    lineHeight: 1.50
    letterSpacing: 0px
  eyebrow:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0px
  tag-pill:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.50
    letterSpacing: 0px
  caption:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 2.00
    letterSpacing: 0px
  micro-label:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0px
  button-primary:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 14.4px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0.144px
  button-compact:
    fontFamily: "Vodafone, Helvetica Neue, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0.12px

spacing:
  micro: 1px
  2xs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 38px
  5xl: 64px
  6xl: 96px

rounded:
  none: 0px
  micro: 1px
  tight: 2px
  card: 6px
  glass-pill: 24px
  badge-pill: 32px
  cta-pill: 60px
  pill: 9999px

components:
  # Primary red rectangle — utility / form CTA
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-primary}"
    rounded: "{rounded.tight}"
    padding: 12px 10px
    borderColor: "{colors.primary}"

  # Primary red pill — editorial content CTA
  button-primary-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-primary}"
    rounded: "{rounded.cta-pill}"
    padding: 16px 16px

  # Ghost white rectangle — secondary form
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-form}"
    typography: "{typography.button-primary}"
    rounded: "{rounded.tight}"
    padding: 12px 10px
    borderColor: "{colors.text-form}"

  # Glass pill — sits on dark hero
  button-glass-pill:
    backgroundColor: "{colors.glass-white}"
    textColor: "{colors.on-surface-dark}"
    typography: "{typography.button-primary}"
    rounded: "{rounded.glass-pill}"
    padding: 8px 16px

  # Content ghost pill — low-emphasis
  button-content-ghost:
    backgroundColor: "{colors.glass-translucent}"
    textColor: "{colors.primary}"
    typography: "{typography.button-primary}"
    rounded: "{rounded.cta-pill}"
    padding: 15px

  # Icon control button — circular
  button-icon:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    size: 40px

  # News / editorial card
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.card}"
    padding: 16px

  # Asymmetric corner card — featured
  card-asymmetric:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.card}"
    padding: 16px

  # Circular portrait
  portrait:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.pill}"
    size: 100px

  # Input
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-form}"
    typography: "{typography.body}"
    rounded: "{rounded.tight}"
    padding: 12px 10px
    borderColor: "{colors.text-form}"
  input-error:
    backgroundColor: "{colors.background}"
    borderColor: "{colors.primary}"

  # Outlined red pill — article metadata tag
  tag-outlined:
    backgroundColor: "{colors.pill-white-80}"
    textColor: "{colors.ink}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.tight}"
    padding: 6px
    borderColor: "{colors.primary}"

  # Filled neutral pill
  tag-neutral:
    backgroundColor: "{colors.surface-neutral}"
    textColor: "{colors.ink}"
    typography: "{typography.tag-pill}"
    rounded: "{rounded.badge-pill}"
    padding: 4px 12px

  # Top nav
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 16px 32px

  # Red divider band — chapter break
  divider-band:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: 64px 0px

  # Share ticker / data panel
  panel-data:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-surface-dark}"
    typography: "{typography.h1-bold}"
    padding: 32px

  # Footer
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-surface-dark}"
    typography: "{typography.body}"
    padding: 64px 32px
    borderColor: "{colors.divider-white}"
---

# Vodafone Design System

## Overview

Vodafone's corporate web system carries the confident, broadcast-scale presence of a global telecom brand — built around a single, fiercely-owned brand red and a restrained, editorial layout that lets imagery and type carry the emotional weight. Every page opens the same way: a cinematic dark hero image behind a towering, tight-tracked uppercase display headline ("EVERYONE. CONNECTED.", "INVESTORS", "OUR BUSINESS") followed by a deep red full-width band that acts as a chapter break, then a crisp white editorial grid or a near-black section reserved for institutional content (share ticker, global map, ESG data). The voice is institutional but human: warm documentary photography set against clean neutral surfaces that never compete with content.

The typography system is the signature. A custom Vodafone display face runs all the way up to 144px in heavy 800-weight uppercase with negative tracking, holding that voice consistently across every page template. Body copy sits in a calm 16-18px mid-weight rhythm. This dual scale — monumental at the top, almost quiet at the bottom — creates the "corporate newsroom" feeling: every page reads like the front of a national paper whose masthead happens to be red.

Surface treatment is disciplined: a three-surface pass of white (editorial canvas) → Vodafone red (band dividers, CTA buttons) → near-black charcoal (footer, share-ticker panel, global-impact map). There is almost no decorative shadow, almost no gradient, almost no rounded-corner softness. Edges are small and clinical (`{rounded.tight}` and `{rounded.card}`), buttons operate as a two-tier system — tight 2px rectangles for utility/form actions, and fully-rounded 60px pills for primary content CTAs.

**Key Characteristics:**
- Vodafone Red (`{colors.primary}`) is the single dominant accent — used for CTAs, dividers, band sections, the speech-mark logo, and rotated "IMPACT" wordmark
- Monumental uppercase display type (up to 144px, weight 800, negative letter-spacing) paired with calm body copy
- Universal page rhythm: dark hero → uppercase headline → red band → white editorial → charcoal institutional → footer
- Two-tier button system: tight `{rounded.tight}` rectangles for utility, `{rounded.cta-pill}` pills for editorial CTAs
- Documentary photography over illustration; no stock-icon noise
- Near-absence of shadows and gradients — hierarchy comes from type weight, color blocks, spacing
- Deep charcoal (`{colors.surface-dark}`) reused as footer AND institutional data panel

## Colors

### Primary
- **Vodafone Red** (`{colors.primary}`): The brand's single, non-negotiable signature — primary CTA backgrounds, speech-mark logo, full-bleed band dividers, tag-pill outlines, rotated brand-mark type. Must never be substituted or tinted.

### Secondary & Accent
- **Pure White** (`{colors.background}`): The dominant editorial canvas.
- **Signal Blue** (`{colors.link-blue}`): Reserved for inline text links in resting state.
- **Deep Brand Red Shade** (`{colors.primary-deep}`): Quiet label chips on sustainability — used sparingly for low-prominence tag elements.

### Surface & Background
- **Canvas White** (`{colors.background}`): Primary page and card surface.
- **Light Neutral** (`{colors.surface-neutral}`): Filled neutral pill-badge backgrounds.
- **Charcoal Institutional Panel** (`{colors.surface-dark}`): Same color used for text reused as full-width dark surface for footer, share-ticker, world map.
- **Translucent White Overlay** (`{colors.glass-white}`): Soft glass tint on pill buttons sitting on dark hero imagery.

### Neutrals & Text
- **Charcoal Headline** (`{colors.ink}`): Headings on light surfaces — near-black with a faint cool tint.
- **Secondary Body Grey** (`{colors.text-secondary}`): Body copy, meta text, secondary labels.
- **Form Text Grey** (`{colors.text-form}`): Borders on input-style ghost buttons.
- **Disabled Grey** (`{colors.text-disabled}`): Inactive chip text.
- **Translucent White Divider** (`{colors.divider-white}`): Hairline column dividers on dark institutional panels.

Vodafone's design is intentionally gradient-free. The only tonal variation is the photographic vignette on hero imagery — the image itself, not CSS, provides the tonal ramp.

## Typography

### Font Family
- **Primary**: `Vodafone` (custom corporate sans-serif)
- **Fallback stack**: `Vodafone, "Helvetica Neue", Arial, sans-serif`
- **Icon font**: `icomoon` for pictograph glyphs
- **Rendering**: `font-smoothing: antialiased` across the board

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-xl}`, `{typography.body}`, etc.).

| Token | Use |
|---|---|
| `display-xl` | 144px hero — "EVERYONE. CONNECTED." |
| `display-l` | 126px hero — longer headlines |
| `display-m` | 90px secondary hero / full-bleed section heads |
| `display-impact` | 70px sustainability numeric callouts |
| `h1-light` / `h1-bold` | 48px section headlines (light editorial vs bold institutional) |
| `h2-light` / `h2-bold` | 40px sub-section headers |
| `h3-bold` | 32px card cluster titles |
| `h4-bold` / `h4-light` | 24px card titles vs intro paragraphs |
| `h5-bold` | 20px compact module titles |
| `lead-body` | 20px intro paragraphs |
| `body-large` / `body-bold` | 18px long-form / emphasized |
| `body` | 16px default paragraph |
| `label-uppercase` | 16px uppercase navigational labels |
| `eyebrow` | 14px article date stamps and meta |
| `tag-pill` | 14px badge text in red-outlined pills |
| `caption` | 12px footer meta, legal lines |
| `micro-label` | 12px uppercase tiny labels |
| `button-primary` | 14.4px primary filled button |
| `button-compact` | 12px compact button label |

### Principles
- **Dual-scale drama**: stretches from 144px down to 8.5px without mid-range showing off.
- **Uppercase display, mixed-case body**: largest sizes are uppercase with negative tracking; everything 48px and below is sentence case.
- **Weight spread**: only three real weights — 800 (display), 700 (bold bodies, buttons, tags), 400 (reading body). Light 300 used for editorial 40-48px headlines.
- **No italics, no decorative letterspacing on body**: body is deliberately neutral so display can shout.
- **Rotated brand-mark type**: "IMPACT" set in brand red and rotated 90° on sustainability map — the template's signature typographic flourish.

### Note on Font Substitutes
The Vodafone corporate typeface is proprietary. Substitute with **Inter** at weights 400/600/800, or **Neue Haas Grotesk**. Inter needs letter-spacing reduced by 1-2% at 80px+ to approximate the tight tracking; line-height should be 0.85-0.95 for the uppercase display tier.

## Layout

### Spacing System
The complete scale lives in the `spacing:` token block above. Base unit is 8px. Two values (`{spacing.3xl}` 32px and `{spacing.4xl}` 38px) appear universally — the template's rhythm constants.

### Grid & Container
- Max content width: ~1440px on very large screens; articles and hero modules typically 1200px
- Card grid: 3-up or 4-up at desktop, 2-up at tablet, stacked 1-up at mobile
- Horizontal padding: 32px desktop, 20px tablet, 16px mobile
- Gutters between cards: 24px desktop, 16px mobile
- Institutional panels: always full-bleed at every breakpoint

### Whitespace Philosophy
Vodafone's editorial canvas leans generous — whitespace is a visual palette cleanser between a monumental headline and the card grid or data panel that follows. Sections are separated by tall vertical rhythm (64-96px) plus the occasional red band that acts as both separator and brand signal. Within cards, spacing is tight (12-16px) so the photography can take the stage.

## Elevation & Depth

Vodafone's system is deliberately flat. There is almost no conventional box-shadow.

| Level | Treatment | Use |
|-------|-----------|-----|
| 0 — Surface | No shadow, no border | Default card, default section |
| 1 — Outline | 1px solid border at low-opacity | Ghost buttons, outlined pills |
| 2 — Inset Highlight | `inset 0 0 0 1px` on focus | Pressed / focused controls |
| 3 — Photographic depth | Photography itself carries depth | Hero imagery |
| 4 — Surface shift | Charcoal panel below white canvas | Share ticker / world map / footer |

**Shadow Philosophy**: Vodafone treats drop shadows as a distraction from brand clarity. The dominant "elevation" is a **color surface shift** — switching from white editorial canvas to charcoal institutional panel — rather than a lift-off drop shadow.

### Decorative Depth
- Atmospheric dark hero photography (no CSS overlay needed)
- Rotated vertical "IMPACT" wordmark on sustainability map — illusion of a fourth wall

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `micro` | 1px | Inline text wraps, small badges |
| `tight` | 2px | Primary and secondary rectangle button corners — utility-form look |
| `card` | 6px | News cards, images, input fields |
| `glass-pill` | 24px | Translucent white pills on dark hero imagery |
| `badge-pill` | 32px | Filled neutral pill badges |
| `cta-pill` | 60px | Primary red content CTAs — editorial button look |
| `pill` | 9999px | Icon buttons, circular portraits, ESG pictograms |

## Components

The full component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.panel-data}`).

Vodafone operates a genuine two-tier primary button system. Both tiers are equally primary — the difference is context (form/chrome vs editorial/content), not hierarchy.

### Buttons
- **`button-primary`** — Vodafone Red rectangle, white text, `{rounded.tight}`. For form/utility actions ("Accept All Cookies", "Subscribe").
- **`button-primary-pill`** — Vodafone Red pill, white text, `{rounded.cta-pill}`. For editorial/content CTAs.
- **`button-ghost`** — White surface, charcoal text, `{rounded.tight}`. Secondary form action.
- **`button-glass-pill`** — White-tinted glass on dark hero imagery, `{rounded.glass-pill}`.
- **`button-content-ghost`** — Translucent surface with red text, `{rounded.cta-pill}`. Low-emphasis content CTA.
- **`button-icon`** — Circular 40px white control with charcoal icon. Carousel arrows, video controls.

### Cards & Containers
- **`card`** — White surface, `{rounded.card}`, no shadow. News/editorial tile with 16:9 image on top.
- **`card-asymmetric`** — Featured cards using single-corner radius `0px 6px 0px 0px` echoing the speech-mark logo's curve.
- **`portrait`** — Perfect circle for ESG pictograms and executive portraits.

### Inputs
- **`input`** — White surface, `{colors.text-form}` 1px border, `{rounded.tight}` corners. Error: border shifts to Vodafone Red.

### Tag Pills / Badges
- **`tag-outlined`** — Slightly translucent white, near-black uppercase 12px weight 600, 1px Vodafone Red border, `{rounded.tight}`.
- **`tag-neutral`** — Light Neutral background, charcoal text, `{rounded.badge-pill}` fully pill-shaped.

### Navigation
- **`nav-bar`** — Transparent over hero, solid white on scroll/interior. Vodafone speech-mark logo left, 16px nav links, icomoon utility icons right. Mobile collapses to hamburger at ~768px.

### Red Divider Band
- **`divider-band`** — Full-width Vodafone Red strip between hero and editorial body. No text, no controls — purely visual chapter break. ~40-80px tall.

### Share Ticker / Data Panel
- **`panel-data`** — Charcoal Institutional Panel with 48px weight 800 white numeric display, 14px secondary grey meta. Hairline white-translucent dividers.

### Global Impact Map (Sustainability)
- Charcoal background, dark minimal world-map illustration in slightly lighter grey
- Red circular markers on operational locations
- Vertically-rotated "IMPACT" wordmark in Vodafone Red running along the edge

### Footer
- **`footer`** — Universal Charcoal Institutional Panel. 4-column link grid, "Connect with us" social row, legal/privacy line. Red speech-mark bottom-right.

## Do's and Don'ts

### Do
- Use Vodafone Red (`{colors.primary}`) as the single loudest element — one primary CTA per fold, one red band per editorial break
- Set display headlines in uppercase 800-weight with tight negative tracking; let them run to 90-144px on desktop
- Pair monumental display type with calm 16-18px body copy
- Switch button radius based on context: `{rounded.tight}` for form/utility, `{rounded.cta-pill}` for editorial content
- Let documentary photography breathe at 16:9 or 1:1 on `{rounded.card}` — no decorative borders, no heavy overlays
- Use the red band as full-width chapter divider between every hero and content below
- Anchor every page with charcoal institutional surface — footer always; on investor/sustainability extend to share ticker / global-impact map
- Respect the universal page rhythm

### Don't
- Don't introduce a second brand hue to rival Vodafone Red
- Don't soften rectangle button corners beyond `{rounded.tight}`, and don't shrink pill button corners below `{rounded.cta-pill}` — both shapes are load-bearing
- Don't add drop shadows to cards or buttons — system is intentionally flat
- Don't use gradients on backgrounds, buttons, or text
- Don't mix uppercase tracking on body text — uppercase is reserved for display, labels, micro-labels
- Don't use italics for emphasis — use weight 600/700 instead
- Don't decorate headlines with colored underlines or highlights
- Don't use pure black for text or surfaces — always use Charcoal Headline `{colors.ink}`

---

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | ≤ 600px | Nav collapses to hamburger; hero display ~56-72px; cards stack 1-up |
| Mobile Large | 601-767px | Hero display ~72-90px; cards still stack 1-up |
| Tablet | 768-1023px | Nav re-expands; cards grid 2-up; hero ~90-120px |
| Laptop | 1024-1199px | Full nav; cards 3-up; hero ~120-144px |
| Desktop | 1200-1439px | Standard editorial layout; cards 3-up or 4-up |
| Wide | ≥ 1440px | Content caps at 1440px; outer canvas padding grows |

### Touch Targets
All interactive controls meet a 44×44px minimum on mobile. Icon buttons use 40×40px circular hit areas with 4px invisible padding on touch devices. Primary CTAs land at approximately 48×48px on mobile.

### Collapsing Strategy
- Nav: horizontal links collapse into hamburger at 768px; logo stays left-aligned
- Card grid: 4-up → 3-up at 1200px → 2-up at 768px → 1-up at 600px
- Hero display type: step-reduces 144 → 126 → 90 → 72 → 56px
- Section padding: 96px → 64px → 48px
- Red divider bands: remain full-width; height compresses 80px → 40px
- Institutional panels: multi-column content restacks into single vertical stream; charcoal surface stays edge-to-edge
- Vertically-rotated "IMPACT" wordmark: becomes horizontal label or drops on mobile

### Image Behavior
- Hero imagery: art-directed variant at mobile (tighter crop) vs desktop (wide atmospheric frame)
- Card thumbnails: always 16:9 regardless of viewport; `loading="lazy"` standard
- Circular portraits: 80-120px desktop, 64-80px mobile
- Logo: fixed at 40×40px across breakpoints

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Vodafone Red `{colors.primary}`
- Background: Canvas White `{colors.background}`
- Heading text: Charcoal Headline `{colors.ink}`
- Body text: Secondary Body Grey `{colors.text-secondary}`
- Institutional surface: Charcoal Institutional Panel `{colors.surface-dark}`
- Inline link: Signal Blue `{colors.link-blue}`
- Quiet pill background: Light Neutral `{colors.surface-neutral}`

### Example Component Prompts

- "Create a primary red rectangle button: Vodafone Red (`{colors.primary}`) background, pure white 14.4px weight 700 text, 2px border radius (sharp corners), 12px vertical × 10px horizontal padding. Use for form and utility actions. No shadow, no gradient."
- "Create a primary red pill CTA: Vodafone Red (`{colors.primary}`) background, pure white 14.4px weight 700 text, 60px border radius (fully pill-shaped), 16px uniform padding. Use for editorial content calls-to-action."
- "Design an editorial news card: white background, 6px border radius, 16:9 image at the top, 12px eyebrow row containing a date and a red-outlined uppercase tag pill, then a 24px weight 700 Charcoal title. No shadow — spacing alone separates cards."
- "Build a hero section: dark atmospheric photo as the full-bleed background, monumental uppercase headline at 144px weight 800 with -1px letter-spacing, single Vodafone Red pill CTA beneath it, no overlay gradient."
- "Create a red divider band: full-width strip of Vodafone Red (`{colors.primary}`), 64px tall on desktop and 40px on mobile, no text, no controls — purely a visual chapter break."
- "Design an institutional data panel: full-bleed Charcoal Institutional Panel (`{colors.surface-dark}`) background, large numeric display at 48px weight 800 white with negative letter-spacing, 14px weight 400 grey meta row beneath."
- "Design a global impact map: Charcoal Institutional Panel background, minimal grey world-map illustration, red Vodafone-red circular markers on operational locations, brand word 'IMPACT' set at large display size in brand red and rotated 90° to run vertically along one edge."

### Iteration Guide

1. Focus on ONE component at a time — the system has few moving parts, so refinements compound
2. Reference specific color tokens from this document
3. Use natural language ("sharper corners," "more generous vertical rhythm") alongside specific measurements
4. Radius rule: `{rounded.tight}` for form/utility, `{rounded.cta-pill}` for editorial pills, `{rounded.card}` for cards, `{rounded.pill}` for icon and portrait circles
5. Keep the brand rule absolute: only one Vodafone Red element should dominate any given fold

### Known Gaps

- Form input styles (text fields, dropdowns, toggles) are not exposed on these page templates; specs are inferred from the ghost-button pattern
- The Vodafone corporate typeface is proprietary; Inter with tightened tracking is the closest open substitute
- Animation and transition timings are intentionally not documented — site uses them sparingly
- Share ticker's exact number styling is documented from investor-page screenshot; regional variants may display differently
