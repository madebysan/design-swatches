---
version: alpha
name: Things
things-tagline: Mac-native craft
description: Paper-cool canvas (#f2f5f7), system SF Pro stack, dual-layer warm shadow, single Things Blue accent, graduated border-radius, scale(0.95) press feedback.

colors:
  # Canvas + cards
  background: "#f2f5f7"
  surface: "#ffffff"

  # Brand accent
  primary: "#2576eb"
  primary-soft: "#4f91fb"
  primary-bright: "#649fff"
  primary-deep: "#3c84f3"
  sky: "#5c9cf5"
  sky-cited: "#1b5dbd"

  # Text hierarchy
  ink: "#303336"
  ink-deep: "#2c3138"
  ink-mid: "#44474b"
  text-secondary: "#55606e"
  text-tertiary: "#8e9196"
  text-disabled: "#8792a1"
  text-mist: "#9299a4"

  # On-color
  on-primary: "#ffffff"

  # Borders
  border: "#dfe3e8"
  border-divider: "#dde1e7"  # was rgba(0,28,70,.12) — flattened over paper

  # Interactive states (opaque approximations)
  hover-tint: "#ebeef0"      # was rgba(4,15,26,.05) — flattened over paper
  selection-tint: "#cfdef9"  # was rgba(92,156,245,.2) — flattened over paper
  focus-ring: "#92baf5"      # was rgba(37,118,235,.5) — flattened over paper

  # Shadow tints
  shadow-soft: "#dadde0"      # was rgba(0,0,0,.1) — flattened over paper
  shadow-soft-light: "#e5e8eb" # was rgba(0,0,0,.05) — flattened over paper
  shadow-edge: "#cfd5dd"       # was rgba(38,52,74,.15) — flattened over paper

typography:
  display:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0px
  subheading-large:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.00
    letterSpacing: 0px
  subheading-quiet:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0px
  heading-medium:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 20.25px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0px
  heading-medium-quiet:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 20.25px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 0px
  link-prominent:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 20.25px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0px
  body-large:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0px
  link-default:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0px
  body-standard:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 16.96px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 0px
  body:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 0px
  caption:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 15.3px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0px
  caption-bold:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 15.3px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0px
  ui-small:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0px
  micro-link:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 13.68px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 0px
  micro:
    fontFamily: "ui-sans-serif, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 18px
  xl: 27px
  2xl: 40px
  3xl: 56px
  4xl: 81px

rounded:
  none: 0px
  xs: 3px
  sm: 4.5px
  md: 6px
  comfortable: 6.4px
  apple: 7.6px
  panel: 10.8px
  card: 12.8px
  featured: 18px
  pill: 9999px

components:
  # Primary blue button — Apple-flavored
  button-primary:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-standard}"
    rounded: "{rounded.apple}"
    padding: 7.12px 16.96px
  button-primary-hover:
    backgroundColor: "{colors.primary-bright}"
  button-primary-active:
    backgroundColor: "{colors.primary-deep}"

  # Ghost link-button
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.body-standard}"
    rounded: "{rounded.apple}"
    padding: 7.12px 16.96px

  # Subtle panel button
  button-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-standard}"
    rounded: "{rounded.comfortable}"
    padding: 7.12px 16.96px

  # Card — standard
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.card}"
    padding: 27px

  # Card — featured (testimonials, hero panels)
  card-featured:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.featured}"
    padding: 27px

  # Compact card
  card-compact:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.panel}"
    padding: 18px

  # Input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.comfortable}"
    padding: 8px
    borderColor: "{colors.border}"
  input-focus:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.focus-ring}"

  # Top nav
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 12px 27px
    borderColor: "{colors.shadow-edge}"

  # Nav link
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body}"
  nav-link-hover:
    textColor: "{colors.primary}"

  # Check-circle (empty)
  check-circle:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.pill}"
    size: 20px
    borderColor: "{colors.border}"
  check-circle-checked:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.pill}"
    size: 20px
  check-circle-starred:
    backgroundColor: "{colors.sky}"
    rounded: "{rounded.pill}"
    size: 20px

  # Pill / tag
  pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.panel}"
    padding: 2px 8px

  # Selected list-row tint
  list-row-selected:
    backgroundColor: "{colors.selection-tint}"
    textColor: "{colors.ink}"

  # Hover row
  list-row-hover:
    backgroundColor: "{colors.hover-tint}"
    textColor: "{colors.ink}"
---

# Things Design System

## Overview

Things is the Platonic ideal of Mac-native craft — a to-do app that feels like a leather-bound notebook sitting on a walnut desk, not a productivity dashboard begging for attention. The entire surface is built on a paper-cool off-white canvas (`{colors.background}`) that reads as premium stationery rather than screen glare, and the typography is classic San Francisco — `ui-sans-serif` with `-apple-system` fallbacks — set at calm, conversational sizes that never crowd the eye. Where most productivity apps shout with bold purples and neon checkmarks, Things whispers. Its signal is restraint, and the result is an interface that has won an Apple Design Award in three different decades because every pixel has been loved.

The defining move is the *trio* of warm neutrals — `{colors.text-tertiary}` (mid gray), `{colors.text-secondary}` (blue-gray for links and secondary UI), and `{colors.ink-deep}` (deep charcoal for headings) — paired with a single saturated blue (`{colors.primary}`) that functions as the only chromatic accent in the system. That blue shows up exactly where it has to: the check-circle when a task is starred, the primary CTA, focus rings on inputs. Everything else is gray-on-paper, letting content breathe. Weights stay in the 400–700 range, but the composition almost never reaches for 700 at display sizes; 36px headings at weight 700 only at the very top of the page, and from there the hierarchy drops to 600 and 400 with a matter-of-fact Apple HIG rhythm. This is type treated like UI, not type treated like editorial.

What separates Things from every other "minimalist" app is its shadow system. Instead of the harsh drop shadows most web products reach for, or the flat no-shadow sterility, Things uses a signature dual-layer warm shadow. The first layer is a whisper of lift at 2px offset with 8px blur — enough to suggest a card resting on paper. The second is a hair-thin 2px halo with zero offset that acts as a quasi-border, defining the card's edge without needing an actual stroke. Combined with generous 18px border-radius on featured cards and a 10–12.8px radius on secondary surfaces, this gives every element a tactile, light-catching presence. Things doesn't simulate paper — it inhabits it.

**Key Characteristics:**
- SF Pro / `ui-sans-serif` system stack at Apple HIG-calm sizes — 36px max display, 16–18px body
- Paper-cool canvas (`{colors.background}`) — the definitive "not pure white" productivity background
- Dual-layer shadow signature — `0 2px 8px` soft lift paired with `0 0 2px` edge halo
- Blue accent (`{colors.primary}` / `{colors.sky}`) applied only to primary CTAs, focus rings, and check-circles
- Generous border-radius spectrum (3px inline → 18px featured cards) for subtle varied rhythm
- Asymmetric button padding (`7.12px 16.96px`) — Apple-flavored, slightly wider horizontally
- Scale transform on active press (`scale(0.95)`) — the tactile "click-down" micro-interaction
- Focus halo using blue at 50% opacity — accessibility without harshness

## Colors

### Primary
- **Paper** (`{colors.background}`): The primary canvas — cool off-white, barest blue-green undertone. The shade of high-quality bond paper in daylight.
- **Things Blue** (`{colors.primary}`): The single chromatic accent — primary CTA, link, focus anchor.
- **Sky Blue** (`{colors.sky}`): The softer variant — selected-row highlight, secondary link, starred check-circle.

### Text
- **Charcoal** (`{colors.ink}`): Primary text — headings, body, interactive labels.
- **Deep Slate** (`{colors.ink-deep}`): Slightly deeper alternate for emphasized headings.
- **Ink** (`{colors.ink-mid}`): Mid-tone for secondary headings.
- **Blue-Gray** (`{colors.text-secondary}`): Secondary text, timestamps, attribution.
- **Stone** (`{colors.text-tertiary}`): Tertiary text and metadata.
- **Fog** (`{colors.text-disabled}`): Disabled state, inactive nav.
- **Mist** (`{colors.text-mist}`): Lightest usable gray.

### Surface & Borders
- **Paper Canvas** (`{colors.background}`): Page and section background.
- **Pure White** (`{colors.surface}`): Card backgrounds, inputs, elevated surfaces.
- **Border Cool** (`{colors.border}`): Input borders and subtle dividers.
- **Divider Translucent** (`{colors.border-divider}`): Top-only hairline divider for list separators.

### Interactive States
- **Hover Tint** (`{colors.hover-tint}`): Ultra-subtle hover background on list rows.
- **Selection Tint** (`{colors.selection-tint}`): Selected-state — Sky Blue at 20% opacity, soft lavender-blue cast.
- **Focus Ring Blue** (`{colors.focus-ring}`): The keyboard halo — Things Blue at 50% opacity.
- **Active Press**: Buttons don't change color on press — they `scale(0.95)`, borrowed from iOS.

### Shadow Tints
- **Shadow Soft** (`{colors.shadow-soft}`): Signature card shadow base — soft downward lift.
- **Shadow Soft Light** (`{colors.shadow-soft-light}`): Hover-state lift; lighter, tighter.
- **Shadow Edge** (`{colors.shadow-edge}`): Sticky-header bottom border — flat 1px, no blur.

Things is functionally gradient-free. The visual richness comes entirely from layered shadows on the paper canvas.

## Typography

### Font Family
- **Primary**: `ui-sans-serif`, with fallbacks: `-apple-system`, `system-ui`, `Roboto`
- **Monospace**: Default system mono stack where needed (task attributes, keyboard shortcuts).

*Note: On macOS this resolves to SF Pro Text at body and SF Pro Display at headings. The design presumes Apple's native optical sizing; web substitutes can use Inter as a stand-in.*

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display}`, `{typography.body}`, etc.).

| Token | Use |
|---|---|
| `display` | Maximum size — top-of-page moments |
| `subheading-large` | Section heads, feature titles |
| `subheading-quiet` | Narrative sub-headings |
| `heading-medium` | Card titles, emphasized list headers |
| `heading-medium-quiet` | Readable sub-heading |
| `link-prominent` | Large CTA-adjacent links |
| `body-large` | Intro paragraphs, feature descriptions |
| `link-default` | Inline links at body-large size |
| `body-standard` | Bold emphasis within body |
| `body` | Standard reading text, nav links |
| `caption` | Metadata, small labels |
| `caption-bold` | Emphasized metadata, timestamps |
| `ui-small` | Button labels, small navigation |
| `micro-link` | Footer links, fine-print navigation |
| `micro` | Smallest labels, legal footer |

### Principles
- **System-native optical sizing**: `ui-sans-serif` automatically gets SF Pro Text at small sizes and SF Pro Display at large sizes on Apple platforms. Don't fight it.
- **Weight restraint**: 400 / 600 / 700 only. No 300, no 500, no 800.
- **Tight heading line-heights**: 1.00–1.20 — composed without descender collisions.
- **Relaxed body**: 1.30–1.35 — Apple HIG default.
- **No letter-spacing tricks**: SF Pro is self-spacing.
- **Heading AA hierarchy**: 36 → 24 → 20 → 18 → 16 — clean ratio ladder.

## Layout

### Spacing System
The complete scale lives in the `spacing:` token block above. Base unit is 8px with Apple-fractional values (the app sits at 0.9rem root sizing). Generous section spacing: `{spacing.4xl}` between major sections, `{spacing.2xl}` within sections.

### Grid & Container
- Max content width: approximately 1106px
- Hero: centered, single-column with generous vertical padding
- Testimonial grids: 4-column desktop → 2-column tablet → single column mobile
- Things stays on the paper canvas throughout — no dark/light section alternation

### Whitespace Philosophy
- **Breath over density**: Things uses more whitespace than comparable productivity tools. The empty space IS the product.
- **Paper as breathing room**: The `{colors.background}` canvas around white cards acts as visual rest.
- **Section beats**: Generous `{spacing.4xl}` (81px) section gaps create chapters without dividers.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Paper canvas, inline body text |
| Edge (Level 1) | `0 1px 0 {colors.shadow-edge}` | Sticky headers, nav bottom divider |
| Signature Lift (Level 2) | `0 2px 8px {colors.shadow-soft}, 0 0 2px {colors.shadow-soft}` | Standard cards, testimonial cards — THE Things shadow |
| Picked-Up (Level 3) | `0 2px 10px {colors.shadow-soft}, 0 0 0 1px {colors.shadow-soft-light}` | Hover-state elevation for cards, floating panels |
| Hover Nudge (Level 4) | `0 2px 4px {colors.shadow-soft-light}` | Button hover — subtle signal |
| Focus Halo (Level 5) | `0 0 0 2px {colors.focus-ring}` | Keyboard focus on all interactive elements |

**Shadow Philosophy**: Things' elevation is defined by the **dual-layer signature shadow** — a soft `0 2px 8px` downward lift paired with a `0 0 2px` hair-thin halo. The first layer creates the sensation of a card resting on paper. The second acts as a graphic edge, defining the card without a visible stroke. Together they produce the distinct Things tactile feel.

The shadow colors are technically neutral, but applied over the paper-cool canvas the perceived result is slightly warm — the shadow "inherits" the ambient paper tone. Swapping for pure white ruins the effect.

### Decorative Depth
- **No gradients, no blur, no glassmorphism**: Depth comes from shadow + card/paper layering.
- **Transform-based press feedback**: `scale(0.95)` on active replaces "shadow deepens." Physical scale compression like an iOS control.
- **Focus as color, not drop shadow**: Focus uses the blue ring, not increased elevation.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `xs` | 3px | Inline tags, tiny clipped images |
| `sm` | 4.5px | Highlighted mark elements, small inline buttons |
| `md` | 6px | Primary buttons, action links — "Apple-HIG-default" |
| `comfortable` | 6.4px | Input fields — softer than buttons |
| `apple` | 7.6px | Primary CTA — "real macOS button" Goldilocks radius |
| `panel` | 10.8px | Small panels, tag pills, badges |
| `card` | 12.8px | Standard card containers |
| `featured` | 18px | Testimonial cards, hero panels — signature generous radius |
| `pill` | 9999px | Avatars, circular check-circles, icon buttons |

Things' radius philosophy is *graduated* — a full ladder so different elements feel hierarchically distinct.

## Components

The full component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card-featured}`).

### Buttons
- **`button-primary`** — Things Blue Apple-flavored fill, white text, `{rounded.apple}` radius, asymmetric padding. Hover brightens; active deepens via `scale(0.95)` rather than color shift in app.
- **`button-ghost`** — Transparent, blue text. Underline appears on hover.
- **`button-panel`** — White surface with signature shadow, charcoal text. Tertiary actions on paper.

### Cards
- **`card`** — White surface, `{rounded.card}` radius, signature shadow. The standard.
- **`card-featured`** — `{rounded.featured}` radius, generous 27px+ padding. Testimonials and hero panels.
- **`card-compact`** — `{rounded.panel}` radius, 18px padding. Smaller surfaces.

### Inputs
- **`input`** — White surface, `{colors.border}` 1px hairline, `{rounded.comfortable}`. Focus replaces border with the blue ring shadow at 50% opacity. Placeholder uses `{colors.text-tertiary}`.

### Links (multi-state palette)
Things uses 8 distinct link treatments — primary content, de-emphasized, brand blue, action blue, legal, secondary metadata, caption, cited. Hierarchy is achieved through gray value alone, never new colors.

### Navigation
- **`nav-bar`** — White bar with `{colors.shadow-edge}` 1px bottom shadow as divider. Logo + wordmark left; links + primary CTA right.
- **`nav-link`** — 16px charcoal text. Hover: underline.

### Check-Circle Micro-interaction
- **`check-circle`** — 20px circle, 1.5px stroke `{colors.border}`, transparent fill.
- **`check-circle-checked`** — `{colors.primary}` fill, white checkmark, scale-bounce.
- **`check-circle-starred`** — `{colors.sky}` with star glyph instead of tick.

### Quotes / Testimonials
- White surface, `{rounded.featured}`, signature shadow, 27px padding. Tweet body 15.3px charcoal; @handle in stone; attribution name 15.3px weight 700.

### Pills / Badges
- **`pill`** — White surface (or paper-tinted) with shadow, `{rounded.panel}` (softly rounded, not fully pill). 13px text in charcoal.

## Do's and Don'ts

### Do
- Use Paper (`{colors.background}`) as the canvas — pure white destroys the craft
- Layer the dual signature shadow on every card — `0 2px 8px` plus `0 0 2px` at 10% black
- Use `ui-sans-serif` with `-apple-system` fallback — optical sizing is doing free work
- Limit weights to 400 / 600 / 700 — three-weight economy is the calm
- Apply the blue accent (`{colors.primary}`) only where it must signal action or focus
- Use graduated border-radius (3 → 6 → 10.8 → 12.8 → 18px) for hierarchy
- Pad buttons asymmetrically (`7.12px 16.96px`) — Apple-native horizontal emphasis
- Use `scale(0.95)` transform on active press, not color darkening
- Let the paper canvas breathe between cards — `{spacing.4xl}` section spacing

### Don't
- Don't use pure white as the page background — Paper is always the backdrop
- Don't add gradient fills, glassmorphism, or backdrop blurs — Things is flat color + shadow
- Don't darken buttons on hover — use the subtle lift shadow instead
- Don't use cool blue-grays — the Things grays have a warmer cast
- Don't introduce a second accent color — blue is the only chromatic voice
- Don't use pill (`{rounded.pill}`) radius on buttons — the Apple-native 7.6px is specific
- Don't use heavy drop shadows — the signature is restraint
- Don't use custom web fonts — `ui-sans-serif` IS the font
- Don't use letter-spacing tricks — SF Pro is self-spacing
- Don't stack too many elevation levels — Level 0, Level 2, and Level 5 cover 90% of cases

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile XS | <340px | Minimum layout, single column, compact padding |
| Mobile | 340–479px | Single column, 48–56px vertical section spacing |
| Mobile Large | 480–620px | Slightly roomier padding, single column |
| Tablet | 620–899px | 2-column grids begin (testimonials), condensed nav |
| Small Desktop | 899–1002px | 3-column grids, expanded nav |
| Desktop | 1002–1106px | Full 4-column testimonial grid, 1106px max container |
| Large Desktop | ≥1106px | Centered content with generous side margins |

### Touch Targets
- Buttons: `7.12px × 16.96px` padding yields ~42px min tap height on mobile
- Nav links: 16px font with generous padding for thumb navigation
- Check-circle interactive area: always ≥ 44px hit zone
- Form inputs: 8px padding + 16px font = ~40px tap target

### Collapsing Strategy
- Navigation: horizontal link bar → hamburger toggle below tablet
- Testimonial grids: 4-col → 2-col → single
- Hero typography: 36px → 28px → 24px, weight 700 maintained
- Section spacing: 81px desktop → 48px mobile
- Card radius: 18px holds at all breakpoints
- Shadows: signature shadow holds at all breakpoints — non-negotiable

### Image Behavior
- Product screenshots maintain their own rounded corners
- Testimonial avatars: always 32px circular
- No art-direction breakpoint swaps
- Images inside cards clipped to match card radius

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Things Blue `{colors.primary}` (or softer `{colors.primary-soft}` for button fill)
- Page Background: Paper `{colors.background}`
- Card Surface: Pure White `{colors.surface}`
- Primary Text: Charcoal `{colors.ink}`
- Secondary Text: Blue-Gray `{colors.text-secondary}`
- Tertiary Text: Stone `{colors.text-tertiary}`
- Border: `{colors.border}`
- Focus Ring: `0 0 0 2px {colors.focus-ring}`
- Signature Shadow: `0 2px 8px {colors.shadow-soft}, 0 0 2px {colors.shadow-soft}`

### Example Component Prompts
- "Create a hero section on Paper (`{colors.background}`) with a headline at 36px `ui-sans-serif` weight 700, line-height 1.00, color Charcoal (`{colors.ink}`). Subtitle at 18px weight 400, line-height 1.35, color Blue-Gray (`{colors.text-secondary}`). Primary CTA: background `{colors.primary-soft}`, white text, 16.96px weight 700, padding `7.12px 16.96px`, radius 7.6px, signature shadow on hover."
- "Design a testimonial card on Pure White (`{colors.surface}`) with 18px border-radius and the signature Things shadow. Internal padding 27px. Quote text at 15.3px weight 400 Charcoal, attribution name at 15.3px weight 700, date at 13px weight 400 Stone."
- "Build an input field: 1px solid `{colors.border}`, 6.4px radius, 8px padding, 16px `ui-sans-serif` weight 400 Charcoal. Focus: border becomes transparent, box-shadow `0 0 0 2px {colors.focus-ring}`."
- "Create a check-circle: 20px diameter, 1.5px stroke `{colors.border}`, transparent fill. On checked state, fill becomes Things Blue (`{colors.primary}`) with white checkmark glyph, scale-bounce animation."
- "Design a nav bar: white background, 1px shadow bottom (`{colors.shadow-edge}`). Links at 16px weight 400 Charcoal, hover: underline. Primary CTA right-aligned using Things Blue button spec."

### Iteration Guide
1. Always start on the Paper canvas — never pure white
2. Use the signature dual-layer shadow on every elevated card
3. Weights are 400 / 600 / 700 only
4. Use the system font stack — custom fonts are a downgrade
5. Border-radius is graduated: 3px inline, 6–7.6px buttons, 10.8–12.8px panels, 18px featured
6. Button hover uses the subtle lift shadow, not color change
7. Button active uses `scale(0.95)`, not background darkening
8. The blue accent is sacred — primary CTAs, links, focus rings, check-circles
9. Focus is always the blue ring shadow at 50% opacity, never outline
10. Let the paper canvas breathe — generous section spacing is non-negotiable
