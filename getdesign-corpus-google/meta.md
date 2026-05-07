---
version: alpha
name: Meta Store
description: Photography-first retail design for Meta hardware. Pill-shaped Meta Blue CTAs, Optimistic VF typography with ss01/ss02, binary white/dark surfaces, gallery-grade whitespace.

colors:
  # Brand primary
  primary: "#0064e0"
  primary-hover: "#0143b5"
  primary-pressed: "#004bb9"
  primary-light: "#47a5fa"
  facebook-blue: "#1877f2"
  link-blue: "#385898"

  # Product-line accents
  rayban-red: "#d6311f"
  oculus-purple: "#a121ce"
  work-purple: "#6441d2"
  portal-blue: "#1b365d"
  portal-hero-blue: "#c8e4e8"
  portal-light-blue: "#add4e0"

  # Surface & background
  background: "#ffffff"
  surface: "#ffffff"
  soft-gray: "#f1f4f7"
  warm-gray: "#f7f8fa"
  web-wash: "#f0f2f5"
  linen: "#f2f0e6"
  baby-blue: "#e8f3ff"
  near-black: "#1c1e21"
  oculus-light: "#181a1b"
  oculus-dark: "#000000"
  overlay: "#666666"   # was rgba(0,0,0,0.6) — flattened approx

  # Text & ink
  ink: "#050505"
  ink-charcoal: "#1c2b33"
  icon-secondary: "#465a69"
  text-secondary: "#65676b"
  text-slate: "#5d6c7b"
  section-header: "#4b4c4f"
  button-text: "#444950"
  text-disabled: "#bcc0c4"
  cta-disabled-text: "#8595a4"
  divider: "#ced0d4"
  divider-gray: "#dee3e9"
  cta-border: "#cbd2d9"
  border-strong: "#909396"

  # Inverted text
  on-primary: "#ffffff"
  on-dark: "#ffffff"

  # Semantic
  success: "#31a24c"
  store-success: "#007d1e"
  error: "#e41e3f"
  store-error: "#c80a28"
  warning: "#f7b928"
  positive-bg: "#dcf7d2"     # was rgba(36,228,0,0.15) — flattened over white
  error-bg: "#ffe4e9"        # was rgba(255,123,145,0.15) — flattened over white
  warning-bg: "#fff8cc"      # was rgba(255,226,0,0.15) — flattened over white
  info-bg: "#d9eeff"         # was rgba(0,145,255,0.15) — flattened over white

  # Base spectrum (FDS)
  cherry: "#f3425f"
  grape: "#9360f7"
  lime: "#45bd62"
  seafoam: "#54c7ec"
  teal: "#2abba7"
  tomato: "#fb724b"
  pink: "#ff66bf"

  # Outlined-button border (opaque approx of rgba(10,19,23,0.12))
  outline-soft: "#dee0e2"
  # Frosted nav (opaque approx of rgba(241,244,247,0.8))
  nav-frosted: "#f4f6f9"

typography:
  display-1:
    fontFamily: "Optimistic VF, Montserrat, Helvetica, Arial, sans-serif"
    fontSize: 64px
    fontWeight: 500
    lineHeight: 1.16
    letterSpacing: 0px
    fontFeature: "ss01, ss02"
  display-2:
    fontFamily: "Optimistic VF, Montserrat, Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.17
    letterSpacing: 0px
    fontFeature: "ss01, ss02"
  heading-1:
    fontFamily: "Optimistic VF, Montserrat, Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.28
    letterSpacing: 0px
  heading-2:
    fontFamily: "Optimistic VF, Montserrat, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.21
    letterSpacing: 0px
  heading-3:
    fontFamily: "Optimistic VF, Montserrat, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.44
    letterSpacing: 0px
    fontFeature: "ss01, ss02"
  body:
    fontFamily: "Optimistic VF, Montserrat, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.44
    letterSpacing: 0px
  body-compact:
    fontFamily: "Optimistic VF, Montserrat, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: -0.16px
  caption-bold:
    fontFamily: "Optimistic VF, Montserrat, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0px
  caption:
    fontFamily: "Optimistic VF, Montserrat, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: -0.14px
  small:
    fontFamily: "Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  button:
    fontFamily: "Optimistic VF, Montserrat, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: -0.14px

spacing:
  hairline: 1px
  xs: 4px
  sm: 8px
  card-x: 10px
  md: 12px
  caption: 14px
  lg: 16px
  body-rhythm: 18px
  xl: 24px
  2xl: 32px
  3xl: 40px
  4xl: 48px
  5xl: 64px
  6xl: 80px

rounded:
  sm: 8px
  lg: 20px
  xl: 24px
  pill: 100px

components:
  # Buttons
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 22px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-charcoal}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 22px
  button-secondary-hover:
    backgroundColor: "{colors.icon-secondary}"
    textColor: "{colors.on-dark}"
  button-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.link-blue}"
    typography: "{typography.button}"
    rounded: "{rounded.xl}"
    padding: 4px 12px
  button-disabled:
    backgroundColor: "{colors.divider-gray}"
    textColor: "{colors.cta-disabled-text}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 22px

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-charcoal}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 20px 10px
  card-flat:
    backgroundColor: "{colors.warm-gray}"
    textColor: "{colors.ink-charcoal}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 20px 10px
  card-feature:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-charcoal}"
    typography: "{typography.body}"
    rounded: "{rounded.xl}"
    padding: 24px

  # Inputs
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-charcoal}"
    typography: "{typography.body-compact}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-charcoal}"
  input-error:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.store-error}"

  # Navigation
  nav-bar:
    backgroundColor: "{colors.nav-frosted}"
    textColor: "{colors.ink-charcoal}"
    typography: "{typography.body-compact}"
    padding: 0 24px

  # Dark immersive surface
  dark-section:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-2}"
    padding: 80px 24px

  # Badges
  badge-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  badge-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  badge-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.pill}"
    padding: 4px 12px

  # Modal overlay
  modal-overlay:
    backgroundColor: "{colors.overlay}"
    textColor: "{colors.on-dark}"
    padding: 0px
---

# Meta Store Design System

## Overview

The Meta Store is a product-forward retail experience built to sell hardware — Quest VR headsets, Ray-Ban Meta smart glasses, and accessories. The design walks a tightrope between consumer electronics showroom and lifestyle editorial, deploying cinematic product photography against expansive white canvas (`{colors.background}`) to create a gallery-like sense of aspiration. Every design decision serves the merchandise: generous negative space frames hero product shots like museum pieces, while alternating light and dark surface sections create a visual rhythm that mimics the experience of walking through a physical retail space.

The "Dolly" design system (Meta's internal name for the store layer) sits atop the broader FDS (Facebook Design System) foundation, inheriting its gray scale and semantic tokens while overlaying its own product-focused palette. The result is a system that feels distinctly Meta — the custom Optimistic typeface brings warmth and approachability to what could otherwise be cold tech retail — yet flexible enough to showcase wildly different product lines (from VR headsets to fashion eyewear) without feeling disjointed. The surface strategy is binary: pure white (`{colors.surface}`) for browsing and information, rich dark (`{colors.near-black}`) for immersive product moments.

The store's visual hierarchy is ruthlessly simple. Photography does the heavy lifting, supported by short, punchy headlines in Optimistic Medium and body text that stays brief and scannable. Calls to action are pill-shaped, unmistakable, and always Meta Blue (`{colors.primary}`). There is no visual noise, no decoration for decoration's sake — every element either sells or navigates.

**Key Characteristics:**
- Photography-first retail design where products are the visual heroes, not UI
- Binary surface strategy: pure white for information, deep dark for immersive product moments
- Pill-shaped CTAs in saturated Meta Blue (`{colors.primary}`) create unmistakable action points
- Optimistic VF typeface with OpenType `ss01`/`ss02` features brings geometric warmth
- Generous whitespace frames products like gallery exhibits
- 8px spacing grid with disciplined vertical rhythm
- Alternating light/dark sections create a "walkthrough" retail cadence

## Colors

### Primary
- **Meta Blue** (`{colors.primary}`): Primary CTA background, interactive links, action-driving elements throughout the store
- **Meta Blue Hover** (`{colors.primary-hover}`): Darkened blue for hover states on primary buttons
- **Meta Blue Pressed** (`{colors.primary-pressed}`): Deepest blue for active/pressed button states
- **Meta Blue Light** (`{colors.primary-light}`): Lighter blue variant used on dark backgrounds for CTAs
- **Facebook Blue** (`{colors.facebook-blue}`): Legacy accent inherited from FDS, used for deemphasized button text and badges

### Secondary & Accent
- **Ray-Ban Red** (`{colors.rayban-red}`): Product-specific accent for Ray-Ban Meta smart glasses sections
- **Oculus Purple** (`{colors.oculus-purple}`): Quest/Oculus product accent for VR content
- **Work Purple** (`{colors.work-purple}`): Accent for Meta for Work/enterprise content
- **Portal Blue** (`{colors.portal-blue}`): Deep navy accent for Portal product line
- **Portal Hero Blue** (`{colors.portal-hero-blue}`): Soft teal-blue for Portal hero backgrounds
- **Portal Light Blue** (`{colors.portal-light-blue}`): Secondary Portal surface tint

### Surface & Background
- **White** (`{colors.surface}`): Primary page canvas, nav bar background, card surfaces
- **Soft Gray** (`{colors.soft-gray}`): Secondary background for content sections
- **Warm Gray** (`{colors.warm-gray}`): Flat card background, subtle surface differentiation
- **Web Wash** (`{colors.web-wash}`): Deemphasized background areas, attachment footers
- **Linen** (`{colors.linen}`): Warm off-white for lifestyle-adjacent sections
- **Baby Blue** (`{colors.baby-blue}`): Highlight background, subtle blue tint for informational areas
- **Near Black** (`{colors.near-black}`): Dark section backgrounds, immersive product showcase areas
- **Oculus Light** (`{colors.oculus-light}`): Slightly warm dark surface for Quest product sections
- **Oculus Dark** (`{colors.oculus-dark}`): Pure black for maximum contrast product displays
- **Overlay** (`{colors.overlay}`): Modal/lightbox backdrop (was `rgba(0, 0, 0, 0.6)`)

### Neutrals & Text
- **Primary Text** (`{colors.ink}`): Main body and heading text on light surfaces
- **Dark Charcoal** (`{colors.ink-charcoal}`): Dolly system primary text
- **Icon Secondary** (`{colors.icon-secondary}`): Secondary icon fills, subdued UI elements
- **Secondary Text** (`{colors.text-secondary}`): Supporting copy, labels, timestamps
- **Slate Gray** (`{colors.text-slate}`): Meta Store secondary text, product descriptions
- **Section Header** (`{colors.section-header}`): Mid-gray for section titles
- **Button Text Gray** (`{colors.button-text}`): FDS button text default
- **Disabled Text** (`{colors.text-disabled}`): Inactive button labels, placeholder text
- **CTA Disabled Text** (`{colors.cta-disabled-text}`): Muted blue-gray for disabled interactive labels
- **Divider** (`{colors.divider}`): Content separators, input borders
- **Divider Gray** (`{colors.divider-gray}`): Lighter divider for Dolly sections
- **CTA Gray Border** (`{colors.cta-border}`): Outline button borders
- **Dark Gray Border** (`{colors.border-strong}`): Stronger outline for emphasis

### Semantic & Accent
- **Success Green** (`{colors.success}`) / **Store Success** (`{colors.store-success}`): positive indicators
- **Error Red** (`{colors.error}`) / **Store Error** (`{colors.store-error}`): error states
- **Warning Amber** (`{colors.warning}`): caution indicators
- **Subtle backgrounds**: `{colors.positive-bg}`, `{colors.error-bg}`, `{colors.warning-bg}`, `{colors.info-bg}` (each was a 0.15-alpha tint, flattened over white)

### Base Color Spectrum (FDS)
- Cherry (`{colors.cherry}`), Grape (`{colors.grape}`), Lime (`{colors.lime}`), Seafoam (`{colors.seafoam}`), Teal (`{colors.teal}`), Tomato (`{colors.tomato}`), Pink (`{colors.pink}`).

### Gradient System
- **Dark Overlay Gradient**: `linear-gradient(rgba(0,0,0,0), {colors.overlay})` — applied over dark product photography for text legibility
- **Blue Infinity Gradient**: The Meta symbol uses a blue-to-teal gradient on brand materials, though the store uses flat blue
- **Shadow Alpha Scale**: 0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50, 0.60, 0.80 — black and white alpha ramps for layered transparency

## Typography

### Font Family
- **Primary:** Optimistic VF (variable font by Dalton Maag, commissioned by Meta). Fallbacks: Montserrat, Helvetica, Arial, Noto Sans. OpenType features: `"ss01", "ss02"` activate Meta-specific alternate glyphs. Variable weight axis observed at 300, 400, 500, 700.
- **Secondary:** Helvetica (with Arial fallback) — used for small utility text (12px footer links, legal copy).

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference each role via tokens (`{typography.display-1}`, `{typography.body}`, etc).

| Token | Use |
|---|---|
| `display-1` | Hero headlines on desktop (ss01+ss02) |
| `display-2` | Section heroes, product titles |
| `heading-1` | Major section headings |
| `heading-2` | Subheadings, lighter feel (weight 300) |
| `heading-3` | Card titles, bold callouts (ss01+ss02) |
| `body` | Product descriptions, body copy |
| `body-compact` | Navigation links, UI labels |
| `caption-bold` | Emphasized labels, price text |
| `caption` | Secondary labels, metadata |
| `small` | Footer links, legal text, timestamps |
| `button` | Button label text |

### Principles

Optimistic VF is the cornerstone of Meta's typographic identity — a humanist sans-serif with geometric underpinnings that strikes a balance between Silicon Valley precision and consumer warmth. The "ss01" and "ss02" stylistic sets introduce alternate glyphs that give headlines a distinctive Meta character. Weight 500 (Medium) dominates headlines, creating a presence that commands without shouting, while the unexpected use of weight 300 (Light) at 28px adds an airy, editorial quality to subheadings. Negative letter-spacing at smaller sizes (-0.14px to -0.16px) tightens the optical rhythm for UI elements, keeping the reading experience crisp and efficient.

## Layout

### Spacing System

The complete spacing scale lives in the `spacing:` token block above. Base unit is `{spacing.sm}` (8px).

### Grid & Container
- Max container width: ~1440px, centered with auto margins
- Product grid: 3-column on desktop, 2-column on tablet, 1-column on mobile
- Feature grid: 2-column split (image + content), stacks on mobile
- Grid gap: `{spacing.xl}` between cards, `{spacing.lg}` on mobile
- Page horizontal padding: `{spacing.xl}`–`{spacing.3xl}` depending on breakpoint

### Whitespace Philosophy

Whitespace is the store's primary luxury signifier. Sections breathe with `{spacing.5xl}`–`{spacing.6xl}` vertical padding, creating a sense of unhurried browsing. Product images float in generous negative space rather than being crammed edge-to-edge. This restrained spacing communicates premium positioning — the visual equivalent of wide aisles in a high-end retail store.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, background differentiation only | Default cards, sections |
| Level 1 | `0 2px 4px 0 rgba(0,0,0,0.1)` | Subtle lift for interactive cards |
| Level 2 | `0 12px 28px 0 rgba(0,0,0,0.2), 0 2px 4px 0 rgba(0,0,0,0.1)` | Elevated cards, dropdowns |
| Overlay | `{colors.overlay}` full-screen | Modal/lightbox backdrop |
| Inset | `rgba(255,255,255,0.5)` inset | Inner glow on glass-effect surfaces |

The Meta Store favors a primarily flat elevation model. Most surface differentiation comes from background color shifts (white → soft gray → dark) rather than shadows. When shadows appear, they are soft, diffused, and use the dual-shadow pattern (a large blurred shadow for ambient light + a small sharp shadow for direct light). This creates a physically plausible depth feel without heavy visual weight.

### Decorative Depth

- **Frosted glass nav**: `{colors.nav-frosted}` background with backdrop-filter blur, creating a translucent navigation bar
- **Dark section gradient**: `linear-gradient(rgba(0,0,0,0), {colors.overlay})` overlay on product photography for text legibility
- **Glimmer loading states**: Pulsating opacity animation (0.25 → 1.0) on `#979a9f` base color with 8px radius, 1000ms steps timing — used for skeleton screens during product image loading

## Shapes

| Token | Value | Use |
|---|---|---|
| `sm` | 8px | Inputs, small UI elements, glimmer placeholders |
| `lg` | 20px | Cards (`--card-corner-radius`) |
| `xl` | 24px | Feature cards, product highlight areas, ghost buttons |
| `pill` | 100px | Pill buttons, tags, badges (fully rounded) |

The Meta Store is all smooth curves — no sharp corners under `{rounded.sm}`. Pill is the signature CTA shape.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (`{components.button-primary}`, `{components.card-feature}`, `{components.nav-bar}`) rather than reconstructing them.

### Buttons
- **`button-primary`** — Meta Blue pill CTA. The signature interactive shape. Hover lifts to `{colors.primary-hover}` with scale(1.1); pressed shifts to `{colors.primary-pressed}` with scale(0.9).
- **`button-secondary`** — Outlined pill. Transparent fill, soft outline (`{colors.outline-soft}`), `{colors.ink-charcoal}` text. Hover fills to `{colors.icon-secondary}`.
- **`button-ghost`** — Link-style button with `{colors.link-blue}` text and `{rounded.xl}` corners.
- **`button-disabled`** — `{colors.divider-gray}` background, `{colors.cta-disabled-text}` text, no hover.

### Cards
- **`card`** — White (`{colors.surface}`) background, `{rounded.lg}` corners, generous interior padding.
- **`card-flat`** — `{colors.warm-gray}` background, no shadow.
- **`card-feature`** — `{rounded.xl}` corners, used for product highlight areas with full-bleed imagery.

### Inputs
- **`input`** — White background, `{colors.divider}` border, `{rounded.sm}` corners. Focus shifts border to Meta Blue with 3px outer ring.
- **`input-error`** — Red border (`{colors.store-error}`) and label color.

### Navigation
- **`nav-bar`** — Sticky white bar with frosted-glass effect (`{colors.nav-frosted}` + backdrop blur). Logo left, links center, Meta Blue pill CTA right. ~56px desktop, 48px mobile.

### Dark Sections
- **`dark-section`** — Full-bleed `{colors.near-black}` immersive product showcase. Hero text in `{colors.on-dark}`, generous `{spacing.6xl}` vertical padding.

### Badges
- **`badge-success`** / **`badge-error`** / **`badge-warning`** — pill-shaped semantic indicators using the corresponding semantic color.

### Image Treatment
- Product hero: full-width, cinematic aspect ratio (~21:9 on desktop, ~4:3 on mobile)
- Product cards: 1:1 or 4:3, edge-to-edge within card radius
- Feature images: rounded corners matching card radius (`{rounded.lg}`–`{rounded.xl}`)
- Dark text-over-image: gradient overlay `linear-gradient(rgba(0,0,0,0), {colors.overlay})`
- Lazy loading: native `loading="lazy"` on below-fold images
- WebP format with JPEG fallback

### Product-Specific Sections
- **Quest sections**: Dark backgrounds (`{colors.oculus-light}` or `{colors.oculus-dark}`), white/light text, purple accents (`{colors.oculus-purple}`)
- **Ray-Ban sections**: Warm lifestyle photography, red accents (`{colors.rayban-red}`), linen tones (`{colors.linen}`)
- **Portal sections**: Teal-blue palette (`{colors.portal-hero-blue}`, `{colors.portal-light-blue}`), navy accents (`{colors.portal-blue}`)

## Do's and Don'ts

### Do
- Use pill-shaped (`{rounded.pill}`) buttons for all primary and secondary CTAs
- Let product photography dominate — make images the visual hero of every section
- Alternate between light and dark surface sections to create visual rhythm
- Use Optimistic VF with `ss01` and `ss02` features for all display text
- Keep body copy brief and scannable — this is retail, not editorial
- Use the dual-shadow pattern (ambient + direct) when elevation is needed
- Apply Meta Blue (`{colors.primary}`) exclusively for actionable elements
- Use generous whitespace (`{spacing.5xl}`–`{spacing.6xl}` section padding) to convey premium feel
- Apply gradient overlays on dark photography when placing text over images
- Use the semantic color tokens (success, error, warning) consistently for status communication

### Don't
- Don't use sharp corners (< 8px radius) — the Meta Store is all smooth curves
- Don't mix product-specific accents (Ray-Ban Red with Quest Purple in the same section)
- Don't add decorative borders or ornamental dividers — dividers are functional only
- Don't place important text directly on photography without a gradient scrim
- Don't use weight 300 for anything smaller than 28px — it becomes too thin
- Don't use Facebook Blue (`{colors.facebook-blue}`) as a primary CTA color — use Meta Blue (`{colors.primary}`) instead
- Don't crowd product images — maintain generous padding around all photography
- Don't use more than 2 levels of text hierarchy in a single card
- Don't add drop shadows to cards in dark sections — rely on border and color separation
- Don't use long paragraphs — limit to 2-3 lines of body copy per block

---

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Single column, hamburger nav, hero text shrinks to 36px, full-width product cards, 48px section padding |
| Tablet | 768-1024px | 2-column product grid, compact nav, hero text at 48px |
| Desktop | 1024-1440px | 3-column product grid, full horizontal nav, hero text at 64px, 80px section padding |
| Large Desktop | >1440px | Max-width container (1440px) centered, increased horizontal margins |

### Touch Targets

- Minimum touch target: 44x44px (WCAG AAA compliant)
- Mobile button height: minimum 44px with 10px vertical padding
- Nav hamburger icon: 48x48px touch area
- Product card tappable area: full card surface

### Collapsing Strategy

- **Navigation**: Horizontal links collapse to hamburger menu below 768px; CTA button remains visible
- **Product grids**: 3-col → 2-col at 1024px → 1-col at 768px
- **Hero sections**: Display text scales from 64px → 48px → 36px; CTA buttons stack vertically on mobile
- **Feature sections**: 2-column (image + text) → full-width stacked below 768px, image on top
- **Section padding**: 80px → 64px → 48px → 32px as viewport narrows
- **Card radius**: Remains consistent at 20-24px across all breakpoints

### Image Behavior

- Responsive images via srcset with multiple resolutions
- WebP format with progressive JPEG fallback
- Hero images: full-bleed on mobile, contained on desktop
- Product grid images: maintain aspect ratio, scale proportionally
- Art direction: hero crop changes between desktop (wide cinematic) and mobile (tighter product focus)
- Lazy loading with glimmer skeleton (pulsating gray placeholder) during load

---

## Agent Prompt Guide

### Quick Color Reference

- Primary CTA: Meta Blue (`#0064E0`)
- Background: White (`#FFFFFF`)
- Heading text: Dark Charcoal (`#1C2B33`)
- Body text: Slate Gray (`#5D6C7B`)
- Border/divider: Divider Gray (`#DEE3E9`)
- Secondary surface: Soft Gray (`#F1F4F7`)
- Dark sections: Near Black (`#1C1E21`)

### Example Component Prompts

- "Create a product hero section with a full-width cinematic image, `linear-gradient(rgba(0,0,0,0), rgba(0,0,0,0.6))` text overlay, Optimistic-style 64px/500 white headline, and a Meta Blue (`#0064E0`) pill button (100px radius, 10px 22px padding)"
- "Design a 3-column product card grid with 20px rounded corners, white backgrounds, edge-to-edge product images at top, 18px/400 body text in Slate Gray (`#5D6C7B`), and 24px grid gap"
- "Build a sticky navigation bar with white background, `rgba(241, 244, 247, 0.8)` frosted glass effect, 16px/500 dark text links, and a right-aligned Meta Blue pill CTA"
- "Create a dark product showcase section with `#1C1E21` background, white 48px/500 headline, `#5D6C7B` body text, and a secondary outlined pill button with `rgba(10, 19, 23, 0.12)` border"
- "Design a feature comparison grid with Soft Gray (`#F1F4F7`) background, 24px rounded cards, Meta Blue checkmark icons, and 14px/700 bold labels"

### Iteration Guide

When refining existing screens generated with this design system:
1. Focus on ONE component at a time
2. Reference specific color names and hex codes from this document
3. Use natural language descriptions, not CSS values — "pill-shaped Meta Blue button" not "border-radius: 100px; background: #0064E0"
4. Describe the desired "feel" alongside specific measurements — "generous whitespace like a gallery" means 64-80px section padding
5. For dark sections, specify which product context (Quest dark `#181A1B`, pure black `#000000`, or standard dark `#1C1E21`)
6. Always specify the Optimistic VF weight explicitly (300, 400, 500, or 700) — each creates a dramatically different feel
