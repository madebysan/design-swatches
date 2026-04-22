# Design System Inspired by Atlassian Design System

## 1. Visual Theme & Atmosphere

The Atlassian Design System is the enterprise design vocabulary that powers Jira, Confluence, Trello, and Bitbucket — four products serving 250,000+ organizations, with a design system that has to stay consistent across 30 years of product evolution. The homepage opens on a clean white canvas (`#ffffff`) with near-black text (`#101214`) and an **unmistakable blue** (`#1868db`) — Atlassian's primary brand color, applied sparingly but with authority. This is enterprise SaaS perfected: precise, accessible, boringly consistent in the best possible way.

Typography uses Atlassian's **custom typeface — Atlassian Sans** — with a secondary **Charlie Display** for marketing headlines and **Atlassian Mono** for code. The sans uses an unusual weight 653 (variable-font custom axis) for the display tier, along with more conventional 500/700. The 653 weight is between semibold (600) and bold (700), giving display type a distinct confidence without shouting.

The defining differentiator is Atlassian's **semantic token vocabulary** — 24+ design tokens found in the CSS scan, named with precise intent: `--ds-background-brand-subtlest-hovered`, `--ds-text-accent-teal`, `--ds-background-brand-boldest`. Each token encodes role + intensity + state. This is enterprise design systems done right — tokens that describe purpose, not appearance.

**Key Characteristics:**
- Atlassian Sans (custom typeface) with weight 653 as a variable-font signature
- Electric blue brand (`#1868db`) applied sparingly as primary accent
- Rich palette of sub-brand accent colors (saffron, teal, purple, magenta, orange)
- `4px` / `8px` dominant radii — conservative, enterprise-appropriate
- Semantic token naming (`ds-background-brand-subtlest-hovered`)
- Dual-layer shadow system for precise elevation
- Accessibility-first: WCAG AAA compliance by default
- Design-for-scale: Jira alone has 1,000+ distinct UI views

## 2. Color Palette & Roles

### Brand
- **Brand Blue** (`#1868db`): Primary brand color — 426 occurrences. CTAs, links, active states.
- **Brand Boldest** (`#1c2b42`): Deep navy for dark brand surfaces. `--ds-background-brand-boldest`.
- **Brand Subtlest** (`#e8f1ff`): Pale blue tint for hover states.
- **Brand Subtlest Hovered** (`#cfe1fd`): Slightly stronger hover tint. `--ds-background-brand-subtlest-hovered`.
- **Brand Pressed** (`#adcbfb`): Active press state. `--ds-background-brand-subtlest-pressed`.

### Neutral Scale
- **Neutral 900** (`#101214`): Primary text, strongest emphasis.
- **Neutral 800** (`#1e1f21`): Dark text.
- **Neutral 700** (`#44546f`): Label text.
- **Neutral 600** (`#505258`): Secondary text — 146 occurrences.
- **Neutral 400** (`#7d818a`): Muted text.
- **Neutral 300** (`#b3b9c4`): Placeholders, disabled.
- **Neutral 200** (`#dcdfe4`): Default borders.
- **Neutral 100** (`#f8f9fa`): Muted surface.
- **Neutral 0** (`#ffffff`): Base canvas.

### Accent (sub-brand colors)
- **Saffron** (`#fca700`): `--ad-color-brand-saffron`. Highlighting warnings.
- **Grass Green** (`#6a9a23`): Success states (44 occurrences).
- **Magenta** (`#af59e1`): Status indicators (27 occurrences). `--ds-text-accent-magenta-bolder: #50253F`.
- **Purple** (`#af5eff`): Beta features, new indicators. `--ds-text-accent-purple-bolder: #48245D`.
- **Orange** (`#e06c00`): Warnings. `--ds-text-orange-bolder`.
- **Teal** (`#206a83`): Info states. `--ds-text-accent-teal: #206A83`.
- **Blue Bolder** (`#123263`): Deep blue for accent-blue text.

### Semantic
- **Danger** (`#ae2e24`): Destructive. `--ds-text-danger: #AE2E24`.
- **Warning** (`#9e4c00`): Warning text. `--ds-text-warning: #9E4C00`.

## 3. Typography Rules

### Font Family
- **Primary**: `Atlassian Sans` — Atlassian's custom sans-serif (variable font with weight axis including 475, 500, 653, 700).
- **Display**: `Charlie Display` — a more expressive display typeface used for marketing hero moments only.
- **Monospace**: `Atlassian Mono` — custom mono for code.
- Fallback stack: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Giant | Atlassian Sans | 112px | 700 | 1.02 | normal |
| Display Hero | Atlassian Sans | 68px | 700 | 1.05 | normal |
| Display Large | Atlassian Sans | 44px | 700 | 1.10 | normal |
| Display / Charlie | Charlie Display | 32px | 653 | 1.15 | normal |
| H1 | Atlassian Sans | 40px | 653 | 1.15 | normal |
| H2 | Atlassian Sans | 28px | 500 | 1.25 | normal |
| H3 | Atlassian Sans | 24px | 400 | 1.30 | normal |
| Body Large | Atlassian Sans | 16px | 400 | 1.50 | normal |
| Body | Atlassian Sans | 14px | 400 | 1.43 | normal |
| Caption | Atlassian Mono | 14px | 400 | 1.43 | normal |

### Principles
- **Weight 653 is unique**: Available via Atlassian Sans's variable font weight axis. Sits between semibold and bold for display authority.
- **No letter-spacing**: Atlassian explicitly keeps tracking at normal across all sizes — generous and accessible.
- **Charlie Display for marketing only**: H2/H3 inside app UI uses Atlassian Sans; Charlie appears only on marketing pages.
- **Atlassian Mono for code**: Distinct from typical Mono Sans or JetBrains Mono — branded consistency.

## 4. Component Stylings

### Buttons
- **Primary**: `#1868db` bg, white text, `4px` radius, `8px 16px` padding, 14px Atlassian Sans weight 500.
- **Subtle**: `#f8f9fa` bg, `#44546f` text, `4px` radius, hover `#dcdfe4`.
- **Link**: transparent bg, `#1868db` text, no border, no bg.
- **Danger**: `#ae2e24` bg, white text.

### Cards
- `#ffffff` bg, `1px solid #dcdfe4`, `8px` radius, `24px` padding.
- Shadow: `0 1px 1px rgba(30,31,33,0.25), 0 0 1px rgba(30,31,33,0.31)`.

### Inputs
- `#ffffff` bg, `1px solid #dcdfe4`, `4px` radius, `8px 12px` padding.
- Focus: `2px solid #1868db` with no offset (inset focus).

### Badges
- `3px` radius (not pill, not rounded — distinctive), `2px 8px` padding.
- Variants by color scale: success (green), warning (saffron), error (red), in-progress (blue), done (purple).

### Toolbars / Nav
- Fixed top app bar, `48-56px` height, white bg with `1px solid #dcdfe4` bottom border.
- Icon buttons: `32px × 32px`, `3px` radius on hover state.

## 5. Layout Principles

### Spacing System
- Base unit: **4px** (Atlassian's `grid` token)
- Dominant values: `8px` (55 uses), `16px` (18), `12px` (14), `24px` (7), `6px` (20)
- Token names: `space.100` (8px), `space.200` (16px), `space.400` (32px)

### Grid
- Atlassian's `Grid` primitive with `gap`, `alignItems`, `justifyContent` props
- App layout: persistent 56px left rail + 240px nav panel + content
- Marketing: 12-column with `24px` gutter, max `1200px`

### Border Radius Scale
- `2px`: Inline elements, tiny chrome (26 uses)
- `3px`: Badges (distinctive)
- `4px`: Buttons, inputs — the workhorse (16 uses)
- `6-8px`: Cards, dropdowns (9 uses at 8px)
- `16-28px`: Featured callouts, marketing hero cards

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | None | Background |
| Level 1 | `0 1px 1px rgba(30,31,33,0.25), 0 0 1px rgba(30,31,33,0.31)` | Card rest |
| Level 2 | `0 4px 8px rgba(30,31,33,0.15), 0 0 1px rgba(30,31,33,0.31)` | Card hover, menu |
| Level 3 | `0 8px 12px rgba(30,31,33,0.15), 0 0 1px rgba(30,31,33,0.31)` | Dropdown, popover |
| Level 4 | `0 40px 20px 20px rgba(0,0,0,0.09)` | Modal dialogs (unusual spread value) |

**Shadow Philosophy**: Atlassian uses dual-layer shadows with a `0 0 1px` near-shadow for crisp edge definition + a softer far-shadow for depth. The `rgba(30,31,33,...)` shadow color is a neutral near-black that photographs consistently across brand contexts (web, mobile, marketing). Deep shadow uses `0px 40px 20px 20px` spread — highly unusual, creates an atmospheric modal effect.

## 7. Do's and Don'ts

### Do
- Use semantic tokens (`--ds-background-brand-subtlest-hovered`) — not hex
- Default to `4px` radius for buttons/inputs, `8px` for cards
- Use Atlassian Sans weight 653 for display/H1 (variable-font weight axis)
- Reserve Charlie Display for marketing-hero moments only
- Use the rich accent palette (saffron, magenta, teal, purple) for status indicators
- Apply dual-layer shadows — crisp 1px + soft atmospheric

### Don't
- Don't use pill radius on buttons — stays `4px` in app UI
- Don't hardcode brand blue — use the `ds-` tokens
- Don't mix Atlassian Mono with other mono fonts — brand consistency matters
- Don't use tight letter-spacing — Atlassian is normal-tracked at all sizes
- Don't use generic weight 600 for display — the variable-axis 653 is specific

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<600px` | Left rail becomes bottom bar, nav panel slides up |
| Tablet | `600-1024px` | Left rail visible, nav panel toggles |
| Desktop | `1024-1280px` | Full app layout, rail + nav + content |
| Large | `>1280px` | Max content width applied |

### Touch Targets
- Buttons: `32-36px` minimum height
- Icon buttons in toolbars: `32px × 32px`
- Tappable rows: `44px` minimum

### Collapsing Strategy
- Display: 112px → 68px → 44px across breakpoints
- Left rail: persistent → collapsible → bottom nav
- Sidebars: multi-panel → single panel → overlay drawer
- Tables: horizontal scroll with sticky first column

## 9. Agent Prompt Guide

### Quick Color Reference
- Brand Blue: `#1868db`
- Brand Boldest: `#1c2b42`
- Foreground: `#101214`
- Muted FG: `#505258`
- Border: `#dcdfe4`
- Background: `#ffffff`
- Success: `#6a9a23`
- Warning: `#fca700`
- Danger: `#ae2e24`

### Example Component Prompts
- "Create a primary button: #1868db bg, white text, 4px radius, 8px 16px padding, 14px Atlassian Sans weight 500. Hover: #0d5fcb (darker). Focus: 2px inset #1868db ring."
- "Design a card: white bg, 1px solid #dcdfe4, 8px radius, 24px padding, box-shadow 0 1px 1px rgba(30,31,33,0.25), 0 0 1px rgba(30,31,33,0.31). Title at 20px Atlassian Sans weight 500 color #101214."
- "Build a status badge: 3px radius (not pill), 2px 8px padding, 12px Atlassian Sans weight 500. Success: #dfe8d2 bg, #3e5700 text. In progress: #cfe1fd bg, #0055cc text."

### Iteration Guide
1. Tokens, not hex — always use the `ds-` semantic names
2. `4px` radius for interactive, `8px` for cards, `3px` for badges — the enterprise rhythm
3. Weight 653 (variable axis) is the display signature — 500/700 for body
4. Dual-layer shadows with `1px` inner + soft outer
5. Brand blue (`#1868db`) is primary; reserve sub-brand accents for status
6. Accessibility is structural — never skip focus rings, contrast is AAA by default
