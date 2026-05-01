---
slug: mercury-weather
name: Mercury Weather
url: https://mercuryweather.com
domain: mercuryweather.com
category: Productivity
styles: [Gradient, Colorful, Tactile]
tagline: "Coral-to-navy painterly gradients, skeuomorphic dials, SF Pro thin numerals floating in atmosphere."
fonts: []
primary_color: "#FFB07A"
---

# Mercury Weather — Design System

> Painterly skies, dimensional dials, the weather as a felt atmosphere. Mercury Weather treats a forecast like a window — something you look through, not at — and builds its entire visual language around that single conceit.

---

## 1. Atmosphere & Vibe

Mercury Weather doesn't draw weather; it **renders weather as light**. The entire interface is a slowly-shifting painterly sky — a living gradient that morphs from the cool coral of sunrise, through the flat cerulean of midday, into the bruised magenta of dusk, and finally down into the deep navy hush of night. The app's hero surface is never a "white card with a number on it." It is a time-of-day mood that happens to carry information — temperature, conditions, humidity — stacked in front of it like type on a photograph. This is the core craft move: atmosphere leads, data follows.

Underneath the sky sits the second half of the craft: **skeuomorphic weather instruments**. Mercury leans unapologetically into real-world referents — a glass-face wind compass with a pivoting needle, a circular UV ring that fills like a physical dial, a tinted thermometer bar that reads hot-to-cold along a gradient scale, a moon phase rendered as a dimensional sphere with terminator shadow. None of it is flat. None of it is stroked. Everything has depth, a soft specular highlight, and an inner shadow that tells you the dial is set **into** the surface rather than painted onto it. The app feels like a tactile control panel from a well-designed aircraft cockpit — except the cockpit is your weekend plans.

The third layer is **warm, confident typography**. SF Pro carries the entire text hierarchy: oversize thin-weight temperature readouts (the headline "72°" is a display-weight number, letter-spaced tightly, sitting in front of the gradient sky), paired with a quiet text stack for condition labels, location names, and timeline entries. Nothing competes with the atmosphere. The result is an app that feels simultaneously **romantic** (the painterly sky, the warm transitions) and **precise** (the dial mechanics, the crisp numerals) — craft iOS at its calmest and most confident.

---

## 2. Color — The Weather-Mood Palette

Mercury's palette isn't a brand palette. It's a **set of skies** — painterly gradients keyed to time-of-day and weather condition. The same forecast looks radically different at 6am, 1pm, and 11pm because the background is doing the emotional work.

### Sky moods (gradient pairs)

| Mood | Top | Bottom | Use |
|---|---|---|---|
| **Dawn** | `#FFB07A` Sunrise Coral | `#F5C9A8` Peach Veil | 5–8am, clear |
| **Midday Clear** | `#4FA8D8` Sky Blue | `#A9D5EC` Haze | 10am–3pm, clear |
| **Golden Hour** | `#F28A5A` Amber | `#D86A9A` Rose | 5–7pm, clear |
| **Dusk Storm** | `#7A4E8F` Plum | `#3A2C52` Bruise | Overcast evening |
| **Deep Night** | `#0E1B3A` Midnight | `#1C2E5A` Indigo | 10pm–4am, clear |
| **Overcast** | `#6E7D8C` Pewter | `#B4BEC8` Oyster | Grey daytime |
| **Rain Day** | `#4A5F7A` Slate Blue | `#7A8EA3` Tin | Active precipitation |
| **Snow Day** | `#C9D7E6` Glacier | `#F0F5FA` Bone | Winter clear |

### Functional neutrals (warm, not cold)

| Token | Hex | Role |
|---|---|---|
| `--ink` | `#1F1B2E` | Primary text on light skies |
| `--ink-soft` | `#55506B` | Secondary text, labels |
| `--parchment` | `#FBF5ED` | Warm surface (settings sheets) |
| `--fog` | `#EDE7DC` | Soft dividers, inactive |
| `--hairline` | `rgba(31, 27, 46, 0.08)` | Quiet borders on skies |

### Accent mercury

| Token | Hex | Role |
|---|---|---|
| `--mercury` | `#E06D3C` | Brand warm accent (sunset orange) |
| `--mercury-deep` | `#B8471F` | Pressed / hover state |
| `--moonlight` | `#E8E4F0` | Night-mode accent |
| `--ember` | `#F4A261` | Warning / high UV |
| `--verdant` | `#6A9A7B` | Pleasant conditions badge |
| `--storm` | `#4A5F7A` | Severe weather alert surface |

**Rule:** no single color is "the Mercury color." The accent is **whatever time it is where you're standing**. The orange is only ever *an* accent — never a tint overlay on skies, never a large fill. It earns its presence on CTAs and warm active states.

### Condition-specific color moods

| Condition | Primary sky | Secondary wash | Type color |
|---|---|---|---|
| Clear + sunny | Sunrise Coral → Sky Blue | Warm haze | `#1F1B2E` |
| Partly cloudy | Midday Sky → Haze | Soft cloud white `#F0F5FA` at 35% | `#1F1B2E` |
| Rain | Slate Blue → Tin | Cool mist overlay at 12% | `#FBF5ED` |
| Thunderstorm | Bruise → Midnight | Electric cyan flash `#6FD2F7` (rare) | `#FBF5ED` |
| Snow | Glacier → Bone | Ivory particle layer | `#1F1B2E` |
| Fog | Oyster → Parchment | Smoky vignette | `#3A3450` |
| Clear night | Midnight → Indigo | Starfield, moon glow | `#FBF5ED` |
| Overcast | Pewter → Oyster | Low-contrast wash | `#1F1B2E` |

**Accessibility note:** body text on any sky gradient must pass WCAG AA against the *darkest* pixel of the gradient, not the average. When in doubt, drop a subtle 10% scrim between sky and type.

---

## 3. Typography

**Type family:** SF Pro (Display + Text, with Rounded reserved for numerals in large dial readouts). Never substitute.

### Scale

| Token | Size | Weight | Tracking | Role |
|---|---|---|---|---|
| Temperature Hero | 128 / 96 | Thin (100) | -4% | The "72°" on the main sky |
| Display | 44 | Light (300) | -1.5% | Location name ("San Francisco") |
| Title | 28 | Regular (400) | -0.5% | Condition ("Partly Cloudy") |
| Subtitle | 20 | Regular (400) | -0.2% | "H: 74° L: 58°" |
| Body | 16 | Regular (400) | 0 | Forecast copy, descriptions |
| Label | 13 | Medium (500) | +2% (uppercase) | Dial titles ("UV INDEX", "WIND") |
| Caption | 12 | Regular (400) | 0 | Timeline hour tags |
| Mono | 14 | SF Mono Regular | 0 | Coordinates, precise readings |

### Rules

- Temperature numerals **never** bold — always thin weight, letter-spaced negative.
- Labels above dials are **uppercase, tracked-out**, small (13/500/+2%).
- Body copy stays at weight 400. Don't use 600+ for emphasis — use color shift instead.
- Drop shadow on type over skies: `0 1px 2px rgba(0,0,0,0.12)` — just enough to lift off gradient without looking stamped.

---

## 4. Shape Language

Mercury's shapes split into two families:

### Soft rectangles (surfaces, sheets, cards)
- **Corner radius:** 20px for full-bleed sky cards, 16px for stacked data tiles, 12px for inline chips and badges.
- Borders are almost never drawn — separation comes from elevation (shadow) or atmospheric contrast, not hairlines.
- Sheet corners (settings, detail views): 24px top corners only, iOS modal convention.

### Circles (dials, instruments, moon)
- **Wind compass:** perfect circle, ~180px, with a physical-feeling needle that rotates with degree markers at the rim.
- **UV ring / AQI ring / humidity ring:** hollow circular progress, 8–10px stroke, with a gradient fill that shifts from green → amber → red as the value climbs.
- **Moon phase:** 3D sphere, not a 2D crescent. Rendered with a soft radial highlight and a terminator shadow that matches actual phase geometry.
- **Sun path:** shallow arc (not full circle), with a glowing dot that sits at the sun's current elevation along the arc.

**Rule:** numeric summaries are circular. Temporal sequences (hourly, 10-day) are horizontal rectangles. Never the other way around.

---

## 5. Spacing Rhythm

Built on an **8pt grid**, with a deliberate "breathe" between sky and data.

| Token | Value | Use |
|---|---|---|
| `xs` | 4 | Icon-to-label, tight stacks |
| `sm` | 8 | Intra-card spacing |
| `md` | 16 | Card-to-card gutters |
| `lg` | 24 | Section gaps |
| `xl` | 40 | Sky-hero to data stack |
| `xxl` | 64 | Top of screen to temperature |

The temperature hero always has **at least 64pt of sky above and 40pt below** before the condition label starts. Never crowd the hero number — the gradient needs room to breathe.

### Layout grid

Home screen (iPhone, portrait) is a **single-column vertical scroll** with these zones in order:
1. Sky hero with temperature (56–64% of first screen height)
2. Condition narrative (thin 1-line sentence, not a paragraph)
3. Hourly strip (horizontal scroll, 88pt tall)
4. 10-day vertical list
5. Dial grid (2-col, 4–6 dials: UV, wind, humidity, air quality, sunrise/sunset, pressure)
6. Map preview (rounded 20px, ~220pt tall, tap to expand)
7. Details footer (attribution, last updated timestamp)

iPad and Mac adaptations use a two-column layout: sky hero + hourly on the left (fixed), dials and map on the right (scrollable). The sky never shrinks below 420pt tall on any surface — it's the anchor.

### Tap targets

Minimum 44×44pt for every interactive element, per Apple HIG. Dials are large (96–180pt) but the actual tap zone extends to the whole card containing them — no "precision taps on a 96pt dial." Scroll hit-slop on horizontal hourly strip: 12pt above and below the strip itself.

---

## 6. Depth & Elevation — Atmospheric Shadows

Mercury does not use hard drop shadows. Every shadow is a **soft atmospheric bloom** that reads like light scattering through humid air, not like a floating rectangle.

### Elevation tokens

| Level | Use | Shadow |
|---|---|---|
| **Ambient** | Data tiles sitting on sky | `0 1px 2px rgba(20, 30, 60, 0.06), 0 8px 24px rgba(20, 30, 60, 0.08)` |
| **Raised** | Dials, instrument surfaces | `0 2px 6px rgba(20, 30, 60, 0.10), 0 20px 40px rgba(20, 30, 60, 0.12)` |
| **Sheet** | Modals, settings overlay | `0 0 40px rgba(0, 0, 0, 0.18), 0 32px 64px rgba(0, 0, 0, 0.24)` |

### Gradient overlays (the signature move)

Every large surface carries a **diagonal gradient overlay** from top-left (highlight, +8% luminance) to bottom-right (shadow, -12% luminance) at ~10% opacity. This is what makes a tile feel like a painted surface rather than a flat swatch. Applied at `mix-blend-mode: overlay` so it responds to the underlying sky color.

### Glass layer

Data tiles placed directly over the sky use a **frosted glass** treatment: `backdrop-filter: blur(24px) saturate(140%)` with a `rgba(255,255,255,0.14)` tint on light skies, `rgba(20,30,60,0.32)` on dark skies. Always paired with a 1px inner highlight at top: `inset 0 1px 0 rgba(255,255,255,0.25)`.

### Inner shadow (dial insets)

Circular dials always carry an **inner shadow** that seats them into their container: `inset 0 2px 4px rgba(0,0,0,0.15)`. This is what sells the "instrument is set into a panel" feel vs. "circle is floating on top."

### Highlight pass (the top-edge gloss)

Every dimensional dial, tile, and card carries a 1px inner highlight at the top edge: `inset 0 1px 0 rgba(255, 255, 255, 0.22)` on light skies, stepped to `rgba(255, 255, 255, 0.35)` on dark skies. This reads as a soft reflection catching the horizon light and is the single cheapest trick that separates Mercury from flat weather apps.

### Needle and indicator depth

Dial needles are not flat triangles. Each needle is a two-layer composite:
1. Base: dark core shape (`#1F1B2E`) with a 4px blur shadow below it
2. Highlight: a thin (1.5px) inner stroke of `rgba(255,255,255,0.35)` along the top edge only

This makes a needle read as a physical object casting a shadow on the dial face, not a vector drawing on top.

### Ambient light behavior

The whole UI slowly adjusts ambient shadow opacity to time of day: shadows are **longer and warmer** near sunrise/sunset (opacity 0.14, offset 2px further), **tighter and cooler** at midday (opacity 0.08, offset pulled in), **softest and coolest** at night (opacity 0.18 but radius doubled). This is a 5-second tween, imperceptible in the moment, felt over minutes.

---

## 7. Animation Personality

Slow, cinematic, never snappy. Mercury animates like atmospheric phenomena, not like UI.

- **Sky transitions:** 800ms ease-in-out when crossing time-of-day thresholds. Never a jump.
- **Dial needle motion:** Spring physics, overshoot ~8%, settle ~1.2s. Feels like a real weight swinging to rest.
- **Scroll parallax:** Background sky moves at 0.3x scroll speed; foreground temperature stays pinned for the first 60% of scroll, then glides up to a compact header. The horizon shifts.
- **Condition illustration loop:** Clouds drift slowly across the sky (4–8s per cycle), rain falls at a consistent 600ms cadence, snow tumbles with randomized drift.
- **Haptic:** Light tick on dial settle, medium bump on sheet dismiss, none on scroll.

**Never:** bounce-on-tap, elastic pull-to-refresh, card flip. Weather is not playful — it's atmospheric.

### Motion tokens

| Token | Duration | Easing | Use |
|---|---|---|---|
| `calm` | 240ms | `cubic-bezier(0.32, 0.72, 0, 1)` | Tap response, hover lifts |
| `settle` | 520ms | spring (stiffness 180, damping 18) | Dial needles, value changes |
| `breathe` | 800ms | ease-in-out | Sky crossfades, mood shifts |
| `drift` | 4000–8000ms | linear loop | Cloud drift, particle motion |
| `horizon` | scroll-linked | parallax 0.3x | Background sky on scroll |

### Reduced motion

When `prefers-reduced-motion` is active: crossfade skies instantly rather than tween; disable cloud drift; keep dial settle but collapse to 200ms linear; keep haptics. Never strip atmosphere — reduce motion, not character.

---

## 8. Patterns — Solved UI Problems

### Empty state (permissions not granted)
A painterly dawn sky, a small thin-weight "?" glyph where the temperature would be, and body copy: "Mercury needs your location to paint your sky." Warm amber CTA "Enable Location".

### Loading state
Keep the last known sky as background. Show a faint, slow-pulsing opacity wash (not a spinner). Temperature fades to `opacity: 0.4` while new data arrives. Never show a skeleton grey — it would break the atmosphere.

### Error state (no connection)
Dim the sky 20%, cross-fade a very soft overcast tint over the top, and surface a single-line neutral message: "Offline. Showing last update from 2:14 PM." No red. No warning icon.

### Weather condition illustrations
Every condition (sunny, partly cloudy, thunderstorm, fog, hail, snow, windy, clear night) has a **hand-crafted illustration** that matches the sky gradient of the moment. Never an iconographic glyph — always a scene. Clouds have soft bottoms and highlighted tops. Rain is diagonal silver strokes, not dots.

### Hourly timeline
Horizontal scroll, 24 columns. Each hour = a mini-sky-strip (tall, thin gradient matching that hour's predicted mood) with temperature on top and a tiny condition illustration centered. The strip **is** the forecast — reading left-to-right gives you a visual narrative of the day.

### 10-day forecast
Vertical list. Each row is a horizontal bar whose fill gradient spans the day's low-to-high temperature against the overall week range. You read the shape of the week, then the numbers.

### Radar / map
Apple MapKit with a custom color tint matching current sky mood. Precipitation layer rendered with painterly blobs, not grid tiles. Land is dimmed to ~40% luminance; water fades to the sky's indigo. Precip colors move from pale mist (light rain) to luminous magenta (heavy rain/hail) — never traffic-light greens and yellows.

### Notifications
System banners follow the current sky: a morning notification reads over a dawn-coral tinted banner, an evening one over plum. App icon badge uses Mercury Accent (`#E06D3C`) only for urgent alerts (severe weather, freeze warning) — never for count badges.

### Widgets & Lock Screen
Small widget: simplified sky gradient + temperature only, no dials. Medium: sky + temperature + 4-hour strip. Large: full hourly timeline visible. All widgets must render cleanly at 50% opacity for Lock Screen tinted mode — test with a mid-gray tint overlay before shipping.

### Settings sheet
Parchment surface (`#FBF5ED`) with warm dividers. No sky gradient inside settings — the sky is reserved for weather content. Settings feels like opening the back of a pocket watch: warm, quiet, mechanical. Toggles use Mercury Accent when on.

### Severe weather alert
Full-bleed deep `--storm` blue with a subtle diagonal scanline texture. Thin-weight "SEVERE" label in ember orange, body copy in parchment white. Single CTA, no hero number. Calm, not panicked — Mercury never shouts.

### Location search
Search field is a floating pill with glass-blur background over the current sky. Results drop in with a 120ms fade + 4px vertical translate — gentle. Each result shows local temp as a preview sky strip on the right edge of the row.

---

## 9.5. Voice & Tone

Mercury is **warm, observational, quietly poetic**. It narrates weather the way a friend who notices things would — never a meteorologist, never a news anchor.

### Voice anchors
- **Observational over declarative.** "Sunset at 7:48 will paint Ocean Beach in amber and rose" over "Clear skies expected this evening."
- **Specific over generic.** "A gentle westerly" over "Light winds."
- **Sensory over numeric.** Lead with what it feels like; numbers substantiate.
- **Never cute.** No emoji, no puns, no "brr it's cold!" — Mercury has taste.
- **Never alarmist.** Even severe weather copy is composed: "Stay indoors. Lightning within 5 miles until 9 PM."

### Example copy
- Empty state: "Mercury needs your location to paint your sky."
- Loading: "Checking the sky…"
- Rain starting: "Rain arriving in about 18 minutes. Windows worth closing."
- Good day: "A clean day, high of 74°. The kind of light painters work for."
- Cold snap: "Dropping to 28° overnight. Pipes and plants might want covering."

---

---

## 9. Do's and Don'ts

### Do
- **Use gradients for atmosphere** — every large surface should carry a time-of-day sky gradient. The gradient is the brand.
- **Use dimensional shapes for weather dials** — circular instruments with inner shadow, highlights, and needle depth. Make them feel physical.
- **Let the sky do the emotional work** — keep data typography thin and quiet. The background carries the mood.
- **Match illustration style to painterly skies** — soft, airbrushed, gradient-shaded. No flat geometry.
- **Animate at atmospheric speed** — 600–1200ms, ease-in-out, never snappy.
- **Pair SF Pro Thin at hero scale with uppercase tracked-out labels** at small scale.
- **Use warm neutrals** (parchment, fog) over cool greys whenever text lands off-sky.

### Don't
- **Don't use flat weather icons.** SF Symbols weather glyphs are a last resort; hand-crafted dimensional illustrations are the standard.
- **Don't use a single brand color** as the hero color. Mercury's accent is whatever the sky is right now.
- **Don't use hard drop shadows.** Soft atmospheric blooms only. A sharp-edged shadow kills the painterly feel instantly.
- **Don't crowd the temperature hero.** 64pt breathing room above, 40pt below, no exceptions.
- **Don't bold temperature numerals.** Thin weight, letter-spaced negative — always.
- **Don't use cold gray backgrounds** for sheets or modals. Parchment (`#FBF5ED`) or a dimmed sky.
- **Don't break skeuomorphism with flat UI moves** — no underline-only links, no hairline-only tabs. Everything has depth.
- **Don't use red for errors.** It fights the sky. Dim and dissolve instead.
- **Don't animate with bounce or elasticity.** Springs yes, rubber no. Weather has weight, not whimsy.

---

*This is a living document. When the sky changes, the spec changes with it.*
