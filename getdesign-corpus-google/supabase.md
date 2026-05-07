---
version: alpha
name: Supabase
description: Dark-mode-native developer platform — near-black canvas, Circular geometric sans, emerald-green identity accent, pill primary CTAs, and depth communicated through a precise dark-border hierarchy.

colors:
  # Canvas + surfaces
  background: "#171717"
  surface: "#0f0f0f"
  surface-light: "#242424"
  glass-dark: "#292929"  # was rgba(41,41,41,0.84) — Google format requires hex

  # Brand emerald
  primary: "#3ecf8e"
  primary-link: "#00c573"
  primary-border: "#5a8e72"  # opaque approx of rgba(62,207,142,0.3) over #171717 — Google format requires hex

  # Ink
  ink: "#fafafa"
  ink-near-white: "#efefef"
  ink-light-gray: "#b4b4b4"
  ink-mid-gray: "#898989"
  ink-dark-gray: "#4d4d4d"
  ink-charcoal: "#434343"
  on-primary: "#171717"

  # Border hierarchy
  border-subtle: "#242424"
  border: "#2e2e2e"
  border-mid: "#363636"
  border-light: "#393939"

  # Radix accent tokens (sRGB equivalents)
  accent-purple: "#5b5bd6"
  accent-violet: "#6e56cf"
  accent-crimson: "#e93d82"
  accent-indigo: "#3e63dd"
  accent-yellow: "#ffe629"
  accent-tomato: "#e54d2e"
  accent-orange: "#f76b15"

  # Subtle wash tints (opaque approximations)
  slate-alpha-wash: "#1a1c1f"  # was hsla(210,87.8%,16.1%,0.031) — Google format requires hex
  fixed-frost: "#2c3338"  # was hsla(200,90.3%,93.4%,0.109) — Google format requires hex

  # Shadow tint
  shadow-soft: "#000000"  # was rgba(0,0,0,0.1) — Google format requires hex

typography:
  display-hero:
    fontFamily: "Circular, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  heading-section:
    fontFamily: "Circular, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0px
  card-title:
    fontFamily: "Circular, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: -0.16px
  sub-heading:
    fontFamily: "Circular, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0px
  body:
    fontFamily: "Circular, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  nav-link:
    fontFamily: "Circular, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0px
  button:
    fontFamily: "Circular, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.14
    letterSpacing: 0px
  caption:
    fontFamily: "Circular, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  small:
    fontFamily: "Circular, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  code-label:
    fontFamily: "Source Code Pro, Office Code Pro, Menlo, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 1.2px

spacing:
  hairline: 1px
  xxs: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 48px
  5xl: 64px
  6xl: 96px
  7xl: 128px

rounded:
  none: 0px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  pill: 9999px

components:
  # Primary pill button — dark with white border
  button-primary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 32px

  # Secondary pill — dark with dark border
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 32px

  # Ghost
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 8px 8px
  button-ghost-hover:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink}"

  # Cards
  card:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  card-feature:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xl}"
    padding: 32px

  # Pill tab
  tab:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-mid-gray}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 6px 16px
  tab-active:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.primary}"

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.primary-link}"

  # Frosted overlay panel
  overlay:
    backgroundColor: "{colors.glass-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 16px
---

# Supabase Design System

## Overview

Supabase's website is a dark-mode-native developer platform that channels the aesthetic of a premium code editor — deep black backgrounds (`{colors.surface}`, `{colors.background}`) with emerald green accents (`{colors.primary}`, `{colors.primary-link}`) that reference the brand's open-source, PostgreSQL-green identity. The design system feels like it was born in a terminal window and evolved into a sophisticated marketing surface without losing its developer soul.

The typography is built on "Circular" — a geometric sans-serif with rounded terminals that softens the technical edge. At 72px with a 1.00 line-height, the hero text is compressed to its absolute minimum vertical space, creating dense, impactful statements that waste nothing. The monospace companion (Source Code Pro) appears sparingly for uppercase technical labels with `1.2px` letter-spacing, creating the "developer console" markers that connect the marketing site to the product experience.

What makes Supabase distinctive is its sophisticated HSL-based color token system. Rather than flat hex values, Supabase uses HSL with alpha channels for nearly every color, enabling a nuanced layering system where colors interact through transparency. This creates depth through translucency — borders, surfaces, and accents at partial opacity all blend with the dark background to create a rich, dimensional palette from minimal color ingredients.

The green accent (`{colors.primary}`) appears selectively — in the Supabase logo, in link colors (`{colors.primary-link}`), and in border highlights — always as a signal of "this is Supabase" rather than as a decorative element. Pill-shaped buttons (`{rounded.pill}`) for primary CTAs contrast with standard `{rounded.sm}` radius for secondary elements.

**Key Characteristics:**
- Dark-mode-native: near-black backgrounds (`{colors.surface}`, `{colors.background}`) — never pure black
- Emerald green brand accent (`{colors.primary}`, `{colors.primary-link}`) used sparingly as identity marker
- Circular font — geometric sans-serif with rounded terminals
- Source Code Pro for uppercase technical labels (`1.2px` letter-spacing)
- HSL-based color token system with alpha channels for translucent layering
- Pill buttons (`{rounded.pill}`) for primary CTAs, `{rounded.sm}` for secondary
- Neutral gray scale from `{colors.background}` through `{colors.ink-mid-gray}` to `{colors.ink-near-white}`
- Border system using dark grays (`{colors.border}`, `{colors.border-mid}`, `{colors.border-light}`)
- Minimal shadows — depth through border contrast and transparency
- Radix color primitives (crimson, purple, violet, indigo, yellow, tomato, orange, slate)

## Colors

### Brand
- **Supabase Green** (`{colors.primary}`): Primary brand color, logo, accent borders.
- **Green Link** (`{colors.primary-link}`): Interactive green for links and actions.
- **Green Border** (`{colors.primary-border}`): Subtle green border accent (opaque approximation of `rgba(62,207,142,0.3)`).

### Neutral Scale (Dark Mode)
- **Near Black** (`{colors.surface}`): Primary button background, deepest surface.
- **Dark** (`{colors.background}`): Page background, primary canvas.
- **Dark Border** (`{colors.border-subtle}`): Horizontal rule, section dividers.
- **Border Dark** (`{colors.border}`): Card borders, tab borders.
- **Mid Border** (`{colors.border-mid}`): Button borders, dividers.
- **Border Light** (`{colors.border-light}`): Secondary borders.
- **Charcoal** (`{colors.ink-charcoal}`): Tertiary borders, dark accents.
- **Dark Gray** (`{colors.ink-dark-gray}`): Heavy secondary text.
- **Mid Gray** (`{colors.ink-mid-gray}`): Muted text, link color.
- **Light Gray** (`{colors.ink-light-gray}`): Secondary link text.
- **Near White** (`{colors.ink-near-white}`): Light border, subtle surface.
- **Off White** (`{colors.ink}`): Primary text, button text.

### Radix Color Tokens
- **Purple/Violet/Crimson/Indigo/Yellow/Tomato/Orange** (`{colors.accent-purple}`, `{colors.accent-violet}`, `{colors.accent-crimson}`, `{colors.accent-indigo}`, `{colors.accent-yellow}`, `{colors.accent-tomato}`, `{colors.accent-orange}`): sRGB equivalents of the original HSL Radix tokens — used semantically for state badges and accent moments.

### Surface & Overlay
- **Glass Dark** (`{colors.glass-dark}`): Translucent dark overlay — opaque approximation of `rgba(41, 41, 41, 0.84)`.
- **Slate Alpha Wash** (`{colors.slate-alpha-wash}`): Ultra-subtle blue wash.
- **Fixed Frost** (`{colors.fixed-frost}`): Light frost overlay tint.

### Shadows
Supabase uses **almost no shadows** in its dark theme. Depth is created through border contrast and surface color differences. Focus states use a subtle drop shadow tinted `{colors.shadow-soft}`.

## Typography

### Font Families
- **Primary**: `Circular`, fallback `Helvetica Neue, Helvetica, Arial`
- **Monospace**: `Source Code Pro`, fallback `Office Code Pro, Menlo`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`).

| Token | Use |
|---|---|
| `display-hero` | Maximum density, zero waste (72px / 1.00 line-height) |
| `heading-section` | Feature section titles (36px) |
| `card-title` | Card titles with `-0.16px` tracking (24px) |
| `sub-heading` | Secondary headings (18px) |
| `body` | Standard body text (16px) |
| `nav-link` | Navigation items (14px / 500) |
| `button` | Button labels (14px / 500) |
| `caption` | Metadata, tags |
| `small` | Fine print, footer links (12px) |
| `code-label` | Uppercase Source Code Pro technical markers |

### Principles
- **Weight restraint**: Nearly all text uses weight 400. Weight 500 appears only for navigation and button labels. There is no bold (700) — hierarchy is created through size, not weight.
- **1.00 hero line-height**: The hero text is compressed to absolute zero leading — the defining typographic gesture: dense, efficient, no wasted vertical space.
- **Negative tracking on cards**: Card titles use `-0.16px` letter-spacing — a subtle differentiator.
- **Monospace as ritual**: Source Code Pro in uppercase with `1.2px` letter-spacing is the "developer console" voice — used sparingly.
- **Geometric personality**: Circular's rounded terminals create warmth in what could otherwise be a cold technical interface.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

Notable: large jumps from `4xl` (48px) → `5xl` (64px) → `6xl` (96px) → `7xl` (128px) for major section spacing.

### Grid & Container
- Centered content with generous max-width
- Full-width dark sections with constrained inner content
- Feature grids: icon-based grids with consistent card sizes
- Logo grids for "Trusted by" sections
- Footer: multi-column on dark background

### Whitespace Philosophy
- **Dramatic section spacing**: `6xl`–`7xl` between major sections creates a cinematic pacing.
- **Dense content blocks**: Within sections, spacing is tight (`lg`–`2xl`), creating concentrated information clusters.
- **Border-defined space**: Instead of whitespace + shadows for separation, Supabase uses thin borders on dark backgrounds — separation through line, not gap.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, border `{colors.border}` | Default state, most surfaces |
| Subtle Border (Level 1) | Border `{colors.border-mid}` or `{colors.border-light}` | Interactive elements, hover |
| Focus (Level 2) | Drop shadow tinted `{colors.shadow-soft}` | Focus states only |
| Green Accent (Level 3) | Border `{colors.primary-border}` | Brand-highlighted elements |

**Shadow Philosophy**: Supabase deliberately avoids shadows. In a dark-mode-native design, shadows are nearly invisible and serve no purpose. Instead, depth is communicated through a sophisticated border hierarchy — from `{colors.border-subtle}` (barely visible) through `{colors.border}` (standard) to `{colors.border-light}` (prominent). The green accent border is the "elevated" state — the brand color itself becomes the depth signal.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Inline rules, separators |
| `sm` | 6px | Ghost buttons, small elements |
| `md` | 8px | Cards, containers |
| `lg` | 12px | Mid-size panels |
| `xl` | 16px | Feature cards, major containers |
| `pill` | 9999px | Primary buttons, tab indicators |

## Components

The complete component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card}`).

### Buttons
- **`button-primary`** — Dark `{colors.surface}` pill with white border (`1px solid {colors.ink}`). Use for "Start your project" CTAs.
- **`button-secondary`** — Dark pill with `1px solid {colors.border}` muted border, opacity 0.8.
- **`button-ghost`** — Transparent rectangle with `{rounded.sm}` corners for tertiary/icon actions.

### Cards & Containers
- **`card`** — Dark surface with `1px solid {colors.border}` border, `{rounded.md}` corners.
- **`card-feature`** — Larger feature card at `{rounded.xl}` corners.

### Tabs
- **`tab`** / **`tab-active`** — Pill tabs (`{rounded.pill}`); active state lifts to `{colors.surface-light}` with green text.

### Links
- Brand green (`{colors.primary-link}`) for Supabase-marked links
- Off-white (`{colors.ink}`) for standard links
- Light gray (`{colors.ink-light-gray}`) for muted links
- Mid gray (`{colors.ink-mid-gray}`) for tertiary/footer links

### Navigation
- **`nav-bar`** — Dark page-matching nav with Supabase logo (green icon), Circular 14px/500 nav links, green "Start your project" CTA pill, sticky behavior.

### Overlay
- **`overlay`** — Frosted dark glass panel using `{colors.glass-dark}`.

## Do's and Don'ts

### Do
- Use near-black backgrounds (`{colors.surface}`, `{colors.background}`) — depth comes from the gray border hierarchy
- Apply Supabase green (`{colors.primary}`, `{colors.primary-link}`) sparingly — it's an identity marker, not a decoration
- Use Circular at weight 400 for nearly everything — 500 only for buttons and nav
- Set hero text to 1.00 line-height — the zero-leading is the typographic signature
- Create depth through border color differences (`{colors.border-subtle}` → `{colors.border}` → `{colors.border-mid}`)
- Use pill shape (`{rounded.pill}`) exclusively for primary CTAs and tabs
- Employ HSL-based colors with alpha for translucent layering effects
- Use Source Code Pro uppercase labels for developer-context markers

### Don't
- Don't add box-shadows — they're invisible on dark backgrounds and break the border-defined depth system
- Don't use bold (700) text weight — the system uses 400 and 500 only
- Don't apply green to backgrounds or large surfaces — it's for borders, links, and small accents
- Don't use warm colors (crimson, orange) as primary design elements — they exist as semantic tokens for states
- Don't increase hero line-height above 1.00 — the density is intentional
- Don't use large border radius (16px+) on buttons — pills (`{rounded.pill}`) or standard (`{rounded.sm}`)
- Don't lighten the background above `{colors.background}` for primary surfaces — the darkness is structural
- Don't forget the translucent borders — alpha border colors are the layering mechanism

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <600px | Single column, stacked features, condensed nav |
| Desktop | >600px | Multi-column grids, full nav, expanded sections |

*Note: Supabase uses a notably minimal breakpoint system — primarily a single 600px breakpoint, suggesting a mobile-first approach with progressive enhancement.*

### Collapsing Strategy
- Hero: 72px → scales down proportionally
- Feature grids: multi-column → single column stacked
- Logo row: horizontal → wrapped grid
- Navigation: full → hamburger
- Section spacing: 90–128px → 48–64px
- Buttons: inline → full-width stacked

---

## Agent Prompt Guide

### Quick Color Reference
- Background: `{colors.surface}` (button), `{colors.background}` (page)
- Text: `{colors.ink}` (primary), `{colors.ink-light-gray}` (secondary), `{colors.ink-mid-gray}` (muted)
- Brand green: `{colors.primary}` (brand), `{colors.primary-link}` (links)
- Borders: `{colors.border-subtle}` (subtle), `{colors.border}` (standard), `{colors.border-mid}` (prominent)
- Green border: `{colors.primary-border}` (accent)

### Example Component Prompts
- "Create a hero section on `{colors.background}` background. Headline at 72px Circular weight 400, line-height 1.00, `{colors.ink}` text. Sub-text at 16px Circular weight 400, line-height 1.50, `{colors.ink-light-gray}`. Pill CTA button (`{colors.surface}` bg, `{colors.ink}` text, 9999px radius, 8px 32px padding, 1px solid `{colors.ink}` border)."
- "Design a feature card: `{colors.background}` background, 1px solid `{colors.border}` border, 16px radius. Title at 24px Circular weight 400, letter-spacing -0.16px. Body at 14px weight 400, `{colors.ink-mid-gray}` text."
- "Build navigation bar: `{colors.background}` background. Circular 14px weight 500 for links, `{colors.ink}` text. Supabase logo with green icon left-aligned. Green pill CTA 'Start your project' right-aligned."
- "Create a technical label: Source Code Pro 12px, uppercase, letter-spacing 1.2px, `{colors.ink-mid-gray}` text."
- "Design a framework logo grid: 6-column layout on dark, grayscale logos at 60% opacity, 1px solid `{colors.border}` between sections."

### Iteration Guide
1. Start with `{colors.background}` — everything is dark-mode-native
2. Green is the brand identity marker — use it for links, logo, and accent borders only
3. Depth comes from borders (`{colors.border-subtle}` → `{colors.border}` → `{colors.border-mid}`), not shadows
4. Weight 400 is the default for everything — 500 only for interactive elements
5. Hero line-height of 1.00 is the signature typographic move
6. Pill (`{rounded.pill}`) for primary actions, `{rounded.sm}` for secondary, `{rounded.md}`–`{rounded.xl}` for cards
7. HSL with alpha channels creates the sophisticated translucent layering
