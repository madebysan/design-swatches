---
version: alpha
name: Clay
description: Warm cream canvas with a vivid named-flavor swatch palette (Matcha, Slushie, Lemon, Ube, Pomegranate, Blueberry, Dragonfruit), Roobert with 5 OpenType stylistic sets, playful rotate-tilt hover animations, and multi-layer pressed-into-clay shadows.

colors:
  # Primary canvas + ink
  background: "#faf9f7"          # Warm Cream
  surface: "#ffffff"
  ink: "#000000"
  ink-inverted: "#ffffff"

  # Brand accent — primary uses Matcha as Clay's strongest swatch identity
  primary: "#078a52"             # Matcha 600

  # Swatch palette
  matcha-300: "#84e7a5"
  matcha-600: "#078a52"
  matcha-800: "#02492a"
  slushie-500: "#3bd3fd"
  slushie-800: "#0089ad"
  lemon-400: "#f8cc65"
  lemon-500: "#fbbd41"
  lemon-700: "#d08a11"
  lemon-800: "#9d6a09"
  ube-300: "#c1b0ff"
  ube-800: "#43089f"
  ube-900: "#32037d"
  pomegranate-400: "#fc7981"
  blueberry-800: "#01418d"
  dragonfruit: "#e64a8a"

  # Neutral scale (warm)
  text-warm-silver: "#9f9b93"
  text-warm-charcoal: "#55534e"
  text-dark-charcoal: "#333333"

  # Surface & border
  border: "#dad4c8"              # Oat Border
  border-light: "#eee9df"        # Oat Light
  border-cool: "#e6e8ec"
  border-dark: "#525a69"
  surface-frost: "#eff1f3"       # Light Frost
  border-button: "#717989"
  hover-dark: "#434346"

  # Badges
  badge-blue-bg: "#f0f8ff"
  badge-blue-text: "#3859f9"
  focus-ring: "#146ef5"

  # Text on background
  on-background: "#000000"
  on-surface: "#000000"
  on-primary: "#ffffff"

  # Shadow tints
  shadow-clay: "#1a1a1a"  # opaque approx of rgba(0,0,0,0.1) — Google format requires hex
  shadow-hover: "#000000"

typography:
  display-hero:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 80px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: -3.2px
  display-secondary:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 60px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: -2.4px
  section-heading:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 44px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -1.32px
  card-heading:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -0.64px
  feature-title:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: -0.4px
  sub-heading:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: -0.16px
  body-large:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  body:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: -0.36px
  body-standard:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: -0.16px
  button-large:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button-small:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: -0.13px
  nav-link:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.60
    letterSpacing: 0px
  caption:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.14px
  small:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  uppercase-label:
    fontFamily: "Roobert, Arial, ui-sans-serif, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 1.08px
  code:
    fontFamily: "Space Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px

spacing:
  micro: 1px
  2xs: 2px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  2xl: 20px
  3xl: 24px

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  badge: 11px
  card: 12px
  feature: 24px
  section: 40px
  pill: 9999px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px

  # Primary — transparent with playful hover
  button-primary:
    backgroundColor: "{colors.surface-frost}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.card}"
    padding: 6px 13px
  button-primary-hover:
    backgroundColor: "{colors.hover-dark}"
    textColor: "{colors.ink-inverted}"

  # White solid
  button-white:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.card}"
    padding: 6px 6px
  button-white-hover:
    backgroundColor: "{colors.border}"
    textColor: "{colors.ink}"

  # Ghost outlined
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.xs}"
    padding: 8px 8px
  button-ghost-hover:
    backgroundColor: "{colors.dragonfruit}"
    textColor: "{colors.ink-inverted}"

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: 24px
  card-feature:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.feature}"
    padding: 32px
  card-section:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.section}"
    padding: 48px

  # Swatch sections
  section-matcha:
    backgroundColor: "{colors.matcha-800}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.section-heading}"
    rounded: "{rounded.section}"
    padding: 48px
  section-slushie:
    backgroundColor: "{colors.slushie-800}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.section-heading}"
    rounded: "{rounded.section}"
    padding: 48px
  section-ube:
    backgroundColor: "{colors.ube-800}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.section-heading}"
    rounded: "{rounded.section}"
    padding: 48px
  section-lemon:
    backgroundColor: "{colors.lemon-500}"
    textColor: "{colors.ink}"
    typography: "{typography.section-heading}"
    rounded: "{rounded.section}"
    padding: 48px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-standard}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"

  # Badge
  badge-blue:
    backgroundColor: "{colors.badge-blue-bg}"
    textColor: "{colors.badge-blue-text}"
    typography: "{typography.uppercase-label}"
    rounded: "{rounded.badge}"
    padding: 4px 8px

  # Trust pill
  pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
---

# Clay Design System

## Overview

Clay's website is a warm, playful celebration of color that treats B2B data enrichment like a craft rather than an enterprise chore. The design language is built on a foundation of warm cream backgrounds (`{colors.background}`) and oat-toned borders (`{colors.border}`, `{colors.border-light}`) that give every surface the tactile quality of handmade paper. Against this artisanal canvas, a vivid swatch palette explodes with personality — Matcha green, Slushie cyan, Lemon gold, Ube purple, Pomegranate pink, Blueberry navy, and Dragonfruit magenta — each named like flavors at a juice bar, not colors in an enterprise UI kit.

The typography is anchored by Roobert, a geometric sans-serif with character, loaded with an extensive set of OpenType stylistic sets (`"ss01"`, `"ss03"`, `"ss10"`, `"ss11"`, `"ss12"`) that give the text a distinctive, slightly quirky personality. At display scale (80px, weight 600), Roobert uses aggressive negative letter-spacing (-3.2px) that compresses headlines into punchy, billboard-like statements. Space Mono serves as the monospace companion for code and technical labels, completing the craft-meets-tech duality.

What makes Clay truly distinctive is its hover micro-animations: buttons on hover rotate slightly (`rotateZ(-8deg)`), translate upward, change background to a contrasting swatch color, and cast a hard offset shadow. This playful hover behavior — where a button literally tilts and jumps on interaction — creates a sense of physical delight that's rare in B2B software. Combined with generously rounded containers (24px–40px radius), dashed borders alongside solid ones, and a multi-layer shadow system that includes inset highlights, Clay feels like a design system that was made by people who genuinely enjoy making things.

**Key Characteristics:**
- Warm cream canvas (`{colors.background}`) with oat-toned borders (`{colors.border}`) — artisanal, not clinical
- Named swatch palette: Matcha, Slushie, Lemon, Ube, Pomegranate, Blueberry, Dragonfruit
- Roobert font with 5 OpenType stylistic sets — quirky geometric character
- Playful hover animations: rotateZ(-8deg) + translateY upward + hard offset shadow
- Space Mono for code and technical labels
- Generous border radius: 24px cards, 40px sections, full pill
- Mixed border styles: solid + dashed in the same interface
- Multi-layer shadow with inset highlight

## Colors

### Primary
- **Clay Black** (`{colors.ink}`): Text, headings, pricing card text.
- **Pure White** (`{colors.surface}`): Card backgrounds, button backgrounds, inverse text.
- **Warm Cream** (`{colors.background}`): Page background — the warm, paper-like canvas.

### Swatch Palette — Named Colors

**Matcha (Green)**
- Matcha 300 (`{colors.matcha-300}`), Matcha 600 (`{colors.matcha-600}`), Matcha 800 (`{colors.matcha-800}`)

**Slushie (Cyan)**
- Slushie 500 (`{colors.slushie-500}`), Slushie 800 (`{colors.slushie-800}`)

**Lemon (Gold)**
- Lemon 400 (`{colors.lemon-400}`), Lemon 500 (`{colors.lemon-500}`), Lemon 700 (`{colors.lemon-700}`), Lemon 800 (`{colors.lemon-800}`)

**Ube (Purple)**
- Ube 300 (`{colors.ube-300}`), Ube 800 (`{colors.ube-800}`), Ube 900 (`{colors.ube-900}`)

**Pomegranate (Pink/Red)**
- Pomegranate 400 (`{colors.pomegranate-400}`)

**Blueberry (Navy Blue)**
- Blueberry 800 (`{colors.blueberry-800}`)

**Dragonfruit (Magenta)**
- Dragonfruit (`{colors.dragonfruit}`) — used for hover states on ghost buttons.

### Neutral Scale (Warm)
- Warm Silver (`{colors.text-warm-silver}`), Warm Charcoal (`{colors.text-warm-charcoal}`), Dark Charcoal (`{colors.text-dark-charcoal}`).

### Surface & Border
- Oat Border (`{colors.border}`) — primary border, warm cream-toned.
- Oat Light (`{colors.border-light}`) — secondary lighter border.
- Cool Border (`{colors.border-cool}`) — cool-toned for contrast sections.
- Dark Border (`{colors.border-dark}`) — borders on dark sections.
- Light Frost (`{colors.surface-frost}`) — subtle button background.
- Button Border (`{colors.border-button}`) — outlined buttons.

### Badges & Focus
- Badge Blue (`{colors.badge-blue-bg}` / `{colors.badge-blue-text}`).
- Focus Ring (`{colors.focus-ring}`) — accessibility indicator.

### Shadows
- Shadow Clay (`{colors.shadow-clay}`) — multi-layer with inset highlight.
- Shadow Hover (`{colors.shadow-hover}`) — hard offset shadow on hover.

## Typography

### Font Families
- **Primary**: `Roobert`, fallback `Arial`
- **Monospace**: `Space Mono`
- **OpenType Features**: `"ss01"`, `"ss03"`, `"ss10"`, `"ss11"`, `"ss12"` on all Roobert text

The complete type scale lives in the `typography:` token block above.

| Token | Use |
|---|---|
| `display-hero` | 80px hero with -3.2px tracking |
| `display-secondary` | 60px secondary display |
| `section-heading` | 44px section heading |
| `card-heading` | 32px card heading |
| `feature-title` | 20px feature title |
| `sub-heading` | 20px sub-heading |
| `body-large` | 20px lead body |
| `body` | 18px standard body |
| `body-standard` | 16px standard body |
| `button` | 16px button label |
| `button-large` | 24px large button |
| `button-small` | 13px small button |
| `nav-link` | 15px nav link |
| `caption` | 14px caption |
| `small` | 12px small text |
| `uppercase-label` | 12px uppercase with 1.08px tracking |
| `code` | 14px Space Mono |

### Principles
- **Five stylistic sets as identity**: `"ss01"`, `"ss03"`, `"ss10"`, `"ss11"`, `"ss12"` on Roobert. `ss01` is reserved for headings — body omits it for subtle hierarchy.
- **Aggressive display compression**: -3.2px at 80px, -2.4px at 60px — most compressed display tracking alongside generous body line-height.
- **Three-tier weight system**: 600 (headings), 500 (UI), 400 (body) — strict roles.
- **Uppercase labels with positive tracking**: 12px uppercase at 1.08px letter-spacing.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

### Grid & Container
- Max content width centered
- Feature sections alternate between white cards and colorful swatch backgrounds
- Card grids: 2–3 columns on desktop
- Full-width colorful sections break the grid
- Footer with generous 40px radius container

### Whitespace Philosophy
- **Warm, generous breathing**: Cream background provides warm rest between blocks. Spacing is generous but inviting.
- **Color as spatial rhythm**: Alternating swatch-colored sections create visual rhythm through hue.
- **Craft-like density inside cards**: Compact within, generous outside.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, cream canvas | Page background |
| Clay Shadow (Level 1) | Multi-layer with inset highlight using `{colors.shadow-clay}` | Cards, buttons |
| Hover Hard (Level 2) | Hard offset shadow `{colors.shadow-hover}` -7px 7px | Hover state — playful |
| Focus (Level 3) | 2px solid `{colors.focus-ring}` outline | Keyboard focus ring |

**Shadow Philosophy**: Clay's shadow system is uniquely three-layered: a downward cast, an upward inset highlight, and a subtle edge. This creates a "pressed into clay" quality where elements feel both raised AND embedded. The hover hard shadow (`-7px 7px`) is deliberately retro-graphic, referencing print-era drop shadows.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Sharp inline elements |
| `xs` | 4px | Ghost buttons, inputs |
| `sm` | 8px | Small cards, images, links |
| `badge` | 11px | Tag badges |
| `card` | 12px | Standard cards, buttons |
| `feature` | 24px | Feature cards, images, panels |
| `section` | 40px | Large sections, footer, containers |
| `pill` | 9999px | CTAs, pill-shaped buttons |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Transparent (Light Frost), black text. Hover: rotation + dark fill + hard shadow.
- **`button-white`** — White solid for primary CTAs on colored sections.
- **`button-ghost`** — Outlined (1px). Hover transitions to Dragonfruit fill with white text + animated rotation.

### Cards & Containers
- **`card`** — White on cream, oat border, 12px radius.
- **`card-feature`** — 24px radius for feature cards/images.
- **`card-section`** — 40px radius for section containers/footer.
- Multi-layer Clay Shadow on cards with inset highlight.

### Swatch Sections
- **`section-matcha`** — Matcha 800 background, white text.
- **`section-slushie`** — Slushie 800 background, white text.
- **`section-ube`** — Ube 800 background, white text.
- **`section-lemon`** — Lemon 500 background, black text.

### Inputs
- **`input`** — Black text, 1px solid border, 4px radius.

### Badge & Pill
- **`badge-blue`** — Blue-tinted badge with vivid blue text.
- **`pill`** — Full-pill rounded action button.

### Distinctive Components

**Playful Hover Buttons**: Rotate -8deg + translate upward on hover. Hard offset shadow (-7px 7px) instead of soft blur. Background transitions to contrasting swatch color.

**Dashed Border Elements**: Dashed borders (`1px dashed {colors.border}`) alongside solid borders for secondary containers and decorative elements. Hand-drawn, craft-like quality.

## Do's and Don'ts

### Do
- Use warm cream (`{colors.background}`) as the page background — the warmth is the identity
- Apply all 5 OpenType stylistic sets on Roobert headings
- Use the named swatch palette for section backgrounds
- Apply the playful hover animation: rotateZ(-8deg), translate upward, hard shadow -7px 7px
- Use warm oat borders (`{colors.border}`) — not neutral gray
- Mix solid and dashed borders for visual variety
- Use generous radius: 24px for cards, 40px for sections
- Use weight 600 for headings, 500 for UI, 400 for body

### Don't
- Don't use cool gray backgrounds — warm cream (`{colors.background}`) is non-negotiable
- Don't use neutral gray borders — always use the warm oat tones
- Don't mix more than 2 swatch colors in the same section
- Don't skip the OpenType stylistic sets
- Don't use subtle hover effects — rotation + hard shadow is the signature
- Don't use small border radius (<12px) on feature cards
- Don't use standard blur-based shadows — Clay uses hard offset and multi-layer inset
- Don't forget the uppercase labels with 1.08px tracking

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile Small | <479px | Single column, tight padding |
| Mobile | 479–767px | Standard mobile, stacked layout |
| Tablet | 768–991px | 2-column grids, condensed nav |
| Desktop | 992px+ | Full layout, 3-column grids, expanded sections |

### Touch Targets
- Buttons: minimum 6.4px + 12.8px padding
- Nav links: 15px font with generous spacing
- Mobile: full-width buttons

### Collapsing Strategy
- Hero: 80px → 60px → smaller display
- Navigation: horizontal → hamburger at 767px
- Feature sections: multi-column → stacked
- Colorful sections: maintain full-width but compress padding
- Card grids: 3-column → 2-column → single column

### Image Behavior
- Product screenshots scale proportionally
- Colorful section illustrations adapt to viewport width
- Rounded corners maintained across breakpoints

---

## Agent Prompt Guide

### Quick Color Reference
- Background: Warm Cream `{colors.background}`
- Text: Clay Black `{colors.ink}`
- Secondary text: Warm Silver `{colors.text-warm-silver}`
- Border: Oat Border `{colors.border}`
- Green accent: Matcha 600 `{colors.matcha-600}`
- Cyan accent: Slushie 500 `{colors.slushie-500}`
- Gold accent: Lemon 500 `{colors.lemon-500}`
- Purple accent: Ube 800 `{colors.ube-800}`
- Pink accent: Pomegranate 400 `{colors.pomegranate-400}`

### Example Component Prompts
- "Create a hero on warm cream (`{colors.background}`) background. Headline at 80px Roobert weight 600, line-height 1.00, letter-spacing -3.2px, OpenType 'ss01 ss03 ss10 ss11 ss12', black text. Subtitle at 20px weight 400, line-height 1.40, `{colors.text-warm-silver}` text. Two buttons: white solid pill (12px radius) and ghost outlined (4px radius, 1px solid `{colors.border-button}`)."
- "Design a colorful section with Matcha 800 (`{colors.matcha-800}`) background. Heading at 44px Roobert weight 600, letter-spacing -1.32px, white text. Body at 18px weight 400, line-height 1.60, `{colors.matcha-300}` text. White card inset with oat border (`{colors.border}`), 24px radius."
- "Build a button with playful hover: default transparent background, black text, 16px Roobert weight 500. On hover: background `{colors.hover-dark}`, text white, transform rotateZ(-8deg) translateY upward, hard shadow -7px 7px."
- "Create a card: white background, 1px solid `{colors.border}` border, 24px radius. Multi-layer shadow with inset highlight. Title at 32px Roobert weight 600, letter-spacing -0.64px."
- "Design an uppercase label: 12px Roobert weight 600, text-transform uppercase, letter-spacing 1.08px, OpenType 'ss03 ss10 ss11 ss12'."

### Iteration Guide
1. Start with warm cream — never cool white
2. Swatch colors are for full sections, not small accents — go bold with matcha, slushie, ube
3. Oat borders everywhere — dashed variants for decoration
4. OpenType stylistic sets are mandatory
5. Hover animations are the signature — rotation + hard shadow, not subtle fades
6. Generous radius: 24px cards, 40px sections
7. Three weights: 600 (headings), 500 (UI), 400 (body) — strict roles
