---
version: alpha
name: Granola
description: Warm-paper meeting notebook design — off-whites with yellow-olive undertones, lime-green accent restraint, Quadrant serif + Melange sans pairing, layered ring-inset shadows, 8px workhorse radius.

colors:
  # Primary
  ink: "#0e0f0c"             # Granola Ink — warm near-black
  primary: "#94f27f"          # Accent Lime
  primary-strong: "#79d65e"
  on-primary: "#0d7916"       # forest green text on lime

  # Surfaces
  background: "#ffffff"        # Paper White
  surface: "#eaebe5"           # Oat Cream — signature warm
  surface-mist: "#d5d5d2"      # Stone Mist
  surface-input: "#e3e3e3"

  # Oats palette (decorative tertiary)
  oats-red-200: "#f29e8b"
  oats-red-300: "#e95d3d"
  oats-purple-200: "#cebef8"
  oats-yellow-200: "#febe29"
  oats-yellow-300: "#ed9212"
  oats-green-100: "#e5eacd"
  oats-green-200: "#d1e043"
  oats-blue-200: "#b8d5ff"
  oats-pink-100: "#ffdef6"
  oats-pink-200: "#ffbcef"
  oats-gold-100: "#ede1a1"

  # Text
  ink-deep: "#0e0f0c"
  charcoal-warm: "#292929"
  stone-500: "#454745"
  stone-400: "#4e4d4b"
  neutral-400: "#acada8"
  warm-silver: "#818179"
  muted-sage: "#72726e"

  # Borders
  border-warm: "#d5d5d2"
  border-cool: "#cfd9de"
  border-hairline: "#bdbaa3"   # opaque approx of #47432a33 (olive at 20% alpha) over white — Google format requires hex
  border-section: "#eaebe5"

  # Semantic / focus
  focus-ring: "#7be36e"        # opaque approx of hsl(109 82% 72%)
  destructive: "#ed4444"        # opaque approx of hsl(0 84% 60%)
  accent-wash: "#d6f9c8"        # opaque approx of #93f27d33 over white

  # Dark CTA (rare)
  dark: "#000000"
  on-dark: "#ffffff"

  # Shadow stand-ins
  shadow-soft: "#f5f5f5"        # opaque approx of low-alpha drop — Google format requires hex
  shadow-floating: "#dcdcdc"    # opaque approx of rgba(0,0,0,0.15) drop

typography:
  display-hero:
    fontFamily: "Quadrant, Quadrant Fallback, Georgia, Times New Roman, serif"
    fontSize: 68px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -1.02px
  display-secondary:
    fontFamily: "Quadrant, Quadrant Fallback, Georgia, Times New Roman, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -0.72px
  heading-large:
    fontFamily: "Quadrant, Quadrant Fallback, Georgia, Times New Roman, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.11
    letterSpacing: -0.54px
  heading:
    fontFamily: "Quadrant, Quadrant Fallback, Georgia, Times New Roman, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  heading-soft:
    fontFamily: "Melange, Melange Fallback, -apple-system, Inter, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.33
    letterSpacing: 0.24px
  body-large:
    fontFamily: "Melange, Melange Fallback, -apple-system, Inter, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.2px
  body:
    fontFamily: "Melange, Melange Fallback, -apple-system, Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  body-emphasis:
    fontFamily: "Melange, Melange Fallback, -apple-system, Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0px
  caption:
    fontFamily: "Melange, Melange Fallback, -apple-system, Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0.14px
  caption-bold:
    fontFamily: "Melange, Melange Fallback, -apple-system, Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.14px
  micro:
    fontFamily: "Melange, Melange Fallback, -apple-system, Inter, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.13px

spacing:
  micro: 2px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  2xl: 20px
  3xl: 24px
  4xl: 32px
  5xl: 48px
  6xl: 64px
  7xl: 96px
  8xl: 176px

rounded:
  none: 0px
  input: 4px
  subtle: 6px
  default: 8px
  card: 12px
  large: 16px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-large}"
    rounded: "{rounded.pill}"
    padding: 0px 24px
  button-primary-hover:
    backgroundColor: "{colors.primary-strong}"

  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-emphasis}"
    rounded: "{rounded.default}"
    padding: 8px 12px
  button-secondary-hover:
    backgroundColor: "{colors.surface}"

  button-tertiary:
    backgroundColor: "{colors.oats-green-100}"
    textColor: "{colors.charcoal-warm}"
    typography: "{typography.body-emphasis}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  button-dark:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-emphasis}"
    rounded: "{rounded.default}"
    padding: 8px 16px

  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.default}"
    padding: 24px

  card-elevated:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.card}"
    padding: 28px

  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.input}"
    padding: 9px 12px
  input-focus:
    backgroundColor: "{colors.background}"

  link:
    textColor: "{colors.ink-deep}"
    typography: "{typography.body}"
    padding: 0px

  badge-tag:
    backgroundColor: "{colors.oats-green-100}"
    textColor: "{colors.charcoal-warm}"
    typography: "{typography.micro}"
    rounded: "{rounded.pill}"
    padding: 2px 10px

  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-emphasis}"
    padding: 16px 24px

  modal:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.card}"
    padding: 24px
---

# Granola Design System

## Overview

Granola looks like a meeting notebook rendered in light — a warm-neutral canvas with the confidence of a native macOS app and the soft-spoken restraint of a thoughtful notetaker. The entire experience sits on warm off-whites (`{colors.background}` pure, `{colors.surface}` oats-green-tinted, plus a paper-cream tone) that feel closer to unbleached paper than LCD glass. Where most AI tools arrive with cold blue gradients and chrome, Granola arrives quietly: a quiet lime-green accent (`{colors.primary}`) reserved like a highlighter for the single action that matters on any given screen, surrounded by neutrals that carry a faint yellow-olive undertone (`{colors.warm-silver}`, `{colors.neutral-400}`, `{colors.stone-500}`). Nothing is cold. Nothing is flat.

The craft shows up in the depth. Cards and surfaces use ring-based inset shadows layered with ambient drop shadows to create a tactile, macOS-native sense of floating — like a Finder window hovering over a warm paper desk. Borders are almost never hard: `{colors.border-warm}` or the hairline `{colors.border-hairline}` (a warm olive at 20% opacity flattened) provide containment without aggression. The default radius is `{rounded.default}` (8px) for cards and `{rounded.pill}` (9999px) for pills — soft but not playful, professional but not rigid.

The typographic voice is the third pillar of the craft. Granola pairs a custom serif-display face (**Quadrant**, used for hero and heading text at tight tracking and line-height 1.00) with a precise sans (**Melange**, 300–500 weight for UI, body, and caption) — the combination reads as "editorial AI assistant" rather than "productivity SaaS." Display type is weight 400 but sits large and airy. UI type is weight 400–500 with modest letter-spacing (0.2px on buttons and links) that adds a breath of polish without ever announcing itself.

**Key Characteristics:**
- Warm off-white canvas (`{colors.background}` pure + `{colors.surface}` cream + paper-cream) — never cold, never gray-blue
- Lime-green accent (`{colors.primary}`) used with extreme restraint — CTAs, focus rings, highlights, nothing else
- Custom Quadrant serif for display/heading + Melange sans for UI — editorial pairing
- Warm-toned neutrals throughout (`{colors.warm-silver}`, `{colors.neutral-400}`, `{colors.stone-500}`) with yellow-olive undertones
- Subtle layered shadows: inset hairline + ambient ring + deep ambient drop — warm-tinted, macOS-native
- `{rounded.default}` card radius, `{rounded.pill}` pill radius, `{rounded.input}` input radius — a deliberate three-step scale
- Warm hairline borders (`{colors.border-warm}`, `{colors.border-hairline}`) — containment without aggression
- Heroicons + inline SVGs with linear stroke treatment — never solid, never over-detailed
- "Oats" palette tokens (red, purple, yellow, green, pink, blue) as decorative accents for illustrations only

## Colors

### Primary
- **Granola Ink** (`{colors.ink}`): Primary text on light surfaces — a warm near-black with a faint olive undertone. Not pure black.
- **Accent Lime** (`{colors.primary}`): The signature Granola green. Used sparingly — primary CTAs, focus rings, key highlights in illustrations.
- **Accent Strong** (`{colors.primary-strong}`): Deeper lime for hover states.
- **Accent Text** (`{colors.on-primary}`): Forest-green text color used on lime backgrounds.

### Secondary & Accent (the "Oats" palette)
Granola exposes a named tertiary palette called "Oats" — decorative, warm, and used almost exclusively in illustrations, badges, and category tints.
- **Oats Red 200** (`{colors.oats-red-200}`), **Oats Red 300** (`{colors.oats-red-300}`)
- **Oats Purple 200** (`{colors.oats-purple-200}`)
- **Oats Yellow 200** (`{colors.oats-yellow-200}`), **Oats Yellow 300** (`{colors.oats-yellow-300}`)
- **Oats Green 100** (`{colors.oats-green-100}`), **Oats Green 200** (`{colors.oats-green-200}`)
- **Oats Blue 200** (`{colors.oats-blue-200}`)
- **Oats Pink 100/200** (`{colors.oats-pink-100}` / `{colors.oats-pink-200}`)
- **Oats Gold 100** (`{colors.oats-gold-100}`)

### Surface & Background
- **Paper White** (`{colors.background}`): The primary page background. Pure white but always paired with warm borders and shadows.
- **Oat Cream** (`{colors.surface}`): The signature warm surface — secondary sections, card backgrounds.
- **Stone Mist** (`{colors.surface-mist}`): Slightly warmer-than-neutral light gray — card borders.
- **Border Hairline** (`{colors.border-hairline}`): Olive-tinted hairline — softest possible containment.
- **Input Gray** (`{colors.surface-input}`): Form input borders in unfocused state.

### Neutrals & Text
- **Ink Deep** (`{colors.ink-deep}`): Primary text — warm near-black.
- **Charcoal Warm** (`{colors.charcoal-warm}`): Secondary heading text, button labels on cream.
- **Stone 500** (`{colors.stone-500}`): Body text at comfortable reading emphasis.
- **Stone 400** (`{colors.stone-400}`): Caption and metadata text.
- **Neutral 400** (`{colors.neutral-400}`): Disabled text, placeholder text.
- **Warm Silver** (`{colors.warm-silver}`): Tertiary labels, footnotes, timestamp text.
- **Muted Sage** (`{colors.muted-sage}`): The olive-adjacent mid-gray for soft text on dark.

### Semantic & Accent
- **Focus Ring** (`{colors.focus-ring}`): Light lime ring color for input focus.
- **Destructive** (`{colors.destructive}`): Warm red for destructive actions and errors.
- **Accent Wash** (`{colors.accent-wash}`): Lime highlight wash — selected text, highlighted note regions.

### Gradient System
Granola is **largely gradient-free** — the warm-neutral palette does the work. The one common exception is soft radial washes behind hero elements: low-alpha Oats-family tints fading to transparent. Never hard color stops. Never rainbow sweeps. Depth comes from shadow layering, not from gradients.

### Shadow Tokens
- **Soft** (`{colors.shadow-soft}`): Subtle drop approximation
- **Floating** (`{colors.shadow-floating}`): Deeper modal/popover drop approximation

## Typography

### Font Family
- **Display & Heading**: `Quadrant` — a custom serif display face with editorial proportions. Fallbacks: `"Quadrant Fallback", Georgia, "Times New Roman", serif`.
- **UI, Body & Caption**: `Melange` — a custom sans-serif at 300/400/500/600 weights. Fallbacks: `"Melange Fallback", -apple-system, BlinkMacSystemFont, "Inter", system-ui, sans-serif`.
- **System UI accents** (download buttons, OS-chrome moments): `-apple-system, system-ui, "Segoe UI", Roboto, Helvetica, Arial`.

*Note: Quadrant and Melange are custom licensed faces. External implementations should substitute Georgia for the serif display and Inter or SF Pro Text for the sans.*

### Hierarchy

| Token | Use |
|---|---|
| `display-hero` | 68px Quadrant 400 with -1.02px tracking — editorial hero |
| `display-secondary` | 48px Quadrant 400 — section anchors |
| `heading-large` | 36px Quadrant 400 — feature titles |
| `heading` | 24px Quadrant 400 — card titles, modal titles |
| `heading-soft` | 24px Melange 300 with 0.24px tracking — alternate sans heading |
| `body-large` | 20px Melange 500 with 0.2px tracking — button labels, prominent links |
| `body` | 16px Melange 400 — default reading |
| `body-emphasis` | 16px Melange 500 — emphasized inline |
| `caption` | 14px Melange 400 — metadata, labels, hints |
| `caption-bold` | 14px Melange 600 — micro-headers |
| `micro` | 13px Melange 500 — smallest UI text |

### Rules
- Display type is **weight 400** — not light, not bold. The craft is in proportion, not weight.
- Headings and body use **negative letter-spacing at scale** (-0.54px to -1.02px). Small text uses slight positive tracking (0.14px–0.2px) for legibility.
- Line-heights are tight at the top (1.00 for display, 1.11 for large headings) and comfortable in body (1.40–1.50).
- Never use Quadrant at body sizes. Never use Melange at display sizes. The pairing is strict.
- Button labels use Melange 500 at 16–20px with 0.2px tracking.

## Layout

### Spacing System
Spacing is based on an **8px** rhythm with granular 2/4/6 values for component-internal rhythm. Scale lives in YAML and runs from `micro` (2px) to `8xl` (176px). The most-used values are 8px, 16px, 24px, 12px, 4px.

### Grid & Containers
- 12-column grid with 20px gutters on main content
- Max content width: ~1200px. Hero max width: ~1400px with generous internal padding
- Section vertical padding: 64–176px — generous, editorial
- Card padding: 24–28px internal

### Breakpoints
`300, 320, 480, 576, 640, 768, 992, 1024, 1280px` — a fine-grained responsive scale. The meaningful ones: `640px` (mobile→tablet), `1024px` (tablet→desktop).

## Elevation & Depth

Granola's depth system is the single most important dimension of its craft. Shadows are **warm-tinted, multi-layer, and subtle** — stacked ring-based insets combined with ambient drops to create tactile macOS-native surfaces.

### The Shadow Scale

**Level 0 — Flat / Ambient Ring (the default elevated surface)**
An inner ring at 3% black. Used on most cards, notes, and interactive surfaces. It reads as "this is a contained surface" without looking like a shadow — the dominant elevation treatment.

**Level 1 — Soft Lift (hover, subtle emphasis)**
Inset ring + tight ambient + soft ambient. The craft move — layers combine so the shadow never looks computed; it looks photographic.

**Level 2 — Standard Card Elevation**
Inset ring + 4/12 ambient + 36px soft warm wash creates a gentle halo around the card, like a soft lamp behind parchment.

**Level 3 — Floating / Modal**
Inset ring + 8/48 ambient at deeper alpha — used for modals, popovers, and cards that need to float dramatically. Even "floating" is restrained — alpha is 15% max.

### Rules
- **Always layer.** A single shadow declaration looks flat. Granola's craft is the *combination* of inset ring + ambient drop + optional soft spread.
- **Warm-tinted, not gray-blue.** Shadows use low alpha so the warm surface color shows through.
- **Inset rings replace borders** on elevated surfaces.
- **No dramatic directional shadows.** Direction is near-centered, the spread is soft.

### Usage
- **Level 0** (inset ring): default state for cards, notes, buttons
- **Level 1** (soft lift): hover on cards and notes
- **Level 2** (card elevation): primary hero cards, feature cards
- **Level 3** (floating): modals, popovers, dropdown menus

## Shapes

### Border Radius

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `input` | 4px | Form inputs, tight utilitarian elements |
| `subtle` | 6px | Secondary containment, small images |
| `default` | 8px | Default card, button, container radius — the workhorse |
| `card` | 12px | Elevated cards and prominent containers |
| `large` | 16px | Large feature cards |
| `pill` | 9999px | Tags, CTAs, avatars, icon buttons |

**Rule of thumb:** Default to `{rounded.default}` for any rectangular surface. Use `{rounded.pill}` for anything that should read as a chip, tag, or avatar. Reserve `{rounded.card}`+ for elevated hero cards.

### Borders
- Default: 1px solid `{colors.border-warm}` — warm light gray, the most common border.
- Cool alternate: 1px solid `{colors.border-cool}` — used in tweet-embed and quote contexts only.
- Warm hairline: 1px solid `{colors.border-hairline}` — the softest possible containment.
- Section dividers: 1px solid `{colors.border-section}` — a warm cream separator.
- Never use hard black borders. Never use pure gray — always warm-tinted.

## Components

The complete component spec lives in YAML.

### Buttons
- **`button-primary`** — Lime accent pill, the signature CTA. `{colors.primary}` bg with forest-green `{colors.on-primary}` text.
- **`button-secondary`** — White surface with warm border, `{rounded.default}` radius.
- **`button-tertiary`** — Soft Oats-green pill for secondary emphasis.
- **`button-dark`** — Black on white, used rarely for consent/dramatic dark-context CTAs.

### Inputs
- **`input`** / **`input-focus`** — White surface with `{colors.surface-input}` border, tight `{rounded.input}` (4px) radius. Focus state shifts border to `{colors.primary}` with focus-ring wash.

### Cards (the canonical meeting-note)
- **`card`** — Standard 8px-radius note card. Border replaced by inset ring shadow.
- **`card-elevated`** — `{rounded.card}` (12px) radius for prominent containers.

### Links / Tags / Modal / Nav
- **`link`** — Inline ink-color text, no underline.
- **`badge-tag`** — Pill-shaped Oats-tinted tag.
- **`nav-bar`** — Horizontal sticky header with Melange 500 nav links.
- **`modal`** — Background panel for modal content with `{rounded.card}` radius.

## Iconography & Illustration

### Icon System
- **Treatment:** linear stroke, 1.5–2px stroke weight
- **Sets in use:** Heroicons + custom SVGs
- **For implementations:** `solar:*-linear` from Iconify is the closest stylistic match
- **Default size:** 16–24px
- **Color:** inherits text color (`{colors.ink-deep}` on light, `{colors.on-dark}` on dark) — icons are never branded lime except when paired with a primary CTA

### Illustration
- Organic, hand-rendered feel with flat Oats-palette fills
- Subjects: meeting scenes, sticky-notes, calendars, people silhouettes, audio waveforms
- No gradients inside illustrations — color comes from the Oats family as flat fills
- Illustrations live on cream (`{colors.surface}`) backgrounds, never pure white

## Motion & Interaction

Granola's motion is macOS-native — present, never decorative.

### Principles
- **Ease-out, short durations** (150–220ms for hover, 220–320ms for layout shifts)
- **Opacity + position** over scale. Buttons don't bounce; they dim slightly and softly translate
- **Inset shadow transitions** on hover: a darkening wash animates in over 150ms
- **Focus rings** appear instantly (no transition) — accessibility takes priority over smoothness
- **Cards lift on hover** — Level 0 → Level 1 shadow transition over 200ms
- **Note-taking UI** (inside product): live text streams in character-by-character

### Don't
- No parallax scrolling
- No scroll-triggered animations beyond simple fade-ins
- No spring bounces on UI chrome
- No auto-playing illustrations

### Do
- Honor `prefers-reduced-motion` by disabling all transitions > 100ms
- Keep motion on the mouse (hover) and keyboard (focus) axis — not on scroll
- Let the shadows do the work — a card lifting from Level 0 to Level 2 on hover conveys more than any animation

## Do's and Don'ts

### Do
- Use `{colors.background}` (paper white) and `{colors.surface}` (oat cream) as the canvas pair
- Reserve `{colors.primary}` for primary CTAs, focus rings, key highlights only
- Pair Quadrant for display/heading with Melange for UI/body — never mix
- Use warm-tinted neutrals throughout
- Layer shadows: inset ring + ambient drop + soft spread
- Default to `{rounded.default}` (8px) for surfaces and `{rounded.pill}` for chips
- Use Heroicons or solar:*-linear icons at 1.5–2px stroke

### Don't
- Don't use cold blue-gray neutrals
- Don't use pill radius on cards — pills are for tags, CTAs, avatars
- Don't use a single drop-shadow declaration on cards — Granola layers
- Don't use hard black borders or pure mid-gray
- Don't mix Oats palette tints into UI chrome — they're for illustrations
- Don't introduce gradients
- Don't use Quadrant at body sizes or Melange at display sizes

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <640px | Single column, stacked cards, hero ~36–48px |
| Tablet | 640–1024px | 2-column grids, condensed nav |
| Desktop | >1024px | Full layout, multi-column, 68px hero |

### Touch Targets
- Pill buttons: minimum 40px tap height, generous padding
- Nav links: comfortable 44px tap area
- Form inputs: 36px+ height with 9px vertical padding

### Collapsing Strategy
- Hero: 68px → 48px → 36px progressive scaling
- Section padding: 176px → 96px → 48px on mobile
- Card grids: 3-col → 2-col → single column
- Nav: horizontal links → hamburger drawer

---

## Agent Prompt Guide

### Quick Color Reference
- Page Background: Paper White (`{colors.background}`)
- Section Surface: Oat Cream (`{colors.surface}`)
- Primary CTA: Accent Lime (`{colors.primary}`) with forest-green text (`{colors.on-primary}`)
- Body Text: Stone 500 (`{colors.stone-500}`)
- Heading Text: Granola Ink (`{colors.ink}`)
- Border: Stone Mist (`{colors.border-warm}`)
- Hairline: Olive (`{colors.border-hairline}`)

### Example Component Prompts
- "Create a hero on Paper White (`{colors.background}`) with a 68px Quadrant headline weight 400, line-height 1.0, letter-spacing -1.02px, color Granola Ink. Subtitle in 20px Melange weight 500 with 0.2px tracking. Primary lime CTA pill (`{colors.primary}` bg, `{colors.on-primary}` text, `{rounded.pill}` radius)."
- "Design a meeting-note card on `{colors.background}` with `{rounded.default}` radius, no border (use inset ring shadow), 24px padding. Title in 24px Quadrant 400. Body in 16px Melange 400 line-height 1.50."
- "Build a button-secondary: white surface, 1px `{colors.border-warm}` border, `{rounded.default}`, 8px 12px padding, 16px Melange 500 ink text, hover wash at low alpha."
- "Create an Oats badge: `{colors.oats-green-100}` background, `{colors.charcoal-warm}` text, `{rounded.pill}`, 2px 10px padding, 13px Melange 500."
- "Design a focused input: white background, 1px `{colors.primary}` border, `{rounded.input}` radius, 9px 12px padding, plus a 3px low-alpha lime focus-ring wash."

### Iteration Guide
1. Default canvas is `{colors.background}` with `{colors.surface}` for cream sections
2. Lime is sacred — one or two applications per screen
3. Always pair Quadrant (display) with Melange (UI) — never substitute generic fonts in the same render
4. Border-radius is three-step: `{rounded.input}` for inputs, `{rounded.default}` for surfaces, `{rounded.pill}` for chips
5. Shadows always layer (inset ring + ambient drop) — never single-layer
6. Icons inherit text color, not lime — except on primary buttons
