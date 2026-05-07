---
version: alpha
name: Warp
description: Campfire-warm dark terminal aesthetic — earthy near-black canvas, parchment-cream text, restrained Matter sans-serif at Regular weight, nature photography woven with product screenshots.

colors:
  # Primary
  background: "#1a1817"     # warm earthy near-black derived from page background
  surface: "#1a1817"
  ink: "#faf9f6"            # Warm Parchment — primary text
  primary: "#353534"        # Earth Gray — pill button bg

  # Text scale
  on-background: "#faf9f6"
  on-surface: "#faf9f6"
  on-primary: "#afaeac"     # Ash Gray — button text on dark pill
  text-secondary: "#afaeac" # Ash Gray
  text-tertiary: "#868584"  # Stone Gray
  link: "#666469"           # Muted Purple — underlined links

  # Borders & surfaces
  border: "#e2e2e2"         # was rgba(226,226,226,0.35) — flattened for hex
  border-soft: "#454545"    # Dark Charcoal alt border
  surface-veil: "#262421"   # was rgba(255,255,255,0.04) over warm dark — flattened

  # Tag overlay (frosted)
  tag-frost: "#cccccc"      # was rgba(255,255,255,0.16) — flattened
  tag-ink: "#000000"

typography:
  display-hero:
    fontFamily: "Matter, system-ui, sans-serif"
    fontSize: 80px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -2.4px
  display-section:
    fontFamily: "Matter, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.56px
  section-heading:
    fontFamily: "Matter, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.48px
  feature-heading:
    fontFamily: "Matter, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.4px
  sub-heading-large:
    fontFamily: "Matter, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.72px
  card-display:
    fontFamily: "Matter SQ, Matter, system-ui, sans-serif"
    fontSize: 42px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  sub-heading:
    fontFamily: "Matter, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.19
    letterSpacing: 0px
  body-heading:
    fontFamily: "Matter, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.72px
  card-title:
    fontFamily: "Matter Medium, Matter, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.14
    letterSpacing: 0px
  body-large:
    fontFamily: "Matter, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: -0.2px
  body:
    fontFamily: "Matter, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.18px
  nav:
    fontFamily: "Matter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0px
  button-ui:
    fontFamily: "Matter Medium, Matter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0px
  caption:
    fontFamily: "Matter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 1.4px
  small-label:
    fontFamily: "Matter, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 2.4px
  micro:
    fontFamily: "Matter, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0px
  code-ui:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  code-body:
    fontFamily: "Matter Mono, ui-monospace, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -0.2px

spacing:
  micro: 1px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 80px
  5xl: 120px

rounded:
  sm: 4px
  md: 6px
  lg: 8px
  video: 10px
  feature: 12px
  large: 14px
  rounded: 40px
  pill: 50px
  progress: 200px

components:
  # Buttons
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 10px 20px

  button-frosted-tag:
    backgroundColor: "{colors.tag-frost}"
    textColor: "{colors.tag-ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: 1px 6px

  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav}"
    rounded: "{rounded.sm}"
    padding: 8px 12px

  # Cards
  card-photography:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: 0px
  card-bordered:
    backgroundColor: "{colors.surface-veil}"
    textColor: "{colors.ink}"
    rounded: "{rounded.feature}"
    padding: 24px
  card-terminal:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.feature}"
    padding: 16px

  # Inputs
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-tertiary}"
    typography: "{typography.nav}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.text-tertiary}"
    typography: "{typography.nav}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.ink}"

  # Image / video
  video:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.video}"
    padding: 0px

  # Editorial label
  label-editorial:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-tertiary}"
    typography: "{typography.small-label}"
    padding: 4px 0px

  # Link
  link-underlined:
    textColor: "{colors.link}"
    typography: "{typography.body}"
---

# Warp Design System

## Overview

Warp's website feels like sitting at a campfire in a deep forest — warm, dark, and alive with quiet confidence. Unlike the cold, blue-tinted blacks favored by most developer tools, Warp wraps everything in a warm near-black that feels like charred wood or dark earth. The text isn't pure white either — it's Warm Parchment (`{colors.ink}`), a barely-perceptible cream that softens every headline and makes the dark canvas feel inviting rather than austere.

The typography is the secret weapon: Matter, a geometric sans-serif with distinctive character, deployed at Regular weight across virtually all text. The font choice is unusual for a developer tool — Matter has a softness and humanity that signals "this terminal is for everyone, not just greybeards." Combined with tight line-heights and controlled negative letter-spacing on headlines, the effect is refined and approachable simultaneously. Nature photography is woven between terminal screenshots, creating a visual language that says: this tool brings you closer to flow, to calm productivity.

The overall design philosophy is restraint through warmth. Minimal color (almost monochromatic warm grays), minimal ornamentation, and a focus on product showcases set against cinematic dark landscapes. It's a terminal company that markets like a lifestyle brand.

**Key Characteristics:**
- Warm dark background — earthy near-black with warm gray undertones (`{colors.background}`)
- Warm Parchment (`{colors.ink}`) text instead of pure white — subtle cream warmth
- Matter font family (Regular weight) — geometric but approachable
- Nature photography interleaved with product screenshots
- Almost monochromatic warm gray palette — no bold accent colors
- Uppercase labels with wide letter-spacing (2.4px) for categorization — editorial signaling
- Pill-shaped dark buttons (`{colors.primary}`, 50px radius) — restrained, muted CTAs

## Colors

### Primary
- **Warm Parchment** (`{colors.ink}`): Primary text color — a barely-cream off-white that softens every surface.
- **Earth Gray** (`{colors.primary}`): Button backgrounds, dark interactive surfaces — warm, not cold.
- **Deep Void** (`{colors.background}`): The warm dark canvas derived from the body background.

### Secondary & Accent
- **Stone Gray** (`{colors.text-tertiary}`): Secondary text, muted descriptions — warm mid-gray.
- **Ash Gray** (`{colors.on-primary}`): Body text, button text — the workhorse reading color.
- **Purple-Tint Gray** (`{colors.link}`): Link text with subtle purple undertone — underlined links in content.

### Surface & Background
- **Frosted Veil** (`{colors.surface-veil}`): Ultra-subtle white overlay for surface differentiation.
- **Mist Border** (`{colors.border}`): Semi-transparent border approximation for card containment.
- **Dark Charcoal Alt** (`{colors.border-soft}`): Alternate border tone.

### Neutrals & Text
- **Warm Parchment** (`{colors.ink}`): Headlines, high-emphasis text.
- **Ash Gray** (`{colors.on-primary}`): Body paragraphs, descriptions.
- **Stone Gray** (`{colors.text-tertiary}`): Secondary labels, subdued information.
- **Muted Purple** (`{colors.link}`): Underlined links, tertiary content.

### Semantic & Accent
- Warp operates as an almost monochromatic system — no bold accent colors.
- Interactive states are communicated through opacity changes and underline decorations rather than color shifts.
- Any accent color would break the warm, restrained palette.

**No gradients.** Depth is created through layered semi-transparent surfaces and photography rather than color gradients.

## Typography

### Font Family
- **Display & Body**: Matter Regular — geometric sans-serif with soft character.
- **Medium**: Matter Medium (500) — for emphasis.
- **Square**: Matter SQ Regular — squared variant for select display contexts.
- **UI Supplement**: Inter — used for specific UI elements.
- **Monospace Display**: Geist Mono — for code/terminal display headings.
- **Monospace Body**: Matter Mono Regular — custom mono companion.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-hero` | Maximum compression, hero impact (80px) |
| `display-section` | Feature section headings (56px) |
| `section-heading` | Alternate heading weight (48px) |
| `feature-heading` | Feature block titles (40px) |
| `sub-heading-large` | Sub-section headers (36px) |
| `card-display` | Squared variant for special display |
| `sub-heading` | Content sub-headings (32px) |
| `body-heading` | Bold content intros (24px) |
| `card-title` | Emphasized card headers (Matter Medium 22px) |
| `body-large` | Primary body text, relaxed |
| `body` | Standard body paragraphs |
| `nav` | Navigation links, UI text |
| `button-ui` | Button labels (Matter Medium) |
| `caption` | Uppercase labels (transform: uppercase) |
| `small-label` | Uppercase micro-labels |
| `micro` | Smallest text elements |
| `code-ui` | Terminal/code display (Geist Mono) |
| `code-body` | Code content (Matter Mono) |

### Principles
- **Regular weight dominance**: Nearly all text uses weight 400 — even headlines. Matter Medium (500) appears only for emphasis (card titles, buttons).
- **Uppercase as editorial signal**: Small labels and categories use uppercase transform with wide letter-spacing (1.4px–2.4px), creating a magazine-editorial categorization system.
- **Warm legibility**: Matter's geometric softness + warm text colors + controlled negative tracking creates text that reads as effortlessly human on dark surfaces.
- **No bold display**: Zero use of bold (700+) anywhere — restraint is the philosophy.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

Section padding: `4xl`–`5xl` (80px–120px) vertical between major sections. Card padding: `lg`–`2xl` internal. Component gaps: `sm`–`lg` between related elements.

### Grid & Container
- Max width: ~1500px container, centered
- Column patterns: full-width hero, 2-column feature sections with photography, single-column testimonials
- Cinematic layout: wide containers that let photography breathe

### Whitespace Philosophy
- **Vast and warm**: generous spacing between sections — the dark background creates a warm void that feels contemplative rather than empty.
- **Photography as whitespace**: nature images serve as visual breathing room between dense product information.
- **Editorial pacing**: the layout reads like a magazine — each section is a deliberate page-turn moment.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 (Flat) | No shadow, dark background | Page canvas, most surfaces |
| Level 1 (Veil) | `{colors.surface-veil}` overlay | Subtle surface differentiation |
| Level 2 (Border) | `1px solid {colors.border}` | Card containment, section separation |
| Level 3 (Ambient) | inferred soft warm shadow | Image containers, floating elements |

**Shadow Philosophy**: Warp's elevation system is remarkably flat — almost zero shadow usage on the marketing site. Depth is communicated through:
- **Semi-transparent borders** instead of shadows — borders create a ghostly containment
- **Photography layering** — images create natural depth without artificial shadows
- **Surface opacity shifts** — subtle overlays create barely-perceptible layer differences

The effect is calm and grounded — nothing floats, everything rests.

### Decorative Depth
- **Photography as depth**: nature images create atmospheric depth that shadows cannot
- **No glass or blur effects**: the design avoids trendy glassmorphism entirely
- **Warm ambient**: any glow comes from the photography's natural lighting, not artificial CSS

## Shapes

| Token | Value | Use |
|---|---|---|
| `sm` | 4px | Small interactive elements — buttons, tags |
| `md` | 6px | Standard components — links, small containers |
| `lg` | 8px | Images, video containers, standard cards |
| `video` | 10px | Video elements, medium containers |
| `feature` | 12px | Feature cards, large images |
| `large` | 14px | Large containers, prominent cards |
| `rounded` | 40px | Large rounded sections |
| `pill` | 50px | Pill buttons — primary CTAs |
| `progress` | 200px | Progress bars — full pill shape |

## Components

The complete component spec lives in the `components:` token block above. Reference tokens directly.

### Buttons
- **`button-pill`** — Earth Gray pill with Ash Gray text, 50px radius. The primary CTA — warm, muted, understated.
- **`button-frosted-tag`** — frosted overlay tag for small inline labels.
- **`button-ghost`** — text-only with underline decoration on hover.

Hover: subtle opacity or brightness shift — no dramatic color changes.

### Cards & Containers
- **`card-photography`** — full-bleed nature imagery with overlay text, 8–12px radius.
- **`card-terminal`** — product UI embedded in dark containers with rounded corners.
- **`card-bordered`** — semi-transparent border for containment, 12–14px radius.

Hover is minimal — content cards don't dramatically change, maintaining the calm aesthetic.

### Inputs
Dark background inputs with warm gray text. Focus: border brightness increase, no colored rings (consistent with the monochromatic palette).

### Navigation
- Top nav: dark background, warm parchment brand text, Matter Regular at 16px for links
- Link color: Stone Gray for muted nav, Warm Parchment for active/hover
- CTA: dark pill at nav end — restrained, not attention-grabbing
- Mobile: collapses to simplified navigation
- Sticky on scroll

### Image Treatment
- Nature photography (landscapes, forests, golden-hour scenes) — completely unique for a developer tool
- Terminal screenshots: product UI in realistic terminal window frames
- Mixed composition: nature images and terminal screenshots interleaved
- Full-bleed: images often span full container width with 8px radius
- Video elements: 10px border-radius

## Do's and Don'ts

### Do
- Use warm off-white (`{colors.ink}`) for text instead of pure white — the cream undertone is essential
- Keep buttons restrained and muted — dark fill with muted text, no bright CTAs
- Apply Matter Regular (weight 400) for nearly everything, even headlines. Reserve Medium (500) for emphasis only
- Use uppercase labels with wide letter-spacing (1.4px–2.4px) for categorization
- Interleave nature photography with product screenshots — core to the brand
- Maintain the almost monochromatic warm gray palette
- Use semi-transparent borders for card containment instead of shadows
- Keep negative letter-spacing on headlines (-0.4px to -2.4px) for Matter's compressed display

### Don't
- Use pure white (`#ffffff`) for text — it's always warm parchment
- Add bold accent colors (blue, red, green) — the system is deliberately monochromatic
- Apply bold weight (700+) — Warp never goes above Medium (500)
- Use heavy drop shadows
- Create cold or blue-tinted dark backgrounds
- Add decorative gradients or glow effects
- Use tight, compressed layouts — the editorial spacing is generous
- Mix in additional typefaces beyond the Matter family + Inter supplement

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <810px | Single column, stacked sections, hero text reduces to ~48px, hamburger nav |
| Tablet | 810px–1500px | 2-column features begin, photography scales, nav links partially visible |
| Desktop | >1500px | Full cinematic layout, 80px hero display, side-by-side photography + text |

### Touch Targets
- Pill buttons: 50px radius with 10px padding — comfortable touch targets
- Nav links: 16px text with surrounding padding for accessibility
- Mobile CTAs: full-width pills on mobile for easy thumb reach

### Collapsing Strategy
- **Navigation**: full horizontal nav → simplified mobile navigation
- **Hero text**: 80px display → 56px → 48px across breakpoints
- **Feature sections**: side-by-side photography + text → stacked vertically
- **Photography**: scales within containers, maintains cinematic aspect ratios
- **Section spacing**: reduces proportionally — generous desktop → compact mobile

### Image Behavior
- Nature photography scales responsively, maintaining wide cinematic ratios
- Terminal screenshots maintain aspect ratios within responsive containers
- Video elements scale with 10px radius maintained
- No art direction changes — same compositions across breakpoints

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Text: Warm Parchment (`{colors.ink}`)
- Secondary Text: Ash Gray (`{colors.on-primary}`)
- Tertiary Text: Stone Gray (`{colors.text-tertiary}`)
- Button Background: Earth Gray (`{colors.primary}`)
- Border: Mist Border (`{colors.border}`)
- Background: Deep warm near-black (`{colors.background}`)

### Example Component Prompts
- "Create a hero section on warm dark background with 80px Matter Regular heading in warm parchment (`{colors.ink}`), line-height 1.0, letter-spacing -2.4px, and a dark pill button (`{colors.primary}`, 50px radius, `{colors.on-primary}` text)"
- "Design a feature card with semi-transparent border (`{colors.border}`), 12px radius, warm dark background, Matter Regular heading at 24px, and ash gray (`{colors.on-primary}`) body text at 18px"
- "Build a category label using Matter Regular at 12px, uppercase transform, letter-spacing 2.4px, stone gray (`{colors.text-tertiary}`) color — editorial magazine style"
- "Create a testimonial section with warm parchment quotes in Matter Regular 24px, attributed in stone gray (`{colors.text-tertiary}`), on dark background with minimal ornamentation"
- "Design a navigation bar with warm dark background, Matter Regular links at 16px in stone gray (`{colors.text-tertiary}`), hover to warm parchment (`{colors.ink}`), and a dark pill CTA button (`{colors.primary}`) at the right"

### Iteration Guide
1. Verify text color is warm parchment (`{colors.ink}`) not pure white — the warmth is subtle but essential
2. Ensure all buttons use the restrained dark palette (`{colors.primary}`) — no bright or colorful CTAs
3. Check that Matter Regular (400) is the default weight — Medium (500) only for emphasis
4. Confirm uppercase labels have wide letter-spacing (1.4px–2.4px)
5. The overall tone should feel warm and calm, like a well-designed magazine — not aggressive or tech-flashy
