---
slug: notboring
name: Not Boring Apps
url: https://notboring.software
domain: notboring.software
category: Productivity
styles: [Tactile, Colorful, Gradient, Bold]
tagline: "Beveled pills, gradient-saturated hues, and multi-layer shadows that make pixels feel pressable."
fonts: [Founders Grotesk, JetBrains Mono, Arial]
primary_color: "#0000ee"
---

# Design System Inspired by Not Boring Apps

> Beveled pills, gradient-saturated hues, and multi-layer shadows that make pixels feel pressable.

## 1. Visual Theme & Atmosphere

Not Boring Apps is Andy Allen's declaration of war on flat design. Where the rest of the industry spent a decade sanding every surface smooth — stripping shadows, killing bevels, flattening icons into single-color glyphs — Not Boring went the other direction with total conviction. Every pixel is pushed, molded, and dimensionalized until the interface feels less like a screen and more like a tray of small, expensive toys. The Calculator has a bar of soap for a display. The Weather app has a suspended marble that rotates to show the sky. The Habits app rewards you with confetti that bounces like real confetti. This is skeuomorphism reborn — not the iOS 6 leather-stitching caricature, but a new species: playful, precise, obsessively crafted, and proud of it.

The design language is built around the principle that software should feel *good to touch*. Buttons are never flat rectangles — they're beveled pills with an inside highlight near the top edge and a drop shadow underneath, mimicking the way light actually hits physical objects. Icons are never single-color glyphs — they're miniature 3D sculptures with gradients, rim lights, and subtle ambient occlusion. Colors are never muted for the sake of sophistication — they're saturated to the edge of taste, often running as gradients from one vivid hue to another (magenta to violet, lime to teal, electric blue to cyan). The website itself (notboring.software) is a deliberate foil: black on white, Founders Grotesk, an almost-boring Webflow scaffold that acts as a neutral museum wall. The real design lives one tap away, inside the apps. That contrast — plain gallery, extraordinary objects — is the whole pitch.

What cements Not Boring's stature is the Apple Design Award on the shelf for Not Boring Weather (2022), plus the repeated acclaim for Calculator and Habits. Apple's own design team pointed to Not Boring as evidence that the iOS platform still rewards craft, even when the platform's own chrome has gone Swiss-minimalist. Every detail in a Not Boring app is a quiet rebellion: the tap haptic that matches the visual bounce, the sound design that sounds like actual wood or glass, the way a button press briefly deforms the surface rather than just changing color. The system is maximalism with the rigor of minimalism — every tactile embellishment earns its place by doing a job: reinforcing state, providing feedback, or just making a boring routine a little less boring.

**Key Characteristics:**
- Saturated, high-chroma colors with gradient fills as the default (not an accent)
- Multi-layer dimensional shadows: inset highlight near top + soft drop shadow below + occasional colored glow
- Generous border-radius (12px-24px+) on tiles and buttons, full pills on primary CTAs
- Founders Grotesk + JetBrains Mono as the website pairing; custom type + SF Pro inside the apps
- Icons rendered as small 3D objects — beveled, gradient-filled, with highlights and soft shadows
- Tactile button treatment: top highlight, side bevel, drop shadow, pressed-state compression
- Playful-but-rigorous: nothing is random; every dimensional flourish serves feedback or delight
- Black-on-white marketing site that deliberately contrasts with the maximalist apps

## 2. Color Palette & Roles

Not Boring's palette splits cleanly in two. The **website** uses a near-monochrome Webflow palette — black text on white, with `#0000ee` raw link blue and `#aaaaaa` gray for captions. The **apps** themselves run a maximalist chromatic language built on saturated gradients and vivid solids. This DESIGN.md documents both, but leans into the app palette because that's where the brand actually lives.

### Primary (Marketing Site)
- **Pure Black** (`#000000`): Primary text, button backgrounds, logo. No softening — Not Boring's website uses true black.
- **Pure White** (`#ffffff`): Page canvas, button text on dark, card backgrounds.
- **Near Black** (`#333333`): Body copy, link default — slightly softened from pure black for paragraph comfort.
- **Soft Gray** (`#aaaaaa`): Secondary captions, muted metadata.
- **Andy Yellow** (`#ffe600`): Hover state accent (`--andyyellow` in source), playful punctuation. The single warm accent on an otherwise monochrome site.

### Brand Accent (Apps — Vivid Gradients)
Not Boring's app icons and UI are built on gradient fills running corner-to-corner. These are the signature blends:

- **Sunrise** (`#ff3366` → `#ff9933`): Coral-to-amber gradient — the Calculator display glow, morning/warm moments.
- **Electric Violet** (`#a039ff` → `#4e3bff`): Magenta-to-indigo — the primary "dimensional" gradient, used on hero buttons and the Habits reward state.
- **Sky Ribbon** (`#21c4ff` → `#7b68ff`): Cyan-to-periwinkle — Weather app's daytime panel, cool interactive surfaces.
- **Lime Pop** (`#9cff2e` → `#18c48a`): Neon-lime to teal — success states, streaks, celebratory moments.
- **Sunset Peach** (`#ff6b9a` → `#ffb86b`): Hot pink to apricot — gentle evening tones, alternate positive state.

### App Solids (High-Chroma)
- **Magenta** (`#ff2e7a`): Attention, hot CTAs, streak highlights.
- **Electric Blue** (`#3b5bff`): Primary interactive state, link color inside apps.
- **Solar Yellow** (`#ffd23f`): Playful emphasis, the "Andy Yellow" app-side cousin — warmer, richer.
- **Neon Lime** (`#a6ff2e`): Confirmation, success.
- **Deep Violet** (`#4e3bff`): Dimensional shadow tint, dark-mode anchor.
- **Tangerine** (`#ff7a1a`): Warning, alerts that still feel friendly.

### Neutrals
- **Off-White** (`#f7f7f5`): App canvas — the slightest warm tint away from pure white, giving surfaces a paper-like warmth under bright dimensional content.
- **Soft Cloud** (`#ececf0`): Secondary surfaces, unselected tile backgrounds.
- **Inked Gray** (`#1a1a1d`): Dark-mode canvas, button stroke on light surfaces.
- **Midnight** (`#0b0b12`): Dark-mode deepest layer — almost black, with a blue undertone to complement the vivid gradients.
- **Stone** (`#86868b`): Tertiary text, disabled states.

### Shadow & Highlight Colors
Not Boring's dimensionality depends on paired highlight and shadow layers. These are the component colors, not opaque fills:

- **Top Highlight Warm** (`rgba(255, 255, 255, 0.65)`): Inset top-edge highlight on buttons and tiles — the "light hitting the plastic."
- **Top Highlight Cool** (`rgba(255, 255, 255, 0.35)`): Softer highlight for deeper/darker surfaces.
- **Inner Rim** (`rgba(0, 0, 0, 0.08)`): Inset bottom-edge shadow — the "bottom edge of the bevel."
- **Drop Soft** (`rgba(17, 12, 46, 0.12)`): Ambient drop shadow, brand-tinted with indigo.
- **Drop Deep** (`rgba(17, 12, 46, 0.22)`): Primary drop shadow for elevated pills.
- **Color Glow** (`rgba(78, 59, 255, 0.35)`): Colored glow shadow under vivid buttons — shadow that matches the element's hue.

### Gradient System
Gradients are the system, not a flourish. Every primary CTA, every icon, every celebratory surface uses a gradient rather than a flat fill. Standard direction is 135° (top-left to bottom-right), which aligns with the implied light source that also governs shadows and highlights. Two-color gradients dominate; three-color gradients appear occasionally on hero moments. The rule: if a surface is going to be an "object" (a button, a tile, an icon), it gets a gradient. If it's chrome (borders, dividers, text), it stays solid.

## 3. Typography Rules

### Font Family
- **Primary (Website)**: `Founders Grotesk`, with fallback: `"Helvetica Neue", Arial, sans-serif`. Klim Type Foundry's signature grotesk — geometric but warm, with distinctive round terminals.
- **Mono (Website)**: `JetBrains Mono`, uppercase, wide tracking — used for metadata and micro labels on the marketing site.
- **Body (Website)**: `Arial` — intentionally boring system fallback for smaller copy, reinforcing the "plain gallery" stance.
- **Apps**: Default to `SF Pro` / `-apple-system` on iOS, often paired with custom display type per app (each app in the family has its own typographic personality within shared rules).

*Note: For external implementations, `Inter` is a strong web-safe substitute for Founders Grotesk at weight 500-600. Keep JetBrains Mono as-is — it's free and open-source.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Founders Grotesk | 76px (4.75rem) | 700 | 1.00 | normal | Landing page hero — bold, grounded |
| Display Large | Founders Grotesk | 44px (2.75rem) | 600 | 1.20 | normal | Section anchors |
| Display Medium | Founders Grotesk | 44px (2.75rem) | 400 | 1.20 | normal | Lighter section intros |
| Heading | Founders Grotesk | 36px (2.25rem) | 600 | 1.00 | normal | Feature cards, app titles |
| Sub-heading | Founders Grotesk | 24px (1.50rem) | 400 | 1.43 | normal | Secondary titles, descriptions |
| Body Large | Founders Grotesk | 22px (1.38rem) | 600 | 0.91 | normal | Button labels, emphasized copy |
| Body Small | Founders Grotesk | 18px (1.13rem) | 400 | 1.11 | 0.5px | Meta labels, small headings |
| Body | Arial | 14px (0.88rem) | 400 | 1.43 | normal | Standard body, captions |
| Micro Caps | JetBrains Mono | 12px (0.75rem) | 700 | 1.67 | normal | Micro labels, UPPERCASE |
| Micro Link | Arial | 12px (0.75rem) | 300 | 1.67 | 0.5px | Footer links, UPPERCASE |
| Display Link | Arial | 36px (2.25rem) | 400 | 1.00 | normal | Oversized nav/footer links |

### Principles
- **Two-font contrast**: Founders Grotesk for presence, Arial for plainness. The combination is deliberate — when everything else in the design system is maxed out (dimensional apps, saturated gradients), the type stays quiet.
- **Uppercase mono for chrome**: JetBrains Mono at 12px uppercase marks UI chrome, section labels, and technical metadata. It carries the "made by real humans who care" signal.
- **Weight 600 as default headline**: Unlike Stripe/Cape (which run weight 300), Not Boring's marketing uses confident weight 600-700. The apps are playful enough; the site doesn't need to be.
- **Tight display line-height (1.00)**: Headlines sit tight and grounded — aligned with the hard-rectangle structure of the Webflow scaffold.
- **Progressive fallback**: Headings use Founders Grotesk; body often drops to Arial. This is not lazy — it's a stated preference for system defaults in "boring" contexts, reinforcing the brand thesis.

## 4. Component Stylings

### Buttons

**Primary Black (Marketing)**
- Background: `#000000`
- Text: `#ffffff`
- Padding: `12px 30px 15px` (asymmetric, slightly bottom-heavy)
- Radius: `4px`
- Font: Founders Grotesk 22px weight 600
- Hover: background shifts to `#ffe600` (Andy Yellow), text stays black
- Use: Primary CTA on marketing site ("Download", "Get the App")

**Outlined Black (Marketing)**
- Background: `#ffffff`
- Text: `#000000`
- Border: `2px solid #000000`
- Padding: `12px 30px 15px`
- Radius: `4px`
- Font: Founders Grotesk 22px weight 600
- Hover: fills to Andy Yellow
- Use: Secondary action ("Learn More")

**Dimensional Pill (App UI) — The Signature**
- Background: linear-gradient(135deg, `#a039ff` 0%, `#4e3bff` 100%) *(or any brand gradient)*
- Text: `#ffffff`, weight 600
- Padding: `14px 28px`
- Radius: `16px` (generous) or full pill (`999px`)
- Shadow stack (this is the whole point):
  1. **Inset top highlight**: `inset 0 1px 0 rgba(255, 255, 255, 0.65)` — the thin bright line where light hits the top edge
  2. **Inset bottom shadow**: `inset 0 -2px 4px rgba(0, 0, 0, 0.18)` — the soft darkening at the bottom edge (the bevel's shadowed side)
  3. **Outer ambient**: `0 2px 4px rgba(17, 12, 46, 0.12)` — close, soft ambient lift
  4. **Outer drop**: `0 12px 24px -4px rgba(78, 59, 255, 0.45)` — deep, colored drop shadow matching the element's hue
- Active/pressed: compress vertically by 1-2px, reduce outer shadow offsets, slightly deepen inset bottom shadow — the button feels "pushed in"
- Use: Primary CTA inside any Not Boring app

### Tiles & Cards
- Background: `#ffffff` with linear gradient overlay (subtle warm-to-cool top-to-bottom), or brand gradient for "object" tiles
- Radius: `20px` (standard), `24px` (featured), `16px` (compact)
- Border: typically borderless — elevation comes from shadows, not outlines
- Shadow stack:
  1. **Ambient rim**: `inset 0 1px 0 rgba(255, 255, 255, 0.8)` — top-edge highlight
  2. **Drop soft**: `0 2px 6px rgba(17, 12, 46, 0.08)` — close ambient
  3. **Drop deep**: `0 18px 36px -12px rgba(17, 12, 46, 0.22)` — spreads out below
- Hover: drop shadows intensify slightly, tile lifts 2-3px via transform

### Icons — 3D Objects
Not Boring icons are never flat glyphs. Each is a small dimensional object:
- **Base**: filled gradient (135° direction), radius matching tile scale
- **Top highlight**: inset bright rim, 1-2px from top edge, `rgba(255, 255, 255, 0.7)`
- **Bottom shadow**: inset dark rim, 1-2px from bottom, `rgba(0, 0, 0, 0.15)`
- **Drop shadow**: colored (matches the icon's hue family) with ~35% alpha, 8-16px blur
- In Iconify terms: use `solar:*-bold` or `ph:*-fill` variants, then layer with CSS gradient backgrounds and the shadow stack above

### Inputs & Forms
- Border: `0px 0px 2px solid #000000` (underline only — minimal, editorial)
- Radius: `0px` (sharp)
- Focus: underline color shifts to `#3898ec` (electric blue), outline removed
- Text: `#000000`, Founders Grotesk 18-22px weight 400
- Placeholder: `#aaaaaa`
- Use: form fields on the marketing site; apps use custom dimensional input treatments per context

### Navigation
- Sticky horizontal nav, Arial 12px uppercase (`0.5px` tracking)
- Logo left (the "Andy Doodle" 3D character mark)
- Links: `#333333`, no underline
- CTA right-aligned: black pill with white text
- Mobile: hamburger with 4px radius

### Decorative Elements
- **3D object illustrations**: Not Boring's signature — rendered 3D toys (cubes, spheres, pills, marbles) that appear in heroes and empty states. Always multi-color, always with ray-traced-feeling highlights.
- **Gradient ribbons**: long horizontal gradient strips used as accent dividers or progress fills
- **Confetti**: physically-simulated celebratory particles on completion states

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Observed scale: 5px, 6px, 8px, 9px, 10px, 12px, 15px, 16px, 20px, 24px, 30px, 40px, 100px
- Notable: The marketing site uses `100px` generously for section padding — a lot of air. The apps themselves are denser, using 12-20px for most tile internals, respecting thumb-reach zones.

### Grid & Container
- Marketing max-width: ~1000px (tight, editorial)
- Hero: centered single column with a 3D illustration as focal point
- Feature grid: 2-3 columns on desktop, single-column stack on mobile
- Apps: full-device canvas, no fixed max-width — everything respects iOS safe areas

### Whitespace Philosophy
- **Generous around objects**: Dimensional 3D elements need room to breathe — shadows extend beyond element bounds and require uncluttered surroundings to read correctly.
- **Dense inside objects**: A Not Boring tile might have 6 pieces of information, but each sits on its own micro-surface (a pill, a chip, a segment). Information is layered into the object, not laid out around it.
- **Asymmetric button padding**: `12px 30px 15px` (top-right-bottom-left is not default) — bottom padding is slightly greater than top to account for the optical center of the bevel's highlight/shadow pair.

### Border Radius Scale
- Sharp (2-4px): marketing buttons, inputs, dividers — deliberately plain
- Comfortable (8-12px): small app chrome
- Generous (16-20px): standard app tiles, secondary buttons, cards
- Hero (24-32px): featured tiles, modals, wallet-card-style elements
- Pill (999px): primary CTAs, toggle segments, control pills — full-round for any element that reads as a "key" or "button" object

## 6. Depth & Elevation — The Dimensional System

This is the heart of Not Boring. Where most design systems have 3-4 elevation levels each defined by a single drop shadow, Not Boring's elevation is built from **paired layers**: a highlight layer on top and a shadow layer below, with additional colored glow when the element is a vivid-gradient "object."

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
|-------|------------|-----|
| Flat (0) | No shadow | Background text, inline copy |
| Stamped (1) | Inset highlight only: `inset 0 1px 0 rgba(255,255,255,0.5)` | Subtle 3D-ness on chips and badges |
| Tile (2) | Inset highlight + soft drop: `inset 0 1px 0 rgba(255,255,255,0.8), 0 4px 12px rgba(17,12,46,0.10)` | Standard tiles on app canvas |
| Card (3) | Full paired stack: top inset + bottom inset + ambient drop + deep drop | Featured cards, modal contents |
| Pill (4) | Full stack + colored glow matching element hue | Primary CTAs, hero buttons |
| Overlay (5) | Pill stack + larger spread + darker ambient | Modals, floating panels, overlays |
| Pressed | Compressed: reduced outer shadows, deeper inset bottom | Active/touch state — feels physically depressed |

### The Shadow Philosophy

Not Boring's shadows are not just *elevation* — they're *illumination*. The system assumes a single soft light source from the top (roughly 10° off vertical), which governs every surface treatment:

1. **Top edges always brighter** (inset white highlight)
2. **Bottom edges always darker** (inset dark shadow)
3. **Drop shadow always below** the element (never sideways, never above)
4. **Colored glow matches the element's hue family** — a magenta button drops magenta light, a cyan button drops cyan light

Combined with the gradient fill (which itself implies a top-left highlight and bottom-right shadow), every interactive element reads as a small sculpted object sitting on a surface. This is the whole trick. Once you see it, you can't unsee it.

### Pressed States (Tactile Feedback)

When a button is tapped, three things happen simultaneously:
- Outer drop shadows reduce by ~50% (element sinks toward surface)
- Inset bottom shadow deepens by ~30% (compression effect)
- Element transforms `translateY(1px) scale(0.98)` — barely perceptible but crucial

This mimics the real physics of pressing a soft rubber button. Without it, Not Boring's buttons would just be static sculptures — with it, they feel *alive*.

## 7. Do's and Don'ts

### Do
- **Use gradient fills as the default** for any interactive "object" (buttons, tiles, icons) — not as a special accent
- **Layer your shadows**: at minimum, pair an inset top highlight with an outer drop shadow. For primary CTAs, add a colored glow
- **Tint your shadows**: use `rgba(17, 12, 46, …)` (indigo-tinted) rather than `rgba(0, 0, 0, …)` for ambient lift — it ties shadows to the palette
- **Match colored glows to the element's hue** — a magenta button has a magenta glow, a lime button has a lime glow
- **Use generous border-radius (16-24px)** on tiles and secondary buttons; full pills (`999px`) on primary CTAs
- **Use Founders Grotesk 600-700** for marketing headlines — this is a confident brand, not a whisper
- **Respect the pressed state**: compress the element on tap, don't just change its color
- **Pair saturated colors** — magenta with violet, cyan with periwinkle, lime with teal. Single-hue designs feel under-built here.
- **Use bevels, highlights, and gradients proudly** — they're the whole point
- **Treat icons as 3D objects** — gradient fills, inset highlights, colored drop shadows

### Don't
- **Don't go flat.** A single-color button with no inset highlight betrays the entire brand thesis. If you catch yourself writing `background: #4e3bff; border-radius: 8px;` with nothing else, stop.
- **Don't use neutral gray drop shadows** — always tint with the brand's indigo (`rgba(17, 12, 46, …)`) or a color matching the element's hue
- **Don't use sharp 0-2px radius** on app tiles or CTAs — that's Cape's language, not Not Boring's. Save sharp corners for the marketing site's plain chrome.
- **Don't mute the palette** — Not Boring's colors are maxed-out on purpose. Desaturating them kills the toy-like quality.
- **Don't use solid fills on primary CTAs** — the dimensional gradient with paired highlight/shadow is non-negotiable
- **Don't skip the pressed state** — a Not Boring button that doesn't physically react to touch feels broken
- **Don't use web-safe stock iconography** (Font Awesome outlines, thin-line glyphs) — if you must use a web icon set, pick `solar:*-bold` or `ph:*-fill` and layer dimensional treatments on top
- **Don't be tasteful to the point of being quiet** — Not Boring's whole thesis is that polite flatness is the enemy of good software. Lean in.

## 8. Responsive Behavior

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

## 9. Agent Prompt Guide

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
