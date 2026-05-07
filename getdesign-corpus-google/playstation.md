---
version: alpha
name: PlayStation
description: Three-surface channel layout (black hero, white content, blue footer) with SST weight 300 luxury display headlines and a signature scale-1.2 cyan hover treatment.

colors:
  # Canvas — three surfaces
  background: "#ffffff"
  background-dark: "#000000"  # masthead, hero
  surface: "#ffffff"
  surface-ice: "#f5f7fa"
  surface-shadow: "#121314"  # dark gradient anchor
  divider-tint: "#f3f3f3"

  # Ink
  ink: "#000000"
  ink-deep: "#1f1f1f"
  ink-inverted: "#ffffff"
  text-secondary: "#6b6b6b"
  text-muted: "#cccccc"
  text-placeholder: "#666666"  # was rgba(0,0,0,0.6) — flattened

  # Brand
  primary: "#0070cc"  # PlayStation Blue
  primary-hover: "#1eaedb"  # PlayStation Cyan — hover/focus only
  primary-secondary: "#0172ce"
  on-primary: "#ffffff"

  # Links
  link: "#0068bd"  # dark link blue (light surfaces)
  link-hover: "#1883fd"
  link-on-dark: "#53b1ff"

  # Commerce
  commerce-orange: "#d53b00"
  commerce-orange-active: "#aa2f00"

  # Status
  warning-red: "#c81b3a"

  # Borders
  border: "#dedede"
  border-input: "#cccccc"

  # Filter mist (sticky filter bars)
  filter-mist: "#f7f9fc"  # was rgba(245,247,250,0.3) — flattened

  # Shadow tints (flattened approximations)
  shadow-feather: "#f0f0f0"  # was rgba(0,0,0,0.06)
  shadow-soft: "#ebebeb"  # was rgba(0,0,0,0.08)
  shadow-medium: "#d6d6d6"  # was rgba(0,0,0,0.16)
  shadow-hero: "#333333"  # was rgba(0,0,0,0.8)

  # Gradient stops
  gradient-light-top: "#ffffff"
  gradient-light-bottom: "#f5f7fa"

typography:
  hero-display-xl:
    fontFamily: "SST, Playstation SST, Arial, Helvetica, sans-serif"
    fontSize: 54px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.1px
  hero-display-large:
    fontFamily: "SST, Playstation SST, Arial, Helvetica, sans-serif"
    fontSize: 44px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.1px
  large-display:
    fontFamily: "SST, Playstation SST, Arial, Helvetica, sans-serif"
    fontSize: 35px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0px
  mid-display:
    fontFamily: "SST, Playstation SST, Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.1px
  compact-display:
    fontFamily: "SST, Playstation SST, Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.1px
  ui-heading-small:
    fontFamily: "SST, Playstation SST, Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  button:
    fontFamily: "SST, Playstation SST, Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.4px
  button-emphasized:
    fontFamily: "SST, Playstation SST, Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.45px
  body-relaxed:
    fontFamily: "SST, Playstation SST, Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  compact-button:
    fontFamily: "SST, Playstation SST, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.324px
  utility-caption:
    fontFamily: "SST, Playstation SST, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  caption-body:
    fontFamily: "SST, Playstation SST, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  micro-caption:
    fontFamily: "SST, Playstation SST, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px

spacing:
  micro: 1px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px
  5xl: 96px

rounded:
  none: 0px
  sm: 2px
  micro: 3px
  md: 6px
  lg: 12px
  xl: 19px
  2xl: 20px
  3xl: 24px
  4xl: 36px
  5xl: 48px
  pill: 9999px

components:
  # Primary blue pill CTA
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"

  # Secondary white outline
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-secondary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 16px 20px

  # Commerce orange (PS Store)
  button-commerce:
    backgroundColor: "{colors.commerce-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-emphasized}"
    rounded: "{rounded.pill}"
    padding: 12px 28px
  button-commerce-active:
    backgroundColor: "{colors.commerce-orange-active}"
    textColor: "{colors.on-primary}"

  # Transparent ghost
  button-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-deep}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 0px 10px

  # Mini in-card CTA
  button-mini:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.compact-button}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  # Game cover tile
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 20px
  card-feature:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.3xl}"
    padding: 32px

  # Hero card on photography
  card-hero:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.ink-inverted}"
    rounded: "{rounded.3xl}"
    padding: 48px

  # Text input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-deep}"
    typography: "{typography.body-relaxed}"
    rounded: "{rounded.micro}"
    padding: 8px 12px

  # Game store pill (platform tag)
  badge-platform:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.utility-caption}"
    rounded: "{rounded.pill}"
    padding: 14px 18px

  # Top nav (always black)
  nav-bar:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.utility-caption}"
    padding: 16px 32px

  # Footer (cobalt blue)
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.body-relaxed}"
    padding: 48px
---

# PlayStation Design System

## Overview

PlayStation.com carries itself like the marketing wing of a premium consumer-electronics brand that happens to sell entertainment. The page is organized as a **vertical channel of alternating surfaces**: a near-black masthead and hero, a sequence of paper-white editorial panels in the middle, and a deep cobalt-blue footer that anchors the entire experience. Between those surface modes the site leans hard on photography and 3D product renders — the PS5 console, game cover art, DualSense controllers — letting the hardware do the emotional work while the chrome stays restrained.

The signature typographic move is **SST Light (weight 300) at large sizes**. Sony's custom SST family is used from 22px up to 54px in weight 300, giving display headlines a whispered, elegant quality that feels closer to a luxury watch ad than a game store. That "quiet authority" is the exact opposite of The Verge's Manuka shout or Wired's newsstand density — PlayStation wants the type to recede and the product to lead. Body and UI lean on weights 500-700, but the *display* voice is consistently thin and calm.

The one place restraint breaks is **interaction**. Every primary button has the same hover move: fill swaps to an electric cyan (`{colors.primary-hover}`), a 2px white border appears, a 2px PlayStation-blue outer ring blooms behind it, and the entire button **scales up 1.2×**. That combination of color pop, border, ring, and lift-scale is a signature move unique to Sony among major brands — a miniature "power-on" animation that the site repeats hundreds of times across a single page.

**Key Characteristics:**
- Three-surface channel layout: near-black hero, paper-white content, cobalt-blue footer — alternating, never blending
- SST weight 300 at 22-54px for display — "quiet authority" headlines that let product photography lead
- PlayStation Blue (`{colors.primary}`) as the brand anchor; cyan (`{colors.primary-hover}`) reserved exclusively for hover/focus states
- Every interactive element scales 1.2× on hover — a signature "power-on" lift unique to PlayStation
- Pill buttons at full pill radius; card art in rounded 12-24px rectangles
- Commerce-orange (`{colors.commerce-orange}`) used exclusively for PlayStation Store / buy-state CTAs
- Wide breakpoint coverage up to 2120px — the site scales all the way to 4K-TV browsing contexts

## Colors

### Primary (Brand Anchor)
- **PlayStation Blue** (`{colors.primary}`): The brand's anchor color. Used on the primary footer, inline links, primary button fills on dark surfaces, and every "official" marker.
- **Console Black** (`{colors.background-dark}`): Pure black for the masthead, hero backdrops, and product presentation zones.

### Secondary & Accent
- **PlayStation Cyan** (`{colors.primary-hover}`): The interaction color. Applied ONLY to hover, focus, and active states of buttons and links. Never appears as a default background or a text color at rest.
- **Link Hover Blue** (`{colors.link-hover}`): The brighter variant used on inline text-link hovers.
- **Dark Link Blue** (`{colors.link}`): The link color at rest on light surfaces.

### Surface & Background
- **Paper White** (`{colors.surface}`): Primary content canvas for editorial panels between the masthead and footer.
- **Ice Mist** (`{colors.surface-ice}`): The atmospheric end-stop of the light section-gradient.
- **Divider Tint** (`{colors.divider-tint}`): The quiet horizontal-rule color between content rows.
- **Shadow Black** (`{colors.surface-shadow}`): The starting anchor of the dark section-gradient.
- **Filter Mist** (`{colors.filter-mist}`): Translucent background flattened, used behind sticky filter bars.

### Neutrals & Text
- **Display Ink** (`{colors.ink}`): Primary display headlines on white surfaces.
- **Deep Charcoal** (`{colors.ink-deep}`): Body headlines and link color at rest — slightly softer than pure black.
- **Body Gray** (`{colors.text-secondary}`): Secondary body text and metadata.
- **Mute Gray** (`{colors.text-muted}`): Tertiary labels, disabled states.
- **Placeholder Ink** (`{colors.text-placeholder}`): Form placeholder text — flattened approx of 60% black.
- **Inverse White** (`{colors.ink-inverted}`): Primary text on dark and blue surfaces.
- **Dark-Link Blue** (`{colors.link-on-dark}`): The link color at rest on dark/black surfaces.

### Semantic & Commerce
- **Commerce Orange** (`{colors.commerce-orange}`): Reserved for PlayStation Store buy-state CTAs, price callouts, and "on sale" badges.
- **Commerce Orange Active** (`{colors.commerce-orange-active}`): The pressed/active state of commerce buttons.
- **Warning Red** (`{colors.warning-red}`): Form errors and destructive-action warnings.
- **Shadow Feather/Soft/Medium/Hero** — flattened approximations of the four-tier shadow system at 0.06 / 0.08 / 0.16 / 0.8 opacity.

### Gradient System
PlayStation uses **two section gradients** and nothing else:
- **Light Section Gradient**: from `{colors.gradient-light-top}` → `{colors.gradient-light-bottom}` — an almost-imperceptible wash.
- **Dark Section Gradient**: from `{colors.surface-shadow}` → `{colors.background-dark}` — a short vertical wash that gives hero panels a subtle vignette.

Both gradients are used **only as section backgrounds**, never inside components. There are no gradient buttons, no gradient text, no glowing halos.

## Typography

### Font Family
- **SST** / **Playstation SST** (Sony, proprietary) — fallback: `Arial, Helvetica`. Sony's custom global typeface, designed by Toshi Omagari and Akira Kobayashi.
- The weight **300 at 22-54px** is PlayStation's typographic signature.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `hero-display-xl` | The biggest SST moment on the page — quiet-weight luxury headline |
| `hero-display-large` | Secondary hero headlines |
| `large-display` | Feature panel headlines |
| `mid-display` | Section headings |
| `compact-display` | Module titles — still in light weight 300 |
| `ui-heading-small` | Tight UI headings |
| `button` | Primary button label |
| `button-emphasized` | Higher-emphasis CTAs (buy, subscribe) |
| `body-relaxed` | Standard reading body |
| `compact-button` | Mini CTAs in cards |
| `utility-caption` | Captions, tag labels |
| `caption-body` | Standard metadata |
| `micro-caption` | Footer microcopy, legal text |

### Principles
- **Weight 300 at large sizes is the voice.** PlayStation is the only major console brand that uses a light-weight display for its hero headlines. Resist the urge to "upgrade" display type to 500 or 700.
- **Weight jumps at the UI layer.** Below 18px the system shifts to 500-700 for legibility.
- **Letter-spacing is barely-there.** Most values are 0.1-0.45px, either positive or slightly negative.
- **No all-caps.** Kickers and tags stay in title case or sentence case.
- **No serif anywhere.** The entire system is sans.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px with section padding at `3xl`-`5xl` (48-96px) vertical between major panels.

### Grid & Container
- Max width: ~1920px (breakpoints tuned up to 2120px). Container caps typically around 1280-1920px.
- 12-column responsive grid that resolves into 3/4/6-column game tile rows.
- Outer padding: 16px mobile → 48px tablet → 64-96px desktop.
- Gutters: 16-24px between columns, tighter (8-12px) inside tile clusters.

### Whitespace Philosophy
PlayStation treats whitespace like a luxury brand treats store lighting — as a premium signal. There is noticeably more vertical breathing room between modules than on any other major retail site. The white editorial panels often hold only one headline + one image + one CTA at hero-scale padding. The effect is a "gallery pace" where each product gets its own room.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | No shadow | Default content on `{colors.surface}` |
| 1 | `0 5px 9px {colors.shadow-feather}` | Feather-light editorial panel lift |
| 2 | `0 5px 9px {colors.shadow-soft}` | Standard grid tile elevation |
| 3 | `0 5px 9px {colors.shadow-medium}` | Emphasized card (hover or active) |
| 4 | `0 5px 9px {colors.shadow-hero}` | Hero overlay shadow — dramatic drop used over photography |
| 5 | `0 0 0 2px {colors.primary}` (focus ring) | Primary button focus state |
| 6 | `0 0 0 2px {colors.background-dark}` (hover ring) | Secondary button hover ring |

PlayStation's depth philosophy is **layered but restrained**. The shadow scale runs from 0.06 to 0.16 for normal states, then jumps to 0.8 for hero drops — there is no 0.2, 0.3, 0.4 middle ground. Most of the page sits almost flat, but when a hero card needs to float over photography, it genuinely floats. Elevation is either whispered or shouted, never muttered.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Edge-to-edge sections |
| `sm` | 2px | Cookie banner buttons, small admin UI |
| `micro` | 3px | Form inputs, tab panels (functional UI cue) |
| `md` | 6px | Compact buttons and inline images |
| `lg` | 12px | Standard game cover images and content images |
| `xl` | 19px | Feature cards |
| `2xl` | 20px | Inline tag spans |
| `3xl` | 24px | Hero cards, primary feature frames |
| `4xl` | 36px | Full-pill nav and secondary button variants |
| `5xl` | 48px | Large feature buttons |
| `pill` | 9999px | Full pill primary buttons and circular icon buttons |

PlayStation deliberately uses different radii for different *hierarchies*: 3px for utility, 12px for media, 24px for features, pill for CTAs.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly.

### Buttons
- **`button-primary`** — PlayStation Blue full pill, white SST 18px/500. The signature hover: cyan fill + 2px white border + 2px blue outer ring + scale(1.2).
- **`button-secondary`** — White outline pill on dark, cyan-fill hover (same signature).
- **`button-commerce`** — Commerce Orange pill for PS Store / Buy CTAs. Active darkens to `{colors.commerce-orange-active}`.
- **`button-ghost`** — Transparent with light gray border for nav-style actions.
- **`button-mini`** — In-card 14px CTA at 0.324px tracking.

### Cards
- **`card`** — Standard 12px-radius white card with feather shadow.
- **`card-feature`** — Larger 24px-radius feature card.
- **`card-hero`** — Black-anchored hero card on photography with dramatic 0.8-opacity shadow.

### Inputs
- **`input`** — White surface, `{colors.border-input}` border, 3px radius (the tightest in the system). Focus brings 2px primary-color ring.

### Game Store Pill
- **`badge-platform`** — Full pill platform tag (PS5/PS4/PSVR2) for game tiles.

### Navigation & Footer
- **`nav-bar`** — Always black. Stays pinned. Does not invert over light panels.
- **`footer`** — Cobalt PlayStation Blue, anchors the page.

## Do's and Don'ts

### Do
- Use PlayStation Blue (`{colors.primary}`) as the primary CTA fill and the footer anchor
- Use SST weight 300 for every display headline 22px and above
- Apply the full hover signature to every primary button: cyan fill + 2px white border + 2px blue outer ring + scale(1.2)
- Use full-pill radius (`{rounded.pill}`) on primary and commerce buttons
- Reserve PlayStation Cyan (`{colors.primary-hover}`) exclusively for hover, focus, and active states — never as a resting background
- Use Commerce Orange (`{colors.commerce-orange}`) only on PlayStation Store / purchase CTAs and price callouts
- Alternate dark hero panels with white content panels and anchor with a deep blue footer
- Use dramatic `{colors.shadow-hero}` hero drop shadows when a card overlaps product photography
- Keep the top nav black on every scroll position — it does not invert to white over light panels

### Don't
- Don't bold display headlines. Weight 300 at 22-54px is the PlayStation voice.
- Don't use ALL-CAPS labels or kickers. PlayStation rarely uses uppercase.
- Don't use gradient buttons, text, or backgrounds outside the two declared section gradients.
- Don't introduce warm colors outside Commerce Orange.
- Don't use square corners on buttons or media — pick from the eleven radii but never `0`.
- Don't skip the `scale(1.2)` hover move on primary buttons.
- Don't use serif type. The system is 100% SST sans.
- Don't let cyan appear as a text or background color at rest. It only exists in motion.
- Don't design panels that fight for attention. Whitespace gives each module its own "gallery room".

---

## Responsive Behavior

*(Preserved from original 9-section format — Google's parser keeps unknown sections.)*

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Small Mobile | <400px | Single column, nav collapses to hamburger, SST hero scales to ~28px |
| Mobile | 400-599px | Single column, tiles stack full-width, padding opens to 16px |
| Large Mobile | 600-767px | Still single column but 2-column tile option in select modules |
| Tablet Portrait | 768-1023px | 2-column game grid, nav still condensed |
| Tablet Landscape | 1024-1279px | 3-4 column grid, full nav restored |
| Desktop | 1280-1599px | Full editorial grid, max hero display scale (44-54px) |
| Large Desktop | 1600-1919px | Container caps at 1600px, margins expand |
| 4K / Big-Screen | ≥1920px | Container expands to 1920px max, hero content scales up |
| Ultra-Wide | ≥2120px | Extreme breakpoint — page stays anchored, outer margins absorb extra width |

PlayStation tunes specifically for **big-screen contexts** (1920-2120px) because PS5 owners frequently browse the site on TVs.

### Touch Targets
- Primary pill buttons are ~48-56px tall (SST 18px text + ~12-16px vertical padding) — comfortably WCAG AAA.
- Nav links are smaller (~32-40px tall) at desktop; on mobile they pad out to 48px+ inside the drawer.
- Icon circle buttons are 40-48px — touch-friendly.

### Collapsing Strategy
- **Nav**: full nav → condensed → hamburger drawer.
- **Grid**: 6-col → 4-col → 3-col → 2-col → 1-col.
- **Spacing**: section padding tightens from 96px → 64px → 48px → 32px → 24px.
- **Type**: SST hero scales from 54px → 44px → 35px → 28px → 22px. The light weight 300 is preserved at every size.
- **Hero photography**: art-direction swap — desktop uses wide 16:9 crops, mobile uses 4:3 or 1:1 crops.

### Image Behavior
- Responsive raster (`srcset` + `<picture>` with art-direction).
- 4K-ready: the site serves high-density imagery at 1920px+ to avoid upscaling on TV browsing.
- `loading="lazy"` on everything below the fold; hero is `eager` with a preload hint.

---

## Agent Prompt Guide

*(Preserved from original 9-section format — the copy-paste payload section.)*

### Quick Color Reference
- **Primary CTA**: PlayStation Blue (`{colors.primary}`)
- **Hover / Focus Accent**: PlayStation Cyan (`{colors.primary-hover}`)
- **Background (White Surface)**: Paper White (`{colors.surface}`)
- **Background (Dark Surface)**: Console Black (`{colors.background-dark}`)
- **Heading Text on White**: Display Ink (`{colors.ink}`)
- **Body Text on White**: Deep Charcoal (`{colors.ink-deep}`)
- **Body Text on Black**: Inverse White (`{colors.ink-inverted}`)
- **Commerce / Buy Accent**: Commerce Orange (`{colors.commerce-orange}`)
- **Footer Anchor**: PlayStation Blue (`{colors.primary}`)

### Example Component Prompts
1. "Create a primary CTA button with a `{colors.primary}` PlayStation Blue fill, white text in SST 18px / 500 / 0.4px tracking, full pill border radius, 12px × 24px padding. On hover, the background transitions to `{colors.primary-hover}` PlayStation Cyan, a 2px white border appears, a 2px `{colors.primary}` outer ring blooms via box-shadow, and the entire button scales 1.2× — all in a 180ms ease transition."
2. "Design a hero panel on a `{colors.background-dark}` Console Black canvas with a 54px SST weight 300 headline in `{colors.ink-inverted}` with -0.1px letter-spacing and 1.25 line-height. Place a single primary CTA below with the standard PlayStation hover treatment. No ALL-CAPS labels anywhere."
3. "Build a game cover tile: 3:4 aspect ratio image with 12px border radius, feather-weight `0 5px 9px {colors.shadow-soft}` drop shadow, a 14px SST 700 title below, a 12px SST 500 platform tag, and a mini 14px / 700 / 0.324px tracking primary CTA in PlayStation Blue."
4. "Create a commerce pill button for a PlayStation Store purchase: `{colors.commerce-orange}` Commerce Orange fill, `{colors.ink-inverted}` text in SST 18px / 700 / 0.45px tracking, full pill radius, 12px × 28px padding. Active state darkens to `{colors.commerce-orange-active}`. Hover follows the standard cyan-invert with 1.2× scale."
5. "Design a white content panel between dark hero sections: `{colors.surface}` background with the subtle `{colors.gradient-light-top}` → `{colors.gradient-light-bottom}` gradient, 24px border radius, 48px interior padding, feather-weight `0 5px 9px {colors.shadow-feather}` elevation, a 35px SST 300 headline, a 18px body paragraph, and a single primary CTA."

### Iteration Guide
1. **Audit display weight.** Every headline 22px and above should be SST weight 300.
2. **Audit the hover treatment.** Every primary button must scale 1.2× on hover with the cyan-fill + white-border + blue-ring combination.
3. **Audit corners.** Every container and button should land on 2, 3, 6, 12, 19, 20, 24, 36, 48, or pill.
4. **Audit color sprawl.** Only PlayStation Blue, Cyan, Commerce Orange, and the declared grays/blacks/whites should appear in chrome.
5. **Audit surface alternation.** The page should alternate dark hero → white content → dark hero → white content → blue footer.
6. **Audit casing.** Sentence case and title case only. No ALL-CAPS labels, buttons, or kickers.
7. **Audit shadow weight.** Shadow opacity should land on 0.06 / 0.08 / 0.16 / 0.8 — nothing in between.
8. **Audit whitespace.** If two modules feel "competitive", add 48-96px of vertical breathing room.
