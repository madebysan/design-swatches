---
version: alpha
name: "Ramp"
description: "Lausanne with ss01 stylistic set, signature Ramp Yellow CTA on near-black product chrome, 6px button radius."

colors:
  background: "#ffffff"
  surface: "#f4f2f0"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#f7fafc"
  primary: "#f0e84a"
  on-primary: "#ffffff"
  border: "#212121"
  focus-ring: "#f0e84a"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "lausanne, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "lausanne, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "lausanne, ui-sans-serif, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "lausanne, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "lausanne, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "lausanne, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "lausanne, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "lausanne, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
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

# Ramp Design System

## Overview

Ramp's website is what happens when a fintech company hires a type foundry instead of an agency. The page sits on a clean cream-white canvas (`#ffffff` with a soft `#f4f2f0` secondary surface) and commits to a single typeface — `lausanne` from Type Cartel — set with the OpenType `ss01` stylistic set enabled globally. Every headline, every body line, every button label runs through the same variable face with the same alternate glyphs, producing the most consistent typographic surface in fintech. Where Stripe whispers in violet weight-300 and Mercury floats on muted neutrals, Ramp commits to one bright chromatic gesture: **Ramp Yellow** (`#f0e84a`), a saturated chartreuse-leaning yellow that lives on the primary CTA and nowhere else. The contrast is institutional confidence with a single pop of acid.

The defining typographic move is `lausanne` at weight 400 across the entire scale — no light display weights, no extra-bold heads, no italic. The page achieves hierarchy through size and line-height alone: 48px display at `1.04` line-height with negative `-0.01px` tracking compresses headlines into dense graphic blocks, while body at 16px / 1.50 stays generous and readable. The `ss01` stylistic set modifies specific glyph forms (likely alternate `a`, `g`, `t`) to give the face a more geometric, contemporary feel — and that single OpenType setting is the brand's typographic DNA. Disable it, and the personality flattens immediately.

What separates Ramp from every other fintech site is the **product-first chrome**. Headlines never compete with the dashboard screenshots. Cards are 12px-radius white panels with single-pixel hairline borders in lab-color-space neutrals (`lab(91.62 -0.16 -2.27)`, an almost imperceptible cool grey). Shadows are minimal — Ramp's hover state on cards is a soft `rgba(17, 17, 17, 0.173) 0px 0px 30px` ambient glow rather than the drop-shadow stack other fintechs lean on. The yellow CTA is the only saturated colour in the system, which means every "Get Started" button on every page reads as the signal — there's nothing competing with it for chromatic attention.

**Key Characteristics:**
- `lausanne` typeface globally with OpenType `ss01` stylistic set on every text element — the brand's typographic signature
- Weight 400 across the entire scale — display, body, buttons, captions all share one weight
- Negative letter-spacing on display sizes: `-0.01px` at 48px, `-0.005px` at 40px (subtle but consistent)
- Ramp Yellow CTA (`#f0e84a`) — the single saturated chromatic note in the system
- Cream-white canvas (`#ffffff`) with `#f4f2f0` secondary surface for alternating panels
- 6px button radius, 12px card radius, 16px feature card radius — conservative rounding scale
- Hairline borders in lab-space neutrals (`lab(91.62 -0.16 -2.27)`, `lab(83.02 1.03 2.02)`) — barely-there structure
- Soft ambient hover shadow (`rgba(17, 17, 17, 0.173) 0px 0px 30px`) — atmospheric, not architectural
- Inputs use 10px radius and bottom-padded layouts for prominent email-capture moments
- Tailwind + Radix UI + shadcn/ui as the underlying technical foundation — modern primitive-driven build

## Colors

### Primary Brand
- **Ramp Yellow** (`#f0e84a`): The signature CTA fill — a saturated chartreuse-yellow extracted from `lab(92.1406 -20.4979 84.7726)`. Lives on the primary "Get Started" button and nowhere else. The single chromatic gesture in the entire system.
- **Ramp Black** (`#212121`): Primary text colour — extracted from `lab(2.84 0.37 0.97)` and the `--color-black-500` variable's underlying tone. Not pure black; a near-black with a slight neutral undertone.
- **Pure White** (`#ffffff`): Page background, card surface, button text on dark sections.

### Brand Neutral
- **Cream Surface** (`#f4f2f0`): Secondary surface tint — used for feature card backgrounds and alternate panels. Half-step warmer than the canvas.
- **Soft Cream** (`#f7fafc`): Cookie/overlay surface — the lightest cool neutral in the system.
- **Body Slate** (`#4a5568`): Secondary text colour — captions, muted body, footer copy.
- **Label Slate** (`#2d3748`): Form labels and inline navigation links — a deeper slate than body for structural emphasis.
- **Hairline Mid** (`#e2e8f0`): Default divider colour for soft separators.
- **Hairline Cool** (`#e1e7ee`): Disabled-state and inactive surface tint.

### Border Colors (lab-space)
- **Card Border Cool** (`lab(91.62 -0.16 -2.27)` ≈ `#e8eaeb`): The most-used border colour (34 instances) — barely-perceptible cool grey on card edges.
- **Card Border Warm** (`lab(83.02 1.03 2.02)` ≈ `#cfcdcb`): Secondary border colour (34 instances) — slightly warmer for tinted-panel cards.
- **Black 10%** (`rgba(33, 33, 33, 0.1)`): Subtle low-opacity border for dividers and inline rules.

### Status & Functional
- **Success Green** (`#38a169`): GPC-applied indicator, confirmation states.
- **Error Red** (`#e53e3e`): Error states, GPC-overridden alerts.
- **Error Surface** (`#f7c2c2`): Light error background tint.
- **Disabled Border** (`#a0aec0`): Disabled secondary button border.
- **Row Hover** (`#edf2f7`): Table-row hover background.
- **Badge Background** (`#718096`): Generic neutral badge fill.

### Inverse Surfaces
- **Inverse Black** (`#2b2e35`): Dark CTA button background on light sections (used for "Sign In", "Demo", secondary CTAs that aren't yellow).
- **Inverse Hover** (`#4f525b`): Hover state for the inverse-black button.

### Gradient System
- Ramp's published surfaces are **gradient-restrained** in core chrome. Brand gradients (the indigo→magenta atmospheric heroes from prior iterations) appear in select hero photography but never on buttons, cards, or structural surfaces. Every CTA is a flat saturated yellow; every card is a flat white or cream with a hairline border. The page achieves richness through typography and product photography, not through coloured chrome.

## Typography

### Font Family
- **Primary**: `lausanne` from Type Cartel, fallback `lausanne Fallback`. A geometric grotesk variable font with extensive OpenType alternate glyph support.
- **OpenType Features**: `"ss01"` enabled globally on all text — this is Ramp's typographic DNA. Disabling it changes the brand voice.
- **Icon System**: `Material Icons Outlined` and `Material Icons` for inline UI glyphs — only place a non-`lausanne` typeface appears.

*Note: `lausanne` is a commercial typeface from Type Cartel. For external implementations, `Inter` at weight 400–500 with custom letter-spacing serves as the closest free substitute; `söhne` from Klim Type Foundry is a closer paid alternative. The `ss01` stylistic set's exact glyph modifications are font-specific — when substituting, accept that the alternate-glyph signature will not transfer.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Features | Notes |
|------|------|------|--------|-------------|----------------|----------|-------|
| Display Hero | lausanne | 48px (3.00rem) | 400 | 1.04 | -0.01px | ss01 | Maximum size — homepage hero, feature heroes |
| Display Large | lausanne | 40px (2.50rem) | 400 | 1.05 | -0.005px | ss01 | Section heroes, page-front headlines |
| Section Heading | lausanne | 28px (1.75rem) | 400 | 1.14 | normal | ss01 | Feature section titles |
| Sub-Heading | lausanne | 24px (1.50rem) | 400 | 1.17 | normal | ss01 | Card heads, sub-section openers |
| Card Heading | lausanne | 20px (1.25rem) | 400 | 1.30 | normal | ss01 | Smaller card titles, feature blocks |
| Body / Standard | lausanne | 16px (1.00rem) | 400 | 1.50 | normal | ss01 | Default reading copy, body text |
| Link / Button Body | lausanne | 16px (1.00rem) | 400 | 1.50 | normal | ss01 | Primary CTAs, inline navigation |
| Button Compact | lausanne | 14px (0.88rem) | 500 | 1.00 | normal | ss01 | Secondary / compact buttons |
| Body Small | lausanne | 14px (0.88rem) | 400 | 1.43 | normal | ss01 | Footer body, secondary descriptions |
| Caption | lausanne | 13px (0.81rem) | 400 | 1.46 | normal | ss01 | Image captions, table cells |
| Tabular Caption | lausanne | 12px (0.75rem) | 400 | 1.00 | normal | ss01 | Material icons inline labels |
| Eyebrow / Micro Label | lausanne | 10px (0.63rem) | 400 | 1.50–2.20 | 0.18–0.5px | ss01, uppercase | Section eyebrows, category markers |

### Principles
- **One typeface, one weight**: lausanne at weight 400 carries 95% of the system. Weight 500 appears only on compact buttons and inline links. There is no bold (700) anywhere — hierarchy is achieved through size and line-height.
- **`ss01` is non-negotiable**: The stylistic set is enabled on every text element. It modifies specific glyphs to a more geometric, contemporary feel — and the brand voice depends on it.
- **Negative letter-spacing on display only**: -0.01px at 48px, -0.005px at 40px. Subtle but consistent — body and small text use default tracking.
- **Tight display line-height**: 48px headlines run at `1.04`, 40px at `1.05`. Display blocks are vertically compressed graphic units, not paragraphs.
- **Generous body line-height**: 16px body at `1.50` line-height is generous and readable. The contrast with tight display is the rhythm.
- **UPPERCASE for eyebrows only**: 10px micro labels use `uppercase` with `0.18–0.5px` letter-spacing. Buttons and headlines stay sentence case.

## Layout

### Spacing System
- Base unit: 4px (with strong reliance on 8 and 24)
- Scale: `1px, 4px, 6px, 8px, 10px, 12px, 16px, 20px, 24px, 32px, 40px, 48px, 56px, 64px, 128px`
- Notable: `8px` is the dominant value (216 instances), with `4px` (71), `20px` (71), and `24px` (69) carrying the rest. `128px` (9 uses) handles section-level breaks. The scale is dense at the small end (4–12px every 2px) for tight chrome and skips to 32–128px for section spacing.

### Grid & Container
- Max content width: ~`1280px` for centred content with full-bleed sections extending beyond
- Hero: centered single-column with generous padding, lightweight headlines paired with product screenshot cards
- Feature sections: 2–3 column grids for feature cards; 4-column on customer-logo strips
- Tailwind + Radix UI + shadcn/ui is the underlying stack — utility classes drive most spacing and layout

### Whitespace Philosophy
- **Product-first composition**: Layout subordinates to product photography. Cards are containers for dashboard screenshots, not standalone graphic objects.
- **Section rhythm via surface alternation**: White panels alternate with cream (`#f4f2f0`) panels — never a true dark-section break, the brand stays in the cream-white range with the yellow CTA as the only chromatic punctuation.
- **Generous card padding**: `24px–32px` internal padding around card content. Ramp uses negative space to make dashboard screenshots feel premium.

### Border Radius Scale
- Tight (`4px`): Badges, neutral pills, secondary tag chips
- Standard (`6px`): Buttons, compact UI elements — the workhorse interactive radius
- Card (`8px`): Default card containers
- Input (`10px`): Email inputs, slightly more rounded than buttons for tactile distinction
- Feature (`12px`): Feature tiles, customer-story cards, video frames
- Hero (`16px`): Hero feature cards, large feature panels
- Pill (effectively `infinity`): One-off micro-pills (`3.36e+07px`) for tag chips

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, card defaults, inline content |
| Inset Glow (Level 1) | `rgba(255, 255, 255, 0.6) 0px 0px 2px 0px inset` | Ghost buttons — subtle inner highlight |
| Hairline (Level 2) | `1px solid lab(...)` border | Card edges, section dividers |
| Ambient Glow (Level 3) | `rgba(17, 17, 17, 0.173) 0px 0px 30px` | Card hover state — atmospheric outward glow |
| Soft Drop (Level 4) | `rgba(0, 0, 0, 0.04) 0px 1px 4px 0px` | Floating elements, subtle elevated surfaces |
| Focus Ring (Level 5) | `rgba(0, 0, 0, 0.1) 0px 4px 12px, rgba(0, 0, 0, 0.2) 0px 0px 0px 2px` | Keyboard focus on inputs and CTAs |

**Shadow Philosophy**: Ramp's depth language is restrained and atmospheric. Where Stripe layers blue-tinted multi-shadows for premium gravity and Lego stacks hard-offset brick-press shadows for tactility, Ramp uses **single-direction ambient glows** that radiate outward without offset. The signature card-hover treatment is `rgba(17, 17, 17, 0.173) 0px 0px 30px` — a 30px-radius shadow with no x or y offset, producing a gentle aura around the element rather than a directional lift. Cards don't appear to "rise" — they appear to softly illuminate. This matches the typographic restraint: where the type stays at one weight, the elevation stays at one direction.

### Decorative Depth
- Cream-surface cards (`#f4f2f0`) create depth via tonal shift rather than shadow — the cream panel reads as recessed against the white canvas
- Hairline borders in lab-space neutrals do all structural separation
- The yellow CTA is its own form of visual elevation — pure chromatic contrast against the muted system makes it leap forward without any shadow

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

**Primary Yellow CTA**
- Background: Ramp Yellow (`#f0e84a`)
- Text: Ramp Black (`#212121`)
- Padding: `0px 20px` horizontal, height ~40–48px via 16px line-height
- Radius: `6px`
- Border: `none`
- Shadow: `none` at rest
- Font: 16px lausanne weight 400, `ss01`
- Hover: subtle background-shift via `--fides-overlay-hover-color` token
- Use: Primary CTA — "Get Started", "Get Ramp", "See Pricing"

**Inverse Black CTA**
- Background: Ramp Black (`#212121` or `#2b2e35` for muted variant)
- Text: Pure White (`#ffffff`)
- Padding: `0px 20px` horizontal
- Radius: `6px`
- Font: 16px lausanne weight 400, `ss01`
- Hover: background lifts to `#4f525b`
- Use: Secondary CTAs — "Sign In", "Watch Demo", inline secondary actions

**Ghost / Link Style**
- Background: `rgba(255, 255, 255, 0.05)` — barely-there transparent fill
- Text: Ramp Black (`#212121`)
- Padding: `12px 16px`
- Radius: `6px`
- Border: `none`
- Shadow: `rgba(255, 255, 255, 0.6) 0px 0px 2px 0px inset` — soft inner glow
- Font: 14px lausanne weight 400, `ss01`
- Hover: `box-shadow: rgba(17, 17, 17, 0.173) 0px 0px 30px` ambient atmospheric glow
- Use: Tertiary actions, sub-CTAs inside cards

**Card-as-Button (Feature Tile)**
- Background: Cream Surface (`#f4f2f0`)
- Text: Ramp Black (`#212121`)
- Padding: `24px`
- Radius: `12px`
- Border: `none`
- Shadow: `none` at rest
- Font: 16px lausanne weight 400, `ss01`
- Use: Feature-grid tiles that double as CTAs — pricing, product entry points

### Cards & Containers

**Standard Card**
- Background: Pure White (`#ffffff`)
- Border: `1px solid lab(91.62 -0.16 -2.27)` (≈`#e8eaeb`) — barely-perceptible cool grey hairline
- Radius: `8px` (default) or `12px` (feature) or `16px` (hero)
- Shadow: `none` at rest, `rgba(17, 17, 17, 0.173) 0px 0px 30px` on hover
- Padding: `24px–32px` internal

**Cream Feature Tile**
- Background: Cream Surface (`#f4f2f0`)
- Border: `none`
- Radius: `12px`
- Shadow: `none`
- Padding: `24px`
- Use: Pricing cards, feature highlights, alternating-section panels

**Aspect-Square Image Card**
- Background: Pure White (`#ffffff`)
- Border: `1px solid oklab(0.2145 0.00153 0.00048 / 0.1)` — 10% black hairline
- Radius: `12px`
- Padding: `0px` — image fills the card
- Hover: background tints via `--fides-overlay-hover-color`
- Use: Customer-story tiles, product screenshot cards

### Badges / Tags / Pills

**Neutral Badge**
- Background: Badge Background (`#718096`)
- Text: Pure White (`#ffffff`)
- Padding: `4px 10px`
- Radius: `4px`
- Font: 13px lausanne weight 400, `ss01`
- Use: Secondary metadata, role indicators

**Eyebrow Label**
- Background: `transparent`
- Text: Ramp Black (`#212121`)
- Padding: `0px`
- Font: 10px lausanne weight 400, `ss01`, UPPERCASE, `0.18–0.5px` letter-spacing
- Use: Section eyebrows above hero headlines — "PLATFORM", "FOR FINANCE TEAMS"

### Inputs & Forms

**Standard Email Input**
- Background: `transparent`
- Border: `none` (inputs sit inside a card with the card carrying the border)
- Radius: `10px` — slightly more rounded than buttons
- Padding: `0px 16px 0px 24px` — left-padded for prominent email-capture moments
- Font: 16px lausanne weight 400, `ss01`
- Placeholder: muted slate
- Focus: outline disabled, parent card may apply `box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px, rgba(0, 0, 0, 0.2) 0px 0px 0px 2px`

**Inverse Email Input (on dark hero)**
- Background: `transparent`
- Text: Pure White (`#ffffff`)
- Border: `none` (white card carries the border at `rgba(255, 255, 255, 0.3)`)
- Radius: `10px`
- Padding: `0px 16px 0px 24px`

### Navigation
- Top nav: white background, sticky on scroll with backdrop-filter blur
- Logo: `lausanne`-set wordmark left-aligned at 75x20 SVG dimensions
- Links: 14px lausanne weight 400, `#212121`, `ss01` enabled
- Hover: link colour drops to 60% opacity (`lab(2.84 0.37 0.97 / 0.6)`)
- Primary CTA "Get Started" right-aligned: yellow fill, 6px radius, 16px lausanne weight 400
- Mobile: hamburger drawer collapses primary nav; CTA persists

### Decorative Elements

**Atmospheric Hover Glow**
- `rgba(17, 17, 17, 0.173) 0px 0px 30px` ambient hover shadow on interactive cards and ghost buttons
- The signature elevation cue: cards don't lift, they glow softly outward
- Distinct from drop shadows — the glow has no direction, no offset, just radius

**Hairline-as-Structure**
- `1px solid lab(...)` borders in barely-perceptible cool greys carry all card and divider structure
- The two most-used border colours (34 instances each) are nearly invisible at standard rendering — the system trusts whitespace over visible structure

**Inset Glow on Ghost Buttons**
- `rgba(255, 255, 255, 0.6) 0px 0px 2px 0px inset` produces a subtle inner glow that lifts ghost buttons just enough to read as interactive

## Do's and Don'ts

### Do
- Use `lausanne` (or substitute) with the `ss01` OpenType feature on every text element — this is the brand's typographic signature
- Set the entire system at weight 400; reach for 500 only on compact buttons and inline links
- Reserve Ramp Yellow (`#f0e84a`) for the primary CTA — never use it as a surface fill, never use it on body type
- Use cream surface (`#f4f2f0`) as the alternating secondary panel — never a dark section
- Apply negative letter-spacing on display sizes 40px+: `-0.005px` at 40px, `-0.01px` at 48px
- Keep border-radius in the 4–16px range — `6px` for buttons, `12px` for cards, `16px` for hero features
- Use the ambient hover glow (`rgba(17, 17, 17, 0.173) 0px 0px 30px`) on interactive cards
- Use hairline lab-space borders (`lab(91.62 -0.16 -2.27)`) for card edges — barely-perceptible structure
- Set body line-height to `1.50` for readable contrast against tight `1.04–1.17` display
- Use `Material Icons Outlined` for inline UI glyphs — the only non-lausanne typeface allowed

### Don't
- Don't use bold (700) `lausanne` for headlines — weight 400 is the brand voice, hierarchy is from size only
- Don't disable the `ss01` stylistic set — the alternate glyphs define the personality
- Don't introduce a second saturated colour to compete with Ramp Yellow — the single-CTA signal is the point
- Don't use Ramp Yellow as a surface fill on cards or sections — it lives on buttons only
- Don't add drop shadows with x/y offsets — Ramp's elevation is direction-less ambient glow
- Don't use pill-shaped buttons (`9999px` radius) — the system caps at `16px` radius for hero cards
- Don't use letter-spacing on body or button text — only display 40px+ gets negative tracking
- Don't pair Ramp with a script or serif typeface — `lausanne` carries the entire system
- Don't use pure black (`#000000`) for body — Ramp Black (`#212121`) is the institutional neutral
- Don't introduce dark-mode brand sections — the system stays in the white-cream-yellow range

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <600px | Single-column, hero compresses to 32–40px, stacked CTAs |
| Mobile Plus | 600–768px | Single-column with wider feature cards |
| Tablet | 768–1024px | 2-column feature grids, sticky CTA in nav |
| Desktop | 1024–1280px | Full layout, 3-column feature grids, hero at 48px |
| Large Desktop | ≥1280px | Centered content with generous flanking margins |

### Touch Targets
- Primary CTAs: `0px 20px` horizontal padding produces ~40–48px tap height
- Nav links: 14px with adequate spacing
- Feature cards: full-card tap target, no nested clickable regions
- Email inputs: minimum 48px height for tap-comfortable entry

### Collapsing Strategy
- **Nav**: Horizontal nav + right-aligned CTA collapses to hamburger on tablet and below
- **Hero**: 48px display → 40px → 32px on mobile, weight 400 maintained throughout
- **Feature cards**: 3-column → 2-column → single-column stacked
- **Customer logo strips**: 6-up desktop → 3-up mobile, logos scale proportionally
- **Section spacing**: 64–128px desktop → 32–48px mobile
- **Cream panel breaks**: Maintained at all breakpoints — surface alternation is preserved

### Image Behavior
- Dashboard / product screenshots maintain 12px radius and atmospheric hover glow at all sizes
- Customer-story video frames maintain 12px radius with play-button overlay
- Hero illustration / decorative imagery scales proportionally; no art-direction swap between breakpoints

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Ramp Yellow (`#f0e84a`)
- Inverse CTA: Ramp Black (`#212121`)
- Page Background: Pure White (`#ffffff`)
- Secondary Surface: Cream (`#f4f2f0`)
- Body Text: Ramp Black (`#212121`)
- Muted Body: Body Slate (`#4a5568`)
- Label Slate: `#2d3748`
- Card Border: `lab(91.62 -0.16 -2.27)` (≈ `#e8eaeb`)
- Hairline 10%: `rgba(33, 33, 33, 0.1)`
- Success: `#38a169`
- Error: `#e53e3e`

### Quick Type Reference
- Display: lausanne 48px / weight 400 / line-height 1.04 / letter-spacing -0.01px / `ss01`
- Section heading: lausanne 28px / weight 400 / line-height 1.14 / `ss01`
- Body: lausanne 16px / weight 400 / line-height 1.50 / `ss01`
- Button: lausanne 16px / weight 400 / line-height 1.50 / `ss01`
- Eyebrow: lausanne 10px / weight 400 / line-height 1.50 / letter-spacing 0.5px / UPPERCASE / `ss01`

### Example Component Prompts
- "Create a hero on `#ffffff`. Headline at 48px lausanne weight 400, line-height 1.04, letter-spacing -0.01px, color `#212121`, font-feature-settings `'ss01'`. Eyebrow above at 10px lausanne weight 400 UPPERCASE letter-spacing 0.5px. Sub-deck at 20px weight 400 line-height 1.30. Primary CTA: `#f0e84a` background, `#212121` text, `6px` radius, padding `0px 20px`, 16px lausanne weight 400 with `'ss01'`."
- "Design a feature card on `#f4f2f0` cream surface, `12px` radius, no border, `24px` internal padding. Card title at 24px lausanne weight 400 line-height 1.17, body at 16px weight 400 line-height 1.50, color `#212121` throughout. Add an ambient hover glow: `box-shadow: rgba(17, 17, 17, 0.173) 0px 0px 30px`."
- "Build a customer-story card: white background, `1px solid lab(91.62 -0.16 -2.27)` border, `12px` radius, aspect-square. Logo top-left, video play-button center, customer name in 20px lausanne weight 400 with `'ss01'` at the bottom-left."
- "Create a navigation bar: white sticky header with backdrop-blur. lausanne 14px weight 400 with `'ss01'` for nav links in `#212121`, hover at 60% opacity. Right-aligned 'Get Started' yellow CTA: `#f0e84a` bg, `#212121` text, `6px` radius, 16px lausanne."
- "Design an email-capture input: white card with `12px` radius and `1px solid lab(91.62 -0.16 -2.27)` border. Inside: 16px lausanne weight 400 input with `0px 16px 0px 24px` padding, `transparent` bg, no border (card carries it). Submit button to the right: yellow CTA `#f0e84a`, `6px` radius, 16px lausanne `'ss01'`."

### Iteration Guide
1. Always enable `font-feature-settings: "ss01"` on lausanne text — this is the brand's typographic DNA
2. Weight 400 is the only weight; reach for 500 only on small compact buttons and inline links
3. Ramp Yellow (`#f0e84a`) lives on the primary CTA only — never on surfaces, never on body, never as a brand accent on cards
4. Border-radius scale is `6px` (buttons) → `8px` (cards) → `10px` (inputs) → `12px` (feature cards) → `16px` (hero)
5. Body text is `#212121` (Ramp Black), muted body is `#4a5568` (Body Slate), labels are `#2d3748` (Label Slate)
6. Cards use barely-perceptible lab-space hairlines — `lab(91.62 -0.16 -2.27)` is the most-used border
7. Hover state on cards is the ambient glow `rgba(17, 17, 17, 0.173) 0px 0px 30px` — no directional drop shadows
8. Display sizes get negative letter-spacing (`-0.005px` at 40px, `-0.01px` at 48px); body and small text use default tracking
9. UPPERCASE only on 10px eyebrows with `0.18–0.5px` tracking — buttons and headlines stay sentence case
10. Cream surface (`#f4f2f0`) alternates with white for section rhythm — no dark-mode brand panels
