---
version: alpha
name: Not Boring Apps
description: Maximalist dimensional skeuomorphism reborn. Saturated gradient fills, six-layer shadow stacks with inset highlights and indigo-tinted drops, hue-matched colored glows, and a deliberately-plain Founders Grotesk marketing site that frames the apps like a museum wall.

colors:
  # Marketing site (deliberately monochrome)
  ink: "#000000"
  background: "#ffffff"
  surface: "#ffffff"
  ink-soft: "#333333"
  gray-soft: "#aaaaaa"
  andy-yellow: "#ffe600"

  # App canvas
  app-canvas: "#f7f7f5"
  soft-cloud: "#ececf0"
  inked-gray: "#1a1a1d"
  midnight: "#0b0b12"
  stone: "#86868b"

  # Brand gradient stops (used as gradient pairs)
  sunrise-start: "#ff3366"
  sunrise-end: "#ff9933"
  electric-violet-start: "#a039ff"
  electric-violet-end: "#4e3bff"
  sky-ribbon-start: "#21c4ff"
  sky-ribbon-end: "#7b68ff"
  lime-pop-start: "#9cff2e"
  lime-pop-end: "#18c48a"
  sunset-peach-start: "#ff6b9a"
  sunset-peach-end: "#ffb86b"

  # Primary brand anchor (alias for the violet gradient end)
  primary: "#4e3bff"

  # App solids
  magenta: "#ff2e7a"
  electric-blue: "#3b5bff"
  solar-yellow: "#ffd23f"
  neon-lime: "#a6ff2e"
  deep-violet: "#4e3bff"
  tangerine: "#ff7a1a"

  # Inverted text
  on-primary: "#ffffff"
  on-dark: "#ffffff"

  # Shadow & highlight color tokens (opaque approximations)
  highlight-warm: "#fff7e6"   # was rgba(255,255,255,0.65) — flattened over warm tile
  highlight-cool: "#f0f4fa"   # was rgba(255,255,255,0.35) — flattened
  inner-rim: "#ebebeb"        # was rgba(0,0,0,0.08) — flattened over white
  drop-soft: "#dfdde6"        # was rgba(17,12,46,0.12) — flattened over white
  drop-deep: "#c4c0d2"        # was rgba(17,12,46,0.22) — flattened over white
  color-glow-violet: "#b6acf2" # was rgba(78,59,255,0.35) — flattened over white

typography:
  display-hero:
    fontFamily: "Founders Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 76px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0px
  display-large:
    fontFamily: "Founders Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 44px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0px
  display-medium:
    fontFamily: "Founders Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 44px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0px
  heading:
    fontFamily: "Founders Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  sub-heading:
    fontFamily: "Founders Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  body-large:
    fontFamily: "Founders Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 0.91
    letterSpacing: 0px
  body-small:
    fontFamily: "Founders Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.11
    letterSpacing: 0.5px
  body:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  micro-caps:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.67
    letterSpacing: 0.5px
  micro-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.67
    letterSpacing: 0.5px
  display-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px

spacing:
  micro: 4px
  xs: 5px
  xs-plus: 6px
  sm: 8px
  sm-plus: 10px
  md: 12px
  md-plus: 15px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 30px
  4xl: 40px
  5xl: 100px

rounded:
  sharp: 4px
  comfortable: 12px
  generous: 20px
  large: 24px
  hero: 32px
  pill: 999px

components:
  # Marketing site buttons
  button-primary-marketing:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-large}"
    rounded: "{rounded.sharp}"
    padding: 12px 30px 15px
  button-primary-marketing-hover:
    backgroundColor: "{colors.andy-yellow}"
    textColor: "{colors.ink}"
  button-outlined-marketing:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-large}"
    rounded: "{rounded.sharp}"
    padding: 12px 30px 15px

  # Signature dimensional pill (app)
  button-dimensional:
    backgroundColor: "{colors.electric-violet-start}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-large}"
    rounded: "{rounded.large}"
    padding: 14px 28px
  button-dimensional-pressed:
    backgroundColor: "{colors.electric-violet-end}"
    textColor: "{colors.on-primary}"

  # Tiles & cards (app)
  tile:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.heading}"
    rounded: "{rounded.generous}"
    padding: 20px
  tile-featured:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.heading}"
    rounded: "{rounded.large}"
    padding: 24px
  tile-compact:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-small}"
    rounded: "{rounded.comfortable}"
    padding: 16px

  # Icon cell (3D object)
  icon-cell:
    backgroundColor: "{colors.electric-violet-start}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.comfortable}"
    padding: 12px
    size: 56px

  # Inputs (marketing site — minimal underline)
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-small}"
    rounded: "{rounded.sharp}"
    padding: 12px 0px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-soft}"
    typography: "{typography.micro-link}"
    padding: 16px 30px

  # Status / category chip
  chip:
    backgroundColor: "{colors.app-canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.micro-caps}"
    rounded: "{rounded.pill}"
    padding: 4px 12px

  # Modal / overlay panel
  modal:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.hero}"
    padding: 24px
---

# Not Boring Apps Design System

## Overview

Not Boring Apps is Andy Allen's declaration of war on flat design. Where the rest of the industry spent a decade sanding every surface smooth — stripping shadows, killing bevels, flattening icons into single-color glyphs — Not Boring went the other direction with total conviction. Every pixel is pushed, molded, and dimensionalized until the interface feels less like a screen and more like a tray of small, expensive toys. The Calculator has a bar of soap for a display. The Weather app has a suspended marble that rotates to show the sky. The Habits app rewards you with confetti that bounces like real confetti. This is skeuomorphism reborn — not the iOS 6 leather-stitching caricature, but a new species: playful, precise, obsessively crafted, and proud of it.

The design language is built around the principle that software should feel *good to touch*. Buttons are never flat rectangles — they're beveled pills with an inside highlight near the top edge and a drop shadow underneath, mimicking the way light actually hits physical objects. Icons are never single-color glyphs — they're miniature 3D sculptures with gradients, rim lights, and subtle ambient occlusion. Colors are never muted for the sake of sophistication — they're saturated to the edge of taste, often running as gradients from one vivid hue to another (magenta to violet, lime to teal, electric blue to cyan). The website itself (notboring.software) is a deliberate foil: black on white (`{colors.background}` + `{colors.ink}`), Founders Grotesk, an almost-boring Webflow scaffold that acts as a neutral museum wall. The real design lives one tap away, inside the apps. That contrast — plain gallery, extraordinary objects — is the whole pitch.

What cements Not Boring's stature is the Apple Design Award on the shelf for Not Boring Weather (2022), plus the repeated acclaim for Calculator and Habits. Apple's own design team pointed to Not Boring as evidence that the iOS platform still rewards craft, even when the platform's own chrome has gone Swiss-minimalist. Every detail in a Not Boring app is a quiet rebellion: the tap haptic that matches the visual bounce, the sound design that sounds like actual wood or glass, the way a button press briefly deforms the surface rather than just changing color. The system is maximalism with the rigor of minimalism — every tactile embellishment earns its place by doing a job: reinforcing state, providing feedback, or just making a boring routine a little less boring.

**Key Characteristics:**
- Saturated, high-chroma colors with gradient fills as the default (not an accent)
- Multi-layer dimensional shadows: inset highlight near top + soft drop shadow below + occasional colored glow
- Generous border-radius (12px-24px+) on tiles and buttons, full pills (`{rounded.pill}`) on primary CTAs
- Founders Grotesk + JetBrains Mono as the website pairing; custom type + SF Pro inside the apps
- Icons rendered as small 3D objects — beveled, gradient-filled, with highlights and soft shadows
- Tactile button treatment: top highlight, side bevel, drop shadow, pressed-state compression
- Playful-but-rigorous: nothing is random; every dimensional flourish serves feedback or delight
- Black-on-white marketing site that deliberately contrasts with the maximalist apps

## Colors

Not Boring's palette splits cleanly in two. The **website** uses a near-monochrome Webflow palette — black text on white. The **apps** themselves run a maximalist chromatic language built on saturated gradients and vivid solids.

### Primary (Marketing Site)
- **Pure Black** (`{colors.ink}`): Primary text, button backgrounds, logo
- **Pure White** (`{colors.background}`): Page canvas, button text on dark, card backgrounds
- **Near Black** (`{colors.ink-soft}`): Body copy, link default
- **Soft Gray** (`{colors.gray-soft}`): Secondary captions, muted metadata
- **Andy Yellow** (`{colors.andy-yellow}`): Hover state accent, the single warm accent on the otherwise monochrome site

### Brand Accent (Apps — Vivid Gradients)

Not Boring's app icons and UI are built on gradient fills running corner-to-corner (135°). Token pairs:

- **Sunrise**: `{colors.sunrise-start}` → `{colors.sunrise-end}` — coral-to-amber, Calculator display glow, morning/warm moments
- **Electric Violet**: `{colors.electric-violet-start}` → `{colors.electric-violet-end}` — magenta-to-indigo, primary "dimensional" gradient, hero buttons, Habits reward
- **Sky Ribbon**: `{colors.sky-ribbon-start}` → `{colors.sky-ribbon-end}` — cyan-to-periwinkle, Weather daytime panel
- **Lime Pop**: `{colors.lime-pop-start}` → `{colors.lime-pop-end}` — neon-lime to teal, success and streaks
- **Sunset Peach**: `{colors.sunset-peach-start}` → `{colors.sunset-peach-end}` — hot pink to apricot, gentle evening tones

### App Solids (High-Chroma)
- **Magenta** (`{colors.magenta}`): Attention, hot CTAs, streak highlights
- **Electric Blue** (`{colors.electric-blue}`): Primary interactive state, link color inside apps
- **Solar Yellow** (`{colors.solar-yellow}`): Playful emphasis, the Andy Yellow app-side cousin
- **Neon Lime** (`{colors.neon-lime}`): Confirmation, success
- **Deep Violet** (`{colors.deep-violet}`): Dimensional shadow tint, dark-mode anchor
- **Tangerine** (`{colors.tangerine}`): Warning, alerts that still feel friendly

### Neutrals
- **Off-White** (`{colors.app-canvas}`): App canvas — the slightest warm tint away from pure white
- **Soft Cloud** (`{colors.soft-cloud}`): Secondary surfaces, unselected tile backgrounds
- **Inked Gray** (`{colors.inked-gray}`): Dark-mode canvas, button stroke on light surfaces
- **Midnight** (`{colors.midnight}`): Dark-mode deepest layer
- **Stone** (`{colors.stone}`): Tertiary text, disabled states

### Shadow & Highlight Colors

Not Boring's dimensionality depends on paired highlight and shadow layers. These are the component colors (opaque approximations of the original rgba values, used in declarations):

- **Top Highlight Warm** (`{colors.highlight-warm}`): Inset top-edge highlight — "light hitting the plastic" (was `rgba(255, 255, 255, 0.65)`)
- **Top Highlight Cool** (`{colors.highlight-cool}`): Softer highlight for deeper/darker surfaces
- **Inner Rim** (`{colors.inner-rim}`): Inset bottom-edge shadow — bottom edge of the bevel
- **Drop Soft** (`{colors.drop-soft}`): Ambient drop shadow, brand-tinted with indigo
- **Drop Deep** (`{colors.drop-deep}`): Primary drop shadow for elevated pills
- **Color Glow** (`{colors.color-glow-violet}`): Hue-matched glow shadow under vivid buttons (was `rgba(78, 59, 255, 0.35)`)

### Gradient System
Gradients are the system, not a flourish. Every primary CTA, every icon, every celebratory surface uses a gradient rather than a flat fill. Standard direction is 135° (top-left to bottom-right), aligning with the implied light source that also governs shadows and highlights. Two-color gradients dominate; three-color gradients appear occasionally on hero moments. **The rule:** if a surface is going to be an "object" (a button, a tile, an icon), it gets a gradient. If it's chrome (borders, dividers, text), it stays solid.

## Typography

### Font Family
- **Primary (Website)**: `Founders Grotesk`, with fallback: `"Helvetica Neue", Arial, sans-serif`. Klim Type Foundry's signature grotesk — geometric but warm, with distinctive round terminals.
- **Mono (Website)**: `JetBrains Mono`, uppercase, wide tracking — used for metadata and micro labels.
- **Body (Website)**: `Arial` — intentionally boring system fallback for smaller copy, reinforcing the "plain gallery" stance.
- **Apps**: Default to `SF Pro` / `-apple-system` on iOS, often paired with custom display type per app.

*Note: For external implementations, `Inter` is a strong web-safe substitute for Founders Grotesk at weight 500-600. Keep JetBrains Mono as-is — free and open-source.*

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference each role via tokens.

| Token | Use |
|---|---|
| `display-hero` | Landing page hero — bold, grounded |
| `display-large` | Section anchors |
| `display-medium` | Lighter section intros |
| `heading` | Feature cards, app titles |
| `sub-heading` | Secondary titles, descriptions |
| `body-large` | Button labels, emphasized copy |
| `body-small` | Meta labels, small headings |
| `body` | Standard body, captions (Arial, by design) |
| `micro-caps` | Micro labels (uppercase JetBrains Mono) |
| `micro-link` | Footer links (uppercase Arial) |
| `display-link` | Oversized nav/footer links |

### Principles
- **Two-font contrast**: Founders Grotesk for presence, Arial for plainness. The combination is deliberate — when the apps are maxed out, the site stays quiet.
- **Uppercase mono for chrome**: JetBrains Mono at 12px uppercase marks UI chrome, section labels, and technical metadata.
- **Weight 600 as default headline**: Unlike Stripe/Cape (which run weight 300), Not Boring's marketing uses confident weight 600-700.
- **Tight display line-height (1.00)**: Headlines sit tight and grounded.
- **Progressive fallback**: Headings use Founders Grotesk; body often drops to Arial. Not lazy — it's a stated preference for system defaults in "boring" contexts.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is `{spacing.sm}` (8px). The marketing site uses `{spacing.5xl}` (100px) generously for section padding; apps run denser at 12–20px for tile internals.

### Grid & Container
- Marketing max-width: ~1000px (tight, editorial)
- Hero: centered single column with a 3D illustration as focal point
- Feature grid: 2–3 columns on desktop, single-column stack on mobile
- Apps: full-device canvas, no fixed max-width — everything respects iOS safe areas

### Whitespace Philosophy
- **Generous around objects**: Dimensional 3D elements need room to breathe — shadows extend beyond element bounds.
- **Dense inside objects**: A Not Boring tile might have 6 pieces of information, but each sits on its own micro-surface (a pill, a chip, a segment). Information is layered into the object, not laid out around it.
- **Asymmetric button padding**: `12px 30px 15px` (top-right-bottom-left is not default) — bottom padding is slightly greater than top to account for the optical center of the bevel's highlight/shadow pair.

## Elevation & Depth

This is the heart of Not Boring. Where most design systems have 3–4 elevation levels each defined by a single drop shadow, Not Boring's elevation is built from **paired layers**: a highlight layer on top and a shadow layer below, with additional colored glow when the element is a vivid-gradient "object."

### The Six-Layer Shadow Stack

A fully-dimensional Not Boring button uses up to six simultaneous shadow declarations:

```css
box-shadow:
  /* 1. Inset top highlight — the light hitting the top bevel */
  inset 0 1px 0 0 rgba(255, 255, 255, 0.65),
  /* 2. Inset top glow — soft bloom below the highlight */
  inset 0 2px 6px -2px rgba(255, 255, 255, 0.35),
  /* 3. Inset bottom shadow — darkening at the bottom bevel */
  inset 0 -2px 4px -1px rgba(0, 0, 0, 0.18),
  /* 4. Outer ambient — close, soft lift */
  0 2px 4px 0 rgba(17, 12, 46, 0.12),
  /* 5. Outer drop — main elevation */
  0 12px 24px -4px rgba(17, 12, 46, 0.22),
  /* 6. Colored glow — hue-matched shadow spreading below */
  0 20px 40px -8px rgba(78, 59, 255, 0.35);
```

### Elevation Levels

| Level | Composition | Use |
|---|---|---|
| Flat (0) | No shadow | Background text, inline copy |
| Stamped (1) | Inset highlight only | Subtle 3D-ness on chips and badges |
| Tile (2) | Inset highlight + soft drop using `{colors.drop-soft}` | Standard tiles on app canvas |
| Card (3) | Full paired stack: top inset + bottom inset + ambient drop + deep drop (`{colors.drop-deep}`) | Featured cards, modal contents |
| Pill (4) | Full stack + colored glow matching element hue (e.g. `{colors.color-glow-violet}`) | Primary CTAs, hero buttons |
| Overlay (5) | Pill stack + larger spread + darker ambient | Modals, floating panels, overlays |
| Pressed | Compressed: reduced outer shadows, deeper inset bottom | Active/touch state — feels physically depressed |

### The Shadow Philosophy

Not Boring's shadows are not just *elevation* — they're *illumination*. The system assumes a single soft light source from the top (roughly 10° off vertical):

1. **Top edges always brighter** (inset white highlight)
2. **Bottom edges always darker** (inset dark shadow)
3. **Drop shadow always below** the element
4. **Colored glow matches the element's hue family** — a magenta button drops magenta light, a cyan button drops cyan light

### Pressed States (Tactile Feedback)

When a button is tapped, three things happen simultaneously:
- Outer drop shadows reduce by ~50% (element sinks toward surface)
- Inset bottom shadow deepens by ~30% (compression effect)
- Element transforms `translateY(1px) scale(0.98)` — barely perceptible but crucial

## Shapes

| Token | Value | Use |
|---|---|---|
| `sharp` | 4px | Marketing buttons, inputs, dividers — deliberately plain |
| `comfortable` | 12px | Small app chrome |
| `generous` | 20px | Standard app tiles, secondary buttons, cards |
| `large` | 24px | Featured tiles, dimensional CTAs |
| `hero` | 32px | Wallet-card-style elements, modals |
| `pill` | 999px | Primary CTAs, toggle segments, control pills |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (e.g. `{components.button-dimensional}`, `{components.tile-featured}`) rather than reconstructing them.

### Marketing Buttons
- **`button-primary-marketing`** — Black on white, sharp 4px corners. Hover fills to Andy Yellow.
- **`button-outlined-marketing`** — White with 2px black outline. Hover fills to Andy Yellow.

### Dimensional App Buttons (the signature)
- **`button-dimensional`** — Gradient-filled pill or `{rounded.large}` rectangle with the full six-layer shadow stack. Pair with one of the brand gradient color pairs (Electric Violet, Sky Ribbon, Lime Pop, Sunrise, Sunset Peach).
- **`button-dimensional-pressed`** — Compressed variant: translateY(1px) + scale(0.98), reduced outer shadows, deeper inset bottom.

### Tiles & Cards
- **`tile`** — Standard `{rounded.generous}` tile, white surface with subtle warm-to-cool overlay, dimensional shadow stack.
- **`tile-featured`** — Larger `{rounded.large}` featured tile with stronger drop shadow.
- **`tile-compact`** — Smaller `{rounded.comfortable}` chip-tile.

### Icons — 3D Objects
- **`icon-cell`** — 56×56 (or 64×64) gradient-filled rounded square. Pair with inset top highlight + bottom shadow + colored hue-matched drop.

### Inputs
- **`input`** — Marketing form field, underline only (2px black bottom border), sharp corners, no fill.

### Navigation
- **`nav-bar`** — Sticky horizontal, Arial 12px uppercase, Andy Doodle logo left, black pill CTA right.

### Chip
- **`chip`** — Pill-shaped JetBrains Mono uppercase tag for category and metadata.

### Modal
- **`modal`** — Wallet-card-style overlay with `{rounded.hero}` corners.

### Decorative Elements
- **3D object illustrations** — Rendered 3D toys (cubes, spheres, pills, marbles) in heroes and empty states.
- **Gradient ribbons** — long horizontal gradient strips used as accent dividers or progress fills.
- **Confetti** — physically-simulated celebratory particles on completion states.

## Do's and Don'ts

### Do
- **Use gradient fills as the default** for any interactive "object" (buttons, tiles, icons) — not as a special accent
- **Layer your shadows**: at minimum, pair an inset top highlight with an outer drop shadow. For primary CTAs, add a colored glow
- **Tint your shadows**: use `{colors.drop-deep}`-style indigo-tinted shadows rather than pure neutral black — it ties shadows to the palette
- **Match colored glows to the element's hue** — a magenta button has a magenta glow, a lime button has a lime glow
- **Use generous border-radius** (`{rounded.generous}`–`{rounded.large}`) on tiles and secondary buttons; full pills (`{rounded.pill}`) on primary CTAs
- **Use Founders Grotesk 600-700** for marketing headlines — this is a confident brand, not a whisper
- **Respect the pressed state**: compress the element on tap, don't just change its color
- **Pair saturated colors** — magenta with violet, cyan with periwinkle, lime with teal. Single-hue designs feel under-built here.
- **Use bevels, highlights, and gradients proudly** — they're the whole point
- **Treat icons as 3D objects** — gradient fills, inset highlights, colored drop shadows

### Don't
- **Don't go flat.** A single-color button with no inset highlight betrays the entire brand thesis.
- **Don't use neutral gray drop shadows** — always tint with the brand's indigo or a color matching the element's hue
- **Don't use sharp 0–2px radius** on app tiles or CTAs — that's Cape's language, not Not Boring's. Save sharp corners for the marketing site's plain chrome.
- **Don't mute the palette** — Not Boring's colors are maxed-out on purpose. Desaturating them kills the toy-like quality.
- **Don't use solid fills on primary CTAs** — the dimensional gradient with paired highlight/shadow is non-negotiable
- **Don't skip the pressed state** — a Not Boring button that doesn't physically react to touch feels broken
- **Don't use web-safe stock iconography** (Font Awesome outlines, thin-line glyphs) — pick `solar:*-bold` or `ph:*-fill` and layer dimensional treatments on top
- **Don't be tasteful to the point of being quiet** — Not Boring's whole thesis is that polite flatness is the enemy of good software. Lean in.

---

## Responsive Behavior

### Breakpoints (from Dembrandt extraction)
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <479px | Single column, collapsed nav, reduced hero sizes |
| Mobile | 479-767px | Single column, full-width tiles |
| Tablet | 768-991px | 2-column feature grids, medium padding |
| Desktop | >991px | Full layout, 3-column grids, generous 100px section padding |

### Touch Targets
- Marketing buttons: 22px type + 12-15px vertical padding = ~52px tap height (comfortable)
- App primary CTAs: 14px type + 14-16px vertical padding + full-pill radius = 48px+ tap height with large radius making the hit area forgiving

### Collapsing Strategy
- Hero: 76px display → 44px on tablet → 36px on mobile, weight 700 maintained
- Navigation: horizontal Arial uppercase links → hamburger toggle below 768px
- 3D hero object: scales proportionally, maintains its ray-traced highlights at all sizes
- Feature grids: 3-column → 2-column → single column
- Section padding: 100px desktop → 40px mobile
- Inside apps: dimensional treatments persist at all sizes — shadows scale proportionally with the element

### Image Behavior
- 3D illustration assets are rendered at 2x-3x and scaled down for crispness
- Gradient fills are pure CSS (no image files) so they scale infinitely
- App screenshots on the marketing site maintain device-frame chrome and drop the same indigo-tinted shadow stack

---

## Agent Prompt Guide

### Quick Color Reference
- Marketing text: Pure Black (`#000000`)
- Marketing hover/accent: Andy Yellow (`#ffe600`)
- App canvas: Off-White (`#f7f7f5`)
- Primary app gradient: Electric Violet (`#a039ff` → `#4e3bff`, 135°)
- Secondary app gradient: Sky Ribbon (`#21c4ff` → `#7b68ff`, 135°)
- Success gradient: Lime Pop (`#9cff2e` → `#18c48a`, 135°)
- Warm gradient: Sunrise (`#ff3366` → `#ff9933`, 135°)
- Ambient drop shadow tint: indigo (`rgba(17, 12, 46, 0.22)`)
- Colored glow: match element hue at ~35% alpha

### Example Component Prompts

- **"Build a Not Boring primary CTA."** Full pill (border-radius 999px or 16px generous). Background `linear-gradient(135deg, #a039ff 0%, #4e3bff 100%)`. White text, Founders Grotesk 600 (or SF Pro 600). Padding 14px 28px. Shadow stack: `inset 0 1px 0 rgba(255,255,255,0.65), inset 0 -2px 4px rgba(0,0,0,0.18), 0 2px 4px rgba(17,12,46,0.12), 0 12px 24px -4px rgba(78,59,255,0.35)`. On press: translateY(1px) scale(0.98) + reduced outer shadows.

- **"Design a Not Boring app tile."** Background white with subtle `linear-gradient(180deg, #ffffff 0%, #f7f7f5 100%)` overlay. Border-radius 20px. No border. Shadow: `inset 0 1px 0 rgba(255,255,255,0.8), 0 2px 6px rgba(17,12,46,0.08), 0 18px 36px -12px rgba(17,12,46,0.22)`. Hover: translateY(-2px), shadows intensify 20%.

- **"Create a Not Boring icon cell."** 56x56 or 64x64 rounded square (radius 16px). Filled with a 135° brand gradient (pick from palette). Add `inset 0 1px 0 rgba(255,255,255,0.7)` top highlight and `inset 0 -1px 0 rgba(0,0,0,0.15)` bottom shadow. Drop shadow matches icon's hue at 35% alpha.

- **"Design the marketing hero headline."** Founders Grotesk 76px weight 700, line-height 1.00, color `#000000`. Tagline below in Founders Grotesk 24px weight 400, line-height 1.43, color `#333333`. Emoji allowed inline. Black pill CTA right-aligned or centered.

- **"Build a pressed-state variant."** Start from the primary CTA. Apply: transform `translateY(1px) scale(0.98)`, reduce outer shadows by 50%, deepen inset bottom shadow to `rgba(0,0,0,0.26)`. The button should *feel* pushed, not just darkened.

### Iteration Guide
1. **Start with the gradient.** Every "object" surface starts with a 135° two-color gradient from the palette. Never a solid fill on a CTA.
2. **Add the inset top highlight** next (`inset 0 1px 0 rgba(255,255,255,0.6-0.8)`). This single line of CSS is what makes a rectangle feel like a physical object.
3. **Add the outer drop shadow** tinted with `rgba(17, 12, 46, …)`. Never use neutral black-only shadows.
4. **If it's a primary CTA, add a colored glow** matching the element's hue (~35% alpha, 20-40px blur, negative spread).
5. **Border-radius lives in 16-24px for tiles, full pills for CTAs**. Sharp corners (0-4px) are reserved for the marketing chrome.
6. **Use Founders Grotesk 600-700 for headlines.** This brand is confident, not whispered.
7. **Pressed states compress the element**. Without this, Not Boring buttons are static sculptures — with it, they're alive.
8. **When in doubt, add more dimension, not less.** The entire point is that flatness is the enemy. Bevel it, highlight it, glow it, press it.
