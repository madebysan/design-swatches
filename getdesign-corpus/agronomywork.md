# Design System Inspired by Agronomy Workshop

## 1. Visual Theme & Atmosphere

Agronomy Workshop is editorial restraint applied to a category that almost never gets it: golf apparel. The site reads like a quiet design quarterly, not a sportswear shop. A warm bone-paper background (`#eeede8`) carries the entire experience, broken only by oversized field photography of the product worn outdoors and a near-black ink (`#1e1e1e`) for type. There is no chrome, no gradient, no shadow, no decorative flourish — every gram of visual weight is doing structural work.

The defining typographic move is **OT Neue Montreal Medium Semi Squeezed** at 54px with a punishingly tight `0.81` line-height and `-1.08px` letter-spacing. That `0.81` is the signature: most editorial systems live at 0.95–1.05; Agronomy crushes its display type until the lines almost kiss. Combined with the "Semi Squeezed" cut — a horizontally narrowed grotesk — the headlines read like compressed industrial signage. Below display, **Gerstner Programm FSL** (a revival of Karl Gerstner's 1960s Swiss programmatic typeface) does the small-text and link work, and **ABC Marfa Mono** appears at 10px with `1px` tracked-out spacing for category labels and chrome. Three typefaces, each doing one specific job, none of them defaults.

What makes the system feel like a magazine instead of a Framer template is the **product-photo-as-hero** approach. Catalog imagery isn't cropped into rounded cards — it sits in clean rectangular frames against the bone canvas, often two-up at the same size, with all metadata pushed to a tiny caption underneath. Discount banners arrive as a flat unblended yellow strip (`#ffeb00`-ish field) at the bottom of a product tile. The bag/cart preview opens in a flat blue (`#0473f2`) rectangle. The whole composition is held together by 5px border-radius on tiles and 20px on a few specialized containers — a deliberate two-step radius scale, not a continuum.

**Key Characteristics:**
- Bone-paper canvas (`#eeede8`) — warm off-white that reads as natural fiber, not screen
- OT Neue Montreal Medium Semi Squeezed at 54px with `0.81` line-height — the signature crush
- Gerstner Programm FSL for body/links, ABC Marfa Mono at 10px for chrome labels
- Three typefaces, three jobs — no overlap, no fallbacks doing real work
- Photography sits in clean rectangles, not rounded cards — magazine, not e-commerce
- 5px and 20px radii only — binary corner system, no in-between values
- Saturated yellow promo strip and pure blue (`#0473f2`) action color as the only chromatic moments
- Underline-by-default links in black — Bauhaus directness over hover affordances
- Zero shadows in the system — depth comes from photography, not elevation

## 2. Color Palette & Roles

### Primary
- **Field Bone** (`#eeede8`): The page canvas. A warm putty/oat that suggests undyed cotton or recycled paper. Used everywhere — section backgrounds, product tile backgrounds, navigation bar.
- **Ink Charcoal** (`#1e1e1e`): The primary text color. Deliberately not pure black — softens against the bone canvas while still reading as definitive. Used for headlines, body, product names, captions.
- **Pure Black** (`#000000`): Reserved for borders on certain framed elements and the highest-contrast moments. Outranks Ink Charcoal only when graphic crispness matters more than warmth.

### Brand Accent
- **Action Blue** (`#0473f2`): The single chromatic UI color — applied to the cart/bag drawer, key call-to-action surfaces, and active-state moments. Pure web blue, undiluted, used like a stamp.
- **Promo Yellow** (~`#ffeb00`): The promotional banner color (e.g., "15% Off First Order"). Saturated and unblended — appears as a flat field strip across product tile bottoms.

### Neutrals & Text
- **Ink Charcoal** (`#1e1e1e`): All primary type — headings, body, navigation, captions
- **Quiet Gray** (`#666666`): Secondary metadata text — colorway labels under product names, supporting copy
- **Mute Gray** (`#888888`): Tertiary text — deepest-shade caption text, disabled states
- **Pure White** (`#ffffff`): Limited use — appears on certain product imagery backgrounds and inverted moments only

### Surface & Borders
- **Surface Bone** (`#eeede8`): Default panel background — matches page canvas, no contrast
- **Border Black** (`#000000`): When borders appear, they are full-weight 2px and in pure black
- **Inset Border** (`2px inset rgb(0,0,0)`): Specialized 2px inset border treatment on certain presentation elements — a Swiss-print convention rather than a UI convention

### Link Colors
- **Link Black** (`#000000`): Default link color, paired with `text-decoration: underline` — links signal themselves typographically, not chromatically
- **Legacy Web Blue** (`#0000ee`): Default browser blue retained on certain raw links — appears intentionally untouched, a Geocities-era nod that fits the pragmatic mood

### Gradient System
- Agronomy Workshop is **gradient-free**. There are no linear gradients, no radial gradients, no atmospheric blends. Every fill is a flat color rectangle. The only "gradients" in the visual experience come from product photography — never from CSS.

## 3. Typography Rules

### Font Family
- **Display**: `OT Neue Montreal Medium Semi Squeezed` — used for all heading-1 surfaces. The "Semi Squeezed" cut is the load-bearing detail.
- **Body / Link**: `Gerstner Programm FSL Regular` — Karl Gerstner's 1963 Swiss typeface, revived by FSL. Used for paragraphs, links, and most caption text. OpenType features in use: `blwf`, `cv03`, `cv04`, `cv09`, `cv11`.
- **Mono / Chrome**: `ABC Marfa Mono Unlicensed Trial Regular` — used at 10px with `1px` letter-spacing for category labels and small chrome elements, frequently uppercase.
- **Fallback**: Generic `sans-serif` only on a handful of utility links at 12px

*Note: All three are commercial typefaces. For external implementations, GT America Compressed or PP Neue Machina (display), Söhne or Inter (body), and JetBrains Mono or IBM Plex Mono (chrome) serve as close substitutes.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | OT Neue Montreal Medium Semi Squeezed | 54px (3.38rem) | 500 | 0.81 (crushed) | -1.08px | The signature — display headlines at sub-1.0 line-height |
| Display Mid | OT Neue Montreal Medium Semi Squeezed | 32px (2.00rem) | 500 | 1.00 | -0.64px | Section heads, product name on detail pages |
| Sub-heading | Gerstner Programm FSL Regular | 18px (1.13rem) | 400 | 0.89 | normal | Smaller heading-1 role — also tight line-height |
| Body / Link | Gerstner Programm FSL Regular | 14px (0.88rem) | 400 | 1.14 | normal or -0.28px | Standard reading text, link surfaces |
| Caption | Gerstner Programm FSL Regular | 14px (0.88rem) | 400 | 1.14 | -0.28px | Metadata, product captions, footer |
| Utility Link | sans-serif fallback | 12px (0.75rem) | 400 | normal | normal | Footer/legal links — left intentionally raw |
| Chrome Label | ABC Marfa Mono | 10px (0.63rem) | 400 | 1.20 | 1px | Category tags, "NEW", section markers — often uppercase |

### Principles
- **The 0.81 line-height is the signature**: At 54px display, line-height runs at `0.81` — almost 20% below the typographic norm. This crushes display lines into dense industrial blocks. Never relax it.
- **Three typefaces, three roles**: Display (Neue Montreal), body (Gerstner), chrome (Marfa Mono). Each appears at one or two sizes max. No typeface borrows another's job.
- **Squeezed grotesk over standard grotesk**: The "Semi Squeezed" cut is the difference between this looking like every Framer site and looking like Agronomy. If substituting, pick a condensed/compressed cut, not a regular one.
- **Mono labels in uppercase with 1px tracking**: Chrome text (10px Marfa Mono) is uppercase with `1px` letter-spacing — engineered/spec-sheet feel, not editorial.
- **Tight progressive tracking on display**: Letter-spacing scales from `-1.08px` at 54px to `-0.64px` at 32px to neutral by body size. The crush is always proportional.
- **Underline links by default**: Body links carry `text-decoration: underline` rather than relying on color. A pre-2010 web convention that reads as deliberately unfussy here.

## 4. Component Stylings

### Buttons

The site avoids traditional button shapes for most actions — links and full-bleed clickable rectangles do the work. Where button-like surfaces exist, they follow these patterns:

**Action Blue Bar**
- Background: Action Blue (`#0473f2`)
- Text: Pure White (`#ffffff`)
- Padding: full-width strip, 12–16px vertical
- Radius: `5px`
- Border: none
- Font: 14px Gerstner Programm FSL, weight 400
- Use: Add to cart, primary CTA bars, cart drawer surface

**Promo Yellow Strip**
- Background: Saturated yellow (~`#ffeb00`)
- Text: Ink Charcoal (`#1e1e1e`), 10–12px ABC Marfa Mono uppercase
- Radius: matches parent tile (typically `5px` bottom corners only)
- Use: Bottom-pinned promo strips on product tiles ("15% OFF FIRST ORDER")
- Critical detail: the yellow is unblended, no shadow, no border — flat field as graphic emphasis

**Underlined Text Link (Default)**
- Background: transparent
- Text: Ink Charcoal (`#1e1e1e`) or Pure Black (`#000000`)
- Decoration: `underline` always present
- Hover: inherits Framer default — color/decoration shift via CSS variable cascade
- Use: Inline links, navigation, "Shop", "Index", "Bag"

### Cards & Containers

**Product Tile**
- Background: Field Bone (`#eeede8`) or Pure White (`#ffffff`) depending on product photography
- Border: none — the photograph defines the edge
- Radius: `5px`
- Shadow: none (this is non-negotiable in the system)
- Internal padding: minimal — image dominates; metadata sits as 14px caption beneath
- Aspect ratio: square or portrait (3:4) — never landscape

**Drawer / Modal Container**
- Background: Pure White (`#ffffff`) or Field Bone
- Radius: `20px` (the secondary radius — only appears on overlays)
- Border: none
- Use: Cart drawer, product quick-view, lightbox containers

### Badges / Tags / Pills

**Mono Chrome Label**
- Background: transparent
- Text: Ink Charcoal (`#1e1e1e`), 10px ABC Marfa Mono uppercase, `1px` letter-spacing
- Padding: minimal — 2–4px vertical, 4–6px horizontal
- Radius: `0px` or none — labels float in space
- Use: "NEW", "SOLD OUT", category markers

**Color Swatch Dot**
- Background: solid product color (e.g., black, brown earth tones)
- Size: ~16×16px
- Radius: `9999px` (perfect circle)
- Border: `1px solid #000` on lighter swatches for definition
- Use: Color variant selection on product tiles — sits as a row of dots beneath the product name

### Inputs & Forms

**Email / Text Input**
- Background: `rgba(235, 235, 235, 0)` — transparent over the bone canvas with a hint of inset gray
- Border: `0px none` default — relies on shape and outline for affordance
- Outline: `rgb(30, 30, 30) none 3px` — 3px outline reserve for focus states
- Radius: `5px`
- Padding: `8px 12px`
- Font: 14px Gerstner Programm FSL, color `#1e1e1e`
- Use: Newsletter signup, email capture, search

### Navigation

- Top nav: minimal three-item bar — `Index` (left), small wordmark/QR mark (center), `Bag` (right). Sometimes `Shop` appears as a fourth item.
- Background: Field Bone (`#eeede8`) — matches page canvas
- Sticky behavior: pinned to top, page scrolls beneath
- Links: Gerstner Programm FSL 14px weight 400, color `#1e1e1e` or `#000000`
- Hover: color/decoration cascades via Framer CSS variables — typically a softening to a desaturated shade
- The nav offers no dropdowns, no mega-menus, no search field, no account icon — reduction is the navigation system

### Decorative Elements

**Field Photography Frame**
- Imagery sits flush in tiles with `5px` radius and no border
- No gradient overlays, no scrims, no chrome
- Captions live OUTSIDE the photograph, never overlaid
- This is the system's primary "decorative" move — the photograph itself

**Yellow Promo Strip**
- Flat saturated yellow rectangle pinned to the bottom of a product tile
- Mono caps text inside
- Acts as the only "shouted" visual element on the page

**QR / Mark Glyph**
- A small QR-like center mark in the navigation acts as the wordmark
- Tiny (~24×24px), monochrome, no surrounding chrome

## 5. Layout Principles

### Spacing System
- Base unit: **8px**, with a tight 4px sub-grid for chrome
- Scale: 4px, 5px, 6px, 8px, 16px, 20px, 40px, 80px, 86px
- Notable: The scale skips many values (no 12px, no 24px, no 32px, no 48px, no 64px). Agronomy moves in big jumps — chrome at 4–8px, content at 16–20px, sections at 40–86px. The mid-range is intentionally absent.

### Grid & Container
- Two-column product grid is the dominant layout — same-size tiles, equal weight
- Three-column variants appear on the shop page for denser browsing
- Desktop max-width feels generous (~1440px+) with edge-to-edge tile placement
- No centered narrow content column — the grid takes the full width
- Hero sections often run as two-up product portraits at near-equal sizing

### Whitespace Philosophy
- **Magazine pacing**: Sections breathe with 40–86px of vertical separation
- **Tile rhythm**: Inside a grid, tiles sit at near-zero gutters (4–8px) — they almost touch, creating a contact-sheet rhythm
- **Caption-as-air**: Tiny 14px captions under each product give just enough breathing room — no oversized whitespace below items
- **Scroll as chapters**: Each scroll-screen contains one logical section. The page is paced like a printed catalog spread

### Border Radius Scale
- Tight (5px): Buttons, tiles, inputs, links — the workhorse radius
- Generous (20px): Modal/drawer containers and a small set of specialty surfaces
- Full circle (9999px): Color swatch dots only
- No mid-range radii: Agronomy does not use 8, 10, 12, or 16px values. The system jumps from 5 to 20 with nothing between.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border, no inset | Default for all surfaces — page canvas, tiles, body |
| Inset Line (Level 1) | `2px inset rgb(0, 0, 0)` | Specialized presentation elements only — Swiss-print convention |
| Outline Reserve (Level 2) | `3px solid rgb(30, 30, 30)` | Reserved for focus states on inputs, never decorative |

**Shadow Philosophy**: Agronomy Workshop has **no shadow system**. The dembrandt extraction returned an empty shadows array — and visually this matches what's on the page. There are no drop shadows, no inner shadows, no glow effects, no soft edges. Where other catalogs would lift product tiles off the page with a `0 4px 12px rgba(0,0,0,0.08)`, Agronomy lets them sit flat against the bone canvas. Depth is achieved entirely through photography — the dimensionality of a sweater on a body, the perspective of a hat on a windswept hillside. The interface itself is paper-flat.

This is the system's most unusual technical decision. Most modern e-commerce templates inherit shadow defaults from their UI framework; Agronomy explicitly rejects them. Treat shadows as forbidden unless implementing a focus state for accessibility.

### Decorative Depth
- All depth lives in the photography
- Inset borders (`2px inset`) appear once or twice as a referential print convention, not a UI affordance
- Focus rings rely on 3px solid outlines, not blurred halos

## 7. Do's and Don'ts

### Do
- Use OT Neue Montreal Medium Semi Squeezed (or a compressed/condensed grotesk) for display — the squeeze is the brand
- Set display line-height to `0.81` — the crush is the signature
- Pair with Gerstner Programm FSL (or a Swiss-modernist body face) for paragraphs and links
- Use ABC Marfa Mono at 10px uppercase with `1px` letter-spacing for chrome labels
- Keep the canvas Field Bone (`#eeede8`) — never pure white as the page background
- Underline links by default — chromatic distinction is not the link affordance
- Use `5px` radius for tiles/buttons/inputs and `20px` only for modals/drawers
- Treat photography as the depth system — no CSS shadows
- Use Action Blue (`#0473f2`) as a flat stamp — full-bleed CTA bars, cart drawer
- Use the saturated yellow promo strip as the only "loud" element on a tile
- Move in big spacing jumps (4–8px chrome → 16–20px content → 40–86px sections)

### Don't
- Don't use Pure White (`#ffffff`) for the page background — Field Bone is the canvas
- Don't relax the `0.81` display line-height to 1.0 or above — the crush defines the brand
- Don't introduce drop shadows, inner shadows, or glow effects anywhere — shadow-free is non-negotiable
- Don't mix radius values (8, 10, 12, 16px) — the system is binary at 5px and 20px
- Don't use color-only link affordance — links must underline
- Don't add hover lift, scale, or shadow transitions on tiles — they sit flat
- Don't introduce mid-range tracking on display — `-1.08px` at 54px or it isn't right
- Don't use a regular grotesk in place of a squeezed one — the compression is the visual identity
- Don't dilute Action Blue with a pastel variant — it's pure `#0473f2` or nothing
- Don't add gradient fills to the promo strip — flat unblended yellow only
- Don't centre content in a narrow column — the grid spans the full viewport
- Don't add navigation chrome (search icons, account dropdowns, mega-menus) — three to four nav items maximum

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column tiles, hero drops to ~32px |
| Mobile | 375–810px | Single-column or 2-column tile grid, 32–40px display |
| Tablet | 810–1200px | 2-column dominant, occasional 3-column on shop |
| Desktop | 1200px+ | Full 2-column hero, 3-column shop grid, 54px display unlocked |
| Edge | ≥1440px | Maximum tile sizing, edge-to-edge layout |

The dembrandt extraction surfaces explicit breakpoints at `98px` (a chrome-level utility break) and `810px` (the major mobile-to-desktop transition). The 810px breakpoint is where the grid restructures and display type scales up.

### Touch Targets
- Tile clickable areas: full-tile tap targets (image + caption are one link)
- Nav links: 14px text with generous 16–20px vertical padding for thumb reach
- Color swatch dots: 16×16px visual with implicit 32×32px tap area
- CTA bars: full-bleed strips with 12–16px vertical padding — very large by default

### Collapsing Strategy
- **Nav**: Three-item bar holds across all breakpoints — no hamburger needed because there's nothing to collapse into
- **Display type**: 54px → 40px → 32px progressive scaling, line-height stays at `0.81–1.00`
- **Product grid**: 3-column → 2-column → 1-column as viewport narrows
- **Captions**: Stay at 14px Gerstner across all breakpoints — readability over scale
- **Spacing**: 86px section gaps reduce to ~40px on mobile, but the chapter-pacing rhythm holds

### Image Behavior
- Product photography stays full-bleed within its tile at every breakpoint
- Aspect ratios are preserved — 3:4 portrait or 1:1 square, never rebalanced
- No art direction changes across breakpoints — the same hero photo serves desktop and mobile
- The 5px radius on photography stays constant

## 9. Agent Prompt Guide

### Quick Color Reference
- Page Background: Field Bone (`#eeede8`)
- Primary Text: Ink Charcoal (`#1e1e1e`)
- Secondary Text: Quiet Gray (`#666666`)
- Tertiary Text: Mute Gray (`#888888`)
- Border / Highest Contrast: Pure Black (`#000000`)
- Action / CTA: Action Blue (`#0473f2`)
- Promo Banner: Saturated Yellow (~`#ffeb00`)
- Inverted Surface: Pure White (`#ffffff`)
- No shadows, no gradients, ever

### Example Component Prompts
- "Create a hero section on Field Bone (`#eeede8`) with a headline at 54px OT Neue Montreal Medium Semi Squeezed, weight 500, line-height `0.81`, letter-spacing `-1.08px`, color `#1e1e1e`. Caption underneath in 14px Gerstner Programm FSL Regular, weight 400, line-height `1.14`, color `#1e1e1e`. No shadow. No border."
- "Design a product tile — square aspect ratio, `5px` border-radius, `#eeede8` background, no border, no shadow. Photograph fills the tile flush. Below the tile, two lines of metadata: product name in 14px Gerstner FSL `#1e1e1e`, colorway in 14px Gerstner FSL `#666666`. Optional bottom-pinned saturated yellow strip (`#ffeb00`) for promo text in 10px ABC Marfa Mono uppercase with `1px` letter-spacing."
- "Build a cart drawer — `20px` border-radius, `#ffffff` background, no shadow. Inside, an Action Blue (`#0473f2`) full-width CTA strip at the bottom, `5px` radius corners, white text in 14px Gerstner FSL."
- "Create a chrome label — 10px ABC Marfa Mono uppercase, `1px` letter-spacing, color `#1e1e1e`, no background, no border, no padding to speak of. Used for 'NEW', category tags, spec-sheet markers."
- "Design a top navigation bar — Field Bone background, three text links left/center/right (`Index`, mark glyph, `Bag`) in 14px Gerstner FSL, color `#1e1e1e`, no underline on nav, no hover background. Pinned to top of viewport."
- "Build an email input — transparent background, `5px` radius, `8px 12px` padding, 14px Gerstner FSL, color `#1e1e1e`. No visible border in default state. Focus state shows a 3px solid outline in `#1e1e1e`."

### Iteration Guide
1. The display line-height is `0.81` — never relax it. If the headline doesn't feel crushed, it's wrong.
2. Three typefaces only: OT Neue Montreal Semi Squeezed (display), Gerstner FSL (body), ABC Marfa Mono (chrome). One job each.
3. Border radius is binary — `5px` for tiles/buttons/inputs, `20px` for modals/drawers. Nothing in between.
4. Zero shadows. Depth lives entirely in photography. If you reach for `box-shadow`, you're solving the wrong problem.
5. Field Bone (`#eeede8`) is the canvas, not white. Pure white only appears inside product photography or specific inverted surfaces.
6. Underline links — color is not the affordance. The underline IS the link.
7. Spacing moves in big jumps: 4–8px (chrome), 16–20px (content), 40–86px (sections). Avoid 12, 24, 32, 48, 64.
8. Action Blue (`#0473f2`) is a stamp — full-bleed CTA bars and the cart surface. Don't dilute it, don't gradient it, don't apply it to text.
9. The promo yellow is unblended saturated `#ffeb00` — flat field, no border, no shadow, mono caps text inside.
10. Photography sits in clean rectangles, not rounded cards — magazine, not e-commerce.
