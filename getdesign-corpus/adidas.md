---
slug: adidas
name: adidas
url: https://adidas.com
domain: adidas.com
category: Retail
styles: [Light, Minimalist, Gradient, Monochromatic]
tagline: "Monochromatic corporate directive."
fonts: [adineue, Arial]
primary_color: "#ffffff"
---

# Design System Inspired by adidas

> Monochromatic corporate directive.

## 1. Visual Theme & Atmosphere

The system projects a direct, no-nonsense corporate voice, stripped down to essential communication. It uses a stark achromatic palette of black and white, punctuated by subtle gray accents that define secondary text and structural elements. The complete absence of visual flair — no shadows, gradients, photography, or rounded corners beyond a minimal 3px — communicates efficiency and seriousness rather than warmth. This is a system tuned for transactional clarity: error pages, account flows, terms-of-service screens. The custom 'adineue' typeface offers a distinct but understated brand presence; functional UI surfaces (buttons, inputs) fall back to Arial for legibility.

**Key Characteristics:**
- Achromatic palette only — pitch black (`#000000`) on absolute white (`#ffffff`)
- Three gray tones for hierarchy: `#e0e0e0`, `#cccccc`, `#999999`
- Custom adineue typeface for editorial text, Arial for functional UI controls
- 3px border-radius — present but minimal, never decorative
- No shadows, no gradients, no photography
- 1.4 line-height across all text — comfortable reading without expansion
- 40px section gaps establish vertical rhythm; 8px element gaps keep density tight
- Black `#000000` doubles as button fill and border — no separate stroke color
- Inputs sit on white with a `#cccccc` border — the only mid-gray visible chrome

## 2. Color Palette & Roles

### Background Surfaces
- **Absolute Zero** (`#ffffff`): Page backgrounds, input field backgrounds.

### Text & Content
- **Pitch Black** (`#000000`): Primary text, headings, button text on white surfaces, primary CTA fills.
- **Concrete Gray** (`#999999`): Secondary text, less-prominent labels, error message body.

### Border & Divider
- **Pebble** (`#cccccc`): Default input field borders.
- **Shadow Play** (`#e0e0e0`): Subtle dividers and structural lines.

## 3. Typography Rules

### Font Families
- **adineue** (substitute: system-ui, Helvetica Neue): Primary brand typeface for headings and body text. Conveys directness through a distinct but understated geometric form. Weight 400 for body, weight 700 for section headings.
- **Arial** (substitute: Arial, Helvetica): Used for interactive elements — buttons and input fields — providing broad system compatibility and legibility for functional UI. The split between adineue (editorial) and Arial (functional) is deliberate.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | adineue | 25px | 700 | 1.4 | normal |
| Heading | adineue | 23px | 700 | 1.4 | normal |
| Subheading | adineue | 20px | 500 | 1.4 | normal |
| Body | adineue | 17px | 400 | 1.4 | normal |
| Caption | adineue | 14px | 400 | 1.4 | normal |
| Button / Input | Arial | 15–16px | 400–500 | 1.4 | normal |

### Principles
- **Two-family functional split**: adineue carries editorial content; Arial handles functional controls. The split signals 'this is content' vs 'this is a control.'
- **Single line-height**: Every role uses 1.4 — there is no expressive line-height variation. The system reads as a corporate document, not a designed page.
- **Modest display scale**: Display headlines top out at 25px — there is no hero typography. Content is presented at near-uniform size with weight as the primary hierarchy signal.
- **Normal letter-spacing throughout**: No tracking adjustments at any scale.

## 4. Component Stylings

### Buttons

**Primary Action Button**
- Background: `#000000` (Pitch Black), Text: `#ffffff` (Absolute Zero)
- Border: `1px solid #000000`, Radius: `3px`
- Padding: `14px 32px`. Font: Arial weight 500, 16px
- The black-on-black border is functional consistency, not decoration

### Inputs

**Default Input Field**
- Background: `#ffffff`, Text: `#000000`
- Border: `1px solid #cccccc` (Pebble), Radius: `3px`
- Padding: `8px` all sides. Font: Arial weight 400, 15px
- The `#cccccc` border is the only mid-gray chrome surface in the system

### Text Components

**Section Heading**
- Color: `#000000`. Font: adineue weight 700, 23px, line-height 1.4
- Margin-bottom: 40px — establishes section rhythm

**Body Paragraph**
- Color: `#000000`. Font: adineue weight 400, 17px, line-height 1.4
- Margin-bottom: 20px

**Reference / Error Identifier**
- Color: `#000000`. Font: adineue weight 400, 14px, line-height 1.4
- Used for unique identifiers (error codes, transaction IDs, technical references)

**Secondary Description Text**
- Color: `#000000` standard, `#999999` (Concrete Gray) in error message contexts
- Font: adineue weight 400, 14px, line-height 1.4

## 5. Layout Principles

### Spacing System
- **Element gap**: 8px — tight density between adjacent elements
- **Section gap**: 40px — major content breaks
- **Card padding**: 20px
- **Body paragraph margin-bottom**: 20px (in-flow text rhythm)
- **Heading margin-bottom**: 40px (section rhythm)

### Border Radius Scale
- **All components**: `3px`
- A single global radius — present but minimal, never used decoratively

### Grid
- No fixed max-width detected — content uses centered text blocks with single or two-column layouts
- Sections stack vertically with 40px breaks
- No global navigation pattern present in source — suggests minimal or absent chrome on this page type

### Layout & Composition
The page primarily uses a max-width contained model, centrally aligning content within a clear visual frame. Hero sections feature a centered headline and brand logo. Sections are composed of text blocks, often arranged in single or two-column layouts, with consistent vertical spacing (40px for major sections, 20px within text blocks) creating a strong rhythm. Content is generally stacked and centered for key messages, then shifts to a left-aligned, two-column structure for detailed explanatory text. The layout density is comfortable, providing sufficient white space around text to avoid crowding. No imagery competes with copy — the message is the page.

## 6. Depth & Elevation

| Level | Hex | Name | Purpose |
|-------|-----|------|---------|
| 1 | `#ffffff` | Absolute Zero | Page background, input surfaces |
| 2 | `#000000` | Pitch Black | Primary action button surfaces (inverted) |

**Shadow Philosophy**: adidas has no elevation system. There is no drop-shadow, no inner shadow, no luminance stepping. Depth is communicated only through the binary contrast between black and white surfaces, with `#cccccc` borders defining input boundaries. The flatness is the point — this is a system designed for legal copy, account screens, and transactional flows where any decoration would feel inappropriate.

## 7. Do's and Don'ts

### Do

- Use Pitch Black (`#000000`) for all primary text, headings, and interactive button backgrounds.
- Maintain a minimal border-radius of 3px for all interactive elements like buttons and input fields.
- Apply adineue for all headline and body text, ensuring a consistent brand tone.
- Utilize 40px of vertical margin for significant section breaks and larger content blocks.
- Employ the 1.4 line height for adineue body and heading text for comfortable reading.
- Use Absolute Zero (`#ffffff`) as the primary page background and for input field backgrounds.
- Apply Concrete Gray (`#999999`) only for secondary, less prominent text or muted borders.

### Don't

- Avoid using any colors outside the defined achromatic palette of Pitch Black, Absolute Zero, Shadow Play, Concrete Gray, and Pebble.
- Do not introduce any drop shadows or complex elevation effects; the design relies on flat separation.
- Never use rounded corners exceeding 3px; maintain the sharp, angular aesthetic.
- Refrain from introducing decorative gradients; stick to solid color fills.
- Do not deviate from the specified font families (adineue, Arial) or their assigned weights and sizes.
- Avoid introducing images or graphics with vibrant colors; all visuals should either be monochromatic or integrate seamlessly with the achromatic theme.
- Do not use letter spacing other than 'normal' for any text elements.

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column stack, padding compresses |
| md | 768px+ | Two-column text layouts available |
| lg | 1024px+ | Full max-width content, generous side margins |
| xl | 1280px+ | Max content width applies |

### Touch Targets
- Primary buttons at `14px 32px` padding meet the 40px minimum touch target comfortably
- Inputs at `8px` padding need adequate vertical spacing in stacked forms

### Collapsing Strategy
- Two-column text blocks collapse to single-column at mobile
- Section gaps compress from 40px to ~24–32px at mobile
- Heading margin-bottom reduces from 40px to ~24px to preserve density
- Buttons retain padding and 3px radius at all sizes — no shape change

## 9. Agent Prompt Guide

### Quick Color Reference
- Text: `#000000` (Pitch Black)
- Background: `#ffffff` (Absolute Zero)
- Secondary text: `#999999` (Concrete Gray)
- Input border: `#cccccc` (Pebble)
- Subtle divider: `#e0e0e0` (Shadow Play)

### Example Component Prompts

1. **Primary Action Button**: background `#000000`, text `#ffffff`, Arial weight 500 16px, padding 14px 32px, border 1px solid `#000000`, border-radius 3px.
2. **Default Input Field**: background `#ffffff`, text `#000000`, Arial weight 400 15px, padding 8px on all sides, border 1px solid `#cccccc`, border-radius 3px.
3. **Section Heading**: text `#000000`, adineue weight 700 23px, line-height 1.4, margin-bottom 40px.
4. **Body Paragraph**: text `#000000`, adineue weight 400 17px, line-height 1.4, margin-bottom 20px.
5. **Error Reference Code**: text `#000000`, adineue weight 400 14px, line-height 1.4 — for displaying unique IDs or transaction references.

### Iteration Guide
1. Achromatic only — no colors outside black, white, and the gray scale.
2. 3px is the universal radius — never go larger, never go to zero.
3. adineue for content, Arial for controls — keep the split clean.
4. 1.4 line-height everywhere — don't expand or compress.
5. No shadows. Ever. Surface contrast does all the elevation work.

## Preview

![adidas](https://ysxnuuuj3kqhdyj2.public.blob.vercel-storage.com/1775933004482-thumb.jpg)
