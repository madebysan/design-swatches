# Design System Inspired by Antimetal

## 1. Visual Theme & Atmosphere

Antimetal is what happens when an infrastructure cost-optimization tool refuses to look like one. The category default is a dark dashboard with neon graphs and the visual energy of a Kubernetes config file. Antimetal goes the other way: a near-white canvas (`#fafeff`), a serif headline face (`Ivar Text`) doing the heavy lifting, and a single jolt of electric chartreuse (`#d0f100`) on exactly one button per screen, the "Book a demo" pill. It reads more like a confident editorial product page than a B2B dashboard ad.

The defining structural move is the **fully pill-shaped CTA**. Antimetal's primary buttons use `border-radius: 33554400px` (the "make it a stadium no matter what" trick), so every CTA, header through footer, is a perfect capsule. Pair that with cards rounded 16–60px and you get a system allergic to sharp corners. Where competitors signal seriousness with hard edges, Antimetal signals approachability through soft geometry.

The third signature is the **layered, cool-tinted shadow stack**. Cards get four to seven stacked shadows in slate-blue (`rgba(0, 39, 80, ...)`), almost always paired with a 1px white inset highlight on top. The effect is product-photography lighting, cards lifted off the page like photographed objects rather than UI rectangles. Add `display-p3` values for the lime, yellow, and accent blue, and the whole system is tuned specifically for wide-gamut Apple displays.

**Key Characteristics:**
- Warm off-white canvas (`#fafeff`) — slightly cooler than Cape's, reads as paper-meets-screen
- Ivar Text serif for display headings paired with a custom sans (`abcdFont`, likely ABC Diatype) for UI
- Electric chartreuse signal color (`#d0f100`) — used exclusively for the primary "Book a demo" pill
- Deep navy primary (`#001033`) — appears as logo background, secondary CTA, and dark mode canvas
- Fully pill-shaped buttons (`33554400px` radius) — every primary action is a capsule
- Layered slate-blue shadow stacks with white inset highlights — cards lit like product photography
- Generous 16–60px card radii — soft geometry as a brand signal in a hard-edged category
- Dotted constellation logomark (`⋮⋮⋮ Antimetal`) — small, mechanical, sits left of the wordmark
- `display-p3` wide-gamut color values throughout — designed for Retina/XDR displays
- Wide breathing room around hero copy; product UI screenshots float in vignettes, not frames

## 2. Color Palette & Roles

### Primary
- **Deep Navy** (`#001033`): The brand's anchor color. Logo background, dark-mode canvas, secondary CTA fill. Functions as Antimetal's "black" — never pure `#000`, always this slightly-lifted indigo.
- **Off-White** (`#fafeff`): Primary page background. A barely-tinted cool white that reads as paper.
- **Pure White** (`#ffffff`): Reserved for inset shadow highlights and inverted text on dark surfaces.

### Brand Accent — The Signal
- **Signal Lime** (`#d0f100` / `color(display-p3 .8157 .9451 0)`): The single chromatic punch. Reserved for the primary CTA (`Book a demo`) and decorative status moments. Wide-gamut value chosen specifically for P3 displays — looks dim on sRGB monitors and electric on modern Macs.
- **Yellow Primary** (`color(display-p3 .9961 .6314 .0039)`): A warmer sibling of the lime — used for highlight pills and "fix" indicators within product UI illustrations.
- **Yellow Shade** (`color(display-p3 .2196 .1882 0)`): The dark-mode counterpart for yellow accents.

### Text Hierarchy (Layered Opacity on Navy)
Antimetal builds its text hierarchy by layering opacity on a single navy base (`#1b2540`) rather than introducing new colors:
- **Text Default** (`#1b2540a3`, ~64% opacity): Body copy, paragraph text. Soft enough to recede.
- **Text Secondary** (`#1b2540b8`, ~72% opacity): Subheads, captions.
- **Text Blog** (`#1b2540e0`, ~88% opacity): Long-form reading text.
- **Icon Muted** (`#1b25408f`, ~56% opacity): Secondary icons.
- **Icon Disabled** (`#1b254052`, ~32% opacity): Inactive states.
- **Headings**: Solid `rgb(27, 37, 64)` — full weight only on display type.

### Surface & Borders (The Ghost System)
A second opacity ladder, this time on the deeper navy `#0c264d`, exclusively for surfaces and chrome:
- **Bg Faint / Ghost / Muted / Loud** (`#0c264d` at 3% / 2% / 5% / 8%): Section banding, hover wells, card fills, pressed states
- **Border Faint / Muted / Loud** (`#0c264d` at 4% / 6%, then `#1528441a` at 10%): 1px dividers, card edges, emphasized containers

### Accent Blue & Diff Colors
- **Accent Blue** (`color(display-p3 .0039 .3686 .9961)` rest, `#131d8e` hover): Link blue, used sparingly inside product UI mockups
- **Diff Green** (`rgb(0, 146, 55)`): "Fix applied" success state inside dashboards
- **Diff Mint** (`rgb(183, 255, 222)`): Highlight pill behind diff additions

### Gradient System
Antimetal is almost gradient-free for chrome and CTAs — it relies on solid + shadow layering. Gradients only appear in decorative `.avif` background transitions and subtle radial glows behind hero copy. CTA fills are always solid.

## 3. Typography Rules

### Font Family
- **Display / Editorial**: `Ivar Text` (Letters from Sweden) — a contemporary serif with optical refinement and stylistic sets activated. Weight 400.
- **UI / Body**: `abcdFont` — Antimetal's internal name for what is almost certainly **ABC Diatype** (Dinamo Typefaces), a precision grotesk. Weights 400 and 450.
- **Fallbacks**: `system-ui` for both.
- **OpenType Features on Ivar Text**: `"ss04", "ss06", "ss09", "ss10", "ss11"` — five stylistic sets active, giving the headline serifs subtly modified terminals and figures (likely tabular numerals + alternate `g`/`a`/`R`).

*Note: Ivar Text is a commercial Letters from Sweden release. ABC Diatype is from Dinamo. For external implementations: GT Sectra or Tiempos Headline serve as Ivar Text substitutes; Inter or Söhne work in place of Diatype.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Ivar Text | 48px (3.00rem) | 400 | 1.17 | -0.46px | Hero headline with five stylistic sets active |
| Display Large | Ivar Text | 46px (2.88rem) | 400 | 1.04 | -0.46px | Section openers — even tighter line-height |
| Display | Ivar Text | 40px (2.50rem) | 400 | 1.05 | -0.4px | Major feature heads |
| Section Heading | Ivar Text | 32px (2.00rem) | 400 | 1.25 | -0.32px | Sub-section titles |
| Sub-heading Large | Diatype | 28px (1.75rem) | 480 | 1.07 | -0.42px | Card titles in heavier weight (480, not 500) |
| Sub-heading | Diatype | 24px (1.50rem) | 450 | 1.17 | -0.24px | Feature card heads, large CTA labels |
| Body Large | Diatype | 22px (1.38rem) | 450 | 1.09 | -0.22px | Lead paragraphs |
| Body | Diatype | 20px (1.25rem) | 400 | 1.30 | -0.1px | Standard reading paragraphs |
| Body Small | Diatype | 18px (1.13rem) | 400 | 1.33 | -0.09px | Secondary body |
| UI Default | Diatype | 16px (1.00rem) | 400 | 1.50 | normal | Buttons, nav, body UI |
| UI Compact | Diatype | 15px (0.94rem) | 450 | 1.33 | -0.075px | Pill button labels |
| Caption | Diatype | 14px (0.88rem) | 450 | 1.43 | normal | Metadata, tag labels |
| Caption Small | Diatype | 13px (0.81rem) | 400 | 1.54 | normal | Footnotes, system text |

### Principles
- **Serif up top, sans below**: Ivar Text owns every display surface ≥28px. Diatype owns everything below. Hard transition, not a gradient.
- **Custom intermediate weights**: Diatype runs at `400` and `450` — not the standard `400/500/700` ladder. The 450 reads as "subtly emphasized," and there is no true bold in body type.
- **Stylistic sets always on**: Every Ivar Text instance ships with `ss04, ss06, ss09, ss10, ss11` active. The serifs are tuned, not default.
- **Tight optical tracking**: Display uses `-0.46px` to `-0.32px`, mid sizes `-0.24px`, body returns to neutral.
- **Generous serif line-height**: Ivar runs at 1.04–1.25 — serif terminals need vertical air a grotesk wouldn't.

## 4. Component Stylings

### Buttons

**Signal Lime CTA (Primary — "Book a demo")**
- Background: Signal Lime (`#d0f100` / P3 `color(display-p3 .8157 .9451 0)`)
- Text: Deep Navy (`rgb(27, 37, 64)`) at 16px; Off-White (`rgb(250, 254, 255)`) at hero 24px
- Padding: `0px 18px` (compact, 32px tall) or `0px 24px` (hero, ~56px tall)
- Radius: `33554400px` — fully pill
- Shadow ("lime glow" stack — four nested inset white glows simulating an inner light source):
  ```
  rgba(255,255,255,0.08) 0 0 16px 8px inset,
  rgba(255,255,255,0.08) 0 0 8px 4px inset,
  rgba(255,255,255,0.08) 0 0 4px 2px inset,
  rgba(255,255,255,0.12) 0 0 2px 1px inset
  ```
- Font: Diatype 15–24px, weight 400–450
- Hover: cyan inset glow (`rgba(219, 247, 255, 0.32)`) appears
- Use: Exactly one per viewport — "Book a demo" is the only action that earns this treatment

**Navy Pill (Secondary — "Log in", header CTA)**
- Background: Deep Navy (`rgb(0, 16, 51)`); Text: Off-White; Radius: `33554400px`
- Shadow (7-layer "polished metal" stack — top-edge highlight, ambient lift, deep undershadow):
  ```
  rgba(24,37,66,0.32) 0 1px 3px,
  rgba(24,37,66,0.44) 0 12px 24px -12px,
  rgba(219,247,255,0.06) 0 8px 16px 0 inset,
  rgba(219,247,255,0.48) 0 0.5px 0.5px 0 inset,
  rgba(219,247,255,0.04) 0 -4px 8px 0 inset,
  rgba(219,247,255,0.24) 0 -0.5px 0.5px 0 inset
  ```
- Font: Diatype 15px weight 450
- Use: Header sign-in, secondary CTAs throughout

**Ghost Pill (Tertiary)**
- Background: `rgba(0, 0, 0, 0)` (transparent)
- Text: Deep Navy (`rgb(27, 37, 64)`) on light; Off-White (`rgb(250, 254, 255)`) on dark
- Border: `1px solid oklab(0.959716 -0.0186663 -0.0181907 / 0.06)` — barely-there hairline
- Radius: `33554400px`
- Shadow: `none` default; cyan inset glow on hover (`rgba(219, 247, 255, 0.32) 0px 0.5px 0.5px inset`)
- Use: Nav links treated as buttons, low-emphasis actions

**Light Soft-Pressed (Form Submit)**
- Background: transparent; Text: Navy; Padding: `8px 6px 8px 8px`; Radius: `8px` (rare exception to the pill rule, for compact form chrome)
- Shadow ("white-paper-on-paper" — 1px white top inset + 4 progressively softer slate drops): `rgba(255,255,255,0.72) 0 1px 1px inset, rgba(4,33,80,0.02) 0 8px 16px, rgba(4,33,80,0.06) 0 1px 2px, rgba(4,33,80,0.04) 0 0 0 1px`
- Use: Inline form submit, compact secondary controls

**Icon Pill (Circular Action)**
- Background: `rgba(12, 38, 77, 0.08)` ghost navy; Icon: Navy at 32% opacity; Padding: `8px` (32×32 circle); Radius: `33554400px`
- Use: Close buttons, navigation arrows, copy-link affordances

### Cards & Containers
- Background: Off-White (`#fafeff`) on light; Deep Navy (`#001033`) on inverted sections
- Border: `1px solid rgba(0, 39, 80, 0.04)` — almost invisible structural hint
- Radius: **16px** default (used 14×, high confidence) for product cards and mockup frames; **20px** for labeled cards; **60px** (used 22×) for hero containers and feature wells
- Shadow — "photographed product" stack: `rgba(0,39,80,0.08) 0 6px 16px -3px, rgba(0,39,80,0.04) 0 0 0 1px`. For floating UI, escalate to 5 layers + 1px white top inset: `rgba(255,255,255,0.88) 0 1px 1px inset, rgba(0,39,80,0.04) 0 48px 72px -12px, rgba(0,39,80,0.03) 0 28px 40px, rgba(0,39,80,0.02) 0 4px 12px, rgba(0,39,80,0.04) 0 0 0 1px`
- Internal padding: 24–48px for content cards; up to 96px for hero feature blocks

### Badges / Tags / Pills
- **Status Pill** (e.g. "● The fix issued", "● Cleanup step on CI job")
  - Background: `rgba(12, 38, 77, 0.05)` — ghost navy fill
  - Text: Diatype 14px weight 450, color Navy at ~88%
  - Padding: `4px 10px`
  - Radius: `33554400px` (pill)
  - Leading dot: 6×6px solid green (`rgb(0, 146, 55)`) or yellow (P3 yellow primary)
- **Compliance Badge** ("SOC 2 · GDPR · HIPAA")
  - Background: transparent or ghost
  - Text: Diatype 13px weight 450
  - Stroke: 1px hairline navy at 4%

### Inputs & Forms
- Background: transparent or `#fafeff`
- Text color: `rgb(27, 37, 64)` (Navy)
- Border: `0px solid` — Antimetal forms are borderless on the field itself, relying on a wrapper card with the photographed-product shadow stack
- Radius: `0px` on the field; the wrapping container holds the rounded corner
- Padding: `15px 20px`
- Font: Diatype 16px weight 400
- Focus: outline-only, no fill change — `outline: rgb(27, 37, 64) none 3px`

### Navigation
- **Top bar**: Off-white background, no shadow, minimal hairline divider on scroll
- Logo: dotted constellation glyph + "Antimetal" wordmark in Ivar Text 24px
- Center nav links: Diatype 16px weight 400, color navy
- Right cluster: "Log in" (Ghost Pill) + "Book a demo" (Signal Lime Pill)
- Mobile breakpoint: 992px — collapses to hamburger
- Sticky behavior: stays pinned on scroll with subtle backdrop blur

### Decorative Elements
- **Layered Shadow Stack**: 4–7 stacked shadows in slate-blue `rgba(0, 39, 80, ...)` paired with a 1px white top inset — studio product photography, not flat UI elevation.
- **`.avif` Decorative Transitions**: Section breaks use AVIF imagery (`footer-background-transition-dark.avif`) — soft animated gradient washes acting as visual chapter dividers.
- **Wide-Gamut P3 Color**: Lime, yellow, and accent blue ship as `display-p3` values. On Retina/XDR the lime CTA visibly glows beyond sRGB; on non-P3 monitors it falls back gracefully but loses its kick.

## 5. Layout Principles

### Spacing System
- Base unit: 8px (high-confidence — appears 50× in extracted data, the most common spacing value)
- Compact scale: 1px, 2px, 4px, 6px, 8px (chrome and tight UI)
- Mid scale: 12px, 16px, 20px, 24px, 28px, 32px (component padding and small gaps)
- Large scale: 38px, 56px, 72px, 96px (section spacing and hero margins)
- Notable: `12px` is heavily used (49×) as a near-tie with 8px — Antimetal's compact rhythm sits between the two

### Grid & Container
- Single major breakpoint at **992px** — mobile/desktop is binary, not a multi-step waterfall
- Max content width: ~1200px for centered hero blocks; product-illustration sections frequently break to ~1400px for cinematic mockup display
- Hero: 2-column on desktop (text left, animated mockup right) collapsing to stacked on mobile
- Feature sections: 3-column "Diagnose / Fix / Prevent" tile pattern with 60px-radius cards
- Integration showcase: logo grid with 4–6 columns of partner marks (GitHub, AWS, PagerDuty, Slack) at low contrast

### Whitespace Philosophy
- **Editorial vertical rhythm**: 96–128px between major sections — page reads like a magazine spread punctuated by product mockups
- **Card-led density**: Inside cards, density is editorial-light. Outside cards, the canvas breathes with significant padding
- **Mockup framing**: Product UI screenshots float in their own shadow-lit vignettes rather than being chrome-bordered. The shadow IS the frame.

### Border Radius Scale
- **2–8px**: Vestigial micro-radii on inline diff blocks and form chrome wrappers
- **16px**: Default card radius (high confidence, 14×) — feature cards, image frames
- **20–28px**: Labeled cards, specialty canvas containers
- **60px**: Hero feature wells (high confidence, 22×) — the "soft cathedral" radius
- **33554400px (pill)**: All buttons, status chips, icon actions

The system is **not binary** like Cape — Antimetal uses a graduated radius ladder where larger surfaces get softer corners, and every interactive element is fully pill-shaped.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no inset | Page canvas, body text, structural containers |
| Hairline Inset (Level 1) | `rgba(0, 39, 80, 0.04) 0px 0px 0px 1px` | 1px shadow border on cards — replaces hard `border` properties |
| Card Lift (Level 2) | `0 6px 16px -3px rgba(0,39,80,.08), 0 0 0 1px rgba(0,39,80,.04)` | Default product cards, image frames, integration tiles |
| Floating UI (Level 3) | 4-layer slate stack + `rgba(255,255,255,0.88) 0 1px 1px inset` top highlight | Hovering modal cards, dashboard mockups, feature spotlights |
| Cinematic Float (Level 4) | 5+ layer stack with `0 56px 88px` ambient + 1px white inset | Hero product mockups — the "photographed off the page" treatment |
| Glow Pill (Level 5) | 4 nested `rgba(255,255,255,0.08–0.12)` insets | Signal Lime CTA — internal light source effect |
| Polished Metal (Level 6) | 7-layer navy stack with cyan inset highlights | Navy primary pill — the most depth-rich button in the system |

**Shadow Philosophy**: Antimetal's shadow system is **photographic**, not architectural. Every elevated surface has a top-edge highlight (1px white inset), an ambient mid-distance shadow, and a long deep contact shadow. The pattern mirrors product photography: key light from above, fill from the front, deep shadow grounding the object. No surface uses a single drop-shadow — minimum 4 stacked layers, often 7.

The slate-blue hue (`rgba(0, 39, 80, ...)`) is deliberate. Pure-black shadows would read as harsh against the off-white canvas. Tinting the shadow with the brand navy creates color cohesion across background, text, and depth.

## 7. Do's and Don'ts

### Do
- Use Ivar Text serif (with `ss04, ss06, ss09, ss10, ss11` active) for all display headings ≥28px
- Pair Ivar Text up top with ABC Diatype (or `abcdFont` equivalent) for everything below 28px — hard cutoff, no gradient
- Reserve Signal Lime (`#d0f100`) exclusively for the primary "Book a demo" CTA — one per viewport
- Use fully pill (`33554400px`) radius on every interactive button, status chip, and icon action
- Stack 4–7 shadow layers in slate-blue (`rgba(0, 39, 80, ...)`) for elevated surfaces
- Always include a 1px white top inset (`rgba(255, 255, 255, 0.72–0.88) 0 1px 1px inset`) on lifted cards
- Build text hierarchy via opacity layering on `#1b2540` rather than picking new colors
- Use `display-p3` color values for the lime, yellow, and accent blue — embrace wide-gamut Mac displays
- Soft-corner everything: 16px default cards, 60px for hero feature wells
- Treat product mockups as photographed objects — let the shadow be the frame, not a hard border

### Don't
- Don't use pure black (`#000000`) for text or shadows — always Navy (`#001033` / `#1b2540`)
- Don't use a single drop-shadow for elevation — stack at minimum 4 layers, always with a white inset highlight
- Don't introduce a third typeface — Ivar Text + Diatype carries the entire system
- Don't use weight 500–700 on Diatype body text — `450` is the maximum emphasis allowed
- Don't apply Signal Lime to anything other than the primary CTA — one application per screen, not two
- Don't use rectangular primary buttons — every CTA is a pill, no exceptions
- Don't introduce hard 1px borders — use a `0 0 0 1px rgba(0,39,80,0.04)` shadow-as-border instead
- Don't use neon green (`#00ff00`) or lime as a sRGB hex — always declare the P3 fallback for wide-gamut accuracy
- Don't crowd the hero — Antimetal hero copy gets 96–128px of vertical air on every side
- Don't introduce gradient fills on CTAs — solid lime or solid navy, layered shadows do the lift

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <650px | Single column, hero stacks, nav collapses to hamburger |
| Tablet | 650–991px | 2-column feature grids, hero remains stacked |
| Desktop | ≥992px | Full multi-column layout, 2-column hero, 3-tile feature grid |
| Wide Desktop | ≥1280px | Hero mockups expand to ~1400px breaking the standard container |

The single official breakpoint at **992px** is deliberate — Antimetal does not waterfall through 5 breakpoints. The site flips from "stacked editorial mobile" to "two-column desktop" with one decision boundary.

### Touch Targets
- Primary pill CTAs: ~48–56px tall on hero, ~32px on header chrome
- Icon pills: 32×32px with extended ~40px tap area; form fields 48–56px tall

### Collapsing Strategy
- **Hero**: 2-column → stacked, mockup reorders below copy
- **Feature tiles**: 3-column "Diagnose / Fix / Prevent" → vertical stack, retaining 16–20px radius
- **Type scale**: 48px Ivar → 32px tablet → 28px mobile, stylistic sets active at all sizes
- **Section spacing**: 128px desktop → 64px mobile, halved but still editorial
- **Card radius**: 60px hero wells reduce to 28–32px on mobile to maintain visual proportion
- Product UI mockups keep the full shadow stack at all sizes — no cheapened mobile treatment

## 9. Agent Prompt Guide

### Quick Color Reference
- Page Background: Off-White (`#fafeff`)
- Primary Text: Navy (`rgb(27, 37, 64)`) at 100%; body at `#1b2540a3` (~64% opacity)
- Headings (Display): Solid Navy (`#1b2540`) in Ivar Text weight 400
- Primary CTA: Signal Lime (`#d0f100` / P3 `color(display-p3 .8157 .9451 0)`)
- Secondary CTA: Deep Navy (`#001033`) with off-white text
- Card Surface: `#fafeff` with shadow `0 6px 16px -3px rgba(0,39,80,.08), 0 0 0 1px rgba(0,39,80,.04)`
- Floating UI Shadow: 5-layer slate stack + `rgba(255,255,255,0.88) 0 1px 1px inset` top highlight
- Border-as-shadow: `rgba(0, 39, 80, 0.04) 0px 0px 0px 1px`
- Pill Radius: `33554400px` (or simply `9999px` — equivalent)

### Example Component Prompts

- "Create a hero on Off-White (`#fafeff`): headline at 48px Ivar Text weight 400, line-height 1.17, letter-spacing -0.46px, color `rgb(27, 37, 64)`, stylistic sets `ss04, ss06, ss09, ss10, ss11` active. Subtitle at 20px Diatype weight 400 in `#1b2540a3`. Primary CTA: Signal Lime pill (`#d0f100`), 24px Diatype weight 450, padding `0 24px`, radius `33554400px`, four-layer inset white glow."

- "Design a feature card on `#fafeff` with `16px` radius and the photographed-product shadow: `rgba(0,39,80,0.08) 0 6px 16px -3px, rgba(0,39,80,0.04) 0 0 0 1px`. Title in Ivar Text 32px weight 400, body in Diatype 16px color `#1b2540a3`, padding 32–48px."

- "Build a navy primary pill — background `rgb(0, 16, 51)`, text `rgb(250, 254, 255)` in Diatype 15px weight 450, radius `33554400px`. Apply the 7-layer 'polished metal' shadow: combine `0 1px 3px rgba(24,37,66,0.32)`, `0 12px 24px -12px rgba(24,37,66,0.44)`, plus four `rgba(219,247,255,...)` cyan insets for the top-edge highlight and undershadow."

- "Create a status pill — background `rgba(12, 38, 77, 0.05)`, leading 6×6px green dot (`rgb(0, 146, 55)`), Diatype 14px weight 450 in `#1b2540e0`, padding `4px 10px`, fully pill radius."

- "Design a floating mockup card — radius 60px, no border, shadow stack: `rgba(255,255,255,0.88) 0 1px 1px inset, rgba(0,39,80,0.04) 0 48px 72px -12px, rgba(0,39,80,0.03) 0 28px 40px 0, rgba(0,39,80,0.04) 0 0 0 1px`. Internal padding 32px."

### Iteration Guide
1. Default to Ivar Text weight 400 for any heading ≥28px, Diatype weight 400/450 below — never mix the two within a single tier
2. Every interactive button gets `33554400px` (fully pill) radius — no rectangular primary CTAs
3. Signal Lime (`#d0f100`) is reserved for the single primary CTA per viewport — additional applications dilute the brand
4. Stack a minimum of 4 shadow layers in `rgba(0, 39, 80, ...)` for any elevated card, paired with a 1px white top inset
5. Build text hierarchy by layering opacity on `#1b2540` (Navy) rather than introducing new gray tokens
6. Use `display-p3` color values for the lime, yellow, and accent blue — sRGB hex is the fallback only
7. The dotted constellation logomark sits left of the wordmark in Ivar Text — never substitute a different glyph
8. Card radii follow the ladder: 16px default, 20px labeled, 60px hero — never invent a mid-range value
9. Replace `border: 1px solid` with `box-shadow: 0 0 0 1px rgba(0, 39, 80, 0.04)` for hairline edges — keeps the soft photographic quality
10. Activate Ivar Text stylistic sets `ss04, ss06, ss09, ss10, ss11` on every display surface — the brand serifs are tuned, not default
