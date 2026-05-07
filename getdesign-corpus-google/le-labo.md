---
version: alpha
name: "Le Labo"
description: "Token-first design system reference for Le Labo."

colors:
  background: "#ffffff"
  surface: "#f7f7f5"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#333333"
  primary: "#ffffff"
  on-primary: "#ffffff"
  border: "#f6f8f6"
  focus-ring: "#ffffff"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
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

# Le Labo Design System

## Overview

Le Labo's website is a digital extension of its apothecary storefronts: an evocative, dimly lit laboratory where fragrance is hand-blended on demand. The experience opens not with a hero, but with a **gateway** — a sepia-toned photograph of a vintage roll-top desk crowded with amber bottles, brass instruments, and weathered drawers, the white stencil wordmark "LE LABO / GRASSE NEW YORK®" floating above the scene. Visitors must select a country before they're allowed in. This deliberate friction is the brand's first design statement: nothing here is rushed, mass-market, or assumed.

Once inside, the system collapses to a stark, functional palette: white pages (`#fff`), warm cream surfaces (`#f7f7f5`, `#f6f8f6`), and graphite text (`#333`) — the shade of pencil on lab notebook paper. The defining typeface is **Magda**, a stencil-cut grotesque whose letterforms carry the visible breaks of a literal stencil plate. Magda runs in **bold uppercase** for product names, fragrance numbers, and section markers, set tight against generous white space and faint hairline rules. The secondary face, **Bell Gothic Std**, handles banner titles and CTAs in a quieter, condensed register — a typeface originally drawn for telephone directories, perfectly on-brand for a house that prizes utilitarian beauty.

What separates Le Labo from every other luxury fragrance site is its **refusal of luxury cues**. There are no gold flourishes, no serif-italic headlines, no soft-focus campaign films, no parallax scrolling. The visual language is the apothecary itself: stencil labels, hand-stamped cardboard, brown-amber glass, weighing-scale chrome, ledger paper. Everything looks like it could have been printed with a Heidelberg press in 1932. The website doesn't decorate; it documents.

**Key Characteristics:**
- Magda stencil typeface for all product names and headlines — the visible cuts in the letterforms ARE the brand
- Bell Gothic Std as the utilitarian secondary face — telephone-directory pragmatism, not luxury serif
- Sepia/dark photograph storytelling — vintage apothecary scenes shot in low warm light
- Off-white cream page surfaces (`#f7f7f5`, `#f6f8f6`) — paper, not screen
- All product names typeset in `UPPERCASE BOLD MAGDA` with `0.02em` tracking — feels rubber-stamped
- Zero gradient, zero rounded corners (`border-radius: 0`) — the system is sharp and printed
- Hairline gray dividers (`#e5e5e5`, `#ebebeb`) replace shadows for separation
- No emoji, no icons-as-decoration — small functional UI glyphs only
- Text-driven layouts where the typeface IS the illustration

## Colors

### Primary
- **Lab Paper White** (`#ffffff`): Default page surface — clinical, unornamented. The base canvas of nearly every product and editorial page.
- **Notebook Graphite** (`#333333`): Primary text color. Le Labo specifically uses `#333`, not `#000` — softer than ink, reads like pencil on cream paper.
- **Stencil Black** (`#000000`): Reserved for the wordmark, primary CTAs (`btn-black`), and product names that need maximum stamp authority.

### Surface & Background Tones
- **Cream Surface** (`#f7f7f5`): Warm off-white panel background for editorial sections, alternating page bands. The "bone china" of the system.
- **Apothecary Mist** (`#f6f8f6`): Cooler cream variant with the faintest green undertone — used on form panels and softer feature surfaces.
- **Apothecary Cream** (`#ebebeb`, `#e5e5e5`, `#e7e7e7`, `#e8e8e8`): A whole family of near-identical light grays for hairline rules, panel separators, and field borders. Le Labo treats these almost interchangeably — slight variance is part of the hand-stamped aesthetic.

### Neutrals & Text
- **Notebook Graphite** (`#333`): Primary body text — the workhorse.
- **Charcoal** (`#262626`): Heading text (h2 specifically) — slightly darker for hierarchy.
- **Pencil Lead** (`#424242`): Secondary text, link hover states.
- **Slate** (`#595959`): The signature gray button background (`btn-grey`) — heavy enough to read as authoritative, soft enough to avoid screaming.
- **Stone** (`#6c6c6c`): Muted body text, captions, `btn-link` color.
- **Ash** (`#787878`): h4 sub-heading color — quietly recedes.
- **Pebble** (`#8e8e8e`, `#999`): Placeholder text, disabled states, tertiary metadata.
- **Driftwood** (`#b2b2b2`, `#bfbfbf`, `#c6c6c6`): Disabled button backgrounds, faded UI.

### Accent (used with extreme restraint)
- **Apothecary Crimson** (`#b63547`): The single chromatic accent in the entire system — used only for "Sold Out" notices, error messages, and rare emphasis. Not a brand color, a warning color.
- **Amber Glass** (`#7a4a1f` approx, observed in product photography): The brown of the iconic Le Labo bottle — appears in imagery, never in UI chrome. It's a photographic color, not a system color.

### Borders & Dividers
- **Hairline** (`1px solid #e5e5e5` or `#ebebeb`): The default rule everywhere — between rows, around cards, on form fields. Le Labo uses these as paragraph indents would work in print: structural, invisible until needed.
- **Heavy Outline** (`2px solid #595959`): Used on `btn-grey-outline` — the rare bordered button.

### Gradient System
- **None.** Le Labo is gradient-free. Every fill is solid. This is the apothecary contract: nothing is glossy, nothing is rendered, nothing is digital-first.

## Typography

### Font Family
- **Primary Display**: `'Magda', sans-serif` — stencil-cut grotesque, used in `bold` for all uppercase headlines, product names, fragrance numbers, and editorial titles. Magda's letterforms have the visible "bridges" of a real cut-tin stencil — the bowls of `O`, `D`, `B`, `R` show breaks. This is not a decorative effect; it's the typeface itself, and it's the entire visual signature of Le Labo.
- **Secondary**: `'Bell Gothic Std', 'Arial', 'Helvetica', sans-serif` — narrow, utilitarian sans originally designed for the AT&T phone book. Used on banner titles, button labels, and any uppercase UI chrome.
- **Body Fallback**: `'Helvetica', sans-serif` — used for body copy, h4 sub-heads, and `btn-link` text. Plain, transparent, gets out of the way.

*Note: Magda is a commercial typeface from Mika Mischler / Nouvelle Noire. For external implementations, Stencil Std, Octin Stencil, or a custom-cut Helvetica with stencil bridges serve as substitutes. Bell Gothic is available via Adobe Fonts.*

### Hierarchy

| Role | Font | Size | Weight | Transform | Letter Spacing | Notes |
|------|------|------|--------|-----------|----------------|-------|
| Wordmark | Magda | 36–48px | bold | UPPERCASE | 0.02em | "LE LABO" with superscript ® and "GRASSE NEW YORK" beneath |
| Banner Title (Hero) | Bell Gothic Std | 26px | normal | UPPERCASE | 0.02em | Centered on banner imagery |
| Display / Product Name | Magda | 30px (h1) | bold | UPPERCASE | 0.02em | Fragrance names: "SANTAL 33", "ROSE 31" |
| Section Heading (h2) | Magda | 20px | normal | UPPERCASE | 0.02em | Section headers, color `#262626` |
| Sub-heading (h3) | Magda | 16px | normal | UPPERCASE | 0.02em | Card titles, list section heads |
| Sub-heading (h4) | Helvetica | 14px | normal | none | normal | Tertiary heads, color `#787878` |
| Sub-heading (h5) | Magda | 13px | normal | UPPERCASE | 0.02em | Micro section markers |
| Sub-heading (h6) | Magda | 12px | normal | UPPERCASE | 0.02em | Smallest stencil label |
| Body | Helvetica | 14–16px | normal | none | normal | Reading copy, color `#333` |
| Body Small | Helvetica | 13px | normal | none | normal | Captions, metadata |
| Button Primary | Bell Gothic Std | 16px | normal | UPPERCASE | 0.02em | Line-height 54px (button height) |
| Button Link | Helvetica | 14px | normal | none | 0.02em | Underlined text link, color `#6c6c6c` |
| Caption / Legal | Helvetica | 11–12px | normal | none | normal | Footer copy, fine print |

### Principles
- **Magda + UPPERCASE is the brand voice**. Any time a product is named, a section is labeled, or a stamp is needed, Magda goes uppercase with `0.02em` tracking. This is the rubber-stamp gesture that runs through everything Le Labo prints.
- **Bell Gothic for action, Magda for identity**. Buttons, banner overlays, and CTAs use Bell Gothic — quieter, more pragmatic. Magda is reserved for what needs to feel hand-cut.
- **Helvetica for reading**. Body copy never tries to be branded. Le Labo trusts that the reader has come for the story; the font shouldn't perform.
- **Tight tracking on uppercase** (`0.02em`): Just enough air between letters to keep them legible at small sizes, not so much that they feel airy or feminine. The tracking is mechanical, not decorative.
- **Tiny base sizes**: Default body sits at 14–16px and headlines at 20–30px — small for a luxury site, because Le Labo treats the page like a printed insert, not a billboard.
- **No italic, no script, no bold-as-weight**. The only weights in active use are `normal` and `bold`. There is no italic in the brand. Emphasis comes from caps + Magda, not from a slant.

## Layout

### Spacing System
- Base unit: 5px (with frequent 10px, 15px, 20px multiples)
- Common values observed: `0`, `5px`, `9px`, `10px`, `15px`, `17px`, `20px`, `30px`, `50px`, `90px`
- Notable: Le Labo uses `15px` and `17px` as workhorses — slightly off the typical 8px grid, giving the system a hand-set, slightly imperfect rhythm rather than algorithmic precision
- Section margins: 90px below banners (`banner-push`), 50–60px between major content blocks

### Grid & Container
- Max content width: ~1400px for editorial sections, 1200px for product grids
- Product grid: 3-column on desktop, 2-column on tablet, 1-column on mobile
- Editorial pages: single-column centered, max ~700–800px reading column
- Banner sections: full-width image with centered overlay text, 50% vertical centering via `transform: translateY(-50%)`

### Whitespace Philosophy
- **Apothecary breathing room**: Generous vertical space around section heads (50–90px) — the page reads like an editorial, not a catalog
- **Tight horizontal margins on text blocks**: Body content stays narrow (~700px max) — Le Labo wants you to read, not scan
- **Image-anchored pacing**: A single sepia photograph or a row of amber bottles anchors each section. The space between images carries meaning.

### Border Radius Scale
- **Single value: `0px`**. There is exactly one radius in the entire system. No pills, no rounded inputs, no soft cards. Sharpness is the rule.
- The only "round" elements are circular product photographs (the bottle profile in some marketing imagery), which are photographic, not CSS

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text, default surfaces |
| Hairline (Level 1) | `1px solid #e5e5e5` or `#ebebeb` | Cards, list rows, form fields, section dividers |
| Heavy Rule (Level 2) | `2px solid #595959` | Outline buttons, emphasized framed blocks |
| Surface Tone Shift | Background change `#fff → #f7f7f5` | Editorial section breaks, panel content, alternating bands |
| Photograph Frame (Level 3) | Image with no chrome, hairline below | Product cards, editorial moments |

**Shadow Philosophy**: Le Labo uses **no box-shadow**. Anywhere. Depth is signaled exclusively through hairline rules and gentle surface tone shifts (white to cream to mist). This is the apothecary contract again: shadows are digital glamour, and Le Labo refuses digital glamour. The page should feel like flipping through a printed catalog — pages turn, surfaces change tone, but nothing floats.

### Decorative Depth
- Surface alternation creates rhythm: pure white sections give way to `#f7f7f5` cream panels, occasionally to `#f6f8f6` mist for forms — these tone shifts work the way chapter breaks do in a book
- Sepia photography sections function as inset visual moments, not as full-bleed hero theatre
- The wordmark sits as a stamp at the top — fixed position, no shadow, no animation

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

**Primary Black** (`btn-black`)
- Background: `#000`
- Text: `#fff`
- Font: 16px Bell Gothic Std, normal weight, UPPERCASE, `letter-spacing: 0.02em`
- Line-height: 54px (creates 54px tap target)
- Padding: typically `0 50px` for inline width
- Radius: `0` (sharp)
- Border: none
- Hover: background shifts to `#333`
- Use: primary CTAs — "ADD TO CART", "ENTER SITE", "SUBSCRIBE"

**Slate Grey** (`btn-grey`)
- Background: `#595959`
- Text: `#fff`
- Font: 16px Bell Gothic Std, UPPERCASE, `letter-spacing: 0.02em`, line-height 54px
- Radius: `0`
- Hover: background shifts to `#333`
- Disabled state: background `#bfbfbf`, text `#a3a3a3`
- Use: secondary primary actions where black would be too aggressive

**Slate Outline** (`btn-grey-outline`)
- Background: `transparent`
- Border: `2px solid #595959`
- Text: `#595959`
- Font: 16px Bell Gothic Std, UPPERCASE, line-height 50px
- Hover: text + border shift to `#333`
- Use: tertiary actions, "Learn More" style links

**Text Link** (`btn-link`)
- Background: none, border: none
- Text: `#6c6c6c`, underlined
- Font: Helvetica normal, `letter-spacing: 0.02em`
- Hover: text shifts to `#333`, underline preserved
- Use: in-body actions, "view details", footnote links

### Cards & Containers
- Background: `#fff` or `#f7f7f5` for cream variants
- Border: `1px solid #e5e5e5` or `#ebebeb` — hairline only
- Radius: `0` — no rounded corners anywhere
- Shadow: **none** — Le Labo does not use box-shadow; depth is signaled by hairline rules and surface tone shifts only
- Internal padding: 15–20px standard, 30px for editorial blocks

### Product Cards
- Surface: `#fff`
- Image: full-bleed product photograph at top, brown amber bottle on neutral background, no rounded corners on image
- Title block: Magda 16–18px UPPERCASE bold, `#333`, text-align center
- Subtitle: Helvetica 13px normal, `#6c6c6c` ("eau de parfum", "candle", "shampoo")
- Price: Helvetica 13–14px, `#333`, no currency styling
- Hairline divider above and below the card stack — never frames

### Forms & Inputs
- Background: `#fff` or `#f6f8f6`
- Border: `1px solid #e5e5e5`
- Radius: `0`
- Font: Helvetica 14–16px, color `#333`
- Padding: 15–17px vertical, 15–20px horizontal
- Placeholder color: `#999` or `#b2b2b2`
- Focus: border darkens to `#595959` (no glow ring, no color shift)
- Labels: Magda 12–13px UPPERCASE bold, `letter-spacing: 0.02em`, sit above the field

### Navigation
- Top nav: white background, centered "LE LABO" wordmark in Magda bold uppercase
- Below wordmark: utility row with country/language picker (right) and search/cart (right), home/account links (left)
- Main nav: horizontal row of UPPERCASE Bell Gothic links — "FRAGRANCES", "BODY & HAIR", "HOME", "GIFTS", "DISCOVERY", "STORES", "LABORATORY"
- Hover: link color shifts from `#333` to `#000` with no underline
- Active: thin `1px solid #333` underline
- Mobile: 81×79px hamburger button (`btn-menu`) with right border `1px solid #e5e5e5`
- Sticky: nav remains pinned at top on scroll, white surface stays opaque

### The Iconic Hand-Stamped Label (decorative element)
- Cream/kraft paper background (`#e8e0d0` approx in product imagery — a paper color, not a UI token)
- Magda bold uppercase product name at large size
- "FOR:" line followed by the customer's name in handwritten ink (set in product detail UI as a styled `<input>` rendered onto a label preview)
- "MADE: [date] / [city]" line in smaller Magda
- Batch number and bottle number in smallest Magda
- This label appears as a decorative reproduction in product photography, not as a literal UI component — the website mimics it through stacked Magda uppercase blocks separated by hairline rules

### Decorative Elements
- **Hairline horizontal rules** (`1px solid #e5e5e5`) used as section separators — replaces the visual role headlines play in most sites
- **Sepia-toned vintage photography** in editorial sections and the gateway — never illustrated, never iconified
- **Amber-bottle product photography** on neutral cream backgrounds — the bottle does the visual heavy lifting
- **Black wordmark + ® superscript** treated as a stamp at small sizes (footer, card overlays)

## Do's and Don'ts

### Do
- Use Magda bold UPPERCASE for every product name, fragrance number, and section title
- Use Bell Gothic Std for buttons, banner titles, and uppercase UI chrome
- Use Helvetica for body copy and reading text — let it disappear
- Set `letter-spacing: 0.02em` on all uppercase Magda and Bell Gothic
- Keep `border-radius: 0` everywhere — sharpness is the system
- Use `1px solid #e5e5e5` hairlines instead of shadows for separation
- Use `#333` for body text, never pure `#000`
- Alternate `#fff` and `#f7f7f5` panels for editorial pacing
- Set buttons at `line-height: 54px` for primary CTAs (creates the 54px tap height)
- Trust photography to do the storytelling — sepia, vintage, amber-glass product shots
- Treat the wordmark as a stamp: centered, with the superscript ® and "GRASSE NEW YORK" subtitle

### Don't
- Don't use rounded corners anywhere — radius is `0`, end of discussion
- Don't use box-shadow — no `0 4px 12px rgba(0,0,0,0.1)` energy here
- Don't use gradients — every fill is solid
- Don't introduce italic anywhere — Le Labo has no italic voice
- Don't use serif fonts (no Garamond, no Caslon, no Didot) — Magda + Bell Gothic + Helvetica is the entire system
- Don't use bright accent colors — the only chromatic accent is `#b63547` for warnings, used sparingly
- Don't soften body text below `#333` — anything lighter becomes muddy on cream
- Don't use ALL CAPS Helvetica — uppercase is a Magda/Bell Gothic prerogative
- Don't crop product photography into circles or non-rectangular shapes — bottles are shot square or 4:5
- Don't use any decorative ornaments (flourishes, ribbons, monograms) — the stencil typeface IS the ornament
- Don't use luxury cues (gold, marble, suede textures) — Le Labo's luxury is functional, not decorative

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Single-column, hamburger nav, stacked CTAs, 14px body |
| Tablet | 768–1023px | 2-column product grids, mobile nav still active until 1024px |
| Desktop | 1024–1399px | Full horizontal nav, 3-column product grids, full editorial layouts |
| Large Desktop | ≥1400px | Maximum content width (~1400px), wordmark at full scale |

### Touch Targets
- Primary CTAs: 54px tap height (line-height: 54px)
- Outline buttons: 50px tap height (line-height: 50px)
- Mobile menu button: 81×79px solid square
- Nav links: generous 17–20px padding for thumb access

### Collapsing Strategy
- **Nav**: Horizontal main nav collapses below 1024px to a left-aligned hamburger (`btn-menu`); full-screen drawer on open with stacked uppercase Bell Gothic links
- **Wordmark**: Scales down proportionally but stays centered; "GRASSE NEW YORK" subtitle persists at all sizes
- **Hero banners**: Full-bleed image preserved; overlay text scales from 26px to 20px Bell Gothic
- **Product grid**: 3-col → 2-col → 1-col with `90px` bottom margin per banner row maintained
- **Editorial type**: 30px h1 → 24px → 20px on mobile
- **Spacing**: 90px banner-push compresses to ~40px on mobile but maintains the breathing rhythm

### Image Behavior
- Product photography stays full-bleed at every breakpoint
- Sepia editorial photography preserved without art-direction changes
- Wordmark never becomes icon-only — "LE LABO / GRASSE NEW YORK" persists
- No retina-specific imagery swap — Le Labo serves single high-res JPEGs

---

## Agent Prompt Guide

### Quick Color Reference
- Page Background: Lab Paper White (`#ffffff`)
- Cream Panel: Apothecary Cream (`#f7f7f5`)
- Mist Panel: Apothecary Mist (`#f6f8f6`)
- Primary Text: Notebook Graphite (`#333333`)
- Heading Text: Charcoal (`#262626`)
- Stencil Black: (`#000000`) — wordmark and primary CTA only
- Slate Button: (`#595959`)
- Stone Body: (`#6c6c6c`)
- Hairline: `1px solid #e5e5e5` or `#ebebeb`
- Warning Crimson: (`#b63547`) — sparingly

### Example Component Prompts
- "Create a product card on `#ffffff` with no shadow, hairline `1px solid #e5e5e5` borders. Product name in Magda bold UPPERCASE 18px, `letter-spacing: 0.02em`, color `#333`. Subtitle 'eau de parfum' in Helvetica 13px normal, color `#6c6c6c`. Price in Helvetica 14px, color `#333`, no currency styling. Image full-bleed at top, no `border-radius`."
- "Build a primary CTA: `background: #000`, `color: #fff`, `font-family: Bell Gothic Std`, font-size 16px, `text-transform: uppercase`, `letter-spacing: 0.02em`, `line-height: 54px`, `padding: 0 50px`, `border-radius: 0`, `border: none`. Hover shifts background to `#333`."
- "Design a hero banner with a full-width sepia-toned vintage photograph (apothecary scene, low warm light). Centered overlay: site title 'LE LABO' in Magda bold uppercase 36px, subtitle 'GRASSE NEW YORK' in Magda bold uppercase 14px directly beneath, both in `#fff`. No gradient scrim — trust the photograph."
- "Create a section divider: 60px vertical space, `1px solid #e5e5e5` horizontal rule centered at 1400px max-width. No icons, no decoration."
- "Design a form field: white background, `1px solid #e5e5e5` border, `border-radius: 0`, padding 17px 20px, font Helvetica 16px color `#333`, placeholder color `#999`. Label above the field in Magda bold UPPERCASE 12px, `letter-spacing: 0.02em`. Focus state: border darkens to `#595959`, no glow."
- "Build an editorial section: alternate `#ffffff` and `#f7f7f5` background bands, each band 90px+ vertical padding. Section heading in Magda bold UPPERCASE 20px color `#262626`. Body in Helvetica 14–16px color `#333`, max-width 700px centered."

### Iteration Guide
1. Default to Magda bold UPPERCASE for any product name, section header, or stamp moment — this is the brand voice
2. Default to `border-radius: 0` everywhere — never round a corner
3. Replace shadows with hairline `1px solid #e5e5e5` rules and surface tone shifts
4. Body text is `#333`, headings are `#262626`, pure `#000` is reserved for the wordmark and primary CTAs
5. Letter-spacing on uppercase is always `0.02em` — never wider, never tighter
6. Buttons are 54px tall (line-height) with Bell Gothic Std uppercase labels
7. Surface alternation: `#fff` → `#f7f7f5` → `#f6f8f6` is the only "elevation" system
8. No gradient, no italic, no rounded corners, no box-shadow, no decorative icons — the stencil typeface carries every aesthetic load
9. Trust sepia photography to do the emotional work — the UI itself stays clinical
