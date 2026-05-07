---
version: alpha
name: "Glossier"
description: "Token-first design system reference for Glossier."

colors:
  background: "#ffffff"
  surface: "#f6e3e6"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#f94200"
  primary: "#ffffff"
  on-primary: "#ffffff"
  border: "#e8e8e8"
  focus-ring: "#ffffff"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Apercu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 360px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Apercu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 251px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Apercu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Apercu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Apercu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Apercu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Apercu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Apercu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
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

# Glossier Design System

## Overview

Glossier's website is the canonical "millennial DTC beauty" interface — an aesthetic this brand effectively defined and that everyone else has been copying for ten years. The page opens on stark pure white (`#ffffff`) framing oversized photography, switches to a signature soft pink (`#f6e3e6`) for the footer and select panels, and trusts a single neo-grotesque (`Apercu`) to do every typographic job from product names to checkout. There are no gradients, no shadows, no chrome — just paper-clean surfaces, generous space, and product photography that has been styled to within a millimeter of its life.

The defining quality is what's *missing*. Glossier strips out all visual noise that competitor beauty brands lean on: no gold foil flourishes, no serif "luxe" type, no editorial gradients, no decorative ornaments. What's left is a hyper-feminine minimalism that codes as "the cool girl who barely tried" — every surface flat, every corner sharp at `0px` radius, every button a plain rectangle in `#e8e8e8` or pure white with a 1px black border. The brand color (millennial pink) is rationed almost as carefully as Cape rations its lavender: it shows up as the secondary semantic surface, in the footer, in occasional content panels, and in product packaging photography — never as a button or accent on the main canvas.

Where the system gets interesting is the **promo bar** — a saturated vermillion (`#f94200`) strip pinned to the top of the page that breaks the otherwise mono-pink-white palette with one burst of zero-restraint chromatic energy. It's the visual equivalent of a lipstick smudge on a clean white tee: deliberately loud, deliberately on-brand. Combined with the colossal "Glossier" wordmark that anchors the hero (set in Apercu at near-viewport scale), the system communicates a brand that's so confident in its identity it refuses to dress up.

**Key Characteristics:**
- Apercu (with Apercu Pro and Apercu Mono variants) — the only typeface, every weight, every size
- Pure white (`#ffffff`) as primary canvas — no off-white, no warm paper tones
- Glossier Pink (`#f6e3e6`) as secondary surface — footer, content panels, packaging adjacency
- Vermillion (`#f94200`) promo bar — the only saturated chromatic accent, used once per page
- Sharp 0-radius corners on every button, card, and container
- 1px black borders as the workhorse separator (`#000000`) — paired with 1px `#e8e8e8` on inputs
- Massive typographic moments — wordmark scaling to multi-hundred px on hero
- Photography-led layouts — product shots fill cards, faces fill heroes, no illustration ever
- Zero shadows on the primary surface — flatness is the brand
- 8px spacing baseline with a tight rhythm in the chrome (1px, 4px, 8px) and big leaps for sections (40px, 46px, 125px)

## Colors

### Primary
- **Glossier Black** (`#000000`): Primary text, headings, body, all icon strokes, button text on light surfaces, 1px borders. Pure black — no softening, no near-black neutral.
- **Pure White** (`#ffffff`): Primary page background, card surfaces, button fills on light promo zones. The default canvas.
- **Glossier Pink** (`#f6e3e6`): The signature secondary surface — footer, promotional content panels, occasional card backgrounds. The brand color, used as a *surface*, never as type or stroke.

### Brand Accents
- **Vermillion Promo** (`#f94200`): The signature top-bar attention color. Appears once on the page, wraps from edge to edge, holds white type. Reserved for limited-time offers, sale messaging, "Free Shipping" announcements.
- **Promo White** (`#ffffff`): Type and icon color when sitting on Vermillion or pink surfaces.

### Neutrals & Text
- **Glossier Black** (`#000000`): All primary text — headings, body, nav, button labels.
- **Mid Gray** (`#666666`): Secondary metadata, sub-labels, video player chrome, form helper text.
- **Light Surface Gray** (`#f7f7f7`): Tertiary panel surface, hover state on white CTAs, "soft pressed" feedback.
- **Button Gray** (`#e8e8e8`): Default fill for low-emphasis buttons — the "neutral CTA" surface that lets a product photo dominate.

### Surface & Borders
- **Surface White** (`#ffffff`): Default panel and card background.
- **Surface Pink** (`#f6e3e6`): Tinted-section background — footer, brand-moment panels.
- **Border Black** (`#000000`): 1px solid borders on outline buttons, dropdown selects, primary form controls.
- **Border Soft** (`#e8e8e8`): 1px solid borders on text inputs, modals, low-emphasis dividers.
- **Border Hairline** (`rgba(0, 0, 0, 0.06)`): Decorative `1px 0px 0px` top borders on list items and stacked rows.

### Shadow Colors
- The system is **almost shadow-free**. The handful of shadows that exist are 1-count edge effects (`rgba(0,0,0,0.05) 0px -1px 0px 0px` for promo bar separation, `rgba(199,197,199) 0px 0px 12px 2px` for an isolated product callout). Treat shadows as not-in-system — flatness is the rule.

### Gradient System
- Glossier is **gradient-free**. No fills, no chrome, no soft transitions. Every color is a flat solid. This is non-negotiable — the second a gradient appears, the brand reads as a knockoff.

## Typography

### Font Family
- **Primary**: `Apercu`, with fallback `Gill Sans`
- **Display / Pro**: `Apercu Pro`, with fallback `Helvetica, Arial`
- **Monospace / Technical**: `Apercu Mono` — used for technical labels, ingredient lists, footer micro-copy, sometimes price chrome
- **OpenType Features**: Standard ligatures only. No swashes, no stylistic alternates.

*Note: Apercu is a commercial typeface from Colophon Foundry. For external implementations, GT America or Söhne serve as close substitutes; Inter Tight or Manrope work as web-safe alternatives.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Wordmark Hero | Apercu | 240–360px | 500 | 0.85 | -0.02em | Massive "Glossier" mark — fills the viewport on hero moments |
| Display Large | Apercu | 56px (3.50rem) | 500 | 1.05 | -0.01em | Section titles, brand statements |
| Display | Apercu | 40px (2.50rem) | 500 | 1.10 | normal | Feature heads, "Glossier you." style brand moments |
| Heading 1 | Apercu | 32px (2.00rem) | 500 | 1.09 | normal | Page-level titles, often UPPERCASE on collection heads |
| Heading 1 (Pro) | Apercu Pro | 32px (2.00rem) | 400 | 1.10 | normal | Editorial heading variant — softer than the 500 weight |
| Heading 2 | Apercu | 20px (1.25rem) | 400 | 1.40 | normal | Sub-section heads, product card titles |
| Body Large | Apercu | 18–20px | 400 | 1.40 | normal | Intro paragraphs, product descriptions |
| Body | Apercu | 16px (1.00rem) | 400 | 1.50 | normal | Standard reading text, footer columns |
| Link | Apercu | 16px (1.00rem) | 400 | 1.15 | normal | Inline links, footer links — black, often underlined on hover |
| Button | Apercu | 16px (1.00rem) | 400 | 1.23 | 0.03px | Primary button labels — sentence case, not uppercase |
| Button Bold | Apercu | 16px (1.00rem) | 700 | 1.50 | normal | Emphasized button variant — used sparingly |
| Caption | Apercu | 14px (0.88rem) | 400 | 1.35 | 0.05em | Metadata, legal, form helper text |
| Mono Label | Apercu Mono | 12–14px | 400 | 1.20 | 0.05em | Technical chrome — ingredient lists, SKU IDs, footer micro |

### Principles
- **Apercu is non-negotiable**: Every single piece of type on the site is Apercu (or Apercu Pro / Apercu Mono). No serif anywhere, no display oddities, no script. The typeface IS the brand voice.
- **Weight 400 is the default**: Body, links, buttons, nav — all run at 400. Weight 500 is reserved for headings; weight 700 for the rare emphasized inline word or alternate button. The system rarely needs more than two weights on a screen.
- **Sentence case for buttons**: Buttons read "Add to bag", "Shop now", "Find your shade" — not "ADD TO BAG". This is the millennial-friendly signal that separates Glossier from the all-caps luxury beauty conventions.
- **Uppercase reserved for collection titles**: When uppercase appears (collection headers, "FREE SHIPPING" promos, "NEW" badges), it's at small-to-mid sizes (12–16px) with light tracking (`0.03–0.05em`).
- **Tight display line-height**: Heading line-height runs 1.05–1.10 on large display sizes, locking the wordmark hero into a tight visual block that almost reads as a logo even when set in plain Apercu.
- **No negative tracking on body**: Below 24px, letter-spacing returns to default — the legibility-first decision that lets product copy feel approachable.

## Layout

### Spacing System
- Base unit: 8px (with 1px and 4px as compact sub-units for tight UI chrome)
- Scale: 1px, 4px, 8px, 10px, 15px, 16px, 24px, 40px, 46px, 125px
- Notable: The scale has a tight chrome cluster (1px, 4px, 8px appear in the highest counts — for borders, fine padding, and grid gutters) and a wide pacing range (40–125px) for section breaks. Mid values (12px, 18px, 20px) are used sparingly — Glossier prefers committing to either tight or wide.

### Grid & Container
- Max content width: approximately 1280–1400px depending on section
- Hero: full-bleed photography with overlaid wordmark, no container constraint
- Product grid: 4 columns at desktop, 2 columns at tablet, 1 at mobile
- Footer: 4–5 column link grid on `#f6e3e6` pink, full-bleed
- Content blocks regularly break the container for full-bleed photography or pink surface moments

### Whitespace Philosophy
- **Editorial sparseness**: Each major section gets 80–125px of vertical breathing room — Glossier reads like a fashion editorial, not a product catalog
- **Tight grid, loose section**: Inside a product grid, gutters are 8–16px (tight). Between sections, spacing jumps to 80px+ (loose). This creates dense pockets of content separated by oxygen.
- **Photograph as breath**: Where other systems use whitespace alone to pace, Glossier alternates white canvas with full-bleed photography — the imagery itself functions as a visual rest stop

### Border Radius Scale
- Sharp (0px): Default for buttons, cards, containers, badges, modals — the workhorse radius and brand signature
- Near-Sharp (2px): Occasional soft edge on form inputs, cookie controls, marginal UI
- Soft (17–20px): Reserved exclusively for tertiary chrome (cookie banner filters, internal modal pills) — should NOT appear in the primary visual system
- No mid-range radii: The brand-facing system is binary — sharp `0px` or absent. If you find yourself reaching for `8px` or `12px`, you've left the brand.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no inset, no border | Page canvas, body text, product cards, the default |
| Hairline (Level 1) | `1px solid #000000` or `1px solid #e8e8e8` | Form inputs, outline buttons, dividers — graphic separation, not depth |
| Tinted Surface (Level 2) | Solid `#f6e3e6` or `#f7f7f7` background block | Footer, brand panels, hover-state surfaces — chromatic separation, not elevation |
| Edge Shadow (Level 3, rare) | `rgba(0,0,0,0.05) 0px -1px 0px 0px` | Sticky promo-bar separation only — used to lock the bar against the page |
| Soft Glow (Level 4, exception) | `rgb(199,197,199) 0px 0px 12px 2px` | Isolated product moment / badge callout — should be considered out-of-system unless deliberately deployed |

**Shadow Philosophy**: Glossier's depth system is essentially "there is no depth." The flatness is the brand. Where competitor beauty sites pile on drop shadows to suggest luxe physicality (perfume bottles floating on velvet), Glossier presents every element as if it were lying on a piece of paper — completely flat, separated only by color, hairline borders, or empty space. The system uses chromatic surfaces (pink, light gray) instead of elevation to create zones. This is the visual equivalent of natural light, no makeup — the conceptual brand promise rendered in CSS.

### Decorative Depth
- Pink surfaces (`#f6e3e6`) function as the system's only "elevation" — they create separation zones without lifting elements
- 1px black borders pair with sharp corners to create graphic, printed-zine quality
- No glows, no inner shadows, no inset effects on the primary system
- Photography provides depth where the UI refuses to — product shots have natural lighting and shadow, but the chrome around them stays flat

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

**Primary Light (Default Workhorse)**
- Background: Button Gray (`#e8e8e8`)
- Text: Glossier Black (`#000000`)
- Padding: 8px 16px
- Radius: `0px` (sharp rectangular)
- Border: `0px none`
- Box-shadow: `none`
- Font: 16px Apercu weight 400, sentence case, letter-spacing `0.03px`
- Hover: background shifts to `#f6f6f7`, opacity drops to 0.9
- Use: "Add to bag", "Shop now", "Find your shade" — the most common CTA

**Primary White (On Pink/Photo Surfaces)**
- Background: Pure White (`#ffffff`)
- Text: Glossier Black (`#000000`)
- Padding: 8px 16px
- Radius: `0px`
- Border: `0px none`
- Hover: background shifts to `#f6f6f7`, opacity 0.9
- Use: CTAs sitting on `#f6e3e6` pink panels or full-bleed product photography

**Outline Black**
- Background: `#ffffff` or transparent
- Text: Glossier Black (`#000000`)
- Padding: 8px 16px
- Radius: `0px`
- Border: `1px solid #000000`
- Hover: background fills to `#000000`, text inverts to `#ffffff`
- Use: Secondary actions, "Learn more", "View all" — the editorial CTA variant

**Promo Bar Vermillion**
- Background: Vermillion (`#f94200`)
- Text: Pure White (`#ffffff`)
- Padding: 0px (full-bleed bar — interior content uses 14px font, 8–16px content padding)
- Radius: `0px`
- Border: `0px none`
- Font: 14px Apercu weight 400
- Use: Site-wide promo bar at top of every page — limited-edition launches, free shipping, sale messaging

**Quaternary Dark (Video Controls)**
- Background: Mid Gray (`#666666`)
- Text: Pure White (`#ffffff`)
- Padding: 0px (icon-only, square hit target)
- Radius: `0px`
- Use: Video player controls, dark-overlay UI elements

### Cards & Containers
- Background: `#ffffff` (default) or `#f6e3e6` (brand-moment panels)
- Border: `0px` default — cards rely on white-space and grid placement, not frames
- Radius: `0px` for product cards, content blocks, modals
- Shadow: `none` — cards are absolutely flat
- Internal padding: tight on product cards (8–16px), generous on content panels (24–46px)
- Product image: occupies full card width, sits flush to top edge — no inset, no chrome

### Badges / Tags / Pills
**Outline Mono Tag**
- Background: transparent
- Text: Glossier Black (`#000000`)
- Border: `1px solid #000000`
- Radius: `0px` (sharp) or `2px` (occasionally)
- Padding: 4px 8px
- Font: 12–14px Apercu Mono or Apercu weight 400, sometimes UPPERCASE with `0.05em` tracking
- Use: "NEW", "BESTSELLER", "LIMITED", category markers

**Pink Inline Badge**
- Background: Glossier Pink (`#f6e3e6`)
- Text: Glossier Black (`#000000`)
- Padding: 4px 8px
- Radius: `0px`
- Use: Soft brand-tinted badges on white surfaces — promotional callouts that don't need vermillion's volume

### Inputs & Forms
- Background: `#ffffff`
- Border: `1px solid #e8e8e8` default; `1px solid #000000` on focus
- Radius: `0px` or `2px` (close to sharp)
- Font: 16px Apercu weight 400
- Text color: `#000000`
- Placeholder: `#666666`
- Focus: black border, no ring; sometimes paired with `outline: rgb(0,0,0) auto 2px` for accessibility
- Padding: 10–16px vertical, 12–16px horizontal
- Label: 14px Apercu weight 400, often Mono for technical fields

### Navigation
- Top bar: white background, 1px black bottom border, sticky on scroll
- Logo: "Glossier" wordmark centered (or left-aligned on collection pages), Apercu weight 500
- Links: Apercu 16px weight 400, `#000000`, sentence case
- Hover: underline appears (`text-decoration: underline`) — color stays black
- Cart icon: minimal SVG, top-right, with optional count badge in vermillion or black
- Mobile: hamburger left, wordmark center, cart right — three-zone simplicity

### Decorative Elements

**Photographic Hero**
- Full-bleed product or model photography fills the hero zone
- Massive "Glossier" wordmark overlays the photograph at 240px+ in white
- No gradient scrim — trust in the photograph's inherent contrast
- Use: Homepage hero, collection landings, brand-moment campaigns

**Pink Surface Block**
- Solid `#f6e3e6` rectangle, 0-radius, full-width or contained
- Hosts editorial copy, product callouts, footer — anywhere the white canvas needs a soft visual break
- No border, no shadow — the color alone defines the zone

**1px Black Hairline**
- Single 1px solid black line — top, bottom, or all-sides on selected containers
- The system's only "decorative" treatment beyond pink surfaces and photographs

## Do's and Don'ts

### Do
- Use Apercu for every typographic role — display, body, button, label
- Default to weight 400; reserve weight 500 for headings and weight 700 for rare emphasis
- Keep buttons in sentence case ("Add to bag") — not all-caps shouting
- Use sharp `0px` corners on every rectangular element — buttons, cards, modals, inputs
- Apply Glossier Pink (`#f6e3e6`) as a surface, never as type or border
- Reserve Vermillion (`#f94200`) for the single site-wide promo bar — not for buttons or accents
- Use 1px black borders to separate, not shadows — the system is graphic, not atmospheric
- Lean on full-bleed product photography for visual interest — the imagery is the illustration
- Set massive wordmark moments (240px+ Apercu weight 500) as hero anchors
- Pair tight grid gutters (8–16px) with wide section breaks (80–125px) for editorial rhythm

### Don't
- Don't introduce a serif anywhere — Apercu is the only voice
- Don't use all-caps buttons — Glossier's button voice is sentence case, weight 400
- Don't add gradients, shadows, or atmospheric depth — flatness is non-negotiable
- Don't use Glossier Pink as a button background or text color — it lives as a surface only
- Don't introduce mid-range border-radius (4–16px) — the system is binary (sharp or absent)
- Don't add chromatic colors beyond pink and vermillion — purple, mint, lavender, etc. are not Glossier
- Don't use weight 600+ on display headings — weight 500 is the ceiling
- Don't ornament with lines, dots, dividers — let space and pink surfaces do the separation
- Don't dim photography with overlays or scrims — trust the natural lighting
- Don't off-white the background — Glossier is pure `#ffffff`, not `#fafafa` or `#f5f5f5`

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, wordmark drops to 80–120px |
| Mobile | 375–600px | Single-column, 1-up product grid, 32–48px headings |
| Tablet Small | 600–768px | 2-column product grid, 48–72px headings |
| Tablet | 768–1024px | 2–3 column grid, 72–120px wordmark |
| Desktop | 1024–1280px | 4-column product grid, 120–240px wordmark |
| Large Desktop | ≥1280px | Maximum scale — 240–360px wordmark, full editorial layout |

### Touch Targets
- Primary CTAs: minimum 44px tap height; 8px 16px padding on mobile
- Nav links: full-row tap targets in mobile drawer (54–60px tall)
- Cart, search, hamburger icons: 44×44px minimum hit area
- Product cards: full card is tappable to product detail page

### Collapsing Strategy
- **Nav**: Horizontal link bar collapses to hamburger menu on mobile; full-screen drawer on open
- **Wordmark**: 240–360px → 80–120px progressive scaling; never becomes a logo crop
- **Product grid**: 4-col → 2-col → 1-col with grid gutters maintaining 8–16px regardless of breakpoint
- **Promo bar**: Stays full-width on every breakpoint; text auto-shrinks rather than wrapping
- **Footer**: 4–5 columns → 2 columns → stacked accordion on mobile
- **Section spacing**: 125px desktop → 48–64px mobile — reduces but maintains editorial pace
- **Photography**: Maintains full-bleed treatment on mobile; aspect ratio shifts from 16:9 to 4:5 or 1:1 for portrait phones

### Image Behavior
- Product imagery maintains square or portrait aspect ratio across breakpoints
- Hero photography reframes (not crops) — Glossier serves art-directed alternates for mobile portrait orientation
- No art direction simplification — the same brand language adapts to small viewports
- Wordmark scales fluidly with viewport width; never substituted for an icon mark

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA Background: Button Gray (`#e8e8e8`) — note: NOT pink
- Page Background: Pure White (`#ffffff`)
- Brand Surface: Glossier Pink (`#f6e3e6`)
- Promo Accent: Vermillion (`#f94200`) — used in site-wide promo bar only
- Primary Text: Glossier Black (`#000000`)
- Secondary Text: Mid Gray (`#666666`)
- Soft Surface: Light Gray (`#f7f7f7`)
- Input Border: Border Soft (`#e8e8e8`)
- Strong Border: Border Black (`#000000`)
- Default Radius: `0px`
- Default Shadow: `none`

### Example Component Prompts
- "Create a Glossier-style hero on pure white (`#ffffff`) with the word 'Glossier' set in Apercu weight 500 at 280px, line-height 0.85, color `#000000`, sitting over a full-bleed product photograph. Add a sentence-case CTA button: background `#e8e8e8`, text `#000000`, 8px 16px padding, `0px` radius, font Apercu 16px weight 400."
- "Design a product card on `#ffffff` with `0px` radius and no shadow. Product photograph fills the top edge-to-edge in 1:1 aspect ratio. Below: title in Apercu 20px weight 400, price in Apercu 16px weight 400, 'Add to bag' button in `#e8e8e8`. 16px internal padding, no border."
- "Build a site-wide promo bar — full-width strip in `#f94200` (vermillion), 14px Apercu weight 400 white text, sentence case, single-line. No padding visible. Sticky to top of viewport."
- "Create an outline-style secondary button — transparent background, `1px solid #000000` border, `0px` radius, 8px 16px padding, Apercu 16px weight 400 text in `#000000`. Hover state inverts: black fill, white text."
- "Design a footer block with `#f6e3e6` (Glossier Pink) full-width background, 4-column link grid, Apercu 16px weight 400 black links, 24px column gutters, 80px top/bottom padding. No borders, no shadows."
- "Style a form input with `1px solid #e8e8e8` border, `0px` radius, 12px 16px padding, Apercu 16px weight 400 placeholder in `#666666`. Focus state changes border to `1px solid #000000` — no ring, no shadow."

### Iteration Guide
1. Default to Apercu (or Apercu Pro / Apercu Mono) — no other typeface, ever. Substitute GT America or Söhne if Apercu is unavailable.
2. Keep radius at `0px` for everything visible. Sharp corners are the brand signature.
3. The default page background is pure white (`#ffffff`) — never off-white. Glossier Pink (`#f6e3e6`) is a surface for the footer and select panels, never a default canvas.
4. Buttons are sentence case, weight 400, neutral gray (`#e8e8e8`) — not bold, not all-caps, not pink.
5. Vermillion (`#f94200`) appears once per page in the promo bar only. Never use it for buttons or accents.
6. No shadows. No gradients. No glows. The brand is flat — depth comes from photography and pink surfaces.
7. Lean massive on hero typography — wordmark moments at 240px+ in Apercu weight 500 are signature.
8. Tight grid gutters (8–16px) inside dense zones, wide breaks (80–125px) between sections.
9. Photography does the visual heavy-lifting — no illustrations, no icons-as-decoration, no graphic flourishes.
10. If you're tempted to add a 12px radius, a soft shadow, or a gradient — stop. You've left the brand.
