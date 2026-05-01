---
slug: daisyui
name: DaisyUI
url: https://daisyui.com
domain: daisyui.com
category: Design System
styles: [Colorful, Light, Playful]
tagline: "Outfit 900, full-pill radii, 36 OKLCH themes swapped by a single attribute."
fonts: [Outfit, ui-monospace, ui-sans-serif]
primary_color: "#661ae6"
---

# Design System Inspired by DaisyUI

> Outfit 900, full-pill radii, 36 OKLCH themes swapped by a single attribute.

## 1. Visual Theme & Atmosphere

DaisyUI is what happens when a Tailwind plugin decides to be friendly. The homepage is a kaleidoscope of themes with names like Cupcake, Valentine, Retro, and Synthwave — each one a complete palette (primary, secondary, accent, neutral, base) that swaps live via a single CSS variable change. The default aesthetic is playful: Outfit typeface at heavyweight 900 for display, saturated colors, full-pill button radii, and rounded corners everywhere. Where shadcn disappears into neutral and Stripe whispers through weight 300, DaisyUI announces itself — loud, colorful, and unashamed of it.

The typographic choice is **Outfit** — a geometric sans-serif with an unusual weight range (100-900). At display sizes it runs at weight 900 with slight negative tracking; at body sizes it drops to 400. No variable font axes are used; weights are discrete. The pairing is `ui-monospace` for code blocks and `system-ui` for the occasional system-native element. Icons are font-agnostic — the docs use Lucide, Heroicons, or any SVG set, whatever the user prefers.

The defining move is the **theme system**. 36 built-in themes, each defined as a set of OKLCH color variables scoped to a `[data-theme]` attribute. Components reference `bg-primary`, `text-primary-content`, `bg-accent` — semantic names that resolve to whatever the active theme says. Swap the theme attribute, every component updates. This is CSS theming taken to its logical end: not a dark mode toggle, but a full personality switch.

**Key Characteristics:**
- Outfit as primary typeface, weight 900 for display — playful, heavy, geometric
- 36 built-in themes (Cupcake, Dracula, Synthwave, Retro, etc.) as OKLCH palettes
- Semantic component classes (`btn`, `btn-primary`, `card`) on top of Tailwind utilities
- Full-pill button radius by default — rounded, friendly
- Colorful-by-default — saturated primaries, accent colors, celebration aesthetic
- Zero dependencies on Tailwind utility components — pure CSS layer
- OKLCH color space throughout — perceptually uniform, theme-swap-safe

## 2. Color Palette & Roles

DaisyUI's palette isn't a fixed set of hex values — it's a **semantic token system** that resolves per theme. The default (light) theme uses:

### Semantic Roles
- **primary** (`#661ae6`): Main brand color, primary buttons, active links.
- **primary-content** (`#ffffff`): Text on primary surfaces.
- **secondary** (`#d926a9`): Secondary brand, accent buttons.
- **accent** (`#1fb2a6`): Tertiary highlight, notification dots, selected chip borders.
- **neutral** (`#1d232a`): Default text, footer background in light themes.
- **base-100** (`#ffffff`): Primary page background.
- **base-200** (`#f2f2f2`): Alternate surface (cards, inputs).
- **base-300** (`#e5e6e6`): Borders, dividers.
- **base-content** (`#1f2937`): Default text on base surfaces.

### State Colors
- **info** (`#3abff8`): Info alerts, help text highlights.
- **success** (`#36d399`): Confirmation badges, success alerts.
- **warning** (`#fbbd23`): Caution states, yellow alerts.
- **error** (`#f87272`): Destructive actions, error alerts.

### Theme Variations (examples)
- **cupcake**: Soft pastels — primary `#65c3c8` teal, accent `#eeaf3a` gold
- **dracula**: Dark mode purple — primary `#ff79c6` magenta on `#282a36` canvas
- **synthwave**: Retro neon — primary `#e779c1` pink on `#2d1b69` deep purple
- **retro**: Warm vintage — primary `#ef9995` coral on `#e4d8b4` cream

### Raw Colors (from scanned homepage)
- 7,217 `oklch()` color references — DaisyUI is fully OKLCH-native
- 1,068 `oklab()` references for opacity overlays
- 358 `#000000` references — used sparingly, mostly for borders in dark themes

## 3. Typography Rules

### Font Family
- **Primary**: `Outfit`, fallback: `ui-sans-serif, system-ui, sans-serif`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, monospace`
- **System (docs)**: `ui-sans-serif, system-ui, sans-serif` for nav and docs chrome

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Hero | Outfit | 72px | 900 | 1.05 | -1.5px |
| Display Large | Outfit | 64px | 900 | 1.10 | -1.2px |
| H1 | Outfit | 48px | 700 | 1.15 | normal |
| H2 | Outfit | 36px | 700 | 1.20 | normal |
| H3 | Outfit | 24px | 700 | 1.30 | normal |
| Body Large | Outfit | 18px | 600 | 1.50 | normal |
| Body | Outfit | 16px | 400 | 1.50 | normal |
| Button | Outfit | 14px | 600 | 1.20 | normal |
| Caption | Outfit | 12px | 400 | 1.33 | normal |
| Code | ui-monospace | 14px | 400 | 1.50 | normal |

### Principles
- **Weight 900 as the display signature**: Outfit at weight 900 is the brand's most recognizable typographic choice — fully drawn letterforms, maximum presence.
- **Weight 300 for light display accents**: Some theme variants use weight 300 for a softer, retro-inspired display treatment.
- **Letter-spacing is conservative**: DaisyUI doesn't lean on tight tracking — display sizes use `-1.5px` at most, below 24px tracking stays at normal.
- **Mono for code only**: Unlike shadcn's liberal use of Geist Mono for timestamps and data, DaisyUI reserves monospace for code blocks and inline `<code>`.

## 4. Component Stylings

### Buttons
- **btn-primary**: `bg-primary`, `text-primary-content`, `9999px` radius (pill), 14px Outfit weight 600.
- **btn-outline**: transparent bg, `1px solid bg-primary`, `text-primary`, pill radius.
- **btn-ghost**: transparent bg, `text-base-content`, hover `bg-base-200`.
- **btn-link**: no bg, no border, underline on hover.
- **btn-sm**: `32px` height with smaller padding.
- **btn-xs**: `24px` height for compact UIs.

### Cards
- **card**: `bg-base-100`, `1px solid base-300`, `16px` radius, `24px` padding, subtle `0 1px 2px rgba(0,0,0,0.05)` shadow.
- **card-bordered**: adds a stronger `2px solid base-300` border.
- **card-compact**: `12px` padding for dense layouts.

### Inputs
- **input**: `bg-base-100`, `1px solid base-300`, `8px` radius, `12px 16px` padding.
- **input-bordered**: stronger border for form emphasis.
- **input-primary**: border in primary color, primary-colored focus ring.

### Badges
- **badge**: `9999px` radius (pill), `4px 8px` padding, 12px Outfit weight 500.
- Variants: `badge-primary`, `badge-success`, `badge-warning`, `badge-error` — each reading from the semantic color.

### Alerts
- **alert**: 2px accent border-left, `bg-base-200`, `12px` radius, icon left-aligned.
- Variants for info, success, warning, error.

### Modals / Drawers
- **modal-box**: `16px` radius, `bg-base-100`, `24px` padding, `0 20px 40px rgba(0,0,0,0.1)` shadow.

## 5. Layout Principles

### Spacing System
- Base unit: **4px** (Tailwind-aligned)
- Dominant values: `4px` (1,193 uses — gap-1), `6px` (410, gap-1.5), `8px` (191, gap-2)
- DaisyUI uses Tailwind's spacing scale exactly — nothing custom

### Grid
- 12-column grid via Tailwind
- `container mx-auto` with `max-width: 1280px` as the default marketing container
- Docs layout: `sidebar-aside-256px` + content column

### Whitespace
- **Generous padding inside cards**: `24px` default, `16px` on compact variants
- **Bold section rhythm**: `80-120px` between homepage sections, `32-48px` between card rows
- **Full-pill buttons breathe**: button padding (`0 20px`) accommodates the pill shape without crowding text

### Border Radius Scale
- Sharp (`0px`): avoided almost everywhere
- Standard (`8px`): inputs, small cards, code blocks
- Comfortable (`16px`): cards, modals, larger surfaces
- Pill (`9999px`): buttons, badges, avatars, switches — the default for interactive elements

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | No shadow | Backgrounds, inline elements |
| Subtle | `0 1px 2px rgba(0,0,0,0.05)` | Cards at rest |
| Hover | `0 4px 8px rgba(0,0,0,0.08)` | Card hover state |
| Modal | `0 10px 30px rgba(0,0,0,0.15)` | Modals, elevated dropdowns |

**Shadow Philosophy**: DaisyUI's shadows are soft and small — they add the impression of lift without obscuring the bright colors underneath. Per theme, shadow intensity adjusts: dark themes use a subtle white inner shadow for lift, light themes use a soft black outer shadow.

## 7. Do's and Don'ts

### Do
- Use semantic classes (`btn-primary`, `card`, `badge-success`) — never hardcoded colors
- Use pill radius (`9999px`) for buttons and badges — the brand voice
- Pick a theme and let the semantic variables do the work — don't override individual components
- Use Outfit weight 900 for hero displays — the signature
- Use OKLCH color values if extending the theme — stays perceptually uniform

### Don't
- Don't hardcode hex colors in components — break the theme system
- Don't use border-radius values between 0-6px on interactive elements — DaisyUI is rounded by default
- Don't override semantic tokens per-component — change the theme instead
- Don't mix Outfit with Inter — keep the geometric personality consistent
- Don't use weight 800 for display — go to 900 for full impact

## 8. Responsive Behavior

### Breakpoints (Tailwind)
| Name | Width | Changes |
|------|-------|---------|
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

## 9. Agent Prompt Guide

### Quick Color Reference (cupcake theme)
- Primary: `oklch(65% 0.06 200)` (teal)
- Primary content: `oklch(18% 0.03 200)` (dark teal)
- Accent: `oklch(75% 0.12 60)` (gold)
- Base-100: `#faf7f5` (warm white)
- Base-content: `#291e00` (dark brown)

### Example Component Prompts
- "Create a hero: base-100 background, Outfit 72px weight 900 letter-spacing -1.5px, `text-base-content`. Subtitle at 18px weight 400. Primary button with `bg-primary`, 9999px radius, 12px padding, `text-primary-content`."
- "Design a card: `bg-base-100`, `border border-base-300`, `16px` radius, `24px` padding, `shadow-sm`. Title at 24px Outfit weight 700 color `base-content`. Action button at bottom right — pill radius, `bg-primary`."
- "Build a badge: `bg-success`, `text-success-content`, `4px 8px` padding, `9999px` radius, 12px weight 500. Optional icon left at 14px."

### Iteration Guide
1. Pick a theme first, then compose components — the theme IS the design
2. Pill radius (`9999px`) is the brand voice for interactive elements
3. Outfit weight 900 at display is non-negotiable for hero sections
4. Use semantic tokens, not hex — `bg-primary` over `bg-[#661ae6]`
5. Keep padding generous inside components; DaisyUI is friendly, not dense
6. For dark themes, use the provided theme variants (dracula, synthwave) — don't just invert
