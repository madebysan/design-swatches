---
version: alpha
name: Nike
description: Monochromatic UI that lets product photography be the only color. Massive uppercase Nike Futura ND display at 96px with 0.90 line-height, full-bleed photography, pill-shaped CTAs, radically flat elevation.

colors:
  # Primary
  primary: "#111111"
  ink: "#111111"
  background: "#ffffff"
  surface: "#ffffff"

  # Surface scale
  snow: "#fafafa"
  gray-100: "#f5f5f5"
  gray-200: "#e5e5e5"
  gray-300: "#cacacb"
  gray-400: "#9e9ea0"
  gray-500: "#707072"
  gray-700: "#39393b"
  gray-800: "#28282a"
  gray-900: "#1f1f21"

  # Text
  text-primary: "#111111"
  text-secondary: "#707072"
  text-disabled: "#9e9ea0"
  text-disabled-inverse: "#4b4b4d"

  # Borders
  border-primary: "#707072"
  border-secondary: "#cacacb"
  border-active: "#111111"

  # Inverted
  on-primary: "#ffffff"
  on-dark: "#ffffff"

  # Semantic
  red-600: "#d30005"
  red-500: "#ee0005"
  badge-orange: "#d33918"
  orange-400: "#ff5000"
  green-600: "#007d48"
  green-500: "#1eaa52"
  blue-500: "#1151ff"
  blue-400: "#1190ff"
  yellow-200: "#fedf35"
  focus-ring: "#275dc5"

  # Extended ramp endpoints
  red-50: "#ffe5e5"
  red-900: "#530300"
  orange-50: "#ffe2d6"
  orange-900: "#3e1009"
  yellow-50: "#fef087"
  yellow-600: "#fca600"
  yellow-900: "#99470a"
  green-50: "#dfffb9"
  green-900: "#003c2a"
  teal-50: "#d4fffb"
  teal-600: "#008e98"
  teal-900: "#043441"
  blue-50: "#d6eeff"
  blue-900: "#020664"
  purple-50: "#e4e1fc"
  purple-600: "#6e0ff6"
  purple-900: "#1c0060"
  pink-50: "#ffe1f3"
  pink-600: "#ed1aa0"
  pink-900: "#4c012d"

typography:
  display:
    fontFamily: "Nike Futura ND, Helvetica Now Text Medium, Helvetica, Arial, sans-serif"
    fontSize: 96px
    fontWeight: 500
    lineHeight: 0.9
    letterSpacing: 0px
  heading-1:
    fontFamily: "Helvetica Now Display Medium, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0px
  heading-2:
    fontFamily: "Helvetica Now Display Medium, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0px
  heading-3:
    fontFamily: "Helvetica Now Text Medium, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Helvetica Now Text, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0px
  body-medium:
    fontFamily: "Helvetica Now Text Medium, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.75
    letterSpacing: 0px
  link:
    fontFamily: "Helvetica Now Text Medium, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.75
    letterSpacing: 0px
  link-small:
    fontFamily: "Helvetica Now Text Medium, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.86
    letterSpacing: 0px
  button:
    fontFamily: "Helvetica Now Text Medium, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  button-small:
    fontFamily: "Helvetica Now Text Medium, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  caption:
    fontFamily: "Helvetica Now Text Medium, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  small:
    fontFamily: "Helvetica Now Text Medium, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  tiny:
    fontFamily: "Helvetica Now Text, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px

spacing:
  xs: 4px
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
  md: 18px
  lg: 20px
  xl: 24px
  pill: 30px
  full: 9999px

components:
  # Buttons
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.gray-500}"
    textColor: "{colors.on-primary}"
  button-primary-on-dark:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-disabled:
    backgroundColor: "{colors.gray-200}"
    textColor: "{colors.gray-400}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-icon:
    backgroundColor: "{colors.gray-100}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: 6px
    size: 36px

  # Cards
  card-product:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-3}"
    rounded: "{rounded.none}"
    padding: 12px 0px
  card-ui:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Inputs
  input:
    backgroundColor: "{colors.gray-100}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  input-search:
    backgroundColor: "{colors.gray-100}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xl}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.gray-100}"
    textColor: "{colors.ink}"

  # Navigation
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    padding: 16px 48px

  # Promotional banner
  banner-promo:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.small}"
    padding: 8px 16px

  # Filter pill
  filter-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-small}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  # Badges
  badge-error:
    backgroundColor: "{colors.red-600}"
    textColor: "{colors.on-dark}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  badge-success:
    backgroundColor: "{colors.green-600}"
    textColor: "{colors.on-dark}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
---

# Nike Design System

## Overview

Nike.com is a kinetic retail cathedral — a site that channels the explosive energy of sport into a digital shopping experience. The design operates on a principle of radical simplicity: strip everything back to black, white, and grey so that athletic photography and product color can dominate without competition. The result feels less like a website and more like a sports editorial laid out with the precision of a luxury magazine. Every pixel of real estate is either selling product or driving toward product.

The "Podium CDS" (Nike's internal Core Design System) establishes an aggressively monochromatic foundation. The UI disappears into black (`{colors.ink}`) text and white surfaces (`{colors.background}`), allowing hero photography — sweating athletes, mid-air shoes, stadium energy — to carry the emotional weight. When color does appear in the UI, it's almost exclusively functional: red for errors, blue for links, green for success. The product itself is the color story. This restraint creates a visual paradox: the most colorful pages on the internet feel the most minimal, because all vibrancy comes from merchandise rather than interface.

The typography system is the other half of Nike's visual identity. Massive uppercase headlines in Nike Futura ND — a custom condensed Futura variant with impossibly tight line-height (0.90) — punch through hero imagery like a typographic shockwave. Below the headlines, the workhorse Helvetica Now family handles everything from navigation to product descriptions with Swiss-precision clarity. This split between expressive display type and functional body type mirrors Nike's brand duality: inspiration meets execution.

**Key Characteristics:**
- Monochromatic UI (black/white/grey) that lets product photography be the only color source
- Massive uppercase display typography (96px, line-height 0.90) that punches through hero images
- Full-bleed photography with no border radius — imagery fills every available edge
- Pill-shaped buttons (`{rounded.pill}`) as the primary interactive element
- 8px spacing grid with athletic discipline — every measurement snaps to the system
- Category-driven shopping architecture with large navigational image cards
- Shadow-free, border-minimal elevation model — surface differentiation through grey shifts only

## Colors

### Primary
- **Nike Black** (`{colors.ink}`): Foundation — primary text, button backgrounds, nav text, hero overlays. Deliberately not pure black, creating a fractionally softer reading experience.
- **Nike White** (`{colors.background}`): Primary page canvas, button text on dark, card surfaces, nav bar background.

### Surface & Background
- **Snow** (`{colors.snow}`): Lightest surface, near-white differentiation
- **Light Gray** (`{colors.gray-100}`): Secondary background, search input fill, image placeholder, loading skeleton
- **Hover Gray** (`{colors.gray-200}`): Hover state background, disabled button fill
- **Dark Surface** (`{colors.gray-800}`): Primary background on dark/inverted sections
- **Deep Charcoal** (`{colors.gray-900}`): Inverse primary background, darkest non-black surface
- **Dark Hover** (`{colors.gray-700}`): Hover state on dark backgrounds

### Neutrals & Text
- **Primary Text** (`{colors.text-primary}`): Main body text, headings, nav links
- **Secondary Text** (`{colors.text-secondary}`): Descriptive copy, metadata, timestamps, price labels
- **Disabled Text** (`{colors.text-disabled}`): Inactive elements, unavailable options
- **Disabled Inverse** (`{colors.text-disabled-inverse}`): Disabled text on dark backgrounds
- **Border Primary** (`{colors.border-primary}`): Standard border color
- **Border Secondary** (`{colors.border-secondary}`): Subtle borders, input borders, divider lines
- **Border Active** (`{colors.border-active}`): Active/focused border, matching primary text

### Semantic & Accent
- **Nike Red** (`{colors.red-600}`): Critical errors, sale badges, urgent notifications
- **Bright Red** (`{colors.red-500}`): Slightly lighter red for emphasis
- **Nike Orange Badge** (`{colors.badge-orange}`): Badge text, promotional callouts
- **Orange Flash** (`{colors.orange-400}`): Expressive orange accent
- **Success Green** (`{colors.green-600}`): Confirmation, availability, positive states
- **Success Inverse** (`{colors.green-500}`): Success on dark backgrounds
- **Link Blue** (`{colors.blue-500}`): Text links, informational highlights
- **Info Inverse** (`{colors.blue-400}`): Links on dark backgrounds
- **Warning Yellow** (`{colors.yellow-200}`): Warning backgrounds, attention banners
- **Focus Ring** (`{colors.focus-ring}`): Keyboard focus indicator (was `rgba(39, 93, 197, 1)`)

### Extended Color Spectrum (Podium CDS)
Each color ramp runs 50–900 for expressive use in campaigns and product pages. Endpoints are tokenised (`{colors.red-50}` … `{colors.red-900}`, and similarly for orange, yellow, green, teal, blue, purple, pink).

### Gradient System
Nike avoids UI gradients. When gradients appear, they are photographic — applied to product hero backgrounds (e.g., a red shoe on a red-to-deeper-red gradient). The design system itself is flat-color only.

## Typography

### Font Family
- **Display:** Nike Futura ND (custom condensed Futura variant exclusive to Nike). Fallbacks: Helvetica Now Text Medium, Helvetica, Arial. Used exclusively for large uppercase display headlines. Tight line-height (0.90) and uppercase transform.
- **Heading:** Helvetica Now Display Medium. Section headings and product titles at 24–32px.
- **Body Medium:** Helvetica Now Text Medium (weight 500). Links, buttons, captions, emphasized body.
- **Body:** Helvetica Now Text (weight 400). Standard body copy, descriptions, metadata.
- **Arabic:** Neue Frutiger Arabic — locale-specific alternative.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference each role via tokens.

| Token | Use |
|---|---|
| `display` | Nike Futura ND uppercase hero headline (96px) |
| `heading-1` | Section titles |
| `heading-2` | Subsections |
| `heading-3` | Card titles |
| `body` | Product descriptions |
| `body-medium` | Emphasized text |
| `link` / `link-small` | Navigation, footer/utility links |
| `button` / `button-small` | CTA text |
| `caption` | Price labels |
| `small` | Timestamps |
| `tiny` | Legal text |

### Principles

Nike's typography is a study in tension. The display layer — Nike Futura ND at 96px with a devastating 0.90 line-height — is engineered to feel like a stadium scoreboard: massive, condensed, uppercase, impossible to ignore. It transforms headlines into battle cries. Below the display layer, Helvetica Now provides a clinical counterpoint: Swiss-precision legibility with generous 1.75 line-height for comfortable product browsing. Weight 500 (Medium) dominates throughout the body text, giving Nike's prose a slight assertiveness without the heaviness of bold — every sentence reads like a confident recommendation, not a shout.

## Layout

### Spacing System

The complete spacing scale lives in the `spacing:` token block above. Base unit is `{spacing.xs}` (4px), primary grid is 8px multiples.

### Grid & Container
- Max container width: 1920px
- Standard content width: ~1440px with horizontal padding
- Product grid: 3-column on desktop, 2-column on tablet, 1-column on mobile
- Category grid: 3-column with full-bleed images
- Grid gap: 4–12px between product cards (intentionally tight)
- Horizontal padding: `{spacing.4xl}` desktop, `{spacing.2xl}` tablet, `{spacing.lg}` mobile

### Whitespace Philosophy
Nike's whitespace strategy is deliberately aggressive — not in the luxurious, breathing way of a fashion brand, but in a compressed, high-density way that fills every pixel with either content or intentional absence. Product grids use minimal gaps (4–12px) to create a sense of abundance and choice. Section breaks are generous (`{spacing.4xl}`–`{spacing.6xl}`) to separate shopping contexts. The overall effect is a store that feels packed with product while remaining navigable — like a well-organized athletic superstore.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Default state for everything |
| Divider | `0 -1px 0 0 {colors.gray-200} inset` | Subtle inset line between sections |
| Focus | `0 0 0 2px {colors.focus-ring}` | Keyboard focus ring |
| Overlay | Dark scrim over photography | Text-on-image legibility |

Nike's elevation philosophy is radically flat. There are no card shadows, no hover lifts, no floating elements. Depth is communicated exclusively through color — dark sections recede, light sections advance, grey shifts indicate state changes. This flatness reinforces the athletic, no-nonsense brand personality: no visual frills, just direct communication. The only "shadow" in the entire system is a 1px inset divider line and the accessibility-required focus ring.

### Decorative Depth
- **Hero photography overlays**: Dark gradient scrims over full-bleed photography for text readability
- **Product background gradients**: Colored backgrounds behind hero product shots (e.g., red shoe on red gradient)
- **Banner bars**: Solid `{colors.ink}` promotional strips at page top

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Product images, hero photography (sharp edges) |
| `sm` | 8px | Form inputs (non-search) |
| `md` | 18px | Small interactive elements |
| `lg` | 20px | Containers, cards with UI content |
| `xl` | 24px | Search inputs, medium pills |
| `pill` | 30px | Buttons, tags, filters (full pill) |
| `full` | 9999px | Circular icon buttons, avatar placeholders |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (e.g. `{components.button-primary}`, `{components.card-product}`) rather than reconstructing them.

### Buttons
- **`button-primary`** — Nike Black pill CTA. Hover shifts background to `{colors.gray-500}`.
- **`button-primary-on-dark`** — White pill on dark backgrounds.
- **`button-secondary`** — Outlined pill, transparent fill, `{colors.gray-300}` border.
- **`button-disabled`** — `{colors.gray-200}` fill with `{colors.gray-400}` text.
- **`button-icon`** — Circular icon button on `{colors.gray-100}`.

### Cards
- **`card-product`** — Edge-to-edge product image (no radius) with text metadata below in `{spacing.md}` gap. No shadows, no hover lift.
- **`card-ui`** — UI container with `{rounded.lg}` corners and `{spacing.2xl}` interior padding.

### Inputs
- **`input`** — `{colors.gray-100}` background, `{rounded.sm}` corners. Focus shifts border to `{colors.border-active}` with focus ring.
- **`input-search`** — Same fill, `{rounded.xl}` pill shape.

### Navigation
- **`nav-bar`** — Sticky white header, ~60px tall. Swoosh logo left, category links centered, search/favorites/cart icons right. Hover shifts text to `{colors.gray-500}`.

### Promotional Banner
- **`banner-promo`** — Full-width `{colors.ink}` bar with white centered text. Used for shipping promos, member benefits, sale announcements.

### Filter Pill
- **`filter-pill`** — Pill-shaped filter/tag, white fill, dark text.

### Badges
- **`badge-error`** / **`badge-success`** — Pill-shaped semantic indicators.

## Do's and Don'ts

### Do
- Use Nike Black (`{colors.ink}`) for all primary text — never pure `#000000`
- Keep buttons pill-shaped (`{rounded.pill}`) and limited to primary/secondary variants
- Use full-bleed, edge-to-edge photography for hero sections — no border radius on images
- Let product photography provide all color vibrancy; keep UI monochromatic
- Use uppercase Nike Futura ND ONLY for display headlines (96px+)
- Maintain tight product grid gaps (4–12px) for a dense, abundant feel
- Use `{colors.gray-100}` for all input and placeholder backgrounds
- Reserve color exclusively for semantic meaning (red=error, green=success, blue=link)
- Use weight 500 (Medium) for all interactive text elements

### Don't
- Don't add shadows to cards — Nike's elevation model is entirely flat
- Don't use border radius on product imagery — only UI elements get rounded corners
- Don't introduce brand colors beyond the grey scale for UI elements
- Don't use Nike Futura ND below 24px — it's exclusively a display face
- Don't add hover lift effects — Nike cards don't animate on hover
- Don't use regular weight (400) for buttons or links — always use 500
- Don't place colored backgrounds behind UI elements — color is reserved for product contexts
- Don't use more than two levels of text hierarchy per card (title + body)
- Don't add decorative dividers — the 1px inset is the only divider pattern
- Don't soften the contrast — Nike's design deliberately pushes black-on-white to maximum

---

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, hamburger nav, display text scales down, tight 16px padding |
| Small Tablet | 640-768px | 2-column product grid begins, nav still collapsed |
| Tablet | 768-960px | 2-column grids, category cards scale, horizontal padding 24px |
| Small Desktop | 960-1024px | Nav expands to full horizontal, 3-column product grid |
| Desktop | 1024-1440px | Full layout, expanded nav, 3-column grids, 48px padding |
| Large Desktop | >1440px | Max-width container centered, increased margins, hero images full-bleed |

### Touch Targets

- Minimum touch target: 44x44px (WCAG AAA)
- Mobile nav icons: 48x48px touch area
- Product cards: full surface is tappable
- Filter pills: minimum 36px height with 12px padding

### Collapsing Strategy

- **Navigation**: Full category links → hamburger menu below 960px; search, favorites, cart icons remain visible
- **Product grids**: 3-col → 2-col at 960px → 1-col at 640px
- **Hero sections**: Display text scales from 96px → 64px → 48px; hero images remain full-bleed at all sizes
- **Category cards**: 3-col → 2-col → 1-col with maintained full-bleed imagery
- **Section padding**: 80px → 48px → 32px → 24px as viewport narrows
- **Promotional banner**: text wraps or truncates, maintains dark background

### Image Behavior

- Responsive images via Nike CDN (`c.static-nike.com`) with width parameters
- Product images: srcset with multiple resolutions (w_320, w_640, w_960, w_1920)
- Hero images: full-bleed at all breakpoints, aspect ratio shifts (16:9 desktop → 4:3 mobile)
- Lazy loading: native `loading="lazy"`, grey-100 placeholder during load
- Art direction: hero crops change between desktop and mobile compositions

---

## Agent Prompt Guide

### Quick Color Reference

- Primary CTA: Nike Black (`#111111`)
- Background: White (`#FFFFFF`)
- Secondary surface: Light Gray (`#F5F5F5`)
- Heading text: Nike Black (`#111111`)
- Body text / hover: Secondary Text (`#707072`)
- Border: Border Secondary (`#CACACB`)
- Error: Nike Red (`#D30005`)
- Link: Link Blue (`#1151FF`)

### Example Component Prompts

- "Create a product hero section with full-bleed edge-to-edge photography, no border radius, a dark gradient overlay for text, and a massive uppercase 96px/500 headline in Nike Futura style with 0.90 line-height and a Nike Black (#111111) pill button (30px radius)"
- "Design a 3-column product card grid with square images (no border radius), 4px gap between cards, product name in 16px/500 Nike Black (#111111), price in 14px/500, and secondary text in Grey-500 (#707072)"
- "Build a sticky white navigation bar with a left-aligned logo, centered category links in 16px/500 (#111111) with hover color #707072, and right-aligned search (24px radius, #F5F5F5 background), favorites, and cart icons"
- "Create a promotional banner strip with #111111 background, white 12px/500 centered text, and 8px vertical padding — full width, no border radius"
- "Design a secondary outlined button with transparent background, 1.5px #CACACB border, 30px pill radius, 16px/500 #111111 text, hover border darkening to #707072"

### Iteration Guide

When refining existing screens generated with this design system:
1. Focus on ONE component at a time
2. Reference specific color names and hex codes from this document
3. Remember: product photography is the color — UI stays monochromatic
4. Use the grey scale for state changes: #F5F5F5 → #E5E5E5 → #CACACB → #707072
5. If something feels too colorful in the UI, it probably is — Nike keeps UI greyscale
6. Display type (Nike Futura) should ALWAYS be uppercase and never below 24px
7. Body type (Helvetica Now) should almost always be weight 500 for interactive elements
