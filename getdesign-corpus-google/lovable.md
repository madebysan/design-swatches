---
version: alpha
name: Lovable
description: Warm parchment-toned canvas with Camera Plain Variable — humanist warmth, opacity-driven gray scale derived from charcoal, signature inset-shadow buttons, and warm border containment.

colors:
  # Base
  background: "#f7f4ed"
  surface: "#fcfbf8"
  ink: "#1c1c1c"
  on-primary: "#fcfbf8"

  # Borders / dividers
  border: "#eceae4"
  border-strong: "#a3a3a2"  # was rgba(28,28,28,0.4) over #f7f4ed — Google format requires hex

  # Charcoal opacity scale (opaque approximations on cream)
  charcoal-83: "#383837"  # was rgba(28,28,28,0.83) — Google format requires hex
  charcoal-82: "#3a3a39"  # was rgba(28,28,28,0.82) — Google format requires hex
  muted-gray: "#5f5f5d"
  charcoal-04: "#f0ede5"  # was rgba(28,28,28,0.04) over cream — Google format requires hex
  charcoal-03: "#f1eee7"  # was rgba(28,28,28,0.03) over cream — Google format requires hex

  # Interactive
  ring-blue: "#3b82f6"

  # Inset shadow approximations (opaque)
  inset-highlight: "#cccccc"  # was rgba(255,255,255,0.2) — Google format requires hex
  inset-dark: "#0a0a0a"  # was rgba(0,0,0,0.2) — Google format requires hex
  shadow-soft: "#e6e6e6"  # was rgba(0,0,0,0.05) on cream — Google format requires hex
  shadow-focus: "#cccccc"  # was rgba(0,0,0,0.1) — Google format requires hex

typography:
  display-hero:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -1.5px
  display-alt:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 480
    lineHeight: 1.00
    letterSpacing: 0px
  section-heading:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.00
    letterSpacing: -1.2px
  sub-heading:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -0.9px
  card-title:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0px
  body:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button-small:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  caption:
    fontFamily: "Camera Plain Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px

spacing:
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 40px
  3xl: 56px
  4xl: 80px
  5xl: 96px
  6xl: 128px
  7xl: 176px

rounded:
  none: 0px
  sm: 4px
  md: 6px
  lg: 8px
  card: 12px
  container: 16px
  pill: 9999px

components:
  # Primary dark button — signature inset shadow
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 16px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"

  # Ghost / outlined
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 16px

  # Cream surface button
  button-surface:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 16px

  # Pill / icon button
  button-pill:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-small}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  # Card
  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.card}"
    padding: 24px
  card-large:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.container}"
    padding: 32px

  # Input
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 16px 24px

  # Suggestion pill (AI chat)
  suggestion-pill:
    backgroundColor: "{colors.background}"
    textColor: "{colors.muted-gray}"
    typography: "{typography.button-small}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
---

# Lovable Design System

## Overview

Lovable's website radiates warmth through restraint. The entire page sits on a creamy, parchment-toned background (`{colors.background}`) that immediately separates it from the cold-white conventions of most developer tool sites. This isn't minimalism for minimalism's sake — it's a deliberate choice to feel approachable, almost analog, like a well-crafted notebook. The near-black text (`{colors.ink}`) against this warm cream creates a contrast ratio that's easy on the eyes while maintaining sharp readability.

The custom Camera Plain Variable typeface is the system's secret weapon. Unlike geometric sans-serifs that signal "tech company," Camera Plain has a humanist warmth — slightly rounded terminals, organic curves, and a comfortable reading rhythm. At display sizes (48px–60px), weight 600 with aggressive negative letter-spacing (-0.9px to -1.5px) compresses headlines into confident, editorial statements. The font uses `ui-sans-serif, system-ui` as fallbacks, acknowledging that the custom typeface carries the brand personality.

What makes Lovable's visual system distinctive is its opacity-driven depth model. Rather than using a traditional gray scale, the system modulates `{colors.ink}` at varying opacities to create a unified tonal range. Every shade of gray on the page is technically the same hue — just more or less transparent. This creates a visual coherence that's nearly impossible to achieve with arbitrary hex values. The border system follows suit: `{colors.border}` for light divisions and `{colors.border-strong}` for stronger interactive boundaries.

**Key Characteristics:**
- Warm parchment background (`{colors.background}`) — not white, not beige, a deliberate cream
- Camera Plain Variable typeface with humanist warmth and editorial letter-spacing at display sizes
- Opacity-driven color system: all grays derived from `{colors.ink}` at varying transparency levels
- Inset shadow technique on buttons (white highlight top + dark ring inset)
- Warm neutral border palette: `{colors.border}` for subtle, `{colors.border-strong}` for interactive
- Full-pill radius (`{rounded.pill}`) used extensively for action buttons and icon containers
- Focus state uses soft warm shadow for emphasis
- shadcn/ui + Radix UI component primitives with Tailwind CSS utility styling

## Colors

### Primary
- **Cream** (`{colors.background}`): Page background, card surfaces, button surfaces — warm, paper-like, human
- **Charcoal** (`{colors.ink}`): Primary text, headings, dark button backgrounds — not pure black
- **Off-White** (`{colors.surface}`): Button text on dark backgrounds, subtle highlight

### Neutral Scale (Opacity-Based)
- **Charcoal 83%** (`{colors.charcoal-83}`): Strong secondary text
- **Charcoal 82%** (`{colors.charcoal-82}`): Body copy
- **Muted Gray** (`{colors.muted-gray}`): Secondary text, descriptions, captions
- **Charcoal 4%** (`{colors.charcoal-04}`): Subtle hover backgrounds, micro-tints
- **Charcoal 3%** (`{colors.charcoal-03}`): Barely-visible overlays

### Surface & Border
- **Light Cream** (`{colors.border}`): Card borders, dividers, image outlines — the warm divider line
- **Cream Surface** (`{colors.background}`): Card backgrounds, section fills

### Interactive
- **Ring Blue** (`{colors.ring-blue}`): Tailwind focus ring
- **Focus Shadow** (`{colors.shadow-focus}`): Focus and active state shadow — soft, warm, diffused

## Typography

### Font Family
- **Primary**: `Camera Plain Variable`, fallbacks `ui-sans-serif, system-ui`
- **Weight range**: 400 (body/reading), 480 (special display), 600 (headings/emphasis)
- **Feature**: Variable font with continuous weight axis

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens (`{typography.display-hero}`, `{typography.body}`) directly.

| Token | Use |
|---|---|
| `display-hero` | 60px maximum impact, weight 600 |
| `display-alt` | 60px lighter hero variant, weight 480 |
| `section-heading` | 48px feature section titles |
| `sub-heading` | 36px sub-sections |
| `card-title` | 20px card headings |
| `body-large` | 18px introductions |
| `body` | 16px standard reading |
| `button` | 16px button labels |
| `button-small` | 14px compact buttons |
| `caption` | 14px metadata |

### Principles
- **Warm humanist voice**: Camera Plain's slightly rounded terminals contrast with the sharp geometric sans-serifs of most developer tools.
- **Variable weight as design tool**: continuous weight values (e.g., 480) enable nuanced hierarchy beyond standard stops.
- **Compression at scale**: headlines use negative letter-spacing (-0.9px to -1.5px) for editorial impact.
- **Two weights, clear roles**: 400 (body/UI/links/buttons) and 600 (headings/emphasis).

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is **8px**, with the scale expanding generously at the top end — sections use `5xl`–`7xl` vertical spacing for editorial breathing room.

### Grid & Container
- Max content width: ~1200px (centered)
- Hero: centered single-column with massive vertical padding
- Feature sections: 2–3 column grids
- Full-width footer with multi-column link layout

### Whitespace Philosophy
- **Editorial generosity**: spacing is lavish at section boundaries (`5xl`–`7xl`). The warm cream background makes these expanses feel cozy rather than empty.
- **Content-driven rhythm**: tight internal spacing within cards (`sm`–`lg`) contrasts with wide section gaps.
- **Section separation**: footer uses 1px `{colors.border}` and 16px radius. Sections defined by generous spacing rather than border lines.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, cream background | Page surface, most content |
| Bordered (Level 1) | `1px solid {colors.border}` | Cards, images, dividers |
| Inset (Level 2) | `inset 0 0.5px 0 {colors.inset-highlight}, inset 0 0 0 0.5px {colors.inset-dark}, 0 1px 2px {colors.shadow-soft}` | Dark buttons, primary actions |
| Focus (Level 3) | `0 4px 12px {colors.shadow-focus}` | Active/focus states |
| Ring (Accessibility) | 2px ring `{colors.ring-blue}` | Keyboard focus on inputs |

**Shadow Philosophy**: Lovable's depth system is intentionally shallow. Instead of floating cards with dramatic drop-shadows, the system relies on warm borders against the cream surface. The only notable shadow pattern is the inset shadow on dark buttons — a multi-layer technique where a white highlight line sits at the top edge while a dark ring and soft drop handle the bottom. This creates a tactile, pressed-into-surface feeling rather than a hovering-above-surface feeling.

### Decorative Depth
- Hero: soft, warm multi-color gradient wash (pinks, oranges, blues) behind hero — atmospheric, barely visible
- Footer: gradient background with warm tones transitioning to the bottom
- No harsh section dividers — spacing and background warmth handle transitions

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Sharp inline elements (rare) |
| `sm` | 4px | Small interactive elements |
| `md` | 6px | Buttons, inputs, navigation menu |
| `lg` | 8px | Compact cards, divs |
| `card` | 12px | Standard cards, image containers |
| `container` | 16px | Large containers, footer sections |
| `pill` | 9999px | Action pills, icon buttons, toggles |

## Components

The complete component spec lives in the `components:` token block above. Reference components directly (`{components.button-primary}`, `{components.card}`).

### Buttons
- **`button-primary`** — charcoal fill with off-white text and the signature multi-layer inset shadow.
- **`button-ghost`** — transparent fill with strong border for secondary actions.
- **`button-surface`** — cream surface with no border for tertiary/toolbar actions.
- **`button-pill`** — full-pill action toggle (plan mode, voice recording).

### Cards
- **`card`** — cream surface with 1px warm border, 12px radius, no box-shadow.
- **`card-large`** — 16px radius for larger containers.

### Inputs
- **`input`** — cream surface, 1px warm border, 6px radius. Focus uses a 2px Ring Blue outline.

### Navigation
- **`nav-bar`** — clean horizontal nav on cream, fixed. Logo left, links and dark CTA right.

### AI Chat / Suggestion
- **`suggestion-pill`** — full pill with warm border, used in the AI chat input area.

## Do's and Don'ts

### Do
- Use the warm cream background (`{colors.background}`) as the page foundation
- Use Camera Plain Variable at display sizes with negative letter-spacing (-0.9px to -1.5px)
- Derive all grays from `{colors.ink}` at varying opacity levels for tonal unity
- Use the inset shadow technique on dark buttons for tactile depth
- Use `{colors.border}` borders instead of shadows for card containment
- Keep the weight system narrow: 400 for body/UI, 600 for headings
- Use full-pill radius only for action pills and icon buttons
- Apply opacity 0.8 on active states for responsive tactile feedback

### Don't
- Don't use pure white as a page background — the cream is intentional
- Don't use heavy box-shadows for cards — borders are the containment mechanism
- Don't introduce saturated accent colors — the palette is intentionally warm-neutral
- Don't use weight 700 (bold) — 600 is the maximum
- Don't apply 9999px radius on rectangular buttons — pills are for icon/action toggles
- Don't use sharp focus outlines — the system uses soft shadow-based focus indicators
- Don't mix border styles
- Don't increase letter-spacing on headings — Camera Plain is designed to run tight at scale

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile Small | <600px | Tight single column, reduced padding |
| Mobile | 600–640px | Standard mobile layout |
| Tablet Small | 640–700px | 2-column grids begin |
| Tablet | 700–768px | Card grids expand |
| Desktop Small | 768–1024px | Multi-column layouts |
| Desktop | 1024–1280px | Full feature layout |
| Large Desktop | 1280–1536px | Maximum content width, generous margins |

### Touch Targets
- Buttons: 8px 16px padding (comfortable touch)
- Navigation: adequate spacing between items
- Pill buttons: 9999px radius creates large tap-friendly targets
- Menu toggle: 6px radius button with adequate sizing

### Collapsing Strategy
- Hero: 60px → 48px → 36px headline scaling with proportional letter-spacing
- Navigation: horizontal links → hamburger menu at 768px
- Feature cards: 3-column → 2-column → single column stacked
- Template gallery: grid → stacked vertical cards
- Stats bar: horizontal → stacked vertical
- Footer: multi-column → stacked single column
- Section spacing: 128px+ → 64px on mobile

### Image Behavior
- Template screenshots maintain 1px `{colors.border}` border at all sizes
- 12px border radius preserved across breakpoints
- Gallery images responsive with consistent aspect ratios
- Hero gradient softens/simplifies on mobile

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Charcoal (`{colors.ink}`)
- Background: Cream (`{colors.background}`)
- Heading text: Charcoal (`{colors.ink}`)
- Body text: Muted Gray (`{colors.muted-gray}`)
- Border: `{colors.border}` (passive), `{colors.border-strong}` (interactive)
- Focus: `{colors.shadow-focus}` glow
- Button text on dark: `{colors.on-primary}`

### Example Component Prompts
- "Create a hero section on cream background (`{colors.background}`). Headline at 60px Camera Plain Variable weight 600, line-height 1.10, letter-spacing -1.5px, color `{colors.ink}`. Subtitle at 18px weight 400, line-height 1.38, color `{colors.muted-gray}`. Dark CTA button (`{colors.ink}` bg, `{colors.on-primary}` text, 6px radius, 8px 16px padding, inset shadow) and ghost button."
- "Design a card on cream (`{colors.background}`) background. Border: 1px solid `{colors.border}`. Radius 12px. No box-shadow. Title at 20px Camera Plain Variable weight 400, color `{colors.ink}`. Body at 14px weight 400, color `{colors.muted-gray}`."
- "Build a template gallery: grid of cards with 12px radius, 1px solid `{colors.border}` border, cream backgrounds. Each card: image with 12px top radius, title below."
- "Create navigation: sticky on cream (`{colors.background}`). Camera Plain 16px weight 400 for links, `{colors.ink}` text. Dark CTA button right-aligned with inset shadow."
- "Design a stats section: large numbers at 48px Camera Plain weight 600, letter-spacing -1.2px, `{colors.ink}`. Labels below at 16px weight 400, `{colors.muted-gray}`. Horizontal layout with 32px gap."

### Iteration Guide
1. Always use cream (`{colors.background}`) as the base — never pure white
2. Derive grays from `{colors.ink}` at opacity levels rather than using distinct hex values
3. Use `{colors.border}` borders for containment, not shadows
4. Letter-spacing scales with size: -1.5px at 60px, -1.2px at 48px, -0.9px at 36px, normal at 16px
5. Two weights: 400 (everything except headings) and 600 (headings)
6. The inset shadow on dark buttons is the signature detail — don't skip it
7. Camera Plain Variable at weight 480 is for special display moments only
