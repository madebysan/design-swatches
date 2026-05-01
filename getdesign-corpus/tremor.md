---
slug: tremor
name: Tremor
url: https://tremor.so
domain: tremor.so
category: Design System
styles: [Light, Minimal, Colorful]
tagline: "Shadow-free borders, Geist 700, mint teal reserved strictly for data series."
fonts: [Geist, ui-monospace]
primary_color: "#9cd2bb"
---

# Design System Inspired by Tremor

> Shadow-free borders, Geist 700, mint teal reserved strictly for data series.

## 1. Visual Theme & Atmosphere

Tremor is the design system that looks like a spreadsheet pretending to be beautiful. The homepage is a dense grid of dashboards, KPI cards, and chart primitives rendered in a restrained palette — pure white canvas (`#ffffff`), near-black type (`#0a0a0a`), and a signature mint-teal (`#9cd2bb`) that appears in chart data series but never in chrome. This is dashboard-first design: every surface exists to frame data, every color has to survive on a 14-color chart without losing contrast.

Typography leans on **Geist** — Vercel's sans-serif — with weight 700 at display sizes and tight `-2.1px` letter-spacing that evokes financial terminal UIs. Where Stripe uses weight 300 for whisper-weight authority, Tremor uses 700 for data-grade bold. The typeface alternates with `ui-monospace` for tabular numerals, code samples, and API references — a deliberate technical cadence.

Tremor's defining choice is its **absence of shadows**. The 4 shadow values detected on the homepage are all `rgba(0,0,0,0)` — transparent placeholders, empty elevations. Cards lift through `1px` borders in `#e5e5e5` or subtle `6px` rounded edges, never through drop shadow. This is intentional: shadows blur data edges and compete with chart lines. Tremor wants the chart to be the elevation.

**Key Characteristics:**
- Pure white canvas with near-black text — data-first palette
- Geist weight 700 at display, `-2.1px` letter-spacing — financial-terminal authority
- Mint teal (`#9cd2bb`) as a data accent color, never chrome
- `6px` / `8px` dominant radii — restrained, spreadsheet-adjacent
- No shadows on static surfaces — borders only
- `ui-monospace` for tabular data and code — always
- Copy-paste philosophy (like shadcn) — components live in your repo
- Built on Tailwind + Recharts — fully typed, no hidden abstractions

## 2. Color Palette & Roles

### Core Neutrals
- **White** (`#ffffff`): Canvas, card surfaces, chart backgrounds.
- **Near-Black** (`#0a0a0a`): Primary text, axis labels, strong labels.
- **Slate** (`#888d94`): Secondary text — the single most-used color on the homepage (1,296 uses), not a heading color but the baseline chrome tone.
- **Slate 100** (`#f1f5f9`): Muted surface for table headers, disabled states.
- **Border** (`#e5e5e5`): The hairline — cards, dividers, chart gridlines.

### Data Accent (charts only)
- **Mint** (`#9cd2bb`): The signature Tremor green. Used as the first series color in charts, never as an interactive element.
- **Blue 600** (`#2563eb`): Second series color, also used for links.
- **Blue 500** (`#3b82f6`): Third series color, hover states.
- **Amber 500** (`#f59e0b`): Warnings, attention series.
- **Red 500** (`#ef4444`): Error bars, negative deltas.
- **Slate 600** (`#475569`): Secondary series, comparison data.

### Semantic Roles (KPI indicators)
- **Success** (`#16a34a`): Positive delta badges (↑ 12.4%).
- **Error** (`#dc2626`): Negative delta badges (↓ 3.2%).
- **Warning** (`#d97706`): Caution indicators on thresholds.
- **Muted foreground** (`#737373`): Labels, timestamps, axis text.

## 3. Typography Rules

### Font Family
- **Primary**: `Geist`, fallback: `ui-sans-serif, system-ui, sans-serif`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, monospace` (no branded mono)
- Tremor explicitly avoids Geist Mono in favor of the system monospace for tabular data, keeping the ecosystem agnostic.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Geist | 60px | 700 | 1.08 | -2.1px |
| H1 (KPI) | Geist | 36px | 700 | 1.10 | -1.26px |
| H2 | Geist | 30px | 600 | 1.15 | -1.5px |
| H3 | Geist | 20px | 600 | 1.25 | normal |
| Body Large | Geist | 18px | 400 | 1.50 | normal |
| Body | Geist | 16px | 400 | 1.50 | normal |
| Caption | Geist | 14px | 500 | 1.43 | normal |
| Mono (data) | ui-monospace | 14px | 400 | 1.43 | normal |

### Principles
- **Weight 700 for KPI numbers**: Dashboard number displays (`$142,830`, `+12.4%`) use weight 700 with tight letter-spacing for instant legibility.
- **Monospace is non-optional**: Any tabular or technical data (prices, IDs, column headers in tables) renders in `ui-monospace`.
- **Tight tracking above 24px**: Letter-spacing tightens aggressively from `-1.26px` at 36px to `-2.1px` at 60px — compact, engineered.

## 4. Component Stylings

### Buttons
- **Primary**: `#0a0a0a` bg, `#ffffff` text, `6px` radius, `8px 12px` padding, 14px weight 500.
- **Secondary**: white bg, `1px solid #e5e5e5`, `#0a0a0a` text, `6px` radius.
- **Ghost**: transparent, `#0a0a0a` text, hover `#f5f5f5`.

### Cards
- `#ffffff` bg, `1px solid #e5e5e5`, `8px` radius, `16px-24px` padding, **no shadow**.
- Chart cards: same treatment with the chart consuming the padding interior.

### KPI Cards
- Large number at 30px Geist weight 700 letter-spacing `-1.5px`
- Delta badge inline at 12px weight 500, pill radius (`9999px`)
- Label above at 14px weight 500 color `#737373` uppercase tracking `0.04em`

### Inputs
- `#ffffff` bg, `1px solid #e5e5e5`, `6px` radius, `8px 12px` padding.
- Focus: `1px solid #0a0a0a`, no ring (Tremor avoids focus rings on search/filter inputs to keep the dashboard chrome quiet).

### Charts
- Gridlines: `#e5e5e5` at `0.5` stroke
- Axis text: 12px `ui-monospace` weight 400 color `#737373`
- Data series: 2px stroke lines, 4px dot markers
- Tooltips: white bg, `1px solid #e5e5e5`, `6px` radius, slight `0 1px 3px rgba(0,0,0,0.05)` shadow

### Badges
- `9999px` radius (pill) for deltas — this is the one place full-pill appears
- Success: `#dcfce7` bg, `#15803d` text, `1px solid #bbf7d0`
- Error: `#fee2e2` bg, `#b91c1c` text

## 5. Layout Principles

### Spacing System
- Base unit: **4px**
- Dominant values (from homepage): `16px` (121 uses), `4px` (45), `8px` (38), `10px` (22) — dense UI rhythm

### Grid
- Dashboard grid: 12-column with `16-24px` gutters
- KPI row: 4 cards at `span-3` each on desktop
- Chart below: full-width or `span-8` with a `span-4` legend/filter panel

### Whitespace
- **Dense by design**: Tremor is meant for dashboards — component internal padding stays compressed (`12-16px`)
- **Generous between sections**: `32-48px` vertical gaps between dashboard rows
- **Aligned to chart grid**: card padding often matches chart margin to align numbers with data

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | No shadow, no border | Page background |
| Border | `1px solid #e5e5e5` | Cards, inputs, chart containers — default |
| Subtle | `0 1px 3px rgba(0,0,0,0.05)` | Tooltips, dropdowns only |
| Menu | `0 4px 12px rgba(0,0,0,0.08)` | Popover menus, filter dropdowns |

**Shadow Philosophy**: Tremor deliberately has no shadow system for static UI. Shadows only appear on elements that float over data (tooltips, popovers). Cards, KPIs, and chart containers all lift through border contrast alone — a decision that keeps chart edges clean and prevents dashboard visual noise.

## 7. Do's and Don'ts

### Do
- Use `6px-8px` radius on cards and inputs — the workhorse
- Use Geist weight 700 with tight letter-spacing for KPI numbers
- Use `ui-monospace` (not Geist Mono) for data columns and timestamps
- Default to border-only elevation — no drop shadows on static cards
- Use the mint teal (`#9cd2bb`) ONLY in chart data series
- Use full-pill radius (`9999px`) for delta badges only
- Keep chart gridlines subtle (`#e5e5e5`, 0.5 stroke)

### Don't
- Don't use drop shadows on dashboard cards — borders are the elevation
- Don't use the mint teal as a button or link color — it's data only
- Don't use Geist Mono — Tremor sticks with `ui-monospace` for neutrality
- Don't use border-radius above `12px` on chart containers — stays tight
- Don't add focus rings to filter inputs — keeps the dashboard quiet

## 8. Responsive Behavior

### Breakpoints (Tailwind defaults)
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | KPIs stack single column, charts scroll horizontally |
| md | `768px+` | 2-column KPI row, full-width charts |
| lg | `1024px+` | 4-column KPI row, side-by-side chart panels |
| xl | `1280px+` | Full dashboard grid |

### Touch Targets
- Filter chips: `32px` minimum height
- Icon-only buttons: `36px × 36px`
- Legend swatches: `16px × 16px` with `8px` padding around for tap

### Collapsing Strategy
- KPI cards: 4-col → 2-col → 1-col
- Charts: maintain aspect ratio, reduce internal padding `16px → 12px` on mobile
- Axis labels: rotate to `-45deg` or abbreviate (`$1.2K` vs `$1,200`)

## 9. Agent Prompt Guide

### Quick Color Reference
- Background: `#ffffff`
- Text: `#0a0a0a` (primary), `#737373` (muted)
- Border: `#e5e5e5`
- Data mint: `#9cd2bb`
- Data blue: `#2563eb`
- Success/Error: `#16a34a` / `#dc2626`

### Example Component Prompts
- "Create a KPI card: white bg, 1px solid #e5e5e5, 8px radius, 20px padding, no shadow. Label at 14px Geist weight 500 uppercase tracking 0.04em color #737373. Value at 30px Geist weight 700 letter-spacing -1.5px color #0a0a0a. Delta badge inline: 12px weight 500, 9999px radius, bg #dcfce7, text #15803d."
- "Design a chart container: white bg, 1px solid #e5e5e5, 8px radius, 16px padding. Chart gridlines at #e5e5e5 0.5 stroke. Axis text 12px ui-monospace weight 400 color #737373. First data series color #9cd2bb (mint teal)."
- "Build a data table: borderless, headers in Geist 14px weight 500 uppercase tracking 0.04em color #737373. Rows in ui-monospace 14px weight 400 color #0a0a0a. Row separator 1px solid #e5e5e5."

### Iteration Guide
1. Default radius is `6-8px` — keep it tight, spreadsheet-adjacent
2. No drop shadows on static cards — 1px borders carry all the elevation
3. Mint teal (`#9cd2bb`) is a data color — don't use it on buttons or links
4. Numbers are monospace, always — use `ui-monospace` not Geist Mono
5. Weight 700 for KPI values with `-2.1px` tracking at 60px scale
6. Delta badges are the only pill-radius element — everything else is `6-8px`
