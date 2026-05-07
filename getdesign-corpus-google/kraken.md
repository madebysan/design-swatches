---
version: alpha
name: Kraken
description: Trustworthy crypto exchange identity built on Kraken Purple — clean white surfaces, near-black ink, dual-typeface system (Kraken-Brand + Kraken-Product), and confident 12px button radii.

colors:
  # Base
  background: "#ffffff"
  ink: "#101114"
  on-primary: "#ffffff"

  # Brand purple
  primary: "#7132f5"
  primary-dark: "#5741d8"
  primary-deep: "#5b1ecf"
  primary-subtle: "#ece3fe"  # was rgba(133,91,251,0.16) — Google format requires hex

  # Neutral scale
  cool-gray: "#686b82"
  silver-blue: "#9497a9"
  border: "#dedee5"
  surface-tint: "#f4f4f7"  # was rgba(148,151,169,0.08) — Google format requires hex
  ink-secondary: "#484b5e"

  # Semantic
  success: "#149e61"
  success-dark: "#026b3f"
  success-tint: "#e0f0ea"  # was rgba(20,158,97,0.16) — Google format requires hex
  neutral-tint: "#e8e9ec"  # was rgba(104,107,130,0.12) — Google format requires hex

  # Shadow tint (opaque approximation)
  shadow-subtle: "#f7f7f7"  # was rgba(0,0,0,0.03) — Google format requires hex
  shadow-micro: "#f5f6f7"  # was rgba(16,24,40,0.04) — Google format requires hex

typography:
  display-hero:
    fontFamily: "Kraken-Brand, IBM Plex Sans, Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.17
    letterSpacing: -1px
  section-heading:
    fontFamily: "Kraken-Brand, IBM Plex Sans, Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: -0.5px
  sub-heading:
    fontFamily: "Kraken-Brand, IBM Plex Sans, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.5px
  feature-title:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0px
  body:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0px
  body-medium:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0px
  button:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0px
  caption:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  small:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  micro:
    fontFamily: "Kraken-Product, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 7px
    fontWeight: 500
    lineHeight: 1.00
    letterSpacing: 0px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px

rounded:
  none: 0px
  sm: 6px
  md: 10px
  lg: 12px
  xl: 16px
  pill: 9999px
  circle: 9999px

components:
  # Primary purple button
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: 13px 16px

  # Outlined purple variant
  button-outlined:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: 13px 16px

  # Subtle purple variant
  button-subtle:
    backgroundColor: "{colors.primary-subtle}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: 8px 12px

  # White button with shadow
  button-white:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 13px 16px

  # Secondary gray
  button-secondary:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: 13px 16px

  # Card
  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.xl}"
    padding: 24px

  # Input
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 12px 16px

  # Success badge
  badge-success:
    backgroundColor: "{colors.success-tint}"
    textColor: "{colors.success-dark}"
    typography: "{typography.small}"
    rounded: "{rounded.sm}"
    padding: 4px 8px

  # Neutral badge
  badge-neutral:
    backgroundColor: "{colors.neutral-tint}"
    textColor: "{colors.ink-secondary}"
    typography: "{typography.small}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
---

# Kraken Design System

## Overview

Kraken's website is a clean, trustworthy crypto exchange that uses purple as its commanding brand color. The design operates on white backgrounds with Kraken Purple (`{colors.primary}`, `{colors.primary-dark}`, `{colors.primary-deep}`) creating a distinctive, professional crypto identity. The proprietary Kraken-Brand font handles display headings with bold (700) weight and negative tracking, while Kraken-Product (with IBM Plex Sans fallback) serves as the UI workhorse.

The design language pairs confident purple branding with cool blue-gray neutrals — a deliberate move away from the saturated colorful palettes common to consumer crypto. Subtle shadows (whisper-level, ~3% opacity) keep the surface feeling light and airy, while a green accent serves only positive/success states like price indicators.

**Key Characteristics:**
- Kraken Purple (`{colors.primary}`) as primary brand with darker variants for depth
- Kraken-Brand (display) + Kraken-Product (UI) dual font system
- Near-black (`{colors.ink}`) text with cool blue-gray neutral scale
- 12px radius buttons (rounded but not pill)
- Subtle shadows — whisper-level, never dramatic
- Green accent (`{colors.success}`) for positive/success states only

## Colors

### Primary
- **Kraken Purple** (`{colors.primary}`): Primary CTA, brand accent, links
- **Purple Dark** (`{colors.primary-dark}`): Button borders, outlined variants
- **Purple Deep** (`{colors.primary-deep}`): Deepest purple
- **Purple Subtle** (`{colors.primary-subtle}`): Subtle purple-tinted button backgrounds
- **Near Black** (`{colors.ink}`): Primary text

### Neutral
- **Cool Gray** (`{colors.cool-gray}`): Primary neutral
- **Silver Blue** (`{colors.silver-blue}`): Secondary text, muted elements
- **White** (`{colors.background}`): Primary surface
- **Border Gray** (`{colors.border}`): Divider borders
- **Surface Tint** (`{colors.surface-tint}`): Secondary button background

### Semantic
- **Success Green** (`{colors.success}`): Positive states
- **Success Dark** (`{colors.success-dark}`): Success badge text
- **Success Tint** (`{colors.success-tint}`): Success badge fill

## Typography

### Font Families
- **Display**: `Kraken-Brand`, fallbacks `IBM Plex Sans, Helvetica, Arial`
- **UI / Body**: `Kraken-Product`, fallbacks `Helvetica Neue, Helvetica, Arial`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens (`{typography.display-hero}`, `{typography.body}`) directly.

| Token | Use |
|---|---|
| `display-hero` | 48px hero, weight 700 |
| `section-heading` | 36px section heads |
| `sub-heading` | 28px sub-section heads |
| `feature-title` | 22px feature heads (Kraken-Product) |
| `body` | Standard reading text |
| `body-medium` | Emphasized body |
| `button` | Button labels |
| `caption` | Small captions |
| `small` | 12px metadata |
| `micro` | 7px uppercase micro labels |

### Principles
- **Two-font discipline**: Display in Kraken-Brand bold, body and UI in Kraken-Product. No mixing.
- **Negative tracking on display**: -1px at 48px, -0.5px at 36px and 28px. Body stays at normal tracking.
- **Weight 700 for display gravitas, 400/500/600 for UI flexibility**.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. The scale runs `micro` (2px) through `2xl` (24px), with intermediate values at 4 / 8 / 12 / 16 / 20.

### Grid & Container
- Standard centered content with max-width caps around 1200–1280px
- Card grids: 2–3 columns on desktop collapsing to single column on mobile

### Whitespace Philosophy
Kraken sits between editorial and product-dense — generous between sections (`xl`–`2xl`) but tight inside cards. Purple is the spatial anchor: large purple CTAs draw the eye to action.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Default surfaces |
| Subtle (Level 1) | `0 4px 24px {colors.shadow-subtle}` | White buttons, lifted cards |
| Micro (Level 2) | `0 1px 4px {colors.shadow-micro}` | Hairline elevation hints |

**Shadow Philosophy**: Kraken's shadows are whisper-level — barely-perceptible elevation cues rather than dramatic floats. The white-on-white card uses the only meaningful shadow in the system.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Sharp inline elements (rare) |
| `sm` | 6px | Small badges |
| `md` | 10px | White buttons |
| `lg` | 12px | All standard buttons — the Kraken default |
| `xl` | 16px | Cards |
| `pill` | 9999px | Full pill shapes (rare in product UI) |
| `circle` | 9999px | Avatars, status dots |

The 12px button radius is the system's identity — rounded but not pill, signaling approachability without losing precision.

## Components

The complete component spec lives in the `components:` token block above. Reference components directly (`{components.button-primary}`, `{components.card}`).

### Buttons
- **`button-primary`** — purple fill, white text, 12px radius
- **`button-outlined`** — white fill with purple-dark border and text
- **`button-subtle`** — pale purple tinted background with primary text
- **`button-white`** — white surface with subtle shadow, 10px radius
- **`button-secondary`** — gray-tinted neutral background

### Cards
- **`card`** — white surface, 16px radius, no border by default

### Inputs
- **`input`** — white surface, 12px radius, 12px×16px padding

### Badges
- **`badge-success`** — green-tinted fill, 6px radius
- **`badge-neutral`** — gray-tinted fill, 6px radius

## Do's and Don'ts

### Do
- Use Kraken Purple (`{colors.primary}`) for CTAs and links
- Apply 12px radius on all buttons
- Use Kraken-Brand for headings, Kraken-Product for body
- Reserve green (`{colors.success}`) for positive/price-up states only
- Keep shadows whisper-level (3–4% opacity)

### Don't
- Don't use pill buttons — 12px is the max radius for buttons
- Don't use other purples outside the defined scale
- Don't introduce additional accent colors beyond the brand purple and success green
- Don't mix the two fonts within a single content block

---

## Responsive Behavior

Breakpoints: 375px, 425px, 640px, 768px, 1024px, 1280px, 1536px

### Touch Targets
- Buttons: 13px vertical padding ensures 44px+ effective tap height with 16px text
- Inputs: 12px×16px padding for thumb-comfortable input

### Collapsing Strategy
- Hero: 48px → 36px → 28px progressive scaling
- Cards: 3-col → 2-col → stacked
- Sections compress vertical padding on mobile

---

## Agent Prompt Guide

### Quick Color Reference
- Brand: Kraken Purple (`{colors.primary}`)
- Dark variant: `{colors.primary-dark}`
- Text: Near Black (`{colors.ink}`)
- Secondary text: `{colors.silver-blue}`
- Background: White (`{colors.background}`)

### Example Component Prompts
- "Create hero: white background. Kraken-Brand 48px weight 700, letter-spacing -1px. Purple CTA (`{colors.primary}`, 12px radius, 13px 16px padding)."
- "Build a card grid: white cards, 16px radius, 24px padding, 1px solid `{colors.border}`. Title in Kraken-Product 22px weight 600. Body 16px weight 400 in `{colors.silver-blue}`."
- "Add a success badge: `{colors.success-tint}` fill, `{colors.success-dark}` text, 6px radius, 4px 8px padding, 12px Kraken-Product weight 500."

### Iteration Guide
1. Purple is the brand — use it for CTAs and emphasis
2. 12px radius is the workhorse button shape
3. Two fonts only: Kraken-Brand for display, Kraken-Product for everything else
4. Shadows are whisper-level — never use dramatic drop shadows
5. Green only for positive states — never for primary actions
