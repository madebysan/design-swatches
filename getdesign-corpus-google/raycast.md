---
version: alpha
name: Raycast
description: macOS-native dark interior design — near-black blue-tinted void, multi-layer inset shadows simulating physical depth, Inter with positive tracking, and Raycast Red as a punctuation accent.

colors:
  # Primary surfaces
  background: "#07080a"
  surface: "#101111"
  surface-card: "#1b1c1e"
  surface-button-fg: "#18191a"
  key-start: "#121212"
  key-end: "#0d0d0d"

  # Text
  ink: "#f9f9f9"
  ink-secondary: "#cecece"
  ink-tertiary: "#c0c0c0"
  text-medium: "#9c9c9d"
  text-dim: "#6a6b6c"
  text-disabled: "#434345"

  # Brand / Accent
  primary: "#FF6363"
  accent-blue: "#55b3ff"
  accent-green: "#5fc992"
  accent-yellow: "#ffbc33"

  # Tints (opaque approximations)
  blue-tint: "#0c2638"  # was hsla(202,100%,67%,0.15) — flattened over background
  red-tint: "#3b1a1f"   # was hsla(0,100%,69%,0.15) — flattened over background

  # Borders
  border: "#252829"
  border-strong: "#2f3031"
  border-subtle: "#1a1b1c"  # opaque approx of rgba(255,255,255,0.06) over background — Google format requires hex

  # Inverted CTA
  on-primary: "#ffffff"
  cta-light: "#f0f0f0"  # was hsla(0,0%,100%,0.815) — flattened over background

typography:
  display-hero:
    fontFamily: "Inter, Inter Fallback, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: 0px
    fontFeature: "'liga' 0, 'ss02', 'ss08'"
  section-display:
    fontFamily: "Inter, Inter Fallback, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.17
    letterSpacing: 0.2px
    fontFeature: "'calt', 'kern', 'liga', 'ss03'"
  section-heading:
    fontFamily: "Inter, Inter Fallback, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.2px
    fontFeature: "'calt', 'kern', 'liga', 'ss03'"
  card-heading:
    fontFamily: "Inter, Inter Fallback, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0px
    fontFeature: "'calt', 'kern', 'liga', 'ss03'"
  sub-heading:
    fontFamily: "Inter, Inter Fallback, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.60
    letterSpacing: 0.2px
  body-large:
    fontFamily: "Inter, Inter Fallback, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.2px
  body:
    fontFamily: "Inter, Inter Fallback, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.60
    letterSpacing: 0.2px
  body-tight:
    fontFamily: "Inter, Inter Fallback, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.1px
  button:
    fontFamily: "Inter, Inter Fallback, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "Inter, Inter Fallback, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.3px
  caption:
    fontFamily: "Inter, Inter Fallback, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.14
    letterSpacing: 0.2px
  small:
    fontFamily: "Inter, Inter Fallback, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0px
  code:
    fontFamily: "GeistMono, ui-monospace, SFMono-Regular, Roboto Mono, Menlo, Monaco, monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.60
    letterSpacing: 0.3px

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
  5xl: 80px
  6xl: 120px

rounded:
  sharp: 2px
  micro: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  2xl: 20px
  pill: 9999px

components:
  # Buttons
  button-primary-pill:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-dim}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  button-cta:
    backgroundColor: "{colors.cta-light}"
    textColor: "{colors.surface-button-fg}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-elevated:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-feature:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 32px

  # Inputs
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-tight}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.text-medium}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.ink}"

  # Badges & Keys
  badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 0px 6px
  key-cap:
    backgroundColor: "{colors.key-start}"
    textColor: "{colors.ink}"
    typography: "{typography.small}"
    rounded: "{rounded.micro}"
    padding: 4px 6px

  # Alert states
  alert-error:
    backgroundColor: "{colors.red-tint}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: 16px
  alert-info:
    backgroundColor: "{colors.blue-tint}"
    textColor: "{colors.accent-blue}"
    rounded: "{rounded.lg}"
    padding: 16px
---

# Raycast Design System

## Overview

Raycast's marketing site feels like the dark interior of a precision instrument — a Swiss watch case carved from obsidian. The background isn't just dark, it's an almost-black blue-tint (`{colors.background}`) that creates a sense of being inside a macOS native application rather than a website. Every surface, every border, every shadow is calibrated to evoke the feeling of a high-performance desktop utility: fast, minimal, trustworthy.

The signature move is the layered shadow system borrowed from macOS window chrome: multi-layer box-shadows with inset highlights that simulate physical depth, as if cards and buttons are actual pressed or raised glass elements on a dark desk. Combined with Raycast Red (`{colors.primary}`) — deployed almost exclusively in the hero's iconic diagonal stripe pattern — the palette creates a brand that reads as "powerful tool with personality." The red doesn't dominate; it punctuates.

Inter is used everywhere — headings, body, buttons, captions — with extensive OpenType features (`calt`, `kern`, `liga`, `ss03`) creating a consistent, readable typographic voice. The positive letter-spacing (0.2px–0.4px on body text) is unusual for a dark UI and gives the text an airy, breathable quality that counterbalances the dense, dark surfaces. GeistMono appears for code elements, reinforcing the developer-tool identity.

**Key Characteristics:**
- Near-black blue-tinted background (`{colors.background}`) — not pure black, subtly blue-shifted
- macOS-native shadow system with multi-layer inset highlights simulating physical depth
- Raycast Red (`{colors.primary}`) as a punctuation color — hero stripes, not pervasive
- Inter with positive letter-spacing (0.2px) for an airy, readable dark-mode experience
- Radix UI component primitives powering the interaction layer
- Subtle white borders for containment on dark surfaces
- Keyboard shortcut styling with gradient key caps and heavy shadows

## Colors

### Primary
- **Near-Black Blue** (`{colors.background}`): Primary page background — the foundational void with a subtle blue-cold undertone.
- **Pure White / Near White** (`{colors.ink}`): Primary heading text, high-emphasis elements.
- **Raycast Red** (`{colors.primary}`): Brand accent — hero stripes, danger states, critical highlights.

### Secondary & Accent
- **Raycast Blue** (`{colors.accent-blue}`): Interactive accent — links, focus states, selected items.
- **Raycast Green** (`{colors.accent-green}`): Success states, positive indicators.
- **Raycast Yellow** (`{colors.accent-yellow}`): Warning accents, highlights.
- **Blue Tint** (`{colors.blue-tint}`): Tint overlay for interactive surfaces.
- **Red Tint** (`{colors.red-tint}`): Tint overlay for danger/error surfaces.

### Surface & Background
- **Deep Background** (`{colors.background}`): Page canvas, the darkest surface.
- **Surface 100** (`{colors.surface}`): Elevated surface, card backgrounds.
- **Key Start** (`{colors.key-start}`): Keyboard key gradient start.
- **Key End** (`{colors.key-end}`): Keyboard key gradient end.
- **Card Surface** (`{colors.surface-card}`): Badge backgrounds, tag fills, elevated containers.
- **Button Foreground** (`{colors.surface-button-fg}`): Dark surface for button text on light backgrounds.

### Neutrals & Text
- **Near White** (`{colors.ink}`): Primary body text, high-emphasis content.
- **Light Gray** (`{colors.ink-secondary}`): Secondary body text, descriptions.
- **Silver** (`{colors.ink-tertiary}`): Tertiary text, subdued labels.
- **Medium Gray** (`{colors.text-medium}`): Link default color, secondary navigation.
- **Dim Gray** (`{colors.text-dim}`): Disabled text, low-emphasis labels.
- **Dark Gray** (`{colors.text-disabled}`): Muted borders, inactive navigation links.
- **Border** (`{colors.border}`): Standard border color for cards and dividers.
- **Dark Border** (`{colors.border-strong}`): Separator lines, table borders.

### Gradient System
- **Keyboard Key Gradient**: Linear gradient from `{colors.key-start}` (top) to `{colors.key-end}` (bottom) — simulates physical key depth.
- **Warm Glow**: Subtle warm radial spread used as ambient atmosphere behind featured elements.

## Typography

### Font Family
- **Primary**: `Inter` — humanist sans-serif, used everywhere. Fallbacks: `Inter Fallback`, system sans-serif.
- **System**: `SF Pro Text` — Apple system font for select macOS-native UI elements.
- **Monospace**: `GeistMono` — Vercel's monospace font for code elements.
- **OpenType features**: `calt`, `kern`, `liga`, `ss03` enabled globally; `ss02`, `ss08` on display text; `liga` disabled on hero headings.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | 64px Inter 600 — hero headlines |
| `section-display` | 56px Inter 400 — feature section displays |
| `section-heading` | 24px Inter 500 — sub-section headings |
| `card-heading` | 22px Inter 400 — card titles |
| `sub-heading` | 20px Inter 500 — relaxed sub-heading |
| `body-large` | 18px Inter 400 |
| `body` | 16px Inter 500 — primary body, relaxed rhythm |
| `body-tight` | 16px Inter 400 — compact UI labels |
| `button` | 16px Inter 600 — semibold, slightly wider tracking |
| `nav-link` | 16px Inter 500 — navigation |
| `caption` | 14px Inter 500 — small labels, metadata |
| `small` | 12px Inter 600 — badges, micro-labels |
| `code` | 14px GeistMono 500 |

### Principles
- **Positive tracking on dark**: Unlike most dark UIs that use tight or neutral letter-spacing, Raycast applies +0.2px to +0.4px — creating an airy, readable feel that compensates for the dark background.
- **Weight 500 as baseline**: Most body text uses medium weight (500), not regular (400) — subtle extra heft improves legibility on dark surfaces.
- **Display restraint**: Hero text at 64px/600 is confident but not oversized — Raycast avoids typographic spectacle in favor of functional elegance.
- **OpenType everywhere**: `ss03` (stylistic set 3) is enabled globally across Inter, giving the typeface a slightly more geometric, tool-like quality.

## Layout

### Spacing System
Base unit is **8px**. Section padding spans `5xl`–`6xl` (80–120px) vertical between major sections; card padding `lg`–`3xl`.

### Grid & Container
- Max width: ~1200px container, centered
- Column patterns: Single-column hero, 2–3 column feature grids, full-width showcase sections
- App showcase: Product UI presented in centered window frames

### Whitespace Philosophy
- **Dramatic negative space**: Sections float in vast dark void, creating cinematic pacing between features
- **Dense product, sparse marketing**: Product UI screenshots are information-dense, but surrounding marketing copy uses minimal text with generous spacing
- **Vertical rhythm**: Consistent 24px–32px gaps between elements within sections

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 (Void) | No shadow, dark background surface | Page background |
| Level 1 (Subtle) | `rgba(0,0,0,0.28) 0px 1.189px 2.377px` | Minimal lift, inline elements |
| Level 2 (Ring) | `rgb(27,28,30) 0px 0px 0px 1px outer + rgb(7,8,10) 0px 0px 0px 1px inset` | Card containment, double-ring |
| Level 3 (Button) | Multi-layer with inset top highlight + dark inset bottom | macOS-native button press |
| Level 4 (Key) | 5-layer shadow stack with inset press effects | Keyboard shortcut key caps |
| Level 5 (Floating) | Heavy depth + glow ring + insets | Command palette, floating panels |

**Shadow Philosophy**: Raycast's shadow system is the most macOS-native on the web. Multi-layer shadows combine outer rings for containment, inset top highlights simulating light from above, and inset bottom darks simulating shadow underneath. Elements feel like glass or brushed metal, not flat rectangles.

### Decorative Depth
- **Warm glow**: Subtle warm aura behind featured elements on the cold dark canvas
- **Blue info glow**: For interactive state emphasis
- **Red danger glow**: For error/destructive state emphasis

## Shapes

| Token | Value | Use |
|---|---|---|
| `sharp` | 2px | Micro-elements, code spans |
| `micro` | 4px | Keyboard keys, tiny indicators |
| `sm` | 6px | Buttons, badges, tags — workhorse |
| `md` | 8px | Input fields, inline components |
| `lg` | 12px | Standard cards, product screenshots |
| `xl` | 16px | Large cards, feature sections |
| `2xl` | 20px | Hero cards, prominent containers |
| `pill` | 9999px | Pill buttons, nav CTAs |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly rather than reconstructing them.

### Buttons
- **`button-primary-pill`** — Transparent on dark, white text, full pill, multi-layer inset shadow. Hover: opacity 0.6.
- **`button-secondary`** — Transparent, 6px radius, subtle white border + drop shadow. Hover: opacity 0.6.
- **`button-ghost`** — No background or border, gray text, pill shape. Hover: text brightens to white.
- **`button-cta`** — Semi-transparent white surface, dark text, pill shape — the download CTA.
- **Transition**: All buttons use opacity transition for hover rather than background-color change — a signature Raycast interaction pattern.

### Cards & Containers
- **`card`** — Surface with 1px subtle white border, 12px–16px radius.
- **`card-elevated`** — Double-ring shadow technique (outer + inset) for premium containment.
- **`card-feature`** — 16px–20px radius with subtle warm glow behind hero content.
- **Hover**: Cards brighten slightly via border opacity increase or subtle shadow enhancement.

### Inputs & Forms
- **`input`** — Dark fields with subtle border, 8px radius.
- **`input-focus`** — Border brightens, blue glow ring appears.

### Navigation
- **`nav-bar`** — Dark background blending with page, white text links at 16px weight 500.
- **`nav-link`** — Gray text → white on hover, underline decoration on hover.
- Sticky at top with subtle border separator.

### Badges & Keys
- **`badge`** — Card-surface bg with white text, 6px radius.
- **`key-cap`** — Gradient background (key-start → key-end), heavy multi-layer shadow simulating physical keys.

### Alerts
- **`alert-error`** — Red-tint surface with brand red text and icon.
- **`alert-info`** — Blue-tint surface with accent blue text and icon.

## Do's and Don'ts

### Do
- Use `{colors.background}` (not pure black) — the blue-cold tint is essential to the Raycast feel
- Apply positive letter-spacing (+0.2px) on body text — deliberately different from most dark UIs
- Use multi-layer shadows with inset highlights for interactive elements — the macOS-native depth is signature
- Keep Raycast Red (`{colors.primary}`) as punctuation, not pervasive — reserve it for hero moments and error states
- Use subtle white borders for card containment — barely visible, structurally essential
- Apply weight 500 as the body text baseline — medium weight improves dark-mode legibility
- Use pill shapes (`{rounded.pill}`) for primary CTAs, rectangular shapes (6–8px) for secondary actions
- Enable OpenType features `calt`, `kern`, `liga`, `ss03` on all Inter text
- Use opacity transitions (hover: opacity 0.6) for button interactions, not color changes

### Don't
- Don't use pure black (`#000000`) as the background — the blue tint differentiates Raycast from generic dark themes
- Don't apply negative letter-spacing on body text — Raycast deliberately uses positive spacing for readability
- Don't use Raycast Blue as the primary accent for everything — blue is for interactive/info, red is the brand color
- Don't create single-layer flat shadows — the multi-layer inset system is core to the macOS-native aesthetic
- Don't use regular weight (400) for body text when 500 is available — extra weight prevents dark-mode text from feeling thin
- Don't mix warm and cool borders — stick to the cool gray border palette
- Don't apply heavy drop shadows without inset companions — shadows always come in pairs
- Don't use decorative elements, gradients, or colorful backgrounds — the dark void is the stage, content is the performer

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <600px | Single column, stacked cards, hamburger nav, hero text reduces to ~40px |
| Small Tablet | 600–768px | 2-column grid begins, nav partially visible |
| Tablet | 768–1024px | 2–3 column features, nav expanding, screenshots scale |
| Desktop | 1024–1200px | Full layout, all nav links visible, 64px hero display |
| Large Desktop | >1200px | Max-width container centered, generous side margins |

### Touch Targets
- Pill buttons: pill radius with 20px padding — well above 44px minimum
- Secondary buttons: 8px padding minimum, but border provides visual target expansion
- Nav links: 16px text with surrounding padding for accessible touch targets

### Collapsing Strategy
- **Navigation**: Full horizontal nav → hamburger at mobile with slide-out menu
- **Hero**: 64px display → 48px → 36px across breakpoints
- **Feature grids**: 3-column → 2-column → single-column stack
- **Product screenshots**: Scale within containers, maintaining macOS window chrome proportions
- **Keyboard shortcut displays**: Simplify or hide on mobile where keyboard shortcuts are irrelevant

### Image Behavior
- Product screenshots scale responsively within fixed-ratio containers
- Hero diagonal stripe pattern scales proportionally
- macOS window chrome rounded corners maintained at all sizes
- No lazy-loading artifacts — images are critical to the product narrative

## Agent Prompt Guide

### Quick Color Reference
- Primary Background: Near-Black Blue (`{colors.background}`)
- Primary Text: Near White (`{colors.ink}`)
- Brand Accent: Raycast Red (`{colors.primary}`)
- Interactive Blue: Raycast Blue (`{colors.accent-blue}`)
- Secondary Text: Medium Gray (`{colors.text-medium}`)
- Card Surface: Surface 100 (`{colors.surface}`)
- Border: Dark Border (`{colors.border}`)

### Example Component Prompts
- "Create a hero section on `{colors.background}` with 64px Inter heading (weight 600, line-height 1.1), near-white text (`{colors.ink}`), and a semi-transparent white pill CTA button"
- "Design a feature card with `{colors.surface}` background, subtle white border, 16px border-radius, double-ring shadow, 22px Inter heading, and `{colors.text-medium}` body text"
- "Build a navigation bar on dark background (`{colors.background}`), Inter links at 16px weight 500 in `{colors.text-medium}`, hover to white, and a translucent white pill button at the right end"
- "Create a keyboard shortcut display with key caps using gradient background (`{colors.key-start}` → `{colors.key-end}`), 5-layer shadow for physical depth, 4px radius, Inter 12px weight 600 text"
- "Design an alert card with `{colors.surface}` surface, Raycast Red (`{colors.primary}`) left border accent, translucent red glow, white heading, and `{colors.ink-secondary}` description text"

### Iteration Guide
1. Check the background is `{colors.background}` not pure black — the blue tint is critical
2. Verify letter-spacing is positive (+0.2px) on body text — negative spacing breaks the Raycast aesthetic
3. Ensure shadows have both outer and inset layers — single-layer shadows look flat and wrong
4. Confirm Inter has OpenType features `calt`, `kern`, `liga`, `ss03` enabled
5. Test that hover states use opacity transitions (0.6) not color swaps — this is a core interaction pattern
