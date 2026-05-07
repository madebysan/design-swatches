---
version: alpha
name: HeroUI
description: NextUI's v3 refresh — confident, color-celebrating React UI library with electric blue brand, vibrant purple secondary, full-pill chips, and a six-role semantic color system.

colors:
  # Base
  background: "#ffffff"
  surface: "#f9f9f9"
  ink: "#171717"
  ink-card: "#0a0a0a"
  on-primary: "#ffffff"

  # Semantic — primary (electric blue)
  primary: "#006fee"
  primary-100: "#dbeeff"
  primary-900: "#003663"

  # Semantic — secondary (vibrant purple)
  secondary: "#7828c8"
  secondary-100: "#f2eafa"
  secondary-900: "#300c4f"

  # Semantic — success (emerald)
  success: "#17c964"
  success-100: "#e8faf0"
  success-900: "#095028"

  # Semantic — warning (amber)
  warning: "#f5a524"
  warning-100: "#fefce8"
  warning-900: "#62420e"

  # Semantic — danger (red-pink)
  danger: "#f31260"
  danger-100: "#fee7ef"
  danger-900: "#610726"

  # Default neutral scale
  default-200: "#f4f4f5"
  default-500: "#71717a"
  default-900: "#18181b"

  # Borders / dividers
  divider: "#e5e5e5"

  # Focus
  focus: "#006fee"

  # Shadow tints (opaque approximations)
  shadow-sm: "#f5f5f5"  # was rgba(0,0,0,0.04) — Google format requires hex
  shadow-md: "#ebebeb"  # was rgba(0,0,0,0.08) — Google format requires hex
  shadow-lg: "#dedede"  # was rgba(0,0,0,0.12) — Google format requires hex

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: -1.2px
  h1:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.9px
  h2:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0px
  h3:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.56
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  label:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  code:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  2xl: 24px
  3xl: 32px

rounded:
  none: 0px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  card: 14px
  pill: 9999px

components:
  # Primary button — solid electric blue
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: 6px 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-900}"
    textColor: "{colors.on-primary}"

  # Bordered (outline) button
  button-bordered:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 6px 16px

  # Light (ghost) button
  button-light:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 6px 16px

  # Flat (soft tinted) button
  button-flat:
    backgroundColor: "{colors.primary-100}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 6px 16px

  # Card — bordered, white
  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.card}"
    padding: 24px
  card-hover:
    backgroundColor: "{colors.surface}"

  # Input — bordered
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  input-flat:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Chip — full pill, HeroUI's signature badge
  chip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
    padding: 3px 10px
  chip-flat:
    backgroundColor: "{colors.primary-100}"
    textColor: "{colors.primary}"
    rounded: "{rounded.pill}"
    padding: 3px 10px

  # Tab container — pill background
  tabs:
    backgroundColor: "{colors.default-200}"
    rounded: "{rounded.pill}"
    padding: 4px
  tab-active:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"

  # Switch — pill track
  switch-on:
    backgroundColor: "{colors.success}"
    rounded: "{rounded.pill}"
  switch-off:
    backgroundColor: "{colors.divider}"
    rounded: "{rounded.pill}"
---

# HeroUI Design System

## Overview

HeroUI is the v3 refresh of NextUI — rebranded, re-tokened, re-energized. The homepage is a confident showcase of components with saturated brand color (`{colors.primary}` electric blue), vibrant secondary (`{colors.secondary}` purple), and a full-pill radius culture that runs through buttons, tabs, and badges. Where shadcn restrains and Park UI neutralizes, HeroUI **celebrates** — colors, curves, and the polished confidence of a library that expects its components to appear on landing pages, not just admin panels.

Typography is **Inter** across the system — no custom typeface, no experimental weight. Inter weight 700 at 48px with `-1.2px` tracking for hero display, weight 600 for UI text, weight 400 for body. The restraint here is deliberate: HeroUI wants the color system to be the brand voice, and neutral typography keeps attention on the chromatic palette.

The defining move is HeroUI's **semantic color system with full scales**. Six roles (default, primary, secondary, success, warning, danger), each with a 50–900 scale, each WCAG-AA verified. Components accept `color="primary"` as a prop, resolving to the full theme scale at runtime. This is NextUI's legacy refined — Tailwind Variants as the styling engine, React Aria as the accessibility primitives.

**Key Characteristics:**
- Inter as the sole typeface — weight 700 at display, weight 600 for UI
- Electric blue brand (`{colors.primary}`) with vibrant purple secondary (`{colors.secondary}`)
- `12px` / `14px` radii dominant — generous, friendly
- Full-pill radius (`{rounded.pill}`) used liberally — tabs, chips, some buttons
- Six semantic color roles each with full 50–900 scales
- Built on React Aria + Tailwind Variants + Framer Motion
- v3 is a breaking redesign from NextUI (not a patch upgrade)
- Dark mode is a first-class theme, not an afterthought

## Colors

### Semantic Roles
Each role exposes a 50–900 scale; the 500 step is the role's anchor.
- **default**: Neutral gray scale — `{colors.default-200}` → `{colors.default-500}` → `{colors.default-900}`
- **primary**: Electric blue — `{colors.primary-100}` → `{colors.primary}` → `{colors.primary-900}`
- **secondary**: Vibrant purple — `{colors.secondary-100}` → `{colors.secondary}` → `{colors.secondary-900}`
- **success**: Emerald — `{colors.success-100}` → `{colors.success}` → `{colors.success-900}`
- **warning**: Amber — `{colors.warning-100}` → `{colors.warning}` → `{colors.warning-900}`
- **danger**: Red-pink — `{colors.danger-100}` → `{colors.danger}` → `{colors.danger-900}`

### Base
- **Background** (`{colors.background}`): Page canvas.
- **Foreground** (`{colors.ink}`): Primary text.
- **Card** (`{colors.background}`): Card surface, with card foreground at `{colors.ink-card}`.
- **Divider** (`{colors.divider}`): Hairline borders.
- **Focus** (`{colors.focus}`): Focus ring color (primary anchor).

## Typography

### Font Family
- **Primary**: `Inter`, fallback: `ui-sans-serif, system-ui, sans-serif`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, monospace`
- HeroUI ships fonts via `next/font` — preloaded, swap behavior tuned

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`).

| Token | Use |
|---|---|
| `display-hero` | Maximum size — landing hero statements |
| `h1` | Major page headers |
| `h2` | Section headings |
| `h3` | Sub-section heads |
| `body-large` | Intro paragraphs, emphasized body text |
| `body` | Standard reading text |
| `label` | UI labels, emphasized small text |
| `caption` | Small metadata, helper text |
| `code` | Inline code, monospace |

### Principles
- **Weight 700 for display, weight 600 for UI**: clean two-weight hierarchy, minimal in-between.
- **Negative tracking at display**: `-1.2px` at 48px, lighter below — less aggressive than shadcn but more than Material.
- **No custom typeface**: Inter handles everything; HeroUI commits fully to Inter rather than branded typography.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is **4px** (Tailwind-aligned). Dominant values are `xs` (4px), `md` (8px), and `lg` (12px) — slightly denser than Material, comparable to shadcn.

### Grid & Container
- 12-column via Tailwind
- Max width: ~1280px
- Gutter: 16–24px

### Whitespace Philosophy
HeroUI's spacing is product-density-friendly, not editorial. Sections use `2xl`–`3xl` separations rather than the lavish `5xl`+ gaps of brand-led marketing systems. Components feel "Tailwind-aligned" — predictable, comfortable, and never overly airy.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Cards default |
| sm (Level 1) | `0 2px 4px {colors.shadow-sm}` | Card rest |
| md (Level 2) | `0 4px 12px {colors.shadow-md}` | Dropdowns, cards hover |
| lg (Level 3) | `0 8px 30px {colors.shadow-lg}` | Modals, featured cards |
| xl (Level 4) | `0 20px 50px {colors.shadow-lg}` | Modal dialogs |

**Shadow Philosophy**: HeroUI uses a 4-level shadow scale borrowed from Tailwind's defaults with slightly softer edges. Shadows are neutral (no color tinting) and applied sparingly — most components sit flat with a `1px` border, reserving shadows for floating/interactive elements.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Sharp inline elements (rare) |
| `sm` | 8px | Small buttons, chips |
| `md` | 12px | Buttons, inputs — the HeroUI default |
| `card` | 14px | Cards |
| `lg` | 16px | Comfortable cards, dropdowns |
| `xl` | 20px | Featured cards, modals |
| `pill` | 9999px | Chips, switches, tab containers — liberal use |

## Components

The complete component spec lives in the `components:` token block above. Reference components directly (`{components.button-primary}`, `{components.chip}`).

### Buttons
- **`button-primary`** — solid electric blue, 12px radius, the canonical CTA.
- **`button-bordered`** — 1px outline, transparent fill, primary text.
- **`button-light`** — ghost, no background, primary text.
- **`button-flat`** — soft-tinted background using the role's `-100` scale step.

Size variants: sm (32px), md (40px — default), lg (48px). Radius variants: none, sm, md, lg, full.

### Cards
- **`card`** — white surface, 1px divider border, 14px radius, 24px padding.
- Hover: shifts to `{colors.surface}` background and increases shadow by one level.

### Inputs
- **`input`** — bordered variant, white surface, 12px radius.
- **`input-flat`** — surface-tinted, no border.
- Underlined variant uses a 2px bottom border only.
- Focus: primary border with a soft tinted ring.

### Chips (HeroUI's branded badges)
- **`chip`** — full pill, solid color background with white text.
- **`chip-flat`** — full pill, role `-100` background with role-anchor text.

### Tabs
- **`tabs`** — pill-shaped container with a tinted default background.
- **`tab-active`** — white background with subtle shadow lift.

### Switches
- **`switch-on`** / **`switch-off`** — pill track, 44×24px default. Track color shifts from neutral to success on activation.

## Do's and Don'ts

### Do
- Use semantic color props (`color="primary"`) — never hardcoded hex
- Default to `{rounded.md}` (12px) for buttons, `{rounded.card}` (14px) for cards
- Use full-pill radius on chips, switches, and tabs containers
- Use Inter weight 700 for display, weight 600 for UI, weight 400 for body
- Pair the primary electric blue with the vibrant purple secondary when you need accent variety
- Use the shadow scale progressively (`sm` → `md` → `lg`) for elevation hierarchy

### Don't
- Don't override individual theme colors — swap the theme object instead
- Don't use weight 800+ for display — HeroUI is weight 700 maxed
- Don't mix Material or Carbon radii — HeroUI's rhythm is `12 / 14 / 16 / full`
- Don't use custom icon sets that conflict with the Solar Duotone default
- Don't skip `radius="full"` on chips — pill shape is the brand

---

## Responsive Behavior

### Breakpoints (Tailwind)
| Name | Width | Changes |
|---|---|---|
| sm | `640px+` | 2-column layouts |
| md | `768px+` | 3-column features |
| lg | `1024px+` | Full desktop, tab bars horizontal |
| xl | `1280px+` | Max content applies |

### Touch Targets
- `sm` button (32px) — minimum for touch
- `md` button (40px) — default for desktop + touch
- Icon buttons: `40px × 40px`

### Collapsing Strategy
- Hero: 48px → 36px → 30px
- Horizontal tabs → vertical list or dropdown on mobile
- Cards: 3-col → 2-col → stacked
- Modal widths: centered → full-sheet on mobile

---

## Agent Prompt Guide

### Quick Color Reference
- Primary: `{colors.primary}` (electric blue)
- Secondary: `{colors.secondary}` (vibrant purple)
- Success: `{colors.success}` (emerald)
- Warning: `{colors.warning}` (amber)
- Danger: `{colors.danger}` (red-pink)
- Foreground: `{colors.ink}`
- Divider: `{colors.divider}`
- Background: `{colors.background}`

### Example Component Prompts
- "Create a hero: white bg. Headline at 48px Inter weight 700, letter-spacing -1.2px, line-height 1.10, color `{colors.ink}`. Subtitle 18px weight 500 color `{colors.default-500}`. Primary button: `{colors.primary}` bg, white text, 12px radius, 10px 20px padding, 14px weight 600. Hover: 90% opacity overlay."
- "Design a card: white bg, 1px solid `{colors.divider}`, 14px radius, 24px padding, soft shadow. Title 20px Inter weight 600. Body 14px weight 400 color `{colors.default-500}`. Action chip (full pill, `{colors.primary}` bg, white text, 12px weight 500)."
- "Build a chip: 9999px radius, 3px 10px padding, 12px Inter weight 500. Variants: solid (color bg + white text), bordered (1px solid color + color text), flat (color `-100` bg + color text), dot (small colored circle + neutral text)."

### Iteration Guide
1. Think in semantic color props — `color="primary"` not hex
2. `12px` radius is the default for buttons/inputs; `9999px` for chips/switches
3. Inter weight 700 display, weight 600 UI, weight 400 body — no middle weight
4. Shadows are neutral; use scale progressively (sm/md/lg/xl)
5. For dark mode, HeroUI provides a pre-built dark theme — don't manually invert
6. Tab bars use `9999px` radius on the container; active tab gets white bg with subtle shadow
