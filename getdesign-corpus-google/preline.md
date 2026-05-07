---
version: alpha
name: Preline
description: Mainstream Tailwind SaaS design system with 840+ components, white canvas, blue-500 accent, and 8/12px radii — refined defaults, never opinionated.

colors:
  # Surface
  background: "#ffffff"
  surface-muted: "#f3f4f6"

  # Text
  ink: "#111827"
  text-secondary: "#374151"
  text-muted: "#6b7280"

  # Borders
  border: "#e5e7eb"
  border-strong: "#d1d5db"
  border-soft: "#bfdbfe"

  # Brand
  primary: "#3b82f6"
  primary-hover: "#2563eb"
  primary-soft: "#eff6ff"
  on-primary: "#ffffff"

  # Semantic
  success: "#10b981"
  success-bg: "#ecfdf5"
  warning: "#f59e0b"
  error: "#ef4444"
  info: "#06b6d4"

  # Algolia branded helpers
  algolia-primary: "#5468ff"
  hit-color: "#4b5563"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1.8px
  display-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: 0px
  h1:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0px
  h2:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0px
  h3:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  code:
    fontFamily: "Kode Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 14px
  xl: 16px
  2xl: 24px
  3xl: 32px

rounded:
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  pill: 9999px

components:
  # Buttons
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 16px
  button-soft:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 16px
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 16px
  button-ghost-hover:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.ink}"
  button-danger:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 16px

  # Cards
  card:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Inputs
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
  input-error:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Dropdowns
  dropdown:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 8px 12px

  # Badges
  badge-soft:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-solid:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 8px

  # Alerts
  alert:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 16px

  # Navbar
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.text-secondary}"
    typography: "{typography.button}"
    padding: 8px 12px
---

# Preline Design System

## Overview

Preline is the design system that ships SaaS by Friday. The homepage is a gallery of 840+ Tailwind components — marketing heroes, pricing tables, admin dashboards, empty states — each one polished to production quality and ready for copy-paste. The aesthetic is deliberately mainstream: white canvas (`{colors.background}`), near-black text (`{colors.ink}`), and a steady blue (`{colors.primary}`) that signals interaction without demanding attention. This is Tailwind's default idiom, refined.

Typography is **Inter** (used via `ui-sans-serif` system stack) with weight 700 at display sizes and `-1.8px` letter-spacing — standard modern SaaS. Code is rendered in **Kode Mono** (a less-common choice than Geist Mono or JetBrains Mono) which gives docs and API snippets a subtly retro feel. The character of Preline isn't typographic innovation — it's the completeness of the component coverage.

What distinguishes Preline is **scale**: 840+ individual components organized across marketing sections, application UI, and admin dashboards. Radii tend to `8px` (157 elements) and `12px` (144 elements) — a mid-range that avoids both shadcn's sharpness and Material's softness. Shadows are present but subtle — SaaS-appropriate drop shadows that lift cards without drama.

**Key Characteristics:**
- Inter typeface (ui-sans-serif) with weight 700 at display — modern SaaS
- Blue `{colors.primary}` as the sole interactive accent — Tailwind's blue-500
- `8px` / `12px` dominant radii — mid-range, mainstream
- 840+ components across marketing, app UI, and admin
- Kode Mono for code blocks — subtly retro
- Subtle SaaS shadows (`0 1px 2px`, `0 4px 6px`)
- Works with Alpine.js, Astro, or vanilla HTML — framework-agnostic
- Preline UI Pro: 1100+ additional components for commercial use

## Colors

### Core
- **Primary Blue** (`{colors.primary}`): Primary CTAs, links, active states. Tailwind blue-500.
- **Primary Hover** (`{colors.primary-hover}`): Darker blue on hover. Tailwind blue-600.
- **Primary Light** (`{colors.primary-soft}`): Subtle blue background tint. Tailwind blue-50.
- **Gray 900** (`{colors.ink}`): Primary text, headings.
- **Gray 700** (`{colors.text-secondary}`): Secondary text, form labels.
- **Gray 500** (`{colors.text-muted}`): Muted text, placeholders.
- **Gray 300** (`{colors.border-strong}`): Strong borders, disabled text.
- **Gray 200** (`{colors.border}`): Default borders, dividers.
- **Gray 100** (`{colors.surface-muted}`): Muted surface.
- **White** (`{colors.background}`): Primary canvas.

### Semantic States
- **Success** (`{colors.success}`): Confirmation badges (emerald-500).
- **Success BG** (`{colors.success-bg}`): Success surface.
- **Warning** (`{colors.warning}`): Caution states (amber-500).
- **Error** (`{colors.error}`): Destructive actions (red-500).
- **Info** (`{colors.info}`): Informational highlights (cyan-500).

### CSS Variables (from scanned docs)
- `--color-navbar`: `{colors.background}`
- `--docsearch-primary-color`: `{colors.primary}`
- `--docsearch-logo-color`: `{colors.algolia-primary}` (Algolia-branded)
- `--docsearch-hit-color`: `{colors.hit-color}`

## Typography

### Font Family
- **Primary**: `Inter, ui-sans-serif, system-ui, -apple-system, sans-serif` — Inter is the implicit default.
- **Monospace**: `Kode Mono, ui-monospace, monospace` — a slightly whimsical mono.
- **Serif (accent)**: `Domine, serif` — rarely used, reserved for editorial content.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | Largest hero — Inter weight 700 at 72px |
| `display-large` | Secondary hero, full-width section heads |
| `h1` | Primary page headings |
| `h2` | Section headings |
| `h3` | Sub-section headings |
| `body-large` | Intro paragraphs, lead text |
| `body` | Standard reading text |
| `button` | Button labels, UI controls |
| `caption` | Small text, metadata |
| `code` | Code snippets |

### Principles
- **Weight 700 for display, 600 for sub-heads**: Standard two-weight hierarchy.
- **No letter-spacing below 24px**: Tracking returns to normal at body sizes.
- **Kode Mono for code only**: Inline `<code>` and fenced code blocks — not for data tables.
- **Inter fallback via ui-sans-serif**: Preline intentionally avoids importing Inter from Google Fonts; it lets the system pick up Inter where installed, falls back to San Francisco / Segoe UI otherwise.

## Layout

### Spacing System
Base unit is **4px** (Tailwind-aligned). Dominant values: `lg` (14px) is unusual and Preline-distinct, between shadcn (6–10px) and Material (24px).

### Grid
- Marketing: 12-column with 24px gutters, max 1280px
- Admin: sidebar 256px + content with 32px padding
- Pricing: 3-column with equal heights, centered highlight card scales `1.05`

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow | Page background |
| Level 1 | `0 1px 2px rgba(0,0,0,0.05)` | Card at rest |
| Level 2 | `0 4px 6px -1px rgba(0,0,0,0.1)` | Card hover, popover |
| Level 3 | `0 10px 15px -3px rgba(0,0,0,0.1)` | Modal, dropdown |
| Level 4 | `0 20px 25px -5px rgba(0,0,0,0.1)` | Notification, toast |

**Shadow Philosophy**: Preline uses Tailwind's default shadow scale exactly — soft, neutral, mainstream. Shadows stay on the lighter end of the spectrum, suitable for light backgrounds. Dark mode adjusts shadow opacity but keeps the offsets identical.

## Shapes

| Token | Value | Use |
|---|---|---|
| `sm` | 6px | Badges, small chips |
| `md` | 8px | Buttons, inputs, dropdowns — the workhorse |
| `lg` | 12px | Cards, alerts — the default for larger surfaces |
| `xl` | 16px | Feature cards, testimonials |
| `pill` | 9999px | Avatars, status pills (sparingly) |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (`{components.button-primary}`, `{components.card}`) rather than reconstructing them.

### Buttons
- **`button-primary`** — Blue-500 fill, white text, 8px radius. Hover transitions to blue-600.
- **`button-secondary`** — White surface, 1px gray-200 border, gray-900 text. Quiet baseline.
- **`button-soft`** — Tinted blue-50 surface, blue-500 text. Soft secondary actions.
- **`button-ghost`** — Transparent, gray-900 text. Hover: gray-100 background.
- **`button-danger`** — Red-500 fill for destructive actions.
- Size variants: xs (28px), sm (32px), md (40px), lg (48px), xl (56px).

### Cards
- **`card`** — White surface, 12px radius, 24px padding. Subtle `0 1px 2px` shadow at rest.
- Card with image: image top corners 12px radius, content below.

### Inputs
- **`input`** — White surface, 1px gray-300 border, 8px radius, 12px 16px padding.
- **`input-focus`** — 2px primary border with 3px tinted ring.
- **`input-error`** — 2px error border.

### Dropdowns / Menus
- **`dropdown`** — White surface, 1px gray-200 border, 8px radius, lifted shadow.
- Items: 8px 12px padding, hover gray-100.

### Badges
- **`badge-soft`** — Blue-50 surface, blue-500 text, blue-200 border.
- **`badge-solid`** — Blue-500 surface, white text.
- **`badge-success`** — Success surface, success text.

### Alerts
- **`alert`** — 12px radius, 16px padding, accent border-left 4px. Icon + content + close.

## Do's and Don'ts

### Do
- Use `8px` radius for buttons, `12px` for cards — the Preline rhythm
- Default to blue-500 (`{colors.primary}`) for interactive accents
- Use soft button variants (`{components.button-soft}`) for secondary actions
- Apply subtle SaaS shadows (`shadow-sm`, `shadow-md`) on hover
- Use Kode Mono for inline code and code blocks
- Pair components from the same Preline family (marketing with marketing, admin with admin)

### Don't
- Don't use vibrant/brand colors beyond the blue — Preline is deliberately mainstream
- Don't use pill radius (`9999px`) on buttons — stays `8px`
- Don't skip the focus ring — Preline maintains Tailwind's accessibility defaults
- Don't use Geist or SF — stick with the system Inter stack
- Don't add motion — Preline is static by default, interactivity via Alpine/Astro

## Responsive Behavior

### Breakpoints (Tailwind)
| Name | Width | Changes |
|---|---|---|
| sm | `640px+` | 2-column forms, horizontal nav |
| md | `768px+` | 3-column marketing grids |
| lg | `1024px+` | Full desktop, admin sidebar visible |
| xl | `1280px+` | Max-width applies, dense dashboards |

### Touch Targets
- Button `sm` (32px) minimum
- Nav links `44px` with adequate padding

### Collapsing Strategy
- Hero: 72px → 48px → 36px
- Nav: horizontal → hamburger with slide-over drawer
- Admin sidebar: visible → collapsible → overlay drawer
- Pricing: 3-col → stacked with highlight on top

## Agent Prompt Guide

### Quick Color Reference
- Primary: `{colors.primary}` (blue-500)
- Primary hover: `{colors.primary-hover}` (blue-600)
- Text: `{colors.ink}` (gray-900)
- Muted text: `{colors.text-muted}` (gray-500)
- Border: `{colors.border}` (gray-200)
- Surface: `{colors.background}`
- Muted surface: `{colors.surface-muted}` (gray-100)

### Example Component Prompts
- "Create a hero: white bg, 72px Inter weight 700 letter-spacing -1.8px, color `{colors.ink}`. Subtitle 18px weight 400 color `{colors.text-muted}`. Primary CTA: `{colors.primary}` bg, `{colors.on-primary}` text, 8px radius, 12px 24px padding, 14px weight 500."
- "Design a pricing card: white bg, 1px solid `{colors.border}`, 12px radius, 24px padding, shadow-sm. Title 20px weight 600. Price 48px weight 700 color `{colors.ink}`. Feature list with check icons. Highlighted variant: 2px solid `{colors.primary}`, scale(1.05)."
- "Build an admin sidebar: 256px wide, white bg, 1px solid `{colors.border}` right border. Nav links 14px weight 500 color `{colors.text-secondary}`, active state bg `{colors.primary-soft}` text `{colors.primary}` with 4px left border."

### Iteration Guide
1. Preline's aesthetic is mainstream Tailwind — don't over-design
2. Blue-500 is the only brand color — resist adding more accents
3. Cards get `12px` radius; buttons/inputs get `8px`
4. Use soft button variants for secondary actions — keeps the UI quiet
5. For dark mode, swap base to `#0f172a` and keep the same radius/spacing
6. Pair Preline with Alpine.js for interactivity — it's the intended dance partner
