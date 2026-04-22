# Design System Inspired by shadcn/ui

## 1. Visual Theme & Atmosphere

shadcn/ui is the design system that looks like nothing and that is exactly the point. Where most systems announce themselves through color or ornament, shadcn announces itself through absence — a pure white canvas (`#ffffff`), near-black text (`#0a0a0a`), and a single neutral border color (`#e5e5e5`) doing 90% of the visible work. The homepage is a showroom of components arranged on a grid: a payment form, a team invite card, a pricing table, an appointment picker. Each one rendered in the same restrained palette, each one legible without inspection. The system's radical move is to treat monochrome not as a limitation but as the default state of a well-designed component library.

The typographic choice reinforces this discipline. **Geist** — Vercel's sans-serif, shipped through `next/font` and carried by shadcn as its default — sits at 16px/1.5 for body and jumps to 48px weight 600 with `-2.4px` letter-spacing for display headings. That negative tracking is the single most brand-defining value in the whole kit: it tightens hero type into a dense, engineered block that reads as confident without being loud. Geist Mono appears in labels, data cells, and code — a companion face that keeps technical content in its own lane without resorting to the usual Roboto Mono or Menlo.

What truly distinguishes shadcn is its radius. `10px` is the workhorse — applied to 29 elements on the homepage (buttons, cards, inputs, dropdowns) — sitting between the tight 4-6px of Apple-adjacent systems and the soft 16-20px of Material-inspired systems. `8px` handles badges and smaller chrome, and a full `9999px` rounds avatars and pill-shaped tabs. No shadow system to speak of: surfaces lift through border contrast and a single 1px hairline (`#e5e5e5`), with shadows reserved almost entirely for focus rings (`0 0 0 2px rgba(0,0,0,0.2)`). The resulting aesthetic is flat, pragmatic, and aggressively un-branded — a system that disappears into whatever product ships it.

**Key Characteristics:**
- Monochrome palette anchored on `#ffffff`, `#0a0a0a`, and `#e5e5e5` — the Tailwind neutral scale in practice
- Geist as primary typeface with `-2.4px` letter-spacing at display sizes — the tightest tracking in mainstream UI kits
- Weight 600 (not 700) for headings — confident without shouting
- `10px` as the default border-radius — distinctly "not shadcn's competition"
- Geist Mono for labels, data, timestamps, and code — the technical companion
- Flat surfaces, hairline borders, focus rings instead of drop shadows
- Copy-and-paste philosophy: the components ship as source code, not an npm package
- Radix UI primitives underneath — accessibility is a primitive, not a feature

## 2. Color Palette & Roles

### Core Neutral Scale (Tailwind `neutral`)
- **Pure White** (`#ffffff`): Page background, card surfaces, input backgrounds.
- **Near-Black** (`#0a0a0a`): Primary text color, primary button backgrounds, active tab indicators. Not pure black — softened just enough to feel warm on white.
- **Zinc 50** (`#fafafa`): Subtle alternate surface, hover backgrounds on ghost buttons, muted card interiors.
- **Zinc 100** (`#f5f5f5`): Input background (subtle), pressed button state, code block surface.
- **Zinc 200** (`#e5e5e5`): The standard border color. Every hairline divider, every card edge, every input outline. Doing more work than any other single token in the system.
- **Zinc 400** (`#a1a1a1`): Placeholder text, disabled text, muted icons.
- **Zinc 500** (`#737373`): Secondary text, muted foreground. `--muted-foreground` in the theme.
- **Zinc 700** (`#404040`): Strong body text in dark contexts, secondary headings.
- **Zinc 900** (`#171717`): Near-identical twin of Near-Black — used interchangeably for text in default theme.

### Semantic Roles (CSS variable names from shadcn theme)
- `--background` (`#ffffff`): Page canvas.
- `--foreground` (`#0a0a0a`): Primary text.
- `--card` (`#ffffff`): Card surface.
- `--card-foreground` (`#0a0a0a`): Text on cards.
- `--primary` (`#171717`): Primary button background, active indicators.
- `--primary-foreground` (`#fafafa`): Text on primary.
- `--secondary` (`#f5f5f5`): Secondary button background, muted chips.
- `--muted` (`#f5f5f5`): Muted surface backgrounds.
- `--muted-foreground` (`#737373`): Muted text, captions.
- `--accent` (`#f5f5f5`): Hover state for ghost buttons and menu items.
- `--border` (`#e5e5e5`): All borders and dividers.
- `--input` (`#e5e5e5`): Input border color (matches `--border`).
- `--ring` (`#0a0a0a`): Focus ring color — 2px offset, matches primary.
- `--destructive` (`#ef4444`): Red for destructive actions (the one accent color that appears).

### Surface Contrast
The system intentionally keeps contrast between adjacent surfaces extremely low — card on background is `#ffffff` on `#ffffff`, separated only by the 1px `#e5e5e5` border. This creates a floating, modular feel where components feel like cut paper rather than elevated cards.

### Dark Mode (inverse)
- `--background` flips to `#0a0a0a`
- `--foreground` flips to `#fafafa`
- `--border` flips to `#262626` (Zinc 800)
- `--muted-foreground` flips to `#a1a1a1` (Zinc 400)
- The same `10px` radius, same `1px` borders — the structure is preserved; only the values invert.

## 3. Typography Rules

### Font Family
- **Primary**: `Geist`, with fallback stack: `Geist Fallback, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`
- **Monospace**: `Geist Mono`, with fallback: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace`
- **Variable font**: Both Geist and Geist Mono ship as variable fonts — weight is a continuous axis (100-900).

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display / Hero | Geist | 48px (3.00rem) | 600 | 1.10 | -2.4px | Hero headline on homepage — the signature tight tracking |
| H1 (Docs) | Geist | 36px (2.25rem) | 600 | 1.11 | -1.8px | Page headings inside the docs layout |
| H2 | Geist | 30px (1.88rem) | 600 | 1.20 | -0.9px | Section headings |
| H3 | Geist | 24px (1.50rem) | 600 | 1.25 | -0.48px | Sub-sections, card titles |
| H4 | Geist | 20px (1.25rem) | 600 | 1.30 | normal | Small heads, component names |
| Body Large | Geist | 18px (1.13rem) | 400 | 1.56 | normal | Intro paragraphs, lead text |
| Body | Geist | 16px (1.00rem) | 400 | 1.50 | normal | Default reading size |
| Body Small | Geist | 14px (0.88rem) | 400 | 1.43 | normal | Secondary text, form labels |
| Caption | Geist | 12.8px (0.80rem) | 500 | 1.50 | normal | Labels, UI chrome, table headers |
| Caption Small | Geist | 12px (0.75rem) | 500 | 1.33 | normal | Badges, timestamps, fine print |
| Button | Geist | 14px (0.88rem) | 500 | 1.43 | normal | Primary/secondary buttons |
| Button Small | Geist | 12.8px (0.80rem) | 500 | 1.43 | normal | Compact buttons, pagination |
| Link | Geist | 14px (0.88rem) | 500 | 1.43 | normal | Nav links, inline anchors |
| Data / Mono | Geist Mono | 14px (0.88rem) | 400 | 1.43 | normal | Tabular data, timestamps, IDs |
| Code Inline | Geist Mono | 14px (0.88rem) | 500 | 1.43 | normal | `inline code` within prose |

### Principles
- **Negative tracking at scale**: Letter-spacing tightens aggressively above 24px — `-2.4px` at 48px, `-1.8px` at 36px, `-0.9px` at 30px. Below 20px, tracking returns to normal.
- **Weight 600 is the headline weight**: No 700 (bold) and no 800 (extra-bold). The system believes 600 carries enough authority and reserves heavier weights for explicit emphasis, which is rarely needed.
- **Body defaults to 16px/1.5**: A conservative, readability-first default — the same ratio Tailwind ships as `text-base leading-6`.
- **Mono for data, not decoration**: Geist Mono never appears as a design flourish. It appears when numbers need to align, when IDs are shown, or when code is quoted. Any other use is off-brand.
- **Fallback-aware**: "Geist Fallback" is a metric-matched system font that loads before Geist finishes, preventing CLS. This is a shipped technical decision, not a nice-to-have.

## 4. Component Stylings

### Buttons

**Primary**
- Background: `#171717` (near-black)
- Text: `#fafafa`
- Padding: `9px 16px` (h-9 px-4 in Tailwind terms)
- Radius: `10px`
- Font: 14px Geist weight 500
- Hover: background shifts to `#171717` with 90% opacity
- Focus: `0 0 0 2px #0a0a0a` ring with `2px` offset

**Secondary / Outline**
- Background: `#ffffff`
- Text: `#0a0a0a`
- Padding: `9px 16px`
- Radius: `10px`
- Border: `1px solid #e5e5e5`
- Hover: background `#f5f5f5`

**Ghost**
- Background: transparent
- Text: `#0a0a0a`
- Padding: `9px 16px`
- Radius: `10px`
- No border
- Hover: background `#f5f5f5`

**Destructive**
- Background: `#ef4444`
- Text: `#fafafa`
- Radius: `10px`

### Cards
- Background: `#ffffff`
- Border: `1px solid #e5e5e5`
- Radius: `14px` (slightly more generous than buttons — the one exception to the 10px rule)
- Padding: `24px` (p-6)
- Shadow: none by default. `0 1px 2px 0 rgb(0 0 0 / 0.05)` only when explicitly elevated.

### Inputs
- Background: `#ffffff`
- Border: `1px solid #e5e5e5`
- Radius: `10px`
- Padding: `9px 12px`
- Font: 14px Geist weight 400
- Focus: `0 0 0 2px #0a0a0a` ring, border color unchanged
- Placeholder: `#a1a1a1`

### Badges
- Background: `#171717` (solid) or `#f5f5f5` (secondary) or transparent with border (outline)
- Text: matches inverse
- Padding: `2px 10px`
- Radius: `9999px` (full pill) — badges are the one element that breaks from 10px
- Font: 12px Geist weight 500
- Border: `1px solid transparent` (solid) or `1px solid #e5e5e5` (outline)

### Dropdowns / Menus
- Background: `#ffffff`
- Border: `1px solid #e5e5e5`
- Radius: `10px`
- Shadow: `0 4px 12px rgba(0,0,0,0.1)` — the only place shadows appear prominently
- Item padding: `6px 8px`
- Item hover: background `#f5f5f5`

### Navigation
- Sticky top bar, white background, `1px solid #e5e5e5` bottom border
- Links: 14px Geist weight 500, `#0a0a0a` text
- Link hover: `#737373` (muted-foreground)
- Active nav item: underlined with `border-bottom: 2px solid #0a0a0a` or pill-style background

### Switches & Toggles
- Track: `#e5e5e5` (off) or `#0a0a0a` (on)
- Thumb: `#ffffff` with subtle shadow
- Radius: `9999px` (pill)
- Transition: `0.2s ease-out`

## 5. Layout Principles

### Spacing System
- Base unit: 4px
- Scale: `1, 2, 4, 6, 8, 10, 12, 16, 24, 40, 80` (px)
- Dominant values: 6px (gap-1.5), 10px (gap-2.5), 16px (gap-4), 24px (gap-6) — matches Tailwind spacing scale exactly

### Grid & Container
- Max content width: `1400px` (Tailwind's `max-w-screen-2xl`)
- Docs layout: `256px` sidebar + content column with `64px` page padding
- Homepage: centered single-column hero (max 768px for text) with a component showcase grid below
- Forms: single column, `14px` vertical rhythm between fields

### Whitespace Philosophy
- **Breathing room, not emptiness**: The system uses generous padding inside components (`24px` cards, `40px+` hero sections) but tight spacing between related items (`6-8px` between badges, `10px` between form labels and inputs).
- **Component density is low by default**: Each component on the homepage gets its own card with room around it — shadcn shows off components, doesn't cram them.
- **Section rhythm**: `80px` vertical gap between major homepage sections, `24px` between cards in a grid.

### Border Radius Scale
- Sharp (0-4px): Checkboxes (`4px`) — the only element using sub-10px radius in the default set
- Standard (`10px`): Buttons, inputs, menus, dropdowns, smaller cards. The workhorse.
- Comfortable (`14px`): Cards, larger containers.
- Full (`9999px`): Pills, badges, switches, avatars.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page background, inline text |
| Border Lift (Level 1) | `1px solid #e5e5e5` | Cards, inputs, buttons — the default way surfaces separate |
| Subtle (Level 2) | `0 1px 2px 0 rgb(0 0 0 / 0.05)` | Explicit card elevation, hover states |
| Popover (Level 3) | `0 4px 12px rgba(0,0,0,0.1)` with `1px solid #e5e5e5` | Dropdowns, popovers, menus |
| Modal (Level 4) | `0 10px 40px rgba(0,0,0,0.15)` with `1px solid #e5e5e5` | Dialogs, command palettes |
| Focus Ring | `0 0 0 2px #0a0a0a` offset by `2px` | Keyboard focus, active input |

**Shadow Philosophy**: shadcn deliberately resists elevation. Where Material Design leans on shadow as the primary depth cue and Apple uses subtle dual-layer shadows, shadcn uses borders. A `1px` hairline in `#e5e5e5` does the work of a 4-layer shadow. This has two effects: (1) the system feels flat, modern, and CAD-like, and (2) it renders identically in light and dark mode without tuning. Shadows only appear when depth is functionally required — dropdowns that float over content, modals that interrupt the page, focus rings that must be perceivable. Every other surface "lifts" through border contrast alone.

## 7. Do's and Don'ts

### Do
- Use `10px` as the default border-radius for buttons, inputs, and cards — this is the single most identifying measurement in the system
- Apply `-2.4px` letter-spacing to hero headlines at 48px — negative tracking is Geist's signature
- Use `#e5e5e5` borders instead of shadows for standard card elevation
- Pair Geist with Geist Mono for any data, timestamp, or code display
- Default to weight 600 for headings, weight 500 for buttons/links, weight 400 for body
- Use the Tailwind neutral scale (`zinc` or `neutral`) as your full palette — resist the urge to add color
- Reserve `9999px` (full pill) for badges, switches, and avatars only
- Use `1px` focus rings (`0 0 0 2px #0a0a0a` offset by `2px`) — never colored rings

### Don't
- Don't use drop shadows on static cards — the hairline border is the elevation
- Don't use letter-spacing at body sizes (14-16px) — keep tracking at normal
- Don't use weight 700/800 for headings — 600 is the heavy end of the scale
- Don't use pill-radius (`9999px`) on buttons or inputs — those are `10px`
- Don't use saturated brand colors in the default theme — the whole point is monochrome
- Don't mix Geist with Inter or system-ui for headings — the Geist Fallback handles loading
- Don't use border-radius above `14px` on cards — it starts to look Material
- Don't skip the focus ring — shadcn's accessibility story is load-bearing (Radix underneath)

## 8. Responsive Behavior

### Breakpoints (Tailwind defaults)
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | `<640px` | Single column, sidebar collapses to sheet, hero scales to 32px |
| sm | `640px+` | 2-column grids allowed, forms stay single-column |
| md | `768px+` | Docs sidebar appears, 3-column component grids |
| lg | `1024px+` | Full desktop layout, 4-column grids for component galleries |
| xl | `1280px+` | Max content width applies (`1400px`) |

### Touch Targets
- Buttons maintain `36px` minimum height (h-9 = `9px × 2` padding + text) — at the accessibility floor
- Touch-friendly icon buttons use `h-10 w-10` (`40px × 40px`)
- Tappable list items have `py-3` minimum (`12px` vertical padding)

### Collapsing Strategy
- Hero: 48px → 36px → 30px across breakpoints, weight 600 maintained
- Docs sidebar: fixed 256px on desktop → slide-in sheet on mobile (triggered by hamburger)
- Component grids: `lg:grid-cols-4` → `md:grid-cols-2` → single column
- Form fields: always single column; only labels shrink on mobile
- Tables: horizontal scroll on mobile with sticky first column
- Dialog/modal width: max 512px on desktop, full-width with padding on mobile

### Image Behavior
- Component screenshots maintain `14px` radius at all sizes
- Og images render at 1200×630 with centered type at `-2.4px` tracking
- Favicons are `16x16` with the subtle black-on-white `S` mark

## 9. Agent Prompt Guide

### Quick Color Reference
- Background: `#ffffff`
- Foreground (text): `#0a0a0a`
- Primary button: `#171717` (dark) with `#fafafa` text
- Secondary button: `#ffffff` with `1px solid #e5e5e5`
- Muted surface: `#f5f5f5`
- Muted text: `#737373`
- Border (everywhere): `#e5e5e5`
- Placeholder text: `#a1a1a1`
- Focus ring: `#0a0a0a` at 2px with 2px offset
- Destructive: `#ef4444`

### Example Component Prompts
- "Create a hero section on white (`#ffffff`). Headline at 48px Geist weight 600, line-height 1.10, letter-spacing -2.4px, color #0a0a0a. Subtitle at 18px weight 400, line-height 1.56, color #737373. Primary button (#171717 bg, #fafafa text, 10px radius, 9px 16px padding, 14px Geist weight 500) and outline button (#ffffff bg, 1px solid #e5e5e5, 10px radius, 14px weight 500)."
- "Design a card: white background, 1px solid #e5e5e5 border, 14px radius, 24px padding, no shadow. Title at 20px Geist weight 600, letter-spacing normal. Body at 14px weight 400, #737373 color, line-height 1.43. Action button bottom-right at 10px radius."
- "Build a badge: 12px Geist weight 500, 2px 10px padding, 9999px radius (full pill). Solid variant: #171717 bg, #fafafa text. Outline variant: transparent bg, 1px solid #e5e5e5, #0a0a0a text."
- "Create a form input: #ffffff bg, 1px solid #e5e5e5 border, 10px radius, 9px 12px padding, 14px Geist weight 400, #a1a1a1 placeholder. Focus ring: 0 0 0 2px #0a0a0a with 2px offset (use box-shadow with outline: none)."
- "Design a navigation bar: sticky top, white bg, 1px solid #e5e5e5 bottom border, 16px vertical padding. Links at 14px Geist weight 500, #0a0a0a default, #737373 hover. Right-aligned primary CTA button. Full-width, no internal max-width constraint."

### Iteration Guide
1. Start with `10px` radius — if a component doesn't look right, it's rarely the radius that's wrong
2. Default to weight 600 headings, weight 500 UI text, weight 400 body — no bolder, no lighter
3. Apply `-2.4px` letter-spacing only at 48px+ — below 30px, return to normal tracking
4. Reach for borders before shadows: `1px solid #e5e5e5` solves 90% of depth problems
5. Keep the palette monochrome until a specific semantic role demands color (destructive = red, success = green, but nothing decorative)
6. For any numeric/code display, switch the font stack to Geist Mono — don't just change size
7. Use `#737373` for secondary text, `#a1a1a1` for placeholder/disabled — never `#cccccc` or pure gray
8. Focus rings are non-negotiable — 2px offset 2px thick, black — and must be visible on any background
