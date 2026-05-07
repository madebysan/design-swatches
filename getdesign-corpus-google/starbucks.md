---
version: alpha
name: Starbucks
description: Warm retail flagship — cream canvas, four-tier green brand system mapped by role, SoDoSans with -0.01em tracking, universal 50px pill buttons with scale(0.95) active press, and a signature floating Frap circular CTA.

colors:
  # Canvas / surfaces
  background: "#f2f0eb"
  background-ceramic: "#edebe9"
  surface: "#ffffff"
  surface-cool: "#f9f9f9"
  surface-gold-cream: "#faf6ee"

  # Brand greens — four tiers
  primary: "#00754A"
  primary-bright: "#008248"
  brand-green: "#006241"
  house-green: "#1E3932"
  green-uplift: "#2b5148"
  green-light: "#d4e9e2"

  # Gold (Rewards-only)
  gold: "#cba258"
  gold-light: "#dfc49d"

  # Black for high-contrast strips
  black: "#000000"

  # Ink
  ink: "#222222"  # opaque approx of rgba(0,0,0,0.87) over cream — Google format requires hex
  ink-soft: "#6e6e6e"  # opaque approx of rgba(0,0,0,0.58) — Google format requires hex
  ink-on-dark: "#ffffff"
  ink-on-dark-soft: "#b8b8b8"  # opaque approx of rgba(255,255,255,0.70) over house-green — Google format requires hex
  ink-rewards: "#33433d"

  # On-color tokens
  on-primary: "#ffffff"
  on-house-green: "#ffffff"
  on-gold: "#1E3932"

  # Semantic
  error: "#c82014"
  warning: "#fbbc05"

  # Borders
  border-input: "#d6dbde"
  border-hairline: "#e7e7e7"

  # Shadow tints
  shadow-card: "#000000"  # was rgba(0,0,0,0.14/0.24) — Google format requires hex
  shadow-frap: "#000000"  # was rgba(0,0,0,0.24) — Google format requires hex

typography:
  display:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 80px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.16px
  jumbo:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 58px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.16px
  hero-large:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 45px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.16px
  h1:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: -0.16px
  h2:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.16px
  body-large:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 19px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: -0.16px
  body:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.16px
  small:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.14px
  small-bold:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: -0.14px
  micro:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.13px
  button:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.16px
  button-small:
    fontFamily: "SoDoSans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.14px
  rewards-serif:
    fontFamily: "Lander Tall, Iowan Old Style, Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0px
  careers-script:
    fontFamily: "Kalam, Comic Sans MS, cursive"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px

spacing:
  xxs: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 40px
  2xl: 48px
  3xl: 56px
  4xl: 64px

rounded:
  none: 0px
  xs: 4px
  md: 12px
  pill: 50px
  circle: 50px

components:
  # Primary filled CTA pill (Green Accent)
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 7px 16px
  button-primary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"

  # Primary outlined pill
  button-primary-outline:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 7px 16px

  # Black filled — top "Join now" strip
  button-black:
    backgroundColor: "{colors.black}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-small}"
    rounded: "{rounded.pill}"
    padding: 7px 16px

  # Dark outlined — "Sign in"
  button-dark-outline:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-small}"
    rounded: "{rounded.pill}"
    padding: 7px 16px

  # White-on-green inverted (used over house-green bands)
  button-inverted:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 7px 16px

  # Outlined on dark (white border on house-green)
  button-outline-dark:
    backgroundColor: "{colors.house-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 7px 16px

  # Consent agree (slightly brighter green)
  button-consent:
    backgroundColor: "{colors.primary-bright}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-small}"
    rounded: "{rounded.pill}"
    padding: 7px 16px

  # Frap floating circular order button (signature)
  button-frap:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.circle}"
    padding: 16px

  # Customize button (PDP)
  button-customize:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 14px 40px

  # Add to Order button (PDP)
  button-add-to-order:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 14px 32px

  # Rewards Cost Pill
  badge-rewards-cost:
    backgroundColor: "{colors.house-green}"
    textColor: "{colors.gold}"
    typography: "{typography.micro}"
    rounded: "{rounded.pill}"
    padding: 4px 12px

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px

  # Partnership card (Rewards)
  card-partnership:
    backgroundColor: "{colors.surface-gold-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px

  # Rewards status card (dark green tier panels)
  card-rewards-status:
    backgroundColor: "{colors.house-green}"
    textColor: "{colors.on-house-green}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px

  # Dropdown
  dropdown:
    backgroundColor: "{colors.surface-cool}"
    textColor: "{colors.ink}"
    typography: "{typography.h2}"
    rounded: "{rounded.md}"
    padding: 16px

  # Modal
  modal:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px

  # Floating-label input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: 12px

  # Add-in / Milk select
  input-select:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: 12px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.small-bold}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.small}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.primary}"

  # Feature band (dark green hero strip)
  feature-band:
    backgroundColor: "{colors.house-green}"
    textColor: "{colors.on-house-green}"
    typography: "{typography.body}"
    padding: 64px 40px

  # Feedback tab (top-rounded only)
  tab-feedback:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.small}"
    rounded: "{rounded.md}"
    padding: 8px 16px
---

# Starbucks Design System

## Overview

Starbucks' design system is a warm, confident retail flagship wearing the green of their storefront apron across every surface. The canvas alternates between a neutral-warm cream (`{colors.background}`) and a ceramic off-white (`{colors.background-ceramic}`) — colors that reference actual store materials: paper napkins, café walls, wood finishes — while the signature Starbucks Green (`{colors.brand-green}`) anchors the brand moment on hero bands, CTAs, and the Rewards experience. The greens come in four calibrated shades (Starbucks, Accent, House, Uplift) each mapped to a specific surface role, and gold (`{colors.gold}`) appears only around Rewards-status ceremony — not as a general accent.

Typography carries most of the brand voice. The proprietary **SoDoSans** typeface (custom to Starbucks) sits across nearly every surface with a tight `-0.01em` letter-spacing — it reads confident and friendly rather than fashion-magazine severe. What's unusual: the Rewards page switches to a warm serif (`Lander Tall, Iowan Old Style, Georgia`) for specific headline moments, subtly echoing the nostalgic feel of a coffeehouse chalkboard. And the Careers pages use a handwritten script (`Kalam, Comic Sans MS, cursive`) for personal cup-name touches. Three typefaces, three contexts — the system is disciplined about when each appears.

The surfaces breathe through rounded geometry. Every button is a 50px full-pill. Cards take a 12px rounded-rectangle. The "Frap" floating CTA — a 56px circular order button in Green Accent (`{colors.primary}`) — is the product's signature depth move: it floats bottom-right with a layered shadow stack and compresses via `scale(0.95)` on press. Elevations are otherwise restrained — card shadows stay whisper-soft, global nav gets a quiet three-layer shadow stack. The whole system feels like clean café signage: legible, warm, and never shouting.

**Key Characteristics:**
- Four-tier green brand system (Starbucks / Accent / House / Uplift) each mapped to a distinct surface role
- Gold (`{colors.gold}`) reserved for Rewards-status moments only; never a general-purpose accent
- Warm-neutral canvas (`{colors.background}` / `{colors.background-ceramic}`) instead of cold white
- Custom proprietary typeface (SoDoSans) with tight `-0.01em` letter-spacing as the universal voice
- Context-specific type switches: serif for Rewards, script for Careers cup-names
- Full-pill buttons (`{rounded.pill}`) universal, `scale(0.95)` active press the signature micro-interaction
- Floating "Frap" circular CTA — the product's signature elevation element
- Gift-card surfaces designed as photographed physical product
- 12px card radius + whisper-soft shadows keep content cards flat-plus-hint-of-lift
- Rem-based spacing scale anchored at 1.6rem (~16px), stepping to 6.4rem (~64px)

**Color-block page rhythm:** Cream hero → White content sections → Dark-green (`{colors.house-green}`) feature band with white text → Cream utility zone → Dark-green footer with gold/white text — an espresso-dark bookend around the bright body.

## Colors

### Primary
- **Starbucks Green** (`{colors.brand-green}`): The historic brand green. Used on h1 headings, primary section headers on the Rewards page, and as the main brand signal wherever a single dominant color is needed.
- **Green Accent** (`{colors.primary}`): A slightly brighter, more luminous green. The primary filled-CTA color and the fill of the floating Frap circular button.
- **House Green** (`{colors.house-green}`): The deep near-black brand green. Footer surface, feature-band backgrounds, reward-status dark surfaces, and the Rewards hero band.
- **Green Uplift** (`{colors.green-uplift}`): A secondary mid-dark green used sparingly on decorative accents.
- **Green Light** (`{colors.green-light}`): A pale mint wash used for form-valid-state tints and light green utility surfaces.

### Secondary & Accent
- **Gold** (`{colors.gold}`): Reserved almost exclusively for Rewards-status ceremony — Gold-tier callouts, partnership badges (SkyMiles, Bonvoy), and premium-feeling accents. Never a general-purpose brand color.
- **Gold Light** (`{colors.gold-light}`): Softer gold for background washes on gold-tier sections.
- **Gold Lightest** (`{colors.surface-gold-cream}`): Cream-gold page-surface wash used under partnership sections — ties gold back into the warm neutral system.

### Surface & Background
- **White** (`{colors.surface}`): Primary card and modal surface.
- **Neutral Cool** (`{colors.surface-cool}`): Subtle cool-gray surface for dropdown menus, form-card wraps, quiet utility containers.
- **Neutral Warm** (`{colors.background}`): The warm cream primary page canvas.
- **Ceramic** (`{colors.background-ceramic}`): A slightly warmer/darker cream for zone separators and partnership band.
- **Black** (`{colors.black}`): Deep ink reserved for the dark top-of-page CTA strip and high-contrast top-nav sign-in buttons.

### Neutrals & Text
- **Text Black** (`{colors.ink}`): Primary heading and body text on light surfaces. Opaque approximation of `rgba(0,0,0,0.87)` — reads warmer than pure black.
- **Text Black Soft** (`{colors.ink-soft}`): Secondary/metadata text on light surfaces (opaque approx of `rgba(0,0,0,0.58)`).
- **Text White** (`{colors.ink-on-dark}`): Primary text on dark green surfaces.
- **Text White Soft** (`{colors.ink-on-dark-soft}`): Secondary text on dark-green surfaces (opaque approx of `rgba(255,255,255,0.70)`).
- **Rewards Green** (`{colors.ink-rewards}`): A dedicated muted slate-green used only on Rewards-page text blocks.

### Semantic
- **Red** (`{colors.error}`): Error and destructive state.
- **Yellow** (`{colors.warning}`): Warning state, legacy brand touch.

### Gradient System
No structural gradient tokens observed. Surface hierarchy is solid-color-block throughout — the system relies on its five-tier cream/green surface palette rather than gradients.

## Typography

### Font Family
- **Primary**: `SoDoSans, "Helvetica Neue", Helvetica, Arial, sans-serif`
- **Loading Fallback**: `"Helvetica Neue", Helvetica, Arial, sans-serif`
- **Rewards Serif**: `"Lander Tall", "Iowan Old Style", Georgia, serif`
- **Careers Script**: `"Kalam", "Comic Sans MS", cursive`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.h1}`, `{typography.body}`).

| Token | Use |
|---|---|
| `display` | Largest Rewards/hero display (80px) |
| `jumbo` | Secondary hero headings (58px) |
| `hero-large` | Landing section headlines (45px) |
| `h1` | Starbucks-Green primary heading (24/600) |
| `h2` | Regular-weight section title in Text Black (24/400) |
| `body-large` | Hero intro copy, feature-band body (19px) |
| `body` | Default body copy (16px) |
| `small`, `small-bold` | Button labels, metadata, form labels (14px) |
| `micro` | Active float-label state, caption micro-copy (13px) |
| `button`, `button-small` | All pill-button labels |
| `rewards-serif` | Rewards-page editorial headlines (Lander Tall) |
| `careers-script` | Careers-page handwritten cup-name moments (Kalam) |

### Principles
- **Tight negative tracking (`-0.01em`)** is applied almost universally — gives SoDoSans its confident presence without feeling squeezed.
- **Weight shifts carry hierarchy, not size shifts.** H1 and H2 share the same 24px size; only weight (600 vs 400) and color separate them.
- **Size tokens use rem anchored to `1rem = 10px`** via `font-size: 62.5%` root trick.
- **Context-specific typeface swaps** — serif on Rewards, script on Careers — are deliberate and localized.
- **Body text never goes pure black** — it sits at `{colors.ink}` to match the warm-neutral canvas temperature.

### Note on Font Substitutes
SoDoSans is proprietary (licensed from House Industries). Open-source substitutes: Inter, Manrope, Nunito Sans. Lander Tall (Rewards serif) is custom — substitute Iowan Old Style, Lora, or Source Serif Pro. Kalam is on Google Fonts directly.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Rem-based, anchored at `1rem = 10px`.

The universal rhythm constant is `sm` (16px) — the most frequent spacing unit across the system (default outer gutter, card padding baseline, body text size).

### Grid & Container
- Column width scale: 343px / 500px / 720px / 1440px
- Gift-card grid: 3–5 up responsive grid of ~343px tiles
- Rewards status section: 3-up dark-green panels at lg+
- Hero asymmetric split: 40% image / 60% content

### Whitespace Philosophy
Whitespace carries the feeling of "plenty of space in the café." Section padding leans generous (`xl`–`4xl`). Content blocks separated by whitespace rather than dividers. The cream canvas is itself a visual breath between white cards and green feature bands.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Card | Whisper-soft dual shadow tinted `{colors.shadow-card}` | Default content cards |
| Global Nav | Triple-layer soft lift tinted `{colors.shadow-card}` | Fixed top bar |
| Frap Base | Halo tinted `{colors.shadow-frap}` | Base around floating circular CTA |
| Frap Ambient | Stacked directional ambient tinted `{colors.shadow-frap}` | Floats Frap forward |
| Gift Card | Light drop shadow | Physical-card feel for gift tiles |

**Shadow philosophy**: Whisper-soft, layered over solid — never a single heavy drop shadow. The system stacks 2–3 low-alpha shadows with different offsets to simulate real-world ambient + direct lighting. The Frap button is the most elevated element on any page.

### Decorative Depth
- No gradient system — surfaces are solid color-block
- Color-block banding carries perceived depth (dark-green bands read as recessed feature zones between cream/white body sections)
- SVG filter shadows on Starbucks-Card visuals add slight 3D physicality

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Full-bleed feature bands |
| `xs` | 4px | Add-in/milk select inputs, store-availability selector |
| `md` | 12px | Cards, modals, menu-item tiles |
| `pill` | 50px | All buttons — universal full-pill |
| `circle` | 50px | Frap floating button, avatar thumbnails, circular icons |

## Components

The complete component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.button-frap}`).

### Buttons
Eight primary variants:
- **`button-primary`** — Filled Green Accent CTA pill ("Explore our afternoon menu").
- **`button-primary-outline`** — Transparent with green border ("Start an order").
- **`button-black`** — Black-filled "Join now" strip CTA.
- **`button-dark-outline`** — Transparent with dark border ("Sign in").
- **`button-inverted`** — White-filled with green text on house-green bands.
- **`button-outline-dark`** — White-bordered transparent on dark bands.
- **`button-consent`** — Slightly brighter green for cookie-consent Agree.
- **`button-frap`** — Floating 56px circular order button. Layered shadow stack and `scale(0.95)` active state.

PDP-specific buttons:
- **`button-customize`** — Outlined green pill with sparkle icon.
- **`button-add-to-order`** — Filled Green Accent pill.
- **`badge-rewards-cost`** — Gold-bordered "200★ item" pill on Rewards-eligible products.

### Cards & Containers
- **`card`** — White surface, `{rounded.md}` corners, whisper-soft dual shadow.
- **`card-partnership`** — Cream-gold partnership card on Rewards page.
- **`card-rewards-status`** — Dark-green tier panel (Bronze/Silver/Gold) for Rewards status grid.
- **`dropdown`** — Cool-neutral dropdown (Account menu).
- **`modal`** — White surface modal with generous top padding for header/close.

### Inputs & Forms
- **`input`** — Floating-label input. Label animates from base size up to `13px` when focused/filled. Valid state gets a green tint, invalid gets a red tint.
- **`input-select`** — Add-in / Milk outlined rectangle, 4px radius, floating uppercase label.
- Numeric stepper: `−` minus + count + `+` plus, circular 32px buttons with 1px border.

### Navigation
- **`nav-bar`** — Global top bar with progressive height (64px → 99px) and three-layer soft shadow.
- **`nav-link`** — Inline links in 14/600 SoDoSans.
- Sub-nav: 53px or 48px secondary horizontal tab group beneath the global nav.
- Mobile collapses to a hamburger drawer below tablet; the Frap floating button persists at bottom-right regardless of nav state.

### Feature Band
- **`feature-band`** — Full-width house-green strip with white text, paired CTAs (white-filled + outlined-on-dark), and product photography. 40/60 or 50/50 split.

### Feedback Tab
- **`tab-feedback`** — Fixed bottom-right "Provide feedback" tab with top-only rounded corners.

### Image Treatment
- Hero photography occupies ~40vw of a split-hero, text 60vw
- Gift card illustrations are distinct hand-drawn watercolor-feel photographs
- Image fade-in: `opacity 0.3s ease-in` on load

## Do's and Don'ts

### Do
- Use Neutral Warm (`{colors.background}`) or Ceramic (`{colors.background-ceramic}`) as page canvas instead of pure white
- Map the green tiers to their intended surface role (Starbucks Green for headings, Green Accent for CTAs, House Green for deep bands, Uplift for decorative)
- Keep tracking tight at `-0.01em` / `-0.16px` on SoDoSans across the whole system
- Use `{rounded.pill}` (50px) full-pill radius on every button without exception
- Apply `transform: scale(0.95)` as the universal button active state
- Reserve Gold (`{colors.gold}`) for Rewards-status ceremony moments only
- Use SoDoSans for nearly everything; Lander Tall serif only for Rewards editorial; Kalam script for Careers cup-names
- Layer 2–3 low-alpha shadows instead of one heavier drop shadow
- Use the Frap circular CTA as the persistent floating order entry on every shopping surface
- Let the cream canvas breathe between content cards — use whitespace, not dividers

### Don't
- Don't use pure white as the page canvas — the warm cream temperature is load-bearing
- Don't pick "one brand green" — the four-green system is intentional
- Don't use Gold as a general-purpose accent — it's a Rewards signal only
- Don't square the corners on buttons — the `{rounded.pill}` is universal
- Don't introduce gradient fills — the system is color-block throughout
- Don't weight-contrast h1 and h2 by size — hierarchy comes from weight + color
- Don't use pure black for body text — `{colors.ink}` matches the warm canvas
- Don't skip the `scale(0.95)` active feedback on buttons — it's a signature micro-interaction
- Don't stack single heavy shadows; always layer 2–3 low-alpha ones
- Don't introduce serifs or scripts into the main shopping flow

---

## Responsive Behavior

### Breakpoints

Inferred from component width tokens and progressive nav heights:

| Name | Width | Key Changes |
|------|-------|-------------|
| xs | < 480px | Global nav 64px; hamburger menu; single-column layouts; pill buttons full-width |
| Mobile | 480–767px | Global nav 72px; gift-card grid 2-up; card padding tightens |
| Tablet | 768–1023px | Global nav 83px; gift-card grid 3-up; hero split begins to appear |
| Desktop | 1024–1439px | Global nav 99px; gift-card grid 4-up; full asymmetric hero 40/60 |
| XLarge | 1440px+ | Content caps at column-width-XL; gift-card grid 5-up; extra cream margin |

### Touch Targets

- Pill buttons at `7px 16px` padding measure ~32px tall — below 44px WCAG AAA. On mobile, button padding may expand to meet the minimum.
- Frap floating circular button at `56px` is well above minimum.
- Frap uses an 8px touch offset to extend tap area beyond visual edge.
- Form float-label inputs grow their label font size on mobile for easier tapping.

### Collapsing Strategy

- **Global nav height scales progressively**: 64 → 72 → 83 → 99px across breakpoints
- **Hero split collapses**: 40/60 asymmetric → stacked at mobile
- **Gift-card grid**: 5-up → 4-up → 3-up → 2-up → 1-up
- **Feature bands**: Stay full-width but text + imagery stack vertically on mobile
- **Outer gutter scales**: 16px → 24px → 40px as viewport grows
- **Rewards 3-column status panels**: Stack to single column on mobile

### Image Behavior

- Hero product photography crops tighter vertically on mobile
- Gift-card illustrations preserve aspect ratio; card grid reflows
- `opacity 0.3s ease-in` fade-in transition on image load
- Rewards app-in-hand photography scales proportionally; never stretches

---

## Agent Prompt Guide

### Quick Color Reference

- Primary CTA: Green Accent (`{colors.primary}`)
- Primary CTA text: White (`{colors.on-primary}`)
- Brand heading: Starbucks Green (`{colors.brand-green}`)
- Feature band / footer: House Green (`{colors.house-green}`)
- Page canvas: Neutral Warm (`{colors.background}`)
- Card canvas: White (`{colors.surface}`)
- Heading text on light: Text Black (`{colors.ink}`)
- Body text on light: Text Black Soft (`{colors.ink-soft}`)
- Body text on dark-green: Text White Soft (`{colors.ink-on-dark-soft}`)
- Rewards accent: Gold (`{colors.gold}`)
- Rewards text: Rewards Green (`{colors.ink-rewards}`)
- Destructive: Red (`{colors.error}`)

### Example Component Prompts

1. "Create a primary Starbucks CTA pill button with Green Accent (`{colors.primary}`) background, white text 'Explore our afternoon menu', SoDoSans 16px weight 600 with `-0.01em` letter-spacing, `50px` border-radius, `7px 16px` padding. Apply `transform: scale(0.95)` as the active state with a `0.2s ease` transition."

2. "Design a content card with White (`{colors.surface}`) background at `12px` border-radius, layered shadow tinted `{colors.shadow-card}`. Pad contents `16–24px`. Place on a Neutral Warm (`{colors.background}`) page canvas with `16px` gap to siblings."

3. "Build the Frap floating circular order button — `56px` diameter, Green Accent (`{colors.primary}`) fill, white shopping-bag icon centered. Layered shadow tinted `{colors.shadow-frap}`. Fixed bottom-right with extended touch offset. Active state collapses ambient shadow with `scale(0.95)`."

4. "Build a dark-green feature band — full-width section with House Green (`{colors.house-green}`) background. Left column: white SoDoSans h2 at 24px weight 600, Text White Soft (`{colors.ink-on-dark-soft}`) body, paired CTAs (white-filled with green text + white-outlined). Right column: product photography. Split ratio 40/60, stacked vertically below 768px."

5. "Create a Rewards status card — House Green panel with `12px` border-radius, colored gradient top stripe (Bronze/Silver/Gold tier). Title in SoDoSans 24px weight 600 in white. Benefits list as white bullets with `{colors.ink-on-dark-soft}` secondary captions. Stack 3 panels at lg+, single column on mobile."

6. "Design a gift-card tile — card radius matches `12px`, fills with an illustrated photograph (hand-drawn watercolor-painted feel) as the entire surface. Subtle drop shadow makes it feel like a physical card on the cream canvas."

7. "Create a product-detail header — House Green band with breadcrumb in 14/400 white above a SoDoSans 32/700 uppercase white title. Product photograph centered. Below: 4-up size selector — cup icon, size name (16/700 white), fluid-ounce in 13/400 Text White Soft. Selected size wraps the cup in a `2px solid {colors.primary}` ring."

8. "Build a customize flow — under the size selector, 3 stacked outlined-rectangle input rows (white bg, `1px solid {colors.border-input}`, `4px` radius) with floating labels in 13/700 uppercase. Outlined green 'Customize' pill paired with Green Accent filled 'Add to Order' pill."

9. "Design a product description band — full-width House Green below product header. Top: gold-outlined '200★ item' Rewards Cost Pill. White 16/400/1.5 description, white 14/700 nutrition summary, white-outlined 'Full nutrition & ingredients list' pill button."

10. "Create a nutrition facts table — two-column layout inside a White card. Left: 'Ingredients' header (24/400). Right: 'Nutrition' label/value rows separated by `1px solid {colors.border-hairline}` hairlines. Footnote markers in 13/400 Text Black Soft."

### Iteration Guide

1. Focus on ONE component at a time
2. Reference specific color names from this document
3. Use natural language descriptions ("warm cream canvas," "four-tier green system") alongside exact values
4. Preserve `{rounded.pill}` + `scale(0.95)` active state universally
5. Check that greens are mapped to their correct role
6. Don't introduce gradients — the system is color-block
7. Keep SoDoSans tracking at `-0.01em` / `-0.16px` across the board

### Known Gaps

- SoDoSans is proprietary (not on Google Fonts) — substitute Inter or Manrope
- Lander Tall (Rewards serif) is also custom — substitute Iowan Old Style, Lora, or Source Serif Pro
- Specific per-component animation timings beyond the documented values are not captured for every interactive surface
- Form error-state full styling visible on the tint token but not exhaustively extracted
- Careers-page specific components (cup-name card, search radio grid) are referenced in token names but not covered here
- Starbucks Visa Card detailed mockup specs are hinted at by tokens but not fully documented
