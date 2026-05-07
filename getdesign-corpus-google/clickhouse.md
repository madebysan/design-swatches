---
version: alpha
name: ClickHouse
description: High-performance database aesthetic — pure black canvas with neon yellow-green (#faff69) accent, Inter at weight 900 for hero display text, charcoal-bordered cards, forest green secondary CTAs, and inset shadow active states.

colors:
  # Primary canvas + ink
  background: "#000000"
  surface: "#000000"
  surface-elevated: "#141414"    # Near Black
  surface-hover: "#3a3a3a"       # Hover Gray
  ink: "#ffffff"
  ink-inverted: "#151515"

  # Brand accent — Neon Volt
  primary: "#faff69"
  primary-dark: "#f4f692"        # Pale Yellow active state

  # Secondary action — Forest Green
  secondary: "#166534"
  secondary-dark: "#14572f"

  # Olive accents
  border-olive: "#4f5100"
  olive-dark: "#161600"

  # Text states
  on-background: "#ffffff"
  on-surface: "#ffffff"
  on-primary: "#151515"
  on-secondary: "#ffffff"
  text-secondary: "#a0a0a0"      # Silver
  text-tertiary: "#585858"       # Mid Gray

  # Borders & containment
  border: "#414141"              # Charcoal
  border-deep: "#343434"         # Deep Charcoal
  border-light: "#e5e7eb"

  # Shadow tints (opaque approximations)
  shadow-subtle: "#1a1a1a"  # was rgba(0,0,0,0.1) — flattened
  shadow-elevated: "#0d0d0d"
  shadow-inset: "#242424"

typography:
  display-mega:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 96px
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: 0px
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0px
  feature-heading:
    fontFamily: "Basier, Arial, ui-sans-serif, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0px
  sub-heading:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0px
  feature-title:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  uppercase-label:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 1.4px
  code:
    fontFamily: "Inconsolata, ui-monospace, monospace"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.50
    letterSpacing: 0px
  small:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0px
  micro:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.79
    letterSpacing: 0px

spacing:
  micro: 2px
  2xs: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px

rounded:
  none: 0px
  sm: 4px
  md: 8px
  pill: 9999px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 8px 12px

  # Neon Volt primary CTA
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-primary-hover:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
  button-primary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.primary-dark}"

  # Dark solid action
  button-dark:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-dark-hover:
    backgroundColor: "{colors.surface-hover}"
    textColor: "{colors.ink}"
  button-dark-active:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.primary-dark}"

  # Forest Green CTA
  button-green:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-green-hover:
    backgroundColor: "{colors.surface-hover}"
    textColor: "{colors.ink}"

  # Ghost / outlined
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 0px 32px
  button-ghost-hover:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"

  # Pill toggle
  button-pill:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  # Card / container
  card:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  card-neon:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px

  # Code block
  code-block:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.code}"
    rounded: "{rounded.sm}"
    padding: 16px

  # Form input
  input:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
---

# ClickHouse Design System

## Overview

ClickHouse's interface is a high-performance cockpit rendered in acid yellow-green on obsidian black — a design that screams "speed" before you read a single word. The entire experience lives in darkness: pure black backgrounds (`{colors.background}`) with dark charcoal cards creating a terminal-grade aesthetic where the only chromatic interruption is the signature neon yellow-green (`{colors.primary}`) that slashes across CTAs, borders, and highlighted moments like a highlighter pen on a dark console.

The typography is aggressively heavy — Inter at weight 900 (Black) for the hero headline at 96px creates text blocks that feel like they have physical mass. This "database for AI" site communicates raw power through visual weight: thick type, high-contrast neon accents, and performance stats displayed as oversized numbers. There's nothing subtle about ClickHouse's design, and that's entirely the point — it mirrors the product's promise of extreme speed and performance.

What makes ClickHouse distinctive is the electrifying tension between the near-black canvas and the neon yellow-green accent. This color combination (`{colors.primary}` on `{colors.background}`) creates one of the highest-contrast pairings in any tech brand, making every CTA button, every highlighted card, and every accent border impossible to miss. Supporting this is a forest green (`{colors.secondary}`) for secondary CTAs that adds depth to the action hierarchy without competing with the neon.

**Key Characteristics:**
- Pure black canvas (`{colors.background}`) with neon yellow-green (`{colors.primary}`) accent — maximum contrast
- Extra-heavy display typography: Inter at weight 900 (Black) up to 96px
- Dark charcoal card system with `{colors.border}` borders
- Forest green (`{colors.secondary}`) secondary CTA buttons
- Performance stats as oversized display numbers
- Uppercase labels with wide letter-spacing (1.4px) for navigation structure
- Active/pressed state shifts text to pale yellow (`{colors.primary-dark}`)
- All links hover to neon yellow-green — unified interactive signal
- Inset shadows on select elements creating "pressed into the surface" depth

## Colors

### Primary
- **Neon Volt** (`{colors.primary}`): The signature brand color — a vivid acid yellow-green. Used for primary CTAs, accent borders, link hovers, and highlighted moments.
- **Forest Green** (`{colors.secondary}`): Secondary CTA color — deep, saturated green for "Get Started" buttons.
- **Dark Forest** (`{colors.secondary-dark}`): A darker green variant for borders and secondary accents.

### Secondary & Accent
- **Pale Yellow** (`{colors.primary-dark}`): Active/pressed state text color — softer, muted version of Neon Volt.
- **Border Olive** (`{colors.border-olive}`): A dark olive-yellow for ghost button borders — the neon's muted sibling.
- **Olive Dark** (`{colors.olive-dark}`): The darkest neon-tinted color for subtle brand text.

### Surface & Background
- **Pure Black** (`{colors.background}`): Primary page background — absolute black for maximum contrast.
- **Near Black** (`{colors.surface-elevated}`): Button backgrounds and slightly elevated dark surfaces.
- **Charcoal** (`{colors.border}`): Primary border color — workhorse for card and container containment.
- **Deep Charcoal** (`{colors.border-deep}`): Darker border variant for subtle division lines.
- **Hover Gray** (`{colors.surface-hover}`): Button hover state background.

### Text
- **Pure White** (`{colors.ink}`): Primary text on dark surfaces.
- **Silver** (`{colors.text-secondary}`): Secondary body text and muted content.
- **Mid Gray** (`{colors.text-tertiary}`): Subtle gray overlay for depth effects.
- **Border Light** (`{colors.border-light}`): Light border variant (used in rare light contexts).

### Gradient System
None in the traditional sense. ClickHouse uses flat color blocks and high-contrast borders. The "gradient" is the contrast itself — neon yellow-green against pure black creates a visual intensity that gradients would dilute.

## Typography

### Font Families
- **Primary**: `Inter` (Next.js optimized variant)
- **Secondary Display**: `Basier`, fallbacks `Arial, Helvetica`
- **Code**: `Inconsolata`

The complete type scale lives in the `typography:` token block above.

| Token | Use |
|---|---|
| `display-mega` | 96px maximum hero — extra-heavy weight 900 |
| `display-hero` | 72px section hero |
| `feature-heading` | 36px Basier feature heading |
| `sub-heading` | 24px card heading |
| `feature-title` | 20px small feature title |
| `body-large` | 18px intro paragraph, button text |
| `body` | 16px standard body, nav, button |
| `caption` | 14px metadata, descriptions |
| `uppercase-label` | 14px uppercase with 1.4px tracking |
| `code` | 16px Inconsolata weight 600 |
| `small` | 12px small text |
| `micro` | 11.2px tag text |

### Principles
- **Weight 900 is the weapon**: Display headline uses Inter Black (900) at 96px — physical, almost architectural presence.
- **Full weight spectrum**: System uses 400, 500, 600, 700, and 900. Weight IS hierarchy.
- **Uppercase with maximum tracking**: Section overlines use 1.4px letter-spacing — wider than most systems.
- **Dual sans-serif**: Inter handles display and body; Basier handles feature section headings at 600 weight.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

### Grid & Container
- Max container width: up to 2200px (extra-wide) with responsive scaling
- Hero: full-width dark with massive typography
- Feature sections: multi-column card grids with dark borders
- Stats: horizontal metric bar
- Full-dark page — no light sections

### Whitespace Philosophy
- **Dark void as canvas**: Pure black background provides infinite depth.
- **Dense information**: Feature cards and stats packed with data, reflecting the database product's performance focus.
- **Neon highlights as wayfinding**: Yellow-green accents guide the eye like runway lights.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Black background, text blocks |
| Bordered (Level 1) | 1px solid `{colors.border}` | Standard cards, containers |
| Subtle (Level 2) | Subtle drop shadow at `{colors.shadow-subtle}` | Subtle card lift |
| Elevated (Level 3) | Larger drop shadow | Feature cards, hover states |
| Pressed/Inset (Level 4) | Inset shadow at `{colors.shadow-inset}` | Active/pressed elements — "sunk into the surface" |
| Neon Highlight (Level 5) | Neon Volt border `{colors.primary}` | Featured/selected cards |

**Shadow Philosophy**: ClickHouse uses shadows on a black canvas, where they're barely visible — they exist more for subtle dimensionality than obvious elevation. The most distinctive depth mechanism is the **inset shadow** (Level 4), creating a "pressed into the surface" effect unique to ClickHouse. The neon border highlight is the primary attention-getting depth mechanism.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Sharp inline elements |
| `sm` | 4px | Buttons, badges, small elements, code blocks |
| `md` | 8px | Cards, containers, dividers |
| `pill` | 9999px | Toggle buttons, status indicators |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Neon Volt fill, near-black text, 4px radius. The eye-catching CTA.
- **`button-dark`** — Near-black fill, white text. Standard action.
- **`button-green`** — Forest Green fill — "Get Started" / primary conversion.
- **`button-ghost`** — Transparent with olive-tinted border. Secondary actions.
- **`button-pill`** — `{rounded.pill}` for toggle/switch elements.

### Cards & Containers
- **`card`** — Transparent or near-black, charcoal border, 4–8px radius.
- **`card-neon`** — Standard dark card with neon yellow-green border highlight for "selected" or "featured" treatment.

### Code Blocks
- **`code-block`** — Dark surface with Inconsolata at weight 600. Terminal-like aesthetic.

### Inputs
- **`input`** — Near-black bg, white text, 4px radius.

### Navigation
- Dark nav on black, ClickHouse wordmark + icon in yellow/neon. Links hover to Neon Volt. CTA: Neon Volt or Forest Green.

### Distinctive Components

**Performance Stats**: Oversized numbers (72px+, weight 700–900), brief descriptions beneath, high-contrast neon accents. The primary visual proof of performance claims.

**Trust Bar**: Company logos on dark, monochrome/white logo treatment.

## Do's and Don'ts

### Do
- Use Neon Volt (`{colors.primary}`) as the sole chromatic accent — must pop against pure black
- Use Inter at weight 900 for hero display text — extreme weight IS the personality
- Keep everything on pure black (`{colors.background}`) — never use dark gray as page background
- Use charcoal borders (`{colors.border}`) for all card containment
- Apply Forest Green (`{colors.secondary}`) for primary CTA buttons
- Show performance stats as oversized display numbers
- Use uppercase with wide letter-spacing (1.4px) for section labels
- Apply Pale Yellow (`{colors.primary-dark}`) for active/pressed text states
- Link hovers should ALWAYS shift to Neon Volt

### Don't
- Don't introduce additional colors — strictly black, neon, green, and gray
- Don't use the neon as a background fill — accent and border color only (except CTAs)
- Don't reduce display weight below 700 — heavy weight is core to personality
- Don't use light/white backgrounds anywhere
- Don't round corners beyond 8px — sharp geometry reflects database precision
- Don't use soft/diffused shadows on black — they're invisible. Use border-based depth
- Don't skip the inset shadow on active states
- Don't use warm neutrals — all grays are perfectly neutral

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <640px | Single column, stacked cards |
| Small Tablet | 640–768px | Minor adjustments |
| Tablet | 768–1024px | 2-column grids |
| Desktop | 1024–1280px | Standard layout |
| Large Desktop | 1280–1536px | Expanded content |
| Ultra-wide | 1536–2200px | Maximum container width |

### Touch Targets
- Buttons with 12px 16px padding minimum
- Card surfaces as touch targets
- Adequate nav link spacing

### Collapsing Strategy
- **Hero text**: 96px → 72px → 48px → 36px
- **Feature grids**: multi-column → 2 → 1 column
- **Stats**: horizontal → stacked
- **Navigation**: full → hamburger

### Image Behavior
- Product screenshots maintain aspect ratio
- Code blocks use horizontal scroll on narrow screens
- All images on dark backgrounds

---

## Agent Prompt Guide

### Quick Color Reference
- Brand Accent: Neon Volt `{colors.primary}`
- Page Background: Pure Black `{colors.background}`
- CTA Green: Forest Green `{colors.secondary}`
- Card Border: Charcoal `{colors.border}`
- Primary Text: Pure White `{colors.ink}`
- Secondary Text: Silver `{colors.text-secondary}`
- Active State: Pale Yellow `{colors.primary-dark}`
- Button Surface: Near Black `{colors.surface-elevated}`

### Example Component Prompts
- "Create a hero section on Pure Black (`{colors.background}`) with a massive headline at 96px Inter weight 900, line-height 1.0. Pure White text. Add a Neon Volt (`{colors.primary}`) CTA button (dark text, 4px radius, 0px 16px padding) and a ghost button (transparent, 1px solid `{colors.border-olive}` border)."
- "Design a feature card on black with 1px solid `{colors.border}` border and 8px radius. Title at 24px Inter weight 700, body at 16px in Silver (`{colors.text-secondary}`). Add a neon-highlighted variant with 1px solid `{colors.primary}` border."
- "Build a performance stats bar: large numbers at 72px Inter weight 700 in Pure White. Brief descriptions at 14px in Silver. On black background."
- "Create a Forest Green (`{colors.secondary}`) CTA button: white text, 12px 16px padding, 4px radius, 1px solid `{colors.surface-elevated}` border. Hover: bg shifts to `{colors.surface-hover}`, text to 80% opacity."
- "Design an uppercase section label: 14px Inter weight 600, letter-spacing 1.4px, uppercase. Silver (`{colors.text-secondary}`) text on black."

### Iteration Guide
1. Keep everything on pure black — no dark gray alternatives
2. Neon Volt (`{colors.primary}`) for accents and CTAs only — never large backgrounds
3. Weight 900 for hero, 700 for headings, 600 for labels, 400-500 for body
4. Active states use Pale Yellow (`{colors.primary-dark}`) — not just opacity
5. All links hover to Neon Volt — consistent interactive feedback
6. Charcoal borders are the primary depth mechanism
