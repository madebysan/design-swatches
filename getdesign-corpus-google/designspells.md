---
version: alpha
name: "Design Spells"
description: "Token-first design system reference for Design Spells."

colors:
  background: "#ffffff"
  surface: "#e7e5e4"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#78716c"
  primary: "#fafaf9"
  on-primary: "#ffffff"
  border: "#1c1917"
  focus-ring: "#fafaf9"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 96px
    fontWeight: 300
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 67px
    fontWeight: 300
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
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
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

# Design Spells Design System

## Overview

Design Spells is Brian Lovin's micro-interaction archive — short videos and GIFs documenting "details that feel like magic" in shipped products. The site itself practices what it curates: extreme typographic restraint that makes the embedded media the only color in the room. The page opens on a warm paper canvas (`#fafaf9` — Tailwind `stone-50`) and runs everything else in stone-grays and pure black. The defining gesture is a giant Fraunces serif headline at 96px weight 300, soft-italic in feel, set against an otherwise relentlessly utilitarian Inter UI. It reads like a literary journal that happens to be about UI craft.

The composition is a single-column reading column with a slim top nav, the oversized serif title block, then a vertical feed of spell entries — each a small thumbnail or video preview, a one-line description, the source app, and the contributor's name as a hairline-pill credit. There is no hero illustration, no marketing copy, no scroll animation. The page trusts the spells themselves to do the entertaining. Hover states are nearly invisible: links shift to a desaturated sky blue (`rgb(2, 132, 199)` — Tailwind `sky-600`), buttons gain a faint inner border ring. The chrome stays out of the way.

What distinguishes Design Spells most is the **pill-with-hairline-inset** treatment that runs through every interactive element. Buttons, tags, and contributor credits all share a single visual primitive: a `9999px` pill in stone-50 with a 1px inset shadow at `#e7e5e4` (stone-200) — no border, no drop shadow, no fill contrast. It's a hairline, drawn from the inside, on a near-white surface. This single gesture, repeated 19 times on the homepage, is the entire design system's stamp. Combined with the Fraunces-meets-Inter pairing and the stone palette, the site feels like a quiet, slightly bookish blog where each post is a five-second video.

**Key Characteristics:**
- Fraunces at 96px weight 300 for the marquee title — serif elegance over grotesk authority
- Inter at weight 400 for everything else (nav, body, button labels, captions) — invisible UI font
- Stone palette only (`#fafaf9` page, `#1c1917` text, `#78716c` muted, `#292524` deep) — zero brand color
- Pill radius (`9999px`) with inset 1px hairline (`#e7e5e4`) — the signature surface
- Sky-600 (`#0284c7`) link hover — the only chromatic accent in the system
- Single-column reading layout — no sidebar, no grid, no decorative chrome
- Embedded video/GIF spells carry all the visual energy — chrome stays neutral
- Editorial pacing — generous 80px and 128px section gaps between major blocks

## Colors

### Primary
- **Spell Black** (`#000000`): Pure black for headline title text and high-emphasis labels. Appears 80 times — the workhorse text color.
- **Spell Stone** (`#1c1917` — Tailwind `stone-900`): Primary body and link color. Slightly warmer than pure black, used for paragraphs, button labels, and most body copy.
- **Paper** (`#fafaf9` — Tailwind `stone-50`): Page background. A warm off-white that reads as printed paper, not screen.

### Brand Accent
- **Sky Hover** (`rgb(2, 132, 199)` — Tailwind `sky-600`): Link hover color. The only saturated color in the entire system. Appears only when a cursor lands on a link.

### Neutrals & Text
- **Stone Muted** (`#78716c` — Tailwind `stone-500`): Secondary text — contributor credits, timestamps, source labels. Often paired with weight 600 for tag-like roles.
- **Stone Light** (`#a8a29e` — Tailwind `stone-400`): Tertiary text — hints, footer copy, deemphasized metadata.
- **Stone Border** (`#e7e5e4` — Tailwind `stone-200`): Hairline inset shadow color — the pill outline.
- **Stone Bg** (`#e5e7eb` — Tailwind `gray-200`): Filled pill backgrounds for secondary tags and avatar slots. The most-used color on the page (159 occurrences) but always as quiet surface.

### Surface & Borders
- **Card Surface** (`#fafaf9`): Default card and button background — same as page. Surfaces are revealed by the inset hairline, not by a fill change.
- **Inverted Surface** (`#292524` — Tailwind `stone-800`): Reserved for dark mode and rare inverted moments (footer, code blocks).
- **Pure White** (`#ffffff`): Hover-state surface accents at 80% and 95% opacity — used sparingly for subtle lift moments.

### Shadow Colors
- **Inset Hairline** (`rgb(231, 229, 228)`): The signature `0 0 0 1px inset` line that draws every pill and card edge.
- **Lift Shadow** (`rgba(0, 0, 0, 0.1)`): Used in `0px 20px 25px -5px` plus `0px 8px 10px -6px` Tailwind `shadow-xl` pattern — applied only to one elevated card or modal at a time.

### Gradient System
- Design Spells is **gradient-free**. Every surface is a flat stone-tone. Color depth comes from the inset hairline, never from a fill ramp. The only "gradient" feeling on the page is the natural color of the embedded videos themselves.

## Typography

### Font Family
- **Display**: `Fraunces`, fallback `serif` — variable serif from Google Fonts, used at weight 300 only
- **UI / Body**: `Inter`, fallback `sans-serif` — variable sans, weights 400 and 600
- **OpenType Features**: Fraunces is set with default optical sizing — no custom variation axes pushed. Inter uses default features only.

*Note: Fraunces is a variable serif by Undercase Type, free via Google Fonts. Inter is Rasmus Andersson's open-source workhorse, also free via Google Fonts. The pairing is editorial-blog standard — the personality lives in Fraunces.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Title | Fraunces | 96px (6.00rem) | 300 | 1.00 | -2.4px | The marquee — page title, set once |
| Page H1 (mobile) | Inter | 36px (2.25rem) | 700 | 1.11 | -1.8px | Mobile fallback for marquee — bolder, tighter |
| Section Heading | Inter | 30px (1.88rem) | 400 | 1.20 | normal | Mid-page section markers |
| Sub-heading | Inter | 24px (1.50rem) | 400 | 1.33 | -1.2px | Spell-detail page titles |
| Body / Nav | Inter | 16px (1.00rem) | 400 | 1.50 | -0.4px | Standard reading text and nav links |
| Button Label | Inter | 16px (1.00rem) | 400 | 1.50 | -0.8px | Primary CTA labels — slight extra negative tracking |
| Tag / Caption Strong | Inter | 14px (0.88rem) | 600 | 1.25 | -0.35px | Contributor credits, source-app pills |
| Caption | Inter | 14px (0.88rem) | 400 | 1.25–1.43 | -0.35px / normal | Metadata, timestamps |

### Principles
- **Fraunces is sacred**: weight 300 only, used exactly once per page as the marquee title at 96px. Never use Fraunces below 48px — it loses its character at small sizes.
- **Inter does everything else**: body, nav, buttons, captions, tags. The system is binary — display serif or UI sans, no in-between.
- **Aggressive negative tracking on display**: Fraunces at 96px runs `-2.4px` letter-spacing — about `-2.5%`. Inter scales tighter with size: `-1.8px` at 36px, `-1.2px` at 24px, `-0.8px` at button size, `-0.4px` at 16px, `-0.35px` at 14px.
- **Tight serif line-height**: The Fraunces title runs at 1.00 line-height — a single dense block. Inter body sits at 1.50 for comfortable reading.
- **Two-weight Inter**: 400 default, 600 for tags and emphasis. No Inter bold (700) anywhere except the mobile-fallback H1.
- **No uppercase**: every text element runs in mixed case. No CAPS chrome, no tracked-out labels — the system is sentence-case throughout.

## Layout

### Spacing System
- Base unit: `4px` (Tailwind default)
- Scale: 4px, 8px, 16px, 24px, 32px, 80px, 128px
- Most-used: 4px (50 occurrences) for tight chrome and 8px (20 occurrences) for component padding
- The big jump from 32px to 80px is intentional — small details and large section breaks, no awkward middle ground
- 128px reserved for the marquee-to-feed transition — the only place that gets the maximum air

### Grid & Container
- Single-column max-width approximately 720–800px for the spell feed (reading column)
- The marquee Fraunces title spans wider — up to 960–1080px
- No sidebar. No 2-column. No 3-column grid. The site is a vertical scroll of entries.
- Mobile: the same single column, same padding, same hierarchy — just scaled type

### Whitespace Philosophy
- **Editorial pacing**: 80px between spell sections, 128px between the title block and the feed — the page reads like a literary magazine with one giant title and a quiet list
- **Tight inside, generous outside**: components are compact (`4px 12px` padding) but section gaps are huge (`80px+`). The eye rests between entries, never inside them.
- **No decorative dividers**: section breaks happen through whitespace alone. No horizontal rules, no background-color alternations.

### Border Radius Scale
- Sharp-ish (`2px`): hairline frames around small thumbnails — 16 occurrences
- Standard (`4px`): occasional softening — 4 occurrences
- Container (`8px`): default for cards and inputs — 18 occurrences
- Editorial (`16px`): one-off larger surfaces — 1 occurrence
- Pill (`9999px`): every button, every tag, every avatar — 24 occurrences (most-used)
- The system favors the extremes: pills for chrome, 8px for content surfaces. 16px+ is rare.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, body text, large surfaces |
| Hairline (Level 1) | `rgb(231, 229, 228) 0 0 0 1px inset` | Buttons, pills, tags, input borders — the workhorse |
| Lift (Level 2) | `rgba(0, 0, 0, 0.1) 0 20px 25px -5px, rgba(0, 0, 0, 0.1) 0 8px 10px -6px` | Reserved for one elevated element per view (modal, hover-revealed card) |
| Focus Ring (Level 3) | `outline: rgb(28, 25, 23) none 3px` | Keyboard focus on interactive elements |

**Shadow Philosophy**: Design Spells uses a single shadow primitive — the inset hairline — as both border and depth. This collapses what most systems split into `border-color`, `box-shadow`, and `outline-color` into one declaration. The result is a visually quieter page: surfaces don't lift off the canvas, they're drawn onto it. When real elevation is required (a modal, a hover-revealed card), the system reaches for Tailwind's `shadow-xl` recipe — a soft, atmospheric drop with both close and far shadow stops. But this is rare. On a typical homepage view, the only depth is the hairline.

### Decorative Depth
- The inset hairline pairs with the pill radius to create a "drawn label" feel — tags read as engraved into the paper, not stuck on top
- No glow effects, no glass blur, no color-tinted shadows
- Hover does not change elevation — only link color shifts. The page does not "lift" interactively.

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

**Default Pill (the only button)**
- Background: Paper (`#fafaf9`)
- Text: Spell Stone (`#1c1917`)
- Padding: `4px 12px` (compact) — `py-1 px-3` in Tailwind
- Radius: `9999px` (full pill)
- Border: `0px solid` — no actual border
- Shadow: `rgb(231, 229, 228) 0px 0px 0px 1px inset` — the hairline inset
- Font: 16px Inter weight 400, no transform, `-0.8px` letter-spacing
- Hover: link color shifts to `rgb(2, 132, 199)`; surface stays neutral
- Outline: `rgb(28, 25, 23) none 3px` for keyboard focus
- Use: Every button on the site — submit, login, follow, view all. There is no primary/secondary distinction.

**Inverted Pill (rare)**
- Background: Stone-800 (`#292524`)
- Text: Paper (`#fafaf9`)
- Same `9999px` radius, same `4px 12px` padding
- No shadow — the dark fill carries the contrast
- Use: Footer or dark-mode contexts only

### Cards & Containers
- Background: Paper (`#fafaf9`) — matches the page
- Border: `0px` default — surfaces appear via the inset hairline
- Radius: typically `8px` for spell-row containers, `2px` for hairline frames around video previews, `9999px` for circular avatar slots
- Shadow: usually flat — when elevation is needed, use the Tailwind `shadow-xl` recipe (`rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px`) and apply to exactly one card at a time
- Internal padding: 16–32px — generous for reading, never cramped

### Badges / Tags / Pills

**Hairline Pill (default)**
- Background: Paper (`#fafaf9`) or Stone-Bg (`#e5e7eb`)
- Text: Spell Stone (`#1c1917`) or Stone Muted (`#78716c`)
- Padding: `4px 12px`
- Radius: `9999px`
- Border: `0px` — uses inset shadow `0 0 0 1px #e7e5e4`
- Font: 14px Inter weight 600 (or 400), `-0.35px` tracking
- Use: Source-app credits, contributor names, category markers — the page is structured around these

**Filled Stone Pill**
- Background: Stone-Bg (`#e5e7eb`)
- Text: Stone Muted (`#78716c`)
- Same `9999px` radius
- No shadow — the fill differentiates
- Use: Quieter tag variant, used as background pill for avatar slots

### Inputs & Forms
- Background: Paper (`#fafaf9`) or pure white (`#ffffff`)
- Border: `0px` with the inset hairline shadow `0 0 0 1px #e7e5e4` — same primitive as buttons
- Radius: `8px` for text inputs (slightly less round than buttons)
- Font: 16px Inter weight 400, `-0.4px` tracking
- Text color: Spell Stone (`#1c1917`)
- Focus: outline shifts to `rgb(28, 25, 23) none 3px` — sharp keyboard ring
- Padding: 8–12px vertical, 12–16px horizontal

### Navigation
- Top nav: thin horizontal bar — Design Spells wordmark left, a few text links right (Submit, About, RSS)
- Links: Inter 16px weight 400, `#000000`
- Hover: color shifts to Sky-600 (`rgb(2, 132, 199)`) — the only color event in normal browsing
- No dropdowns, no mega-menus — the nav is a flat list of three to four items
- Sticky behavior: nav stays at top; the spell feed scrolls beneath

### Decorative Elements

**Hairline Inset**
- `rgb(231, 229, 228) 0px 0px 0px 1px inset` — applied to 19 elements per page
- Used on every pill, button, tag, and bordered card
- Replaces both `border: 1px solid` and `box-shadow: 0 1px 2px` in the system — one primitive, one purpose

**Embedded Video Frame**
- Each spell entry hosts an MP4 or GIF preview, often autoplaying on hover
- Frame radius: `8px` typically, `2px` for tight chrome moments
- No drop shadow on the video — it sits flat on Paper
- Aspect ratios vary (the source product determines them) — the site does not normalize

## Do's and Don'ts

### Do
- Use Fraunces at weight 300 for exactly one title per page — it's the marquee
- Set everything else in Inter weight 400, with weight 600 for tag emphasis
- Apply the hairline inset (`0 0 0 1px #e7e5e4`) as the universal border primitive
- Use `9999px` pill radius for every interactive chrome element
- Use Sky-600 (`#0284c7`) only on link hover — preserve its singularity
- Keep the page in a single reading column — no sidebars, no grids
- Use 80–128px gaps between major sections — the editorial pace is the brand
- Let embedded videos and GIFs carry the color and energy
- Use Stone-200 (`#e7e5e4`) for the inset hairline — never gray-300 or darker
- Use mixed-case throughout — no uppercase chrome

### Don't
- Don't use Fraunces below 48px — it loses character and looks dated
- Don't use weight 500 or 700 on Fraunces — only weight 300
- Don't introduce a brand color anywhere except link hover — the system is intentionally chromatic-free
- Don't add `border: 1px solid` — always use the inset shadow instead
- Don't use mid-radius values like 12px or 24px — the system is `2/8/9999` with rare `4` and `16`
- Don't apply `shadow-xl` lift to multiple elements at once — only one elevated surface per view
- Don't pair the Fraunces title with a Fraunces subtitle — the serif appears once and yields to Inter
- Don't use Stone-50 (`#fafaf9`) on Stone-50 — surfaces need the inset hairline to register
- Don't add gradients, glows, or glass blur — the page is flat by intent
- Don't use a sidebar or multi-column layout — the single column is the format

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Fraunces title drops to 36–48px, padding reduces to 16px |
| Tablet | 640–768px | Title at 56–72px, padding at 24px |
| Desktop | 768–1024px | Title at 72–96px, full marquee weight |
| Large Desktop | 1024–1280px | Maximum scale, 80–128px section gaps |
| XL | ≥1280px | Same content; reading column stays ~800px max — extra space becomes margin |

### Touch Targets
- Pill buttons at `4px 12px` are below the 44px minimum at default size — increase vertical padding to 8–10px on mobile to hit the tap target
- Nav links: inline text, increase padding to 12px vertical on mobile for thumb reach
- Spell entries: full-width tap targets on mobile — the entire row is interactive

### Collapsing Strategy
- **Title**: 96px → 36–48px on mobile, switching from Fraunces weight 300 to Inter weight 700 if needed for legibility — but Fraunces preferred at 48px+ if it holds
- **Section spacing**: 128px → 48px on mobile — reduces but maintains editorial breathing
- **Reading column**: stays single-column at all sizes — the layout is responsive by being inherently linear
- **Video previews**: maintain aspect ratio, fill column width on mobile
- **Letter-spacing**: scales proportionally — the negative tracking values are intentional at every size

### Image Behavior
- Spell preview videos and GIFs maintain their native aspect ratios
- No art direction changes — the same media adapts to smaller viewports
- Autoplay-on-hover behavior degrades to tap-to-play on touch devices

---

## Agent Prompt Guide

### Quick Color Reference
- Page Background: Paper (`#fafaf9`)
- Primary Text: Spell Stone (`#1c1917`)
- Display Title: Pure Black (`#000000`)
- Muted Text: Stone Muted (`#78716c`)
- Tertiary Text: Stone Light (`#a8a29e`)
- Hairline Inset: Stone-200 (`#e7e5e4`)
- Filled Pill Bg: Stone-Bg (`#e5e7eb`)
- Link Hover: Sky-600 (`rgb(2, 132, 199)`)
- Lift Shadow: `rgba(0, 0, 0, 0.1) 0 20px 25px -5px, rgba(0, 0, 0, 0.1) 0 8px 10px -6px`
- Hairline Shadow: `rgb(231, 229, 228) 0 0 0 1px inset`

### Example Component Prompts
- "Create a marquee title block on Paper (`#fafaf9`) with a single line of Fraunces 96px weight 300, line-height 1.00, letter-spacing -2.4px, color `#000000`. Center it in an 800px reading column with 128px of bottom margin."
- "Design a pill button — background `#fafaf9`, text `#1c1917`, padding `4px 12px`, radius `9999px`, no border, shadow `rgb(231, 229, 228) 0 0 0 1px inset`. Inter 16px weight 400, letter-spacing `-0.8px`. Hover: text color shifts to `rgb(2, 132, 199)`, surface stays the same."
- "Build a spell-feed entry — full-width row in single column, 24px vertical padding. Left: 8px-radius video thumbnail at 96×96px. Right: title in Inter 16px weight 400 black, source app in Inter 14px weight 600 stone-500, contributor pill (hairline-inset, `4px 12px`)."
- "Create a hairline tag pill — Paper (`#fafaf9`) bg, `#1c1917` text, `4px 12px` padding, `9999px` radius, no border, inset shadow `0 0 0 1px #e7e5e4`. Inter 14px weight 600, letter-spacing `-0.35px`."
- "Design an elevated modal card — Paper (`#fafaf9`) bg, 16px radius, padding 32px, shadow `rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px`. This is the only lifted element on screen."

### Iteration Guide
1. Default to Inter weight 400 for everything — Fraunces appears exactly once per page as the marquee
2. Keep radius binary: `9999px` for chrome (pills, buttons, tags), `8px` for content (cards, inputs, frames). Avoid mid-range values.
3. Use the hairline inset shadow (`0 0 0 1px #e7e5e4`) as the universal border. Never `border: 1px solid` — always inset shadow.
4. Sky-600 (`rgb(2, 132, 199)`) is the only chromatic color in the system — applied only to link hover
5. Negative letter-spacing scales with size: `-2.4px` at 96px, `-1.8px` at 36px, down to `-0.35px` at 14px
6. Stay in stone tones: `#fafaf9` page, `#1c1917` text, `#78716c` muted, `#292524` deep — no warm reds, no cool blues
7. Single-column layout always — no sidebars, no grids. Editorial reading rhythm is the brand.
8. Let embedded media (videos, GIFs, screenshots) carry visual energy — chrome stays neutral, content provides color
