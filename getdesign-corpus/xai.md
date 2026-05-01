---
slug: xai
name: xAI
url: https://x.ai
domain: x.ai
category: AI
styles: [Dark, Mono, Minimal]
tagline: "Monochrome by design — Universal Sans 80px tight, GeistMono uppercase 14px, 9999px pill buttons on near-black `#1f2228`."
fonts: [Universal Sans, GeistMono]
primary_color: "#1f2228"
---

# Design System Inspired by xAI

> Monochrome by design — Universal Sans 80px tight, GeistMono uppercase 14px, 9999px pill buttons on near-black `#1f2228`.

## 1. Visual Theme & Atmosphere

xAI's site is the most aggressively monochromatic page in the major-AI-lab cohort — and that is the point. There is no chromatic accent color. The entire system runs on white (`#ffffff`), a near-black with a faint cool-blue chroma (`#1f2228` / `lch(13.16% 4.48 273.6)`), a slightly deeper `#0a0a0a`, and a single neutral mid-gray (`#7d8187`) for secondary text. That's the palette. There is no purple, no cyan, no teal, no warm-orange tech-AI accent. Where Anthropic uses terracotta and parchment, where OpenAI hints at a green-teal, xAI commits to **pure neutral chrome** — and the absence is the brand statement.

The typographic signature is **Universal Sans at weight 400**, sized from 16px up to 80px / line-height 1.00 with tight letter-spacing (`-2px` at the hero). Universal Sans (designed by Universal Thirst / Tobias Frere-Jones, distributed via Universal Type Foundry) is a single-weight grotesk with terminal precision — it reads as "engineering instrument" rather than "marketing typeface." The uppercase chrome layer runs in **GeistMono** (Vercel's open-source mono) at 14px with `letter-spacing: 1.4px` and `text-transform: uppercase` — for buttons, links, and small caps. This sans + mono pairing is the second-most-defining move after the monochrome palette.

What makes xAI feel **uniquely terminal-direct** is the **9999px full-pill border-radius** (13 instances on the homepage — every button is a perfect pill) combined with the **almost complete absence of shadows**. The only declared shadow on the page is `rgb(255, 255, 255) 0px 0px 0px 0px, rgb(113, 113, 122) 0px 0px 0px 2px` — a 2px ring focus indicator. That's the entire shadow system. There are no drop shadows, no atmospheric blurs, no glows, no glassmorphism. Surfaces sit flat on the canvas and depth comes exclusively from 1px borders at low alpha (`rgba(255, 255, 255, 0.25)` and `rgba(255, 255, 255, 0.1)`) and from solid color blocks. The page reads like a monospace terminal that decided to take a UI design class — and stopped attending after week two on principle.

**Key Characteristics:**
- Monochrome by design — only `#ffffff`, `#1f2228`, `#0a0a0a`, and `#7d8187` appear
- Universal Sans at 80px / weight 400 / line-height 1.00 / letter-spacing -2px — the hero headline
- GeistMono uppercase 14px / letter-spacing 1.4px — buttons, links, and small caps chrome
- 9999px full-pill border-radius on all 13 buttons — every interactive surface is a perfect pill
- Single shadow: `0px 0px 0px 2px rgb(113, 113, 122)` focus ring — that's the entire elevation system
- 1px borders at 10% and 25% white alpha for chrome — `rgba(255, 255, 255, 0.25)` and `rgba(255, 255, 255, 0.1)`
- Seven declared breakpoints from 640px to 2000px — full-fidelity responsive scaffolding
- Aggressive 8px-grid spacing: 4/6/8/16/20/24/32/64/128px — exponential rather than linear
- Submit-a-query-to-Grok button is one of the 9999px pills — the LLM affordance is just another pill
- No chromatic accent. By design.

## 2. Color Palette & Roles

### Primary
- **Pure White** (`#ffffff`): The dominant surface color. 308 occurrences — the most-used color on the page. Used as text on dark surfaces, background on light surfaces, and 1px border color (with alpha) for chrome.
- **xAI Near-Black** (`#1f2228`): The primary brand-anchor color. 302 occurrences. A near-black with a faint cool-blue chroma (`lch(13.16% 4.48 273.6)`) — softer than pure black, slightly cooler than warm. Used as text on light surfaces, fills on dark surfaces, and the page's structural ink.
- **Deep Black** (`#0a0a0a`): A darker variant — 5 occurrences. Used for button text on white pill CTAs, and select inverse moments. Treat as the "true black" anchor when more contrast is needed than `#1f2228` provides.

### Text
- **Pure White** (`#ffffff`): Primary text on dark surfaces.
- **xAI Near-Black** (`#1f2228`): Primary text on light surfaces. The default ink.
- **Mid Gray** (`#7d8187`): Secondary text — 27 occurrences. The single neutral gray, used for de-emphasized metadata, captions, and disabled states. A 53% lightness blue-gray with a faint cool tint matching `#1f2228`'s chroma.
- **Hover Gray** (`rgba(125, 129, 135, 0.2)`): The 20%-alpha variant of mid gray, used for hover veils on chrome.

### Surface
- **Pure White** (`#ffffff`): Light content surface.
- **xAI Near-Black** (`#1f2228`): Dark content surface — the page's hero canvas.
- **Hover Wash** (`rgba(255, 255, 255, 0.8)`): 80%-alpha white veil — used as a hover state on dark surfaces.

### Border System
- **White Chrome Border** (`rgba(255, 255, 255, 0.25)`): 1px solid, 12 occurrences — the workhorse button border on dark surfaces. White at 25% alpha gives the button a subtle outline without shouting.
- **White Hairline** (`rgba(255, 255, 255, 0.1)`): 1px solid, used for card containment and section dividers on dark surfaces.
- **Near-Black Border** (`#1f2228`): `0px 0px 0px 1px` solid, used for left-only chrome borders on light surfaces.

### Status & Highlight
- **No declared status colors.** xAI does not surface error/warning/success colors on the homepage. The system trusts the absence of feedback as part of the minimalism.
- **Focus Ring** (`rgb(113, 113, 122)`): A 2px focus ring shadow — the only declared shadow on the page. A neutral mid-gray with a slight warmth offset from the cool-tinted near-black.

### Gradient System
- **No gradients.** The xAI page is gradient-free. There are no purple-pink gradients, no atmospheric AI-glow halos, no animated radial fills. The system is solid color blocks doing all heavy lifting.
- **No glassmorphism.** No frosted-glass surfaces, no `backdrop-filter` blurs.
- **No glow effects.** No box-shadow halos in chromatic colors.

This monochrome discipline is the brand. Adding any chromatic accent breaks the voice.

## 3. Typography Rules

### Font Family
- **Display / Body**: `universalSans` (Universal Type Foundry — Tobias Frere-Jones, Universal Thirst). Single-weight 400 carries the entire sans system. Fallback: `universalSans Fallback` (a metric-matched fallback typeface).
- **Mono / Chrome**: `GeistMono` (Vercel, open-source). Used for buttons, link chrome, and uppercase small-caps. Fallback chain: `ui-monospace, SFMono-Regular, Roboto Mono, Menlo, Monaco, Liberation Mono, DejaVu Sans Mono, Courier New`.

*Note: Universal Sans requires a foundry license — for external implementations, **Inter** at weight 400/500 with tight tracking is the closest open-source substitute, or **Söhne** for a closer match. **GeistMono** is freely available via Vercel's `geist-font` package or Google Fonts.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Hero Display (XL) | universalSans | 80px (5rem) | 400 | 1.00 | -2px | none | Page-anchor headline — engineering-instrument display |
| Section Display (L) | universalSans | 48px (3rem) | 400 | 1.00 | -1.2px | none | Section heads |
| Section Display (M) | universalSans | 36px (2.25rem) | 400 | 1.11 | -0.9px | none | Sub-section heads |
| Body Large | universalSans | 20px (1.25rem) | 400 | 1.40 | normal | none | Lead paragraphs |
| Body | universalSans | 16px (1rem) | 400 | 1.50 | normal | none | Standard body, link text, button labels |
| Mono Caption / Button | GeistMono | 14px (0.88rem) | 400 | 1.43 | 1.4px | uppercase | Chrome — buttons, link labels, small caps |

### Principles
- **Single weight (400) is the system.** Universal Sans runs at weight 400 across every size from 16px to 80px. There is no bold display moment, no light-weight editorial moment. The single-weight discipline reads as "engineering instrument."
- **Tight tracking on display sizes.** From 36px up, letter-spacing trims to `-0.9px` to `-2px` — the larger the type, the tighter the tracking. This is consistent with grotesk display typography conventions.
- **Mono uppercase as chrome.** GeistMono at 14px / 1.4px tracking / uppercase is the buttons, links, and small-caps voice. The mono family is reserved for chrome — never used for body or display.
- **No italic, no all-caps in display, no decorative weights.** The system has zero flourish. Chrome is uppercase mono; everything else is sentence-case Universal Sans.
- **Line-height 1.00 at hero scale.** The 80px hero stacks tightly with no descender breathing room — a pure architectural display gesture. Below 36px, line-height opens to 1.40–1.50 for readability.
- **Tight character set.** Only the printable ASCII range and a handful of pull-quotes. No fancy OpenType features (small caps, ligatures, swashes).

## 4. Component Stylings

### Buttons

**Primary — Ghost Pill on Dark**
- Background: `rgba(0, 0, 0, 0)` (transparent over dark canvas)
- Text: `#ffffff`, GeistMono 14px weight 400 / 1.4px tracking / UPPERCASE
- Padding: `8px 16px`
- Radius: `9999px` — full pill (the workhorse)
- Border: `1px solid rgba(255, 255, 255, 0.25)`
- Shadow: none at rest
- Outline: `rgb(255, 255, 255) none 3px` (focus)
- Hover: background fills to `hsl(var(--secondary)/.05)` (5% white wash)
- Focus: 2px ring via `0px 0px 0px 2px rgb(113, 113, 122)` shadow
- Use: All primary CTAs on dark surfaces — "Try Grok", "Read the Paper", "Careers"

**Inverse — White Pill**
- Background: `#ffffff`
- Text: `#0a0a0a` (near-black)
- Padding: `4px 12px`
- Radius: `9999px` — full pill
- Border: `1px solid #ffffff`
- Opacity: 0.5 at rest (decorative state, not always interactive)
- Hover: text shifts to `rgba(255, 255, 255, 0.8)` (counterintuitive — white-on-white)
- Use: Compact label pills, status indicators

**Submit-a-Query-to-Grok Pill**
- Same shape as the primary pill — `9999px` radius
- The LLM affordance is just another pill in the system, not a special chrome
- This is the brand statement: "the AI is not special, the design is."

### Cards & Containers

- Background: transparent over `#1f2228` near-black canvas, OR `#ffffff` on inverted sections
- Border: `1px solid rgba(255, 255, 255, 0.1)` on dark; `1px solid #1f2228` on light
- Radius: `24px` (form/textarea), `9999px` (pill chrome), or `0` (sharp section dividers)
- Shadow: none — depth comes from borders and color blocks
- Internal padding: 16–32px standard

### Inputs & Forms

**Text Input / Textarea**
- Background: transparent or `#ffffff`
- Text: `#ffffff` on dark, `#1f2228` on light
- Border: `1px solid rgba(255, 255, 255, 0.25)` on dark, `1px solid #1f2228` on light
- Radius: `24px` — gentle rounded corners, the only non-pill radius in the system
- Padding: 12–16px
- Font: Universal Sans 16px weight 400
- Focus: 2px focus ring shadow `0px 0px 0px 2px rgb(113, 113, 122)`

### Navigation

- Top nav: transparent over `#1f2228` near-black hero, `~64px` tall
- Logo: xAI wordmark in white `#ffffff`, left-aligned
- Nav links: GeistMono 14px / 1.4px tracking / UPPERCASE, white `#ffffff`
- Hover: subtle 5% white background wash, no underline appears
- CTA: ghost pill button with `1px solid rgba(255, 255, 255, 0.25)` border
- Sticky behavior: nav stays fixed on scroll, transparent over hero, may pick up subtle border on light sections
- Mobile: collapses to hamburger drawer with the same pill chrome inside

### Section Borders

- **Top divider** (`1px 0px 0px solid rgb(31, 34, 40)`): used on light surfaces to separate sections
- **Side rails** (`0px 0px 0px 1px solid rgb(31, 34, 40)`): used for left-only chrome borders
- **Vertical hairlines** (`1px 0px solid rgba(255, 255, 255, 0.1)`): used between content modules on dark

### Decorative Elements

**xAI Wordmark**
- "xAI" in white Universal Sans 400, slightly tighter tracking than the body
- Roughly 60–80px wide depending on viewport
- Always on dark surface — the wordmark assumes a near-black canvas

**Submit Button (Grok Query Affordance)**
- Same 9999px pill chrome as every other button
- White background, near-black text, GeistMono uppercase label
- The LLM is just another pill — this is the brand position statement

## 5. Layout Principles

### Spacing System
- Base unit: 8px (the most-used spacing values are 4, 8, 16, 32 — pure 8-grid)
- Scale: 1, 4, 6, 8, 16, 20, 24, 32, 40, 64, 80, 96, 128, 256px
- Notable: the scale is **exponential rather than linear**. Values double aggressively (16 → 32 → 64 → 128 → 256) skipping mid-range steps. This creates a strong sense of architectural rhythm — sections breathe at 64–128px, components breathe at 8–32px.
- Section padding: 64–128px between major panels; 32–64px between subsections
- Component padding: 8–16px standard for buttons, 16–32px for cards

### Grid & Container
- Seven declared breakpoints: 640px, 768px, 1000px, 1024px, 1280px, 1536px, 2000px
- Max content width: estimated 1280–1536px based on the breakpoint cluster
- Hero zones: full-bleed, centered Universal Sans 80px headline
- Content sections: single-column or 2-column, deliberately under-grided
- The page does not use a 12-column grid — it uses a calmer 1–3-column rhythm

### Whitespace Philosophy
- **Architectural breathing room.** Sections breathe with 64–128px of vertical space — the page is calmer than most AI labs by 30–50%
- **No competing modules.** Each section gets its own "room" — there is rarely more than one primary CTA, one headline, and one image per panel
- **Centered composition.** Hero content is consistently centered in the viewport — there is no asymmetric "designed" layout
- **The white space IS the message.** xAI uses absence (of color, of decoration, of competing modules) as the design statement

### Border Radius Scale
- Sharp (`0px`): Default elements, full-bleed sections
- Mid (`24px`): Forms, textareas, inputs (the only "soft" radius in the system)
- Pill (`9999px`): All buttons (13 occurrences on the homepage)

That's it. There is no 4px, 6px, 8px, 12px, or 16px middle-radius. The system has a radius dichotomy: sharp corners or full pills, with one exception for inputs.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Default content surfaces |
| Hairline (Level 1) | `1px solid rgba(255, 255, 255, 0.1)` | Section dividers, card containment on dark |
| Chrome Border (Level 2) | `1px solid rgba(255, 255, 255, 0.25)` | Button and pill containment on dark |
| Focus Ring (Level 3) | `0px 0px 0px 2px rgb(113, 113, 122)` | Keyboard focus on interactive elements |

That is the entire elevation system. Four levels, no drop shadows, no atmospheric blur, no glow halos.

**Shadow Philosophy**: xAI's depth system is **almost entirely absent**. The single declared shadow is the focus ring at `0px 0px 0px 2px rgb(113, 113, 122)` — a 2px neutral-gray ring that announces keyboard focus. There are no drop shadows, no atmospheric blurs, no glows, no Material elevation tiers. Depth comes exclusively from:

1. The contrast between white and `#1f2228` near-black surfaces
2. 1px borders at 10% and 25% alpha
3. The architectural breathing room between sections

This is the most aggressive shadow-restraint in the major-AI-lab cohort. Where Anthropic uses warm ring shadows, where OpenAI uses subtle drop shadows, xAI uses **nothing**. The absence is the brand.

### Decorative Depth
- The 9999px full-pill chrome creates a soft visual rhythm without explicit shadow work
- 1px borders at low alpha (10–25%) replace what would be drop shadows in other systems
- The cool blue chroma in `#1f2228` (vs pure `#000`) gives a subtle atmospheric warmth without using a gradient

## 7. Do's and Don'ts

### Do
- Use `#1f2228` near-black as the dark surface — never pure `#000`. The cool-blue chroma matters
- Use `9999px` border-radius on every button and pill — full-pill is the chrome signature
- Use Universal Sans weight 400 for everything — display, body, UI. Single-weight discipline is the system
- Use GeistMono uppercase 14px with `letter-spacing: 1.4px` for buttons, links, and small caps
- Apply tight letter-spacing (`-0.9px` to `-2px`) on display sizes 36px and above
- Use 1px borders at 10% and 25% white alpha — never solid 1px borders at 100% alpha on dark
- Center hero composition — the page is symmetric, not asymmetric
- Use the focus ring `0px 0px 0px 2px rgb(113, 113, 122)` as the only shadow

### Don't
- Don't introduce ANY chromatic accent color — no purple, no cyan, no warm orange, no green. The monochrome IS the brand
- Don't use pure black `#000` for surfaces — `#1f2228` is the brand near-black
- Don't add drop shadows, glows, or atmospheric blurs — the elevation system is borders only
- Don't bold the type — every weight is 400 in Universal Sans
- Don't use middle-radius values (4px, 8px, 12px, 16px) on chrome — the radius scale is binary (sharp or 9999px pill)
- Don't add gradients, glassmorphism, or backdrop-filter blurs — the system is solid color blocks only
- Don't lowercase the GeistMono chrome — buttons and links are UPPERCASE with 1.4px tracking
- Don't use serif fonts anywhere — the system is sans + mono only
- Don't add hover scales, lifts, or transforms — the only state change is a 5% background wash
- Don't introduce a status color system on the homepage — xAI doesn't surface error/warning/success on landing pages

## 8. Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single-column, hamburger nav, hero scales to ~32px |
| Large Mobile | 640px | 2-column option begins for select modules |
| Tablet | 768px | Condensed nav, 2-col grid, hero ~48px |
| Mid Tablet | 1000–1024px | Full editorial layout, hero scales up |
| Desktop | 1280px | Container caps, max hero ~80px, full pill nav |
| Large Desktop | 1536px | Expanded outer margins |
| Ultra-Wide | 2000px | Page stays centered, outer margins absorb extra width |

The 7-breakpoint scaffolding indicates a system tuned across the standard responsive range, with extreme breakpoints at 2000px for ultra-wide displays.

### Touch Targets
- Pill buttons: ~36–44px tall (GeistMono 14px + 8–12px vertical padding) — at the lower edge of WCAG AAA
- Nav links: ~36–44px tap area through padding
- Submit-a-query-to-Grok pill: 40–48px on touch devices

### Collapsing Strategy
- Nav: full horizontal nav collapses to hamburger drawer on mobile
- Type scale: 80px → 48px → 36px → 20px progressive heading scale
- Section padding: 128px → 64px → 32px as viewport narrows
- Layout: 2-column → 1-column at <768px

### Image Behavior
- Images are sparse on the page — xAI uses minimal photography, leaning on type and chrome
- When images appear, they hold 16:9 or 1:1 aspect with sharp `0px` corners or rare `24px` rounded corners
- No art-direction swaps — the same crop renders at all sizes

## 9. Agent Prompt Guide

### Quick Color Reference
- Surface (Dark): `#1f2228` — xAI Near-Black with cool chroma
- Surface (Light): `#ffffff`
- Inverse Black: `#0a0a0a` — for high-contrast text on white
- Mid Gray: `#7d8187` — secondary text only
- Border (Dark surface): `rgba(255, 255, 255, 0.25)` — buttons; `rgba(255, 255, 255, 0.1)` — sections
- Focus ring: `0px 0px 0px 2px rgb(113, 113, 122)`

### Example Component Prompts

1. *"Create an xAI hero on `#1f2228` near-black: Universal Sans 80px weight 400 headline in `#ffffff`, line-height 1.00, letter-spacing -2px. Centered. Below it, a single ghost pill button — transparent background, 1px solid `rgba(255, 255, 255, 0.25)` border, 9999px radius, 8×16px padding, GeistMono 14px UPPERCASE label with 1.4px tracking."*

2. *"Build a section divider on dark: `1px solid rgba(255, 255, 255, 0.1)` top border, 64–128px vertical padding. Section heading in Universal Sans 36px weight 400 with -0.9px tracking, line-height 1.11. Body text below in 16px Universal Sans weight 400 with 1.50 line-height in `#7d8187` mid gray."*

3. *"Style a primary ghost pill: transparent background, 1px solid `rgba(255, 255, 255, 0.25)` border, 9999px border-radius (full pill), 8×16px padding, GeistMono 14px weight 400 UPPERCASE label with 1.4px letter-spacing. Hover state: `hsl(var(--secondary)/.05)` background wash. Focus state: 2px ring shadow `0px 0px 0px 2px rgb(113, 113, 122)`."*

4. *"Design a Submit-to-Grok input affordance: transparent background, 1px solid `rgba(255, 255, 255, 0.25)` border, 24px border-radius (the only non-pill radius), Universal Sans 16px weight 400 placeholder text in `#7d8187`. Submit button is a 9999px pill with white fill and `#0a0a0a` text in GeistMono 14px UPPERCASE."*

5. *"Build a card on dark: transparent background, 1px solid `rgba(255, 255, 255, 0.1)` border, no border-radius (sharp corners), 32px internal padding. Title in Universal Sans 20px weight 400 in white, body in 16px Universal Sans in `#7d8187` mid gray. No drop shadow."*

### Iteration Guide

1. **Audit color sprawl.** If any chromatic color appears (purple, cyan, blue, orange, green, etc.), remove it. xAI is monochrome by design — the only colors are `#ffffff`, `#1f2228`, `#0a0a0a`, `#7d8187`, and the `rgb(113, 113, 122)` focus ring.
2. **Audit the near-black.** Surfaces should be `#1f2228` (cool-tinted near-black), not pure `#000`. The cool chroma is the brand.
3. **Audit the radius scale.** Buttons must be `9999px` full pills. Inputs are `24px`. Everything else is `0px` sharp. Middle-radius values (4, 6, 8, 12, 16px) break the system.
4. **Audit the type system.** Headlines and body are Universal Sans weight 400. Chrome (buttons, links, small caps) is GeistMono UPPERCASE 14px / 1.4px tracking. If you see Inter, Helvetica Neue, or any other typeface, replace it.
5. **Audit the weight.** Universal Sans runs at weight 400 only. If you see weight 500, 600, or 700 anywhere in the type system, correct to 400.
6. **Audit shadow weight.** The only declared shadow is the 2px focus ring. If you see drop shadows, atmospheric blurs, glows, or Material-style elevation, remove them all.
7. **Audit display tracking.** Headlines 36px and above need negative letter-spacing (-0.9 to -2px). Default tracking on a 80px hero breaks the architectural feel.
8. **Audit the chrome casing.** Buttons, link labels, and small caps are UPPERCASE GeistMono with 1.4px tracking. If you see lowercase or sentence-case chrome, correct it.
9. **Audit the centeredness.** xAI hero composition is symmetric and centered. If the hero is left-aligned or asymmetric, it has tipped away from the brand.
10. **When in doubt, ask: "what would a terminal designer do?"** The page is a monospace terminal that took two weeks of UI design lessons. If the answer is "add a color," the answer is wrong.
