---
version: alpha
name: "Leonardo AI"
description: "Token-first design system reference for Leonardo AI."

colors:
  background: "#ffffff"
  surface: "#ff3386"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#6e60ee"
  primary: "#ffffff"
  on-primary: "#ffffff"
  border: "#ff5d4b"
  focus-ring: "#ffffff"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 222px
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 155px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 69px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 28px
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

# Leonardo AI Design System

## Overview

Leonardo AI's visual identity is loud, structural, and unapologetically poster-like — the opposite of the dark-glass aesthetic most generative-AI brands chase. The page is built on a clean white canvas (`#ffffff`) interrupted by enormous black blocks, and the entire composition is anchored by a custom display typeface (`leoSans`) that runs at weight 900 in uppercase at sizes up to **222px**. Where competitors signal "AI" with iridescent gradients and dark cosmic UI, Leonardo signals it with magazine-cover typography. The screen reads like a Helvetica-Black movie poster scaled to fill a browser.

The color story is binary at first glance — pure black on pure white — but a wider chromatic system sits underneath, exposed through CSS variables: hotpink (`#ff3386`), orange (`#ff5d4b`), purple (`#6e60ee`), blue (`#33d0ff`), yellow (`#ffc533`), green (`#03e65b`), and two pinks (`#d25fff`, `#d591d5`). These aren't decorative gradients — they're hard, saturated solids reserved for accent moments. Purple `#6e60ee` is the most-used (count: 120 in the home extraction), surfacing on primary CTAs; the others appear as category tags, subject labels, and rotating hero color swaps. The system feels less like a gradient-driven AI brand and more like a graphic-design studio that happens to ship AI tooling.

What defines Leonardo most is the **fully-pill button at huge proportions**. Every interactive element — primary CTA, navigation arrow, category tab, video control — uses a border radius of `3.35544e+07px` (effectively infinite, rendered as a perfect pill). The padding is generous: `18px 67.5px` for hero CTAs. Combined with the screaming-uppercase headlines and the white-on-black/black-on-white panel inversions, the system telegraphs confidence through scale and rhythm rather than chrome or texture. There are no soft drop shadows in the resting state — buttons sit flat on their surface. Depth, when it appears, comes from layered black panels and full-bleed motion video, not from elevation.

**Key Characteristics:**
- `leoSans` weight 900 uppercase at 222px / 130px / 100px — display type IS the hero
- Tight line-height of `0.80` on all big display sizes — headlines stack like brick walls
- Negative letter-spacing scaling from `-4.44px` at 222px down to `-0.86px` at 86px
- Fully-pill buttons (radius `3.35544e+07px`) at every size — the signature shape
- White canvas (`#ffffff`) is the primary surface; pure black (`#000000`) for inverted panels
- Purple `#6e60ee` as the primary chromatic accent on key CTAs
- Multicolor secondary palette (hotpink, orange, blue, yellow, green, pink2) for tags and category color swaps
- `canvaSans` as the body/UI workhorse — quieter sans-serif at 14–18px for everything that isn't a poster
- Card radius locks at `11.25px` and `19.25px` — soft but never round
- Video-driven hero sections with previous/next directional arrow buttons (asymmetric pill-half radii)

## Colors

### Primary
- **Leo White** (`#ffffff`): The dominant page surface — light sections, card backgrounds, button fills on dark panels. Pure white, not warmed.
- **Leo Black** (`#000000`): Inverted panels, primary text on light, button fills, full-bleed dark sections. Pure black — Leonardo doesn't soften.
- **Hairline White** (`#ededed`): Subtle background tint and section divider — used sparingly to break up the white canvas without committing to gray.

### Brand Accent
- **Leo Purple** (`#6e60ee`): The signature CTA color and the only accent that earns a starring role on the homepage. Applied to primary buttons ("Start free trial", "Sign up"), in-text links on light surfaces (with underline), and select decorative moments.

### Multicolor Tag Palette
Leonardo exposes a full poster-color palette through CSS variables. These appear as category swatches, subject tags ("Action", "Anime", "Photo"), and accent moments — never as gradients. Each is a hard solid.
- **Hot Pink** (`#ff3386`): Energy / "fashion" / featured tag
- **Orange** (`#ff5d4b`): "Action" / heat / warm subject tag
- **Yellow** (`#ffc533`): Caution / highlight / playful tag
- **Green** (`#03e65b`): "New" / status / success tag (45 occurrences in home extraction — high frequency)
- **Blue** (`#33d0ff`): "Tech" / cool subject / link accent
- **Pink2** (`#d25fff`): "Anime" / dream / saturated alt-pink
- **Pink** (`#d591d5`): Soft pink — pastel companion to pink2

### Neutrals & Text
- **Body Black** (`#000000`): Primary text on white surfaces.
- **Body White** (`#ffffff`): Primary text on black panels.
- **Gray2** (`#999999`): Secondary text, disabled states, fine-print labels.
- **Soft White 60%** (`oklab(0.999994 0.0000455677 0.0000200868 / 0.6)`): Secondary link text on dark surfaces — readable but recessive.
- **Soft White 40%** (`oklab(0.999994 0.0000455678 0.0000200868 / 0.4)`): Tertiary link text on dark surfaces — disclaimer / fine print.
- **Soft White 30%** (`rgba(255, 255, 255, 0.3)`): Focus ring border on dark — inverted version of focus outline.

### Surface & Borders
- **White Surface** (`#ffffff`): Default light section background.
- **Black Surface** (`#000000`): Inverted section background — used for full-bleed panels.
- **Hairline Surface** (`#ededed`): Subtle alternating panel.
- **Border Soft White** (`rgba(255, 255, 255, 0.7)`): Outline borders on dark-surface ghost buttons (the directional arrow controls use `1px 1px 1px 0px` — three-sided to allow a paired-button seam).
- **Hairline Border Black** (`oklab / 0.1` → ~`rgba(0,0,0,0.1)`): Card and divider borders on light.

### Shadow & Glow
- **Hero Drop Shadow** (`rgba(0, 0, 0, 0.5) 0px 24px 80px 0px`): Heaviest shadow in the system — used on floating display imagery over the white canvas to create cinematic lift.
- **Mid Drop Shadow** (`rgba(0, 0, 0, 0.4) 0px 16px 48px 0px`): Mid-elevation card lift on hero imagery.
- **Standard Card Shadow** (`rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px`): Tailwind default `shadow-sm` baseline — used on light-surface chips and form controls.
- **Focus Outline** (`oklab(0.708 0 0 / 0.5) none 3px`): 3px gray outline ring on every interactive element — keyboard accessibility. Universal across buttons, links, tabs.

### Gradient System
Leonardo is **functionally gradient-free in chrome**. Buttons, cards, surfaces, and tags are all hard solid fills. The gradient energy lives entirely in the **video imagery** — Leonardo's hero loops cycle through full-color generated stills and motion clips, and those stills carry whatever radiance the AI outputs render. The interface itself stays poster-flat. If a CSS gradient is used, it's behind a video carousel as a fallback, never on UI chrome.

## Typography

### Font Family
- **Display**: `leoSans`, with fallback: `leoSans Fallback`, then system sans-serif. The headline workhorse — used at weights 800–900, almost always uppercase.
- **Body / UI**: `canvaSans`, with fallback: `canvaSans Fallback`, then system sans-serif. The quieter companion — used at weights 400–700 for body, links, buttons, captions.
- **Specialty**: `ufficioDisplay` makes a single appearance at 45.9px weight 500 uppercase — used for one-off editorial headers or section labels that need a softer tone than `leoSans`.

*Note: `leoSans` is a custom Leonardo typeface. For external implementations, Druk Wide, Söhne Breit, or Helvetica Black serve as close substitutes at display sizes. `canvaSans` is Canva's open typeface family — Inter or DM Sans work as web-safe alternatives for body text.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Display Mega | leoSans | 222px (13.88rem) | 900 | 0.85 | -4.44px | UPPERCASE | Maximum hero — "Make Anything" sized statements |
| Display XL | leoSans | 130px (8.13rem) | 900 | 0.90 | -1.3px | UPPERCASE | Section-killing hero |
| Display Large | leoSans | 100–115px (6.25–7.19rem) | 900 | 0.80 | normal | UPPERCASE | Standard feature-section heads |
| Display | leoSans | 79–90px (4.94–5.63rem) | 900 | 0.80 | normal | UPPERCASE | Sub-section headers |
| Heading XL | leoSans | 64–69px (4.00–4.31rem) | 900 | 0.80 | normal | UPPERCASE | Card and panel titles |
| Heading Large | leoSans | 45.9–52px (2.87–3.25rem) | 800–900 | 0.93–1.00 | -0.918px | UPPERCASE | Mid-section heads, card titles |
| Editorial | ufficioDisplay | 45.9px (2.87rem) | 500 | 0.93 | -0.918px | UPPERCASE | Editorial alternate to leoSans — one-off section labels |
| Sub-heading | leoSans | 30px (1.87rem) | 500 | 1.25 | normal | UPPERCASE | Smaller poster lines, eyebrow heads |
| Body Large | canvaSans | 26–28px (1.62–1.75rem) | 500 | 1.00–1.10 | 0.7px | normal | Hero subhead / lede paragraph |
| Body | canvaSans | 18–22px (1.13–1.37rem) | 400–500 | 1.20–1.33 | normal | normal | Standard reading text |
| Button | canvaSans | 18px (1.13rem) | 500–700 | 1.10–1.33 | normal | normal | Primary CTA labels |
| UI Default | canvaSans | 16px (1.00rem) | 400–700 | 1.25 | normal | normal | Nav, form fields, secondary UI |
| Caption | canvaSans | 14px (0.88rem) | 400–500 | 1.25 | normal | normal | Metadata, sub-labels, footer copy |
| Caption Small | canvaSans | 11.88–13.86px (0.74–0.87rem) | 400–500 | 1.25 | normal | normal | Fine print, micro-labels, breadcrumbs |

### Principles
- **Weight 900 + uppercase as the brand voice**: Every display-size headline is `leoSans` weight 900, ALL CAPS. This is non-negotiable at sizes 60px+. Lowercase or weight ≤700 reads as a different brand entirely.
- **Tight 0.80 line-height locks display blocks**: Headlines at 64–222px run at line-height `0.80` — extremely tight. Multi-line display copy stacks like brick masonry, with descenders almost touching the next line's caps. This is the signature density.
- **Negative tracking at scale**: Letter-spacing scales aggressively negative as type grows — `-4.44px` at 222px, `-1.3px` at 130px, `-0.918px` at 45.9px. Below 30px tracking returns to normal or slightly positive.
- **Two-typeface system**: `leoSans` for shouting (display, posters, big statements), `canvaSans` for talking (body, UI, captions). Never mix — `leoSans` at 16px reads as a button, `canvaSans` at 200px would never happen.
- **Sentence-case body, UPPERCASE display**: The contrast between caps headlines and mixed-case body creates a clear poster-vs-magazine rhythm. Buttons stay sentence-case (e.g., "Start free trial", not "START FREE TRIAL") — the buttons are part of the body voice, not the poster voice.
- **Weight 800 fallback for fluid responsive scales**: At 220px the system occasionally drops to weight 800 with line-height 0.90 and tracking `-4.39992px` — a slightly less aggressive cut for variable-width responsive contexts.

## Layout

### Spacing System
- Base unit: ~9px (with `6.75px` as the compact sub-unit — many counts derive from a 4.5/9/13.5/18/27 step)
- Scale: 1px, 2px, 2.25px, 6.75px, 9px, 13.5px, 18px, 22.5px, 27px, 36px, 45px, 54px, 72px, 90px, 180px
- Notable: The scale is **not a clean 8px grid** — it derives from a 4.5px (or 9px) base, producing values like 6.75 / 13.5 / 22.5 / 67.5. This non-standard rhythm is part of what makes Leonardo's spacing feel a touch "off" in a deliberate way — closer to a print-design grid than a typical web 8-system.
- Heaviest densities live at 6.75px (144 occurrences) and 18px (89 occurrences) — fine UI spacing and standard component padding respectively

### Grid & Container
- Max content width: ~1280px breakpoint cap; content frequently centers within ~1160px
- Hero: full-bleed video edge-to-edge, type overlaid
- Feature sections: alternate single-column statements with 2-column or 3-column grids of stadium cards
- Panel inversion: white sections alternate with full-black sections for chapter rhythm
- The page reads as **panel-stacked** more than gridded — each section is its own complete poster

### Whitespace Philosophy
- **Poster pacing**: Each major section gets a dedicated viewport — type fills the screen, panel ends, next panel begins. Not scroll-dense.
- **Type-anchored rhythm**: A 222px headline gets ~180px of vertical air; an 18px caption gets ~9–13.5px. The scale is proportional, not formulaic.
- **Black/white alternation**: Inverted sections create chapter breaks without dividers — Leonardo never uses a horizontal rule.
- **Image dominance in inverted panels**: Black sections lean on full-bleed video and generated imagery; white sections lean on type. The brand never mixes the two emphasis strategies in the same panel.

### Border Radius Scale
- `0px`: Almost never — only on full-bleed images and split arrow halves (one corner of the pair)
- `6px` / `9px`: Image and thumbnail rounding — minimal softening
- **`11.25px`**: The default card radius — used 72 times in the home extraction. The workhorse.
- `15.25px` / `19.25px`: Featured card / panel radius — slightly more emphasis
- `23.25px`: Hero card radius — generous but still architectural
- `60px`: Half-pill on directional arrow buttons (paired seam)
- `360px`: Bottom dome of stadium cards
- `999px` / `3.35544e+07px`: Full pill — every button, every tag, every chip
- **No mid-range gap below 23px**: The system jumps from 23px to fully-pill — there is no `40px` or `60px` standalone radius

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body type, structural panels |
| Hairline (Level 1) | `1px solid oklab/0.1` (light) or `1px solid rgba(255,255,255,0.3)` (dark) | Card edges, input outlines, divider seams |
| Soft Card (Level 2) | `rgba(0,0,0,0.1) 0px 1px 3px 0px, rgba(0,0,0,0.1) 0px 1px 2px` | Light-surface chips, form controls, small cards |
| Floating Imagery (Level 3) | `rgba(0,0,0,0.4) 0px 16px 48px 0px` | Hero generated-image cards floating over white |
| Hero Lift (Level 4) | `rgba(0,0,0,0.5) 0px 24px 80px 0px` | Largest cinematic imagery, primary feature panels |
| Focus Ring (Modal) | `oklab(0.708 0 0 / 0.5) none 3px` outline | Keyboard focus on every interactive element |

**Shadow Philosophy**: Leonardo's elevation system is binary in spirit — UI chrome (buttons, tags, cards) sits flat, while **imagery floats**. The shadow values that exist are all reserved for the AI-generated images themselves, not for the interface containers around them. A button never has a drop shadow at rest; a hero generation card always does. This separation reinforces the brand idea: **the chrome is just framing, the art is the product**. When chrome does need depth, it gets the Level 1 hairline border — never a shadow. The result is an interface that feels like a gallery wall: white space, framed art, no glow on the frames themselves.

### Decorative Depth
- Black/white panel inversion provides "depth through chapter" — you don't need shadows when alternating panels create cinematic structure on their own
- Video motion behind hero type creates a parallax sense of depth without any CSS transform
- The fully-pill button shape reads as recessive on white but assertive on black — the same component changes hierarchy by surface, not by elevation

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

**Primary Purple (Hero CTA)**
- Background: Leo Purple (`#6e60ee`)
- Text: Pure White (`#ffffff`) on dark panels, near-black (`oklch(0.145 0 0)` ≈ `#252525`) on light
- Padding: `18px 67.5px` (hero) or `18px 27px` (standard)
- Radius: `3.35544e+07px` (fully pill — infinite radius)
- Border: `0px solid` (no border)
- Shadow: `none` at rest
- Outline: `oklab(0.708 0 0 / 0.5) none 3px` (focus only)
- Font: 18px `canvaSans` weight 500, sentence-case
- Use: Primary marketing CTA — "Start free trial", "Sign up", "Get started"

**Primary White (Inverted CTA)**
- Background: Pure White (`#ffffff`)
- Text: Pure Black (`#000000`)
- Padding: `18px 27px` standard, `4.5px 13.5px` compact (chip variant)
- Radius: `3.35544e+07px` (fully pill)
- Shadow: `none`
- Font: 18px `canvaSans` weight 500
- Use: CTAs on black panels — "Try it free" on inverted hero sections

**Soft Tonal Button**
- Background: `oklab(0.8853 ... / 0.1)` — translucent near-white at 10% (frosted neutral)
- Text: `oklch(0.556 0 0)` — mid-gray
- Padding: `18px 67.5px`
- Radius: `3.35544e+07px` (pill)
- Use: Secondary/disabled CTAs, low-emphasis actions on light surfaces

**Directional Arrow (Carousel Pair)**
- Background: transparent (default), `rgba(255, 255, 255, 0.15)` on hover
- Text: White (`#ffffff`)
- Border: `1px 1px 1px 0px solid rgba(255, 255, 255, 0.7)` (left arrow — three-sided) or `1px 0px 1px 1px solid rgba(255, 255, 255, 0.7)` (right arrow)
- Radius: `0px 60px 60px 0px` (left) or `60px 0px 0px 60px` (right) — paired half-pills that snap together at the seam
- Hover: `transform: translate(-5%)` (left) or `translate(5%)` (right) — they pull away from the seam on hover
- Active: `transform: scale(0.975)` — soft press
- Use: Previous/next video, previous/next slide carousel controls

**Circular Icon Button**
- Background: White (`#ffffff`)
- Text/Icon: Black (`#000000`)
- Padding: `6.75px` (square)
- Radius: `3.35544e+07px` (pill — collapses to perfect circle at square dimensions)
- Use: Mute/unmute on hero video, scroll arrows, small action triggers

### Cards & Containers
- Background: `#ffffff` on light sections; `#000000` on inverted panels
- Border: `1px solid oklab/0.1` (≈ 10% black) on light cards; `1px solid rgba(255,255,255,0.3)` on dark
- Radius: **`11.25px`** for standard cards (default — most common at 72 occurrences); `19.25px` for prominent cards; `23.25px` for featured / hero cards
- Roof + Floor radii (`11.25px 11.25px 0px 0px` and `0px 0px 11.25px 11.25px`): used on stacked card halves where image meets caption
- Shadow: `none` on resting cards; `rgba(0,0,0,0.4) 0px 16px 48px 0px` for hero-floating imagery
- Internal padding: 18–27px standard, scales to 54–72px on feature panels

### Decorative Pill Container (the signature shape)
- Some cards and image containers use `23.25px 23.25px 360px 360px` — gentle top corners with a near-circular bottom dome
- Creates a "stadium card" or "tombstone" silhouette — image cards that read like archways
- Used for featured generations, model previews, and category showcases

### Badges / Tags / Pills

**Color Tag (Subject/Category)**
- Background: One of the multicolor variables — Hot Pink, Orange, Yellow, Green, Blue, Pink2, Pink, Purple
- Text: Black (`#000000`) for legibility on every color
- Padding: `4.5px 13.5px`
- Radius: `999px` (pill — count: 17 occurrences)
- Font: 12–14px `canvaSans` weight 500 or 700, sentence-case
- Use: Subject tags ("Action", "Anime", "Photo", "Fashion"), category indicators, model labels

**Tab Pill (Filter Group)**
- Background: transparent default, white on selected
- Text: white default, black on selected
- Padding: `4.5px 13.5px`
- Radius: `999px` per pill, sitting inside an `11.25px` tablist container
- Use: Tabbed content filters, model type selectors

**Mini Pill / Chip**
- Background: White or a multicolor variable
- Padding: `4.5px 13.5px`
- Radius: `3.35544e+07px` (full pill, like the buttons)
- Use: Status badges, "New" markers, micro-labels next to feature names

### Inputs & Forms
- Background: `#ffffff` on light surface, `#000000` on dark
- Border: `1px solid` near-black on light, `rgba(255, 255, 255, 0.3)` on dark
- Radius: `11.25px` (matches card system)
- Font: 16–18px `canvaSans` weight 400
- Focus: border shifts to `var(--color-black, #000)` on light or full white on dark, with the standard 3px outline
- Placeholder: `oklch(0.556 0 0)` — mid-gray, mid-weight

### Navigation
- Top nav: horizontal black bar (`#000000`) on the dark hero, transparent over light scroll
- Logo: white wordmark SVG (300×33px) on black, swaps to black on light
- Links: 14–18px `canvaSans` weight 400–500 in white (over black) or near-black (over light)
- Right-side CTAs: "Login" as text-only, "Sign up" as Leo Purple pill button
- Mobile: collapses to hamburger; menu slides as a full-bleed dark panel

### Decorative Elements

**Full-Bleed Video Hero**
- Generated video stills cycle behind the hero typography
- The headline sits over the video at maximum size (105–222px) with no scrim
- Video occupies the entire viewport on initial load — type is overlaid, not behind a frame
- Carousel arrows (the paired half-pill directional buttons) advance through the video set

**Asymmetric Stadium Cards**
- The `23.25px 23.25px 360px 360px` radius pattern creates an arch silhouette — small radius on top, near-circular dome on bottom
- Used for portrait-format AI-generated showcase cards
- Reinforces the "AI generates art objects" frame — these cards look like framed prints, not screenshots

**Marquee Logo / Tag Strips**
- Horizontal scrolling strips of category tags or partner logos
- Tags rotate through the multicolor palette as they scroll
- No fade gradient at the edges — the strip cuts hard at the viewport bound

## Do's and Don'ts

### Do
- Use `leoSans` weight 900 uppercase for every display-size headline (60px+) — this is the brand voice
- Run line-height at `0.80` on headlines 60px+ for the signature stacked-brick density
- Apply negative letter-spacing scaling proportionally with size (`-4.44px` at 222px, `-1.3px` at 130px, normal below 30px)
- Use fully-pill radius (`9999px` / `999px` / `3.35544e+07px`) for every button, tag, chip, and pill control
- Use `11.25px` as the default card radius — escalate to `19.25px` and `23.25px` for emphasis
- Reserve Leo Purple (`#6e60ee`) for primary CTAs and key interactive moments on light surfaces
- Use the multicolor tag palette (hot pink, orange, yellow, green, blue, pink2) as hard solid fills on category tags — never as gradients
- Pair `leoSans` (display) with `canvaSans` (body) — never mix
- Use `canvaSans` 18px weight 500 sentence-case for button labels (not uppercase)
- Alternate full-black and full-white panel sections for chapter-like pacing
- Float generated AI imagery with the heavy `0px 16px 48px` or `0px 24px 80px` shadows
- Use the asymmetric arched radius (`23.25px 23.25px 360px 360px`) for portrait showcase cards — the stadium silhouette

### Don't
- Don't use `leoSans` below weight 800 at display sizes — the heaviness IS the identity
- Don't use mixed-case for display headlines — always UPPERCASE at 60px+
- Don't introduce any radius value between 30px and 360px — the gap is intentional (small or fully pill, nothing in between)
- Don't use gradients on UI chrome — Leonardo's gradient energy lives entirely inside the AI-generated imagery, never on buttons or surfaces
- Don't soften the black or white — Leonardo uses `#000000` and `#ffffff`, never grays for primary surfaces
- Don't put drop shadows on buttons or cards — only on floating imagery
- Don't use horizontal rules for section breaks — alternating black/white panels do that work
- Don't use the multicolor tag palette as accent colors elsewhere — they're tag-only; Leo Purple is the one accent that crosses surfaces
- Don't put `canvaSans` at sizes above 30px — `leoSans` owns display
- Don't put `leoSans` at sizes below 30px (except as a weight-900 micro-eyebrow) — `canvaSans` owns body
- Don't add noise textures, glow halos, or frosted backdrop blurs — Leonardo is poster-flat
- Don't center-align body copy — Leonardo's body text is left-aligned; only display headlines and CTAs center

---

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <640px | Single-column, hero type drops to ~64–86px, paired arrow buttons stack |
| Mobile | 640–767px | Hero ~86–100px, 2-up tag strips, single-column features |
| Tablet | 768–1023px | Hero ~100–130px, 2-column feature grids begin |
| Small Desktop | 1024–1159px | Hero ~130–180px, 3-column card grids |
| Desktop | 1160–1279px | Hero ~180–222px, full multi-column showcase grids |
| Large Desktop | ≥1280px | Maximum type scale (222px hero), max-width content cap |

### Touch Targets
- Primary CTAs: minimum 44px tap height; standard button is 18px text + `18px 67.5px` padding → ~54px tall
- Tag pills: `4.5px 13.5px` padding → ~25px tall — supplemented with 8px+ surrounding gap for thumb area
- Directional carousel arrows: pair occupies a generous ~80×60px target on mobile

### Collapsing Strategy
- **Hero type**: 222px → 130px → 100px → 86px progressive scale; weight 900 maintained throughout
- **Tracking**: Negative letter-spacing scales proportionally — `-4.44px` at 222px, `-0.86px` at 86px, normal below 30px
- **Line-height**: Display stays at `0.80–0.93` even at mobile sizes — the brick-stack density is preserved
- **Carousel arrows**: Paired half-pill arrows stack vertically on small mobile, becoming top/bottom instead of left/right
- **Stadium cards**: The arched-bottom radius compresses but the silhouette holds — 360px dome scales to viewport
- **Multicolor tag strips**: Marquees shorten cycle distance on mobile; tags maintain `999px` pill radius
- **Panel inversion**: Black/white alternation persists at every breakpoint — chapter rhythm is non-responsive
- **Section spacing**: 180px on desktop reduces to ~90px on mobile, but never below — Leonardo defends its breathing room

### Image Behavior
- Full-bleed hero video stays full-bleed at every breakpoint — never letter-boxed
- Generated showcase images maintain stadium-arch silhouette and `0px 16px 48px` shadow on mobile
- Image grids reflow from 4-up → 3-up → 2-up → 1-up as breakpoints narrow
- Logo wordmark scales but never collapses to icon — the leonardo wordmark is always the wordmark

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Leo Purple (`#6e60ee`)
- Light Surface: Pure White (`#ffffff`)
- Dark Surface: Pure Black (`#000000`)
- Hairline Surface: `#ededed`
- Primary Text on Light: `#000000`
- Primary Text on Dark: `#ffffff`
- Secondary Text on Light: `#999999` (Gray2)
- Soft White on Dark (60% / 40% / 30%): `rgba(255,255,255,0.6)`, `rgba(255,255,255,0.4)`, `rgba(255,255,255,0.3)`
- Tag Hot Pink: `#ff3386` · Orange: `#ff5d4b` · Yellow: `#ffc533` · Green: `#03e65b` · Blue: `#33d0ff` · Pink2: `#d25fff` · Pink: `#d591d5`
- Hero Imagery Shadow: `rgba(0, 0, 0, 0.5) 0px 24px 80px 0px`
- Focus Outline: `oklab(0.708 0 0 / 0.5) none 3px`

### Example Component Prompts
- "Create a hero section on a pure white background with a headline at 130px `leoSans` weight 900 UPPERCASE, line-height `0.80`, letter-spacing `-1.3px`, color `#000000`. Below it, a Leo Purple (`#6e60ee`) primary CTA button — 18px `canvaSans` weight 500 sentence-case ('Start free trial'), white text, fully-pill (`9999px`) radius, padding `18px 67.5px`, no shadow, no border."
- "Build a generated-image showcase card with stadium-arch radius `23.25px 23.25px 360px 360px`, dropping `rgba(0, 0, 0, 0.4) 0px 16px 48px 0px` over a white canvas. Caption sits below with a 14px `canvaSans` weight 500 title in `#000000` and a tag pill — green (`#03e65b`) background, black text, `999px` radius, `4.5px 13.5px` padding."
- "Construct a paired carousel control with two half-pill buttons sharing a vertical seam: left button has radius `0px 60px 60px 0px` and `1px 1px 1px 0px solid rgba(255, 255, 255, 0.7)` border; right has radius `60px 0px 0px 60px` and `1px 0px 1px 1px solid rgba(255, 255, 255, 0.7)` border. Hover translates each button 5% away from the seam; active state scales to `0.975`."
- "Design an inverted panel section with `#000000` background, white headline at 100px `leoSans` weight 900 UPPERCASE line-height `0.80`. Add three category tags below — Hot Pink (`#ff3386`), Orange (`#ff5d4b`), Yellow (`#ffc533`) — each a `999px` pill with black text, `4.5px 13.5px` padding, 14px `canvaSans` weight 500."
- "Create a horizontal marquee strip of multicolor tag pills cycling through the seven-color tag palette. Each pill is `999px` radius, `4.5px 13.5px` padding, 14px `canvaSans` weight 500, black text. Marquee scrolls left at constant velocity, no fade-edge gradient — hard cut at viewport bounds."

### Iteration Guide
1. Default to `leoSans` weight 900 UPPERCASE for every display-size headline — sentence-case display reads as a different brand
2. Lock display line-height to `0.80` — the brick-stacked density is the signature
3. Use fully-pill radius (`9999px`) for every button, tag, and chip — no mid-range radii on interactive shapes
4. Card radius escalates: `11.25px` default → `19.25px` featured → `23.25px` hero. Stadium-arch (`23.25px 23.25px 360px 360px`) for portrait showcase cards.
5. Leo Purple (`#6e60ee`) is the one cross-surface accent — multicolor palette is tag-only
6. Float imagery with heavy shadows; flat-finish all UI chrome
7. Alternate `#ffffff` and `#000000` full panels for chapter rhythm — no dividers
8. `canvaSans` for everything below 30px; `leoSans` for everything above 60px
9. Negative letter-spacing scales with size — `-4.44px` at 222px, normal at body
10. Buttons stay sentence-case ("Start free trial"); only display headlines uppercase
