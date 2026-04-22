# Design System Inspired by Cape

## 1. Visual Theme & Atmosphere

Cape's website is precision-engineered minimalism in service of a serious topic: personal privacy and secure cellular service. The page opens on a warm off-white canvas (`#f5f5f5`) that deliberately avoids the sterile pure-white of typical privacy/security sites. Everything is built around an oversized grotesk headline, deep black body, and a single saturated lavender accent (`#9891e1`) that functions as a stamp — applied sparingly to signup CTAs, focus states, and occasional decorative moments. The overall impression is of a Swiss-inspired privacy brand that trusts typography to do the work most sites delegate to illustration.

The custom `FK Grotesk` typeface is the defining element of Cape's visual identity. Every display-size heading runs at weight 300 — an unusually light weight for a privacy/security brand, where the convention is bold reassurance. Cape chooses the opposite: whisper-confident headlines at 105px with negative letter-spacing (`-0.2px` at display, up to `-1%` at mid sizes) and tight 1.00 line-height. The letterforms themselves carry the brand — structured, engineered, and almost architectural in the way they lock to the grid. Where competitors use large colorful hero illustrations, Cape uses only type and a product photograph; the confidence comes from restraint.

What distinguishes Cape most is its **shadow system**. Rather than soft diffuse drop shadows, Cape uses hard offset shadows — `-3px 3px 0 white` and `-4px 4px 0 black` — that create a dimensional, rubber-stamp effect. These are not elevation shadows in the traditional sense; they're graphic stamps that give interactive elements a tactile, almost printed quality. Combined with sharp 0-radius corners on most elements and the occasional fully-pill (`9999px`) circular element, Cape's system feels editorial and mechanical at the same time.

**Key Characteristics:**
- FK Grotesk at weight 300 for all display and heading text — confident lightness over bold reassurance
- Warm off-white canvas (`#f5f5f5`) — deliberately not pure white, avoiding sterile tech aesthetic
- Lavender stamp accent (`#9891e1`) used exclusively for signup CTAs and focus moments
- Hard offset shadows (`-4px 4px 0 black`) — rubber-stamp depth, not atmospheric lift
- Sharp 0-radius corners on most surfaces; pill (`9999px`) reserved for circular nav elements
- Tight negative letter-spacing scaling from `-0.2px` at display down to `-1%` at body
- Video/photograph hero moments — product imagery drops directly into layout without chrome
- Large-scale type as the primary visual structure — typography IS the illustration

## 2. Color Palette & Roles

### Primary
- **Cape Black** (`#000000`): Primary text, headings, body copy, secondary button backgrounds. Pure black — Cape does not soften its primary text color.
- **Cape Off-White** (`#f5f5f5`): Primary page background. A warm neutral that reads as paper rather than screen.
- **Pure White** (`#ffffff`): Reserved for inverted surfaces, button text on dark, offset shadow highlights.

### Brand Accent
- **Cape Lavender** (`#9891e1`): The signature accent — applied to primary CTAs ("SIGN UP"), focus outlines, and selected-state indicators. The only chromatic color in the system.
- **Pale Lilac** (`#e9e4f4`): A tinted surface variant of lavender for background panels, badge fills, and soft lavender-themed containers. Used sparingly.

### Neutrals & Text
- **Cape Black** (`#000000`): All primary text — headings, body, nav links, button labels.
- **Deep Focus Slate** (`rgba(43, 51, 63, 0.75)`): Hover text color — a desaturated blue-gray that creates a subtle "pressed" sensation.
- **Focus Gray** (`rgba(115, 133, 159, 0.5)`): Focus-state background tint — a cool blue-gray at 50% opacity for keyboard-focus feedback.

### Surface & Borders
- **Surface Off-White** (`#f5f5f5`): Default panel background — matches page canvas.
- **Border Black** (`#000000`): Full-weight 1px borders around circular pill elements and framed containers.
- **Border Transparent** (`rgba(0, 0, 0, 0)`): Default-state border on ghost buttons, becomes visible on hover.

### Shadow & Stamp Colors
- **Stamp Black** (`rgb(0, 0, 0)`): Hard offset shadows on buttons and cards — `-4px 4px 0 0` for the rubber-stamp effect.
- **Stamp White** (`rgb(255, 255, 255)`): Inverted stamp shadow — `-3px 3px 0 0` on dark-surface elements.
- **Shadow Focus Black** (`rgba(0, 0, 0, 0.1)`): Soft drop shadow on focus states — `0px 4px 12px` for subtle elevation.
- **Shadow Focus Ring** (`rgba(0, 0, 0, 0.2)`): Focus ring halo — `0px 0px 0px 2px` for keyboard accessibility.

### Gradient System
- Cape is **gradient-free**. The system relies on solid-color relationships, hard offset shadows, and high contrast. No gradient fills anywhere — the lavender accent is always solid `#9891e1`.

## 3. Typography Rules

### Font Family
- **Primary**: `FK Grotesk`, with fallback: `Arial`, `sans-serif`
- **Monospace / Technical**: Same `FK Grotesk` in uppercase with wider tracking, used for button labels and UI chrome
- **OpenType Features**: Standard ligatures only — no stylistic sets or feature exotica. The typeface itself carries the character.

*Note: FK Grotesk is a commercial typeface from Florian Karsten Typefaces. For external implementations, Neue Haas Grotesk Display or Söhne serve as close substitutes; Inter at low weight works as a web-safe alternative.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | FK Grotesk | 105px (6.56rem) | 300 | 1.00 (tight) | -0.2px | Maximum size — landing hero statements |
| Display Large | FK Grotesk | 56px (3.50rem) | 300 | 1.00 | -0.2px | Secondary hero, full-width section heads |
| Display | FK Grotesk | 48px (3.00rem) | 300 | 1.00–1.20 | -1% | Primary feature section titles |
| Section Heading | FK Grotesk | 40px (2.50rem) | 300 | 1.00 | -1% | Feature sub-section heads |
| Sub-heading Large | FK Grotesk | 36px (2.25rem) | 300 | 1.00–1.25 | -1% / -0.24px | Card titles, sub-section markers |
| Sub-heading | FK Grotesk | 28px (1.75rem) | 300 | 1.00 | -1% | Smaller section heads, pull quotes |
| Sub-heading Small | FK Grotesk | 24px (1.50rem) | 300–400 | 1.08–1.30 | -0.2px / -0.24px | Feature titles, small card heads |
| Body Large | FK Grotesk | 20px (1.25rem) | 300 | 1.30 | -0.2px | Intro paragraphs, emphasized body text |
| Body | FK Grotesk | 16px (1.00rem) | 300–400 | 1.40 | normal | Standard reading text |
| Nav Link | FK Grotesk | 16px (1.00rem) | 400 | 1.00 | normal | Top navigation links |
| Button UI | FK Grotesk | 12px (0.75rem) | 400 | 1.00 | 0.05em | Button labels, UI chrome (often uppercase) |
| Caption | FK Grotesk | 12–14px | 400 | 1.33–1.50 | normal | Small metadata, legal text |
| Caption Small | FK Grotesk | 10px (0.63rem) | 400 | 1.00 | normal | Micro labels, timestamps |

### Principles
- **Weight 300 as signature**: Every display-size heading uses weight 300. Where security/privacy brands default to bold reassurance, Cape communicates trust through precision instead of weight. The lightness is the confidence.
- **Progressive negative tracking**: Letter-spacing tightens proportionally with size — from `-1%` at 48px down to `-0.2px` at 20px. Below body size, tracking returns to normal for readability.
- **Tight display line-height**: Headings run at 1.00–1.20 line-height — unusually tight for 48px+ display type. This locks headlines into dense engineered blocks rather than airy editorial passages.
- **Two-weight simplicity**: Weight 300 for display and body, weight 400 for UI and nav. No bold (700) anywhere in display. The typeface character is enough.
- **Uppercase for chrome**: Button labels and certain UI indicators ("SIGN UP", "LOG IN") use uppercase at small sizes, creating a clear distinction between content (mixed case) and action (uppercase). Often paired with mono-like spacing conventions.

## 4. Component Stylings

### Buttons

**Primary Lavender**
- Background: Cape Lavender (`#9891e1`)
- Text: Cape Black (`#000000`)
- Padding: asymmetric — 8px 16px compact, 12px 24px standard
- Radius: `0px` (sharp rectangular)
- Border: `0px` default, `1px solid #000` on hover
- Shadow: `-4px 4px 0 0 #000` — hard offset black stamp shadow
- Font: 12px FK Grotesk weight 400, uppercase, letter-spacing `0.05em`
- Hover: background shifts to `rgba(50, 50, 50, 0.9)`, text to `rgba(43, 51, 63, 0.75)`
- Use: Primary CTA — "SIGN UP", "BUY A PHONE", "GET STARTED"

**Black Inverted**
- Background: Cape Black (`#000000`)
- Text: Pure White (`#ffffff`)
- Padding: 8px 16px
- Radius: `0px`
- Shadow: `-3px 3px 0 0 #fff` on dark surfaces — inverted offset stamp
- Hover: background shifts to `rgba(50, 50, 50, 0.9)`
- Use: Secondary CTAs on light backgrounds, video player controls

**Pale Lilac Panel**
- Background: Pale Lilac (`#e9e4f4`)
- Text: Cape Black (`#000000`)
- Radius: `0px`
- Shadow: `-4px 4px 0 0 #000`
- Use: Tinted-surface button variant — informational CTAs where lavender primary would be too strong

**Off-White Ghost**
- Background: Cape Off-White (`#f5f5f5`)
- Text: Cape Black (`#000000`)
- Radius: `0px`
- Border: `0px solid #000000` default, transitions to visible on hover
- Use: Tertiary/low-emphasis actions on the off-white canvas

**Circular Pill (Navigation Dots)**
- Background: transparent or `#000`
- Size: 12px × 12px
- Radius: `9999px`
- Border: `1px solid #000`
- Transform: `matrix(1.1, 0, 0, 1.1, 0, 0)` on active — 10% scale emphasis
- Use: Pagination dots, selection indicators, circular navigation UI

### Cards & Containers
- Background: `#f5f5f5` (off-white) on light sections; `#000000` on dark/video overlays
- Border: `0px` default — cards rely on space, not frames
- Radius: `0px` for rectangular content containers; `9999px` only for circular/pill elements
- Shadow: hard offset (`-4px 4px 0 0 #000`) for "stamped" card treatment; `none` for structural containers
- Internal padding: generous — 32–64px for feature cards, reflecting editorial air

### Badges / Tags / Pills
**Lavender Badge**
- Background: Cape Lavender (`#9891e1`)
- Text: Cape Black (`#000000`)
- Padding: 2.4px 8px
- Radius: `0px` or `9999px` depending on decorative vs status use
- Font: 12px FK Grotesk weight 400

**Outline Pill**
- Background: transparent
- Text: Cape Black (`#000000`)
- Border: `1px solid #000000`
- Radius: `9999px`
- Use: Category markers, feature tags in navigation panels

### Inputs & Forms
- Background: `#ffffff` or `#f5f5f5`
- Border: `1px solid #000000`
- Radius: `0px` or `3px` (nearly sharp)
- Font: 16px FK Grotesk weight 400
- Text color: `#000000`
- Focus: `rgba(115, 133, 159, 0.5)` background tint + focus ring `rgba(0, 0, 0, 0.2) 0px 0px 0px 2px`
- Padding: 10–16px vertical, 12–16px horizontal

### Navigation
- Top nav: horizontal white bar, left-aligned Cape logo (SVG wordmark), right-aligned "SIGN UP" (Lavender) and "LOG IN" (ghost) CTAs
- Hover menus: large multi-column panels that drop from the top nav, filled with feature lists and links
- Links: FK Grotesk 16px weight 400, `#000000`
- Hover: text color shifts to desaturated `rgba(43, 51, 63, 0.75)`
- Sticky behavior: nav remains fixed at top, video/imagery scrolls beneath

### Decorative Elements

**Offset Stamp Shadow**
- `-4px 4px 0 0 #000` (default direction) or `-3px 3px 0 0 #fff` (inverted)
- Applied to: primary CTAs, feature cards, emphasized content blocks
- Creates a 3D "printed" quality — the signal that this element is interactive or important

**Full-Bleed Video/Image**
- Hero product shots and cinematic imagery fill the viewport edge-to-edge
- Text overlays sit on the image without gradient scrims — trust in the image composition
- Used for product hero, testimonial backgrounds, "Meet the team" moments

## 5. Layout Principles

### Spacing System
- Base unit: 8px (with 2.4px as a compact sub-unit for tight UI)
- Scale: 2.4px, 6px, 8px, 10px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px
- Notable: The scale has a compact end (2.4px–10px) for chrome/UI and a generous end (64px+) for section spacing. Mid-range values (20–30px) are used sparingly — Cape either sits tight or breathes wide.

### Grid & Container
- Max content width: approximately 1200px for centered content
- Hero: full-width or two-column (text left, image/video right)
- Feature sections: single-column statements, or 2-column feature pairs
- Full-bleed dark sections alternate with the off-white canvas for immersive product moments
- Content regularly breaks the container on video/imagery sections for full cinematic effect

### Whitespace Philosophy
- **Editorial pacing**: Each section gets significant vertical breathing room (100–200px between majors) — the page reads like a well-laid magazine spread
- **Type-anchored rhythm**: Sections are paced by their headline weight. A 105px headline needs 160px of air above and below; an 16px body paragraph only needs 24px
- **Dark/light alternation**: Off-white canvas sections alternate with full-bleed video/dark imagery — creating chapter-like breaks without requiring decorative dividers

### Border Radius Scale
- Sharp (0px): Default for buttons, cards, containers, badges, inputs — the workhorse radius
- Minimal (2–3px): Occasional soft edge on certain specialty containers
- Pill (9999px): Circular navigation dots, avatars, toggle indicators, image crops
- No mid-range radii: Cape does not use 4–16px values. The system is binary — sharp rectangular or fully circular.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no inset | Page canvas, body text, structural containers |
| Inset Line (Level 1) | `rgb(0,0,0) 0px 0px 0px 0px inset` | Button baseline state — primes the hover/focus shadow transition |
| Offset Stamp (Level 2) | `-4px 4px 0 0 #000` (default) or `-3px 3px 0 0 #fff` (inverted) | Primary CTAs, emphasized cards — the signature stamp treatment |
| Focus Halo (Level 3) | `rgba(0,0,0,0.1) 0px 4px 12px, rgba(0,0,0,0.2) 0px 0px 0px 2px` | Keyboard focus on interactive elements |
| Glow Ring (Level 4) | `rgb(255,255,255) 0px 0px 1em` | Video player / dark-surface focus states |

**Shadow Philosophy**: Cape's depth system is graphic, not atmospheric. Where most sites use blurred drop shadows to simulate physical elevation, Cape uses hard-edged offset shadows that read as graphic stamps — the kind you'd see on a risograph print or a hand-set letterpress piece. The `-4px 4px 0 0` pattern has no blur radius and no spread — it's a pure color rectangle offset from its parent. This creates a flat, printed quality that echoes the grotesk-on-paper ethos of the rest of the system. When soft shadows appear, they're reserved for focus/hover states and remain subtle.

### Decorative Depth
- Offset stamps pair with the sharp 0-radius corners to create a cohesive "printed graphic" feel
- Inset shadows (`0 0 0 0 inset`) are used as baseline state declarations so transitions to offset shadows feel physical
- No ambient/glow effects except on dark video surfaces where a subtle `0 0 1em` white glow signals focus

## 7. Do's and Don'ts

### Do
- Use FK Grotesk weight 300 for every display and heading size — lightness is the brand voice
- Apply Cape Lavender (`#9891e1`) only to primary CTAs and focus states — preserve its stamp quality
- Use hard offset shadows (`-4px 4px 0 0`) for the signature rubber-stamp depth effect
- Keep corner radius at `0px` for all rectangular surfaces — sharpness is intentional
- Use `9999px` pill radius only for genuinely circular elements (dots, avatars, toggles)
- Apply tight negative letter-spacing (`-1%` to `-0.2px`) on display-size headings
- Use uppercase with `letter-spacing: 0.05em` for button labels and UI chrome
- Alternate off-white sections with full-bleed dark/video sections for chapter-like pacing
- Let typography do the illustration work — avoid decorative icons or graphic flourishes

### Don't
- Don't use weight 500–700 on FK Grotesk headings — weight 300 is the ceiling
- Don't introduce mid-range border-radius (4–16px) — the system is binary (sharp or pill)
- Don't use blurred drop shadows for depth — the signature is hard offset stamps
- Don't use pure white (`#ffffff`) for the page background — always off-white (`#f5f5f5`)
- Don't saturate with the lavender accent — one or two applications per screen maximum
- Don't introduce other chromatic colors — the system is mono + lavender only
- Don't use lightweight body text on lavender backgrounds — contrast with black for legibility
- Don't add gradient fills anywhere — Cape is solid-color only
- Don't use large hero illustrations — product photography or video fills that role

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero type drops to 36–48px |
| Mobile | 375–650px | Single-column, 48–56px hero, stacked CTAs |
| Tablet | 650–1000px | 2-column grids begin, 56–72px hero |
| Desktop | 1000–1269px | Full multi-column layouts, 72–90px hero |
| Large Desktop | ≥1269px | Maximum type scale (105px hero), 1200px container |

### Touch Targets
- Primary CTAs: min 44px tap height, 16px horizontal padding on mobile
- Nav links: generous padding for thumb navigation
- Circular navigation dots: min 12px with 20px tap area

### Collapsing Strategy
- **Nav**: Horizontal link bar collapses to hamburger on mobile; full-screen menu on open
- **Hero**: 105px → 56px → 40px progressive scaling across breakpoints, weight 300 maintained throughout
- **Feature sections**: 2-column feature pairs collapse to stacked single-column
- **Video/imagery**: Hero photo/video reorders below text on mobile rather than side-by-side
- **Section spacing**: 128px+ desktop → 48–64px mobile — reduces but maintains editorial pace
- **Letter-spacing**: Tracking remains proportionally tight at all breakpoints

### Image Behavior
- Product imagery maintains full-bleed treatment on mobile
- Video sections compress aspect ratio but preserve cinematic framing
- No art direction changes — the same visual language adapts to smaller viewports
- Logo wordmark scales but never becomes icon-only

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Cape Lavender (`#9891e1`)
- Page Background: Cape Off-White (`#f5f5f5`)
- Primary Text: Cape Black (`#000000`)
- Hover Text: Deep Focus Slate (`rgba(43, 51, 63, 0.75)`)
- Lavender Surface: Pale Lilac (`#e9e4f4`)
- Focus Background: Focus Gray (`rgba(115, 133, 159, 0.5)`)
- Focus Ring: `rgba(0, 0, 0, 0.2) 0px 0px 0px 2px`
- Stamp Shadow: `-4px 4px 0 0 #000` or `-3px 3px 0 0 #fff` (inverted)

### Example Component Prompts
- "Create a hero section on Cape Off-White (`#f5f5f5`) with a headline at 105px FK Grotesk weight 300, line-height 1.00, letter-spacing -0.2px, color `#000000`. Use a Cape Lavender (`#9891e1`) CTA button — 12px FK Grotesk weight 400 uppercase, `0.05em` letter-spacing, `0px` radius, `-4px 4px 0 0 #000` hard offset shadow."
- "Design a feature card on `#f5f5f5` with `0px` border-radius, no border, and a hard offset shadow `-4px 4px 0 0 #000`. Title in FK Grotesk 48px weight 300, tight letter-spacing `-1%`. Body in FK Grotesk 20px weight 300, line-height 1.30."
- "Build a full-bleed video hero section with dark imagery. Overlay text left-aligned, bottom-positioned: headline at 56px FK Grotesk weight 300 in pure white, subtitle at 16px weight 400. Add a Cape Lavender (`#9891e1`) CTA with `-3px 3px 0 0 #fff` inverted offset shadow."
- "Create a circular pagination dot — 12×12px, `9999px` radius, `1px solid #000` border, transparent or black fill based on state. Active state scales to `matrix(1.1, 0, 0, 1.1, 0, 0)`."
- "Design an outline pill badge — transparent background, `1px solid #000`, `9999px` radius, 12px FK Grotesk weight 400 text in `#000000`, padding 2.4px 8px."

### Iteration Guide
1. Default to FK Grotesk weight 300 for all display and heading sizes — lightness is non-negotiable
2. Keep radius binary: `0px` for rectangular, `9999px` for circular. Never mid-range.
3. Use hard offset shadows (`-4px 4px 0 0`) for CTAs and emphasized cards — no blur, no spread
4. Lavender (`#9891e1`) is sacred — one or two applications per screen, primarily on primary CTAs
5. Negative letter-spacing scales with size: `-0.2px` at display, `-1%` at mid sizes, normal at body
6. Uppercase UI text pairs with `0.05em` letter-spacing and weight 400 — never weight 300 uppercase
7. Off-white (`#f5f5f5`) is the page canvas — reserve pure white for inversions only
8. Let typography carry the composition; avoid decorative icons or illustrations
