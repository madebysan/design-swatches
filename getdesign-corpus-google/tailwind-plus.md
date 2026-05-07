---
version: alpha
name: Tailwind Plus
description: Editorial monochrome from Tailwind Labs — InterVariable weight 400 at 96px with -4.8px tracking, IBM Plex Mono for eyebrows, pill buttons, 12px cards, 32px heroes, inset hairline shadows.

colors:
  # Canvas + ink
  background: "#ffffff"
  surface: "#f8fafc"
  ink: "#000000"
  ink-soft: "#0a0a0a"

  # Slate scale
  slate-900: "#0f172a"
  slate-700: "#334155"
  slate-500: "#64748b"
  slate-300: "#cbd5e1"
  slate-200: "#e2e8f0"
  slate-100: "#f1f5f9"
  slate-50: "#f8fafc"

  # Brand accent
  primary: "#0ea5e9"
  primary-light: "#38bdf8"

  # Semantic
  success: "#10b981"
  warning: "#f59e0b"
  error: "#ef4444"

  # On-color
  on-primary: "#ffffff"
  on-ink: "#ffffff"

  # Borders + lines
  border: "#e2e8f0"

  # Shadow tints (opaque approximations)
  shadow-inset-rest: "#f2f2f2"  # was rgba(0,0,0,.05) — flattened over white
  shadow-inset-hover: "#ebebeb" # was rgba(0,0,0,.08) — flattened over white
  shadow-popover: "#e6e6e6"     # was rgba(0,0,0,.1) — flattened over white
  shadow-modal: "#d1d1d1"       # was rgba(0,0,0,.18) — flattened over white

typography:
  display-huge:
    fontFamily: "InterVariable, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 96px
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: -4.8px
  display-hero:
    fontFamily: "InterVariable, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-light:
    fontFamily: "InterVariable, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 300
    lineHeight: 1.10
    letterSpacing: 0px
  display-medium:
    fontFamily: "InterVariable, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 500
    lineHeight: 1.10
    letterSpacing: 0px
  h1:
    fontFamily: "InterVariable, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: -1px
  h2:
    fontFamily: "InterVariable, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: -0.6px
  body:
    fontFamily: "InterVariable, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0px
  eyebrow:
    fontFamily: "IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 1.4px
  mono-caption:
    fontFamily: "IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 1.3px
  mono-small:
    fontFamily: "IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0.3px
  button-ui:
    fontFamily: "InterVariable, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 80px
  5xl: 120px

rounded:
  none: 0px
  sm: 6px
  md: 12px
  lg: 16px
  xl: 32px
  pill: 9999px

components:
  # Primary pill button — slate-900 ground
  button-primary:
    backgroundColor: "{colors.slate-900}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 10px 20px
  button-primary-hover:
    backgroundColor: "{colors.ink}"

  # Secondary pill — white surface, slate hairline
  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.slate-900}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 10px 20px
    borderColor: "{colors.slate-200}"
  button-secondary-hover:
    backgroundColor: "{colors.slate-50}"

  # Ghost button
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.slate-700}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 10px 20px
  button-ghost-hover:
    backgroundColor: "{colors.slate-100}"

  # Circular icon button
  button-icon:
    backgroundColor: "{colors.background}"
    textColor: "{colors.slate-900}"
    rounded: "{rounded.pill}"
    size: 40px

  # Card — workhorse 12px radius, inset hairline
  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.md}"
    padding: 24px
    borderColor: "{colors.slate-200}"

  # Hero / feature panel — distinctive 32px radius
  hero-panel:
    backgroundColor: "{colors.slate-50}"
    rounded: "{rounded.xl}"
    padding: 80px

  # Pill input — filled, no rest border
  input:
    backgroundColor: "{colors.slate-50}"
    textColor: "{colors.slate-900}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 10px 16px
  input-focus:
    backgroundColor: "{colors.slate-50}"
    borderColor: "{colors.slate-900}"

  # Eyebrow / mono badge
  badge:
    backgroundColor: "{colors.slate-100}"
    textColor: "{colors.slate-700}"
    typography: "{typography.mono-caption}"
    rounded: "{rounded.pill}"
    padding: 2px 12px

  # Dropdown / menu surface
  menu:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.md}"
    padding: 8px
    borderColor: "{colors.slate-200}"
---

# Tailwind Plus Design System

## Overview

Tailwind Plus is what Tailwind Labs themselves ship when they need component libraries. The homepage is a curated gallery of 500+ marketing components, 300+ e-commerce templates, and the Catalyst React kit — all by the same team that built Tailwind CSS. The aesthetic is the platonic ideal of Tailwind: pure white canvas (`{colors.background}`), pure black text (`{colors.ink}`), Inter at weight 400 (unusual — most SaaS uses 600+) with aggressive `-4.8px` tracking at 96px display, and IBM Plex Mono for technical captions.

Typography's defining move is **weight 400 at 96px** with `-4.8px` letter-spacing. This is extraordinarily light for display sizes — most kits use 600-800 at that scale. It reads as editorial, book-like, sophisticated. Combined with `IBM Plex Mono` for eyebrow labels and captions (with positive letter-spacing of `+1.3-1.4px`), the system creates a type voice that feels more like The New York Times than a SaaS dashboard.

The defining structural choice is `{rounded.xl}` (32px) border-radius on hero sections — much larger than typical — paired with `{rounded.md}` (12px) on cards and `{rounded.pill}` on buttons. This three-tier radius (pill/medium/large) is distinctive. Shadows are almost entirely absent; the one active shadow is a subtle inset hairline.

**Key Characteristics:**
- Inter (InterVariable) at weight 400 for display — editorial, not bold
- `-4.8px` letter-spacing at 96px — the most aggressive tracking in this corpus
- IBM Plex Mono for eyebrows/captions with positive tracking — technical voice
- Pure monochrome palette (black/white/slate) + single sky accent (`{colors.primary}`)
- `{rounded.xl}` on heroes, `{rounded.md}` on cards, `{rounded.pill}` on buttons — three-tier
- Mostly no shadows — inset hairlines carry all elevation
- Includes Catalyst React UI kit — Tailwind's official component library
- Built, shipped, and maintained by Tailwind Labs themselves

## Colors

### Core
- **White** (`{colors.background}`): Canvas.
- **Black** (`{colors.ink}`): Primary text, primary button background.
- **Foreground** (`{colors.ink-soft}`): Alternative near-black for text where pure black feels heavy.

### Slate Scale
- **Slate 900** (`{colors.slate-900}`): Primary text alternative — confident dark.
- **Slate 700** (`{colors.slate-700}`): Body emphasis.
- **Slate 500** (`{colors.slate-500}`): Muted text.
- **Slate 300** (`{colors.slate-300}`): Disabled state.
- **Slate 200** (`{colors.slate-200}`): Default border.
- **Slate 100** (`{colors.slate-100}`): Muted surface.
- **Slate 50** (`{colors.slate-50}`): Very subtle surface.

### Accent
- **Sky 500** (`{colors.primary}`): Primary accent — links, occasional hover states.
- **Sky 400** (`{colors.primary-light}`): Lighter accent.

### Semantic
- **Emerald 500** (`{colors.success}`): Success.
- **Amber 500** (`{colors.warning}`): Warning.
- **Red 500** (`{colors.error}`): Error.

Tailwind Plus explicitly avoids a heavy token system, relying on Tailwind's utility classes instead — only two CSS variables ship in the scan.

## Typography

### Font Family
- **Primary**: `InterVariable`, fallback: `Inter, ui-sans-serif, system-ui, sans-serif`
- **Mono**: `IBM Plex Mono`, fallback: `ui-monospace, SFMono-Regular, Menlo, monospace`
- InterVariable is the full variable-font version of Inter, loaded once with the weight axis available 100-900.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-huge}`, `{typography.body}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-huge` | 96px landing hero — the editorial signature |
| `display-hero` | Secondary hero, large statements |
| `display-light` | Lighter weight 300 display variant |
| `display-medium` | Medium 500 display variant |
| `h1` | Section headlines |
| `h2` | Sub-section heads, card titles |
| `body` | Standard reading text |
| `eyebrow` | Uppercase IBM Plex Mono labels — "INTRODUCING CATALYST" |
| `mono-caption` | Captions, technical metadata |
| `mono-small` | Micro labels, footers |
| `button-ui` | Button labels |

### Principles
- **Weight 400 at display**: Tailwind Plus's most defensible typographic choice. Editorial feel, anti-SaaS.
- **Aggressive negative tracking**: `-4.8px` at 96px is unusual — creates a dense, engineered display block.
- **Positive tracking on mono**: `+1.3-1.4px` on IBM Plex Mono eyebrows — airy, technical.
- **Mono as category voice**: Eyebrows and captions render in IBM Plex Mono with uppercase + tracking — editorial branding.
- **InterVariable handles all weight variation**: One font file, any weight 100-900 available at runtime.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 4px (Tailwind default), with `{spacing.sm}` (8px) dominating UI chrome and `{spacing.4xl}`–`{spacing.5xl}` reserved for hero vertical padding.

### Grid & Container
- 12-column Tailwind grid
- Hero sections often full-bleed with `{spacing.4xl}`–`{spacing.5xl}` vertical padding
- Marketing features: 2-3 column with `{spacing.2xl}` gutters
- Max content width: 1440px on `2xl` breakpoint

### Whitespace Philosophy
- Tight UI chrome with generous section breathing
- `{spacing.sm}` dominance suggests dense interactive surfaces
- Hero sections breathe at `{spacing.4xl}`+ vertical

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (dominant) | None | Most static surfaces |
| Inset Hairline | `0 0 0 1px {colors.shadow-inset-rest} inset` | Card rest — subtle inner border |
| Inset Strong | `0 0 0 1px {colors.shadow-inset-hover} inset` | Hover state |
| Popover | `0 12px 28px -8px {colors.shadow-popover}` | Dropdowns, menus |
| Modal | `0 24px 48px -12px {colors.shadow-modal}` | Dialog, large overlay |

**Shadow Philosophy**: Tailwind Plus's most distinctive shadow treatment is the **inset hairline** — a subtle interior border. This creates a "cut from the background" feel without casting a drop shadow. Elevation in Tailwind Plus is the absence of shadow combined with whitespace and typographic hierarchy.

## Shapes

The system runs on a three-tier radius scale that's rare in this corpus.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved — almost never used |
| `sm` | 6px | Search inputs, small nav chrome |
| `md` | 12px | Cards, content blocks — the workhorse |
| `lg` | 16px | Testimonials, featured content |
| `xl` | 32px | Hero sections, callouts — distinctive and reserved |
| `pill` | 9999px | All buttons, inputs, chips, badges |

The combination of pill buttons, medium cards, and extra-large heroes is the Tailwind Plus shape signature.

## Components

The full component spec lives in the `components:` token block above. Reference component tokens directly (`{components.button-primary}`, `{components.card}`) rather than reconstructing them.

### Buttons
- **`button-primary`** — `{colors.slate-900}` ground, white text, `{rounded.pill}`. The default CTA.
- **`button-secondary`** — White surface with `{colors.slate-200}` hairline.
- **`button-ghost`** — Transparent until hover, `{colors.slate-700}` text.
- **`button-icon`** — 40×40 circular.

### Cards
- `{components.card}` — White surface, `{rounded.md}`, inset hairline shadow. The workhorse.

### Hero / Feature Sections
- `{components.hero-panel}` — `{rounded.xl}` radius is the largest in the system. Reserved but impactful.

### Inputs
- `{components.input}` — `{colors.slate-50}` filled background, `{rounded.pill}`, no rest border. Focus rings are 2px solid slate-900 with 3px offset.

### Badges
- `{components.badge}` — `{rounded.pill}`, IBM Plex Mono uppercase with positive tracking. Editorial treatment.

### Dropdowns / Menus
- `{components.menu}` — White surface, `{rounded.md}`, popover shadow.

## Do's and Don'ts

### Do
- Use InterVariable at weight 400 for display — the editorial voice
- Apply `-4.8px` letter-spacing at 96px — the most aggressive tracking in this corpus
- Use IBM Plex Mono with positive tracking (`+1.3-1.4px`) for eyebrows and captions
- Default to `{rounded.pill}` for buttons and inputs — the Tailwind Plus shape language
- Use `{rounded.md}` cards, `{rounded.xl}` heroes — the three-tier radius
- Apply inset hairline shadows, not drop shadows
- Keep the palette monochrome + sky accent — resist adding colors

### Don't
- Don't use weight 700+ at display — Tailwind Plus is editorial, not bold
- Don't use `ui-monospace` instead of IBM Plex Mono — the branded mono is the voice
- Don't use drop shadows on static elements — inset hairlines are the elevation
- Don't use sharp (`<8px`) radii on interactive — Tailwind Plus is fully rounded
- Don't skip the positive letter-spacing on mono text — it's the editorial gesture

---

## Responsive Behavior

### Breakpoints (Tailwind defaults)
| Name | Width | Changes |
|------|-------|---------|
| sm | `640px+` | 2-column layouts |
| md | `768px+` | 3-column features |
| lg | `1024px+` | Full desktop |
| xl | `1280px+` | Hero sections max-width |
| 2xl | `1536px+` | Max content 1440px |

### Touch Targets
- Buttons: `40-44px` minimum height via pill padding
- Icon buttons: `40px × 40px` circular

### Collapsing Strategy
- Display: 96px → 60px → 48px across breakpoints, weight 400 maintained
- Hero radius: 32px → 24px → 16px on mobile
- Marketing sections: 3-col → 2-col → stacked
- Mono captions: tracking reduces to `+0.5px` on mobile

---

## Agent Prompt Guide

### Quick Color Reference
- Background: `{colors.background}`
- Foreground: `{colors.ink-soft}` or `{colors.ink}`
- Slate primary text: `{colors.slate-900}`
- Slate muted: `{colors.slate-500}`
- Border: `{colors.slate-200}` (slate-200)
- Surface: `{colors.surface}` (slate-50)
- Accent: `{colors.primary}` (sky-500)

### Example Component Prompts
- "Create a hero: white bg, 32px radius, 80px vertical padding. Eyebrow: 'INTRODUCING CATALYST' in IBM Plex Mono 12px weight 600 tracking +1.4px color `{colors.slate-500}`. Headline: 96px InterVariable weight 400, letter-spacing -4.8px, line-height 0.95, color `{colors.ink}`. Subtitle: 20px weight 400 color `{colors.slate-700}`. Pill button: `{colors.slate-900}` bg, white text, 9999px radius, 10px 20px padding, 14px weight 500."
- "Design a card: white bg, 12px radius, 24px padding, box-shadow 0 0 0 1px `{colors.shadow-inset-rest}` inset (inset hairline, no drop shadow). Title 24px InterVariable weight 500 letter-spacing -0.6px. Body 16px weight 400 line-height 1.60 color `{colors.slate-700}`. Pill badge: IBM Plex Mono 11px weight 500 tracking +0.2px uppercase."
- "Build a pill input: `{colors.slate-50}` bg, no border at rest, 9999px radius, 10px 16px padding, 16px InterVariable weight 400 color `{colors.slate-900}`. Focus: 2px solid `{colors.slate-900}` ring with 3px offset."

### Iteration Guide
1. Weight 400 at display is the editorial signature — resist weight 600+
2. `-4.8px` tracking at 96px — aggressive, intentional
3. IBM Plex Mono with POSITIVE tracking for eyebrows — `+1.3-1.4px`
4. Three-tier radius: `{rounded.pill}` (buttons/inputs), `{rounded.md}` (cards), `{rounded.xl}` (heroes)
5. Inset hairlines (`0 0 0 1px inset`) replace drop shadows
6. Monochrome + one accent (sky blue) — resist adding palette
