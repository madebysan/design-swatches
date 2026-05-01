---
slug: once-ui
name: Once UI
url: https://once-ui.com
domain: once-ui.com
category: Design System
styles: [Dark, Minimal, Bold]
tagline: "Charcoal canvas, Geist at weight 300, emerald glow where shadows would be."
fonts: [Geist, Geist Mono]
primary_color: "#08a97c"
---

# Design System Inspired by Once UI

> Charcoal canvas, Geist at weight 300, emerald glow where shadows would be.

## 1. Visual Theme & Atmosphere

Once UI is the design system that treats dark mode as home. The homepage opens on a deep charcoal canvas (`#0a0a0a`) with a signature **emerald-teal** brand color (`#08a97c`) that glows faintly — an atmospheric green suggesting growth, engineering precision, and the polish of a product the team ships themselves. Where Aceternity uses motion and Material uses tactile surfaces, Once UI uses **glow**: inset shadows, subtle color bleed, and a spatial quality that feels like Vercel-adjacent but with more personality.

Typography is **Geist** at weight 300 for display — extraordinarily light for hero headlines (80px, weight 300, `-4px` letter-spacing) — paired with **Geist Mono** at weight 300 for technical accents, labels, and data. This whisper-weight approach gives the kit an engineered feel without the heaviness of weight 700 SaaS display. Body returns to weight 400 for readability.

The defining move is Once UI's **token depth**: 16+ brand-scoped CSS variables alone (`--function-brand-600`, `--brand-border-medium`, `--brand-alpha-weak`, `--solid-inset-color-danger`), each with specific semantic roles. The system is engineered for theming — every surface, every border, every fill reads from a token that can be swapped without touching components.

**Key Characteristics:**
- Dark-first canvas (`#0a0a0a`) — light mode is a variant, not the default
- Emerald-teal brand (`#08a97c` / `#01cb90`) with a soft glow aesthetic
- Geist at weight 300 for display — whisper-weight precision
- Geist Mono at weight 300 for technical labels — signature mono treatment
- `12px` / `16px` dominant radii — generous but not soft
- Glow-based shadows (alpha blends of the brand color) — not drop shadows
- 16+ brand token variables — theming is structural
- Pill-radius buttons (`20px`) for primary interactive elements

## 2. Color Palette & Roles

### Brand Scale
- **Brand 600** (`#08a97c`): Primary brand anchor. `--function-brand-600`. Used on primary CTAs, active states, brand accents.
- **Brand 700** (`#01cb90`): Brighter variant for hover states. `--function-brand-700`.
- **Brand Border Strong** (`#56ecad`): Saturated border for selected states.
- **Brand Border Medium** (`#84f6c3`): Softer brand-colored border.
- **Brand Background Medium** (`#b4fdda`): Tinted surface for brand-themed areas.
- **Brand Alpha Weak** (`#08a97c26`): 15% brand color for hover tints.
- **Brand Alpha Strong** (`#08a97c80`): 50% brand color for focus rings.
- **Brand On Solid Strong** (`#ffffff`): Text color on filled brand surfaces.

### Neutrals (dark-first)
- **Background** (`#0a0a0a`): Primary page canvas.
- **Surface** (`#141414`): Card backgrounds.
- **Surface Elevated** (`#1a1a1a`): Hover/lifted surfaces.
- **Border Neutral** (`#292929`): Hairline borders.
- **Text Primary** (`#ffffff`): Headings, emphasized text.
- **Text Secondary** (`#d2d2d2`): Body text.
- **Text Muted** (`#959595`): Captions, labels.
- **Text Disabled** (`#595959`): Disabled states.

### Semantic States
- **Danger** (`#ff5f53`): Destructive actions.
- **Danger Inset** (`#ff5f5380`): 50% alpha for backgrounds.
- **Success** (`#0a8637`): Confirmation badges.

## 3. Typography Rules

### Font Family
- **Primary**: `Geist`, fallback: `ui-sans-serif, system-ui, sans-serif`
- **Monospace**: `Geist Mono`, fallback: `ui-monospace, monospace`
- Once UI uses **weight 300** as the signature display weight — unusual; most kits start at 400 or 500

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Hero | Geist | 80px | 300 | 1.03 | -4px |
| Display Large | Geist | 48px | 300 | 1.08 | -1.44px |
| H1 | Geist | 40px | 600 | 1.15 | -0.8px |
| H2 | Geist | 32px | 600 | 1.20 | normal |
| H3 | Geist | 24px | 500 | 1.30 | normal |
| Body Large | Geist | 18px | 400 | 1.50 | normal |
| Body | Geist | 16px | 400 | 1.50 | normal |
| Mono Large | Geist Mono | 18px | 300 | 1.40 | normal |
| Mono | Geist Mono | 14px | 400 | 1.43 | normal |
| Mono Small | Geist Mono | 12px | 300 | 1.33 | normal |

### Principles
- **Weight 300 is the signature**: At display sizes, weight 300 with `-4px` tracking creates a whisper-weight hero treatment — ethereal, engineered.
- **Weight 600 for section headlines**: H1/H2 shift to weight 600 for emphasis — the jump from 300 to 600 is deliberate, dramatic.
- **Geist Mono at weight 300**: Once UI uses mono at light weight for a distinct technical aesthetic — ultra-modern, slightly sci-fi.
- **Arial fallback at 20px**: The scan showed Arial appearing at 20px and 13.33px — system font fallback for icon-adjacent elements.

## 4. Component Stylings

### Buttons
- **Primary**: `#0a0a0a` or brand color bg, `#ffffff` text, `20px` radius (pill-ish), `8px 12px` padding, 14px weight 500.
- **Ghost**: transparent bg, `#ffffff` text, `1px solid #292929`, `20px` radius.
- **Brand**: `#08a97c` bg, `#ffffff` text, `20px` radius, subtle green glow on hover.

### Cards
- `#141414` bg, `1px solid #292929`, `12px` radius, `24px` padding.
- Shadow: `0 0 20px rgba(8,169,124,0.15)` — subtle brand glow, not drop shadow.
- Elevated variant: `16px` radius with `0 0 40px rgba(8,169,124,0.25)` glow.

### Inputs
- `#1a1a1a` bg, `1px solid #292929`, `12px` radius, `8px 12px` padding.
- Focus: `1px solid #08a97c` with `0 0 0 2px rgba(8,169,124,0.25)` brand ring.
- Placeholder: `#595959`.

### Badges
- `9999px` radius (full pill), `2px 10px` padding, 12px Geist Mono weight 400.
- Variants: brand (green), neutral (gray), danger (red).

### Menus / Dropdowns
- `#141414` bg, `1px solid #292929`, `12px` radius.
- Shadow: `0 8px 32px rgba(0,0,0,0.5), 0 0 20px rgba(8,169,124,0.1)`.

## 5. Layout Principles

### Spacing System
- Base unit: **4px**
- Dominant values: `8px` (103 uses), `4px` (77), `12px` (35), `16px` (29)
- Slightly denser than Material, comparable to shadcn

### Grid
- 12-column with `24px` gutters
- Max content width: `1280px`
- Marketing: centered hero, card grids below
- App UI: sidebar `256px` + content

### Border Radius Scale
- Sharp (`4px`): Avoided — Once UI doesn't use below 6px
- Compact (`6-8px`): Small buttons, chips, badges
- Standard (`12px`): Inputs, dropdowns, small cards — the workhorse
- Comfortable (`16px`): Cards, modals, featured surfaces
- Pill (`20px`): Buttons — the brand signature
- Full (`9999px`): Badges, pills, avatars

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | No shadow | Background surfaces |
| Glow 1 | `0 0 20px rgba(8,169,124,0.1)` inset | Subtle brand glow on hover |
| Glow 2 | `0 0 20px rgba(8,169,124,0.15)` | Card ambient lift |
| Glow 3 | `0 0 40px rgba(8,169,124,0.25)` | Featured surface, brand-moment |
| Modal | `0 20px 60px rgba(0,0,0,0.6), 0 0 40px rgba(8,169,124,0.2)` | Dialogs, command palette |

**Shadow Philosophy**: Once UI treats shadows as **glow** — alpha-blended brand color emissions, not neutral gray drop shadows. The effect is atmospheric rather than spatial: elements don't sit above the surface, they emit from it. This reads especially well in dark mode, where the emerald glow feels like a deliberate light source. In light mode, the same pattern applies but with reduced intensity.

## 7. Do's and Don'ts

### Do
- Design for dark mode first — build the light variant by inverting tokens, not restyling
- Use Geist at weight 300 for hero displays with `-4px` letter-spacing
- Use Geist Mono at weight 300 for technical labels and captions
- Apply brand glow (`rgba(8,169,124,0.15)`) for elevation, not drop shadows
- Use `12px` for inputs/cards, `20px` for buttons — the Once UI rhythm
- Read from brand tokens (`--function-brand-600`), never hardcode hex

### Don't
- Don't use neutral drop shadows — breaks the glow aesthetic
- Don't use weight 700 for display — Once UI uses 300 for hero impact
- Don't skip Geist Mono on labels — the mono-at-weight-300 IS part of the brand
- Don't use border-radius below 6px — Once UI is rounded
- Don't override individual brand tokens — change the token, let the system update

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | Single column, nav becomes drawer |
| md | `768px+` | 2-column grids |
| lg | `1024px+` | Full desktop layout, sidebar visible |
| xl | `1280px+` | Max content width |

### Touch Targets
- Buttons: `40px` minimum height
- Icon buttons: `36px × 36px`

### Collapsing Strategy
- Hero: 80px → 56px → 40px across breakpoints, weight 300 maintained
- Sidebar: visible → collapsible → overlay drawer
- Cards: 3-col → 2-col → stacked
- Glow intensity: unchanged — Once UI keeps its atmospheric quality on mobile

## 9. Agent Prompt Guide

### Quick Color Reference
- Background: `#0a0a0a`
- Surface: `#141414`
- Border: `#292929`
- Text: `#ffffff` (primary), `#959595` (muted)
- Brand: `#08a97c` (600), `#01cb90` (700)
- Brand glow: `rgba(8,169,124,0.15)` — 15% alpha emerald

### Example Component Prompts
- "Create a hero section on #0a0a0a. Headline at 80px Geist weight 300, letter-spacing -4px, line-height 1.03, color #ffffff. Subtitle 18px weight 400 color #d2d2d2. Primary button: #08a97c bg, white text, 20px radius, 10px 20px padding, 14px weight 500, box-shadow 0 0 20px rgba(8,169,124,0.3) on hover."
- "Design a card: #141414 bg, 1px solid #292929, 12px radius, 24px padding, box-shadow 0 0 20px rgba(8,169,124,0.1). Title at 24px Geist weight 500, letter-spacing -0.5px, color #ffffff. Body at 16px weight 400 color #d2d2d2."
- "Build an input: #1a1a1a bg, 1px solid #292929, 12px radius, 8px 12px padding, 14px Geist weight 400, color #ffffff. Focus: 1px solid #08a97c, box-shadow 0 0 0 2px rgba(8,169,124,0.25)."

### Iteration Guide
1. Start dark — light mode is a token flip, not a different design
2. Weight 300 with `-4px` tracking is the signature hero treatment
3. Glow (`rgba(8,169,124,0.15)`) is the elevation — avoid black shadows
4. Geist Mono at weight 300 for labels — it's the technical voice
5. Brand tokens drive everything — resist hardcoding
6. `20px` radius buttons, `12px` inputs, `16px` featured cards — the Once UI rhythm
