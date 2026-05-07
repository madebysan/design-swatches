---
version: alpha
name: Stripe
description: Premium fintech canvas — white surfaces, deep-navy headings, signature Stripe Purple, sohne-var weight 300 with ss01 stylistic set, conservative 4–8px corners, and brand-tinted multi-layer shadows.

colors:
  # Canvas + surfaces
  background: "#ffffff"
  surface: "#ffffff"
  surface-light: "#f6f9fc"

  # Brand
  primary: "#533afd"
  primary-hover: "#4434d4"
  primary-deep: "#2e2b8c"
  primary-light: "#b9b9f9"
  primary-mid: "#665efd"

  # Brand dark surfaces
  brand-dark: "#1c1e54"
  brand-darkest: "#0d253d"

  # Ink / text
  ink: "#061b31"
  ink-label: "#273951"
  ink-body: "#64748d"
  on-primary: "#ffffff"

  # Accents (decorative only)
  ruby: "#ea2261"
  magenta: "#f96bee"
  magenta-light: "#ffd7ef"

  # Semantic
  success: "#15be53"
  success-text: "#108c3d"
  success-bg: "#dff6e6"  # was rgba(21,190,83,0.2) — Google format requires hex
  success-border: "#bde9c8"  # was rgba(21,190,83,0.4) — Google format requires hex
  lemon: "#9b6829"
  info-text: "#2874ad"
  info-border: "#d4e7f5"  # was rgba(43,145,223,0.2) — Google format requires hex

  # Borders
  border: "#e5edf5"
  border-soft-purple: "#d6d9fc"
  border-magenta: "#ffd7ef"
  border-dashed: "#362baa"
  border-disabled: "#d4dee9"
  border-dark: "#061b31"

  # Shadow tints
  shadow-blue: "#323250"  # was rgba(50,50,93,0.25) — Google format requires hex
  shadow-dark-blue: "#030327"  # was rgba(3,3,39,0.25) — Google format requires hex
  shadow-black: "#171717"  # was rgba(0,0,0,0.1) / rgba(23,23,23,0.06-0.08) — Google format requires hex

typography:
  display-hero:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.03
    letterSpacing: -1.4px
    fontFeature: "ss01"
  display-large:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.96px
    fontFeature: "ss01"
  heading-section:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.64px
    fontFeature: "ss01"
  sub-heading-large:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 26px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.26px
    fontFeature: "ss01"
  sub-heading:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.22px
    fontFeature: "ss01"
  body-large:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0px
    fontFeature: "ss01"
  body:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0px
    fontFeature: "ss01"
  button:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
    fontFeature: "ss01"
  button-small:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
    fontFeature: "ss01"
  link:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
    fontFeature: "ss01"
  caption:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px
    fontFeature: "ss01"
  caption-small:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0px
    fontFeature: "ss01"
  caption-tabular:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: -0.36px
    fontFeature: "tnum"
  micro:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.1px
    fontFeature: "ss01"
  micro-tabular:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
    fontFeature: "tnum"
  nano:
    fontFamily: "sohne-var, SF Pro Display, system-ui, sans-serif"
    fontSize: 8px
    fontWeight: 300
    lineHeight: 1.07
    letterSpacing: 0px
    fontFeature: "ss01"
  code-body:
    fontFamily: "SourceCodePro, SFMono-Regular, monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 2.0
    letterSpacing: 0px
  code-bold:
    fontFamily: "SourceCodePro, SFMono-Regular, monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 2.0
    letterSpacing: 0px
  code-micro:
    fontFamily: "SourceCodePro, SFMono-Regular, monospace"
    fontSize: 9px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0px

spacing:
  hairline: 1px
  micro: 2px
  xxs: 4px
  xs: 6px
  sm: 8px
  md: 10px
  lg: 12px
  xl: 16px
  2xl: 20px
  3xl: 32px
  4xl: 48px
  5xl: 64px

rounded:
  none: 0px
  micro: 1px
  sm: 4px
  md: 5px
  lg: 6px
  xl: 8px

components:
  # Primary purple CTA
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"

  # Ghost / outlined
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-ghost-hover:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.primary}"

  # Transparent info
  button-info:
    backgroundColor: "{colors.background}"
    textColor: "{colors.info-text}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 8px 16px

  # Disabled / neutral
  button-disabled:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-body}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 8px 16px

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-featured:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xl}"
    padding: 32px

  # Badges
  badge-neutral:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.sm}"
    padding: 0px 6px
  badge-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    typography: "{typography.micro}"
    rounded: "{rounded.sm}"
    padding: 1px 6px

  # Inputs
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    rounded: "{rounded.lg}"
    padding: 12px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.primary}"

  # Dark brand section panel
  section-dark:
    backgroundColor: "{colors.brand-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    padding: 64px 40px
---

# Stripe Design System

## Overview

Stripe's website is the gold standard of fintech design — a system that manages to feel simultaneously technical and luxurious, precise and warm. The page opens on a clean white canvas (`{colors.background}`) with deep navy headings (`{colors.ink}`) and a signature purple (`{colors.primary}`) that functions as both brand anchor and interactive accent. This isn't the cold, clinical purple of enterprise software; it's a rich, saturated violet that reads as confident and premium. The overall impression is of a financial institution redesigned by a world-class type foundry.

The custom `sohne-var` variable font is the defining element of Stripe's visual identity. Every text element enables the OpenType `ss01` stylistic set, which modifies character shapes for a distinctly geometric, modern feel. At display sizes (48–56px), sohne-var runs at weight 300 — an extraordinarily light weight for headlines that creates an ethereal, almost whispered authority. This is the opposite of the "bold hero headline" convention; Stripe's headlines feel like they don't need to shout. The negative letter-spacing (`-1.4px` at 56px, `-0.96px` at 48px) tightens the text into dense, engineered blocks. At smaller sizes, the system also uses weight 300 with proportionally reduced tracking, and tabular numerals via `tnum` for financial data display.

What truly distinguishes Stripe is its shadow system. Rather than the flat or single-layer approach of most sites, Stripe uses multi-layer, blue-tinted shadows: the signature `{colors.shadow-blue}` combined with `{colors.shadow-black}` creates shadows with a cool, almost atmospheric depth — like elements are floating in a twilight sky. The blue-gray undertone of the primary shadow color ties directly to the navy-purple brand palette, making even elevation feel on-brand.

**Key Characteristics:**
- sohne-var with OpenType `ss01` on all text — a custom stylistic set that defines the brand's letterforms
- Weight 300 as the signature headline weight — light, confident, anti-convention
- Negative letter-spacing at display sizes (`-1.4px` at 56px, progressive relaxation downward)
- Blue-tinted multi-layer shadows tinted with `{colors.shadow-blue}` — elevation that feels brand-colored
- Deep navy (`{colors.ink}`) headings instead of black — warm, premium, financial-grade
- Conservative border-radius (`{rounded.sm}`–`{rounded.xl}`) — nothing pill-shaped, nothing harsh
- Ruby (`{colors.ruby}`) and magenta (`{colors.magenta}`) accents for gradient and decorative elements
- `SourceCodePro` as the monospace companion for code and technical labels

## Colors

### Primary
- **Stripe Purple** (`{colors.primary}`): Primary brand color, CTA backgrounds, link text, interactive highlights.
- **Deep Navy** (`{colors.ink}`): Primary heading color. Not black, not gray — a very dark blue that adds warmth and depth.
- **Pure White** (`{colors.background}`): Page background, card surfaces, button text on dark backgrounds.

### Brand & Dark
- **Brand Dark** (`{colors.brand-dark}`): Deep indigo for dark sections, footer backgrounds, immersive brand moments.
- **Dark Navy** (`{colors.brand-darkest}`): The darkest neutral — almost-black with a blue undertone.

### Accent Colors
- **Ruby** (`{colors.ruby}`): Warm red-pink for icons, alerts, accent elements.
- **Magenta** (`{colors.magenta}`): Vivid pink-purple for gradients and decorative highlights.
- **Magenta Light** (`{colors.magenta-light}`): Tinted surface for magenta-themed cards and badges.

### Interactive
- **Primary Purple** (`{colors.primary}`): Primary link color, active states, selected elements.
- **Purple Hover** (`{colors.primary-hover}`): Darker purple for hover states.
- **Purple Deep** (`{colors.primary-deep}`): Dark purple for icon hover states.
- **Purple Light** (`{colors.primary-light}`): Soft lavender for subdued hover backgrounds.
- **Purple Mid** (`{colors.primary-mid}`): Range selector and input highlight color.

### Neutral Scale
- **Heading** (`{colors.ink}`): Primary headings, nav text, strong labels.
- **Label** (`{colors.ink-label}`): Form labels, secondary headings.
- **Body** (`{colors.ink-body}`): Secondary text, descriptions, captions.

### Semantic
- **Success Green** (`{colors.success}`): Status badges, success indicators.
- **Success Text** (`{colors.success-text}`): Success badge text color.
- **Success BG** (`{colors.success-bg}`): Opaque approximation of `rgba(21,190,83,0.2)` for badge backgrounds.
- **Success Border** (`{colors.success-border}`): Opaque approximation of `rgba(21,190,83,0.4)` for badge borders.
- **Lemon** (`{colors.lemon}`): Warning and highlight accent.
- **Info Text** (`{colors.info-text}`): Tertiary/info text.

### Surface & Borders
- **Border Default** (`{colors.border}`): Standard border color for cards, dividers, containers.
- **Border Purple** (`{colors.primary-light}`): Active/selected state borders.
- **Border Soft Purple** (`{colors.border-soft-purple}`): Subtle purple-tinted borders for secondary elements.
- **Border Magenta** (`{colors.border-magenta}`): Pink-tinted borders for magenta-themed elements.
- **Border Dashed** (`{colors.border-dashed}`): Dashed borders for drop zones and placeholder elements.

### Shadow Colors
- **Shadow Blue** (`{colors.shadow-blue}`): The signature — blue-tinted primary shadow tint (opaque approx of `rgba(50,50,93,0.25)`).
- **Shadow Dark Blue** (`{colors.shadow-dark-blue}`): Deeper blue tint for elevated elements.
- **Shadow Black** (`{colors.shadow-black}`): Secondary shadow tint for depth reinforcement.

## Typography

### Font Family
- **Primary**: `sohne-var`, fallback `SF Pro Display`
- **Monospace**: `SourceCodePro`, fallback `SFMono-Regular`
- **OpenType Features**: `ss01` enabled globally on all sohne-var text; `tnum` for tabular numbers on financial data and captions.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`).

| Token | Use |
|---|---|
| `display-hero` | Maximum size, whisper-weight authority (56px) |
| `display-large` | Secondary hero headlines (48px) |
| `heading-section` | Feature section titles (32px) |
| `sub-heading-large` | Card headings, sub-sections (26px) |
| `sub-heading` | Smaller section heads (22px) |
| `body-large` | Feature descriptions, intro text (18px) |
| `body` | Standard reading text (16px) |
| `button`, `button-small` | Button labels |
| `link` | Navigation links (14px) |
| `caption`, `caption-small` | Small labels, fine print |
| `caption-tabular` | Financial data, numbers |
| `micro`, `micro-tabular`, `nano` | Tiny axis labels, chart data |
| `code-body`, `code-bold`, `code-micro` | SourceCodePro for code blocks |

### Principles
- **Light weight as signature**: Weight 300 at display sizes is Stripe's most distinctive typographic choice. Lightness as luxury — text is so confident it doesn't need weight to be authoritative.
- **ss01 everywhere**: The `ss01` stylistic set is non-negotiable for sohne-var text — it modifies specific glyphs to create a more geometric, contemporary feel.
- **Two OpenType modes**: `ss01` for display/body text, `tnum` for tabular numerals in financial data — they never overlap.
- **Progressive tracking**: Letter-spacing tightens proportionally with size and returns to normal at 16px and below.
- **Two-weight simplicity**: Primarily 300 (body and headings) and 400 (UI/buttons). No bold (700) in the primary font.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

The scale is dense at the small end (every few px from `xxs`–`lg`), reflecting Stripe's precision-oriented UI for financial data.

### Grid & Container
- Max content width: ~1080px
- Hero: centered single-column with generous padding, lightweight headlines
- Feature sections: 2–3 column grids for feature cards
- Full-width dark sections with `{colors.brand-dark}` background for brand immersion
- Code/dashboard previews as contained cards with blue-tinted shadows

### Whitespace Philosophy
- **Precision spacing**: Unlike vast emptiness of minimalist systems, Stripe uses measured, purposeful whitespace.
- **Dense data, generous chrome**: Financial data displays are tightly packed; the UI chrome around them is generously spaced.
- **Section rhythm**: White sections alternate with dark brand sections (`{colors.brand-dark}`) — dramatic light/dark cadence.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Page background, inline text |
| Ambient (Level 1) | Soft drop shadow tinted `{colors.shadow-black}` | Subtle card lift, hover hints |
| Standard (Level 2) | Drop shadow tinted `{colors.shadow-black}` | Standard cards, content panels |
| Elevated (Level 3) | Stacked far-blue + near-black drop shadows tinted `{colors.shadow-blue}` and `{colors.shadow-black}` | Featured cards, dropdowns, popovers |
| Deep (Level 4) | Stacked deep-blue + black tinted `{colors.shadow-dark-blue}` and `{colors.shadow-black}` | Modals, floating panels |
| Ring (Accessibility) | `2px solid {colors.primary}` outline | Keyboard focus ring |

**Shadow Philosophy**: Stripe's shadow system is built on chromatic depth. Where most design systems use neutral gray or black shadows, Stripe's primary shadow color is a deep blue-gray that echoes the brand's navy palette. The multi-layer approach pairs this blue-tinted shadow with a pure black secondary layer at a different offset, creating parallax-like depth where the branded shadow sits farther from the element and the neutral shadow sits closer.

### Decorative Depth
- Dark brand sections (`{colors.brand-dark}`) create immersive depth through background color contrast
- Gradient overlays with ruby-to-magenta transitions for hero decorations

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Inline rules, separators |
| `micro` | 1px | Fine-grained elements |
| `sm` | 4px | Buttons, inputs, badges, cards — the workhorse |
| `md` | 5px | Standard card containers |
| `lg` | 6px | Navigation, larger interactive elements |
| `xl` | 8px | Featured cards, hero elements |

Stripe stays in the 4–8px range. Never pill-shaped, never soft Material-style.

## Components

The complete component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card}`).

### Buttons
- **`button-primary`** — Stripe Purple solid CTA, white text, `{rounded.sm}` corners.
- **`button-ghost`** — Transparent with `1px solid {colors.primary-light}` border and purple text.
- **`button-info`** — Transparent with info-blue text and tinted border.
- **`button-disabled`** — Muted neutral state.

### Cards & Containers
- **`card`** — White surface, `1px solid {colors.border}` border, `{rounded.lg}` corners, the multi-layer brand shadow stack.
- **`card-featured`** — Larger cards at `{rounded.xl}` corners.

### Badges
- **`badge-neutral`** — White pill with hairline border, micro text.
- **`badge-success`** — Tinted green pill with green text.

### Inputs
- **`input`** — White surface, `1px solid {colors.border}` border, `{rounded.sm}` corners. Focus shifts border to `{colors.primary}`. Labels use `{colors.ink-label}`, placeholders use `{colors.ink-body}`.

### Navigation
Clean horizontal nav on white, sticky with backdrop blur. Brand logotype left-aligned. Links in sohne-var 14px weight 400, `{colors.ink}` text with `ss01`. `{rounded.lg}` on nav container. Right-aligned purple CTA. Mobile collapses to hamburger.

### Decorative Elements
- **Dashed Borders**: `1px dashed {colors.border-dashed}` for placeholder/drop zones; `1px dashed {colors.border-magenta}` for magenta-themed decorative borders.
- **Gradient Accents**: Ruby-to-magenta gradients (`{colors.ruby}` to `{colors.magenta}`) for hero decorations.
- **Brand Dark Sections** (`section-dark`): `{colors.brand-dark}` backgrounds with white text.

## Do's and Don'ts

### Do
- Use sohne-var with `ss01` on every text element — the stylistic set IS the brand
- Use weight 300 for all headlines and body text — lightness is the signature
- Apply blue-tinted shadows (tinted `{colors.shadow-blue}`) for all elevated elements
- Use `{colors.ink}` (deep navy) for headings instead of black — the warmth matters
- Keep border-radius between `{rounded.sm}`–`{rounded.xl}` — conservative rounding is intentional
- Use `tnum` for any tabular/financial number display
- Layer shadows: blue-tinted far + neutral close for depth parallax
- Use `{colors.primary}` purple as the primary interactive/CTA color

### Don't
- Don't use weight 600–700 for sohne-var headlines — weight 300 is the brand voice
- Don't use large border-radius (12px+, pill shapes) on cards or buttons — Stripe is conservative
- Don't use neutral gray shadows — always tint with blue
- Don't skip `ss01` on any sohne-var text — the alternate glyphs define the personality
- Don't use pure black for headings — always `{colors.ink}` deep navy
- Don't use warm accent colors (orange, yellow) for interactive elements — purple is primary
- Don't apply positive letter-spacing at display sizes — Stripe tracks tight
- Don't use the magenta/ruby accents for buttons or links — they're decorative/gradient only

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, reduced heading sizes, stacked cards |
| Tablet | 640–1024px | 2-column grids, moderate padding |
| Desktop | 1024–1280px | Full layout, 3-column feature grids |
| Large Desktop | >1280px | Centered content with generous margins |

### Touch Targets
- Buttons use comfortable padding (8–16px vertical)
- Navigation links at 14px with adequate spacing
- Badges have 6px horizontal padding minimum for tap targets
- Mobile nav toggle with 6px radius button

### Collapsing Strategy
- Hero: 56px display → 32px on mobile, weight 300 maintained
- Navigation: horizontal links + CTAs → hamburger toggle
- Feature cards: 3-column → 2-column → single column stacked
- Dark brand sections: maintain full-width treatment, reduce internal padding
- Financial data tables: horizontal scroll on mobile
- Section spacing: 64px+ → 40px on mobile
- Typography scale compresses across breakpoints

### Image Behavior
- Dashboard/product screenshots maintain blue-tinted shadow at all sizes
- Hero gradient decorations simplify on mobile
- Code blocks maintain `SourceCodePro` treatment, may horizontally scroll
- Card images maintain consistent 4–6px border-radius

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Stripe Purple (`{colors.primary}`)
- CTA Hover: Purple Dark (`{colors.primary-hover}`)
- Background: Pure White (`{colors.background}`)
- Heading text: Deep Navy (`{colors.ink}`)
- Body text: Slate (`{colors.ink-body}`)
- Label text: Dark Slate (`{colors.ink-label}`)
- Border: Soft Blue (`{colors.border}`)
- Link: Stripe Purple (`{colors.primary}`)
- Dark section: Brand Dark (`{colors.brand-dark}`)
- Success: Green (`{colors.success}`)
- Accent decorative: Ruby (`{colors.ruby}`), Magenta (`{colors.magenta}`)

### Example Component Prompts
- "Create a hero section on white background. Headline at 48px sohne-var weight 300, line-height 1.15, letter-spacing -0.96px, color `{colors.ink}`, font-feature-settings 'ss01'. Subtitle at 18px weight 300, line-height 1.40, color `{colors.ink-body}`. Purple CTA button (`{colors.primary}`, 4px radius, 8px 16px padding, white text) and ghost button (transparent, 1px solid `{colors.primary-light}`, `{colors.primary}` text, 4px radius)."
- "Design a card: white background, 1px solid `{colors.border}` border, 6px radius. Shadow: stacked blue-tinted (`{colors.shadow-blue}`) far + black (`{colors.shadow-black}`) near. Title at 22px sohne-var weight 300, letter-spacing -0.22px, color `{colors.ink}`, 'ss01'. Body at 16px weight 300, `{colors.ink-body}`."
- "Build a success badge: `{colors.success-bg}` background, `{colors.success-text}` text, 4px radius, 1px 6px padding, 10px sohne-var weight 300, border 1px solid `{colors.success-border}`."
- "Create navigation: white sticky header with backdrop-filter blur(12px). sohne-var 14px weight 400 for links, `{colors.ink}` text, 'ss01'. Purple CTA 'Start now' right-aligned (`{colors.primary}` bg, white text, 4px radius). Nav container 6px radius."
- "Design a dark brand section: `{colors.brand-dark}` background, white text. Headline 32px sohne-var weight 300, letter-spacing -0.64px, 'ss01'. Body 16px weight 300 in white at reduced opacity. Cards inside use light borders with 6px radius."

### Iteration Guide
1. Always enable `font-feature-settings: "ss01"` on sohne-var text — this is the brand's typographic DNA
2. Weight 300 is the default; use 400 only for buttons/links/navigation
3. Shadow formula: tinted `{colors.shadow-blue}` far + tinted `{colors.shadow-black}` near for the parallax effect
4. Heading color is `{colors.ink}` (deep navy), body is `{colors.ink-body}` (slate), labels are `{colors.ink-label}` (dark slate)
5. Border-radius stays in the 4–8px range — never pill shapes or large rounding
6. Use `tnum` for any numbers in tables, charts, or financial displays
7. Dark sections use `{colors.brand-dark}` — not black, not gray, but a deep branded indigo
8. SourceCodePro for code at 12px/500 with 2.00 line-height (very generous for readability)
