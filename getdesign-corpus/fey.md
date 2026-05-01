---
slug: fey
name: Fey
url: https://feyapp.com
domain: feyapp.com
category: Finance
styles: [Dark, Tactile, Minimal]
tagline: "Warm charcoal canvas, Calibre at 600, and 29 shadows doing all the color's work."
fonts: [calibre, JetBrains Mono]
primary_color: "#868f97"
---

# Design System Inspired by Fey

> Warm charcoal canvas, Calibre at 600, and 29 shadows doing all the color's work.

## 1. Visual Theme & Atmosphere

Fey's website is warm-dark finance craft at its purest — a near-black canvas that reads as charcoal rather than void, inhabited by floating cards that drift above the surface on cushions of layered shadow. The site opens on a warm charcoal field (`#0b0b0b` at its deepest, with an imperceptible brown-red cast that distinguishes it from Linear's blue-cool black) where the only chromatic event is a single copper-to-amber gradient on the headline — "Earnings in real time" rendered in a sunrise wash that feels lit from within. Everything else — chrome buttons, translucent notification cards, the edges of UI widgets — lives in grayscale, tuned with meticulous inset highlights to feel dimensional rather than flat. This is not a dark theme; it is a dim room, deliberately lit.

The typography is built on `calibre` (the Klim Type Foundry workhorse), running at heavier weights than the Linear/Stripe axis — 600 at display sizes, 400 for body, with a tight 1.00–1.10 line-height at headline scales that compresses type into stable blocks. Where Stripe whispers in weight 300 and Linear engineers in 510, Fey speaks in weight 600: confident, semi-bold, declarative. Numeric displays lean on tabular numerals so a portfolio value at `$24,847.20` never jitters as it ticks. The feel is an Apple-class product utility — precise, typographically disciplined, aware that every pixel on a finance dashboard is a load-bearing piece of information.

What makes Fey unmistakable is its shadow system. The extracted design tokens reveal **29 distinct shadow definitions** — an obsessive taxonomy that treats elevation not as a single `box-shadow` but as a compound lighting model. Primary cards float on 3-layer stacks (`rgba(0,0,0,0.66) 0px 53px 87px, rgba(0,0,0,0.40) 0px 20px 27px, rgba(0,0,0,0.26) 0px 4px 7px`) that simulate a key light plus two fills. Glassy chrome buttons pair outer ambient shadows with `inset` highlights (`rgba(255,255,255,0.32) 1.25px 1.25px 1.25px inset`) to catch a pin-prick of top-edge light. Chart elements ride on chromatic glows — cyan-blue for one dataset (`rgb(59,152,215) 0px 18px 100px 10px`), acid-yellow-green for its counterpart (`rgb(191,240,0) 0px 18px 100px 10px`) — so gains and losses literally radiate their own atmosphere. This is the Fey signature: dimensional depth as the primary design tool, with color reserved for the single note that carries the message.

**Key Characteristics:**
- Warm charcoal canvas (`#0b0b0b`) — not pure `#000000`; holds a faint red-brown undertone that reads as "lit dark" rather than "absence"
- Copper-amber gradient (`#FFB088` → `#E87A4F`) as the ONE chromatic gesture — headlines, key numbers, moments of emphasis only
- `calibre` typeface at weight 600 for display, 400 for body — heavier than the Linear/Stripe axis
- 29-shadow system: 3-to-5 layer stacks for cards, inset-highlight + outer-shadow compounds for buttons, chromatic glows for chart data
- Semi-transparent white borders (`rgba(255,255,255,0.04)` to `rgba(255,255,255,0.16)`) as the only stroke vocabulary
- Pill-shaped pay-off buttons (radius `99px` / `999px`) paired with card radii of `16px` — a deliberate radius bimodal
- Chart glow pairs: cyan `rgb(71,159,250)` for one series, acid-green `rgb(195,245,0)` for the other — colored light, not colored fills
- Tabular numerals on every numeric display — portfolio values, percentages, timestamps never jitter
- Info-blue link color (`#479ffa`) as the single interactive chromatic hit — used in links, not in buttons

## 2. Color Palette & Roles

Fey is a near-achromatic system. Color is a finite resource, not a design decision — it appears in the headline gradient, the chart glows, and nowhere else. Text, chrome, and surfaces are all white/gray on warm charcoal.

### Background & Surface
- **Warm Charcoal** (`#0b0b0b`): Primary canvas. The true page background — a warm near-black with a red-brown undertone. Never use `#000000` at the top level.
- **Deep Black** (`#000000`): Reserved for the darkest layer — edge gradients, vignette overlays, image underlays. A destination, not a default.
- **Surface 1** (`rgba(255,255,255,0.03)`): The lightest elevated surface — hover-state backgrounds, subtle tile tints.
- **Surface 2** (`rgba(255,255,255,0.06)`): Standard elevated surface for cards sitting on the canvas.
- **Surface 3** (`rgba(255,255,255,0.08)`): Button ghost fill, input background, slightly more pronounced lift.
- **Surface Glass** (`rgba(255,255,255,0.12)`): Hover state for translucent buttons, tooltip backgrounds.
- **Surface Frost** (`rgba(255,255,255,0.20)`): Active/selected state on translucent chrome.

### Typography Colors
- **Pure White** (`#ffffff`): Primary text on dark. Used for headings, emphasized values, and the "live" state of UI.
- **Mist** (`#e6e6e6`): Chrome button text, de-emphasized white — off-white for lower-stakes white text.
- **Gunmetal** (`rgba(134,143,151,0.6)`): Secondary text — metadata, captions, timestamps. The cool gray holds its place on the warm charcoal without fighting.
- **Gunmetal Solid** (`#868f97`): Link tertiary, disabled states.

### Brand & Signature Gradient
- **Amber Peach** (`#FFB088`): The lighter stop of the signature gradient — used at the left edge of glowing headlines.
- **Copper Glow** (`#E87A4F`): The saturated middle of the signature gradient — the Fey orange.
- **Burnt Sienna** (`#C45A34`): The darker stop where the gradient terminates or sits on its own for deep-accent moments.
- **Headline Gradient**: `linear-gradient(90deg, #FFB088 0%, #E87A4F 55%, #C45A34 100%)` — applied via `background-clip: text` on hero headlines only.

### Interactive & Link
- **Info Blue** (`#479ffa`): Link color. The ONLY chromatic text that isn't the amber gradient. Used on inline links, never on buttons.

### Chart & Data-Viz Glow Colors
These colors appear exclusively as `box-shadow` glows and stroke colors on chart series — never as fills or background colors.
- **Gain Cyan** (`#479ffa`): The positive/gain series in portfolio charts. Glow stack: `rgb(71,159,250) 0px 4px 16px 2px, rgb(59,152,215) 0px 18px 100px 10px`.
- **Loss Acid** (`#c3f500`): The counter series (historical or comparison). Glow stack: `rgb(203,255,0) 0px 4px 16px 2px, rgb(191,240,0) 0px 18px 100px 10px`.
- **Semantic Gain** (`#22c55e`): For explicit positive movement indicators (up-arrows, +%, green badges). Suggested — Fey's raw tokens don't include a standard gains green; use the acid glow for chart series and this solid green for readout badges.
- **Semantic Loss** (`#ef4444`): For explicit negative movement indicators. Symmetrical pair with gain green.

### Borders & Dividers
- **Hairline Subtle** (`rgba(255,255,255,0.04)`): The most delicate divider — 1px or 3px when used as a pixel-art outline.
- **Hairline Standard** (`rgba(255,255,255,0.08)`): Default card and container border.
- **Hairline Stronger** (`rgba(255,255,255,0.10)`): Button outline, input border.
- **Hairline Dashed** (`rgba(255,255,255,0.16)`): Dashed placeholder/drop-zone style at 1px.

## 3. Typography Rules

### Font Family
- **Primary**: `calibre` (Klim Type Foundry). Fallback stack: `"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`.
- **Monospace**: Not directly observed in the token set — use `"JetBrains Mono", ui-monospace, "SF Mono", Menlo` for code/data displays when needed.
- **OpenType Features**: `font-variant-numeric: tabular-nums` on every numeric display (portfolio values, percentages, chart axis labels, timestamps). This is non-negotiable for a finance product.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Features | Notes |
|------|------|------|--------|-------------|----------------|----------|-------|
| Hero Display | calibre | 54px (3.38rem) | 600 | 1.00 (tight) | normal | — | Single-line hero headlines with gradient fill |
| Display Large | calibre | 48px (3.00rem) | 600 | 1.10 | normal | — | Section hero headlines |
| Heading Large | calibre | 26px (1.63rem) | 600 | 1.00 (tight) | normal | — | Tile titles, dashboard headers |
| Heading | calibre | 24px (1.50rem) | 600–700 | 1.30–1.40 | normal | — | Card titles, feature headers |
| Heading Small | calibre | 18px (1.13rem) | 600–700 | 1.30 | normal | — | Subsection titles |
| Link Large | calibre | 18px (1.13rem) | 600 | 1.00 | normal | — | Prominent "Learn more" style links |
| Body Large | calibre | 18px (1.13rem) | 400 | 1.25 | normal | — | Intro paragraphs, feature descriptions |
| Body | calibre | 16px (1.00rem) | 400 | 1.40 | normal | — | Standard reading text |
| Button | calibre | 14–16px | 400–600 | 1.00–1.32 | normal | — | Primary CTA and secondary buttons |
| Micro Heading | calibre | 15px (0.94rem) | 400–600 | 1.25 | -0.8px | — | Small-caps-adjacent labels with tight tracking |
| Label | calibre | 14px (0.88rem) | 600 | 1.00 | normal | — | Form labels, caption headers |
| Caption | calibre | 14px (0.88rem) | 400 | 1.36 | normal | — | Inline metadata, helper text |
| Caption Small | calibre | 12px (0.75rem) | 600 | 1.40 | normal | — | Tile meta labels |
| Micro | calibre | 11px (0.69rem) | 400 | 1.40 | normal | — | Fine print, timestamps |
| Tag / Nano | calibre | 10px (0.63rem) | 500 | 1.40 | -0.8px | — | Smallest labels — tickers, axis markers |
| Tabular Numeric | calibre | any | 400–600 | match context | normal | `tabular-nums` | ALL money, percentages, ticker data |

### Principles
- **Weight 600 as the headline voice**: Fey lives at 600 where Stripe lives at 300 and Linear lives at 510. Headlines are semi-bold — confident without shouting, dense without being heavy.
- **Tight display line-heights**: 1.00 at 26px+, 1.10 at 48px. Headlines are stable blocks, not flowing paragraphs.
- **Generous body line-height**: 1.25 to 1.40 for body, 1.36 for captions. The ratio between display tightness and body breathing room is the typographic tension of the system.
- **Tabular numerals always on numbers**: A portfolio value is a data point — it must not reflow or jitter as digits change. Enable `font-variant-numeric: tabular-nums` on any container displaying money, percentages, or timestamps.
- **Negative tracking only at micro sizes**: The only elements with `letter-spacing: -0.8px` are 15px micro-headings and 10px nano labels — the small sizes where tightening improves density. Display sizes stay at normal tracking.
- **Two-weight discipline**: Primarily 400 (body, caption) and 600 (display, heading, label). 700 appears rarely for extra-bold emphasis. No light-weight display.

## 4. Component Stylings

### Buttons

**Chrome Primary** (signature)
- Background: `#e6e6e6` (off-white chrome)
- Text: `#000000`
- Padding: `7px 16px`
- Radius: `99px` (full pill)
- Font: 14px calibre weight 600
- Shadow: `rgba(255,255,255,0.25) 0px 0px 14px 0px` (subtle white glow — the chrome catches ambient light)
- Focus: `rgba(0,0,0,0.1) 0px 4px 12px, rgba(0,0,0,0.2) 0px 0px 0px 2px` (deepened shadow + ring)
- Hover: background shifts to `rgba(255,255,255,0.92)`
- Use: Primary CTAs ("Download", "Get started", "Join beta")

**Glass Ghost**
- Background: `rgba(255,255,255,0.08)`
- Text: `#ffffff`
- Padding: `7px 16px`
- Radius: `99px`
- Border: `1px solid rgba(255,255,255,0.10)`
- Font: 14px calibre weight 600
- Hover: background → `rgba(255,255,255,0.12)`
- Use: Secondary actions, inline CTAs inside dark cards ("Join live call", "Learn more")

**Icon Circle**
- Background: `rgba(255,255,255,0.08)` or `rgba(255,255,255,0.20)`
- Border-radius: `50%`
- Size: 28–36px square
- Use: Play/pause, dismiss, expand — small discrete interactions

### Cards & Containers

**Floating Card** (the Fey signature element)
- Background: `#0b0b0b` or slightly lighter `rgba(255,255,255,0.03)` on canvas
- Border: `1px solid rgba(255,255,255,0.08)`
- Radius: `16px` (standard), `12px 12px 0 0` for panel-top treatments
- Padding: 24px–32px
- Shadow (key card): `rgba(0,0,0,0.66) 0px 53px 87px 0px, rgba(0,0,0,0.40) 0px 20px 27px 0px, rgba(0,0,0,0.26) 0px 4px 7px 0px` — the 3-layer stack that defines Fey's depth
- Shadow (subtle lift): `rgba(0,0,0,0.12) 0px 30px 16px, rgba(0,0,0,0.07) 0px 15px 8px, rgba(0,0,0,0.04) 0px 6px 4px` — softer 3-layer for secondary cards

**Notification Pill** (the "Cloudflare earnings call just started" card from the hero)
- Background: `rgba(255,255,255,0.03)` or fully translucent with backdrop blur
- Border: `1px solid rgba(255,255,255,0.08)`
- Radius: `99px` (full pill for inline notifications) or `16px` for taller rows
- Padding: `12px 16px`
- Shadow: `rgb(19,20,25) 0px 0px 0px 0.75px, rgba(0,0,0,0.28) 0px 14px 24px 0px` — hairline outline + 1-layer drop, the "notification floating on glass" treatment
- Contains: icon left (24px rounded), label + secondary text, right-aligned ghost button

**Portfolio / Chart Card**
- All floating-card properties above, plus:
- Numeric headers use `font-variant-numeric: tabular-nums`
- Chart area uses chromatic glow shadows (see Depth section)
- Ticker row at bottom in 10–12px nano type with tabular numerals

### Chart & Data-Viz Cells
Fey's chart cells are the loudest application of its shadow philosophy.
- Line/area chart series use `box-shadow` glows, not fills: `rgb(71,159,250) 0px 4px 16px 2px` for one stack and `rgb(195,245,0) 0px 4px 16px 2px` for its counter
- Secondary atmospheric glow at 100px blur: `rgb(59,152,215) 0px 18px 100px 10px` creates the ambient halo around the data
- Data points/markers at `50%` radius with matching series color
- Axis labels at 10–12px calibre 500 with `-0.8px` tracking and tabular numerals

### Inputs & Forms
- Background: `rgba(255,255,255,0.03)` to `rgba(255,255,255,0.06)`
- Border: `1px solid rgba(255,255,255,0.08)`
- Radius: `5px` (tight) or `6px` (comfortable)
- Text: `#ffffff`, 14–16px calibre 400
- Placeholder: `rgba(134,143,151,0.6)` (Gunmetal)
- Focus: border shifts to `rgba(255,255,255,0.20)` with a subtle outer ring `rgba(255,255,255,0.10) 0 0 0 2px`
- Labels above: 14px calibre 600, color `#e6e6e6`

### Badges & Pills
**Status Pill (gain)**
- Background: `rgba(34,197,94,0.15)`
- Border: `1px solid rgba(34,197,94,0.30)`
- Text: `#4ade80`
- Padding: `2px 8px`, radius `99px`
- Font: 11px calibre 600, tabular numerals

**Status Pill (loss)**
- Symmetric with gain, swap green → red (`#ef4444`)

**Neutral Ticker Tag**
- Background: `rgba(255,255,255,0.06)`
- Border: `1px solid rgba(255,255,255,0.08)`
- Text: `#e6e6e6`
- Padding: `2px 8px`, radius `4px` (squarer than the gain/loss pills)

### Navigation
- Transparent bar over warm charcoal, sticky with backdrop blur `blur(20px)`
- Brand mark left, nav links center (calibre 16px weight 400)
- CTA right: Chrome Primary pill button
- Bottom border: `1px solid rgba(255,255,255,0.04)` — barely-there

## 5. Layout Principles

### Spacing System
- Base unit: 8px with precision intermediates at 2, 6, 7, 14, 17.5
- Observed scale: 2px, 3.75px, 6px, 7px, 14px, 17.5px, 22px, 24px, 32px, 42px, 56px, 79px, 82px, 98px, 120px, 128px, 136px, 152px, 232px
- The presence of `7px`, `14px`, `17.5px`, `42px` suggests a finer 7/14-rhythm layered onto the base 8. Use 8, 16, 24, 32 as the standard rhythm; reach for 7/14/42 for tight financial-UI intervals (button padding, ticker spacing).

### Grid & Container
- Hero: centered column with generous top padding (~120–232px), single-column lockup
- Dashboard sections: 12-column grid, cards spanning 4/6/8/12
- Chart cards: tend to span full width on their row, 320–400px tall
- Max content width: ~1200px with generous margins at large breakpoints

### Whitespace Philosophy
- **Depth over density**: Where Stripe controls rhythm through tight spacing, Fey controls atmosphere through vast dark space. The canvas around cards is as important as the cards themselves — shadow needs room to fall.
- **Breathing-room hero**: The hero headline sits in a large expanse of warm charcoal, with the supporting notification card floating ~80px below. This vertical breathing is what lets the shadows read.
- **Dense card internals**: Inside a card, spacing tightens (8–16px between elements). Outside cards, it relaxes (56–120px between sections).

### Border Radius Scale
- **Micro** (3.2–4px): Input fields, text areas
- **Tight** (5–6px): Small tiles, image thumbnails
- **Comfortable** (7–10px): Standard interactive surfaces
- **Card** (16px): Standard card radius — the workhorse for floating elements
- **Large** (24px): Featured hero cards
- **Top-rounded** (`12px 12px 0 0`): Panel headers, modal tops where the bottom joins a container
- **Pill** (99px / 999px): CTAs, notification pills, all pay-off actions
- **Circle** (50%): Avatars, icon buttons

Notable: Fey's radius scale is bimodal — everything is either modestly rounded (4–16px) or fully pill-shaped (99px+). The mid-range 20–48px radii that other systems use for "soft" cards are deliberately avoided.

## 6. Depth & Elevation — The 29-Shadow System

Fey's shadow system is the single most distinctive aspect of the design language. Rather than a conventional 3–5 elevation ladder, Fey maintains a taxonomy of **29 distinct shadow definitions**, grouped by role and composition principle. Understand the groups, not the individual values.

### Group 1 — Ambient Field Shadow (atmospheric hum)
Single-layer shadows at 44–60px blur, 0px offset, used for the ambient "glow" around hero elements sitting on the canvas.
- `rgba(0, 0, 0, 0.8) 0px 0px 44px 0px` — used 4 times in the token set
- `rgba(0, 0, 0, 0.5) 0px 0px 35px 0px` — secondary ambient
- `rgba(0, 0, 0, 0.5) 0px 0px 35px 0px` — darker variant

**Use**: Hero orbs, featured objects that sit in the center of a space. This is "presence" shadow — it doesn't drop, it surrounds.

### Group 2 — Card Drop Stack (the workhorse)
Multi-layer stacks that simulate a key light plus fill lights. The dominant Fey pattern.

**3-Layer Card Shadow (primary):**
```
rgba(0, 0, 0, 0.66) 0px 53px 87px 0px,
rgba(0, 0, 0, 0.40) 0px 20px 27px 0px,
rgba(0, 0, 0, 0.26) 0px 4px 7px 0px
```
The far shadow at 87px blur establishes atmosphere, the mid at 27px grounds the card to the surface, and the tight 7px contact shadow sharpens the edge. This is the "floating card over warm charcoal" signature.

**5-Layer Card Shadow (hero-level):**
```
rgba(0, 0, 0, 0.45) 0px 45px 75px 0px,
rgba(0, 0, 0, 0.325) 0px 26px 39px 0px,
rgba(0, 0, 0, 0.25) 0px 13px 18px 0px,
rgba(0, 0, 0, 0.196) 0px 5px 8px 0px,
rgba(0, 0, 0, 0.125) 0px 1px 3px 0px
```
Five layers at progressively tighter offsets/opacities — a continuous falloff curve rather than discrete steps. Reserve for the single most prominent element on a screen.

**Subtle 3-Layer (secondary cards):**
```
rgba(0, 0, 0, 0.12) 0px 30px 16px 0px,
rgba(0, 0, 0, 0.07) 0px 15px 8px 0px,
rgba(0, 0, 0, 0.04) 0px 6px 4px 0px
```
A hushed version of the workhorse — lower opacity, no mid blur-push. Use for cards that shouldn't dominate.

### Group 3 — Hairline + Drop (notification chrome)
The signature of Fey's floating notification pills.

```
rgb(19, 20, 25) 0px 0px 0px 0.75px,
rgba(0, 0, 0, 0.28) 0px 14px 24px 0px
```
A near-black 0.75px outline (optically indistinguishable from a 1px border at normal viewing) paired with a single soft drop. The outline gives the pill its crispness; the drop lets it float. Use on inline notification chips, tooltips, and translucent floating chrome.

### Group 4 — Glass Button (inset highlight + drop)
The chrome/glass button treatment.

```
rgba(255, 255, 255, 0.32) 1.25px 1.25px 1.25px 0px inset,
rgba(255, 255, 255, 0.05) 1.25px -1.25px 1.25px 0px inset,
rgba(0, 0, 0, 0.753) 9.22px 43.56px 43.31px 0px
```
Two inset highlights (one top-left warm, one bottom-right cool-tinted) simulate a pin-prick of light catching a curved glass surface. The outer shadow grounds the button on its surface. This is what makes Fey's chrome buttons look injection-molded rather than flat.

### Group 5 — Deep Panel Shadow (max depth)
For modal-level or deeply elevated content.

```
rgba(0, 0, 0, 0.5) 0px 118px 112px 0px,
rgba(0, 0, 0, 0.36) 0px 69.47px 58.42px 0px,
rgba(0, 0, 0, 0.282) 0px 35.68px 27.42px 0px,
rgba(255, 255, 255, 0.32) 0.5px 0.5px 0.5px 0px inset,
rgba(255, 255, 255, 0.05) 0.5px -0.5px 0.5px 0px inset
```
Three drop layers at enormous blur (up to 118px) combined with inset rim-lights. Use sparingly — modal sheets, floating command palettes.

### Group 6 — Chromatic Glow (chart series)
Shadow-as-color. Chart series don't use fills — they use colored glow stacks.

**Cyan/Blue series (gain, primary):**
```
rgb(72, 159, 218) 0px 4px 16px 2px,
rgb(64, 155, 216) 0px 8px 20px 4px,
rgb(80, 163, 220) 2px 12px 22px 8px,
rgb(85, 166, 221) 2px 7px 18px 6px,
rgb(93, 170, 222) 2px 6px 29px 2px,
rgb(51, 148, 214) 0px 5px 18px 10px,
rgb(59, 152, 215) 0px 18px 100px 10px
```
Seven overlaid glows of the same hue at varying offsets, blurs, and spreads — creates the "luminous trail" look on a data line.

**Acid-green series (counter):**
```
rgb(203, 255, 0) 0px 4px 16px 2px,
rgb(195, 245, 0) 0px 8px 20px 4px,
rgb(205, 255, 10) 2px 12px 22px 8px,
rgb(206, 255, 15) 2px 7px 18px 6px,
rgb(208, 255, 26) 2px 6px 29px 2px,
rgb(183, 230, 0) 0px 5px 18px 10px,
rgb(191, 240, 0) 0px 18px 100px 10px
```
Symmetric structure, swapped hue. The pairing is intentional: two luminous gases mixing in the same glass tube.

### Summary Elevation Ladder
For practical application, collapse the 29 shadows into 6 semantic tiers:

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | No shadow | Canvas text, disabled states |
| Ambient | `rgba(0,0,0,0.5) 0px 0px 35px 0px` | Hero glow, featured object halo |
| Standard | Subtle 3-layer stack (Group 2 subtle) | Background cards, supporting content |
| Elevated | 3-layer card stack (Group 2 primary) | Primary cards, dashboard cells — the workhorse |
| Hero | 5-layer card stack (Group 2 hero) | The most prominent element on a screen |
| Floating | Hairline + drop (Group 3) | Notification chips, tooltips |
| Chrome | Inset highlights + drop (Group 4) | Glass/chrome buttons |
| Chart | Chromatic glow stack (Group 6) | Data-viz lines, series markers |

**Shadow Philosophy**: Fey treats elevation as a cinematographic lighting problem. Every elevated surface is lit by a virtual 3-point rig — key light above-behind (the 87px-blur far shadow), fill below (the 27px mid), and contact/edge light (the 7px tight). Cards don't "have a shadow"; they exist in a lit room. This is why single-layer `box-shadow` values look wrong on a Fey surface — they break the lighting model.

## 7. Do's and Don'ts

### Do
- Use warm charcoal `#0b0b0b` as the canvas, not pure black — the warmth matters
- Apply 3-layer shadow stacks on every elevated card, minimum — no single-layer drops
- Enable `font-variant-numeric: tabular-nums` on every numeric display without exception
- Reserve the copper-amber gradient for headlines only — never for buttons, never for icons
- Use pill radius (99px+) on all primary CTAs and notification chips
- Pair inset highlights with outer shadows on all chrome/glass buttons
- Use colored `box-shadow` glows (not fills) for chart series — gain cyan, loss acid-green
- Use semi-transparent white borders (`rgba(255,255,255,0.04–0.10)`) throughout
- Use calibre at weight 600 for headlines — that's the brand voice
- Keep text hierarchy achromatic (white, off-white, gunmetal) except for the single gradient moment

### Don't
- Don't use pure `#000000` as the page background — Fey's black is always warm
- Don't use single-layer `box-shadow` on cards — it breaks the lighting model
- Don't apply the copper gradient to buttons, icons, borders, or backgrounds — it's a typographic event only
- Don't use saturated color fills in charts — Fey charts glow, they don't paint
- Don't use proportional numerals on money or percentages — jitter is disqualifying
- Don't reach for mid-range radii (20–48px) — Fey is bimodal: 4–16px or pill
- Don't use calibre at weight 300 or below — Fey headlines are weight 600, confident
- Don't introduce a third chromatic color — Fey is achromatic + amber gradient + chart glows, period
- Don't use drop shadows with warm tints — Fey's shadows are neutral black; the warmth is in the canvas, not the depth

## 8. Responsive Behavior

### Breakpoints
Fey's token set shows an unusually dense breakpoint array — 24 distinct widths from 340px to 1440px. Treat this as evidence of a highly tuned responsive layout. For practical use:

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <540px | Single column, hero collapses to 32–40px display |
| Mobile | 540–768px | Single column, 24px horizontal padding |
| Tablet | 768–1024px | 2-column grids for feature tiles |
| Desktop | 1024–1280px | Full 12-column layout, 3–4 column feature grids |
| Large Desktop | >1280px | Centered content, generous side margins |

### Touch Targets
- Pill buttons hit a minimum of `7px 16px` padding for a ~32px touch target — tight but acceptable; increase to `10px 20px` on mobile
- Icon circles at 36–44px on mobile
- Chart data points enlarged to minimum 24px tap-target with invisible hit-area expansion

### Collapsing Strategy
- Hero display: 54px → 40px → 32px across breakpoints, weight 600 maintained
- Card shadows: 5-layer hero stacks simplify to 3-layer on mobile to save render cost
- Chart glows: reduce from 7-stack to 3-stack on mobile; maintain the color semantics
- Notification pills: stay pill-shaped but wrap content vertically on narrow screens
- Dashboard grids: 4-col → 2-col → 1-col stacked

### Image & Media Behavior
- Product screenshots maintain the 3-layer card shadow at all breakpoints
- Chart SVGs resize fluidly with `preserveAspectRatio` and maintain their glow stacks via `filter: drop-shadow()` as a fallback on elements that can't take multi-layer `box-shadow`
- Hero gradient text uses `background-clip: text` — falls back to solid `#E87A4F` where unsupported

## 9. Agent Prompt Guide

### Quick Color Reference
- Canvas: Warm Charcoal (`#0b0b0b`)
- Card border: Hairline Standard (`rgba(255,255,255,0.08)`)
- Primary text: Pure White (`#ffffff`)
- Secondary text: Gunmetal (`rgba(134,143,151,0.6)`)
- Link: Info Blue (`#479ffa`)
- Headline gradient: `linear-gradient(90deg, #FFB088 0%, #E87A4F 55%, #C45A34 100%)` applied via `background-clip: text`
- Chrome button: `#e6e6e6` bg, `#000` text
- Gain chart glow: `#479ffa` — used as `box-shadow` color, not fill
- Loss chart glow: `#c3f500` — used as `box-shadow` color, not fill
- Semantic gain pill: `#22c55e` on `rgba(34,197,94,0.15)` bg
- Semantic loss pill: `#ef4444` on `rgba(239,68,68,0.15)` bg

### Example Component Prompts
- "Create a floating portfolio card on a `#0b0b0b` canvas. 16px radius, 1px solid `rgba(255,255,255,0.08)` border, `rgba(255,255,255,0.03)` background. Shadow: `rgba(0,0,0,0.66) 0px 53px 87px, rgba(0,0,0,0.40) 0px 20px 27px, rgba(0,0,0,0.26) 0px 4px 7px`. Inside: value at 48px calibre 600 with `font-variant-numeric: tabular-nums` displaying `$24,847.20`. Below, +2.34% today in 14px calibre 600 color `#22c55e`."
- "Build a hero headline: `calibre`, 54px, weight 600, line-height 1.00, color transparent, `background: linear-gradient(90deg, #FFB088, #E87A4F 55%, #C45A34)`, `background-clip: text`, `-webkit-background-clip: text`. Subtitle in 18px calibre 400, color `rgba(255,255,255,0.7)`."
- "Design a chrome CTA: `#e6e6e6` background, `#000` text, 14px calibre 600, `7px 16px` padding, `99px` radius, `box-shadow: rgba(255,255,255,0.25) 0px 0px 14px 0px`. Hover: background `rgba(255,255,255,0.92)`. Focus: `box-shadow: rgba(0,0,0,0.1) 0px 4px 12px, rgba(0,0,0,0.2) 0px 0px 0px 2px`."
- "Build a notification pill: 99px radius, `rgba(255,255,255,0.03)` background, `box-shadow: rgb(19,20,25) 0px 0px 0px 0.75px, rgba(0,0,0,0.28) 0px 14px 24px`. Contains 24px icon, label in 14px calibre 600 white, secondary text in 14px calibre 400 gunmetal, right-aligned ghost button."
- "Design a chart line series with Fey glow: SVG stroke at 2px `#479ffa`, `filter: drop-shadow(0 4px 16px rgba(71,159,250,0.5)) drop-shadow(0 18px 100px rgba(59,152,215,0.3))`. Data points as 8px circles with the same drop-shadow stack."

### Iteration Guide
1. Always start from warm charcoal `#0b0b0b` — never pure black
2. Never use single-layer `box-shadow` on elevated elements — use the 3-layer card stack (`rgba(0,0,0,0.66) 0 53px 87px, rgba(0,0,0,0.40) 0 20px 27px, rgba(0,0,0,0.26) 0 4px 7px`)
3. calibre at weight 600 for headlines, 400 for body — no weight 300, no weight 500 for type
4. Tabular numerals on every number, without exception
5. The copper gradient is typographic only — `background-clip: text` on `<h1>`, `<h2>`, or `<span>` with an explicit semantic role
6. Chrome buttons need the inset-highlight + outer-shadow compound to look "injection-molded"
7. Chart series use `box-shadow` or `filter: drop-shadow` glows, not `fill` or `background-color`
8. Border strokes are always semi-transparent white at 4–10% opacity — no solid gray borders
9. Radii are bimodal: 4–16px for containers, 99px+ for pills. Avoid the 20–48px mid-range.
