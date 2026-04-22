# Design System Inspired by Primer

## 1. Visual Theme & Atmosphere

Primer is GitHub's design system — the chrome that renders 100 million pull requests, 4 billion lines of code, and countless merge conflicts. The homepage opens in a measured palette: white canvas (`#ffffff`), a deep charcoal text (`#1f2328`) that isn't quite black, and GitHub's signature interactive blue (`#0969da`) applied with developer-grade restraint. This is design for developers by developers — every pixel justified by an accessibility audit, every component drawn in context of 240+ semantic color tokens.

Typography is **Mona Sans** — GitHub's custom variable typeface. The display treatment uses an unusual weight 440 (a variable-font custom axis between light and regular), weight 480 for section headlines, and weight 500 for UI. The variable weight axis lets Primer tune type to exact intent: weight 440 for confident-but-quiet hero text, weight 480 for emphasis without shouting. Monospace content renders in `ui-monospace` (system default) — GitHub intentionally avoids a branded mono to stay ecosystem-neutral.

The defining feature is Primer's **token vocabulary**: 240+ semantic color tokens found in the CSS scan, each named by purpose (`--diffBlob-hunkNum-bgColor-rest`, `--base-color-scale-teal-4`, `--brand-Label-color-green-blue-start`). This is the deepest token system in any design system we've scanned — every micro-context of GitHub UI has its own named color. The philosophy: if a designer has to pick a color from memory, something is under-specified.

**Key Characteristics:**
- Mona Sans at weight 440 for display — variable font axis, custom weight
- Deep charcoal text (`#1f2328`) instead of pure black
- GitHub's interactive blue (`#0969da`) as the single interactive accent
- `6px` dominant radius on buttons — smaller than most SaaS kits
- 240+ semantic color tokens — extraordinarily deep vocabulary
- Full accessibility compliance (WCAG AAA combos verified)
- Open source — the Primer React + CSS packages are MIT
- Context-specific tokens (`diffBlob`, `label`, `data`, `brand`) — domain vocabulary

## 2. Color Palette & Roles

### Base Scale (tokens prefixed `--base-color-scale-`)
- **Gray 9** (`#1f2328`): Primary text — `--fg-default`. Not black, not gray-900 — a specific charcoal.
- **Gray 7** (`#59636e`): Secondary text — `--fg-muted`.
- **Gray 6** (`#6e7781`): Muted FG.
- **Gray 5** (`#77827a`): Subtle text (20 occurrences on the scan).
- **Gray 3** (`#d0d7de`): Default border — `--border-default`.
- **Gray 2** (`#eff2f5`): Subtle surface.
- **Gray 1** (`#f6f8fa`): Muted canvas — `--canvas-subtle`.
- **White** (`#ffffff`): Primary canvas — `--canvas-default`.

### Accent / Interactive
- **Accent FG** (`#0969da`): Links, active states — `--accent-fg`.
- **Accent Emphasis** (`#0969da`): Primary button bg — `--accent-emphasis`.
- **Accent Muted** (`#ddf4ff`): Subtle accent bg — `--accent-muted`.
- **Accent Subtle** (`#ddf4ff40`): Very subtle tint.

### Semantic Roles
- **Success FG** (`#2da44e`): Merged, built, passing — `--success-fg`.
- **Success Emphasis** (`#1a7f37`): Strong success.
- **Attention FG** (`#9a6700`): Draft, amber, warn — `--attention-fg`.
- **Danger FG** (`#cf222e`): Error, failure — `--danger-fg`.
- **Done FG** (`#8250df`): Closed PR, purple — `--done-fg`.

### Domain-Specific (Primer's unique feature)
- **Label Orange BG Hover** (`#fecfaa`): Specific hover state for orange labels.
- **Display Lime BG Muted** (`#e3f2b5`): Data viz color in lime scale.
- **Data Yellow Emphasis** (`#b88700`): Specific to data displays.
- **DiffBlob HunkNum BG Rest** (`#b6e3ff`): The line-number background on a diff hunk header — yes, this has its own token.

## 3. Typography Rules

### Font Family
- **Primary**: `Mona Sans`, fallback: `-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif`.
- **Variable Font**: Mona Sans is a variable font with weight axis 100-900. Custom weights like 440 and 480 are specific Primer values.
- **Monospace**: `ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace`.
- Primer ships Mona Sans via `@github/mona-sans` NPM package.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Hero | Mona Sans | 56px | 440 | 1.15 | normal |
| H1 | Mona Sans | 34px | 500 | 1.20 | normal |
| H2 | Mona Sans | 28px | 480 | 1.25 | normal |
| H3 | Mona Sans | 22px | 480 | 1.30 | normal |
| Title | Mona Sans | 22px | 400 | 1.36 | normal |
| Body Large | Mona Sans | 16px | 400 | 1.50 | normal |
| Body | Mona Sans | 14px | 400 | 1.43 | normal |
| Button | Mona Sans | 14px | 500 | 1.43 | normal |
| Caption | Mona Sans | 12px | 400 | 1.33 | normal |
| Code | ui-monospace | 14px | 400 | 1.50 | normal |

### Principles
- **Weight 440 is unique**: Custom variable-axis weight for display. Sits between light (300) and regular (400) — confident but not bold.
- **Weight 480 for section headlines**: Between regular and medium — subtle emphasis.
- **No tight letter-spacing**: Primer keeps all tracking at normal — accessibility and readability first.
- **Mona Sans Variable (VF suffix)**: Primer distinguishes "Mona Sans" (static weights) from "Mona Sans VF" (variable font) in the scan — the VF handles body sizes.

## 4. Component Stylings

### Buttons
- **Default (Secondary)**: `#f6f8fa` bg, `1px solid rgba(31,35,40,0.15)`, `#1f2328` text, `6px` radius, 14px Mona Sans weight 500.
- **Primary**: `#2da44e` bg, white text — GitHub uses green as primary action color (merge, create).
- **Outline**: transparent bg, `1px solid #1f2328`, `#1f2328` text.
- **Danger**: `#cf222e` bg, white text.
- **Invisible**: transparent bg, no border, `#656d76` text.

### Cards / Boxes
- `#ffffff` bg, `1px solid #d0d7de`, `6px` radius, no padding (apply internally).
- Primer calls containers "Box" not "Card" — intentional naming.

### Inputs
- `#ffffff` bg, `1px solid rgba(31,35,40,0.15)`, `6px` radius, `5px 12px` padding, 14px Mona Sans weight 400.
- Focus: `2px solid #0969da`, `0 0 0 3px rgba(9,105,218,0.3)` ring.
- Primer uses `ui-monospace` in code-input fields (branch names, commit messages).

### Labels / Tags (Primer's distinctive component)
- Rounded: `24px` radius (very rounded but not pill), `2px 10px` padding.
- Filled variant: solid color + contrasting text (e.g., `#dafbe1` bg + `#1a7f37` text for Merged).
- Outline variant: transparent bg, 1px colored border.
- Hundreds of pre-defined label colors via `--label-*` tokens.

### State Badges
- **Open** (green): `#dafbe1` bg, `#1a7f37` text.
- **Closed** (red): `#ffebe9` bg, `#cf222e` text.
- **Merged** (purple): `#fbefff` bg, `#8250df` text.
- **Draft** (gray): `#f6f8fa` bg, `#59636e` text.

## 5. Layout Principles

### Spacing System
- Base unit: **4px** (Primer uses rem for sizing, 16px base)
- Dominant values: `32px` (15 uses), `24px` (6), `20px` (5), `12px` (6), `16px` (2)
- Vertical rhythm favors `32px` section gaps, `16-24px` within

### Grid
- Max content widths: `768px` (reading), `1280px` (app)
- Sidebar patterns: persistent 296px on GitHub app UI
- Marketing: 12-column with `32px` gutters

### Border Radius Scale
- Sharp (`2px`): Kbd, separators
- Compact (`6px`): Buttons, inputs — Primer's workhorse (10 uses)
- Medium (`8px`): Images, small cards (3 uses)
- Large (`24px`): Labels, pills, status badges (13 uses)
- Full (`9999px`): Avatars, some badges (3 uses)

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | None | Background, most cards |
| Level 1 | `0 1px 0 rgba(31,35,40,0.04)` | Subtle card lift, only 3 uses |
| Level 2 | `0 3px 6px rgba(31,35,40,0.15)` | Menu, popover |
| Level 3 | `0 8px 24px rgba(31,35,40,0.2)` | Modal, large overlay |

**Shadow Philosophy**: Primer uses shadows minimally — the scan found only 3 shadow occurrences total, all the same `0 1px 0` value. Elevation is carried by `1px` borders and whitespace, not by drop shadows. This is a deliberate aesthetic choice: GitHub's chrome stays flat so that user content (code, diffs, issues) reads as the elevated material.

## 7. Do's and Don'ts

### Do
- Use the `fg-*`, `bg-*`, `border-*` semantic tokens — never hardcoded hex
- Use Mona Sans at weight 440 for display, weight 500 for UI, weight 400 for body
- Default to `6px` radius for buttons, inputs — the Primer workhorse
- Use `24px` radius for labels and status badges (not pill)
- Use green (`#2da44e`) for primary actions — merge, create, commit
- Keep elevation flat — 1px borders carry all the lift
- Use `ui-monospace` for code, branch names, commit SHAs

### Don't
- Don't use drop shadows liberally — Primer is flat
- Don't use pill radius on buttons or inputs — stays `6px`
- Don't use Mona Sans weight 700 — Primer caps at 500
- Don't use tight letter-spacing — accessibility first
- Don't use bright brand colors beyond GitHub blue — resist decorative color
- Don't skip focus rings — the 3px `rgba(9,105,218,0.3)` is the accessibility baseline

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<544px` | Single column, hamburger nav |
| sm | `544-768px` | Tablet layout, sidebar toggle |
| md | `768-1012px` | Content + single sidebar |
| lg | `1012-1280px` | Full GitHub app layout |
| xl | `>1280px` | Max content width applied |

### Touch Targets
- Buttons: `32-36px` minimum height (Primer uses `height: auto` with `py-1.5` style)
- Tappable list items: `44px` minimum

### Collapsing Strategy
- Display: 56px → 34px on mobile
- GitHub app: multi-sidebar → single-sidebar → drawer
- Tables: horizontal scroll with sticky first column
- Labels: wrap to multiple lines rather than truncate

## 9. Agent Prompt Guide

### Quick Color Reference
- Foreground: `#1f2328` (fg-default)
- Muted FG: `#59636e` (fg-muted)
- Accent FG: `#0969da`
- Canvas: `#ffffff`
- Canvas Subtle: `#f6f8fa`
- Border: `#d0d7de` (border-default)
- Success: `#2da44e`
- Danger: `#cf222e`

### Example Component Prompts
- "Create a GitHub-style header: white bg, 1px solid #d0d7de bottom border. Logo left. Nav links 14px Mona Sans weight 500 color #1f2328. Search input: #f6f8fa bg, 1px solid rgba(31,35,40,0.15), 6px radius. Primary button: #2da44e bg (green!), white text, 6px radius, 5px 16px padding."
- "Design a PR card: white bg, 1px solid #d0d7de, 6px radius. Title 16px Mona Sans weight 500 color #1f2328. Status label: 24px radius, 2px 10px padding — #dafbe1 bg + #1a7f37 text (merged) or #ffebe9 bg + #cf222e text (closed)."
- "Build a diff viewer: ui-monospace 13px weight 400. Line number column #f6f8fa bg color #6e7781. Added lines #dafbe1 bg color #1a7f37. Removed lines #ffebe9 bg color #cf222e."

### Iteration Guide
1. Primer uses semantic tokens exclusively — `fg-default`, `border-default`, `accent-emphasis`
2. `6px` is the default radius — not 8, not 10, specifically 6
3. Green is the primary action color — not blue (blue is for links)
4. Mona Sans weight 440 for display, 500 for UI, 400 for body
5. Elevation is flat — 1px borders and whitespace carry depth
6. Accessibility is structural — every component ships with keyboard + screen reader tested
