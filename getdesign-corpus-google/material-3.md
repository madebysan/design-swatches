---
version: alpha
name: Material Design 3
description: Google's M3 Expressive — tactile, colorful, alive. 24px-dominant radii, signature purple #6442d6, Google Sans at the nonstandard weight 475, dual-layer elevation, dynamic color, fully-rounded FABs.

colors:
  # Primary (light)
  primary: "#6442d6"
  primary-container: "#f8f1f6"
  on-primary: "#ffffff"
  on-primary-container: "#21182b"

  # Primary (dark)
  primary-dark: "#9f86ff"
  primary-container-dark: "#4d2dcb"

  # Neutral / surface
  surface: "#ffffff"
  surface-variant: "#f8f1f6"
  on-surface: "#1c1b1d"
  on-surface-variant: "#4d4256"
  outline: "#dcdaf5"
  surface-dark: "#1f1f1f"

  # Accent / dynamic-derived
  secondary: "#6e5692"
  tertiary: "#825268"

  # Semantic
  error: "#b3261e"

  # Pure tokens (sourced from CSS vars)
  white: "#ffffff"
  black: "#000000"

  # Scrims (opaque approximations of rgba scrims)
  scrim-dark: "#5c5c5c"   # was rgba(31,31,31,0.64) — Google format requires hex
  scrim-light: "#c2c2c2"  # was rgba(255,255,255,0.24) — flattened approx
  scrim-light-soft: "#dedede"  # was rgba(255,255,255,0.12) — flattened approx

  # Common shadow / state-layer approximations
  shadow-key: "#4d4d4d"   # was rgba(0,0,0,0.3) — flattened approx
  shadow-ambient: "#d9d9d9"  # was rgba(0,0,0,0.15) — flattened approx
  state-layer-primary: "#ebe6fb"  # was rgba(100,66,214,0.08) — flattened over white

typography:
  display-large:
    fontFamily: "Google Sans, Roboto, system-ui, sans-serif"
    fontSize: 96px
    fontWeight: 475
    lineHeight: 1.0
    letterSpacing: 0px
  display-medium:
    fontFamily: "Google Sans, Roboto, system-ui, sans-serif"
    fontSize: 57px
    fontWeight: 475
    lineHeight: 1.12
    letterSpacing: 0px
  display-small:
    fontFamily: "Google Sans, Roboto, system-ui, sans-serif"
    fontSize: 45px
    fontWeight: 475
    lineHeight: 1.16
    letterSpacing: 0px
  headline-large:
    fontFamily: "Google Sans, Roboto, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 475
    lineHeight: 1.25
    letterSpacing: 0px
  headline-medium:
    fontFamily: "Google Sans, Roboto, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 475
    lineHeight: 1.29
    letterSpacing: 0px
  headline-small:
    fontFamily: "Google Sans, Roboto, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 475
    lineHeight: 1.33
    letterSpacing: 0px
  title-large:
    fontFamily: "Google Sans, Roboto, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0px
  title-medium:
    fontFamily: "Google Sans Text, Roboto, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  title-small:
    fontFamily: "Google Sans Text, Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  body-large:
    fontFamily: "Google Sans Text, Roboto, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-medium:
    fontFamily: "Google Sans Text, Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  body-small:
    fontFamily: "Google Sans Text, Roboto, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  label-large:
    fontFamily: "Google Sans Text, Roboto, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  label-medium:
    fontFamily: "Google Sans Text, Roboto, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0px
  label-small:
    fontFamily: "Google Sans Text, Roboto, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 48px
  5xl: 64px
  6xl: 96px
  7xl: 120px

rounded:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 28px
  switch: 32px
  pill: 9999px

components:
  # Buttons
  button-filled:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-large}"
    rounded: "{rounded.xl}"
    padding: 10px 24px
  button-filled-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  button-elevated:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.label-large}"
    rounded: "{rounded.xl}"
    padding: 10px 24px
  button-outlined:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.label-large}"
    rounded: "{rounded.xl}"
    padding: 10px 24px
  button-outlined-hover:
    backgroundColor: "{colors.state-layer-primary}"
    textColor: "{colors.primary}"
  button-text:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.label-large}"
    rounded: "{rounded.xl}"
    padding: 10px 12px
  button-text-hover:
    backgroundColor: "{colors.state-layer-primary}"
    textColor: "{colors.primary}"

  # FABs
  fab:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.on-primary-container}"
    rounded: "{rounded.pill}"
    padding: 16px
    size: 56px
  fab-extended:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.on-primary-container}"
    typography: "{typography.label-large}"
    rounded: "{rounded.lg}"
    padding: 16px 20px

  # Cards
  card-elevated:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.2xl}"
    padding: 16px
  card-filled:
    backgroundColor: "{colors.primary-container}"
    rounded: "{rounded.2xl}"
    padding: 16px
  card-outlined:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.2xl}"
    padding: 16px

  # Text fields
  input-outlined:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-large}"
    rounded: "{rounded.xs}"
    padding: 16px
  input-outlined-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
  input-filled:
    backgroundColor: "{colors.surface-variant}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-large}"
    rounded: "{rounded.xs}"
    padding: 16px

  # Chips
  chip:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-large}"
    rounded: "{rounded.sm}"
    padding: 0 16px
  chip-selected:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.on-primary-container}"
    typography: "{typography.label-large}"
    rounded: "{rounded.sm}"
    padding: 0 16px

  # Switches
  switch-track-off:
    backgroundColor: "{colors.outline}"
    rounded: "{rounded.pill}"
  switch-track-on:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.pill}"

  # Navigation
  app-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.title-large}"
    padding: 0 16px
  navigation-drawer:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.on-primary-container}"
    rounded: "{rounded.lg}"
    padding: 16px
  navigation-bar:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.on-primary-container}"
    typography: "{typography.label-medium}"
    padding: 12px 0

  # Dialogs / sheets
  dialog:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.3xl}"
    padding: 24px
  bottom-sheet:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.3xl}"
    padding: 24px
---

# Material Design 3 Design System

## Overview

Material Design 3 — and specifically the M3 Expressive refresh — is Google's thesis that software should feel tactile, colorful, and alive. Where shadcn erases itself and Stripe whispers through typography, M3 celebrates chrome. Large rounded corners (`{rounded.2xl}` is the dominant radius, used 31 times on the homepage), generous `{spacing.2xl}` units (the single most-used value on the page, appearing 49 times), and a signature purple (`{colors.primary}`) that serves as a brand anchor while the **dynamic color** system generates entire palettes from a user's wallpaper. The canvas alternates between pure white and a warm pink-blush (`{colors.primary-container}`) that Google calls a "primary container" — a tinted surface that carries brand atmosphere without demanding attention.

The typography is Google Sans at weight 475 — a nonstandard, distinctly Google weight that sits between book (400) and medium (500), softer than medium but with more presence than regular. At display sizes it scales to 96px with line-height 1.00 — gigantic, confident, and unapologetically friendly. Body text drops to Google Sans Text (a subtly different metric) at 16px weight 400 with 1.50 line-height. Icons are handled by **Google Symbols** — a variable font where weight, fill, and grade are all continuous axes, turning every icon into a piece of typography rather than a rasterized asset.

What truly distinguishes M3 is its **motion and elevation philosophy**. Shadows are subtle but always present — an elevation system codified into `elevation-0` through `elevation-5`, each with specific dual-layer shadows (a key shadow for directional depth + an ambient shadow for soft perimeter glow). Components don't just appear — they grow, fade, and spring with material-specific easing curves. The radius scale itself is an expressive device: switches are nearly circular (`{rounded.switch}`), FABs are fully rounded (`{rounded.pill}`), cards land at `{rounded.2xl}`, buttons at `{rounded.xs}`–`{rounded.xl}` depending on size class. Nothing is sharp. Nothing is flat. Everything has weight, rounded edges, and the sense that if you pressed it, it would respond.

**Key Characteristics:**
- Signature purple `{colors.primary}` (light) / `{colors.primary-dark}` (dark) as the primary brand anchor
- Google Sans at weight 475 — a nonstandard weight that IS the brand
- Google Symbols variable font for icons (weight + fill + grade axes)
- `{spacing.2xl}` as the dominant spacing + radius value — M3's proportional DNA
- Primary container `{colors.primary-container}` as a tinted surface for brand atmosphere
- Dynamic Color system — palettes generated algorithmically from a seed color
- Dual-layer shadow elevation: directional key + ambient perimeter
- Fully rounded FABs (`{rounded.pill}`) and pill switches (`{rounded.switch}`) — never sharp
- 5-level elevation system (0-5), each with named shadow values
- Expressive motion: spring curves, not linear transitions

## Colors

### Primary (Light Theme)
- **Primary Purple** (`{colors.primary}`): Primary brand color — used on CTAs, icons, active states. 51 occurrences on the homepage. A saturated but not neon purple.
- **Primary Container** (`{colors.primary-container}`): A pink-blush tinted surface for brand atmosphere. Used on large area backgrounds and card interiors that need to feel "on-brand" without shouting.
- **On Primary** (`{colors.on-primary}`): Text/icon color on the purple primary surface.
- **On Primary Container** (`{colors.on-primary-container}`): Text/icon color on the pink-blush container.

### Primary (Dark Theme)
- **Primary Purple Dark** (`{colors.primary-dark}`): Lighter, more luminous purple for dark contexts — defined as `--mio-theme-color-primary` in the scanned CSS.
- **Primary Container Dark** (`{colors.primary-container-dark}`): Deeper purple as container in dark mode.

### Neutral Scale
- **Surface** (`{colors.surface}`): Base light surface.
- **Surface Variant** (`{colors.surface-variant}`): Slightly warmer surface for differentiation.
- **On Surface** (`{colors.on-surface}`): Primary text color — warm near-black (370 occurrences make this the most-used color on the page).
- **On Surface Variant** (`{colors.on-surface-variant}`): Secondary text (96 occurrences) — a warm purple-tinged gray, not neutral gray.
- **Outline** (`{colors.outline}`): Border color with a soft lavender cast, tying borders to the brand palette.
- **Dark Surface** (`{colors.surface-dark}`): Near-black for dark-mode canvas.

### Accent & Support
- **Secondary / Tertiary**: M3's dynamic color system generates secondary (`{colors.secondary}` muted purple) and tertiary (`{colors.tertiary}` rose) palettes from the primary seed.
- **Error** (`{colors.error}`): Red for destructive/error states.
- **Success Green**: M3 does not ship a default success color — the system encourages teams to extend with custom role names.

### Scrim (overlays)
- `{colors.scrim-dark}` — dark scrim for modals/dialogs over content (was `rgba(31, 31, 31, 0.64)`)
- `{colors.scrim-light}` / `{colors.scrim-light-soft}` — light scrims for video controls

### CSS Variable Names (from scanned site)
- `--mio-theme-color-primary` (`{colors.primary-dark}` / dynamic)
- `--mio-theme-color-white` (`{colors.white}`)
- `--mio-theme-color-black` (`{colors.black}`)
- `--mio-theme-color-scrim-video-container` (`{colors.scrim-dark}`)

## Typography

### Font Family
- **Primary**: `Google Sans`, fallback: `Roboto`, `system-ui`, sans-serif
- **Body**: `Google Sans Text` (metric-matched sibling tuned for body readability)
- **Icons**: `Google Symbols` (variable font, features: `"liga"` enabled for ligature-based icon rendering)
- **Variable Font**: Google Sans ships with a custom weight axis — **475** is used extensively, a weight between regular (400) and medium (500) that does not exist in most fonts.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference each role via tokens (e.g. `{typography.display-large}`, `{typography.body-large}`).

| Token | Use |
|---|---|
| `display-large` | Homepage hero — maximum scale |
| `display-medium` | Feature hero |
| `display-small` | Section heads |
| `headline-large` | Page titles |
| `headline-medium` | Card titles |
| `headline-small` | Sub-headings |
| `title-large` | Prominent labels |
| `title-medium` | Button text, list item titles |
| `title-small` | Compact titles |
| `body-large` | Default body — most comfortable |
| `body-medium` | Secondary body, dense UI |
| `body-small` | Captions, metadata |
| `label-large` | Button labels, chips |
| `label-medium` | Tabs, badge labels |
| `label-small` | Smallest chrome labels |

### Principles
- **Weight 475 is the brand voice**: Not 400, not 500 — exactly 475. This is the weight that makes Google Sans feel like Google Sans, and it's non-negotiable at display/headline sizes.
- **Display vs Body is a family split, not just a size jump**: Google Sans for display/headline, Google Sans Text for body/labels. The metric difference is tuned for readability at small sizes.
- **No letter-spacing**: Unlike Stripe's tight tracking, M3 keeps tracking at normal across all sizes. Generosity over precision.
- **Google Symbols for icons**: Icons are rendered as ligatures from Google Symbols — `{weight, fill, grade, opsz}` are all variable axes, allowing icons to match UI density dynamically.
- **Ligature features**: `font-feature-settings: "liga"` is always on for icon spans.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is `4dp` (`{spacing.xs}`), rendered as px on web.

Dominant values from the scanned homepage: `{spacing.2xl}` (49 uses), 1px (46, outlines), `{spacing.xs}` (16), `{spacing.sm}` (7), `{spacing.lg}` (3), `{spacing.6xl}` (9 for hero sections).

### Grid & Container
- 12-column grid with `{spacing.2xl}` gutters on desktop
- Margins: `{spacing.lg}` (compact), `{spacing.2xl}` (medium), `{spacing.3xl}` (expanded)
- Max content width varies; M3 encourages full-bleed layouts with panel-based regions

### Whitespace Philosophy
- **Generous and proportional**: M3's whitespace scales with surface importance. Hero sections get `{spacing.6xl}+` vertical rhythm; compact UI gets `{spacing.lg}`. Whitespace is a layout tool, not a default.
- **Primary container as atmosphere**: Large blocks of `{colors.primary-container}` carry brand without color fatigue. A full-width tinted section is considered "on-brand" even without a logo or CTA.
- **Section rhythm**: `{spacing.6xl}` hero padding → `{spacing.5xl}` section gap → `{spacing.2xl}` component gap → `{spacing.sm}`–`{spacing.lg}` within components.

## Elevation & Depth

### M3 Elevation Levels

| Level | Treatment | Use |
|---|---|---|
| 0 | none | Surface at rest, most components default |
| 1 | dual-layer key + ambient (subtle) | Cards, elevated buttons, hover lift |
| 2 | dual-layer (slightly stronger) | Top app bar scrolled, active chips |
| 3 | dual-layer (medium) | FABs, nav drawer, dialogs |
| 4 | dual-layer (high) | Nav drawer active, modal sheets |
| 5 | dual-layer (highest) | Search results over content |

Each level pairs a directional **key shadow** (e.g. `0 1px 2px {colors.shadow-key}`) with a soft **ambient shadow** (e.g. `0 1px 3px 1px {colors.shadow-ambient}`). The original spec uses rgba alpha; flattened opaque approximations are exposed as `{colors.shadow-key}` and `{colors.shadow-ambient}`.

**Shadow Philosophy**: M3's elevation is two things simultaneously — a **shadow system** for perceived depth and a **surface tint system** that applies a semi-transparent primary color overlay at higher elevations, making elevated surfaces feel slightly tinted by the brand. This is especially visible in dark mode, where elevation-4/5 surfaces pick up a perceptible purple cast. Elevation is also animated — state changes (hover, press, drag) cause measurable elevation transitions, not just color shifts. Unlike shadcn's border-first or Stripe's blue-tinted approach, M3 commits fully to shadow as a primary design material.

## Shapes

The radius scale is its own expressive axis — M3 ships seven discrete steps plus a fully-round value, each tuned for a specific component class.

| Token | Value | Use |
|---|---|---|
| `xs` | 4px | Text fields, dense chips, compact buttons |
| `sm` | 8px | Input chips, filter chips, avatars |
| `md` | 12px | Small cards, small dialogs |
| `lg` | 16px | Standard cards, extended FABs |
| `xl` | 20px | Buttons of all sizes (the M3 button pill) |
| `2xl` | 24px | Cards, prominent buttons, menu surfaces — **the dominant radius** |
| `3xl` | 28px | Dialogs, bottom sheets |
| `switch` | 32px | Switch tracks (nearly pill) |
| `pill` | 9999px | FABs, switches, pills, avatars |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (e.g. `{components.button-filled}`, `{components.card-elevated}`, `{components.fab}`) rather than reconstructing them.

### Buttons (M3 type classes)
- **`button-filled`** — primary action. `{colors.primary}` background, `{colors.on-primary}` text, `{rounded.xl}` radius, elevation 0 by default; lifts to elevation 1 + 8% state-layer overlay on hover.
- **`button-elevated`** — `{colors.surface}` background with elevation 1 shadow, `{colors.primary}` text. Hover increases to elevation 2.
- **`button-outlined`** — transparent fill, 1px `{colors.outline}` border, `{colors.primary}` text. Hover applies an 8% primary state-layer (`{colors.state-layer-primary}`).
- **`button-text`** — no fill, no border, `{colors.primary}` text only. Hover applies the same 8% state-layer.

### FABs (Floating Action Buttons)
- **`fab`** — `{colors.primary-container}` background, icon in `{colors.on-primary-container}`. `{rounded.pill}` radius for small/regular. Default elevation 3, elevation 4 on hover. Sizes: 40px (small), 56px (standard), 96px (large).
- **`fab-extended`** — same colors, `{rounded.lg}` radius, label + icon.

### Cards
- **`card-elevated`** — `{colors.surface}` background, `{rounded.2xl}` radius (M3's signature card shape), elevation 1 default / 2 hover.
- **`card-filled`** — `{colors.primary-container}` background, no shadow.
- **`card-outlined`** — `{colors.surface}` background with 1px `{colors.outline}` border, no shadow.

### Text Fields
- **`input-outlined`** (default): 1px `{colors.outline}` at rest, 2px `{colors.primary}` on focus. `{rounded.xs}` corners.
- **`input-filled`**: `{colors.surface-variant}` background with bottom-only indicator line. `{rounded.xs}` top corners only.
- Floating label that translates on focus/filled — Material's signature pattern. Helper text in `{typography.body-small}` at `{colors.on-surface-variant}`.

### Chips
- 32px height, `{rounded.sm}` radius, 16px horizontal padding.
- `chip` (assist/filter) carries a 1px `{colors.outline}` border and transparent fill.
- `chip-selected` switches to `{colors.primary-container}` background.

### Switches
- Track 32px tall, 52px wide, `{rounded.pill}`.
- `switch-track-off` uses `{colors.outline}`, `switch-track-on` uses `{colors.primary}`.
- Thumb 16px (off) → 24px (on); selected icon inside the active thumb is the M3 Expressive distinction.

### Navigation
- **`app-bar`**: 64px height, `{colors.surface}` background, no border. Elevation 0 at rest, 2 when scrolled.
- **`navigation-drawer`**: 360px wide, `{colors.primary-container}` surface, `{rounded.lg}` on top/right corners.
- **Navigation Rail**: 80px wide compact side rail for tablets.
- **`navigation-bar`**: bottom navigation, 80px height, `{colors.primary-container}` background.

### Dialogs / Sheets
- **`dialog`** — `{rounded.3xl}` radius, elevation 3, scrim `{colors.scrim-dark}` behind.
- **`bottom-sheet`** — same radius applied only to top corners.

## Do's and Don'ts

### Do
- Use `{rounded.2xl}` as the default card radius — M3's signature dimension
- Use Google Sans at weight 475 for display/headline — the nonstandard weight IS the brand
- Use Google Sans Text (not Google Sans) for body and labels — different metrics, same family
- Apply the 5-level elevation system for any surface that needs depth
- Use `{colors.primary-container}` as a large-area tinted surface for brand atmosphere
- Use Google Symbols with ligature rendering for icons — not SVG, not icon fonts
- Keep spacing on the `4dp` scale — `{spacing.xs}`, `{spacing.sm}`, `{spacing.md}`, `{spacing.lg}`, `{spacing.2xl}`, `{spacing.3xl}`, `{spacing.4xl}`
- Fully round FABs (`{rounded.pill}`) and switches (`{rounded.switch}` track)
- Apply state layer overlays (8% primary, e.g. `{colors.state-layer-primary}`) for hover/focus on interactive surfaces

### Don't
- Don't use sharp corners (`0–2px` radius) on interactive elements — M3 is categorically rounded
- Don't use standard weights (400 or 500) for display — weight 475 is specific
- Don't mix neutral grays with the outline color (`{colors.outline}`) — the lavender tint matters
- Don't use flat shadows — always dual-layer (key + ambient)
- Don't tighten letter-spacing on display sizes — M3 is normal-tracked
- Don't use tiny radii on cards — `{rounded.2xl}` is the floor, not `{rounded.sm}`
- Don't replace the purple with a competitor's color unless also swapping the whole dynamic palette
- Don't use box-shadow alone on elevated surfaces in dark mode — include the surface tint overlay

---

## Responsive Behavior

### Breakpoints (M3 window size classes)
| Class | Width | Key Changes |
|------|-------|-------------|
| Compact | `<600dp` | Single-column, bottom nav bar, `16dp` margins |
| Medium | `600-839dp` | Two-column content, navigation rail (80dp wide), `24dp` margins |
| Expanded | `840-1199dp` | Multi-pane layouts, permanent navigation drawer (360dp), `24dp` margins |
| Large | `1200-1599dp` | Three-pane layouts, expanded drawers |
| Extra Large | `≥1600dp` | Full canvas layouts, multiple sidebars |

### Touch Targets
- All interactive targets minimum `48dp × 48dp` — M3's accessibility floor
- Icon buttons wrap their `24dp` icon in a `48dp` hit target
- List items minimum `48dp` tall

### Collapsing Strategy
- Display Large: 96px → 57px → 45px across breakpoints, weight 475 maintained
- Navigation: permanent drawer → rail → bottom bar (from expanded to compact)
- Cards: maintain `24px` radius at all sizes, padding compresses from `24px` to `16px`
- FABs: persist at `56px × 56px` regardless of breakpoint
- Dialogs: full-screen on compact, centered modal on medium+
- Bottom sheets: replace dialogs on compact

### Image Behavior
- Images inside cards inherit `24px` radius top corners (clip with overflow hidden)
- Hero images full-bleed with `96px` vertical padding around content

---

## Agent Prompt Guide

### Quick Color Reference
- Primary: Material Purple (`#6442d6`)
- Primary Dark: Light Purple (`#9f86ff`)
- Primary Container: Pink Blush (`#f8f1f6`)
- Surface: White (`#ffffff`)
- On Surface (text): Near Black (`#1c1b1d`)
- On Surface Variant (secondary text): Warm Gray (`#4d4256`)
- Outline: Lavender (`#dcdaf5`)
- Dark Surface: Near Black (`#1f1f1f`)
- Scrim: rgba(31,31,31,0.64)

### Example Component Prompts
- "Create a hero: white background, 96px vertical padding. Headline at 96px Google Sans weight 475, line-height 1.00, color #1c1b1d. Subtitle at 22px Google Sans Text weight 400, line-height 1.36, color #4d4256. Filled button: #6442d6 bg, white text, 20px radius, 10px 24px padding, 14px Google Sans Text weight 500. Outlined button: transparent, 1px solid #dcdaf5, #6442d6 text, 20px radius."
- "Design an elevated card: #ffffff background, 24px radius, 16px padding, elevation-1 shadow (0 1px 2px rgba(0,0,0,0.3), 0 1px 3px 1px rgba(0,0,0,0.15)). Title at 24px Google Sans weight 475 color #1c1b1d. Body at 14px Google Sans Text weight 400, line-height 1.43, color #4d4256."
- "Build an FAB: #f8f1f6 bg, 56px square, 50% radius (fully round), elevation-3 shadow. Icon in Google Symbols at 24px, color #21182b. Hover: elevation-4, 8% state layer overlay."
- "Create a filled text field: #f8f1f6 background, no border, 4px top-corners radius, 56px height, 16px padding. Floating label at 12px weight 400 color #4d4256, translates to top on focus. Focus indicator: 2px bottom border #6442d6."
- "Design a chip: 32px height, 8px radius, 1px solid #dcdaf5 border, transparent bg (unselected) or #f8f1f6 (selected). Label at 14px Google Sans Text weight 500. Optional leading icon (Google Symbols at 18px)."

### Iteration Guide
1. Start with `24px` card radius — if it looks wrong, try `16px` or `28px`, never `8px` or less
2. Use weight 475 specifically for display (Google Sans). If unavailable, fallback to 500 — never 400
3. Icons are typography: use Google Symbols with `font-feature-settings: "liga"`; icon size should match text size
4. For any interactive surface, add an 8% primary state layer on hover — not just a color shift
5. Elevation is always dual-layer (key + ambient) — single shadows read as flat
6. Primary container (`#f8f1f6`) is for atmosphere, not accents — use it as a *surface*, not a highlight
7. For dark mode, surfaces at elevation-2+ should pick up a primary-color tint (~5% opacity overlay)
8. Spring animations: M3 uses `cubic-bezier(0.2, 0, 0, 1)` for emphasized transitions — don't use linear
