---
version: alpha
name: ElevenLabs
description: Restrained elegance for premium voice AI. Near-white canvas with warm undertones, Waldenburg weight 300 ethereal headlines, multi-layered sub-0.1 opacity shadow stacks, warm-stone pill CTAs.

colors:
  # Primary surfaces
  background: "#ffffff"
  surface: "#f5f5f5"
  surface-warm: "#f5f2ef"
  surface-alt: "#f6f6f6"
  ink: "#000000"
  ink-inverted: "#ffffff"

  # Brand accent (kept achromatic — black is the primary action color)
  primary: "#000000"
  on-primary: "#ffffff"

  # Neutral text
  text-secondary: "#4e4e4e"
  text-muted: "#777169"

  # Borders
  border: "#e5e5e5"
  border-subtle: "#f2f2f2"  # opaque approx of rgba(0,0,0,0.05) over white — Google format requires hex

  # Focus
  focus-ring: "#93c5fd"      # opaque approx of rgb(147 197 253 / 0.5)

  # Decorative grid (rarely seen)
  grid-cyan: "#dffefe"       # opaque approx of #7fffff at 25% over white

  # Shadow stand-ins (opaque approximations)
  shadow-soft: "#f0f0f0"     # was rgba(0,0,0,0.04) — Google format requires hex
  shadow-edge: "#e6e6e6"     # was rgba(0,0,0,0.06)
  shadow-warm: "#f5efe9"     # was rgba(78,50,23,0.04) — warm-tinted shadow

typography:
  display-hero:
    fontFamily: "Waldenburg, Waldenburg Fallback, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.96px
  section-heading:
    fontFamily: "Waldenburg, Waldenburg Fallback, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.17
    letterSpacing: 0px
  card-heading:
    fontFamily: "Waldenburg, Waldenburg Fallback, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.13
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0px
  body:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0.18px
  body-standard:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0.16px
  body-medium:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0.16px
  nav-ui:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.15px
  button:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.47
    letterSpacing: 0px
  button-uppercase:
    fontFamily: "WaldenburgFH, WaldenburgFH Fallback, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: 0.7px
  caption:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0.14px
  small:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0px
  code:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.85
    letterSpacing: 0px
  micro:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0px
  tiny:
    fontFamily: "Inter, Inter Fallback, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0px

spacing:
  micro: 1px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 40px
  5xl: 64px
  6xl: 96px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
  2xl: 20px
  3xl: 24px
  warm: 30px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 0px 14px
  button-primary-hover:
    backgroundColor: "{colors.text-secondary}"

  button-white:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  button-warm:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.warm}"
    padding: 12px 20px

  button-uppercase:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.button-uppercase}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.xl}"
    padding: 24px

  card-large:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.3xl}"
    padding: 32px

  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-standard}"
    rounded: "{rounded.md}"
    padding: 12px 20px
  input-focus:
    backgroundColor: "{colors.background}"

  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-ui}"
    padding: 16px 24px

  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-ui}"
    padding: 8px 12px

  badge:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.small}"
    rounded: "{rounded.sm}"
    padding: 4px 10px
---

# ElevenLabs Design System

## Overview

ElevenLabs' website is a study in restrained elegance — a near-white canvas (`{colors.background}`, `{colors.surface}`) where typography and subtle shadows do all the heavy lifting. The design feels like a premium audio product brochure: clean, spacious, and confident enough to let the content speak (literally, given ElevenLabs makes voice AI). There's an almost Apple-like quality to the whitespace strategy, but warmer — the occasional warm stone tint (`{colors.surface-warm}`, `{colors.text-muted}`) prevents the purity from feeling clinical.

The typography system is built on a fascinating duality: Waldenburg at weight 300 (light) for display headings creates ethereal, whisper-thin titles that feel like sound waves rendered in type — delicate, precise, and surprisingly impactful at large sizes. This light-weight display approach is the design's signature — where most sites use bold headings to grab attention, ElevenLabs uses lightness to create intrigue. Inter handles all body and UI text with workmanlike reliability, using slight positive letter-spacing (0.14px–0.18px) that gives body text an airy, well-spaced quality. WaldenburgFH appears as a bold uppercase variant for specific button labels.

What makes ElevenLabs distinctive is its multi-layered shadow system. Rather than simple box-shadows, elements use complex stacks: inset border-shadows, outline shadows, and soft elevation shadows — all at remarkably low opacities. The result is a design where surfaces seem to barely exist, floating just above the page with the lightest possible touch. Pill-shaped buttons with warm-tinted backgrounds (`{colors.surface-warm}`) and warm shadows (`{colors.shadow-warm}`) add a tactile, physical quality.

**Key Characteristics:**
- Near-white canvas with warm undertones (`{colors.surface}`, `{colors.surface-warm}`)
- Waldenburg weight 300 (light) for display — ethereal, whisper-thin headings
- Inter with positive letter-spacing (0.14–0.18px) for body — airy readability
- Multi-layered shadow stacks at sub-0.1 opacity — surfaces barely exist
- Pill buttons with warm stone-tinted backgrounds
- WaldenburgFH bold uppercase for specific CTA labels
- Warm shadow tints (`{colors.shadow-warm}`) — shadows have color, not just darkness
- Geist Mono for code snippets, set with relaxed 1.85 line-height

## Colors

### Primary
- **Pure White** (`{colors.background}`): Primary background, card surfaces, button backgrounds
- **Light Gray** (`{colors.surface}`): Secondary surface, subtle section differentiation
- **Warm Stone** (`{colors.surface-warm}`): Featured CTA background — the warm signature
- **Black** (`{colors.ink}`): Primary text, headings, dark buttons

### Neutral Scale
- **Dark Gray** (`{colors.text-secondary}`): Secondary text, descriptions
- **Warm Gray** (`{colors.text-muted}`): Tertiary text, muted links, decorative underlines
- **Near White** (`{colors.surface-alt}`): Alternate light surface

### Interactive
- **Grid Cyan** (`{colors.grid-cyan}`): Decorative grid overlay (used at low opacity in source)
- **Ring Blue** (`{colors.focus-ring}`): Focus ring color
- **Border Light** (`{colors.border}`): Explicit borders
- **Border Subtle** (`{colors.border-subtle}`): Ultra-subtle bottom borders

### Shadow Stand-Ins
- **Soft Elevation** (`{colors.shadow-soft}`): Gentle drop-shadow approximation
- **Edge Shadow** (`{colors.shadow-edge}`): Subtle edge definition
- **Warm Shadow** (`{colors.shadow-warm}`): Warm-tinted shadow color for featured CTAs

## Typography

### Font Families
- **Display**: `Waldenburg`, fallback: `Waldenburg Fallback`
- **Display Bold**: `WaldenburgFH`, fallback: `WaldenburgFH Fallback`
- **Body / UI**: `Inter`, fallback: `Inter Fallback`
- **Monospace**: `Geist Mono` or `ui-monospace`

### Hierarchy

| Token | Use |
|---|---|
| `display-hero` | Whisper-thin hero — Waldenburg 48px weight 300, -0.96px tracking |
| `section-heading` | Waldenburg 36px weight 300 |
| `card-heading` | Waldenburg 32px weight 300 |
| `body-large` | Inter 20px weight 400 — introductions |
| `body` | Inter 18px weight 400 with +0.18px tracking — standard reading |
| `body-standard` | Inter 16px weight 400 — UI text |
| `body-medium` | Inter 16px weight 500 — emphasized body |
| `nav-ui` | Inter 15px weight 500 — navigation |
| `button` | Inter 15px weight 500 — button labels |
| `button-uppercase` | WaldenburgFH 14px weight 700 — CTA labels |
| `caption` | Inter 14px weight 400 — metadata |
| `small` | Inter 13px weight 500 — tags, badges |
| `code` | Geist Mono 13px, line-height 1.85 |
| `micro` | Inter 12px — tiny labels |
| `tiny` | Inter 10px — fine print |

### Principles
- **Light as the hero weight**: Waldenburg at 300 is the defining typographic choice. Where other design systems use bold for impact, ElevenLabs uses lightness — thin strokes that feel like audio waveforms, creating intrigue through restraint.
- **Positive letter-spacing on body**: Inter uses +0.14px to +0.18px tracking across body text, creating an airy, well-spaced reading rhythm that contrasts with the tight display tracking (-0.96px).
- **WaldenburgFH for emphasis**: A bold (700) uppercase variant of Waldenburg appears only in specific CTA button labels with 0.7px letter-spacing — the one place where the type system gets loud.
- **Monospace as ambient**: Geist Mono at relaxed line-height (1.85) for code blocks feels unhurried and readable.

## Layout

### Spacing System
Base unit is **8px**. Scale lives in YAML — `xs` through `6xl` (4–96px). The system is generous in section spacing and tight in component-internal rhythm.

### Grid & Container
- Centered content with generous max-width
- Single-column hero, expanding to feature grids
- Full-width gradient sections for product showcases
- White card grids on light gray backgrounds

### Whitespace Philosophy
- **Apple-like generosity**: Massive vertical spacing between sections creates a premium, unhurried pace. Each section is an exhibit.
- **Warm emptiness**: The whitespace isn't cold — the warm stone undertones and warm shadows give empty space a tactile, physical quality.
- **Typography-led rhythm**: The light-weight Waldenburg headings create visual "whispers" that draw the eye through vast white space.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Page background, text blocks |
| Inset Edge (Level 0.5) | Inset half-pixel border | Internal border definition |
| Outline Ring (Level 1) | Multi-layer soft shadow | Shadow-as-border for cards |
| Card (Level 2) | 1px ring + soft 4px drop | Button elevation, prominent cards |
| Warm Lift (Level 3) | Warm-tinted 6px/16px drop using `{colors.shadow-warm}` | Featured CTAs |
| Focus | Blue ring via `{colors.focus-ring}` | Keyboard focus |

**Shadow Philosophy**: ElevenLabs uses the most refined shadow system of any design system analyzed. Every shadow is at sub-0.1 opacity, many include both outward cast AND inward inset components, and the warm CTA shadows use an actual warm color rather than neutral black. The inset half-pixel borders create edges so subtle they're felt rather than seen — surfaces define themselves through the lightest possible touch.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved — almost never used |
| `xs` | 2px | Small links, inline elements |
| `sm` | 4px | Nav items, tab panels, tags |
| `md` | 8px | Small containers |
| `lg` | 12px | Medium cards, dropdowns |
| `xl` | 16px | Standard cards, articles |
| `2xl` | 20px | Featured cards, code panels |
| `3xl` | 24px | Large panels, section containers |
| `warm` | 30px | Warm stone CTA radius |
| `pill` | 9999px | Primary buttons, navigation pills |

## Components

The complete component spec lives in YAML. Reference component tokens directly.

### Buttons
- **`button-primary`** — Black pill on white. Primary CTA.
- **`button-white`** — White pill (designed for shadow-bordered look on white).
- **`button-warm`** — Warm stone pill using `{colors.surface-warm}` — the signature.
- **`button-uppercase`** — Bold WaldenburgFH uppercase label, 14px weight 700.

### Cards
- **`card`** — 24px padding, `{rounded.xl}` (16px) radius — standard cards.
- **`card-large`** — 32px padding, `{rounded.3xl}` (24px) radius — featured panels.

### Inputs
- **`input`** — White surface with subtle border, `{rounded.md}` radius, generous 12/20 padding.

### Navigation
- **`nav-bar`** — Sticky white header with `{typography.nav-ui}` links.
- **`nav-link`** — Black text, generous touch padding.

### Badges
- **`badge`** — Light gray surface with small (4px) radius — small labels and tags.

## Do's and Don'ts

### Do
- Use Waldenburg weight 300 for all display headings — the lightness IS the brand
- Apply multi-layer shadows (inset + outline + elevation) at sub-0.1 opacity
- Use warm stone tints (`{colors.surface-warm}`) for featured elements
- Apply positive letter-spacing (+0.14 to +0.18px) on Inter body text
- Use `{rounded.pill}` for primary buttons — pill shape is standard
- Use warm-tinted shadows (`{colors.shadow-warm}`) on featured CTAs
- Keep the page predominantly white with subtle gray section differentiation
- Use WaldenburgFH bold uppercase ONLY for specific CTA button labels

### Don't
- Don't use bold (700) Waldenburg for headings — weight 300 is non-negotiable
- Don't use heavy shadows (>0.1 opacity) — the ethereal quality requires whisper-level depth
- Don't use cool gray borders — the system is warm-tinted throughout
- Don't skip the inset shadow component — half-pixel inset borders define edges
- Don't apply negative letter-spacing to body text — Inter uses positive tracking
- Don't use sharp corners (<8px) on cards — the generous radius is structural
- Don't introduce brand colors — the palette is intentionally achromatic with warm undertones
- Don't make buttons opaque and heavy — the warm translucent stone treatment is the signature

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <1024px | Single column, hamburger nav, stacked sections |
| Desktop | >1024px | Full layout, horizontal nav, multi-column grids |

### Touch Targets
- Pill buttons with generous padding (12px–20px)
- Navigation links at 15px with adequate spacing
- Select dropdowns maintain comfortable sizing

### Collapsing Strategy
- Navigation: horizontal → hamburger at 1024px
- Feature grids: multi-column → stacked
- Hero: maintains centered layout, font scales proportionally
- Gradient sections: full-width maintained, content stacks
- Spacing compresses proportionally

### Image Behavior
- Product screenshots scale responsively
- Gradient backgrounds simplify on mobile
- Audio waveform previews maintain aspect ratio
- Rounded corners maintained across breakpoints

---

## Agent Prompt Guide

### Quick Color Reference
- Background: Pure White (`{colors.background}`) or Light Gray (`{colors.surface}`)
- Text: Black (`{colors.ink}`)
- Secondary text: Dark Gray (`{colors.text-secondary}`)
- Muted text: Warm Gray (`{colors.text-muted}`)
- Warm surface: Warm Stone (`{colors.surface-warm}`)
- Border: `{colors.border}` or `{colors.border-subtle}`

### Example Component Prompts
- "Create a hero on white background. Headline at 48px Waldenburg weight 300, line-height 1.08, letter-spacing -0.96px, black text. Subtitle at 18px Inter weight 400, line-height 1.50+, letter-spacing 0.18px, `{colors.text-secondary}` text. Two pill buttons: black (`{rounded.pill}`, 0px 14px padding) and warm stone (`{colors.surface-warm}`, `{rounded.warm}` radius, 12px 20px padding, warm shadow `{colors.shadow-warm}`)."
- "Design a card: white background, 20px radius. Multi-layer shadow stack. Title at 32px Waldenburg weight 300, body at 16px Inter weight 400 letter-spacing 0.16px, `{colors.text-secondary}`."
- "Build a white pill button: white bg, `{rounded.pill}` radius. Soft shadow stack. Text at 15px Inter weight 500."
- "Create an uppercase CTA label: 14px WaldenburgFH weight 700, text-transform uppercase, letter-spacing 0.7px."
- "Design navigation: white sticky header. Inter 15px weight 500. Black pill CTA right-aligned. Border-bottom: `{colors.border-subtle}`."

### Iteration Guide
1. Start with white — the warm undertone comes from shadows and stone surfaces, not backgrounds
2. Waldenburg 300 for headings — never bold, the lightness is the identity
3. Multi-layer shadows: always include inset + outline + elevation at sub-0.1 opacity
4. Positive letter-spacing on Inter body (+0.14px to +0.18px) — the airy reading quality
5. Warm stone CTA is the signature — `{colors.surface-warm}` with warm-tinted shadow
6. Pill (`{rounded.pill}`) for buttons, generous radius (16–24px) for cards
