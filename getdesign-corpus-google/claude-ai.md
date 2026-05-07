---
version: alpha
name: Claude (Anthropic)
description: Warm, literary parchment design — custom Anthropic Serif headlines on a warm off-white canvas, terracotta brand accent, exclusively warm-toned neutrals, ring-based shadow system, and editorial pacing.

colors:
  # Primary canvas + ink
  background: "#f5f4ed"          # Parchment
  surface: "#faf9f5"             # Ivory
  surface-white: "#ffffff"
  surface-warm: "#e8e6dc"        # Warm Sand
  surface-dark: "#30302e"        # Dark Surface
  ink: "#141413"                 # Anthropic Near Black
  ink-inverted: "#faf9f5"

  # Brand accent
  primary: "#c96442"             # Terracotta Brand
  primary-light: "#d97757"       # Coral Accent

  # Text states
  on-background: "#141413"
  on-surface: "#141413"
  on-primary: "#faf9f5"
  text-charcoal: "#4d4c48"
  text-olive: "#5e5d59"
  text-stone: "#87867f"
  text-dark-warm: "#3d3d3a"
  text-warm-silver: "#b0aea5"

  # Borders
  border: "#f0eee6"              # Border Cream
  border-warm: "#e8e6dc"
  border-dark: "#30302e"

  # Ring shadow colors
  ring-warm: "#d1cfc5"
  ring-subtle: "#dedc01"
  ring-deep: "#c2c0b6"

  # Semantic
  error: "#b53333"               # Error Crimson
  focus: "#3898ec"               # Focus Blue — only cool color in the system

  # Whisper shadow (opaque approx of rgba(0,0,0,0.05))
  shadow-whisper: "#f2f0e8"  # was rgba(0,0,0,0.05) flattened over Parchment — Google format requires hex

typography:
  display-hero:
    fontFamily: "Anthropic Serif, Georgia, ui-serif, serif"
    fontSize: 64px
    fontWeight: 500
    lineHeight: 1.10
    letterSpacing: 0px
  section-heading:
    fontFamily: "Anthropic Serif, Georgia, ui-serif, serif"
    fontSize: 52px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0px
  sub-heading-large:
    fontFamily: "Anthropic Serif, Georgia, ui-serif, serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0px
  sub-heading:
    fontFamily: "Anthropic Serif, Georgia, ui-serif, serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.10
    letterSpacing: 0px
  sub-heading-small:
    fontFamily: "Anthropic Serif, Georgia, ui-serif, serif"
    fontSize: 25px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0px
  feature-title:
    fontFamily: "Anthropic Serif, Georgia, ui-serif, serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0px
  body-serif:
    fontFamily: "Anthropic Serif, Georgia, ui-serif, serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0px
  body-large:
    fontFamily: "Anthropic Sans, Arial, ui-sans-serif, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0px
  body-nav:
    fontFamily: "Anthropic Sans, Arial, ui-sans-serif, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  body:
    fontFamily: "Anthropic Sans, Arial, ui-sans-serif, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  body-small:
    fontFamily: "Anthropic Sans, Arial, ui-sans-serif, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  caption:
    fontFamily: "Anthropic Sans, Arial, ui-sans-serif, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  label:
    fontFamily: "Anthropic Sans, Arial, ui-sans-serif, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.12px
  overline:
    fontFamily: "Anthropic Sans, Arial, ui-sans-serif, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0.5px
  code:
    fontFamily: "Anthropic Mono, ui-monospace, monospace"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: -0.32px

spacing:
  micro: 3px
  2xs: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 80px
  4xl: 120px

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  2xl: 24px
  3xl: 32px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-nav}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-nav}"
    padding: 8px 12px

  # Brand Terracotta — primary CTA
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 9px 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.on-primary}"

  # Warm Sand secondary
  button-warm:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.text-charcoal}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px 12px

  # White surface button
  button-white:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 8px 16px

  # Dark charcoal
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px 12px

  # Dark primary (on dark theme)
  button-dark-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.text-warm-silver}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 10px 17px

  # Standard card
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  card-featured:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 32px
  card-hero:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.3xl}"
    padding: 32px

  # Dark card
  card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink-inverted}"
    rounded: "{rounded.md}"
    padding: 24px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 2px 12px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
---

# Claude (Anthropic) Design System

## Overview

Claude's interface is a literary salon reimagined as a product page — warm, unhurried, and quietly intellectual. The entire experience is built on a parchment-toned canvas (`{colors.background}`) that deliberately evokes the feeling of high-quality paper rather than a digital surface. Where most AI product pages lean into cold, futuristic aesthetics, Claude's design radiates human warmth, as if the AI itself has good taste in interior design.

The signature move is the custom Anthropic Serif typeface — a medium-weight serif with generous proportions that gives every headline the gravitas of a book title. Combined with organic, hand-drawn-feeling illustrations in terracotta (`{colors.primary}`), black, and muted green, the visual language says "thoughtful companion" rather than "powerful tool." The serif headlines breathe at tight-but-comfortable line-heights (1.10–1.30), creating a cadence that feels more like reading an essay than scanning a product page.

What makes Claude's design truly distinctive is its warm neutral palette. Every gray has a yellow-brown undertone (`{colors.text-olive}`, `{colors.text-stone}`, `{colors.text-charcoal}`) — there are no cool blue-grays anywhere. Borders are cream-tinted (`{colors.border}`, `{colors.border-warm}`), shadows use warm transparent blacks, and even the darkest surfaces (`{colors.ink}`, `{colors.surface-dark}`) carry a barely perceptible olive warmth. This chromatic consistency creates a space that feels lived-in and trustworthy.

**Key Characteristics:**
- Warm parchment canvas (`{colors.background}`) evoking premium paper, not screens
- Custom Anthropic type family: Serif for headlines, Sans for UI, Mono for code
- Terracotta brand accent (`{colors.primary}`) — warm, earthy, deliberately un-tech
- Exclusively warm-toned neutrals — every gray has a yellow-brown undertone
- Organic, editorial illustrations replacing typical tech iconography
- Ring-based shadow system creating border-like depth without visible borders
- Magazine-like pacing with generous section spacing and serif-driven hierarchy

## Colors

### Primary
- **Anthropic Near Black** (`{colors.ink}`): Primary text and dark-theme surface — warm, almost olive-tinted. The warmest "black" in any major tech brand.
- **Terracotta Brand** (`{colors.primary}`): The core brand color — burnt orange-brown for primary CTAs and brand moments. Deliberately earthy and un-tech.
- **Coral Accent** (`{colors.primary-light}`): Lighter, warmer variant for text accents, links on dark surfaces, and secondary emphasis.

### Secondary & Accent
- **Error Crimson** (`{colors.error}`): Deep, warm red for error states.
- **Focus Blue** (`{colors.focus}`): Standard blue for input focus rings — the only cool color in the entire system.

### Surface & Background
- **Parchment** (`{colors.background}`): Primary page background — warm cream with yellow-green tint.
- **Ivory** (`{colors.surface}`): Lightest surface — cards and elevated containers on Parchment.
- **Pure White** (`{colors.surface-white}`): Specific button surfaces and maximum-contrast elements.
- **Warm Sand** (`{colors.surface-warm}`): Button backgrounds — noticeably warm light gray.
- **Dark Surface** (`{colors.surface-dark}`): Dark-theme containers and elevated dark elements.
- **Deep Dark** (`{colors.ink}`): Dark-theme page background.

### Text
- **Charcoal Warm** (`{colors.text-charcoal}`): Button text on light warm surfaces.
- **Olive Gray** (`{colors.text-olive}`): Secondary body text — distinctly warm medium-dark gray.
- **Stone Gray** (`{colors.text-stone}`): Tertiary text and footnotes.
- **Dark Warm** (`{colors.text-dark-warm}`): Dark text links and emphasized secondary text.
- **Warm Silver** (`{colors.text-warm-silver}`): Text on dark surfaces.

### Borders & Rings
- **Border Cream** (`{colors.border}`): Standard light-theme border — barely visible warm cream.
- **Border Warm** (`{colors.border-warm}`): Prominent borders, section dividers.
- **Border Dark** (`{colors.border-dark}`): Standard border on dark surfaces.
- **Ring Warm** (`{colors.ring-warm}`): Shadow ring color for button hover/focus states.
- **Ring Subtle** (`{colors.ring-subtle}`): Secondary ring variant.
- **Ring Deep** (`{colors.ring-deep}`): Deeper ring for active/pressed states.

### Gradient System
Claude's design is **gradient-free** in the traditional sense. Depth and visual richness come from the interplay of warm surface tones, organic illustrations, and light/dark section alternation. The warm palette itself creates a "gradient" effect as the eye moves through cream → sand → stone → charcoal → black sections.

## Typography

### Font Families
- **Headline**: `Anthropic Serif`, with fallback `Georgia`
- **Body / UI**: `Anthropic Sans`, with fallback `Arial`
- **Code**: `Anthropic Mono`

*Note: These are custom typefaces. For external implementations, Georgia serves as the serif substitute and system-ui/Inter as the sans substitute.*

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-hero` | 64px hero with book-title presence |
| `section-heading` | 52px feature section anchor |
| `sub-heading-large` | 36px secondary section markers |
| `sub-heading` | 32px card titles, feature names |
| `sub-heading-small` | 25px smaller section titles |
| `feature-title` | 20px small feature heading |
| `body-serif` | 17px serif body for editorial passages |
| `body-large` | 20px intro paragraph |
| `body-nav` | 17px navigation links and UI |
| `body` | 16px standard body and button text |
| `body-small` | 15px compact body |
| `caption` | 14px metadata |
| `label` | 12px small labels with 0.12px tracking |
| `overline` | 10px uppercase overline labels |
| `code` | 15px Anthropic Mono |

### Principles
- **Serif for authority, sans for utility**: Anthropic Serif carries all headlines at weight 500. Anthropic Sans handles all functional UI text.
- **Single weight for serifs**: All Anthropic Serif headings use weight 500 — no bold, no light. Same author wrote every heading.
- **Relaxed body line-height**: Most body text uses generous line-height — significantly more than typical tech sites. Reading experience closer to a book than a dashboard.
- **Tight-but-not-compressed headings**: Line-heights of 1.10–1.30 for headings are tight but never claustrophobic.
- **Micro letter-spacing on labels**: Small sans text uses deliberate letter-spacing (0.12px–0.5px) for readability.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px. Section vertical spacing is generous (`{spacing.3xl}`–`{spacing.4xl}` between majors).

### Grid & Container
- Max container width: ~1200px, centered
- Hero: centered with editorial layout
- Feature sections: single-column or 2–3 column card grids
- Model comparison: clean 3-column grid
- Full-width dark sections breaking the container for emphasis

### Whitespace Philosophy
- **Editorial pacing**: Each section breathes like a magazine spread.
- **Serif-driven rhythm**: Serif headings establish a literary cadence demanding more whitespace.
- **Content island approach**: Sections alternate between light and dark, creating distinct "rooms".

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Parchment background, inline text |
| Contained (Level 1) | 1px solid `{colors.border}` light or `{colors.border-dark}` | Standard cards, sections |
| Ring (Level 2) | `0px 0px 0px 1px` ring with `{colors.ring-warm}` | Interactive cards, buttons, hover states |
| Whisper (Level 3) | Soft drop shadow with `{colors.shadow-whisper}` tint | Elevated feature cards, product screenshots |
| Inset (Level 4) | Inset 1px ring at low opacity | Active/pressed button states |

**Shadow Philosophy**: Claude communicates depth through **warm-toned ring shadows** rather than traditional drop shadows. The signature `0px 0px 0px 1px` pattern creates a border-like halo that's softer than an actual border. When drop shadows do appear, they're extremely soft — barely visible lifts that suggest floating rather than casting.

The most dramatic depth effect comes from alternating between Parchment (`{colors.background}`) and Near Black (`{colors.ink}`) sections — entire sections shift elevation by changing the ambient light level.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Sharp inline elements |
| `xs` | 4px | Minimal inline elements |
| `sm` | 6px | Subtly rounded small buttons |
| `md` | 8px | Standard buttons, cards, containers |
| `lg` | 12px | Generously rounded primary buttons, inputs, nav |
| `xl` | 16px | Featured containers, video players, tab lists |
| `2xl` | 24px | Tag-like elements, highlighted containers |
| `3xl` | 32px | Hero containers, embedded media, large cards |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Brand Terracotta `{colors.primary}` with Ivory text. The only chromatic CTA.
- **`button-warm`** — Warm Sand `{colors.surface-warm}` with Charcoal Warm text. The workhorse — warm, unassuming, clearly interactive.
- **`button-white`** — Pure White surface, near-black text. Clean, elevated.
- **`button-dark`** — Dark Surface `{colors.surface-dark}` with Ivory text. Inverted for dark-on-light emphasis.
- **`button-dark-primary`** — Used on dark theme surfaces.

### Cards & Containers
- **`card`** — Ivory or Pure White, 8px radius, Border Cream.
- **`card-featured`** — 16px radius for featured.
- **`card-hero`** — 32px radius for hero containers and embedded media.
- **`card-dark`** — Dark Surface, 8px radius.

### Inputs
- **`input`** — Anthropic Near Black text, 12px radius, focus ring with Focus Blue.

### Navigation
- Sticky top nav, mix of Near Black, Olive Gray, Dark Warm link colors.

### Distinctive Components

**Model Comparison Cards**: Three-column grid with bordered cards, each gets a name, description, and capability badges. Border Warm separation between items.

**Organic Illustrations**: Hand-drawn-feeling vector illustrations in terracotta, black, and muted green. Abstract, conceptual rather than literal.

**Dark/Light Section Alternation**: Page alternates between Parchment and Near Black sections — chapter-like reading rhythm.

## Do's and Don'ts

### Do
- Use Parchment (`{colors.background}`) as the primary light background — the warm cream IS the Claude personality
- Use Anthropic Serif at weight 500 for all headlines — single-weight consistency is intentional
- Use Terracotta Brand (`{colors.primary}`) only for primary CTAs and brand moments
- Keep all neutrals warm-toned — every gray should have a yellow-brown undertone
- Use ring shadows for interactive element states instead of drop shadows
- Maintain the editorial serif/sans hierarchy
- Use generous body line-height for a literary reading experience
- Alternate between light and dark sections to create chapter-like page rhythm
- Apply generous border-radius (12–32px) for soft, approachable feel

### Don't
- Don't use cool blue-grays anywhere — palette is exclusively warm-toned
- Don't use bold (700+) weight on Anthropic Serif — weight 500 is the ceiling
- Don't introduce saturated colors beyond Terracotta — palette is muted
- Don't use sharp corners (< 6px radius) on buttons or cards
- Don't apply heavy drop shadows — depth comes from ring shadows and background shifts
- Don't use pure white (`{colors.surface-white}`) as a page background
- Don't use geometric/tech-style illustrations — Claude's are organic and hand-drawn-feeling
- Don't reduce body line-height below 1.40
- Don't use monospace fonts for non-code content
- Don't mix in sans-serif for headlines

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Small Mobile | <479px | Minimum layout, stacked everything, compact typography |
| Mobile | 479–640px | Single column, hamburger nav, reduced heading sizes |
| Large Mobile | 640–767px | Slightly wider content area |
| Tablet | 768–991px | 2-column grids begin, condensed nav |
| Desktop | 992px+ | Full multi-column layout, expanded nav, max hero (64px) |

### Touch Targets
- Buttons: generous padding (8–16px vertical minimum)
- Navigation: adequately spaced for thumb navigation
- Card surfaces: large touch targets
- Minimum recommended: 44×44px

### Collapsing Strategy
- **Navigation**: full horizontal nav → hamburger
- **Feature sections**: multi-column → stacked single column
- **Hero text**: 64px → 36px → ~25px progressive scaling
- **Model cards**: 3-column → stacked vertical
- **Section padding**: reduces but maintains editorial rhythm

### Image Behavior
- Product screenshots scale proportionally within rounded containers
- Illustrations maintain quality at all sizes
- Video embeds maintain 16:9 with rounded corners
- No art direction changes between breakpoints

---

## Agent Prompt Guide

### Quick Color Reference
- Brand CTA: Terracotta Brand `{colors.primary}`
- Page Background: Parchment `{colors.background}`
- Card Surface: Ivory `{colors.surface}`
- Primary Text: Anthropic Near Black `{colors.ink}`
- Secondary Text: Olive Gray `{colors.text-olive}`
- Tertiary Text: Stone Gray `{colors.text-stone}`
- Borders (light): Border Cream `{colors.border}`
- Dark Surface: Dark Surface `{colors.surface-dark}`

### Example Component Prompts
- "Create a hero section on Parchment (`{colors.background}`) with a headline at 64px Anthropic Serif weight 500, line-height 1.10. Use Anthropic Near Black (`{colors.ink}`) text. Add a subtitle in Olive Gray (`{colors.text-olive}`) at 20px Anthropic Sans with 1.60 line-height. Place a Terracotta Brand (`{colors.primary}`) CTA button with Ivory text, 12px radius."
- "Design a feature card on Ivory (`{colors.surface}`) with a 1px solid Border Cream (`{colors.border}`) border and comfortably rounded corners (8px). Title in Anthropic Serif at 25px weight 500, description in Olive Gray (`{colors.text-olive}`) at 16px Anthropic Sans. Add a whisper shadow."
- "Build a dark section on Anthropic Near Black (`{colors.ink}`) with Ivory headline text in Anthropic Serif at 52px weight 500. Use Warm Silver (`{colors.text-warm-silver}`) for body text. Borders in Dark Surface."
- "Create a button in Warm Sand (`{colors.surface-warm}`) with Charcoal Warm (`{colors.text-charcoal}`) text, 8px radius, and a ring shadow."
- "Design a model comparison grid with three cards on Ivory surfaces. Each card gets a Border Warm (`{colors.border-warm}`) top border, model name in Anthropic Serif at 25px, description in Olive Gray at 15px Anthropic Sans."

### Iteration Guide
1. Focus on ONE component at a time
2. Reference specific color names — "use Olive Gray (`{colors.text-olive}`)" not "make it gray"
3. Always specify warm-toned variants — no cool grays
4. Describe serif vs sans usage explicitly
5. For shadows, use "ring shadow" or "whisper shadow" — never generic "drop shadow"
6. Specify the warm background — "on Parchment" or "on Near Black"
7. Keep illustrations organic and conceptual — "hand-drawn-feeling" style
