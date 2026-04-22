# Design System Inspired by Material Design 3

## 1. Visual Theme & Atmosphere

Material Design 3 — and specifically the M3 Expressive refresh — is Google's thesis that software should feel tactile, colorful, and alive. Where shadcn erases itself and Stripe whispers through typography, M3 celebrates chrome. Large rounded corners (`24px` is the dominant radius, used 31 times on the homepage), generous `24px` spacing units (the single most-used value on the page, appearing 49 times), and a signature purple (`#6442d6`) that serves as a brand anchor while the **dynamic color** system generates entire palettes from a user's wallpaper. The canvas alternates between pure white and a warm pink-blush (`#f8f1f6`) that Google calls a "primary container" — a tinted surface that carries brand atmosphere without demanding attention.

The typography is Google Sans at weight 475 — a nonstandard, distinctly Google weight that sits between book (400) and medium (500), softer than medium but with more presence than regular. At display sizes it scales to 96px (`6.00rem`) with line-height 1.00 — gigantic, confident, and unapologetically friendly. Body text drops to Google Sans Text (a subtly different metric) at 16px weight 400 with 1.50 line-height. Icons are handled by **Google Symbols** — a variable font where weight, fill, and grade are all continuous axes, turning every icon into a piece of typography rather than a rasterized asset.

What truly distinguishes M3 is its **motion and elevation philosophy**. Shadows are subtle but always present — an elevation system codified into `elevation-0` through `elevation-5`, each with specific dual-layer shadows (a key shadow for directional depth + an ambient shadow for soft perimeter glow). Components don't just appear — they grow, fade, and spring with material-specific easing curves. The radius scale itself is an expressive device: switches are nearly circular (`32px`), FABs are fully rounded (`50%`), cards land at `24px`, buttons at `4px-20px` depending on size class. Nothing is sharp. Nothing is flat. Everything has weight, rounded edges, and the sense that if you pressed it, it would respond.

**Key Characteristics:**
- Signature purple `#6442d6` (light) / `#9f86ff` (dark) as the primary brand anchor
- Google Sans at weight 475 — a nonstandard weight that IS the brand
- Google Symbols variable font for icons (weight + fill + grade axes)
- `24px` as the dominant spacing + radius value — M3's proportional DNA
- Primary container `#f8f1f6` as a tinted surface for brand atmosphere
- Dynamic Color system — palettes generated algorithmically from a seed color
- Dual-layer shadow elevation: directional key + ambient perimeter
- Fully rounded FABs (`50%`) and pill switches (`32px`) — never sharp
- 5-level elevation system (0-5), each with named shadow values
- Expressive motion: spring curves, not linear transitions

## 2. Color Palette & Roles

### Primary (Light Theme)
- **Primary Purple** (`#6442d6`): Primary brand color — used on CTAs, icons, active states. 51 occurrences on the homepage. A saturated but not neon purple.
- **Primary Container** (`#f8f1f6`): A pink-blush tinted surface for brand atmosphere. Used on large area backgrounds and card interiors that need to feel "on-brand" without shouting.
- **On Primary** (`#ffffff`): Text/icon color on the purple primary surface.
- **On Primary Container** (`#21182b`): Text/icon color on the pink-blush container.

### Primary (Dark Theme)
- **Primary Purple Dark** (`#9f86ff`): Lighter, more luminous purple for dark contexts — defined as `--mio-theme-color-primary` in the scanned CSS.
- **Primary Container Dark** (`#4d2dcb`): Deeper purple as container in dark mode.

### Neutral Scale
- **Surface** (`#ffffff`): Base light surface.
- **Surface Variant** (`#f8f1f6`): Slightly warmer surface for differentiation.
- **On Surface** (`#1c1b1d`): Primary text color — warm near-black (370 occurrences make this the most-used color on the page).
- **On Surface Variant** (`#4d4256`): Secondary text (96 occurrences) — a warm purple-tinged gray, not neutral gray.
- **Outline** (`#dcdaf5`): Border color with a soft lavender cast, tying borders to the brand palette.
- **Dark Surface** (`#1f1f1f`): Near-black for dark-mode canvas.

### Accent & Support
- **Secondary / Tertiary**: M3's dynamic color system generates secondary (`#6e5692` muted purple) and tertiary (`#825268` rose) palettes from the primary seed.
- **Error** (`#b3261e`): Red for destructive/error states.
- **Success Green**: M3 does not ship a default success color — the system encourages teams to extend with custom role names.

### Scrim (overlays)
- `rgba(31, 31, 31, 0.64)` — dark scrim for modals/dialogs over content
- `rgba(255, 255, 255, 0.24)` / `rgba(255, 255, 255, 0.12)` — light scrims for video controls

### CSS Variable Names (from scanned site)
- `--mio-theme-color-primary` (`#9f86ff` / dynamic)
- `--mio-theme-color-white` (`#ffffff`)
- `--mio-theme-color-black` (`#000000`)
- `--mio-theme-color-scrim-video-container` (`rgb(31 31 31 / 64%)`)

## 3. Typography Rules

### Font Family
- **Primary**: `Google Sans`, fallback: `Roboto`, `system-ui`, sans-serif
- **Body**: `Google Sans Text` (metric-matched sibling tuned for body readability)
- **Icons**: `Google Symbols` (variable font, features: `"liga"` enabled for ligature-based icon rendering)
- **Variable Font**: Google Sans ships with a custom weight axis — **475** is used extensively, a weight between regular (400) and medium (500) that does not exist in most fonts.

### Hierarchy (M3 type scale)

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Large | Google Sans | 96px (6.00rem) | 475 | 1.00 | normal | Homepage hero — maximum scale |
| Display Medium | Google Sans | 57px (3.56rem) | 475 | 1.12 | normal | Feature hero |
| Display Small | Google Sans | 45px (2.81rem) | 475 | 1.16 | normal | Section heads |
| Headline Large | Google Sans | 32px (2.00rem) | 475 | 1.25 | normal | Page titles |
| Headline Medium | Google Sans | 28px (1.75rem) | 475 | 1.29 | normal | Card titles |
| Headline Small | Google Sans | 24px (1.50rem) | 475 | 1.33 | normal | Sub-headings |
| Title Large | Google Sans | 22px (1.38rem) | 400 | 1.36 | normal | Prominent labels |
| Title Medium | Google Sans Text | 16px (1.00rem) | 500 | 1.50 | normal | Button text, list item titles |
| Title Small | Google Sans Text | 14px (0.88rem) | 500 | 1.43 | normal | Compact titles |
| Body Large | Google Sans Text | 16px (1.00rem) | 400 | 1.50 | normal | Default body — most comfortable |
| Body Medium | Google Sans Text | 14px (0.88rem) | 400 | 1.43 | normal | Secondary body, dense UI |
| Body Small | Google Sans Text | 12px (0.75rem) | 400 | 1.33 | normal | Captions, metadata |
| Label Large | Google Sans Text | 14px (0.88rem) | 500 | 1.43 | normal | Button labels, chips |
| Label Medium | Google Sans Text | 12px (0.75rem) | 500 | 1.33 | normal | Tabs, badge labels |
| Label Small | Google Sans Text | 11px (0.69rem) | 500 | 1.45 | normal | Smallest chrome labels |

### Principles
- **Weight 475 is the brand voice**: Not 400, not 500 — exactly 475. This is the weight that makes Google Sans feel like Google Sans, and it's non-negotiable at display/headline sizes.
- **Display vs Body is a family split, not just a size jump**: Google Sans for display/headline, Google Sans Text for body/labels. The metric difference is tuned for readability at small sizes.
- **No letter-spacing**: Unlike Stripe's tight tracking, M3 keeps tracking at normal across all sizes. Generosity over precision.
- **Google Symbols for icons**: Icons are rendered as ligatures from Google Symbols — `{weight, fill, grade, opsz}` are all variable axes, allowing icons to match UI density dynamically.
- **Ligature features**: `font-feature-settings: "liga"` is always on for icon spans.

## 4. Component Stylings

### Buttons (M3 type classes)

**Filled Button** (primary)
- Background: `#6442d6`
- Text: `#ffffff`
- Padding: `10px 24px`
- Radius: `20px` (pill-ish, not fully round)
- Font: 14px Google Sans Text weight 500
- Elevation: `0` (flat by default)
- Hover: elevation lifts to `1` + surface tint overlay at 8% opacity
- Height: `40px` standard, `36px` small, `56px` extra-large

**Elevated Button**
- Background: `#ffffff` (surface)
- Text: `#6442d6`
- Elevation: `1` (`0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)`)
- Radius: `20px`
- Hover: elevation increases to `2`

**Outlined Button**
- Background: transparent
- Text: `#6442d6`
- Border: `1px solid #dcdaf5` (outline)
- Radius: `20px`
- Hover: background `rgba(100,66,214,0.08)` (primary at 8%)

**Text Button**
- Background: transparent (no fill)
- Text: `#6442d6`
- No border
- Radius: `20px`
- Hover: `rgba(100,66,214,0.08)` state layer

**FAB (Floating Action Button)**
- Background: `#f8f1f6` (primary container)
- Icon: `#21182b` (on primary container)
- Radius: `50%` (fully round) for small/regular, `16px` for extended
- Elevation: `3` by default, `4` on hover
- Size: `56px × 56px` (standard FAB), `40px` (small), `96px` (large)

### Cards
- Background: `#ffffff` (elevated) or `#f8f1f6` (filled) or transparent with outline
- Radius: `24px` — M3's signature card radius
- Padding: `16px` standard
- Elevation (elevated variant): `1` by default, `2` on hover
- Outlined variant: `1px solid #dcdaf5`, no shadow

### Text Fields
- **Outlined** (default): `1px solid #dcdaf5` at rest, `2px solid #6442d6` on focus
- **Filled**: `#f8f1f6` background with bottom-only indicator line
- Radius: `4px` (top/top-only for filled) or `4px` all corners for outlined
- Padding: `16px` vertical
- Label: floating label that translates on focus/filled — Material's signature pattern
- Helper text: 12px weight 400, `#4d4256`

### Chips
- Height: `32px`
- Radius: `8px` (input/filter chips)
- Padding: `0 16px`
- Font: 14px Google Sans Text weight 500
- Border: `1px solid #dcdaf5` (assist/filter variant)
- Background: transparent (default), `#f8f1f6` (filled/selected)

### Switches
- Track: `32px` tall, `52px` wide
- Track Off: `#dcdaf5`, track On: `#6442d6`
- Thumb: `16px` circle (off) → `24px` circle (on)
- Radius: `9999px` on track
- Selected icon inside thumb (M3 Expressive distinction)

### Navigation
- **Top App Bar**: `64px` height, `#ffffff` surface, no border, elevation `0` at rest, `2` when scrolled
- **Navigation Drawer**: `360px` wide, `#f8f1f6` surface, `16px` radius on top/right
- **Navigation Rail**: `80px` wide compact side rail for tablets
- **Navigation Bar**: bottom navigation, `80px` height, `#f8f1f6` background

### Dialogs / Sheets
- Radius: `28px` (dialogs), `28px` top-corners only (bottom sheets)
- Scrim: `rgba(0,0,0,0.32)` behind
- Elevation: `3`

## 5. Layout Principles

### Spacing System
- Base unit: `4dp` (density-independent pixel, rendered as px on web)
- Scale: `4, 8, 12, 16, 20, 24, 32, 48, 64, 96, 120` (px)
- Dominant values (from scanned homepage): `24px` (49 uses), `1px` (46, outlines), `4px` (16), `8px` (7), `16px` (3), `96px` (9 for hero sections)

### Grid & Container
- 12-column grid with `24dp` gutters on desktop
- Margins: `16dp` (compact), `24dp` (medium), `32dp` (expanded)
- Max content width varies; M3 encourages full-bleed layouts with panel-based regions

### Whitespace Philosophy
- **Generous and proportional**: M3's whitespace scales with surface importance. Hero sections get `96px+` vertical rhythm; compact UI gets `16px`. Whitespace is a layout tool, not a default.
- **Primary container as atmosphere**: Large blocks of `#f8f1f6` carry brand without color fatigue. A full-width tinted section is considered "on-brand" even without a logo or CTA.
- **Section rhythm**: `96px` hero padding → `64px` section gap → `24px` component gap → `8-16px` within components.

### Border Radius Scale
- **Extra Small** (`4px`): Text fields, dense chips, compact buttons
- **Small** (`8px`): Input chips, filter chips, avatars
- **Medium** (`12px`): Small cards, small dialogs
- **Large** (`16px`): Standard cards, extended FABs
- **Extra Large** (`24px`): Cards, prominent buttons, menu surfaces — **the dominant radius**
- **Extra Large Top** (`24px` top corners only): Bottom sheets, nav drawers
- **Pill** (`20px`): Buttons of all sizes
- **Full** (`9999px` / `50%`): FABs, switches, pills, avatars

## 6. Depth & Elevation

### M3 Elevation Levels

| Level | Key Shadow | Ambient Shadow | Use |
|-------|-----------|----------------|-----|
| 0 | none | none | Surface at rest, most components default |
| 1 | `0 1px 2px rgba(0,0,0,0.3)` | `0 1px 3px 1px rgba(0,0,0,0.15)` | Cards, elevated buttons, hover lift |
| 2 | `0 1px 2px rgba(0,0,0,0.3)` | `0 2px 6px 2px rgba(0,0,0,0.15)` | Top app bar scrolled, active chips |
| 3 | `0 4px 8px 3px rgba(0,0,0,0.15)` | `0 1px 3px rgba(0,0,0,0.3)` | FABs, nav drawer, dialogs |
| 4 | `0 6px 10px 4px rgba(0,0,0,0.15)` | `0 2px 3px rgba(0,0,0,0.3)` | Nav drawer active, modal sheets |
| 5 | `0 8px 12px 6px rgba(0,0,0,0.15)` | `0 4px 4px rgba(0,0,0,0.3)` | Search results over content |

**Shadow Philosophy**: M3's elevation is two things simultaneously — a **shadow system** for perceived depth and a **surface tint system** that applies a semi-transparent primary color overlay at higher elevations, making elevated surfaces feel slightly tinted by the brand. This is especially visible in dark mode, where elevation-4/5 surfaces pick up a perceptible purple cast. Elevation is also animated — state changes (hover, press, drag) cause measurable elevation transitions, not just color shifts. Unlike shadcn's border-first or Stripe's blue-tinted approach, M3 commits fully to shadow as a primary design material.

## 7. Do's and Don'ts

### Do
- Use `24px` as the default card radius — M3's signature dimension
- Use Google Sans at weight 475 for display/headline — the nonstandard weight IS the brand
- Use Google Sans Text (not Google Sans) for body and labels — different metrics, same family
- Apply the 5-level elevation system for any surface that needs depth
- Use `#f8f1f6` (primary container) as a large-area tinted surface for brand atmosphere
- Use Google Symbols with ligature rendering for icons — not SVG, not icon fonts
- Keep spacing on the `4dp` scale — 4, 8, 12, 16, 24, 32, 48
- Fully round FABs (`50%`) and switches (`32px` height with pill track)
- Apply state layer overlays (8% primary) for hover/focus on interactive surfaces

### Don't
- Don't use sharp corners (`0-2px` radius) on interactive elements — M3 is categorically rounded
- Don't use standard weights (400 or 500) for display — weight 475 is specific
- Don't mix neutral grays with the outline color (`#dcdaf5`) — the lavender tint matters
- Don't use flat shadows — always dual-layer (key + ambient)
- Don't tighten letter-spacing on display sizes — M3 is normal-tracked
- Don't use tiny radii on cards — `24px` is the floor, not `8px`
- Don't replace the purple with a competitor's color unless also swapping the whole dynamic palette
- Don't use box-shadow alone on elevated surfaces in dark mode — include the surface tint overlay

## 8. Responsive Behavior

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

## 9. Agent Prompt Guide

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
