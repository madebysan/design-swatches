---
version: alpha
name: Binance.US
description: Crypto trading-floor system — alternating white and near-black sections, Binance Yellow as singular accent, BinancePlex typeface, pill CTAs, whisper-light shadows.

colors:
  # Surface
  background: "#ffffff"
  surface: "#ffffff"
  surface-snow: "#f5f5f5"
  surface-dark: "#222126"
  surface-dark-card: "#2b2f36"

  # Brand yellows
  primary: "#f0b90b"
  primary-gold: "#ffd000"
  primary-light: "#f8d12f"
  primary-active: "#d0980b"

  # Ink + text
  ink: "#1e2026"
  ink-inverted: "#ffffff"
  text-secondary: "#32313a"
  text-muted: "#848e9c"
  text-disabled: "#686a6c"
  text-tertiary: "#777e90"
  text-hover: "#1a1a1a"

  on-background: "#1e2026"
  on-surface: "#1e2026"
  on-primary: "#1e2026"
  on-dark: "#ffffff"

  # Brand interactive
  focus-blue: "#1eaedb"

  # Crypto semantic
  success: "#0ecb81"
  error: "#f6465d"

  # Borders
  border: "#e6e8ea"
  border-gold: "#ffd000"

  # Shadow tints (opaque approximations)
  shadow-card: "#f2f3f3"  # was rgba(32,32,37,0.05) — flattened
  shadow-hover: "#f4f4f4"  # was rgba(8,8,8,0.05) — flattened
  shadow-pill: "#999999"  # rgb(153,153,153) for pill drop
  shadow-heavy: "#000000"  # rgba(0,0,0) modal drop

typography:
  display-hero:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: 0px
  display-secondary:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0px
  heading-1:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0px
  heading-2:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0px
  heading-3:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  heading-4:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  body-semibold:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0px
  body-bold:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.16px
  button-small:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 14.4px
    fontWeight: 600
    lineHeight: 1.6
    letterSpacing: 0.72px
  caption:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  caption-semibold:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0px
  small:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  tiny:
    fontFamily: "BinancePlex, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0px

spacing:
  micro: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 20px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px
  5xl: 80px

rounded:
  none: 0px
  micro: 1px
  xs: 2px
  sm: 6px
  md: 8px
  lg: 10px
  xl: 12px
  2xl: 24px
  pill: 50px

components:
  # Sticky white nav
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.body-semibold}"
    rounded: "{rounded.none}"
    padding: 12px 32px

  # Primary yellow CTA — square-ish
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 6px 32px
  button-primary-hover:
    backgroundColor: "{colors.focus-blue}"
    textColor: "{colors.on-dark}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"

  # Primary gold pill — signature CTA
  button-pill:
    backgroundColor: "{colors.primary-gold}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 10px 24px

  # Secondary outlined pill
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 10px 24px

  # Disabled
  button-disabled:
    backgroundColor: "{colors.border}"
    textColor: "{colors.text-muted}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 6px 32px

  # Card — content
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px

  # Card — data
  card-data:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 16px

  # Card — dark surface
  card-dark:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xl}"
    padding: 24px

  # Card — large hero / video
  card-hero:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.2xl}"
    padding: 32px

  # Form input
  input:
    backgroundColor: "{colors.surface-snow}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 0px 12px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"

  # Tag / badge
  badge:
    backgroundColor: "{colors.surface-snow}"
    textColor: "{colors.ink}"
    typography: "{typography.small}"
    rounded: "{rounded.lg}"
    padding: 2px 8px

  # Crypto positive indicator
  badge-up:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.success}"
    typography: "{typography.caption-semibold}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  badge-down:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"
    typography: "{typography.caption-semibold}"
    rounded: "{rounded.sm}"
    padding: 2px 8px

  # Section dark wrapper
  section-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 64px 32px
---

# Binance.US Design System

## Overview

Binance.US radiates the polished urgency of a digital trading floor — a space where money moves and decisions happen in seconds. The design is a two-tone composition that alternates between stark white trading surfaces and deep near-black panels (`{colors.surface-dark}`), creating a visual rhythm that mirrors the bull-and-bear duality of crypto markets. Binance Yellow (`{colors.primary}`) cuts through this monochrome foundation like a gold ingot on a steel desk — unmistakable, confident, and engineered to guide every eye toward the next action.

The interface speaks the language of fintech trust. Custom BinancePlex typography gives every headline and data point a proprietary gravitas, while generous whitespace and restrained decoration keep the focus on numbers, charts, and call-to-action buttons. The design avoids visual complexity in favor of operational clarity — every element exists to either inform or convert. Product screenshots of the mobile trading app dominate the middle sections, presented on floating device mockups against golden gradients, reinforcing that this is a platform you carry with you.

What makes Binance.US distinctive is the tension between warmth and precision. The golden yellow brand color — warm, optimistic, almost celebratory — lives inside a system of cold, clinical grey text and razor-sharp borders. This isn't a playful fintech like Robinhood or a corporate fortress like Fidelity — it's a crypto-native platform that wraps cutting-edge trading technology in the visual language of established finance.

**Key Characteristics:**
- Two-tone light/dark section alternation — white surfaces for trust, dark panels for depth
- Binance Yellow (`{colors.primary}`) as the singular accent color driving all primary actions
- BinancePlex custom typeface providing proprietary brand identity at every text level
- Pill-shaped CTA buttons (50px radius) that demand attention
- Floating device mockups on golden gradients for product showcasing
- Crypto price tickers with real-time data prominently displayed
- Shadow-light elevation with subtle 5% opacity card shadows

## Colors

### Primary
- **Binance Yellow** (`{colors.primary}`): The signature — primary CTA backgrounds, brand accent, active states, link color.
- **Binance Gold** (`{colors.primary-gold}`): Lighter gold used for pill button borders, secondary CTA fills, and golden gradient highlights.
- **Light Gold** (`{colors.primary-light}`): Soft gold for gradient endpoints and hover-adjacent states.

### Secondary & Accent
- **Active Yellow** (`{colors.primary-active}`): Darkened yellow for active/pressed button states.
- **Focus Blue** (`{colors.focus-blue}`): Accessibility focus state on hover and focus.

### Surface & Background
- **Pure White** (`{colors.surface}`): Primary page canvas, card surfaces.
- **Snow** (`{colors.surface-snow}`): Subtle surface differentiation, input backgrounds.
- **Binance Dark** (`{colors.surface-dark}`): Dark section backgrounds, footer canvas — near-black with a faint purple undertone.
- **Dark Card** (`{colors.surface-dark-card}`): Card surfaces within dark sections.
- **Ink** (`{colors.ink}`): Button text on yellow backgrounds, deepest text color.

### Neutrals & Text
- **Primary Text** (`{colors.ink}`): Main body, headings on light.
- **Secondary Text** (`{colors.text-secondary}`): Navigation links, descriptive copy.
- **Slate** (`{colors.text-muted}`): Tertiary text, metadata, timestamps — the workhorse grey.
- **Steel** (`{colors.text-disabled}`): Disabled-adjacent text.
- **Muted** (`{colors.text-tertiary}`): Secondary navigation, less prominent footer.
- **Hover Dark** (`{colors.text-hover}`): Universal link hover color.

### Semantic
- **Crypto Green** (`{colors.success}`): Positive price movement, success states.
- **Crypto Red** (`{colors.error}`): Negative price movement, error states.
- **Border Light** (`{colors.border}`): Standard card and section borders.
- **Border Gold** (`{colors.border-gold}`): Active/selected state borders.

### Gradient System
- **Golden Glow**: Radial gradient from `{colors.primary}` center to `{colors.primary-light}` edge — used behind product mockup screenshots.
- **Dark Fade**: Linear gradient from `{colors.surface-dark}` to transparent — used for dark section transitions.

## Typography

### Font Family
- **Primary**: BinancePlex (custom proprietary). Fallbacks: Arial, sans-serif. Weights: 400, 500, 600, 700.
- **System**: system-ui stack for cookie banners and third-party UI.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Use those tokens directly.

| Token | Use |
|---|---|
| `display-hero` | Hero headlines, maximum impact (60px) |
| `display-secondary` | Section titles on dark backgrounds (34px) |
| `heading-1` | Major section headings |
| `heading-2` | Feature headings, card titles (700) |
| `heading-3` | Subsection headings (600) |
| `heading-4` | Card headings, feature labels |
| `body-large` | Hero subtitle, lead paragraphs |
| `body` / `body-semibold` / `body-bold` | Standard body and emphasis variants |
| `button-ui` | Primary button text |
| `button-small` | Secondary buttons with wider tracking |
| `caption` / `caption-semibold` | Metadata, prices, labels |
| `small` | Tags, badges, fine print |
| `tiny` | Micro-labels, chart annotations |

### Principles
BinancePlex is engineered for data-dense interfaces where numbers and text must coexist at multiple scales. The typeface has tabular numerals by default — critical for price columns and portfolio values. Weights lean heavier (500-700), giving the interface authority. Tight line-heights (1.00-1.25) on headings create a stacked, compressed feel that mirrors trading dashboards, while body text opens up to 1.50 for comfortable reading.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

| Token | Value | Use |
|-------|-------|-----|
| `micro` | 4px | Tight inline gaps |
| `xs` | 8px | Base unit, button icon gaps |
| `sm` | 12px | Card internal padding |
| `md` | 16px | Standard padding |
| `lg` | 20px | Card gaps |
| `xl` | 24px | Section internal padding |
| `2xl` | 32px | Section breaks |
| `3xl` | 48px | Major section padding |
| `4xl` | 64px | Hero section padding |
| `5xl` | 80px | Large section spacing |

### Grid & Container
- Max container width: 1200px (centered)
- Hero area: single column with side-by-side text + image above 1024px
- Feature grid: 3-column on desktop, single column on mobile
- Horizontal padding: 32px desktop, 16px mobile
- Grid gap: 24px between feature cards

### Whitespace Philosophy
Binance.US uses whitespace as a trust signal. Generous padding around the hero section creates spaciousness that counters the information density typically associated with crypto exchanges. Light sections breathe; dark sections compress, packing features into tighter grids to convey capability and depth.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | No shadow | Default for inline elements |
| Subtle | 3px+5px drop using `{colors.shadow-card}` (~5%) | Content cards, resting state |
| Medium | 3px+5px+5px spread using `{colors.shadow-hover}` (~5%) | Hovered cards, elevated containers |
| Pill Shadow | 2px+10px-3px using `{colors.shadow-pill}` | Pill CTA buttons, floating actions |
| Heavy | 32px+37px drop using `{colors.shadow-heavy}` | Modal overlays, dropdown menus |

Binance.US uses a whisper-light shadow system. Card shadows are barely perceptible at 5% opacity — they exist not for dramatic depth but as subtle ground cues. The pill button shadow is the exception: slightly more visible to give CTAs a "floating" quality.

### Decorative Depth
- **Golden gradient backgrounds**: Behind device mockup sections, radial golden glow centered on the product
- **Dark-to-light section transitions**: Hard cut between white and `{colors.surface-dark}` sections
- **Price ticker strip**: Flat, borderless data bar

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Flat sections |
| `micro` | 1px | Subtle edge softening |
| `xs` | 2px | Close buttons, micro-interactive |
| `sm` | 6px | Primary buttons (non-pill), small cards |
| `md` | 8px | Form inputs, data cards |
| `lg` | 10px | Navigation pills, tag containers |
| `xl` | 12px | Content cards |
| `2xl` | 24px | Video containers, hero imagery |
| `pill` | 50px | Pill buttons, search inputs |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Yellow fill, `{rounded.sm}` (6px). Hover: focus blue. Active: darker yellow.
- **`button-pill`** — Gold fill, `{rounded.pill}` (50px). The signature CTA shape.
- **`button-secondary`** — White outline pill with yellow text.
- **`button-disabled`** — Soft gray with muted text.

### Cards & Containers
- **`card`** — White, `{rounded.xl}` (12px), barely-visible shadow
- **`card-data`** — Tighter `{rounded.md}` for trading data
- **`card-dark`** — On dark sections, `{colors.surface-dark-card}` fill
- **`card-hero`** — `{rounded.2xl}` (24px) for video/hero containers

### Inputs & Forms
**`input`** — Snow background, hairline border, `{rounded.md}` (8px), 0px × 12px padding (compact for trading context). Focus shifts border to black.

### Navigation
**`nav-bar`** — White, sticky, ~64px height. Yellow logo mark + dark wordmark left. Links 14px/600 in `{colors.text-secondary}`. Yellow pill "Get Started" CTA right.

### Trust Indicators
- Real-time crypto price ticker (BTC, BNB, SOL with green/red change)
- "Trusted by millions" section with stats on dark background
- Security badges and regulatory mentions
- QR code for direct app download in footer

## Do's and Don'ts

### Do
- Use Binance Yellow (`{colors.primary}`) exclusively for primary CTAs and brand accents — single point of color
- Keep light and dark sections strictly alternating for visual rhythm
- Use BinancePlex at weight 500+ for all interactive elements
- Apply `{rounded.pill}` (50px) radius to all primary CTA pill buttons — the signature shape
- Maintain `{rounded.xl}` (12px) on content cards for a polished but not overly rounded feel
- Show real-time data prominently — numbers build trust
- Use Slate (`{colors.text-muted}`) for all secondary/metadata text
- Keep shadows at 5% opacity or less

### Don't
- Don't introduce additional brand colors — Binance Yellow is the only accent; all other color is data-driven (green up, red down)
- Don't use rounded corners above 12px on content cards — only CTAs and video containers go higher
- Don't add heavy shadows or hover lift effects
- Don't use BinancePlex below weight 500 for headings
- Don't place yellow text on yellow backgrounds — always ensure high contrast
- Don't mix pill (50px) and square (6px) button styles in the same row
- Don't soften the dark sections — `{colors.surface-dark}` should feel authoritative
- Don't use decorative illustrations — imagery should be product screenshots or data visualizations
- Don't add animation beyond subtle 200ms transitions — financial platforms need stability
- Don't use colored backgrounds for semantic states in cards — keep cards white or dark, use text color

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <425px | Single column, stacked hero, hamburger nav |
| Small Mobile | 425-599px | Wider mobile layout, price ticker wraps |
| Tablet Small | 600-768px | 2-column feature grid begins |
| Tablet | 769-896px | Hero side-by-side layout begins |
| Desktop Small | 897-1024px | Full nav expands, 3-column features |
| Desktop | 1024-1280px | Full layout, max content width |
| Large Desktop | 1280-1440px | Increased margins, centered container |
| XL Desktop | >1440px | Max-width container (1200px) |

### Touch Targets
- Minimum touch target: 44x44px (WCAG AAA)
- Pill CTA buttons: 48px height minimum
- Nav links: 44px touch area
- Crypto ticker items: full-width tappable rows on mobile

### Collapsing Strategy
- **Navigation**: Full horizontal links → hamburger menu below 897px
- **Hero section**: Side-by-side → stacked at 768px
- **Feature grid**: 3-col → 2-col at 768px → 1-col at 600px
- **Price ticker**: Horizontal row → wrapping or scrollable at 600px
- **Section padding**: 64px → 48px → 32px → 16px as viewport narrows
- **Device mockups**: Scale down proportionally
- **Footer**: Multi-column → stacked accordion on mobile

### Image Behavior
- Device mockups: CSS-scaled with max-width constraints
- Hero imagery: contained within rounded containers (`{rounded.2xl}`)
- App screenshots: responsive width with fixed aspect ratio
- QR code: fixed 120px square, hidden on mobile

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Binance Yellow (`{colors.primary}`)
- Secondary CTA: Binance Gold (`{colors.primary-gold}`)
- Background Light: Pure White (`{colors.surface}`)
- Background Dark: Binance Dark (`{colors.surface-dark}`)
- Heading text: Ink (`{colors.ink}`)
- Body text: Slate (`{colors.text-muted}`)
- Border: Border Light (`{colors.border}`)
- Positive: Crypto Green (`{colors.success}`)
- Negative: Crypto Red (`{colors.error}`)

### Example Component Prompts
- "Create a hero section with white background, a 60px/700 bold headline in Ink (`{colors.ink}`), a 20px/500 subtitle in Slate (`{colors.text-muted}`), and a Binance Yellow (`{colors.primary}`) pill button (`{rounded.pill}`) with dark text (`{colors.ink}`)."
- "Design a crypto price ticker strip showing BTC, BNB, SOL prices in 14px/600 Ink with green (`{colors.success}`) or red (`{colors.error}`) percentage changes, on a white background with `{colors.border}` bottom border."
- "Build a feature card grid (3-column, 24px gap) with `{rounded.xl}` white cards, subtle shadow (`{colors.shadow-card}` tint), each containing a yellow (`{colors.primary}`) icon, 20px/600 heading, and 14px/500 `{colors.text-muted}` description."
- "Create a dark section (`{colors.surface-dark}`) with a 34px/700 white headline centered, and a 3-column feature grid using dark cards (`{colors.surface-dark-card}`) with `{rounded.xl}` and yellow accent icons."
- "Design a sticky navigation bar with white background, Binance logo left, 14px/600 `{colors.text-secondary}` nav links center, and a yellow (`{colors.primary}`) pill button (`{rounded.pill}`, 6px padding 32px) labeled 'Get Started' right."

### Iteration Guide
1. Focus on ONE component at a time
2. Reference specific color names and hex codes from this document
3. Remember: Binance Yellow is the ONLY accent color — everything else is grey/dark/white
4. Use the dark/light section alternation for visual pacing
5. Numbers and data should be prominent — this is a financial platform
6. Pill buttons (`{rounded.pill}`) for CTAs, regular buttons (`{rounded.sm}`) for form actions
7. Keep shadows almost invisible (5% opacity) — trust comes from clarity, not depth
8. BinancePlex at 600+ weight for any text that needs to feel authoritative
