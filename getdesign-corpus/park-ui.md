# Design System Inspired by Park UI

## 1. Visual Theme & Atmosphere

Park UI is the design system for the agentic era — three-framework-compatible (React, Solid, Vue), tokens-first, aggressively neutral. The homepage is a showroom of components on a pure white canvas (`#ffffff`) with near-black text (`#000000`) and zero brand color in the chrome. This is the "Radix Themes with muscle" aesthetic — crisp borders, `4px` radii, Outfit display type, and a philosophy that the design system IS the tokens, not the components.

Typography is **Outfit** across the board — the same geometric sans-serif DaisyUI uses, but at weight 700 for display (not 900) with `-1.2px` letter-spacing. The 20px+ type uses weight 600 or 400 exclusively — no in-between weights, no weight 500. This two-weight simplicity is deliberate: Park UI wants components to compose cleanly, which means typography must be predictable.

The defining technical choice is Park UI's **595 CSS variables**. The scan found a massive token vocabulary — every Radix color scale (12 tones × 14 hues × light + dark + alpha), every spacing value, every radius, every elevation — all defined as custom properties. Components reference tokens like `--colors-neutral-solid-bg` or `--colors-jade-9`, never hex. This is the Radix Themes token system adopted wholesale into Panda CSS.

**Key Characteristics:**
- Outfit typeface, weight 700 at display — geometric, clean
- `4px` dominant radius (60 elements) — tighter than DaisyUI, consistent with Radix
- Built on Ark UI (headless primitives) + Panda CSS (compile-time CSS)
- 595 CSS variables — Radix Themes scale wholesale
- Framework-agnostic: React, Solid, Vue from one source
- Neutral-first palette (gray/black/white) — accent via Radix hues (jade, violet, ruby)
- No custom brand color — you bring your own
- Pill buttons absent — Park UI uses `4px` radius even on buttons

## 2. Color Palette & Roles

Park UI ships the full **Radix Themes** palette — 14 color scales (gray, mauve, slate, sage, olive, sand, red, orange, amber, yellow, green, teal, jade, cyan, blue, indigo, violet, purple, plum, pink, crimson, ruby, tomato, brown, bronze, gold) each with 12 steps (1-12) in both light + dark + alpha variants.

### Core Neutral (default theme)
- **Neutral 1** (`#fcfcfc`): Page background.
- **Neutral 2** (`#f9f9f9`): Subtle surface.
- **Neutral 3** (`#f0f0f0`): Element background.
- **Neutral 6** (`#d9d9d9`): Strong border.
- **Neutral 8** (`#8d8d8d`): Subtle text, muted foreground.
- **Neutral 9** (`#8f8f8f`): Solid backgrounds, badges.
- **Neutral 11** (`#646464`): Secondary text.
- **Neutral 12** (`#202020`): Primary text — near-black.

### Solid Role
- **Neutral Solid BG** (`#000000`): Primary buttons, active indicators.

### Accent Scales (examples — selectable per theme)
- **Jade 9** (`#29a383`): Green accent (`--colors-jade-9`).
- **Violet A3** (`#4400ee0f`): 6% violet alpha for subtle tints.
- **Amber Subtle BG Hover** (`#ffd40063`): 39% amber alpha for warning hovers.
- **Indigo 6** (`#c1d0ff`): Light indigo border.
- **Ruby 9** (`#e93d82`): Destructive accent (if theme is ruby).
- **Crimson 9** (`#e93d82`): Alternative destructive hue.

## 3. Typography Rules

### Font Family
- **Primary**: `Outfit`, fallback: `ui-sans-serif, system-ui, sans-serif`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, monospace`
- Park UI uses only ONE typeface family across the entire system — Outfit everywhere except code blocks.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Outfit | 60px | 700 | 1.10 | -1.2px |
| H1 | Outfit | 48px | 600 | 1.15 | -0.96px |
| H2 | Outfit | 32px | 600 | 1.20 | normal |
| H3 | Outfit | 24px | 600 | 1.30 | normal |
| Body Large | Outfit | 20px | 400 | 1.50 | normal |
| Body | Outfit | 16px | 400 | 1.50 | normal |
| Button | Outfit | 14px | 600 | 1.43 | normal |
| Caption | Outfit | 12px | 400 | 1.33 | normal |
| Code | ui-monospace | 14px | 400 | 1.43 | normal |

### Principles
- **Two-weight system**: 400 for body, 600 for UI text and headings, 700 for display — no 500, no 800, no in-between.
- **Outfit everywhere**: Unlike DaisyUI (which uses Outfit but also ui-sans for chrome), Park UI commits to Outfit throughout.
- **Conservative tracking**: Letter-spacing stays at `-1.2px` max — less aggressive than Stripe or shadcn.

## 4. Component Stylings

### Buttons
- **Solid**: `#000000` bg, `#ffffff` text, `4px` radius, `0 12px` padding, `36px` height, 14px Outfit weight 600.
- **Subtle**: `rgba(0,0,0,0.06)` bg, `#202020` text, `4px` radius.
- **Outline**: transparent bg, `1px solid #d9d9d9`, `#202020` text, `4px` radius.
- **Ghost**: transparent, hover `rgba(0,0,0,0.06)`.

### Cards
- `#ffffff` bg, `1px solid #d9d9d9`, `6px` radius, `24px` padding.
- Shadow: `0 1px 2px rgba(0,0,0,0.15), 0 0 1px rgba(0,0,0,0.192)` — subtle dual-shadow.

### Inputs
- `#ffffff` bg, `1px solid #d9d9d9`, `4px` radius, `0 12px` padding, `36px` height.
- Focus: `2px outline offset 2px` in theme color.

### Badges
- `4px` radius (not pill), `2px 8px` padding, 12px weight 500.
- Variants via Radix color scales: `solid`, `soft`, `outline` per hue.

### Dropdowns / Menus
- `#ffffff` bg, `1px solid #d9d9d9`, `6px` radius.
- Shadow: `0 4px 8px rgba(0,0,0,0.09), 0 0 1px rgba(0,0,0,0.09)`.

### Switches
- Track: `16px` tall, `32px` wide, `9999px` radius.
- Thumb: `12px` circle, white.

## 5. Layout Principles

### Spacing System
- Base unit: **4px**
- Dominant values: `24px` (38 uses), `16px` (17), `4px` (12), `8px` (8)
- More generous than shadcn (4-10px workhorses), less than Material (24-48px)

### Grid
- 12-column Tailwind/Panda grid
- `24px` section padding
- `16px` gutter gap

### Border Radius Scale
- Sharp (`2px`): Small inline elements, kbd
- Standard (`4px`): Buttons, inputs, badges — the workhorse (60 uses)
- Comfortable (`6px`): Cards, dropdowns
- Full (`9999px`): Avatars, switches, the occasional pill

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | No shadow | Page background |
| Subtle | `0 1px 2px rgba(0,0,0,0.15), 0 0 1px rgba(0,0,0,0.19)` | Card at rest (dual hairline) |
| Hover | `0 4px 8px rgba(0,0,0,0.09), 0 0 1px rgba(0,0,0,0.09)` | Card hover |
| Elevated | `0 8px 16px rgba(0,0,0,0.09), 0 0 1px rgba(0,0,0,0.09)` | Popovers, dropdowns |

**Shadow Philosophy**: Park UI follows Radix Themes' dual-layer shadow pattern — a soft outer shadow for atmospheric depth + a `1px` near-shadow for crisp edge definition. This prevents fuzzy-edged cards while keeping the lift soft.

## 7. Do's and Don'ts

### Do
- Use Radix color tokens (`--colors-jade-9`) — never hardcoded hex
- Default to `4px` radius for buttons/inputs, `6px` for cards
- Use the two-weight Outfit system (400 body, 600 UI/headings)
- Apply dual-layer shadows — outer glow + 1px inner definition
- Pick one accent scale per theme (jade, violet, ruby) — don't mix

### Don't
- Don't use pill radius (`9999px`) on buttons — Park UI is `4px`
- Don't use `weight 500` — it's not in the two-weight system
- Don't mix multiple accent scales in one theme — disruptive
- Don't override individual tokens — swap the scale at the `[data-theme]` level
- Don't use DaisyUI-style vibrant color combinations — Park UI is neutral-first

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| sm | `640px+` | 2-column card grids |
| md | `768px+` | 3-column features |
| lg | `1024px+` | Full desktop, docs sidebar |
| xl | `1280px+` | Max-width applies |

### Touch Targets
- Buttons: `36px` minimum (height via Radix sizing)
- Icon buttons: `36px × 36px`

### Collapsing Strategy
- Hero: 60px → 40px → 32px
- Sidebar: visible → collapsible → drawer
- Cards: 3-col → 2-col → stacked

## 9. Agent Prompt Guide

### Quick Color Reference (default neutral theme)
- Background: `#fcfcfc` (neutral-1)
- Surface: `#ffffff`
- Text: `#202020` (neutral-12)
- Muted text: `#646464` (neutral-11)
- Border: `#d9d9d9` (neutral-6)
- Primary solid: `#000000`

### Example Component Prompts
- "Create a hero: white bg. Headline at 60px Outfit weight 700, letter-spacing -1.2px, line-height 1.10, color #202020. Subtitle at 20px Outfit weight 400 color #646464. Solid button: #000000 bg, white text, 4px radius, 0 24px padding, 36px height, 14px Outfit weight 600."
- "Design a card: white bg, 1px solid #d9d9d9, 6px radius, 24px padding, box-shadow 0 1px 2px rgba(0,0,0,0.15), 0 0 1px rgba(0,0,0,0.19). Title at 24px Outfit weight 600. Body at 16px weight 400 color #646464."
- "Build a subtle button: rgba(0,0,0,0.06) bg, #202020 text, 4px radius, 0 12px padding, 36px height, 14px Outfit weight 600. Hover: rgba(0,0,0,0.1)."

### Iteration Guide
1. Radix tokens are the source of truth — never hardcode colors
2. `4px` radius for interactive elements, `6px` for containers — the Park UI rhythm
3. Two-weight typography (400/600) — resist weight 500
4. Dual-layer shadows (`outer + 1px inner`) — keeps card edges crisp
5. Pick ONE accent scale per theme — neutral + jade, neutral + violet, never both
6. Button height is always `36px` — sized through Radix's size scale
