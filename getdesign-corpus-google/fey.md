---
version: alpha
name: Fey
description: Warm-dark finance craft — charcoal canvas, single copper-amber gradient, calibre weight 600 headlines, 29-shadow taxonomy with 3-layer card stacks, chromatic chart glows, and tabular numerals on every number.

colors:
  # Background & Surface (opaque approximations of translucent overlays)
  background: "#0b0b0b"           # Warm Charcoal canvas
  ink-deep: "#000000"              # Deep Black — vignettes
  surface-1: "#161616"             # opaque approx of rgba(255,255,255,0.03) over #0b0b0b — Google format requires hex
  surface-2: "#1f1f1f"             # opaque approx of rgba(255,255,255,0.06)
  surface-3: "#252525"             # opaque approx of rgba(255,255,255,0.08)
  surface-glass: "#2c2c2c"         # opaque approx of rgba(255,255,255,0.12)
  surface-frost: "#3d3d3d"         # opaque approx of rgba(255,255,255,0.20)

  # Text
  ink: "#ffffff"                   # Pure White
  text-secondary: "#e6e6e6"        # Mist
  text-muted: "#5e646b"            # opaque approx of rgba(134,143,151,0.6) over #0b0b0b
  text-tertiary: "#868f97"         # Gunmetal Solid

  # Brand gradient stops
  primary: "#e87a4f"               # Copper Glow — middle of the gradient
  primary-light: "#ffb088"         # Amber Peach
  primary-dark: "#c45a34"           # Burnt Sienna

  # Interactive
  link: "#479ffa"                   # Info Blue (also gain chart)

  # Chart series
  gain-cyan: "#479ffa"
  loss-acid: "#c3f500"
  semantic-gain: "#22c55e"
  semantic-gain-bg: "#1a3a25"      # opaque approx of rgba(34,197,94,0.15)
  semantic-loss: "#ef4444"
  semantic-loss-bg: "#3a1a1c"      # opaque approx of rgba(239,68,68,0.15)
  semantic-gain-text: "#4ade80"

  # Borders
  border-subtle: "#161717"          # opaque approx of rgba(255,255,255,0.04)
  border-standard: "#1c1c1d"        # opaque approx of rgba(255,255,255,0.08)
  border-stronger: "#1f2020"        # opaque approx of rgba(255,255,255,0.10)

  # Chrome button
  chrome: "#e6e6e6"
  on-chrome: "#000000"

  # Notification outline
  notif-outline: "#131419"

typography:
  hero-display:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 54px
    fontWeight: 600
    lineHeight: 1.00
    letterSpacing: 0px
  display-large:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: 0px
  heading-large:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.00
    letterSpacing: 0px
  heading:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0px
  heading-small:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0px
  body-large:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0px
  body:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  button:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.00
    letterSpacing: 0px
  micro-heading:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.8px
  label:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.00
    letterSpacing: 0px
  caption:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0px
  caption-small:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0px
  micro:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  nano:
    fontFamily: "calibre, Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: -0.8px

spacing:
  micro: 2px
  xs: 6px
  sm: 8px
  md: 14px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 42px
  4xl: 56px
  5xl: 79px
  6xl: 98px
  7xl: 128px
  8xl: 232px

rounded:
  none: 0px
  micro: 4px
  tight: 6px
  comfortable: 10px
  card: 16px
  large: 24px
  pill: 99px
  full: 9999px

components:
  button-primary:
    backgroundColor: "{colors.chrome}"
    textColor: "{colors.on-chrome}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 7px 16px
  button-primary-hover:
    backgroundColor: "{colors.text-secondary}"

  button-glass:
    backgroundColor: "{colors.surface-3}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 7px 16px
  button-glass-hover:
    backgroundColor: "{colors.surface-glass}"

  button-icon:
    backgroundColor: "{colors.surface-3}"
    rounded: "{rounded.full}"
    padding: 8px 8px

  card-floating:
    backgroundColor: "{colors.surface-1}"
    rounded: "{rounded.card}"
    padding: 24px

  card-hero:
    backgroundColor: "{colors.surface-1}"
    rounded: "{rounded.large}"
    padding: 32px

  notification-pill:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 12px 16px

  input:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.tight}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.surface-2}"

  badge-gain:
    backgroundColor: "{colors.semantic-gain-bg}"
    textColor: "{colors.semantic-gain-text}"
    typography: "{typography.micro}"
    rounded: "{rounded.pill}"
    padding: 2px 8px

  badge-loss:
    backgroundColor: "{colors.semantic-loss-bg}"
    textColor: "{colors.semantic-loss}"
    typography: "{typography.micro}"
    rounded: "{rounded.pill}"
    padding: 2px 8px

  ticker-tag:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.micro}"
    rounded: "{rounded.micro}"
    padding: 2px 8px

  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 16px 24px

  link:
    textColor: "{colors.link}"
    typography: "{typography.body}"
    padding: 0px
---

# Fey Design System

## Overview

Fey's website is warm-dark finance craft at its purest — a near-black canvas that reads as charcoal rather than void, inhabited by floating cards that drift above the surface on cushions of layered shadow. The site opens on a warm charcoal field (`{colors.background}` at its deepest, with an imperceptible brown-red cast that distinguishes it from Linear's blue-cool black) where the only chromatic event is a single copper-to-amber gradient on the headline — "Earnings in real time" rendered in a sunrise wash that feels lit from within. Everything else — chrome buttons, translucent notification cards, the edges of UI widgets — lives in grayscale, tuned with meticulous inset highlights to feel dimensional rather than flat. This is not a dark theme; it is a dim room, deliberately lit.

The typography is built on `calibre` (the Klim Type Foundry workhorse), running at heavier weights than the Linear/Stripe axis — 600 at display sizes, 400 for body, with a tight 1.00–1.10 line-height at headline scales that compresses type into stable blocks. Where Stripe whispers in weight 300 and Linear engineers in 510, Fey speaks in weight 600: confident, semi-bold, declarative. Numeric displays lean on tabular numerals so a portfolio value at `$24,847.20` never jitters as it ticks. The feel is an Apple-class product utility — precise, typographically disciplined, aware that every pixel on a finance dashboard is a load-bearing piece of information.

What makes Fey unmistakable is its shadow system. The extracted design tokens reveal **29 distinct shadow definitions** — an obsessive taxonomy that treats elevation not as a single `box-shadow` but as a compound lighting model. Primary cards float on 3-layer stacks that simulate a key light plus two fills. Glassy chrome buttons pair outer ambient shadows with `inset` highlights to catch a pin-prick of top-edge light. Chart elements ride on chromatic glows — cyan-blue (`{colors.gain-cyan}`) for one dataset, acid-yellow-green (`{colors.loss-acid}`) for its counterpart — so gains and losses literally radiate their own atmosphere.

**Key Characteristics:**
- Warm charcoal canvas (`{colors.background}`) — not pure `#000000`; holds a faint red-brown undertone
- Copper-amber gradient (`{colors.primary-light}` → `{colors.primary}` → `{colors.primary-dark}`) as the ONE chromatic gesture — headlines, key numbers, moments of emphasis only
- `calibre` typeface at weight 600 for display, 400 for body
- 29-shadow system: 3-to-5 layer stacks for cards, inset-highlight + outer-shadow compounds for buttons, chromatic glows for chart data
- Semi-transparent white borders (4–16% alpha) flattened to `{colors.border-subtle}` / `{colors.border-standard}` / `{colors.border-stronger}` here
- Pill-shaped pay-off buttons (`{rounded.pill}`) paired with card radii of `{rounded.card}` — a deliberate radius bimodal
- Chart glow pairs: cyan `{colors.gain-cyan}` for one series, acid-green `{colors.loss-acid}` for the other
- Tabular numerals on every numeric display
- Info-blue link color (`{colors.link}`) as the single interactive chromatic hit

## Colors

Fey is a near-achromatic system. Color is a finite resource — it appears in the headline gradient, the chart glows, and nowhere else.

### Background & Surface
- **Warm Charcoal** (`{colors.background}`): Primary canvas. Never use pure black at the top level.
- **Deep Black** (`{colors.ink-deep}`): Reserved for the darkest layer — edge gradients, vignette overlays.
- **Surface 1** (`{colors.surface-1}`): The lightest elevated surface — hover-state backgrounds.
- **Surface 2** (`{colors.surface-2}`): Standard elevated surface for cards sitting on the canvas.
- **Surface 3** (`{colors.surface-3}`): Button ghost fill, input background.
- **Surface Glass** (`{colors.surface-glass}`): Hover state for translucent buttons, tooltip backgrounds.
- **Surface Frost** (`{colors.surface-frost}`): Active/selected state on translucent chrome.

### Typography Colors
- **Pure White** (`{colors.ink}`): Primary text on dark.
- **Mist** (`{colors.text-secondary}`): Chrome button text, de-emphasized white.
- **Gunmetal** (`{colors.text-muted}`): Secondary text — metadata, captions, timestamps.
- **Gunmetal Solid** (`{colors.text-tertiary}`): Link tertiary, disabled states.

### Brand & Signature Gradient
- **Amber Peach** (`{colors.primary-light}`): The lighter stop of the signature gradient.
- **Copper Glow** (`{colors.primary}`): The saturated middle — the Fey orange.
- **Burnt Sienna** (`{colors.primary-dark}`): The darker stop.
- **Headline Gradient**: `linear-gradient(90deg, {colors.primary-light} 0%, {colors.primary} 55%, {colors.primary-dark} 100%)` — applied via `background-clip: text` on hero headlines only.

### Interactive & Link
- **Info Blue** (`{colors.link}`): Link color. The ONLY chromatic text that isn't the amber gradient.

### Chart & Data-Viz Glow Colors
These colors appear exclusively as `box-shadow` glows and stroke colors on chart series — never as fills.
- **Gain Cyan** (`{colors.gain-cyan}`): The positive/gain series.
- **Loss Acid** (`{colors.loss-acid}`): The counter series.
- **Semantic Gain** (`{colors.semantic-gain}`): For explicit positive movement indicators.
- **Semantic Loss** (`{colors.semantic-loss}`): For explicit negative movement indicators.

### Borders & Dividers
- **Hairline Subtle** (`{colors.border-subtle}`): The most delicate divider.
- **Hairline Standard** (`{colors.border-standard}`): Default card and container border.
- **Hairline Stronger** (`{colors.border-stronger}`): Button outline, input border.

## Typography

### Font Family
- **Primary**: `calibre` (Klim Type Foundry). Fallback: `Inter, -apple-system, BlinkMacSystemFont, sans-serif`.
- **Monospace**: Use `JetBrains Mono, ui-monospace, SF Mono, Menlo` for code/data displays when needed.
- **OpenType Features**: `font-variant-numeric: tabular-nums` on every numeric display. Non-negotiable for a finance product.

### Hierarchy

| Token | Use |
|---|---|
| `hero-display` | 54px calibre 600 — gradient hero headlines |
| `display-large` | 48px calibre 600 — section hero headlines |
| `heading-large` | 26px calibre 600 — tile titles, dashboard headers |
| `heading` | 24px calibre 600 — card titles |
| `heading-small` | 18px calibre 600 — subsection titles |
| `body-large` | 18px calibre 400 — intro paragraphs |
| `body` | 16px calibre 400 — standard reading text |
| `button` | 14px calibre 600 — CTAs |
| `micro-heading` | 15px calibre 600 with -0.8px tracking — small-caps-adjacent labels |
| `label` | 14px calibre 600 — form labels |
| `caption` | 14px calibre 400 — inline metadata |
| `caption-small` | 12px calibre 600 — tile meta labels |
| `micro` | 11px calibre 400 — fine print, timestamps |
| `nano` | 10px calibre 500 with -0.8px tracking — tickers, axis markers |

### Principles
- **Weight 600 as the headline voice**: Fey lives at 600 where Stripe lives at 300 and Linear lives at 510. Headlines are semi-bold — confident without shouting, dense without being heavy.
- **Tight display line-heights**: 1.00 at 26px+, 1.10 at 48px.
- **Generous body line-height**: 1.25 to 1.40 for body, 1.36 for captions.
- **Tabular numerals always on numbers**: A portfolio value is a data point — it must not reflow or jitter as digits change.
- **Negative tracking only at micro sizes**: -0.8px on 15px micro-headings and 10px nano labels — the small sizes where tightening improves density.
- **Two-weight discipline**: Primarily 400 (body, caption) and 600 (display, heading, label).

## Layout

### Spacing System
Base unit is **8px** with precision intermediates at 2, 6, 14, 42. Observed scale runs from `micro` (2px) to `8xl` (232px). The presence of 7/14-rhythm intervals supports tight financial-UI spacing.

### Grid & Container
- Hero: centered column with generous top padding (~120–232px)
- Dashboard sections: 12-column grid, cards spanning 4/6/8/12
- Chart cards: tend to span full width on their row, 320–400px tall
- Max content width: ~1200px with generous margins

### Whitespace Philosophy
- **Depth over density**: The canvas around cards is as important as the cards themselves — shadow needs room to fall.
- **Breathing-room hero**: The hero headline sits in a large expanse of warm charcoal.
- **Dense card internals**: Inside a card, spacing tightens (8–16px between elements). Outside cards, it relaxes (56–120px between sections).

## Elevation & Depth

Fey's shadow system is the single most distinctive aspect of the design language. Rather than a conventional 3–5 elevation ladder, Fey maintains a taxonomy of **29 distinct shadow definitions**, grouped by role.

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow | Canvas text, disabled states |
| Ambient | `rgba(0,0,0,0.5) 0px 0px 35px 0px` | Hero glow, featured object halo |
| Standard | Subtle 3-layer stack | Background cards, supporting content |
| Elevated | 3-layer card stack: `rgba(0,0,0,0.66) 0px 53px 87px, rgba(0,0,0,0.40) 0px 20px 27px, rgba(0,0,0,0.26) 0px 4px 7px` | Primary cards — the workhorse |
| Hero | 5-layer card stack with continuous falloff | The most prominent element on a screen |
| Floating | Hairline + drop: `rgb(19,20,25) 0px 0px 0px 0.75px, rgba(0,0,0,0.28) 0px 14px 24px` | Notification chips, tooltips |
| Chrome | Inset highlights + outer drop | Glass/chrome buttons |
| Chart | Chromatic glow stack | Data-viz lines, series markers |

**Group 6 — Chromatic Glow** (chart series): Shadow-as-color. Chart series don't use fills — they use colored glow stacks. Gain stack uses `{colors.gain-cyan}` at varying offsets, blurs, and spreads. Counter series uses `{colors.loss-acid}`. Two luminous gases mixing in the same glass tube.

**Shadow Philosophy**: Fey treats elevation as a cinematographic lighting problem. Every elevated surface is lit by a virtual 3-point rig — key light above-behind (the 87px-blur far shadow), fill below (the 27px mid), and contact/edge light (the 7px tight). Cards don't "have a shadow"; they exist in a lit room. Single-layer `box-shadow` values look wrong on a Fey surface — they break the lighting model.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `micro` | 4px | Ticker tags, neutral chips |
| `tight` | 6px | Inputs, small thumbnails |
| `comfortable` | 10px | Standard interactive surfaces |
| `card` | 16px | Standard floating card radius — the workhorse |
| `large` | 24px | Featured hero cards |
| `pill` | 99px | CTAs, notification pills, all pay-off actions |
| `full` | 9999px | Avatars, icon buttons, fully circular |

Notable: Fey's radius scale is bimodal — everything is either modestly rounded (4–16px) or fully pill-shaped (99px+). The mid-range 20–48px radii that other systems use for "soft" cards are deliberately avoided.

## Components

The complete component spec lives in YAML.

### Buttons
- **`button-primary`** (Chrome) — `{colors.chrome}` off-white background, black text, pill radius. Primary CTAs ("Download", "Get started").
- **`button-glass`** — Translucent `{colors.surface-3}` background. Secondary actions.
- **`button-icon`** — Circular `{rounded.full}` icon button — play/pause, dismiss.

### Cards
- **`card-floating`** — The Fey signature element. `{rounded.card}` radius, surface-1 background, 3-layer card stack shadow.
- **`card-hero`** — Larger 32px-padded hero card with `{rounded.large}` radius.

### Notification Pills
- **`notification-pill`** — `{rounded.pill}` shape with hairline + drop shadow. Contains icon, label, secondary text.

### Inputs
- **`input`** / **`input-focus`** — Dark surface, `{rounded.tight}` (6px), 14–16px calibre 400 white text.

### Badges & Pills
- **`badge-gain`** — Semantic gain pill on tinted green background.
- **`badge-loss`** — Symmetric loss pill on tinted red.
- **`ticker-tag`** — Neutral square-edged ticker chip with `{rounded.micro}` (4px).

### Navigation
- **`nav-bar`** — Transparent bar over warm charcoal, sticky with backdrop blur, calibre 16px weight 400 links.

### Links
- **`link`** — Inline `{colors.link}` text.

## Do's and Don'ts

### Do
- Use warm charcoal `{colors.background}` as the canvas, not pure black — the warmth matters
- Apply 3-layer shadow stacks on every elevated card, minimum — no single-layer drops
- Enable `font-variant-numeric: tabular-nums` on every numeric display without exception
- Reserve the copper-amber gradient for headlines only — never for buttons, never for icons
- Use pill radius (`{rounded.pill}`) on all primary CTAs and notification chips
- Pair inset highlights with outer shadows on all chrome/glass buttons
- Use colored `box-shadow` glows (not fills) for chart series — gain cyan, loss acid-green
- Use semi-transparent white borders throughout
- Use calibre at weight 600 for headlines — that's the brand voice
- Keep text hierarchy achromatic (white, off-white, gunmetal) except for the single gradient moment

### Don't
- Don't use pure `#000000` as the page background — Fey's black is always warm
- Don't use single-layer `box-shadow` on cards — it breaks the lighting model
- Don't apply the copper gradient to buttons, icons, borders, or backgrounds — it's a typographic event only
- Don't use saturated color fills in charts — Fey charts glow, they don't paint
- Don't use proportional numerals on money or percentages — jitter is disqualifying
- Don't reach for mid-range radii (20–48px) — Fey is bimodal: 4–16px or pill
- Don't use calibre at weight 300 or below — Fey headlines are weight 600, confident
- Don't introduce a third chromatic color
- Don't use drop shadows with warm tints — Fey's shadows are neutral black; the warmth is in the canvas

---

## Responsive Behavior

### Breakpoints
Fey's token set shows an unusually dense breakpoint array — 24 distinct widths from 340px to 1440px. For practical use:

| Name | Width | Key Changes |
|---|---|---|
| Mobile Small | <540px | Single column, hero collapses to 32–40px display |
| Mobile | 540–768px | Single column, 24px horizontal padding |
| Tablet | 768–1024px | 2-column grids for feature tiles |
| Desktop | 1024–1280px | Full 12-column layout, 3–4 column feature grids |
| Large Desktop | >1280px | Centered content, generous side margins |

### Touch Targets
- Pill buttons hit a minimum of 7px 16px padding for a ~32px touch target — tight but acceptable; increase to 10px 20px on mobile
- Icon circles at 36–44px on mobile
- Chart data points enlarged to minimum 24px tap-target with invisible hit-area expansion

### Collapsing Strategy
- Hero display: 54px → 40px → 32px across breakpoints, weight 600 maintained
- Card shadows: 5-layer hero stacks simplify to 3-layer on mobile to save render cost
- Chart glows: reduce from 7-stack to 3-stack on mobile; maintain the color semantics
- Notification pills: stay pill-shaped but wrap content vertically on narrow screens
- Dashboard grids: 4-col → 2-col → 1-col stacked

### Image & Media Behavior
- Product screenshots maintain the 3-layer card shadow at all breakpoints
- Chart SVGs resize fluidly with `preserveAspectRatio` and maintain their glow stacks via `filter: drop-shadow()` as a fallback on elements that can't take multi-layer `box-shadow`
- Hero gradient text uses `background-clip: text` — falls back to solid `{colors.primary}` where unsupported

---

## Agent Prompt Guide

### Quick Color Reference
- Canvas: Warm Charcoal (`{colors.background}`)
- Card border: Hairline Standard (`{colors.border-standard}`)
- Primary text: Pure White (`{colors.ink}`)
- Secondary text: Gunmetal (`{colors.text-muted}`)
- Link: Info Blue (`{colors.link}`)
- Headline gradient: `linear-gradient(90deg, {colors.primary-light} 0%, {colors.primary} 55%, {colors.primary-dark} 100%)` applied via `background-clip: text`
- Chrome button: `{colors.chrome}` bg, `{colors.on-chrome}` text
- Gain chart glow: `{colors.gain-cyan}` — used as `box-shadow` color, not fill
- Loss chart glow: `{colors.loss-acid}` — used as `box-shadow` color, not fill
- Semantic gain pill: `{colors.semantic-gain}` text on tinted green bg
- Semantic loss pill: `{colors.semantic-loss}` text on tinted red bg

### Example Component Prompts
- "Create a floating portfolio card on a `{colors.background}` canvas. `{rounded.card}` radius, 1px solid `{colors.border-standard}` border, `{colors.surface-1}` background. Shadow: 3-layer card stack. Inside: value at 48px calibre 600 with `font-variant-numeric: tabular-nums` displaying `$24,847.20`. Below, +2.34% today in 14px calibre 600 color `{colors.semantic-gain}`."
- "Build a hero headline: `calibre`, 54px, weight 600, line-height 1.00, color transparent, copper-amber gradient via `background-clip: text`. Subtitle in 18px calibre 400, color rgba white at ~70%."
- "Design a chrome CTA: `{colors.chrome}` background, `{colors.on-chrome}` text, 14px calibre 600, 7px 16px padding, `{rounded.pill}` radius, subtle white outer glow. Hover: brighter background. Focus: deepened shadow + ring."
- "Build a notification pill: `{rounded.pill}` radius, `{colors.surface-1}` background, hairline outline + drop shadow. Contains 24px icon, label in 14px calibre 600 white, secondary text in 14px calibre 400 gunmetal, right-aligned ghost button."
- "Design a chart line series with Fey glow: SVG stroke at 2px `{colors.gain-cyan}`, multi-layer drop-shadow stack at varying blurs/spreads. Data points as 8px circles with the same drop-shadow stack."

### Iteration Guide
1. Always start from warm charcoal `{colors.background}` — never pure black
2. Never use single-layer `box-shadow` on elevated elements — use the 3-layer card stack
3. calibre at weight 600 for headlines, 400 for body — no weight 300, no weight 500 for type
4. Tabular numerals on every number, without exception
5. The copper gradient is typographic only — `background-clip: text` on `<h1>`, `<h2>`, or `<span>` with an explicit semantic role
6. Chrome buttons need the inset-highlight + outer-shadow compound to look "injection-molded"
7. Chart series use `box-shadow` or `filter: drop-shadow` glows, not `fill` or `background-color`
8. Border strokes are always semi-transparent white at 4–10% opacity — no solid gray borders
9. Radii are bimodal: 4–16px for containers, 99px+ for pills. Avoid the 20–48px mid-range.
