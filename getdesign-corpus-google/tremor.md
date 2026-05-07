---
version: alpha
name: Tremor
description: Dashboard-first system — pure white canvas, Geist 700 with tight tracking for KPIs, ui-monospace for tabular data, mint teal as a chart color only, 6-8px radii, borders for elevation, no shadows on static surfaces.

colors:
  # Canvas + ink
  background: "#ffffff"
  surface: "#ffffff"
  surface-muted: "#f1f5f9"
  ink: "#0a0a0a"
  ink-inverted: "#ffffff"

  # Text hierarchy
  on-background: "#0a0a0a"
  on-primary: "#ffffff"
  text-secondary: "#888d94"
  text-muted: "#737373"

  # Brand / data accent
  primary: "#9cd2bb"

  # Data series (charts only)
  series-blue: "#2563eb"
  series-blue-light: "#3b82f6"
  series-amber: "#f59e0b"
  series-red: "#ef4444"
  series-slate: "#475569"

  # Semantic — KPI deltas
  success: "#16a34a"
  success-bg: "#dcfce7"
  success-text: "#15803d"
  success-border: "#bbf7d0"
  error: "#dc2626"
  error-bg: "#fee2e2"
  error-text: "#b91c1c"
  warning: "#d97706"

  # Borders
  border: "#e5e5e5"

  # Subtle shadows for floating UI (opaque approximations)
  shadow-tooltip: "#f2f2f2" # was rgba(0,0,0,.05) — flattened over white
  shadow-menu: "#ebebeb"    # was rgba(0,0,0,.08) — flattened over white

typography:
  display:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -2.1px
  h1:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: -1.26px
  h2:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -1.5px
  h3:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  body:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  caption:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  button-ui:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0px
  mono:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  mono-axis:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px

rounded:
  none: 0px
  sm: 6px
  md: 8px
  lg: 12px
  pill: 9999px

components:
  # Primary button — near-black ground
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 8px 12px

  # Secondary button — white surface
  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    borderColor: "{colors.border}"

  # Ghost button
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  button-ghost-hover:
    backgroundColor: "{colors.surface-muted}"

  # Standard card — border-only elevation
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 16px
    borderColor: "{colors.border}"

  # Chart card — same treatment
  card-chart:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 16px
    borderColor: "{colors.border}"

  # KPI card — large number display
  card-kpi:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.h2}"
    rounded: "{rounded.md}"
    padding: 20px
    borderColor: "{colors.border}"

  # Input
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    borderColor: "{colors.border}"
  input-focus:
    backgroundColor: "{colors.background}"
    borderColor: "{colors.ink}"

  # Delta badge — success
  badge-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 2px 8px
    borderColor: "{colors.success-border}"

  # Delta badge — error
  badge-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error-text}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 2px 8px

  # Tooltip — only place a subtle shadow appears
  tooltip:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    borderColor: "{colors.border}"

  # Popover menu
  menu:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px
    borderColor: "{colors.border}"

  # Table header cell
  table-header:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.text-muted}"
    typography: "{typography.caption}"
    padding: 8px 12px
---

# Tremor Design System

## Overview

Tremor is the design system that looks like a spreadsheet pretending to be beautiful. The homepage is a dense grid of dashboards, KPI cards, and chart primitives rendered in a restrained palette — pure white canvas (`{colors.background}`), near-black type (`{colors.ink}`), and a signature mint-teal (`{colors.primary}`) that appears in chart data series but never in chrome. This is dashboard-first design: every surface exists to frame data, every color has to survive on a 14-color chart without losing contrast.

Typography leans on **Geist** — Vercel's sans-serif — with weight 700 at display sizes and tight `-2.1px` letter-spacing that evokes financial terminal UIs. Where Stripe uses weight 300 for whisper-weight authority, Tremor uses 700 for data-grade bold. The typeface alternates with `ui-monospace` for tabular numerals, code samples, and API references — a deliberate technical cadence.

Tremor's defining choice is its **absence of shadows**. Cards lift through `1px` borders in `{colors.border}` or subtle 6–8px rounded edges, never through drop shadow. This is intentional: shadows blur data edges and compete with chart lines. Tremor wants the chart to be the elevation.

**Key Characteristics:**
- Pure white canvas with near-black text — data-first palette
- Geist weight 700 at display, `-2.1px` letter-spacing — financial-terminal authority
- Mint teal (`{colors.primary}`) as a data accent color, never chrome
- `{rounded.sm}` / `{rounded.md}` dominant radii — restrained, spreadsheet-adjacent
- No shadows on static surfaces — borders only
- `ui-monospace` for tabular data and code — always
- Copy-paste philosophy (like shadcn) — components live in your repo
- Built on Tailwind + Recharts — fully typed, no hidden abstractions

## Colors

### Core Neutrals
- **White** (`{colors.background}`): Canvas, card surfaces, chart backgrounds.
- **Near-Black** (`{colors.ink}`): Primary text, axis labels, strong labels.
- **Slate** (`{colors.text-secondary}`): Secondary text — the most-used color on the homepage, baseline chrome tone.
- **Slate 100** (`{colors.surface-muted}`): Muted surface for table headers, disabled states.
- **Border** (`{colors.border}`): The hairline — cards, dividers, chart gridlines.

### Data Accent (charts only)
- **Mint** (`{colors.primary}`): The signature Tremor green. First series color, never interactive.
- **Blue 600** (`{colors.series-blue}`): Second series, also used for links.
- **Blue 500** (`{colors.series-blue-light}`): Third series, hover states.
- **Amber 500** (`{colors.series-amber}`): Warnings, attention series.
- **Red 500** (`{colors.series-red}`): Error bars, negative deltas.
- **Slate 600** (`{colors.series-slate}`): Secondary series, comparison data.

### Semantic Roles (KPI indicators)
- **Success** (`{colors.success}`): Positive delta badges (↑ 12.4%).
- **Error** (`{colors.error}`): Negative delta badges (↓ 3.2%).
- **Warning** (`{colors.warning}`): Caution indicators on thresholds.
- **Muted foreground** (`{colors.text-muted}`): Labels, timestamps, axis text.

## Typography

### Font Family
- **Primary**: `Geist`, fallback: `ui-sans-serif, system-ui, sans-serif`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, monospace` (no branded mono)

Tremor explicitly avoids Geist Mono in favor of system monospace — keeping the ecosystem agnostic.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display}`, `{typography.body}`, etc.).

| Token | Use |
|---|---|
| `display` | 60px hero — financial-terminal scale |
| `h1` | 36px KPI numbers |
| `h2` | Section headings |
| `h3` | Card / panel titles |
| `body-large` | Intro paragraphs |
| `body` | Standard reading |
| `caption` | Labels, metadata |
| `button-ui` | Button text |
| `mono` | Tabular data, code, IDs |
| `mono-axis` | Chart axis labels |

### Principles
- **Weight 700 for KPI numbers**: Dashboard number displays use weight 700 with tight tracking for instant legibility.
- **Monospace is non-optional**: Any tabular or technical data renders in `ui-monospace`.
- **Tight tracking above 24px**: Letter-spacing tightens aggressively from `-1.26px` at 36px to `-2.1px` at 60px.

## Layout

### Spacing System
The complete scale lives in the `spacing:` token block above. Base unit is 4px. Dominant values cluster at `{spacing.lg}` (16px), with section spacing using `{spacing.2xl}`–`{spacing.3xl}`.

### Grid & Container
- Dashboard grid: 12-column with 16–24px gutters
- KPI row: 4 cards at span-3 each on desktop
- Chart below: full-width or span-8 with span-4 legend/filter panel

### Whitespace Philosophy
- **Dense by design**: Tremor is meant for dashboards — internal padding stays compressed (12–16px)
- **Generous between sections**: `{spacing.2xl}`–`{spacing.3xl}` vertical between dashboard rows
- **Aligned to chart grid**: card padding often matches chart margin to align numbers with data

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Page background |
| Border | `1px solid {colors.border}` | Cards, inputs, chart containers — default |
| Subtle | `0 1px 3px {colors.shadow-tooltip}` | Tooltips, dropdowns only |
| Menu | `0 4px 12px {colors.shadow-menu}` | Popover menus, filter dropdowns |

**Shadow Philosophy**: Tremor deliberately has no shadow system for static UI. Shadows only appear on elements that float over data (tooltips, popovers). Cards, KPIs, and chart containers all lift through border contrast alone — keeping chart edges clean and preventing dashboard visual noise.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `sm` | 6px | Buttons, inputs — workhorse |
| `md` | 8px | Cards, chart containers |
| `lg` | 12px | Larger panels (rare) |
| `pill` | 9999px | Delta badges only — the single full-pill element |

## Components

The full component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card-kpi}`).

### Buttons
- **`button-primary`** — Near-black ground, white text, `{rounded.sm}`.
- **`button-secondary`** — White surface with `{colors.border}` 1px hairline.
- **`button-ghost`** — Transparent until hover, near-black text.

### Cards
- **`card`** — White surface, `{colors.border}` 1px, `{rounded.md}`, no shadow. The default.
- **`card-chart`** — Same treatment with chart consuming interior padding.
- **`card-kpi`** — Large number 30px Geist 700 letter-spacing -1.5px; delta badge inline; uppercase label above at 14px weight 500 with 0.04em tracking color `{colors.text-muted}`.

### Inputs
- **`input`** — White surface, `{colors.border}` 1px, `{rounded.sm}`. Focus shifts border to near-black, no ring (Tremor avoids focus rings on filter inputs to keep dashboard chrome quiet).

### Charts
- Gridlines: `{colors.border}` at 0.5 stroke
- Axis text: 12px `ui-monospace` weight 400 color `{colors.text-muted}`
- Data series: 2px stroke lines, 4px dot markers
- Tooltips: white background, 1px border, `{rounded.sm}`, slight shadow

### Badges
- **`badge-success`** — `{rounded.pill}` for deltas. The one place full-pill appears.
- **`badge-error`** — Same shape with red palette.

### Tooltip / Menu
- **`tooltip`** — Floats over data, gets the only subtle shadow.
- **`menu`** — Popover dropdown with deeper shadow.

### Tables
- **`table-header`** — Muted surface background, uppercase mono caption, `{colors.text-muted}`.

## Do's and Don'ts

### Do
- Use `{rounded.sm}`–`{rounded.md}` on cards and inputs — the workhorse
- Use Geist weight 700 with tight letter-spacing for KPI numbers
- Use `ui-monospace` (not Geist Mono) for data columns and timestamps
- Default to border-only elevation — no drop shadows on static cards
- Use the mint teal (`{colors.primary}`) ONLY in chart data series
- Use full-pill radius (`{rounded.pill}`) for delta badges only
- Keep chart gridlines subtle (`{colors.border}`, 0.5 stroke)

### Don't
- Don't use drop shadows on dashboard cards — borders are the elevation
- Don't use the mint teal as a button or link color — data only
- Don't use Geist Mono — Tremor sticks with `ui-monospace` for neutrality
- Don't use border-radius above `{rounded.lg}` (12px) on chart containers
- Don't add focus rings to filter inputs — keeps the dashboard quiet

---

## Responsive Behavior

### Breakpoints (Tailwind defaults)
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | KPIs stack single column, charts scroll horizontally |
| md | `768px+` | 2-column KPI row, full-width charts |
| lg | `1024px+` | 4-column KPI row, side-by-side chart panels |
| xl | `1280px+` | Full dashboard grid |

### Touch Targets
- Filter chips: 32px minimum height
- Icon-only buttons: 36px × 36px
- Legend swatches: 16px × 16px with 8px padding for tap

### Collapsing Strategy
- KPI cards: 4-col → 2-col → 1-col
- Charts: maintain aspect ratio, reduce internal padding 16px → 12px on mobile
- Axis labels: rotate to -45deg or abbreviate ($1.2K vs $1,200)

---

## Agent Prompt Guide

### Quick Color Reference
- Background: `{colors.background}`
- Text: `{colors.ink}` (primary), `{colors.text-muted}` (muted)
- Border: `{colors.border}`
- Data mint: `{colors.primary}`
- Data blue: `{colors.series-blue}`
- Success / Error: `{colors.success}` / `{colors.error}`

### Example Component Prompts
- "Create a KPI card: white bg, 1px solid `{colors.border}`, 8px radius, 20px padding, no shadow. Label at 14px Geist weight 500 uppercase tracking 0.04em color `{colors.text-muted}`. Value at 30px Geist weight 700 letter-spacing -1.5px color `{colors.ink}`. Delta badge inline: 12px weight 500, 9999px radius, bg `{colors.success-bg}`, text `{colors.success-text}`."
- "Design a chart container: white bg, 1px solid `{colors.border}`, 8px radius, 16px padding. Chart gridlines at `{colors.border}` 0.5 stroke. Axis text 12px ui-monospace weight 400 color `{colors.text-muted}`. First data series color `{colors.primary}` (mint teal)."
- "Build a data table: borderless, headers in Geist 14px weight 500 uppercase tracking 0.04em color `{colors.text-muted}`. Rows in ui-monospace 14px weight 400 color `{colors.ink}`. Row separator 1px solid `{colors.border}`."

### Iteration Guide
1. Default radius is `{rounded.sm}`–`{rounded.md}` — keep it tight, spreadsheet-adjacent
2. No drop shadows on static cards — 1px borders carry all elevation
3. Mint teal (`{colors.primary}`) is a data color — don't use it on buttons or links
4. Numbers are monospace, always — use `ui-monospace` not Geist Mono
5. Weight 700 for KPI values with -2.1px tracking at 60px scale
6. Delta badges are the only pill-radius element — everything else is `{rounded.sm}`–`{rounded.md}`
