---
version: alpha
name: Uber
description: Confident black-and-white minimalism — UberMove Bold billboard headlines, UberMoveText body, pill-shaped (999px) buttons and chips, whisper-soft 0.12-0.16 shadows, warm illustrations against monochrome chrome.

colors:
  # Canvas + ink
  background: "#ffffff"
  surface: "#ffffff"
  surface-dark: "#000000"
  ink: "#000000"
  ink-inverted: "#ffffff"

  # Brand — primary CTA
  primary: "#000000"
  on-primary: "#ffffff"

  # Interactive states
  hover-gray: "#e2e2e2"
  hover-light: "#f3f3f3"
  chip-gray: "#efefef"
  press-tint: "#ebebeb"  # was rgba(0,0,0,.08) — flattened over white

  # Text hierarchy
  on-background: "#000000"
  on-surface-dark: "#ffffff"
  text-secondary: "#4b4b4b"
  text-muted: "#afafaf"

  # Borders
  border: "#000000"

  # Link states
  link-blue: "#0000ee"

  # Shadow tints (opaque approximations)
  shadow-card: "#e0e0e0"     # was rgba(0,0,0,.12) — flattened over white
  shadow-medium: "#d6d6d6"   # was rgba(0,0,0,.16) — flattened over white

typography:
  display:
    fontFamily: "UberMove, UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0px
  section-heading:
    fontFamily: "UberMove, UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: 0px
  card-title:
    fontFamily: "UberMove, UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0px
  sub-heading:
    fontFamily: "UberMove, UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0px
  small-heading:
    fontFamily: "UberMove, UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.40
    letterSpacing: 0px
  nav-large:
    fontFamily: "UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0px
  body:
    fontFamily: "UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button-ui:
    fontFamily: "UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  caption:
    fontFamily: "UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  micro:
    fontFamily: "UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.67
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 64px
  4xl: 96px

rounded:
  none: 0px
  sm: 8px
  md: 12px
  pill: 9999px

components:
  # Primary black pill CTA
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 10px 12px

  # Secondary white pill
  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 10px 12px
  button-secondary-hover:
    backgroundColor: "{colors.hover-gray}"

  # Chip / filter
  button-chip:
    backgroundColor: "{colors.chip-gray}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 14px 16px
  button-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"

  # Floating action — white with shadow
  button-floating:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 14px
  button-floating-hover:
    backgroundColor: "{colors.hover-light}"

  # Card — standard
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: 24px

  # Featured card
  card-featured:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 32px

  # Input
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    borderColor: "{colors.border}"

  # Top nav bar
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-large}"
    padding: 16px 24px

  # Footer (dark)
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-surface-dark}"
    typography: "{typography.body}"
    padding: 64px 24px

  # Footer link
  footer-link:
    textColor: "{colors.text-muted}"
    typography: "{typography.caption}"
  footer-link-hover:
    textColor: "{colors.on-surface-dark}"
---

# Uber Design System

## Overview

Uber's design language is a masterclass in confident minimalism — a black-and-white universe where every pixel serves a purpose and nothing decorates without earning its place. The entire experience is built on a stark duality: jet black (`{colors.ink}`) and pure white (`{colors.background}`), with virtually no mid-tone grays diluting the message. This isn't the sterile minimalism of a startup that hasn't finished designing — it's the deliberate restraint of a brand so established it can afford to whisper.

The signature typeface, UberMove, is a proprietary geometric sans-serif with a distinctly square, engineered quality. Headlines in UberMove Bold at 52px carry the weight of a billboard — authoritative, direct, unapologetic. The companion face UberMoveText handles body copy and buttons with a slightly softer, more readable character at medium weight (500). Together, they create a typographic system that feels like a transit map: clear, efficient, built for scanning at speed.

What makes Uber's design truly distinctive is its use of full-bleed photography and illustration paired with pill-shaped interactive elements (`{rounded.pill}`). Navigation chips, CTA buttons, and category selectors all share this capsule shape, creating a tactile, thumb-friendly interface language that's unmistakably Uber. The illustrations — warm, slightly stylized scenes of drivers, riders, and cityscapes — inject humanity into what could otherwise be a cold, monochrome system. The site alternates between white content sections and a full-black footer, with card-based layouts using the gentlest possible shadows to create subtle lift without breaking the flat aesthetic.

**Key Characteristics:**
- Pure black-and-white foundation with virtually no mid-tone grays in UI chrome
- UberMove (headlines) + UberMoveText (body/UI) — proprietary geometric sans-serif family
- Pill-shaped everything: buttons, chips, nav items all use `{rounded.pill}` border-radius
- Warm, human illustrations contrasting the stark monochrome interface
- Card-based layout with whisper-soft shadows (0.12-0.16 opacity)
- 8px spacing grid with compact, information-dense layouts
- Bold photography integrated as full-bleed hero backgrounds
- Black footer anchoring the page with a dark, high-contrast environment

## Colors

### Primary
- **Uber Black** (`{colors.ink}`): The defining brand color — used for primary buttons, headlines, navigation text, and footer. True, uncompromising black.
- **Pure White** (`{colors.background}`): Primary surface color and inverse text. Page backgrounds, card surfaces, text on black elements.

### Interactive & Button States
- **Hover Gray** (`{colors.hover-gray}`): White button hover state — clean cool light gray.
- **Hover Light** (`{colors.hover-light}`): Subtle hover for elevated white buttons — barely-there gray.
- **Chip Gray** (`{colors.chip-gray}`): Background for secondary/filter buttons and navigation chips.

### Text & Content
- **Body Gray** (`{colors.text-secondary}`): Secondary text and footer links — true mid-gray, no warm/cool bias.
- **Muted Gray** (`{colors.text-muted}`): Tertiary text, de-emphasized footer links, placeholder.

### Borders & Separation
- **Border Black** (`{colors.border}`): Thin 1px borders for structural containment — used sparingly.

### Shadows & Depth
- **Shadow Card** (`{colors.shadow-card}`): Standard card elevation — featherweight lift.
- **Shadow Medium** (`{colors.shadow-medium}`): Slightly stronger elevation for floating action buttons.
- **Press Tint** (`{colors.press-tint}`): Inset effect for active/pressed states.

### Link States
- **Default Link Blue** (`{colors.link-blue}`): Standard browser blue for body links.
- **Link White** (`{colors.on-surface-dark}`): Links on dark surfaces.

Uber's design is **entirely gradient-free**. The black/white duality and flat color blocks create all visual hierarchy.

## Typography

### Font Family
- **Headline / Display**: `UberMove`, with fallbacks: `UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif`
- **Body / UI**: `UberMoveText`, with fallbacks: `system-ui, Helvetica Neue, Helvetica, Arial, sans-serif`

*Note: UberMove and UberMoveText are proprietary. For external implementations, use `system-ui` or Inter as the closest substitute. The geometric, square-proportioned character can be approximated with Inter or DM Sans.*

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display}`, `{typography.body}`, etc.).

| Token | Use |
|---|---|
| `display` | 52px hero — billboard presence |
| `section-heading` | Major section anchors |
| `card-title` | Card and feature headings |
| `sub-heading` | Secondary section headers |
| `small-heading` | Compact headings, list titles |
| `nav-large` | Navigation links, prominent UI text |
| `body` | Standard body text |
| `button-ui` | Button labels |
| `caption` | Metadata, descriptions, small links |
| `micro` | Fine print, legal text |

### Principles
- **Bold headlines, medium body**: UberMove headings are exclusively weight 700. UberMoveText body and UI uses 400-500.
- **Tight heading line-heights**: All headlines 1.22-1.40 — compact and punchy, designed for scanning.
- **Functional typography**: No letter-spacing, no text-transform, no ornamental sizing.
- **Two fonts, strict roles**: UberMove exclusively for headings. UberMoveText exclusively for body/buttons/UI.

## Layout

### Spacing System
The complete scale lives in the `spacing:` token block above. Base unit is 8px. Section vertical spacing: `{spacing.3xl}`–`{spacing.4xl}` between major sections.

### Grid & Container
- Max container width: approximately 1136px, centered
- Hero: split layout with text left, visual right
- Feature sections: 2-column card grids or full-width single-column
- Footer: multi-column link grid on black background

### Whitespace Philosophy
- **Efficient, not airy**: Functional whitespace — enough to separate, never empty. Transit-system spacing.
- **Content-dense cards**: Cards pack information tightly, relying on shadow and radius for boundaries.
- **Section breathing room**: Major sections get generous vertical spacing; within sections, elements are closely grouped.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, solid background | Page background, inline content |
| Subtle (Level 1) | `0 4px 16px {colors.shadow-card}` | Standard content cards, feature blocks |
| Medium (Level 2) | `0 4px 16px {colors.shadow-medium}` | Elevated cards, overlay elements |
| Floating (Level 3) | `0 2px 8px {colors.shadow-medium}` + translateY(2px) | Floating action buttons, map controls |
| Pressed (Level 4) | `inset {colors.press-tint}` | Active/pressed button states |
| Focus Ring | `0 0 0 2px inset {colors.on-primary}` | Keyboard focus indicators |

**Shadow Philosophy**: Uber uses shadow purely as a structural tool, never decoratively. Always black at very low opacity (0.08-0.16), creating bare minimum lift. No colored shadows, no layered stacks, no ambient glow. Depth is communicated more through black/white section contrast than shadow elevation.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved — no square corners on interactive |
| `sm` | 8px | Content cards, input fields, listboxes |
| `md` | 12px | Featured cards, larger containers |
| `pill` | 9999px | All buttons, chips, navigation items — non-negotiable |

## Components

The full component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card-featured}`).

### Buttons
- **`button-primary`** — Black pill, white text. The primary action.
- **`button-secondary`** — White pill, black text. Used on dark surfaces or alongside primary.
- **`button-chip`** — Chip Gray pill for filters and categories. Active inverts to black.
- **`button-floating`** — White pill with shadow + translateY for FABs.

### Cards
- **`card`** — White surface, `{rounded.sm}`, shadow-only definition.
- **`card-featured`** — `{rounded.md}` for promoted/featured content.

### Inputs
- **`input`** — White surface, 1px black border (the only place visible borders appear prominently), `{rounded.sm}`.

### Navigation
- **`nav-bar`** — Sticky white background with logo + pill chip nav. Mobile collapses to hamburger.

### Footer
- **`footer`** — Black background anchoring the page. White headings; muted footer links hover to white.

### Image Treatment
- Warm, hand-illustrated scenes (not photographs in feature sections)
- Slightly stylized people, contemporary vibe, warm tones
- Hero sections: bold photography or illustration as full-width backgrounds
- All imagery uses `{rounded.sm}` or `{rounded.md}` when contained in cards

### Distinctive Components
- **Category Pill Navigation** — Horizontal pills ("Ride", "Drive", "Business", "Uber Eats")
- **Hero with Dual Action** — Text/CTA left, map/illustration right; pickup/destination inputs side by side
- **Plan-Ahead Cards** — Illustration-heavy, warm imagery, black CTA at bottom

## Do's and Don'ts

### Do
- Use true black and pure white as the primary palette — the stark contrast IS Uber
- Use `{rounded.pill}` for all buttons, chips, and pill-shaped navigation
- Keep all headings in UberMove Bold (700) for billboard-level impact
- Use whisper-soft shadows for card elevation — barely visible
- Maintain compact, information-dense layouts — efficiency over airiness
- Use warm, human-centric illustrations to soften the monochrome interface
- Apply `{rounded.sm}` for content cards and `{rounded.md}` for featured containers
- Use UberMoveText weight 500 for navigation and prominent UI text
- Pair black primary buttons with white secondaries

### Don't
- Don't introduce color into UI chrome — strictly black, white, and gray
- Don't use rounded corners less than `{rounded.pill}` on buttons — pill shape is core identity
- Don't apply heavy shadows or high-opacity drop shadows
- Don't use serif fonts anywhere
- Don't create airy spacious layouts with excessive whitespace
- Don't use gradients or color overlays
- Don't mix UberMove into body or UberMoveText into headlines
- Don't use decorative borders
- Don't soften the black/white contrast with off-whites or near-blacks

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | 320px | Single column, stacked inputs, compact typography |
| Mobile | 600px | Stacked layout, hamburger nav |
| Tablet Small | 768px | Two-column grids begin, expanded card layouts |
| Tablet | 1119px | Full tablet layout, side-by-side hero content |
| Desktop Small | 1120px | Desktop grid activates, horizontal nav pills |
| Desktop | 1136px | Full desktop layout, maximum container width, split hero |

### Touch Targets
- All pill buttons: minimum 44px height
- Navigation chips: generous 14px 16px padding for thumb tapping
- Circular controls: 50% radius for large, easy-to-hit targets
- Card surfaces serve as full-area touch targets on mobile

### Collapsing Strategy
- Navigation: horizontal pill nav collapses to hamburger with circular toggle
- Hero: split layout (text + visual) stacks to single column
- Input fields: side-by-side pickup/destination stack vertically
- Feature cards: 2-column → full-width stacked
- Headings: 52px → 36px → 32px → 24px → 20px
- Footer: multi-column → accordion or stacked single column
- Category pills: horizontal scroll with overflow on smaller screens

### Image Behavior
- Illustrations scale proportionally within containers
- Hero imagery maintains aspect ratio; may crop on smaller screens
- QR code sections hide on mobile (app download shifts to direct store links)
- Card imagery maintains 8-12px border radius at all sizes

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Button: Uber Black `{colors.ink}`
- Page Background: Pure White `{colors.background}`
- Button Text (on black): Pure White `{colors.on-primary}`
- Button Text (on white): Uber Black `{colors.ink}`
- Secondary Text: Body Gray `{colors.text-secondary}`
- Tertiary Text: Muted Gray `{colors.text-muted}`
- Chip Background: Chip Gray `{colors.chip-gray}`
- Hover State: Hover Gray `{colors.hover-gray}`
- Card Shadow: `0 4px 16px {colors.shadow-card}`
- Footer Background: Uber Black `{colors.ink}`

### Example Component Prompts
- "Create a hero section on Pure White (`{colors.background}`) with a headline at 52px UberMove Bold (700), line-height 1.23. Use Uber Black (`{colors.ink}`) text. Add a subtitle in Body Gray (`{colors.text-secondary}`) at 16px UberMoveText weight 400 with 1.50 line-height. Place an Uber Black pill CTA button with Pure White text, 999px radius, padding 10px 12px."
- "Design a category navigation bar with horizontal pill buttons. Each pill: Chip Gray (`{colors.chip-gray}`) background, Uber Black (`{colors.ink}`) text, 14px 16px padding, 999px border-radius. Active pill inverts to Uber Black background with Pure White text."
- "Build a feature card on Pure White with 8px border-radius and shadow `0 4px 16px {colors.shadow-card}`. Title in UberMove at 24px weight 700, description in Body Gray at 16px UberMoveText. Add a black pill CTA button at the bottom."
- "Create a dark footer on Uber Black with Pure White heading text in UberMove at 20px weight 700. Footer links in Muted Gray (`{colors.text-muted}`) at 14px UberMoveText. Links hover to Pure White."
- "Design a floating action button with Pure White background, 999px radius, 14px padding, and shadow `0 2px 8px {colors.shadow-medium}`. Hover shifts background to `{colors.hover-light}`."

### Iteration Guide
1. Focus on ONE component at a time
2. Reference the strict black/white palette — "use Uber Black `{colors.ink}`" not "make it dark"
3. Always specify `{rounded.pill}` for buttons and pills — non-negotiable for the Uber identity
4. Describe the font family explicitly — "UberMove Bold for the heading, UberMoveText Medium for the label"
5. For shadows, use whisper shadow — never heavy drop shadows
6. Keep layouts compact and information-dense — efficient, not airy
7. Illustrations should be warm and human — describe "stylized people in warm tones"
8. Pair black CTAs with white secondaries for balanced dual-action layouts
