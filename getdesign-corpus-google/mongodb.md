---
version: alpha
name: MongoDB
description: Forest-dark teal-black canvas with electric MongoDB Green accent. Three-font system — Value Serif for hero, Euclid Circular A for body (light weight 300), Source Code Pro uppercase for technical labels. Dual-mode dark/light sections with teal-tinted shadows.

colors:
  # Primary brand
  primary: "#00ed64"
  forest-black: "#001e2b"
  mongodb-green: "#00ed64"
  dark-green: "#00684a"

  # Interactive
  action-blue: "#006cfa"
  hover-blue: "#3860be"
  teal-active: "#1eaedb"

  # Neutral scale
  deep-teal: "#1c2d38"
  teal-gray: "#3d4f58"
  dark-slate: "#21313c"
  cool-gray: "#5c6c75"
  silver-teal: "#b8c4c2"
  light-input: "#e8edeb"
  surface-light: "#ffffff"
  ink: "#000000"

  # Aliases
  background: "#001e2b"
  surface: "#001e2b"
  on-primary: "#000000"
  on-dark: "#ffffff"

  # Shadows (opaque approximations)
  shadow-forest: "#d6dadc"   # was rgba(0,30,43,0.12) — flattened over white
  shadow-forest-deep: "#dcdddd" # was rgba(0,0,0,0.13) — flattened over white
  shadow-standard: "#d9d9d9" # was rgba(0,0,0,0.15) — flattened over white
  shadow-subtle: "#e6e6e6"   # was rgba(0,0,0,0.10) — flattened over white

typography:
  display-hero:
    fontFamily: "MongoDB Value Serif, Times, serif"
    fontSize: 96px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0px
  display-secondary:
    fontFamily: "MongoDB Value Serif, Times, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  section-heading:
    fontFamily: "Euclid Circular A, Akzidenz-Grotesk Std, Arial, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0px
  sub-heading:
    fontFamily: "Euclid Circular A, Akzidenz-Grotesk Std, Arial, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0px
  body-large:
    fontFamily: "Euclid Circular A, Akzidenz-Grotesk Std, Arial, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0px
  body:
    fontFamily: "Euclid Circular A, Akzidenz-Grotesk Std, Arial, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  body-light:
    fontFamily: "Euclid Circular A, Akzidenz-Grotesk Std, Arial, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0px
  nav-ui:
    fontFamily: "Euclid Circular A, Akzidenz-Grotesk Std, Arial, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.16px
  body-bold:
    fontFamily: "Euclid Circular A, Akzidenz-Grotesk Std, Arial, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  button:
    fontFamily: "Euclid Circular A, Akzidenz-Grotesk Std, Arial, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.135px
  caption:
    fontFamily: "Euclid Circular A, Akzidenz-Grotesk Std, Arial, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.71
    letterSpacing: 0px
  small:
    fontFamily: "Euclid Circular A, Akzidenz-Grotesk Std, Arial, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.82
    letterSpacing: 0.2px
  code-heading:
    fontFamily: "Source Code Pro, ui-monospace, monospace"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0px
  code-body:
    fontFamily: "Source Code Pro, ui-monospace, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  code-label:
    fontFamily: "Source Code Pro, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.14
    letterSpacing: 1.5px
  code-micro:
    fontFamily: "Source Code Pro, ui-monospace, monospace"
    fontSize: 9px
    fontWeight: 600
    lineHeight: 2.67
    letterSpacing: 2.5px

spacing:
  hairline: 1px
  xs: 4px
  xs-plus: 7px
  sm: 8px
  sm-plus: 10px
  md: 12px
  md-plus: 14px
  lg: 16px
  lg-plus: 18px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 48px
  5xl: 64px
  6xl: 80px

rounded:
  hairline: 2px
  xs: 4px
  sm: 8px
  md: 16px
  toggle: 20px
  lg: 24px
  image: 30px
  hero: 48px
  pill: 100px

components:
  # Buttons
  button-primary:
    backgroundColor: "{colors.dark-green}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.mongodb-green}"
    textColor: "{colors.ink}"
  button-dark-teal:
    backgroundColor: "{colors.deep-teal}"
    textColor: "{colors.cool-gray}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-dark-teal-hover:
    backgroundColor: "{colors.teal-active}"
    textColor: "{colors.on-dark}"
  button-outlined:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.forest-black}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 12px 24px

  # Cards
  card-light:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  card-dark:
    backgroundColor: "{colors.deep-teal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  card-dark-hero:
    backgroundColor: "{colors.forest-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-secondary}"
    rounded: "{rounded.hero}"
    padding: 48px

  # Image container
  image-container:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink}"
    rounded: "{rounded.image}"
    padding: 0px

  # Inputs
  input-light:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: 12px 8px
  input-dark:
    backgroundColor: "{colors.deep-teal}"
    textColor: "{colors.light-input}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: 12px 8px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.forest-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-ui}"
    padding: 16px 24px

  # Code label (the technical signpost)
  code-label-tag:
    backgroundColor: "{colors.forest-black}"
    textColor: "{colors.mongodb-green}"
    typography: "{typography.code-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
---

# MongoDB Design System

## Overview

MongoDB's website is a deep-forest-meets-terminal experience — a design system rooted in the darkest teal-black (`{colors.forest-black}`) that evokes both the density of a database and the depth of a forest canopy. Against this near-black canvas, a striking neon green (`{colors.mongodb-green}`) pulses as the brand accent — bright enough to feel electric, organic enough to feel alive. This isn't the cold neon of cyberpunk; it's the bioluminescent green of something growing in the dark.

The typography system is architecturally ambitious: MongoDB Value Serif for massive hero headlines (96px) creates an editorial, authoritative presence — serif type at database-company scale is a bold choice that says "we're not just another tech company." Euclid Circular A handles the heavy lifting of body and UI text with an unusually wide weight range (300–700), while Source Code Pro serves as the code and label font with distinctive uppercase treatments featuring very wide letter-spacing (1px–3px). This three-font system creates a hierarchy that spans editorial elegance → geometric professionalism → engineering precision.

What makes MongoDB distinctive is its dual-mode design: a dark hero/feature section world (`{colors.forest-black}` with neon green accents) and a light content world (white with teal-gray borders `{colors.silver-teal}`). The transition between these modes creates dramatic contrast. The shadow system uses teal-tinted dark shadows that maintain the forest-dark atmosphere even on light surfaces. Buttons use pill shapes with MongoDB Green borders (`{colors.dark-green}`), and the entire component system references the LeafyGreen design system.

**Key Characteristics:**
- Deep teal-black backgrounds (`{colors.forest-black}`) — forest-dark, not space-dark
- Neon MongoDB Green (`{colors.mongodb-green}`) as the singular brand accent — electric and organic
- MongoDB Value Serif for hero headlines — editorial authority at tech scale
- Euclid Circular A for body with weight 300 (light) as a distinctive body weight
- Source Code Pro with wide uppercase letter-spacing (1px–3px) for technical labels
- Teal-tinted shadows (`{colors.shadow-forest}`) — shadows carry the forest color
- Dual-mode: dark teal hero sections + light white content sections
- Pill buttons (`{rounded.pill}`) with green borders (`{colors.dark-green}`)
- Link Blue (`{colors.action-blue}`) and hover transition to `{colors.hover-blue}`

## Colors

### Primary Brand
- **Forest Black** (`{colors.forest-black}`): Primary dark background — the deepest teal-black
- **MongoDB Green** (`{colors.mongodb-green}`): Primary brand accent — neon green for highlights, underlines, gradients
- **Dark Green** (`{colors.dark-green}`): Button borders, link text on light — muted green for functional use

### Interactive
- **Action Blue** (`{colors.action-blue}`): Secondary accent — links, interactive highlights
- **Hover Blue** (`{colors.hover-blue}`): All link hover states transition to this blue
- **Teal Active** (`{colors.teal-active}`): Button hover background — bright teal

### Neutral Scale
- **Deep Teal** (`{colors.deep-teal}`): Dark button backgrounds, secondary dark surfaces
- **Teal Gray** (`{colors.teal-gray}`): Dark borders on dark surfaces
- **Dark Slate** (`{colors.dark-slate}`): Dark link text variant
- **Cool Gray** (`{colors.cool-gray}`): Muted text on dark, secondary button text
- **Silver Teal** (`{colors.silver-teal}`): Borders on light surfaces, dividers
- **Light Input** (`{colors.light-input}`): Input text on dark surfaces
- **Pure White** (`{colors.surface-light}`): Light section background, button text on dark
- **Black** (`{colors.ink}`): Text on light surfaces, darkest elements

### Shadows
- **Forest Shadow** — `{colors.shadow-forest}` `0 26px 44px` + `{colors.shadow-forest-deep}` `0 7px 13px`: Primary card elevation — teal-tinted (was `rgba(0, 30, 43, 0.12)`)
- **Standard Shadow** — `{colors.shadow-standard}` `0 3px 20px`: General elevation
- **Subtle Shadow** — `{colors.shadow-subtle}` `0 2px 4px`: Light card lift

## Typography

### Font Families
- **Display Serif**: `MongoDB Value Serif` — editorial hero headlines
- **Body / UI**: `Euclid Circular A` — geometric sans-serif workhorse
- **Code / Labels**: `Source Code Pro` — monospace with uppercase label treatments
- **Fallbacks**: `Akzidenz-Grotesk Std` (with CJK: Noto Sans KR/SC/JP), `Times`, `Arial`, `system-ui`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference each role via tokens.

| Token | Use |
|---|---|
| `display-hero` | Serif authority hero headline (96px) |
| `display-secondary` | Serif sub-hero (64px) |
| `section-heading` | Geometric precision section heads |
| `sub-heading` | Feature titles |
| `body-large` | Introductions |
| `body` | Standard body |
| `body-light` | Light-weight reading text (weight 300) |
| `nav-ui` | Navigation, emphasized UI |
| `body-bold` | Strong emphasis |
| `button` | CTA labels |
| `caption` | Metadata |
| `small` | Tags, annotations |
| `code-heading` | Code showcase titles |
| `code-body` | Code blocks |
| `code-label` | Technical labels (uppercase, wide-tracked) |
| `code-micro` | Smallest uppercase tags |

### Principles
- **Serif for authority**: MongoDB Value Serif at hero scale creates an editorial presence unusual in tech — it communicates that MongoDB is an institution, not a startup.
- **Weight 300 as body default**: Euclid Circular A uses light (300) for body text, creating an airy reading experience that contrasts with the dense, dark backgrounds.
- **Wide-tracked monospace labels**: Source Code Pro uppercase at 1px–3px letter-spacing creates technical signposts that feel like database field labels — systematic, structured, classified.
- **Four-weight range**: 300 (light body) → 400 (standard) → 500 (UI/nav) → 700 (bold CTA) — wider than most systems, enabling fine-grained hierarchy.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is `{spacing.sm}` (8px).

### Grid & Container
- Max content width centered
- Dark hero section with contained content
- Light content sections below
- Card grids: 2–3 columns
- Full-width dark footer

### Whitespace Philosophy
- **Dramatic mode transitions**: The shift from dark teal sections to white content creates built-in visual breathing through contrast, not just space.
- **Generous dark sections**: Dark hero and feature areas use extra vertical padding (`{spacing.6xl}`+) to let the forest-dark background breathe.
- **Compact light sections**: White content areas are denser, with tighter card grids and less vertical spacing.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Default surfaces |
| Subtle (Level 1) | `{colors.shadow-subtle}` `0 2px 4px` | Light card lift |
| Standard (Level 2) | `{colors.shadow-standard}` `0 3px 9px` | Standard cards |
| Prominent (Level 3) | `{colors.shadow-standard}` `0 3px 20px` | Elevated panels |
| Forest (Level 4) | `{colors.shadow-forest}` `0 26px 44px` + `{colors.shadow-forest-deep}` `0 7px 13px` | Hero cards — teal-tinted |

**Shadow Philosophy**: MongoDB's shadow system is unique in that the primary elevation shadow uses teal-tinted color values that carry the forest-dark brand color into the depth system. This means even on white surfaces, shadows feel like they belong to the MongoDB color world rather than being generic neutral black.

## Shapes

| Token | Value | Use |
|---|---|---|
| `hairline` | 2px | Small spans, badges |
| `xs` | 4px | Inputs, small buttons |
| `sm` | 8px | Standard buttons, links |
| `md` | 16px | Standard cards, containers |
| `toggle` | 20px | Switch elements |
| `lg` | 24px | Large panels |
| `image` | 30px | Image containers |
| `hero` | 48px | Hero cards |
| `pill` | 100px | Buttons, navigation pills |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (e.g. `{components.button-primary}`, `{components.card-dark-hero}`) rather than reconstructing them.

### Buttons
- **`button-primary`** — Dark-green pill (`{colors.dark-green}`) with black text. Hover lifts to neon `{colors.mongodb-green}` and scales up slightly.
- **`button-dark-teal`** — Deep-teal pill with cool-gray text. Hover shifts to `{colors.teal-active}` background with white text and a 5px translateX.
- **`button-outlined`** — White pill with `{colors.silver-teal}` border, dark text. For light surfaces.

### Cards & Containers
- **`card-light`** — White surface with `{colors.silver-teal}` border, `{rounded.md}` corners, paired with the forest-tinted shadow.
- **`card-dark`** — Deep-teal surface with `{colors.teal-gray}` border for the dark mode.
- **`card-dark-hero`** — Larger forest-black hero card at `{rounded.hero}` radius.
- **`image-container`** — Image holder at `{rounded.image}` radius (30px).

### Inputs
- **`input-light`** — White surface, `{colors.silver-teal}` border, `{rounded.xs}` corners.
- **`input-dark`** — Deep-teal surface with `{colors.light-input}` text on dark.

### Navigation
- **`nav-bar`** — Forest-black header. Euclid Circular A nav links, MongoDB leaf logo + wordmark left, green CTA pill right. Mega-menu dropdowns by product category.

### Code Labels
- **`code-label-tag`** — The "database field label" aesthetic. Source Code Pro uppercase, 1.5–2px tracking, used as section category markers above headings.

### Distinctive Patterns
- **Neon Green Accent Underlines** — `0px 2px 2px 0px solid {colors.mongodb-green}` on feature headings; also appears in `{colors.action-blue}` variant.
- **Source Code Label System** — 14px uppercase Source Code Pro with wide tracking, used as section markers.
- **Image Treatment** — Dashboard screenshots on dark backgrounds, green-accented UI elements in screenshots, `{rounded.image}` radius on image containers.

## Do's and Don'ts

### Do
- Use `{colors.forest-black}` for dark sections — not pure black
- Apply MongoDB Green (`{colors.mongodb-green}`) sparingly for maximum electric impact
- Use MongoDB Value Serif ONLY for hero/display headings — Euclid Circular A for everything else
- Apply Source Code Pro uppercase with wide tracking (1px–3px) for technical labels
- Use teal-tinted shadows (`{colors.shadow-forest}`) for primary card elevation
- Maintain the dark/light section duality — dramatic contrast between modes
- Use weight 300 for body text — the light weight is the readable voice
- Apply pill radius (`{rounded.pill}`) to primary action buttons

### Don't
- Don't use pure black (`#000000`) for dark backgrounds — always use teal-black (`{colors.forest-black}`)
- Don't use MongoDB Green (`{colors.mongodb-green}`) on backgrounds — it's an accent for text, underlines, and small highlights
- Don't use standard gray shadows — always use teal-tinted (`{colors.shadow-forest}`)
- Don't apply serif font to body text — MongoDB Value Serif is hero-only
- Don't use narrow letter-spacing on Source Code Pro labels — the wide tracking IS the identity
- Don't mix dark and light section treatments within the same section
- Don't use warm colors — the palette is strictly cool (teal, green, blue)
- Don't forget the green accent underlines — they're the signature decorative element

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <425px | Tight single column |
| Mobile | 425–768px | Standard mobile |
| Tablet | 768–1024px | 2-column grids begin |
| Desktop | 1024–1280px | Standard layout |
| Large Desktop | 1280–1440px | Expanded layout |
| Ultra-wide | >1440px | Maximum width, generous margins |

### Touch Targets
- Pill buttons with generous padding
- Navigation links at 16px with adequate spacing
- Card surfaces as full-area touch targets

### Collapsing Strategy
- Hero: MongoDB Value Serif 96px → 64px → scales further
- Navigation: horizontal mega-menu → hamburger
- Feature cards: multi-column → stacked
- Dark/light sections maintain their mode at all sizes
- Source Code Pro labels maintain uppercase treatment

### Image Behavior
- Dashboard screenshots scale proportionally
- Dark section backgrounds maintained full-width
- Image radius maintained across breakpoints

---

## Agent Prompt Guide

### Quick Color Reference
- Dark background: Forest Black (`#001e2b`)
- Brand accent: MongoDB Green (`#00ed64`)
- Functional green: Dark Green (`#00684a`)
- Link blue: Action Blue (`#006cfa`)
- Text on light: Black (`#000000`)
- Text on dark: White (`#ffffff`) or Light Input (`#e8edeb`)
- Border light: Silver Teal (`#b8c4c2`)
- Border dark: Teal Gray (`#3d4f58`)

### Example Component Prompts
- "Create a hero on forest-black (#001e2b) background. Headline at 96px MongoDB Value Serif weight 400, line-height 1.20, white text with 'potential' highlighted in MongoDB Green (#00ed64). Subtitle at 18px Euclid Circular A weight 400. Green pill CTA (#00684a, 100px radius). Neon green gradient glow behind product screenshot."
- "Design a card on white background: 1px solid #b8c4c2 border, 16px radius, shadow rgba(0,30,43,0.12) 0px 26px 44px. Title at 24px Euclid Circular A weight 500. Body at 16px weight 300. Source Code Pro 14px uppercase label above title with 2px letter-spacing."
- "Build a dark section: #001e2b background, 1px solid #3d4f58 border on cards. White text. MongoDB Green (#00ed64) accent underlines on headings using bottom-border 2px solid."
- "Create technical label: Source Code Pro 14px, text-transform uppercase, letter-spacing 2px, weight 500, #00ed64 color on dark background."
- "Design a pill button: #1c2d38 background, 1px solid #3d4f58 border, 100px radius, #5c6c75 text. Hover: #1eaedb background, white text, translateX(5px)."

### Iteration Guide
1. Start with the mode decision: dark (#001e2b) for hero/features, white for content
2. MongoDB Green (#00ed64) is electric — use once per section for maximum impact
3. Serif headlines (MongoDB Value Serif) create the editorial authority — never use for body
4. Weight 300 body text creates the airy reading experience — don't default to 400
5. Source Code Pro uppercase with wide tracking for technical labels — the database voice
6. Teal-tinted shadows keep everything in the MongoDB color world
