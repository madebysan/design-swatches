---
version: alpha
name: Pinterest
description: Warm-toned inspiration canvas with Pinterest Red accent, Pin Sans typography, olive/sand neutrals, and generous 16-40px border radii.

colors:
  # Canvas
  background: "#ffffff"
  surface: "#ffffff"
  surface-fog: "#f6f6f3"

  # Ink
  ink: "#211922"  # plum black — warm with hint of plum
  ink-pure: "#000000"
  ink-inverted: "#ffffff"
  text-secondary: "#62625b"  # olive gray
  text-muted: "#91918c"  # warm silver

  # Brand
  primary: "#e60023"  # Pinterest Red
  on-primary: "#000000"  # black on red — Pinterest's signature contrast

  # Brand secondary
  green-700: "#103c25"
  green-700-hover: "#0b2819"

  # Interactive
  link: "#2b48d4"
  focus-ring: "#435ee5"
  performance-purple: "#6845ab"
  recommendation-purple: "#7e238b"
  facebook-blue: "#0866ff"
  pressed-blue: "#617bff"

  # Surface variants — warm tones
  sand-gray: "#e5e5e0"  # secondary button background
  warm-light: "#e0e0d9"  # circular button backgrounds
  warm-wash: "#fcfcf7"  # was hsla(60,20%,98%,0.5) — flattened over white
  border-disabled: "#c8c8c1"
  hover-gray: "#bcbcb3"
  surface-dark: "#33332e"  # dark section / footer

  # Borders
  border: "#91918c"

  # Semantic
  error: "#9e0a0a"

typography:
  display-hero:
    fontFamily: "Pin Sans, -apple-system, system-ui, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 70px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0px
  section-heading:
    fontFamily: "Pin Sans, -apple-system, system-ui, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -1.2px
  body:
    fontFamily: "Pin Sans, -apple-system, system-ui, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px
  caption-bold:
    fontFamily: "Pin Sans, -apple-system, system-ui, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0px
  caption:
    fontFamily: "Pin Sans, -apple-system, system-ui, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  caption-medium:
    fontFamily: "Pin Sans, -apple-system, system-ui, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  button:
    fontFamily: "Pin Sans, -apple-system, system-ui, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 80px
  5xl: 100px

rounded:
  none: 0px
  sm: 12px
  md: 16px
  lg: 20px
  xl: 28px
  2xl: 32px
  3xl: 40px
  pill: 9999px

components:
  # Primary red CTA — black text on red is Pinterest's signature
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 6px 14px

  # Secondary sand button
  button-secondary:
    backgroundColor: "{colors.sand-gray}"
    textColor: "{colors.ink-pure}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 6px 14px

  # Circular action button
  button-circular:
    backgroundColor: "{colors.warm-light}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: 10px

  # Ghost / transparent
  button-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-pure}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 6px 14px

  # Pin card
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 16px
  card-feature:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Email / text input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 11px 15px

  # Warm wash badge
  badge:
    backgroundColor: "{colors.warm-wash}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 10px

  # Dark footer
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.caption-medium}"
    padding: 32px
---

# Pinterest Design System

## Overview

Pinterest's website is a warm, inspiration-driven canvas that treats visual discovery like a lifestyle magazine. The design operates on a soft, slightly warm white background with Pinterest Red (`{colors.primary}`) as the singular, bold brand accent. Unlike the cool blues of most tech platforms, Pinterest's neutral scale has a distinctly warm undertone — grays lean toward olive/sand (`{colors.text-muted}`, `{colors.text-secondary}`, `{colors.sand-gray}`) rather than cool steel, creating a cozy, craft-like atmosphere that invites browsing.

The typography uses Pin Sans — a custom proprietary font with a broad fallback stack including Japanese fonts, reflecting Pinterest's global reach. At display scale (70px, weight 600), Pin Sans creates large, inviting headlines. At smaller sizes, the system is compact: buttons at 12px, captions at 12-14px. The CSS variable naming system (`--comp-*`, `--sema-*`, `--base-*`) reveals a sophisticated three-tier design token architecture: component-level, semantic-level, and base-level tokens.

What distinguishes Pinterest is its generous border-radius system (12px-40px, plus full pill for circles) and warm-tinted button backgrounds. The secondary button (`{colors.sand-gray}`) has a distinctly warm, sand-like tone rather than cold gray. The primary red button uses 16px radius — rounded but not pill-shaped. Combined with warm badge backgrounds (`{colors.warm-wash}` — a subtle yellow-warm wash) and photography-dominant layouts, the result is a design that feels handcrafted and personal, not corporate and sterile.

**Key Characteristics:**
- Warm white canvas with olive/sand-toned neutrals — cozy, not clinical
- Pinterest Red (`{colors.primary}`) as singular bold accent — never subtle, always confident
- Pin Sans custom font with global fallback stack (including CJK)
- Three-tier token architecture: `--comp-*` / `--sema-*` / `--base-*`
- Warm secondary surfaces: sand gray (`{colors.sand-gray}`), warm badge (`{colors.warm-wash}`)
- Generous border-radius: 16px standard, up to 40px for large containers
- Photography-first content — pins/images are the primary visual element
- Dark near-purple text (`{colors.ink}`) — warm, with a hint of plum

## Colors

### Primary Brand
- **Pinterest Red** (`{colors.primary}`): Primary CTA, brand accent — bold, confident red
- **Green 700** (`{colors.green-700}`): Success/nature accent
- **Green 700 Hover** (`{colors.green-700-hover}`): Pressed green

### Text
- **Plum Black** (`{colors.ink}`): Primary text — warm near-black with plum undertone
- **Black** (`{colors.ink-pure}`): Secondary text, button text on red
- **Olive Gray** (`{colors.text-secondary}`): Secondary descriptions, muted text
- **Warm Silver** (`{colors.text-muted}`): Disabled text, input borders
- **White** (`{colors.ink-inverted}`): Text on dark/colored surfaces

### Interactive
- **Focus Blue** (`{colors.focus-ring}`): Focus rings
- **Performance Purple** (`{colors.performance-purple}`): Performance features accent
- **Recommendation Purple** (`{colors.recommendation-purple}`): AI recommendation accent
- **Link Blue** (`{colors.link}`): Link text color
- **Facebook Blue** (`{colors.facebook-blue}`): Social login
- **Pressed Blue** (`{colors.pressed-blue}`): Pressed state

### Surface & Border
- **Sand Gray** (`{colors.sand-gray}`): Secondary button background — warm, craft-like
- **Warm Light** (`{colors.warm-light}`): Circular button backgrounds, badges
- **Warm Wash** (`{colors.warm-wash}`): Subtle warm badge bg
- **Fog** (`{colors.surface-fog}`): Light surface
- **Border Disabled** (`{colors.border-disabled}`): Disabled borders
- **Hover Gray** (`{colors.hover-gray}`): Hover border
- **Dark Surface** (`{colors.surface-dark}`): Dark section backgrounds

### Semantic
- **Error Red** (`{colors.error}`): Checkbox/form error states

## Typography

### Font Family
- **Primary**: `Pin Sans`, fallbacks: `-apple-system, system-ui, Segoe UI, Roboto, Helvetica Neue, Helvetica, Arial`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-hero` | Maximum impact headline (70px) |
| `section-heading` | Section titles, with negative tracking |
| `body` | Standard reading text |
| `caption-bold` | Strong metadata |
| `caption` | Small text, tags |
| `caption-medium` | Slightly emphasized small text |
| `button` | Button labels (compact at 12px) |

### Principles
- **Compact type scale**: The range is 12px-70px with a dramatic jump — most functional text is 12-16px, creating a dense, app-like information hierarchy.
- **Warm weight distribution**: 600-700 for headings, 400-500 for body. No ultra-light weights — the type always feels substantial.
- **Negative tracking on headings**: -1.2px on 28px headings creates cozy, intimate section titles.
- **Single font family**: Pin Sans handles everything — no secondary display or monospace font detected.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px with large jumps (`3xl` 48px → `4xl` 80px → `5xl` 100px) for section spacing.

### Grid & Container
- Masonry grid for pin content (signature layout)
- Centered content sections with generous max-width
- Full-width dark footer
- Search bar as primary navigation element

### Whitespace Philosophy
- **Inspiration density**: The masonry grid packs pins tightly — the content density IS the value proposition. Whitespace exists between sections, not within the grid.
- **Breathing above, density below**: Hero/feature sections get generous padding; the pin grid is compact and immersive.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Default — pins rely on content, not shadow |
| Subtle (Level 1) | Minimal shadow | Elevated overlays, dropdowns |
| Focus (Accessibility) | `2px solid {colors.focus-ring}` ring | Focus states |

**Shadow Philosophy**: Pinterest uses minimal shadows. The masonry grid relies on content (photography) to create visual interest rather than elevation effects. Depth comes from the warmth of surface colors and the generous rounding of containers.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Edge-to-edge sections |
| `sm` | 12px | Small cards, links |
| `md` | 16px | Buttons, inputs, medium cards — the workhorse |
| `lg` | 20px | Feature cards |
| `xl` | 28px | Large containers |
| `2xl` | 32px | Tab elements, large panels |
| `3xl` | 40px | Hero containers, large feature blocks |
| `pill` | 9999px | Action buttons, tab indicators |

The radius floor is 12px — Pinterest never uses sharp 4px corners. The generous rounding is core to the warm, handcrafted feel.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly.

### Buttons
- **`button-primary`** — Pinterest Red fill with **black** text (the unusual signature), 16px radius.
- **`button-secondary`** — Sand gray fill with black text, 16px radius.
- **`button-circular`** — Warm light circular surface for pin actions and nav controls.
- **`button-ghost`** — Transparent with black text for tertiary actions.

### Cards
- **`card`** — Photography-first pin card, 16px radius, no shadow.
- **`card-feature`** — Larger feature card at 20px radius for editorial moments.

### Inputs
- **`input`** — White surface with `1px solid {colors.border}`, 16px radius, 11px 15px padding.

### Badge
- **`badge`** — Warm wash background for subtle warm-tinted labels.

### Navigation & Footer
- Clean header with Pinterest logo + search bar centered. Pin Sans 16px nav links. Pinterest Red accents for active states.
- **`footer`** — Dark surface (`{colors.surface-dark}`) with multi-column layout.

## Do's and Don'ts

### Do
- Use warm neutrals (`{colors.sand-gray}`, `{colors.warm-light}`, `{colors.text-muted}`) — the warm olive/sand tone is the identity
- Apply Pinterest Red (`{colors.primary}`) only for primary CTAs — it's bold and singular
- Use Pin Sans exclusively — one font for everything
- Apply generous border-radius: `{rounded.md}` for buttons/inputs, `{rounded.lg}`+ for cards
- Keep the masonry grid dense — content density is the value
- Use warm badge backgrounds (`{colors.warm-wash}`) for subtle warm washes
- Use plum black (`{colors.ink}`) for primary text — it's warmer than pure black

### Don't
- Don't use cool gray neutrals — always warm/olive-toned
- Don't use pure black for primary text — use plum black `{colors.ink}`
- Don't use pill-shaped buttons — 16px radius is rounded but not pill
- Don't add heavy shadows — Pinterest is flat by design, depth from content
- Don't use small border-radius (<12px) on cards — the generous rounding is core
- Don't introduce additional brand colors — red + warm neutrals is the complete palette
- Don't use thin font weights — Pin Sans at 400 minimum

---

## Responsive Behavior

*(Preserved from original 9-section format — Google's parser keeps unknown sections.)*

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <576px | Single column, compact layout |
| Mobile Large | 576-768px | 2-column pin grid |
| Tablet | 768-890px | Expanded grid |
| Desktop Small | 890-1312px | Standard masonry grid |
| Desktop | 1312-1440px | Full layout |
| Large Desktop | 1440-1680px | Expanded grid columns |
| Ultra-wide | >1680px | Maximum grid density |

### Collapsing Strategy
- Pin grid: 5+ columns → 3 → 2 → 1
- Navigation: search bar + icons → simplified mobile nav
- Feature sections: side-by-side → stacked
- Hero: 70px → scales down proportionally
- Footer: dark multi-column → stacked

---

## Agent Prompt Guide

*(Preserved from original 9-section format — the copy-paste payload section.)*

### Quick Color Reference
- Brand: Pinterest Red (`{colors.primary}`)
- Background: White (`{colors.background}`)
- Text: Plum Black (`{colors.ink}`)
- Secondary text: Olive Gray (`{colors.text-secondary}`)
- Button surface: Sand Gray (`{colors.sand-gray}`)
- Border: Warm Silver (`{colors.border}`)
- Focus: Focus Blue (`{colors.focus-ring}`)

### Example Component Prompts
- "Create a hero: white background. Headline at 70px Pin Sans weight 600, plum black `{colors.ink}`. Red CTA button (`{colors.primary}`, 16px radius, 6px 14px padding). Secondary sand button (`{colors.sand-gray}`, 16px radius)."
- "Design a pin card: white background, 16px radius, no shadow. Photography fills top, 16px Pin Sans weight 400 description below in `{colors.text-secondary}`."
- "Build a circular action button: `{colors.warm-light}` background, full pill radius, `{colors.ink}` icon."
- "Create an input field: white background, 1px solid `{colors.border}`, 16px radius, 11px 15px padding. Focus: blue outline via semantic tokens."
- "Design the dark footer: `{colors.surface-dark}` background. Pinterest script logo in white. 12px Pin Sans links in `{colors.text-muted}`."

### Iteration Guide
1. Warm neutrals everywhere — olive/sand grays, never cool steel
2. Pinterest Red for CTAs only — bold and singular
3. 16px radius on buttons/inputs, 20px+ on cards — generous but not pill
4. Pin Sans is the only font — compact at 12px for UI, 70px for display
5. Photography carries the design — the UI stays warm and minimal
6. Plum black (`{colors.ink}`) for text — warmer than pure black
