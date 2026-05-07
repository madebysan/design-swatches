---
version: alpha
name: MiniMax
description: White-dominant AI product showcase. Multi-font system (DM Sans, Outfit, Poppins, Roboto), pill-button geometry, colorful product cards on a clean canvas, purple-tinted brand glow shadows.

colors:
  # Brand
  primary: "#1456f0"
  brand-blue: "#1456f0"
  sky-blue: "#3daeff"
  brand-pink: "#ea5ec1"
  brand-deep: "#17437d"

  # Blue scale
  primary-200: "#bfdbfe"
  primary-light: "#60a5fa"
  primary-500: "#3b82f6"
  primary-600: "#2563eb"
  primary-700: "#1d4ed8"

  # Text
  ink: "#222222"
  ink-dark: "#18181b"
  ink-charcoal: "#181e25"
  text-secondary: "#45515e"
  text-muted: "#8e8e93"
  text-helper: "#5f5f5f"

  # Surface
  background: "#ffffff"
  surface: "#ffffff"
  surface-light: "#f0f0f0"
  glass-white: "#fafafa"     # was hsla(0,0%,100%,0.4) — flattened approx
  border-light: "#f2f3f5"
  border: "#e5e7eb"

  # Inverted
  on-primary: "#ffffff"
  on-dark: "#cccccc"          # was rgba(255,255,255,0.8) — flattened over #181e25 approx

  # Semantic
  success-bg: "#e8ffea"

  # Shadow tints (opaque approximations)
  shadow-neutral: "#ebebeb"   # was rgba(0,0,0,0.08) — flattened
  shadow-brand: "#d6d2e6"     # was rgba(44,30,116,0.16) — flattened over white
  shadow-brand-soft: "#dedaeb" # was rgba(44,30,116,0.11) — flattened over white
  shadow-elevated: "#dadada"  # was rgba(36,36,36,0.08) — flattened

  # Subtle pill-nav tint (was rgba(0,0,0,0.05))
  nav-tint: "#f2f2f2"

typography:
  display-hero:
    fontFamily: "DM Sans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 80px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: 0px
  display-hero-outfit:
    fontFamily: "Outfit, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 80px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: 0px
  section-heading:
    fontFamily: "Outfit, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 31px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0px
  section-heading-alt:
    fontFamily: "Roboto, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 0.88
    letterSpacing: 0px
  card-title:
    fontFamily: "Outfit, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.71
    letterSpacing: 0px
  sub-heading:
    fontFamily: "Poppins, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  feature-label:
    fontFamily: "Poppins, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  body-large:
    fontFamily: "DM Sans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "DM Sans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-bold:
    fontFamily: "DM Sans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  nav-link:
    fontFamily: "DM Sans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  button-small:
    fontFamily: "DM Sans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0px
  caption:
    fontFamily: "DM Sans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0px
  small-label:
    fontFamily: "DM Sans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  micro:
    fontFamily: "DM Sans, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px

spacing:
  hairline: 1px
  micro: 2px
  xs: 4px
  xs-plus: 6px
  sm: 8px
  sm-plus: 10px
  button: 11px
  md: 14px
  md-plus: 16px
  lg: 24px
  xl: 32px
  2xl: 40px
  3xl: 50px
  4xl: 64px
  5xl: 80px

rounded:
  xs: 4px
  sm: 8px
  md: 13px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  pill: 9999px

components:
  # Buttons
  button-primary-dark:
    backgroundColor: "{colors.ink-charcoal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-small}"
    rounded: "{rounded.sm}"
    padding: 11px 20px
  button-pill-nav:
    backgroundColor: "{colors.nav-tint}"
    textColor: "{colors.ink-dark}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  button-pill-white:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-charcoal}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  button-secondary:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink}"
    typography: "{typography.button-small}"
    rounded: "{rounded.sm}"
    padding: 11px 20px

  # Product card — colorful gradient hero card
  card-product:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.card-title}"
    rounded: "{rounded.xl}"
    padding: 24px
  card-product-hero:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.card-title}"
    rounded: "{rounded.2xl}"
    padding: 24px

  # AI product card (compact matrix tile)
  card-ai-tile:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 16px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-dark}"
    typography: "{typography.nav-link}"
    padding: 16px 24px

  # Footer (dark)
  footer:
    backgroundColor: "{colors.ink-charcoal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: 64px 24px

  # Tag / badge
  badge:
    backgroundColor: "{colors.primary-200}"
    textColor: "{colors.primary-700}"
    typography: "{typography.small-label}"
    rounded: "{rounded.pill}"
    padding: 4px 10px

  # Input (inferred from generic UI conventions)
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
---

# MiniMax Design System

## Overview

MiniMax's website is a clean, product-showcase platform for a Chinese AI technology company that bridges consumer-friendly appeal with technical credibility. The design language is predominantly white-space-driven with a light, airy feel — pure white backgrounds (`{colors.background}`) dominate, letting colorful product cards and AI model illustrations serve as the visual anchors. The overall aesthetic sits at the intersection of Apple's product marketing clarity and a playful, rounded design language that makes AI technology feel approachable.

The typography system is notably multi-font: DM Sans serves as the primary UI workhorse, Outfit handles display headings with geometric elegance, Poppins appears for mid-tier headings, and Roboto handles data-heavy contexts. This variety reflects a brand in rapid growth — each font serves a distinct communicative purpose rather than competing for attention. The hero heading at 80px weight 500 in both DM Sans and Outfit with a tight 1.10 line-height creates a bold but not aggressive opening statement.

What makes MiniMax distinctive is its pill-button geometry (`{rounded.pill}` radius) for navigation and primary actions, combined with softer 8px–24px radiused cards for product showcases. The product cards themselves are richly colorful — vibrant gradients in pink, purple, orange, and blue — creating a "gallery of AI capabilities" feel. Against the white canvas, these colorful cards pop like app icons on a phone home screen, making each AI model/product feel like a self-contained creative tool.

**Key Characteristics:**
- White-dominant layout with colorful product card accents
- Multi-font system: DM Sans (UI), Outfit (display), Poppins (mid-tier), Roboto (data)
- Pill buttons (`{rounded.pill}`) for primary navigation and CTAs
- Generous rounded cards (`{rounded.xl}`–`{rounded.2xl}`) for product showcases
- Brand blue spectrum: from `{colors.brand-blue}` through `{colors.primary-500}` to `{colors.primary-light}`
- Brand pink (`{colors.brand-pink}`) as secondary accent
- Near-black text (`{colors.ink}`, `{colors.ink-dark}`) on white backgrounds
- Purple-tinted shadows creating subtle brand-colored depth
- Dark footer section (`{colors.ink-charcoal}`) with product/company links

## Colors

### Brand Primary
- **Brand Blue** (`{colors.brand-blue}`): `--brand-6`, primary brand identity color
- **Sky Blue** (`{colors.sky-blue}`): `--col-brand00`, lighter brand variant for accents
- **Brand Pink** (`{colors.brand-pink}`): `--col-brand02`, secondary brand accent

### Blue Scale (Primary)
- **Primary 200** (`{colors.primary-200}`): light blue backgrounds
- **Primary Light** (`{colors.primary-light}`): active states, highlights
- **Primary 500** (`{colors.primary-500}`): standard blue actions
- **Primary 600** (`{colors.primary-600}`): hover states
- **Primary 700** (`{colors.primary-700}`): pressed/active states
- **Brand Deep** (`{colors.brand-deep}`): deep blue for emphasis

### Text Colors
- **Near Black** (`{colors.ink}`): primary text
- **Dark** (`{colors.ink-dark}`): button text, headings
- **Charcoal** (`{colors.ink-charcoal}`): dark surface text, footer background
- **Dark Gray** (`{colors.text-secondary}`): secondary text
- **Mid Gray** (`{colors.text-muted}`): tertiary text, muted labels
- **Light Gray** (`{colors.text-helper}`): helper text

### Surface & Background
- **Pure White** (`{colors.surface}`): primary background
- **Light Gray** (`{colors.surface-light}`): secondary button backgrounds
- **Glass White** (`{colors.glass-white}`): frosted glass overlay (was `hsla(0, 0%, 100%, 0.4)`)
- **Border Light** (`{colors.border-light}`): subtle section dividers
- **Border Gray** (`{colors.border}`): component borders

### Semantic
- **Success Background** (`{colors.success-bg}`): positive state backgrounds

### Shadows
- **Standard** — `{colors.shadow-neutral}` at `0px 4px 6px`: default card shadow (was `rgba(0, 0, 0, 0.08)`)
- **Soft Glow** — `{colors.shadow-neutral}` at `0px 0px 22.576px`: ambient soft shadow
- **Brand Purple** — `{colors.shadow-brand}` at `0px 0px 15px`: brand-tinted glow (was `rgba(44, 30, 116, 0.16)`)
- **Brand Purple Offset** — `{colors.shadow-brand-soft}` at `6.5px 2px 17.5px`: directional brand glow
- **Card Elevation** — `{colors.shadow-elevated}` at `0px 12px 16px -4px`: lifted card shadow

## Typography

### Font Families
- **Primary UI**: `DM Sans`, with fallbacks: `Helvetica Neue, Helvetica, Arial`
- **Display**: `Outfit`, with fallbacks: `Helvetica Neue, Helvetica, Arial`
- **Mid-tier**: `Poppins`
- **Data/Technical**: `Roboto`, with fallbacks: `Helvetica Neue, Helvetica, Arial`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference each role via tokens.

| Token | Use |
|---|---|
| `display-hero` | Hero headlines (DM Sans variant) |
| `display-hero-outfit` | Hero headlines (Outfit variant) |
| `section-heading` | Feature section titles |
| `section-heading-alt` | Compact headers (Roboto/DM Sans, tight line-height) |
| `card-title` | Product card headings |
| `sub-heading` | Mid-tier headings |
| `feature-label` | Feature names |
| `body-large` | Emphasized body |
| `body` | Standard body text |
| `body-bold` | Strong emphasis |
| `nav-link` | Navigation, links |
| `button-small` | Compact buttons |
| `caption` | Metadata |
| `small-label` | Tags, badges |
| `micro` | Tiny annotations |

### Principles
- **Multi-font purpose**: DM Sans = UI workhorse (body, nav, buttons); Outfit = geometric display (headings, product names); Poppins = friendly mid-tier (sub-headings, features); Roboto = technical/data contexts.
- **Universal 1.50 line-height**: The overwhelming majority of text uses 1.50 line-height, creating a consistent reading rhythm regardless of font or size. Exceptions: display (1.10 tight) and some captions (1.70 relaxed).
- **Weight 500 as default emphasis**: Most headings use 500 (medium) rather than bold, creating a modern, approachable tone. 600 for section titles, 700 reserved for strong emphasis.
- **Compact hierarchy**: The size scale jumps from 80px display straight to 28–32px section, then 16–20px body — a deliberate compression that keeps the visual hierarchy feeling efficient.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is `{spacing.sm}` (8px).

### Grid & Container
- Max content width centered on page
- Product card grids: horizontal scroll or 3–4 column layout
- Full-width white sections with contained content
- Dark footer at full-width

### Whitespace Philosophy
- **Gallery spacing**: Products are presented like gallery items with generous white space between cards, letting each AI model breathe as its own showcase.
- **Section rhythm**: Large vertical gaps (`{spacing.4xl}`–`{spacing.5xl}`) between major sections create distinct "chapters" of content.
- **Card breathing**: Product cards use internal padding of `{spacing.md-plus}`–`{spacing.lg}` with ample whitespace around text.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | White background, text blocks |
| Subtle (Level 1) | `{colors.shadow-neutral}` `0 4px 6px` | Standard cards, containers |
| Ambient (Level 2) | `{colors.shadow-neutral}` `0 0 22.576px` | Soft glow around elements |
| Brand Glow (Level 3) | `{colors.shadow-brand}` `0 0 15px` | Featured product cards |
| Elevated (Level 4) | `{colors.shadow-elevated}` `0 12px 16px -4px` | Lifted cards, hover states |

**Shadow Philosophy**: MiniMax uses a distinctive purple-tinted shadow for featured elements, creating a subtle brand-color glow that connects the shadow system to the blue brand identity. Standard shadows use neutral black but at low opacity (~8%), keeping everything feeling light and airy. The directional shadow variant adds dimensional interest to hero product cards.

## Shapes

| Token | Value | Use |
|---|---|---|
| `xs` | 4px | Small tags, micro badges |
| `sm` | 8px | Buttons, small cards |
| `md` | 13px | Comfortable medium cards, panels |
| `lg` | 16px | Larger cards |
| `xl` | 20px | Large product cards |
| `2xl` | 24px | Hero product cards, major containers |
| `3xl` | 32px | Badge pills, rounded panels |
| `pill` | 9999px | Buttons, nav tabs |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (e.g. `{components.button-primary-dark}`, `{components.card-product}`) rather than reconstructing them.

### Buttons
- **`button-primary-dark`** — Charcoal pill-CTA, used for "Get Started" / "Learn More" actions.
- **`button-pill-nav`** — Subtle-tint pill, full radius, for nav tabs and filter toggles.
- **`button-pill-white`** — White pill for secondary nav and inactive tabs.
- **`button-secondary`** — Light-gray secondary action, smaller radius for utility tasks.

### Cards
- **`card-product`** — Standard product card with `{rounded.xl}` corners. Vibrant gradient backgrounds carry the brand color via the artwork, not the chrome.
- **`card-product-hero`** — Featured product card at `{rounded.2xl}`, paired with the `{colors.shadow-brand}` purple glow.
- **`card-ai-tile`** — Compact AI matrix tile, `{rounded.md}`, neutral shadow.

### Links
- **Primary**: `{colors.ink-dark}` or `{colors.ink-charcoal}`, underline on dark text
- **Secondary**: `{colors.text-muted}`, muted for less emphasis
- **On Dark**: `{colors.on-dark}` for footer and dark sections

### Navigation
- **`nav-bar`** — Clean horizontal nav on white. MiniMax logo left-aligned (red accent in logo). Pill-shaped active indicators (`{rounded.pill}`). "Login" text link, minimal right-side actions. Sticky header behavior.

### Footer
- **`footer`** — Dark surface (`{colors.ink-charcoal}`) at full width. Product/company links in `{colors.on-dark}`.

### Inputs
- **`input`** — White background, `{colors.border}` border, `{rounded.sm}` corners. Focus shifts to `{colors.primary-500}`.

### Badges
- **`badge`** — Pill-shaped tag with light-blue fill (`{colors.primary-200}`) and primary-700 text.

## Do's and Don'ts

### Do
- Use white as the dominant background — let product cards provide the color
- Apply pill radius (`{rounded.pill}`) for navigation tabs and toggle buttons
- Use generous border radius (`{rounded.xl}`–`{rounded.2xl}`) for product showcase cards
- Employ the purple-tinted shadow for featured/hero product cards
- Keep body text at DM Sans weight 400–500 — heavier weights for buttons only
- Use Outfit for display headings, DM Sans for everything functional
- Maintain the universal 1.50 line-height across body text
- Let colorful product illustrations/gradients serve as the primary visual interest

### Don't
- Don't add colored backgrounds to main content sections — white is structural
- Don't use sharp corners (0–4px radius) on product cards — the rounded aesthetic is core
- Don't apply the brand pink (`{colors.brand-pink}`) to text or buttons — it's for logo and decorative accents only
- Don't mix more than one display font per section (Outfit OR Poppins, not both)
- Don't use weight 700 for headings — 500–600 is the range, 700 is reserved for strong emphasis in body text
- Don't darken shadows beyond 0.16 opacity — the light, airy feel requires restraint
- Don't use Roboto for headings — it's the data/technical context font only

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Single column, stacked product cards, hamburger nav |
| Tablet | 768–1024px | 2-column product grids, condensed spacing |
| Desktop | >1024px | Full horizontal card layouts, expanded spacing |

### Collapsing Strategy
- Hero: 80px → responsive scaling to ~40px on mobile
- Product card grid: horizontal scroll → 2-column → single column stacked
- Navigation: horizontal → hamburger menu
- Footer: multi-column → stacked sections
- Spacing: 64–80px gaps → 32–40px on mobile

---

## Agent Prompt Guide

### Quick Color Reference
- Background: `#ffffff` (primary), `#181e25` (dark/footer)
- Text: `#222222` (primary), `#45515e` (secondary), `#8e8e93` (muted)
- Brand Blue: `#1456f0` (brand), `#3b82f6` (primary-500), `#2563eb` (hover)
- Brand Pink: `#ea5ec1` (accent only)
- Borders: `#e5e7eb`, `#f2f3f5`

### Example Component Prompts
- "Create a hero section on white background. Headline at 80px Outfit weight 500, line-height 1.10, near-black (#222222) text. Sub-text at 16px DM Sans weight 400, line-height 1.50, #45515e. Dark CTA button (#181e25, 8px radius, 11px 20px padding, white text)."
- "Design a product card grid: white cards with 20px border-radius, shadow rgba(44,30,116,0.16) 0px 0px 15px. Product name at 28px Outfit weight 600. Internal gradient background for the product illustration area."
- "Build navigation bar: white background, DM Sans 14px weight 500 for links, #18181b text. Pill-shaped active tab (9999px radius, rgba(0,0,0,0.05) background). MiniMax logo left-aligned."
- "Create an AI product matrix: 4-column grid of cards with 13px radius, subtle shadow rgba(0,0,0,0.08) 0px 4px 6px. Centered icon above product name in DM Sans 16px weight 500."
- "Design footer on dark (#181e25) background. Product links in DM Sans 14px, rgba(255,255,255,0.8). Multi-column layout."

### Iteration Guide
1. Start with white — color comes from product cards and illustrations only
2. Pill buttons (9999px) for nav/tabs, standard radius (8px) for CTA buttons
3. Purple-tinted shadows for featured cards, neutral shadows for everything else
4. DM Sans handles 70% of text — Outfit is display-only, Poppins is mid-tier only
5. Keep weights moderate (500–600 for headings) — the brand tone is confident but approachable
6. Large radius cards (20–24px) for products, smaller radius (8–13px) for UI elements
