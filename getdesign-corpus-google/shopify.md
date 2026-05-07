---
version: alpha
name: Shopify
description: Dark-first cinematic commerce platform — near-black canvas with deep forest-teal undertones, ethereal NeueHaasGrotesk display at weight 330, neon green focus accent, and full-pill primary CTAs.

colors:
  # Canvas hierarchy (dark-first)
  background: "#000000"
  surface: "#02090A"
  surface-elevated: "#061A1C"
  surface-prominent: "#102620"
  surface-light: "#ffffff"

  # Ink
  ink: "#ffffff"
  ink-on-light: "#000000"
  ink-muted: "#A1A1AA"
  ink-subtle: "#71717A"
  ink-disabled: "#52525B"

  # Brand accent — Neon Green (focus & highlights only)
  primary: "#36F4A4"
  on-primary: "#000000"

  # Atmospheric green washes
  aloe: "#C1FBD4"
  pistachio: "#D4F9E0"

  # Neutral scale (Zinc)
  neutral-light: "#D4D4D8"
  neutral-divider: "#3F3F46"
  light-border: "#E4E4E7"

  # Borders
  border-card: "#1E2C31"
  border-input: "#3F3F46"

  # Link variants
  link-muted: "#9797A2"
  link-sage: "#9DABAD"
  link-lavender: "#BDBDCA"
  link-mint: "#99B3AD"

  # Glass / overlay (opaque approximation)
  glass-frosted: "#333333"  # was rgba(255,255,255,0.2) over black — Google format requires hex
  shadow-tint: "#0a0a0a"  # was rgba(0,0,0,0.1) — Google format requires hex
  edge-highlight: "#0c0c0c"  # was rgba(255,255,255,0.03) inset — Google format requires hex

typography:
  display-xl:
    fontFamily: "NeueHaasGrotesk, Helvetica, Arial, sans-serif"
    fontSize: 96px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  display-light:
    fontFamily: "NeueHaasGrotesk, Helvetica, Arial, sans-serif"
    fontSize: 96px
    fontWeight: 330
    lineHeight: 0.96
    letterSpacing: 0px
  display-bold:
    fontFamily: "NeueHaasGrotesk, Helvetica, Arial, sans-serif"
    fontSize: 90px
    fontWeight: 750
    lineHeight: 1.0
    letterSpacing: 4.54px
  h1:
    fontFamily: "NeueHaasGrotesk, Helvetica, Arial, sans-serif"
    fontSize: 70px
    fontWeight: 330
    lineHeight: 1.0
    letterSpacing: 0px
  h2:
    fontFamily: "NeueHaasGrotesk, Helvetica, Arial, sans-serif"
    fontSize: 55px
    fontWeight: 330
    lineHeight: 1.16
    letterSpacing: 0px
  h3:
    fontFamily: "NeueHaasGrotesk, Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 330
    lineHeight: 1.14
    letterSpacing: 0px
  h4:
    fontFamily: "NeueHaasGrotesk, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 360
    lineHeight: 1.14
    letterSpacing: 0.32px
  h5:
    fontFamily: "NeueHaasGrotesk, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.28
    letterSpacing: 0.42px
  h6:
    fontFamily: "NeueHaasGrotesk, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.14
    letterSpacing: 0.36px
  body-large:
    fontFamily: "Inter Variable, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  body:
    fontFamily: "Inter Variable, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0px
  body-medium:
    fontFamily: "Inter Variable, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 550
    lineHeight: 1.56
    letterSpacing: 0px
  body-small:
    fontFamily: "Inter Variable, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button:
    fontFamily: "NeueHaasGrotesk, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  nav-link:
    fontFamily: "NeueHaasGrotesk, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.72px
  caption:
    fontFamily: "Inter Variable, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.49
    letterSpacing: 0.28px
  overline:
    fontFamily: "NeueHaasGrotesk, Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 1.54px
  micro:
    fontFamily: "Inter Variable, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: -0.13px
  label:
    fontFamily: "Inter Variable, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.72px
  code:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  code-small:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 28px
  2xl: 32px
  3xl: 40px
  4xl: 64px
  5xl: 96px
  6xl: 120px

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  decorative: 340px
  pill: 9999px

components:
  # Primary white pill CTA
  button-primary:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink-on-light}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 26px
  button-primary-focus:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink-on-light}"

  # Secondary ghost pill
  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 26px
  button-secondary-hover:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink-on-light}"

  # Frosted-glass tag
  badge-frosted:
    backgroundColor: "{colors.glass-frosted}"
    textColor: "{colors.ink}"
    typography: "{typography.body-small}"
    rounded: "{rounded.xs}"
    padding: 12px 16px

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 24px
  card-featured:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 32px

  # Inputs
  input:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.body-small}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"

  # Navigation
  nav-bar:
    backgroundColor: "{colors.surface-prominent}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 16px 64px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-hover:
    textColor: "{colors.ink-muted}"
---

# Shopify Design System

## Overview

Shopify.com is a dark-first digital theatre — a website that stages its commerce platform like a cinematic premiere. The entire experience unfolds against an abyss of near-black surfaces that carry the faintest whisper of deep forest green (`{colors.background}`, `{colors.surface}`, `{colors.surface-elevated}`, `{colors.surface-prominent}`), creating a nocturnal atmosphere that feels less like a SaaS marketing page and more like an exclusive product reveal at a tech keynote. This darkness isn't cold or corporate — it's the warm, enveloping dark of a luxury experience, like sitting in the front row of a darkened auditorium.

The typography is the undeniable star. NeueHaasGrotesk — a refined Helvetica descendant — appears at monumental scale (96px) with impossibly light weight (330–400), creating headlines that feel etched in light rather than printed in ink. The `ss03` OpenType feature gives letterforms a distinctive character that separates Shopify's type from generic Helvetica usage. Below the display layer, Inter Variable handles body text with surgical precision, using equally unusual variable weights (420, 450, 550) that live in the spaces between traditional weight stops. This precision signals a company that sweats every detail.

Color is used with extreme restraint. The primary accent is Shopify Neon Green (`{colors.primary}`) — an electric mint that appears exclusively on focus rings and accent highlights, pulsing like a bioluminescent signal against the dark canvas. Softer green tints (Aloe `{colors.aloe}`, Pistachio `{colors.pistachio}`) provide atmospheric washes. White is the only text color that matters on dark surfaces, while a zinc-based neutral scale (`{colors.ink-muted}` through `{colors.neutral-divider}`) handles the hierarchy of quiet information. The result is a design that makes commerce technology feel like it belongs in a science-fiction future.

**Key Characteristics:**
- Dark-first design with deep forest-teal undertones (not pure black)
- Ultra-light display typography (weight 330) at monumental scale (96px) creating an ethereal presence
- Neon Green (`{colors.primary}`) as the singular high-energy accent against darkness
- Full-pill buttons (`{rounded.pill}`) as the primary interactive shape
- Layered, multi-stage box shadows creating photographic depth
- Product screenshots embedded in dark UI contexts, matching the surrounding darkness
- Zinc-based neutral scale for text hierarchy — balanced between warm and cool

## Colors

### Primary
- **Shopify White** (`{colors.surface-light}`): Primary text on dark surfaces, button fills, high-contrast elements.
- **Shopify Black** (`{colors.background}`): Body background, button text on white, maximum contrast base.

### Secondary & Accent
- **Neon Green** (`{colors.primary}`): The signature accent — focus rings, interactive highlights, active state indicators. Electric and bioluminescent.
- **Aloe** (`{colors.aloe}`): Soft green wash for decorative backgrounds, atmospheric cards.
- **Pistachio** (`{colors.pistachio}`): Lightest green tint for subtle surface differentiation.

### Surface & Background
- **Void** (`{colors.background}`): Root page background — true black for maximum depth.
- **Deep Teal** (`{colors.surface}`): Card surfaces, content containers — near-black with green undertone.
- **Dark Forest** (`{colors.surface-elevated}`): Section backgrounds with visible green character.
- **Forest** (`{colors.surface-prominent}`): Elevated dark surfaces, header backgrounds — the warmest dark shade.
- **Dark Card Border** (`{colors.border-card}`): Card borders on dark surfaces, subtle boundary definition.

### Neutrals & Text (Zinc Scale)
- **Shade-30** (`{colors.neutral-light}`): Lightest neutral, barely-there borders on dark.
- **Muted Text** (`{colors.ink-muted}`): Secondary text, metadata, descriptions — the quiet voice.
- **Shade-50** (`{colors.ink-subtle}`): Tertiary text, timestamps, least important info.
- **Shade-60** (`{colors.ink-disabled}`): Disabled text, decorative neutrals.
- **Shade-70** (`{colors.neutral-divider}`): Subtle dividers, barely-visible UI boundaries.
- **Light Border** (`{colors.light-border}`): Borders on light surfaces (rare — only in light-mode modals).

### Semantic Links
- **Link Muted** (`{colors.link-muted}`): Muted link text with underline decoration.
- **Link Sage** (`{colors.link-sage}`): Teal-tinted muted links.
- **Link Lavender** (`{colors.link-lavender}`): Lighter link variant.
- **Link Mint** (`{colors.link-mint}`): Green-tinted link variant for themed sections.

### Gradient System
- **Dark Teal Wash**: Radial gradient from `{colors.surface-prominent}` center to `{colors.surface}` edge — used behind product showcases.
- **Green Atmospheric**: Subtle green-tinted ambient gradients behind hero sections, creating depth without solid colors.
- **Spotlight**: Focused bright area fading to black — keynote-style presentation lighting.

## Typography

### Font Family
- **Display**: NeueHaasGrotesk (refined Helvetica descendant, variable font), fallback `Helvetica, Arial, sans-serif`
- **Body**: Inter Variable, fallback `Helvetica, Arial, sans-serif`
- **Mono**: `ui-monospace`, fallback `SFMono-Regular, Menlo, Monaco, Consolas, monospace`
- **OpenType features**: `ss03` (stylistic set 3) active across all text — distinctive letterform alternates

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-light}`, `{typography.body}`).

| Token | Use |
|---|---|
| `display-xl` | Hero headlines (96px) |
| `display-light` | Ethereal display at weight 330 (96px) — the signature look |
| `display-bold` | Emphasis display (90px, weight 750) |
| `h1`–`h6` | Section heads from 70px down to 24px |
| `body-large` | Lead paragraphs (20px) |
| `body` | Standard body text (18px Inter Variable) |
| `body-medium` | Emphasized body (weight 550) |
| `body-small` | Compact body (16px) |
| `button` | CTA text (16px) |
| `nav-link` | Navigation items (18px, `0.72px` letter-spacing) |
| `caption`, `overline`, `micro`, `label` | Metadata, wide-tracked labels, small chrome |
| `code`, `code-small` | Monospace blocks |

### Principles
Shopify's typography is a masterclass in variable font precision. The display layer lives almost exclusively at weights 330–400 — featherweight text that appears to hover above the dark background like projected light. The opposite of the bold approach most SaaS sites take: where others shout, Shopify whispers at scale. The 96px headlines at weight 330 create a paradox of enormous size and delicate stroke. The `ss03` OpenType feature activates a stylistic set that gives specific characters a more refined appearance. Inter Variable handles body with weights like 420 and 550 that exist between traditional stops — every piece of text has exactly the visual weight it needs.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

The scale spans tight chrome (`xxs`–`xs`) up through theatrical section breaks (`5xl`–`6xl`).

### Grid & Container
- Max container width: ~1280px (centered)
- Hero: full-width, edge-to-edge dark background with centered text
- Feature sections: 2-column layouts with text and product screenshots
- Stats sections: horizontal layout with large numbers
- Horizontal padding: `4xl` desktop, `2xl` tablet, `md` mobile
- Grid gap: `lg`–`2xl` between major content blocks

### Whitespace Philosophy
Shopify's whitespace strategy is theatrical. Sections are separated by vast expanses of dark space — `5xl`–`6xl` of pure black breathing room — that create the pacing of a presentation, not a webpage. Each content block is its own "slide" in a keynote-style scroll. Within sections, spacing is tighter and more deliberate, creating focal density against the expansive void.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Base | No shadow, dark surface | Default page background |
| Subtle (Level 1) | `0 0 0 1px` tinted `{colors.shadow-tint}` + inset `{colors.edge-highlight}` glow | Resting cards |
| Medium (Level 2) | Stacked 1px ring + 2px + 4px + 8px blurs tinted `{colors.shadow-tint}` | Elevated cards, featured sections |
| High (Level 3) | `0 25px 50px -12px` tinted `{colors.shadow-tint}` | Modals, dropdowns, overlays |
| Focus | `0 0 0 2px {colors.primary}` | Keyboard focus ring (Neon Green) |

**Shadow Philosophy**: Shopify's shadow system is unusually sophisticated. Rather than single-value shadows, cards use a stacked, multi-layer approach: a 1px ring for boundary definition, 2px/4px/8px progressive blurs for natural light falloff, and a delicate inset white glow that simulates a top-lit glass surface. On dark backgrounds, shadows function more as "ambient occlusion" than traditional elevation — the card appears to sink slightly into the surface rather than float above it.

### Decorative Depth
- **Dark teal gradients**: Ambient radial washes behind hero sections and product showcases
- **Spotlight effects**: Bright centered areas fading to black
- **Edge glow**: Subtle light-colored edges on dark cards via inset box-shadow
- **Green atmospheric halos**: Faint green tints in background gradients

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Rare — default state for full-bleed surfaces |
| `xs` | 4px | Tags, badges, micro-elements |
| `sm` | 8px | Standard cards, inputs, video containers |
| `md` | 12px | Featured cards, image containers, non-pill buttons |
| `lg` | 20px | Top-rounded cards (`20px 20px 0 0`), modal headers |
| `decorative` | 340px | Large rounded decorative elements |
| `pill` | 9999px | Pill buttons, pill badges, nav elements |

## Components

The complete component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card}`).

### Buttons
- **`button-primary`** — White-fill pill with black text. `{rounded.pill}` corners, asymmetric `12px 26px` padding for visual balance, focus shows a 2px Neon Green outline.
- **`button-secondary`** — Ghost pill with white border on dark surfaces; hover fills white.
- **`badge-frosted`** — Frosted-glass tag (opaque approximation of `rgba(255,255,255,0.2)` over dark) at `{rounded.xs}` corners.

### Cards & Containers
- **`card`** — Deep Teal surface with `1px solid {colors.border-card}` border, `{rounded.sm}` corners, the multi-layered shadow stack.
- **`card-featured`** — Same but `{rounded.md}` and 32px padding.

### Inputs & Forms
- **`input`** — Dark Forest surface, white text, `1px solid {colors.border-input}` border, `{rounded.sm}` corners. Focus shows a 2px `{colors.primary}` ring.

### Navigation
Transparent over dark hero, becomes Forest (`{colors.surface-prominent}`) on scroll. White Shopify wordmark left, 18px/500 NeueHaasGrotesk nav links with `0.72px` letter-spacing white. Right-aligned white pill "Start for free" button + ghost secondary CTA.

### Image Treatment
Product screenshots embed in dark UI contexts, matching the surrounding darkness. All images sit flush within dark containers — no bright borders or frames. Lazy loading with dark placeholder surfaces.

### Trust Indicators
Stats displayed prominently ("15+", "150M+") at display scale in NeueHaasGrotesk. Partner/developer ecosystem callout sections. Dark-themed testimonials integrated into the page flow.

## Do's and Don'ts

### Do
- Use the dark teal-black surface hierarchy (`{colors.background}` → `{colors.surface}` → `{colors.surface-elevated}` → `{colors.surface-prominent}`) for depth
- Keep display typography at weight 330–400 — the ethereal lightness is the design's signature
- Use Neon Green (`{colors.primary}`) exclusively for focus states and critical accent highlights
- Apply `{rounded.pill}` to all primary CTA buttons — the full pill is non-negotiable
- Use the multi-layered shadow system for card elevation — single shadows look flat
- Maintain the `ss03` OpenType feature across all text — it's part of the typographic identity
- Use Inter Variable for body and NeueHaasGrotesk for headings — never mix their roles
- Create theatrical spacing between sections (`5xl+`) for cinematic pacing

### Don't
- Don't use pure black for text on dark backgrounds — use white only
- Don't introduce warm colors (orange, red, yellow) — the palette is strictly cool (greens, teals, neutrals)
- Don't use font weights above 500 for NeueHaasGrotesk body text — heavy weights break the ethereal feel
- Don't apply green accents to large surfaces — Neon Green is for small, precise highlights only
- Don't use sharp corners (0px radius) on interactive elements — everything rounds
- Don't add bright backgrounds — the dark theme is fundamental, not optional
- Don't use single-layer box shadows — the stacked approach is the system
- Don't set line-height above 1.56 for body text — Shopify's text is relatively compact
- Don't mix NeueHaasGrotesk and Inter at the same size/role — their weight scales differ
- Don't use letter-spacing below 0 for headings — Shopify headings track neutral or positive

---

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, hamburger nav, display text scales to 48px, 16px padding |
| Tablet | 640–1024px | 2-column grids begin, display text at 70px, 32px padding |
| Desktop | 1024–1440px | Full layout, expanded nav, 96px display, 64px padding |
| Large Desktop | >1440px | Max-width container centered, increased section spacing |

### Touch Targets
- Minimum touch target: 44×44px (WCAG AAA)
- Pill buttons: 48px height minimum with generous horizontal padding
- Nav links: 44px touch area
- Card surfaces: full card is tappable where linked

### Collapsing Strategy
- **Navigation**: Full horizontal links → hamburger menu below 1024px; logo and CTA remain visible
- **Hero section**: 96px display → 70px tablet → 48px mobile; single-column center alignment
- **Feature sections**: 2-column text+image → stacked single column below 768px
- **Stats**: Horizontal row → stacked vertical on mobile
- **Section padding**: 64px → 40px → 24px → 16px as viewport narrows
- **Cards**: Grid → stack, maintaining full-width on mobile

### Image Behavior
- Product screenshots: responsive within dark containers, maintain aspect ratio
- Hero images: full-width on all breakpoints, lazy loaded with dark placeholders
- Admin UI previews: scale proportionally, may crop on mobile
- All images use CDN with responsive srcset

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Shopify White (`{colors.surface-light}`)
- Page background: Void Black (`{colors.background}`)
- Card surface: Deep Teal (`{colors.surface}`)
- Section bg: Dark Forest (`{colors.surface-elevated}`)
- Elevated bg: Forest (`{colors.surface-prominent}`)
- Accent: Neon Green (`{colors.primary}`)
- Body text: White (`{colors.ink}`)
- Muted text: Muted (`{colors.ink-muted}`)
- Border dark: Dark Card Border (`{colors.border-card}`)

### Example Component Prompts
- "Create a hero section on true black (`{colors.background}`) with a 96px/330 NeueHaasGrotesk headline in white, a 20px/500 subtitle in `{colors.ink-muted}`, and two pill buttons: white filled (`{rounded.pill}`) and ghost with 2px white border."
- "Design a feature card on Deep Teal (`{colors.surface}`) with 1px `{colors.border-card}` border, 12px radius, multi-layer shadow tinted `{colors.shadow-tint}`, containing a 32px/360 white heading and 18px/400 `{colors.ink-muted}` body text."
- "Build a stats section on Dark Forest (`{colors.surface-elevated}`) with 96px/750 white numbers (NeueHaasGrotesk), 16px/400 `{colors.ink-muted}` descriptive labels, and generous 64px spacing between stat blocks."
- "Create a sticky nav with transparent background (becomes `{colors.surface-prominent}` on scroll), white Shopify logo left, 18px/500 white nav links with 0.72px letter-spacing, and a white pill 'Start for free' button right."
- "Design a tag/badge with frosted glass background (`{colors.glass-frosted}`), 4px radius, 12px 16px padding, white 16px text — floating over a dark card surface."

### Iteration Guide
1. Focus on ONE component at a time
2. Reference specific color names from this document
3. Remember: this is a DARK-FIRST design — light surfaces are the exception, not the rule
4. Display text should always feel feather-light (weight 330–400) — if it looks heavy, reduce weight
5. Neon Green (`{colors.primary}`) is precious — use sparingly for focus and accent only
6. The dark surface hierarchy creates subtle depth
7. Shadows are multi-layered — a single `box-shadow` value won't capture the Shopify card feel
8. `ss03` OpenType feature must be active on all text for typographic consistency
