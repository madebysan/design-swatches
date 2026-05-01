---
slug: ableton
name: Ableton
url: https://ableton.com
domain: ableton.com
category: Productivity
styles: [Light, Bold, Monochromatic]
tagline: "High-contrast digital studio. A canvas of stark black and white, illuminated by electric blue."
fonts: [futura-pt]
primary_color: "#0000ff"
---

# Design System Inspired by Ableton

> High-contrast digital studio. A canvas of stark black and white, illuminated by electric blue.

## 1. Visual Theme & Atmosphere

Ableton presents a digital canvas for creative tools, characterized by its stark, high-contrast monochrome base with strategic, vibrant accents. The primary palette of pitch black and pure white, occasionally softened by a flat light gray for input fields, is punctuated by a singular intense violet-blue (`#0000ff`) — the kind of saturated digital primary you'd find on a CRT or a synth's status LED. The result is energetic, almost electric, reflecting the dynamic nature of music production: tools first, decoration nowhere.

Typography is single-source: futura-pt does everything, from 90px display headlines down to 14px utility tags. The geometric letterforms are assertive and direct yet softened by their circular bowls, balancing technical instruction with visual approachability. There's no serif companion, no humanist body face — futura-pt's range of weights and sizes carries the entire typographic system. Headlines run weight 700 at 90px with line-height 1.0, creating tight architectural blocks; body text and UI labels relax into weight 400.

The shape language is uncompromising. Border-radius is `0px` everywhere — buttons, cards, inputs, tags — producing sharp-edged, hard-cornered components that feel less like web UI and more like printed broadcast graphics or a piece of hardware. Two warm/cool accent colors (Melody Red `#ff8389`, Synth Teal `#00d2be`) appear as flat categorization tags on content cards, deployed sparingly as pure functional labeling. The overall composition is utilitarian, product-focused, with full-bleed hero shots of hardware and software giving way to constrained 1200px content sections.

**Key Characteristics:**
- Stark monochrome base — pitch black (`#000000`) text on canvas white (`#ffffff`)
- Single saturated accent: Electric Violet (`#0000ff`) — reserved exclusively for primary CTAs and active nav states
- futura-pt as the sole typeface — geometric, single-family, weight-driven hierarchy
- Hero headlines at 90px weight 700, line-height 1.0 — architectural compression
- `0px` border-radius across the entire system — sharp edges as a defining signature
- No drop shadows, no gradients, no elevation effects — flat surfaces, pure contrast
- Two flat accent tags (Melody Red, Synth Teal) on content cards — categorization only
- Studio Gray (`#eeeeee`) for input field backgrounds — the only neutral mid-tone
- 10px element gaps and 69px section gaps — tight density punctuated by generous section breathing
- Imagery is utilitarian: tight product shots, studio environments, monochrome icons

## 2. Color Palette & Roles

### Background Surfaces
- **Canvas White** (`#ffffff`): Primary page background, default content surface.
- **Studio Gray** (`#eeeeee`): Input field backgrounds — the only mid-tone in the system.

### Text & Content
- **Midnight Ink** (`#000000`): Primary text, headlines, body, button labels on accent colors.

### Brand & Accent
- **Electric Violet** (`#0000ff`): The single brand accent. Primary CTA fills, active navigation links, hover states. Reserved for interactive elements only — never decorative.

### Categorization Tags
- **Melody Red** (`#ff8389`): Warm-side categorization badge on content cards.
- **Synth Teal** (`#00d2be`): Cool-side categorization badge on content cards.

## 3. Typography Rules

### Font Families
- **futura-pt** (substitute: Futura, Avenir): The sole typeface for all content. Geometric forms provide a technical yet approachable feel, integral to the brand's identity. Used at weight 400 for body and UI, weight 700 for display headlines. No secondary or fallback face within the system — futura-pt is the entire typographic identity.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Hero Display | futura-pt | 90px | 700 | 1.00 | normal |
| Heading | futura-pt | 32–48px | 700 | 1.10 | normal |
| Body | futura-pt | 16px | 400 | 1.50 | normal |
| Nav / UI Label | futura-pt | 16px | 400 | 1.40 | normal |
| Tag / Caption | futura-pt | 14px | 400 | 1.40 | normal |

### Principles
- **Single-family discipline**: futura-pt does everything. Hierarchy is built through weight (400 vs 700) and size, never family changes. The lack of a serif or humanist companion is intentional — it preserves the technical, instrumented feel.
- **Architectural display compression**: Hero headlines at 90px line-height 1.00 produce tight, blocky type that reads as printed signage rather than typeset prose.
- **Weight as voice, not size**: Most UI sits at weight 400 / 16px regardless of role — section headers, body, nav links are all the same size. The 700/90px display weight is a sharp jump, not a gradient.
- **Normal letter-spacing throughout**: Even at 90px display, futura-pt is set with normal tracking — the geometry doesn't need negative spacing to look composed.

## 4. Component Stylings

### Buttons

**Primary CTA Button (Electric Violet)**
- Background: `#0000ff`, Text: `#ffffff`, Border: none, Radius: `0px`
- Padding: `7px 30px`. Font: futura-pt 400 16px
- Used for primary conversion actions ('Try Live 12 free')

**Ghost Button**
- Background: transparent, Text: `#000000`, Radius: `0px`, no padding
- Used for inline tertiary actions, often paired with adjacent text

### Cards

**Basic Content Card**
- Background: transparent, Radius: `0px`, no shadow, `0px` padding
- Acts as a structural grouping without visual weight — the card itself adds nothing
- Visual hierarchy comes from the categorization tag placed above content, not from card chrome

### Categorization Tags

**Melody Red Tag**
- Background: `#ff8389`, Text: `#000000`, Radius: `0px`
- Padding: `1.96px 11.9px`. Font: futura-pt 400 14px
- Used for warm-side categorization (e.g., 'Downloads')

**Synth Teal Tag**
- Background: `#00d2be`, Text: `#000000`, Radius: `0px`
- Padding: `1.96px 11.9px`. Font: futura-pt 400 14px
- Used for cool-side categorization

The 1.96px vertical padding is unusually precise — these tags sit tight against their type, producing a printed sticker rather than a UI chip.

### Inputs

**Default Input Field**
- Background: `#eeeeee` (Studio Gray), Text: `#000000`, Border: none, Radius: `0px`
- Padding: `8px 15px`. Font: futura-pt 400 16px
- The flat gray fill on a white page provides the only contrast — there is no border ring

### Navigation

**Navigation Link**
- Text: `#000000` for default, `#0000ff` for active/hover
- Font: futura-pt 400 16px, no specific padding, relies on element spacing
- Color shift on hover is the only state indicator — no underline, no background fill

## 5. Layout Principles

### Spacing System
- **Element gap**: 10px — tight density between adjacent elements
- **Section gap**: 69px — generous vertical breathing between major sections
- **Card padding**: `0px` — cards are pure structural groupings
- The 10px → 69px jump is sharp; there's no mid-tier gap. Elements either sit close together or are separated by full section rhythm.

### Border Radius Scale
- **All components**: `0px`
- The system has no radius scale because it has no radii. Every button, card, input, and tag is hard-cornered.

### Grid
- **Max-width**: ~1200px centered for content sections
- Hero sections often break the constraint with full-bleed product imagery
- Content sections use 2-column or 3-column splits — text on one side, product image or nested cards on the other

### Layout & Composition
The page mixes full-bleed and constrained content. Hero sections are full-bleed with a centered headline overlaid on a product photograph. Subsequent sections use a ~1200px max-width centered container, breaking into two-column layouts (text + image) or 3-up grids (cards). Vertical rhythm relies on consistent section gaps (~69px). Navigation is a sticky top bar providing persistent access to product areas. Content arranges into visually digestible blocks — grids of 3 are common — keeping clutter minimal and emphasizing direct interaction with media and text.

## 6. Depth & Elevation

| Level | Hex | Name | Purpose |
|-------|-----|------|---------|
| 1 | `#ffffff` | Canvas White | Page background, default surface |
| 2 | `#eeeeee` | Studio Gray | Input field background — only mid-tone surface |

**Shadow Philosophy**: Ableton has no shadow system. The aesthetic relies entirely on flat, high-contrast surfaces — black on white, accent fills on neutral grounds. Elevation is communicated through nothing more than background contrast (white → light gray for inputs) and the saturated `#0000ff` of interactive elements punching through. Adding a drop-shadow would dilute the broadcast-graphic clarity that defines the system.

## 7. Do's and Don'ts

### Do

- Use Midnight Ink (`#000000`) for all primary text elements to ensure high contrast.
- Apply Canvas White (`#ffffff`) as the default background for content sections.
- Utilize Electric Violet (`#0000ff`) exclusively for primary interactive elements, such as CTA buttons and active navigation links, to draw attention.
- Maintain a consistent `0px` border-radius across all buttons, cards, and input fields for a sharp, unyielding aesthetic.
- Employ futura-pt throughout the UI, with variations in weight and size to create hierarchy while retaining brand consistency.
- Maintain minimal vertical padding of 1.96px for utility tags with a vibrant background and 7px for primary action buttons.

### Don't

- Avoid using drop shadows or complex gradients; the aesthetic relies on flat, high-contrast surfaces.
- Do not introduce additional rounded corners beyond `0px`; sharp edges are a defining characteristic.
- Do not deviate from the futura-pt typeface; alternative fonts will dilute the brand's typographic identity.
- Refrain from using Electric Violet (`#0000ff`) for purely decorative elements; reserve it for interactive or highlight states.
- Do not use background colors other than Canvas White (`#ffffff`) or Studio Gray (`#eeeeee`) for primary content containers; chromatic colors are for accents only.
- Avoid excessive spacing between elements; a comfortable but not overly sparse density is preferred, often using `10px` element gaps.

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single-column layout, hero scales down, full-bleed product images crop to portrait |
| md | 768px+ | Two-column splits return, 2-up card grids |
| lg | 1024px+ | Full 3-up card grids, hero returns to landscape full-bleed |
| xl | 1280px+ | Max-width 1200px applies, side margins grow |

### Touch Targets
- Primary buttons at `7px 30px` padding stay near the 40px minimum touch target on mobile
- Tag chips with `1.96px 11.9px` padding are decorative-scale — pair with adequate parent spacing on touch

### Collapsing Strategy
- Hero display 90px → ~60px → ~40px on mobile, line-height 1.0 maintained
- 3-column card grids collapse to 2-up at md, single column on mobile
- Section gaps compress from 69px to ~40px at mobile to preserve density without over-stretching
- Hero full-bleed imagery preserved at all sizes — the product shot is the atmosphere

## 9. Agent Prompt Guide

### Quick Color Reference
- Text: `#000000` (Midnight Ink)
- Background: `#ffffff` (Canvas White)
- CTA: `#0000ff` (Electric Violet)
- Border / button frame: `#000000` (where applicable)
- Accent tag (warm): `#ff8389` (Melody Red)
- Accent tag (cool): `#00d2be` (Synth Teal)
- Input background: `#eeeeee` (Studio Gray)

### Example Component Prompts

1. **Primary CTA Button**: background `#0000ff`, text `#ffffff`, futura-pt 400 16px, padding 7px 30px, border-radius 0px. Text 'Try Live 12 free'.
2. **Content Card with Tag**: transparent card background, 0px border-radius, no shadow. Above content, place a category tag: background `#ff8389`, text `#000000`, futura-pt 400 14px, padding 1.96px 11.9px. Tag text 'Downloads'.
3. **Hero Headline**: text `#000000`, futura-pt 700 90px, line-height 1.0, normal letter-spacing. Text 'Rent-to-own – now available for all upgrades'.
4. **Input Field**: background `#eeeeee`, text `#000000`, futura-pt 400 16px, padding 8px 15px, border-radius 0px. Placeholder 'Search...' in lighter text.
5. **Navigation Link**: text `#000000`, futura-pt 400 16px. On hover/active change text color to `#0000ff`. No underline. Text 'Shop'.

### Iteration Guide
1. futura-pt only — no companion face, no fallback for hierarchy.
2. `0px` border-radius is non-negotiable — sharp corners are the brand.
3. Electric Violet (`#0000ff`) is sacred — only on interactive elements, never decorative.
4. Flat surfaces only — never add shadows, gradients, or elevation effects.
5. Hero at 90px weight 700 line-height 1.0 — architectural compression is the headline voice.
6. Categorization tags (`#ff8389` / `#00d2be`) are warm/cool semantic pair — don't introduce a third.

## Preview

![Ableton](https://ysxnuuuj3kqhdyj2.public.blob.vercel-storage.com/1775924774685-thumb.jpg)
