---
slug: allbirds
name: Allbirds
url: https://allbirds.com
domain: allbirds.com
category: Retail
styles: [Light]
tagline: "Soft natural palette. Like hand-woven textiles and smoothed river stones."
fonts: [Geograph, Self Modern, HurmeGeometricSans3-Regular]
primary_color: "#e0dacf"
---

# Design System Inspired by Allbirds

> Soft natural palette. Like hand-woven textiles and smoothed river stones.

## 1. Visual Theme & Atmosphere

Allbirds presents a natural, approachable e-commerce experience built on soft neutrals and muted earth-toned chromatic accents. The base canvas is white linen (`#ffffff`) with warm mist (`#e0dacf`) panels providing subtle section differentiation, and a deep muted olive (`#222519`) deployed for selective dark product moments. Brand swatches — desert clay, sky dust, sandstone tan, sunlit ochre — appear not as decoration but as the literal background colors behind product photography, treating each shoe like a stone resting on its complementary surface.

Typography is a dual-personality pairing. Geograph carries the entire functional UI — body text, navigation, button labels, captions — at a clean geometric weight. Self Modern, a traditional serif, is reserved for editorial-style display headlines like 'Bold By Nature'. The contrast between modern utility (Geograph) and understated elegance (Self Modern) is the system's typographic signature: contemporary product flow with editorial moments of pause.

The most distinctive shape signature is the extreme button radius. Buttons and inputs use a `1.67772e+07px` radius — effectively unbounded — making every interactive element a perfect pill regardless of width. Cards meanwhile sit at a softer, contained 16px radius. This produces a deliberate tension: cards feel architectural and grounded, while buttons feel woven and tactile. Hard utility chips at 4px radius play against this, giving navigation and inline labels a sharper, instructional shape.

**Key Characteristics:**
- White linen base (`#ffffff`) with warm mist (`#e0dacf`) panel breaks
- Dual-typeface system: Geograph (UI) + Self Modern (editorial display) + HurmeGeometricSans3 (specific buttons)
- Pill-shape buttons and inputs (`1.67772e+07px` radius — effectively unbounded)
- Card radius at 16px — grounded against pill-shape interactions
- Earthy brand swatches (Desert Clay, Sky Dust, Sandstone Tan, Sunlit Ochre) as product backgrounds, not decoration
- Muted Olive (`#222519`) for occasional dark product surfaces — natural, not synthetic black
- 4px radius for utility chips — sharp shape contrast against pill buttons
- 4px element gaps with 42–90px section gaps — tight rhythm, generous breathing
- No drop shadows — elevation comes from background color shifts and subtle borders
- Photography is product-tight or lifestyle-natural, never glossy or filtered

## 2. Color Palette & Roles

### Background Surfaces
- **White Linen** (`#ffffff`): Primary page background.
- **Warm Mist** (`#e0dacf`): Subtle section backgrounds — the primary anchor color.
- **Muted Olive** (`#222519`): Dark product section backgrounds — natural, not synthetic black.

### Text & Content
- **Black Ink** (`#000000`): Primary text on light surfaces.
- **Charcoal Slate** (`#212121`): Secondary text, button fills, navigation links.
- **Storm Gray** (`#525252`): Muted secondary text, placeholder text.
- **White Linen** (`#ffffff`): Text on dark Muted Olive backgrounds.

### Brand & Accent
- **Desert Clay** (`#a57e75`): Product background swatch — warm earth.
- **Sky Dust** (`#879aab`): Product background swatch — cool sky.
- **Sandstone Tan** (`#d1b0a4`): Product background swatch — warm tan.
- **Sunlit Ochre** (`#9e8949`): Product background swatch — warm gold.

These four are surface colors, not decorative accents. They appear as the literal backdrop behind product photography, providing tonal variation from card to card.

## 3. Typography Rules

### Font Families
- **Geograph** (substitute: Inter, Söhne): Primary UI font for body text, navigation, buttons, and informational display. Clean geometric shape ensures readability across sizes — anchors the entire interface.
- **Self Modern** (substitute: Playfair Display, Tiempos Headline): Distinctive editorial-style headlines and display text ('Bold By Nature'). Traditional serif form provides contrast to the sans-serif, adding sophisticated naturalism.
- **HurmeGeometricSans3-Regular** (substitute: Montserrat, Avenir): Limited use, primarily for specific button text where a slightly more open, geometric feel is desired.

### Hierarchy

| Role | Font | Size | Line Height | Letter Spacing |
|------|------|------|-------------|----------------|
| Display | Self Modern | 40px | 1.20 | normal |
| Heading-lg | Geograph | 24px | 1.33 | normal |
| Heading | Geograph | 20px | 1.40 | normal |
| Subheading | Geograph | 18px | 1.50 | normal |
| Body | Geograph | 16px | 1.50 | normal |
| Body-sm | Geograph | 14px | 1.43 | 0.025 |
| Caption | Geograph | 12px | 1.50 | 0.05 |

### Principles
- **Sans for utility, serif for editorial**: Geograph runs the operational UI. Self Modern punctuates it with editorial moments — hero headlines, marketing display. The two never blend in body copy; the switch is always semantic.
- **Positive letter-spacing at small sizes**: Captions get +0.05 tracking, body-sm gets +0.025. Both prevent optical crowding without expanding the type's geometry.
- **Comfortable line-heights throughout**: 1.40–1.50 for body and subheadings, 1.20 only at display scale where tight setting suits headline mass.
- **Minimal weight variation**: Geograph runs at weight 400 across most roles — hierarchy is built through size, not weight. Self Modern stays at weight 400 even at 40px display.

## 4. Component Stylings

### Buttons

**Primary Filled Button**
- Background: `#212121` (Charcoal Slate), Text: `#ffffff`, Border: none
- Radius: `1.67772e+07px` (effectively unbounded — pill shape)
- Padding: `8px 16px`. Font: Geograph weight 400, 14px, line-height 1.14
- The dark fill on light page provides high CTA contrast

**Secondary Filled Button**
- Background: `#ffffff`, Text: `#000000`, Border: none
- Radius: pill (`1.67772e+07px`), Padding: `8px 16px`
- Font: Geograph weight 400, 14px. Inverted surface from primary — same shape, white fill

**Secondary Outlined Button (Light surface)**
- Background: transparent, Text: `#000000`, Border: `1px solid #000000`
- Radius: `0px`, Padding: `0px`. Font: Geograph weight 400
- An exception to the pill rule — this variant is square and flat, used inline rather than as a primary action

**Secondary Outlined Button (Dark surface)**
- Background: transparent, Text: `#ffffff`, Border: `1px solid #ffffff`
- Radius: pill (`1.67772e+07px`), Padding: `8px 16px`
- Font: Geograph weight 400. Returns to pill shape on dark sections

### Cards

**Product Display Card**
- Background: `#ffffff` (White Linen) or `#222519` (Muted Olive) or one of the brand swatches
- Radius: `16px`, Content padding: `8px`
- Images often full-bleed to the card edges within the rounded boundary
- The 16px radius is the system's grounded card shape — soft but architectural

### Inputs

**Pill Input Field**
- Background: `#ffffff`, Text: `#000000`, Border: `1px solid #000000`
- Radius: pill (`1.67772e+07px`)
- Padding: `10px 12px` left, `80px` right (asymmetric, for internal action elements like search/clear icons)
- Font: Geograph weight 400. Placeholder in `#525252` (Storm Gray)

### Badges & Chips

**Utility Chip**
- Background: `#ffffff`, Text: `#000000`, Border: `1px solid #212121`
- Radius: `4px`, Padding: `4px 8px`
- Used for inline informational tags ('NEW ARRIVALS')
- The 4px radius creates a sharp shape contrast against the pill-button language — chips read as instructional signage rather than interactive controls

### Navigation

**Header Navigation Link**
- Text: `#212121` (Charcoal Slate) on light, `#ffffff` on dark
- Font: Geograph weight 400, 14px
- Hover state indicated by underline or color shift
- Top bar typically fixed with a clean, centered logo and right-aligned utility icons (cart, search, account)

## 5. Layout Principles

### Spacing System
- **Element gap**: 4px — very tight micro-rhythm between adjacent elements
- **Section gap**: 42–90px — wide range depending on hierarchical importance
- **Card content padding**: 8px — minimal, lets product imagery dominate
- The 4px element gap is unusually tight; it works because the surrounding section breathing is generous

### Border Radius Scale
- **Buttons & Inputs**: `1.67772e+07px` (pill)
- **Cards**: `16px`
- **Utility chips**: `4px`
- **Sharp variant buttons**: `0px` (specific outlined button on light surface)

The system has four distinct radius languages: pill (interactive), grounded (cards), sharp instructional (chips), and flat exception (one outlined button). Each shape corresponds to a function.

### Grid
- No fixed max-width — the system uses constrained content sections with full-bleed hero moments
- 2-column or multi-column product grids with responsive cards
- Sticky top navigation with centered logo and right-aligned utility

### Layout & Composition
The page primarily uses a max-width contained layout, though some hero sections extend full-bleed. Hero patterns vary: some feature large full-width product arrangements with text overlay, while others adopt a split layout with a lifestyle image on one side and a headline plus CTA on the other. Sections feature consistent vertical spacing (sectionGap 42–90px) and often employ 2-column or multi-column grids for products and content blocks. Product listings appear in responsive card grids. Content flow is primarily linear, with distinct sections visually separated by background color changes (white linen → warm mist → muted olive) or clear vertical spacing.

## 6. Depth & Elevation

| Level | Hex | Name | Purpose |
|-------|-----|------|---------|
| 1 | `#ffffff` | White Linen | Page background, default card surface |
| 2 | `#e0dacf` | Warm Mist | Subtle section panel — softens the page rhythm |
| 3 | `#222519` | Muted Olive | Dark product surface — natural inversion |
| 3 | `#a57e75` / `#879aab` / `#d1b0a4` / `#9e8949` | Brand Swatches | Product card surfaces — tonal variation |

**Shadow Philosophy**: Allbirds uses no drop-shadows. Elevation is achieved through background color shifts — white linen for the page, warm mist for soft section breaks, brand swatches and muted olive for product card surfaces. Subtle borders (1px) appear on inputs and outlined buttons, but cards rely on color contrast alone. The flatness reinforces the natural, hand-finished aesthetic; a synthetic shadow would feel out of place in a system referencing wool, wood, and stone.

## 7. Do's and Don'ts

### Do

- Prioritize Geograph for all body text, navigation, and button labels at its specified weights and sizes to maintain UI consistency.
- Use Self Modern 400 for all marketing headlines and display text to express brand elegance.
- Apply `1.67772e+07px` radius to all interactive buttons and inputs for a soft, approachable feel, effectively making them pill-shaped.
- Utilize the color progression from White Linen (`#ffffff`) background to Charcoal Slate (`#212121`) buttons for clear contrast and hierarchy.
- Maintain a clear product focus by centering product imagery on clean backgrounds (White Linen, Muted Olive, or other brand swatch colors).
- Use 4px radius for utility chips so they read as instructional signage, not interactive controls.

### Don't

- Avoid using box-shadows extensively; elevation is primarily achieved through background color shifts and subtle borders.
- Do not introduce sharp corners on primary interactive elements like buttons or input fields, as the pill-like radius is a signature brand element.
- Refrain from highly saturated or vibrant accent colors; the brand palette relies on muted, earthy tones and achromatic neutrals.
- Do not deviate from the established font families; Geograph and Self Modern provide a distinct dual-personality to the typography.
- Avoid using thin line-heights on body text; ensure readability with line-heights of 1.4 to 1.5 for optimal comfort.
- Don't apply pill radius to cards or modals — the unbounded radius is reserved for interactive controls only.

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, hero scales down, multi-col grids stack |
| md | 768px+ | Two-column splits return, 2-up product grids |
| lg | 1024px+ | Full multi-column product grids, full-width hero |
| xl | 1280px+ | Generous side margins, full layout |

### Touch Targets
- Pill buttons at `8px 16px` padding need accompanying line-height to clear 40px touch — typically achieved through Geograph's natural ascent
- Pill inputs with `10px` vertical padding meet touch comfortably
- Header utility icons (cart, search) sized for thumb access on mobile

### Collapsing Strategy
- Hero display 40px → ~32–36px on mobile, line-height 1.20 maintained
- 4-column product grids collapse to 2-up at md, single column on mobile
- Section gaps compress from 90px to ~42px at mobile
- Pill button radius preserved at all sizes — the shape is non-negotiable
- Card 16px radius preserved at all sizes

## 9. Agent Prompt Guide

### Quick Color Reference
- Text: `#000000` (Black Ink)
- Background: `#ffffff` (White Linen)
- CTA Background: `#212121` (Charcoal Slate)
- CTA Text: `#ffffff` (White Linen)
- Border: `#000000` (Black Ink)
- Section panel: `#e0dacf` (Warm Mist)
- Dark surface: `#222519` (Muted Olive)
- Product accent: `#9e8949` (Sunlit Ochre) or `#a57e75` (Desert Clay)

### Example Component Prompts

1. **Primary CTA Button**: background `#212121`, text `#ffffff`, border-radius `1.67772e+07px` (pill), padding 8px 16px, font Geograph 400 14px line-height 1.14.
2. **Product Card**: background `#ffffff`, border-radius 16px, content padding 8px. Include product image full-bleed within rounded boundary, plus a 'NEW ARRIVALS' utility chip (background `#ffffff`, text `#000000`, border 1px solid `#212121`, radius 4px, padding 4px 8px).
3. **Hero Headline**: 'Bold By Nature' using Self Modern 400 40px, text `#000000`, line-height 1.20, normal letter-spacing.
4. **Pill Input Field**: background `#ffffff`, text `#000000`, border 1px solid `#000000`, border-radius `1.67772e+07px`, padding 10px 80px 10px 12px (asymmetric for internal action icon). Placeholder text in `#525252` (Storm Gray).
5. **Section Panel Block**: background `#e0dacf` (Warm Mist), full-width section. Heading in Self Modern 40px `#000000`. Body in Geograph 16px `#212121`. 90px vertical padding above and below.

### Iteration Guide
1. Pill (`1.67772e+07px`) for interactive controls, 16px for cards, 4px for utility chips — three radii, three roles.
2. Geograph for utility, Self Modern for editorial — never blend in body copy.
3. Brand swatches (Desert Clay, Sky Dust, Sandstone Tan, Sunlit Ochre) are product surface colors, not decorative accents.
4. Warm Mist (`#e0dacf`) is the soft section break — Muted Olive is the inverted surface.
5. No shadows. Elevation comes from color shifts and 1px borders.
6. Positive letter-spacing only at small sizes (12px gets +0.05, 14px gets +0.025) — display sizes stay normal.

## Preview

![Allbirds](https://ysxnuuuj3kqhdyj2.public.blob.vercel-storage.com/1775924481316-thumb.jpg)
