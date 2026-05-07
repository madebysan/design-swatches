---
version: alpha
name: Mintlify
description: Documentation-as-product design — luminous white canvas, brand green accent, Inter with tight negative tracking at display sizes, full-pill buttons, ultra-subtle 5% borders for separation.

colors:
  # Primary
  primary: "#18e299"
  ink: "#0d0d0d"
  background: "#ffffff"
  surface: "#ffffff"

  # Brand variants
  brand-green: "#18e299"
  brand-green-light: "#d4fae8"
  brand-green-deep: "#0fa76e"

  # Semantic
  warning: "#c37d0d"
  info: "#3772cf"
  error: "#d45656"

  # Neutral scale
  gray-900: "#0d0d0d"
  gray-700: "#333333"
  gray-500: "#666666"
  gray-400: "#888888"
  gray-200: "#e5e5e5"
  gray-100: "#f5f5f5"
  gray-50: "#fafafa"

  # Borders (opaque approximations of rgba alphas)
  border-subtle: "#f2f2f2"   # was rgba(0,0,0,0.05) — flattened over white
  border-medium: "#ebebeb"   # was rgba(0,0,0,0.08) — flattened over white

  # Inverted
  on-primary: "#0d0d0d"
  on-dark: "#ededed"

  # Dark mode
  background-dark: "#0d0d0d"
  surface-dark: "#141414"
  text-dark: "#ededed"
  text-dark-secondary: "#a0a0a0"
  border-dark: "#2e2e2e"     # was rgba(255,255,255,0.08) — flattened over #0d0d0d

  # Shadow tints (opaque approximations)
  shadow-card: "#f7f7f7"     # was rgba(0,0,0,0.03) — flattened
  shadow-button: "#f0f0f0"   # was rgba(0,0,0,0.06) — flattened

typography:
  display-hero:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 64px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -1.28px
  section-heading:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.8px
  sub-heading:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.24px
  card-title:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  card-title-light:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.2px
  body-large:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-medium:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  button:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  link:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  label-uppercase:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0.65px
  small:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: -0.26px
  mono-code:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0.6px
  mono-badge:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, monospace"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.6px
  mono-micro:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, monospace"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px

spacing:
  micro: 2px
  xs: 4px
  xs-plus: 6px
  sm: 8px
  sm-plus: 10px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px
  5xl: 96px

rounded:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  pill: 9999px

components:
  # Buttons
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.background}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 24px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.background}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 4.5px 12px
  button-nav:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    rounded: "{rounded.sm}"
    padding: 5px 6px
  button-brand:
    backgroundColor: "{colors.brand-green}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 24px

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  card-featured:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 32px
  card-trust:
    backgroundColor: "{colors.gray-50}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: 24px

  # Inputs
  input-email:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  input-email-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"

  # Navigation
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    padding: 16px 24px

  # Badges
  badge-green:
    backgroundColor: "{colors.brand-green-light}"
    textColor: "{colors.brand-green-deep}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  badge-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.background}"
    typography: "{typography.mono-badge}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  badge-info:
    backgroundColor: "{colors.info}"
    textColor: "{colors.background}"
    typography: "{typography.mono-badge}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  badge-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.background}"
    typography: "{typography.mono-badge}"
    rounded: "{rounded.pill}"
    padding: 4px 12px

  # Code chip / inline
  code-inline:
    backgroundColor: "{colors.gray-100}"
    textColor: "{colors.gray-700}"
    typography: "{typography.mono-code}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
---

# Mintlify Design System

## Overview

Mintlify's website is a study in documentation-as-product design — a white, airy, information-rich surface that treats clarity as its highest aesthetic value. The page opens with a luminous white (`{colors.background}`) background, near-black (`{colors.ink}`) text, and a signature green brand accent (`{colors.brand-green}`) that signals freshness and intelligence without dominating the palette. The overall mood is calm, confident, and engineered for legibility — a design system that whispers "we care about your developer experience" in every pixel.

The Inter font family carries the entire typographic load. At display sizes (40–64px), it uses tight negative letter-spacing (-0.8px to -1.28px) and semibold weight (600), creating headlines that feel focused and compressed like well-written documentation headers. Body text at 16–18px with 150% line-height provides generous reading comfort. Geist Mono appears exclusively for code and technical labels — uppercase, tracked-out, small — the voice of the terminal inside the marketing page.

What distinguishes Mintlify from other documentation platforms is its atmospheric gradient hero. A soft, cloud-like green-to-white gradient wash behind the hero content creates a sense of ethereal intelligence — documentation that floats above the noise. Below the hero, the page settles into a disciplined alternation of white sections separated by subtle 5% opacity borders. Cards use generous padding (`{spacing.xl}`+) with large radii (`{rounded.md}`–`{rounded.lg}`) and whisper-thin borders, creating containers that feel open rather than boxed.

**Key Characteristics:**
- Inter with tight negative tracking at display sizes (-0.8px to -1.28px) — compressed yet readable
- Geist Mono for code labels: uppercase, 12px, tracked-out, the terminal voice
- Brand green (`{colors.brand-green}`) used sparingly — CTAs, hover states, focus rings, and accent touches
- Atmospheric gradient hero with cloud-like green-white wash
- Ultra-round corners: `{rounded.md}` for containers, `{rounded.lg}` for featured cards, `{rounded.pill}` for buttons and pills
- Subtle 5% opacity borders (`{colors.border-subtle}`) creating barely-there separation
- 8px base spacing system with generous section padding (`{spacing.3xl}`–`{spacing.5xl}`)
- Clean white canvas — no gray backgrounds, no color sections, depth through borders and whitespace alone

## Colors

### Primary
- **Near Black** (`{colors.ink}`): Primary text, headings, dark surfaces. Not pure black — the micro-softness improves reading comfort.
- **Pure White** (`{colors.background}`): Page background, card surfaces, input backgrounds.
- **Brand Green** (`{colors.brand-green}`): The signature accent — CTAs, links on hover, focus rings, brand identity.

### Secondary Accents
- **Brand Green Light** (`{colors.brand-green-light}`): Tinted green surface for badges, hover states, subtle backgrounds.
- **Brand Green Deep** (`{colors.brand-green-deep}`): Darker green for text on light-green badges, hover states on brand elements.
- **Warm Amber** (`{colors.warning}`): Warning states, caution badges.
- **Soft Blue** (`{colors.info}`): Tag backgrounds, informational annotations.
- **Error Red** (`{colors.error}`): Error states, destructive actions.

### Neutral Scale
- **Gray 900** (`{colors.gray-900}`): Primary heading text, nav links.
- **Gray 700** (`{colors.gray-700}`): Secondary text, descriptions, body copy.
- **Gray 500** (`{colors.gray-500}`): Tertiary text, muted labels.
- **Gray 400** (`{colors.gray-400}`): Placeholder text, disabled states, code annotations.
- **Gray 200** (`{colors.gray-200}`): Borders, dividers, card outlines.
- **Gray 100** (`{colors.gray-100}`): Subtle surface backgrounds, hover states.
- **Gray 50** (`{colors.gray-50}`): Near-white surface tint.

### Interactive
- **Link Default** (`{colors.ink}`): Links match text color, relying on underline/context.
- **Link Hover** (`{colors.brand-green}`): Brand green on hover.
- **Focus Ring** (`{colors.brand-green}`): Brand green focus outline for inputs and interactive elements.

### Surface & Overlay
- **Card Background** (`{colors.surface}`): White cards on white background, separated by borders.
- **Border Subtle** (`{colors.border-subtle}`): 5% black opacity borders — the primary separation mechanism (was `rgba(0,0,0,0.05)`).
- **Border Medium** (`{colors.border-medium}`): Slightly stronger borders for interactive elements.

### Shadows & Depth
- **Card Shadow** (`{colors.shadow-card}` `0px 2px 4px`): Barely-there ambient shadow for subtle lift.
- **Button Shadow** (`{colors.shadow-button}` `0px 1px 2px`): Micro-shadow for button depth.
- **No heavy shadows**: Mintlify relies on borders, not shadows, for depth.

## Typography

### Font Family
- **Primary**: `Inter`, with fallback: `Inter Fallback, system-ui, -apple-system, sans-serif`
- **Monospace**: `Geist Mono`, with fallback: `Geist Mono Fallback, ui-monospace, SFMono-Regular, monospace`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference each role via tokens.

| Token | Use |
|---|---|
| `display-hero` | Maximum impact, hero headlines |
| `section-heading` | Feature section titles |
| `sub-heading` | Card headings, sub-sections |
| `card-title` | Feature card titles |
| `card-title-light` | Secondary card headings |
| `body-large` | Hero descriptions, introductions |
| `body` | Standard reading text |
| `body-medium` | Navigation, emphasized text |
| `button` | Button labels |
| `link` | Navigation links, small CTAs |
| `caption` | Metadata, descriptions |
| `label-uppercase` | Section labels (uppercase, tracked +0.65px) |
| `small` | Small body text |
| `mono-code` | Technical labels (uppercase, Geist Mono) |
| `mono-badge` | Status badges (uppercase, weight 600) |
| `mono-micro` | Tiny labels (uppercase) |

### Principles
- **Tight tracking at display sizes**: Inter at 40–64px uses -0.8px to -1.28px letter-spacing. This compression creates headlines that feel deliberate and space-efficient — documentation headings, not billboard copy.
- **Relaxed reading at body sizes**: 16–18px body text uses normal tracking with 150% line-height, creating generous reading lanes. Documentation demands comfort.
- **Two-font system**: Inter for all human-readable content, Geist Mono exclusively for technical/code contexts. The boundary is strict — no mixing.
- **Uppercase as hierarchy signal**: Section labels and technical tags use uppercase + positive tracking (0.6px–0.65px) as a clear visual delimiter between content types.
- **Three weights**: 400 (body/reading), 500 (UI/navigation/emphasis), 600 (headings/titles). No bold (700) in the system.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is `{spacing.sm}` (8px).
- Section padding: `{spacing.3xl}`–`{spacing.5xl}` vertical
- Card padding: `{spacing.xl}`–`{spacing.2xl}`
- Component gaps: `{spacing.sm}`–`{spacing.lg}`

### Grid & Container
- Max content width: approximately 1200px
- Hero: centered single-column with generous top padding (`{spacing.5xl}`+)
- Feature sections: 2–3 column CSS Grid for cards
- Full-width sections with contained content
- Consistent horizontal padding: `{spacing.xl}` (mobile) to `{spacing.2xl}` (desktop)

### Whitespace Philosophy
- **Documentation-grade breathing room**: Every element has generous surrounding whitespace. Mintlify sells documentation, so the marketing page itself demonstrates reading comfort.
- **Sections as chapters**: Each feature section is a self-contained unit with `{spacing.3xl}`–`{spacing.5xl}` vertical padding, creating clear "chapter breaks."
- **Content density is low**: Unlike developer tools that pack the page, Mintlify uses 1–2 key messages per section with supporting imagery.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Page background, text blocks |
| Subtle Border (Level 1) | `1px solid {colors.border-subtle}` | Standard card borders, dividers |
| Medium Border (Level 1b) | `1px solid {colors.border-medium}` | Interactive elements, input borders |
| Ambient Shadow (Level 2) | `{colors.shadow-card}` `0 2px 4px` | Cards with subtle lift |
| Button Shadow (Level 2b) | `{colors.shadow-button}` `0 1px 2px` | Button micro-depth |
| Focus Ring (Accessibility) | `1px solid {colors.brand-green}` outline | Focused inputs, active interactive elements |

**Shadow Philosophy**: Mintlify barely uses shadows. The depth system is almost entirely border-driven — ultra-subtle 5% opacity borders create separation without visual weight. When shadows appear, they're atmospheric whispers (3% opacity, 2px blur, 4px spread) that add the barest sense of lift. This restraint keeps the page feeling flat and paper-like — appropriate for a documentation company whose product is about clarity and readability.

### Decorative Depth
- Hero gradient: atmospheric green-white cloud gradient behind hero content
- No background color alternation — white on white throughout
- Depth comes from border opacity variation (5% → 8%) and whitespace

## Shapes

| Token | Value | Use |
|---|---|---|
| `xs` | 4px | Inline code, small tags, tooltips |
| `sm` | 8px | Nav buttons, transparent buttons, small containers |
| `md` | 16px | Cards, content containers, image wrappers |
| `lg` | 24px | Featured cards, hero containers, section panels |
| `pill` | 9999px | Buttons, inputs, badges, pills — the signature shape |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (e.g. `{components.button-primary}`, `{components.card-featured}`) rather than reconstructing them.

### Buttons
- **`button-primary`** — Near-black pill CTA. Signature primary action ("Get Started", "Start Building").
- **`button-secondary`** — White ghost pill with `{colors.border-medium}` border. Used for "Request Demo", "View Docs".
- **`button-nav`** — Transparent nav-item button with `{rounded.sm}` corners.
- **`button-brand`** — Brand-green pill, reserved for special promotional CTAs.

### Cards
- **`card`** — White surface, `{rounded.md}` corners, 1px `{colors.border-subtle}` border, `{spacing.xl}` padding, ambient `{colors.shadow-card}` lift.
- **`card-featured`** — Larger `{rounded.lg}` radius, `{spacing.2xl}` padding. Inner content can carry its own `{rounded.md}` containers.
- **`card-trust`** — `{colors.gray-50}` or white surface with consistent logo sizing for the "loved by" trust grid.

### Inputs
- **`input-email`** — Pill-shaped (`{rounded.pill}`) input matching button geometry. Focus ring `1px solid {colors.brand-green}`.

### Navigation
- **`nav-bar`** — Sticky white header with backdrop-filter blur. Brand logotype left, links center, dark pill CTA right. Bottom border in `{colors.border-subtle}`.

### Badges
- **`badge-green`** — Brand-green light fill with deep-green text, uppercase mono.
- **`badge-warning`** / **`badge-info`** / **`badge-error`** — semantic color fills for advisory states.

### Code
- **`code-inline`** — Light gray (`{colors.gray-100}`) chip, Geist Mono, 4px corners.

### Distinctive Patterns
- **Atmospheric Hero** — Full-width gradient wash (soft green → white) behind centered hero content, dual CTA pair (dark primary + ghost secondary).
- **Trust Bar / Logo Grid** — Company logos in muted grayscale; subtle border separation; uppercase tracked-out section label above.
- **Feature Cards with Icons** — Icon at top, `{typography.card-title}` heading, gray description, 2–3 column grid on desktop.
- **CTA Footer Section** — Dark or gradient background, large headline, pill email input, brand green accent on CTAs.

## Do's and Don'ts

### Do
- Always use full-pill radius (`{rounded.pill}`) for buttons and inputs — this is Mintlify's signature shape
- Keep borders at `{colors.border-subtle}` (5% opacity) — stronger borders break the airy feeling
- Letter-spacing scales with font size: -1.28px at 64px, -0.8px at 40px, -0.24px at 24px, normal at 16px
- Use only three weights: 400 (read), 500 (interact), 600 (announce)
- Reserve brand green (`{colors.brand-green}`) for CTAs and hover states — never for decorative fills
- Use Geist Mono uppercase for technical labels, Inter for everything else
- Keep section padding generous: `{spacing.4xl}`–`{spacing.5xl}` on desktop, `{spacing.3xl}` on mobile
- Maintain a white canvas throughout — separation through borders and whitespace, not background color

### Don't
- Don't use heavy shadows — Mintlify relies on borders, not shadows, for depth
- Don't introduce gray background sections — white throughout is the rule
- Don't use bold (weight 700) anywhere — the system tops out at 600
- Don't mix Inter and Geist Mono inside the same component (badges/labels can be all-mono)
- Don't apply brand green to body text or large fills — accent only
- Don't use mid-range corner radii on buttons — full pill or none
- Don't add background color alternation between sections — depth comes from borders and air

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Single column, stacked layout, hamburger nav |
| Tablet | 768–1024px | Two-column grids begin, expanded padding |
| Desktop | >1024px | Full layout, 3-column grids, maximum content width |

### Touch Targets
- Buttons with full-pill shape have comfortable 8px+ vertical padding
- Navigation links spaced with adequate 16px+ gaps
- Mobile menu provides full-width tap targets

### Collapsing Strategy
- Hero: 64px → 40px headline, maintains tight tracking proportionally
- Navigation: horizontal links + CTA → hamburger menu at 768px
- Feature cards: 3-column → 2-column → single column stacked
- Section spacing: 96px → 48px on mobile
- Footer: multi-column → stacked single column
- Trust bar: grid → horizontal scroll or stacked

### Image Behavior
- Product screenshots maintain aspect ratio with responsive containers
- Hero gradient simplifies on mobile
- Full-width sections maintain edge-to-edge treatment

### Dark Mode
- **Background**: `{colors.background-dark}`
- **Text Primary**: `{colors.text-dark}`
- **Text Secondary**: `{colors.text-dark-secondary}`
- **Brand Green**: `{colors.brand-green}` (unchanged — works on both backgrounds)
- **Border**: `{colors.border-dark}`
- **Card Background**: `{colors.surface-dark}` (slightly lighter than page)
- Buttons invert: white background dark text becomes dark background light text. Focus ring remains brand green. Hero gradient shifts to dark-tinted green atmospheric wash.

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Near Black (`#0d0d0d`)
- Background: Pure White (`#ffffff`)
- Heading text: Near Black (`#0d0d0d`)
- Body text: Gray 700 (`#333333`)
- Border: `rgba(0,0,0,0.05)` (5% opacity)
- Brand accent: Green (`#18E299`)
- Link hover: Brand Green (`#18E299`)
- Focus ring: Brand Green (`#18E299`)

### Example Component Prompts
- "Create a hero section on white background with atmospheric green-white gradient wash. Headline at 64px Inter weight 600, line-height 1.15, letter-spacing -1.28px, color #0d0d0d. Subtitle at 18px Inter weight 400, line-height 1.50, color #666666. Dark pill CTA (#0d0d0d, 9999px radius, 8px 24px padding) and ghost pill button (white, 1px solid rgba(0,0,0,0.08), 9999px radius)."
- "Design a card: white background, 1px solid rgba(0,0,0,0.05) border, 16px radius, 24px padding, shadow rgba(0,0,0,0.03) 0px 2px 4px. Title at 20px Inter weight 600, letter-spacing -0.2px. Body at 14px weight 400, #666666."
- "Build a pill badge: #d4fae8 background, #0fa76e text, 9999px radius, 4px 12px padding, 13px Inter weight 500, uppercase."
- "Create navigation: white sticky header with backdrop-filter blur(12px). Inter 15px weight 500 for links, #0d0d0d text. Dark pill CTA 'Get Started' right-aligned, 9999px radius. Bottom border: 1px solid rgba(0,0,0,0.05)."
- "Design a trust section showing company logos in muted gray. Grid layout with 16px radius containers, 1px border at 5% opacity. Label above: 'Loved by your favorite companies' at 13px Inter weight 500, uppercase, tracking 0.65px."

### Iteration Guide
1. Always use full-pill radius (9999px) for buttons and inputs — this is Mintlify's signature shape
2. Keep borders at 5% opacity (`rgba(0,0,0,0.05)`) — stronger borders break the airy feeling
3. Letter-spacing scales with font size: -1.28px at 64px, -0.8px at 40px, -0.24px at 24px, normal at 16px
4. Three weights only: 400 (read), 500 (interact), 600 (announce)
5. Brand green (`#18E299`) is used sparingly — CTAs and hover states only, never for decorative fills
6. Geist Mono uppercase for technical labels, Inter for everything else
7. Section padding is generous: 64px–96px on desktop, 48px on mobile
8. No gray background sections — white throughout, separation through borders and whitespace
