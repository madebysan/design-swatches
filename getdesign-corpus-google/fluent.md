---
version: alpha
name: Microsoft Fluent 2
description: Material-depth design language for Windows 11, Microsoft 365, and Copilot. Acrylic and Mica materials, Segoe UI Variable typography, Communication Blue brand anchor, 4px grid precision, surgical shadow stacks.

colors:
  # Light theme neutral backgrounds
  background: "#f5f5f5"           # Canvas (Mica-adjacent)
  surface: "#fafafa"
  surface-alt: "#ffffff"
  surface-subtle: "#f0f0f0"

  # Dark / Mica theme
  background-dark: "#202020"
  surface-dark: "#292929"
  surface-alt-dark: "#2f2f2f"
  surface-subtle-dark: "#1a1a1a"

  # Text (foreground)
  ink: "#242424"                   # Foreground 1
  text-secondary: "#424242"        # Foreground 2
  text-muted: "#616161"            # Foreground 3 — signature gray
  text-disabled: "#707070"         # Foreground 4
  ink-inverted: "#ffffff"

  # Brand
  primary: "#0078d4"               # Communication Blue
  primary-hover: "#115ea3"
  primary-pressed: "#0f548c"
  primary-stroke: "#0f6cbd"
  on-primary: "#ffffff"

  # Personality palette samples
  red: "#d13438"
  red-dark: "#c50f1f"
  orange: "#f7630c"
  marigold: "#eaa300"
  yellow: "#fde300"
  green: "#107c10"
  green-light: "#13a10e"
  teal: "#02767a"
  lavender: "#7160e8"
  grape: "#881798"
  magenta: "#6b0043"
  berry: "#c239b3"

  # Status semantic
  success: "#107c10"
  success-bg: "#dff6dd"
  warning: "#f7630c"
  error: "#d13438"
  info: "#0078d4"

  # Borders
  border: "#d1d1d1"
  border-subtle: "#e0e0e0"
  border-faint: "#f0f0f0"
  border-dark: "#757575"

  # Acrylic approximations (opaque flatten)
  acrylic-light: "#fafafa"          # opaque approx of rgba(255,255,255,0.60) — Google format requires hex
  acrylic-dark: "#2f2f2f"           # opaque approx of rgba(32,32,32,0.60)

  # Shadow stand-in
  shadow-soft: "#e0e0e0"            # opaque approx of rgba(0,0,0,0.12) — Google format requires hex

typography:
  title-xl:
    fontFamily: "Segoe UI Variable, Segoe UI, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 52px
    fontWeight: 600
    lineHeight: 1.00
    letterSpacing: -1.6px
  title:
    fontFamily: "Segoe UI Variable, Segoe UI, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: -1.6px
  subtitle:
    fontFamily: "Segoe UI Variable, Segoe UI, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0px
  heading:
    fontFamily: "Segoe UI Variable, Segoe UI, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0px
  large:
    fontFamily: "Segoe UI Variable, Segoe UI, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0px
  body-large:
    fontFamily: "Segoe UI Variable, Segoe UI, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0px
  body-strong:
    fontFamily: "Segoe UI Variable, Segoe UI, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0px
  body:
    fontFamily: "Segoe UI Variable, Segoe UI, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0px
  caption:
    fontFamily: "Segoe UI Variable, Segoe UI, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0px
  caption-strong:
    fontFamily: "Segoe UI Variable, Segoe UI, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0px
  caption-2:
    fontFamily: "Segoe UI Variable, Segoe UI, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  micro:
    fontFamily: "Segoe UI Variable, Segoe UI, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0px
  overline:
    fontFamily: "Segoe UI Variable, Segoe UI, -apple-system, system-ui, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 2.56px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 40px
  5xl: 48px
  6xl: 64px
  7xl: 80px

rounded:
  none: 0px
  micro: 2px
  default: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 20px
  pill: 24px
  full: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.default}"
    padding: 6px 12px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"

  button-secondary:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.default}"
    padding: 6px 12px
  button-secondary-hover:
    backgroundColor: "{colors.background}"

  button-subtle:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.default}"
    padding: 6px 12px

  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.pill}"
    padding: 8px 20px

  card-standard:
    backgroundColor: "{colors.surface-alt}"
    rounded: "{rounded.md}"
    padding: 16px

  card-featured:
    backgroundColor: "{colors.surface-alt}"
    rounded: "{rounded.lg}"
    padding: 24px

  card-acrylic:
    backgroundColor: "{colors.acrylic-light}"
    rounded: "{rounded.md}"
    padding: 16px

  input:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.default}"
    padding: 6px 10px
  input-focus:
    backgroundColor: "{colors.surface-alt}"

  badge-neutral:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.caption-2}"
    rounded: "{rounded.default}"
    padding: 2px 8px

  badge-brand:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-2}"
    rounded: "{rounded.default}"
    padding: 2px 8px

  badge-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.caption-2}"
    rounded: "{rounded.default}"
    padding: 2px 8px

  pill-chip:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-2}"
    rounded: "{rounded.full}"
    padding: 2px 10px

  nav-rail:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-strong}"
    padding: 12px 16px

  nav-item:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 8px 12px
---

# Microsoft Fluent 2 Design System

## Overview

Fluent 2 is Microsoft's design language for Windows 11, Microsoft 365, Teams, and Copilot — a system built around the idea that software surfaces should have **material depth**, not just visual hierarchy. Where iOS glassmorphism leans hedonistic and atmospheric, Fluent 2 leans architectural: translucency is used to signal structure, layering, and intent. The signature of the system is the pairing of two specific materials — **Acrylic** (a blurred, translucent surface with luminosity and noise) and **Mica** (a subtle, opaque wallpaper-tinted background that shifts with the user's desktop). Together they replace flat "dark mode vs light mode" with a spatial model of stacked, semi-permeable planes.

The typography is built on **Segoe UI** — Microsoft's decades-old humanist sans — with Segoe UI Variable now shipping on Windows 11 for optical size adjustments at display, text, and small sizes. Display headings run 400–600 weight with tight negative tracking (-1.6px at 52px); body copy sits at a comfortable 16/1.38; captions drop to 10–12px with 600 weight when they need presence in chrome. Compared with Linear's aggressive 72px headlines, Fluent 2's hero scale tops out around 52px — this is a workhorse system designed to live inside productivity apps, not marketing pages.

The neutral palette is the restrained part: near-pure black, a signature 61-gray (`{colors.text-muted}`), pure white, and a cool `{colors.background}` canvas tint. The brand anchor is **Communication Blue** (`{colors.primary}`) — Microsoft's interactive link blue, used for buttons, focus states, and emphasized UI. Beyond that, Fluent 2 ships the richest semantic palette of any modern design system: 28+ numbered neutral backgrounds, 12 foreground variants, and a full personality palette.

**Key Characteristics:**
- Acrylic material: backdrop blur 20–60px + saturate 180% over a translucent surface with luminosity tint
- Mica material: opaque, subtly wallpaper-tinted canvas — cool `{colors.background}` light / `{colors.background-dark}` dark
- Segoe UI / Segoe UI Variable — humanist sans, optical sizes, Microsoft's native typeface since Vista
- 4px baseline precision throughout — radius scale is `2px · 4px · 6px · 8px`, with 12px reserved for cards and 24px+ for pill buttons
- Communication Blue (`{colors.primary}`) as the single brand anchor across every product surface
- Token-driven color system
- Shadow layers are precise, not atmospheric: dual-layer drops at `{colors.shadow-soft}` opacity
- Cool neutral tint (slight blue-gray undertone) rather than warm — this is "office software", not "editorial"

## Colors

### Neutral Backgrounds (Light Theme)
- **Canvas** (`{colors.background}`): Page background — the Mica-adjacent neutral base.
- **Surface** (`{colors.surface}`): Card surfaces one level above canvas.
- **Surface Alt** (`{colors.surface-alt}`): Elevated panels, dialog bodies, input fields.
- **Subtle** (`{colors.surface-subtle}`): Hover states on surfaces, inset zones.

### Neutral Backgrounds (Dark / Mica Theme)
- **Mica Dark** (`{colors.background-dark}`): Dark canvas — wallpaper-tinted base.
- **Surface Dark** (`{colors.surface-dark}`): Elevated surface on dark.
- **Surface Alt Dark** (`{colors.surface-alt-dark}`): Highest elevation on dark.
- **Subtle Dark** (`{colors.surface-subtle-dark}`): Recessed / inset areas on dark.

### Text & Foreground
- **Foreground 1** (`{colors.ink}`): Primary text — near-black with a cool cast.
- **Foreground 2** (`{colors.text-secondary}`): Secondary text, labels.
- **Foreground 3** (`{colors.text-muted}`): **Fluent's signature gray** — muted labels, placeholders, metadata.
- **Foreground 4** (`{colors.text-disabled}`): Disabled text, tertiary info.
- **Foreground Inverse** (`{colors.ink-inverted}`): Text on brand / dark surfaces.

### Brand Anchor
- **Communication Blue** (`{colors.primary}`): The primary brand color — used for buttons, links, focus rings, selected states.
- **Brand Hover** (`{colors.primary-hover}`): Darker shade for hover.
- **Brand Pressed** (`{colors.primary-pressed}`): Pressed / active state.
- **Brand Stroke** (`{colors.primary-stroke}`): Compound brand stroke for borders around branded chrome.

### Personality Palette (sampled)
- **Red** (`{colors.red}`), **Dark Red** (`{colors.red-dark}`), **Orange** (`{colors.orange}`), **Marigold** (`{colors.marigold}`), **Yellow** (`{colors.yellow}`), **Green** (`{colors.green}`), **Light Green** (`{colors.green-light}`), **Teal** (`{colors.teal}`), **Lavender** (`{colors.lavender}`), **Grape** (`{colors.grape}`), **Magenta** (`{colors.magenta}`), **Berry** (`{colors.berry}`).

### Status Semantic
- **Success** (`{colors.success}`), **Warning** (`{colors.warning}`), **Error** (`{colors.error}`), **Info** (`{colors.info}`).

### Borders & Strokes
- **Stroke 1** (`{colors.border}`): Standard light border — the default visible edge.
- **Stroke 2** (`{colors.border-subtle}`): Subtle border.
- **Stroke 3** (`{colors.border-faint}`): Nearly invisible hairline.
- **Stroke Dark 1** (`{colors.border-dark}`): Standard dark-theme border.
- **Focus Stroke**: Communication Blue (`{colors.primary}`), 2px — Keyboard focus ring.

## Typography

### Font Family
- **Primary**: `Segoe UI Variable`, falling back to `Segoe UI Web (West European), Segoe UI, -apple-system, system-ui, Roboto, Helvetica Neue`
- **Fluent 2 ships with Segoe UI Variable** (Windows 11+): optical sizes at Display, Text, and Small points
- **No OpenType display features** — Segoe UI is already optically tuned

### Hierarchy

| Token | Use |
|---|---|
| `title-xl` | 52px Segoe UI Variable 600, -1.6px tracking — hero heading |
| `title` | 40px weight 600, -1.6px tracking — section titles |
| `subtitle` | 28px weight 400 — sub-hero |
| `heading` | 24px weight 600 — feature headings |
| `large` | 20px weight 600 — Button XL, prominent labels |
| `body-large` | 18px weight 400 — intro / lead |
| `body-strong` | 16px weight 600 — emphasized body, link |
| `body` | 16px weight 400 — default reading |
| `caption` | 14px weight 400 — secondary text |
| `caption-strong` | 14px weight 600 — button text, strong labels |
| `caption-2` | 12px weight 400 — metadata, footer |
| `micro` | 10px weight 600 — chip labels, tiny UI |
| `overline` | 16px weight 700 with 2.56px tracking — uppercase eyebrow |

### Principles
- **Segoe UI Variable does the optical work**: use Display OpSz for 24px+, Text OpSz for 12–23px, Small OpSz for ≤11px when the variable font is available
- **Tight tracking at display, relaxed at body**: -1.6px at 52px, -0.24–0.48px at 28–40px, normal below 24px
- **Three weights do most of the work**: 400 (read), 600 (emphasize), 700 (overline only). No 500, no 800+
- **Uppercase lives only in overlines**: 16px/700 with 2.56px tracking is the signature eyebrow treatment
- **Line-height tightens as size grows**: 1.40 at 10px → 1.36 at 14px → 1.38 at 16px → 1.33 at 24px → 1.15 at 28px → 1.00 at 52px

## Layout

### Spacing Scale
Base unit is **4px**. Scale lives in YAML — `xs` (4px) through `7xl` (80px). The 4px baseline is non-negotiable — every padding, margin, and gap snaps to it.

### Grid & Container
- Max content width: 1200px (docs), 1440px (full app shells)
- Docs layout: 240px left rail + 1fr content + 240px right TOC
- Card grids: 2, 3, or 4 columns with 16–24px gutters
- Responsive collapse: rails become drawers at <1024px

### Whitespace Philosophy
- **Density serves productivity**: Fluent 2 is noticeably denser than Stripe or Linear — this is a system for apps where users spend hours
- **4px precision over generous padding**: where other systems use 24/32/48, Fluent 2 uses 12/16/20
- **Material stacking creates space, not margin**: depth via Acrylic/Mica means you don't need white gaps to separate sections

## Elevation & Depth

Fluent 2's depth model has **two materials and six elevation levels**.

### Materials

**Acrylic** — Translucent + Blurred + Luminous
- The "glassmorphism" surface, with precise physics
- Formula: light theme uses `{colors.acrylic-light}` translucent + `backdrop-filter: blur(20px) saturate(180%)`
- Dark variant uses `{colors.acrylic-dark}` translucent
- **Used for**: flyouts, menus, command bars, tooltips, dialogs, taskbar — any transient surface
- **Must appear over content** to work — Acrylic over a solid page is just a fuzzy square

**Mica** — Opaque + Wallpaper-Tinted + Subtle
- Solid surface that SAMPLES the user's wallpaper
- Light approx `{colors.background}`, dark approx `{colors.background-dark}`
- **Not blurred, not translucent** — used for window backgrounds, app shells

### Elevation Layers

| Level | Treatment | Use |
|---|---|---|
| Base (0) | Flat Mica surface, no shadow | Window background, page canvas |
| Shadow 2 | Tight 2px shadow at 12% black | Subtle card hairline, resting state |
| Shadow 4 | Dual 0/2 layer at 12/14% black | Standard cards, resting surface |
| Shadow 8 | Dual 4px + 0px stack | Hover state, raised panels |
| Shadow 16 | Dual 8px + 0px stack | Flyouts, popovers, tooltips |
| Shadow 28 | Dual 14px + 0px stack | Dialogs, modals |
| Shadow 64 | Dual 32px + 0px stack | Full-window dialogs, context menus |

### The 4px Depth Step
Fluent 2's precision comes from locking shadow offsets to the 4px grid: `0, 2, 4, 8, 16, 28, 64`. The blur radius always equals or exceeds 2× the offset.

**Acrylic + Mica working together**: The app window uses Mica. Inside the window, sidebar rails sit at Shadow 2. Cards on the canvas sit at Shadow 4. Hover a card → Shadow 8. Open a dropdown → it uses **Acrylic** (not just Shadow 16) because it needs to FLOAT, not just lift.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `micro` | 2px | Inline UI elements, toggle tracks, small tags |
| `default` | 4px | Buttons, inputs, badges, standard cards — the Fluent 2 default |
| `sm` | 6px | Secondary buttons, dropdowns |
| `md` | 8px | Cards, panels, menus |
| `lg` | 12px | Featured cards, images with rounded corners |
| `xl` | 20px | Hero cards, callouts |
| `pill` | 24px | Large CTA pills |
| `full` | 9999px | Filter chips, status chips |

## Components

The complete component spec lives in YAML.

### Buttons
- **`button-primary`** — Communication Blue background, 4px radius, 6/12 padding. Hover/pressed variants use darker brand shades.
- **`button-secondary`** — White surface, gray border, default radius.
- **`button-subtle`** — Toolbars, icon buttons, menu items.
- **`button-pill`** — 24px radius pill for prominent CTAs (onboarding, marketing).

### Cards
- **`card-standard`** — White background, 8px radius, 16px padding, dual-layer Shadow 4.
- **`card-featured`** — 12px radius, 24px padding for hero/featured sections.
- **`card-acrylic`** — The signature material treatment. Translucent surface with backdrop blur. Must sit over colored or image-filled backdrop.

### Inputs
- **`input`** — White surface, 1px gray border, 4px radius, 6/10 padding. Focus state thickens the **bottom border** to 2px Communication Blue (no outline ring).

### Badges & Chips
- **`badge-neutral`** — Light gray surface, secondary text.
- **`badge-brand`** — Communication Blue surface, white text.
- **`badge-success`** — Soft green tint with semantic green text.
- **`pill-chip`** — Filter/status chip with `{rounded.full}` (9999px).

### Navigation
- **`nav-rail`** — Surface bg with subtle border-right (240px width)
- **`nav-item`** — Standard nav row. Active item adds left border-2 brand color.

## Do's and Don'ts

### Do
- Use Communication Blue (`{colors.primary}`) as the anchor — not a competing brand color
- Snap every size, padding, margin, and radius to the 4px grid
- Use 4px radius as the default — only go to 8px for cards, 24px for pill CTAs
- Use Segoe UI Variable when on Windows, Segoe UI as fallback, then -apple-system
- Apply Acrylic to transient UI chrome (menus, flyouts, tooltips) — not to static page surfaces
- Use Mica as the foundational window background, not for content panels
- Use `{colors.text-muted}` for muted text and placeholders — Fluent's signature gray
- Focus state = bottom border thickens to 2px Communication Blue (don't use a ring outline)
- Use numbered semantic tokens when possible — they're what Figma components expect
- Keep the shadow stack precise: 0px 0px 2px + 0px 2px 4px for Shadow 4. Never a single fat shadow

### Don't
- Don't use pure black for text — `{colors.ink}` (Foreground 1) prevents eye strain
- Don't apply Acrylic to full-page backgrounds — it only reads as Acrylic over colored content
- Don't use Mica for cards or buttons — it's a canvas material, not a component material
- Don't use rounded-full buttons as the default — Fluent's default is 4px
- Don't use warm neutrals (beige, cream) — Fluent's palette is cool-leaning
- Don't use 500 or 800 weights — 400/600/700 is the entire weight system
- Don't use custom focus rings — the 2px bottom-border-in-Communication-Blue is the Fluent focus treatment
- Don't scale display text below 1.0 line-height
- Don't use soft atmospheric drop shadows (large blur, no offset) — Fluent shadows are directional and shallow
- Don't theme Acrylic with heavy color tints — 3–8% is the ceiling

---

## Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|---|---|---|
| Small | <480px | Single column, compact chrome, rails become drawers |
| Medium | 480–768px | 2-col grids, visible but collapsible rail |
| Large | 768–1280px | Standard app shell — rail + content + optional TOC |
| XL | >1280px | Full app shell with right TOC, generous margins |

### Touch Targets
- Minimum 32px tall for buttons (medium), 40px for large
- Icon buttons: 32×32px default, 28px compact
- Pill CTAs: 40–48px tall for marketing / onboarding
- Input fields: 32px height default

### Collapsing Strategy
- Display headings scale: 52px → 40px → 28px
- Left rail (240px) collapses to 48px icon rail at Medium, to drawer at Small
- Card grids: 4 → 3 → 2 → 1
- Padding: 24px → 16px → 12px at Small
- Acrylic menus become full-screen sheets on Small

### Material Behavior
- Acrylic degrades gracefully: on browsers without `backdrop-filter`, fall back to solid higher-opacity approximation
- Mica wallpaper sampling is Windows-native; on web, use a static cool-neutral as approximation
- Reduced motion: disable Acrylic reveal animations but keep the blur

---

## Agent Prompt Guide

### Quick Color Reference
- Primary: Communication Blue `{colors.primary}`
- Primary Hover: `{colors.primary-hover}`
- Primary Pressed: `{colors.primary-pressed}`
- Page background (Mica-adjacent): `{colors.background}`
- Surface: `{colors.surface-alt}`
- Surface subtle: `{colors.surface-subtle}`
- Primary text (Foreground 1): `{colors.ink}`
- Secondary text (Foreground 2): `{colors.text-secondary}`
- Muted text (Foreground 3): `{colors.text-muted}` (signature)
- Border default: `{colors.border}`
- Border subtle: `{colors.border-subtle}`
- Success: `{colors.success}`
- Warning: `{colors.warning}`
- Error: `{colors.error}`
- Focus: `{colors.primary}` (2px bottom border)

### Example Component Prompts
- "Create a hero on `{colors.background}` background. Headline 52px Segoe UI Variable weight 600, line-height 1.00, letter-spacing -1.6px, color `{colors.ink}`. Subtitle 18px weight 400, color `{colors.text-muted}`. Primary button: `{colors.primary}` bg, white text, `{rounded.default}` radius, 6px 12px padding."
- "Design a standard card: `{colors.surface-alt}` background, 1px solid `{colors.border-subtle}` border, `{rounded.md}` radius, 16px padding, dual-layer shadow stack. Title 16px Segoe UI weight 600, body 14px weight 400 color `{colors.text-muted}`."
- "Design an Acrylic menu flyout: translucent `{colors.acrylic-light}` background, backdrop-filter blur(20px) saturate(180%), `{rounded.md}` radius, dual-layer shadow stack. Must sit over colored or image backdrop to read as Acrylic."
- "Build an input field: `{colors.surface-alt}` bg, 1px solid `{colors.border}`, `{rounded.default}` radius, 6px 10px padding. On focus: bottom border thickens to 2px `{colors.primary}` — no outline ring. Text color `{colors.ink}`, placeholder `{colors.text-muted}`."
- "Create a pill CTA: `{colors.primary}` background, white text 16px weight 600, `{rounded.pill}` radius, 8px 20px padding. Hover `{colors.primary-hover}`. For onboarding and marketing surfaces only."

### Iteration Guide
1. Start with Segoe UI Variable if available, Segoe UI as fallback — never Arial or system-ui alone
2. Communication Blue (`{colors.primary}`) is the only brand color you need; every other hue is semantic (status) or personality palette
3. Snap to 4px — if your spacing or radius ends in an odd number, fix it
4. Default radius is 4px, not 6 or 8; 8 is for cards only; 24 is for pill CTAs only
5. Shadow stacks are additive — never a single fat shadow
6. Acrylic only over content backdrops; Mica only as canvas; Shadow for standard elevation
7. Focus = 2px bottom border in `{colors.primary}`, never a full outline ring
8. Muted text is `{colors.text-muted}` — the signature Fluent gray that nearly every site gets wrong
