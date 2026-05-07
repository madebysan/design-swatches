---
version: alpha
name: Once UI
description: Dark-first design with emerald-teal brand glow, Geist at weight 300 for whisper-weight display type, and atmospheric brand-color shadows instead of neutral drop shadows.

colors:
  # Canvas (dark-first)
  background: "#0a0a0a"
  surface: "#141414"
  surface-elevated: "#1a1a1a"

  # Ink
  ink: "#ffffff"
  ink-inverted: "#0a0a0a"
  text-secondary: "#d2d2d2"
  text-muted: "#959595"
  text-disabled: "#595959"

  # Brand scale
  primary: "#08a97c"  # brand 600
  primary-hover: "#01cb90"  # brand 700
  on-primary: "#ffffff"
  brand-border-strong: "#56ecad"
  brand-border-medium: "#84f6c3"
  brand-background-medium: "#b4fdda"
  brand-alpha-weak: "#1a3329"  # was rgba(8,169,124,0.15) — flattened over #0a0a0a
  brand-alpha-strong: "#085541"  # was rgba(8,169,124,0.5) — flattened over #0a0a0a
  brand-glow: "#1a3329"  # was rgba(8,169,124,0.15) glow — flattened opaque approx

  # Borders
  border: "#292929"

  # Semantic
  danger: "#ff5f53"
  danger-inset: "#852f2a"  # was rgba(255,95,83,0.5) — flattened over #0a0a0a
  success: "#0a8637"

typography:
  display-hero:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 80px
    fontWeight: 300
    lineHeight: 1.03
    letterSpacing: -4px
  display-large:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -1.44px
  h1:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.8px
  h2:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0px
  h3:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0px
  body-large:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0px
  mono-large:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0px
  mono:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  mono-small:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.33
    letterSpacing: 0px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px
  5xl: 96px

rounded:
  none: 0px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  pill-button: 20px
  pill: 9999px

components:
  # Primary brand button
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill-button}"
    padding: 8px 12px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"

  # Ghost button
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill-button}"
    padding: 8px 12px

  # Solid dark button (alternate primary)
  button-solid:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill-button}"
    padding: 8px 12px

  # Card
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-elevated:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px

  # Input
  input:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"

  # Badge
  badge:
    backgroundColor: "{colors.brand-alpha-weak}"
    textColor: "{colors.primary}"
    typography: "{typography.mono-small}"
    rounded: "{rounded.pill}"
    padding: 2px 10px
  badge-danger:
    backgroundColor: "{colors.danger-inset}"
    textColor: "{colors.danger}"
    typography: "{typography.mono-small}"
    rounded: "{rounded.pill}"
    padding: 2px 10px
  badge-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.mono-small}"
    rounded: "{rounded.pill}"
    padding: 2px 10px
---

# Once UI Design System

## Overview

Once UI is the design system that treats dark mode as home. The homepage opens on a deep charcoal canvas (`{colors.background}`) with a signature **emerald-teal** brand color (`{colors.primary}`) that glows faintly — an atmospheric green suggesting growth, engineering precision, and the polish of a product the team ships themselves. Where Aceternity uses motion and Material uses tactile surfaces, Once UI uses **glow**: inset shadows, subtle color bleed, and a spatial quality that feels like Vercel-adjacent but with more personality.

Typography is **Geist** at weight 300 for display — extraordinarily light for hero headlines (80px, weight 300, `-4px` letter-spacing) — paired with **Geist Mono** at weight 300 for technical accents, labels, and data. This whisper-weight approach gives the kit an engineered feel without the heaviness of weight 700 SaaS display. Body returns to weight 400 for readability.

The defining move is Once UI's **token depth**: 16+ brand-scoped CSS variables alone (`--function-brand-600`, `--brand-border-medium`, `--brand-alpha-weak`, `--solid-inset-color-danger`), each with specific semantic roles. The system is engineered for theming — every surface, every border, every fill reads from a token that can be swapped without touching components.

**Key Characteristics:**
- Dark-first canvas (`{colors.background}`) — light mode is a variant, not the default
- Emerald-teal brand (`{colors.primary}` / `{colors.primary-hover}`) with a soft glow aesthetic
- Geist at weight 300 for display — whisper-weight precision
- Geist Mono at weight 300 for technical labels — signature mono treatment
- `12px` / `16px` dominant radii — generous but not soft
- Glow-based shadows (alpha blends of the brand color) — not drop shadows
- 16+ brand token variables — theming is structural
- Pill-radius buttons (`20px`) for primary interactive elements

## Colors

### Brand Scale
- **Brand 600** (`{colors.primary}`): Primary brand anchor. Used on primary CTAs, active states, brand accents.
- **Brand 700** (`{colors.primary-hover}`): Brighter variant for hover states.
- **Brand Border Strong** (`{colors.brand-border-strong}`): Saturated border for selected states.
- **Brand Border Medium** (`{colors.brand-border-medium}`): Softer brand-colored border.
- **Brand Background Medium** (`{colors.brand-background-medium}`): Tinted surface for brand-themed areas.
- **Brand Alpha Weak** (`{colors.brand-alpha-weak}`): Flattened approximation of 15% brand color for hover tints.
- **Brand Alpha Strong** (`{colors.brand-alpha-strong}`): Flattened approximation of 50% brand color for focus rings.
- **Brand On Solid Strong** (`{colors.on-primary}`): Text color on filled brand surfaces.

### Neutrals (dark-first)
- **Background** (`{colors.background}`): Primary page canvas.
- **Surface** (`{colors.surface}`): Card backgrounds.
- **Surface Elevated** (`{colors.surface-elevated}`): Hover/lifted surfaces.
- **Border Neutral** (`{colors.border}`): Hairline borders.
- **Text Primary** (`{colors.ink}`): Headings, emphasized text.
- **Text Secondary** (`{colors.text-secondary}`): Body text.
- **Text Muted** (`{colors.text-muted}`): Captions, labels.
- **Text Disabled** (`{colors.text-disabled}`): Disabled states.

### Semantic States
- **Danger** (`{colors.danger}`): Destructive actions.
- **Danger Inset** (`{colors.danger-inset}`): Flattened approximation of 50% alpha for backgrounds.
- **Success** (`{colors.success}`): Confirmation badges.

## Typography

### Font Family
- **Primary**: `Geist`, fallback: `ui-sans-serif, system-ui, sans-serif`
- **Monospace**: `Geist Mono`, fallback: `ui-monospace, monospace`
- Once UI uses **weight 300** as the signature display weight — unusual; most kits start at 400 or 500

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-hero` | 80px hero, whisper-weight 300, `-4px` tracking |
| `display-large` | 48px secondary hero |
| `h1` | Section headlines, weight 600 |
| `h2` | Sub-section headlines |
| `h3` | Card titles |
| `body-large` | Lead paragraphs |
| `body` | Standard reading text |
| `button` | Button labels |
| `mono-large` | Featured mono labels |
| `mono` | Standard mono caption |
| `mono-small` | Tags, badges, dense labels |

### Principles
- **Weight 300 is the signature**: At display sizes, weight 300 with `-4px` tracking creates a whisper-weight hero treatment — ethereal, engineered.
- **Weight 600 for section headlines**: H1/H2 shift to weight 600 for emphasis — the jump from 300 to 600 is deliberate, dramatic.
- **Geist Mono at weight 300**: Once UI uses mono at light weight for a distinct technical aesthetic — ultra-modern, slightly sci-fi.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 4px, with `sm` (8px) the dominant value.

### Grid & Container
- 12-column with 24px gutters
- Max content width: 1280px
- Marketing: centered hero, card grids below
- App UI: sidebar 256px + content

### Whitespace Philosophy
- Comfortable but engineered — never sparse
- Atmospheric depth carries the eye, not negative space alone
- Card-heavy layouts with consistent gutters

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow | Background surfaces |
| Glow 1 | `0 0 20px {colors.brand-alpha-weak}` inset | Subtle brand glow on hover |
| Glow 2 | `0 0 20px {colors.brand-glow}` | Card ambient lift |
| Glow 3 | `0 0 40px {colors.brand-alpha-strong}` | Featured surface, brand-moment |
| Modal | `0 20px 60px {colors.background}, 0 0 40px {colors.brand-alpha-strong}` | Dialogs, command palette |

**Shadow Philosophy**: Once UI treats shadows as **glow** — alpha-blended brand color emissions, not neutral gray drop shadows. The effect is atmospheric rather than spatial: elements don't sit above the surface, they emit from it. This reads especially well in dark mode, where the emerald glow feels like a deliberate light source. In light mode, the same pattern applies but with reduced intensity.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Edge-to-edge sections |
| `sm` | 6px | Small chips, micro-radii |
| `md` | 8px | Compact buttons, badges |
| `lg` | 12px | Inputs, dropdowns, small cards — the workhorse |
| `xl` | 16px | Cards, modals, featured surfaces |
| `pill-button` | 20px | Buttons — the brand signature |
| `pill` | 9999px | Badges, pills, avatars |

Once UI doesn't use sharp 4px corners — `sm` (6px) is the floor. Buttons use a distinctive `20px` pill-button radius rather than full pill, giving CTAs a softened-rectangle silhouette.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly.

### Buttons
- **`button-primary`** — Brand emerald fill with white text. Hover: brighter `{colors.primary-hover}` plus brand glow.
- **`button-ghost`** — Transparent surface with `1px solid {colors.border}` border for tertiary actions.
- **`button-solid`** — Solid dark surface for inverted CTAs in light contexts.

### Cards
- **`card`** — Standard surface card with hairline border and subtle brand glow.
- **`card-elevated`** — Larger 16px-radius variant with stronger brand glow for featured panels.

### Inputs
Surface-elevated background with hairline border and 12px radius. Focus state adds a 1px brand-color border plus `{colors.brand-alpha-strong}` ring.

### Badges
- **`badge`** — Brand-tinted pill for status/labels.
- **`badge-danger`** / **`badge-success`** — Semantic variants.

### Menus / Dropdowns
Surface card pattern with deeper modal-grade shadow stack.

## Do's and Don'ts

### Do
- Design for dark mode first — build the light variant by inverting tokens, not restyling
- Use Geist at weight 300 for hero displays with `-4px` letter-spacing
- Use Geist Mono at weight 300 for technical labels and captions
- Apply brand glow (`{colors.brand-alpha-weak}` / `{colors.brand-glow}`) for elevation, not drop shadows
- Use `{rounded.lg}` for inputs/cards, `{rounded.pill-button}` for buttons — the Once UI rhythm
- Read from brand tokens, never hardcode hex

### Don't
- Don't use neutral drop shadows — breaks the glow aesthetic
- Don't use weight 700 for display — Once UI uses 300 for hero impact
- Don't skip Geist Mono on labels — the mono-at-weight-300 IS part of the brand
- Don't use border-radius below 6px — Once UI is rounded
- Don't override individual brand tokens — change the token, let the system update

---

## Responsive Behavior

*(Preserved from original 9-section format — Google's parser keeps unknown sections.)*

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

---

## Agent Prompt Guide

*(Preserved from original 9-section format — the copy-paste payload section.)*

### Quick Color Reference
- Background: `{colors.background}`
- Surface: `{colors.surface}`
- Border: `{colors.border}`
- Text: `{colors.ink}` (primary), `{colors.text-muted}` (muted)
- Brand: `{colors.primary}` (600), `{colors.primary-hover}` (700)
- Brand glow: `{colors.brand-glow}` — flattened 15% alpha emerald

### Example Component Prompts
- "Create a hero section on `{colors.background}`. Headline at 80px Geist weight 300, letter-spacing -4px, line-height 1.03, color `{colors.ink}`. Subtitle 18px weight 400 color `{colors.text-secondary}`. Primary button: `{colors.primary}` bg, white text, 20px radius, 10px 20px padding, 14px weight 500, brand glow on hover."
- "Design a card: `{colors.surface}` bg, 1px solid `{colors.border}`, 12px radius, 24px padding, glow `{colors.brand-glow}`. Title at 24px Geist weight 500, letter-spacing -0.5px, color `{colors.ink}`. Body at 16px weight 400 color `{colors.text-secondary}`."
- "Build an input: `{colors.surface-elevated}` bg, 1px solid `{colors.border}`, 12px radius, 8px 12px padding, 14px Geist weight 400, color `{colors.ink}`. Focus: 1px solid `{colors.primary}`, ring `{colors.brand-alpha-strong}`."

### Iteration Guide
1. Start dark — light mode is a token flip, not a different design
2. Weight 300 with `-4px` tracking is the signature hero treatment
3. Glow (`{colors.brand-glow}`) is the elevation — avoid black shadows
4. Geist Mono at weight 300 for labels — it's the technical voice
5. Brand tokens drive everything — resist hardcoding
6. `20px` radius buttons, `12px` inputs, `16px` featured cards — the Once UI rhythm
