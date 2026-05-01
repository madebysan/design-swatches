---
slug: muji
name: Muji
url: https://www.muji.com
domain: muji.com
category: Retail
styles: [Light, Minimal, Warm]
tagline: "Charcoal-stamp ink on warm beige paper, no-brand restraint, Helvetica Neue carrying every word at a calm 16px"
fonts: [Helvetica Neue, Noto Sans JP]
primary_color: "#7f0019"
---

# Design System Inspired by Muji

> Charcoal-stamp ink on warm beige paper, no-brand restraint, Helvetica Neue carrying every word at a calm 16px

## 1. Visual Theme & Atmosphere

Muji's site is no-brand goods translated into pixels. The canvas is a warm cream beige (`#f4eede`) and white (`#ffffff`) interplay, with text set in a soft charcoal (`#3c3c43`) that reads more like stamped sumi ink than pure black. The page never raises its voice — there are no gradients, no decorative illustration, no marketing flourish. Buttons are rectangles with a `4px` radius, borders are hairline `1px` strokes in `#d8d8d9`, and the only chromatic note in the entire system is the muji-red wordmark (`#7f0019`) — a deeply muted oxblood that reads as ceremonial wax-seal rather than CTA accent. Imagery is product-on-paper: clean catalogue photography on cream backgrounds with no shadow stages.

What makes Muji unmistakable is the **dual-script typography contract**. The system runs Helvetica Neue as the primary face, with a deep Japanese fallback chain (`Noto Sans JP`, `Noto Sans JP Fallback`, `Hiragino Kaku Gothic ProN`, `Meiryo`) that lets Latin and Japanese characters share the same optical rhythm. Everything sits at `1.6` line-height — body text, captions, navigation — producing the unforced breathing room of a product catalogue. There are no display sizes above `32px`, and the most common heading size is just `26px` with `2.4px` letter-spacing. Muji refuses to shout, even in hero positions.

The third defining trait is **near-zero ornament**. There are no shadows in the system at all (the dembrandt scrape returns an empty `shadows` array). Elevation is communicated entirely through hairline borders and tonal surface shifts between `#ffffff`, `#f5f5f5`, and `#f4eede`. Tags are sharp rectangles (`0` radius), product cards have no border, and the only circular shapes are filter toggles and pagination dots. The aesthetic is Tokyo stationery aisle rendered in CSS — quiet, useful, faintly warm.

**Key Characteristics:**
- Cream beige canvas (`#f4eede`) and pure white (`#ffffff`) — never grey, always warm
- Charcoal stamp-ink text (`#3c3c43`) — softer than pure black, easier on long reading
- Single-typeface UI — Helvetica Neue with a deep Japanese fallback chain
- Comfortable 16px base body at `1.6` line-height — catalogue rhythm, not landing-page rhythm
- Border radius is binary: `4px` for buttons and tiles, `50%`/`9999px` for circular controls only
- Hairline `1px` borders in `#d8d8d9` for whisper-quiet structure
- Zero shadows in the system — elevation comes from surface tone, not depth
- The muji-red (`#7f0019`) wordmark is the ONLY chromatic accent — deep oxblood, never bright red
- Beige tag chips (`#f4eede`, `#e0ceaa`) for category labels — sharp `0` radius rectangles
- Sentence case throughout UI, never uppercase except for stylistic micro-eyebrows

## 2. Color Palette & Roles

### Primary Brand
- **Muji Red** (`#7f0019`): The brand wordmark color — a deep oxblood that reads as stamp ink rather than CTA red. Reserved for the logo, occasional brand-mark accents, and never used as a button background.

### Brand Accent
- **Alert Red** (`#dd0c14`): The functional sale/error red — saturated and bright, used only for sale prices and form errors. Distinctly NOT the wordmark red.
- **Beige** (`#e0ceaa`): The chromatic warm note — used for switch toggles, active filter tints, and the warmth that makes the cream canvas feel like paper rather than screen.

### Text Scale
- **Charcoal Ink** (`#3c3c43`): All primary text and headings. The defining text color.
- **Mid Grey** (`#76767b` / `#6d6d72`): Secondary text, meta labels, inactive nav.
- **Soft Grey** (`#9d9da0`): Disabled text, placeholder text.
- **Hairline Grey** (`#c4c4c6`): Divider strokes for tertiary structure, inactive borders.

### Surface & Background
- **Pure White** (`#ffffff`): Default product card and module background.
- **Cream Paper** (`#f4eede`): The signature warm surface — used for tag pills, alternate sections, hero panels.
- **Sand Stripe** (`#f5f5f5`): Tertiary surface for subtle striping in long lists and table rows.
- **Hover Tint** (`#ebebec`): One-step warming applied on hover for secondary buttons and list items.

### Borders & Dividers
- **Standard Hairline** (`#d8d8d9`): The default `1px` divider — list separators, form-field bottom borders.
- **Inactive Border** (`#c4c4c6`): Secondary button outlines and tile strokes.
- **Solid Ink** (`#3c3c43`): `1px` and `1.5px` borders on focused or active controls — labels, switches, top-of-card emphasis bars.
- **Translucent Hairline** (`rgba(0, 0, 0, 0.2)`): The 0.5px micro-divider used for table cell strokes and dense lists.

### Shadow System
Muji is **functionally shadow-free**. The dembrandt scrape returned an empty shadows array — there are no drop shadows, glows, or ambient elevations anywhere on the production site. Depth is communicated by surface tone and `1px` border strokes, never blur.

## 3. Typography Rules

### Font Family
- **Primary**: `Helvetica Neue`, fallback chain: `Arial, Noto Sans JP, Noto Sans JP Fallback, Hiragino Kaku Gothic ProN, Meiryo`
- **Loading source**: System fonts only — no Google Fonts, no Adobe Fonts, no variable fonts. Muji uses Helvetica Neue from the OS and falls through to Japanese system faces for CJK characters.

The single-family approach is itself a brand decision: a no-brand brand uses no specialty type. Helvetica Neue is treated as raw material, not signature.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero / H1 (large) | Helvetica Neue | 32px (2rem) | 700 | 1.60 | normal | Largest heading on the site — section openers only |
| H1 (standard) | Helvetica Neue | 26px (1.63rem) | 700 | 1.15 | 0.15em (2.4px) | Standard page heading with wider tracking |
| H1 (compact) | Helvetica Neue | 26px (1.63rem) | 700 | 1.60 | normal | Card or inline heading, no extra tracking |
| Body / H1 (small) | Helvetica Neue | 16px (1rem) | 400 | 1.60 | normal | Default body text and small contextual headings |
| Body Bold | Helvetica Neue | 16px (1rem) | 700 | 1.60 | normal | Emphasized body, product names |
| Button | Helvetica Neue | 16px (1rem) | 700 | 1.60 | normal | Primary and secondary CTAs |
| Caption Bold | Helvetica Neue | 14px (0.88rem) | 700 | 1.60 | normal | Meta labels, small headings |
| Caption | Helvetica Neue | 14px (0.88rem) | 400 | 1.60 | normal | Default meta and supporting copy |
| Small Caption | Helvetica Neue | 12px (0.75rem) | 400 | 1.60 | normal | Footer copy, breadcrumbs |
| Small Bold | Helvetica Neue | 12px (0.75rem) | 700 | 1.60 | normal | Footer headers, micro-labels |
| Micro / Tag | Helvetica Neue | 10px (0.63rem) | 700 | 1.10 | normal | Tag-label text in product tiles |

### Principles
- **One typeface, two weights**: Helvetica Neue at 400 and 700. No 500, no 300. The system caps emphasis with regular vs bold.
- **Universal `1.6` line-height**: From 16px body to 26px heading, almost everything sits at `1.60`. The exception is the 32px hero (also 1.60) and the 10px micro (1.10). This gives Muji's pages an unforced, even rhythm.
- **Sentence case for UI**: Buttons, navigation, tabs, and labels read as natural prose. No uppercase styling.
- **Tracking only at 26px**: The single tracked size is the standard H1 at `2.4px` letter-spacing — every other size uses normal tracking.
- **Body type sits at 16px**: A comfortable reading size, never the 12px-14px density of a dense-editorial brand. Muji is a catalogue, not a literary journal.

## 4. Component Stylings

### Buttons

**Primary (Filled Ink)**
- Background: Charcoal Ink (`#3c3c43`)
- Text: White (`#ffffff`)
- Padding: `16px 20px`
- Radius: `4px`
- Border: `0px none`
- Font: 16px Helvetica Neue, weight 700
- Hover: `rgba(50, 50, 50, 0.9)` background, slight text desaturation
- Active: `#e0ceaa` (beige) background — the brand's warm-press feedback
- Focus: `0.0625em` solid `#ffffff` outline
- Use: Primary CTAs — "Add to cart", "Continue", "Sign up"

**Secondary (Beige Fill)**
- Background: Beige Cream (`#f4eede`)
- Text: Charcoal Ink (`#3c3c43`)
- Padding: `16px 20px`
- Radius: `4px`
- Border: `0px none`
- Hover: `#e0ceaa` background — deepens to brand beige
- Use: Secondary CTAs — "View details", "Save"

**Outline (Ghost)**
- Background: White (`#ffffff`)
- Text: Charcoal Ink (`#3c3c43`)
- Border: `1px solid #c4c4c6`
- Padding: `15px 19px` (1px tighter to compensate for border)
- Radius: `4px`
- Hover: background fills to `#f5f5f5`
- Use: Tertiary actions, form steppers

**Pill Pager (Carousel Active)**
- Background: transparent default, `#3c3c43` (ink) when active
- Border: `1px solid #3c3c43`
- Radius: `9999px` (pill)
- Padding: `0`
- Use: Carousel pagination dots, dot navigation

### Cards & Containers
- Background: White (`#ffffff`) on default, `#f4eede` (cream) on alternate sections
- Border: `0` default; `1px solid #d8d8d9` for top-edge dividers in stacked lists
- Radius: `4px` for product tiles, `0` for full-bleed sections
- Shadow: `none` — the system is flat
- Internal padding: `16px–24px` standard, expanding to `32px+` for hero modules

### Badges / Tags

**Tag Label (Neutral Subtle)**
- Background: `#f5f5f5`
- Text: `#3c3c43`
- Padding: `2px 8px`
- Radius: `0` (sharp rectangle)
- Font: 10px Helvetica Neue, weight 700, line-height 16px

**Tag Label (Filled Beige)**
- Background: `#f4eede`
- Text: `#3c3c43`
- Padding: `2px 8px`
- Radius: `0`
- Font: 10px Helvetica Neue, weight 700
- Use: Promotional and seasonal markers — "新商品", "セール"

### Inputs & Forms
- Background: White (`#ffffff`)
- Border: `1px solid #c4c4c6` default, `1.5px solid #3c3c43` on label/active
- Radius: `4px` (text inputs), `0` (checkbox squares)
- Padding: `12px 16px` typical
- Text colour: `#3c3c43`
- Focus: solid `1.5px #3c3c43` border, no glow

### Navigation
- Top bar: white background, fixed at top, `0` chrome
- Wordmark: `#7f0019` Muji-red rectangular logo, never tinted, never animated
- Primary nav: horizontal row, 14–16px Helvetica Neue 400, `#3c3c43`, sentence case
- Hover: 2px bottom border in `#3c3c43` appears under link
- Utility nav: 12px Helvetica Neue 400, right-aligned (cart, account, store locator)
- Active tab: `2px solid #3c3c43` bottom border

### Links
- Default: `#3c3c43` text, no underline
- Hover: text-decoration underline (no colour change)
- Secondary muted link: `#6d6d72` text, weight 700, hover adds underline

### Switches & Toggles
- Off state: `1px solid #e0ceaa`, `#ffffff` background — beige outline against white
- On state: `1px solid #3c3c43`, ink fill
- The beige border in the off state is one of the few moments the brand's warmth surfaces in a non-typographic way

## 5. Layout Principles

### Spacing System
- Base unit: `8px` (verified — dembrandt reports `scaleType: "8px"`)
- Common scale: `2px`, `4px`, `6px`, `8px`, `10px`, `12px`, `15px`, `16px`, `20px`, `24px`, `48px`, `64px`, `96px`, `100px`
- The most-used values are `8px` (170 occurrences), `4px` (107), and `12px` (74) — small, precise increments stacked into larger compositions

### Grid & Container
- Max content width: ~`1340px` (matches the largest breakpoint)
- Hero: full-bleed imagery with overlaid text columns at ~50% viewport width
- Section content: 12-column grid with consistent `24px` gutters
- Product grid: 4-up desktop, 2-up tablet, scroll-snap horizontal on mobile

### Whitespace Philosophy
- **Catalogue rhythm**: sections separated by `48–96px` vertical padding, never crowded
- **Image anchoring**: product photography sits centered with `24px+` of negative space surrounding it — Muji never edge-bleeds product imagery
- **Tile breathing**: product grids use `16–24px` gutters between cards; cards never touch
- **Ample line-height**: every text block runs at `1.6`, contributing to the calm pacing

### Border Radius Scale
- Sharp (`0`): tags, full-bleed sections, hero containers, checkbox squares
- Soft (`4px`): buttons, inputs, product tiles — the workhorse radius
- Slight-rounded (`10px`): rare — used only for promotional banner panels
- Pill (`9999px`): carousel pagination buttons
- Circular (`50%`): heart/favorite buttons, avatars, switch knobs

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | `box-shadow: none` | Default for every surface — cards, modals, panels at rest |
| Hairline Border (Level 1) | `1px solid #d8d8d9` | Default divider between list items, table rows |
| Active Border (Level 2) | `1.5px solid #3c3c43` | Active or focused control, label highlight |
| Bottom Underline (Level 3) | `0px 0px 2px solid #3c3c43` | Active nav tab indicator, selected link |
| Outline Focus (Level 4) | `outline: 0.0625em solid #ffffff` | Keyboard focus on filled buttons (visible against the ink fill) |

**Shadow Philosophy**: Muji has no drop shadows whatsoever. The `box-shadow` value across every component default state is `none`. Where most retail sites use 4–8 shadow tokens to imply dimensionality, Muji uses zero — its product catalogue aesthetic comes from photography, surface tones, and hairline borders rather than computed lighting. When a control needs to communicate state (active, focused, selected), it does so through colour shift or a thicker border, never blur. The page IS the page; nothing floats above it.

## 7. Do's and Don'ts

### Do
- Use `#ffffff` and `#f4eede` together as the canvas system — alternate sections use cream, content sits on white
- Set body type at `16px` Helvetica Neue with `1.6` line-height for catalogue readability
- Use `#3c3c43` for all primary text — softer than pure black, kinder on long reading
- Default to `4px` radius for buttons, inputs, and product tiles
- Reserve the muji-red (`#7f0019`) for the wordmark only — it is not a CTA color
- Use `1px` hairline borders in `#d8d8d9` for structural dividers
- Keep tag labels rectangular (`0` radius) with `2px 8px` padding
- Use sentence case throughout UI labels, buttons, and navigation
- Stack only two weights — 400 regular and 700 bold — emphasis comes from weight contrast
- Use beige (`#e0ceaa`) for warm-press states (active, on, selected) instead of saturated brand color

### Don't
- Don't add drop shadows to ANY component — Muji is functionally shadow-free
- Don't use the muji-red (`#7f0019`) as a button background — it is a wordmark color, not a CTA
- Don't introduce intermediate weights (300, 500, 600) — the system uses 400 and 700 only
- Don't uppercase navigation or button labels — sentence case is mandatory
- Don't use line-heights below `1.5` for body — the `1.6` rhythm is part of the brand
- Don't overload with chromatic accents — the system is functionally monochromatic on warm cream
- Don't add gradients to surfaces, buttons, or cards — Muji is solid-tint only
- Don't use rounded buttons (`8px+` radius) — the `4px` workhorse is the brand's tactile signature
- Don't bleed product photography to the page edge — Muji always frames imagery with whitespace
- Don't replace Helvetica Neue with a "more modern" grotesk — its banality is the brand

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile S | <600px | Single-column, hamburger nav, horizontal scroll product strips |
| Mobile L | 600–768px | 2-up product grids, condensed nav |
| Tablet | 768–1000px | 3-up grids, primary nav still partially collapsed |
| Desktop | 1000–1340px | Full horizontal nav, 4-up grids |
| Wide Desktop | ≥1340px | Maximum container width, full editorial spacing |

The dembrandt scrape captured 14 distinct breakpoints — Muji uses fine-grained responsive tuning rather than three coarse stops.

### Touch Targets
- Primary buttons: `48px+` tap height via `16px` vertical padding × 2 plus 16px line-height
- Nav links: `44px+` zone in mobile drawer
- Heart / favorite buttons: `40px` minimum diameter
- Tag chips: tappable but secondary — typically inline with body text

### Collapsing Strategy
- **Nav**: Horizontal row collapses to hamburger drawer with cream-tinted full-screen overlay
- **Hero**: Stacks tighter on mobile but maintains image-then-text vertical rhythm
- **Footer**: 4-column desktop layout collapses to vertical accordion with hairline dividers
- **Product grids**: 4-up → 3-up → 2-up → 1-up (or horizontal scroll-snap on smallest viewports)
- **Body type**: stays at `16px` across viewports — Muji never bumps body for mobile

## 9. Agent Prompt Guide

### Quick Reference
- Page Background: `#ffffff` (primary) / `#f4eede` (cream alternate)
- Primary Text: `#3c3c43` (charcoal ink)
- Wordmark: `#7f0019` (muji-red)
- Sale / Error: `#dd0c14`
- Tag Backgrounds: `#f5f5f5` (subtle), `#f4eede` (beige fill)
- Hairline Border: `#d8d8d9`
- Solid Border: `#3c3c43`
- Body Font: `Helvetica Neue, Arial, Noto Sans JP, Hiragino Kaku Gothic ProN, sans-serif`

### Example Component Prompts
- "Create a hero on `#ffffff` with a 26px Helvetica Neue weight-700 heading at line-height 1.15 and 2.4px letter-spacing in `#3c3c43`, a 16px Helvetica Neue weight-400 body paragraph at line-height 1.6, and a primary button: `#3c3c43` background, white text, 16px weight-700, padding 16px 20px, 4px radius, no shadow."
- "Design a product tile on `#ffffff` with `4px` radius, no border, no shadow. Square product image fills the top, then below: 14px Helvetica Neue weight-700 category caption in `#3c3c43`, 16px weight-700 product name (line-height 1.6), and a 16px weight-400 price."
- "Create a tag chip — `#f5f5f5` background, `#3c3c43` text, 10px Helvetica Neue weight-700, line-height 16px, padding `2px 8px`, `0` radius (sharp rectangle), sentence case."
- "Build a navigation bar on `#ffffff` with the muji-red logo (`#7f0019`) on the left, a horizontal row of 14px Helvetica Neue weight-400 links in `#3c3c43`, and a 2px bottom border in `#3c3c43` indicating the active section. Sentence case throughout."
- "Design a form input — `#ffffff` background, `1px solid #c4c4c6` border, `4px` radius, padding `12px 16px`, 16px Helvetica Neue weight-400 in `#3c3c43`. On focus: `1.5px solid #3c3c43`, no glow, no shadow."

### Iteration Guide
1. Default to one typeface only: Helvetica Neue with the Japanese fallback chain. No specialty fonts.
2. Stack only weight 400 and weight 700 — emphasis comes from bold, never from intermediate weights.
3. Body type is `16px` at `1.6` line-height. Don't shrink for "editorial density" — Muji is a catalogue.
4. Use sentence case for every label, button, nav item, and tab. Uppercase is wrong.
5. Border-radius is binary: `4px` for buttons/inputs/tiles, `0` for tags, `50%`/`9999px` for circular elements only.
6. The page palette is white + cream (`#ffffff` + `#f4eede`). Pure grey backgrounds are wrong.
7. Drop shadows do not exist in this system. Use `1px` borders or surface-tone shifts to communicate depth.
8. The muji-red (`#7f0019`) is the wordmark color — never a button background or accent.
9. When a control needs warmth, use beige (`#e0ceaa` or `#f4eede`) — never coral, peach, or pink.
10. Section padding stays generous: `48px+` between content blocks. Pages should feel like a printed catalogue.
