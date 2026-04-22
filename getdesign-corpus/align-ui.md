# Design System Inspired by AlignUI

## 1. Visual Theme & Atmosphere

AlignUI is the design system that was designed in Figma first and then ported to code with unusual fidelity. The homepage announces its ambition: a 80px hero at Inter Variable **weight 550** (a non-integer weight, available only because it's a variable font) with `-2.8px` letter-spacing — a combination that reads simultaneously as neutral SaaS and as engineered. The palette is a carefully calibrated gray scale (`#ebebeb`, `#2e2e2e`, `#707070`) with a **single saturated accent** — a warm orange-red (`#f05023`) — that appears sparingly as the brand anchor.

Typography is the core differentiator. AlignUI uses three font variants: `__interVar` (Inter Variable at custom weights 550), `__Inter` (standard Inter at 400/500), and `__GeistMono` for technical labels. The variable-weight 550 is the defining choice — it sits between medium and semibold, giving display type a confident presence without the blockiness of weight 600.

The component vocabulary is unusually dense: radii at `5px`, `7px`, `9px`, `11px`, `13px` — odd-number values spaced 2px apart — the scan found 30 elements at `9px` radius. This creates a radius scale with much finer granularity than shadcn's `8/10/12/14` or Material's `4/8/16/24`, enabling components that look calibrated rather than pre-built.

**Key Characteristics:**
- Inter Variable at weight 550 — the non-standard display weight that IS the brand
- Neutral gray scale (`#ebebeb`, `#2e2e2e`, `#707070`) with saturated orange (`#f05023`) accent
- Odd-numbered radii (`5, 7, 9, 11, 13px`) — 2px granularity, calibrated feel
- Subtle dual-layer shadows (`0 1px 1px rgba(51,51,51,0.04)` + `0 0 0 1px`)
- Geist Mono for technical labels at 14px weight 500 with `-0.084px` tracking
- Figma-first: the design tokens are exported from Figma, not added after
- Focus ring color `rgb(51 92 255 / 0.5)` — saturated indigo, high-visibility

## 2. Color Palette & Roles

### Neutral Scale
- **Neutral 950** (`#0a0a0a`): Primary text, headings.
- **Neutral 800** (`#2e2e2e`): Secondary text (696 occurrences).
- **Neutral 700** (`#3d3d3d`): Emphasized body text.
- **Neutral 600** (`#525252`): Muted body.
- **Neutral 500** (`#707070`): Secondary muted text (97 occurrences).
- **Neutral 400** (`#8f8f8f`): Disabled text.
- **Neutral 300** (`#b8b8b8`): Placeholders (126 occurrences).
- **Neutral 100** (`#ebebeb`): Primary border color (2,417 occurrences — by far the most-used color).
- **Neutral 50** (`#f7f7f7`): Muted surface.
- **White** (`#ffffff`): Base canvas.

### Brand
- **Accent Orange** (`#f05023`): Singular brand anchor — 48 occurrences. Used on hero accent, focused link state, brand moment.
- **Primary Blue** (`#335cff`): Interactive elements, focus rings (`rgb(51 92 255 / 0.5)` for outline).
- **Accent Light** (`#e1e9ff`): Subtle primary background tint.

### Semantic States
- **Success** (`#1fc16b`): Confirmation badges.
- **Warning** (`#f9c700`): Caution states.
- **Error** (`#e5404c`): Destructive actions.

## 3. Typography Rules

### Font Family
- **Display**: `Inter Variable` (variable font with custom weight axis — 550 is the signature).
- **Body / UI**: `Inter` (standard weights 400, 500).
- **Monospace**: `Geist Mono` (for technical labels).
- AlignUI loads three distinct font files — the variable font is reserved for display sizes only.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Hero | Inter Var | 80px | 550 | 1.05 | -2.8px |
| Display Large | Inter Var | 48px | 550 | 1.10 | -1.344px |
| H1 | Inter Var | 40px | 550 | 1.15 | -0.8px |
| H2 | Inter Var | 32px | 550 | 1.20 | -0.896px |
| H3 | Inter Var | 28px | 550 | 1.25 | -0.56px |
| Sub-heading | Inter Var | 20px | 500 | 1.30 | normal |
| Body | Inter | 16px | 400 | 1.50 | normal |
| Label Medium | Inter | 14px | 500 | 1.43 | -0.084px |
| Label Small | Geist Mono | 14px | 500 | 1.43 | -0.084px |
| Caption | Geist Mono | 11px | 500 | 1.45 | normal |

### Principles
- **Weight 550 is unique**: Only accessible through Inter Variable's weight axis. This is AlignUI's most defensible typographic choice.
- **Mixed-weight within display**: Inter Var 550 for hero/display, Inter 500 for UI chrome, Inter 400 for body.
- **Letter-spacing micro-adjustments**: The `-0.084px` tracking on 14px labels is deliberate — barely perceptible but affects rendering rhythm.
- **Geist Mono at 14px/11px**: Both caption sizes use the same font family — the size differentiates.

## 4. Component Stylings

### Buttons
- **Primary**: `#0a0a0a` bg, white text, `9px` radius, `8px 14px` padding, 14px Inter 500 tracking -0.084px.
- **Outline**: white bg, `1px solid #ebebeb`, `#0a0a0a` text, `9px` radius.
- **Secondary Bg**: `#f2f2f2` bg, `#707070` text, `7px` radius — the unusual odd-value.

### Cards
- `#ffffff` bg, `1px solid #ebebeb`, `11px` radius, `24px` padding.
- Shadow: `0 1px 1px rgba(51,51,51,0.04)` — very subtle.

### Inputs
- `#ffffff` bg, `1px solid #ebebeb`, `9px` radius, `8px 12px` padding.
- Focus: `2px solid #335cff` with `0 0 0 2px rgba(51,92,255,0.2)` ring.

### Badges
- `5px` radius (unusual — not pill), `2px 8px` padding, 12px weight 500.
- AlignUI's radius choice on badges is distinctive — small rectangles, not pills.

### Focus Ring (system-wide)
- `--tw-ring-color: rgb(51 92 255 / 0.5)` — indigo blue at 50% alpha
- `2px` thickness with `2px` offset — accessibility-compliant, high-visibility

## 5. Layout Principles

### Spacing System
- Base unit: **4px**
- Dominant: `4px` (55 uses), `8px` (22), `12px` (20), `10px` (17), `3px` (16)
- Note the `3px` use — unusual, suggests AlignUI calibrates spacing at micro-intervals too

### Grid
- 12-column with `24px` gutters
- Max content width: `1280px`
- Sidebar layouts: `256px` sidebar + content

### Border Radius Scale
- `5px`: Badges (21 uses)
- `7px`: Small buttons, chips (15 uses)
- `9px`: Default buttons, inputs (30 uses — the workhorse)
- `11px`: Cards (8 uses)
- `13px`: Featured cards (5 uses)
- `18px`: Pills, avatars
- Full (`9999px`): Switches

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | None | Background |
| Level 1 | `rgba(0,0,0,0.04) 0px 1px 2px 0px` | Card rest |
| Level 2 | `rgba(51,51,51,0.04) 0px 1px 1px 0.5px, rgba(61,61,61,0.12) 0px 0px 0px 1px` | Card with visible edge |
| Level 3 | `rgba(61,61,61,0.1) 0px 12px 24px, rgba(0,0,0,0.05) 0px 2px 4px` | Popover, dropdown |
| Level 4 | `rgba(61,61,61,0.15) 0px 20px 40px` | Modal |

**Shadow Philosophy**: AlignUI uses dual-layer shadows where the first layer is a crisp `0.5px` or `1px` near-shadow for edge definition and the second is a soft atmospheric outer shadow. The slight half-pixel values suggest Figma-native design (Figma supports sub-pixel offsets naturally).

## 7. Do's and Don'ts

### Do
- Use Inter Variable at weight 550 for display — the variable font is the brand
- Use the odd-number radius scale (`5/7/9/11/13`) — calibrated, intentional
- Apply the `-0.084px` tracking on small UI text (14px labels)
- Pair Inter with Geist Mono for captions — don't mix with other monos
- Use subtle dual-layer shadows — a crisp 1px + soft outer
- Reserve the orange accent (`#f05023`) for brand-moment use only

### Don't
- Don't use Inter at weight 500 for display — AlignUI is specifically 550
- Don't use even-number radii (`4, 8, 12`) — the odd-numbers are the signature
- Don't use dark mode without regenerating all tokens — AlignUI's palette is light-first
- Don't use pill radius on buttons — stays `9px`
- Don't skip the focus ring — the saturated indigo is a brand element

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | Single column, sidebar drawer |
| md | `768px+` | 2-column grids |
| lg | `1024px+` | Full desktop |
| xl | `1280px+` | Max-width |

### Touch Targets
- Buttons: `36px+` minimum height
- Tappable list items: `44px` minimum

### Collapsing Strategy
- Hero: 80px → 48px → 32px, weight 550 maintained
- Nav: horizontal → hamburger drawer
- Sidebar: visible → collapsible → overlay
- Cards: multi-col → stacked, `11px` radius maintained

## 9. Agent Prompt Guide

### Quick Color Reference
- Background: `#ffffff`
- Text: `#0a0a0a` (primary), `#707070` (muted)
- Border: `#ebebeb`
- Surface: `#f7f7f7`
- Primary: `#335cff`
- Accent: `#f05023`
- Focus: `rgba(51,92,255,0.5)`

### Example Component Prompts
- "Create a hero: white bg. Headline at 80px Inter Variable weight 550, letter-spacing -2.8px, line-height 1.05, color #0a0a0a. Subtitle 20px Inter weight 500 color #707070. Primary button: #0a0a0a bg, white text, 9px radius, 8px 14px padding, 14px Inter weight 500 tracking -0.084px."
- "Design a card: white bg, 1px solid #ebebeb, 11px radius, 24px padding, box-shadow 0 1px 1px rgba(51,51,51,0.04). Title 24px Inter Variable weight 550 letter-spacing -0.48px. Body 14px Inter weight 400 tracking -0.084px color #707070."
- "Build a focus ring on any interactive element: 2px solid #335cff with 2px offset, 0 0 0 2px rgba(51,92,255,0.2) secondary ring. Must be perceivable on light backgrounds."

### Iteration Guide
1. Weight 550 on Inter Variable is the display signature — no substitutes
2. Odd-number radii (`5/7/9/11/13`) — resist rounding to even numbers
3. `-0.084px` tracking on 14px UI labels — micro-calibration
4. Dual-layer shadows with `0.5-1px` inner + soft outer
5. Orange (`#f05023`) is a brand-moment color — reserve for accent surfaces
6. Focus rings are saturated indigo — accessibility as an aesthetic commitment
