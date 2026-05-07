---
version: alpha
name: Pitch
description: Theatrical violet-lavender atmosphere with Mark Pro 800 display headlines, Eina01 body type, and signature glassmorphic floating panels over gradient meshes.

colors:
  # Canvas / atmosphere
  background: "#f0eff4"  # lavender wash field
  surface: "#ffffff"
  surface-dark: "#1e1d28"  # deep violet panel

  # Ink — charcoal violet, never pure black
  ink: "#2b2a35"
  ink-pure: "#000000"
  ink-inverted: "#ffffff"
  text-secondary: "#4a4858"
  text-muted: "#6b6a7a"

  # Brand
  primary: "#6b53ff"  # Pitch Violet
  primary-hover: "#586ee0"
  on-primary: "#ffffff"
  display-purple: "#8d49f7"

  # Highlights / accents
  highlight-yellow: "#ffd02c"
  warm-alert: "#ffa000"

  # Glass surfaces (flattened opaque approximations)
  glass-white: "#fafafc"  # was rgba(255,255,255,0.72) — flattened opaque approx
  glass-light: "#fcfcfd"  # was rgba(255,255,255,0.88) — flattened opaque approx
  glass-border: "#e5e5ea"  # was rgba(255,255,255,0.4) — flattened opaque approx
  glass-dark: "#26252f"  # was rgba(30,29,40,0.6) — flattened
  glass-dark-strong: "#211f29"  # was rgba(30,29,40,0.8) — flattened

  # Gradient stops
  gradient-top: "#b9a7ff"
  gradient-bottom: "#6b53ff"

  # Neutrals & borders
  border: "#dddfe5"
  border-cool: "#d7d8e0"
  border-ink: "#2b2a35"

  # Shadow tints (flattened approximations)
  shadow-soft: "#e0e0e0"  # was rgba(0,0,0,0.15) — flattened approx
  shadow-cool: "#d4d6e0"  # was rgba(103,110,144,0.2) — flattened
  shadow-violet: "#c8c5d0"  # was rgba(43,42,53,0.25) — flattened

typography:
  display-xl:
    fontFamily: "Mark Pro, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 90px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -1.8px
  display-large:
    fontFamily: "Mark Pro, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 60px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -1.2px
  display:
    fontFamily: "Mark Pro, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 42px
    fontWeight: 800
    lineHeight: 1.4
    letterSpacing: -0.84px
  h1:
    fontFamily: "Eina01, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0px
  h2:
    fontFamily: "Eina01, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0px
  h3:
    fontFamily: "Mark Pro, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 27px
    fontWeight: 800
    lineHeight: 1.4
    letterSpacing: -0.54px
  intro-large:
    fontFamily: "Eina01, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 2.0
    letterSpacing: 0px
  body-large:
    fontFamily: "Eina01, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0px
  body:
    fontFamily: "Eina01, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 2.0
    letterSpacing: 0px
  link-bold:
    fontFamily: "Eina01, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0px
  button:
    fontFamily: "Eina01, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.4px
  caption:
    fontFamily: "Eina01, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  label:
    fontFamily: "Mark Pro, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.85
    letterSpacing: 1.3px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 28px
  2xl: 30px
  3xl: 40px
  4xl: 60px
  5xl: 120px

rounded:
  none: 0px
  micro: 3px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 14px
  2xl: 20px
  3xl: 26px
  4xl: 56px
  pill: 9999px

components:
  # Primary violet CTA
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 12px 20px
  button-primary-hover:
    backgroundColor: "{colors.display-purple}"
    textColor: "{colors.on-primary}"

  # Secondary ghost
  button-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 12px 20px

  # Circular nav button
  button-circular:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-pure}"
    rounded: "{rounded.pill}"
    padding: 1px 6px
  button-circular-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink-inverted}"

  # Standard card
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 20px
  card-feature:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 32px

  # Glass panel — signature
  glass-panel:
    backgroundColor: "{colors.glass-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px
  glass-panel-dark:
    backgroundColor: "{colors.glass-dark}"
    textColor: "{colors.ink-inverted}"
    rounded: "{rounded.xl}"
    padding: 24px

  # Text input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 14px

  # Violet pill badge
  badge-violet:
    backgroundColor: "{colors.gradient-top}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.2xl}"
    padding: 4px 10px

  # Yellow callout stamp
  badge-yellow:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.micro}"
    padding: 4px 10px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.glass-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 16px 24px
---

# Pitch Design System

## Overview

Pitch is what happens when presentation software stops apologizing for being software. The homepage opens onto a violet-lavender gradient wash — a painterly, atmospheric backdrop that refuses to be a flat hex value — and then places a single, enormous Mark Pro headline (`{colors.ink}`, weight 800, tight line-height) across it. The effect is immediately theatrical: the marketing surface behaves less like a SaaS landing page and more like the inside of a deck itself, where color is a stage and typography is the performer. Pitch's craft is about dimensional depth on a surface most tools leave flat — frosted navigation chrome, floating product dashboards with soft violet-tinted shadows, and panel stacks that suggest a deep z-axis rather than a single plane.

Where Linear and Stripe render restraint, Pitch renders **confidence**. The palette is narrow but saturated: a near-black charcoal-violet (`{colors.ink}`) for type, a signature electric violet (`{colors.primary}`) for interactive moments, and a deeper display purple (`{colors.display-purple}`) that appears as the brand's louder voice. Layered behind all of it are soft lavender-to-periwinkle gradient meshes — never hard stops, always blended — that give the page an ambient, lit-from-within quality. Mark Pro at 90px / weight 800 / -1.8px tracking dominates the hero; Eina01 handles body, links, and buttons at a quieter 16-18px with generous 2.00 line-height for breathing room. The contrast between heavy display type and airy body copy is deliberate: it's how decks work — a big claim, then space to absorb it.

The glassmorphic treatment shows up in the second fold, where the live product UI is rendered as a **frosted floating panel** on top of the violet gradient: a translucent white-ish background flattened to `{colors.glass-white}`, a whisper-thin `{colors.glass-border}` border, a soft 8-14px radius, and a diffuse shadow that grounds it without anchoring it. The panel doesn't sit *on* the page — it hovers over the gradient, which bleeds through subtly from behind. This is the defining Pitch move: **glass as a product surface, not just a decorative flourish**.

**Key Characteristics:**
- Dark-violet primary text (`{colors.ink}`) on lavender-gradient backgrounds — never pure black on white
- Brand electric violet (`{colors.primary}`) as interactive accent, display purple (`{colors.display-purple}`) for marketing emphasis
- Mark Pro at weight 800 for display (90px / 60px / 42px) with aggressive negative tracking (-1.8px at 90px)
- Eina01 at weight 400-700 for body, buttons, links, and UI (13px-22px)
- Button text treatment: uppercase, weight 700, 14px, 1.4px letter-spacing — a stamp-like confidence
- Glassmorphic floating panels: blur 20px effect, translucent white fill, 8-14px radius
- Gradient meshes as ambient background, never as fill — radial violet/lavender bloom behind hero content
- Soft layered shadows in violet-tinted approximations
- Yellow accent (`{colors.highlight-yellow}`) as highlight stamp — playful punctuation in an otherwise violet system
- 8px base spacing, 12px / 20px / 28px / 30px / 40px / 60px / 120px rhythm
- Radius scale: 3px (inline tags), 6px (buttons), 8px (cards), 12-14px (panels), 20-26px (featured cards)

## Colors

### Brand & Accent
- **Pitch Violet** (`{colors.primary}`): The signature brand color. Primary CTA backgrounds, active states, interactive accents, selected items. Electric, confident, unmistakably Pitch.
- **Display Purple** (`{colors.display-purple}`): The louder voice — marketing graphics, gradient stops, link hover highlights. Warmer and more saturated than Pitch Violet.
- **Violet Hover** (`{colors.primary-hover}`): Pressed/active variant of Pitch Violet — slightly shifted blue.
- **Lavender Wash** (`{colors.background}`): The atmospheric background tint — not a surface color, a *field* color.

### Text & Ink
- **Charcoal Violet** (`{colors.ink}`): Primary text and ink color. A near-black with a purple-cool undertone — never use pure `#000`. Headlines, body text, solid UI chrome.
- **Deep Violet Panel** (`{colors.surface-dark}`): Dark panel background — marginally deeper than charcoal violet for stacked dark surfaces.
- **Pure White** (`{colors.surface}`): Card surfaces, reversed text on dark sections, glass panel fill base.
- **True Black** (`{colors.ink-pure}`): Reserved for extreme contrast moments — not the default ink color.

### Accent & Highlight
- **Highlight Yellow** (`{colors.highlight-yellow}`): Playful accent — used as 9px solid border strokes on callout divs, highlight swashes on key words.
- **Warm Alert** (`{colors.warm-alert}`): Dashed-border warning treatment for emphasis states.

### Neutrals & Borders
- **Border Soft** (`{colors.border}`): Default 1px border on images, cards, and dividers.
- **Border Cool** (`{colors.border-cool}`): Slightly cooler card border variant.
- **Border Ink** (`{colors.border-ink}`): Solid dark border used for high-contrast dividers.

### Glass & Atmosphere
- **Glass White** (`{colors.glass-white}`): The glass panel fill (flattened opaque approximation of 72% white).
- **Glass Light** (`{colors.glass-light}`): Lighter glass for nav bars on busy backgrounds.
- **Glass Border** (`{colors.glass-border}`): The characteristic frost-edge border on glass panels.
- **Glass Dark** (`{colors.glass-dark}`): Dark-mode glass — flattened approximation.
- **Glass Dark Strong** (`{colors.glass-dark-strong}`): Ultra-dark glass for modals over gradients.
- **Gradient Stop Top** (`{colors.gradient-top}`): Lavender starting stop for background mesh.
- **Gradient Stop Bottom** (`{colors.gradient-bottom}`): Violet ending stop — the mesh resolves into brand.

## Typography

### Font Families
- **Display**: `Mark Pro`, fallback `-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif`
- **Body / UI**: `Eina01`, same fallbacks
- **No variable fonts, no OpenType feature flags** — Pitch runs classic static weights

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-xl` | The biggest Mark Pro moment on the page — 90px hero |
| `display-large` | Secondary hero headlines (60px) |
| `display` | Feature panel headlines (42px) |
| `h1` | Page-level Eina01 headings (28/800) |
| `h2` | Sub-section Eina01 headings (28/700) |
| `h3` | Mark Pro 27px sub-section heads |
| `intro-large` | Airy 22px intro copy |
| `body-large` | Lead paragraphs |
| `body` | Standard reading text with airy 2.0 line-height |
| `link-bold` | Bold links |
| `button` | UPPERCASE button labels with +1.4px tracking |
| `caption` | Small metadata |
| `label` | UPPERCASE Mark Pro 13px label |

### Principles
- **Mark Pro 800 is the stage voice.** Headlines use weight 800 at every display size.
- **Eina01 is the conversation.** Body, links, buttons, captions — Eina01 runs the UI at weights 400 and 700.
- **Airy body line-heights.** 2.00 line-height on 16-22px body text gives paragraphs breathing room.
- **Tight display tracking.** Tracking scales negatively with size: -1.8px at 90px → -0.54px at 27px.
- **Uppercase buttons and labels.** Button text uses uppercase with +1.4px tracking — a stamp-like signature.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 4px with primary rhythm at `lg` (20px) → `4xl` (60px) → `5xl` (120px).

### Grid & Container
- Max content width: approximately 1280px
- Hero: centered single-column, headline max-width ~900px
- Feature rows: 2-column (image + copy) or 3-column cards
- Product demo sections: full-bleed gradient background with floating glass UI centered

### Whitespace Philosophy
- **The gradient IS the whitespace.** Pitch's violet-lavender mesh is ambient, atmospheric — empty space isn't white, it's colored air.
- **Enormous display type + airy body.** 90px headlines followed by 22px intro copy with 2.00 line-height: a rhythm of punch and pause.
- **Generous vertical breaks.** `5xl` between major sections, `4xl` between subsections.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, gradient background | Page background, section backdrops |
| Whisper (Level 1) | `0 3px 10px {colors.shadow-soft}` | Standard cards, images, small components |
| Lifted (Level 2) | `0 4px 30px {colors.shadow-soft}` | Featured cards, hover states on product tiles |
| Floating (Level 3) | `0 8px 26px {colors.shadow-cool}` | Modals, tooltips — shadow has cool gray tint |
| Deep Float (Level 4) | `0 6px 27px {colors.shadow-violet}` | Nav controls, floating carousel buttons |

**Shadow Philosophy**: Pitch's depth language is **atmospheric, not architectural**. Shadows are soft, diffuse, and slightly violet-tinted when they appear on dark elements. The charcoal-violet shadow family carries the brand's cool cast into the shadow itself. On light surfaces, low-opacity blacks with generous blur radii (10px, 30px) keep shadows hazy and atmospheric rather than crisp and defined. Nothing on Pitch casts a hard shadow.

### The Glass Recipe (Signature)
Glass panels combine the flattened `{colors.glass-white}` background with `{colors.glass-border}` border, a 14px radius, and a layered shadow. They must always sit over a gradient mesh — the blur is the point.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Edge-to-edge sections |
| `micro` | 3px | Inline tags, badge corners on pills |
| `sm` | 6px | Standard buttons, inputs, select dropdowns |
| `md` | 8px | Default cards, images, videos |
| `lg` | 12px | Featured cards, panels |
| `xl` | 14px | Glass panels, product dashboards |
| `2xl` | 20px | Pill badges, hero illustration cards |
| `3xl` | 26px | Large floating dashboards |
| `4xl` | 56px | Hero illustration frames |
| `pill` | 9999px | Circular nav buttons, avatars, status dots |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly.

### Buttons
- **`button-primary`** — Pitch Violet fill with white UPPERCASE text, 6px radius. Hover shifts to `{colors.display-purple}`.
- **`button-ghost`** — Transparent with `{colors.border-ink}` border for secondary CTAs.
- **`button-circular`** — White circle with shadow for carousel arrows, fills violet on active.

### Cards
- **`card`** — Standard 8px-radius white card with `{colors.border}` border and whisper shadow.
- **`card-feature`** — Larger 12px-radius card for feature sections.

### Glass Panels (Signature)
- **`glass-panel`** — Translucent white surface (flattened) with frost-edge border and layered shadow. Must sit over a gradient mesh.
- **`glass-panel-dark`** — Dark-mode equivalent for product chrome.

### Inputs
- **`input`** — White surface, `{colors.border}` border, 6px radius, 12x14px padding. Focus brings primary-color border plus violet ring.

### Badges
- **`badge-violet`** — Lavender pill for status/labels.
- **`badge-yellow`** — Yellow callout stamp for playful emphasis.

### Navigation
- **`nav-bar`** — Glass-light background floating above gradient hero. Eina01 16px nav links. Sign-up CTA in violet.

## Do's and Don'ts

### Do
- Pair Mark Pro (weight 800) display with Eina01 (weight 400/700) body — the typographic rhythm is non-negotiable
- Use violet-tinted charcoal (`{colors.ink}`) as your primary ink instead of pure black
- Layer glass panels over gradient meshes — the blur needs something worth blurring
- Apply backdrop blur generously on floating UI chrome over colored backgrounds
- Use `{colors.glass-white}` as the glass fill — not solid white, never fully opaque
- Reserve `{colors.primary}` for interactive/CTA moments, `{colors.display-purple}` for marketing emphasis
- Uppercase button text at 14px/700 weight with +1.4px tracking — Pitch's button-as-stamp signature
- Use airy line-heights (2.00) on body copy 16-22px to create presentation-like pacing
- Add yellow `{colors.highlight-yellow}` 9px border strokes sparingly for playful emphasis

### Don't
- Don't use pure `{colors.ink-pure}` as primary ink — `{colors.ink}` carries the cool violet cast
- Don't stack glass panels without something colored or gradient behind them — clear glass on white reads like a broken render
- Don't use solid fills for floating product chrome — the translucency IS the product feel
- Don't pair Mark Pro at light weights — it only lives at 800
- Don't use warm neutrals or cream tones in body surfaces — the palette is cool violet throughout
- Don't render hard-edged drop shadows — Pitch shadows are always diffuse
- Don't use gradients with hard color stops — always feather the transitions with radial blooms
- Don't use `{colors.primary}` decoratively — it's reserved for CTAs, selections, and active product states
- Don't introduce more than one warm accent (`{colors.highlight-yellow}`) per section

---

## Responsive Behavior

*(Preserved from original 9-section format — Google's parser keeps unknown sections.)*

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Single column, hero at 42-48px, glass panels edge-to-edge |
| Tablet | 768-1082px | Two-column starts, nav collapses to hamburger |
| Desktop Small | 1082-1399px | Full nav, standard card grids |
| Desktop | 1399-1667px | Default design viewport |
| Large Desktop | >1667px | Expanded margins, hero max-width constraint |

### Collapsing Strategy
- Hero display: 90px → 60px → 42px (tracking adjusts proportionally from -1.8px to -0.84px)
- Glass panels: maintain blur at all sizes, but reduce radius from 14px → 8px on mobile
- Two-column image+copy: stacks vertically on mobile, image above
- Navigation: full links → hamburger at 1082px
- Gradient meshes: simplify from 3-radial to single-radial on mobile for performance

### Touch Targets
- All buttons: minimum 40px tall at 14px type + 12px vertical padding
- Circular nav buttons: 36-44px diameter
- Glass panels on mobile: min-height 200px to stay tappable

---

## Agent Prompt Guide

*(Preserved from original 9-section format — the copy-paste payload section.)*

### Quick Color Reference
- Primary CTA: Pitch Violet (`{colors.primary}`)
- Marketing emphasis: Display Purple (`{colors.display-purple}`)
- Ink: Charcoal Violet (`{colors.ink}`)
- Dark panel: Deep Violet (`{colors.surface-dark}`)
- Glass fill: `{colors.glass-white}`
- Glass border: `{colors.glass-border}`
- Lavender field: `{colors.background}`
- Highlight: Yellow (`{colors.highlight-yellow}`)
- Standard shadow: `0 3px 10px {colors.shadow-soft}`
- Elevated shadow: `0 6px 27px {colors.shadow-violet}`

### Example Component Prompts
- "Create a hero section with a layered gradient mesh in lavender→violet (`{colors.gradient-top}` → `{colors.gradient-bottom}`). Headline in Mark Pro weight 800, 90px, line-height 1.00, letter-spacing -1.8px, color `{colors.ink}`. Intro copy in Eina01 weight 400, 22px, line-height 2.00. Primary CTA: `{colors.primary}` background, white text, Eina01 14px weight 700 UPPERCASE, 1.4px tracking, 6px radius, 12x20px padding."
- "Build a glass product panel: background `{colors.glass-white}` with simulated 20px blur, border `{colors.glass-border}`, 14px radius, shadow `0 4px 30px {colors.shadow-soft}`. Place over a violet gradient mesh."
- "Design a pricing card: white background, 1px solid `{colors.border}`, 12px radius, `0 3px 10px {colors.shadow-soft}` shadow. Plan name in Eina01 28px weight 800. Price in Mark Pro 60px weight 800 with -1.2px tracking. Feature list in Eina01 16px weight 400 with 2.00 line-height. CTA violet `{colors.primary}` full-width bottom."
- "Create a glassmorphic nav bar floating above a gradient hero: position fixed top, background `{colors.glass-light}`, border-bottom `1px solid {colors.glass-border}`. Logo left, nav links Eina01 16px `{colors.ink}`, Sign up CTA right in `{colors.primary}`."
- "Build a testimonial with yellow-stamp highlight: quote in Mark Pro 42px weight 800, letter-spacing -0.84px. Author line in Eina01 14px weight 700 UPPERCASE with 1.4px tracking. Wrap the emphasized word in a `<mark>` with 9px solid `{colors.highlight-yellow}` border."

### Iteration Guide
1. Always layer glass on gradient — backdrop-filter with no colored background behind is invisible
2. Mark Pro 800 for any display moment; Eina01 400/700 for everything else
3. Shadows should have 10-30px blur radius and low opacity — nothing crisp, nothing black
4. Use `{colors.ink}` not `{colors.ink-pure}` — the cool violet cast unifies Pitch's surfaces
5. Reserve `{colors.primary}` for action and `{colors.display-purple}` for attention — they're not interchangeable
6. Button text is UPPERCASE weight 700 with +1.4px tracking
7. When building a glass panel, always ask: "What's behind this?" If "plain white", remove the glass treatment
