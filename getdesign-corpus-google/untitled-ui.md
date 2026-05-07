---
version: alpha
name: Untitled UI
description: The polished SaaS baseline — Inter weight 600 display, purple brand scale, 1-pixel radius granularity, dual-layer slate-blue-tinted shadows, 4px focus rings, gray scale from 25 to 900.

colors:
  # Canvas + ink
  background: "#ffffff"
  surface: "#fafafa"

  # Brand purple scale
  brand-50: "#f4ebff"
  brand-100: "#e9d7fe"
  brand-200: "#d6bbfb"
  brand-300: "#b692f6"
  brand-400: "#9e77ed"
  primary: "#7f56d9"
  brand-600: "#6941c6"
  brand-700: "#53389e"
  brand-800: "#42307d"
  brand-900: "#2e2458"

  # Gray scale
  gray-25: "#fafafa"
  gray-50: "#f9fafb"
  gray-100: "#f2f4f7"
  gray-200: "#e4e7ec"
  gray-300: "#d0d5dd"
  gray-400: "#98a2b3"
  gray-500: "#525252"
  gray-600: "#475467"
  gray-700: "#344054"
  gray-800: "#1d2939"
  ink: "#181d27"

  # On-color
  on-primary: "#ffffff"

  # Semantic
  success: "#12b76a"
  success-bg: "#ecfdf3"
  warning: "#f79009"
  error: "#d92d20"
  error-bg: "#fef3f2"

  # Borders
  border: "#e4e7ec"
  border-strong: "#d0d5dd"

  # Focus ring + shadow tints (opaque approximations)
  focus-ring-brand: "#dccbf6"  # was rgba(127,86,217,.18) — flattened over white
  focus-ring-error: "#f7d3d0"  # was rgba(217,45,32,.18) — flattened over white
  shadow-xs: "#ececef"          # was rgba(16,24,40,.06) — flattened over white
  shadow-sm: "#dcdfe6"          # was rgba(16,24,40,.1) — flattened over white
  shadow-md: "#ced0d6"          # was rgba(16,24,40,.18) — flattened over white

typography:
  display-2xl:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 72px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -1.44px
  display-xl:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 60px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -1.2px
  display-lg:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.96px
  display-md:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 44px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.88px
  display-sm:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 34px
    fontWeight: 600
    lineHeight: 1.24
    letterSpacing: -0.68px
  display-xs:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0px
  text-xl:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0px
  text-lg:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.56
    letterSpacing: 0px
  text-md:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  text-sm:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  text-xs:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0px

spacing:
  micro: 1px
  micro-2: 2px
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
  thin: 1px
  xxs: 4px
  xs: 5px
  sm: 6px
  md: 8px
  lg: 10px
  xl: 12px
  2xl: 16px
  pill: 9999px

components:
  # Primary purple
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.text-sm}"
    rounded: "{rounded.md}"
    padding: 8px 14px
  button-primary-hover:
    backgroundColor: "{colors.brand-600}"

  # Secondary color (purple tint)
  button-secondary-color:
    backgroundColor: "{colors.brand-50}"
    textColor: "{colors.primary}"
    typography: "{typography.text-sm}"
    rounded: "{rounded.md}"
    padding: 8px 14px

  # Secondary gray (white surface)
  button-secondary-gray:
    backgroundColor: "{colors.background}"
    textColor: "{colors.gray-700}"
    typography: "{typography.text-sm}"
    rounded: "{rounded.md}"
    padding: 8px 14px
    borderColor: "{colors.border-strong}"

  # Tertiary color (transparent purple)
  button-tertiary-color:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.text-sm}"
    rounded: "{rounded.md}"
    padding: 8px 14px

  # Tertiary gray (transparent gray)
  button-tertiary-gray:
    backgroundColor: "{colors.background}"
    textColor: "{colors.gray-600}"
    typography: "{typography.text-sm}"
    rounded: "{rounded.md}"
    padding: 8px 14px

  # Card — workhorse 12px radius
  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.xl}"
    padding: 24px
    borderColor: "{colors.border}"

  # Input
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.text-md}"
    rounded: "{rounded.md}"
    padding: 10px 14px
    borderColor: "{colors.border-strong}"
  input-focus:
    backgroundColor: "{colors.background}"
    borderColor: "{colors.primary}"
  input-error:
    backgroundColor: "{colors.background}"
    borderColor: "{colors.error}"

  # Badge — gray default
  badge-gray:
    backgroundColor: "{colors.gray-100}"
    textColor: "{colors.gray-700}"
    typography: "{typography.text-xs}"
    rounded: "{rounded.sm}"
    padding: 2px 8px

  # Badge — brand
  badge-brand:
    backgroundColor: "{colors.brand-50}"
    textColor: "{colors.primary}"
    typography: "{typography.text-xs}"
    rounded: "{rounded.sm}"
    padding: 2px 8px

  # Badge — pill variant
  badge-pill:
    backgroundColor: "{colors.brand-50}"
    textColor: "{colors.primary}"
    typography: "{typography.text-xs}"
    rounded: "{rounded.pill}"
    padding: 2px 10px

  # Badge — success
  badge-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.text-xs}"
    rounded: "{rounded.sm}"
    padding: 2px 8px

  # Badge — error
  badge-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
    typography: "{typography.text-xs}"
    rounded: "{rounded.sm}"
    padding: 2px 8px

  # Dropdown / menu
  menu:
    backgroundColor: "{colors.background}"
    textColor: "{colors.gray-700}"
    typography: "{typography.text-md}"
    rounded: "{rounded.md}"
    padding: 4px
    borderColor: "{colors.border}"

  # Top nav bar
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.gray-700}"
    typography: "{typography.text-md}"
    padding: 16px 24px
---

# Untitled UI Design System

## Overview

Untitled UI is the most-purchased Figma kit on the planet. The homepage is a showcase of the SaaS aesthetic perfected — clean white canvas (`{colors.background}`), near-black headings (`{colors.ink}`), a rich purple brand scale (`{colors.brand-600}` → `{colors.brand-400}` → `{colors.primary}`), and the polished, competent look that has become the baseline for every B2B SaaS landing page since 2021. This is the kit that defined "shipped SaaS" — Jordan Hughes distilled the industry-standard aesthetic into 10,000+ Figma frames.

Typography is **Inter** — the SaaS typeface — with weight 600 at 48px display and `-0.96px` letter-spacing. Inter appears at every size, in every weight from 400 to 700. The choice is anti-signature: Untitled UI wants to look universally polished, not distinctively different. That's the entire value proposition — buy the kit, ship product that looks like it was designed by a ten-person team.

The distinctive attribute is Untitled UI's **radius scale**: `1px`, `4px`, `5px`, `6px`, `7px`, `8px`, `10px` — 1-pixel granularity at the small end. Combined with the dominant `{colors.gray-500}` chrome tone, the kit reads as meticulously calibrated. Every component has been drawn at multiple radii, every radius maps to a component class.

**Key Characteristics:**
- Inter typeface at weight 600 for display, weight 400 for body — universal SaaS
- Purple brand scale (50-900) with `{colors.primary}` as the primary CTA
- 1-pixel radius granularity (`{rounded.thin}` through `{rounded.lg}`) — precisely calibrated
- Shadows use SaaS-standard `rgba(16,24,40,...)` slate-blue-tinted near-black
- Gray scale from `{colors.gray-25}` to `{colors.ink}` with `{colors.gray-500}` as dominant chrome
- 10,000+ Figma components — the kit's differentiator is coverage, not novelty
- Separate React component library that mirrors the Figma exactly

## Colors

### Brand Purple Scale
- **Brand 50** (`{colors.brand-50}`): Very subtle purple tint.
- **Brand 100** (`{colors.brand-100}`): Muted purple surface.
- **Brand 200** (`{colors.brand-200}`): Light purple.
- **Brand 300** (`{colors.brand-300}`): Mid-light.
- **Brand 400** (`{colors.brand-400}`): Brand accent.
- **Brand 500** (`{colors.primary}`): Primary CTA. Default brand anchor.
- **Brand 600** (`{colors.brand-600}`): Hover/pressed state.
- **Brand 700** (`{colors.brand-700}`): Deep brand.
- **Brand 800** (`{colors.brand-800}`): Brand dark.
- **Brand 900** (`{colors.brand-900}`): Maximum depth.

### Gray Scale
- **Gray 25** (`{colors.gray-25}`): Page background variant.
- **Gray 50** (`{colors.gray-50}`): Subtle surface.
- **Gray 100** (`{colors.gray-100}`): Muted surface.
- **Gray 200** (`{colors.gray-200}`): Border default.
- **Gray 300** (`{colors.gray-300}`): Strong border.
- **Gray 400** (`{colors.gray-400}`): Placeholder.
- **Gray 500** (`{colors.gray-500}`): Secondary text — the most-used color.
- **Gray 600** (`{colors.gray-600}`): Strong secondary.
- **Gray 700** (`{colors.gray-700}`): Label text.
- **Gray 800** (`{colors.gray-800}`): Near-black heading.
- **Gray 900** (`{colors.ink}`): Primary heading.

### Semantic Colors
- **Success** (`{colors.success}`) / Surface (`{colors.success-bg}`)
- **Warning** (`{colors.warning}`)
- **Error** (`{colors.error}`) / Surface (`{colors.error-bg}`)

## Typography

### Font Family
- **Primary**: `Inter`, fallback: `ui-sans-serif, system-ui, -apple-system, sans-serif`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, monospace`

Untitled UI uses Inter exclusively — no custom typefaces, no alternates.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-lg}`, `{typography.text-md}`, etc.).

| Token | Use |
|---|---|
| `display-2xl` | 72px hero |
| `display-xl` | Section hero |
| `display-lg` | Page heading |
| `display-md` | Major section title |
| `display-sm` | Sub-section title |
| `display-xs` | Card title, prominent |
| `text-xl` | Lead paragraph |
| `text-lg` | Intro body |
| `text-md` | Standard body |
| `text-sm` | UI labels, button text, captions |
| `text-xs` | Badges, micro labels |

### Principles
- **Weight 600 across all display sizes**: Untitled UI's signature weight for hero and headlines.
- **Weight 500 for UI labels, 400 for body**: Standard two-weight UI typography.
- **Progressive letter-spacing**: `-1.44px` at 72px, `-0.68px` at 34px, normal below 24px.
- **Tailwind-friendly token names**: `Text md`, `Display lg` — easy to map to design and code.

## Layout

### Spacing System
The complete scale lives in the `spacing:` token block above. Base unit is 4px (Tailwind-aligned). Untitled UI uses 1-pixel granularity at small sizes — unusual for a Figma kit.

### Grid & Container
- 12-column with 32px gutters
- Max content widths: 1280px (standard), 1440px (wide), 1600px (max)
- Section padding: `{spacing.5xl}` desktop, `{spacing.4xl}` tablet, `{spacing.3xl}` mobile

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| XS | `0 1px 2px {colors.shadow-xs}` | Subtle card lift |
| SM | `0 1px 2px {colors.shadow-xs}, 0 1px 3px {colors.shadow-sm}` | Card rest (default) |
| MD | `0 2px 4px -2px {colors.shadow-xs}, 0 4px 8px -2px {colors.shadow-sm}` | Card hover, menu |
| LG | `0 4px 6px -2px {colors.shadow-xs}, 0 12px 16px -4px {colors.shadow-sm}` | Dropdown, popover |
| XL | `0 8px 8px -4px {colors.shadow-xs}, 0 20px 24px -4px {colors.shadow-sm}` | Modal |
| 2XL | `0 24px 48px -12px {colors.shadow-md}` | Large modal, hero images |
| Focus Ring Brand | `0 0 0 4px {colors.focus-ring-brand}` | Input/button keyboard focus |
| Focus Ring Error | `0 0 0 4px {colors.focus-ring-error}` | Error-state focus |

**Shadow Philosophy**: Untitled UI uses the SaaS-standard shadow system — dual-layer with slate-blue-tinted near-black for consistent depth. The 4px focus ring is a signature touch — more visible than shadcn's, less clinical than Atlassian's.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `thin` | 1px | Fine chrome elements |
| `xxs` | 4px | Small inline |
| `xs` | 5px | Small inline variant |
| `sm` | 6px | Badges, small images |
| `md` | 8px | Buttons, inputs — workhorse |
| `lg` | 10px | Featured cards |
| `xl` | 12px | Large cards, modals |
| `2xl` | 16px | Hero cards, callouts |
| `pill` | 9999px | Avatars, switches, occasional badges |

## Components

The full component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card}`).

### Buttons
- **`button-primary`** — Brand purple ground, white text, `{rounded.md}`. Hover deepens to brand-600.
- **`button-secondary-color`** — Brand-50 tinted surface, primary text.
- **`button-secondary-gray`** — White surface with `{colors.border-strong}` border, gray-700 text.
- **`button-tertiary-color`** — Transparent, primary text only.
- **`button-tertiary-gray`** — Transparent, gray-600 text only.
- Size variants: xs (28px), sm (32px), md (40px), lg (44px), xl (48px), 2xl (60px).

### Cards
- **`card`** — White surface, `{colors.border}` 1px, `{rounded.xl}` (12px), 24px padding, dual-layer SaaS shadow.

### Inputs
- **`input`** — White surface, `{colors.border-strong}` border, `{rounded.md}`, 10×14 padding. Focus shifts border to brand purple plus the 4px focus ring (signature). Error: red border + red ring.

### Badges
- **`badge-gray`** — Gray-100 surface, gray-700 text.
- **`badge-brand`** — Brand-50 tinted, primary text.
- **`badge-pill`** — Pill variant, brand-50 tinted.
- **`badge-success`** / **`badge-error`** — Semantic surfaces.
- Sizes: sm (22px), md (26px), lg (30px).

### Dropdowns / Menus
- **`menu`** — White surface, gray-200 border, `{rounded.md}`, 4px item padding. LG shadow.

### Navigation
- **`nav-bar`** — Standard top nav, gray-700 text, white background.

## Do's and Don'ts

### Do
- Use the brand purple scale (50-900) progressively — don't pick only `{colors.primary}`
- Apply `{rounded.md}` to buttons, `{rounded.xl}` to cards — the Untitled UI rhythm
- Use Inter weight 600 for display, weight 500 for UI labels, weight 400 for body
- Use the 4px focus ring (`0 0 0 4px {colors.focus-ring-brand}`) — the signature
- Pair with gray scale 50-900 — resist mixing with shadcn's neutrals
- Apply dual-layer SaaS shadows for elevation

### Don't
- Don't use pill radius on buttons — stays `{rounded.md}`
- Don't use weight 700 for headings — Untitled UI is weight 600
- Don't use letter-spacing on text below 24px — tracking stays normal
- Don't substitute Inter — the kit is Inter-specific
- Don't use `#000000` for text — always gray-900 (`{colors.ink}`)

---

## Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | Single column, 48px section padding |
| sm | `640px+` | 2-column layouts |
| md | `768px+` | 3-column features, tablet nav |
| lg | `1024px+` | Full desktop, 12-col grid active |
| xl | `1280px+` | Max-width applied |

### Touch Targets
- Button `sm` (32px) minimum
- Button `md` (40px) default for both touch and desktop
- Icon buttons: 40px × 40px

### Collapsing Strategy
- Display sizes: 72px → 48px → 34px across breakpoints
- Nav: horizontal → slide-over drawer on mobile
- Cards: 4-col → 2-col → single column
- Sidebars: visible → collapsible → overlay

---

## Agent Prompt Guide

### Quick Color Reference
- Brand Primary: `{colors.primary}` (brand-500)
- Brand Hover: `{colors.brand-600}`
- Brand Light: `{colors.brand-50}`
- Background: `{colors.background}`
- Surface: `{colors.surface}` (gray-25)
- Text: `{colors.ink}` (gray-900), `{colors.gray-500}`
- Border: `{colors.border}` (gray-200)

### Example Component Prompts
- "Create a hero: white bg. Headline at 60px Inter weight 600, letter-spacing -1.2px, line-height 1.10, color `{colors.ink}`. Subtitle 20px weight 500 color `{colors.gray-600}`. Primary button: `{colors.primary}` bg, white text, 8px radius, 10px 18px padding, 14px weight 600. Secondary gray: white bg, 1px solid `{colors.border-strong}`, `{colors.gray-700}` text, 8px radius."
- "Design a card: white bg, 1px solid `{colors.border}`, 12px radius, 24px padding, box-shadow `0 1px 2px {colors.shadow-xs}, 0 1px 3px {colors.shadow-sm}`. Title 20px Inter weight 600 color `{colors.ink}`. Body 14px weight 400 color `{colors.gray-600}`."
- "Build an input: white bg, 1px solid `{colors.border-strong}`, 8px radius, 10px 14px padding, 14px Inter weight 400. Focus: 1px solid `{colors.primary}` + `0 0 0 4px {colors.focus-ring-brand}` ring. Placeholder color `{colors.gray-400}`."

### Iteration Guide
1. Think in Untitled UI's gray scale — every chrome element maps to a gray 25-900 token
2. Button radius is `{rounded.md}` (8px), card radius is `{rounded.xl}` (12px) — the workhorse rhythm
3. Focus rings are 4px thick — makes them highly perceivable
4. Inter weight 600 at display, 500 for UI, 400 for body — the SaaS standard
5. Shadow tokens follow the slate-blue-black tint
6. For dark mode, invert gray scale and reduce shadow opacity by ~50%
