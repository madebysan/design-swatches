---
version: alpha
name: Ivory (Tapbots)
description: Tapbots' tactile dimensional design language — warm off-black canvas, SF Pro via -apple-system, dimensional five-layer purple gradient buttons, and the signature Tapbots red mascot accent.

colors:
  # Base
  background: "#1a1a1a"
  surface: "#222222"
  ink: "#ffffff"
  on-primary: "#ffffff"

  # Brand purple spectrum
  primary: "#ba94ff"
  primary-light: "#deccff"
  periwinkle: "#cdd4f8"
  primary-deep: "#4c278e"

  # Tapbots red (signature mascot accent)
  tapbots-red: "#ff4d4d"

  # Button gradient stops
  gradient-top: "#c9a6ff"
  gradient-bottom: "#a07ff0"
  gradient-top-hover: "#d4b5ff"
  gradient-bottom-hover: "#a984ff"

  # Text scale
  text-secondary: "#c3c3c3"
  text-tertiary: "#999999"
  text-quaternary: "#666666"

  # Borders / shadows (opaque approximations)
  border: "#272727"  # was rgba(255,255,255,0.08) over #1a1a1a — Google format requires hex
  border-bright: "#2c2c2c"  # was rgba(255,255,255,0.12) — Google format requires hex
  rim-light: "#3a3a3a"  # was rgba(255,255,255,0.15) — Google format requires hex
  inset-highlight: "#5a5a5a"  # was rgba(255,255,255,0.25) — Google format requires hex

  # Shadow tints (opaque approximations on dark)
  shadow-ambient: "#3a2c5e"  # purple-tinted halo, opaque approx of rgba(186,148,255,0.25) on #1a1a1a
  shadow-contact: "#0d0d0d"  # was rgba(0,0,0,0.2) on #1a1a1a — Google format requires hex
  shadow-card: "#0a0a0a"  # was rgba(0,0,0,0.3) — Google format requires hex
  shadow-hero: "#050505"  # was rgba(0,0,0,0.4) — Google format requires hex

typography:
  display-hero:
    fontFamily: "-apple-system, BlinkMacSystemFont, helvetica-neue, helvetica, arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.20
    letterSpacing: 0px
  heading-bold:
    fontFamily: "-apple-system, BlinkMacSystemFont, helvetica-neue, helvetica, arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: 0px
  heading-regular:
    fontFamily: "-apple-system, BlinkMacSystemFont, helvetica-neue, helvetica, arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: 0px
  sub-heading-light:
    fontFamily: "-apple-system, BlinkMacSystemFont, helvetica-neue, helvetica, arial, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.40
    letterSpacing: 0px
  sub-heading-bold:
    fontFamily: "-apple-system, BlinkMacSystemFont, helvetica-neue, helvetica, arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: 0px
  body-large:
    fontFamily: "-apple-system, BlinkMacSystemFont, helvetica-neue, helvetica, arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  feature-heading:
    fontFamily: "-apple-system, BlinkMacSystemFont, helvetica-neue, helvetica, arial, sans-serif"
    fontSize: 21px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0px
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, helvetica-neue, helvetica, arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.70
    letterSpacing: 0px
  body-light:
    fontFamily: "-apple-system, BlinkMacSystemFont, helvetica-neue, helvetica, arial, sans-serif"
    fontSize: 21px
    fontWeight: 300
    lineHeight: 1.40
    letterSpacing: 0px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, helvetica-neue, helvetica, arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.70
    letterSpacing: 0px
  fine-print:
    fontFamily: "-apple-system, BlinkMacSystemFont, helvetica-neue, helvetica, arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  uppercase-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, helvetica-neue, helvetica, arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.80
    letterSpacing: 0px
  button:
    fontFamily: "-apple-system, BlinkMacSystemFont, helvetica-neue, helvetica, arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 10px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 30px
  3xl: 40px
  4xl: 48px
  5xl: 60px
  6xl: 80px

rounded:
  none: 0px
  sm: 10px
  md: 18px
  pill: 40px
  circle: 9999px

components:
  # Primary CTA — five-layer purple gradient pill
  button-primary:
    backgroundColor: "{colors.gradient-top}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 20px
  button-primary-hover:
    backgroundColor: "{colors.gradient-top-hover}"
    textColor: "{colors.on-primary}"
  button-primary-active:
    backgroundColor: "{colors.gradient-bottom}"
    textColor: "{colors.on-primary}"

  # Tapbots red text link
  link-red:
    backgroundColor: "{colors.background}"
    textColor: "{colors.tapbots-red}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 0px 0px
  link-red-hover:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Footer / nav link
  nav-link:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.nav-link}"
    padding: 4px 0px
  nav-link-hover:
    textColor: "{colors.ink}"

  # Card — feature container
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 30px
  card-hover:
    backgroundColor: "{colors.surface}"

  # Input — form field
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Mascot bird (decorative, non-interactive)
  mascot:
    backgroundColor: "{colors.background}"
    textColor: "{colors.tapbots-red}"
    rounded: "{rounded.none}"
    size: 40px

  # Avatar / circle chip
  avatar:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.circle}"
    size: 40px
---

# Ivory (Tapbots) Design System

## Overview

Tapbots has been carving dimensional iOS buttons since iPhone OS 2 — Paul Haddad and Mark Jardine have spent nearly two decades insisting that software should feel like a physical object. Tweetie, Twitterrific-adjacent, Tweetbot, Pastebot, Calcbot — every one of their apps has shipped with the same quiet philosophy: the screen is a surface, not a window. Buttons have backs. Icons have weight. Toggles click. When you pull-to-refresh, the r2-d2-meets-Atari sound isn't a gimmick — it's a reminder that you just did something physical. Ivory, their post-Twitter Mastodon client, is the purest expression of that legacy they've ever shipped.

The Ivory homepage is a dark, warm, almost cinematic stage built around the product. The background is an off-black `{colors.background}` — never pure `#000`, because Tapbots treats pure black as clinical and Ivory is *warm*. A muted lavender-periwinkle mist (`{colors.periwinkle}`) bleeds through the hero as ambient atmosphere. The mascot — the iconic red-outlined Tapbots bird, descended from the original "bot" robot face — sits in the footer like a signature. Iconography is custom-drawn, not licensed. Every screen shown is a real iOS screenshot with SF Pro Display text kerned to iOS defaults. The site doesn't try to look like a website; it tries to look like an iOS app someone tilted into landscape.

What sets Ivory apart from every other "we made a dark website" moment is its commitment to **tactile button construction.** Every primary CTA is a miniature object: a rounded capsule with a pill-gradient fill (`{colors.gradient-top}` → `{colors.gradient-bottom}`), an inset top-edge highlight simulating a light source overhead, a drop shadow pooling below, and a subtle ring of border color holding the whole thing together. This is the same button recipe Tapbots has been refining since Tweetbot 1.0 in 2011. It is the opposite of flat design. It is *crafted* — and that word, overused everywhere else, is load-bearing here.

**Key Characteristics:**
- Off-black warm dark background (`{colors.background}`) — never pure black
- SF Pro Display/Text native Apple stack — `-apple-system` first, no webfont downloads
- Dimensional CTA buttons with inset highlights + drop shadows + gradient fills
- Tapbots red mascot bird (`{colors.tapbots-red}`) as brand signature
- Purple-lavender accent spectrum (`{colors.primary}` → `{colors.primary-light}` → `{colors.periwinkle}`)
- Pill geometry: 40px border-radius on CTAs, 18px on feature cards
- Light weight 300 on large SF Pro Display headings, 600 on product-name moments
- Native iOS screenshots embedded as product hero — no mockups, no illustrations
- Small footer type (16px) with uppercase section headers — mirrors iOS Settings app
- Hand-crafted iconography — the Tapbots "mascot" bird is never outsourced

## Colors

Ivory's palette lives almost entirely in the dark-mode register. Warmth is the common thread: neutrals are cool-white gray scaled down, not blue-gray or true neutral.

### Primary
- **Off-Black Warm** (`{colors.background}`): Page background, section surfaces — never pure `#000`.
- **Paper White** (`{colors.ink}`): Body text on dark, button text on CTAs, headings.
- **Ivory Purple** (`{colors.primary}`): Primary CTA gradient anchor, link accent, hero glow.

### Purple Accent Spectrum
- **Lavender Light** (`{colors.primary-light}`): Soft highlight tint, paired with `{colors.primary}` for the signature CTA gradient.
- **Periwinkle Mist** (`{colors.periwinkle}`): Hero atmospheric glow, decorative background washes.
- **Purple Deep** (`{colors.primary-deep}`): Active/visited link on certain dark surfaces.

### Signature Accent
- **Tapbots Red** (`{colors.tapbots-red}`): The mascot bird outline, key hover links, brand punctuation.

### Neutral Scale (warm-tuned)
- **Text Strong** (`{colors.ink}`): Headlines on dark backgrounds, product names.
- **Text Primary** (`{colors.text-secondary}`): Body copy on dark.
- **Text Secondary** (`{colors.text-tertiary}`): Secondary paragraph text.
- **Text Tertiary** (`{colors.text-quaternary}`): Metadata, copyright lines, fine print.
- **Border Subtle** (`{colors.border}`): Card edges, divider hairlines on dark surfaces.

### Surface
- **Surface Elevated** (`{colors.surface}`): Feature cards, testimonial blocks — a single step of elevation above `{colors.background}`.

### Button Gradient Stops
The Ivory CTA gradient is the single most important color pairing in the system: `{colors.gradient-top}` (lighter purple, catches simulated overhead light) → `{colors.gradient-bottom}` (slightly darker purple, the "shadow" side of the pill). Hover variants use `{colors.gradient-top-hover}` and `{colors.gradient-bottom-hover}`.

## Typography

Tapbots uses the Apple system font stack exclusively. There are no custom webfonts, no variable fonts, no Google Fonts. The stack is `-apple-system, "helvetica-neue", helvetica, arial` — which resolves to SF Pro Display on modern Apple devices and degrades gracefully elsewhere. This is a deliberate identity choice.

### Font Family
- **Primary**: `-apple-system`, fallbacks `helvetica-neue, helvetica, arial, sans-serif`
- **No web fonts**: deliberate
- **No OpenType features**: SF Pro's default optical sizing handles the work

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens (`{typography.display-hero}`, `{typography.body}`) directly.

| Token | Use |
|---|---|
| `display-hero` | Whisper-weight 36px hero — Ivory product name moment |
| `heading-bold` | Feature section headings, weight 600 |
| `heading-regular` | Sub-section headings |
| `sub-heading-light` | Airy 24px sub-headings, quote moments |
| `sub-heading-bold` | Card titles with emphasis |
| `body-large` | Feature descriptions |
| `feature-heading` | In-card titles, footer column headers |
| `body` | Primary reading text — relaxed 1.7 leading |
| `body-light` | Lighter-weight body for spacious passages |
| `nav-link` | Footer section links |
| `fine-print` | Caption, secondary info |
| `uppercase-label` | All-caps metadata ("SYSTEM REQUIREMENTS", copyright) |
| `button` | Button labels |

### Principles
- **Native optical sizing**: SF Pro Display automatically swaps to SF Pro Text below 19px — no manual switching.
- **Light 300 for "atmosphere", bold 600 for "product"**: whisper-light is reserved for tagline and hero moments; 600 anchors product names and feature titles.
- **Relaxed body leading (1.70–1.80)**: body copy at 20px with line-height 1.70 is unusually airy for a dark-mode site.
- **No negative letter-spacing**: Ivory trusts SF Pro's native metrics.
- **Uppercase metadata at 16px with 1.8 line-height**: echoes iOS Settings screen labels.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is **8px** (extrapolated from 8/16/24/32/48 rhythm). Ivory uses *odd* pixel values that scale from the typographic system, not a strict 8px grid — this is type-driven spacing.

### Grid & Container
- Max content width: ~960px for text-heavy sections, up to 1612px on the hero
- Responsive breakpoints: 414px (iPhone), 500px (small tablet), 700px (large tablet)
- Footer columns: 4-column grid on desktop, collapsing to single-column on mobile

### Whitespace Philosophy
- **Breathing room around the product**: the hero iPhone mockup has 80px+ of dark space on all sides
- **Section separation via dark voids**: no background color swaps between sections; instead, 60–80px of vertical padding separates content blocks
- **Tight in-column density**: inside a footer column, link rows are stacked 8–12px apart

## Elevation & Depth — THE DIMENSIONAL BUTTON STACK

This section is the core of Tapbots' craft legacy. Every button on the Ivory site is built from a multi-layer shadow and gradient stack that simulates a physical, light-lit object.

### The Five-Layer Button Recipe

Every primary CTA assembles **five distinct visual layers**, rendered bottom-to-top in CSS paint order:

| Layer | Treatment | Purpose |
|---|---|---|
| 1. Ambient glow | `0 8px 24px {colors.shadow-ambient}` drop shadow | Wide, soft purple halo |
| 2. Contact shadow | `0 1px 2px {colors.shadow-contact}` drop shadow | Sharp, tight shadow directly below — anchors the object |
| 3. Gradient fill | `linear-gradient(180deg, {colors.gradient-top}, {colors.gradient-bottom})` | The "body" of the button |
| 4. Rim light | `1px solid {colors.rim-light}` border | Hairline rim catching the virtual edge light |
| 5. Inset highlight | `inset 0 1px 0 {colors.inset-highlight}` | The 1px white line along the top inside edge |

### Elevation Table

| Level | Treatment | Use |
|---|---|---|
| Flat (L0) | No shadow | Body copy backgrounds |
| Card (L1) | `0 4px 12px {colors.shadow-card}` + 1px `{colors.border}` border | Feature cards |
| CTA (L2) | Full five-layer stack | All primary buttons |
| Hero (L3) | `0 24px 60px {colors.shadow-hero}` + purple ambient glow behind | Hero iPhone mockup |
| Pressed (L-1) | `inset 0 2px 4px {colors.shadow-contact}`, no drop | Active button state — the "sunken" look |

### Shadow Philosophy

Tapbots shadows are never neutral. Every drop shadow has a **tint** that matches the element's color: purple buttons cast purple-tinted halos, the bird mascot can cast a red-tinted halo in hover states, dark cards cast warm-black shadows. This is the inheritance from 15 years of iOS dimensional buttons: the world is lit, and light passes through the object's color on its way to the surface below.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Inline links, mascot SVG |
| `sm` | 10px | Input fields, small tags |
| `md` | 18px | Feature cards, product hero containers |
| `pill` | 40px | CTA buttons — the signature Ivory shape |
| `circle` | 9999px | Avatar circles, icon chips |

Three radii, clear roles. No mid-range values.

## Components

The complete component spec lives in the `components:` token block above. Reference components directly (`{components.button-primary}`).

### Buttons
- **`button-primary`** — Five-layer dimensional purple gradient pill. The Tapbots signature. Hover: gradient brightens, shadows intensify. Active: `translateY(1px)` + inset dark shadow.
- **`link-red`** — Inline text link in Tapbots red, transitions to white on hover. No underline.

### Cards
- **`card`** — Surface-elevated with 1px subtle border, 18px radius, 30px padding. Hover: border brightens, no lift.

### Inputs
- **`input`** — Background-matched fill, 1px subtle border, 10px radius, focus state shifts the border to `{colors.primary}` with a tinted ring.

### Navigation / Footer
- **`nav-link`** — Footer column link, weight 600 title or weight 400 child link, hover to white.
- The bottom row uses uppercase 16px copyright and is the only uppercase text on the page.

### Distinctive
- **`mascot`** — Tapbots red bird, outline-only SVG, ~40px in the footer. Non-interactive, never animated.
- **`avatar`** — Circular crop, 50% radius.

## Do's and Don'ts

### Do
- Build every CTA from the full five-layer stack — gradient + border + inset highlight + contact shadow + ambient glow
- Use purple-tinted shadows on purple buttons, red-tinted shadows on red elements
- Use off-black `{colors.background}` — never pure `#000`
- Use SF Pro Display (via `-apple-system`) — never substitute Inter or Helvetica
- Embed real iOS screenshots of Ivory, not mockups or illustrations
- Keep the mascot bird visible but quiet — footer-sized, outline-only, Tapbots red
- Use 40px pill radius for CTAs and 18px rounded-square for cards
- Use weight 300 for whisper headings, weight 600 for product names
- Animate pressed buttons with `translateY(1px)` and inset-dark shadow

### Don't
- Don't use flat buttons. A flat button on an Ivory page reads as a broken element
- Don't use neutral gray drop shadows. Tint shadows to match the element's hue
- Don't use pure `#000` anywhere. The dark is warm
- Don't add a webfont. `-apple-system` is the entire typographic decision
- Don't use rounded-square buttons (4–8px radius). CTAs are pills. Cards are soft-squares
- Don't put the mascot bird in the hero. It's a footer-only signature
- Don't use generic lucide/heroicons for product UI. Icons should feel custom, weighted, dimensional
- Don't animate with long durations. Tapbots interactions are snappy — 80–150ms ease-out
- Don't use Material ripples or ink splashes
- Don't letter-space SF Pro. SF Pro's native tracking is the work

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <414px | Single-column footer, hero stacks, CTAs full-width |
| Mobile Large | 414–500px | iPhone-comfortable, footer stacks 2x2 |
| Tablet | 500–700px | Footer transitions to 4-column, hero side-by-side |
| Desktop | >700px | Full 4-column footer, max-width 960px content |

### Touch Targets
- Primary CTAs: 44px minimum height (native iOS touch target guideline) — achieved via 12px vertical padding on 16px text
- Footer links: 20px type with 1.70 line-height creates ~34px row — adequate for pointer targeting on desktop
- The mascot bird in the footer is non-interactive (no hover state) — just a brand signature

### Collapsing Strategy
- Hero: iPhone mockup scales down and stacks above copy on mobile; desktop shows copy-left, phone-right
- Footer: 4 equal columns on ≥700px, 2x2 grid on tablet, single-column stack on mobile
- CTA buttons: width fills container on mobile, auto-width on desktop
- Type scale: 36px hero → 28px on mobile; 32px heading → 24px on mobile
- Button dimensionality is preserved at all sizes — the shadow stack never flattens on mobile

---

## Agent Prompt Guide

### Quick Color Reference
- Page background: `{colors.background}` (warm off-black — never `#000`)
- Text primary: `{colors.ink}` (body on dark)
- Text secondary: `{colors.text-secondary}`
- Text tertiary: `{colors.text-tertiary}`
- Text metadata: `{colors.text-quaternary}`
- Ivory Purple: `{colors.primary}` (gradient anchor), `{colors.primary-light}` (gradient light end)
- Button gradient: `linear-gradient(180deg, {colors.gradient-top} 0%, {colors.gradient-bottom} 100%)`
- Tapbots Red: `{colors.tapbots-red}`
- Ambient glow: `{colors.shadow-ambient}` for purple
- Surface borders: `{colors.border}`

### Example Component Prompts
- "Build an Ivory CTA button: pill shape 40px radius, 12px×20px padding, purple gradient (`{colors.gradient-top}` top → `{colors.gradient-bottom}` bottom), inset white highlight on top edge, contact shadow, purple ambient halo, 1px `{colors.rim-light}` border, white text 16px weight 600 SF Pro."
- "Design an Ivory product hero: full-bleed `{colors.background}` background, radial purple glow `{colors.periwinkle}` at low alpha centered behind a real iOS screenshot framed in an iPhone bezel. Headline 36px SF Pro Display weight 300 white, tagline below at 20px weight 400 `{colors.text-secondary}`."
- "Build the Tapbots footer: four columns with 21px weight 600 titles in white and 20px weight 400 links in `{colors.text-secondary}` (hover → white). Centered Tapbots red mascot bird (outline only, 40px). Bottom row centered uppercase 16px copyright."
- "Create a feature card: `{colors.surface}` background, 1px `{colors.border}` border, 18px radius, 30px padding. Heading 24px weight 600 white, body 20px weight 400 `{colors.text-secondary}` line-height 1.70. Hover: border brightens to `{colors.border-bright}`, no lift."

### Iteration Guide
1. **Every button gets the five-layer stack.** No exceptions.
2. **Shadows inherit hue.** Purple things cast purple shadows.
3. **Use `-apple-system` only.** Don't substitute Inter, Helvetica, or a Google Font.
4. **Off-black, not pure black.** `{colors.background}` is the only correct page background.
5. **Pill 40px for CTAs, rounded 18px for cards, 10px for inputs.** Three radii, clear roles.
6. **Icons should have weight.** Use Solar Bold, Phosphor Fill, or SF Symbols.
7. **Whisper-light 300 for atmosphere, bold 600 for products.**
8. **Embed real iOS screenshots.** No mockups, no illustrations, no 3D-rendered phones.
9. **The mascot bird belongs in the footer.** Outline-only, Tapbots red, small.
10. **Pressed state: `translateY(1px)` + inset dark shadow.** Simulate physicality.
