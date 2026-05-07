---
version: alpha
name: DaisyUI
description: Friendly Tailwind plugin design system. Outfit weight 900 display, 36 OKLCH-based themes, semantic component classes, full-pill button radii, colorful-by-default celebration aesthetic.

colors:
  # Default (light) theme — semantic tokens
  primary: "#661ae6"
  on-primary: "#ffffff"
  secondary: "#d926a9"
  accent: "#1fb2a6"
  neutral: "#1d232a"

  # Base surfaces
  background: "#ffffff"     # base-100
  surface: "#f2f2f2"        # base-200
  surface-alt: "#e5e6e6"    # base-300 (borders/dividers)
  ink: "#1f2937"            # base-content (default text)

  # State colors
  info: "#3abff8"
  success: "#36d399"
  warning: "#fbbd23"
  error: "#f87272"

  # Cupcake theme sample
  cupcake-primary: "#65c3c8"
  cupcake-accent: "#eeaf3a"
  cupcake-bg: "#faf7f5"
  cupcake-content: "#291e00"

  # Dracula sample
  dracula-primary: "#ff79c6"
  dracula-bg: "#282a36"

  # Synthwave sample
  synthwave-primary: "#e779c1"
  synthwave-bg: "#2d1b69"

  # Retro sample
  retro-primary: "#ef9995"
  retro-bg: "#e4d8b4"

  # Shadow surrogate
  shadow-soft: "#f0f0f0"   # opaque approx of rgba(0,0,0,0.05) — Google format requires hex

typography:
  display-hero:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-large:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 900
    lineHeight: 1.10
    letterSpacing: -1.2px
  h1:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0px
  h2:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0px
  h3:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 0px
  body-large:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.50
    letterSpacing: 0px
  body:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0px
  caption:
    fontFamily: "Outfit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  code:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px
  5xl: 80px
  6xl: 120px

rounded:
  none: 0px
  sm: 8px
  md: 16px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 20px
  button-primary-hover:
    backgroundColor: "{colors.secondary}"
  button-outline:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 20px
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 20px
  button-ghost-hover:
    backgroundColor: "{colors.surface}"

  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.md}"
    padding: 24px
  card-compact:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.md}"
    padding: 12px

  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  input-primary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px

  badge-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 8px
  badge-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 8px
  badge-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 8px
  badge-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 8px

  alert:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 16px

  modal-box:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.md}"
    padding: 24px
---

# DaisyUI Design System

## Overview

DaisyUI is what happens when a Tailwind plugin decides to be friendly. The homepage is a kaleidoscope of themes with names like Cupcake, Valentine, Retro, and Synthwave — each one a complete palette (primary, secondary, accent, neutral, base) that swaps live via a single CSS variable change. The default aesthetic is playful: Outfit typeface at heavyweight 900 for display, saturated colors, full-pill button radii, and rounded corners everywhere. Where shadcn disappears into neutral and Stripe whispers through weight 300, DaisyUI announces itself — loud, colorful, and unashamed of it.

The typographic choice is **Outfit** — a geometric sans-serif with an unusual weight range (100-900). At display sizes it runs at weight 900 with slight negative tracking; at body sizes it drops to 400. No variable font axes are used; weights are discrete. The pairing is `ui-monospace` for code blocks and `system-ui` for the occasional system-native element. Icons are font-agnostic — the docs use Lucide, Heroicons, or any SVG set, whatever the user prefers.

The defining move is the **theme system**. 36 built-in themes, each defined as a set of OKLCH color variables scoped to a `[data-theme]` attribute. Components reference `bg-primary`, `text-primary-content`, `bg-accent` — semantic names that resolve to whatever the active theme says. Swap the theme attribute, every component updates. This is CSS theming taken to its logical end: not a dark mode toggle, but a full personality switch.

**Key Characteristics:**
- Outfit as primary typeface, weight 900 for display — playful, heavy, geometric
- 36 built-in themes (Cupcake, Dracula, Synthwave, Retro, etc.) as OKLCH palettes
- Semantic component classes (`btn`, `btn-primary`, `card`) on top of Tailwind utilities
- Full-pill button radius (`{rounded.pill}`) by default — rounded, friendly
- Colorful-by-default — saturated primaries, accent colors, celebration aesthetic
- Zero dependencies on Tailwind utility components — pure CSS layer
- OKLCH color space throughout — perceptually uniform, theme-swap-safe

## Colors

DaisyUI's palette isn't a fixed set of hex values — it's a **semantic token system** that resolves per theme. The default (light) theme tokens live in YAML.

### Semantic Roles
- **Primary** (`{colors.primary}`): Main brand color, primary buttons, active links.
- **On Primary** (`{colors.on-primary}`): Text on primary surfaces.
- **Secondary** (`{colors.secondary}`): Secondary brand, accent buttons.
- **Accent** (`{colors.accent}`): Tertiary highlight, notification dots, selected chip borders.
- **Neutral** (`{colors.neutral}`): Default text, footer background in light themes.
- **Background** (`{colors.background}`): Primary page background (base-100).
- **Surface** (`{colors.surface}`): Alternate surface (base-200) for cards, inputs.
- **Surface Alt** (`{colors.surface-alt}`): Borders, dividers (base-300).
- **Ink** (`{colors.ink}`): Default text on base surfaces (base-content).

### State Colors
- **Info** (`{colors.info}`): Info alerts, help text highlights.
- **Success** (`{colors.success}`): Confirmation badges, success alerts.
- **Warning** (`{colors.warning}`): Caution states, yellow alerts.
- **Error** (`{colors.error}`): Destructive actions, error alerts.

### Theme Variations
- **cupcake**: Soft pastels — primary `{colors.cupcake-primary}` teal, accent `{colors.cupcake-accent}` gold, bg `{colors.cupcake-bg}`.
- **dracula**: Dark mode purple — primary `{colors.dracula-primary}` magenta on `{colors.dracula-bg}` canvas.
- **synthwave**: Retro neon — primary `{colors.synthwave-primary}` pink on `{colors.synthwave-bg}` deep purple.
- **retro**: Warm vintage — primary `{colors.retro-primary}` coral on `{colors.retro-bg}` cream.

DaisyUI is fully OKLCH-native in source — over 7,000 `oklch()` references and 1,000+ `oklab()` overlays. Black is used sparingly, mostly for borders in dark themes. The colors above are opaque sRGB approximations of the published default palette suitable for static handoff.

## Typography

### Font Family
- **Primary**: `Outfit`, fallback `ui-sans-serif, system-ui, sans-serif`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, monospace`
- **System (docs chrome)**: `ui-sans-serif, system-ui, sans-serif`

### Hierarchy

| Token | Use |
|---|---|
| `display-hero` | Maximum hero — 72px Outfit weight 900 with `-1.5px` tracking |
| `display-large` | Section hero — 64px weight 900 |
| `h1`/`h2`/`h3` | Standard heading scale, weight 700 |
| `body-large` | Intros, lead paragraphs |
| `body` | Standard reading text |
| `button` | Button labels (weight 600) |
| `caption` | Metadata, fine print |
| `code` | Monospace code blocks |

### Principles
- **Weight 900 as the display signature**: Outfit at weight 900 is the brand's most recognizable typographic choice — fully drawn letterforms, maximum presence.
- **Weight 300 for light display accents**: Some theme variants use weight 300 for a softer, retro-inspired display treatment.
- **Conservative letter-spacing**: DaisyUI doesn't lean on tight tracking — display sizes use `-1.5px` at most, below 24px tracking stays at normal.
- **Mono for code only**: Unlike systems that use mono for timestamps and data, DaisyUI reserves monospace for code blocks and inline `<code>`.

## Layout

### Spacing System
Base unit is **4px** (Tailwind-aligned). Dominant values are `xs` (4px), tight micro-gaps, and `sm`–`lg` (8–16px) for content spacing. The complete scale lives in the `spacing:` token block above. DaisyUI uses Tailwind's spacing scale exactly — nothing custom.

### Grid & Container
- 12-column grid via Tailwind
- `container mx-auto` with `max-width: 1280px` as the default marketing container
- Docs layout: 256px sidebar + content column

### Whitespace
- **Generous padding inside cards**: 24px default, 12px on compact variants
- **Bold section rhythm**: 80–120px between homepage sections (`5xl`–`6xl`), 32–48px between card rows (`2xl`–`3xl`)
- **Full-pill buttons breathe**: button padding (10px 20px) accommodates the pill shape without crowding text

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow | Backgrounds, inline elements |
| Subtle | Soft shadow `{colors.shadow-soft}` | Cards at rest |
| Hover | Slightly stronger soft shadow | Card hover state |
| Modal | Pronounced soft shadow | Modals, elevated dropdowns |

**Shadow Philosophy**: DaisyUI's shadows are soft and small — they add the impression of lift without obscuring the bright colors underneath. Per theme, shadow intensity adjusts: dark themes use a subtle white inner shadow for lift, light themes use a soft black outer shadow.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Avoided almost everywhere — DaisyUI is rounded by default |
| `sm` | 8px | Inputs, small cards, code blocks |
| `md` | 16px | Cards, modals, larger surfaces |
| `pill` | 9999px | Buttons, badges, avatars, switches — the default for interactive elements |

DaisyUI is rounded-first — interactive elements default to pill, surfaces to comfortable mid-radii.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly rather than reconstructing them.

### Button variants
- **`button-primary`** — Filled primary CTA, pill radius. Uses `{colors.primary}`.
- **`button-outline`** — Transparent surface with primary-colored border, pill radius.
- **`button-ghost`** — No background until hover, pill radius. Tertiary actions.

### Cards
- **`card`** — Standard panel: 24px padding, `{rounded.md}`, light shadow.
- **`card-compact`** — Tighter 12px padding for dense layouts.

### Inputs
- **`input`** — Standard text field, `{rounded.sm}` (8px) radius.
- **`input-primary`** — Same structure with primary-colored focus accents.

### Badges
- **`badge-primary` / `badge-success` / `badge-warning` / `badge-error`** — All pill-shaped, semantic-color-driven.

### Alerts
- **`alert`** — Surface background with semantic accent. 16px padding, `{rounded.md}`.

### Modals
- **`modal-box`** — Background panel for modal content, generous 24px padding, `{rounded.md}`.

## Do's and Don'ts

### Do
- Use semantic classes (`btn-primary`, `card`, `badge-success`) — never hardcoded colors
- Use pill radius (`{rounded.pill}`) for buttons and badges — the brand voice
- Pick a theme and let the semantic variables do the work — don't override individual components
- Use Outfit weight 900 for hero displays — the signature
- Use OKLCH color values if extending the theme — stays perceptually uniform

### Don't
- Don't hardcode hex colors in components — break the theme system
- Don't use border-radius values between 0–6px on interactive elements — DaisyUI is rounded by default
- Don't override semantic tokens per-component — change the theme instead
- Don't mix Outfit with Inter — keep the geometric personality consistent
- Don't use weight 800 for display — go to 900 for full impact

---

## Responsive Behavior

### Breakpoints (Tailwind)
| Name | Width | Changes |
|---|---|---|
| sm | `640px+` | 2-column card grids |
| md | `768px+` | 3-column features, horizontal nav |
| lg | `1024px+` | Full desktop layout, sidebar docs |
| xl | `1280px+` | Max content width applies |

### Touch Targets
- Button `sm` (32px) is the minimum for taps
- Badge radius accommodates single-tap confirmation
- Drawer triggers `44px × 44px` — accessibility floor

### Collapsing Strategy
- Hero: 72px → 48px → 36px across breakpoints, weight 900 maintained
- Nav: horizontal links → hamburger drawer on mobile
- Cards: 3-col → 2-col → single column stacked

---

## Agent Prompt Guide

### Quick Color Reference (cupcake theme)
- Primary: `{colors.cupcake-primary}` (teal)
- Accent: `{colors.cupcake-accent}` (gold)
- Background: `{colors.cupcake-bg}` (warm white)
- Content text: `{colors.cupcake-content}` (dark brown)

### Example Component Prompts
- "Create a hero: base-100 background, Outfit 72px weight 900 letter-spacing -1.5px, content text. Subtitle at 18px weight 400. Primary button with `{colors.primary}`, `{rounded.pill}` radius, 12px padding, `{colors.on-primary}` text."
- "Design a card: `{colors.background}` background, soft shadow, `{rounded.md}` radius, 24px padding. Title at 24px Outfit weight 700 color `{colors.ink}`. Action button at bottom right — pill radius, `{colors.primary}` bg."
- "Build a badge: `{colors.success}` bg, ink text, 4px 8px padding, `{rounded.pill}` radius, 12px weight 500. Optional icon left at 14px."

### Iteration Guide
1. Pick a theme first, then compose components — the theme IS the design
2. Pill radius (`{rounded.pill}`) is the brand voice for interactive elements
3. Outfit weight 900 at display is non-negotiable for hero sections
4. Use semantic tokens, not hex — `{colors.primary}` over `bg-[#661ae6]`
5. Keep padding generous inside components; DaisyUI is friendly, not dense
6. For dark themes, use the provided theme variants (dracula, synthwave) — don't just invert
