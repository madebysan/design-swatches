---
slug: atlassian
name: Atlassian
url: https://www.atlassian.com
domain: atlassian.com
category: SaaS
styles: [Light, Cool]
tagline: "organized digital workspace"
fonts: [Charlie Text, Charlie Display]
primary_color: "#1868db"
---

# Design System Inspired by Atlassian

> organized digital workspace

## 1. Visual Theme & Atmosphere

Atlassian's marketing surface reads like a meticulously organized digital workspace — crisp white canvas (`#ffffff`), near-black text (`#000000`), and a single energetic Periwinkle blue (`#1868db`) doing all the interactive work. Where most enterprise SaaS sites feel sterile, Atlassian punctuates the order with a Conic Energy gradient (`#bf63f3` violet) on hero illustrations and a Harvest Gold (`#fca700`) accent for highlight moments. The result is precise but not clinical: a tool for complex teamwork that signals approachability through deliberate moments of color.

The defining typographic move is `Charlie Display` at scale. Hero display sits at 70px with a positive letter-spacing of `0.84px` — wider tracking, not tighter. This is a notable inversion of the dark-mode-mono-tracking convention. At 48px display the spacing is `0.576px`; at 32px heading, `0.384px`. Atlassian uses positive tracking as a confidence signal, the typographic equivalent of speaking slowly with authority.

The radius system is unusually polarized. Cards sit at a generous `20px`, primary buttons stretch to `10000px` (effectively a pill), and inputs/general elements hold a tight `2px`. The huge gap between rectangle (cards, sections) and pill (buttons) is the signature: containers are calmly rounded, but the thing you click is decisively oval. Pair this with a single, layered card shadow (`rgba(9, 30, 66, 0.31) 0px 0px 1px 0px, rgba(9, 30, 66, 0.25) 0px 1px 1px 0px`) and the system gets its tactile, workspace-grade feel.

**Key Characteristics:**
- White (`#ffffff`) canvas with Slate 900 (`#000000`) text — maximum legibility-first
- Periwinkle 500 (`#1868db`) reserved for primary actions; Harvest Gold (`#fca700`) for accents only
- Conic Energy gradient (`#bf63f3`) on hero illustrations signals dynamism
- Charlie Display at 70px with positive `0.84px` tracking — confident, wide
- Polarized radius vocabulary: `20px` cards vs `10000px` buttons vs `2px` general
- Subtle layered card shadow with cool blue undertone (`rgba(9, 30, 66, …)`)
- 4px base spacing unit drives a tight, workspace-grade rhythm
- Sub-brand accent palette: violet (Conic), gold (Harvest), with disciplined deployment
- Steel Grey (`#1c2b42`) as the cool secondary text — never warm grays
- Sticky top nav with category-organized links

## 2. Color Palette & Roles

### Background Surfaces
- **Canvas Frost** (`#ffffff`): Primary page background.
- **Ash Cloud** (`#f0f1f2`): Subtle background for ghost buttons and quiet UI components.
- **Sky Haze** (`#e9f2fe`): Hover states for interactive elements.
- **Graphite Base** (`#101214`): Dark surface backgrounds for hero or contrast sections.

### Text & Content
- **Slate 900** (`#000000`): Primary text — headings and body on light backgrounds.
- **Steel Grey** (`#1c2b42`): Secondary cool-toned text.
- **Midnight Shadow** (`#292a2e`): Subtle text shades, captions.

### Brand & Accent
- **Periwinkle 500** (`#1868db`): Primary brand color — CTAs, active states, links.
- **Conic Energy** (`#bf63f3`): Distinctive brand gradient color — hero illustrations and decorative elements signaling dynamism.
- **Harvest Gold** (`#fca700`): Highlight accent — never for interactive elements.

### Border & Divider
- **Subtle Mist** (`#b7b9be`): Subtle borders, list item separators.
- **Frost Shadow** (`#c2c7d0`): Card shadow source color.
- **Storm Sky** (`#42526e`): Input field borders and placeholder text.

## 3. Typography Rules

### Font Families
- **Charlie Text** (substitute: Inter): Primary body copy, subheadings, UI labels. Range of weights supports content hierarchy and functional clarity without overwhelming the interface.
- **Charlie Display** (substitute: Poppins): Headlines and prominent display text. Bolder weights with positive tracking create a confident, impactful presence at larger scales.

### Hierarchy

| Role | Font | Size | Line Height | Letter Spacing |
|------|------|------|-------------|----------------|
| Display Large | Charlie Display | 70px | 1.00 | 0.84px |
| Display | Charlie Display | 48px | 1.19 | 0.576px |
| Heading Large | Charlie Display | 40px | 1.20 | 0.48px |
| Heading | Charlie Display | 32px | 1.17 | 0.384px |
| Heading Small | Charlie Display | 24px | 1.29 | 0.288px |
| Subheading | Charlie Text | 20px | 1.25 | normal |
| Body | Charlie Text | 16px | 1.50 | normal |
| Caption | Charlie Text | 13px | 1.40 | normal |

### Principles
- **Positive tracking on display**: Counter to the convention of tightening display type, Atlassian opens it up. `0.84px` at 70px reads as confident, deliberate, well-spaced.
- **Two-typeface split by job**: Charlie Display owns hero and section headlines; Charlie Text owns everything below 20px and all UI labels. Clean role separation.
- **Weight 700–800 for display**: Bold weights at 48–80px create the signature "unleash your superteam"-level hero impact.
- **Body stays normal**: Below 20px, letter-spacing returns to normal — Charlie Text was drawn to read at default tracking.

## 4. Component Stylings

### Buttons

**Primary Action (Filled Pill)**
- Background: Periwinkle 500 (`#1868db`)
- Text: Canvas Frost (`#ffffff`)
- Radius: `10000px`
- Padding: `6px 22px 8px 22px`
- Font: Charlie Text, weight 500
- Use: Primary CTAs site-wide

**Pill Ghost Button**
- Background: Ash Cloud (`#f0f1f2`)
- Text: Slate 900 (`#000000`)
- Radius: `28px`
- Padding: `1px 30px`
- Use: Secondary actions, navigation pills

**Text Link Button**
- Background: transparent
- Text: Slate 900 (`#000000`)
- Radius: `3px`
- Padding: `8px 32px 0px 0px`
- Use: Tertiary actions, in-text navigation

**Icon Button (Round Ghost)**
- Background: transparent
- Icon: Slate 900 (`#000000`)
- Shape: full circle (`100%` radius)
- Padding: `6px` all sides

### Cards

**Elevated Content Card**
- Background: Canvas Frost (`#ffffff`)
- Radius: `20px`
- Padding: `30px 20px`
- Shadow: `rgba(9, 30, 66, 0.31) 0px 0px 1px 0px, rgba(9, 30, 66, 0.25) 0px 1px 1px 0px`
- Use: Featured content, product cards

**Transparent Card**
- Background: transparent
- Radius: `0px`
- Padding: `0px`
- Use: Content that blends into the surrounding section

**Rounded Top Card**
- Background: transparent
- Radius: `20px 20px 0px 0px`
- Padding: `0px`
- Use: Sections that visually connect to content stacked below

### Inputs

**Outline Input Field**
- Background: transparent
- Border-bottom: Storm Sky (`#42526e`)
- Placeholder: Storm Sky (`#42526e`)
- Radius: `0px`
- Padding: minimal
- Use: Minimalist data entry — bottom-line-only treatment

### Navigation
- Sticky persistent top bar
- Links organized into clear categories
- White Canvas Frost background with subtle bottom border
- Primary CTA: filled Periwinkle 500 button, right-aligned

## 5. Layout Principles

### Spacing System
- **elementGap**: `4px` — tight base unit drives the grid
- **sectionGap**: `24px` between content blocks; sections use multiples
- **cardPadding**: `20px` standard

### Border Radius Scale
- **buttons (primary)**: `10000px` (effectively pill)
- **buttons (secondary pill)**: `28px`
- **cards**: `20px`
- **general / inline**: `2px` to `3px`
- **icon button**: `100%` (full circle)

### Grid
- Centered max-width content with consistent vertical rhythm
- Card grids for feature sections
- Two-column splits for text-and-visual blocks
- Hero often full-bleed with centered content stack

### Layout & Composition
The page maintains a centered max-width with consistent vertical spacing. The hero section often uses a full-bleed dark background with a centered headline and prominent primary action button. Content sections alternate between split layouts (text on one side, visual on the other) and centered stacks. Card grids structure feature content. Navigation persists at top with category-organized links. The composition conveys an organized, information-dense yet breathable workspace experience.

## 6. Depth & Elevation

| Level | Hex | Name | Purpose |
|-------|-----|------|---------|
| 0 | `#ffffff` | Canvas Frost | Primary page background |
| 1 | `#f0f1f2` | Ash Cloud | Subtle background for ghost buttons and quiet UI |
| 2 | `#ffffff` + card shadow | Elevated Content Card | Featured cards with subtle depth |

**Shadow Philosophy**: Atlassian uses a single, signature card shadow: `rgba(9, 30, 66, 0.31) 0px 0px 1px 0px, rgba(9, 30, 66, 0.25) 0px 1px 1px 0px`. The cool-blue undertone (rgb 9, 30, 66 — a dark navy) gives elevation a workspace-cool feel rather than a generic gray. The shadow is restrained — barely a 1px lift — but its consistent application across every elevated card creates a unified tactile signature. Buttons, inputs, and nav stay flat; only cards earn the lift.

## 7. Do's and Don'ts

### Do
- Use Periwinkle 500 (`#1868db`) exclusively for primary interactive elements to clearly signpost actions.
- Maintain high contrast by pairing Slate 900 (`#000000`) or Steel Grey (`#1c2b42`) text on Canvas Frost (`#ffffff`).
- Apply `20px` border-radius consistently for all elevated cards and product views.
- Utilize `10000px` border-radius for all primary buttons to create the signature pill shape.
- Employ Charlie Display at 70–80px with weight 700 or 800 for hero headlines.
- Use `4px` as the base unit for horizontal and vertical spacing — multiples of 4 throughout.
- Apply the signature card shadow (`rgba(9, 30, 66, 0.31) 0px 0px 1px 0px, rgba(9, 30, 66, 0.25) 0px 1px 1px 0px`) to all elevated cards.
- Use positive letter-spacing on Charlie Display headlines — wider, not tighter.

### Don't
- Do not use Harvest Gold (`#fca700`) for interactive elements; reserve it for accents and decorative purposes.
- Avoid using multiple border-radii values for buttons; stick to `10000px` for primary, `28px` for secondary pills.
- Do not introduce new shadow styles — consistency with the defined card shadow is critical.
- Refrain from deviating from the `4px` spacing unit to avoid visual clutter.
- Do not use letter-spacing other than `normal` for Charlie Text or the specified positive values for Charlie Display.
- Avoid using Storm Sky (`#42526e`) as a primary text color — it's reserved for inputs and muted UI.
- Do not use transparent + `0px` radius cards for critical distinct content; reserve them for blending sections.

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | Single column, display drops to ~40px, section spacing tightens |
| md | `768px+` | Two-column text+visual layouts engage |
| lg | `1024px+` | Card grids in 3-column, full nav category visible |
| xl | `1280px+` | Wide max-width container with generous side margins |

### Touch Targets
- Primary buttons: `36px+` height with `6px / 8px` vertical padding plus `22px` horizontal
- Pill ghost buttons: ample `30px` horizontal padding for touch comfort
- Icon buttons: `100%` radius keeps them circular and easy to tap

### Collapsing Strategy
- Display: 70px → 48px → 32px on mobile, positive tracking scales proportionally
- 3-column card grids → 2-column → single column stacked
- Two-column text+visual collapses to stacked single column
- Section spacing reduces; cards maintain `20px` padding to preserve tactile feel
- Navigation collapses to hamburger; primary Periwinkle CTA stays visible

## 9. Agent Prompt Guide

### Quick Color Reference
- Text: `#000000` (Slate 900)
- Background: `#ffffff` (Canvas Frost)
- Subtle Background: `#f0f1f2` (Ash Cloud)
- Border (input): `#42526e` (Storm Sky)
- Primary Action: `#1868db` (Periwinkle 500)
- Accent: `#fca700` (Harvest Gold)
- Brand Gradient: Conic Energy (`#bf63f3`)
- Card Shadow: `rgba(9, 30, 66, 0.31) 0px 0px 1px 0px, rgba(9, 30, 66, 0.25) 0px 1px 1px 0px`

### Example Component Prompts
1. **Primary Action Button**: Periwinkle 500 (`#1868db`) background, Canvas Frost (`#ffffff`) text, `10000px` radius, padding `6px 22px 8px 22px`. Charlie Text font, weight 500. Text: "Get Started".
2. **Elevated Content Card**: Canvas Frost (`#ffffff`) background, `20px` radius, shadow `rgba(9, 30, 66, 0.31) 0px 0px 1px 0px, rgba(9, 30, 66, 0.25) 0px 1px 1px 0px`. Padding `30px 20px`. Title in Charlie Display, 32px, weight 800, Slate 900. Body in Charlie Text, 16px, weight 400, Steel Grey.
3. **Hero Display Headline**: Charlie Display, weight 800, 70px, line-height 1.0, letter-spacing `0.84px`, color `#000000`. Text: "Unleash your superteam".
4. **Pill Ghost Button**: Ash Cloud (`#f0f1f2`) background, Slate 900 (`#000000`) text, `28px` radius, padding `1px 30px`. Charlie Text, 16px, weight 500.
5. **Outline Input**: transparent background, Storm Sky (`#42526e`) bottom border, no radius. Placeholder in Storm Sky. Charlie Text, 16px, weight 400, Slate 900.

### Iteration Guide
1. White canvas, black text, one Periwinkle accent — that's the structural baseline.
2. Charlie Display owns 24px and above with positive tracking; Charlie Text owns everything below.
3. Pills for primary buttons (`10000px`), rounded rectangles for cards (`20px`), tight (`2px`) for general inline.
4. Single card shadow with cool-blue undertone — never gray, never multi-layer.
5. Reserve Harvest Gold (`#fca700`) and Conic Energy (`#bf63f3`) for accents and illustrations only.
6. Spacing is `4px`-grid throughout — no arbitrary values.

## Preview

![Atlassian](https://ysxnuuuj3kqhdyj2.public.blob.vercel-storage.com/1777423385035-thumb.jpg)
