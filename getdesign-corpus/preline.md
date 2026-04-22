# Design System Inspired by Preline

## 1. Visual Theme & Atmosphere

Preline is the design system that ships SaaS by Friday. The homepage is a gallery of 840+ Tailwind components — marketing heroes, pricing tables, admin dashboards, empty states — each one polished to production quality and ready for copy-paste. The aesthetic is deliberately mainstream: white canvas (`#ffffff`), near-black text (`#111827`), and a steady blue (`#3b82f6`) that signals interaction without demanding attention. This is Tailwind's default idiom, refined.

Typography is **Inter** (used via `ui-sans-serif` system stack) with weight 700 at display sizes and `-1.8px` letter-spacing — standard modern SaaS. Code is rendered in **Kode Mono** (a less-common choice than Geist Mono or JetBrains Mono) which gives docs and API snippets a subtly retro feel. The character of Preline isn't typographic innovation — it's the completeness of the component coverage.

What distinguishes Preline is **scale**: 840+ individual components organized across marketing sections, application UI, and admin dashboards. Radii tend to `8px` (157 elements) and `12px` (144 elements) — a mid-range that avoids both shadcn's sharpness and Material's softness. Shadows are present but subtle — SaaS-appropriate drop shadows that lift cards without drama.

**Key Characteristics:**
- Inter typeface (ui-sans-serif) with weight 700 at display — modern SaaS
- Blue `#3b82f6` as the sole interactive accent — Tailwind's blue-500
- `8px` / `12px` dominant radii — mid-range, mainstream
- 840+ components across marketing, app UI, and admin
- Kode Mono for code blocks — subtly retro
- Subtle SaaS shadows (`0 1px 2px`, `0 4px 6px`)
- Works with Alpine.js, Astro, or vanilla HTML — framework-agnostic
- Preline UI Pro: 1100+ additional components for commercial use

## 2. Color Palette & Roles

### Core
- **Primary Blue** (`#3b82f6`): Primary CTAs, links, active states. Tailwind blue-500.
- **Primary Hover** (`#2563eb`): Darker blue on hover. Tailwind blue-600.
- **Primary Light** (`#eff6ff`): Subtle blue background tint. Tailwind blue-50.
- **Gray 900** (`#111827`): Primary text, headings.
- **Gray 700** (`#374151`): Secondary text, form labels.
- **Gray 500** (`#6b7280`): Muted text, placeholders.
- **Gray 300** (`#d1d5db`): Strong borders, disabled text.
- **Gray 200** (`#e5e7eb`): Default borders, dividers.
- **Gray 100** (`#f3f4f6`): Muted surface.
- **White** (`#ffffff`): Primary canvas.

### Semantic States
- **Success** (`#10b981`): Confirmation badges (emerald-500).
- **Success BG** (`#ecfdf5`): Success surface.
- **Warning** (`#f59e0b`): Caution states (amber-500).
- **Error** (`#ef4444`): Destructive actions (red-500).
- **Info** (`#06b6d4`): Informational highlights (cyan-500).

### CSS Variables (from scanned docs)
- `--color-navbar`: `#fff`
- `--docsearch-primary-color`: `#3b82f6`
- `--docsearch-logo-color`: `#5468ff` (Algolia-branded)
- `--docsearch-hit-color`: `#4b5563`

## 3. Typography Rules

### Font Family
- **Primary**: `ui-sans-serif, system-ui, -apple-system, sans-serif` — Inter is the implicit default
- **Monospace**: `Kode Mono, ui-monospace, monospace` — a slightly whimsical mono
- **Serif (accent)**: `Domine, serif` — rarely used, reserved for editorial content

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Hero | Inter | 72px | 700 | 1.05 | -1.8px |
| Display Large | Inter | 48px | 700 | 1.10 | normal |
| H1 | Inter | 30px | 700 | 1.20 | normal |
| H2 | Inter | 30px | 600 | 1.25 | normal |
| H3 | Inter | 20px | 600 | 1.30 | normal |
| Body Large | Inter | 18px | 400 | 1.56 | normal |
| Body | Inter | 16px | 400 | 1.50 | normal |
| Button | Inter | 14px | 500 | 1.43 | normal |
| Caption | Inter | 14px | 400 | 1.43 | normal |
| Code | Kode Mono | 14px | 400 | 1.50 | normal |

### Principles
- **Weight 700 for display, 600 for sub-heads**: Standard two-weight hierarchy.
- **No letter-spacing below 24px**: Tracking returns to normal at body sizes.
- **Kode Mono for code only**: Inline `<code>` and fenced code blocks — not for data tables.
- **Inter fallback via ui-sans-serif**: Preline intentionally avoids importing Inter from Google Fonts; it lets the system pick up Inter where installed, falls back to San Francisco / Segoe UI otherwise.

## 4. Component Stylings

### Buttons
- **Primary**: `#3b82f6` bg, `#ffffff` text, `8px` radius, `8px 16px` padding, weight 500.
- **Secondary**: white bg, `1px solid #e5e7eb`, `#111827` text.
- **Soft**: `#eff6ff` bg, `#3b82f6` text, no border.
- **Ghost**: transparent, `#111827` text, hover `#f3f4f6`.
- **Danger**: `#ef4444` bg.
- Size variants: `xs` (28px), `sm` (32px), `md` (40px), `lg` (48px), `xl` (56px).

### Cards
- `#ffffff` bg, `1px solid #e5e7eb`, `12px` radius, `24px` padding, subtle `0 1px 2px rgba(0,0,0,0.05)` shadow.
- Card with image: image top `12px 12px 0 0` radius, content below.

### Inputs
- `#ffffff` bg, `1px solid #d1d5db`, `8px` radius, `12px 16px` padding.
- Focus: `2px solid #3b82f6`, `0 0 0 3px rgba(59,130,246,0.2)` ring.
- Error state: `2px solid #ef4444`.

### Dropdowns / Menus
- `#ffffff` bg, `1px solid #e5e7eb`, `8px` radius, `0 10px 15px -3px rgba(0,0,0,0.1)` shadow.
- Items: `8px 12px` padding, hover `#f3f4f6`.

### Badges
- `4px 8px` padding, `6px` radius, 12px Inter weight 500.
- Soft variants: `#eff6ff` bg, `#3b82f6` text, `1px solid #bfdbfe`.
- Solid variants: `#3b82f6` bg, `#ffffff` text.

### Alerts
- `12px` radius, `16px` padding, accent border-left 4px.
- Icon + content + optional close button.

## 5. Layout Principles

### Spacing System
- Base unit: **4px** (Tailwind-aligned)
- Dominant values: `14px` (166 uses — unusual), `2px` (131), `8px` (112), `12px` (45)
- The `14px` prevalence is Preline's distinct rhythm — less dense than shadcn (6-10px), less generous than Material (24px)

### Grid
- Marketing: 12-column with `24px` gutters, max `1280px`
- Admin: sidebar `256px` + content with `32px` padding
- Pricing: 3-column with equal heights, centered highlight card scales `1.05`

### Border Radius Scale
- Small (`6px`): Badges, small chips
- Standard (`8px`): Buttons, inputs, dropdowns
- Comfortable (`12px`): Cards, alerts — the default for larger surfaces
- Large (`16px`): Feature cards, testimonials

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | No shadow | Page background |
| Level 1 | `0 1px 2px rgba(0,0,0,0.05)` | Card at rest |
| Level 2 | `0 4px 6px -1px rgba(0,0,0,0.1)` | Card hover, popover |
| Level 3 | `0 10px 15px -3px rgba(0,0,0,0.1)` | Modal, dropdown |
| Level 4 | `0 20px 25px -5px rgba(0,0,0,0.1)` | Notification, toast |

**Shadow Philosophy**: Preline uses Tailwind's default shadow scale exactly — soft, neutral, mainstream. Shadows stay on the lighter end of the spectrum, suitable for light backgrounds. Dark mode adjusts shadow opacity but keeps the offsets identical.

## 7. Do's and Don'ts

### Do
- Use `8px` radius for buttons, `12px` for cards — the Preline rhythm
- Default to blue-500 (`#3b82f6`) for interactive accents
- Use soft button variants (`bg-blue-50 text-blue-600`) for secondary actions
- Apply subtle SaaS shadows (`shadow-sm`, `shadow-md`) on hover
- Use Kode Mono for inline code and code blocks
- Pair components from the same Preline family (marketing with marketing, admin with admin)

### Don't
- Don't use vibrant/brand colors beyond the blue — Preline is deliberately mainstream
- Don't use pill radius (`9999px`) on buttons — stays `8px`
- Don't skip the focus ring — Preline maintains Tailwind's accessibility defaults
- Don't use Geist or SF — stick with the system Inter stack
- Don't add motion — Preline is static by default, interactivity via Alpine/Astro

## 8. Responsive Behavior

### Breakpoints (Tailwind)
| Name | Width | Changes |
|------|-------|---------|
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

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary: `#3b82f6` (blue-500)
- Primary hover: `#2563eb` (blue-600)
- Text: `#111827` (gray-900)
- Muted text: `#6b7280` (gray-500)
- Border: `#e5e7eb` (gray-200)
- Surface: `#ffffff`
- Muted surface: `#f3f4f6` (gray-100)

### Example Component Prompts
- "Create a hero: white bg, 72px Inter weight 700 letter-spacing -1.8px, color #111827. Subtitle 18px weight 400 color #6b7280. Primary CTA: #3b82f6 bg, #fff text, 8px radius, 12px 24px padding, 14px weight 500."
- "Design a pricing card: white bg, 1px solid #e5e7eb, 12px radius, 24px padding, shadow-sm. Title 20px weight 600. Price 48px weight 700 color #111827. Feature list with check icons. Highlighted variant: 2px solid #3b82f6, scale(1.05)."
- "Build an admin sidebar: 256px wide, white bg, 1px solid #e5e7eb right border. Nav links 14px weight 500 color #374151, active state bg #eff6ff text #3b82f6 with 4px left border."

### Iteration Guide
1. Preline's aesthetic is mainstream Tailwind — don't over-design
2. Blue-500 is the only brand color — resist adding more accents
3. Cards get `12px` radius; buttons/inputs get `8px`
4. Use soft button variants for secondary actions — keeps the UI quiet
5. For dark mode, swap base to `#0f172a` and keep the same radius/spacing
6. Pair Preline with Alpine.js for interactivity — it's the intended dance partner
