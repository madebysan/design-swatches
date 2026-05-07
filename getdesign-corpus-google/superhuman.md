---
version: alpha
name: Superhuman
description: Luxury productivity surface — predominantly white canvas with a single cinematic deep-purple gradient hero, Super Sans VF on non-standard weight stops (460/540), warm-cream CTAs, and binary 8/16px radius system.

colors:
  # Canvas / surfaces
  background: "#ffffff"
  surface: "#ffffff"
  surface-cream: "#e9e5dd"

  # Hero / brand dark
  brand-dark: "#1b1938"

  # Brand accent — Lavender Glow
  primary: "#cbb7fb"
  on-primary: "#292827"

  # Ink
  ink: "#292827"
  ink-on-dark: "#f5f5f5"  # opaque approx of rgba(255,255,255,0.95) — Google format requires hex
  ink-on-dark-soft: "#cccccc"  # opaque approx of rgba(255,255,255,0.8) — Google format requires hex
  link: "#714cb6"

  # Borders
  border: "#dcd7d3"
  border-dark: "#292827"
  border-on-dark: "#5e5b78"  # opaque approx of rgba(255,255,255,0.2) over brand-dark — Google format requires hex

typography:
  display-hero:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 64px
    fontWeight: 540
    lineHeight: 0.96
    letterSpacing: 0px
  section-display:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 460
    lineHeight: 0.96
    letterSpacing: -1.32px
  section-heading:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 460
    lineHeight: 0.96
    letterSpacing: 0px
  feature-title:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 540
    lineHeight: 1.14
    letterSpacing: -0.63px
  sub-heading-large:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 26px
    fontWeight: 460
    lineHeight: 1.3
    letterSpacing: 0px
  card-heading:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 460
    lineHeight: 0.96
    letterSpacing: -0.315px
  body-heading:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 460
    lineHeight: 1.2
    letterSpacing: 0px
  emphasis-body:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 540
    lineHeight: 1.5
    letterSpacing: -0.135px
  body:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 460
    lineHeight: 1.5
    letterSpacing: 0px
  button-bold:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0px
  button-semi:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  nav-link:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 460
    lineHeight: 1.2
    letterSpacing: 0px
  caption:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.315px
  caption-semi:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0px
  caption-body:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 460
    lineHeight: 1.5
    letterSpacing: 0px
  micro-label:
    fontFamily: "Super Sans VF, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px

spacing:
  micro: 2px
  xxs: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 48px
  5xl: 64px
  6xl: 80px

rounded:
  none: 0px
  sm: 8px
  lg: 16px

components:
  # Warm Cream primary CTA
  button-primary:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.button-bold}"
    rounded: "{rounded.sm}"
    padding: 12px 24px

  # Dark inverse CTA
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    typography: "{typography.button-bold}"
    rounded: "{rounded.sm}"
    padding: 12px 24px

  # Ghost / text link button
  button-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.link}"
    typography: "{typography.button-semi}"
    rounded: "{rounded.sm}"
    padding: 12px 24px

  # Hero CTA — Warm Cream over the purple gradient
  button-hero:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.button-bold}"
    rounded: "{rounded.sm}"
    padding: 12px 24px

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-dark:
    backgroundColor: "{colors.brand-dark}"
    textColor: "{colors.ink-on-dark}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-hero:
    backgroundColor: "{colors.brand-dark}"
    textColor: "{colors.ink-on-dark}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Inputs
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.link}"

  # Lavender accent badge
  badge-lavender:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
---

# Superhuman Design System

## Overview

Superhuman's website feels like opening a luxury envelope — predominantly white, immaculately clean, with a single dramatic gesture of color that commands attention. The hero section is a cinematic purple gradient, a deep twilight wash of `{colors.brand-dark}` that evokes the moment just before dawn, overlaid with confident white typography. Below this dramatic entrance, the rest of the site is almost entirely white canvas with dark charcoal text, creating a stark but refined reading experience.

The typography is the true signature: Super Sans VF, a custom variable font with unconventional weight stops (460, 540, 600, 700) that sit between traditional font weight categories. Weight 460 — slightly heavier than regular but lighter than medium — is the workhorse, creating text that feels more confident than typical 400-weight but never aggressive. The tight line-heights (`0.96` on display text) compress headlines into dense, powerful blocks, while generous `1.50` line-height on body text provides airy readability. This tension between compressed power and breathing room defines the Superhuman typographic voice.

The design philosophy is maximum confidence through minimum decoration. Warm cream buttons (`{colors.surface-cream}`) instead of bright CTAs, a near-absence of borders and shadows, and lavender purple (`{colors.primary}`) as the sole accent color. It's a productivity tool that markets itself like a luxury brand — every pixel earns its place, nothing is merely decorative. The brand naming convention extends to colors: the primary purple is called "Mysteria," straddling blue and purple with deliberate ambiguity.

**Key Characteristics:**
- Deep purple gradient hero (`{colors.brand-dark}`) contrasting against a predominantly white content body
- Super Sans VF variable font with non-standard weight stops (460, 540, 600, 700)
- Ultra-tight display line-height (`0.96`) creating compressed, powerful headlines
- Warm Cream (`{colors.surface-cream}`) buttons instead of bright/saturated CTAs — understated luxury
- Lavender Purple (`{colors.primary}`) as the singular accent color
- Minimal border-radius scale: only `{rounded.sm}` (8px) and `{rounded.lg}` (16px) — no micro-rounding, no pill shapes
- Product screenshots dominate the content — the UI sells itself with minimal surrounding decoration

## Colors

### Primary
- **Mysteria Purple** (`{colors.brand-dark}`): Hero gradient background, deep purple that straddles blue-purple — the darkest expression of the brand.
- **Lavender Glow** (`{colors.primary}`): Primary accent and highlight color — soft purple used for emphasis, decorative elements, and interactive highlights.
- **Charcoal Ink** (`{colors.ink}`): Primary text and heading color on light surfaces — warm near-black with faint brown undertone.

### Secondary & Accent
- **Amethyst Link** (`{colors.link}`): Underlined link text — mid-range purple connecting to the brand palette while signaling interactivity.
- **Translucent White** (`{colors.ink-on-dark}`): Hero overlay text — opaque approximation of `rgba(255,255,255,0.95)`.
- **Misted White** (`{colors.ink-on-dark-soft}`): Secondary text on dark surfaces — opaque approximation of `rgba(255,255,255,0.8)`.

### Surface & Background
- **Pure White** (`{colors.background}`): Primary page background — the dominant canvas color for all content sections.
- **Warm Cream** (`{colors.surface-cream}`): Button background — a warm, neutral cream that avoids the coldness of pure gray.
- **Parchment Border** (`{colors.border}`): Card and divider borders — warm light gray with slight pink undertone.

### Neutrals & Text
- **Charcoal Ink** (`{colors.ink}`): Primary heading and body text on white surfaces.
- **Amethyst Link** (`{colors.link}`): In-content links with underline decoration.
- **Translucent White 95%** (`{colors.ink-on-dark}`): Primary text on dark/purple surfaces.
- **Translucent White 80%** (`{colors.ink-on-dark-soft}`): Secondary text on dark/purple surfaces.

### Semantic
Superhuman operates with extreme color restraint — Lavender Glow (`{colors.primary}`) is the only true accent. Interactive states are communicated through opacity shifts and underline decorations rather than color changes. The warm cream button palette avoids any saturated semantic colors.

### Gradient System
- **Hero Gradient**: Deep purple gradient starting from `{colors.brand-dark}`, transitioning through purple-to-twilight tones across the hero section.
- **Content Transition**: The gradient dissolves into the white content area, creating a cinematic curtain-lift effect as the user scrolls.
- No other gradients on the marketing site — the hero gradient is a singular dramatic gesture.

## Typography

### Font Family
- **Display & Body**: `Super Sans VF` — custom variable font with non-standard weight axis. Fallback: `system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue`
- **Product UI** (referenced in brand): `Messina Sans / Messina Serif / Messina Mono` — used in the product itself.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`).

| Token | Use |
|---|---|
| `display-hero` | 64px / weight 540 / 0.96 line-height — powerful block headlines |
| `section-display` | 48px / weight 460 with `-1.32px` tracking |
| `section-heading` | 48px / weight 460 (alternate without tracking) |
| `feature-title` | 28px / weight 540 / `-0.63px` |
| `sub-heading-large` | 26px / weight 460 |
| `card-heading` | 22px / weight 460 / 0.96 line-height (extreme compression) |
| `body-heading`, `emphasis-body` | 18–20px content intros |
| `body` | Standard reading text (16px / 1.50 line-height) |
| `button-bold`, `button-semi` | 16px UI text at 700 / 600 |
| `nav-link` | Navigation items |
| `caption`, `caption-semi`, `caption-body` | Small metadata variants |
| `micro-label` | 12px bold tags and badges |

### Principles
- **Non-standard weight axis**: Weights 460 and 540 are deliberately between conventional Regular (400) and Medium (500), creating subtly "off"-feeling typography that's slightly heavier than expected.
- **Extreme display compression**: Display headlines at 0.96 line-height collapse lines nearly on top of each other.
- **Body generosity**: Body text at 1.50 line-height is extremely spacious, ensuring comfortable reading after dense headline impact.
- **Selective negative tracking**: Letter-spacing applied surgically — `-1.32px` on 48px headings, `-0.63px` on 28px features, but `0px` on body.
- **Variable font efficiency**: A single font file serves all weight variations.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

Section padding is `4xl`–`6xl` (48–80px), card padding `lg`–`3xl`, and component gaps `sm`–`lg`.

### Grid & Container
- Max width: ~1200px content container, centered
- Column patterns: full-width hero, centered single-column for key messaging, 2–3 column grid for feature cards
- Feature grid: even column distribution for "Your Superhuman suite" product showcase

### Whitespace Philosophy
- **Confident emptiness**: Generous whitespace between sections signals premium positioning.
- **Product as content**: Large product screenshots fill space that lesser sites would fill with marketing copy.
- **Progressive density**: The hero is spacious and cinematic, content sections become denser with feature grids, then opens up again for CTAs.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 (Flat) | No shadow, white background | Primary page canvas, most content surfaces |
| Level 1 (Border) | `1px solid {colors.border}` | Card containment, section dividers |
| Level 2 (Dark Border) | `1px solid {colors.border-dark}` | Header elements, dark section separators |
| Level 3 (Glow) | Subtle shadow | Product screenshot containers, elevated cards |
| Level 4 (Hero Depth) | `1px solid {colors.border-on-dark}` | Elements on the dark purple gradient hero |

### Shadow Philosophy
Superhuman's elevation system is remarkably restrained. Depth is primarily communicated through:
- **Border containment**: Warm-toned borders (`{colors.border}`) at 1px create gentle separation
- **Color contrast**: The hero gradient creates massive depth through color shift rather than shadows
- **Product screenshots**: Screenshots themselves create depth by showing a layered UI within the flat page
- **Opacity layering**: Semi-transparent whites on the hero gradient create atmospheric depth layers

### Decorative Depth
- **Hero gradient**: The `{colors.brand-dark}` → white gradient transition is the primary depth device
- **Lavender accents**: Lavender Glow elements float above the dark gradient
- **No glassmorphism**: Despite the translucent borders, no blur/frosted-glass effects
- **Photography depth**: The hero silhouette image creates natural atmospheric depth

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Inline rules, full-bleed surfaces |
| `sm` | 8px | Buttons, inline elements — the universal small radius |
| `lg` | 16px | Cards, larger containers — the universal large radius |

Only two radii in the entire system — radical simplicity. No micro-rounding, no pill shapes.

## Components

The complete component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card}`).

### Buttons
- **`button-primary`** — Warm Cream signature CTA with Charcoal Ink text and `{rounded.sm}` corners. Warm, muted, luxurious.
- **`button-dark`** — Inverse Charcoal CTA with white text — for contrast sections.
- **`button-ghost`** — No background, underline decoration, Amethyst Link color.
- **`button-hero`** — Warm Cream over the dark purple gradient — pops dramatically against `{colors.brand-dark}`.

### Cards & Containers
- **`card`** — White background, `1px solid {colors.border}` border, `{rounded.lg}` corners — clean and minimal.
- **`card-dark`** — Charcoal-bordered surface for dark sections.
- **`card-hero`** — Semi-transparent white border (`{colors.border-on-dark}`) on purple gradient — ghostly containment.
- Product screenshot cards: large product UI images with clean edges, minimal framing.

### Inputs & Forms
- **`input`** — Minimal form presence on the marketing site. Charcoal-bordered inputs with warm-toned placeholder text. Focus shifts border from `{colors.border}` to `{colors.border-dark}`.

### Navigation
- **`nav-bar`** — Clean white background on content, transparent on hero gradient. Super Sans VF 16px weight 460/600. Warm Cream CTA pill in the nav. Sticky behavior. Mobile collapses to hamburger.

### Image Treatment
- Product screenshots: large, dominant product UI showing the email interface
- Lifestyle photography: a single dramatic image (silhouette against purple/red gradient) in the hero
- Full-width presentation: screenshots span full container width with subtle shadow or no border
- Wide landscape ratios (~16:9) for product screenshots

## Do's and Don'ts

### Do
- Use Super Sans VF at weight 460 as the default — slightly heavier than regular is the brand signature
- Keep display headlines at 0.96 line-height — the compression is intentional and powerful
- Use Warm Cream (`{colors.surface-cream}`) for primary buttons — not white, not gray, specifically warm cream
- Limit border-radius to `{rounded.sm}` (8px) and `{rounded.lg}` (16px) — the binary radius system is deliberate
- Apply negative letter-spacing on headlines only (`-0.63px` to `-1.32px`) — body text stays at 0px
- Use Lavender Glow (`{colors.primary}`) as the only accent color
- Let product screenshots be the primary visual content — the UI sells itself
- Maintain the dramatic hero gradient as a singular gesture — the rest of the page is white

### Don't
- Don't use conventional font weights (400, 500, 600) — Superhuman's 460 and 540 are deliberately between standard stops
- Don't add bright or saturated CTA colors — buttons are intentionally muted in Warm Cream or Charcoal
- Don't introduce additional accent colors beyond Lavender Glow
- Don't apply shadows generously — depth comes from borders, color contrast, and photography
- Don't use tight line-height on body text — display is compressed (0.96) but body is generous (1.50)
- Don't add decorative elements, icons, or illustrations
- Don't create pill-shaped buttons — the system uses `{rounded.sm}` (8px), not rounded pills
- Don't use pure black for text — `{colors.ink}` is warmer and softer

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Single column, hero text reduces to ~36px, stacked feature cards, hamburger nav |
| Tablet | 768px–1024px | 2-column feature grid begins, hero text ~48px, nav partially visible |
| Desktop | 1024px–1440px | Full layout, 64px hero display, multi-column feature grid, full nav |
| Large Desktop | >1440px | Max-width container centered, generous side margins |

### Touch Targets
- Buttons: `{rounded.sm}` with comfortable padding — meets touch target guidelines
- Nav links: 16px text with adequate surrounding padding
- Mobile CTAs: full-width Warm Cream buttons for easy thumb reach
- Links: underline decoration provides clear tap affordance

### Collapsing Strategy
- **Navigation**: Full horizontal nav → hamburger menu on mobile
- **Hero text**: 64px display → 48px → ~36px across breakpoints
- **Feature grid**: Multi-column product showcase → 2-column → single stacked column
- **Product screenshots**: Scale within containers, maintaining landscape ratios
- **Section spacing**: Reduces proportionally — generous desktop margins compress on mobile

### Image Behavior
- Product screenshots scale responsively while maintaining aspect ratios
- Hero silhouette image crops or scales — maintains dramatic composition
- No art direction changes — same compositions across all breakpoints
- Lazy loading likely on below-fold product screenshots

---

## Agent Prompt Guide

### Quick Color Reference
- Hero Background: Mysteria Purple (`{colors.brand-dark}`)
- Primary Text (light bg): Charcoal Ink (`{colors.ink}`)
- Primary Text (dark bg): Translucent White (`{colors.ink-on-dark}`)
- Accent: Lavender Glow (`{colors.primary}`)
- Button Background: Warm Cream (`{colors.surface-cream}`)
- Border: Parchment Border (`{colors.border}`)
- Link: Amethyst Link (`{colors.link}`)
- Page Background: Pure White (`{colors.background}`)

### Example Component Prompts
- "Create a hero section with deep purple gradient background (`{colors.brand-dark}`), 64px Super Sans heading at weight 540, line-height 0.96, white text at 95% opacity, and a warm cream button (`{colors.surface-cream}`, 8px radius, `{colors.ink}` text)."
- "Design a feature card with white background, 1px `{colors.border}` border, 16px radius, 20px Super Sans heading at weight 460, and 16px body text at weight 460 with 1.50 line-height in `{colors.ink}`."
- "Build a navigation bar with white background, Super Sans links at 16px weight 460, a warm cream CTA button (`{colors.surface-cream}`, 8px radius), sticky positioning."
- "Create a product showcase section with centered 48px heading (weight 460, -1.32px letter-spacing, `{colors.ink}`), a large product screenshot below, on white background."
- "Design an accent badge using Lavender Glow (`{colors.primary}`) background, 8px radius, 12px bold text (weight 700), for category labels."

### Iteration Guide
1. Verify font weight is 460 (not 400 or 500) for body and 540 for display — non-standard weights are essential
2. Check that display line-height is 0.96 — if headlines look too spaced, they're wrong
3. Ensure buttons use Warm Cream (`{colors.surface-cream}`) not pure white or gray — the warmth is subtle but critical
4. Confirm the only accent color is Lavender Glow (`{colors.primary}`) — no other hues should appear
5. The overall tone should feel like a luxury product presentation — minimal, confident, with one dramatic color gesture in the hero
