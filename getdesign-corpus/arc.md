# Design System Inspired by Arc Browser

## 1. Visual Theme & Atmosphere

Arc's website is not a browser's landing page — it's a manifesto printed on paper-warm cream, torn open by a bright electric blue, and lit from behind by a soft gradient mesh that hums quietly while you read. The background is an unmistakable off-white (`#fffcec`) — not clinical white, not iOS gray, but a faintly butter-tinted parchment that immediately separates Arc from every Chromium clone on earth. Over this warm canvas, the brand lays a saturated ultramarine (`#3139fb`) that refuses to behave like a corporate accent: it fills entire sections, gets used as a full-bleed background, carries the wordmark, and frames product screenshots like a movie poster. Where Stripe whispers and Linear chisels, Arc *commits to color* — and still feels grown-up about it.

The second defining gesture is the **gradient mesh** — the muted cloud that sits behind every hero. Desaturated peach, mint, butter, and pale violet blur into each other at 40–60% of a full pastel's saturation, creating an atmospheric halo that looks like sunrise diffused through frosted glass rather than a crayon box. It's the visual signature that ties Arc to the Browser Company's broader universe. Over the mesh, the UI sits on **frosted glass panels** — translucent sidebars, blurred command bars, peek windows that dim the page behind them — giving the product a physicality competitors don't attempt. This is software that believes in materials.

What makes Arc feel *different* from every other browser site is the collision of opposites held in one system: the cream paper warmth against the digital electric blue, the hushed mesh atmosphere against the hard geometric buttons, the occasional muted coral against the rigorous Marlin Soft SQ typography. Arc is crafted playfulness held in check — a design tool that still chooses serious over Saturday-morning. Every element is dimensional: buttons cast soft shadows, glass panels layer over colored grounds, and the whole composition reads as built rather than arranged.

**Key Characteristics:**
- Cream off-white canvas (`#fffcec`) — paper-warm, never sterile
- Electric Arc Blue (`#3139fb`) as full-bleed hero color, not just an accent stamp
- **Restrained mesh gradients** (muted peach + mint + butter + violet) as atmospheric halos — 40–60% less saturated than a pure pastel
- **Frosted glass** sidebars, peek panels, command bars — `backdrop-filter: blur()` with translucent fills
- Marlin Soft SQ for display type, Marlin for UI, InterVariable for body — a three-font wardrobe
- Generous rounded corners (10px–22px) — playful but never infantile
- Soft black shadows (`rgba(0,0,0,0.1) 0px 5px 5px 0px`) — diffused, never harsh
- A quiet accent tier (muted coral, soft sky, pale olive) used sparingly — the rainbow is implied, not literal

## 2. Color Palette & Roles

### Primary
- **Arc Blue** (`#3139fb`): The signature. Full-bleed hero backgrounds, wordmark, primary CTAs, pin indicators. This is the most-used color on the page after cream and it is deployed fearlessly at scale.
- **Deep Arc Blue** (`#2702c2`): Solid button fills on cream surfaces, link text on light backgrounds, the darker twin of Arc Blue for contrast-critical moments.
- **Paper Cream** (`#fffcec`): The canvas. Warm off-white that sits between `#fff` and a true butter — the entire site breathes on this color.
- **Paper Cream Warm** (`#fffadd`): A slightly more saturated cream for stacked sections and inset cards. The second note in the paper chord.

### Brand Deep
- **Brand Dark Blue** (`#000354`): The near-black brand navy. Used for dark sections, headers on cream, maximum-contrast text.
- **Pure Black** (`#000000`): Body text, headings on cream. Arc doesn't dilute its black — it wants the contrast against paper.
- **High Contrast Ink** (`rgba(0, 0, 0, 0.65)`): Secondary text on cream when full black is too heavy.

### Gradient Mesh (the atmosphere, restrained)
These are the active mesh blooms — each is roughly half the saturation of a pure pastel. The goal is atmosphere, not a painting.
- **Mesh Peach** (`#f5e4d8`): Upper-left bloom — dusty, warm, barely coral.
- **Mesh Butter** (`#f6ecd2`): Central warm diffusion — muted sunrise note, almost parchment.
- **Mesh Mint** (`#dce8df`): Lower cool bloom — closer to sage than candy mint.
- **Mesh Violet** (`#e3dcf2`): Upper-right pale lavender, balancing the warms without pushing violet.
- **Two-stop mesh accent** (`violet → peach → butter`): A linear or two-stop gradient used on the Little Arc pill, dark-tile avatar chips, and any place that used to carry the conic rainbow. Three hues blending, never the full spectrum.

### Accents (used sparingly — one per surface, not all at once)
- **Muted Coral** (`#d86a73`): Pulled back from the original bright pink. Badges, notification dots, the occasional pin.
- **Arc Salmon** (`#e8c8b8`): Muted peach companion for cards and mid-tone accents.
- **Pale Olive** (`#cfd8a8`): Soft highlighter green, success-adjacent without being a traffic signal.
- **Pale Periwinkle** (`#c8cadc`): Low-emphasis chips and muted surfaces.
- **Brand Red** (`#d64050`): Alerts only. Used almost never.

> Deliberately retired from active use: the full rainbow conic gradient. It now lives only as a historical marker — real Arc surfaces either carry Arc Blue or a 2–3 color mesh blend.

### Secondary (Teals)
- **Teal 1** (`#00eae7`): Vivid aqua, used for highlight rings and electric decorative moments.
- **Teal 3** (`#00a39f`): Mid-teal for icons and illustrations.
- **Teal 7** (`#003828`): Deep forest teal for dark sections and ink on cream.

### Interactive
- **Focus Outline** (`#96c4ff`): System focus ring — soft sky blue, never a sharp black outline.
- **Arc Blue Hover** (`rgba(23, 3, 148, 0.5)`): Translucent deep blue for hover overlays over cream and gradient surfaces.

### Glass & Surface
- **Glass White** (`rgba(255, 252, 236, 0.6)`): Frosted cream — the default glass fill for panels over gradients.
- **Glass Dark** (`rgba(0, 3, 84, 0.35)`): Frosted brand-navy for glass panels over light imagery.
- **Border Soft** (`rgba(0, 0, 0, 0.08)`): Hairline dividers, barely visible.
- **Border Tinted** (`rgba(49, 57, 251, 0.2)`): Arc-blue-tinted borders on interactive cards.

## 3. Typography Rules

### Font Family
- **Display**: `Marlin Soft SQ` / `Marlin` — the signature display and heading family. Geometric, soft-squared, architectural. Fallback: `-apple-system, system-ui, Segoe UI, Roboto`.
- **Body/UI**: `InterVariable` / `Inter` — the workhorse for nav, UI, links, body copy at 17px and below.
- **Accent Serif**: `ABC Oracle` — a bookish serif used for editorial moments and link styling. Fallback: `Helvetica` (not a true serif fallback — ABC Oracle is loaded or it reads as neutral Helvetica).
- **Display Variable**: `Exposure VAR` — variable display used at mid-sizes (36px) for expressive moments. Fallback: `Helvetica`.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero Display | Marlin Soft SQ | 45.5px (2.84rem) | 700 | 0.93 | -1.82px | Super-tight leading, near-overlap |
| Display Large | Marlin Soft SQ | 40px | 700 | 0.97 | -1.6px | Section intros |
| Display Mid | Exposure VAR | 36px | 700 | 1.00 | -0.72px | Expressive variable headings |
| Heading | Marlin | 32px | 700 | 0.97 | -1.6px | Feature blocks |
| Editorial Large | ABC Oracle | 24px | 400 | 1.20 | normal | Serif pull quotes, link moments |
| Editorial | ABC Oracle | 20px | 400 | 1.20 | normal | Sub-headings with a literary tone |
| UI Heading | InterVariable | 17px | 500 | 1.50 | normal | Card titles, nav |
| Link Strong | InterVariable | 17px | 700 | 1.50 | normal | Emphasized inline links |
| Body | Marlin | 16px | 400 | — | normal | General UI copy |
| Nav Link | Marlin Soft SQ | 16px | 700 | — | normal | Primary nav items |
| Meta | Marlin Soft SQ | 14px | 500 | — | -0.28px | Caption/label copy |
| Caption | Marlin Soft SQ | 14px | 500 | — | -0.28px | Secondary labels |
| Button | -apple-system | 14px | 600 | 2.07 | -0.14px | System-font buttons for native feel |
| Micro Link | InterVariable | 12px | 600 | — | 0.4px | Uppercase tracking for chrome labels |

### Principles
- **Marlin Soft SQ is the voice**: The soft-squared geometric sans is Arc's typographic fingerprint. Rounded counters, squared terminals, slight warmth. Used at 700 for all display and at 500/700 for mid-sizes.
- **Ultra-tight display leading (0.93–0.97)**: Display text nearly overlaps vertically — compressed, intentional, almost architectural.
- **Negative letter-spacing scales with size**: -1.82px at 45px, -1.6px at 40px, -0.72px at 36px, -0.28px at 14px. Larger = tighter.
- **ABC Oracle as the editorial comma**: A warm serif breaks up sans-serif monotony for quotes and poetic lines. Used sparingly; never for UI.
- **InterVariable for the small stuff**: Anything below 18px that needs neutral legibility — links, nav, captions — sits on Inter.
- **Three families, no more**: Display (Marlin), Body (Inter), Editorial accent (Oracle). A tight wardrobe.

## 4. Component Stylings

### Buttons

**Primary Solid (on cream)**
- Background: `#2702c2` (deep Arc blue)
- Text: `#ffffff`
- Padding: 8px 20px (height ~36px)
- Radius: **10px**
- Shadow: `rgba(0, 0, 0, 0.1) 0px 5px 5px 0px`
- Font: 14px system-ui weight 600, letter-spacing -0.14px
- Use: "Download for Mac", "Try Dia"

**Primary Inverse (on blue)**
- Background: `#ffffff`
- Text: `#2702c2`
- Padding: 8px 20px
- Radius: 10px
- Shadow: `rgba(0, 0, 0, 0.1) 0px 5px 5px 0px`
- Use: CTAs sitting on the full-bleed Arc Blue hero

**Glass Button (on gradient mesh)**
- Background: `rgba(255, 252, 236, 0.6)`
- `backdrop-filter: blur(16px) saturate(1.4)`
- Border: `1px solid rgba(255, 255, 255, 0.5)`
- Text: `#000354`
- Radius: 22px (pill-adjacent)
- Use: Hero CTAs that sit over the gradient halo

**Mesh Blend CTA (special)**
- Background: linear gradient `violet (#e3dcf2) → peach (#f5e4d8) → butter (#f6ecd2)` at ~115deg
- Text: `#000354` (brand dark) — sits dark on the pale mesh for readability
- Border: `1px solid rgba(255, 255, 255, 0.5)` for a glassy rim
- Radius: 22px
- Use: Little Arc pill, launch moments, celebratory CTAs. Replaces the old conic rainbow — still playful, now grown-up.

### Cards & Containers
- Background: `#ffffff` on cream, or `rgba(255, 252, 236, 0.7)` glass on gradient
- Border: `1px solid rgba(0, 0, 0, 0.06)` (hairline) or `2px solid #3139fb` (active/featured)
- Radius: **8px** (standard), **10px** (comfortable), **22px** (hero/featured)
- Shadow: `rgba(0, 0, 0, 0.1) 0px 5px 5px 0px` — the signature soft drop
- Hover: shadow deepens to `rgba(0, 0, 0, 0.25) 0px 2px 8px 0px`

### Glass Panels (Sidebar, Peek, Command Bar)
- Background: `rgba(255, 252, 236, 0.55)` (cream glass) or `rgba(0, 3, 84, 0.35)` (dark glass)
- `backdrop-filter: blur(20px) saturate(1.8)`
- Border: `1px solid rgba(255, 255, 255, 0.4)` (inner highlight on top edge)
- Radius: 12px (nested) to 22px (floating)
- Shadow: `rgba(0, 0, 0, 0.12) 0px 12px 40px -12px`
- Inner glow: `inset 0 1px 0 rgba(255, 255, 255, 0.6)` for the glassy top-edge shine

### Pins, Tabs, and Little Arc
- Tab pills: 8px radius, 2px Arc blue border when active
- Pin squares: 8px radius, muted accent backgrounds (coral, pale olive, periwinkle, salmon) — one color per pin, never a rainbow row
- Little Arc: a 22px-radius floating glass chip with a 2–3 color mesh blend (violet → peach → butter). The most Arc-flavored detail in the product, now restrained enough to feel professional.

### Inputs & Forms
- Border: `1px solid rgba(0, 0, 0, 0.12)`
- Radius: 10px
- Focus: `1px solid #3139fb`, outer ring `0 0 0 3px rgba(150, 196, 255, 0.35)` (focus-outline color)
- Placeholder: `#696969`
- Background: `#ffffff` or glass

### Badges
- **Neutral**: `#fffadd` background, `#000354` text, 8px radius, 2px 10px padding
- **Pink Pop**: `#f25e6b` background, `#ffffff` text, 8px radius — student campaign energy
- **Glass Dot**: 6px colored circle inside a glass panel for sidebar pin indicators

### Navigation
- Sticky cream background with subtle `backdrop-filter: blur(12px)`
- Marlin Soft SQ 16px weight 700 for nav links, `#000000` text
- Rounded nav container, 10px radius on wrapping bar
- Right-aligned blue CTA button

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Scale (most-used): 3px, 4px, **8px**, 16px, **24px**, 32px, 48px, 72px, 80px, 128px, 160px
- Notable: 24px appears 34 times in the data — it's the workhorse rhythm unit. 8px is the micro-tick. Both are core.

### Grid & Container
- Max content width: ~1080–1200px, centered
- Hero: centered single column, headline + subhead + CTAs, product screenshot below
- Full-bleed Arc Blue sections alternate with cream sections — **a cream/blue cadence** that defines the page rhythm
- Product screenshots sit on the cream with gradient-mesh haloes glowing behind them
- Sidebar mocks (of the browser itself) anchor the middle of the page as hero art

### Whitespace Philosophy
- **Generous around product, tight around type**: Arc gives its browser screenshots cathedral-like space to breathe, then compresses its headline typography into dense, architectural blocks. The contrast is the point.
- **Section as set-piece**: Each scroll section is a distinct environment — cream, blue, cream, dark navy. Not a gradient of one background, but four separate rooms in a house.
- **Color as spacing**: A switch from cream to Arc Blue does more work than 120px of whitespace. Background shifts *are* the rhythm.

### Border Radius Scale
- **4px**: Smallest interactive (tight badges, inline chips)
- **8px**: Standard — tabs, cards, inputs, pins
- **10px**: Comfortable — buttons, primary interactive
- **12px**: Panels, nested glass surfaces
- **22px**: Hero pills, Little Arc, featured glass chips
- **Generous but disciplined**: Arc never goes full-pill for rectangles (no 999px radius on buttons), but 22px gets close for special moments.

## 6. Depth & Elevation — The Glass Layer

Arc's depth system is not built on shadow alone. It's built on the **interaction of glass, gradient, and soft drop shadow** — three physical layers that together create dimensionality.

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (0) | No shadow | Page text, inline elements |
| Ambient (1) | `rgba(0, 0, 0, 0.08) 0px 2px 8px` | Hover hints, subtle lift |
| Standard (2) | `rgba(0, 0, 0, 0.1) 0px 5px 5px 0px` | Buttons, cards — the signature soft drop |
| Floating (3) | `rgba(0, 0, 0, 0.12) 0px 12px 40px -12px` | Glass panels, peek windows, command bar |
| Deep (4) | `rgba(0, 0, 0, 0.25) 0px 24px 60px -20px` | Modals over gradient mesh |
| Ring (focus) | `0 0 0 3px rgba(150, 196, 255, 0.35)` | Keyboard focus — soft sky halo |

### The Glass Recipe
Arc's frosted-glass panels follow a five-step stack:

1. **Colored ground**: Arc Blue, gradient mesh, or dark navy — something to blur.
2. **Translucent fill**: `rgba(255, 252, 236, 0.55)` or `rgba(0, 3, 84, 0.35)`.
3. **Backdrop filter**: `backdrop-filter: blur(20px) saturate(1.8)` — the saturation bump keeps colors vibrant through the frost.
4. **Inner top-edge highlight**: `box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.6)` — simulates light catching the glass rim.
5. **Outer soft drop**: `0 12px 40px -12px rgba(0, 0, 0, 0.12)` — the glass is floating above the ground.

Without saturation boost, glass looks dead. Without the inner highlight, glass looks like translucent plastic. Arc always does both.

### Gradient Mesh Halo
Behind hero content, Arc layers overlapping soft radial gradients:
```
background:
  radial-gradient(40% 60% at 20% 30%, #ffd7c2 0%, transparent 60%),
  radial-gradient(40% 60% at 80% 20%, #d9c8ff 0%, transparent 60%),
  radial-gradient(50% 50% at 70% 80%, #c7f0d8 0%, transparent 60%),
  radial-gradient(40% 40% at 30% 80%, #fff4c0 0%, transparent 60%),
  #fffcec;
```
Four soft blooms over a cream base. The gradient is never animated on-scroll — it's a still atmosphere, not a light show.

## 7. Do's and Don'ts

### Do
- Use **restrained gradient meshes** behind hero moments — Arc's brand is atmospheric, not flat, but also not a paint swatch
- **Layer glass carefully**: colored ground + translucent fill + backdrop-blur + inner highlight + soft drop. All five, every time.
- Use `#3139fb` Arc Blue at full-bleed scale — as a section background, not just as a button
- Pair cream (`#fffcec`) with black text — the warmth is the brand, don't dilute it
- Use Marlin Soft SQ at weight 700 with tight negative letter-spacing (-1.6px+) for display
- Reach for a **2–3 color mesh blend** (not a full rainbow) on celebratory moments — Little Arc, launches, the dark-tile avatar
- Use 8px–22px radii — playful but architectural
- Let the gradient mesh breathe with `backdrop-filter: blur()` on any overlaid panel

### Don't
- **Don't use the full conic rainbow anymore** — it read as childish. Pick 2–3 adjacent mesh hues and blend them linearly instead.
- **Don't use solid single-color fills for hero moments** — Arc's heroes always have a gradient mesh or Arc Blue background, never a flat white
- Don't let the mesh hit full-pastel saturation — keep it 40–60% off the pure tone, or the page starts to feel like a kids app
- Don't flatten the glass — skip `backdrop-filter` and the panels look like PowerPoint rectangles
- Don't use cool gray (`#f3f4f6`) for surfaces — the base is cream (`#fffcec`), warmth matters
- Don't use pill-shaped buttons (999px radius) for rectangles — Arc stays in the 8–22px range
- Don't use harsh dark shadows like Stripe's `rgba(50,50,93,0.25)` — Arc's drops are soft and black-based
- Don't use serif-only heroes — Marlin Soft SQ is the display voice; ABC Oracle is a guest
- Don't drop the OpenType/stylistic alternates — Marlin's personality lives in its geometry
- Don't forget the **saturation boost** on glass: `saturate(1.8)` keeps the gradient vibrant through frost

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Hero headline 32px, single column, mesh gradient simplifies to 2 blooms |
| Tablet | 640–1024px | 2-column grids, glass panels shrink, gradient stays atmospheric |
| Desktop | 1024–1280px | Full layout, 3-column feature grids, full mesh |
| XL | >1280px | Centered content, broader cream/blue margins |

### Touch Targets
- Buttons: 36px+ tall via 8px–10px vertical padding
- Nav links generously spaced with 24px gutters
- Glass chips and pins are 22px+ hit areas

### Collapsing Strategy
- Hero: 45.5px Marlin Soft SQ → 32px on mobile, weight 700 maintained, letter-spacing softens to -0.96px
- Full-bleed Arc Blue sections stay full-bleed on all sizes — the color IS the hierarchy
- Gradient mesh: 5 blooms on desktop → 2–3 blooms on mobile to keep performance
- Glass panels: `backdrop-filter` reduces blur radius on mobile (20px → 12px) for GPU budget
- Product screenshots: horizontal scroll on mobile when UI detail is critical

### Image Behavior
- Product screenshots maintain soft drop shadow at all sizes
- Rainbow conic and mesh elements scale proportionally, never tile
- Little Arc illustration: 22px radius, sits at consistent scale across breakpoints

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Deep Arc Blue (`#2702c2`) on cream, or White on Arc Blue
- Hero background: Arc Blue (`#3139fb`) full-bleed, or cream + gradient mesh
- Background: Paper Cream (`#fffcec`)
- Heading: Pure Black (`#000000`) on cream, White on blue
- Body: Pure Black (`#000000`) or `rgba(0, 0, 0, 0.65)`
- Brand Dark: `#000354`
- Link: `#2702c2` (deep Arc blue) on cream
- Focus ring: `#96c4ff` (soft sky)
- Accent pop: Arc Pinkish (`#f25e6b`)
- Success-adjacent: Light Green (`#d3e081`)
- Mesh blooms (restrained, ~50% saturation): Peach (`#f5e4d8`), Butter (`#f6ecd2`), Mint (`#dce8df`), Violet (`#e3dcf2`)
- Mesh blend (replaces rainbow conic): linear `#e3dcf2 → #f5e4d8 → #f6ecd2` at ~115deg
- Muted coral accent: `#d86a73` (use sparingly, never as a primary CTA)

### Example Component Prompts
- "Create an Arc hero: cream background (`#fffcec`). Behind the headline, layer four restrained radial gradients — peach (`#f5e4d8`) at 18% 28%, violet (`#e3dcf2`) at 82% 18%, mint (`#dce8df`) at 75% 85%, butter (`#f6ecd2`) at 25% 82%, all fading to transparent. Apply `filter: saturate(0.85)` on the mesh layer. Headline in Marlin Soft SQ 45.5px weight 700, line-height 0.93, letter-spacing -1.82px, color `#000000`. Primary CTA: deep Arc Blue `#2702c2`, white text, 10px radius."
- "Design a glass sidebar panel: translucent cream fill `rgba(255, 252, 236, 0.55)`, `backdrop-filter: blur(20px) saturate(1.8)`, inner top highlight `inset 0 1px 0 rgba(255,255,255,0.6)`, outer drop `0 12px 40px -12px rgba(0,0,0,0.12)`, radius 12px. Sits over an Arc Blue or gradient mesh ground."
- "Full-bleed Arc section: `#3139fb` background, white Marlin Soft SQ 40px weight 700 headline, letter-spacing -1.6px. White pill CTA button (`#fff` bg, `#2702c2` text, 10px radius) inverse-style."
- "Mesh blend CTA (replaces rainbow): `linear-gradient(115deg, #e3dcf2, #f5e4d8 55%, #f6ecd2)`, 22px radius, brand-dark text (`#000354`), 1px white-50 border. Used for Little Arc and launch moments only."
- "Product screenshot treatment: sit the image on cream with a soft mesh halo behind it. 12px radius on the image, drop shadow `rgba(0,0,0,0.1) 0px 5px 5px 0px` plus a secondary ambient `rgba(0,0,0,0.06) 0px 24px 60px -24px`."

### Iteration Guide
1. **Always start with cream** (`#fffcec`) as the base — white is wrong, gray is wrong, only paper is right.
2. **Heroes need atmosphere** — either a full-bleed Arc Blue or a gradient mesh. Never flat white.
3. **Glass needs all five layers**: ground + fill + blur + saturate + inner highlight + outer drop. Skip any one and it dies.
4. **Marlin Soft SQ 700 with -1.6px+ tracking** is the display voice. Don't go lighter for hero type.
5. **Radius stays 8–22px** — no pills for rectangles, no sharp corners for interactive.
6. **Shadows are soft and black-based** (`rgba(0,0,0,0.1)` + 5px blur). Arc doesn't use blue-tinted shadows — the color happens in the ground, not the shadow.
7. **Section cadence: cream → Arc Blue → cream → navy** — alternate rooms rather than gradient transitions.
8. **Muted accents** (coral, pale olive, periwinkle, salmon) are the secondary layer — use them for tabs, pins, badges, never for primary CTAs. One color per surface, never a full rainbow row.
9. **The mesh is a mood, not a graphic.** If it looks like a paint swatch or a kids app, pull the saturation down another 20% — atmosphere should be felt, not announced.
