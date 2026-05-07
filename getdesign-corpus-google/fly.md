---
version: alpha
name: "Fly.io"
description: "Token-first design system reference for Fly.io."

colors:
  background: "#ffffff"
  surface: "#281950"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#7c3aed"
  primary: "#e7e6f4"
  on-primary: "#ffffff"
  border: "#a39ac1"
  focus-ring: "#e7e6f4"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 25px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
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

# Fly.io Design System

## Overview

Fly.io's website is what happens when a serious infrastructure company refuses to look like one. The hero opens on a near-white lavender wash (`#e7e6f4`) with a deep aubergine headline (`#281950`) set in the warm humanist serif **Mackinac**, italicized for emphasis on the key promise ("Run any code *fearlessly*"). Wrapped around the type sits a chaotic, hand-drawn illustration system — balloons, ribbons, sparkle bursts, technicolor wires — rendered in a saturated rainbow of teals, peaches, blues, yellows, and pinks. It's the exact opposite of the gray-on-white "modern dev tool" template. Fly.io looks like a children's book about distributed systems.

That tension between editorial seriousness and illustrated playfulness is the brand's signature. The typography stack is genuinely refined: Mackinac (a chunky display serif with bracketed terminals) at weight 500 for every headline, paired with **Fricolage Grotesque** at weight 325 for body — an unusually light grotesk that lets the serif do the shouting. Spacing is generous, line-heights are tall (1.50 on all body sizes), and section breaks rely on illustration vignettes rather than rules or color blocks. Each feature section gets its own little drawn scene: a person on a swing for "Sandboxes That Feel Like a Superpower," a stack of disks tied with ribbon for "Storage That Keeps Up." Every illustration is editorial, not iconographic — none of them look like UI.

The third defining trait is Fly.io's **two-mode color system**. Most of the page lives in the lavender-and-aubergine "daylight" palette, but the page closes (and the nav drops down) on a deep purple gradient — a `#281950` to violet field that hosts a second dark theme: white text, lavender-mist secondary text (`#a39ac1`), violet `#7c3aed` button fills with inset purple ring shadows. Yellow (`#facc15`) is reserved for hover-state link underlines on the dark surface — a subtle developer-y cue that something's clickable. The site moves between these two surfaces deliberately, and component variants exist for both modes.

**Key Characteristics:**
- Mackinac serif at weight 500 for every headline; chunky bracketed display typeface, italic for emphasis
- Fricolage Grotesque at weight 325 for body — extra-light grotesk that defers to the serif
- Lavender-mist canvas (`#e7e6f4`) with deep aubergine ink (`#281950`) — never plain white, never plain black
- Hand-drawn illustrated vignettes per section (balloons, swings, ribbons, hot-air balloons, characters)
- Saturated rainbow accents inside illustrations: teal `#5eead4`, peach `#f97316`, blue `#3b82f6`, yellow `#f59e0b`, green `#10b981`
- Pill-radius buttons (`9999px`) as the default, with one wild "ribbon" variant (`8px 20px 20px 8px`) for the nav login chip
- Inset purple ring shadows (`rgba(67, 56, 202, 0.25) 0px 0px 0px 1px inset`) on every primary button — replaces traditional borders
- Deep-purple gradient footer/dark mode variant where yellow becomes the hover accent
- Tab-shaped pricing chips with rainbow-tinted glow shadows, one per service category

## Colors

### Primary
- **Fly Aubergine** (`#281950`): Primary text on light surfaces, hero headlines, body copy. Used 309 times on the pricing page — the workhorse ink. Not black; never black.
- **Lavender Mist** (`#e7e6f4`): Default page background and section panel fill. Used 433 times — far more than white. Reads as paper-with-purple-undertone.
- **Pure White** (`#ffffff`): Reserved for cards, inputs, and text on the dark gradient sections.

### Brand Accent
- **Fly Violet** (`#7c3aed`): The signature interactive color. Primary CTA fills, link hover color on light surfaces, focus rings. The Tailwind `violet-600` exact value.
- **Indigo Inset** (`rgba(67, 56, 202, 0.25)`): Used as a 1px inset ring shadow inside violet buttons — the "border" effect without an actual border.
- **Lavender Lilac** (`#ddd6fe`): Hover-state background tint on violet buttons (Tailwind `violet-200`). Buttons go from violet to lilac on hover, inverting the contrast.
- **Plum Shadow** (`rgba(91, 33, 182, 0.1)`): Soft drop-shadow tint applied to translucent dark-surface buttons.

### Neutrals & Text
- **Fly Aubergine** (`#281950`): All headline and body text on light.
- **Ink Slate** (`#202237`): Secondary text option, slightly cooler than aubergine. Used for link defaults in some contexts.
- **Lavender Fog** (`#a39ac1`): Tertiary/muted text on dark surfaces — footer subnav, captions, deemphasized labels.
- **Cool Gray Border** (`#ccd0e0`): The single neutral border tone for input chrome.
- **Border Whisper** (`#e1e4ef`): Hairline 1px nav divider — barely-there separator on the sticky top bar.

### Surface & Borders
- **Light Surface** (`#e7e6f4`): Default panel and page canvas.
- **Card Surface** (`#ffffff`): Elevated card fill on the lavender canvas.
- **Dark Surface** (`#281950` → violet gradient): Page footer and "Build Whatever You Can Think Up" closing section. Hosts inverted button variants.
- **Translucent White Border** (`rgba(255, 255, 255, 0.25)`): 1px outline used on translucent dark-mode buttons; bumps to `0.5` on hover.

### Illustration Accents (chromatic palette)
These appear inside hand-drawn illustrations and as single-accent splashes on tab-style pricing chips. Never used for primary UI.
- **Peach Orange** (`#f97316`) — Tailwind `orange-500`
- **Sky Blue** (`#3b82f6`) — Tailwind `blue-500`
- **Mint Green** (`#10b981`) — Tailwind `emerald-500`
- **Amber Yellow** (`#f59e0b`) — Tailwind `amber-500`
- **Sunbeam Yellow** (`#facc15`) — Tailwind `yellow-400`, reserved for hover underline on dark surfaces
- **Teal Mint** (`#5eead4`) — Tailwind `teal-300`, the unexpected hover-fill on primary CTAs

### Shadow & Glow Colors
- **Plum Soft Shadow** (`rgba(91, 33, 182, 0.1)`): Default ambient shadow on hovering pill buttons — `0px 5px 5px -2px, 0px 2px 4px -2px`.
- **Indigo Inset Ring** (`rgba(67, 56, 202, 0.25)`): The signature `0 0 0 1px inset` ring on violet buttons.
- **Lavender Inset Highlight** (`rgb(231, 230, 244) 0px -3px 6px -2px inset`): A bottom-inner highlight on white pill buttons — reads like printed letterpress.
- **Tab Glow Shadows** (one per service): Mint `rgba(16, 185, 129, 0.3)`, Blue `rgba(59, 130, 246, 0.3)`, Orange `rgba(249, 115, 22, 0.3)`, Amber `rgba(245, 158, 11, 0.3)` — `0 20px 25px -5px, 0 8px 10px -6px` rainbow drops on the pricing-tab cluster.

### Gradient System
- **Aubergine-to-Violet Closing Gradient**: From `#281950` at the top to a deeper violet at the bottom of the closing CTA panel and footer. Subtle, photograph-like — not a flashy hero gradient.
- No hero gradient on light surface — illustrations carry the chromatic energy instead.

## Typography

### Font Family
- **Display**: `Mackinac`, with fallback: `ui-serif, Georgia, Cambria, "Times New Roman", Times`. A bracketed humanist display serif with chunky terminals — used at weight 500 throughout, often italicized for emphasis.
- **Body / UI**: `Fricolage Grotesque`, with fallback: `ui-sans-serif, system-ui, "Apple Color Emoji", "Segoe UI Emoji"`. An unusually low default weight of 325 makes long-form copy feel airy.
- **Available weights observed**: Mackinac 500 only. Fricolage Grotesque 325, 450, 500, 575.

*Note: Mackinac is a P22 / House Industries-adjacent display serif. Tiempos Headline, Recoleta, or Söhne Schmal serve as close substitutes; for web-safe fallbacks, italic Tiempos or Source Serif Pro work. Fricolage Grotesque can be substituted with Inter at weight 350 or Söhne at Buch.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Mackinac | 64px (4.00rem) | 500 | 1.15 | -2.88px | Homepage hero — italic for emphasized words |
| Display Large | Mackinac | 60px (3.75rem) | 500 | 1.25 | -2.7px | Closing CTA section heads on dark surface |
| Section Headline | Mackinac | 36px (2.25rem) | 500 | 1.33 | -0.9px | Major feature section heads |
| Subsection | Mackinac | 30px (1.88rem) | 500 | 1.32 | -0.75px | Pricing tier headers, secondary heads |
| Card Title | Mackinac | 22px (1.38rem) | 500 | 1.32 | -0.55px | Feature card heads, sub-section markers |
| Lead Body | Fricolage Grotesque | 20.5px (1.28rem) | 325 | 1.50 | normal | Hero subtitle, intro paragraphs |
| Body Large | Fricolage Grotesque | 19px (1.19rem) | 325 | 1.50 | normal | Section descriptions, product feature copy |
| Body | Fricolage Grotesque | 16px (1.00rem) | 325 | 1.50 | normal | Standard reading text |
| Button Label | Fricolage Grotesque | 15.5px (0.97rem) | 450 | 1.50 | normal | Primary button text |
| Nav / UI | Fricolage Grotesque | 14.5px (0.91rem) | 450 | 1.50 | normal | Top nav links, secondary buttons |
| Eyebrow Caps | Fricolage Grotesque | 14.5px (0.91rem) | 575 | 1.50 | 0.725px | Uppercase section labels above headlines |
| Caption | Fricolage Grotesque | 12px (0.75rem) | 500 | 1.50 | 0.3–0.6px | Uppercase chrome labels, footer headers |
| Caption Small | Fricolage Grotesque | 12px (0.75rem) | 325 | 1.50 | normal | Footnote, legal, footer subnav |

### Principles
- **Serif headlines, grotesk body**: The Mackinac/Fricolage pairing is the entire identity in two fonts. Don't swap one without the other.
- **Aggressive negative tracking on display**: Mackinac headlines pull tight — `-2.88px` at 64px, scaling proportionally down to `-0.55px` at 22px. The serif terminals would otherwise gap.
- **Italic for emphasis, never bold**: Hero headlines italicize the operative phrase ("Run any code *fearlessly*") — Mackinac's italic is a separate cut and carries warmth. Bolder weight is not in the system.
- **Body weight is 325, not 400**: This is the design's quiet trick. Fricolage at 325 reads like a draftsman's hand — light, precise, never demanding. Don't promote body to 400 unless it's a button or nav link.
- **Tall 1.50 line-height everywhere**: Both display and body run at line-heights between 1.32 and 1.66. The page breathes vertically.
- **Uppercase eyebrows**: Small caps-style labels above headlines use weight 575 with `0.725px` tracking — a borrowed editorial convention to mark sections without using a horizontal rule.

## Layout

### Spacing System
- Base unit: 8px, with 4px and 6px sub-units for chrome
- Observed scale: 2px, 4px, 6px, 8px, 10px, 12px, 16px, 20px, 24px, 32px, 40px, 48px, 70px, 80px, 96px, 128px
- High-frequency values: 16px (59 uses) and 10px (44 uses) are the workhorses; 128px (16 uses) handles vertical section breaks
- Notable: a 70px and 297.6px both appear once — unusual one-offs likely tied to specific illustration alignment

### Grid & Container
- Max content width: ~1200px for centered content; closing CTA section spans full width on dark gradient
- Hero: two-column at desktop (text left, illustration right), full-width at mobile
- Feature sections: alternating two-column layouts (image-left/right swap each row), with a single-column "anchor" section between every 2–3 feature pairs
- Pricing: full-width tab cluster across top, then a wide pricing card panel below with one row per tier

### Whitespace Philosophy
- **Generous and editorial**: 96–128px between major sections at desktop; 48–64px on mobile
- **Illustration as breathing room**: Sections are visually paced by their illustration vignettes, not by negative space alone — the drawings ARE the rhythm
- **Tall line-heights**: 1.50 across all body sizes means paragraphs themselves contribute vertical air
- **Light over dark transitions**: The closing CTA panel + footer cover the bottom 25% of the page in deep purple; the rest of the page floats on lavender mist

### Border Radius Scale
- Hairline / Sharp (0px): Section dividers and full-bleed photographic content
- Small (8px): Compact buttons, inline chips
- Medium (10px): Inputs, smaller cards, default chip
- Standard (16px): The workhorse card radius — used 9 times on the home page
- Large (24px): Pricing panels, feature spotlights
- Pill (9999px): Buttons, badges, navigation chips — the dominant interactive shape
- Asymmetric (`8px 20px 20px 8px` and `9999px 9999px 0px 0px`): Reserved for two specific custom shapes — the login ribbon chip and the pricing-tab top
- The system uses **multiple mid-range radii** (10/16/24) deliberately — this is not a binary system

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, body text, illustration scenes |
| Inset Ring (Level 1) | `rgba(67, 56, 202, 0.25) 0 0 0 1px inset` | Violet pill buttons — the signature "border" replacement |
| Letterpress Inset (Level 1.5) | `rgb(231, 230, 244) 0 -3px 6px -2px inset` | White pill buttons — bottom-inner lavender glow |
| Soft Plum Drop (Level 2) | `rgba(91, 33, 182, 0.1) 0 5px 5px -2px, 0 2px 4px -2px` | Translucent buttons hovering on dark gradient |
| Card Double-Layer (Level 3) | `rgba(32, 34, 55, 0.075) 0 0 0 1px, rgba(32, 34, 55, 0.05) 0 10px 15px -3px, rgba(32, 34, 55, 0.05) 0 4px 6px -4px` | Feature cards, dropdown menus |
| Tab Glow (Level 4) | Per-service rainbow drops — e.g., `rgba(16, 185, 129, 0.3) 0 20px 25px -5px, 0 8px 10px -6px` | Pricing service tabs |
| Hero Lift (Level 5) | `rgb(91, 33, 182) 0 0 0 1px, rgba(255, 255, 255, 0.4) 0 0 0 2px, rgba(0, 0, 0, 0.1) 0 10px 15px -3px` | Featured pricing card with violet outline + white halo + ambient lift |

**Shadow Philosophy**: Fly.io's depth system uses shadows to do two distinct jobs. First, **inset rings** function as borders without being borders — the violet button has no `border`, it has a 1px indigo ring sitting inside. This produces a printed, debossed quality on every interactive element. Second, **outer drops** are atmospheric: extremely low-opacity (5–10%) offsets in either purple or near-black, producing a soft photographic lift. The most distinctive variant is the **rainbow tab glow** on the pricing chips — each service category gets a colored shadow that semantically reinforces the category (mint = compute, blue = networking, orange = storage, amber = GPUs). Color shadows here are not decorative; they're meaning.

### Decorative Depth
- Inset rings + soft outer drops layer freely — buttons routinely have both
- The hero pricing card stacks three shadow layers (ring + halo + drop) for emphasis without scaling up
- No hard offset shadows, no neumorphism, no glows — the system is restrained-photographic

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

**Primary Violet Pill**
- Background: Fly Violet (`#7c3aed`)
- Text: Pure White (`#ffffff`)
- Padding: 0px 20px (height set by line-height)
- Radius: `9999px` (full pill)
- Border: `1px solid rgba(255, 255, 255, 0)` (transparent — placeholder for hover transition)
- Shadow: `rgba(67, 56, 202, 0.25) 0px 0px 0px 1px inset` — the indigo inset ring is the signature
- Font: 15.5px Fricolage Grotesque weight 450, sentence case
- Hover: background flips to mint teal `rgba(94, 234, 212, 0.9)`, text to aubergine `#281950` — full color inversion, mildly chaotic
- Active: deeper violet `#6d28d9`, text drops to `rgba(46, 16, 101, 0.5)`
- Use: Primary CTA — "Get Started", "Try Fly.io"

**Translucent Dark-Mode Pill**
- Background: `rgba(255, 255, 255, 0)` (fully transparent)
- Text: Pure White (`#ffffff`)
- Padding: 0px 20px
- Radius: `9999px`
- Border: `1px solid rgba(255, 255, 255, 0.25)` — visible hairline outline
- Shadow: `rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(91, 33, 182, 0.1) 0px 5px 5px -2px, rgba(91, 33, 182, 0.1) 0px 2px 4px -2px` — soft plum drop
- Hover: same teal inversion as primary
- Use: Secondary action on dark gradient sections — "Sign In", "Read the Docs"

**White Letterpress Pill**
- Background: Pure White (`#ffffff`)
- Text: Fly Aubergine (`#281950`)
- Padding: 0px 20px
- Radius: `9999px`
- Border: `1px solid rgba(91, 33, 182, 0.125)` — hairline plum
- Shadow: `rgb(231, 230, 244) 0px -3px 6px -2px inset` — bottom-inner lavender highlight, reads like a debossed business card
- Use: Tertiary CTA on light surfaces — "Learn More", documentation links

**Ribbon Login Chip**
- Background: Fly Violet (`#7c3aed`)
- Text: Pure White (`#ffffff`)
- Padding: 0px 12px 0px 10px (asymmetric — left edge slightly tighter)
- Radius: `8px 20px 20px 8px` — rounded right side, soft-square left, ribbon shape
- Border: 0px
- Shadow: same indigo inset ring as primary
- Font: 14.5px Fricolage Grotesque weight 450
- Use: Top-right nav login affordance — the only non-pill button shape in the system, used to mark the persistent account entry point

**Tab Pricing Chip (Service Selector)**
- Background: White card with colored shadow
- Radius: `9999px 9999px 0px 0px` — top-only pill, sits flush against the panel below
- Shadow varies per service:
  - Compute (mint): `rgba(16, 185, 129, 0.35) 0px 0px 0px 1px, rgba(16, 185, 129, 0.3) 0px 20px 25px -5px, rgba(16, 185, 129, 0.3) 0px 8px 10px -6px`
  - Networking (blue): same shape with `rgba(59, 130, 246, 0.3)`
  - Storage (orange): `rgba(249, 115, 22, 0.3)`
  - GPUs (amber): `rgba(245, 158, 11, 0.3)`
- Use: Pricing-page service selector — each tab glows in its category color

### Cards & Containers
- Background: `#ffffff` cards on `#e7e6f4` canvas — a 5% contrast lift, not a strong border
- Border: typically none, or `1px solid #e1e4ef` (border-whisper) for full-bleed nav
- Radius: 16px is the workhorse for feature cards; 24px for large pricing panels; 10px for inline chips
- Shadow: `rgb(255, 255, 255) 0px 0px 0px 0px, rgba(32, 34, 55, 0.075) 0px 0px 0px 1px, rgba(32, 34, 55, 0.05) 0px 10px 15px -3px, rgba(32, 34, 55, 0.05) 0px 4px 6px -4px` — the standard double-layer card lift
- Internal padding: 32–48px for feature cards, 64–96px for marquee panels

### Badges / Tags / Pills
- Eyebrow caps labels (`12px Fricolage 575 uppercase, letter-spacing 0.6px, color #281950`) substitute for traditional badges throughout the marketing site
- True pills only appear in pricing tier markers — `9999px` radius, white background, hairline border, eyebrow text inside

### Inputs & Forms
- Background: `#ffffff`
- Border: `1px solid #ccd0e0` (cool gray)
- Radius: 10px
- Font: 16px Fricolage Grotesque weight 325, color `#281950`
- Focus: violet ring `rgba(124, 58, 237, 0.5) 0 0 0 3px` (Tailwind ring pattern)
- Padding: 12–16px vertical, 16px horizontal

### Navigation
- Top nav: sticky white bar on light surface, sits on a `1px 0 0 0 solid rgb(225, 228, 239)` hairline divider
- Logo: Fly.io balloon-and-wordmark SVG, 111×36px, leftmost
- Nav links: 14.5px Fricolage weight 450, color `#281950`, hover shifts to `#7c3aed` with underline
- Right cluster: "Sign In" ghost link → ribbon-shaped login chip → violet pill primary CTA
- Dropdown menus: white cards with the standard double-layer card shadow, 16px radius

### Decorative Elements

**Hand-Drawn Illustration Vignettes**
- Each major feature section is anchored by a small (~280–340px wide) hand-drawn scene
- Examples observed: balloons clustered on a string, person pumping legs on a swing, stack of disks tied with ribbon, hot-air balloon with cargo basket, character sketching at a drafting table
- Color palette inside illustrations: saturated rainbow (peach, teal, blue, yellow, mint, lavender) on white or transparent background
- Linework: black or dark aubergine, varying weight, with hand-trembling imperfections — drawn, not vector-perfected
- Function: replaces icons, dividers, and section-anchor imagery all at once

**Inset Ring Shadows**
- The `0 0 0 1px inset` indigo or lavender ring on buttons replaces a traditional border
- Creates a subtle "letterpress / debossed business card" quality — interactive elements feel printed rather than rendered
- Pairs with the soft outer drop shadows for a layered tactile effect

**Eyebrow Caps Labels**
- Uppercase 12px Fricolage 575 weight with 0.6px tracking, sitting above section headlines
- Example: "WHAT WE BUILD" above a Mackinac headline; "PLATFORM" above pricing
- The system's substitute for icon-led section markers

## Do's and Don'ts

### Do
- Use Mackinac at weight 500 italic for hero emphasis — it is the brand voice
- Set body text in Fricolage Grotesque weight 325 — the lightness is the signature
- Apply the indigo inset ring (`rgba(67, 56, 202, 0.25) 0 0 0 1px inset`) on every violet primary button
- Pair every feature section with a hand-drawn illustration vignette, not an icon
- Use lavender mist (`#e7e6f4`) as the canvas — never plain white
- Use deep aubergine (`#281950`) as text — never pure black
- Reserve yellow (`#facc15`) for hover-underline accents on dark gradient surfaces only
- Use rainbow-tinted shadows on category-distinguishing tabs (compute=mint, networking=blue, storage=orange, GPUs=amber)
- Set tall 1.50 line-heights across all body and most display sizes
- Use uppercase Fricolage 575 weight as eyebrow labels above headlines

### Don't
- Don't use Mackinac at any weight other than 500 — there is no "bold" or "regular" option in this system
- Don't promote body text to weight 400 or 500 — body lives at 325
- Don't use plain `#000` text or plain `#fff` page background — both read as foreign
- Don't replace the inset ring with a solid 1px border — the inset is the differentiator
- Don't introduce flat geometric icons — the illustration system is hand-drawn or it isn't on-brand
- Don't use chromatic accents (orange, blue, mint) for primary UI — they belong inside illustrations or as category shadows only
- Don't use sharp 0px radius for buttons — pills are the default
- Don't apply more than one tertiary chromatic color per section — illustrations carry the rainbow, UI doesn't
- Don't use hero gradients on light surfaces — illustrations carry the energy, gradients live in the closing dark band

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <480px | Single column, hero drops to ~36px, illustrations scale down 50% |
| Mobile | 480–640px | Single column, 40–48px hero, stacked CTA pills full-width |
| Tablet Small | 640–768px | Two-column copy starts, illustrations at 70% scale |
| Tablet | 768–1024px | Full feature alternation begins, hero ~52px |
| Desktop | 1024–1200px | Full multi-column layouts, hero ~58px |
| Large Desktop | 1200–1400px | Hero at full 64px, max content width ~1200px |
| XL Desktop | 1400–1728px | Container holds at 1200px, additional whitespace on either side |
| Ultra Wide | ≥1728px | Container caps at 1200px, hero illustration may extend further right |

### Touch Targets
- Pill buttons: minimum 44px tap height with 20px horizontal padding maintained at all breakpoints
- Nav links: 14.5px text with generous vertical padding (16–20px) to clear thumb-sized hit zones
- Pricing tabs: full-width tappable cluster on mobile, condensed to inline tabs at desktop

### Collapsing Strategy
- **Nav**: Horizontal link bar collapses to hamburger on mobile; opens as a full-screen sheet with the same lavender background
- **Hero**: 64px → 48px → 36px progressive scaling, with italic emphasis preserved at every size
- **Two-column features**: Image-left/text-right pattern collapses to image-on-top, text-below
- **Pricing tabs**: Horizontal tab cluster becomes a vertical accordion list on mobile, with category-colored shadows preserved
- **Closing dark CTA**: Full-bleed gradient persists at all sizes; closing illustration scales to 60% on mobile
- **Footer**: 4-column nav grid → 2-column → 1-column accordion across breakpoints

### Image Behavior
- Hand-drawn illustrations maintain their artistic quality at all sizes — no art-direction swap, just proportional scaling
- Illustrations sit edge-to-edge on mobile (no card chrome) but inside cards on desktop
- Logo wordmark scales but never reduces to icon-only — the balloon mark stays attached
- All illustrations are SVG/WebP and ship at high resolution

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Fly Violet (`#7c3aed`)
- Page Background: Lavender Mist (`#e7e6f4`)
- Primary Text: Fly Aubergine (`#281950`)
- Secondary Text on Dark: Lavender Fog (`#a39ac1`)
- Inset Ring: `rgba(67, 56, 202, 0.25) 0px 0px 0px 1px inset`
- Hover Underline (dark surfaces): Sunbeam Yellow (`#facc15`)
- Hover Underline (light surfaces): Fly Violet (`#7c3aed`)
- Hover Button Fill: Mint Teal (`rgba(94, 234, 212, 0.9)`)
- Card Surface: Pure White (`#ffffff`) on lavender canvas
- Closing Gradient: Fly Aubergine (`#281950`) to deeper violet (`#5b21b6`)

### Example Component Prompts
- "Create a hero section on Lavender Mist (`#e7e6f4`) with a headline at 64px Mackinac weight 500, line-height 1.15, letter-spacing -2.88px, color `#281950`. Italicize the operative phrase. Subtitle in Fricolage Grotesque 20.5px weight 325, line-height 1.50. Add a primary CTA — Fly Violet (`#7c3aed`) pill button, `9999px` radius, 15.5px Fricolage weight 450 white text, with `rgba(67, 56, 202, 0.25) 0px 0px 0px 1px inset` ring shadow."
- "Design a feature card on `#ffffff` over lavender canvas. Radius 16px, no border, shadow stack `rgba(32, 34, 55, 0.075) 0 0 0 1px, rgba(32, 34, 55, 0.05) 0 10px 15px -3px, rgba(32, 34, 55, 0.05) 0 4px 6px -4px`. Eyebrow label in 12px Fricolage 575 uppercase letter-spacing 0.6px. Title in Mackinac 22px weight 500 letter-spacing -0.55px. Body in Fricolage 16px weight 325 line-height 1.50. Anchor with a hand-drawn illustration vignette (~280px) — a balloon, a swing, a ribbon, something playful and editorial."
- "Build a pricing-tab chip cluster — four service tabs (Compute, Networking, Storage, GPUs). Each tab uses `9999px 9999px 0px 0px` radius (top-only pill), white background, with a category-colored glow shadow: mint `rgba(16, 185, 129, 0.3)`, blue `rgba(59, 130, 246, 0.3)`, orange `rgba(249, 115, 22, 0.3)`, amber `rgba(245, 158, 11, 0.3)` at `0 20px 25px -5px, 0 8px 10px -6px`. Tab text in 14.5px Fricolage weight 450, color `#281950`."
- "Design a translucent dark-mode pill button for the closing CTA section — `rgba(255, 255, 255, 0)` background, `1px solid rgba(255, 255, 255, 0.25)` border, `9999px` radius, white 15.5px Fricolage weight 450 text. Hover flips to mint teal fill. Drop shadow `rgba(91, 33, 182, 0.1) 0 5px 5px -2px, 0 2px 4px -2px`."
- "Create a nav login chip — Fly Violet (`#7c3aed`) background, white text, asymmetric `8px 20px 20px 8px` ribbon-shaped radius, 14.5px Fricolage weight 450, indigo inset ring shadow."

### Iteration Guide
1. Default to Mackinac weight 500 for every headline; never reach for a heavier or lighter cut
2. Keep body at Fricolage Grotesque weight 325 — promoting it to 400 instantly wrecks the elegance
3. Buttons are pills (`9999px`) by default; use the ribbon (`8px 20px 20px 8px`) only for the persistent login chip
4. Apply the indigo inset ring (`rgba(67, 56, 202, 0.25) 0 0 0 1px inset`) wherever there's a violet button — it replaces the border
5. Lavender mist (`#e7e6f4`) is the canvas, aubergine (`#281950`) is the ink — neither plain white nor plain black ever appears as page background or text
6. Italicize Mackinac for emphasis, never bolden — italic is the only emphasis weight in the serif system
7. Hand-drawn illustrations are mandatory per major feature section — flat icons break the brand
8. Chromatic colors (orange/blue/mint/amber) live inside illustrations or as category shadows on pricing tabs — they don't appear in primary UI
9. Yellow underline hovers belong on dark gradient surfaces; violet underline hovers belong on light
10. Tall 1.50 line-heights are the default for everything — let the page breathe vertically
