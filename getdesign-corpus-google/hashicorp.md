---
version: alpha
name: HashiCorp
description: Enterprise infrastructure design language — dual light/dark modes, custom HashiCorp Sans 600–700 weight headings, multi-product brand color system via mds-color tokens, whisper-level shadows, tight 2–8px radii.

colors:
  # Brand primary
  primary: "#000000"               # HashiCorp brand black

  # Surfaces (dual mode)
  background: "#ffffff"             # Light bg
  surface-light: "#f1f2f3"          # subtle light surface
  background-dark: "#15181e"        # Dark Charcoal — hero/dark mode
  background-darker: "#0d0e12"      # Near Black — deepest dark surface

  # Text
  ink: "#000000"
  ink-dark: "#3b3d45"               # Charcoal — secondary text on light
  ink-inverted: "#efeff1"           # Near White — primary text on dark
  text-secondary: "#d5d7db"         # Mid Gray — button text on dark
  text-helper: "#656a76"            # Helper text
  text-subtle: "#b2b6bd"            # Cool Gray

  # Product brand colors
  terraform: "#7b42bc"
  vault: "#ffcf25"
  waypoint: "#14c6cb"
  waypoint-hover: "#12b6bb"
  vagrant: "#1868f2"
  purple-accent: "#911ced"
  purple-visited: "#a737ff"
  purple-deep: "#42225b"
  badge-border: "#b457ff"

  # Semantic
  link: "#2264d6"                   # primary links on light
  link-dark: "#1060ff"              # primary action on dark
  link-bright: "#2b89ff"
  amber: "#bb5a00"
  amber-light: "#fbeabf"
  vault-faint: "#fff9cf"
  orange-core: "#a9722e"
  red-core: "#731e25"
  navy-core: "#101a59"

  # Borders
  border: "#cccccc"                 # opaque approx of rgba(178,182,189,0.4) over white — Google format requires hex
  border-input: "#616875"
  on-primary: "#ffffff"

  # Shadow stand-in
  shadow-soft: "#f0f0f1"            # opaque approx of rgba(97,104,117,0.05) — Google format requires hex

typography:
  display-hero:
    fontFamily: "HashiCorp Sans, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 82px
    fontWeight: 600
    lineHeight: 1.17
    letterSpacing: 0px
  section-heading:
    fontFamily: "HashiCorp Sans, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 52px
    fontWeight: 600
    lineHeight: 1.19
    letterSpacing: 0px
  feature-heading:
    fontFamily: "HashiCorp Sans, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.19
    letterSpacing: -0.42px
  sub-heading:
    fontFamily: "HashiCorp Sans, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 34px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0px
  card-title:
    fontFamily: "HashiCorp Sans, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.19
    letterSpacing: 0px
  small-title:
    fontFamily: "HashiCorp Sans, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 19px
    fontWeight: 700
    lineHeight: 1.21
    letterSpacing: 0px
  body-emphasis:
    fontFamily: "HashiCorp Sans, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 17px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 0px
  body-large:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  body:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.63
    letterSpacing: 0px
  nav-link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.60
    letterSpacing: 0px
  small-body:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  caption:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  uppercase-label:
    fontFamily: "HashiCorp Sans, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.69
    letterSpacing: 1.3px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 40px
  5xl: 48px
  6xl: 64px
  7xl: 80px

rounded:
  none: 0px
  micro: 2px
  xs: 3px
  sm: 4px
  md: 5px
  card: 8px

components:
  button-primary-dark:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.md}"
    padding: 9px 15px

  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-dark}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    padding: 8px 12px

  button-terraform:
    backgroundColor: "{colors.terraform}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.md}"
    padding: 9px 15px

  button-vault:
    backgroundColor: "{colors.vault}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.md}"
    padding: 9px 15px

  button-waypoint:
    backgroundColor: "{colors.waypoint}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.md}"
    padding: 9px 15px
  button-waypoint-hover:
    backgroundColor: "{colors.waypoint-hover}"

  badge-purple:
    backgroundColor: "{colors.purple-deep}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 3px 7px

  input-dark:
    backgroundColor: "{colors.background-darker}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 11px 11px

  checkbox:
    backgroundColor: "{colors.background-darker}"
    rounded: "{rounded.xs}"
    padding: 0px

  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.card}"
    padding: 24px

  card-dark:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.ink-inverted}"
    rounded: "{rounded.card}"
    padding: 24px

  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-dark}"
    typography: "{typography.nav-link}"
    padding: 16px 24px

  link-light:
    textColor: "{colors.link}"
    typography: "{typography.body}"
    padding: 0px

  link-dark:
    textColor: "{colors.link-dark}"
    typography: "{typography.body}"
    padding: 0px
---

# HashiCorp Design System

## Overview

HashiCorp's website is enterprise infrastructure made tangible — a design system that must communicate the complexity of cloud infrastructure management while remaining approachable. The visual language splits between two modes: a clean white light-mode for informational sections and a dramatic dark-mode (`{colors.background-dark}`, `{colors.background-darker}`) for hero areas and product showcases, creating a day/night duality that mirrors the "build in light, deploy in dark" developer workflow.

The typography is anchored by a custom brand font (HashiCorp Sans) that carries substantial weight — literally. Headings use 600–700 weights with tight line-heights (1.17–1.19), creating dense, authoritative text blocks that communicate enterprise confidence. The hero headline at 82px weight 600 with OpenType `"kern"` enabled is not decorative — it's infrastructure-grade typography.

What distinguishes HashiCorp is its multi-product color system. Each product in the portfolio has its own brand color — Terraform purple (`{colors.terraform}`), Vault yellow (`{colors.vault}`), Waypoint teal (`{colors.waypoint}`), Vagrant blue (`{colors.vagrant}`) — and these colors appear throughout as accent tokens via a CSS custom property system. This creates a design system within a design system: the parent brand is black-and-white with blue accents, while each child product injects its own chromatic identity.

The component system uses the `mds` (Markdown Design System) prefix, indicating a systematic, token-driven approach where colors, spacing, and states are all managed through CSS variables. Shadows are remarkably subtle — dual-layer micro-shadows that are nearly invisible but provide just enough depth to separate interactive surfaces from the background.

**Key Characteristics:**
- Dual-mode: clean white sections + dramatic dark (`{colors.background-dark}`) hero/product areas
- Custom HashiCorp Sans font with 600–700 weights and `"kern"` feature
- Multi-product color system via mds-color CSS custom properties
- Product brand colors: Terraform purple, Vault yellow, Waypoint teal, Vagrant blue
- Uppercase letter-spaced captions (13px, weight 600, 1.3px letter-spacing)
- Micro-shadows: dual-layer at 0.05 opacity — depth through whisper, not shout
- Token-driven mds component system with semantic variable names
- Tight border radius: 2px–8px, nothing pill-shaped or circular
- System-ui fallback stack for secondary text

## Colors

### Brand Primary
- **Black** (`{colors.primary}`): Primary brand color, text on light surfaces.
- **Dark Charcoal** (`{colors.background-dark}`): Dark mode backgrounds, hero sections.
- **Near Black** (`{colors.background-darker}`): Deepest dark mode surface, form inputs on dark.

### Neutral Scale
- **Light Gray** (`{colors.surface-light}`): Light backgrounds, subtle surfaces.
- **Mid Gray** (`{colors.text-secondary}`): Borders, button text on dark.
- **Cool Gray** (`{colors.text-subtle}`): Tertiary text and border accents.
- **Dark Gray** (`{colors.text-helper}`): Helper text, secondary labels.
- **Charcoal** (`{colors.ink-dark}`): Secondary text on light, button borders.
- **Near White** (`{colors.ink-inverted}`): Primary text on dark surfaces.

### Product Brand Colors
- **Terraform Purple** (`{colors.terraform}`)
- **Vault Yellow** (`{colors.vault}`)
- **Waypoint Teal** (`{colors.waypoint}`) and Hover (`{colors.waypoint-hover}`)
- **Vagrant Blue** (`{colors.vagrant}`)
- **Purple Accent** (`{colors.purple-accent}`)
- **Visited Purple** (`{colors.purple-visited}`)

### Semantic Colors
- **Action Blue (light)** (`{colors.link}`): Primary links on light backgrounds.
- **Action Blue (dark)** (`{colors.link-dark}`): Primary action links on dark.
- **Bright Blue** (`{colors.link-bright}`): Active links, hover accent.
- **Amber** (`{colors.amber}`): warning states.
- **Amber Light** (`{colors.amber-light}`): warning backgrounds.
- **Vault Faint Yellow** (`{colors.vault-faint}`)
- **Orange** (`{colors.orange-core}`)
- **Red** (`{colors.red-core}`): error states.
- **Navy** (`{colors.navy-core}`)

### Shadow & Border Tokens
- **Micro Shadow** (`{colors.shadow-soft}`): Default card/button elevation approximation.
- **Border** (`{colors.border}`): Standard 1px border on light surfaces.
- **Border Input** (`{colors.border-input}`): Stronger border on dark inputs.

## Typography

### Font Families
- **Primary Brand**: `HashiCorp Sans` (loaded as `__hashicorpSans_*`), with system fallback.
- **System UI**: `system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial`

### Hierarchy

| Token | Use |
|---|---|
| `display-hero` | 82px HashiCorp Sans 600 — hero with kern enabled |
| `section-heading` | 52px weight 600 |
| `feature-heading` | 42px weight 700 with -0.42px tracking |
| `sub-heading` | 34px weight 600–700 |
| `card-title` | 26px weight 700 |
| `small-title` | 19px weight 700 |
| `body-emphasis` | 17px weight 600–700 — bold body |
| `body-large` | 20px system-ui 400 — hero descriptions |
| `body` | 16px system-ui 400, line-height 1.63 |
| `nav-link` | 15px system-ui 500 |
| `small-body` | 14px system-ui 400 |
| `caption` | 13px system-ui 400 — metadata |
| `uppercase-label` | 13px HashiCorp Sans 600 with 1.3px tracking — wayfinding labels |

### Principles
- **Brand/System split**: HashiCorp Sans for headings and brand-critical text; system-ui for body, navigation, and functional text. The brand font carries the weight, system-ui carries the words.
- **Kern always on**: All HashiCorp Sans text enables OpenType `"kern"` — letterfitting is non-negotiable.
- **Tight headings**: Every heading uses 1.17–1.21 line-height, creating dense, stacked text blocks that feel infrastructural — solid, load-bearing.
- **Relaxed body**: Body text uses 1.50–1.69 line-height (notably generous), creating comfortable reading rhythm beneath the dense headings.
- **Uppercase labels as wayfinding**: 13px uppercase with 1.3px letter-spacing serves as the systematic category/section marker — always HashiCorp Sans weight 600.

## Layout

### Spacing System
Base unit is **8px**. Scale lives in YAML — `micro` (2px) through `7xl` (80px).

### Grid & Container
- Max content width: ~1150px (xl breakpoint)
- Full-width dark hero sections with contained content
- Card grids: 2–3 column layouts
- Generous horizontal padding at desktop scale

### Whitespace Philosophy
- **Enterprise breathing room**: Generous vertical spacing between sections (48px–80px+) communicates stability and seriousness
- **Dense headings, spacious body**: Tight line-height headings sit above relaxed body text, creating visual "weight at the top" of each section
- **Dark as canvas**: Dark hero sections use extra vertical padding to let 3D illustrations and gradients breathe

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Default surfaces, text blocks |
| Whisper (Level 1) | Dual-layer micro shadow at very low alpha (`{colors.shadow-soft}`) | Cards, buttons, interactive surfaces |
| Focus (Level 2) | 3px solid focus outline (color-matched to context) | Focus rings |

**Shadow Philosophy**: HashiCorp uses arguably the subtlest shadow system in modern web design. The dual-layer shadows at 5% opacity are nearly invisible — they exist not to create visual depth but to signal interactivity. If you can see the shadow, it's too strong. This restraint communicates the enterprise value of stability — nothing floats, nothing is uncertain.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `micro` | 2px | Links, small inline elements |
| `xs` | 3px | Checkboxes, small inputs |
| `sm` | 4px | Secondary buttons |
| `md` | 5px | Primary buttons, badges, inputs |
| `card` | 8px | Cards, containers, images |

Nothing pill-shaped or circular — the radius is structurally tight.

## Components

The complete component spec lives in YAML.

### Buttons
- **`button-primary-dark`** — Dark surface button with `{colors.text-secondary}` text and 5px radius.
- **`button-secondary`** — Clean white surface with charcoal text, 4px radius.
- **`button-terraform`** / **`button-vault`** / **`button-waypoint`** (with hover) — Each product owns one branded button color.

### Badges / Pills
- **`badge-purple`** — Deep purple surface for categorical badges.

### Inputs
- **`input-dark`** — Dark form input with `{colors.background-darker}` surface.
- **`checkbox`** — Tight 3px radius checkbox on dark surface.

### Cards
- **`card`** — Light-mode white card with 8px radius and whisper shadow.
- **`card-dark`** — Dark-mode card on `{colors.background-dark}`.

### Navigation
- **`nav-bar`** — Clean horizontal nav. Logo left, links center, CTAs right. Dark mode variant for hero sections.

### Links
- **`link-light`** / **`link-dark`** — Action blue, mode-appropriate.

## Do's and Don'ts

### Do
- Use HashiCorp Sans for headings and brand text, system-ui for body and UI text
- Enable `"kern"` on all HashiCorp Sans text
- Use product brand colors ONLY for their respective products (Terraform = purple, Vault = yellow, etc.)
- Apply uppercase labels at 13px weight 600 with 1.3px letter-spacing for section markers
- Keep shadows at the "whisper" level (0.05 opacity dual-layer)
- Use the mds-color token system for consistent color application
- Maintain the tight-heading / relaxed-body rhythm (1.17–1.21 vs 1.50–1.69 line-heights)
- Use 3px solid focus outlines for accessibility

### Don't
- Don't use product brand colors outside their product context (no Terraform purple on Vault content)
- Don't increase shadow opacity above 0.1 — the whisper level is intentional
- Don't use pill-shaped buttons (>8px radius) — the sharp, minimal radius is structural
- Don't skip the `"kern"` feature on headings — the font requires it
- Don't use HashiCorp Sans for small body text — it's designed for 17px+ heading use
- Don't mix product colors in the same component — each product has one color
- Don't use pure black for dark backgrounds — use `{colors.background-dark}` or `{colors.background-darker}`
- Don't forget the asymmetric button padding — 9px 9px 9px 15px is intentional

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <768px | Single column, hamburger nav, stacked CTAs |
| Tablet | 768–992px | 2-column grids, nav begins expanding |
| Desktop | 992–1150px | Full layout, mega-menu nav |
| Large | >1150px | Max-width centered, generous margins |

### Collapsing Strategy
- Hero: 82px → 52px → 42px heading sizes
- Navigation: mega-menu → hamburger
- Product cards: 3-column → 2-column → stacked
- Dark sections maintain full-width but compress padding
- Buttons: inline → full-width stacked on mobile

---

## Agent Prompt Guide

### Quick Color Reference
- Light bg: `{colors.background}`, `{colors.surface-light}`
- Dark bg: `{colors.background-dark}`, `{colors.background-darker}`
- Text light: `{colors.ink}`, `{colors.ink-dark}`
- Text dark: `{colors.ink-inverted}`, `{colors.text-secondary}`
- Links: `{colors.link}` (light), `{colors.link-dark}` (dark), `{colors.link-bright}` (active)
- Helper text: `{colors.text-helper}`
- Borders: `{colors.border}`, `{colors.border-input}`
- Focus: 3px solid product-appropriate color

### Example Component Prompts
- "Create a hero on dark background (`{colors.background-dark}`). Headline at 82px HashiCorp Sans weight 600, line-height 1.17, kern enabled, white text. Sub-text at 20px system-ui weight 400, line-height 1.50, `{colors.text-secondary}` text. Two buttons: primary dark (`{colors.background-dark}`, `{rounded.md}`, 9px 15px padding) and secondary white (`{colors.background}`, `{rounded.sm}`, 8px 12px padding)."
- "Design a product card: white background, `{rounded.card}` radius, dual-layer shadow at low alpha. Title at 26px HashiCorp Sans weight 700, body at 16px system-ui weight 400 line-height 1.63."
- "Build an uppercase section label: 13px HashiCorp Sans weight 600, line-height 1.69, letter-spacing 1.3px, text-transform uppercase, `{colors.text-helper}` color."
- "Create a product-specific CTA button: Terraform → `{colors.terraform}` background, Vault → `{colors.vault}` with dark text, Waypoint → `{colors.waypoint}`. All: `{rounded.md}` radius, 500 weight text, 16px system-ui."
- "Design a dark form: `{colors.background-darker}` input background, `{colors.ink-inverted}` text, 1px solid `{colors.border-input}` border, `{rounded.md}` radius, 11px padding. Focus: 3px solid accent-color outline."

### Iteration Guide
1. Always start with the mode decision: light (white) for informational, dark (`{colors.background-dark}`) for hero/product
2. HashiCorp Sans for headings only (17px+), system-ui for everything else
3. Shadows are at whisper level (0.05 opacity) — if visible, reduce
4. Product colors are sacred — each product owns exactly one color
5. Focus rings are always 3px solid, color-matched to product context
6. Uppercase labels are the systematic wayfinding pattern — 13px, 600, 1.3px tracking
