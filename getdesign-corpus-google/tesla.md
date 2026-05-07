---
version: alpha
name: Tesla
description: Radical subtraction — pure white or pure black canvas, single Electric Blue CTA, Universal Sans, photography as the only decoration, 4px radius, zero shadows.

colors:
  # Canvas
  background: "#ffffff"
  surface: "#f4f4f4"
  surface-dark: "#171a20"
  ink: "#171a20"
  ink-inverted: "#ffffff"

  # Brand accent — sole chromatic color
  primary: "#3e6ae1"

  # Text hierarchy
  on-background: "#171a20"
  on-primary: "#ffffff"
  on-surface-dark: "#ffffff"
  text-body: "#393c41"
  text-tertiary: "#5c5e62"
  text-placeholder: "#8e8e8e"

  # Borders + dividers
  border: "#eeeeee"
  border-subtle: "#d0d1d2"

  # Frosted nav + overlay (opaque approximations)
  frost-white: "#fafafa"   # was rgba(255,255,255,.75) — flattened over white
  overlay-modal: "#525252" # was rgba(128,128,128,.65) — flattened over white
  shadow-soft: "#f2f2f2"   # was rgba(0,0,0,.05) — flattened over white

typography:
  hero:
    fontFamily: "Universal Sans Display, -apple-system, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0px
  product-name:
    fontFamily: "Universal Sans Text, -apple-system, Arial, sans-serif"
    fontSize: 17px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: 0px
  nav-item:
    fontFamily: "Universal Sans Text, -apple-system, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0px
  body:
    fontFamily: "Universal Sans Text, -apple-system, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  button-ui:
    fontFamily: "Universal Sans Text, -apple-system, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0px
  sub-link:
    fontFamily: "Universal Sans Text, -apple-system, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  promo:
    fontFamily: "Universal Sans Display, -apple-system, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 0.91
    letterSpacing: 0px
  category-label:
    fontFamily: "Universal Sans Text, -apple-system, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px

rounded:
  none: 0px
  sm: 4px
  md: 12px
  pill: 9999px

components:
  # Primary CTA — sole chromatic moment
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 4px 16px
  button-primary-hover:
    backgroundColor: "{colors.primary}"

  # Secondary CTA — white surface
  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-body}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 4px 16px

  # Top nav button
  button-nav:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-item}"
    rounded: "{rounded.sm}"
    padding: 4px 16px
  button-nav-hover:
    backgroundColor: "{colors.surface}"

  # Text link
  text-link:
    textColor: "{colors.text-tertiary}"
    typography: "{typography.sub-link}"

  # Vehicle card — transparent in nav panel
  card-vehicle:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.none}"
    padding: 16px

  # Category card — full-bleed photography with corners
  card-category:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.md}"
    padding: 0px

  # Input
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    borderColor: "{colors.border}"

  # Frosted nav bar
  nav-bar:
    backgroundColor: "{colors.frost-white}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-item}"
    padding: 8px 24px

  # Modal overlay
  modal-overlay:
    backgroundColor: "{colors.overlay-modal}"
---

# Tesla Design System

## Overview

Tesla's website is an exercise in radical subtraction — a digital showroom where the product is everything and the interface is almost nothing. The page opens with a full-viewport hero that fills the entire screen with a single, uncropped photograph of a car. There are no decorative borders, no gradients layered onto chrome, no patterns, no shadows, no atmospheric washes. The canvas is either pure white (`{colors.background}`) or pure black — Tesla alternates between the two as the only two background values in the system. The UI exists only to provide just enough navigational structure to get out of the way. Every pixel that isn't product imagery is empty space, and that restraint is the design system's most powerful statement.

The color philosophy is ascetic rather than expressive. A single blue (`{colors.primary}`) exists only as a functional signal — it lives on the primary CTA background and on text links, never as atmospheric tint, never as decorative fill, never as a glow or a wash. Three shades of dark gray handle text hierarchy. White handles everything else. The emotional weight is carried entirely by photography and whitespace — the UI has no opinion of its own. The navigation bar floats above the hero with no visible background, border, or shadow; the TESLA wordmark and five navigation labels simply exist in the space, trusting the imagery beneath them to provide sufficient contrast.

Typography recently transitioned from Gotham to Universal Sans — a custom family split into "Display" for headlines and "Text" for body/UI elements — unifying the website, mobile app, and in-car software into a single typographic voice. The Display variant renders hero titles at 40px weight 500, while the Text variant handles everything from navigation (14px/500) to body copy (14px/400). The font carries a geometric precision with slightly humanist terminals that feels engineered rather than designed — exactly matching Tesla's brand identity of technology that doesn't need to announce itself. Headings never carry colored accents. There are no text shadows, no text gradients, no decorative type treatments. Every letterform earns its place through clarity alone.

**Key Characteristics:**
- Full-viewport hero sections (100vh) showing a single piece of car photography — no overlays or tints
- Pure white OR pure black as the canvas — never tinted, never gradient, never patterned
- Electric Blue (`{colors.primary}`) appears ONLY on primary CTA buttons and text links
- Zero UI decoration on chrome: no shadows, no gradients, no borders on tiles
- Universal Sans family (Display + Text) unifying web, app, and in-car interfaces
- Headings always neutral (`{colors.ink}` on white, `{colors.ink-inverted}` on black) — no colored accents on type
- Photography carries 100% of the visual richness
- Transparent nav floating directly over hero imagery
- 0.33s cubic-bezier transitions as the universal timing
- "Ask a Question" persistent chatbot bar anchored to the viewport bottom

## Colors

### Primary
- **Electric Blue** (`{colors.primary}`): The ONLY chromatic color. Used strictly for primary CTA background and text links — never as atmospheric tint, glow, decorative fill, or heading accent.
- **Pure White** (`{colors.background}`): Primary canvas — backgrounds, panels, navigation, surface tiles.
- **Carbon Dark** (`{colors.surface-dark}`): Secondary canvas. On dark sections, all text inverts to `{colors.ink-inverted}` and the same minimalism rules apply.

### Surface & Background
- **White Canvas** (`{colors.background}`): Page background, navigation panel, dropdown menus, and surface containers.
- **Light Ash** (`{colors.surface}`): Subtle alternate surface for section differentiation.
- **Carbon Dark** (`{colors.surface-dark}`): Dark surface for hero text overlays.
- **Frosted Glass** (`{colors.frost-white}`): Semi-transparent white for navigation backdrop-filter effects on scroll.

### Neutrals & Text
- **Carbon Dark** (`{colors.ink}`): Primary heading and navigation text.
- **Graphite** (`{colors.text-body}`): Body text and secondary content.
- **Pewter** (`{colors.text-tertiary}`): Tertiary text for sub-links.
- **Silver Fog** (`{colors.text-placeholder}`): Placeholder text and disabled states.
- **Cloud Gray** (`{colors.border}`): Light borders and divider lines.
- **Pale Silver** (`{colors.border-subtle}`): Subtle UI borders and delineation.

Tesla's marketing site avoids semantic color coding and gradients entirely. Depth is achieved through photography and whitespace; layering is opacity-based, not gradient-based.

## Typography

### Font Family
- **Display**: `Universal Sans Display`, fallback `-apple-system, Arial, sans-serif` — used for hero titles and large model names.
- **Text/UI**: `Universal Sans Text`, fallback `-apple-system, Arial, sans-serif` — used for navigation, body, buttons, and UI text.
- No OpenType features, no italics on the marketing site.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.hero}`, `{typography.body}`, etc.).

| Token | Use |
|---|---|
| `hero` | 40px hero titles — model names on dark photography |
| `product-name` | Model names in nav panel and cards |
| `nav-item` | Primary navigation labels |
| `body` | Paragraph and descriptive content |
| `button-ui` | CTA button text |
| `sub-link` | Tertiary links (Learn, Order, Experience) |
| `promo` | White promotional eyebrow text on hero ("0% APR Available") |
| `category-label` | White text labels on category cards |

### Principles
- **"Normal" letter-spacing everywhere**: Tesla uses default tracking at every level — the typeface speaks for itself.
- **Weight restraint**: Only 500 (medium) for headings/UI and 400 (regular) for body. No bold, no light.
- **Unified sizing**: Most UI text clusters at 14px; only hero (40px) and promo (22px) break away.
- **Display vs Text split**: Two-variant system creates subtle optical correction at scale.
- **No text transforms**: No uppercase in nav or CTAs — confidence through lowercase calm.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px; common values cluster at `{spacing.sm}` and `{spacing.md}`. Section padding uses full-viewport sections with content centered vertically.

### Grid & Container
- Max width: approximately 1383px (full viewport for most content)
- Hero: full-bleed, edge-to-edge, 100vh sections
- Navigation panel: 3-column grid with right-aligned text sidebar
- Category cards: 2-up horizontal layout

### Whitespace Philosophy
Tesla uses whitespace as a luxury signal. Generous vertical spacing (each section is full viewport height) means you see one "message" at a time. White space is the frame that elevates each vehicle to art piece.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 (Flat) | No shadow, no border | Default for all elements at rest |
| Level 1 (Frost) | `{colors.frost-white}` backdrop | Navigation bar on scroll |
| Level 2 (Overlay) | `{colors.overlay-modal}` | Modal overlays and cookie popups |
| Level 3 (Subtle) | `{colors.shadow-soft}` | Minimal shadow hints on rare hover states |

**Shadow Philosophy**: Tesla's approach to elevation is essentially "none." The site avoids box-shadows entirely. Depth comes through z-index layering, opacity-based transparency, and photography itself.

No gradients, glows, or atmospheric effects on UI elements — ever. The hero imagery provides all visual richness; UI chrome stays flat.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Default — sharp edges everywhere |
| `sm` | 4px | Buttons (primary, secondary, nav items) — barely perceptible |
| `md` | 12px | Category cards — noticeable but restrained on larger surfaces |
| `pill` | 9999px | Carousel dot indicators — perfect circles |

The 4px button radius is deliberate and precise — pill or large radii would contradict the technical aesthetic.

## Components

The full component spec lives in the `components:` token block above. Reference component tokens directly (`{components.button-primary}`, `{components.card-category}`).

### Buttons
All buttons use barely-rounded rectangles (`{rounded.sm}`) — sharp, technical, mirroring vehicle precision.

- **`button-primary`** — Electric Blue ground, white text. Used for "Order Now."
- **`button-secondary`** — White ground, graphite text. Used for "View Inventory."
- **`button-nav`** — Transparent until hover, Carbon Dark text. Top nav items.
- **`text-link`** — Pewter text, no background. Sub-links in dropdown panels.

### Cards & Containers
- **`card-vehicle`** — Transparent background, no border, no shadow. Vehicle in nav dropdown panel.
- **`card-category`** — Full-bleed landscape photography, `{rounded.md}`, overflow hidden, white text label top-left.

### Inputs
- **`input`** — Transparent or near-transparent, Carbon Dark text, Universal Sans Text 14px. Minimal border.

### Navigation
- **`nav-bar`** — White or frosted-white background, transitions from transparent over dark hero to opaque white on scroll. No visible separator.

### Image Treatment
- Hero: full-viewport (100vh), edge-to-edge, no padding.
- Vehicle images: transparent PNG renders on white, studio-quality 3/4 angle.
- Category cards: landscape ratio with `{rounded.md}` corners.

## Do's and Don'ts

### Do
- Let photography dominate every screen — the product IS the design
- Use Electric Blue (`{colors.primary}`) exclusively for primary CTAs — never decoration
- Maintain viewport-height sections for major content blocks
- Keep typography at weight 400-500 only — no bold, no light
- Use `{rounded.sm}` for all interactive elements — precision over playfulness
- Trust whitespace as a luxury signal
- Keep all transitions at 0.33s — consistency in motion
- Use transparent PNG vehicle imagery on white for product showcases
- Maintain the Display/Text font split

### Don't
- Don't add shadows to any element — flat, gallery aesthetic
- Don't use more than one chromatic color besides the blue CTA
- Don't apply gradients, patterns, or decorative backgrounds
- Don't use text larger than 40px on web
- Don't add borders to cards or containers — separation through spacing, not lines
- Don't use uppercase text transforms
- Don't introduce rounded-pill buttons or large border-radii
- Don't override Universal Sans
- Don't add hover animations with scale/translate transforms
- Don't clutter the viewport with multiple CTAs

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Single-column layout, hamburger nav, hero text scales to ~28px, CTAs stack vertically |
| Tablet | 768-1024px | 2-column nav panel, hero maintains full-viewport height, CTAs side-by-side |
| Desktop | 1024-1440px | Full horizontal nav, 3-column vehicle grid, hero at 40px, CTAs at 200px/160px |
| Large Desktop | >1440px | Content remains centered, hero scales to fill wider viewports |

### Touch Targets
- Primary CTA buttons: 200px × 40px minimum
- Nav buttons: minimum 32px height with 4px 16px padding
- Carousel arrows: ~44px square white semi-transparent buttons
- Text links: 14px text with adequate line-height spacing

### Collapsing Strategy
- Navigation: horizontal category buttons collapse to hamburger/drawer on mobile
- Hero CTA pair: side-by-side stack vertically on mobile
- Category cards: 2-up collapses to single-column full-width
- Vehicle grid: 3-column → 2-column → single-column
- Section vertical padding remains generous; horizontal padding reduces

### Image Behavior
- Hero images fully responsive at every breakpoint
- Vehicle carousel images use `object-fit: cover`
- Transparent PNG vehicle images scale proportionally within grid cells
- Category card images maintain landscape ratio with overflow hidden

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Electric Blue `{colors.primary}`
- Background: Pure White `{colors.background}`
- Heading text: Carbon Dark `{colors.ink}`
- Body text: Graphite `{colors.text-body}`
- Tertiary text: Pewter `{colors.text-tertiary}`
- Placeholder: Silver Fog `{colors.text-placeholder}`
- Alternate surface: Light Ash `{colors.surface}`
- Dark surface: Carbon Dark `{colors.surface-dark}`

### Example Component Prompts
- "Create a hero section with a full-viewport background image, centered 'Model Y' title in Universal Sans Display at 40px weight 500 in white, a subtitle line below, and two buttons side by side: a primary Electric Blue (`{colors.primary}`) 'Order Now' button and a secondary white 'View Inventory' button, both with 4px border-radius and 40px height"
- "Design a navigation bar with a spaced-letter wordmark on the left, five text buttons (14px, weight 500, `{colors.ink}`) centered, and three icon buttons on the right, all on a white background with no shadow or border"
- "Build a vehicle card grid with 3 columns, each card showing a transparent-background car image above a model name (17px, weight 500, `{colors.ink}`) and two text links (14px, weight 400, `{colors.text-tertiary}`) labeled 'Learn' and 'Order', on a pure white surface"
- "Create a category card with full-bleed landscape photography, 12px border-radius, overflow hidden, and a white text label ('Sport Sedan') positioned in the top-left corner with no overlay gradient"
- "Design a persistent bottom bar with a chat input ('Ask a Question' placeholder), a send icon, and a secondary CTA ('Schedule a Drive Today') with a teal icon, anchored to the viewport bottom on a white background"

### Iteration Guide
1. Focus on ONE component at a time — Tesla's system is so minimal each element must be pixel-perfect
2. Reference specific color tokens — there are only 6-7 colors in the entire system
3. Use natural language descriptions alongside specific measurements — "barely rounded corners" + "border-radius: 4px"
4. Describe the desired "feel" alongside specifics — "gallery-like silence between sections" communicates the philosophy
5. Always verify photography is doing the emotional heavy-lifting — if the UI itself feels "designed," it's too much
