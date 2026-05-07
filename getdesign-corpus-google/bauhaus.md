---
version: alpha
name: "Bauhaus Movement"
description: "Charcoal `#393f46` slate, amber accent at 85% alpha, Dosis weight 400 at 80px — modernist archive turned web shop."

colors:
  background: "#ffffff"
  surface: "#393f46"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#1a1a1a"
  primary: "#d89e2e"
  on-primary: "#ffffff"
  border: "#8d9ba9"
  focus-ring: "#d89e2e"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Dosis, ui-sans-serif, system-ui, sans-serif"
    fontSize: 80px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Dosis, ui-sans-serif, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Dosis, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Dosis, ui-sans-serif, system-ui, sans-serif"
    fontSize: 25px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Dosis, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Dosis, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Dosis, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Dosis, ui-sans-serif, system-ui, sans-serif"
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

# Bauhaus Movement Design System

## Overview

The Bauhaus-Movement shop is the modern e-commerce wrapper around the Bauhaus design school's archive — and it carries the school's "form follows function" doctrine into a 2024 retail context with admirable restraint. The page lives on a charcoal slate canvas (`#393f46`) — not pure black, not Material-Design dark mode, but a desaturated 26%-lightness blue-gray that reads as "industrial primer" or "felt-tip notebook ink." On top of that base, it lays a single warm amber accent (`#d89e2e` at 85% alpha) for buttons, a slate-blue mid-tone (`#8d9ba9`) for secondary text and de-emphasized chrome, and pure white (`#ffffff`) for primary text and elevated surfaces.

The typographic signature is **Dosis at weight 400 from 80px down to 30px** — a humanist geometric sans with rounded terminals, designed by Edgar Tolentino as an open-source homage to early-20th-century geometric grotesks. At 80px / 5rem with `line-height: 1.00` and tight `letter-spacing: -1.74px` to `-0.88px`, it carries the page's H1 voice with a quietly confident architectural feel — closer to Universal (the actual Bauhaus typeface designed by Herbert Bayer in 1925) than to Helvetica or Inter. The system uses weights 300, 400, and 600, with 400 doing 80% of the work.

What makes this site feel **modernist-archival** rather than e-commerce-generic is the **6px-radius-everywhere chunky corner radius** combined with **soft layered shadows** that come almost exclusively from the `rgba(26, 33, 75, 0.12)` family — a midnight-blue-tinted drop that whispers depth without shouting. The 0/4/6/2px radius scale, the `0px 0px 6px 6px` half-rounded panels (top-only / bottom-only corners), and the absence of any gradient or glassmorphism make the chrome feel **printed** rather than rendered. There are no neon highlights, no purple-pink gradients, no animated glow halos — just a quiet conversation between charcoal, amber, and slate-blue, with white as the elevated surface.

**Key Characteristics:**
- Charcoal Slate `#393f46` as the dominant brand color — 2,649 occurrences (the page IS this color)
- Amber Accent `#d89e2e` (`rgba(216, 158, 46, 0.85)` in source) — the single chromatic CTA tint
- Slate Blue `#8d9ba9` for secondary text and "art-brand" accents — a desaturated bridge between charcoal and white
- Dosis weight 400 at 80px / line-height 1.00 — geometric humanist H1 voice
- 6px workhorse radius (91 instances) with `4px 4px 0px 0px` and `0px 0px 6px 6px` half-rounded panels
- Midnight-tinted shadows: `rgba(26, 33, 75, 0.12) 0px 2px 16px -2px` (101 instances)
- 1px hairline borders at `rgba(58, 64, 72, 0.1)` for cards and `rgba(255, 255, 255, 0.1)` on dark surfaces
- Twenty declared breakpoints from 98px to 1400px — full-fidelity responsive scaffolding
- No gradients anywhere — solid color blocks doing all heavy lifting

## Colors

### Primary Brand
- **Charcoal Slate** (`#393f46`): The dominant brand color. 2,649 occurrences — the most-used color on the page. Used for the shopbar background, primary brand surfaces, and the page's structural anchor. A 26% lightness blue-gray — warmer than pure black, cooler than warm gray. Reads as "industrial primer" or "modernist felt-pen ink."
- **Amber Accent** (`#d89e2e`): The single chromatic accent — used for primary buttons, the brand CTA, and select interactive moments. Source uses `rgba(216, 158, 46, 0.85)` at 85% alpha, which softens the amber into a slightly muted warm gold rather than a saturated mustard. 91 occurrences.

### Secondary
- **Slate Blue** (`#8d9ba9`): The bridge color. 270 occurrences. Used for "art-brand" accents — a desaturated 63% lightness blue-gray that sits between Charcoal Slate and white. Used for secondary text on dark, de-emphasized chrome, and atmospheric mid-tones.
- **Pure White** (`#ffffff`): Primary text on dark surfaces, menubar links, shopbar buttons. 754 occurrences — the second most-used color. Treated as a content surface rather than just text.

### Text & Chrome
- **Charcoal Slate** (`#393f46`): Primary text on light surfaces, dark text on white panels, the primary "ink" color.
- **Slate Blue** (`#8d9ba9`): Secondary text on dark surfaces; tertiary text on light surfaces.
- **Mid Gray** (`rgb(158, 158, 158)`): 1px solid border color on listboxes and dropdowns — used for utility chrome.
- **White Hover Wash** (`rgba(255, 255, 255, 0.15)`): The hover/focus state on dark surfaces — a soft white veil rather than a hue shift.

### Surface
- **Charcoal Slate** (`#393f46`): Dark canvas surfaces — the shopbar, brand banners, archival panels.
- **Pure White** (`#ffffff`): Light content surfaces — product cards, editorial inserts, modal interiors.

### Border System
- **Card Border** (`rgba(58, 64, 72, 0.1)`): 1px solid, 10 occurrences — the workhorse light card border. A 10%-alpha charcoal that whispers containment.
- **Button Border** (`rgba(89, 97, 103, 0.15)`): 1px solid, 7 occurrences — slightly more opaque chrome border on buttons.
- **Dark Card Border** (`rgba(255, 255, 255, 0.1)`): 1px solid white at 10% alpha — used on dark surfaces.
- **Span Hairline** (`rgba(255, 255, 255, 0.2)`): 1px solid white at 20% alpha for emphasized chrome.
- **Section Underline** (`#393f46`): `0px 0px 1px` solid charcoal — bottom-only borders on tabs and section dividers.
- **Combobox** (`rgba(0, 0, 0, 0.12)`): 1px solid black at 12% alpha — form input chrome.
- **Amber Hairline** (`#d89e2e`): 1px solid amber, used sparingly on focused buttons and the active form state.

### Status & Highlight
- **Amber Accent** (`#d89e2e`): Doubles as the highlight/sale tint and active-state color.
- **No declared error/warning colors** — likely inherited from the e-commerce platform, but not extracted on the homepage.

### Gradient System
- The Bauhaus Movement shop is **gradient-free**. All depth comes from solid color blocks, hairline borders, and the midnight-tinted layered shadows. There are no purple-pink gradients, no atmospheric glow effects, no glassmorphism. The "form follows function" doctrine carries through.

## Typography

### Font Family
- **Display / Heading**: `Dosis` (Google Fonts) — humanist geometric sans by Edgar Tolentino, designed as an open-source homage to early geometric grotesks. The page uses weights 300, 400, and 600.
- **Body**: System sans fallback (the page does not declare a separate body family — Dosis is used at all sizes, with body falling to system stack).

*Note: For external implementations, **Dosis** is freely available via Google Fonts. As a substitute, **Universal** (the actual Bauhaus typeface designed by Herbert Bayer in 1925, available digitally as Architype Universal) offers the truer historical reference. **DM Sans** or **Inter** at tighter tracking work as practical substitutes.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero (XL) | Dosis | 80px (5rem) | 400 | 1.00 | normal | Page-anchor headline — geometric architectural display |
| Display Hero (L) | Dosis | 72px (4.5rem) | 400 | 1.00 | normal | Secondary hero |
| Display (M) | Dosis | 58px (3.63rem) | 400 | 1.02 | -1.74px | Tight architectural tracking on big sizes |
| Display (S) | Dosis | 44px (2.75rem) | 400 | 1.08 | -0.88px | Section heads |
| Heading Bold | Dosis | 36px (2.25rem) | 600 | 1.05 | -0.72px | Emphasized section heads — the rare 600-weight moment |
| Heading | Dosis | 36px (2.25rem) | 400 | 1.20 | normal | Standard section heads |
| Heading Mid | Dosis | 30px (1.88rem) | 400 | 1.40 | normal | Card titles, feature names |
| Heading Light | Dosis | 30px (1.88rem) | 300 | 1.40 | normal | Light-weight variant for editorial moments |
| Body Large | Dosis | 20px (1.25rem) | 400 | 1.40–1.50 | normal | Lead paragraphs |
| Body | Dosis | 16px (1rem) | 400 | 1.50 | normal | Standard reading body |
| Caption / UI | Dosis | 14px (0.88rem) | 400 | 1.40 | normal | Metadata, byline, form labels |
| Micro | Dosis | 12px (0.75rem) | 400 | 1.40 | normal | Footer microcopy, legal text |

### Principles
- **Weight 400 is the workhorse.** The system uses 300 and 600 sparingly — most headlines, buttons, and body text run at 400. This single-weight emphasis creates the "consistent voice" feel of a modernist publication.
- **Tight tracking on big sizes.** From 44px up, letter-spacing trims to `-0.88px` to `-1.74px` — the larger the type, the tighter the tracking. This is a hallmark of architectural display typography.
- **Line-height 1.00 at 72–80px.** The biggest H1s are set at flat 1.00 line-height — the type stacks tightly without descender breathing room. Below 44px, line-height opens to 1.05–1.40.
- **Geometric humanist over neo-grotesque.** Dosis carries rounded terminals and slightly humanist proportions, giving the page warmth that pure geometric sans (Futura, Avenir) wouldn't.
- **No serif anywhere.** The system is 100% Dosis. There is no editorial-print counterpoint, no italic display moment.
- **No uppercase headlines.** Title case and sentence case dominate — the system treats type as a quiet authority, not a hazard-tape one.

## Layout

### Spacing System
- Base unit: 8px (the most-used spacing value at 404 occurrences)
- Scale: 1, 2, 3, 3.2, 4, 6.4, 8, 10, 12, 16, 20, 24, 32, 40, 48, 64px
- Notable sub-grid values: 3.2px and 6.4px appear frequently — these are likely 0.2rem and 0.4rem at 16px root, indicating a rem-based scale
- Section padding: 48–96px between major panels; 32–48px between subsections
- Card internal padding: 16–24px standard; 32px for feature cards

### Grid & Container
- Twenty declared breakpoints from 98px to 1400px (98, 320, 360, 412, 480, 481, 576, 600, 640, 680, 768, 800, 900, 980, 992, 1024, 1100, 1180, 1200, 1400)
- Max content width: typically `1100–1200px` based on the breakpoint cluster
- Product grids: 4 columns desktop, 3 columns tablet, 2 columns mobile
- Editorial sections: alternate full-bleed and contained
- Sidebar layouts at desktop with 240–280px left rail

### Whitespace Philosophy
- **Modernist breathing room.** Sections breathe with 48–96px of vertical space between major blocks — generous but not luxurious. The pacing reads as "museum wall label" rather than "luxury campaign."
- **Light/dark alternation.** The page alternates `#393f46` charcoal sections with `#ffffff` white content panels — creating a chapter-like rhythm reminiscent of a printed catalog.
- **Grid-first composition.** Content sits in honest 12-column grids with consistent gutters. There is no asymmetric "designed" layout — the page reads as a system, which is the entire Bauhaus point.

### Border Radius Scale
- Sharp (`0px`): Default elements, full-bleed sections
- Tight (`1px`): Decorative spans
- Compact (`2px`): Small badges (105 occurrences)
- Mid-compact (`4px`): Buttons (88 occurrences)
- Workhorse (`6px`): Cards, buttons, list items, menus (91 occurrences) — the most-used radius after 0
- Half-rounded panels: `4px 4px 0px 0px` (84 occurrences, top-rounded), `0px 0px 6px 6px` (169 occurrences, bottom-rounded)
- Pill (`800px+`): Search input variant — a single outlier

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, default panels |
| Hairline (Level 1) | `1px solid rgba(58, 64, 72, 0.1)` | Card containment |
| Inset (Level 2) | `rgba(34, 38, 42, 0.04) 0px 1px 0px 0px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset` | Pressed/active button states |
| Workhorse Lift (Level 3) | `rgba(26, 33, 75, 0.12) 0px 2px 16px -2px, rgba(0, 0, 0, 0.15) 0px 2px 3px -2px` | Default card and button elevation (101 occurrences) |
| Hover Lift (Level 4) | `rgba(26, 33, 75, 0.09) 0px 10px 40px -4px, rgba(0, 0, 0, 0.13) 0px 12px 28px -12px` | Hovered card elevation (14 occurrences) |
| Whisper (Level 5) | `rgba(0, 0, 0, 0.03) 0px 6px 18px 0px` | Quiet ambient lift on editorial inserts |
| Ring (Level 6) | `rgba(0, 0, 0, 0.15) 0px 0px 0px 1px` | Border-replacing shadow ring |
| Atmospheric (Level 7) | `rgba(0, 0, 0, 0.3) 0px 0px 24px 0px` | Modal overlay scrim |

**Shadow Philosophy**: Bauhaus Movement's depth system is **midnight-tinted and layered**. Where Material Design uses neutral-gray shadows at 0.10–0.20 opacity, Bauhaus Movement uses a `rgba(26, 33, 75, ...)` family — a deep navy-purple tint that gives shadows a barely perceptible coolness. Shadows are stacked in pairs (a wide soft shadow + a tight contact shadow) for a printed-poster-on-wall feel rather than a floating-card feel. The two-layer stack `0px 2px 16px -2px` (wide) + `0px 2px 3px -2px` (tight contact) is the workhorse pattern.

### Decorative Depth
- The half-rounded panel pattern (`4px 4px 0px 0px` and `0px 0px 6px 6px`) creates visual "tab edges" and "sleeve flaps" without explicit shadow work
- The 1px solid borders at 10–15% alpha replace shadows in many places — a deliberate flat-modernist move
- Active button presses use an inset white highlight at 25% alpha, simulating the recessed feel of a physical control
- No glow, blur, or atmospheric halos — Bauhaus Movement keeps depth strictly architectural

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

**Primary — Amber Pill**
- Background: `#d89e2e` (often as `rgba(216, 158, 46, 0.85)` from source)
- Text: `#ffffff` (or `#393f46` for high-contrast variants)
- Padding: ~`8px 24px`
- Radius: `6px` (the workhorse) or `4px`
- Border: none, or `1px solid #d89e2e` for outlined variants
- Shadow: `rgba(26, 33, 75, 0.12) 0px 2px 16px -2px, rgba(0, 0, 0, 0.15) 0px 2px 3px -2px`
- Font: Dosis 16px weight 400
- Use: Primary CTAs — "Add to Cart", "Buy", "Subscribe"

**Secondary — White on Charcoal**
- Background: `#ffffff`
- Text: `#393f46`
- Padding: `8px 40px 8px 43.6px` (asymmetric — icon-first layout)
- Radius: `6px`
- Border: `1px solid rgba(89, 97, 103, 0.15)`
- Shadow: `rgba(34, 38, 42, 0.04) 0px 1px 0px 0px, rgba(255, 255, 255, 0.25) 0px 1px 0px 0px inset`
- Use: Secondary CTAs, "Continue Shopping", "View Details"

**Ghost on Dark**
- Background: transparent
- Text: `#ffffff`
- Border: `1px solid rgba(255, 255, 255, 0.2)`
- Radius: `6px`
- Hover: background fills to `rgba(255, 255, 255, 0.15)`
- Use: Tertiary actions on charcoal surfaces

### Cards & Containers

- Background: `#ffffff` (light cards) or `#393f46` (dark archival panels)
- Border: `1px solid rgba(58, 64, 72, 0.1)` on light cards; `1px solid rgba(255, 255, 255, 0.1)` on dark
- Radius: `6px` (default) or `0px 0px 6px 6px` (bottom-rounded panels) or `4px 4px 0px 0px` (top-rounded — 84 occurrences on `<small>` chrome)
- Shadow: `rgba(26, 33, 75, 0.12) 0px 2px 16px -2px, rgba(0, 0, 0, 0.15) 0px 2px 3px -2px` (the workhorse — 101 occurrences)
- Hover: shadow steps up to `rgba(26, 33, 75, 0.09) 0px 10px 40px -4px, rgba(0, 0, 0, 0.13) 0px 12px 28px -12px` (14 occurrences)
- Internal padding: 16–24px standard, 32–40px for feature cards

### Badges / Tags / Pills

**Charcoal Pill**
- Background: `#393f46`
- Text: `#ffffff`
- Padding: `4px 12px`
- Radius: `6px`
- Font: Dosis 12px weight 400
- Use: Category labels, archive tags

**Amber Highlight Pill**
- Background: `#d89e2e`
- Text: `#393f46`
- Padding: `4px 12px`
- Radius: `6px`
- Use: Sale chips, "new" markers, active filters

### Inputs & Forms

**Text Input**
- Background: `#ffffff`
- Text: `#393f46`
- Border: `1px solid rgba(0, 0, 0, 0.12)`
- Radius: `6px`
- Padding: 8–12px
- Font: Dosis 14–16px weight 400
- Focus: border shifts to `#d89e2e` (1px solid amber) and outline appears

**Search Input (Pill Variant)**
- Border-radius: `0px 800px 800px 0px` — half-pill (one extreme outlier in the data)
- Used for the inline search affordance

**Combobox / Listbox**
- Background: `#ffffff`
- Border: `1px solid rgb(158, 158, 158)`
- Radius: `6px`
- Padding: 8–12px

### Navigation

- Top shopbar: `#393f46` charcoal background, full-bleed
- Logo + brand: white wordmark left-aligned
- Menu links: white `#ffffff`, Dosis 16px weight 400, ~12–16px gap
- Hover: text stays white, background washes to `rgba(255, 255, 255, 0.15)`
- Right side: account/cart icons + amber CTA button
- Sticky on scroll
- Mobile: collapses to hamburger drawer with charcoal background and white menu links

### Decorative Elements

**Half-Rounded Panels**
- Top-rounded: `border-radius: 4px 4px 0px 0px` — 84 occurrences on `<small>` chrome
- Bottom-rounded: `border-radius: 0px 0px 6px 6px` — 169 occurrences on div/button chrome
- These half-rounded panels signal "this is a tab edge / sleeve flap" — a modernist nod to architectural detail

**Wordmark / Logo**
- Bauhaus Movement wordmark in white on `#393f46` charcoal
- Geometric sans, slightly tighter tracking than the body Dosis
- Roughly 140–180px wide depending on viewport

## Do's and Don'ts

### Do
- Use Charcoal Slate (`#393f46`) as the dominant brand color — it is the page's structural ink
- Use Amber (`#d89e2e`) only on primary CTAs and the highest-signal moments
- Use Dosis at weight 400 for 80% of the system — reserve 600 for emphasized headlines and 300 for editorial light moments
- Apply tight letter-spacing (`-0.88px` to `-1.74px`) on display sizes 44px and above
- Use 6px border-radius as the workhorse, with `4px 4px 0px 0px` and `0px 0px 6px 6px` for half-rounded panels
- Use the midnight-tinted shadow stack: `rgba(26, 33, 75, 0.12) 0px 2px 16px -2px, rgba(0, 0, 0, 0.15) 0px 2px 3px -2px`
- Alternate `#393f46` charcoal sections with `#ffffff` white panels for chapter-like page rhythm
- Use 1px hairline borders at 10–15% alpha for card containment — not solid 1px borders at 100% alpha

### Don't
- Don't use pure black `#000` for surfaces — Bauhaus Movement uses `#393f46` charcoal slate
- Don't oversaturate the amber — the source is at 85% alpha (`rgba(216, 158, 46, 0.85)`), not full pure
- Don't introduce gradients, glassmorphism, or animated glow effects — the system is solid-color flat
- Don't use neutral-gray shadows — every shadow carries the `rgba(26, 33, 75, ...)` midnight tint
- Don't bold the Dosis headlines past 600 — the typographic voice lives in 400
- Don't use ALL-CAPS for navigation or headings — the system stays in title and sentence case
- Don't pad luxury — section spacing tops out at ~96px, not 160px
- Don't introduce additional chromatic colors — amber is the only chromatic accent

---

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| Watch | 98px | Minimum responsive floor — single-column micro layout |
| Small Mobile | 320–412px | Single-column, hamburger nav, reduced typography |
| Mobile | 480–576px | Slight content widening, still single column |
| Large Mobile | 600–680px | 2-column product grid begins |
| Tablet | 768–800px | 3-column product grid, condensed nav |
| Tablet Landscape | 900–980px | 4-column product grid, full nav with search |
| Desktop | 992–1024px | Full editorial layout, sidebar appears |
| Mid-Desktop | 1100–1180px | Container caps at 1100px, expanded margins |
| Large Desktop | 1200–1400px | Maximum hero typography (72–80px), full multi-column |

The 20-breakpoint scaffolding indicates a responsive system designed for full-fidelity tuning at every device class — typical of a serious e-commerce platform optimized for international shoppers across Apple Watch web views, kiosks, and 1440p monitors alike.

### Touch Targets
- Primary buttons: 40–48px tall (Dosis 16px + 8–12px vertical padding)
- Nav links: ~36–44px tap area through padding
- Product card surfaces: full-card touch targets, 200×280px+ on mobile

### Collapsing Strategy
- Nav: full horizontal nav collapses to hamburger drawer at <768px
- Product grids: 4-col → 3-col → 2-col → 1-col progression
- Type scale: 80px → 72px → 58px → 44px → 36px → 30px progressive heading scale
- Section padding: 96px → 64px → 48px → 32px as viewport narrows
- Sidebar: disappears below 992px, accessible via filter sheet

### Image Behavior
- Product photography: 1:1 square crops, lazy-loaded
- Editorial imagery: 16:9 hero crops with art-direction swaps at 768px
- Archival-style photography: black-and-white treatment preserved at all sizes
- Generous use of object-fit: cover for hero images

---

## Agent Prompt Guide

### Quick Color Reference
- Brand: Charcoal Slate (`#393f46`)
- Accent: Amber (`#d89e2e`) — use at 85% alpha for true source match
- Secondary text: Slate Blue (`#8d9ba9`)
- Surface: Pure White (`#ffffff`)
- Card border: `rgba(58, 64, 72, 0.1)`
- Dark border: `rgba(255, 255, 255, 0.1)`
- Workhorse shadow: `rgba(26, 33, 75, 0.12) 0px 2px 16px -2px, rgba(0, 0, 0, 0.15) 0px 2px 3px -2px`

### Example Component Prompts

1. *"Create a hero on `#393f46` charcoal with a Dosis 80px weight 400 headline in `#ffffff`, line-height 1.00, no letter-spacing. Below it, a 20px Dosis weight 400 subhead in `#8d9ba9` slate blue. CTA button in amber `#d89e2e` with white text, 6px radius, 8×24px padding."*

2. *"Build a product card: `#ffffff` background, `1px solid rgba(58, 64, 72, 0.1)` border, `6px` radius, two-layer shadow `rgba(26, 33, 75, 0.12) 0px 2px 16px -2px, rgba(0, 0, 0, 0.15) 0px 2px 3px -2px`. On hover, shadow steps up to `rgba(26, 33, 75, 0.09) 0px 10px 40px -4px`. Title in Dosis 20px weight 400, price in 16px weight 600."*

3. *"Style a primary amber button: `#d89e2e` background (or `rgba(216, 158, 46, 0.85)` for source match), `#ffffff` text in Dosis 16px weight 400, `6px` border-radius, `8px 24px` padding. Default to no border; hover adds `1px solid #d89e2e`."*

4. *"Design a half-rounded tab panel: `#ffffff` background with `0px 0px 6px 6px` border-radius (bottom-only chunky corners), workhorse shadow. Tab labels in Dosis 16px weight 400 in `#393f46`."*

5. *"Build a charcoal shopbar: `#393f46` background, full-bleed, ~56px tall. White wordmark left, white menu links in Dosis 16px weight 400 centered, amber CTA button right. Hover state on menu links: `rgba(255, 255, 255, 0.15)` background wash."*

### Iteration Guide

1. **Audit the charcoal.** The brand color is `#393f46`, NOT `#000` and NOT `#1a1a1a`. If you see pure black surfaces, correct them.
2. **Audit the amber.** The accent is `#d89e2e` — for true source match use `rgba(216, 158, 46, 0.85)` at 85% alpha. If you see saturated mustard or warm orange, desaturate.
3. **Audit display tracking.** Headlines 44px and above need negative letter-spacing (-0.88 to -1.74px). If display type runs at default tracking, tighten it.
4. **Audit shadow tint.** Every shadow should carry the `rgba(26, 33, 75, ...)` midnight tint. If you see neutral-gray shadows, replace them with the midnight family.
5. **Audit the radius scale.** Buttons and cards land on 4px or 6px. Half-rounded panels use `4px 4px 0px 0px` or `0px 0px 6px 6px`. Square corners break the system.
6. **Audit color sprawl.** Only Charcoal `#393f46`, Amber `#d89e2e`, Slate Blue `#8d9ba9`, and white/borders should appear. No teal, no purple, no pink.
7. **Audit casing.** Title and sentence case only. No ALL-CAPS nav or headings.
8. **Audit weight distribution.** 80% of type runs at Dosis 400. If you see widespread 600 or 700 weight, the system has tipped too "loud."
9. **When in doubt, ask: "would this fit in a 1929 Dessau Bauhaus catalog?"** If yes, ship it. If it screams "modern e-commerce template," strip it back.
