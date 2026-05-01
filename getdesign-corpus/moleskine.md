---
slug: moleskine
name: Moleskine
url: https://www.moleskine.com
domain: moleskine.com
category: Retail
styles: [Light, Minimal, Editorial]
tagline: "Pencil-lead text on cream paper, signature warm orange CTA, composition-notebook chrome and a single typeface carrying every page"
fonts: [CustomJapFont, Brandon Grotesque]
primary_color: "#fb663a"
---

# Design System Inspired by Moleskine

> Pencil-lead text on cream paper, signature warm orange CTA, composition-notebook chrome and a single typeface carrying every page

## 1. Visual Theme & Atmosphere

The Moleskine site is a notebook brand on the web — and the design system reads exactly like that. The canvas is a soft cream paper (`#f4f2ef`) and pure white (`#ffffff`) with deep pencil-lead text (`#211d1d`) — not pure black, but a warmed dark brown-grey that feels like graphite on paper. Every page is anchored by a single chromatic note: a saturated tangerine-orange (`#fb663a`) that powers the brand's primary CTAs, the underlines under hovered links, and the small "new" badges scattered through product grids. There are no gradients, just a few extremely subtle drop shadows on modal containers, and zero ornamental graphics — the brand trusts paper photography and a single grotesk to carry the chrome.

What makes Moleskine unmistakable on the web is the **single-typeface uniformity**. The dembrandt scrape captured every text style using the same custom face (labeled `CustomJapFont` in the stylesheet — likely Moleskine's bespoke variant of a Brandon-Grotesque-class humanist sans, with `Brandon Grotesque, Helvetica` as the fallback chain). Headings, body, navigation, buttons, and captions all share this one face — the system stacks emphasis through weight (300, 400, 500, 700, 900) rather than typeface contrast. Body text sits at 16px line-height 1.5; section headings at 24–28px; the largest hero at 60px (`3.75rem`). It reads like a notebook brand publishing copy in its house style — clean, even, well-cased.

The third defining trait is **composition-notebook chrome**. Border-radius defaults to `4px` on buttons and inputs (the workhorse), with `0` reserved for sharp panels and `2px` for cookie-banner-style micro-buttons. Most surfaces use `0` borders or hairline `1px` strokes in `#a6a4a4` and `#5a5858`. Shadows exist but are barely there — the production scrape captured five low-confidence shadow values, all subtle (`rgba(0, 0, 0, 0.5) 0px 2px 4px 0px` and lighter), reserved for modal containers and lifted slick-carousel buttons. Imagery tracks the brand: paper craft, notebook covers shot at `4:3`, hand-illustration mixed with photography. The aesthetic is Italian stationery brand translated to a polite Bootstrap-driven retail site.

**Key Characteristics:**
- Cream paper canvas (`#f4f2ef`) and white (`#ffffff`) — paper, never neutral grey
- Pencil-lead text (`#211d1d`) — warmed dark, not pure black, signature graphite-on-paper feel
- Single-typeface system — CustomJapFont (Brandon Grotesque variant), 5 weights (300, 400, 500, 700, 900)
- Signature tangerine orange (`#fb663a`) — the only brand-saturated accent, used for CTAs and "new" tags
- Body type at 16px line-height 1.5, hero up to 60px
- Border-radius is `4px` (buttons, inputs, cards) — friendly but not over-rounded
- Hairline borders in `#a6a4a4` and `#5a5858` — composition-notebook gauge
- Subtle low-opacity shadows on modals only — never on cards or buttons
- Pill-rounded badges (`24px` radius) for product tags — soft, paper-sticker feel
- Bootstrap-grid foundation (verified — `Bootstrap, container + row + col` framework hint)

## 2. Color Palette & Roles

### Primary Brand
- **Moleskine Orange** (`#fb663a`): The signature tangerine — used for primary button backgrounds, hovered link underlines, "new product" tag icons, and the brand's chromatic signal. Saturated but warm; reads as embossed orange on paper rather than digital alert.

### Brand Accent
- **Pencil Lead** (`#211d1d`): The deep brand near-black — used for primary text, button outlines, masthead background. The signature warmed dark.
- **Cream Paper** (`#f4f2ef`): The brand surface — used for alternate sections, badge backgrounds, alternate cards. Reads as unbleached paper.
- **Brick Red** (`#d73604`) /* derived from button border in scrape */: Used as the destructive / cancel / cookie-deny button color — distinguishable from primary orange.

### Text Scale
- **Pencil Lead** (`#211d1d`): Primary text and headings — confirmed dominant in scrape (1,176 occurrences).
- **Bootstrap Body** (`#212529`): Default body fallback — Bootstrap's neutral text token, used in long-form descriptions.
- **Mid Slate** (`#5a5858`): Secondary text, captions, meta labels (47 occurrences).
- **Caption Brown** (`#54544f`): Tag-text and footer-style muted tone — warmer than mid slate.
- **Faint Border** (`#a6a4a4`) /* from border scrape */: Tertiary outline color for ghost buttons.

### Surface & Background
- **Pure White** (`#ffffff`): The primary product card and module surface (317 occurrences in scrape).
- **Cream Paper** (`#f4f2ef`): The signature warm surface (281 occurrences) — used for alternate sections, badge fills, secondary panels.
- **Inverted Lead** (`#211d1d`): The dark masthead, footer, and inverse hero sections.

### Borders & Dividers
- **Soft Stroke** (`1px solid #a6a4a4`): Default secondary button outline (23 occurrences in scrape).
- **Pencil Stroke** (`1px solid #211d1d`): Primary button border, masthead bottom rule.
- **Mid Stroke** (`1px solid #5a5858`): Default input border, label bottom-rule.
- **Tag Stroke** (`1px solid #fb663a`): Orange-bordered alert tags (rare but in palette).
- **Faint Cream** (`1px solid #f4f2ef`): Cream-on-cream layering for subtle module separation.

### Shadow System
- **Subtle Drop** (`rgba(0, 0, 0, 0.5) 0px 2px 4px 0px`): Used on modal containers and lifted slick-carousel arrows. The deepest shadow in the system, but still low-opacity.
- **Glow Halo** (`rgba(0, 0, 0, 0.2) 0px 0px 18px 0px`): Used for emphasis dialogs, popovers — extremely soft, almost ambient.
- **Tile Lift** (`rgb(199, 197, 199) 0px 0px 12px 2px`): Reserved for hovered product tiles in some carousel contexts — paper-like soft lift.
- **Inverse Highlight** (`rgb(199, 197, 199) -3px -3px 5px -2px`): A negative-direction shadow used on inset paper elements.

The shadow scale is intentionally restrained — Moleskine never uses harsh dropshadows on cards or buttons. Paper-like soft lifts only.

## 3. Typography Rules

### Font Family
- **Primary**: `CustomJapFont`, fallback chain: `CustomCyrFont, "Brandon Grotesque", Helvetica, Arial, sans-serif`
- **Loading source**: Self-hosted custom face — neither Google Fonts nor Adobe Fonts, neither variable nor system. The `CustomJapFont` / `CustomCyrFont` names suggest separately-tuned variants for Latin, Japanese, and Cyrillic glyph coverage, all delivered from Moleskine's CDN.
- **External substitution**: Use **Brandon Grotesque** if licensed, otherwise **Inter** or **Hanken Grotesk** as commercial-grade substitutes. The face has Brandon Grotesque's slightly humanist round terminals.

The single-family approach is part of the brand identity: Moleskine uses one typeface for every word on every page.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Hero / H1 | CustomJapFont | 60px (3.75rem) | 500 | 1.00 | normal | none | Largest editorial heading — campaign hero |
| Display H1 | CustomJapFont | 48px (3rem) | 400 | 0.67 | normal | none | Sub-hero display — extreme tight line-height for compressed display |
| Section H1 | CustomJapFont | 28px (1.75rem) | 500 | 0.64 | normal | none | Category and section openers |
| Sub Heading | CustomJapFont | 25px (1.56rem) | 400 | 0.96 | normal | none | Secondary section headings |
| Card Title (large) | CustomJapFont | 24px (1.5rem) | 500 | 1.00 | normal | none | Featured-card titles — heavier weight, tight line |
| Article Title (heavy) | CustomJapFont | 24px (1.5rem) | 900 | 1.00 | normal | none | Editorial spotlights — black weight emphasis |
| Card Subtitle | CustomJapFont | 22px (1.38rem) | 500 | 1.45 | normal | none | Card description, comfortable line-height |
| Body Heading | CustomJapFont | 20px (1.25rem) | 700 | 1.40 | normal | none | In-body H2/H3 — emphasized weight |
| Body Title | CustomJapFont | 20px (1.25rem) | 500 | 1.40 | normal | none | Standard body heading |
| Body Title (light) | CustomJapFont | 20px (1.25rem) | 400 | 1.40 | normal | none | Quieter body title |
| Featured Link | CustomJapFont | 18px (1.13rem) | 500 | 1.33 | normal | none | Editorial card links |
| Body | CustomJapFont | 16px (1rem) | 400 | 1.50 | normal | none | Default long-form body |
| Body Bold | CustomJapFont | 16px (1rem) | 500 | 1.50 | normal | none | Emphasized body, button labels |
| Button (compact) | CustomJapFont | 16px (1rem) | 500 | 1.00 | 0.16px | capitalize | Compact CTAs and bento buttons |
| Caption | CustomJapFont | 14px (0.88rem) | 400 | 1.43 | normal | none | Image captions, meta |
| Caption Bold | CustomJapFont | 14px (0.88rem) | 700 | 1.40 | normal | none | Eyebrow-style emphasized caption |
| UI Eyebrow | CustomJapFont | 14.4px (0.9rem) | 700 | 1.00 | 0.144px | none | Section eyebrow above headings |
| Footer Caption | CustomJapFont | 13.008px (0.81rem) | 400 | 1.50 | normal | none | Footer micro-copy |
| Cookie Button | CustomJapFont | 13.008px (0.81rem) | 600 | 1.20 | 0.13px | none | Cookie-banner CTAs |
| Footer Micro | CustomJapFont | 12px (0.75rem) | 400 | 1.40 | normal | none | Footer chrome |
| Caps Eyebrow | CustomJapFont | 12px (0.75rem) | 700 | 1.00 | 0.96px (0.08em) | none | Tiny letter-spaced eyebrow above campaigns |
| Tag / Badge Text | CustomJapFont | 14px (0.88rem) | 400 | 32px | normal | none | Pill-tag text |

### Principles
- **One typeface, five weights**: 300, 400, 500, 700, 900 — emphasis comes from weight escalation, the system uses the full weight ladder
- **Capitalize for compact buttons**: Bento-grid buttons use `text-transform: capitalize` (the only systematic case modification) — gives the CTA a slightly book-cover feel
- **Tight line-height on display**: Hero sizes (48–60px) use `0.67` and `1.00` line-height — visually impactful, condensed display
- **Generous line-height on body**: 16px body sits at `1.5`, captions at `1.4–1.5` — the system trusts readers with the spacing
- **Letter-spacing only on caps eyebrows**: Two specific tokens use letter-spacing (`0.96px` on 12px caps eyebrow, `0.144px` on 14.4px UI eyebrow) — everywhere else is normal tracking
- **No italics**: The system uses no italics anywhere — emphasis is via weight (700, 900) only

## 4. Component Stylings

### Buttons

**Primary (Solid Pencil Lead)**
- Background: `#211d1d`
- Text: `#ffffff`
- Padding: `0px 16px` (vertical centering via line-height)
- Radius: `4px`
- Border: `1px solid #211d1d`
- Font: 20px CustomJapFont weight 500
- Hover: background shifts to `#1eaedb` (a sky-blue hover — Moleskine's secondary chromatic), opacity `0.9`
- Use: Primary CTAs — "Add to cart", "Buy now", "Continue"

**Primary (Orange Brand)**
- Background: `#fb663a`
- Text: `#ffffff`
- Padding: `0px 16px`
- Radius: `4px`
- Border: `1px solid #211d1d`
- Font: 20px CustomJapFont weight 500
- Hover: background inverts to `#ffffff`, text shifts to `#2285f7`, border to `#fb663a`
- Use: The brand's signature warm CTA — featured product launches, hero CTAs

**Secondary (White / Outline)**
- Background: `#ffffff`
- Text: `#211d1d`
- Padding: `0px 16px`
- Radius: `4px`
- Border: `0px` or `1px solid #ffffff`
- Font: 20px CustomJapFont weight 500
- Use: Inverse CTAs on dark surfaces, secondary navigation

**Outline (Ghost)**
- Background: `transparent`
- Text: `#211d1d`
- Border: `1px solid #211d1d`
- Padding: `0px 16px 0px 8px` (asymmetric — slightly tighter on left)
- Radius: `4px`
- Hover: background fills white, text shifts to a hover-blue, opacity `0.6`, border shifts to orange
- Active: background fills with `#2c6415` (deep green press state), white text
- Use: Tertiary outlined CTAs

**Cookie / Brick Red**
- Background: `#d73604` (or transparent inverse)
- Text: `#ffffff`
- Border: `1px solid #d73604`
- Padding: `12px 10px`
- Radius: `2px` (tighter — cookie-banner UI convention)
- Font: 13px CustomJapFont weight 600, letter-spacing 0.13px
- Use: Cookie-banner deny / destructive actions

**Slide / Slick Carousel Round**
- Background: `#ffffff`
- Text: `#000`
- Border: `0`
- Radius: `100%` (perfect circle)
- Padding: `0`
- Use: Carousel arrow buttons

### Cards & Containers
- Background: `#ffffff` default; `#f4f2ef` (cream) on alternate sections
- Border: `0` default; `1px solid #a6a4a4` for ghost-card outlines
- Radius: `4px` for product cards, `8px` for bento modals, `0` for full-bleed sections
- Shadow: typically `none`, occasional `rgb(199, 197, 199) 0px 0px 12px 2px` for hover-lifted tiles
- Internal padding: `16–24px` standard, `32px+` for editorial features

### Badges / Tags

**Product Tag (Pill)**
- Background: `#f4f2ef` (cream)
- Text: `#54544f` (caption brown)
- Padding: `0px 8px`
- Radius: `24px` (pill — distinctly rounded)
- Border: `0`
- Font: 14px CustomJapFont weight 400, line-height 32px
- Use: Product category tags, attribute markers

**New / Hot Tag (Orange)**
- Background: `#fb663a`
- Text: `#ffffff`
- Padding: `0px 8px`
- Radius: `24px`
- Font: 14px CustomJapFont weight 400
- Use: "NEW" markers, limited-edition badges

### Inputs & Forms

**Text Input**
- Background: `transparent`
- Border: `0px none` default; `1px solid #5a5858` on focus
- Border-radius: `4px`
- Padding: `9px 16px`
- Font: 16px CustomJapFont weight 400 in `#211d1d`
- Focus: background fills `#1eaedb` (sky blue), text shifts to white — striking but verified in scrape
- Use: Email, password fields

**Checkbox**
- Background: transparent
- Border: `1px solid #5a5858`
- Radius: `0` (square)
- Focus: orange `0 0 0 0.25rem rgba(251, 102, 58, 0.25)` glow halo

### Navigation
- Top bar: `#211d1d` (lead-black) background, `#ffffff` logo and links
- Wordmark: white logo on dark masthead — composition-notebook cover feel
- Primary nav: 14–16px CustomJapFont weight 500, `#ffffff`, sentence case
- Hover: text underlines, color shifts to `#3860be` (deep brand blue secondary)
- Mobile: collapses to hamburger drawer with full-screen white overlay

### Decorative Elements
- **Pill Tags**: 24px-radius pill chips for product attributes — paper-sticker feel
- **Composition Hairlines**: `1px solid #a6a4a4` strokes between list items, behaving like a notebook's printed gauge lines
- **Orange Underline**: hovered editorial links get a `2px` orange (`#fb663a`) underline — the brand's hover signature

## 5. Layout Principles

### Spacing System
- Base unit: `8px` (verified — `scaleType: "8px"`)
- Common scale: `4px`, `8px`, `10px`, `12px`, `16px`, `24px`, `32px`, `40px`, `56px`, `80px`, `160px`
- Most-used: `24px` (210 occurrences), `16px` (171), `8px` (135), `4px` (106) — a tight foundation built on multiples of 8

### Grid & Container
- Bootstrap-based grid (verified — `container + row + col` evidence)
- Max content width: implied `1200px` standard Bootstrap container, expanding to `1440px` for wide hero modules
- Hero: full-bleed photography with overlaid display text at 48–60px
- Product grid: 4-up desktop with `24px` gutters, scaling to 2-up on tablet, 1-up on mobile
- Footer: 4-column desktop layout, vertical accordion on mobile

### Whitespace Philosophy
- **Notebook breathing**: sections separated by `40–80px` vertical padding — comfortable but not extravagant
- **Image isolation**: product photography sits with `16–24px` of negative space surrounding it; never edge-to-edge unless intentionally hero
- **Tile rhythm**: product grids use uniform `24px` gutters; tiles never touch
- **Generous body line-height**: every text block runs at `1.4–1.5`, contributing to the calm pacing

### Border Radius Scale
- Sharp (`0`): full-bleed sections, hero modules
- Slight (`1–2px`): cookie-banner buttons, micro-UI
- Soft (`4px`): the workhorse — buttons, inputs, product tiles
- Comfortable (`8px`): bento modal corners, larger card containers
- Pill (`24px`): product attribute tags
- Circular (`50%`, `100%`): carousel arrows, avatars, heart buttons

The system uses radii deliberately — `4px` is the workhorse, `24px` for pill tags, and `0`/`50%`/`100%` for edge cases. No 12–20px values appear.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | `box-shadow: none` | Default for cards, buttons, modules at rest |
| Hairline Border (Level 1) | `1px solid #a6a4a4` | Default secondary card and button outline |
| Subtle Modal Drop (Level 2) | `rgba(0, 0, 0, 0.5) 0px 2px 4px 0px` | Modal containers, popovers |
| Soft Glow Halo (Level 3) | `rgba(0, 0, 0, 0.2) 0px 0px 18px 0px` | Dialog emphasis, lightbox containers |
| Hover Tile Lift (Level 4) | `rgb(199, 197, 199) 0px 0px 12px 2px` | Hovered product tiles in carousels |
| Focus Glow (Level 5) | `rgba(251, 102, 58, 0.25) 0px 0px 0px 0.25rem` | Keyboard-focus ring on inputs and primary buttons — the orange focus glow |

**Shadow Philosophy**: Moleskine uses shadows sparingly and softly. The default state of every card and button is flat — cards never have ambient elevation. The system's only consistent shadow is the orange focus-glow halo (`rgba(251, 102, 58, 0.25)`) which appears on inputs and primary buttons during keyboard focus — distinctively the brand color, even in interaction feedback. Where competitor stationery brands lean into harder drop shadows for "premium" feel, Moleskine achieves restraint with `1px` borders and the very occasional soft modal lift. The page reads like paper, not floating UI.

## 7. Do's and Don'ts

### Do
- Use `#ffffff` and `#f4f2ef` (cream paper) together as the canvas system — alternate sections use cream
- Set body type at `16px` CustomJapFont (or Brandon Grotesque substitute) with `1.5` line-height
- Use `#211d1d` (pencil lead) for primary text — softer than pure black, signature warmth
- Reserve the brand orange (`#fb663a`) for primary CTAs and "new" badges only — its rarity is its power
- Default to `4px` radius for buttons, inputs, and product tiles
- Use `24px` radius for pill-style product tags
- Stack emphasis through weight (300, 400, 500, 700, 900) — the system uses the full weight ladder
- Use the orange focus-glow halo (`rgba(251, 102, 58, 0.25) 0 0 0 0.25rem`) for keyboard focus states
- Keep card and button shadows at `none` by default — only modals and lifted tiles get subtle elevation
- Include `text-transform: capitalize` on bento-grid CTAs — distinctive Moleskine casing

### Don't
- Don't add hard drop shadows to cards or buttons — the system is flat by default
- Don't introduce a secondary typeface — Moleskine uses one face (CustomJapFont / Brandon Grotesque) for everything
- Don't use saturated chromatic accents beyond the brand orange — the system is functionally monochrome on cream + the single orange note
- Don't use `border-radius` above `8px` for cards — the workhorse is `4px`
- Don't set body line-height below `1.4` — the breathing room is part of the brand
- Don't use pure black `#000` for text — pencil-lead `#211d1d` is the brand's warmed dark
- Don't apply uppercase to body or button text — capitalization is rare and reserved for compact bento CTAs only
- Don't bleed product photography to page edges — Moleskine always frames imagery with whitespace
- Don't introduce sky-blue (`#1eaedb`) as a chromatic accent — it appears only as button hover state, not as a brand color
- Don't crowd the spacing scale — the brand uses `8/16/24/40/80` rhythm, not arbitrary in-between values

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile XS | <375px | Single-column, hamburger nav, condensed cards |
| Mobile S | 375–500px | Larger cards, primary CTAs full-width |
| Mobile L | 500–768px | 2-up product grids begin |
| Tablet | 768–1024px | 3-up grids, partial nav expansion |
| Desktop | 1024–1440px | Full horizontal nav, 4-up product grids |
| Wide | ≥1440px | Maximum container width, expanded margins |

The dembrandt scrape captured 21 distinct breakpoints from 98px to 1600px — Moleskine uses fine-grained responsive tuning (a Bootstrap-grid hallmark).

### Touch Targets
- Primary buttons: `48px+` tap height via line-height + padding combination
- Pill tags: `32px` line-height ensures comfortable tap zones
- Nav links: `44px+` minimum in mobile drawer
- Carousel arrows: `40px+` circular targets

### Collapsing Strategy
- **Nav**: Horizontal row collapses to hamburger; full-screen white overlay with vertical CustomJapFont stack
- **Hero**: Stacks tighter on mobile; display sizes scale `60px → 32px`
- **Footer**: 4-column desktop layout collapses to vertical accordion with `1px solid #d8d8d8` dividers
- **Product grid**: 4-up → 3-up → 2-up → 1-up with `24px` gutters scaling to `16px`
- **Body type**: stays at `16px` regardless of viewport

## 9. Agent Prompt Guide

### Quick Reference
- Page Background: `#ffffff` (white) / `#f4f2ef` (cream paper alternate)
- Primary Text: `#211d1d` (pencil lead)
- Brand CTA: `#fb663a` (Moleskine orange)
- Secondary Text: `#5a5858` / `#54544f`
- Hairline Border: `#a6a4a4`
- Pencil Border: `#211d1d`
- Focus Glow: `rgba(251, 102, 58, 0.25) 0 0 0 0.25rem`
- Body Font: `CustomJapFont, "Brandon Grotesque", Helvetica, sans-serif`

### Example Component Prompts
- "Create a product card on `#ffffff` with `4px` radius, no border, no shadow. Square product image at top. Below: 14px CustomJapFont weight 400 in `#54544f` with `24px` pill radius cream background tag (`#f4f2ef`), then a 16px weight 500 product name in `#211d1d`, and a 16px weight 400 price."
- "Design a primary CTA — `#fb663a` background, white text, 20px CustomJapFont weight 500, padding 0px 16px (line-height-padded), `4px` radius, `1px solid #211d1d` border. On focus: add a `0 0 0 0.25rem rgba(251, 102, 58, 0.25)` orange glow halo."
- "Build a navigation bar with `#211d1d` (pencil lead) background, white CustomJapFont 16px weight 500 links, sentence case. Hover: text gains underline, color shifts subtly. Mobile collapses to hamburger drawer with full-screen white overlay."
- "Create a pill tag — `#f4f2ef` cream background, `#54544f` text, 14px CustomJapFont weight 400, line-height 32px, padding `0 8px`, `24px` radius (full pill), no border. Use for product attributes like 'Hardcover', 'Lined', 'Pocket'."
- "Design an article hero — `#ffffff` background with full-bleed photography, then a 48px CustomJapFont weight 400 display title at line-height 0.67 (compressed) in `#211d1d`. Below: an `8px` orange (`#fb663a`) accent bar of `40px` width, then 18px CustomJapFont weight 500 lede in `#211d1d` at line-height 1.33."

### Iteration Guide
1. Default to one typeface only: CustomJapFont (or Brandon Grotesque substitute). No secondary face.
2. Stack emphasis through weight — the system uses 300, 400, 500, 700, 900. Reach for weight, not a different font.
3. Body type is `16px` at `1.5` line-height. Captions step down to `14px` at `1.4`.
4. Border-radius is `4px` for the workhorse (buttons, inputs, cards), `24px` for pill tags, `0` for full-bleed sections.
5. The page palette is white + cream (`#ffffff` + `#f4f2ef`). Pure grey backgrounds are wrong.
6. The brand orange (`#fb663a`) is sacred — primary CTAs, "new" tags, focus halos only. Never decorative.
7. Drop shadows are minimal — only modals and lifted tiles get them. Cards and buttons stay flat.
8. Use the orange focus glow (`rgba(251, 102, 58, 0.25) 0 0 0 0.25rem`) for keyboard accessibility — it's both functional and brand-true.
9. Pencil-lead `#211d1d` is the text color, not pure `#000`. The warm-dark IS the brand.
10. Bootstrap grid foundation — use `container + row + col` rhythm and 8-px-multiple spacing throughout.
