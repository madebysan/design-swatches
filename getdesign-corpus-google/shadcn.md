---
version: alpha
name: shadcn/ui
description: Aggressively un-branded monochrome component kit — pure white canvas, near-black ink, single hairline border, 10px workhorse radius, Geist sans with -2.4px display tracking.

colors:
  # Canvas + surfaces
  background: "#ffffff"
  surface-muted: "#fafafa"
  surface-subtle: "#f5f5f5"

  # Ink
  ink: "#0a0a0a"
  ink-strong: "#171717"
  ink-body: "#404040"
  ink-muted: "#737373"
  ink-placeholder: "#a1a1a1"

  # Primary (near-black)
  primary: "#171717"
  on-primary: "#fafafa"

  # Secondary / muted surfaces
  secondary: "#f5f5f5"
  on-secondary: "#0a0a0a"
  accent: "#f5f5f5"
  on-accent: "#0a0a0a"

  # Borders
  border: "#e5e5e5"
  input-border: "#e5e5e5"
  ring: "#0a0a0a"

  # Semantic
  destructive: "#ef4444"
  on-destructive: "#fafafa"

  # Dark mode (referenced for completeness)
  dark-background: "#0a0a0a"
  dark-foreground: "#fafafa"
  dark-border: "#262626"

  # Subtle shadow tint (popovers / modals)
  shadow-soft: "#e5e5e5"  # was rgba(0,0,0,0.05) — Google format requires hex

typography:
  display-hero:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -2.4px
  h1:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.11
    letterSpacing: -1.8px
  h2:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.9px
  h3:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.48px
  h4:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0px
  body-large:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0px
  body:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-small:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  caption:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  caption-small:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0px
  button:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  button-small:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  link:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  data-mono:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  code-inline:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px

spacing:
  hairline: 1px
  micro: 2px
  xxs: 4px
  xs: 6px
  sm: 8px
  md: 10px
  lg: 12px
  xl: 16px
  2xl: 24px
  3xl: 40px
  4xl: 64px
  5xl: 80px

rounded:
  none: 0px
  xs: 4px
  md: 10px
  lg: 14px
  pill: 9999px

components:
  # Primary button
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 9px 16px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
  button-primary-focus:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"

  # Secondary / outline
  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 9px 16px
  button-secondary-hover:
    backgroundColor: "{colors.surface-subtle}"
    textColor: "{colors.ink}"

  # Ghost
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 9px 16px
  button-ghost-hover:
    backgroundColor: "{colors.surface-subtle}"
    textColor: "{colors.ink}"

  # Destructive
  button-destructive:
    backgroundColor: "{colors.destructive}"
    textColor: "{colors.on-destructive}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 9px 16px

  # Card
  card:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Input
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-small}"
    rounded: "{rounded.md}"
    padding: 9px 12px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Badges
  badge-solid:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-small}"
    rounded: "{rounded.pill}"
    padding: 2px 10px
  badge-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.caption-small}"
    rounded: "{rounded.pill}"
    padding: 2px 10px
  badge-outline:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-small}"
    rounded: "{rounded.pill}"
    padding: 2px 10px

  # Dropdown / menu
  dropdown:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-small}"
    rounded: "{rounded.md}"
    padding: 4px
  dropdown-item:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-small}"
    rounded: "{rounded.xs}"
    padding: 6px 8px
  dropdown-item-hover:
    backgroundColor: "{colors.surface-subtle}"
    textColor: "{colors.ink}"

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.ink-muted}"

  # Switch
  switch-off:
    backgroundColor: "{colors.border}"
    rounded: "{rounded.pill}"
  switch-on:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.pill}"
---

# shadcn/ui Design System

## Overview

shadcn/ui is the design system that looks like nothing — and that is exactly the point. Where most systems announce themselves through color or ornament, shadcn announces itself through absence — a pure white canvas (`{colors.background}`), near-black text (`{colors.ink}`), and a single neutral border color (`{colors.border}`) doing 90% of the visible work. The homepage is a showroom of components arranged on a grid: a payment form, a team invite card, a pricing table, an appointment picker. Each one rendered in the same restrained palette, each one legible without inspection. The system's radical move is to treat monochrome not as a limitation but as the default state of a well-designed component library.

The typographic choice reinforces this discipline. **Geist** — Vercel's sans-serif, shipped through `next/font` and carried by shadcn as its default — sits at 16px/1.5 for body and jumps to 48px weight 600 with `-2.4px` letter-spacing for display headings. That negative tracking is the single most brand-defining value in the whole kit: it tightens hero type into a dense, engineered block that reads as confident without being loud. Geist Mono appears in labels, data cells, and code — a companion face that keeps technical content in its own lane without resorting to the usual Roboto Mono or Menlo.

What truly distinguishes shadcn is its radius. `10px` is the workhorse — applied to buttons, cards, inputs, dropdowns — sitting between the tight 4–6px of Apple-adjacent systems and the soft 16–20px of Material-inspired systems. `8–14px` handles cards and other chrome, and a full pill rounds avatars and tabs. No shadow system to speak of: surfaces lift through border contrast and a single 1px hairline (`{colors.border}`), with shadows reserved almost entirely for focus rings. The resulting aesthetic is flat, pragmatic, and aggressively un-branded — a system that disappears into whatever product ships it.

**Key Characteristics:**
- Monochrome palette anchored on `{colors.background}`, `{colors.ink}`, and `{colors.border}` — the Tailwind neutral scale in practice
- Geist as primary typeface with `-2.4px` letter-spacing at display sizes — the tightest tracking in mainstream UI kits
- Weight 600 (not 700) for headings — confident without shouting
- `{rounded.md}` (10px) as the default border-radius — distinctly "not shadcn's competition"
- Geist Mono for labels, data, timestamps, and code — the technical companion
- Flat surfaces, hairline borders, focus rings instead of drop shadows
- Copy-and-paste philosophy: the components ship as source code, not an npm package
- Radix UI primitives underneath — accessibility is a primitive, not a feature

## Colors

### Core Neutral Scale (Tailwind `neutral`)
- **Pure White** (`{colors.background}`): Page background, card surfaces, input backgrounds.
- **Near-Black** (`{colors.ink}`): Primary text color, focus ring, active tab indicators.
- **Zinc 50** (`{colors.surface-muted}`): Subtle alternate surface, hover backgrounds on ghost buttons, muted card interiors.
- **Zinc 100** (`{colors.surface-subtle}`): Input background (subtle), pressed button state, code block surface.
- **Zinc 200** (`{colors.border}`): The standard border color — every hairline divider, every card edge, every input outline.
- **Zinc 400** (`{colors.ink-placeholder}`): Placeholder text, disabled text, muted icons.
- **Zinc 500** (`{colors.ink-muted}`): Secondary text, muted foreground.
- **Zinc 700** (`{colors.ink-body}`): Strong body text in dark contexts, secondary headings.
- **Zinc 900** (`{colors.ink-strong}`): Primary button background, near-twin of Near-Black.

### Semantic Roles
- `--background` (`{colors.background}`): Page canvas.
- `--foreground` (`{colors.ink}`): Primary text.
- `--primary` (`{colors.primary}`): Primary button background.
- `--primary-foreground` (`{colors.on-primary}`): Text on primary.
- `--secondary` (`{colors.secondary}`): Secondary button background, muted chips.
- `--muted-foreground` (`{colors.ink-muted}`): Muted text, captions.
- `--accent` (`{colors.accent}`): Hover state for ghost buttons and menu items.
- `--border` (`{colors.border}`): All borders and dividers.
- `--ring` (`{colors.ring}`): Focus ring color — 2px offset, matches primary.
- `--destructive` (`{colors.destructive}`): Red for destructive actions.

### Surface Contrast
Contrast between adjacent surfaces is intentionally extremely low — card on background is `{colors.background}` on `{colors.background}`, separated only by the 1px `{colors.border}` border. This creates a floating, modular feel where components feel like cut paper rather than elevated cards.

### Dark Mode (inverse)
- `--background` flips to `{colors.dark-background}`
- `--foreground` flips to `{colors.dark-foreground}`
- `--border` flips to `{colors.dark-border}`
- The same `{rounded.md}` radius, same `1px` borders — the structure is preserved; only the values invert.

## Typography

### Font Family
- **Primary**: `Geist`, fallback `Geist Fallback, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`
- **Monospace**: `Geist Mono`, fallback `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace`
- **Variable font**: Both Geist and Geist Mono ship as variable fonts — weight is a continuous axis (100–900).

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`).

| Token | Use |
|---|---|
| `display-hero` | Hero headline (48px, signature `-2.4px` tracking) |
| `h1` | Page headings inside docs (36px) |
| `h2` | Section headings (30px) |
| `h3` | Sub-sections, card titles (24px) |
| `h4` | Small heads, component names (20px) |
| `body-large` | Intro paragraphs, lead text (18px) |
| `body` | Default reading size (16px) |
| `body-small` | Secondary text, form labels (14px) |
| `caption` | Labels, UI chrome, table headers |
| `caption-small` | Badges, timestamps, fine print |
| `button` | Primary/secondary buttons |
| `button-small` | Compact buttons, pagination |
| `link` | Nav links, inline anchors |
| `data-mono` | Tabular data, timestamps, IDs |
| `code-inline` | `inline code` within prose |

### Principles
- **Negative tracking at scale**: Letter-spacing tightens aggressively above 24px — `-2.4px` at 48px, `-1.8px` at 36px, `-0.9px` at 30px. Below 20px, tracking returns to normal.
- **Weight 600 is the headline weight**: No 700 (bold) and no 800 (extra-bold). 600 carries enough authority.
- **Body defaults to 16px/1.5**: A conservative, readability-first default — same ratio Tailwind ships as `text-base leading-6`.
- **Mono for data, not decoration**: Geist Mono never appears as a design flourish. It appears for numbers, IDs, or quoted code.
- **Fallback-aware**: "Geist Fallback" is a metric-matched system font preventing CLS while Geist loads.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 4px.

Dominant values: `xs` (6px), `md` (10px), `xl` (16px), `2xl` (24px) — matching Tailwind's spacing scale.

### Grid & Container
- Max content width: `1400px` (`max-w-screen-2xl`)
- Docs layout: `256px` sidebar + content column with `64px` page padding
- Homepage: centered single-column hero (max 768px text) with a component showcase grid below
- Forms: single column, `xl` vertical rhythm between fields

### Whitespace Philosophy
- **Breathing room, not emptiness**: Generous padding inside components (`2xl` cards, `3xl+` hero sections) but tight spacing between related items (`xs–sm` between badges, `md` between form labels and inputs).
- **Component density is low by default**: Each component on the homepage gets its own card with room around it.
- **Section rhythm**: `5xl` vertical gap between major sections, `2xl` between cards in a grid.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Page background, inline text |
| Border Lift (Level 1) | `1px solid {colors.border}` | Cards, inputs, buttons — the default way surfaces separate |
| Subtle (Level 2) | `0 1px 2px 0` tinted `{colors.shadow-soft}` | Explicit card elevation, hover states |
| Popover (Level 3) | `0 4px 12px` tinted `{colors.shadow-soft}` with `1px solid {colors.border}` | Dropdowns, popovers, menus |
| Modal (Level 4) | `0 10px 40px` tinted `{colors.shadow-soft}` with `1px solid {colors.border}` | Dialogs, command palettes |
| Focus Ring | `0 0 0 2px {colors.ring}` offset by `2px` | Keyboard focus, active input |

**Shadow Philosophy**: shadcn deliberately resists elevation. Where Material Design leans on shadow as the primary depth cue and Apple uses subtle dual-layer shadows, shadcn uses borders. A `1px` hairline in `{colors.border}` does the work of a 4-layer shadow. This (1) feels flat, modern, and CAD-like, and (2) renders identically in light and dark mode without tuning. Shadows only appear where depth is functionally required — dropdowns floating over content, modals interrupting the page, focus rings that must be perceivable. Every other surface "lifts" through border contrast alone.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Inline rules, separators |
| `xs` | 4px | Checkboxes — the only sub-10px element in the default set |
| `md` | 10px | Buttons, inputs, menus, dropdowns. The workhorse. |
| `lg` | 14px | Cards, larger containers |
| `pill` | 9999px | Pills, badges, switches, avatars |

`{rounded.md}` (10px) is the single most identifying measurement in the system.

## Components

The complete component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card}`).

### Buttons
- **`button-primary`** — Near-black solid (`{colors.primary}`) with light text. `{rounded.md}` corners, `9px 16px` padding. Hover dims to `{colors.ink}`. Focus shows a 2px black ring with 2px offset.
- **`button-secondary`** — White with a `1px solid {colors.border}` outline. Hover fills to `{colors.surface-subtle}`.
- **`button-ghost`** — Transparent until hover, then `{colors.surface-subtle}`. No border.
- **`button-destructive`** — Red `{colors.destructive}` with light text. Same `{rounded.md}` radius and padding rhythm.

### Cards
- **`card`** — White surface, `1px solid {colors.border}` border, `{rounded.lg}` (14px — the one exception to the 10px rule), `24px` padding, no shadow by default.

### Inputs
- **`input`** — White surface, `1px solid {colors.border}` border, `{rounded.md}` corners, `9px 12px` padding, 14px Geist weight 400. Focus reveals the 2px black ring; placeholder color is `{colors.ink-placeholder}`.

### Badges
- **`badge-solid`** — Near-black pill with light text.
- **`badge-secondary`** — Muted gray pill with dark text.
- **`badge-outline`** — Transparent pill with `1px solid {colors.border}` and dark text.

### Dropdowns / Menus
- **`dropdown`** — White surface, hairline border, `{rounded.md}` corners, with the system's only prominent drop shadow.
- **`dropdown-item`** — `6px 8px` padding; hover fills `{colors.surface-subtle}`.

### Navigation
Sticky top bar, white background, hairline bottom border. Links at 14px Geist weight 500, `{colors.ink}` default, `{colors.ink-muted}` hover. Active items underline with a 2px black border or a pill-style background.

### Switches & Toggles
- **`switch-off`** — Track in `{colors.border}`.
- **`switch-on`** — Track in `{colors.primary}`.
- Thumb is white `{colors.background}` with subtle shadow; `{rounded.pill}` shape; `0.2s ease-out` transition.

## Do's and Don'ts

### Do
- Use `{rounded.md}` (10px) as the default border-radius for buttons, inputs, and cards
- Apply `-2.4px` letter-spacing to hero headlines at 48px — negative tracking is Geist's signature
- Use `{colors.border}` borders instead of shadows for standard card elevation
- Pair Geist with Geist Mono for any data, timestamp, or code display
- Default to weight 600 for headings, weight 500 for buttons/links, weight 400 for body
- Use the Tailwind neutral scale as your full palette — resist the urge to add color
- Reserve `{rounded.pill}` (9999px) for badges, switches, and avatars only
- Use 2px focus rings on `{colors.ring}` — never colored rings

### Don't
- Don't use drop shadows on static cards — the hairline border is the elevation
- Don't use letter-spacing at body sizes (14–16px) — keep tracking at normal
- Don't use weight 700/800 for headings — 600 is the heavy end of the scale
- Don't use pill-radius on buttons or inputs — those are `{rounded.md}`
- Don't use saturated brand colors in the default theme — the whole point is monochrome
- Don't mix Geist with Inter or system-ui for headings — the Geist Fallback handles loading
- Don't use border-radius above `{rounded.lg}` (14px) on cards — it starts to look Material
- Don't skip the focus ring — shadcn's accessibility story is load-bearing

---

## Responsive Behavior

### Breakpoints (Tailwind defaults)
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | `<640px` | Single column, sidebar collapses to sheet, hero scales to 32px |
| sm | `640px+` | 2-column grids allowed, forms stay single-column |
| md | `768px+` | Docs sidebar appears, 3-column component grids |
| lg | `1024px+` | Full desktop layout, 4-column grids |
| xl | `1280px+` | Max content width applies (`1400px`) |

### Touch Targets
- Buttons maintain `36px` minimum height (h-9 = `9px × 2` padding + text)
- Touch-friendly icon buttons use `h-10 w-10` (`40px × 40px`)
- Tappable list items have `py-3` minimum (`12px` vertical padding)

### Collapsing Strategy
- Hero: 48px → 36px → 30px across breakpoints, weight 600 maintained
- Docs sidebar: fixed 256px on desktop → slide-in sheet on mobile
- Component grids: `lg:grid-cols-4` → `md:grid-cols-2` → single column
- Form fields: always single column; only labels shrink on mobile
- Tables: horizontal scroll on mobile with sticky first column
- Dialog/modal width: max 512px on desktop, full-width with padding on mobile

### Image Behavior
- Component screenshots maintain `14px` radius at all sizes
- OG images render at 1200×630 with centered type at `-2.4px` tracking
- Favicons are `16×16` with the subtle black-on-white `S` mark

---

## Agent Prompt Guide

### Quick Color Reference
- Background: `{colors.background}`
- Foreground (text): `{colors.ink}`
- Primary button: `{colors.primary}` with `{colors.on-primary}` text
- Secondary button: `{colors.background}` with `1px solid {colors.border}`
- Muted surface: `{colors.surface-subtle}`
- Muted text: `{colors.ink-muted}`
- Border (everywhere): `{colors.border}`
- Placeholder text: `{colors.ink-placeholder}`
- Focus ring: `{colors.ring}` at 2px with 2px offset
- Destructive: `{colors.destructive}`

### Example Component Prompts
- "Create a hero section on white (`{colors.background}`). Headline at 48px Geist weight 600, line-height 1.10, letter-spacing -2.4px, color `{colors.ink}`. Subtitle at 18px weight 400, line-height 1.56, color `{colors.ink-muted}`. Primary button (`{colors.primary}` bg, `{colors.on-primary}` text, 10px radius, 9px 16px padding, 14px Geist weight 500) and outline button (white bg, 1px solid `{colors.border}`, 10px radius, 14px weight 500)."
- "Design a card: white background, 1px solid `{colors.border}` border, 14px radius, 24px padding, no shadow. Title at 20px Geist weight 600, letter-spacing normal. Body at 14px weight 400, `{colors.ink-muted}` color, line-height 1.43. Action button bottom-right at 10px radius."
- "Build a badge: 12px Geist weight 500, 2px 10px padding, 9999px radius (full pill). Solid variant: `{colors.primary}` bg, `{colors.on-primary}` text. Outline variant: transparent bg, 1px solid `{colors.border}`, `{colors.ink}` text."
- "Create a form input: `{colors.background}` bg, 1px solid `{colors.border}` border, 10px radius, 9px 12px padding, 14px Geist weight 400, `{colors.ink-placeholder}` placeholder. Focus ring: 0 0 0 2px `{colors.ring}` with 2px offset."
- "Design a navigation bar: sticky top, white bg, 1px solid `{colors.border}` bottom border, 16px vertical padding. Links at 14px Geist weight 500, `{colors.ink}` default, `{colors.ink-muted}` hover. Right-aligned primary CTA button."

### Iteration Guide
1. Start with `{rounded.md}` (10px) — if a component doesn't look right, it's rarely the radius that's wrong
2. Default to weight 600 headings, weight 500 UI text, weight 400 body — no bolder, no lighter
3. Apply `-2.4px` letter-spacing only at 48px+ — below 30px, return to normal tracking
4. Reach for borders before shadows: `1px solid {colors.border}` solves 90% of depth problems
5. Keep the palette monochrome until a specific semantic role demands color (destructive = red)
6. For numeric/code display, switch the font stack to Geist Mono — don't just change size
7. Use `{colors.ink-muted}` for secondary text, `{colors.ink-placeholder}` for placeholder/disabled — never `#cccccc` or pure gray
8. Focus rings are non-negotiable — 2px offset 2px thick, black — visible on any background
