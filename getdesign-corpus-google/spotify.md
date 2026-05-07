---
version: alpha
name: Spotify
description: Content-first dark music interface — near-black canvas, SpotifyMixUI bold/regular binary, pill-and-circle geometry, heavy shadows, and tightly scoped Spotify Green accent reserved for functional moments.

colors:
  # Canvas hierarchy
  background: "#121212"
  surface: "#181818"
  surface-elevated: "#1f1f1f"
  surface-card: "#252525"
  surface-card-alt: "#272727"
  surface-light: "#eeeeee"
  surface-pure-black: "#000000"

  # Brand accent — Spotify Green (functional only)
  primary: "#1ed760"
  on-primary: "#000000"
  primary-border: "#1db954"

  # Ink
  ink: "#ffffff"
  ink-muted: "#b3b3b3"
  ink-near-white: "#cbcbcb"
  ink-light: "#fdfdfd"
  ink-on-light: "#181818"

  # Semantic
  error: "#f3727f"
  warning: "#ffa42b"
  info: "#539df5"

  # Borders
  border: "#4d4d4d"
  border-light: "#7c7c7c"
  separator: "#b3b3b3"

  # Shadow tints (opaque approximations of original rgba)
  shadow-heavy: "#000000"  # was rgba(0,0,0,0.5) — Google format requires hex
  shadow-medium: "#0a0a0a"  # was rgba(0,0,0,0.3) — Google format requires hex
  shadow-inset: "#7c7c7c"  # was rgb(124,124,124) inset border — Google format requires hex

typography:
  section-title:
    fontFamily: "SpotifyMixUITitle, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0px
  feature-heading:
    fontFamily: "SpotifyMixUI, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0px
  body-bold:
    fontFamily: "SpotifyMixUI, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0px
  body:
    fontFamily: "SpotifyMixUI, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-uppercase:
    fontFamily: "SpotifyMixUI, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 1.4px
  button:
    fontFamily: "SpotifyMixUI, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.14px
  nav-link-bold:
    fontFamily: "SpotifyMixUI, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0px
  nav-link:
    fontFamily: "SpotifyMixUI, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px
  caption-bold:
    fontFamily: "SpotifyMixUI, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  caption:
    fontFamily: "SpotifyMixUI, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  small-bold:
    fontFamily: "SpotifyMixUI, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  small:
    fontFamily: "SpotifyMixUI, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  badge:
    fontFamily: "SpotifyMixUI, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0px
  micro:
    fontFamily: "SpotifyMixUI, Helvetica Neue, helvetica, arial, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px

spacing:
  hairline: 1px
  micro: 2px
  xxs: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 20px
  pill-large: 100px
  pill-small: 500px
  pill: 9999px
  circle: 50px

components:
  # Dark pill — primary nav/secondary actions
  button-primary:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.button-uppercase}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  # Large dark pill — primary app nav
  button-large:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-uppercase}"
    rounded: "{rounded.pill-small}"
    padding: 12px 43px

  # Light pill — light-mode CTAs
  button-light:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink-on-light}"
    typography: "{typography.button-uppercase}"
    rounded: "{rounded.pill-small}"
    padding: 12px 24px

  # Outlined pill
  button-outlined:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 16px

  # Circular play
  button-play:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.circle}"
    padding: 12px

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 16px
  card-alt:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 16px

  # Search input
  input:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill-small}"
    padding: 12px 48px
  input-focus:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"

  # Navigation sidebar
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link-bold}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink-muted}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link-bold}"

  # Badges
  badge-green:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-explicit:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
---

# Spotify Design System

## Overview

Spotify's web interface is a dark, immersive music player that wraps listeners in a near-black cocoon (`{colors.surface-pure-black}`, `{colors.background}`, `{colors.surface}`, `{colors.surface-elevated}`) where album art and content become the primary source of color. The design philosophy is "content-first darkness" — the canvas is charcoal to black, and Spotify Green (`{colors.primary}`) enters only when something is functionally active: a play button, a primary CTA, an active nav item. Green is the accent, never the background. Using green as a dominant fill (full-bleed hero washes, large gradients) is off-brand; the brand discipline is that green lights up only where interaction happens.

The typography uses SpotifyMixUI and SpotifyMixUITitle — proprietary fonts from the CircularSp family (Circular by Lineto, customized for Spotify) with an extensive fallback stack that includes Arabic, Hebrew, Cyrillic, Greek, Devanagari, and CJK fonts, reflecting Spotify's global reach. The type system is compact and functional: 700 (bold) for emphasis and navigation, 600 (semibold) for secondary emphasis, and 400 (regular) for body. Buttons use uppercase with positive letter-spacing (`1.4px`–`2px`) for a systematic, label-like quality.

What distinguishes Spotify is its pill-and-circle geometry. Primary buttons use 500px–9999px radius (full pill), circular play buttons use 50% radius, and search inputs are 500px pills. Combined with heavy shadows on elevated elements and a unique inset border-shadow combo, the result is an interface that feels like a premium audio device — tactile, rounded, and built for touch.

**Key Characteristics:**
- Near-black immersive canvas (`{colors.background}`–`{colors.surface-elevated}`) as the dominant surface — the UI disappears behind content
- Spotify Green (`{colors.primary}`) as a tightly scoped accent — play controls, primary CTAs, active states, small badges
- Green rule of thumb: if the green fill covers more than ~5% of a screen, it's too much
- SpotifyMixUI/CircularSp font family with global script support
- Pill buttons (`{rounded.pill-small}`–`{rounded.pill}`) and circular controls (`{rounded.circle}`) — rounded, touch-optimized
- Uppercase button labels with wide letter-spacing (`1.4px`–`2px`)
- Heavy shadows on elevated elements
- Semantic colors: negative red (`{colors.error}`), warning orange (`{colors.warning}`), announcement blue (`{colors.info}`)
- Album art — not UI chrome — provides any additional color on the canvas

## Colors

### Primary Brand
- **Spotify Green** (`{colors.primary}`): Primary brand accent — play buttons, active states, CTAs.
- **Near Black** (`{colors.background}`): Deepest background surface.
- **Dark Surface** (`{colors.surface}`): Cards, containers, elevated surfaces.
- **Mid Dark** (`{colors.surface-elevated}`): Button backgrounds, interactive surfaces.

### Text
- **White** (`{colors.ink}`): `--text-base`, primary text.
- **Silver** (`{colors.ink-muted}`): Secondary text, muted labels, inactive nav.
- **Near White** (`{colors.ink-near-white}`): Slightly brighter secondary text.
- **Light** (`{colors.ink-light}`): Near-pure white for maximum emphasis.

### Semantic
- **Negative Red** (`{colors.error}`): Error states.
- **Warning Orange** (`{colors.warning}`): Warning states.
- **Announcement Blue** (`{colors.info}`): Info states.

### Surface & Border
- **Dark Card** (`{colors.surface-card}`): Elevated card surface.
- **Mid Card** (`{colors.surface-card-alt}`): Alternate card surface.
- **Border Gray** (`{colors.border}`): Button borders on dark.
- **Light Border** (`{colors.border-light}`): Outlined button borders, muted links.
- **Separator** (`{colors.separator}`): Divider lines.
- **Light Surface** (`{colors.surface-light}`): Light-mode buttons (rare).
- **Spotify Green Border** (`{colors.primary-border}`): Green accent border variant.

### Shadows
- **Heavy** (`{colors.shadow-heavy}`): Dialogs, menus, elevated panels.
- **Medium** (`{colors.shadow-medium}`): Cards, dropdowns.
- **Inset Border** (`{colors.shadow-inset}`): Input border-shadow combo tint.

## Typography

### Font Families
- **Title**: `SpotifyMixUITitle`, fallback `CircularSp-Arab, CircularSp-Hebr, CircularSp-Cyrl, CircularSp-Grek, CircularSp-Deva, Helvetica Neue, helvetica, arial, Hiragino Sans, Meiryo, MS Gothic`
- **UI / Body**: `SpotifyMixUI`, same fallback stack

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.section-title}`, `{typography.body}`).

| Token | Use |
|---|---|
| `section-title` | Bold title weight (24px) |
| `feature-heading` | Semibold section heads (18px) |
| `body-bold` | Emphasized text (16px) |
| `body` | Standard body (16px) |
| `button-uppercase` | Uppercase button label, wide tracking |
| `button` | Standard button text |
| `nav-link-bold`, `nav-link` | Active vs inactive navigation |
| `caption-bold`, `caption` | Bold and regular metadata |
| `small-bold`, `small` | Tags, counts, fine print |
| `badge` | Small capitalized badges |
| `micro` | Smallest text (10px) |

### Principles
- **Bold/regular binary**: Most text is either 700 (bold) or 400 (regular), with 600 used sparingly. Hierarchy comes from weight contrast more than size variation.
- **Uppercase buttons as system**: Button labels use uppercase + wide letter-spacing (`1.4px`–`2px`), creating a systematic "label" voice distinct from content text.
- **Compact sizing**: 10px–24px range — narrower than most systems. Spotify's type is designed for scanning playlists, not reading articles.
- **Global script support**: The extensive fallback stack reflects Spotify's 180+ market reach.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

The scale stays compact — Spotify is an app, not a marketing site, and densities are tighter than typical web spacing systems.

### Grid & Container
- Sidebar (fixed) + main content area
- Grid-based album/playlist cards
- Full-width now-playing bar at bottom
- Responsive content area fills remaining space

### Whitespace Philosophy
- **Dark compression**: Spotify packs content densely — playlist grids, track lists, and navigation are tightly spaced. The dark background provides visual rest between elements without needing large gaps.
- **Content density over breathing room**: Every pixel serves the listening experience.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Base (Level 0) | `{colors.background}` background | Deepest layer, page background |
| Surface (Level 1) | `{colors.surface}` or `{colors.surface-elevated}` | Cards, sidebar, containers |
| Elevated (Level 2) | Drop shadow tinted `{colors.shadow-medium}` | Dropdown menus, hover cards |
| Dialog (Level 3) | Heavy drop shadow tinted `{colors.shadow-heavy}` | Modals, overlays, menus |
| Inset (Border) | Inset ring tinted `{colors.shadow-inset}` | Input borders |

**Shadow Philosophy**: Spotify uses notably heavy shadows for a dark-themed app. The 24px-blur shadow creates a dramatic "floating in darkness" effect for dialogs and menus, while the 8px blur provides a more subtle card lift. The inset border-shadow combination on inputs creates a recessed, tactile quality.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Rare — full-bleed surfaces |
| `xs` | 2px | Badges, explicit tags |
| `sm` | 4px | Inputs, small elements |
| `md` | 6px | Album art containers, cards |
| `lg` | 8px | Sections, dialogs |
| `xl` | 20px | Panels, overlay elements |
| `pill-large` | 100px | Large pill buttons |
| `pill-small` | 500px | Primary buttons, search input |
| `pill` | 9999px | Navigation pills, search |
| `circle` | 50px | Play buttons, avatars, icons |

## Components

The complete component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.button-play}`).

### Buttons
- **`button-primary`** — Dark pill (`{colors.surface-elevated}`) for navigation pills and secondary actions.
- **`button-large`** — Large dark pill for primary app navigation buttons.
- **`button-light`** — Light-mode pill for cookie consent and marketing surfaces.
- **`button-outlined`** — Transparent pill with `1px solid {colors.border-light}` border. Asymmetric padding accommodates icons.
- **`button-play`** — Circular Spotify Green play/pause control with black icon.

### Cards & Containers
- **`card`** — Dark `{colors.surface}` card with `{rounded.lg}` corners, no visible border. Hover slightly lightens the background.
- **`card-alt`** — Alternative `{colors.surface-elevated}` variant for layered grids.

### Inputs
- **`input`** — Search input on `{colors.surface-elevated}`, white text, `{rounded.pill-small}` (500px) corners. The signature inset-border-shadow combo creates the recessed feel.

### Navigation
Dark sidebar with SpotifyMixUI 14px weight 700 for active items, 400 for inactive. `{colors.ink-muted}` color for inactive items, `{colors.ink}` for active. Circular icon buttons. Spotify wordmark top-left.

### Badges
- **`badge-green`** — Spotify Green tag for highlighted status.
- **`badge-explicit`** — Muted dark tag for "EXPLICIT" and similar metadata markers.

## Do's and Don'ts

### Do
- Use near-black backgrounds (`{colors.background}`–`{colors.surface-elevated}`) — depth through shade variation
- Apply Spotify Green (`{colors.primary}`) only for play controls, active states, and primary CTAs
- Use pill shape (`{rounded.pill-small}`–`{rounded.pill}`) for all buttons — circular (`{rounded.circle}`) for play controls
- Apply uppercase + wide letter-spacing (`1.4px`–`2px`) on button labels
- Keep typography compact (10px–24px range) — this is an app, not a magazine
- Use heavy shadows (tinted `{colors.shadow-medium}`–`{colors.shadow-heavy}`) for elevated elements on dark backgrounds
- Let album art provide color — the UI itself is achromatic

### Don't
- Don't use Spotify Green decoratively or on backgrounds — it's functional only
- Don't use light backgrounds for primary surfaces — the dark immersion is core
- Don't skip the pill/circle geometry on buttons — square buttons break the identity
- Don't use thin/subtle shadows — on dark backgrounds, shadows need to be heavy to be visible
- Don't add additional brand colors — green + achromatic grays is the complete palette
- Don't use relaxed line-heights — Spotify's typography is compact and dense
- Don't expose raw gray borders — use shadow-based or inset borders instead

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <425px | Compact mobile layout |
| Mobile | 425–576px | Standard mobile |
| Tablet | 576–768px | 2-column grid |
| Tablet Large | 768–896px | Expanded layout |
| Desktop Small | 896–1024px | Sidebar visible |
| Desktop | 1024–1280px | Full desktop layout |
| Large Desktop | >1280px | Expanded grid |

### Collapsing Strategy
- Sidebar: full → collapsed → hidden
- Album grid: 5 columns → 3 → 2 → 1
- Now-playing bar: maintained at all sizes
- Search: pill input maintained, width adjusts
- Navigation: sidebar → bottom bar on mobile

---

## Agent Prompt Guide

### Quick Color Reference
- Background: Near Black (`{colors.background}`)
- Surface: Dark Card (`{colors.surface}`)
- Text: White (`{colors.ink}`)
- Secondary text: Silver (`{colors.ink-muted}`)
- Accent: Spotify Green (`{colors.primary}`)
- Border: `{colors.border}`
- Error: Negative Red (`{colors.error}`)

### Example Component Prompts
- "Create a dark card: `{colors.surface}` background, 8px radius. Title at 16px SpotifyMixUI weight 700, white text. Subtitle at 14px weight 400, `{colors.ink-muted}`. Shadow tinted `{colors.shadow-medium}` on hover."
- "Design a pill button: `{colors.surface-elevated}` background, white text, 9999px radius, 8px 16px padding. 14px SpotifyMixUI weight 700, uppercase, letter-spacing 1.4px."
- "Build a circular play button: Spotify Green (`{colors.primary}`) background, black icon, 50% radius, 12px padding."
- "Create search input: `{colors.surface-elevated}` background, white text, 500px radius, 12px 48px padding. Inset border tinted `{colors.shadow-inset}`."
- "Design navigation sidebar: `{colors.background}` background. Active items: 14px weight 700, white. Inactive: 14px weight 400, `{colors.ink-muted}`."

### Iteration Guide
1. Start with `{colors.background}` — everything lives in near-black darkness
2. Spotify Green for functional highlights only (play, active, CTA)
3. Pill everything — `{rounded.pill-small}` for large, `{rounded.pill}` for small, `{rounded.circle}` for circular
4. Uppercase + wide tracking on buttons — the systematic label voice
5. Heavy shadows for elevation — light shadows are invisible on dark
6. Album art provides all the color — the UI stays achromatic
