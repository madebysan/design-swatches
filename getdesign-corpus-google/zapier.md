---
version: alpha
name: Zapier
description: Warm, approachable professionalism — cream-tinted canvas, near-black with reddish undertone, Zapier Orange accent, three-font system (Degular Display + Inter + GT Alpina), border-forward design with sand neutrals.

colors:
  # Primary
  background: "#fffefb"        # Cream White
  surface: "#fffefb"
  surface-alt: "#fffdf9"       # Off-White
  ink: "#201515"                # Zapier Black — warm near-black with reddish undertone

  # Brand
  primary: "#ff4f00"            # Zapier Orange
  on-primary: "#fffefb"

  # Neutral scale
  ink-secondary: "#36342e"      # Dark Charcoal
  text-muted: "#939084"         # Warm Gray
  border: "#c5c0b1"             # Sand
  surface-soft: "#eceae3"       # Light Sand
  border-mid: "#b5b2aa"         # Mid Warm

  # Interactive
  link: "#201515"

  # Overlay surfaces
  overlay-dark: "#5b5b5c"       # was rgba(45,45,46,0.5) — flattened
  overlay-dark-solid: "#2d2d2e"

  # Active tab indicator (acts as accent)
  tab-active: "#ff4f00"
  tab-hover: "#c5c0b1"

  # Inverted (footer)
  footer-bg: "#201515"
  on-footer: "#fffefb"

typography:
  display-hero-xl:
    fontFamily: "Degular Display, Inter, sans-serif"
    fontSize: 80px
    fontWeight: 500
    lineHeight: 0.9
    letterSpacing: 0px
  display-hero:
    fontFamily: "Degular Display, Inter, sans-serif"
    fontSize: 56px
    fontWeight: 500
    lineHeight: 0.9
    letterSpacing: 0px
  display-hero-sm:
    fontFamily: "Degular Display, Inter, sans-serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 0.9
    letterSpacing: 0px
  display-button:
    fontFamily: "Degular Display, Inter, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 1px
  section-heading:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.04
    letterSpacing: 0px
  editorial-heading:
    fontFamily: "GT Alpina, Georgia, serif"
    fontSize: 48px
    fontWeight: 250
    lineHeight: 1.1
    letterSpacing: -1.92px
  editorial-sub:
    fontFamily: "GT Alpina, Georgia, serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -1.6px
  sub-heading-lg:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -1px
  sub-heading:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0px
  sub-heading-md:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0px
  card-title:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.48px
  body-large:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  body-emphasis:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  body:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.16px
  body-semibold:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.16
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0px
  button-sm:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0px
  caption-upper:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  micro:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0.5px

spacing:
  hairline: 1px
  xs: 4px
  fract-1: 6px
  sm: 8px
  fract-2: 10px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 40px
  5xl: 48px
  6xl: 56px
  7xl: 64px
  8xl: 72px

rounded:
  tight: 3px
  sm: 4px
  content: 5px
  md: 8px
  social: 14px
  pill: 20px

components:
  # Buttons
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 8px 16px

  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.md}"
    padding: 20px 24px
  button-dark-hover:
    backgroundColor: "{colors.border}"
    textColor: "{colors.ink}"

  button-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink-secondary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.md}"
    padding: 20px 24px
  button-light-hover:
    backgroundColor: "{colors.border}"
    textColor: "{colors.ink}"

  button-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-secondary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 0px 16px

  button-overlay:
    backgroundColor: "{colors.overlay-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 16px
  button-overlay-hover:
    backgroundColor: "{colors.overlay-dark-solid}"
    textColor: "{colors.on-primary}"

  # Tab navigation (uses inset shadow approximated via border-mid as visual bottom rule)
  tab-nav:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    padding: 12px 16px
  tab-nav-active:
    backgroundColor: "{colors.background}"
    textColor: "{colors.tab-active}"
    typography: "{typography.button-ui}"
    padding: 12px 16px

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.content}"
    padding: 24px
  card-featured:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 32px

  # Inputs
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.content}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
  input-placeholder:
    textColor: "{colors.text-muted}"
    typography: "{typography.body}"

  # Navigation
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    padding: 8px 12px

  # Stat / display
  stat-display:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.section-heading}"
    padding: 0px

  # Social icon
  social-icon:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.social}"
    padding: 8px

  # Workflow integration card
  card-integration:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.content}"
    padding: 16px

  # Footer
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-footer}"
    typography: "{typography.body}"
    padding: 48px 24px

  # Tight inline span
  inline-tight:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink-secondary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.tight}"
    padding: 2px 6px

  # Mid-warm border surface
  mid-divider:
    backgroundColor: "{colors.border-mid}"
    textColor: "{colors.ink}"
    padding: 0px

  # Tab hover indicator (sand)
  tab-nav-hover:
    backgroundColor: "{colors.background}"
    textColor: "{colors.tab-hover}"
    typography: "{typography.button-ui}"
    padding: 12px 16px

  # Link
  link-default:
    textColor: "{colors.link}"
    typography: "{typography.body}"
---

# Zapier Design System

## Overview

Zapier's website radiates warm, approachable professionalism. It rejects the cold monochrome minimalism of developer tools in favor of a cream-tinted canvas (`{colors.background}`) that feels like unbleached paper — the digital equivalent of a well-organized notebook. The near-black (`{colors.ink}`) text has a faint reddish-brown warmth, creating an atmosphere more human than mechanical. This is automation designed to feel effortless, not technical.

The typographic system is a deliberate interplay of two distinct personalities. **Degular Display** — a geometric, wide-set display face — handles hero-scale headlines at 56–80px with medium weight (500) and extraordinarily tight line-heights (0.90), creating headlines that compress vertically like stacked blocks. **Inter** serves as the workhorse for everything else, from section headings to body text and navigation, with fallbacks to Helvetica and Arial. **GT Alpina**, an elegant thin-weight serif with aggressive negative letter-spacing (-1.6px to -1.92px), makes occasional appearances for softer editorial moments. This three-font system gives Zapier the ability to shift register — from bold and punchy (Degular) to clean and functional (Inter) to refined and literary (GT Alpina).

The brand's signature orange (`{colors.primary}`) is unmistakable — a vivid, saturated red-orange that sits precisely between traffic-cone urgency and sunset warmth. It's used sparingly but decisively: primary CTA buttons, active state underlines, and accent borders. Against the warm cream background, this orange creates a color relationship that feels energetic without being aggressive.

**Key Characteristics:**
- Warm cream canvas (`{colors.background}`) instead of pure white — organic, paper-like warmth
- Near-black with reddish undertone (`{colors.ink}`) — text that breathes rather than dominates
- Degular Display for hero headlines at 0.90 line-height — compressed, impactful, modern
- Inter as the universal UI font across all functional typography
- GT Alpina for editorial accents — thin-weight serif with extreme negative tracking
- Zapier Orange (`{colors.primary}`) as the single accent — vivid, warm, sparingly applied
- Warm neutral palette: borders (`{colors.border}`), muted text (`{colors.text-muted}`), surface tints (`{colors.surface-soft}`)
- 8px base spacing system with generous padding on CTAs (20px 24px)
- Border-forward design: `1px solid` borders in warm grays define structure over shadows

## Colors

### Primary
- **Zapier Black** (`{colors.ink}`): Primary text, headings, dark button backgrounds. A warm near-black with reddish undertones — never cold.
- **Cream White** (`{colors.background}`): Page background, card surfaces, light button fills. Not pure white; the yellowish warmth is intentional.
- **Off-White** (`{colors.surface-alt}`): Secondary background surface, subtle alternate tint.

### Brand Accent
- **Zapier Orange** (`{colors.primary}`): Primary CTA buttons, active underline indicators, accent borders. The signature color — vivid and warm.

### Neutral Scale
- **Dark Charcoal** (`{colors.ink-secondary}`): Secondary text, footer text, border color for strong dividers.
- **Warm Gray** (`{colors.text-muted}`): Tertiary text, muted labels, timestamp-style content.
- **Sand** (`{colors.border}`): Primary border color, hover state backgrounds, divider lines.
- **Light Sand** (`{colors.surface-soft}`): Secondary button backgrounds, light borders, subtle card surfaces.
- **Mid Warm** (`{colors.border-mid}`): Alternate border tone, used on specific span elements.

### Interactive
- **Orange CTA** (`{colors.primary}`): Primary action buttons and active tab underlines.
- **Dark CTA** (`{colors.ink}`): Secondary dark buttons with sand hover state.
- **Light CTA** (`{colors.surface-soft}`): Tertiary/ghost buttons with sand hover.
- **Link Default** (`{colors.link}`): Standard link color, matching body text.

### Overlay & Surface
- **Semi-transparent Dark** (`{colors.overlay-dark}`): Overlay button variant, backdrop-like elements.
- **Pill Surface** (`{colors.surface}`): White pill buttons with sand borders.

### Shadows & Depth
- **Inset Underline (active)**: orange `{colors.tab-active}` -4px inset for active tab indicator.
- **Hover Underline**: sand `{colors.tab-hover}` -4px inset for inactive tab hover.

## Typography

### Font Families
- **Display**: Degular Display — wide geometric display face for hero headlines
- **Primary**: Inter, with fallbacks Helvetica, Arial
- **Editorial**: GT Alpina — thin-weight serif for editorial moments
- **System**: Arial — fallback for form elements and system UI

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-hero-xl` | 80px Degular Display — maximum impact |
| `display-hero` | 56px Degular Display — primary hero |
| `display-hero-sm` | 40px Degular Display — smaller hero |
| `display-button` | 24px Degular Display — large CTA button text |
| `section-heading` | 48px Inter 500 — major section titles |
| `editorial-heading` | 48px GT Alpina 250 — thin editorial |
| `editorial-sub` | 40px GT Alpina 300 — editorial subhead |
| `sub-heading-lg` | 36px Inter 500 |
| `sub-heading` | 32px Inter 400 |
| `sub-heading-md` | 28px Inter 500 |
| `card-title` | 24px Inter 600 |
| `body-large` | 20px Inter — feature descriptions |
| `body-emphasis` | 18px Inter 600 |
| `body` | 16px Inter — standard reading |
| `body-semibold` | 16px Inter 600 — strong labels |
| `button-ui` | 16px Inter 600 |
| `button-sm` | 14px Inter 600 |
| `caption` | 14px Inter 500 |
| `caption-upper` | 14px Inter 600 with 0.5px tracking |
| `micro` | 12px Inter 600 with 0.5px tracking |

### Principles
- **Three-font system, clear roles**: Degular Display commands attention at hero scale only. Inter handles everything functional. GT Alpina adds editorial warmth sparingly.
- **Compressed display**: Degular at 0.90 line-height creates vertically compressed headline blocks.
- **Weight as hierarchy signal**: Inter uses 400 (reading), 500 (navigation/emphasis), 600 (headings/CTAs). Degular uses 500 (display) and 600 (buttons).
- **Uppercase for labels**: Section labels and small categorization use `text-transform: uppercase` with 0.5px letter-spacing.
- **Negative tracking for elegance**: GT Alpina uses -1.6px to -1.92px letter-spacing for its thin-weight editorial headlines.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

CTA buttons use generous padding: 20px 24px for large, 8px 16px for standard. Section padding: `7xl`–`8xl` (64–80px) vertical.

### Grid & Container
- Max content width: ~1200px
- Hero: centered single-column with large top padding
- Feature sections: 2–3 column grids for integration cards
- Full-width sand-bordered dividers between sections
- Footer: multi-column dark background

### Whitespace Philosophy
- **Warm breathing room**: generous vertical spacing between sections, but content areas are relatively dense.
- **Architectural compression**: Degular Display headlines at 0.90 line-height compress vertically.
- **Section rhythm**: cream background throughout, sections separated by sand-colored borders rather than background changes.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Page background, text blocks |
| Bordered (Level 1) | `1px solid {colors.border}` | Standard cards, containers, inputs |
| Strong Border (Level 1b) | `1px solid {colors.ink-secondary}` | Dark dividers, emphasized sections |
| Active Tab (Level 2) | `{colors.tab-active}` 0px -4px inset | Active tab underline (orange) |
| Hover Tab (Level 2b) | `{colors.tab-hover}` 0px -4px inset | Hover tab underline (sand) |
| Focus | `1px solid {colors.primary}` outline | Focus ring on interactive elements |

**Shadow Philosophy**: Zapier deliberately avoids traditional shadow-based elevation. Structure is defined almost entirely through borders — warm sand for standard containment, dark charcoal for emphasis. The only shadow-like technique is the inset box-shadow for tab underlines.

### Decorative Depth
- Orange inset underline on active tabs creates visual "weight" at the bottom of elements
- Sand hover underlines provide preview states without layout shifts
- No background gradients in main content
- Footer uses full dark background for contrast reversal

## Shapes

| Token | Value | Use |
|---|---|---|
| `tight` | 3px | Small inline spans |
| `sm` | 4px | Buttons (orange CTA), tags, small elements |
| `content` | 5px | Cards, links, general containers |
| `md` | 8px | Featured cards, large buttons, tabs |
| `social` | 14px | Social icon buttons |
| `pill` | 20px | Play buttons, large pill buttons |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Zapier Orange, 4px radius, 8px 16px padding. Primary CTA.
- **`button-dark`** — Zapier Black, 8px radius, 20px 24px padding. Hover shifts to sand.
- **`button-light`** — Light Sand background, sand border, 8px radius, 20px 24px padding. Hover shifts to sand.
- **`button-pill`** — White pill, sand border, 20px radius. Filter pills.
- **`button-overlay`** — Semi-transparent dark, 20px radius. Video play buttons, floating actions.

### Tab Navigation
- Active tab uses `{colors.tab-active}` orange inset underline
- Hover tab uses `{colors.tab-hover}` sand inset underline
- Padding 12px 16px

### Cards & Containers
- **`card`** — Cream background, `1px solid {colors.border}`, 5px radius.
- **`card-featured`** — 8px radius, 32px padding.
- No box-shadow elevation — borders define containment.

### Inputs
- Cream background, `1px solid {colors.border}`, 5px radius
- Focus: border shifts to `{colors.primary}` (orange)
- Placeholder: `{colors.text-muted}`

### Navigation
- Clean horizontal nav on cream background
- Inter 16px weight 500, ink text
- Orange button CTA "Start free with email"
- Tab navigation uses inset box-shadow underline technique

### Distinctive Components
- **Workflow Integration Cards** — connected app icons in pairs with sand border containment
- **Stat Counter** — large display number using Inter 48px weight 500
- **Social Proof Icons** — circular icon buttons with sand borders

## Do's and Don'ts

### Do
- Use Degular Display exclusively for hero-scale headlines (40px+) with 0.90 line-height
- Use Inter for all functional UI — navigation, body text, buttons, labels
- Apply warm cream (`{colors.background}`) as the background, never pure white
- Use `{colors.ink}` for text, never pure black — the reddish warmth matters
- Keep Zapier Orange (`{colors.primary}`) reserved for primary CTAs and active state indicators
- Use sand (`{colors.border}`) borders as the primary structural element instead of shadows
- Apply generous button padding (20px 24px) for large CTAs
- Use inset box-shadow underlines for tab navigation rather than border-bottom
- Apply uppercase with 0.5px letter-spacing for section labels and micro-categorization

### Don't
- Don't use Degular Display for body text or UI elements — it's display-only
- Don't use pure white (`#ffffff`) or pure black (`#000000`) — Zapier's palette is warm-shifted
- Don't apply box-shadow elevation to cards — use borders instead
- Don't scatter Zapier Orange across the UI — it's reserved for CTAs and active states
- Don't use tight padding on large CTA buttons
- Don't ignore the warm neutral system — borders should be `{colors.border}`, not gray
- Don't use GT Alpina for functional UI — it's an editorial accent at thin weights only
- Don't apply positive letter-spacing to GT Alpina — it uses aggressive negative tracking
- Don't use rounded pill shapes (9999px) for primary buttons — pills are for tags and social icons

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <450px | Tight single column, reduced hero text |
| Mobile | 450-600px | Standard mobile, stacked layout |
| Mobile Large | 600-640px | Slight horizontal breathing room |
| Tablet Small | 640-680px | 2-column grids begin |
| Tablet | 680-768px | Card grids expand |
| Tablet Large | 768-991px | Full card grids, expanded padding |
| Desktop Small | 991-1024px | Desktop layout initiates |
| Desktop | 1024-1280px | Full layout, maximum content width |
| Large Desktop | >1280px | Centered with generous margins |

### Touch Targets
- Large CTA buttons: 20px 24px padding (comfortable 60px+ height)
- Standard buttons: 8px 16px padding
- Navigation links: 16px weight 500 with adequate spacing
- Social icons: 14px radius circular buttons
- Tab items: 12px 16px padding

### Collapsing Strategy
- Hero: Degular 80px display scales to 40-56px on smaller screens
- Navigation: horizontal links + CTA collapse to hamburger menu
- Feature cards: 3-column grid to 2-column to single-column stacked
- Integration workflow illustrations: maintain aspect ratio, may simplify
- Footer: multi-column dark section collapses to stacked
- Section spacing: 64-80px reduces to 40-48px on mobile

### Image Behavior
- Product screenshots maintain sand border treatment at all sizes
- Integration app icons maintain fixed sizes within responsive containers
- Hero illustrations scale proportionally
- Full-width sections maintain edge-to-edge treatment

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Zapier Orange (`{colors.primary}`)
- Background: Cream White (`{colors.background}`)
- Heading text: Zapier Black (`{colors.ink}`)
- Body text: Dark Charcoal (`{colors.ink-secondary}`)
- Border: Sand (`{colors.border}`)
- Secondary surface: Light Sand (`{colors.surface-soft}`)
- Muted text: Warm Gray (`{colors.text-muted}`)

### Example Component Prompts
- "Create a hero section on cream background (`{colors.background}`). Headline at 56px Degular Display weight 500, line-height 0.90, color `{colors.ink}`. Subtitle at 20px Inter weight 400, line-height 1.20, color `{colors.ink-secondary}`. Orange CTA button (`{colors.primary}`, 4px radius, 8px 16px padding, white text) and dark button (`{colors.ink}`, 8px radius, 20px 24px padding, white text)."
- "Design a card: cream background (`{colors.background}`), `1px solid {colors.border}` border, 5px radius. Title at 24px Inter weight 600, letter-spacing -0.48px, `{colors.ink}`. Body at 16px weight 400, `{colors.ink-secondary}`. No box-shadow."
- "Build a tab navigation: transparent background. Inter 16px weight 500, `{colors.ink}` text. Active tab: orange (`{colors.tab-active}`) 0px -4px inset shadow. Hover: sand (`{colors.tab-hover}`) 0px -4px inset. Padding 12px 16px."
- "Create navigation: cream sticky header (`{colors.background}`). Inter 16px weight 500 for links, `{colors.ink}` text. Orange pill CTA right-aligned (`{colors.primary}`, 4px radius, 8px 16px padding)."
- "Design a footer with dark background (`{colors.footer-bg}`). Text `{colors.on-footer}`. Links in `{colors.border}` with hover to `{colors.on-footer}`. Multi-column layout. Social icons as 14px-radius circles with sand borders."

### Iteration Guide
1. Always use warm cream (`{colors.background}`) background, never pure white — the warmth defines Zapier
2. Borders (`1px solid {colors.border}`) are the structural backbone — avoid shadow elevation
3. Zapier Orange (`{colors.primary}`) is the only accent color; everything else is warm neutrals
4. Three fonts, strict roles: Degular Display (hero), Inter (UI), GT Alpina (editorial)
5. Large CTA buttons need generous padding (20px 24px) — Zapier buttons feel spacious
6. Tab navigation uses inset box-shadow underlines, not border-bottom
7. Text is always warm: `{colors.ink}` for dark, `{colors.ink-secondary}` for body, `{colors.text-muted}` for muted
8. Uppercase labels at 12-14px with 0.5px letter-spacing for section categorization
