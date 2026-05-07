---
version: alpha
name: "Graza"
description: "Token-first design system reference for Graza."

colors:
  background: "#ffffff"
  surface: "#3c422e"
  surface-elevated: "#f5f5f5"
  ink: "#111111"
  ink-muted: "#f6e6d9"
  primary: "#fff4ec"
  on-primary: "#ffffff"
  border: "#d1e030"
  focus-ring: "#fff4ec"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 120px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 84px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 42px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 29px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 46px
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

# Graza Design System

## Overview

Graza's website is a cookbook in browser form. The page opens on a warm cream paper canvas (`#fff4ec`) — closer to the inside of an old hardback cookbook than any DTC site has a right to be — and immediately commits to deep olive-green type (`#3c422e`) that reads as ink rather than text. There is no white anywhere. The whole composition runs on the contrast between paper, ink, and a single electric brand chartreuse (`#d1e030`) that lives on the squeeze-bottle label and bleeds out into oversized accent panels. The vibe is part editorial pantry, part farmer's market handout — confident, food-first, and unmistakably DTC without ever leaning on the polished SaaS gloss.

The signature move is the typographic pairing: a giant condensed Didone serif (`ITC Garamond Condensed`) for display moments — set at 102–120px with negative tracking that pulls letters into one continuous shape — paired against a chunky monospaced typewriter (`GT Alpina Typewriter`) for body, labels, captions, and CTAs. Display headlines feel like cookbook chapter openers ("GRAZA" set 120px tall and almost touching its container edges); body copy feels like a recipe card someone typed on an Olivetti. The combination is loud editorial without ever feeling corporate, and it's the entire personality of the brand in two fonts.

What pushes Graza past "nice DTC site" into actual identity territory is the **dashed-border + hand-drawn olive ornament** system. Section dividers, recipe cards, badges, and product callouts are framed with 1px dashed olive lines (`1px dashed #3c422e`) that read like the perforations on a coupon book or the cut lines on a recipe card pulled from a magazine. Hand-illustrated olive branches, little chef figures, and halftone-style pattern blocks sit between sections as breathing room. Pair that with generously rounded 16–20px corners on every photo, video, and panel — soft, scrapbook, handled — and the page reads as something printed and assembled rather than coded.

**Key Characteristics:**
- Cream paper canvas (`#fff4ec`) — never white, sets the cookbook tone immediately
- Olive-green ink (`#3c422e`) for ALL text — no black anywhere, type carries the warmth
- Brand chartreuse (`#d1e030`) reserved for label moments, big accent panels, the squeeze-bottle yellow
- Display in `ITC Garamond Condensed` 400 at 72–120px with tight `-2.16px` to `-3.6px` negative tracking
- Body in `GT Alpina Typewriter` 400/500 at 16px, line-height 1.50 — chunky and warm
- Dashed olive borders (`1px dashed #3c422e`) as the signature section divider and frame style
- Soft 16–20px radius on all media — photos, videos, panels feel handled and pinned to the page
- Hand-drawn olive branch and illustration spot art between sections, no stock or icon library
- Generous warm-secondary peach surface (`#f6e6d9`) for inverted/secondary panels

## Colors

### Primary
- **Graza Cream** (`#fff4ec`): Primary page background — warm, paper-like, leans peach more than pure ivory. The defining tone.
- **Graza Olive Ink** (`#3c422e`): All primary text, headings, body, borders, button outlines. Replaces black entirely.
- **Graza Peach** (`#f6e6d9`): Secondary surface — used for cards, footer panels, inverted nav blocks. A deeper paper tone.

### Brand Accent
- **Graza Chartreuse** (`#d1e030`): The signature label color — the actual squeeze-bottle yellow-green. Used on hero panels, primary CTAs, tag overlays. The single chromatic anchor.
- **Graza Lime Bright** (`#9eef80`): Accent button fill, "BUY" CTA highlight — a brighter sibling to chartreuse with more green saturation.
- **Graza Stroke Green** (`#9fcd7a`): Secondary stroke and accent green for outlines on chartreuse surfaces.
- **Graza Sun Yellow** (`#fbd535`): Tertiary accent for the "Sizzle" cap color, occasional badges, special promos.

### Neutrals & Text
- **Graza Olive Ink** (`#3c422e`): All text without exception — headings, body, captions, button labels, links.
- **Cream-on-Dark Text** (`#fff4ec`): Inverted text on olive-green or chartreuse panels — the cream becomes the type color.
- **Peach-on-Dark Text** (`#f6e6d9`): Soft inverted text on full olive footer/panels.

### Surface & Borders
- **Cream Surface** (`#fff4ec`): Default canvas panel.
- **Peach Surface** (`#f6e6d9`): Card backgrounds, secondary panels, footer.
- **Olive Border** (`#3c422e`): 1px solid for buttons and frames, 1px dashed for cookbook-style dividers.
- **Cream Border** (`#fff4ec`): Inverted border on dark-olive panels.

### Shadow & Stamp Colors
- Graza is **shadow-free** — the dembrandt extraction returns zero shadow declarations across the page. Depth is created entirely by border weight, dashed-border framing, and color blocking. Buttons sit flat. Cards sit flat. The system is genuinely two-dimensional.

### Gradient System
- Graza is **gradient-free**. Every color application is solid. The richness comes from the cream/peach/olive triangle alternating with full chartreuse panels — never blended.

## Typography

### Font Family
- **Display**: `ITC Garamond Condensed`, fallback to a condensed serif (Didoni, Playfair Display Black with condensed tracking, or Bodoni Condensed for web)
- **Body / UI**: `GT Alpina Typewriter`, fallback to a slab/typewriter mono (`JetBrains Mono`, `Courier Prime`, `IBM Plex Mono`)
- **Captions / Pills**: Same `GT Alpina Typewriter` at 12–13px uppercase
- **Eyebrow / Promo banner**: `Apercu` for the very small uppercase promo strip at top of page
- **OpenType Features**: Standard ligatures only — the typeface character carries the personality

*Note: ITC Garamond Condensed is a commercial typeface from ITC. For external implementations, `Bodoni Condensed`, `Playfair Display` with condensed tracking, or `Recoleta Bold` work as web substitutes. GT Alpina Typewriter is from Grilli Type — `JetBrains Mono` or `IBM Plex Mono` substitute well as free monospaced alternatives.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Mega | ITC Garamond Condensed | 120px (7.50rem) | 400 | 1.00 | -3.6px | "GRAZA" wordmark moments — full-bleed display |
| Display Hero | ITC Garamond Condensed | 102px (6.38rem) | 400 | 0.90 | -2.16px | Primary hero headlines — "Olive oil so fresh, you can taste it." |
| Display Large | ITC Garamond Condensed | 72px (4.50rem) | 400 | 1.00 | -2.16px | Section openers, oversized button text |
| Display Medium | ITC Garamond Condensed | 48px (3.00rem) | 400 | 1.00 | normal | Sub-section heads, callout titles |
| Display Small | ITC Garamond Condensed | 46px (2.88rem) | 400 | 1.60 | -1.44px | Editorial sub-heads — note the unusual 1.60 line-height for poetic spacing |
| Body Large UPPER | GT Alpina Typewriter | 20px (1.25rem) | 500 | 1.50 | normal | Section eyebrows, intro labels — UPPERCASE |
| Body Large | GT Alpina Typewriter | 20px (1.25rem) | 400 | 1.25 | normal | Lead paragraphs, intro copy |
| Body | GT Alpina Typewriter | 18px (1.13rem) | 400 | 1.50 | normal | Standard reading text |
| Body Default | GT Alpina Typewriter | 16px (1.00rem) | 400 | 1.50 | normal | Default body, navigation links |
| Button | GT Alpina Typewriter | 16px (1.00rem) | 500 | 1.50 | normal | Primary CTAs — often UPPERCASE for emphasis |
| Eyebrow | Apercu | 13px (0.81rem) | 400 | 1.00 | normal | UPPERCASE promo banner at very top of page |
| Caption Upper | GT Alpina Typewriter | 12px (0.75rem) | 500 | 1.50 | normal | UPPERCASE labels, badges, fine print headings |
| Caption | GT Alpina Typewriter | 12px (0.75rem) | 400 | 1.50 | normal | Footnotes, legal text, micro-labels |

### Principles
- **Pairing is the system**: ITC Garamond Condensed for display, GT Alpina Typewriter for everything else. No third typeface (the Apercu eyebrow is an outlier reserved for the tiny top promo bar). Every page renders this exact contrast.
- **Tight display tracking, neutral body tracking**: Display sizes use aggressive negative tracking (`-2.16px` to `-3.6px`) that pulls letters into one continuous mass. Body and caption tracking stays at default — typewriter type is already wide and chunky, no additional spacing needed.
- **UPPERCASE for chrome and authority**: Promo banners, button labels, eyebrows, and small section indicators run uppercase in GT Alpina Typewriter. The capitals act as a structural anchor against the soft-cased serif display.
- **Display is never bold**: ITC Garamond Condensed at weight 400 is already heavy enough — no 600/700 anywhere. The condensed proportion and tight tracking carry the weight.
- **Body has two operative weights**: 400 for prose, 500 for emphasized labels, captions, and buttons. No 700 in body either — the typewriter face doesn't need it.

## Layout

### Spacing System
- Base unit: 4px (with strong reliance on a 10px / 20px / 40px / 60px / 100px ladder)
- Scale: 4px, 8px, 10px, 12px, 16px, 20px, 24px, 30px, 35px, 40px, 48px, 60px, 80px, 100px
- Notable: Graza relies heavily on 20px and 24px (each used 18 times in the extraction) as the dominant card-padding unit, with 60px and 100px as the section-spacing macro values. The 35px/30px middle band handles between-card gaps inside grids.

### Grid & Container
- Max content width: ~1440px outer, with content typically respecting a ~1200px column
- Hero: full-bleed product photography with stacked text+CTA card overlay
- Feature sections: 3-column product grids, 2-column feature pairs, full-bleed "Sun Fact" editorial breaks
- Footer: massive olive-on-cream block with multi-column nav, dashed borders separating columns
- Frequent full-bleed accent rows in chartreuse for category transitions and promo moments

### Whitespace Philosophy
- **Editorial pacing, generous breathing**: 60–100px between major sections. Within sections, 20–24px between elements. Cards breathe with 24–40px internal padding.
- **Color blocking as section break**: Instead of dividers or extra spacing, Graza switches surface color (cream → chartreuse → peach → olive) to chapter the page. Each new color is a new chapter.
- **Type-anchored rhythm**: Display headings get 60–80px of vertical breathing room above and below. Body text needs only 20–24px. The heavy condensed display demands its own air.

### Border Radius Scale
- Sharp (0px): No actual sharp rectangles in the system — radius is always present.
- Small (8px): Buttons, inputs — the workhorse interactive radius
- Joined Pair (10px asymmetric): Connected button-input pairs — `0px 10px 10px 0px` and `10px 0px 0px 10px`
- Card (10–16px): Tighter cards, inline panels
- Soft Card (20px): Photo frames, video thumbnails, product imagery — the dominant content-card radius
- Pill (9999px / 100%): Search field, account chip, badges, all fully-rounded UI elements
- Notable: Graza never uses 4px or 6px — radius starts at 8px and jumps to 10/16/20. The system reads soft and handled.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border, color block only | Page canvas, full-bleed sections, body text |
| Solid Outline (Level 1) | `1px solid #3c422e` | Buttons, inputs, hard-edged cards, frames |
| Dashed Cookbook (Level 2) | `1px dashed #3c422e` | Recipe cards, section dividers, cutout blocks — the signature treatment |
| Inset Focus (Level 3) | `box-shadow: 0 0 0 30px var(--bg) inset` | Form-field focus state — fills the input with a focus-tinted cream wash |
| Color Block (Level 4) | Surface swap — cream to chartreuse, cream to olive | Section-level "elevation" via color, not shadow |

**Shadow Philosophy**: Graza has no drop shadows, no inset shadows beyond the focus-state cream wash, and no soft elevation effects anywhere. Depth is communicated through three things: **border weight** (1px solid for hard, 1px dashed for soft), **surface color blocking** (cream / peach / olive / chartreuse alternation), and **typographic scale** (a 120px display headline IS the elevation against 16px body). The dembrandt extraction confirms zero shadow declarations across the page. This is genuinely 2D editorial design, and that's the point — it reads as printed paper, not as a UI.

### Decorative Depth
- Dashed borders create a "cut from a magazine" depth illusion without adding shadow
- Surface color blocking acts as chapter elevation — moving from cream onto a full chartreuse panel reads as moving to a new "page"
- Hand-drawn olive spot art adds visual depth through illustration density without engaging shadow or layering

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

**Primary Lime CTA**
- Background: Graza Lime Bright (`#9eef80`)
- Text: Graza Olive Ink (`#3c422e`)
- Padding: 16px vertical, 24px horizontal (squared button block)
- Radius: `8px`
- Border: `1px solid #3c422e`
- Shadow: `none` (Graza is flat)
- Font: 16px GT Alpina Typewriter weight 500, often UPPERCASE
- Use: Primary "BUY", "ADD TO CART", "GET THE TRIO"

**Olive Solid (Inverted)**
- Background: Graza Olive Ink (`#3c422e`)
- Text: Graza Cream (`#fff4ec`)
- Padding: 16px / 24px
- Radius: `8px`
- Border: `1px solid #3c422e`
- Font: 16px GT Alpina Typewriter weight 500
- Use: Footer CTAs, secondary "Shop All" buttons, inverted-section primary actions

**Cream Outline (Ghost)**
- Background: Graza Cream (`#fff4ec`) or transparent
- Text: Graza Olive Ink (`#3c422e`)
- Border: `1px solid #3c422e`
- Radius: `8px`
- Font: 16px GT Alpina Typewriter weight 500
- Use: Secondary actions, tab-style toggles, "Learn More" patterns

**Connected Pair (Email + Submit)**
- Used in newsletter signup blocks
- Email input: `border-radius: 10px 0px 0px 10px`, 1px solid olive
- Submit button: `border-radius: 0px 10px 10px 0px`, lime fill, joined to input
- Together they read as a single recipe-card unit

**Display Button (Large)**
- Background: Chartreuse (`#d1e030`) or olive
- Text: ITC Garamond Condensed at 48–72px, weight 400
- Use: Hero "BUY NOW" buttons that double as display typography

### Cards & Containers

- Background: Cream (`#fff4ec`) or Peach (`#f6e6d9`) for tinted contrast
- Border: `1px dashed #3c422e` for the signature cookbook-cutout look, or `1px solid #3c422e` for hard-edged containers
- Radius: `16px` or `20px` — the soft scrapbook/recipe-card radius
- Shadow: `none`
- Internal padding: 24–40px — generous editorial padding
- Photo cards: 20px radius, no border, sit on cream with dashed-border captions below

### Badges / Tags / Pills

**Cookbook Tag (Solid Olive)**
- Background: Olive Ink (`#3c422e`)
- Text: Cream (`#fff4ec`)
- Padding: 4px 10px
- Radius: `100%` (fully pill)
- Font: 12px GT Alpina Typewriter weight 500, UPPERCASE
- Use: Product category, "NEW", "LIMITED" stamps

**Cream Outline Tag**
- Background: transparent
- Text: Olive Ink (`#3c422e`)
- Border: `1px solid #3c422e`
- Radius: `100%`
- Font: 12px GT Alpina Typewriter weight 400, UPPERCASE
- Use: Filter chips, ingredient tags, recipe meta

**Dashed Cutout Block**
- Background: Cream
- Border: `1px dashed #3c422e`
- Radius: `16px`
- Internal: padded heading + small body
- Use: Signature recipe-card / coupon-book block — Graza's most identifiable container

### Inputs & Forms

- Background: Cream (`#fff4ec`) or transparent
- Border: `1px solid #3c422e`
- Radius: `8px`
- Padding: 16px
- Font: 16px GT Alpina Typewriter weight 400
- Text: Olive Ink (`#3c422e`)
- Focus: `box-shadow: 0 0 0 30px var(--bg) inset`, `outline: 2px solid transparent`, `background: var(--color-highlight)` — Graza uses an inset cream wash on focus rather than an outline ring
- Placeholder: Olive Ink at reduced opacity

### Navigation

- Top promo strip: full-bleed cream or chartreuse band, 13px Apercu UPPERCASE eyebrow text
- Main nav: cream background, olive logo wordmark left, cart and account icons right
- Links: GT Alpina Typewriter 16px weight 400, olive `#3c422e`, no underline default
- Hover: text decoration appears (underline) in olive — the primary affordance
- Mega-menu drops: full-width panel on cream with peach card splits, hand-drawn olive illustrations as section anchors

### Decorative Elements

**Dashed Cookbook Borders**
- `1px dashed #3c422e` — the signature divider treatment
- Applied to: section breaks, recipe-card frames, signup blocks, between products
- Reads like coupon-book perforations or magazine recipe cut-outs

**Hand-Drawn Olive Spot Art**
- Olive branches, small chef figures, halftone leaf blocks
- Inline SVG, monochrome olive (`#3c422e`) on cream
- Used between major sections as breathing-room ornaments — never decorative-only, always anchoring an idea ("Fun Fact", recipe break, ingredient note)

**Halftone Dot Patterns**
- Brand-label-derived halftone dots in chartreuse over cream
- Used as accent panels behind product photography to echo the squeeze-bottle label aesthetic

**Photo Treatment**
- All product and lifestyle photography sits in 20px-radius rounded frames
- No drop shadows, no scrim overlays — photos sit cleanly on cream with surrounding type breathing
- Color grading leans warm and high-saturation to match the chartreuse-on-cream palette

## Do's and Don'ts

### Do
- Use cream `#fff4ec` as the page background — never pure white. The warmth is non-negotiable.
- Set all body and heading text in olive `#3c422e` — replace black entirely with this olive ink.
- Reserve chartreuse `#d1e030` for label moments, accent panels, and the squeeze-bottle yellow-green identity
- Pair `ITC Garamond Condensed` display with `GT Alpina Typewriter` body — every screen should show this contrast
- Apply tight negative tracking (`-2.16px` to `-3.6px`) on display sizes 72px+
- Use `1px dashed #3c422e` borders for the signature cookbook cutout treatment
- Round all photo and video frames to 20px — the soft scrapbook radius
- UPPERCASE button labels, eyebrows, and badges in GT Alpina Typewriter — the typewriter capitals are part of the identity
- Use hand-drawn olive spot illustrations between sections instead of dividers or icons
- Color-block section breaks (cream → chartreuse → peach → olive) rather than reaching for shadow elevation

### Don't
- Don't use pure black text — always olive ink (`#3c422e`)
- Don't use pure white anywhere — cream (`#fff4ec`) or peach (`#f6e6d9`) only
- Don't add drop shadows to anything — Graza is genuinely flat
- Don't use a sans-serif as the primary body face — typewriter mono is the brand voice
- Don't introduce a third display typeface — Garamond Condensed alone carries display
- Don't use bold weight on Garamond Condensed — 400 is the only display weight
- Don't tighten body tracking — typewriter type wants its natural width
- Don't put chartreuse next to peach in the same composition — chartreuse pairs with cream or olive only
- Don't use icon libraries (Lucide, Heroicons, etc.) — hand-drawn olive spot art replaces icons
- Don't add gradient fills — every color application is solid

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | 375–480px | Single-column, display drops to 56–72px |
| Mobile | 480–680px | Single-column, 72px display, stacked CTAs and product cards |
| Tablet | 680–1024px | 2-column product grids, 80–102px display, side-by-side text+image pairs |
| Desktop | 1024–1440px | Full 3-column product grids, 102–120px display, multi-column footer |
| Large Desktop | ≥1440px | Maximum scale (120px GRAZA wordmark moments), wider section padding |

### Touch Targets
- Primary CTAs: 48px tap height minimum, 16px vertical padding, 24px horizontal padding on mobile
- Nav links: full-row tap targets with 16–20px padding
- Cart/account icons: 44px circular tap area, fully-pill (`100%`) radius
- Email signup pair: stacks vertically on mobile, joined-radius becomes `10px 10px 0 0` (top) and `0 0 10px 10px` (bottom)

### Collapsing Strategy
- **Nav**: Horizontal nav collapses to hamburger; mega-menu becomes full-screen scroll panel on cream
- **Display type**: 120px → 102px → 72px → 56px progressive scaling, weight stays 400, tracking stays proportionally tight
- **Product grids**: 3-col → 2-col → 1-col, with photo radius held at 20px throughout
- **Dashed borders**: Maintained at 1px dashed at all sizes — the cookbook frame is fundamental
- **Section spacing**: 100px desktop → 60px tablet → 40px mobile — compresses but never collapses
- **Hand-drawn ornaments**: Scale proportionally rather than dropping; smaller variants exist for mobile section breaks

### Image Behavior
- Product photography fills viewport edge-to-edge on mobile hero
- Lifestyle/recipe photos maintain 20px radius at every breakpoint
- No art-direction swap — same warm-graded palette adapts to every viewport
- Halftone dot patterns scale proportionally; on mobile, density increases to compensate

---

## Agent Prompt Guide

### Quick Color Reference
- Page Background: Graza Cream (`#fff4ec`)
- Secondary Surface: Graza Peach (`#f6e6d9`)
- Primary Text / Borders: Graza Olive Ink (`#3c422e`)
- Inverted Text: Graza Cream (`#fff4ec`)
- Brand Accent: Graza Chartreuse (`#d1e030`)
- CTA Lime: Graza Lime Bright (`#9eef80`)
- Sun Yellow Accent: Graza Sun (`#fbd535`)
- Stroke Green: Graza Stroke (`#9fcd7a`)
- Dashed Border: `1px dashed #3c422e`
- Solid Border: `1px solid #3c422e`

### Example Component Prompts
- "Create a hero section on Graza Cream (`#fff4ec`) with a headline at 102px ITC Garamond Condensed weight 400, line-height 0.90, letter-spacing -2.16px, color `#3c422e`. Below, a subhead at 20px GT Alpina Typewriter weight 400 line-height 1.25. Primary CTA: Lime Bright (`#9eef80`) background, 1px solid `#3c422e` border, 8px radius, 16px GT Alpina Typewriter weight 500 UPPERCASE."
- "Design a recipe card on Cream (`#fff4ec`) with `1px dashed #3c422e` border, 16px radius, 24px internal padding. Title in ITC Garamond Condensed 48px weight 400. Body in GT Alpina Typewriter 16px weight 400 line-height 1.50."
- "Build a full-bleed accent panel in Chartreuse (`#d1e030`) with display text in ITC Garamond Condensed 120px weight 400 letter-spacing -3.6px in Olive Ink (`#3c422e`). Pair with a hand-drawn olive branch SVG in olive on the right side."
- "Create a connected email signup: input with `border-radius: 10px 0px 0px 10px`, 1px solid `#3c422e`, 16px padding, 16px GT Alpina Typewriter. Submit button next to it with `border-radius: 0px 10px 10px 0px`, Lime Bright (`#9eef80`) fill, same border, 16px UPPERCASE label."
- "Design a product card with photo at 20px radius, no border. Below: olive-pill tag at `border-radius: 100%`, 12px GT Alpina Typewriter weight 500 UPPERCASE. Title in 46px ITC Garamond Condensed line-height 1.60. Price in GT Alpina Typewriter 18px."

### Iteration Guide
1. Default to Cream `#fff4ec` page background and Olive Ink `#3c422e` text — never deviate to white/black
2. Pair ITC Garamond Condensed (display) with GT Alpina Typewriter (body) on every screen — this is the brand
3. Tight negative tracking on display 72px+ (`-2.16px` to `-3.6px`); leave body tracking neutral
4. Reserve Chartreuse `#d1e030` for accent panels and label-evoking moments — not for body or buttons
5. Use Lime Bright `#9eef80` for primary CTAs — it reads as the "active" sibling of chartreuse
6. Round photos and panels to 20px; buttons and inputs to 8px; badges to fully-pill
7. Use `1px dashed #3c422e` borders for cookbook cutout panels — the signature non-shadow depth
8. UPPERCASE all button labels, eyebrows, and badge text in GT Alpina Typewriter weight 500
9. Color-block section transitions (cream → chartreuse → peach → olive) rather than using dividers
10. No drop shadows anywhere — depth is borders, color blocking, and typographic scale only
