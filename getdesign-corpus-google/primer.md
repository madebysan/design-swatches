---
version: alpha
name: Primer
description: GitHub's design system — Mona Sans at custom variable weights (440/480/500), 6px radius workhorse, semantic token vocabulary, and accessibility as structure.

colors:
  # Surfaces
  background: "#ffffff"
  canvas-subtle: "#f6f8fa"
  surface-subtle: "#eff2f5"

  # Text / FG
  ink: "#1f2328"
  fg-muted: "#59636e"
  fg-subtle: "#6e7781"
  fg-faint: "#77827a"

  # Borders
  border: "#d0d7de"
  border-emphasis: "#a3aab1"  # opaque approx of rgba(31,35,40,0.15) over white — Google format requires hex

  # Brand / Accent
  primary: "#0969da"
  accent-fg: "#0969da"
  accent-emphasis: "#0969da"
  accent-muted: "#ddf4ff"

  # Semantic — Success (GitHub uses green as primary action)
  success: "#2da44e"
  success-emphasis: "#1a7f37"
  success-bg: "#dafbe1"

  # Attention
  attention-fg: "#9a6700"

  # Danger
  danger: "#cf222e"
  danger-bg: "#ffebe9"

  # Done / Purple
  done-fg: "#8250df"
  done-bg: "#fbefff"

  # Domain-specific (Primer's signature)
  label-orange-bg: "#fecfaa"
  display-lime-bg: "#e3f2b5"
  data-yellow: "#b88700"
  diff-hunk-bg: "#b6e3ff"

  # Focus
  focus-ring: "#82b8ee"  # opaque approx of rgba(9,105,218,0.3) over white — Google format requires hex

  # Inputs
  on-primary: "#ffffff"

typography:
  display-hero:
    fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 440
    lineHeight: 1.15
    letterSpacing: 0px
  h1:
    fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 34px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0px
  h2:
    fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 480
    lineHeight: 1.25
    letterSpacing: 0px
  h3:
    fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 480
    lineHeight: 1.30
    letterSpacing: 0px
  title:
    fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0px
  body-large:
    fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  body:
    fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  button:
    fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  caption:
    fontFamily: "Mona Sans, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  code:
    fontFamily: "ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px

rounded:
  sharp: 2px
  sm: 6px
  md: 8px
  lg: 24px
  pill: 9999px

components:
  # Buttons
  button-secondary:
    backgroundColor: "{colors.canvas-subtle}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 5px 16px
  button-primary:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 5px 16px
  button-outline:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 5px 16px
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 5px 16px
  button-invisible:
    backgroundColor: "{colors.background}"
    textColor: "{colors.fg-muted}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 5px 16px

  # Cards / Boxes
  box:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 16px

  # Inputs
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 5px 12px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
  input-code:
    backgroundColor: "{colors.canvas-subtle}"
    textColor: "{colors.ink}"
    typography: "{typography.code}"
    rounded: "{rounded.sm}"
    padding: 5px 12px

  # Labels / Tags (Primer's distinctive component)
  label-rounded:
    backgroundColor: "{colors.canvas-subtle}"
    textColor: "{colors.fg-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.lg}"
    padding: 2px 10px

  # State badges
  state-open:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-emphasis}"
    typography: "{typography.caption}"
    rounded: "{rounded.lg}"
    padding: 2px 10px
  state-closed:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger}"
    typography: "{typography.caption}"
    rounded: "{rounded.lg}"
    padding: 2px 10px
  state-merged:
    backgroundColor: "{colors.done-bg}"
    textColor: "{colors.done-fg}"
    typography: "{typography.caption}"
    rounded: "{rounded.lg}"
    padding: 2px 10px
  state-draft:
    backgroundColor: "{colors.canvas-subtle}"
    textColor: "{colors.fg-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.lg}"
    padding: 2px 10px

  # Avatar
  avatar:
    backgroundColor: "{colors.canvas-subtle}"
    rounded: "{rounded.pill}"
    padding: 0px

  # Domain badges
  attention-badge:
    backgroundColor: "{colors.canvas-subtle}"
    textColor: "{colors.attention-fg}"
    typography: "{typography.caption}"
    rounded: "{rounded.lg}"
    padding: 2px 10px
---

# Primer Design System

## Overview

Primer is GitHub's design system — the chrome that renders 100 million pull requests, 4 billion lines of code, and countless merge conflicts. The homepage opens in a measured palette: white canvas (`{colors.background}`), a deep charcoal text (`{colors.ink}`) that isn't quite black, and GitHub's signature interactive blue (`{colors.accent-fg}`) applied with developer-grade restraint. This is design for developers by developers — every pixel justified by an accessibility audit, every component drawn in context of 240+ semantic color tokens.

Typography is **Mona Sans** — GitHub's custom variable typeface. The display treatment uses an unusual weight 440 (a variable-font custom axis between light and regular), weight 480 for section headlines, and weight 500 for UI. The variable weight axis lets Primer tune type to exact intent: weight 440 for confident-but-quiet hero text, weight 480 for emphasis without shouting. Monospace content renders in `ui-monospace` (system default) — GitHub intentionally avoids a branded mono to stay ecosystem-neutral.

The defining feature is Primer's **token vocabulary**: 240+ semantic color tokens found in the CSS scan, each named by purpose (`--diffBlob-hunkNum-bgColor-rest`, `--base-color-scale-teal-4`, `--brand-Label-color-green-blue-start`). This is the deepest token system in any design system we've scanned — every micro-context of GitHub UI has its own named color. The philosophy: if a designer has to pick a color from memory, something is under-specified.

**Key Characteristics:**
- Mona Sans at weight 440 for display — variable font axis, custom weight
- Deep charcoal text (`{colors.ink}`) instead of pure black
- GitHub's interactive blue (`{colors.accent-fg}`) as the single interactive accent
- `6px` dominant radius on buttons — smaller than most SaaS kits
- 240+ semantic color tokens — extraordinarily deep vocabulary
- Full accessibility compliance (WCAG AAA combos verified)
- Open source — the Primer React + CSS packages are MIT
- Context-specific tokens (`diffBlob`, `label`, `data`, `brand`) — domain vocabulary

## Colors

### Base Scale
- **Gray 9** (`{colors.ink}`): Primary text — `--fg-default`. Not black, not gray-900 — a specific charcoal.
- **Gray 7** (`{colors.fg-muted}`): Secondary text — `--fg-muted`.
- **Gray 6** (`{colors.fg-subtle}`): Muted FG.
- **Gray 5** (`{colors.fg-faint}`): Subtle text (20 occurrences on the scan).
- **Gray 3** (`{colors.border}`): Default border — `--border-default`.
- **Gray 2** (`{colors.surface-subtle}`): Subtle surface.
- **Gray 1** (`{colors.canvas-subtle}`): Muted canvas — `--canvas-subtle`.
- **White** (`{colors.background}`): Primary canvas — `--canvas-default`.

### Accent / Interactive
- **Accent FG** (`{colors.accent-fg}`): Links, active states.
- **Accent Emphasis** (`{colors.accent-emphasis}`): Primary button bg.
- **Accent Muted** (`{colors.accent-muted}`): Subtle accent bg.

### Semantic Roles
- **Success FG** (`{colors.success}`): Merged, built, passing — `--success-fg`. GitHub uses green as primary action color.
- **Success Emphasis** (`{colors.success-emphasis}`): Strong success.
- **Attention FG** (`{colors.attention-fg}`): Draft, amber, warn.
- **Danger FG** (`{colors.danger}`): Error, failure.
- **Done FG** (`{colors.done-fg}`): Closed PR, purple.

### Domain-Specific
- **Label Orange BG** (`{colors.label-orange-bg}`): Specific hover state for orange labels.
- **Display Lime BG** (`{colors.display-lime-bg}`): Data viz color in lime scale.
- **Data Yellow** (`{colors.data-yellow}`): Specific to data displays.
- **DiffBlob HunkNum BG** (`{colors.diff-hunk-bg}`): The line-number background on a diff hunk header — yes, this has its own token.

## Typography

### Font Family
- **Primary**: `Mona Sans`, fallback: `-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif`.
- **Variable Font**: Mona Sans is a variable font with weight axis 100–900. Custom weights like 440 and 480 are specific Primer values.
- **Monospace**: `ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace`.
- Primer ships Mona Sans via `@github/mona-sans` NPM package.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | Hero / display — Mona Sans 440 |
| `h1` | Section H1 — Mona Sans 500 |
| `h2` | Section H2 — Mona Sans 480 |
| `h3` | Sub-section — Mona Sans 480 |
| `title` | Card or list titles — weight 400 |
| `body-large` | Lead body, intros |
| `body` | Standard reading text — Mona Sans 14px |
| `button` | UI controls, buttons |
| `caption` | Metadata, fine print |
| `code` | Code, branch names, SHAs |

### Principles
- **Weight 440 is unique**: Custom variable-axis weight for display. Sits between light (300) and regular (400) — confident but not bold.
- **Weight 480 for section headlines**: Between regular and medium — subtle emphasis.
- **No tight letter-spacing**: Primer keeps all tracking at normal — accessibility and readability first.
- **Mona Sans Variable (VF suffix)**: Primer distinguishes "Mona Sans" (static weights) from "Mona Sans VF" (variable font) in the scan — the VF handles body sizes.

## Layout

### Spacing System
Base unit is **4px** (Primer uses rem for sizing, 16px base). Vertical rhythm favors `3xl` (32px) section gaps and `lg`–`2xl` (16–24px) within.

### Grid
- Max content widths: 768px (reading), 1280px (app)
- Sidebar patterns: persistent 296px on GitHub app UI
- Marketing: 12-column with 32px gutters

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | None | Background, most cards |
| Level 1 | `0 1px 0 rgba(31,35,40,0.04)` | Subtle card lift, only 3 uses |
| Level 2 | `0 3px 6px rgba(31,35,40,0.15)` | Menu, popover |
| Level 3 | `0 8px 24px rgba(31,35,40,0.2)` | Modal, large overlay |

**Shadow Philosophy**: Primer uses shadows minimally — the scan found only 3 shadow occurrences total, all the same `0 1px 0` value. Elevation is carried by `1px` borders and whitespace, not by drop shadows. This is a deliberate aesthetic choice: GitHub's chrome stays flat so that user content (code, diffs, issues) reads as the elevated material.

## Shapes

| Token | Value | Use |
|---|---|---|
| `sharp` | 2px | Kbd, separators |
| `sm` | 6px | Buttons, inputs — Primer's workhorse |
| `md` | 8px | Images, small cards |
| `lg` | 24px | Labels, pills, status badges |
| `pill` | 9999px | Avatars, some badges |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (`{components.button-primary}`, `{components.state-open}`) rather than reconstructing them.

### Buttons
- **`button-secondary`** — Default GitHub button: `{colors.canvas-subtle}` surface, gray border, 6px radius.
- **`button-primary`** — `{colors.success}` (green) bg, white text — GitHub uses green as primary action color (merge, create).
- **`button-outline`** — Transparent bg, dark border.
- **`button-danger`** — Red bg, white text.
- **`button-invisible`** — Transparent, muted text.

### Cards / Boxes
- **`box`** — White bg, 1px gray-200 border, 6px radius. Primer calls containers "Box" not "Card" — intentional naming.

### Inputs
- **`input`** — White bg, 1px subtle border, 6px radius, 5px 12px padding.
- **`input-focus`** — 2px primary border with 3px tinted ring.
- **`input-code`** — Uses ui-monospace in code-input fields (branch names, commit messages).

### Labels / State Badges
- **`label-rounded`** — 24px radius (very rounded but not pill), 2px 10px padding. Hundreds of pre-defined label colors via `--label-*` tokens.
- **`state-open`** — Green: `{colors.success-bg}` bg, `{colors.success-emphasis}` text.
- **`state-closed`** — Red: `{colors.danger-bg}` bg, `{colors.danger}` text.
- **`state-merged`** — Purple: `{colors.done-bg}` bg, `{colors.done-fg}` text.
- **`state-draft`** — Gray: `{colors.canvas-subtle}` bg, `{colors.fg-muted}` text.
- **`attention-badge`** — Amber/attention text on a subtle surface.

## Do's and Don'ts

### Do
- Use the `fg-*`, `bg-*`, `border-*` semantic tokens — never hardcoded hex
- Use Mona Sans at weight 440 for display, weight 500 for UI, weight 400 for body
- Default to `6px` radius for buttons, inputs — the Primer workhorse
- Use `24px` radius for labels and status badges (not pill)
- Use green (`{colors.success}`) for primary actions — merge, create, commit
- Keep elevation flat — 1px borders carry all the lift
- Use `ui-monospace` for code, branch names, commit SHAs

### Don't
- Don't use drop shadows liberally — Primer is flat
- Don't use pill radius on buttons or inputs — stays `6px`
- Don't use Mona Sans weight 700 — Primer caps at 500
- Don't use tight letter-spacing — accessibility first
- Don't use bright brand colors beyond GitHub blue — resist decorative color
- Don't skip focus rings — the 3px tinted accent ring is the accessibility baseline

## Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|---|---|---|
| Mobile | `<544px` | Single column, hamburger nav |
| sm | `544–768px` | Tablet layout, sidebar toggle |
| md | `768–1012px` | Content + single sidebar |
| lg | `1012–1280px` | Full GitHub app layout |
| xl | `>1280px` | Max content width applied |

### Touch Targets
- Buttons: `32–36px` minimum height (Primer uses `height: auto` with `py-1.5` style)
- Tappable list items: `44px` minimum

### Collapsing Strategy
- Display: 56px → 34px on mobile
- GitHub app: multi-sidebar → single-sidebar → drawer
- Tables: horizontal scroll with sticky first column
- Labels: wrap to multiple lines rather than truncate

## Agent Prompt Guide

### Quick Color Reference
- Foreground: `{colors.ink}` (fg-default)
- Muted FG: `{colors.fg-muted}` (fg-muted)
- Accent FG: `{colors.accent-fg}`
- Canvas: `{colors.background}`
- Canvas Subtle: `{colors.canvas-subtle}`
- Border: `{colors.border}` (border-default)
- Success: `{colors.success}`
- Danger: `{colors.danger}`

### Example Component Prompts
- "Create a GitHub-style header: white bg, 1px solid `{colors.border}` bottom border. Logo left. Nav links 14px Mona Sans weight 500 color `{colors.ink}`. Search input: `{colors.canvas-subtle}` bg, 1px subtle border, 6px radius. Primary button: `{colors.success}` bg (green!), white text, 6px radius, 5px 16px padding."
- "Design a PR card: white bg, 1px solid `{colors.border}`, 6px radius. Title 16px Mona Sans weight 500 color `{colors.ink}`. Status label: 24px radius, 2px 10px padding — `{colors.success-bg}` bg + `{colors.success-emphasis}` text (merged) or `{colors.danger-bg}` bg + `{colors.danger}` text (closed)."
- "Build a diff viewer: ui-monospace 13px weight 400. Line number column `{colors.canvas-subtle}` bg color `{colors.fg-subtle}`. Added lines `{colors.success-bg}` bg color `{colors.success-emphasis}`. Removed lines `{colors.danger-bg}` bg color `{colors.danger}`."

### Iteration Guide
1. Primer uses semantic tokens exclusively — `fg-default`, `border-default`, `accent-emphasis`
2. `6px` is the default radius — not 8, not 10, specifically 6
3. Green is the primary action color — not blue (blue is for links)
4. Mona Sans weight 440 for display, 500 for UI, 400 for body
5. Elevation is flat — 1px borders and whitespace carry depth
6. Accessibility is structural — every component ships with keyboard + screen reader tested
