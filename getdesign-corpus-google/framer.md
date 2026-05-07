---
version: alpha
name: Framer
description: Cinematic dark canvas for tool-obsessed designers — pure black void, GT Walsheim with extreme negative letter-spacing, Framer Blue accent, pill-shaped buttons, frosted glass surfaces, blue ring shadow containment.

colors:
  # Primary
  background: "#000000"
  ink: "#ffffff"
  primary: "#0099ff"           # Framer Blue
  on-primary: "#ffffff"

  # Secondary surfaces
  surface-elevated: "#090909"  # Near Black

  # Glass (opaque approximations of translucent overlays)
  glass-frosted: "#1a1a1a"     # opaque approx of rgba(255,255,255,0.10) over black — Google format requires hex
  glass-frosted-stronger: "#808080"  # opaque approx of rgba(255,255,255,0.50) over black

  # Text
  text-secondary: "#a6a6a6"    # Muted Silver
  text-muted: "#999999"         # opaque approx of rgba(255,255,255,0.60) over black

  # Accent variants
  primary-glow: "#001f33"       # opaque approx of rgba(0,153,255,0.15) over black
  link-default: "#0000ee"

  # Shadow / ring colors (standalone tokens)
  shadow-edge: "#1a1a1a"        # opaque approx of rgba(255,255,255,0.10) — top edge highlight
  shadow-ambient: "#000000"     # rgba(0,0,0,0.25) cast over black — keep as background
  ring-blue: "#001f33"

typography:
  display-hero:
    fontFamily: "GT Walsheim Framer Medium, GT Walsheim Medium, system-ui, sans-serif"
    fontSize: 110px
    fontWeight: 500
    lineHeight: 0.85
    letterSpacing: -5.5px
  section-display:
    fontFamily: "GT Walsheim Medium, system-ui, sans-serif"
    fontSize: 85px
    fontWeight: 500
    lineHeight: 0.95
    letterSpacing: -4.25px
  section-heading:
    fontFamily: "GT Walsheim Medium, system-ui, sans-serif"
    fontSize: 62px
    fontWeight: 500
    lineHeight: 1.00
    letterSpacing: -3.1px
  feature-heading:
    fontFamily: "GT Walsheim Medium, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.13
    letterSpacing: -1px
  accent-display:
    fontFamily: "Mona Sans, system-ui, sans-serif"
    fontSize: 61.5px
    fontWeight: 100
    lineHeight: 1.00
    letterSpacing: -3.1px
  card-title:
    fontFamily: "Inter Variable, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.01px
  feature-title:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: -0.8px
  sub-heading:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.8px
  body-large:
    fontFamily: "Inter Variable, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.01px
  body:
    fontFamily: "Inter Variable, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.01px
  nav-ui:
    fontFamily: "Inter Variable, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -0.15px
  body-readable:
    fontFamily: "Inter Framer Regular, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0px
  caption:
    fontFamily: "Inter Variable, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  label:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.60
    letterSpacing: 0px
  small-caption:
    fontFamily: "Inter Variable, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  micro-code:
    fontFamily: "Azeret Mono, ui-monospace, monospace"
    fontSize: 10.4px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0px
  badge:
    fontFamily: "Open Runde, Inter, system-ui, sans-serif"
    fontSize: 9px
    fontWeight: 600
    lineHeight: 1.11
    letterSpacing: 0px
  micro-uppercase:
    fontFamily: "Inter Variable, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 7px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: 0.21px

spacing:
  micro: 1px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 40px
  4xl: 56px
  5xl: 80px
  6xl: 120px

rounded:
  none: 0px
  micro: 1px
  xs: 5px
  sm: 8px
  md: 12px
  lg: 15px
  xl: 20px
  pill-small: 40px
  pill: 100px
  full: 9999px

components:
  button-frosted-pill:
    backgroundColor: "{colors.glass-frosted}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill-small}"
    padding: 10px 15px

  button-solid-white:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.background}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 10px 15px

  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill-small}"
    padding: 10px 15px
  button-ghost-hover:
    backgroundColor: "{colors.glass-frosted}"

  card-dark-surface:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px

  card-elevated:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px

  product-screenshot:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.sm}"
    padding: 0px

  input:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"

  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-ui}"
    padding: 16px 24px

  link:
    textColor: "{colors.primary}"
    typography: "{typography.body}"
    padding: 0px

  badge-tag:
    backgroundColor: "{colors.glass-frosted}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 8px
---

# Framer Design System

## Overview

Framer's website is a cinematic, tool-obsessed dark canvas that radiates the confidence of a design tool built by designers who worship craft. The entire experience is drenched in pure black — not a warm charcoal or a cozy dark gray, but an absolute void (`{colors.background}`) that makes every element, every screenshot, every typographic flourish feel like it's floating in deep space. This is a website that treats its own product UI as the hero art, embedding full-fidelity screenshots and interactive demos directly into the narrative flow.

The typography is the signature move: GT Walsheim with aggressively tight letter-spacing (as extreme as -5.5px on 110px display text) creates headlines that feel compressed, kinetic, almost spring-loaded — like words under pressure that might expand at any moment. The transition to Inter for body text is seamless, with extensive OpenType feature usage (`cv01`, `cv05`, `cv09`, `cv11`, `ss03`, `ss07`) that gives even small text a refined, custom feel. Framer Blue (`{colors.primary}`) is deployed sparingly but decisively — as link color, border accents, and subtle ring shadows — creating a cold, electric throughline against the warm-less black.

The overall effect is a nightclub for web designers: dark, precise, seductive, and unapologetically product-forward. Every section exists to showcase what the tool can do, with the website itself serving as proof of concept.

**Key Characteristics:**
- Pure black (`{colors.background}`) void canvas — absolute dark, not warm or gray-tinted
- GT Walsheim display font with extreme negative letter-spacing (-5.5px at 110px)
- Framer Blue (`{colors.primary}`) as the sole accent color — cold, electric, precise
- Pill-shaped buttons (`{rounded.pill-small}`–`{rounded.pill}`) — no sharp corners on interactive elements
- Product screenshots as hero art — the tool IS the marketing
- Frosted glass button variants using `{colors.glass-frosted}` on dark surfaces
- Extensive OpenType feature usage across Inter for refined micro-typography

## Colors

### Primary
- **Pure Black** (`{colors.background}`): Primary background, the void canvas that defines Framer's dark-first identity
- **Pure White** (`{colors.ink}`): Primary text color on dark surfaces, button text on accent backgrounds
- **Framer Blue** (`{colors.primary}`): Primary accent color — links, borders, ring shadows, interactive highlights

### Secondary & Accent
- **Muted Silver** (`{colors.text-secondary}`): Secondary text, subdued labels, dimmed descriptions on dark surfaces
- **Near Black** (`{colors.surface-elevated}`): Elevated dark surface, shadow ring color for subtle depth separation

### Surface & Background
- **Void Black** (`{colors.background}`): Page background, primary canvas
- **Frosted White** (`{colors.glass-frosted}`): Translucent button backgrounds, glass-effect surfaces on dark
- **Subtle White** (`{colors.glass-frosted-stronger}`): Slightly more opaque frosted elements for hover states

### Neutrals & Text
- **Pure White** (`{colors.ink}`): Heading text, high-emphasis body text
- **Muted Silver** (`{colors.text-secondary}`): Body text, descriptions, secondary information
- **Ghost White** (`{colors.text-muted}`): Tertiary text, placeholders on dark surfaces

### Semantic & Accent
- **Framer Blue** (`{colors.primary}`): Links, interactive borders, focus rings
- **Blue Glow** (`{colors.primary-glow}`): Focus ring shadow, subtle blue halo around interactive elements
- **Default Link Blue** (`{colors.link-default}`): Standard browser link color (used sparingly in content areas)
- **Ring Blue** (`{colors.ring-blue}`): Card-border ring shadow color

### Gradient System
- No prominent gradient usage — Framer relies on pure flat black surfaces with occasional blue-tinted glows for depth
- Subtle radial glow effects behind product screenshots using Framer Blue at very low opacity

### Shadow Tokens
- **Edge highlight** (`{colors.shadow-edge}`): Top-edge subtle white highlight on elevated cards
- **Ambient** (`{colors.shadow-ambient}`): Deep ambient shadow color (black) at large blur

## Typography

### Font Family
- **Display**: `GT Walsheim Framer Medium` / `GT Walsheim Medium` — custom geometric sans-serif, weight 500
- **Body/UI**: `Inter Variable` / `Inter` — variable sans-serif with extensive OpenType features
- **Accent**: `Mona Sans` — GitHub's open-source font, used for select elements at ultra-light weight (100)
- **Monospace**: `Azeret Mono` — companion mono for code and technical labels
- **Rounded**: `Open Runde` — small rounded companion font for micro-labels

### Hierarchy

| Token | Use |
|---|---|
| `display-hero` | 110px GT Walsheim 500, -5.5px tracking — extreme negative tracking, compressed impact |
| `section-display` | 85px weight 500, -4.25px tracking |
| `section-heading` | 62px weight 500, -3.1px tracking |
| `feature-heading` | 32px weight 500, -1px tracking |
| `accent-display` | 61.5px Mona Sans weight 100 — ultra-light, ethereal |
| `card-title` | 24px Inter Variable 400 |
| `feature-title` | 22px Inter 700, -0.8px tracking |
| `sub-heading` | 20px Inter 600 |
| `body-large` | 18px Inter Variable 400 |
| `body` | 15px Inter Variable 400 |
| `nav-ui` | 15px Inter Variable, line-height 1.0 |
| `body-readable` | 14px Inter Framer Regular, 1.60 line-height — long-form body |
| `caption` | 14px Inter Variable 400 |
| `label` | 13px Inter 500 |
| `small-caption` | 12px Inter Variable 400 |
| `micro-code` | 10.4px Azeret Mono 400 |
| `badge` | 9px Open Runde 600 |
| `micro-uppercase` | 7px Inter Variable, uppercase, 0.21px tracking |

### Principles
- **Compression as personality**: GT Walsheim's extreme negative letter-spacing (-5.5px at 110px) is the defining typographic gesture — headlines feel spring-loaded, urgent, almost breathless
- **OpenType maximalism**: Inter is deployed with 6+ OpenType features simultaneously
- **Weight restraint on display**: All GT Walsheim usage is weight 500 (medium) — never bold, never regular
- **Ultra-tight line heights**: Display text at 0.85 line-height means letters nearly overlap vertically — intentional density that rewards reading at arm's length

## Layout

### Spacing System
Base unit is **8px**. Scale lives in YAML — `micro` (1px) through `6xl` (120px). Section padding: large vertical spacing (80px–120px between sections). Card padding: 15px–30px internal. Component gaps: 8px–20px between related elements.

### Grid & Container
- Max width: ~1200px container, centered
- Column patterns: Full-width hero, 2-column feature sections, single-column product showcases
- Asymmetric layouts: Feature sections often pair text (40%) with screenshot (60%)

### Whitespace Philosophy
- **Breathe through darkness**: Generous vertical spacing between sections — the black background means whitespace manifests as void, creating dramatic pauses between content blocks
- **Dense within, spacious between**: Individual components are tightly composed (tight line-heights, compressed text) but float in generous surrounding space
- **Product-first density**: Screenshot areas are allowed to be dense and information-rich, contrasting with the sparse marketing text

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 (Flat) | No shadow, pure black surface | Page background, empty areas |
| Level 1 (Ring) | 1px Framer Blue glow ring at low alpha | Card borders, interactive element outlines |
| Level 2 (Contained) | Near-black ring on dark surfaces | Subtle containment |
| Level 3 (Floating) | Top-edge white highlight + deep ambient shadow | Elevated cards, floating elements |

### Shadow Philosophy
Framer's elevation system is inverted from traditional light-theme designs. Instead of darker shadows on light backgrounds, Framer uses:
- **Blue-tinted ring shadows** at very low opacity (using `{colors.primary-glow}`) for containment — a signature move that subtly brands every bordered element
- **White edge highlights** (0.5px) on the top edge of elevated elements — simulating light hitting the top surface
- **Deep ambient shadows** for true floating elements

### Decorative Depth
- **Blue glow auras**: Subtle Framer Blue radial gradients behind key interactive areas
- **No background blur/glassmorphism**: Despite the frosted button effect, there's no heavy glass blur usage — the translucency is achieved through simple rgba opacity

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `micro` | 1px | Nearly squared precision edges |
| `xs` | 5px | Small UI elements, image thumbnails |
| `sm` | 8px | Standard component radius — code blocks, screenshots |
| `md` | 12px | Cards, product screenshots — comfortably rounded |
| `lg` | 15px | Large containers, feature cards |
| `xl` | 20px | Generously rounded cards |
| `pill-small` | 40px | Navigation pills, frosted buttons |
| `pill` | 100px | Full pill — primary CTAs, tag elements |
| `full` | 9999px | Tag chips, fully circular |

## Components

The complete component spec lives in YAML.

### Buttons
- **`button-frosted-pill`** — Frosted glass on dark surface, pill radius. Translucent, ambient, subtle.
- **`button-solid-white`** — Solid white pill, black text. Primary CTA — clean, high-contrast on dark.
- **`button-ghost`** — No visible background; hover reveals frosted background.

### Cards
- **`card-dark-surface`** — Near-black bg with blue ring shadow border.
- **`card-elevated`** — Multi-layer shadow with subtle white top highlight + deep ambient.

### Screenshots
- **`product-screenshot`** — Full-width or padded within dark containers, 8px–12px radius for software UI previews.

### Inputs
- **`input`** / **`input-focus`** — Dark background, subtle border, white text. Focus state: Framer Blue ring border.

### Navigation
- **`nav-bar`** — Dark floating nav bar with white Inter text links and pill CTAs.

### Links / Badges
- **`link`** — Inline text in `{colors.primary}`.
- **`badge-tag`** — Frosted small pill in `{rounded.full}` with `{typography.badge}` Open Runde 9px 600.

## Do's and Don'ts

### Do
- Use pure black (`{colors.background}`) as the primary background — not dark gray, not charcoal
- Apply extreme negative letter-spacing on GT Walsheim display text (-3px to -5.5px)
- Keep all buttons pill-shaped (`{rounded.pill-small}`+ radius) — never use squared or slightly-rounded buttons
- Use Framer Blue (`{colors.primary}`) exclusively for interactive accents — links, borders, focus states
- Deploy `{colors.glass-frosted}` for frosted glass surfaces on dark backgrounds
- Maintain GT Walsheim at weight 500 only — the medium weight IS the brand
- Use extensive OpenType features on Inter text (cv01, cv05, cv09, cv11, ss03, ss07)
- Let product screenshots be the visual centerpiece — the tool markets itself
- Apply blue ring shadows for card containment

### Don't
- Use warm dark backgrounds (no `#1a1a1a`, `#2d2d2d`, or brownish blacks)
- Apply bold (700+) weight to GT Walsheim display text — medium 500 only
- Introduce additional accent colors beyond Framer Blue — this is a one-accent-color system
- Use large border-radius on non-interactive elements (cards use 10px–15px, only buttons get 40px+)
- Add decorative imagery, illustrations, or icons — the product IS the illustration
- Use positive letter-spacing on headlines — everything is compressed, negative tracking
- Create heavy drop shadows — depth is communicated through subtle rings and minimal ambients
- Place light/white backgrounds behind content sections — the void is sacred
- Use serif or display-weight fonts — the system is geometric sans-serif only

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <809px | Single column, stacked feature sections, reduced hero text (62px→40px), hamburger nav |
| Tablet | 809px–1199px | 2-column features begin, nav links partially visible, screenshots scale down |
| Desktop | >1199px | Full layout, expanded nav with all links + CTA, 110px display hero, side-by-side features |

### Touch Targets
- Pill buttons: minimum 40px height with 10px vertical padding — exceeds 44px WCAG minimum
- Nav links: 15px text with generous padding for touch accessibility
- Mobile CTA buttons: Full-width pills on mobile for easy thumb reach

### Collapsing Strategy
- **Navigation**: Full horizontal nav → hamburger menu at mobile breakpoint
- **Hero text**: 110px display → 85px → 62px → ~40px across breakpoints, maintaining extreme negative tracking proportionally
- **Feature sections**: Side-by-side (text + screenshot) → stacked vertically on mobile
- **Product screenshots**: Scale responsively within containers, maintaining aspect ratios
- **Section spacing**: Reduces proportionally — 120px desktop → 60px mobile

### Image Behavior
- Product screenshots are responsive, scaling within their container boundaries
- No art direction changes — same crops across breakpoints
- Dark background ensures screenshots maintain visual impact at any size
- Screenshots lazy-load as user scrolls into view

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Background: Void Black (`{colors.background}`)
- Primary Text: Pure White (`{colors.ink}`)
- Accent/CTA: Framer Blue (`{colors.primary}`)
- Secondary Text: Muted Silver (`{colors.text-secondary}`)
- Frosted Surface: Translucent White (`{colors.glass-frosted}`)
- Elevation Ring: Blue Glow (`{colors.primary-glow}`)

### Example Component Prompts
- "Create a hero section on pure black background with 110px GT Walsheim heading in white, letter-spacing -5.5px, line-height 0.85, and a pill-shaped white CTA button (`{rounded.pill}`) with black text"
- "Design a feature card on black background with a 1px Framer Blue ring shadow border, `{rounded.md}` border-radius, white heading in Inter at 22px weight 700, and muted silver `{colors.text-secondary}` body text"
- "Build a navigation bar with black background, white Inter text links at 15px, and a frosted pill button (`{colors.glass-frosted}` background, `{rounded.pill-small}` radius) as the CTA"
- "Create a product showcase section with a full-width screenshot embedded on black, `{rounded.sm}` border-radius, subtle multi-layer shadow (white top highlight + ambient)"
- "Design a pricing card using pure black surface, Framer Blue (`{colors.primary}`) accent for the selected plan border, white text hierarchy (24px Inter bold heading, 14px regular body), and a solid white pill CTA button"

### Iteration Guide
When refining existing screens generated with this design system:
1. Focus on ONE component at a time — the dark canvas makes each element precious
2. Always verify letter-spacing on GT Walsheim headings — the extreme negative tracking is non-negotiable
3. Check that Framer Blue appears ONLY on interactive elements — never as decorative background or text color for non-links
4. Ensure all buttons are pill-shaped — any squared corner immediately breaks the Framer aesthetic
5. Test frosted glass surfaces by checking they have exactly the right opacity — too opaque looks like a bug, too transparent disappears
