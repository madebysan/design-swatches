---
version: alpha
name: Miro
description: White-canvas collaborative-tool design with pastel accent pairs, Roobert PRO Medium with OpenType character variants, and a single saturated blue interactive color.

colors:
  # Primary
  primary: "#5b76fe"
  primary-pressed: "#2a41b6"
  ink: "#1c1c1e"
  background: "#ffffff"
  surface: "#ffffff"

  # Pastels (light/dark pairs)
  coral-light: "#ffc6c6"
  coral-dark: "#600000"
  rose-light: "#ffd8f4"
  teal-light: "#c3faf5"
  teal-dark: "#187574"
  orange-light: "#ffe6cd"
  yellow-dark: "#746019"
  moss-dark: "#187574"
  pink-soft: "#fde0f0"
  red-light: "#fbd4d4"
  red-muted: "#e3c5c5"

  # Semantic
  success: "#00b473"

  # Neutral
  text-secondary: "#555a6a"
  input-placeholder: "#a5a8b5"
  border: "#c7cad5"
  ring: "#e0e2e8"
  border-input: "#e9eaef"

  # Inverted
  on-primary: "#ffffff"

typography:
  display-hero:
    fontFamily: "Roobert PRO Medium, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -1.68px
    fontFeature: "blwf, cv03, cv04, cv09, cv11"
  section-heading:
    fontFamily: "Roobert PRO Medium, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -1.44px
    fontFeature: "blwf, cv03, cv04, cv09, cv11"
  card-title:
    fontFamily: "Roobert PRO Medium, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.72px
  sub-heading:
    fontFamily: "Noto Sans, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: -0.44px
  feature:
    fontFamily: "Roobert PRO Medium, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0px
  body:
    fontFamily: "Noto Sans, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0px
    fontFeature: "ss01, ss04, ss05"
  body-standard:
    fontFamily: "Noto Sans, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.16px
    fontFeature: "ss01, ss04, ss05"
  button:
    fontFamily: "Roobert PRO Medium, system-ui, sans-serif"
    fontSize: 17.5px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.175px
  caption:
    fontFamily: "Roobert PRO Medium, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.71
    letterSpacing: 0px
  small:
    fontFamily: "Roobert PRO Medium, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.36px
  micro:
    fontFamily: "Roobert PRO, system-ui, sans-serif"
    fontSize: 10.5px
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: 0.5px

spacing:
  hairline: 1px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px

rounded:
  sm: 8px
  md: 12px
  lg: 20px
  xl: 24px
  2xl: 40px
  3xl: 50px
  pill: 9999px

components:
  # Buttons
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.on-primary}"
  button-outlined:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 7px 12px
  button-circle:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: 12px
    size: 44px

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  card-pastel-coral:
    backgroundColor: "{colors.coral-light}"
    textColor: "{colors.coral-dark}"
    typography: "{typography.card-title}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-pastel-teal:
    backgroundColor: "{colors.teal-light}"
    textColor: "{colors.teal-dark}"
    typography: "{typography.card-title}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-large:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.section-heading}"
    rounded: "{rounded.2xl}"
    padding: 48px

  # Input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-standard}"
    rounded: "{rounded.sm}"
    padding: 16px

  # Nav
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-standard}"
    padding: 16px 24px

  # Status badge
  badge-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
---

# Miro Design System

## Overview

Miro's website is a clean, collaborative-tool-forward platform that communicates "visual thinking" through generous whitespace, pastel accent colors, and a confident geometric font. The design uses a predominantly white canvas (`{colors.background}`) with near-black text (`{colors.ink}`) and a distinctive pastel color palette — coral, rose, teal, orange, yellow, moss — each representing different collaboration contexts.

The typography uses Roobert PRO Medium as the primary display font with OpenType character variants (`"blwf", "cv03", "cv04", "cv09", "cv11"`) and negative letter-spacing (-1.68px at 56px). Noto Sans handles body text with its own stylistic set (`"liga" 0, "ss01", "ss04", "ss05"`). The design is built with Framer, giving it smooth animations and modern component patterns.

**Key Characteristics:**
- White canvas with near-black (`{colors.ink}`) text
- Roobert PRO Medium with multiple OpenType character variants
- Pastel accent palette: coral, rose, teal, orange, yellow, moss (light + dark pairs)
- Blue 450 (`{colors.primary}`) as primary interactive color
- Success green (`{colors.success}`) for positive states
- Generous border-radius: 8px–50px range
- Framer-built with smooth motion patterns
- Ring shadow border: `{colors.ring}` `0 0 0 1px`

## Colors

### Primary
- **Near Black** (`{colors.ink}`): Primary text
- **White** (`{colors.surface}`): primary surface
- **Blue 450** (`{colors.primary}`): primary interactive
- **Actionable Pressed** (`{colors.primary-pressed}`): pressed/active blue

### Pastel Accents (Light/Dark pairs)
- **Coral**: Light `{colors.coral-light}` / Dark `{colors.coral-dark}`
- **Rose**: Light `{colors.rose-light}`
- **Teal**: Light `{colors.teal-light}` / Dark `{colors.teal-dark}`
- **Orange**: Light `{colors.orange-light}`
- **Yellow**: Dark `{colors.yellow-dark}`
- **Moss**: Dark `{colors.moss-dark}`
- **Pink** (`{colors.pink-soft}`): Soft pink surface
- **Red** (`{colors.red-light}`): Light red surface
- **Dark Red** (`{colors.red-muted}`): Muted red

### Semantic
- **Success** (`{colors.success}`): success accent

### Neutral
- **Slate** (`{colors.text-secondary}`): Secondary text
- **Input Placeholder** (`{colors.input-placeholder}`): placeholder
- **Border** (`{colors.border}`): Button borders
- **Ring** (`{colors.ring}`): Shadow-as-border
- **Input Border** (`{colors.border-input}`): Soft input outline

## Typography

### Font Families
- **Display**: `Roobert PRO Medium`, with character variants `"blwf", "cv03", "cv04", "cv09", "cv11"`
- **Display Variants**: `Roobert PRO SemiBold`, `Roobert PRO SemiBold Italic`, `Roobert PRO`
- **Body**: `Noto Sans` with stylistic sets `"liga" 0, "ss01", "ss04", "ss05"`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference each role via tokens.

| Token | Use |
|---|---|
| `display-hero` | Hero headline (56px, OpenType variants) |
| `section-heading` | Major section heads |
| `card-title` | Card titles |
| `sub-heading` | Body-led sub-section heads |
| `feature` | Feature label, weight 600 |
| `body` | Standard reading text (Noto Sans) |
| `body-standard` | Compact UI body |
| `button` | Button labels (weight 700) |
| `caption` | Metadata, secondary copy |
| `small` | Small text |
| `micro` | Uppercase micro labels |

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Built on a 1–24px base scale with section-level extension.

### Whitespace Philosophy
- Generous whitespace frames each pastel tile like a sticky note on a whiteboard.
- Section spacing breathes — `{spacing.3xl}`–`{spacing.4xl}` between major content blocks.

## Elevation & Depth

Miro's depth is minimal — shadows are barely-there or absent, and separation comes primarily from pastel surface contrast and the signature ring shadow.

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow | Default surfaces, body sections |
| Ring | `{colors.ring}` `0 0 0 1px` | Card outlines, button outlines, the signature "border-as-shadow" |
| Soft lift | Ambient drop shadow | White circle buttons, floating chrome |

## Shapes

| Token | Value | Use |
|---|---|---|
| `sm` | 8px | Buttons, inputs |
| `md` | 12px | Small cards |
| `lg` | 20px | Standard panels |
| `xl` | 24px | Pastel feature cards |
| `2xl` | 40px | Large containers |
| `3xl` | 50px | Featured/hero containers |
| `pill` | 9999px | Circle buttons, status badges |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (e.g. `{components.button-primary}`, `{components.card-pastel-coral}`).

### Buttons
- **`button-primary`** — Blue 450 CTA (`{colors.primary}`), the single saturated interactive color.
- **`button-outlined`** — Transparent fill with `{colors.border}` outline. Compact padding (`7px 12px`).
- **`button-circle`** — Pill-shaped white floating button.

### Cards
- **`card`** — Standard white panel, `{rounded.md}` corners.
- **`card-pastel-coral`** / **`card-pastel-teal`** — Pastel feature tiles using the light/dark color pair (light fill, dark text). Use only one or two pastel pairs per section.
- **`card-large`** — Large hero/feature container at `{rounded.2xl}` with section-heading typography.

### Inputs
- **`input`** — White surface, `1px solid {colors.border-input}`, `{rounded.sm}` corners, `{spacing.lg}` padding.

### Navigation
- **`nav-bar`** — White sticky header with body-standard typography.

### Badges
- **`badge-success`** — Pill-shaped success indicator using `{colors.success}`.

## Do's and Don'ts

### Do
- Use pastel light/dark pairs for feature sections (`{colors.coral-light}` + `{colors.coral-dark}`, etc.)
- Apply Roobert PRO with the documented OpenType character variants
- Use Blue 450 (`{colors.primary}`) for interactive elements

### Don't
- Don't use heavy shadows — Miro relies on ring outlines and pastel contrast
- Don't mix more than two pastel accents per section
- Don't substitute Roobert PRO without recreating the OpenType variant feel

---

## Responsive Behavior

Breakpoints (Framer-driven): 425px, 576px, 768px, 896px, 1024px, 1200px, 1280px, 1366px, 1700px, 1920px.

### Collapsing Strategy
- Hero text scales proportionally with negative tracking preserved.
- Pastel feature grids: 4-col → 2-col → stacked single column.
- Nav: horizontal links → hamburger at 768px.

---

## Agent Prompt Guide

### Quick Color Reference
- Text: Near Black (`#1c1c1e`)
- Background: White (`#ffffff`)
- Interactive: Blue 450 (`#5b76fe`)
- Success: `#00b473`
- Border: `#c7cad5`

### Example Component Prompts
- "Create hero: white background. Roobert PRO Medium 56px, line-height 1.15, letter-spacing -1.68px. Blue CTA (#5b76fe). Outlined secondary (1px solid #c7cad5, 8px radius)."

### Iteration Guide
1. Use Blue 450 only for actions — pastels carry brand mood, blue carries interactivity
2. Pair light + dark of the same pastel family for each feature tile
3. Keep depth flat — ring shadow is enough
4. Roobert PRO Medium for display, Noto Sans for body — never mix
