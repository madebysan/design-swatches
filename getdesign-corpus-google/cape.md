---
version: alpha
name: Cape
description: Precision-engineered minimalism for personal privacy and secure cellular service. Off-white canvas, FK Grotesk weight 300, single lavender accent, hard offset stamp shadows, sharp 0-radius corners.

colors:
  # Primary canvas + ink
  background: "#f5f5f5"
  surface: "#ffffff"
  ink: "#000000"
  ink-inverted: "#ffffff"

  # Brand accent — used sparingly
  primary: "#9891e1"
  primary-container: "#e9e4f4"

  # Text states
  on-background: "#000000"
  on-surface: "#000000"
  on-primary: "#000000"
  text-hover: "#5e646d"  # opaque approx of rgba(43,51,63,.75) over #f5f5f5 — Google format requires hex

  # Focus / interactive feedback (opaque approximations)
  focus-tint: "#b9c2cf"  # was rgba(115,133,159,.5) — flattened over white
  focus-ring: "#cccccc"  # was rgba(0,0,0,.2) — flattened over white

  # Borders
  border: "#000000"

  # Stamp shadow colors
  stamp-black: "#000000"
  stamp-white: "#ffffff"
  shadow-soft: "#e6e6e6"  # was rgba(0,0,0,.1) — flattened over white

typography:
  display-hero:
    fontFamily: "FK Grotesk, Arial, sans-serif"
    fontSize: 105px
    fontWeight: 300
    lineHeight: 1.0
    letterSpacing: -0.2px
  display-large:
    fontFamily: "FK Grotesk, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.0
    letterSpacing: -0.2px
  display:
    fontFamily: "FK Grotesk, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.48px
  heading-section:
    fontFamily: "FK Grotesk, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.0
    letterSpacing: -0.4px
  heading-sub-large:
    fontFamily: "FK Grotesk, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.36px
  heading-sub:
    fontFamily: "FK Grotesk, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.0
    letterSpacing: -0.28px
  heading-sub-small:
    fontFamily: "FK Grotesk, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.24px
  body-large:
    fontFamily: "FK Grotesk, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: -0.2px
  body:
    fontFamily: "FK Grotesk, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "FK Grotesk, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
  button-ui:
    fontFamily: "FK Grotesk, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.6px
  caption:
    fontFamily: "FK Grotesk, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-small:
    fontFamily: "FK Grotesk, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0

spacing:
  micro: 2.4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px
  5xl: 96px
  6xl: 128px

rounded:
  none: 0px
  soft: 3px
  pill: 9999px

components:
  # Top navigation
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
    textColor: "{colors.text-hover}"

  # Primary CTA — lavender stamp
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.none}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "rgba(50, 50, 50, 0.9)"
    textColor: "{colors.text-hover}"

  # Black inverted CTA
  button-inverted:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  button-inverted-hover:
    backgroundColor: "rgba(50, 50, 50, 0.9)"

  # Lilac secondary
  button-lilac:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.none}"
    padding: 8px 16px

  # Ghost / tertiary
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.none}"
    padding: 8px 16px

  # Circular pill (pagination dots, toggles)
  button-circular:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.pill}"
    size: 12px

  # Card — flat panel, generous interior padding
  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.none}"
    padding: 32px

  # Stamped card — signature offset shadow
  card-stamped:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.none}"
    padding: 32px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.focus-tint}"

  # Lavender badge
  badge-lavender:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.none}"
    padding: 2.4px 8px

  # Outline pill badge
  badge-outline:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 2.4px 8px
---

# Cape Design System

## Overview

Cape's design language is precision-engineered minimalism in service of a serious topic: personal privacy and secure cellular service. The page opens on a warm off-white canvas (`{colors.background}`) that deliberately avoids the sterile pure-white of typical privacy/security sites. Everything is built around an oversized grotesk headline, deep black body, and a single saturated lavender accent (`{colors.primary}`) that functions as a stamp — applied sparingly to signup CTAs, focus states, and occasional decorative moments. The overall impression is of a Swiss-inspired privacy brand that trusts typography to do the work most sites delegate to illustration.

The custom **FK Grotesk** typeface is the defining element of Cape's visual identity. Every display-size heading runs at weight 300 — an unusually light weight for a privacy/security brand, where the convention is bold reassurance. Cape chooses the opposite: whisper-confident headlines at 105px with negative letter-spacing and tight 1.0 line-height. The letterforms themselves carry the brand — structured, engineered, almost architectural in the way they lock to the grid. Where competitors use large colorful hero illustrations, Cape uses only type and a product photograph; the confidence comes from restraint.

What distinguishes Cape most is its **shadow system**. Rather than soft diffuse drop shadows, Cape uses hard offset shadows — `-3px 3px 0 #fff` and `-4px 4px 0 #000` — that create a dimensional, rubber-stamp effect. These are not elevation shadows in the traditional sense; they're graphic stamps that give interactive elements a tactile, almost printed quality. Combined with sharp 0-radius corners on most elements and the occasional fully-pill (`9999px`) circular element, Cape's system feels editorial and mechanical at the same time.

**Key Characteristics:**
- FK Grotesk at weight 300 for all display and heading text — confident lightness over bold reassurance
- Warm off-white canvas (`{colors.background}`) — deliberately not pure white, avoiding sterile tech aesthetic
- Lavender stamp accent (`{colors.primary}`) used exclusively for signup CTAs and focus moments
- Hard offset shadows (`-4px 4px 0 #000`) — rubber-stamp depth, not atmospheric lift
- Sharp 0-radius corners on most surfaces; pill (`9999px`) reserved for circular nav elements
- Tight negative letter-spacing scaling from `-0.2px` at display down to `-0.48px` at mid sizes
- Two-weight simplicity: 300 for content, 400 only for nav and uppercase UI chrome
- Large-scale type as the primary visual structure — typography IS the illustration

## Colors

### Primary
- **Cape Black** (`{colors.ink}`): Primary text, headings, body copy, secondary button backgrounds. Pure black — Cape does not soften its primary text color.
- **Cape Off-White** (`{colors.background}`): Primary page background. A warm neutral that reads as paper rather than screen.
- **Pure White** (`{colors.surface}`): Reserved for inverted surfaces, button text on dark, offset shadow highlights.

### Brand Accent
- **Cape Lavender** (`{colors.primary}`): The signature accent — applied to primary CTAs ("SIGN UP"), focus outlines, and selected-state indicators. The only chromatic color in the system.
- **Pale Lilac** (`{colors.primary-container}`): A tinted surface variant of lavender for background panels, badge fills, and soft lavender-themed containers. Used sparingly.

### Text States
- **Cape Black** (`{colors.ink}`): All primary text — headings, body, nav links, button labels.
- **Deep Focus Slate** (`{colors.text-hover}`): Hover text color — a desaturated blue-gray that creates a subtle "pressed" sensation.

### Focus / Interactive
- **Focus Gray** (`{colors.focus-tint}`): Focus-state background tint at 50% opacity for keyboard-focus feedback.
- **Focus Ring** (`{colors.focus-ring}`): `0px 0px 0px 2px` ring halo for keyboard accessibility.

### Borders
- **Border Black** (`{colors.border}`): Full-weight 1px borders around circular pill elements and framed containers.
- **Border Transparent** (`{colors.border-transparent}`): Default-state border on ghost buttons, becomes visible on hover.

### Shadows
- **Stamp Black** (`{colors.stamp-black}`): `-4px 4px 0 0` for the rubber-stamp effect on light surfaces.
- **Stamp White** (`{colors.stamp-white}`): `-3px 3px 0 0` inverted stamp for dark surfaces.
- **Shadow Soft** (`{colors.shadow-soft}`): `0px 4px 12px` subtle elevation on focus states.

**Cape is gradient-free.** No gradient fills anywhere — the lavender accent is always solid `{colors.primary}`. Solid-color relationships, hard offset shadows, and high contrast carry the entire system.

## Typography

### Font Family
- **Primary**: `FK Grotesk`, with fallback: `Arial`, `sans-serif`
- **OpenType Features**: Standard ligatures only — no stylistic sets. The typeface itself carries the character.

*Note: FK Grotesk is a commercial typeface from Florian Karsten Typefaces. For external implementations, Neue Haas Grotesk Display or Söhne serve as close substitutes; Inter at low weight works as a web-safe alternative.*

### Hierarchy

The complete type scale lives in the `typography:` token block above. Use those tokens directly via reference (`{typography.display-hero}`, `{typography.body}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | Maximum size — landing hero statements |
| `display-large` | Secondary hero, full-width section heads |
| `display` | Primary feature section titles |
| `heading-section` | Feature sub-section heads |
| `heading-sub-large` | Card titles, sub-section markers |
| `heading-sub` | Smaller section heads, pull quotes |
| `heading-sub-small` | Feature titles, small card heads |
| `body-large` | Intro paragraphs, emphasized body text |
| `body` | Standard reading text |
| `nav-link` | Top navigation links |
| `button-ui` | Button labels, UI chrome (often uppercase) |
| `caption` | Small metadata, legal text |
| `caption-small` | Micro labels, timestamps |

### Principles
- **Weight 300 as signature**: Every display-size heading uses weight 300. Where security/privacy brands default to bold reassurance, Cape communicates trust through precision instead of weight. The lightness is the confidence.
- **Progressive negative tracking**: Letter-spacing tightens proportionally with size. Below body size, tracking returns to normal for readability.
- **Tight display line-height**: Headings run at 1.0–1.2 line-height — unusually tight for 48px+ display type. This locks headlines into dense engineered blocks rather than airy editorial passages.
- **Two-weight simplicity**: Weight 300 for display and body, weight 400 for UI and nav. No bold (700) anywhere in display.
- **Uppercase for chrome**: Button labels and UI indicators ("SIGN UP", "LOG IN") use uppercase at small sizes with `0.05em` tracking.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px with `micro` (2.4px) reserved for tight UI chrome.

The scale has a compact end (`micro` to `sm`) for chrome/UI and a generous end (`4xl`+) for section spacing. Mid-range values are used sparingly — Cape either sits tight or breathes wide.

### Grid & Container
- Max content width: approximately 1200px for centered content
- Hero: full-width or two-column (text left, image/video right)
- Feature sections: single-column statements, or 2-column feature pairs
- Full-bleed dark sections alternate with the off-white canvas for immersive product moments

### Whitespace Philosophy
- **Editorial pacing**: Each section gets significant vertical breathing room (`5xl`–`6xl` between majors) — the page reads like a well-laid magazine spread
- **Type-anchored rhythm**: A 105px headline needs `6xl`+ of air; a body paragraph only needs `xl`
- **Dark/light alternation**: Off-white canvas alternates with full-bleed dark imagery — chapter-like breaks without decorative dividers

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Page canvas, body text, structural containers |
| Inset Line (Level 1) | `0 0 0 0 inset` | Button baseline state — primes the hover transition |
| Offset Stamp (Level 2) | `-4px 4px 0 #000` (default) or `-3px 3px 0 #fff` (inverted) | Primary CTAs, emphasized cards — signature stamp treatment |
| Focus Halo (Level 3) | `0 4px 12px {colors.shadow-soft}, 0 0 0 2px {colors.focus-ring}` | Keyboard focus on interactive elements |
| Glow Ring (Level 4) | `0 0 1em #fff` | Video player / dark-surface focus states |

**Shadow Philosophy**: Cape's depth system is graphic, not atmospheric. Where most sites use blurred drop shadows to simulate physical elevation, Cape uses hard-edged offset shadows that read as graphic stamps — the kind you'd see on a risograph print or hand-set letterpress piece. The `-4px 4px 0 0` pattern has no blur radius and no spread — it's a pure color rectangle offset from its parent.

## Shapes

The system is **binary**: sharp rectangular or fully circular. No mid-range radii.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Default for buttons, cards, containers, badges, inputs — the workhorse radius |
| `soft` | 3px | Occasional soft edge on certain specialty containers (rare) |
| `pill` | 9999px | Circular navigation dots, avatars, toggle indicators, image crops |

Cape does not use 4–16px values. The decision to keep radius binary is what gives the system its mechanical, printed character.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (`{components.button-primary}`, `{components.card-stamped}`) rather than reconstructing them.

### Button variants

- **`button-primary`** — Lavender stamp. Signature CTA. Pair with `-4px 4px 0 #000` offset shadow.
- **`button-inverted`** — Black on light surfaces. Pair with `-3px 3px 0 #fff` when over dark.
- **`button-lilac`** — Pale lilac surface variant. Informational CTAs where lavender primary would be too strong.
- **`button-ghost`** — Off-white, transparent border. Tertiary/low-emphasis actions.
- **`button-circular`** — Pagination dots, toggle indicators. Active state scales `matrix(1.1, 0, 0, 1.1, 0, 0)`.

### Cards
- **`card`** — flat panel, no shadow, no border. Content rests on the canvas.
- **`card-stamped`** — same panel with `-4px 4px 0 #000` offset stamp shadow for emphasis.

Internal padding stays generous — `2xl`–`4xl` for feature cards.

### Inputs
Sharp-cornered, white surface, focus state shifts to `focus-tint` background plus 2px focus ring. Always FK Grotesk weight 300.

### Badges
- **`badge-lavender`** — solid lavender pill or square, used for status/notification.
- **`badge-outline`** — transparent with 1px black border, pill-shaped, used for category markers.

### Navigation
Top nav: horizontal white bar, left-aligned wordmark, right-aligned "SIGN UP" (lavender) and "LOG IN" (ghost). Sticky at top, scrolls beneath video/imagery.

## Do's and Don'ts

### Do
- Use FK Grotesk weight 300 for every display and heading size — lightness is the brand voice
- Apply Cape Lavender (`{colors.primary}`) only to primary CTAs and focus states — preserve its stamp quality
- Use hard offset shadows (`-4px 4px 0 #000`) for the signature rubber-stamp depth effect
- Keep corner radius at `{rounded.none}` (0px) for all rectangular surfaces — sharpness is intentional
- Use `{rounded.pill}` only for genuinely circular elements (dots, avatars, toggles)
- Apply tight negative letter-spacing on display-size headings
- Use uppercase with `0.05em` tracking for button labels and UI chrome
- Alternate off-white sections with full-bleed dark/video sections for chapter-like pacing
- Let typography do the illustration work — avoid decorative icons or graphic flourishes

### Don't
- Don't use weight 500–700 on FK Grotesk headings — weight 300 is the ceiling
- Don't introduce mid-range border-radius (4–16px) — the system is binary (sharp or pill)
- Don't use blurred drop shadows for depth — the signature is hard offset stamps
- Don't use pure white (`{colors.surface}`) for the page background — always off-white (`{colors.background}`)
- Don't saturate with the lavender accent — one or two applications per screen maximum
- Don't introduce other chromatic colors — the system is mono + lavender only
- Don't use lightweight body text on lavender backgrounds — contrast with black for legibility
- Don't add gradient fills anywhere — Cape is solid-color only
- Don't use large hero illustrations — product photography or video fills that role

---

## Responsive Behavior

*(Preserved from original 9-section format — Google's parser keeps unknown sections.)*

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile Small | <375px | Single-column, hero type drops to 36–48px |
| Mobile | 375–650px | Single-column, 48–56px hero, stacked CTAs |
| Tablet | 650–1000px | 2-column grids begin, 56–72px hero |
| Desktop | 1000–1269px | Full multi-column layouts, 72–90px hero |
| Large Desktop | ≥1269px | Maximum type scale (105px hero), 1200px container |

### Touch Targets
- Primary CTAs: min 44px tap height, 16px horizontal padding on mobile
- Nav links: generous padding for thumb navigation
- Circular navigation dots: min 12px with 20px tap area

### Collapsing Strategy
- **Nav**: Horizontal link bar collapses to hamburger on mobile
- **Hero**: 105px → 56px → 40px progressive scaling, weight 300 maintained throughout
- **Feature sections**: 2-column pairs collapse to stacked single-column
- **Section spacing**: `6xl`+ desktop → `3xl`–`4xl` mobile — reduces but maintains editorial pace
- **Letter-spacing**: Tracking remains proportionally tight at all breakpoints

---

## Agent Prompt Guide

*(Preserved from original 9-section format — the copy-paste payload section.)*

### Quick Color Reference
- Page Background: `{colors.background}` (off-white)
- Primary Text: `{colors.ink}` (pure black)
- Brand Accent: `{colors.primary}` (lavender) — CTAs and focus only
- Hover Text: `{colors.text-hover}` (desaturated slate)
- Lavender Surface: `{colors.primary-container}` (pale lilac)
- Focus Background: `{colors.focus-tint}`
- Focus Ring: `0 0 0 2px {colors.focus-ring}`
- Stamp Shadow: `-4px 4px 0 #000` (default) or `-3px 3px 0 #fff` (inverted)

### Example Component Prompts

- "Create a hero section on Cape Off-White (`{colors.background}`) with a headline at 105px FK Grotesk weight 300, line-height 1.0, letter-spacing -0.2px, color `{colors.ink}`. Use a Cape Lavender (`{colors.primary}`) CTA button — 12px FK Grotesk weight 400 uppercase, `0.05em` letter-spacing, 0px radius, `-4px 4px 0 #000` hard offset shadow."

- "Design a feature card on `{colors.background}` with 0px border-radius, no border, and a hard offset shadow `-4px 4px 0 #000`. Title in FK Grotesk 48px weight 300, tight letter-spacing. Body in FK Grotesk 20px weight 300, line-height 1.3."

- "Build a full-bleed dark hero section. Overlay text left-aligned, bottom-positioned: headline at 56px FK Grotesk weight 300 in pure white, subtitle at 16px weight 400. Add a Cape Lavender CTA with `-3px 3px 0 #fff` inverted offset shadow."

- "Create a circular pagination dot — 12×12px, 9999px radius, 1px solid #000 border, transparent or black fill based on state. Active state scales `matrix(1.1, 0, 0, 1.1, 0, 0)`."

- "Design an outline pill badge — transparent background, 1px solid #000, 9999px radius, 12px FK Grotesk weight 400 text in `#000000`, padding 2.4px 8px."

### Iteration Guide

1. Default to FK Grotesk weight 300 for all display and heading sizes — lightness is non-negotiable
2. Keep radius binary: `{rounded.none}` for rectangular, `{rounded.pill}` for circular. Never mid-range.
3. Use hard offset shadows (`-4px 4px 0 0`) for CTAs and emphasized cards — no blur, no spread
4. Lavender (`{colors.primary}`) is sacred — one or two applications per screen
5. Negative letter-spacing scales with size; normal at body
6. Uppercase UI text pairs with `0.05em` tracking and weight 400 — never weight 300 uppercase
7. Off-white (`{colors.background}`) is the page canvas — reserve pure white for inversions only
8. Let typography carry the composition; avoid decorative icons or illustrations
