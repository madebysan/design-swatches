---
slug: granola
name: Granola
url: https://granola.ai
domain: granola.ai
category: AI
styles: [Warm, Minimal, Light, Tactile]
tagline: "Quadrant serif on paper-cream canvas, lime-green held back until it earns its moment."
fonts: [Quadrant, Melange, -apple-system]
primary_color: "#94f27f"
---

# Design System Inspired by Granola

> Quadrant serif on paper-cream canvas, lime-green held back until it earns its moment.

## 1. Visual Theme & Atmosphere

Granola looks like a meeting notebook rendered in light — a warm-neutral canvas with the confidence of a native macOS app and the soft-spoken restraint of a thoughtful notetaker. The entire experience sits on warm off-whites (`#ffffff` pure, `#eaebe5` oats-green-tinted, `#f8f7f3` paper-cream) that feel closer to unbleached paper than LCD glass. Where most AI tools arrive with cold blue gradients and chrome, Granola arrives quietly: a quiet lime-green accent (`#94f27f`) reserved like a highlighter for the single action that matters on any given screen, surrounded by neutrals that carry a faint yellow-olive undertone (`#818179`, `#acada8`, `#454745`). Nothing is cold. Nothing is flat.

The craft shows up in the depth. Cards and surfaces use ring-based inset shadows (`rgba(0, 0, 0, 0.03) 0px 0px 2px 0px inset`) layered with ambient drop shadows (`rgba(0, 0, 0, 0.15) 0px 8px 48px 0px`) to create a tactile, macOS-native sense of floating — like a Finder window hovering over a warm paper desk. Borders are almost never hard: `#d5d5d2` or the hairline `#47432a33` (a warm olive at 20% opacity) provide containment without aggression. The default radius is `8px` for cards and `9999px` for pills — soft but not playful, professional but not rigid. A meeting-note card placed on a Granola surface feels the way a well-typeset index card feels on linen.

The typographic voice is the third pillar of the craft. Granola pairs a custom serif-display face (**Quadrant**, used for hero and heading text at tight tracking `-1.02px` and line-height `1.00`) with a precise sans (**Melange**, 300–500 weight for UI, body, and caption) — the combination reads as "editorial AI assistant" rather than "productivity SaaS." Display type is weight 400 but sits large and airy. UI type is weight 400–500 with modest letter-spacing (`0.2px` on buttons and links) that adds a breath of polish without ever announcing itself. This is dimensional design, not flat design — depth lives in the shadows, warmth lives in the palette, craft lives in the type.

**Key Characteristics:**
- Warm off-white canvas (`#ffffff` pure + `#eaebe5` cream + `#f8f7f3` paper) — never cold, never gray-blue
- Lime-green accent (`#94f27f`) used with extreme restraint — CTAs, focus rings, highlights, nothing else
- Custom Quadrant serif for display/heading + Melange sans for UI — editorial pairing
- Warm-toned neutrals throughout (`#818179`, `#acada8`, `#454745`) with yellow-olive undertones
- Subtle layered shadows: inset hairline + ambient ring + deep ambient drop — warm-tinted, macOS-native
- `8px` card radius, `9999px` pill radius, `4px` input radius — a deliberate three-step scale
- Warm hairline borders (`#d5d5d2`, `#47432a33` olive-tinted at 20% alpha) — containment without aggression
- Heroicons + inline SVGs with linear stroke treatment — never solid, never over-detailed
- "Oats" palette tokens (red, purple, yellow, green, pink, blue) as decorative accents for illustrations only

## 2. Color Palette & Roles

### Primary
- **Granola Ink** (`#0e0f0c`): Primary text on light surfaces — a warm near-black with a faint olive undertone (LCH chroma 1.51 on green axis). Not pure black. Gentler, more paper-like.
- **Accent Lime** (`#94f27f`): The signature Granola green. Used sparingly — primary CTAs, focus rings, key highlights in illustrations. Never a surface background.
- **Accent Strong** (`#79d65e`): Deeper lime for hover states on primary CTAs and emphasis in dark contexts.
- **Accent Text** (`#0d7916`): Forest-green text color used on lime backgrounds — provides legible contrast without breaking the warm palette.

### Secondary & Accent (the "Oats" palette)
Granola exposes a named tertiary palette called "Oats" — decorative, warm, and used almost exclusively in illustrations, badges, and category tints. Each family has a 100 (pastel), 200 (soft), 300 (mid), 400 (deep) rhythm.
- **Oats Red 200** (`#f29e8b`): Warm coral for highlights and soft emphasis.
- **Oats Red 300** (`#e95d3d`): Saturated terracotta for category callouts.
- **Oats Purple 200** (`#cebef8`): Dusty lavender for information tints and meeting-type labels.
- **Oats Yellow 200** (`#febe29`): Honey amber for warning-adjacent states and star markers.
- **Oats Yellow 300** (`#ed9212`): Deeper amber for hover emphasis on yellow tokens.
- **Oats Green 100** (`#e5eacd`): Barely-there sage wash — used as a large surface tint on sections that need to feel "highlighted but calm."
- **Oats Green 200** (`#d1e043`): Chartreuse accent — closer to the brand lime but softer, used for decorative tags.
- **Oats Blue 200** (`#b8d5ff`): Sky-wash blue for cool accents and link-chip backgrounds.
- **Oats Pink 100/200** (`#ffdef6` / `#ffbcef`): Cherry-blossom pinks for illustration details.
- **Oats Gold 100** (`#ede1a1`): Vintage-paper gold — used for "classic" or "premium" tints.

### Surface & Background
- **Paper White** (`#ffffff`): The primary page background. Pure white, but always paired with warm borders and shadows so it never reads cold.
- **Oat Cream** (`#eaebe5`): The signature warm surface — used for secondary sections, card backgrounds, and any surface that needs a gentle "pause" from pure white. This is the warm-neutral anchor.
- **Stone Mist** (`#d5d5d2`): Slightly warmer-than-neutral light gray. Used for card borders and subtle section dividers.
- **Border Hairline** (`#47432a33`): Olive at 20% alpha — the softest possible containment, used between list rows and inside dense layouts.
- **Input Gray** (`hsl(0 0% 89%)` / `#e3e3e3`): Form input borders in their default (unfocused) state.

### Neutrals & Text
- **Ink Deep** (`#0e0f0c`): Primary text — warm near-black.
- **Charcoal Warm** (`#292929`): Secondary heading text, button labels on cream surfaces.
- **Stone 500** (`#454745`): Body text at comfortable reading emphasis — warm mid-gray.
- **Stone 400** (`#4e4d4b`): Caption and metadata text.
- **Neutral 400** (`#acada8`): Disabled text, placeholder text, deeply secondary UI labels.
- **Warm Silver** (`#818179`): Tertiary labels, footnotes, timestamp text.
- **Muted Sage** (`#72726e`): The olive-adjacent mid-gray used on dark backgrounds for soft text.

### Semantic & Accent
- **Focus Ring** (`hsl(109 82% 72%)`): A light lime ring color for input focus — tinted to match the accent family, not a generic blue.
- **Destructive** (`hsl(0 84% 60%)`): Warm red for destructive actions and errors. Used only for irreversible UX moments.
- **Accent Wash** (`#93f27d33`): Lime at 20% alpha — the highlighter effect, used for selected text, highlighted note regions, and hover wash on lime surfaces.

### Gradient System
Granola is **largely gradient-free** — the warm-neutral palette does the work that gradients do elsewhere. The one common exception is soft radial washes behind hero elements and illustrated meeting-note scenes: low-alpha Oats-family tints (`rgba(148, 242, 127, 0.15)` for a lime glow; `rgba(206, 190, 248, 0.12)` for a purple glow) fading to transparent. Never hard color stops. Never rainbow sweeps. Depth comes from shadow layering, not from gradients.

## 3. Typography Rules

### Font Family
- **Display & Heading**: `Quadrant` — a custom serif display face with editorial proportions. Fallbacks: `"Quadrant Fallback", Georgia, "Times New Roman", serif`.
- **UI, Body & Caption**: `Melange` — a custom sans-serif at 300/400/500/600 weights. Fallbacks: `"Melange Fallback", -apple-system, BlinkMacSystemFont, "Inter", "SF Pro Text", system-ui, sans-serif`.
- **System UI accents** (download buttons, OS-chrome moments): `-apple-system, system-ui, "Segoe UI", Roboto, Helvetica, Arial` — deliberately reaching for the native macOS feel.

*Note: Quadrant and Melange are custom licensed faces. External implementations should substitute Georgia for the serif display and Inter or SF Pro Text for the sans.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Quadrant | 68px (4.25rem) | 400 | 1.00 | -1.02px | Maximum presence, tight tracking, editorial |
| Display Secondary | Quadrant | 48px (3.00rem) | 400 | 1.00 | -0.72px | Section anchors |
| Heading Large | Quadrant | 36px (2.25rem) | 400 | 1.11 | -0.54px | Feature titles |
| Heading Standard | Quadrant | 24px (1.50rem) | 400 | 1.33 | normal | Card titles, modal titles |
| Heading Soft | Melange | 24px (1.50rem) | 300 | 1.33 | 0.24px | Alternate heading in sans, lighter weight |
| Body Large | Melange | 20px (1.25rem) | 500 | 1.40 | 0.2px | Button labels, prominent links |
| Body Standard | Melange | 16px (1.00rem) | 400 | 1.50 | normal | Default reading text |
| Body Emphasis | Melange | 16px (1.00rem) | 500 | 1.50 | normal | Medium-weight emphasis |
| Caption | Melange | 14px (0.88rem) | 400–500 | 1.29 | 0.14px | Metadata, labels, form hints |
| Caption Bold | Melange | 14px (0.88rem) | 600 | 1.25 | 0.14px | Micro-headers |
| Micro | Melange | 13px (0.81rem) | 400–500 | 1.23 | 0.13px | Smallest UI text |

### Rules
- Display type is **weight 400** — not light, not bold. The craft is in proportion, not weight.
- Headings and body use **negative letter-spacing at scale** (`-0.54px` to `-1.02px`). Small text uses slight positive tracking (`0.14px`–`0.2px`) for legibility.
- Line-heights are tight at the top (`1.00` for display, `1.11` for large headings) and comfortable in body (`1.40`–`1.50`).
- Never use Quadrant at body sizes. Never use Melange at display sizes. The pairing is strict.
- Button labels use Melange 500 at 16–20px with `0.2px` tracking — just enough weight to feel clickable without shouting.

## 4. Layout & Spacing

### Spacing Scale (8-based, with 2/4/6 for micro)
The spacing scale is based on an 8px rhythm with granular 2/4/6 values for component-internal rhythm. The most-used values are **8px, 16px, 24px, 12px, 4px** — in that order.

- `2px` — hairline internal spacing
- `4px` — tight inline gaps, chip padding
- `6px` — icon-to-label gaps
- `8px` — default tight spacing, input/button internal padding
- `12px` — standard component gutter
- `16px` — standard content gap (most frequent value — 187 uses)
- `20px` — section rhythm
- `24px` — card padding, heading-to-body distance
- `32px` — subsection spacing
- `48px` — major section spacing
- `64px` — hero and landing section rhythm
- `96px` — page-level vertical rhythm
- `176px` — top-level landing section breathing room

### Grid & Containers
- 12-column grid with 20px gutters on main content.
- Max content width: ~1200px. Hero max width: ~1400px with generous internal padding.
- Section vertical padding: `64–176px` — generous, editorial.
- Card padding: `24–28px` internal.

### Breakpoints
`300, 320, 480, 576, 640, 768, 992, 1024, 1280px` — a fine-grained responsive scale. The meaningful ones: `640px` (mobile→tablet), `1024px` (tablet→desktop).

## 5. Shape & Form

### Border Radius
- **4px** — form inputs, tight utilitarian elements (15 uses)
- **6px** — secondary containment, small images (4 uses)
- **8px** — default card, button, container radius (109 uses — the workhorse)
- **12px** — elevated cards and prominent containers (15 uses)
- **16px** — large feature cards (occasional)
- **9999px / pill** — tags, CTAs, avatars, icon buttons (98 uses — common)
- **64px** — legacy/consent buttons with very round pill shape (3 uses)

**Rule of thumb:** Default to `8px` for any rectangular surface. Use `9999px` for anything that should read as a chip, tag, or avatar. Reserve `12px`+ for elevated hero cards.

### Borders
- Default: `1px solid #d5d5d2` — warm light gray, the most common border (85 uses).
- Cool alternate: `1px solid #cfd9de` — used in tweet-embed and quote contexts only.
- Warm hairline: `1px solid #47432a33` (olive at 20% alpha) — the softest possible containment.
- Section dividers: `1px solid #eaebe5` — a warm cream separator that disappears into the background.
- Never use hard black borders. Never use pure gray — always warm-tinted.

## 6. Depth & Elevation (the craft layer)

Granola's depth system is the single most important dimension of its craft. Shadows are **warm-tinted, multi-layer, and subtle** — stacked ring-based insets combined with ambient drops to create tactile macOS-native surfaces.

### The Shadow Scale

**Level 0 — Flat / Ambient Ring (the default elevated surface)**
```css
box-shadow: rgba(0, 0, 0, 0.03) 0px 0px 2px 0px inset;
```
An inner ring at 3% black. Used on most cards, notes, and interactive surfaces. It reads as a "this is a contained surface" signal without looking like a shadow. 14 occurrences in the source — the dominant elevation treatment.

**Level 1 — Soft Lift (hover, subtle emphasis)**
```css
box-shadow:
  rgba(0, 0, 0, 0.03) 0px 0px 2px 0px inset,
  rgba(0, 0, 0, 0.04) 0px 1px 2px 0px,
  rgba(0, 0, 0, 0.03) 0px 2px 8px 0px;
```
Inset ring + tight ambient + soft ambient. The craft move — layers combine so the shadow never looks computed; it looks photographic.

**Level 2 — Standard Card Elevation**
```css
box-shadow:
  rgba(0, 0, 0, 0.03) 0px 0px 2px 0px inset,
  rgba(0, 0, 0, 0.05) 0px 4px 12px 0px,
  rgba(0, 0, 0, 0.03) 0px 0px 36px 0px;
```
This is the warm-tinted ambient wash — 36px of spread at 3% alpha creates a gentle halo around the card, like a soft lamp behind parchment. Found in the source at `rgba(0, 0, 0, 0.03) 0px 0px 36px 0px`.

**Level 3 — Floating / Modal**
```css
box-shadow:
  rgba(0, 0, 0, 0.03) 0px 0px 2px 0px inset,
  rgba(0, 0, 0, 0.15) 0px 8px 48px 0px;
```
The deepest shadow in the system — 48px blur at 15% alpha. Used for modals, popovers, and cards that need to float dramatically. Found in the source at `rgba(0, 0, 0, 0.15) 0px 8px 48px 0px`. Note: the alpha is 15%, not 20%+ — even "floating" is restrained.

### Rules
- **Always layer.** A single shadow declaration looks flat. Granola's craft is the *combination* of inset ring + ambient drop + optional soft spread.
- **Warm-tinted, not gray-blue.** Shadows use `rgba(0, 0, 0, x)` with low alpha so the warm surface color shows through — creating the perception of a warm shadow without explicit tinting.
- **Inset rings replace borders** on elevated surfaces. When a card has the `0px 0px 2px inset` ring, it often has no visible border — the ring is the border.
- **No dramatic directional shadows.** Granola does not use `0 20px 40px -10px` style "poster" shadows. The direction is near-centered, the spread is soft.

### Usage
- **Level 0** (inset ring): default state for cards, notes, buttons, any contained surface.
- **Level 1** (soft lift): hover on cards and notes.
- **Level 2** (card elevation): primary hero cards, feature cards, content tiles.
- **Level 3** (floating): modals, popovers, dropdown menus, meeting-note overlay views.

## 7. Components

### Buttons

**Primary (Accent)**
- Background: `#94f27f` (accent lime)
- Text color: `#0d7916` (accent text / forest green)
- Padding: `0 24px 0 20px` (asymmetric for icon-left alignment)
- Border radius: `9999px` (pill)
- Font: Melange 500, 20px, `0.2px` tracking
- Hover: inset box-shadow `rgba(0, 0, 0, 0.1) 0px 0px 0px 999px inset` (darkens the surface evenly)
- Focus: `outline: rgb(112, 179, 255) solid 2px` + inset hover shadow

**Secondary (Neutral)**
- Background: `#ffffff`
- Text color: `#0e0f0c`
- Border: `1px solid #d5d5d2`
- Padding: `8px 12px`
- Border radius: `8px`
- Font: Melange 500, 16px
- Hover: `rgba(0, 0, 0, 0.024)` wash via inset shadow

**Tertiary (Cream)**
- Background: `#e5eacd` (oats-green-100)
- Text: `#292929`
- Border radius: `9999px`
- Used for soft-emphasis secondary actions

**Dark (Rare)**
- Background: `#000000`
- Text: `#ffffff`
- Only used for consent buttons and dramatic dark-context CTAs.

### Inputs
- Background: `#ffffff`
- Border: `1px solid #e3e3e3`
- Border radius: `4px` (tight, utilitarian)
- Padding: `9px 12px`
- Focus: border becomes `#94f27f` accent, plus `0 0 0 3px rgba(148, 242, 127, 0.2)` focus ring wash

### Cards (the canonical meeting-note)
- Background: `#ffffff`
- Border: none (replaced by inset ring)
- Border radius: `8px` or `12px`
- Shadow: Level 0 or Level 2 depending on emphasis
- Padding: `20–28px`
- Internal spacing: `16px` between heading and body; `12px` between metadata chips

### Links
- Default: `#0e0f0c` (ink), no underline
- Secondary: `#454745` or `#72726e`
- Interactive state: color darkens slightly; no underline appears on hover — interactivity is signalled by cursor + surface wash.

### Badges / Tags
- Pill-shaped (`9999px` radius)
- Background: Oats 100-level tints (`#e5eacd`, `#f8cec5`, `#cebef8`, etc.)
- Text color: matching Oats 400-level (e.g., `#5b6f00` on green-100)
- Padding: `2px 10px`
- Font: Melange 500, 12–13px

## 8. Iconography & Illustration

### Icon System
- **Treatment:** linear stroke, 1.5–2px stroke weight
- **Sets in use:** Heroicons + custom SVGs
- **For implementations:** `solar:*-linear` from Iconify is the closest stylistic match — clean linear strokes, consistent geometry, meeting-domain coverage (document, microphone, headphones, calendar, users)
- **Default size:** 16–24px
- **Color:** inherits text color (`#0e0f0c` on light, `#ffffff` on dark) — icons are never branded lime except when paired with a primary CTA

### Illustration
- Organic, hand-rendered feel with flat Oats-palette fills
- Subjects: meeting scenes, sticky-notes, calendars, people silhouettes, audio waveforms
- No gradients inside illustrations — color comes from the Oats family as flat fills
- Illustrations live on cream (`#eaebe5`) backgrounds, never pure white

## 9. Motion & Interaction

Granola's motion is macOS-native — present, never decorative.

### Principles
- **Ease-out, short durations** (150–220ms for hover, 220–320ms for layout shifts).
- **Opacity + position** over scale. Buttons don't bounce; they dim slightly and softly translate.
- **Inset shadow transitions** on hover: the `rgba(0, 0, 0, 0.1) 0px 0px 0px 999px inset` wash animates in over 150ms.
- **Focus rings** appear instantly (no transition) — accessibility takes priority over smoothness.
- **Cards lift on hover** — Level 0 → Level 1 shadow transition over 200ms.
- **Note-taking UI** (inside product): live text streams in character-by-character, with a faint cursor trailing — the only "AI-native" motion moment.

### Don't
- No parallax scrolling.
- No scroll-triggered animations beyond simple fade-ins.
- No spring bounces on UI chrome.
- No auto-playing illustrations — everything is responsive to user intent.

### Do
- Honor `prefers-reduced-motion` by disabling all transitions > 100ms.
- Keep motion on the mouse (hover) and keyboard (focus) axis — not on scroll.
- Let the shadows do the work — a card lifting from Level 0 to Level 2 on hover conveys more than any animation.
