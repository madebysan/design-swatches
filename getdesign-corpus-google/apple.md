---
version: alpha
name: Apple
description: Cinematic product-as-sculpture system — alternating pure-black and light-gray sections, SF Pro with optical sizing, single Apple Blue accent, and 980px pill CTAs.

colors:
  # Surfaces — binary section rhythm
  background: "#f5f5f7"
  background-dark: "#000000"
  surface: "#ffffff"
  surface-button-light: "#fafafc"
  surface-button-active: "#ededf2"

  # Dark surface ladder
  dark-surface-1: "#272729"
  dark-surface-2: "#262628"
  dark-surface-3: "#28282a"
  dark-surface-4: "#2a2a2d"
  dark-surface-5: "#242426"

  # Ink
  ink: "#1d1d1f"
  ink-inverted: "#ffffff"

  # Text states (opaque approximations)
  on-background: "#1d1d1f"
  on-surface: "#1d1d1f"
  on-primary: "#ffffff"
  text-secondary: "#333333"  # was rgba(0,0,0,0.8) — flattened
  text-tertiary: "#858586"  # was rgba(0,0,0,0.48) — flattened
  text-on-dark-hover: "#5c5c5c"  # was rgba(255,255,255,0.32) — flattened on dark

  # Brand accent — interactive only
  primary: "#0071e3"
  link-light: "#0066cc"
  link-dark: "#2997ff"

  # Borders + overlay
  border-soft: "#f5f5f5"  # was rgba(0,0,0,0.04) — flattened
  overlay-media: "#d2d2d7"  # was rgba(210,210,215,0.64) — flattened on white
  shadow-card: "#c7c7c7"  # was rgba(0,0,0,0.22) — flattened
  nav-glass: "#000000"  # base for translucent nav (rgba(0,0,0,0.8))

typography:
  display-hero:
    fontFamily: "SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.07
    letterSpacing: -0.28px
  heading-section:
    fontFamily: "SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0px
  tile-heading:
    fontFamily: "SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.14
    letterSpacing: 0.196px
  card-title:
    fontFamily: "SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 21px
    fontWeight: 700
    lineHeight: 1.19
    letterSpacing: 0.231px
  heading-sub:
    fontFamily: "SF Pro Display, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 21px
    fontWeight: 400
    lineHeight: 1.19
    letterSpacing: 0.231px
  nav-heading:
    fontFamily: "SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 34px
    fontWeight: 600
    lineHeight: 1.47
    letterSpacing: -0.374px
  sub-nav:
    fontFamily: "SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.47
    letterSpacing: -0.374px
  body-emphasis:
    fontFamily: "SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.24
    letterSpacing: -0.374px
  button-large:
    fontFamily: "SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.0
    letterSpacing: 0px
  button-ui:
    fontFamily: "SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 2.41
    letterSpacing: 0px
  link:
    fontFamily: "SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: -0.224px
  caption:
    fontFamily: "SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: -0.224px
  caption-bold:
    fontFamily: "SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.224px
  micro:
    fontFamily: "SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: -0.12px
  nano:
    fontFamily: "SF Pro Text, SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.47
    letterSpacing: -0.08px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 11px
  lg: 14px
  xl: 17px
  2xl: 24px
  3xl: 40px
  4xl: 64px
  5xl: 96px

rounded:
  none: 0px
  xs: 5px
  sm: 8px
  md: 11px
  lg: 12px
  pill: 9999px

components:
  # Translucent nav bar
  nav-bar:
    backgroundColor: "{colors.nav-glass}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.micro}"
    rounded: "{rounded.none}"
    padding: 12px 24px

  # Primary Apple Blue CTA
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 8px 15px
  button-primary-active:
    backgroundColor: "{colors.surface-button-active}"
    textColor: "{colors.ink}"

  # Dark CTA
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 8px 15px

  # Pill outline CTA — signature "Learn more" / "Shop" link
  button-pill-outline:
    backgroundColor: "{colors.background}"
    textColor: "{colors.link-light}"
    typography: "{typography.link}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  button-pill-outline-dark:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.link-dark}"
    typography: "{typography.link}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  # Filter / search button
  button-filter:
    backgroundColor: "{colors.surface-button-light}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 0px 14px

  # Media control — circular
  button-media:
    backgroundColor: "{colors.overlay-media}"
    textColor: "{colors.text-tertiary}"
    rounded: "{rounded.pill}"
    size: 44px
  button-media-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"

  # Card — light section
  card-light:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 32px

  # Card — dark section
  card-dark:
    backgroundColor: "{colors.dark-surface-1}"
    textColor: "{colors.ink-inverted}"
    rounded: "{rounded.sm}"
    padding: 32px

  # Elevated product card with shadow
  card-elevated:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 32px

  # Lifestyle image container
  card-lifestyle:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 0px

  # Form input
  input:
    backgroundColor: "{colors.surface-button-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px 14px

  # Inline link tag
  badge:
    backgroundColor: "{colors.background}"
    textColor: "{colors.link-light}"
    typography: "{typography.link}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
---

# Apple Design System

## Overview

Apple's website is a masterclass in controlled drama — vast expanses of pure black (`{colors.background-dark}`) and near-white (`{colors.background}`) serve as cinematic backdrops for products that are photographed as if they were sculptures in a gallery. The design philosophy is reductive to its core: every pixel exists in service of the product, and the interface itself retreats until it becomes invisible. This is not minimalism as aesthetic preference; it is minimalism as reverence for the object.

The typography anchors everything. San Francisco (SF Pro Display for large sizes, SF Pro Text for body) is Apple's proprietary typeface, engineered with optical sizing that automatically adjusts letterforms depending on point size. At display sizes (56px), weight 600 with a tight line-height of 1.07 and subtle negative letter-spacing (-0.28px) creates headlines that feel machined rather than typeset — precise, confident, and unapologetically direct. At body sizes (17px), the tracking loosens slightly (-0.374px) and line-height opens to 1.47, creating a reading rhythm that is comfortable without ever feeling slack.

The color story is starkly binary. Product sections alternate between pure black backgrounds with white text and light gray (`{colors.background}`) backgrounds with near-black text (`{colors.ink}`). This creates a cinematic pacing — dark sections feel immersive and premium, light sections feel open and informational. The only chromatic accent is Apple Blue (`{colors.primary}`), reserved exclusively for interactive elements: links, buttons, and focus states. This singular accent color in a sea of neutrals gives every clickable element unmistakable visibility.

**Key Characteristics:**
- SF Pro Display/Text with optical sizing — letterforms adapt automatically to size context
- Binary light/dark section rhythm: black alternating with light gray (`{colors.background}`)
- Single accent color: Apple Blue (`{colors.primary}`) reserved exclusively for interactive elements
- Product-as-hero photography on solid color fields — no gradients, no textures, no distractions
- Extremely tight headline line-heights (1.07-1.14) creating compressed, billboard-like impact
- Full-width section layout with centered content — the viewport IS the canvas
- Pill-shaped CTAs (980px radius) creating soft, approachable action buttons
- Generous whitespace between sections allowing each product moment to breathe

## Colors

### Primary
- **Pure Black** (`{colors.background-dark}`): Hero section backgrounds, immersive product showcases. The darkest canvas for the brightest products.
- **Light Gray** (`{colors.background}`): Alternate section backgrounds, informational areas. Not white — the slight blue-gray tint prevents sterility.
- **Near Black** (`{colors.ink}`): Primary text on light backgrounds, dark button fills. Slightly warmer than pure black for comfortable reading.

### Interactive
- **Apple Blue** (`{colors.primary}`): Primary CTA backgrounds, focus rings. The ONLY chromatic color in the interface.
- **Link Blue** (`{colors.link-light}`): Inline text links. Slightly darker than Apple Blue for text-level readability.
- **Bright Blue** (`{colors.link-dark}`): Links on dark backgrounds. Higher luminance for contrast on black sections.

### Text
- **White** (`{colors.ink-inverted}`): Text on dark backgrounds, button text on blue/dark CTAs.
- **Near Black** (`{colors.ink}`): Primary body text on light backgrounds.
- **Black 80%** (`{colors.text-secondary}`): Secondary text, nav items on light backgrounds.
- **Black 48%** (`{colors.text-tertiary}`): Tertiary text, disabled states, carousel controls.

### Surface & Dark Variants
- **Dark Surface 1** (`{colors.dark-surface-1}`): Card backgrounds in dark sections.
- **Dark Surface 2** (`{colors.dark-surface-2}`): Subtle surface variation in dark contexts.
- **Dark Surface 3** (`{colors.dark-surface-3}`): Elevated cards on dark backgrounds.
- **Dark Surface 4** (`{colors.dark-surface-4}`): Highest dark surface elevation.
- **Dark Surface 5** (`{colors.dark-surface-5}`): Deepest dark surface tone.

### Button States
- **Button Active** (`{colors.surface-button-active}`): Active/pressed state for light buttons.
- **Button Default Light** (`{colors.surface-button-light}`): Search/filter button backgrounds.
- **Overlay** (`{colors.overlay-media}`): Media control scrims, overlays.
- **Hover on Dark** (`{colors.text-on-dark-hover}`): Hover state on dark modal close buttons.

### Shadows
- **Card Shadow** (`{colors.shadow-card}`): Soft, diffused elevation for product cards. Offset and wide blur create a natural, photographic shadow.

## Typography

### Font Family
- **Display**: `SF Pro Display`, with fallbacks: `SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif`
- **Body**: `SF Pro Text`, with fallbacks: `SF Pro Icons, Helvetica Neue, Helvetica, Arial, sans-serif`
- SF Pro Display is used at 20px and above; SF Pro Text is optimized for 19px and below.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Use those tokens directly via reference.

| Token | Use |
|---|---|
| `display-hero` | Product launch headlines, maximum impact (56px) |
| `heading-section` | Feature section titles (40px) |
| `tile-heading` | Product tile headlines (28px) |
| `card-title` | Bold card headings (21px / 700) |
| `heading-sub` | Regular card headings (21px / 400) |
| `nav-heading` | Large navigation headings |
| `sub-nav` | Light sub-navigation text |
| `body` | Standard reading text (17px) |
| `body-emphasis` | Emphasized body text, labels |
| `button-large` | Large button text, light weight |
| `button-ui` | Standard button text |
| `link` | Body links, "Learn more" |
| `caption` | Secondary text, descriptions (14px) |
| `caption-bold` | Emphasized captions |
| `micro` | Fine print, footnotes (12px) |
| `nano` | Legal text, smallest size (10px) |

### Principles
- **Optical sizing as philosophy**: SF Pro automatically switches between Display and Text optical sizes. Display versions have wider letter spacing and thinner strokes optimized for large sizes; Text versions are tighter and sturdier for small sizes.
- **Weight restraint**: The scale spans 300 to 700 but most text lives at 400 and 600. Weight 300 appears only on large decorative text. Weight 700 is rare, used only for bold card titles.
- **Negative tracking at all sizes**: Apple applies subtle negative letter-spacing even at body sizes (-0.374px at 17px, -0.224px at 14px, -0.12px at 12px). This creates universally tight, efficient text.
- **Extreme line-height range**: Headlines compress to 1.07 while body text opens to 1.47, and some button contexts stretch to 2.41. This dramatic range creates clear visual hierarchy through rhythm alone.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px. The scale is dense at small sizes with granular increments, then jumps in larger steps for cinematic section pacing.

### Grid & Container
- Max content width: approximately 980px (the recurring "980px radius" in pill buttons echoes this width)
- Hero: full-viewport-width sections with centered content block
- Product grids: 2-3 column layouts within centered container
- Single-column for hero moments — one product, one message, full attention
- No visible grid lines or gutters — spacing creates implied structure

### Whitespace Philosophy
- **Cinematic breathing room**: Each product section occupies a full viewport height. Whitespace between products is the pause between scenes in a film.
- **Vertical rhythm through color blocks**: Apple uses alternating background colors (black, `{colors.background}`, white). Each color change signals a new "scene."
- **Compression within, expansion between**: Text blocks are tightly set while the space surrounding them is vast.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, solid background | Standard content sections |
| Navigation Glass | `backdrop-filter: saturate(180%) blur(20px)` over `{colors.nav-glass}` | Sticky navigation bar — the glass effect |
| Subtle Lift (Level 1) | `3px 5px 30px` drop using `{colors.shadow-card}` | Product cards, floating elements |
| Media Control | `{colors.overlay-media}` background with scale transforms | Play/pause, carousel controls |
| Focus (Accessibility) | `2px solid {colors.primary}` outline | Keyboard focus on all interactive elements |

**Shadow Philosophy**: Apple uses shadow extremely sparingly. The primary shadow is soft, wide, and offset — mimicking diffused studio light casting a natural shadow beneath a physical object. Most elements have NO shadow at all; elevation comes from background color contrast (dark card on darker background, or light card on slightly different gray).

### Decorative Depth
- Navigation glass: translucent, blurred navigation bar floating above content
- Section color transitions: depth implied by alternation between black and light gray sections
- Product photography shadows: products cast shadows in their photography, so the UI doesn't add synthetic ones

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Flat sections |
| `xs` | 5px | Small containers, link tags |
| `sm` | 8px | Buttons, product cards, image containers |
| `md` | 11px | Search inputs, filter buttons |
| `lg` | 12px | Feature panels, lifestyle image containers |
| `pill` | 9999px | CTA links, navigation pills, media controls (50%) |

The "980px" radius value seen in source CSS is functionally equivalent to `{rounded.pill}` — it's used to force a pill shape regardless of element size.

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Apple Blue CTA ("Buy", "Shop iPhone")
- **`button-dark`** — Near-black variant
- **`button-pill-outline`** / **`button-pill-outline-dark`** — Signature "Learn more" / "Shop" pill links
- **`button-filter`** — Search bars, filter controls (`{rounded.md}`, soft background)
- **`button-media`** — Circular media controls; focus state inverts to white background

### Cards & Containers
- **`card-light`** / **`card-dark`** — Section-aware card variants with no border
- **`card-elevated`** — Soft offset shadow for floating product cards
- **`card-lifestyle`** — Larger 12px radius for lifestyle image containers

### Navigation
**`nav-bar`** — Translucent dark glass with `backdrop-filter: saturate(180%) blur(20px)`. 48px height, 12px white text, Apple logo + links + search/bag icons.

### Image Treatment
- Products on solid-color fields — no backgrounds, no context
- Full-bleed section images that span the entire viewport width
- Product photography at extremely high resolution with subtle shadows
- Lifestyle images confined to rounded-corner containers (`{rounded.lg}`+)

### Distinctive Components
- **Product Hero Module** — Full-viewport-width section, 56px headline + one-line descriptor + two pill CTAs side by side
- **Product Grid Tile** — Square card on contrasting background with product image dominating 60-70%
- **Feature Comparison Strip** — Horizontal scroll of product variants

## Do's and Don'ts

### Do
- Use SF Pro Display at 20px+ and SF Pro Text below 20px — respect the optical sizing boundary
- Apply negative letter-spacing at all text sizes — Apple tracks tight universally
- Use Apple Blue (`{colors.primary}`) ONLY for interactive elements
- Alternate between black and light gray (`{colors.background}`) section backgrounds for cinematic rhythm
- Use `{rounded.pill}` for CTA links — the signature Apple link shape
- Keep product imagery on solid-color fields with no competing visual elements
- Use the translucent dark glass for sticky navigation
- Compress headline line-heights to 1.07-1.14 — Apple headlines are famously tight

### Don't
- Don't introduce additional accent colors — the entire chromatic budget is spent on blue
- Don't use heavy shadows or multiple shadow layers — one soft diffused shadow or nothing
- Don't use borders on cards or containers — Apple almost never uses visible borders
- Don't apply wide letter-spacing to SF Pro — it is designed to run tight at every size
- Don't use weight 800 or 900 — the maximum is 700, and even that is rare
- Don't add textures, patterns, or gradients to backgrounds — solid colors only
- Don't make the navigation opaque — the glass blur effect is essential
- Don't center-align body text — Apple body copy is left-aligned; only headlines center
- Don't use rounded corners larger than 12px on rectangular elements (`{rounded.pill}` is for pills only)

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Small Mobile | <360px | Minimum supported, single column |
| Mobile | 360-480px | Standard mobile layout |
| Mobile Large | 480-640px | Wider single column, larger images |
| Tablet Small | 640-834px | 2-column product grids begin |
| Tablet | 834-1024px | Full tablet layout, expanded nav |
| Desktop Small | 1024-1070px | Standard desktop layout begins |
| Desktop | 1070-1440px | Full layout, max content width |
| Large Desktop | >1440px | Centered with generous margins |

### Touch Targets
- Primary CTAs: 8px 15px padding creating ~44px touch height
- Navigation links: 48px height with adequate spacing
- Media controls: circular buttons, minimum 44x44px
- "Learn more" pills: generous padding for comfortable tapping

### Collapsing Strategy
- Hero headlines: 56px Display → 40px → 28px on mobile, maintaining tight line-height
- Product grids: 3-column → 2-column → single column stacked
- Navigation: full horizontal nav → compact mobile menu (hamburger)
- Section backgrounds: maintain full-width color blocks at all breakpoints
- Image sizing: products scale proportionally, never crop

### Image Behavior
- Product photography maintains aspect ratio at all breakpoints
- Hero product images scale down but stay centered
- Full-bleed section backgrounds persist at every size
- Lifestyle images may crop on mobile but maintain rounded corners
- Lazy loading for below-fold product images

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Apple Blue (`{colors.primary}`)
- Page background (light): `{colors.background}`
- Page background (dark): `{colors.background-dark}`
- Heading text (light): `{colors.ink}`
- Heading text (dark): `{colors.ink-inverted}`
- Body text: `{colors.text-secondary}` on light, `{colors.ink-inverted}` on dark
- Link (light bg): `{colors.link-light}`
- Link (dark bg): `{colors.link-dark}`
- Focus ring: `{colors.primary}`
- Card shadow: `{colors.shadow-card}` at 22% opacity, `3px 5px 30px`

### Example Component Prompts
- "Create a hero section on `{colors.background-dark}`. Headline at 56px SF Pro Display weight 600, line-height 1.07, letter-spacing -0.28px, color white. One-line subtitle at 21px SF Pro Display weight 400. Two pill CTAs: 'Learn more' (transparent bg, white text, 1px solid white border, `{rounded.pill}`) and 'Buy' (`{colors.primary}` bg, white text, `{rounded.sm}`, 8px 15px padding)."
- "Design a product card: `{colors.background}` background, `{rounded.sm}` border-radius, no border, no shadow. Product image top 60% of card on solid background. Title at 28px SF Pro Display weight 400, letter-spacing 0.196px. Description at 14px SF Pro Text weight 400, color `{colors.text-secondary}`. 'Learn more' and 'Shop' links in `{colors.link-light}` at 14px."
- "Build the Apple navigation: sticky, 48px height, background `{colors.nav-glass}` at 80% with backdrop-filter: saturate(180%) blur(20px). Links at 12px SF Pro Text weight 400, white text. Apple logo left, links centered, search and bag icons right."
- "Create an alternating section layout: first section `{colors.background-dark}` bg with white text and centered product image, second section `{colors.background}` bg with `{colors.ink}` text. Each section near full-viewport height with 56px headline and two pill CTAs below."
- "Design a 'Learn more' link: text `{colors.link-light}` on light bg or `{colors.link-dark}` on dark bg, 14px SF Pro Text, underline on hover. After the text, include a right-arrow chevron character. Wrap in a container with `{rounded.pill}` for pill shape when used as a standalone CTA."

### Iteration Guide
1. Every interactive element gets Apple Blue (`{colors.primary}`) — no other accent colors
2. Section backgrounds alternate: black for immersive moments, `{colors.background}` for informational moments
3. Typography optical sizing: SF Pro Display at 20px+, SF Pro Text below — never mix
4. Negative letter-spacing at all sizes
5. The navigation glass effect is non-negotiable — it defines the Apple web experience
6. Products always appear on solid color fields — never on gradients or textures in hero modules
7. Shadow is rare and always soft, or nothing at all
8. Pill CTAs use `{rounded.pill}` — the signature Apple capsule shape
