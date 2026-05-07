---
version: alpha
name: "Bear"
description: "Token-first design system reference for Bear."

colors:
  background: "#ffffff"
  surface: "#dd4c4f"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#888888"
  primary: "#ffffff"
  on-primary: "#ffffff"
  border: "#444444"
  focus-ring: "#ffffff"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 51px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  4xl: 96px

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 16px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.background}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    borderColor: "{colors.focus-ring}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  badge:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
---

# Bear Design System

## Overview

Bear's website is the inverse of every productivity-app marketing page on the internet. Where the category leans on dashboards, dark UI, and "powerful for teams" tropes, Bear leans on a hand-drawn polar bear, paper-soft pastel washes, and a custom typeface that reads more like a calligrapher's signage than a SaaS sans. The page sits on a near-pure white canvas (`#ffffff`) and stages every section as a calm composition: a product screenshot, an unhurried headline in `bearsansheadline`, a paragraph of grey body copy, and one of Bear's signature soft cloud-shaped color washes drifting behind the content. The whole site reads as a notebook left open on a clean wooden desk.

The defining element of Bear's identity is its **custom type pairing**. `bearsansheadline` (the display face) carries hand-cut, calligraphic personality — wider apertures, gentle stroke modulation, the kind of letterforms you'd expect on the cover of a journal. `bearsans` (the body face) is its quieter sibling, optimized for reading. Bear ships the same fonts you read your notes in across the marketing site, plus a hand-drawn illustration system: a red bear cub logo, a panda in pricing, a polar bear in the FAQ hero, sparkles in negative space — all in loose calligraphy-pen line weight. Pair this with soft pastel cloud washes (mint, lavender, lemon, peach, pink) and you get the rare productivity site that feels handmade rather than engineered.

**Key Characteristics:**
- Custom `bearsansheadline` and `bearsans` typefaces — the brand's voice carried by the typeface itself
- Bright Bear Red (`#dd4c4f`) as the only chromatic CTA color — applied to download buttons, key links, the bear's hat
- Pure white canvas (`#ffffff`) with soft pastel cloud washes layered behind feature sections
- Hand-drawn illustrations in calligraphy-pen line weight — bear, panda, polar bear, sparkles, stars
- Generous neutral grey palette (`#444444` body text, `#888888` captions, `#f3f5f7` panels) — never harsh
- 16px and 40px corner radii — soft, friendly, never sharp-mechanical
- Centered editorial layout — content hugs the middle, cloud washes drift to the edges
- Single soft drop shadow (`rgba(0,0,0,0.12) 0px 13px 34px`) for floating product mockups

## Colors

### Primary
- **Bear Red** (`#dd4c4f`): The signature accent — applied to the App Store button, all primary CTAs, key in-content links, and tints of the bear logo. The only saturated chromatic color in the system.
- **Bear White** (`#ffffff`): The page canvas. Pure white, not warm — Bear leans on the white for a clean-paper feeling rather than warming it.
- **Bear Ink** (`#444444`): All primary text — headings, body paragraphs, nav links. A soft warm grey-black that reads less aggressive than pure `#000`.

### Brand Accent
- **Bear Red** (`#dd4c4f`): Reserved for primary CTAs ("Get Started"), inline links inside content blocks ("What's New in Bear 2", "Markdown", "Bear Pro"), and the red hat on the bear logo. Approximately one or two applications per screen.
- **Pro Gold** (`#fcb827`): Used exclusively for the "Pro" badge on premium feature mentions — a saturated yellow-gold pill marking Bear Pro features.
- **Info Blue** (`#44a2e5`): A secondary badge color used for "New" markers and supplementary in-content tags. Used very sparingly.

### Neutrals & Text
- **Bear Ink** (`#444444`): Primary text — headings, body, links by default
- **Bear Caption Grey** (`#888888`): Secondary text — captions, metadata, subtle UI labels
- **Bear Border Grey** (`#d9d9d9`): Input borders and the lightest divider lines
- **Bear Panel Grey** (`#f3f5f7`): Soft tinted panels for feature containers and the FAQ docs cards

### Pastel Cloud Washes
The signature atmospheric system. Bear uses oversized soft-edged blob shapes in low-saturation pastel colors, layered behind feature sections to give each section its own mood without hard borders or framed cards. Each wash is ~20–30% saturation, applied as a freeform organic shape.
- **Cloud Lavender** (`#e6dcf2`): "Seamless Markdown" section
- **Cloud Mint** (`#d8ecdf`): "Organize easily"
- **Cloud Lemon** (`#f6ecbb`): "Universal beauty"
- **Cloud Peach** (`#fadfc8`): Pricing section
- **Cloud Pink** (`#f5dde0`): "Privacy" section

### Surface & Borders
- **Surface White** (`#ffffff`): Default page and card background
- **Surface Panel** (`#f3f5f7`): Tinted soft-grey panels for FAQ content cards and nested containers
- **Border Grey** (`1px solid #d9d9d9`): The only visible border in the system — used on form inputs
- **Underline Ink** (`0px 0px 1px solid #444444`): A subtle 1px underline on `<a>` and `<li>` elements — Bear's hover/affordance signal

### Shadows
- **Float Shadow** (`rgba(0, 0, 0, 0.12) 0px 13px 34px 0px`): The system's only meaningful drop shadow. Soft, large blur, used to lift product screenshots and mockups off the page. No second shadow tier — Bear is mostly flat.

### Gradient System
- Bear is **gradient-free** in the literal sense. The pastel cloud washes are solid-color organic shapes, not linear or radial gradients. The system relies on solid color, soft edges, and atmospheric layering rather than gradient transitions.

## Typography

### Font Family
- **Display**: `bearsansheadline` — custom calligraphic display face, used exclusively for headings
- **Body**: `bearsans` — custom sans-serif, used for everything from nav links to captions
- **Fallbacks**: `-apple-system`, `BlinkMacSystemFont`, `Helvetica Neue`, sans-serif
- **OpenType Features**: Standard ligatures only

*Note: `bearsansheadline` and `bearsans` are proprietary typefaces shipped by Shiny Frog. For external implementations, Söhne or Recoleta (display) and Inter or Sohne (body) are reasonable substitutes; for the calligraphic feel, Authentic Sans or Domaine Sans Display work as approximations.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Notes |
|------|------|------|--------|-------------|-------|
| Display Hero | bearsansheadline | 51.2px (3.20rem) | 400 | 1.10 | Top of homepage / FAQ — "Markdown notes you'll love" |
| Display Large | bearsansheadline | 41.6px (2.60rem) | 400 | 1.10 | Major section titles |
| Display Mid | bearsans | 40px (2.50rem) | 400 | 0.68 | Section markers — unusually tight leading |
| Section Heading | bearsansheadline | 30.4px (1.90rem) | 400 | 1.10 | Sub-section heads |
| Sub-heading Bold | bearsans | 28.8px (1.80rem) | 700 | 1.40 | Feature sub-titles in bold |
| Sub-heading | bearsans | 24px (1.50rem) | 400 | 1.13 | Card titles, callouts |
| Nav Link | bearsans | 22.4px (1.40rem) | 500 | 1.21 | Top navigation links — slightly heavier than body |
| Body Large | bearsans | 22.4px (1.40rem) | 400 | 1.40 | Lead paragraphs |
| Sub-heading Small | bearsans | 20px (1.25rem) | 400 | 1.36 | Smaller section labels |
| Body | bearsans | 19.2px (1.20rem) | 400 | 1.42 | Standard reading text |
| Body Bold | bearsans | 17.6px (1.10rem) | 700 | 1.45 | Inline emphasis in body copy |
| UI Body | bearsans | 16px (1.00rem) | 400 | 1.70 | Relaxed body, button text, in-component copy |
| UI Bold | bearsans | 16px (1.00rem) | 700 | 1.40 | Button labels, badges (gold/blue) |
| Small Body | bearsans | 14.4px (0.90rem) | 400 | 1.89 | Footer text, fine print — extra-relaxed leading |
| Caption | bearsans | 12.8px (0.80rem) | 700 | 1.40 | Bold captions, small badges |

### Principles
- **Calligraphy headline, neutral body**: Headlines run in `bearsansheadline` weight 400 — the typeface's character does the work, no bold display needed. Body switches to `bearsans` at the same neutral weight.
- **Weight 400 is the workhorse**: Bear avoids weight 300 entirely and reserves weight 700 for inline emphasis, button labels, and bold callouts. Weight 500 only for nav links.
- **Body breathes, display doesn't**: Body copy at `1.40–1.70` line-height for a paper-novel reading feel. Headlines at `1.10` to keep multi-line display compact.
- **No letter-spacing, no uppercase**: Custom typefaces tuned at native spacing — no tracking adjustments. Sentence case throughout, including buttons. Bear never shouts.

## Layout

### Spacing System
- Base unit: 8px
- Scale: 4.8px, 6.4px, 8px, 11.2px, 12.8px, 16px, 19.2px, 26.88px, 32px, 40px, 41.6px, 44.8px, 48px, 64px, 80px, 96px, 160px
- Notable: A non-rigid scale — Bear uses 12.8px (0.80rem) and 19.2px (1.20rem) heavily as sub-unit spacers, breaking from a strict 8-multiple grid. The custom typefaces and rem-based math drive this looser feel.

### Grid & Container
- Max content width: approximately 1024–1180px for centered text content
- Hero: centered single-column with display headline, sub-paragraph, app store button stack
- Feature sections: alternating left/right two-column (illustration/screenshot one side, text the other) over a pastel cloud wash background
- Pricing: centered two-tier comparison ("Free" / "Pro")
- FAQ: centered hero with search bar, then a soft-panel card grid for documentation categories

### Whitespace Philosophy
- **Editorial pacing**: Each section gets 80–160px of vertical air — Bear breathes
- **Centered rhythm**: Most content is center-aligned within ~700px of the viewport center, with cloud washes drifting outward to the page edges. This gives the site a "calm centered focal point" feel rather than a wide-grid feel.
- **Generous footers**: Footer area gets significant vertical air with the Bear newsletter and community CTA — the page ends gently, not abruptly

### Border Radius Scale
- 3.84–4.8px: Tight badges and inline tags — almost-square corners
- 8px: Buttons (App Store, Get Started)
- 8.8px: Text inputs
- 16px: Image crops, floating product mockup containers
- 40px: Soft-panel cards (FAQ docs cards) — generously rounded for that "pillow" feel
- No sharp 0px radii: Bear does not use sharp rectangular corners anywhere — softness is structural

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, inline content, structural sections |
| Atmospheric Wash (Level 1) | Pastel cloud blob behind content | Feature sections — provides "soft elevation" through color rather than shadow |
| Soft Panel (Level 2) | `#f3f5f7` background, `40px` radius | FAQ docs cards, pricing tier containers |
| Float Shadow (Level 3) | `rgba(0, 0, 0, 0.12) 0px 13px 34px 0px` | Product screenshots, app mockups — the only literal drop shadow |
| Underline Affordance | `1px solid #444444` under links | Inline link affordance — Bear's "this is interactive" signal |

**Shadow Philosophy**: Bear's depth system is atmospheric. Where most apps use multi-tier elevation shadows to imply 3D layering, Bear has effectively one drop shadow — a soft 34px-blur shadow used to lift product screenshots off the page. Everything else relies on color washes (pastel clouds), tinted panels (`#f3f5f7`), and underlines for affordance. A hand-drawn notebook doesn't have rendered 3D depth — it has watercolor washes and pencil shading. The pastel cloud wash IS the elevation system; soft panels at `40px` radius create the only literal "card" enclosure; the `0 13px 34px` shadow under product mockups is the lone literal shadow tier.

## Shapes

The complete radius scale is declared in the `rounded:` token block above.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Hard-edged brand moments and flush layouts |
| `sm` | 4px | Small controls and tight UI details |
| `md` | 8px | Inputs and compact interface elements |
| `lg` | 16px | Cards and larger containers |
| `pill` | 9999px | CTAs, chips, and rounded badges |

## Components

### Buttons

**Primary Red CTA**
- Background: Bear Red (`#dd4c4f`)
- Text: Bear White (`#ffffff`)
- Padding: 8px 24px
- Radius: `8px`
- Border: `0px none`
- Shadow: `none`
- Font: `bearsans` 16px weight 400
- Hover: subtle darkening (no color shift recorded)
- Use: Primary CTA — "Get Started", "Subscribe", "Get the App"

**App Store / Mac App Store Button**
- A black-pill rectangle with white text and inline Apple/Mac App Store glyph
- Radius: `8px`
- Padding: ~10px 20px
- Lives at the top of the homepage hero — Bear leads with the app store, not a marketing form

**Outline Link Button**
- Background: transparent (`#ffffff` on light, no fill)
- Text: Bear Red (`#dd4c4f`) for primary, Bear Ink (`#444444`) for neutral
- Border: typically borderless — relies on the 1px text underline (`0px 0px 1px solid #444444`) under hyperlinked words
- Use: Inline links in body copy, "What's New", "Markdown", "Bear Pro"

### Cards & Containers

**Floating Product Mockup**
- Background: transparent or product screenshot bleed
- Radius: `16px` on rounded image crops
- Shadow: `rgba(0, 0, 0, 0.12) 0px 13px 34px 0px` — single soft float shadow
- Use: Lifting product screenshots, app window mockups, illustration cards above the page surface

**Soft Panel Card** (FAQ "Get Started" card, pricing tier cards)
- Background: Surface Panel (`#f3f5f7`)
- Radius: `40px` — generously rounded, almost stadium-soft
- Border: `0px`
- Padding: 32–48px internal
- Use: Containing sections of grouped content, especially in the FAQ docs hero

**Feature Section Container**
- Background: `#ffffff` with a freeform pastel cloud wash floating behind
- Radius: `0` for the container itself; the visual rounding comes from the wash
- Padding: 80px+ vertical to give cloud washes room to breathe
- Use: Each major homepage feature pitch ("Seamless Markdown", "Organize easily", "Universal beauty")

### Badges / Tags / Pills

**Pro Gold Badge**
- Background: Pro Gold (`#fcb827`)
- Text: White (`#ffffff`)
- Padding: 0 4.8px
- Radius: `4.8px` (soft-rectangle, not pill)
- Font: `bearsans` 16px weight 700
- Line-height: 22.4px (boxed appearance)
- Use: Marking Bear Pro features inline with body copy

**Red Inline Badge**
- Background: Bear Red (`#dd4c4f`)
- Text: White (`#ffffff`)
- Padding: 0 3.84px
- Radius: `3.84px`
- Font: `bearsans` 12.8px weight 700
- Line-height: 17.92px
- Use: Compact inline tags, version markers

**Info Blue Badge**
- Background: Info Blue (`#44a2e5`)
- Text: White (`#ffffff`)
- Padding: 0 4.8px
- Radius: `4.8px`
- Font: `bearsans` 16px weight 700
- Use: "New" markers, supplementary indicators

### Inputs & Forms

**Text Input (Newsletter / Email)**
- Background: Bear White (`#ffffff`)
- Border: `1px solid #d9d9d9`
- Radius: `8.8px`
- Padding: 0 17.6px (vertical alignment via line-height)
- Font: `bearsans` 16px weight 400
- Text color: Bear Ink (`#444444`)
- Outline (focus): Bear Ink (`#444444`) — system focus ring, no custom focus styling
- Use: Newsletter signup, FAQ search bar

### Navigation
- Top nav: horizontal white bar, left-aligned bear logo + "Bear" wordmark, right-aligned text links (Features, Pricing, Blog, Community, Support)
- Links: `bearsans` 22.4px weight 500, color Bear Ink (`#444444`)
- Hover: color resolves to `var(--text-color)` — i.e. no visible color shift, the underline is the affordance
- No mega-menu or dropdown panels — Bear's nav is flat and plain
- Sticky behavior: standard scroll, no fixed-on-scroll pinning

### Decorative Elements

**Hand-Drawn Illustrations**: Polar bear (FAQ hero), red bear with hat (logo), panda (pricing), sketches of paper, mountains, plants. Loose calligraphy-pen line weight, mostly black-on-white with occasional red accents. Always at 200–400px canvas — section-level imagery, never small-icon decoration.

**Sparkle / Star Punctuation**: Four-point sparkles and asterisk-like stars scatter across hero negative space. Light grey at low opacity — quiet ambient texture, drawn in the same pen-line weight as the illustrations.

**Pastel Cloud Wash**: Large freeform blob shapes in pastel sitting behind feature content blocks, softly tinting the section. Hard edges never used; clouds feather to the page edge or fade at the boundary.

## Do's and Don'ts

### Do
- Use `bearsansheadline` weight 400 for every display and heading size — let the typeface character carry the brand
- Use `bearsans` for body, nav, captions — at weight 400 with weight 500 for nav and weight 700 for inline emphasis only
- Apply Bear Red (`#dd4c4f`) sparingly — primary CTA, key inline links, the bear's hat — never as a panel fill
- Use pastel cloud washes (lavender, mint, lemon, peach, pink) as soft section backgrounds — one per section maximum
- Keep corner radii in the soft range — `8px` for buttons, `16px` for images, `40px` for soft panels
- Lean on hand-drawn illustrations at large display size — bear, panda, polar bear, sketches — never small-icon style
- Use the underline on links (`1px solid #444444`) as the primary affordance — color shift is secondary
- Center content within 700–1024px of the viewport — let cloud washes drift to the edges
- Use the single `0 13px 34px rgba(0,0,0,0.12)` shadow only for floating product mockups
- Use sentence case for everything — buttons, headings, body — Bear never shouts

### Don't
- Don't use sharp `0px` corners — Bear's identity is soft-rounded, not mechanical
- Don't introduce a second drop shadow tier — depth is atmospheric (cloud washes), not stacked
- Don't use uppercase or letter-spacing tracking — the custom typefaces are tuned at native spacing
- Don't use weight 300 (thin) or weight 800+ — Bear lives at weight 400/500/700 only
- Don't apply the red accent broadly — never as a panel fill, never for body emphasis, never as the brand color stamp
- Don't replace the hand-drawn illustrations with stock icons or vector iconography — the pen-line weight is the brand
- Don't introduce hard borders or framed cards — sections separate via cloud washes and breathing room, not lines
- Don't use pure black (`#000000`) for body text — Bear Ink (`#444444`) is the warmer, gentler default
- Don't use linear gradients — pastel washes are solid organic shapes, never gradient-rendered
- Don't crowd the layout — Bear's editorial rhythm needs 80–160px of vertical air per section

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero drops to ~32–36px |
| Mobile | 375–650px | Single-column, 36–41.6px hero, stacked CTAs |
| Tablet | 650–1000px | 2-column begins for feature pairs, 41.6–48px hero |
| Desktop | 1000–1269px | Full alternating 2-column layout, 51.2px hero |
| Large Desktop | ≥1269px | Maximum scale (51.2px hero), centered ~1180px container |

### Touch Targets
- Primary CTA (App Store button, "Get Started"): min 44px tap height with 24px horizontal padding on mobile
- Nav links: 22.4px text with generous tap padding
- FAQ search bar: full-width on mobile, ~600px on desktop

### Collapsing Strategy
- **Nav**: Horizontal links collapse to hamburger on mobile
- **Hero**: 51.2px → 41.6px → 30.4px progressive scaling, weight 400 maintained
- **Feature pairs**: Two-column illustration/text pairs stack with the illustration above the text
- **Cloud washes**: Freeform pastels scale and reflow — no art-direction swap
- **Pricing**: Side-by-side tiers stack vertically on mobile
- **Section spacing**: 160px+ desktop → 64–80px mobile

### Image Behavior
Hand-drawn illustrations maintain their full character at all sizes — never replaced with simplified icons. Product screenshots keep the floating shadow but reorder above the text on mobile. The atmospheric language adapts rather than swaps.

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Bear Red (`#dd4c4f`)
- Page Background: Bear White (`#ffffff`)
- Primary Text: Bear Ink (`#444444`)
- Secondary Text: Bear Caption Grey (`#888888`)
- Soft Panel: Surface Panel (`#f3f5f7`)
- Pro Badge: Pro Gold (`#fcb827`)
- Info Badge: Info Blue (`#44a2e5`)
- Input Border: Border Grey (`#d9d9d9`)
- Float Shadow: `rgba(0, 0, 0, 0.12) 0px 13px 34px 0px`
- Cloud Washes: Lavender (`#e6dcf2`), Mint (`#d8ecdf`), Lemon (`#f6ecbb`), Peach (`#fadfc8`), Pink (`#f5dde0`)

### Example Component Prompts
- "Create a hero section on `#ffffff` with a centered headline at 51.2px `bearsansheadline` weight 400, line-height 1.10, color `#444444`. Pair with a 22.4px `bearsans` weight 400 sub-paragraph in `#444444`. Place a Bear Red (`#dd4c4f`) primary CTA button below — 16px text, weight 400, `8px` radius, padding 8px 24px."
- "Design a feature section with a pastel mint cloud wash (`#d8ecdf`) drifting behind a centered illustration. Heading at 30.4px `bearsansheadline` weight 400, line-height 1.10, color `#444444`. Body in `bearsans` 19.2px weight 400, line-height 1.42, color `#444444`."
- "Build a soft panel card with `#f3f5f7` background and `40px` border radius. Title in `bearsansheadline` 28.8px weight 700, body links in Bear Red (`#dd4c4f`) `bearsans` 19.2px weight 400 with no underline."
- "Create a Pro Gold badge — `#fcb827` background, white text, 16px `bearsans` weight 700, padding 0 4.8px, radius `4.8px`, line-height 22.4px. Inline with body copy."
- "Float a product screenshot using `0 13px 34px rgba(0,0,0,0.12)` drop shadow with `16px` border radius. Center in viewport with no border or frame."
- "Design a newsletter input — `#ffffff` background, `1px solid #d9d9d9` border, `8.8px` radius, padding 0 17.6px, `bearsans` 16px weight 400, color `#444444`. Pair with a Bear Red (`#dd4c4f`) submit button at `8px` radius."

### Iteration Guide
1. Default to `bearsansheadline` weight 400 for all display sizes — never reach for bold display, the typeface character is the brand
2. Body always runs in `bearsans` weight 400 — weight 500 for nav, weight 700 for inline emphasis only
3. Bear Red (`#dd4c4f`) is sacred — primary CTA, key inline links, the bear's hat. One or two applications per screen.
4. Corner radius is soft, never sharp: `8px` buttons, `16px` images, `40px` soft panels. Zero `0px` radii.
5. Use one pastel cloud wash per feature section — lavender, mint, lemon, peach, or pink at low saturation
6. Hand-drawn illustrations always sit at large display size — never use them as small-icon decoration
7. The single soft drop shadow (`0 13px 34px rgba(0,0,0,0.12)`) is reserved for floating product mockups
8. Body text is `#444444`, not `#000000` — Bear is gentle, not harsh
9. Sentence case everywhere — buttons, headings, badges. Bear never shouts.
10. Center content; let pastel cloud washes drift to the page edges. The composition breathes from the middle.
