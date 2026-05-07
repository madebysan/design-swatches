---
version: alpha
name: "Aesop"
description: "Token-first design system reference for Aesop."

colors:
  background: "#ffffff"
  surface: "#333333"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#f6f5e8"
  primary: "#fffef2"
  on-primary: "#ffffff"
  border: "#ca432f"
  focus-ring: "#fffef2"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 31px
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
    fontSize: 25px
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
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
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

# Aesop Design System

## Overview

Aesop's website is apothecary minimalism rendered as a digital object. The page sits on a warm parchment cream (`#fffef2`) with deep ink-grey (`#333333`) body copy, and the entire system is built around the relationship between two typefaces — Zapf Humanist for display moments and Suisse Int'l for everything else. Imagery is sparse and ghosted (product silhouettes drifting at low contrast against the background), navigation is whisper-quiet at 14px, and entire screens unfold with nothing but a centred serif headline, a paragraph of dense Suisse body, and one plain rectangular button. There is no chrome here. No gradients announce themselves, no shadows lift cards, no accent colour competes with the typography. The only saturated moment in the entire palette is a single sienna red (`#ca432f`) that surfaces for sale tags and alerts, and it appears so rarely it reads as a stamp.

What separates Aesop from every other minimalist e-commerce site is the **dual-typeface contract**: Zapf Humanist (a humanist serif with calligraphic descenders) handles every section title and editorial heading, while Suisse Int'l (a precise Swiss grotesk) handles navigation, body copy, buttons, prices, and form fields. The serif sets pace and tone. The grotesk does the actual transactional work. Headings never go above ~31px (`1.9375rem`) — Aesop refuses to shout. Body paragraphs run at 12px (`0.75rem`) Suisse with `1.5` line-height, creating dense letterpress-like text blocks. The page reads like a book, not a homepage.

The third defining trait is **near-zero visual noise**. Border radius defaults to `0` for buttons and inputs (with `.25rem` reserved for tags). Box shadows are absent except for hairline `0 0 0 .0625rem #333` strokes used as focus rings. Imagery, when it appears, is centred, low-saturation, and surrounded by enormous negative space — products float in air rather than sit on stages. Where most beauty brands stack lifestyle photography, Aesop runs whole sections of pure typography on parchment. The aesthetic is letterpress restraint translated into pixels.

**Key Characteristics:**
- Parchment cream canvas (`#fffef2`) — never pure white, always biased warm
- Deep ink-grey text (`#333333`) — softer than pure black, easier on long-form reading
- Dual-typeface system — Zapf Humanist serif for headings, Suisse Int'l grotesk for everything else
- Tiny base type (`12px` body, `14px` UI) creating dense, book-like reading rhythm
- Near-zero radius on buttons and inputs (`0`), `.25rem` reserved for tags only
- No gradients, no drop shadows, no decorative icons in the layout
- One muted sienna accent (`#ca432f`) for sale and alert states, used sparingly
- Generous whitespace pacing — sections breathe rather than crowd
- Centred composition for hero and editorial moments — typography as still-life

## Colors

### Primary
- **Aesop Cream** (`#fffef2`): Primary page background — a warm parchment tint that reads as paper, never screen. Also used as inverse text color on dark surfaces and as primary button label color.
- **Aesop Ink** (`#333333`): All primary text, primary button background, focus rings. Slightly softened from pure black for editorial readability.
- **Aesop Sand** (`#f6f5e8`): Secondary surface tint — used for alternate sections, banner panels, and product card backgrounds. A half-step warmer than the canvas.

### Brand Accent
- **Aesop Sienna** (`#ca432f`): The single chromatic note in the system — applied to sale prices, alert states, and limited-edition tags. So rare it reads as a wax seal.
- **Soft Coral** (`#ff816b`): A muted secondary accent for promotional moments, pulled from the same warm-red family.
- **Aesop Olive** (`#965d34`): Tertiary brown-amber accent for editorial illustration moments. Apothecary brown.

### Neutrals & Text
- **Ink** (`#333333`): Primary text and headings.
- **Mid Grey** (`#666666`): Secondary text, captions, inactive tab labels.
- **Light Grey** (`#999999`): Disabled state text and placeholder text.
- **Stone** (`#6b6b60`): Editorial muted text on cream surfaces — warmer than `#666` for tonal continuity.
- **Dim Ink** (`#252525`): Hover-state darkening for the primary button — a one-step deepening from `#333`.

### Surface & Borders
- **Cream Surface** (`#fffef2`): Default panel background, matches canvas.
- **Sand Surface** (`#f6f5e8`): Alternate section background, banners, product tile cards.
- **Pale Sand** (`#ebeade`): Secondary surface tint — used for filter chips and tag backgrounds.
- **Soft Stone** (`#f0efe1`): Tag fill colour for category and label pills.
- **Hairline Border** (`rgba(51, 51, 51, 0.2)`): The default divider — used for input borders, secondary button outlines, and section rules. Always at 20% opacity for whisper-quiet structure.
- **Solid Border** (`#333333`): Used for primary input focus, dark mode dividers, and pagination strokes.

### Shadow & Stamp Colors
- **Hairline Stroke** (`0 0 0 .0625rem #333`): Aesop's only shadow — a 1px ring used as focus indicator, button outline, and form field emphasis. Never blurred.
- **Inset Stroke** (`inset 0 0 0 .0625rem #333`): The inverse — used to imply pressed state without shifting the element's position.
- **Soft Drop** (`0 0 .1875rem rgba(51, 51, 51, 0.2)`): Reserved exclusively for sticky-bar elevation in checkout. Almost invisible at rest.

### Gradient System
- Aesop is **functionally gradient-free**. The only gradient that ships is a `transparent → #000000` scrim used to anchor hero captions over photography (verified at `linear-gradient(to bottom, transparent, #000000)`). No brand decoration ever uses gradients — surfaces are flat tinted paper.

## Typography

### Font Family
- **Display / Editorial**: `Zapf-Humanist`, with fallback `sans-serif`. A humanist serif used for section titles, editorial headings, and the wordmark. Carries the brand voice.
- **Primary UI / Body**: `SuisseIntl`, with fallback `sans-serif`. The Swiss grotesk that handles every transactional surface.
- **Primary Medium**: `SuisseIntl-Medium`, weight 500. Used for buttons, product tile titles, navigation, tabs, prices, and chat snackbars.
- **OpenType Features**: Standard ligatures only. Aesop uses no stylistic alternates, no opticals — the typefaces' default character set carries the work.

*Note: Both faces are commercially licensed (Suisse Int'l from Swiss Typefaces, Zapf Humanist 601 from Bitstream). For external implementations, Söhne or Inter substitute for SuisseIntl, and Zapf Humanist 601 BT or Optima Nova substitute for Zapf-Humanist.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Notes |
|------|------|------|--------|-------------|-------|
| Display / Hero Title | Zapf-Humanist | 31px (1.9375rem) | 400 | 1.33 | Largest editorial heading — section openers, "Browse by category" |
| Section Title | Zapf-Humanist | 25px (1.5625rem) | 400 | 1.33 | Standard section title — "Recommended reading", "Considered companions…" |
| Content Tile Title (large) | Zapf-Humanist | 25px (1.5625rem) | 400 | 1.20 | Large editorial card titles |
| Section Heading H1 | SuisseIntl-Medium | 36px (2.25rem) | 500 | 1.20 | Page-level H1 (used sparingly — usually replaced by Zapf section titles) |
| H2 | SuisseIntl-Medium | 30px (1.875rem) | 500 | 1.30 | Secondary block headings |
| H3 | SuisseIntl-Medium | 19px (1.1875rem) | 500 | 1.40 | Tertiary headings, product titles |
| Product Tile Title | SuisseIntl-Medium | 16px (1rem) | 500 | 1.50 | Product card name |
| Hero Caption | SuisseIntl-Medium | 14px (0.875rem) | 500 | 1.50 | "From aroma, a world unfolds" — eyebrow above hero serif |
| Button | SuisseIntl-Medium | 14px (0.875rem) | 500 | 1.31 (`1.3125rem`) | All button labels — sentence case, never uppercase |
| Tab / Nav Link | SuisseIntl-Medium | 14px (0.875rem) | 500 | 1.50 | Top-level navigation, tab strips |
| Body | SuisseIntl | 12px (0.75rem) | 400 | 1.50 | Default body — dense reading rhythm |
| Caption / Tag | SuisseIntl-Medium | 11px (0.6875rem) | 500 | 1.70 | Tags, filter chips, micro-labels |

### Principles
- **Two-typeface contract**: Zapf-Humanist for editorial titles only; SuisseIntl for everything that takes user input or sells a product. The serif sets tone, the grotesk sells.
- **Tiny base body**: Body copy at `12px` (`.75rem`) is unusually small for modern sites. Combined with `1.5` line-height, it produces dense book-like text blocks that reward close reading.
- **Sentence case everywhere**: Aesop never uppercases its UI. Buttons, navigation, tabs, and labels all read as natural prose — `text-transform: none` is declared explicitly throughout the system.
- **No bold weights**: The heaviest weight in use is 500 (Medium). There is no 700 anywhere in the design system. Emphasis comes from typeface contrast (serif vs grotesk), not weight escalation.
- **Letter-spacing left alone**: Aesop uses default tracking everywhere — no negative tracking on display, no wide tracking on small caps. The typefaces' native spacing carries the work.
- **Line-height as breathing room**: Body copy at `1.5`, headings at `1.20–1.40` — Aesop never crushes line-height, even on display sizes.

## Layout

### Spacing System
- Base unit: `0.0625rem` (1px) for hairlines, `.25rem` (4px) for component padding
- Scale: `.0625rem`, `.125rem`, `.1875rem`, `.25rem`, `.3125rem`, `.4375rem`, `.5rem`, `.625rem`, `.75rem`, `1rem`, `1.25rem`, `1.5rem`, `1.5625rem`, `2rem`, `2.5rem`
- Notable: Aesop uses an unusual 16px-rooted scale with many sub-rem values (`.5625rem`, `.6875rem`) — this comes from a Sass tokenization that prioritises pixel-precise spacing over a rounded scale. Section padding lives at `1.25rem–2.5rem`, never spaced beyond mid-range editorial whitespace.

### Grid & Container
- Max content width: ~`1280px` for product grids and editorial columns
- Hero: full-width with centred content stack — eyebrow caption, serif headline, body paragraph, single CTA
- Section content: alternating between full-width imagery and centred 600–800px text columns
- Footer: 4-column nav layout on desktop (`width: 25%` per column at `≥64em`), single-column accordion on mobile

### Whitespace Philosophy
- **Editorial breathing**: Each section gets generous vertical padding — 80–160px between major content blocks. Aesop pages feel like book chapters, not landing-page sections.
- **Centre-anchored composition**: Display content (titles, hero captions, key paragraphs) sits centred with symmetric whitespace — never aligned hard left without intent.
- **Image isolation**: Product photography and editorial imagery sit with significant negative space surrounding them — never edge-to-edge unless intentionally hero-scale.
- **Tile rhythm**: Product grids use uniform spacing with clear gutters; tiles never touch.

### Border Radius Scale
- Sharp (`0`): Default for buttons, inputs, cards, modals — the workhorse radius
- Slight (`.25rem`): Reserved for tags and filter chips only
- Soft (`.625rem`, `.3125rem`): Specialty containers like banner panels and onboarding modals
- Pill (`50%` / `100%`): Reserved for circular icon buttons, avatars, and pagination dots
- No mid-range: Aesop does not use 8–16px radii. The system reads either letterpress-sharp or fully circular.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | `box-shadow: none` | Default state for nearly every surface — page canvas, cards, modals at rest |
| Hairline Stroke (Level 1) | `box-shadow: 0 0 0 .0625rem #333` | Focus state on buttons and inputs; selected state on toggles |
| Inset Hairline (Level 2) | `box-shadow: inset 0 0 0 .0625rem #333` | Pressed-state indicator that doesn't shift the element |
| Sienna Outline (Level 3) | `box-shadow: 0 0 0 .0625rem #ca432f` | Error states on form inputs |
| Sticky Bar Drop (Level 4) | `box-shadow: 0 0 .1875rem rgba(51, 51, 51, 0.2)` | Reserved for the cart sticky-bar at viewport bottom in checkout flow |

**Shadow Philosophy**: Aesop's elevation is editorial, not architectural. The default state of every surface is flat — there is no ambient elevation in the system. When depth needs to communicate (focus, error, sticky context), Aesop uses 1px hairline strokes rather than blurred shadows. Where competitor beauty sites lean into soft elevation to imply premium, Aesop achieves the opposite by refusing to lift anything off the page. Cards stay on the paper. Buttons stay on the paper. The page IS the paper.

### Decorative Depth
- Hairline strokes do double duty as borders, focus rings, and pressed-state indicators. The single soft shadow (`0 0 .1875rem rgba(51,51,51,.2)`) is reserved for the persistent checkout bar. No glows, no inner highlights, no neumorphic treatments.

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

**Primary**
- Background: Aesop Ink (`#333333`)
- Text: Aesop Cream (`#fffef2`)
- Padding: `.8125rem 1.5rem .75rem` (asymmetric — slightly more top than bottom)
- Min-width: `18.75rem` (300px) — buttons never shrink to fit text on desktop
- Radius: `0`
- Border: `1px solid transparent`
- Font: 14px SuisseIntl-Medium, weight 500, line-height `1.3125rem`, sentence case
- Hover: background shifts to Dim Ink (`#252525`)
- Use: Primary CTA — "Add to cart", "Continue", "Discover our aromas"

**Secondary (Outline)**
- Background: `transparent`
- Text: Aesop Ink (`#333333`)
- Border: `1px solid rgba(51, 51, 51, 0.2)` — barely-there hairline
- Radius: `0`
- Padding: `.8125rem 1.5rem .75rem`
- Hover: background fills to `#333`, text inverts to `#fffef2`
- Use: Secondary CTA — "Discover our aromas" hero button, "Read more"

**Size Variants**
- Tiny: `.5625rem 1rem .5rem` padding, 12px text — compact tile actions
- Small: `.75rem 1.5rem`, 14px — sidebar and modal CTAs
- Large: `1rem 1.5rem`, 14px — mobile primary, full-width checkout
- Disabled: `#f3f3f3` background, `#999` text, `not-allowed` cursor
- Link / Print: `0` border, no min-width, underlined text — inline tertiary actions

### Cards & Containers
- Background: `#fffef2` (cream) on default sections; `#f6f5e8` (sand) on alternates
- Border: `0` default — Aesop trusts whitespace, not strokes
- Radius: `0` for content cards; `.25rem` for tag-style chips
- Shadow: `none` — cards are always flat
- Internal padding: generous — typically `1.25rem` minimum, `2.5rem+` for editorial features

### Badges / Tags / Pills

**Tag (Category Chip)**
- Background: Soft Stone (`#f0efe1`)
- Text: Aesop Ink (`#333333`)
- Padding: `.25rem .5rem`
- Radius: `.25rem`
- Font: 11px SuisseIntl-Medium, weight 500, line-height `1.7`
- Margin: `0 .625rem .625rem 0` — clusters with consistent gutter
- Use: Filter pills, category markers, ingredient tags

**Sale Indicator**
- Color: Aesop Sienna (`#ca432f`)
- Used as a colour swap on price text — no chip, just typography
- Pairs with strikethrough on original price

### Inputs & Forms
- Background: `#fffef2` (cream — matches canvas)
- Border: `1px solid rgba(51, 51, 51, 0.2)` default; `1px solid #333` on focus
- Radius: `0` (sharp rectangular)
- Font: 14–16px SuisseIntl, weight 400
- Text colour: `#333333`
- Padding: `.8125rem 1rem` typical, expanding for select fields
- Focus: solid `1px solid #333` border replaces hairline; no glow, no shadow

### Navigation
- Top bar: parchment cream background, centred Aesop wordmark in Zapf-Humanist serif at ~32px
- Utility links: Stores · Customer service (left) and Email sign up · Account · My cart (right) — all 12–14px SuisseIntl-Medium
- Primary nav: horizontal row centred under the wordmark — "New & Notable · Skin Care · Hand & Body · Fragrance · Home · Hair · Travel · Gifts · Library · Experience"
- Links: 14px SuisseIntl-Medium, weight 500, `#333333`, sentence case
- Hover: subtle underline appears below link text — no colour change
- Search: right-aligned input field with magnifier icon, hairline border
- Sticky behaviour: nav remains fixed at top; on scroll, transparency disables and surface fills with cream

### Decorative Elements
- **Hairline Rules**: `1px solid rgba(51,51,51,0.2)` horizontal dividers between sections — never thicker, Aesop trusts space over strokes
- **Centred Composition**: hero blocks, section titles, and editorial paragraphs centred with text columns rarely exceeding ~600px to preserve reading rhythm
- **Wordmark Treatment**: Zapf-Humanist with a macron over the second "e" (Aēsop) — a literal typographic signature, always `#333` on cream, never tinted

## Do's and Don'ts

### Do
- Use Zapf-Humanist (or substitute serif) only for editorial headings and the wordmark — never for body copy or UI
- Set body type small — `12px` (`.75rem`) at `1.5` line-height — and trust readers to engage with the density
- Default to sentence case for every label, button, and navigation item
- Use `#fffef2` (cream) as the page canvas — never pure white
- Keep border-radius at `0` for buttons and inputs; `.25rem` for tags only
- Use hairline `1px` borders at 20% opacity for whisper-quiet structure
- Centre editorial composition when in doubt — it's the brand's default rhythm
- Reserve the sienna accent (`#ca432f`) for sale prices and error states only — its rarity is its power
- Keep buttons rectangular and full-width-ish — `min-width: 18.75rem` is the desktop default
- Pair Zapf headings with SuisseIntl-Medium eyebrows above them for editorial pacing

### Don't
- Don't use bold weights (700) — the design system caps at SuisseIntl-Medium (500)
- Don't uppercase UI text — sentence case is mandatory throughout
- Don't add drop shadows for elevation — flat is the default and the brand
- Don't use pure white (`#ffffff`) for the page background — always cream (`#fffef2`)
- Don't introduce gradients on surfaces or buttons — Aesop is solid-tint only
- Don't enlarge headings above ~31px — Aesop refuses to shout, even in hero positions
- Don't crowd line-height below `1.5` for body copy — density without breath is the wrong kind of dense
- Don't use the sienna accent decoratively — every appearance must be functional
- Don't pair Zapf-Humanist with another serif — its singular role is non-negotiable
- Don't add rounded corners to buttons — sharp `0` radius is the brand's tactile signature
- Don't use display-scale photography for every section — pure-typography sections are part of the rhythm

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <40em (640px) | Single-column, accordion footer, hamburger nav |
| Tablet | 40–64em (640–1024px) | 2-column grids begin, primary nav still collapsed |
| Desktop | ≥64em (1024px) | Full horizontal nav, 4-column footer, multi-column product grids |
| Large Desktop | ≥80em (1280px) | Maximum container width, full editorial spacing |

### Touch Targets
- Primary buttons: `min-height` ~44px on mobile via `1rem` vertical padding × 2 plus `.875rem` line-height
- Nav links: `1rem` vertical padding for thumb-friendly tap zones in mobile drawer
- Form inputs: minimum `.8125rem` vertical padding for tap-comfortable height
- Product tiles: entire card is tappable, not just the title

### Collapsing Strategy
- **Nav**: Horizontal row collapses to hamburger drawer; full-screen overlay on open with cream background
- **Hero**: Centred composition stacks tighter on mobile; hero image scales but caption sequence stays the same
- **Footer**: 4-column desktop nav (`width: 25%`) collapses to vertical accordion on mobile, with `+`/`–` indicators at `1.25rem`/`1.75rem`
- **Product grids**: 4-up desktop → 2-up mobile, gutters scale proportionally
- **Editorial text columns**: Max-width tightens on mobile but body remains 12px — Aesop never bumps body size on small viewports
- **Section spacing**: 80–160px desktop reduces to 48–80px mobile while preserving editorial rhythm

### Image Behavior
- Product imagery maintains square or 5:4 aspect ratio across breakpoints
- Editorial photography uses `padding-bottom` percentages (`56.25%`, `100%`, `125%`, `177.77%`) to lock aspect ratios across viewports
- Hero compositions reorder: caption-headline-body-button stack stays vertical on every viewport
- The Aesop wordmark scales but never simplifies to an icon — always full type

---

## Agent Prompt Guide

### Quick Color Reference
- Page Background: Aesop Cream (`#fffef2`)
- Primary Text: Aesop Ink (`#333333`)
- Primary Button: `#333333` background, `#fffef2` text
- Secondary Surface: Aesop Sand (`#f6f5e8`)
- Sale / Alert Accent: Aesop Sienna (`#ca432f`)
- Tag Background: Soft Stone (`#f0efe1`)
- Hairline Border: `rgba(51, 51, 51, 0.2)`
- Focus Ring: `0 0 0 .0625rem #333`

### Example Component Prompts
- "Create a hero on `#fffef2` with centred composition: 14px SuisseIntl-Medium eyebrow, 31px Zapf-Humanist serif headline at line-height 1.33, 12px SuisseIntl body at line-height 1.5 in `#333`, and one secondary outline button — `transparent` bg, `1px solid rgba(51,51,51,0.2)` border, `0` radius, 14px SuisseIntl-Medium label."
- "Design a product tile on `#fffef2` with `0` radius, no border, no shadow. Square product image at top. Below: 14px SuisseIntl-Medium category label, 16px SuisseIntl-Medium product name (line-height 1.5), and a 12px SuisseIntl price — all in `#333`."
- "Create a primary CTA — `#333` background, `#fffef2` text, 14px SuisseIntl-Medium weight 500, padding `.8125rem 1.5rem .75rem`, `min-width: 18.75rem`, `0` radius, sentence case ('Add to cart'). Hover deepens to `#252525`."
- "Design a tag chip — `#f0efe1` bg, `#333` text, 11px SuisseIntl-Medium weight 500, line-height 1.7, padding `.25rem .5rem`, `.25rem` radius, sentence case."

### Iteration Guide
1. Default to two typefaces only: Zapf-Humanist for editorial headings, SuisseIntl/SuisseIntl-Medium for everything else. No exceptions.
2. Body type stays at `12px` (`.75rem`) — resist the urge to bump it for "readability". The density is the brand.
3. Use sentence case for every label, button, nav item, and tab. Uppercase is wrong.
4. Border-radius is binary: `0` for buttons/inputs, `.25rem` for tags, `50%` for circular elements only.
5. The page is cream (`#fffef2`), never white. Pure white only appears as inverse text on dark surfaces.
6. Buttons are rectangles, full-width-ish at `min-width: 18.75rem` on desktop, sharp corners.
7. Drop shadows do not exist in this system except the single sticky-bar exception. Use hairline `1px` strokes for focus and structure instead.
8. The sienna accent (`#ca432f`) is sacred — sale prices and error states only.
9. Centre editorial composition by default; left-align only when working inside dense product grids or forms.
10. Section padding stays generous — pages should feel like book chapters, not stacked components.
