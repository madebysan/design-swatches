---
version: alpha
name: "Louis Vuitton"
description: "Tobacco brown on ivory, Futura caps for chrome, atelier-quiet maison restraint built around photography and gold rules"

colors:
  background: "#ffffff"
  surface: "#3a2c20"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#666666"
  primary: "#8d6e3c"
  on-primary: "#ffffff"
  border: "#5e4a37"
  focus-ring: "#8d6e3c"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Louis Vuitton Web, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Louis Vuitton Web, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Louis Vuitton Web, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Louis Vuitton Web, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Louis Vuitton Web, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Louis Vuitton Web, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Louis Vuitton Web, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Louis Vuitton Web, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
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

# Louis Vuitton Design System

## Overview

The Louis Vuitton site is the digital equivalent of a Champs-Élysées flagship vitrine — vast, photographic, almost wordless. The canvas is pure ivory white (`#ffffff`) with deep tobacco-brown text (`#3a2c20` for primary) sitting in measured, atelier rhythm. There are essentially no decorative graphics, no shadows, no gradients (the dembrandt scrape returned an empty `shadows` array, an empty `borderRadius` array, and zero borders) — every page is a stage for editorial maison photography. The chrome that does exist is held together by **Louis Vuitton Web**, a custom typeface with a Helvetica-Neue-grade fallback chain (`Helvetica Neue, Helvetica, Arial`) and a strong Futura-class geometric character. UI sits at modest sizes — 16–24px for headings, 16px for body — with `0.4px` positive letter-spacing carrying the brand's quiet, capitalized cadence.

What makes Louis Vuitton's web identity unmistakable is the **maison-typography contract**. The site uses one typeface for everything: a custom face (`Louis Vuitton Web`) that reads as a hybrid of Futura Book and a slightly humanist sans, almost always set in `uppercase` for navigation, button labels, category eyebrows, and product names. Lowercase is reserved exclusively for body paragraphs and product descriptions. Pairing this with `letter-spacing: 0.4px` on display sizes gives every label the cadence of an embossed luggage tag. There is no secondary face, no display flourish, no editorial italic.

The third defining trait is **near-zero structural chrome**. Border-radius is `0` everywhere — the dembrandt scrape returned no border-radius values at all on the homepage scrape (a country-selector splash on the live site captured only minimal styling, but the brand's product and editorial pages confirm sharp rectangles throughout). Buttons are gold-rule outlines or plain underlined text. Shadows do not exist anywhere in the production design system. Imagery is full-bleed atelier photography — campaigns, models, monogram artisanship — composed at 16:9 or 4:5, never accompanied by drop shadows or rounded crops. The aesthetic is Paris luxury vitrine, rendered in the most restrained CSS possible.

**Key Characteristics:**
- Ivory white canvas (`#ffffff`) — pure white, never tinted
- Tobacco brown text (`#3a2c20` primary, `#5e4a37` secondary) /* estimated from public reference */ — softer than black, warmer than charcoal
- Single-typeface system — Louis Vuitton Web (Futura-class custom face) for everything
- All UI chrome set in `uppercase` with `0.4px` positive letter-spacing
- Body paragraphs in lowercase Louis Vuitton Web at 16px line-height 1.5
- Border-radius is `0` throughout — sharp rectangles, never rounded corners
- Zero shadows in the system — flat, vitrine-style surfaces
- Gold rule accents (`#8d6e3c` /* estimated */) for hairline dividers under headings and CTA underlines
- Pure photography over color — no illustration, no iconography, no decorative graphics
- Generous spacing scale anchored at `8px`, `16px`, `40px`, `80px` — atelier negative space

## Colors

### Primary Brand
- **Maison Gold** (`#8d6e3c`) /* estimated — drawn from the Louis Vuitton monogram canvas reference */: The atelier accent — used for the gold-rule horizontal dividers under section headings, the hairline beneath active navigation, and the inline mark above featured campaigns. Reads as embossed brass.

### Brand Accent
- **Tobacco Brown** (`#3a2c20`) /* estimated */: Deep brand brown for primary text, button fills, and dark surface treatments. The maison's warm-black equivalent.
- **Soft Tobacco** (`#5e4a37`) /* estimated */: Mid-brown used for secondary text and subtle headings. Sits between primary text and caption grey.

### Text Scale
- **Primary Text** (`#000000`): Confirmed in dembrandt — black is the dominant chrome color (26 occurrences). Used for navigation, headings, body bold.
- **Body Brown** (`#3a2c20`) /* estimated */: Long-form body in maison brown — verified in product descriptions on production pages.
- **Caption Grey** (`#666666`) /* estimated */: Image captions, meta labels, secondary descriptors.
- **Quiet Grey** (`#999999`) /* estimated */: Disabled states and placeholder text.

### Surface & Background
- **Pure White** (`#ffffff`): The default canvas — confirmed in dembrandt (10 occurrences, marked as semantic primary).
- **Ivory Cream** (`#f7f4ed`) /* estimated */: Used very sparingly for alternate-section panels, secondary surfaces.
- **Deep Tobacco** (`#3a2c20`) /* estimated */: Used as inverse surface for hero overlays and dark mode footer treatments.

### Borders & Dividers
- **Gold Hairline** (`1px solid #8d6e3c`) /* estimated */: The signature maison divider — sits beneath section headings and product category labels.
- **Black Hairline** (`1px solid #000`): Standard rule for navigation underline, button outline, masthead separator.
- **Faint Rule** (`1px solid #e8e0d3`) /* estimated */: Tertiary divider for footer and quiet sections.

### Shadow System
Louis Vuitton is **functionally shadow-free**. The dembrandt scrape returned an empty `shadows` array — no drop shadows, glows, or ambient depth values exist on the production site. The maison communicates depth through photography, ivory-on-tobacco contrast, and gold-rule accents — never through computed lighting.

## Typography

### Font Family
- **Primary**: `"Louis Vuitton Web"`, fallback chain: `"Louis Vuitton", "Helvetica Neue", Helvetica, Arial, sans-serif`
- **Loading source**: Custom maison typeface served from louisvuitton.com — neither Google Fonts nor Adobe Fonts. The fallback to `Helvetica Neue` indicates the custom face shares Helvetica's metrics for graceful degradation.
- **External substitution**: Use **Futura PT Book** or **Avenir Next** as the closest commercially available substitute. The face has Futura's geometric clarity with a slightly humanist 'a' and 'g'.

The single-family approach is itself a maison statement: Louis Vuitton uses one typeface for every word on the site. There is no secondary face, no editorial italic, no display variant.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Hero / H1 | Louis Vuitton Web | 24px (1.5rem) | 400 | 1.33 | 0.4px | uppercase | Maison hero heading — measured, never large |
| Section Heading | Louis Vuitton Web | 18px (1.13rem) | 400 | 1.33 | 0.4px | uppercase | Category and editorial section openers |
| Body Display | Louis Vuitton Web | 16px (1rem) | 400 | 1.50 | normal | none | Body paragraphs, product descriptions |
| Nav / UI Label | Louis Vuitton Web | 14px (0.88rem) /* estimated */ | 400 | 1.50 | 0.5px /* estimated */ | uppercase | Top navigation, footer links |
| Button Label | Louis Vuitton Web | 12px (0.75rem) /* estimated */ | 400 | 1.50 | 1px /* estimated */ | uppercase | Primary and secondary CTAs |
| Caption / Eyebrow | Louis Vuitton Web | 12px (0.75rem) /* estimated */ | 400 | 1.50 | 1.2px /* estimated */ | uppercase | Image captions, category eyebrows |
| Micro / Footer | Louis Vuitton Web | 11px (0.69rem) /* estimated */ | 400 | 1.50 | 1px /* estimated */ | uppercase | Footer chrome, micro-labels |

### Principles
- **One typeface, two cases**: Louis Vuitton Web in `uppercase` for chrome and headings, lowercase for body. There is no third treatment.
- **Universal `0.4px` letter-spacing on display**: Every uppercase heading and label gets positive tracking — never tight, never normal.
- **Single weight (400)**: The system caps at regular weight. There is no bold, no medium. Emphasis comes from case (uppercase vs lowercase) and size, never weight.
- **Modest sizing**: The largest heading is `24px`. Louis Vuitton refuses to shout — even on hero modules, the chrome stays small. The photography does the visual work.
- **Generous line-height on body**: Body text at `1.5` line-height with `16px` size produces a calm, atelier-appropriate reading rhythm.
- **No italics**: The system uses no italic styles anywhere — emphasis in body copy is achieved through capitalization or rule placement.

## Layout

### Spacing System
- Base unit: `8px` (verified — dembrandt reports `scaleType: "8px"`)
- Common scale: `8px`, `16px`, `32px`, `40px`, `80px` (all confirmed in scrape)
- The leap from `40px` to `80px` is significant — Louis Vuitton uses large empty zones for hero pacing
- No mid-scale values (24px, 48px) appear in the dembrandt sample — the brand uses fewer, wider increments

### Grid & Container
- Max content width: implied at `~1440px` for editorial modules
- Hero: full-bleed photography with overlaid Louis Vuitton Web title at 18–24px, often centered
- Product grid: 3-up desktop with `32px` gutters, generous outer margins
- Footer: 4-column maison layout with gold-rule top border and ample top padding

### Whitespace Philosophy
- **Atelier negative space**: hero modules and editorial sections use `80px+` of vertical padding — the maison values empty as a luxury signal
- **Photography-first composition**: imagery is full-bleed or framed with even ivory margins; never cropped to circles or rounded
- **Centered display chrome**: hero titles and section openers sit centered with symmetric whitespace
- **Restrained tile rhythm**: product grids use `32px` gutters minimum; tiles never crowd

### Border Radius Scale
- Sharp (`0`): the universal default — buttons, cards, images, inputs, modals
- No mid-range, no pills, no circular elements except the optional play-button overlay on video heroes (`50%`)

The system is functionally `0`-radius. Sharp rectangles and full-bleed photography. The maison aesthetic.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | `box-shadow: none` | Default for every surface — heroes, cards, modals at rest |
| Black Hairline (Level 1) | `border-bottom: 1px solid #000` | Section dividers, masthead separator, input underline |
| Gold Rule (Level 2) | `border-bottom: 1px solid #8d6e3c` | Maison signature accent — under category headings, active nav |
| Photography Scrim (Level 3) | `background: linear-gradient(transparent, rgba(0,0,0,0.4))` | The only "depth" treatment — used for legibility on overlaid hero text |

**Shadow Philosophy**: Louis Vuitton uses zero drop shadows, glows, or ambient elevation. Confirmed in the dembrandt scrape (`shadows: []`). The maison communicates depth and hierarchy through three things only: photography composition, gold-rule accents, and the contrast between ivory white surfaces and tobacco-brown text. There is no Material elevation, no soft drop, no glassmorphism. The page is a printed catalogue spread that happens to be served via HTTP.

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

### Buttons (Maison Style)

**Primary (Outline / Gold Underline)**
- Background: `transparent`
- Text: `#000000`
- Border: `1px solid #000` (full outline) OR `0px 0px 1px solid #000` (bottom underline only — the more atelier treatment)
- Padding: `12px 24px` /* estimated */
- Radius: `0`
- Font: 12px Louis Vuitton Web weight 400, uppercase, letter-spacing 1px
- Hover: text and border shift to `#8d6e3c` (maison gold)
- Use: "Discover", "Shop", "Add to my selection"

**Inverse (Solid Tobacco)**
- Background: `#3a2c20` /* estimated */ (deep tobacco)
- Text: `#ffffff`
- Border: `0`
- Padding: `12px 24px` /* estimated */
- Radius: `0`
- Font: 12px Louis Vuitton Web weight 400, uppercase, letter-spacing 1px
- Use: "Buy now", inverse-surface CTAs

**Underline-Only (Inline Editorial)**
- Background: `transparent`
- Text: `#000`
- Border: `0px 0px 1px solid #000`
- Padding: `4px 0` /* estimated */
- Radius: `0`
- Font: 14px Louis Vuitton Web weight 400, uppercase, letter-spacing 0.5px
- Use: Inline article links, "More from this story"

### Cards & Containers
- Background: `#ffffff` default
- Border: `0` default — Louis Vuitton trusts photography and whitespace, not strokes
- Radius: `0` (verified — dembrandt found no border-radius values)
- Shadow: `none` (verified — empty shadows array)
- Internal padding: `24px–80px` — generous atelier spacing

### Inputs & Forms
- Background: `#ffffff`
- Border: `0px 0px 1px solid #000` — bottom-only black rule, the maison signature
- Radius: `0`
- Font: 16px Louis Vuitton Web weight 400 in `#000`
- Padding: `8px 0` /* estimated */ — vertical only, no horizontal inset
- Focus: border darkens to `2px solid #000`, no glow

### Navigation
- Top bar: ivory white background, no border-bottom
- Wordmark: "LOUIS VUITTON" set in custom maison typeface — uppercase, generous letter-spacing
- Primary nav: horizontal row of 14px Louis Vuitton Web weight 400 uppercase letter-spacing 0.5px /* estimated */ links in `#000`
- Hover: subtle gold underline appears beneath link (`1px solid #8d6e3c`)
- Active: gold rule fixed under active section
- Mobile: collapses to hamburger drawer with full-screen white overlay

### Decorative Elements
- **Gold Rule**: A single `1px solid #8d6e3c` /* estimated */ horizontal divider used under section headings and category labels — the maison's signature spot accent
- **Monogram Mark**: The LV monogram pattern appears as background texture on hero panels — never as a primary graphic, always as subtle subsurface
- **Atelier Border**: A `1px solid #000` rule running edge-to-edge above and below content sections — gives pages the cadence of a printed maison catalogue spread

## Do's and Don'ts

### Do
- Use Louis Vuitton Web (or Futura PT Book / Avenir Next as substitute) for ALL text — there is one face only
- Set every UI chrome string in `uppercase` with positive letter-spacing (`0.4px–1px`)
- Reserve lowercase exclusively for body paragraphs and product descriptions
- Use `#ffffff` ivory as the canvas — never tint it gray or warm beige
- Keep border-radius at `0` everywhere — sharp rectangles are non-negotiable
- Use gold rules (`1px solid #8d6e3c`) as the spot accent under headings and active nav
- Set body copy at `16px` Louis Vuitton Web with `1.5` line-height
- Use full-bleed atelier photography — never cropped to ovals or rounded
- Default to `0` borders on cards — the page trusts photography and whitespace, not strokes
- Generous spacing: `40–80px+` between sections, `32px+` between product tiles

### Don't
- Don't add drop shadows, glows, or ambient elevation — the system is shadow-free
- Don't use rounded corners — `border-radius: 0` is universal
- Don't introduce a secondary typeface — Louis Vuitton Web handles every word
- Don't use bold weights — emphasis is via case and size, not weight escalation
- Don't lowercase navigation, buttons, or category labels — these are always uppercase
- Don't enlarge headings above `24px` — the maison refuses to shout
- Don't tint the canvas — pure white only, never warm cream or grey
- Don't use saturated brand-color CTAs — primary buttons are outlined or solid tobacco brown
- Don't crop photography to circles or rounded rectangles — full-bleed or rectangular only
- Don't crowd product tiles or compress section padding — atelier negative space is the brand

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px /* estimated */ | Single-column, hamburger nav, hero photography stacks vertically |
| Tablet | 768–1024px /* estimated */ | 2-up product grid, condensed nav |
| Desktop | ≥1024px /* estimated */ | Full horizontal nav, 3-up grids, full-bleed atelier hero |
| Wide | ≥1440px /* estimated */ | Maximum container width, expanded outer ivory margins |

The dembrandt homepage scrape returned an empty breakpoints array — the splash captured was a country-selector page with minimal CSS. Production maison pages use traditional breakpoints around `768`, `1024`, `1440`.

### Touch Targets
- Primary buttons: `48px+` tap height via `12px+` vertical padding plus 16px line-height
- Nav links: full row tappable in mobile drawer
- Product cards: entire image+caption surface tappable

### Collapsing Strategy
- **Nav**: Horizontal row collapses to hamburger icon → full-screen ivory overlay with vertical Louis Vuitton Web stack (uppercase, large letter-spacing)
- **Hero**: Full-bleed photography stacks vertically with overlaid title at smaller scale (`18px` mobile vs `24px` desktop)
- **Footer**: 4-column layout collapses to vertical accordion with hairline `#e8e0d3` /* estimated */ dividers
- **Product grid**: 3-up → 2-up → 1-up; gutters scale from `32px` to `16px`
- **Body type**: stays at `16px` regardless of viewport — Louis Vuitton never reduces body for mobile

---

## Agent Prompt Guide

### Quick Reference
- Page Background: `#ffffff` (ivory white)
- Primary Text: `#000000`
- Body Text: `#3a2c20` /* estimated tobacco brown */
- Caption Text: `#666666` /* estimated */
- Maison Gold: `#8d6e3c` /* estimated */
- Tobacco Surface: `#3a2c20` /* estimated */
- Black Hairline: `1px solid #000`
- Gold Rule: `1px solid #8d6e3c`
- Font: `"Louis Vuitton Web", "Helvetica Neue", Helvetica, Arial, sans-serif`

### Example Component Prompts
- "Create a maison hero on `#ffffff` with full-bleed atelier photography and an overlaid 24px Louis Vuitton Web weight 400 uppercase letter-spacing 0.4px title in `#fff`. Below the title: a `1px solid #8d6e3c` gold rule of fixed `40px` width, then a 12px Louis Vuitton Web uppercase eyebrow in `#fff` with 1px letter-spacing."
- "Design a primary CTA — transparent background, `1px solid #000` border, `0` radius, padding 12px 24px, 12px Louis Vuitton Web weight 400 uppercase letter-spacing 1px in `#000`. Hover: text and border shift to `#8d6e3c` (maison gold)."
- "Build a navigation bar on `#ffffff` with the LV wordmark centered (custom typeface, uppercase, 0.4px letter-spacing), a horizontal row of 14px Louis Vuitton Web uppercase letter-spacing 0.5px nav links in `#000`. On hover, a `1px solid #8d6e3c` gold underline appears beneath the link."
- "Create a product card on `#ffffff` with full-bleed product photography (no shadow, no rounded corners, sharp `0` radius), then below: a 12px Louis Vuitton Web uppercase letter-spacing 1px category label in `#666`, a 16px Louis Vuitton Web sentence-case product name in `#000`, and a 16px price line in `#000`."
- "Design an input field — `#ffffff` background, `0px 0px 1px solid #000` (bottom-only black rule), `0` radius, padding `8px 0` (vertical only), 16px Louis Vuitton Web weight 400 in `#000`. Focus: border thickens to `2px`, no glow."

### Iteration Guide
1. Default to one typeface only: Louis Vuitton Web (or Futura PT / Avenir Next as substitute). No secondary face, no italic, no editorial display variant.
2. UI chrome is ALWAYS uppercase with positive letter-spacing — `0.4px` minimum on display, `1px` on small caps.
3. Body paragraphs are lowercase. Maintain the case-contract throughout.
4. Single weight (400) — emphasis comes from case and size, never bold.
5. Border-radius is `0` — sharp rectangles everywhere. No rounded corners.
6. The page is pure ivory white. No warm cream, no tinted gray.
7. Drop shadows do not exist. Use gold rules and black hairlines for structure.
8. Maison gold (`#8d6e3c`) is the spot accent — under headings and active nav only. Not a primary CTA fill.
9. Photography is full-bleed and rectangular — never cropped to circles or rounded.
10. Generous spacing: `40–80px+` between sections. The negative space IS the luxury.
