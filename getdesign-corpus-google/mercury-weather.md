---
version: alpha
name: Mercury Weather
description: Painterly time-of-day skies, dimensional skeuomorphic dials, warm SF Pro typography. Atmosphere leads, data follows.

colors:
  # Sky gradient stops — Dawn
  sunrise-coral: "#ffb07a"
  peach-veil: "#f5c9a8"
  # Midday clear
  sky-blue: "#4fa8d8"
  haze: "#a9d5ec"
  # Golden hour
  amber: "#f28a5a"
  rose: "#d86a9a"
  # Dusk storm
  plum: "#7a4e8f"
  bruise: "#3a2c52"
  # Deep night
  midnight: "#0e1b3a"
  indigo: "#1c2e5a"
  # Overcast
  pewter: "#6e7d8c"
  oyster: "#b4bec8"
  # Rain day
  slate-blue: "#4a5f7a"
  tin: "#7a8ea3"
  # Snow day
  glacier: "#c9d7e6"
  bone: "#f0f5fa"

  # Functional neutrals (warm, not cold)
  ink: "#1f1b2e"
  ink-soft: "#55506b"
  parchment: "#fbf5ed"
  fog: "#ede7dc"
  hairline: "#ebeae8"   # was rgba(31,27,46,0.08) over parchment — Google format requires hex

  # Accent mercury
  primary: "#e06d3c"     # mercury — sunset orange
  primary-pressed: "#b8471f"
  moonlight: "#e8e4f0"
  ember: "#f4a261"
  verdant: "#6a9a7b"
  storm: "#4a5f7a"

  # Atmospheric overlays / shadows (opaque flattenings)
  shadow-ambient: "#dbdde3"  # was rgba(20,30,60,0.06)–0.12 — flattened
  shadow-raised: "#b4b9c4"   # was rgba(20,30,60,0.10)–0.12 — flattened
  shadow-sheet: "#3d3d3d"    # was rgba(0,0,0,0.18)–0.24 — flattened

  # Glass tints (opaque approximations)
  glass-light: "#f4f6f9"     # was rgba(255,255,255,0.14) over light skies
  glass-dark: "#2a3550"      # was rgba(20,30,60,0.32) over dark skies

  # Type-on-sky high-contrast pairing
  ink-on-dark-sky: "#fbf5ed"
  ink-on-fog: "#3a3450"

  # Special-purpose
  cyan-flash: "#6fd2f7"

typography:
  temperature-hero:
    fontFamily: "SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 128px
    fontWeight: 100
    lineHeight: 1.0
    letterSpacing: -5.12px
  display:
    fontFamily: "SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 44px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.66px
  title:
    fontFamily: "SF Pro Display, -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.14px
  subtitle:
    fontFamily: "SF Pro Text, -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.04px
  body:
    fontFamily: "SF Pro Text, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  label:
    fontFamily: "SF Pro Text, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.26px
  caption:
    fontFamily: "SF Pro Text, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0px
  mono:
    fontFamily: "SF Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  2xl: 64px

rounded:
  sm: 12px
  md: 16px
  lg: 20px
  xl: 24px
  pill: 9999px

components:
  # Sky hero — full-bleed gradient surface that carries temperature
  sky-hero:
    backgroundColor: "{colors.sky-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.temperature-hero}"
    rounded: "{rounded.lg}"
    padding: 64px 24px 40px

  # Data tile floating over the sky (frosted glass)
  glass-tile:
    backgroundColor: "{colors.glass-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 16px
  glass-tile-dark:
    backgroundColor: "{colors.glass-dark}"
    textColor: "{colors.ink-on-dark-sky}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 16px

  # Skeuomorphic dial (UV ring, wind compass, humidity)
  dial:
    backgroundColor: "{colors.parchment}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 16px
    size: 180px

  # Inline chip
  chip:
    backgroundColor: "{colors.parchment}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 4px 12px

  # Mercury accent CTA
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.parchment}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.parchment}"

  # Quiet ghost button (over sky)
  button-ghost:
    backgroundColor: "{colors.glass-light}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  # Settings sheet — parchment surface, no sky
  settings-sheet:
    backgroundColor: "{colors.parchment}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xl}"
    padding: 24px

  # Hourly mini-strip (one of 24 in horizontal scroll)
  hourly-strip:
    backgroundColor: "{colors.haze}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 8px 4px

  # 10-day forecast row
  forecast-row:
    backgroundColor: "{colors.parchment}"
    textColor: "{colors.ink}"
    typography: "{typography.subtitle}"
    rounded: "{rounded.sm}"
    padding: 12px 16px

  # Severe alert surface
  severe-alert:
    backgroundColor: "{colors.storm}"
    textColor: "{colors.parchment}"
    typography: "{typography.title}"
    rounded: "{rounded.md}"
    padding: 24px

  # Search pill (floating glass)
  search-pill:
    backgroundColor: "{colors.glass-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 12px 20px

  # Status / condition badge
  badge-pleasant:
    backgroundColor: "{colors.verdant}"
    textColor: "{colors.parchment}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  badge-warning:
    backgroundColor: "{colors.ember}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
---

# Mercury Weather Design System

## Overview

Mercury Weather doesn't draw weather; it **renders weather as light**. The entire interface is a slowly-shifting painterly sky — a living gradient that morphs from the cool coral of sunrise (`{colors.sunrise-coral}`), through the flat cerulean of midday (`{colors.sky-blue}`), into the bruised magenta of dusk (`{colors.plum}`), and finally down into the deep navy hush of night (`{colors.midnight}`). The app's hero surface is never a "white card with a number on it." It is a time-of-day mood that happens to carry information — temperature, conditions, humidity — stacked in front of it like type on a photograph. This is the core craft move: atmosphere leads, data follows.

Underneath the sky sits the second half of the craft: **skeuomorphic weather instruments**. Mercury leans unapologetically into real-world referents — a glass-face wind compass with a pivoting needle, a circular UV ring that fills like a physical dial, a tinted thermometer bar that reads hot-to-cold along a gradient scale, a moon phase rendered as a dimensional sphere with terminator shadow. None of it is flat. None of it is stroked. Everything has depth, a soft specular highlight, and an inner shadow that tells you the dial is set **into** the surface rather than painted onto it. The app feels like a tactile control panel from a well-designed aircraft cockpit — except the cockpit is your weekend plans.

The third layer is **warm, confident typography**. SF Pro carries the entire text hierarchy: oversize thin-weight temperature readouts (the headline "72°" is a display-weight number, letter-spaced tightly, sitting in front of the gradient sky), paired with a quiet text stack for condition labels, location names, and timeline entries. Nothing competes with the atmosphere. The result is an app that feels simultaneously **romantic** (the painterly sky, the warm transitions) and **precise** (the dial mechanics, the crisp numerals) — craft iOS at its calmest and most confident.

**Key Characteristics:**
- Time-of-day gradient skies as the brand surface — atmosphere over fixed brand color
- Skeuomorphic dimensional dials with inner shadow + top-edge highlight
- SF Pro Thin at oversize hero scale with negative tracking for temperature
- Warm neutrals (`{colors.parchment}`, `{colors.fog}`) over cool grays for off-sky surfaces
- Mercury accent (`{colors.primary}`) reserved for CTAs and warm active states — never a tint overlay
- Soft atmospheric shadows only — no hard drop shadows
- Hand-crafted illustrations matched to the current sky mood — never flat icons
- Cinematic motion — 240ms calm, 520ms settle, 800ms breathe — never snappy

## Colors

Mercury's palette isn't a brand palette. It's a **set of skies** — painterly gradients keyed to time-of-day and weather condition. The same forecast looks radically different at 6am, 1pm, and 11pm because the background is doing the emotional work.

### Sky moods (gradient pairs)

| Mood | Top → Bottom | Use |
|---|---|---|
| **Dawn** | `{colors.sunrise-coral}` → `{colors.peach-veil}` | 5–8am, clear |
| **Midday Clear** | `{colors.sky-blue}` → `{colors.haze}` | 10am–3pm, clear |
| **Golden Hour** | `{colors.amber}` → `{colors.rose}` | 5–7pm, clear |
| **Dusk Storm** | `{colors.plum}` → `{colors.bruise}` | Overcast evening |
| **Deep Night** | `{colors.midnight}` → `{colors.indigo}` | 10pm–4am, clear |
| **Overcast** | `{colors.pewter}` → `{colors.oyster}` | Grey daytime |
| **Rain Day** | `{colors.slate-blue}` → `{colors.tin}` | Active precipitation |
| **Snow Day** | `{colors.glacier}` → `{colors.bone}` | Winter clear |

### Functional neutrals (warm, not cold)
- **Ink** (`{colors.ink}`): Primary text on light skies
- **Ink Soft** (`{colors.ink-soft}`): Secondary text, labels
- **Parchment** (`{colors.parchment}`): Warm surface for settings sheets
- **Fog** (`{colors.fog}`): Soft dividers, inactive
- **Hairline** (`{colors.hairline}`): Quiet borders on skies (was `rgba(31, 27, 46, 0.08)`)

### Accent mercury
- **Mercury** (`{colors.primary}`): Brand warm accent (sunset orange) — CTAs, active states only
- **Mercury Pressed** (`{colors.primary-pressed}`): Pressed / hover state
- **Moonlight** (`{colors.moonlight}`): Night-mode accent
- **Ember** (`{colors.ember}`): Warning / high UV
- **Verdant** (`{colors.verdant}`): Pleasant conditions badge
- **Storm** (`{colors.storm}`): Severe weather alert surface

**Rule:** no single color is "the Mercury color." The accent is **whatever time it is where you're standing**. The orange is only ever *an* accent — never a tint overlay on skies, never a large fill. It earns its presence on CTAs and warm active states.

**Accessibility note:** body text on any sky gradient must pass WCAG AA against the *darkest* pixel of the gradient, not the average. When in doubt, drop a subtle 10% scrim between sky and type.

## Typography

### Font Family
- **Primary:** SF Pro (Display + Text), with SF Pro Rounded reserved for numerals in large dial readouts. Never substitute.
- **Mono:** SF Mono — coordinates, precise readings.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference roles via tokens (`{typography.temperature-hero}`, `{typography.body}`, etc).

| Token | Use |
|---|---|
| `temperature-hero` | The "72°" on the main sky — display-weight thin (100), tight tracking |
| `display` | Location name ("San Francisco") |
| `title` | Condition ("Partly Cloudy") |
| `subtitle` | "H: 74° L: 58°" |
| `body` | Forecast copy, descriptions |
| `label` | Dial titles ("UV INDEX", "WIND") — uppercase, tracked-out |
| `caption` | Timeline hour tags |
| `mono` | Coordinates, precise readings |

### Principles
- Temperature numerals **never** bold — always thin weight (100), letter-spaced negative.
- Labels above dials are **uppercase, tracked-out**, small (13/500/+0.26px).
- Body copy stays at weight 400. Don't use 600+ for emphasis — use color shift instead.
- Drop shadow on type over skies: `0 1px 2px {colors.shadow-ambient}` — just enough to lift off gradient without looking stamped.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Built on an **8pt grid**, with a deliberate "breathe" between sky and data.

The temperature hero always has **at least `{spacing.2xl}` of sky above and `{spacing.xl}` below** before the condition label starts. Never crowd the hero number — the gradient needs room to breathe.

### Layout grid

Home screen (iPhone, portrait) is a **single-column vertical scroll** with these zones in order:
1. Sky hero with temperature (56–64% of first screen height)
2. Condition narrative (thin 1-line sentence, not a paragraph)
3. Hourly strip (horizontal scroll, 88pt tall)
4. 10-day vertical list
5. Dial grid (2-col, 4–6 dials: UV, wind, humidity, air quality, sunrise/sunset, pressure)
6. Map preview (rounded `{rounded.lg}`, ~220pt tall, tap to expand)
7. Details footer (attribution, last updated timestamp)

iPad and Mac adaptations use a two-column layout: sky hero + hourly on the left (fixed), dials and map on the right (scrollable). The sky never shrinks below 420pt tall on any surface — it's the anchor.

### Tap targets

Minimum 44×44pt for every interactive element, per Apple HIG. Dials are large (96–180pt) but the actual tap zone extends to the whole card containing them — no "precision taps on a 96pt dial." Scroll hit-slop on horizontal hourly strip: 12pt above and below the strip itself.

## Elevation & Depth

Mercury does not use hard drop shadows. Every shadow is a **soft atmospheric bloom** that reads like light scattering through humid air, not like a floating rectangle.

| Level | Treatment | Use |
|---|---|---|
| Ambient | `0 1px 2px {colors.shadow-ambient}, 0 8px 24px {colors.shadow-ambient}` | Data tiles sitting on sky |
| Raised | `0 2px 6px {colors.shadow-raised}, 0 20px 40px {colors.shadow-raised}` | Dials, instrument surfaces |
| Sheet | `0 0 40px {colors.shadow-sheet}, 0 32px 64px {colors.shadow-sheet}` | Modals, settings overlay |

### Gradient overlays (the signature move)

Every large surface carries a **diagonal gradient overlay** from top-left (highlight, +8% luminance) to bottom-right (shadow, -12% luminance) at ~10% opacity. This is what makes a tile feel like a painted surface rather than a flat swatch. Applied at `mix-blend-mode: overlay` so it responds to the underlying sky color.

### Glass layer

Data tiles placed directly over the sky use a **frosted glass** treatment: `backdrop-filter: blur(24px) saturate(140%)` with a `{colors.glass-light}` tint on light skies, `{colors.glass-dark}` on dark skies. Always paired with a 1px inner highlight at top.

### Inner shadow (dial insets)

Circular dials always carry an **inner shadow** that seats them into their container: `inset 0 2px 4px {colors.shadow-raised}`. This is what sells the "instrument is set into a panel" feel vs. "circle is floating on top."

### Highlight pass (the top-edge gloss)

Every dimensional dial, tile, and card carries a 1px inner highlight at the top edge — a soft reflection catching the horizon light. This is the single cheapest trick that separates Mercury from flat weather apps.

### Needle and indicator depth

Dial needles are not flat triangles. Each needle is a two-layer composite:
1. Base: dark core shape (`{colors.ink}`) with a 4px blur shadow below it
2. Highlight: a thin (1.5px) inner stroke along the top edge only

This makes a needle read as a physical object casting a shadow on the dial face, not a vector drawing on top.

### Ambient light behavior

The whole UI slowly adjusts ambient shadow opacity to time of day: shadows are **longer and warmer** near sunrise/sunset, **tighter and cooler** at midday, **softest and coolest** at night. This is a 5-second tween, imperceptible in the moment, felt over minutes.

## Shapes

Mercury's shapes split into two families: soft rectangles for surfaces and perfect circles for instruments.

| Token | Value | Use |
|---|---|---|
| `sm` | 12px | Inline chips and badges, hourly strips |
| `md` | 16px | Stacked data tiles |
| `lg` | 20px | Full-bleed sky cards, map preview |
| `xl` | 24px | Sheet top corners (settings, detail views) |
| `pill` | 9999px | Wind compass, UV ring, moon phase, search pill |

**Rule:** numeric summaries are circular. Temporal sequences (hourly, 10-day) are horizontal rectangles. Never the other way around. Borders are almost never drawn — separation comes from elevation (shadow) or atmospheric contrast, not hairlines.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (e.g. `{components.sky-hero}`, `{components.dial}`) rather than reconstructing them.

### Sky & atmospheric surfaces
- **`sky-hero`** — full-bleed time-of-day gradient surface that carries the temperature readout. Always the anchor of the screen.
- **`glass-tile`** / **`glass-tile-dark`** — frosted-glass data tile floating over the sky. Light variant for daytime skies, dark for night/storm.

### Instruments
- **`dial`** — circular skeuomorphic instrument: wind compass, UV ring, humidity, AQI. Always carries inner shadow, top-edge highlight, and a dimensional needle/indicator.
- **`hourly-strip`** — one of 24 mini-sky-strips in horizontal scroll. The strip *is* the forecast — reading left-to-right gives you a visual narrative of the day.
- **`forecast-row`** — vertical 10-day forecast row whose fill gradient spans the day's low-to-high temperature against the overall week range.

### Buttons
- **`button-primary`** — Mercury accent CTA, used sparingly for warm action moments.
- **`button-primary-hover`** — pressed state in `{colors.primary-pressed}`.
- **`button-ghost`** — quiet pill button over sky, frosted glass background.

### Sheets & overlays
- **`settings-sheet`** — parchment surface, no sky gradient inside — settings is the back of the pocket watch.
- **`severe-alert`** — full-bleed `{colors.storm}` surface for severe weather. Composed, not panicked.

### Inputs
- **`search-pill`** — floating pill with glass-blur background over the current sky. Results drop in with a 120ms fade + 4px vertical translate — gentle.

### Badges
- **`badge-pleasant`** — verdant pill for "good day" condition badge.
- **`badge-warning`** — ember pill for high UV / advisory states.

### Patterns

- **Empty state (permissions not granted):** painterly dawn sky, a small thin-weight "?" glyph where the temperature would be, and body copy ("Mercury needs your location to paint your sky"). Warm amber CTA "Enable Location".
- **Loading state:** keep the last known sky as background. Show a faint, slow-pulsing opacity wash (not a spinner). Temperature fades to `opacity: 0.4` while new data arrives. Never show a skeleton grey — it would break the atmosphere.
- **Error state (no connection):** dim the sky 20%, cross-fade a very soft overcast tint over the top, and surface a single-line neutral message: "Offline. Showing last update from 2:14 PM." No red. No warning icon.
- **Weather condition illustrations:** every condition has a hand-crafted illustration that matches the sky gradient of the moment. Never an iconographic glyph — always a scene.
- **Radar / map:** Apple MapKit with a custom color tint matching current sky mood. Precipitation rendered with painterly blobs, not grid tiles. Never traffic-light greens and yellows.
- **Notifications:** system banners follow the current sky — morning notifications read over a dawn-coral tinted banner, evening over plum. App icon badge uses Mercury Accent only for urgent alerts (severe weather, freeze warning).
- **Widgets & Lock Screen:** Small = sky + temperature only. Medium = sky + temperature + 4-hour strip. Large = full hourly timeline. All widgets must render cleanly at 50% opacity for Lock Screen tinted mode.
- **Location search:** floating glass pill over the current sky. Each result shows local temp as a preview sky strip on the right edge of the row.

### Animation Personality

Slow, cinematic, never snappy. Mercury animates like atmospheric phenomena, not like UI.

| Token | Duration | Easing | Use |
|---|---|---|---|
| `calm` | 240ms | `cubic-bezier(0.32, 0.72, 0, 1)` | Tap response, hover lifts |
| `settle` | 520ms | spring (stiffness 180, damping 18) | Dial needles, value changes |
| `breathe` | 800ms | ease-in-out | Sky crossfades, mood shifts |
| `drift` | 4000–8000ms | linear loop | Cloud drift, particle motion |
| `horizon` | scroll-linked | parallax 0.3x | Background sky on scroll |

When `prefers-reduced-motion` is active: crossfade skies instantly rather than tween; disable cloud drift; keep dial settle but collapse to 200ms linear; keep haptics. Never strip atmosphere — reduce motion, not character.

### Voice & Tone

Mercury is **warm, observational, quietly poetic**. It narrates weather the way a friend who notices things would — never a meteorologist, never a news anchor.

- **Observational over declarative.** "Sunset at 7:48 will paint Ocean Beach in amber and rose" over "Clear skies expected this evening."
- **Specific over generic.** "A gentle westerly" over "Light winds."
- **Sensory over numeric.** Lead with what it feels like; numbers substantiate.
- **Never cute.** No emoji, no puns, no "brr it's cold!" — Mercury has taste.
- **Never alarmist.** Even severe weather copy is composed: "Stay indoors. Lightning within 5 miles until 9 PM."

## Do's and Don'ts

### Do
- **Use gradients for atmosphere** — every large surface should carry a time-of-day sky gradient. The gradient is the brand.
- **Use dimensional shapes for weather dials** — circular instruments with inner shadow, highlights, and needle depth. Make them feel physical.
- **Let the sky do the emotional work** — keep data typography thin and quiet. The background carries the mood.
- **Match illustration style to painterly skies** — soft, airbrushed, gradient-shaded. No flat geometry.
- **Animate at atmospheric speed** — 600–1200ms, ease-in-out, never snappy.
- **Pair SF Pro Thin at hero scale with uppercase tracked-out labels** at small scale.
- **Use warm neutrals** (`{colors.parchment}`, `{colors.fog}`) over cool greys whenever text lands off-sky.

### Don't
- **Don't use flat weather icons.** SF Symbols weather glyphs are a last resort; hand-crafted dimensional illustrations are the standard.
- **Don't use a single brand color** as the hero color. Mercury's accent is whatever the sky is right now.
- **Don't use hard drop shadows.** Soft atmospheric blooms only. A sharp-edged shadow kills the painterly feel instantly.
- **Don't crowd the temperature hero.** `{spacing.2xl}` breathing room above, `{spacing.xl}` below, no exceptions.
- **Don't bold temperature numerals.** Thin weight, letter-spaced negative — always.
- **Don't use cold gray backgrounds** for sheets or modals. Parchment (`{colors.parchment}`) or a dimmed sky.
- **Don't break skeuomorphism with flat UI moves** — no underline-only links, no hairline-only tabs. Everything has depth.
- **Don't use red for errors.** It fights the sky. Dim and dissolve instead.
- **Don't animate with bounce or elasticity.** Springs yes, rubber no. Weather has weight, not whimsy.

---

## Responsive Behavior

*(Adapted to preserve the original spec's layout/adaptation rules.)*

### Breakpoints
| Surface | Layout |
|---|---|
| iPhone (portrait) | Single-column vertical scroll; sky hero 56–64% of first screen |
| iPhone (landscape) | Sky hero shrinks; hourly strip and dial grid become primary |
| iPad | Two-column: sky hero + hourly fixed left, dials + map scrollable right |
| Mac | Same two-column; sky never shrinks below 420pt tall |
| Watch (complication) | Simplified sky gradient + temperature only |
| Lock Screen widget | Must render cleanly at 50% opacity for tinted mode |

### Touch Targets
- All interactive targets minimum 44×44pt (Apple HIG)
- Dials are 96–180pt visually; tap zone extends to the whole containing card
- Horizontal hourly strip carries 12pt scroll hit-slop above and below

### Collapsing Strategy
- Temperature hero scales from 128pt (large) to 96pt (compact)
- Dial grid: 2-col on iPhone, 3–4 col on iPad, all dials maintain `{rounded.pill}` and inner shadow
- Hourly strip becomes a scrollable rail on watchOS; collapses to single "next hour" peek on Lock Screen

---

## Agent Prompt Guide

*(Composed for this conversion — Mercury's source spec ships with a Voice & Tone section in lieu of agent prompts; both are preserved.)*

### Quick Color Reference
- Dawn sky: `{colors.sunrise-coral}` → `{colors.peach-veil}`
- Midday sky: `{colors.sky-blue}` → `{colors.haze}`
- Night sky: `{colors.midnight}` → `{colors.indigo}`
- Mercury accent: `{colors.primary}` (CTAs only)
- Settings surface: `{colors.parchment}`
- Primary text on light sky: `{colors.ink}`
- Primary text on dark sky: `{colors.ink-on-dark-sky}`
- Severe alert: `{colors.storm}`

### Example Component Prompts

- "Build a Mercury sky hero for midday clear: gradient from `{colors.sky-blue}` top to `{colors.haze}` bottom, `{spacing.2xl}` top padding, `{spacing.xl}` bottom. Temperature '72°' at 128px SF Pro Display weight 100, letter-spacing -4%, color `{colors.ink}`. Below: location at 44px weight 300, condition at 28px weight 400."

- "Design a UV-index dial: 180pt circle, parchment base, inner shadow seating it into the container, top-edge highlight. Hollow ring stroke 8px, gradient green → amber → red along the value path. Label 'UV INDEX' above in 13px SF Pro weight 500 uppercase, +0.26px tracking."

- "Create a frosted glass tile floating on the midday sky: `{colors.glass-light}` background, `backdrop-filter: blur(24px) saturate(140%)`, `{rounded.md}` corners, `{spacing.md}` padding, 1px inner top highlight. Body text 16px SF Pro Text weight 400, color `{colors.ink}`."

- "Render a severe weather alert: full-bleed `{colors.storm}`, thin diagonal scanline texture, 'SEVERE' label in `{colors.ember}` thin weight, body in `{colors.parchment}`. Single CTA, no hero number. Calm, not panicked."

- "Build the search pill: floating glass over current sky, `{rounded.pill}`, `{spacing.md}` horizontal padding. Results drop in with 120ms fade + 4px vertical translate. Each result shows local temp as a preview sky strip on the right edge."

### Iteration Guide

1. Start with the sky — pick a gradient pair from the time-of-day table; everything else builds on top.
2. Temperature hero is non-negotiable thin-weight (100), negative-tracked, with `{spacing.2xl}` air above.
3. Dials are circular and dimensional — inner shadow + top-edge highlight + needle with shadow.
4. Mercury accent (`{colors.primary}`) appears once per screen, on the action that matters most.
5. Shadows are atmospheric blooms, never sharp drop shadows.
6. Sheets and settings live on parchment, not sky — switch surface families when leaving the weather context.
7. Animate at atmospheric speeds (240ms / 520ms / 800ms) — never snappy, never bouncy.
8. When in doubt, drop a 10% scrim between sky and type to preserve WCAG AA against the darkest pixel.
