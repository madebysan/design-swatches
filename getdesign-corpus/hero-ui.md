---
slug: hero-ui
name: HeroUI
url: https://heroui.com
domain: heroui.com
category: Design System
styles: [Light, Colorful, Bold]
tagline: "Electric blue and full-pill radii, Inter at 700 doing the structural heavy lifting."
fonts: [Inter, ui-monospace]
primary_color: "#dbeeff"
---

# Design System Inspired by HeroUI

> Electric blue and full-pill radii, Inter at 700 doing the structural heavy lifting.

## 1. Visual Theme & Atmosphere

HeroUI is the v3 refresh of NextUI — rebranded, re-tokened, re-energized. The homepage is a confident showcase of components with saturated brand color (`#006fee` electric blue), vibrant secondary (`#7828c8` purple), and a full-pill radius culture that runs through buttons, tabs, and badges. Where shadcn restrains and Park UI neutralizes, HeroUI **celebrates** — colors, curves, and the polished confidence of a library that expects its components to appear on landing pages, not just admin panels.

Typography is **Inter** across the system — no custom typeface, no experimental weight. Inter weight 700 at 48px with `-1.2px` tracking for hero display, weight 600 for UI text, weight 400 for body. The restraint here is deliberate: HeroUI wants the color system to be the brand voice, and neutral typography keeps attention on the chromatic palette.

The defining move is HeroUI's **semantic color system with full scales**. Six roles (default, primary, secondary, success, warning, danger), each with a 50-900 scale, each WCAG-AA verified. Components accept `color="primary"` as a prop, resolving to the full theme scale at runtime. This is NextUI's legacy refined — Tailwind Variants as the styling engine, React Aria as the accessibility primitives.

**Key Characteristics:**
- Inter as the sole typeface — weight 700 at display, weight 600 for UI
- Electric blue brand (`#006fee`) with vibrant purple secondary (`#7828c8`)
- `12px` / `24px` radii dominant — generous, friendly
- Full-pill radius (`9999px`) used liberally — tabs, chips, some buttons
- Six semantic color roles each with full 50-900 scales
- Built on React Aria + Tailwind Variants + Framer Motion
- v3 is a breaking redesign from NextUI (not a patch upgrade)
- Dark mode is a first-class theme, not an afterthought

## 2. Color Palette & Roles

### Semantic Roles (each has 50-900 scale)
- **default**: Neutral gray scale — `#f4f4f5` (200) → `#71717a` (500) → `#18181b` (900)
- **primary**: Electric blue — `#dbeeff` (100) → `#006fee` (500) → `#003663` (900)
- **secondary**: Vibrant purple — `#f2eafa` (100) → `#7828c8` (500) → `#300c4f` (900)
- **success**: Emerald — `#e8faf0` (100) → `#17c964` (500) → `#095028` (900)
- **warning**: Amber — `#fefce8` (100) → `#f5a524` (500) → `#62420e` (900)
- **danger**: Red pink — `#fee7ef` (100) → `#f31260` (500) → `#610726` (900)

### Base Colors
- **Background** (`#ffffff`): Page canvas.
- **Foreground** (`#171717`): Primary text. `--color-fd-secondary-foreground`.
- **Card** (`#ffffff`): Card surface. `--color-fd-card-foreground: #0a0a0a`.
- **Divider** (`#e5e5e5`): Hairline borders.
- **Focus** (`#006fee`): Focus ring color (primary-500).

### Key CSS Variables
- `--color-fd-secondary`: `#f9f9f9`
- `--color-fd-secondary-foreground`: `#171717`
- `--color-fd-card-foreground`: `#0a0a0a`
- `--color-backdrop`: `rgba(255,255,255,0.4)`
- `--color-fd-overlay`: `rgba(0,0,0,0.2)`
- `--color-fd-diff-add`: `#0eb46419`
- `--color-fd-diff-remove`: `#c80a641f`

## 3. Typography Rules

### Font Family
- **Primary**: `Inter`, fallback: `ui-sans-serif, system-ui, sans-serif`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, monospace`
- HeroUI ships fonts via `next/font` — preloaded, swap behavior tuned

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Hero | Inter | 48px | 700 | 1.10 | -1.2px |
| H1 | Inter | 36px | 700 | 1.15 | -0.9px |
| H2 | Inter | 24px | 600 | 1.25 | normal |
| H3 | Inter | 24px | 500 | 1.25 | normal |
| Body Large | Inter | 18px | 500 | 1.56 | normal |
| Body | Inter | 16px | 400 | 1.50 | normal |
| Label | Inter | 16px | 600 | 1.43 | normal |
| Caption | Inter | 14px | 400 | 1.43 | normal |
| Code | ui-monospace | 14px | 500 | 1.50 | normal |

### Principles
- **Weight 700 for display, weight 600 for UI**: Clean two-weight hierarchy, minimal in-between.
- **Negative tracking at display**: `-1.2px` at 48px, lighter below — less aggressive than shadcn but more than Material.
- **No custom typeface**: Inter handles everything; HeroUI commits fully to Inter rather than branded typography.

## 4. Component Stylings

### Buttons
- **Solid Primary**: `#006fee` bg, white text, `12px` radius (medium), `6px 16px` padding, 14px weight 600.
- **Radius Variants**: `none` (0px), `sm` (8px), `md` (12px — default), `lg` (16px), `full` (9999px).
- **Size Variants**: `sm` (32px), `md` (40px — default), `lg` (48px).
- **Variants**: `solid`, `bordered` (outline), `light` (ghost), `flat` (soft-color bg), `faded`, `shadow` (with elevation), `ghost`.

### Cards
- `#ffffff` bg, `1px solid #e5e5e5`, `14px` radius, `24px` padding.
- Shadow variants: `none`, `sm` (`0 2px 4px rgba(0,0,0,0.04)`), `md` (`0 4px 12px rgba(0,0,0,0.08)`), `lg` (`0 8px 30px rgba(0,0,0,0.12)`).
- Hover lift: shadow increases by one level.

### Inputs
- **Bordered**: `#ffffff` bg, `1px solid #e5e5e5`, `12px` radius, `8px 12px` padding.
- **Flat**: `#f9f9f9` bg, no border.
- **Underlined**: transparent bg, `2px solid #e5e5e5` bottom only.
- Focus: primary-500 border with `0 0 0 2px rgba(0,111,238,0.15)` ring.

### Chips (HeroUI's branded badges)
- `9999px` radius (full pill), `3px 10px` padding, 12px weight 500.
- Variants: `solid`, `bordered`, `light`, `flat`, `faded`, `shadow`, `dot` (colored dot indicator).

### Tabs
- `9999px` radius on the tab container background (`#f4f4f5`)
- Active tab: `#ffffff` bg with `0 1px 3px rgba(0,0,0,0.1)` shadow
- Non-active: transparent with hover to lighter gray

### Switches
- `9999px` pill track, `44px × 24px` default
- Track: `#e5e5e5` (off) → `#17c964` (on, success color)
- Thumb: `#ffffff` with soft shadow

## 5. Layout Principles

### Spacing System
- Base unit: **4px** (Tailwind-aligned)
- Dominant values: `4px` (48 uses), `8px` (29), `6px` (26), `12px` (8)
- Slightly denser than Material, comparable to shadcn

### Grid
- 12-column via Tailwind
- Max width: `1280px`
- Gutter: `16-24px`

### Border Radius Scale
- Sharp (`4px`): Small inline elements (kbd, separators)
- Compact (`6-8px`): Small buttons, chips
- Standard (`12px`): Buttons, inputs — the HeroUI default
- Comfortable (`16px`): Cards, dropdowns
- Large (`20-24px`): Featured cards, modals
- Full (`9999px`): Chips, avatars, tabs, switches — liberal use

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | No shadow | Cards default |
| sm | `0 2px 4px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.06)` | Card rest |
| md | `0 4px 12px rgba(0,0,0,0.08)` | Dropdowns, cards hover |
| lg | `0 8px 30px rgba(0,0,0,0.12)` | Modals, featured cards |
| xl | `0 20px 50px rgba(0,0,0,0.15)` | Modal dialogs |

**Shadow Philosophy**: HeroUI uses a 4-level shadow scale borrowed from Tailwind's default shadows with slight customization for softer edges. Shadows are neutral (no color tinting) and applied sparingly — most components sit flat with `1px` border elevation, reserving shadows for floating/interactive elements.

## 7. Do's and Don'ts

### Do
- Use semantic color props (`color="primary"`) — never hardcoded hex
- Default to `12px` radius for buttons, `14px` for cards
- Use full-pill radius on chips, switches, and tabs containers
- Use Inter weight 700 for display, weight 600 for UI, weight 400 for body
- Pair the primary electric blue with the vibrant purple secondary when you need accent variety
- Use the shadow scale progressively (`sm` → `md` → `lg`) for elevation hierarchy

### Don't
- Don't override individual theme colors — swap the theme object instead
- Don't use weight 800+ for display — HeroUI is weight 700 maxed
- Don't mix Material or Carbon radii — HeroUI's rhythm is `12/14/16/full`
- Don't use custom icon sets that conflict with the Solar Duotone default
- Don't skip the `radius="full"` prop on chips — pill shape is the brand

## 8. Responsive Behavior

### Breakpoints (Tailwind)
| Name | Width | Changes |
|------|-------|---------|
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

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary: `#006fee` (electric blue)
- Secondary: `#7828c8` (vibrant purple)
- Success: `#17c964` (emerald)
- Warning: `#f5a524` (amber)
- Danger: `#f31260` (red-pink)
- Foreground: `#171717`
- Divider: `#e5e5e5`
- Background: `#ffffff`

### Example Component Prompts
- "Create a hero: white bg. Headline at 48px Inter weight 700, letter-spacing -1.2px, line-height 1.10, color #171717. Subtitle 18px weight 500 color #71717a. Primary button: #006fee bg, white text, 12px radius, 10px 20px padding, 14px weight 600. Hover: 90% opacity overlay."
- "Design a card: white bg, 1px solid #e5e5e5, 14px radius, 24px padding, box-shadow 0 2px 4px rgba(0,0,0,0.04). Title 20px Inter weight 600. Body 14px weight 400 color #71717a. Action chip (full pill, #006fee bg, white text, 12px weight 500)."
- "Build a chip: 9999px radius, 3px 10px padding, 12px Inter weight 500. Variants: solid (color bg + white text), bordered (1px solid color + color text), flat (color at 15% alpha bg + color text), dot (small colored circle + neutral text)."

### Iteration Guide
1. Think in semantic color props — `color="primary"` not hex
2. `12px` radius is the default for buttons/inputs; `9999px` for chips/switches
3. Inter weight 700 display, weight 600 UI, weight 400 body — no middle weight
4. Shadows are neutral; use scale progressively (sm/md/lg/xl)
5. For dark mode, HeroUI provides a pre-built dark theme — don't manually invert
6. Tab bars use `9999px` radius on the container; active tab gets white bg with subtle shadow
