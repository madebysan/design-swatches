---
version: alpha
name: xAI
description: Dark-first monospace-driven brutalist minimalism — almost-black canvas with pure white text, GeistMono at extreme display sizes, uppercase tracked-out buttons, zero shadows, sharp corners.

colors:
  # Primary
  background: "#1f2228"
  surface: "#23272d"          # was rgba(255,255,255,0.03) over background — flattened
  surface-hover: "#2a2e35"    # was rgba(255,255,255,0.05) — flattened
  surface-strong: "#31353d"   # was rgba(255,255,255,0.08) — flattened

  ink: "#ffffff"
  primary: "#ffffff"          # singular text + interactive color
  on-primary: "#1f2228"

  # Text scale (opaque approximations of white-with-opacity)
  on-background: "#ffffff"
  on-surface: "#ffffff"
  text-secondary: "#bdbfc3"   # was rgba(255,255,255,0.7) over background
  text-muted: "#8e9197"       # was rgba(255,255,255,0.5)
  text-tertiary: "#8e9197"    # was rgba(255,255,255,0.5)
  text-disabled: "#5d6068"    # was rgba(255,255,255,0.3)

  # Borders (opaque approximations)
  border: "#3a3e45"           # was rgba(255,255,255,0.1)
  border-strong: "#5d6068"    # was rgba(255,255,255,0.2)

  # Focus ring
  focus-ring: "#3b82f6"       # was rgb(59,130,246) at 50% — flattened

typography:
  display-hero:
    fontFamily: "GeistMono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 320px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0px
  section-heading:
    fontFamily: "universalSans, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0px
  body:
    fontFamily: "universalSans, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "GeistMono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 1.4px
  caption:
    fontFamily: "universalSans, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  small-meta:
    fontFamily: "universalSans, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  tag-mono:
    fontFamily: "GeistMono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 1px

spacing:
  xs: 4px
  sm: 8px
  md: 24px
  lg: 48px
  xl: 96px

rounded:
  sharp: 0px
  subtle: 4px

components:
  # Buttons
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sharp}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.text-secondary}"
    textColor: "{colors.on-primary}"

  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sharp}"
    padding: 12px 24px
  button-ghost-hover:
    backgroundColor: "{colors.surface-hover}"
    textColor: "{colors.ink}"

  button-text-link:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 0px
  button-text-link-hover:
    textColor: "{colors.text-muted}"

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sharp}"
    padding: 24px
  card-hover:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.text-muted}"

  # Tag / Badge
  tag-mono:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.tag-mono}"
    rounded: "{rounded.sharp}"
    padding: 4px 8px

  # Inputs
  input:
    backgroundColor: "{colors.surface-hover}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sharp}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.surface-hover}"
    textColor: "{colors.ink}"
  input-label:
    textColor: "{colors.text-secondary}"
    typography: "{typography.caption}"
  input-placeholder:
    textColor: "{colors.text-disabled}"
    typography: "{typography.body}"

  # Surface variant
  card-strong:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.subtle}"
    padding: 24px

  # Focus indicator (referenced for accessibility)
  focus-indicator:
    backgroundColor: "{colors.background}"
    textColor: "{colors.focus-ring}"
    rounded: "{rounded.sharp}"
    padding: 0px

  # Active border state
  card-active:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sharp}"
    padding: 24px

  # Border-strong example for emphasis
  emphasized-divider:
    backgroundColor: "{colors.border-strong}"
    textColor: "{colors.ink}"
    padding: 0px

  border-quiet:
    backgroundColor: "{colors.border}"
    textColor: "{colors.ink}"
    padding: 0px

  text-tertiary-meta:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-tertiary}"
    typography: "{typography.small-meta}"
    padding: 0px
---

# xAI Design System

## Overview

xAI's website is a masterclass in dark-first, monospace-driven brutalist minimalism — a design system that feels like it was built by engineers who understand that restraint is the ultimate form of sophistication. The entire experience is anchored to an almost-black background (`{colors.background}`) with pure white text (`{colors.ink}`), creating a high-contrast, terminal-inspired aesthetic that signals deep technical credibility. There are no gradients, no decorative illustrations, no color accents competing for attention. This is a site that communicates through absence.

The typographic system is split between two carefully chosen typefaces. `GeistMono` (Vercel's monospace font) handles display-level headlines at an extraordinary 320px with weight 300, and also serves as the button typeface in uppercase with tracked-out letter-spacing (1.4px). `universalSans` handles all body and secondary heading text with a clean, geometric sans-serif voice. The monospace-as-display-font choice is the defining aesthetic decision — it positions xAI not as a consumer product but as infrastructure, as something built by people who live in terminals.

The spacing system operates on an 8px base grid with values concentrated at the small end (4px, 8px, 24px, 48px), reflecting a dense, information-focused layout philosophy. Border radius is minimal — the site barely rounds anything, maintaining sharp, architectural edges. There are no decorative shadows, no gradients, no layered elevation. Depth is communicated purely through contrast and whitespace.

**Key Characteristics:**
- Pure dark theme: `{colors.background}` background with `{colors.ink}` text — no gray middle ground
- GeistMono at extreme display sizes (320px, weight 300) — monospace as luxury
- Uppercase monospace buttons with 1.4px letter-spacing — technical, commanding
- universalSans for body text at 16px/1.5 and headings at 30px/1.2 — clean contrast
- Zero decorative elements: no shadows, no gradients, no colored accents
- 8px spacing grid with a sparse, deliberate scale
- Tailwind CSS with arbitrary values — utility-first engineering approach

## Colors

### Primary
- **Pure White** (`{colors.ink}`): The singular text color, link color, and all foreground elements. White is not a background — it is the voice.
- **Dark Background** (`{colors.background}`): The canvas. A warm near-black with a subtle blue undertone (not pure black, not neutral gray).

### Interactive
- **White Default** (`{colors.primary}`): Link and interactive element color in default state.
- **White Muted** (`{colors.text-muted}`): Hover state for links — a deliberate dimming rather than brightening, which is unusual and distinctive.
- **Border Strong** (`{colors.border-strong}`): Active borders, button outlines.
- **Focus Ring** (`{colors.focus-ring}`): Tailwind's default focus ring color, used for keyboard accessibility focus states.

### Surface & Borders
- **Surface Subtle** (`{colors.surface}`): Subtle card backgrounds — barely visible lift.
- **Surface Hover** (`{colors.surface-hover}`): Slightly more visible hover state for interactive containers.
- **Surface Strong** (`{colors.surface-strong}`): Emphasized surface for buttons, ghost-hover.
- **Border Default** (`{colors.border}`): Standard border for cards, dividers, and containers.

### Functional
- **Text Primary** (`{colors.ink}`): All headings, body text, labels.
- **Text Secondary** (`{colors.text-secondary}`): Descriptions, captions, supporting text.
- **Text Tertiary** (`{colors.text-tertiary}`): Muted labels, placeholder text, timestamps.
- **Text Disabled** (`{colors.text-disabled}`): Disabled text, very subtle annotations.

## Typography

### Font Family
- **Display / Buttons**: GeistMono with monospace fallbacks
- **Body / Headings**: universalSans

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-hero` | 320px GeistMono weight 300 — extreme scale, monospace luxury |
| `section-heading` | 30px universalSans 400 — clean sans-serif contrast |
| `body` | 16px universalSans 400 — standard reading text |
| `button-ui` | 14px GeistMono uppercase + 1.4px tracking — technical command style |
| `caption` | 14px universalSans — supporting text |
| `small-meta` | 12px — timestamps, footnotes |
| `tag-mono` | 12px GeistMono uppercase + 1px tracking |

### Principles
- **Monospace as display**: GeistMono at 320px is not a gimmick — it is the brand statement. The fixed-width characters at extreme scale create a rhythmic, architectural quality that no proportional font can achieve.
- **Light weight at scale**: Weight 300 for the 320px headline prevents the monospace from feeling heavy or brutish at extreme sizes.
- **Uppercase buttons**: All button text is uppercase GeistMono with 1.4px letter-spacing.
- **Sans-serif for reading**: universalSans at 16px/1.5 provides excellent readability for body content.
- **Two-font clarity**: monospace for impact and interaction, sans-serif for information and reading.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px. The scale is deliberately sparse — xAI avoids granular spacing distinctions, preferring large jumps that create clear visual hierarchy through whitespace alone.

### Grid & Container
- Max content width: ~1200px
- Hero: full-viewport height with massive centered monospace headline
- Feature sections: simple vertical stacking with generous section padding (48–96px)
- Two-column layouts for feature descriptions at desktop
- Full-width dark sections maintain the single dark background throughout

### Whitespace Philosophy
- **Extreme generosity**: vast amounts of whitespace. The 320px headline with 48px+ surrounding padding creates a sense of emptiness that is itself a design statement.
- **Vertical rhythm over horizontal density**: content stacks vertically with large gaps between sections.
- **No visual noise**: the absence of decorative elements means whitespace is the primary structural tool.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Page background, body content |
| Surface (Level 1) | `{colors.surface}` background | Subtle card surfaces |
| Bordered (Level 2) | `1px solid {colors.border}` | Cards, containers, dividers |
| Active (Level 3) | `1px solid {colors.border-strong}` | Hover states, active elements |
| Focus | `{colors.focus-ring}` ring | Keyboard focus indicator |

**Elevation Philosophy**: xAI rejects the conventional shadow-based elevation system entirely. There are no box-shadows anywhere. Instead, depth is communicated through:
1. opacity-based borders that brighten on interaction (creating a sense of elements "activating" rather than lifting)
2. extremely subtle background opacity shifts (3% to 8%) that create barely-perceptible surface differentiation
3. the massive scale contrast between the 320px display type and 16px body text, which creates typographic depth

This is elevation through contrast and opacity, not through simulated light and shadow.

## Shapes

| Token | Value | Use |
|---|---|---|
| `sharp` | 0px | Primary treatment for buttons, cards, inputs — the default |
| `subtle` | 4px | Occasional softening on secondary containers |

The near-zero radius philosophy is core to the brand's brutalist identity.

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — White background, dark text, GeistMono 14px uppercase, 1.4px tracking, 0px radius. Used for primary CTAs ("TRY GROK", "GET STARTED").
- **`button-ghost`** — Transparent background, white text, `1px solid {colors.border-strong}` outline, GeistMono uppercase. Used for secondary actions ("LEARN MORE", "VIEW API").
- **`button-text-link`** — Inline link, dims to `{colors.text-muted}` on hover.

### Cards & Containers
- **`card`** — Subtle surface background (3% white), `1px solid {colors.border}`, 0px radius (or 4px subtle). No shadow. Hover: border shifts to `{colors.border-strong}`.
- **`card-strong`** — Emphasized surface for buttons and prominent containers.

### Navigation
- Dark background matching page
- Brand logotype: white text, left-aligned
- Links: universalSans 14px weight 400, white text, hover dims to muted white
- CTA: white primary button, right-aligned

### Tags / Badges
- **`tag-mono`** — Transparent background, `1px solid {colors.border-strong}` border, GeistMono 12px uppercase, 1px tracking.

### Inputs
- Transparent or subtle white surface (5%) background
- `1px solid {colors.border-strong}` border
- 0px radius
- Focus: blue ring at 50% opacity
- White text 16px universalSans

## Do's and Don'ts

### Do
- Use `{colors.background}` as the universal background — never pure black `#000000`
- Use GeistMono for all display headlines and button text — monospace IS the brand
- Apply uppercase + 1.4px letter-spacing to all button labels
- Use weight 300 for the massive display headline (320px)
- Keep borders subtle — barely visible, not absent
- Dim interactive elements on hover (`{colors.text-muted}`) — the reverse of convention
- Maintain sharp corners (0px radius) as the default — brutalist precision
- Use universalSans for all body and reading text at 16px/1.5

### Don't
- Don't use box-shadows — xAI has zero shadow elevation
- Don't introduce color accents beyond white and the dark background — the monochromatic palette is sacred
- Don't use large border-radius (8px+, pill shapes) — the sharp edge is intentional
- Don't use bold weights (600–700) for headlines — weight 300–400 only
- Don't brighten elements on hover — xAI dims to muted instead
- Don't add decorative gradients, illustrations, or color blocks
- Don't use proportional fonts for buttons — GeistMono uppercase is mandatory
- Don't use colored status indicators unless absolutely necessary

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, hero headline scales dramatically down |
| Small Tablet | 640-768px | Slight increase in padding |
| Tablet | 768-1024px | Two-column layouts begin, heading sizes increase |
| Desktop | 1024-1280px | Full layout, generous whitespace |
| Large | 1280-1536px | Wider containers, more breathing room |
| Extra Large | 1536-2000px | Maximum content width, centered |
| Ultra | >2000px | Content stays centered, extreme margins |

### Touch Targets
- Buttons use 12px 24px padding for comfortable touch
- Navigation links spaced with 24px gaps
- Minimum tap target: 44px height
- Mobile: full-width buttons for easy thumb reach

### Collapsing Strategy
- Hero: 320px monospace headline scales down dramatically (to ~48px–64px on mobile)
- Navigation: horizontal links collapse to hamburger menu
- Feature sections: two-column to single-column stacking
- Section padding: 96px → 48px → 24px across breakpoints

### Image Behavior
- Minimal imagery — the site relies on typography and whitespace
- Any product screenshots maintain sharp corners
- Full-width media scales proportionally with viewport

---

## Agent Prompt Guide

### Quick Color Reference
- Background: Dark (`{colors.background}`)
- Text Primary: White (`{colors.ink}`)
- Text Secondary: White 70% (`{colors.text-secondary}`)
- Text Muted: White 50% (`{colors.text-muted}`)
- Text Disabled: White 30% (`{colors.text-disabled}`)
- Border Default: White 10% (`{colors.border}`)
- Border Strong: White 20% (`{colors.border-strong}`)
- Surface Subtle: White 3% (`{colors.surface}`)
- Surface Hover: White 8% (`{colors.surface-strong}`)
- Focus Ring: Blue (`{colors.focus-ring}`)
- Button Primary BG: White (`{colors.primary}`), text Dark (`{colors.on-primary}`)

### Example Component Prompts
- "Create a hero section on `{colors.background}`. Headline in GeistMono at 72px weight 300, color `{colors.ink}`, centered. Subtitle in universalSans 18px weight 400, `{colors.text-secondary}`, max-width 600px centered. Two buttons: primary (white bg, dark text, 0px radius, GeistMono 14px uppercase, 1.4px letter-spacing, 12px 24px padding) and ghost (transparent bg, `1px solid {colors.border-strong}`, white text, same font treatment)."
- "Design a card: `{colors.surface}` background, `1px solid {colors.border}` border, 0px radius, 24px padding. No shadow. Title in universalSans 22px weight 400, `{colors.ink}`. Body in universalSans 16px weight 400, `{colors.text-secondary}`, line-height 1.5. Hover: border changes to `{colors.border-strong}`."
- "Build navigation: `{colors.background}` background, full-width. Brand text left (GeistMono 14px uppercase). Links in universalSans 14px `{colors.ink}` with hover to `{colors.text-muted}`. White primary button right-aligned (GeistMono 14px uppercase, 1.4px letter-spacing)."
- "Create a form: dark background. Label in universalSans 14px `{colors.text-secondary}`. Input with transparent bg, `1px solid {colors.border-strong}` border, 0px radius, white text 16px universalSans. Focus: blue ring `{colors.focus-ring}`. Placeholder: `{colors.text-disabled}`."
- "Design a monospace tag/badge: transparent bg, `1px solid {colors.border-strong}`, 0px radius, GeistMono 12px uppercase, 1px letter-spacing, white text, 4px 8px padding."

### Iteration Guide
1. Always start with `{colors.background}` background — never use pure black or gray backgrounds
2. GeistMono for display and buttons, universalSans for everything else — never mix these roles
3. All buttons must be GeistMono uppercase with 1.4px letter-spacing — non-negotiable
4. No shadows, ever — depth comes from border opacity and background opacity only
5. Borders are always white with low opacity (0.1 default, 0.2 for emphasis)
6. Hover behavior dims to muted opacity rather than brightening — the reverse of most systems
7. Sharp corners (0px) by default — only use 4px for specific secondary containers
8. Body text at 16px universalSans with 1.5 line-height for comfortable reading
9. Generous section padding (48px–96px) — let content breathe in the darkness
10. The monochromatic white-on-dark palette is absolute — resist adding color unless critical for function
