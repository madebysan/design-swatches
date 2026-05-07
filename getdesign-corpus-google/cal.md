---
version: alpha
name: Cal.com
description: Monochromatic restraint with Cal Sans display + Inter body, multi-layered shadow elevation, lavish 80–96px section spacing, and zero brand color — boldness through grayscale confidence.

colors:
  # Primary canvas + ink
  background: "#ffffff"
  surface: "#ffffff"
  surface-subtle: "#f5f5f5"
  ink: "#242424"
  ink-deep: "#111111"
  ink-pure: "#000000"
  ink-inverted: "#ffffff"

  # Brand accent — Cal is grayscale; use Charcoal as primary
  primary: "#242424"
  primary-hover: "#1e1f23"

  # Text states
  on-background: "#242424"
  on-surface: "#242424"
  on-primary: "#ffffff"
  text-secondary: "#898989"

  # Links (the only chromatic moments)
  link: "#0099ff"
  link-default: "#0000ee"
  focus-ring: "#3b82f6"  # used at low opacity in shadows; opaque approx

  # Borders — Cal uses ring shadows over CSS borders
  border: "#e5e7eb"
  border-shadow: "#222a35"  # opaque approx of rgba(34,42,53,0.08) — Google format requires hex
  border-input: "#767676"

  # Shadow tints (opaque approximations of multi-layer shadows)
  shadow-strong: "#131316"  # was rgba(19,19,22,0.7) — flattened
  shadow-soft: "#222a35"    # was rgba(34,42,53,0.05)
  shadow-inset: "#000000"   # was rgba(0,0,0,0.16)
  shadow-highlight: "#ffffff"

typography:
  display-hero:
    fontFamily: "Cal Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: 0px
  section-heading:
    fontFamily: "Cal Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: 0px
  feature-heading:
    fontFamily: "Cal Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0px
  sub-heading:
    fontFamily: "Cal Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0.2px
  card-title:
    fontFamily: "Cal Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: 0px
  caption-label:
    fontFamily: "Cal Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.50
    letterSpacing: 0px
  body-light:
    fontFamily: "Cal Sans UI Variable Light, Inter, ui-sans-serif, sans-serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.30
    letterSpacing: -0.2px
  body-light-standard:
    fontFamily: "Cal Sans UI Variable Light, Inter, ui-sans-serif, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.50
    letterSpacing: -0.2px
  caption-light:
    fontFamily: "Cal Sans UI Variable Light, Inter, ui-sans-serif, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.45
    letterSpacing: -0.2px
  ui-label:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption-inter:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.14
    letterSpacing: 0px
  micro:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0px
  code:
    fontFamily: "Roboto Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px

spacing:
  micro: 1px
  2xs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 28px
  3xl: 80px
  4xl: 96px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
  2xl: 16px
  3xl: 29px
  pill: 9999px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-deep}"
    typography: "{typography.ui-label}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink-deep}"
    typography: "{typography.ui-label}"
    padding: 8px 12px

  # Dark primary CTA
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.ui-label}"
    rounded: "{rounded.lg}"
    padding: 10px 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"

  # White / ghost button — relies on shadow ring
  button-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.ui-label}"
    rounded: "{rounded.lg}"
    padding: 10px 16px

  # Pill action / badge
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-inter}"
    rounded: "{rounded.pill}"
    padding: 6px 12px

  # Compact action
  button-compact:
    backgroundColor: "{colors.surface-subtle}"
    textColor: "{colors.ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.md}"
    padding: 4px 8px

  # Card with multi-layered shadow
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.xl}"
    padding: 24px
  card-large:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.2xl}"
    padding: 32px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-pure}"
    typography: "{typography.body-light-standard}"
    rounded: "{rounded.lg}"
    padding: 10px 12px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-pure}"

  # Trust bar / link
  link:
    textColor: "{colors.link}"
    typography: "{typography.caption-inter}"
---

# Cal.com Design System

## Overview

Cal.com's website is a masterclass in monochromatic restraint — a grayscale world where boldness comes not from color but from the sheer confidence of black text on white space. Inspired by Uber's minimal aesthetic, the palette is deliberately stripped of hue: near-black headings (`{colors.ink}`), mid-gray secondary text (`{colors.text-secondary}`), and pure white surfaces. Color is treated as a foreign substance — when it appears (a rare blue link, a green trust badge), it feels like a controlled accent in an otherwise black-and-white photograph.

Cal Sans, the brand's custom geometric display typeface designed by Mark Davis, is the visual centerpiece. Letters are intentionally spaced extremely close at large sizes, creating dense, architectural headlines that feel like they're carved into the page. At 64px and 48px, Cal Sans headings sit at weight 600 with a tight 1.10 line-height — confident, compressed, and immediately recognizable. For body text, the system switches to Inter, providing rock-solid readability that complements Cal Sans's display personality. The typography pairing creates a clear division: Cal Sans speaks, Inter explains.

The elevation system is notably sophisticated for a minimal site — 11 shadow definitions create a nuanced depth hierarchy using multi-layered shadows that combine ring borders, soft diffused shadows, and inset highlights. This shadow-first approach to depth (rather than border-first) gives surfaces a subtle three-dimensionality that feels modern and polished. Built on Framer with a border-radius scale from 2px to 9999px (pill), Cal.com balances geometric precision with soft, rounded interactive elements.

**Key Characteristics:**
- Purely grayscale brand palette — no brand colors, boldness through monochrome
- Cal Sans custom geometric display font with extremely tight default letter-spacing
- Multi-layered shadow system (11 definitions) with ring borders + diffused shadows + inset highlights
- Cal Sans for headings, Inter for body — clean typographic division
- Wide border-radius scale from 2px to 9999px (pill)
- White canvas with near-black `{colors.ink}` text — maximum contrast, zero decoration
- Product screenshots as primary visual content — the scheduling UI sells itself
- Built on Framer platform

## Colors

### Primary
- **Charcoal** (`{colors.ink}`): Primary heading and button text — Cal.com's signature near-black, warmer than pure black.
- **Midnight** (`{colors.ink-deep}`): Deepest text/overlay color.
- **White** (`{colors.background}`): Primary background and surface — the dominant canvas.

### Secondary & Accent
- **Link Blue** (`{colors.link}`): In-text links with underline decoration — the only blue, reserved strictly for hyperlinks.
- **Default Link** (`{colors.link-default}`): Browser-default link color on some elements — unmodified.
- **Focus Ring** (`{colors.focus-ring}`): Keyboard focus indicator — accessibility-only.

### Surface & Background
- **Pure White** (`{colors.surface}`): Page background and card surfaces.
- **Light Gray** (`{colors.surface-subtle}`): Subtle section differentiation.
- **Mid Gray** (`{colors.text-secondary}`): Secondary text, descriptions, and muted labels.

### Text
- **Charcoal** (`{colors.ink}`): Headlines, buttons, primary UI text.
- **Midnight** (`{colors.ink-deep}`): High-contrast links and nav text.
- **Mid Gray** (`{colors.text-secondary}`): Descriptions, secondary labels.
- **Pure Black** (`{colors.ink-pure}`): Certain link text elements.
- **Border Shadow** (`{colors.border-shadow}`): Shadow-based borders using ring shadows instead of CSS borders.

### Semantic
Cal.com is deliberately colorless for brand elements — "a grayscale brand to emphasise on boldness and professionalism". Product UI screenshots show color (blues, greens), but the marketing site itself stays monochrome. The philosophy mirrors Uber's: let the content carry color, the frame stays neutral.

### Gradient System
No gradients on the marketing site — fully flat and monochrome. Depth is achieved entirely through shadows, not color transitions.

## Typography

### Font Families
- **Display**: `Cal Sans` — custom geometric sans-serif by Mark Davis. Open-source on Google Fonts and GitHub. Extremely tight default letter-spacing for large headlines. 6 character variants (Cc, j, t, u, 0, 1).
- **Body**: `Inter` — rock-solid standard body font.
- **UI Light**: `Cal Sans UI Variable Light` — light-weight variant (300) for softer UI text with -0.2px letter-spacing.
- **Mono**: `Roboto Mono` — code blocks and technical content.

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-hero` | 64px hero — maximum impact, tight default spacing |
| `section-heading` | 48px section titles |
| `feature-heading` | 24px feature block headlines |
| `sub-heading` | 20px sub-heading with positive +0.2px tracking |
| `card-title` | 16px smallest Cal Sans usage |
| `caption-label` | 12px small labels in Cal Sans |
| `body-light` | 18px light-weight intro text |
| `body-light-standard` | 16px light-weight body |
| `caption-light` | 14px light captions and descriptions |
| `ui-label` | 16px Inter UI buttons and nav labels |
| `caption-inter` | 14px Inter small UI text |
| `micro` | 12px Inter smallest text |
| `code` | 14px Roboto Mono code snippets |

### Principles
- **Cal Sans at large, Inter at small**: Cal Sans is exclusively for headings and display.
- **Tight by default, space when small**: At 20px and below, positive letter-spacing (+0.2px) prevents cramming.
- **Weight 300 body variant**: Cal Sans UI Variable Light at 300 creates an elegant, airy body text contrasting with dense 600-weight headlines.
- **Weight 600 dominance**: Nearly all Cal Sans usage is at weight 600.
- **Negative tracking on light text**: Cal Sans UI Light uses -0.2px letter-spacing.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px. The scale has a notable jump from `{spacing.2xl}` (28px) to `{spacing.3xl}` (80px) — a deliberate gap emphasizing section-level spacing.

### Grid & Container
- Max width: ~1200px content container, centered
- Full-width hero, centered text blocks, 2-3 column feature grids
- Feature showcase: product screenshots flanked by description text
- Breakpoints: 98px, 640px, 768px, 810px, 1024px, 1199px (Framer-generated)

### Whitespace Philosophy
- **Lavish section spacing**: 80px–96px between sections creates a breathable, premium feel.
- **Product-first content**: Screenshots dominate the visual space.
- **Centered headlines**: Cal Sans headings centered with generous margins.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Page canvas, basic text containers |
| Inset (Level 1) | Inset shadow at low opacity | Pressed/recessed elements, input wells |
| Ring + Soft (Level 2) | Sharp contact shadow + ring border + diffused soft shadow | Cards, containers — the workhorse shadow |
| Inset Highlight (Level 3) | White inset top shadow | Button inner highlight — 3D pressed effect |
| Soft Only (Level 4) | Diffused ambient shadow | Subtle ambient elevation |

**Shadow Philosophy**: Cal.com's shadow system is the most sophisticated element of the design — 11 shadow definitions using a multi-layered compositing technique:
- **Ring borders**: `0px 0px 0px 1px` shadows act as borders, avoiding CSS `border` entirely.
- **Diffused soft shadows**: `0px 4px 8px` at low opacity add gentle ambient depth.
- **Sharp contact shadows**: `0px 1px 5px -4px` create tight bottom-edge shadows for grounding.
- **Inset highlights**: White inset shadows at the top of buttons create a subtle 3D bevel.
- Shadows are composed in comma-separated stacks — each surface gets 2-3 layered shadow definitions.

No gradients or glow effects. All depth comes from the shadow compositing system.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Sharp inline elements |
| `xs` | 2px | Subtle rounding |
| `sm` | 4px | Small UI components |
| `md` | 6px | Buttons, small cards, images |
| `lg` | 8px | Standard interactive elements |
| `xl` | 12px | Medium containers, larger cards |
| `2xl` | 16px | Large section containers |
| `3xl` | 29px | Special rounded elements |
| `pill` | 9999px | Full pill — badges, links |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Charcoal `{colors.primary}` background, white text, 8px radius. Hover: opacity reduction. The signature CTA — maximally dark on white.
- **`button-ghost`** — White background with shadow-ring border, dark text. Uses the multi-layered shadow system for subtle elevation.
- **`button-pill`** — `{rounded.pill}` radius for rounded pill-shaped actions and badges.
- **`button-compact`** — 4px padding, small text — utility actions within product UI.
- Some buttons feature a subtle white inset top highlight creating a 3D pressed effect.

### Cards & Containers
- **`card`** — White background, multi-layered shadow (ring shadow + soft shadow + contact shadow). 12px radius for standard cards.
- **`card-large`** — 16px radius for larger containers.
- Hover: subtle shadow deepening or scale transform.

### Inputs
- **`input`** — White background, near-black text, 1px solid `{colors.border-input}` border. 8px radius. Focus uses Framer's focus outline system.

### Navigation
- White/transparent background, Cal Sans links at near-black.
- Nav text: `{colors.ink-deep}` for primary links.
- Mobile: collapses to hamburger.

### Image Treatment
- Large scheduling UI screenshots — the product is the primary visual.
- Trust logos: grayscale company logos in a horizontal trust bar.
- No decorative imagery — pure product + typography.

## Do's and Don'ts

### Do
- Use Cal Sans exclusively for headings (24px+) and never for body text.
- Apply positive letter-spacing (+0.2px) when using Cal Sans below 24px.
- Maintain the grayscale palette — boldness comes from contrast, not color.
- Use the multi-layered shadow system for card elevation — ring shadow + diffused shadow + contact shadow.
- Keep backgrounds pure white.
- Use Inter for all body text at weight 300–600.
- Let product screenshots be the visual content — no illustrations, no decorative graphics.
- Apply generous section spacing (80px–96px).

### Don't
- Use Cal Sans for body text or text below 16px.
- Add brand colors — Cal.com is intentionally grayscale.
- Use CSS borders when shadows can achieve the same containment.
- Apply negative letter-spacing to Cal Sans at small sizes.
- Create heavy, dark shadows — Cal.com's shadows are subtle.
- Use illustrations, abstract graphics, or decorative elements.
- Mix Cal Sans weights — the font is designed for weight 600.
- Reduce section spacing below 48px.

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <640px | Single column, hero ~36px, stacked features, hamburger nav |
| Tablet Small | 640–768px | 2-column begins for some elements |
| Tablet | 768–810px | Layout adjustments, fuller grid |
| Tablet Large | 810–1024px | Multi-column feature grids |
| Desktop | 1024–1199px | Full layout, expanded navigation |
| Large Desktop | >1199px | Max-width container, centered content |

### Touch Targets
- Buttons: 8px radius with comfortable padding (10px+ vertical)
- Mobile CTAs: full-width dark buttons
- Pill badges: 9999px radius creates large, tappable targets

### Collapsing Strategy
- **Navigation**: full horizontal nav → hamburger on mobile
- **Hero**: 64px Cal Sans display → ~36px on mobile
- **Feature grids**: multi-column → 2-column → single stacked
- **Section spacing**: reduces from 80–96px to ~48px on mobile

### Image Behavior
- Product screenshots scale responsively
- Trust logos reflow to multi-row grid on mobile
- Images use 7px–12px border-radius for consistent rounded corners

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Text: Charcoal `{colors.ink}`
- Deep Text: Midnight `{colors.ink-deep}`
- Secondary Text: Mid Gray `{colors.text-secondary}`
- Background: Pure White `{colors.background}`
- Link: Link Blue `{colors.link}`
- CTA Button: Charcoal `{colors.primary}` bg, white text
- Shadow Border: `{colors.border-shadow}` ring

### Example Component Prompts
- "Create a hero section with white background, 64px Cal Sans heading at weight 600, line-height 1.10, `{colors.ink}` text, centered layout with a dark CTA button (`{colors.primary}`, 8px radius, white text)."
- "Design a scheduling card with white background, multi-layered shadow (sharp contact + ring border + diffused soft), 12px radius."
- "Build a navigation bar with white background, Inter links at 14px weight 500 in `{colors.ink-deep}`, a dark CTA button (`{colors.primary}`), sticky positioning."
- "Create a trust bar with grayscale company logos, horizontally centered, 16px gap between logos, on white background."
- "Design a feature section with 48px Cal Sans heading (weight 600, `{colors.ink}`), 16px Inter body text (weight 300, `{colors.text-secondary}`, line-height 1.50), and a product screenshot with 12px radius and the card shadow."

### Iteration Guide
1. Verify headings use Cal Sans at weight 600, body uses Inter — never mix them
2. Check that the palette is purely grayscale — if you see brand colors, remove them
3. Ensure card elevation uses the multi-layered shadow stack, not CSS borders
4. Confirm section spacing is generous (80px+)
5. The overall tone should feel like a clean, professional scheduling tool — monochrome confidence without decorative flourishes
