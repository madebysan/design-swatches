---
slug: apollo
name: Apollo
url: https://www.apollo.io
domain: apollo.io
category: SaaS
styles: [Light, Warm, Playful]
tagline: "Yellow-green spotlight on warm concrete."
fonts: [Season Mix, Soehne, Abc Diatype, Founders Grotesk Mono]
primary_color: "#ebf212"
---

# Design System Inspired by Apollo

> Yellow-green spotlight on warm concrete.

## 1. Visual Theme & Atmosphere

Apollo's homepage trades the usual SaaS-blue palette for something more tactile: a warm off-white canvas (`#f7f5f2` — concrete, not paper), stark black typography (`#000000`), and a single high-voltage yellow-green (`#ebf212`) doing all the primary-action work. The overall feel is grounded efficiency. Where competitors lean on shadow, gradient, or bright color washes, Apollo uses subtle background shifts (Canvas → Ash Gray) and hairline borders to organize space. Surfaces stay clean and unblemished; visual hierarchy emerges from typography weight and background-color rhythm rather than depth tricks.

The four-typeface stack does specific jobs. **Season Mix** is the display face — semi-bold custom sans with tight tracking, used for marketing headlines. **Soehne** carries body text, inputs, navigation, and button labels with subtle positive tracking — its 0.144px tracking at 16px gives the text a precise, calm rhythm. **Abc Diatype** appears in a more condensed character for secondary body and bolded callouts. **Founders Grotesk Mono** appears for code-like or data-related text, reinforcing the precision-tool brand.

What makes the atmosphere unmistakable is the color discipline. Apollo Gold (`#ebf212`) shows up only on primary CTAs — it's a spotlight, not a wash. Accent Green (`#f8ff2c`), a closely related but distinct yellow-green, appears on decorative fills and never on actions. Together they're a duo of related-but-distinct yellow-greens with assigned roles. Combine that with the warm Canvas, the Crisp White (`#ffffff`) cards lifted just barely off it, and the Ash Gray (`#ccc9c6`) section bands, and you get a system that reads like polished concrete: warm, monochromatic, with one electric highlight.

**Key Characteristics:**
- Canvas (`#f7f5f2`) warm off-white — concrete, not paper
- Apollo Gold (`#ebf212`) reserved exclusively for primary CTAs — never decorative
- Accent Green (`#f8ff2c`) for decorative fills only — never on actions
- Four-typeface stack: Season Mix (display), Soehne (body), Abc Diatype (condensed), Founders Grotesk Mono (data)
- Subtle positive tracking on Soehne (`0.144px` at 16px) creates calm precision
- Negative tracking returns at 20px+ headings (`-0.2`, `-0.24`, `-0.48`, `-0.88` at display)
- 8px radius vocabulary across buttons, cards, inputs — soft but not soft-edged
- No shadows: depth via Canvas → White → Ash Gray surface luminance shifts
- Hairline borders (Subtle Gray `#e5e7eb`) for dividers, never thick lines
- Bottom-line-only inputs — minimal, integrated form treatment
- Display sits at 88px with `-0.88px` negative tracking — confident scale moment

## 2. Color Palette & Roles

### Background Surfaces
- **Canvas** (`#f7f5f2`): Primary page background — warm off-white concrete tone.
- **Crisp White** (`#ffffff`): Card backgrounds — subtle lift from the Canvas.
- **Ash Gray** (`#ccc9c6`): Section backgrounds, navigation, footer — distinct visual segmentation.

### Text & Content
- **Midnight Ink** (`#000000`): Primary text — headings and body.
- **Graphite** (`#1a1a1a`): Input text.
- **Charcoal Text** (`#47423d`): Body text for slightly muted information.
- **Faded Stone** (`#736f6c`): Subtle small print, less important info.

### Brand & Accent
- **Apollo Gold** (`#ebf212`): Primary action buttons — the singular spotlight.
- **Accent Green** (`#f8ff2c`): Decorative fills and illustrative backgrounds — never on actions.
- **Violet Headline** (`#3f3653`): Special-case color for number-based headlines (stat callouts).

### Border & Divider
- **Subtle Gray** (`#e5e7eb`): Hairline dividers and input bottom borders.
- **Soft Stone** (`#94918e`): Heavier hairline borders.

## 3. Typography Rules

### Font Families
- **Season Mix** (substitute: Montserrat): Display and marketing headlines. A semi-bold custom font with tight tracking gives presence without shouting.
- **Soehne** (substitute: Inter): Primary body text, input fields, navigation links, button labels. Precise, readable sans-serif with subtle positive tracking.
- **Abc Diatype** (substitute: Roboto Condensed): Secondary body text, smaller labels, bolded elements. Compact sans with tight negative tracking, complementing Soehne's slightly wider feel.
- **Founders Grotesk Mono** (substitute: IBM Plex Mono): Code-like or data-related text. Monospaced contrast that reinforces precision.

### Hierarchy

| Role | Font | Size | Line Height | Letter Spacing |
|------|------|------|-------------|----------------|
| Display | Season Mix | 88px | 1.05 | -0.88px |
| Heading Large | Season Mix | 48px | 1.05 | -0.48px |
| Heading | Season Mix | 24px | 1.20 | -0.24px |
| Subheading | Season Mix / Soehne | 20px | 1.20 | -0.2px |
| Body Large | Soehne | 18px | 1.00 | 0.162px |
| Body | Soehne | 16px | 1.50 | 0.144px |
| Body Small | Soehne | 14px | 1.20 | 0.196px |
| Caption | Soehne | 12px | 1.20 | 0.168px |

### Principles
- **Tracking inverts at the 20px line**: Below 20px, Soehne uses subtle positive tracking (`0.144` to `0.196`). At 20px and above, Season Mix uses progressively negative tracking (`-0.2` to `-0.88` at display). This creates a precise, calm body reading experience and a confident-but-composed display register.
- **Four-typeface specialization**: Each face has a defined job. Season Mix announces. Soehne explains. Abc Diatype condenses. Founders Grotesk Mono represents data. They never trespass.
- **Soehne stays at weight 400**: The body face uses a single weight throughout — discipline that prevents emphasis sprawl. Bolded body content delegates to Abc Diatype instead.
- **Tight Season Mix tracking is the signature**: At 88px display, `-0.88px` (`-0.01em`) tightens letterforms into a confident, near-architectural mark.

## 4. Component Stylings

### Buttons

**Primary Action**
- Background: Apollo Gold (`#ebf212`)
- Text: Midnight Ink (`#000000`)
- Radius: `8px`
- Padding: `16px` horizontal
- Font: Soehne, 16px, weight 400
- Use: Primary CTA, the system's only spotlight

**Secondary Action (Outline)**
- Background: transparent
- Border: `1px solid #000000` (Midnight Ink)
- Text: Midnight Ink (`#000000`)
- Radius: `8px`
- Padding: `16px` horizontal
- Font: Soehne, 16px, weight 400

**Ghost Button**
- Background: transparent
- Text: Faded Stone (`#736f6c`)
- No border
- Radius: `8px`
- Use: Tertiary actions

**Social Sign-Up Button**
- Background: Canvas (`#f7f5f2`)
- Text: Midnight Ink (`#000000`)
- Border: `1px solid #e5e7eb` (Subtle Gray)
- Radius: `8px`
- Padding: `32px 24px`
- Use: Third-party authentication entries

### Cards

**Default Card**
- Background: Crisp White (`#ffffff`)
- Radius: `8px`
- Padding: `24px`
- No shadow — depth via Canvas-to-White contrast

**Elevated Card**
- Background: Canvas (`#f7f5f2`)
- Radius: `8px`
- Padding: `40px`
- No shadow — accentuated through generous padding rather than lift

**Callout Card**
- Background: Ash Gray (`#ccc9c6`)
- Radius: `12px`
- Padding: `0px` (interior content handles its own spacing)
- Use: Testimonials, quotes, distinct content blocks

### Inputs

**Text Input Field**
- Background: transparent
- Border-bottom: `1px solid #e5e7eb` (Subtle Gray)
- Radius: `0px`
- Padding: `12px` horizontal
- Text: Graphite (`#1a1a1a`), Soehne
- Use: Bottom-line-only minimal data entry

### Navigation
- Sticky top bar
- Links: Soehne, 16px, weight 400, Charcoal Text (`#47423d`)
- Bar background: Ash Gray (`#ccc9c6`) — visually distinct from Canvas page background

## 5. Layout Principles

### Spacing System
- **elementGap**: `8px` — small inline gaps between adjacent elements
- **sectionGap**: `40px` — vertical spacing between major content sections
- **cardPadding**: `24px` standard; `40px` on elevated cards

### Border Radius Scale
- **buttons / default cards / inputs (rounded)**: `8px`
- **callout cards**: `12px`
- **inputs (bottom-line)**: `0px`

### Grid
- No fixed page max-width — content uses centered max-widths inside sections
- Hero often centered with form below
- Two-column text+visual layouts alternate with centered stacks
- Section backgrounds alternate Canvas → Ash Gray to mark vertical rhythm

### Layout & Composition
The page uses a max-width centered container, opening with a full-width header. The hero centers the headline over a Canvas-to-Ash-Gray background transition, followed by a sign-in form with social options. Subsequent sections alternate between Canvas (`#f7f5f2`) and Ash Gray (`#ccc9c6`) backgrounds, creating clear vertical rhythm without visible dividers. Inside sections, content sits in centered stacks or simple two-column text+image splits. The sticky nav remains visually distinct from the page background through its Ash Gray treatment.

## 6. Depth & Elevation

| Level | Hex | Name | Purpose |
|-------|-----|------|---------|
| 1 | `#f7f5f2` | Canvas | Base page background and elevated neutral elements |
| 2 | `#ffffff` | Primary Card Surface | Default card backgrounds — subtle lift from Canvas |
| 3 | `#ccc9c6` | Section Background | Major content section bands, navigation, footer |

**Shadow Philosophy**: Apollo deliberately avoids shadows. Elevation is communicated entirely through background luminance shifts: Canvas (warm off-white) at the page level, Crisp White cards lifted barely above it, Ash Gray section bands recessed below. This creates a polished-concrete aesthetic where surfaces feel like distinct material layers rather than floating planes. The result reads as tactile and grounded — the visual equivalent of a well-finished workshop, not a glossy showroom.

## 7. Do's and Don'ts

### Do
- Use Ash Gray (`#ccc9c6`) for section backgrounds and navigation bars to provide discrete visual breaks.
- Apply Apollo Gold (`#ebf212`) exclusively to primary calls to action — its spotlight quality depends on rarity.
- Set primary headings in Season Mix with tight negative tracking (`-0.0100em` at large sizes).
- Divide content using Subtle Gray (`#e5e7eb`) hairline borders or section background shifts — never pronounced shadows.
- Employ Soehne for all body and interactive text with its specified subtle positive tracking (`0.144px` at 16px).
- Frame interactive elements and most content cards with `8px` border-radius for consistent soft edges.
- Use Crisp White (`#ffffff`) for card backgrounds against the Canvas — subtle layered separation.

### Don't
- Avoid using Accent Green (`#f8ff2c`) for primary actions — it's reserved for decorative fills only.
- Do not introduce additional bold or semibold weights for Soehne; weight 400 is sufficient.
- Refrain from using hard shadows — elevation comes from background-color shifts.
- Do not deviate from the established letter-spacing values; tracking is core to the brand's voice.
- Avoid full-bleed sections that extend edge-to-edge if they contain primary content — content stays within defined widths.
- Do not introduce additional accent colors; Apollo Gold (`#ebf212`) is the only vibrant highlight.
- Do not apply padding indiscriminately; respect `8px` element gaps, `24px` card padding, `40px` section gaps.

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | Single column, display drops to ~48px, section gap tightens to ~32px |
| md | `768px+` | Two-column text+image splits engage |
| lg | `1024px+` | Multi-column card grids; full nav visible |
| xl | `1280px+` | Centered max-width with generous side margins |

### Touch Targets
- Buttons with `16px` horizontal padding and natural Soehne 16px text height yield ~40px touch targets
- Bottom-line inputs need adequate vertical hit area; pair with `12px` horizontal padding minimum

### Collapsing Strategy
- Display: 88px → 48px → 32px on mobile; tracking scales proportionally
- Two-column splits collapse to stacked single column
- Section gap reduces from 40px to ~24px on mobile
- Card padding tightens (`24px` → `16px` on small mobile)
- Sticky nav collapses to hamburger, retains Ash Gray bar background

## 9. Agent Prompt Guide

### Quick Color Reference
- Text: `#000000` (Midnight Ink)
- Background: `#f7f5f2` (Canvas)
- Card Background: `#ffffff` (Crisp White)
- Section Background: `#ccc9c6` (Ash Gray)
- Border: `#e5e7eb` (Subtle Gray)
- Primary Action: `#ebf212` (Apollo Gold)
- Decorative Accent: `#f8ff2c` (Accent Green)

### Example Component Prompts
1. **Primary Action Button**: Apollo Gold (`#ebf212`) background, Midnight Ink (`#000000`) text, `8px` radius, `16px` horizontal padding. Soehne, 16px, weight 400.
2. **Default Card**: Crisp White (`#ffffff`) background, `8px` radius, `24px` padding, no shadow. Title in Season Mix, 24px, weight 550, `-0.24px` letter-spacing, Midnight Ink. Body in Soehne, 16px, weight 400, Charcoal Text (`#47423d`), `0.144px` letter-spacing.
3. **Text Input Field**: transparent background, `1px solid #e5e7eb` bottom border, `0px` radius. Text in Soehne, 16px, weight 400, Graphite (`#1a1a1a`). `12px` horizontal padding.
4. **Secondary Outline Button**: transparent background, `1px solid #000000` border, Midnight Ink text, `8px` radius, `16px` horizontal padding. Soehne, 16px, weight 400.
5. **Display Headline**: Season Mix, 88px, weight 550, line-height 1.05, letter-spacing `-0.88px`, color `#000000`.

### Iteration Guide
1. Canvas warm off-white, Crisp White cards barely lifted, Ash Gray section bands — three layers, no shadow.
2. Apollo Gold (`#ebf212`) is the spotlight — only on primary CTAs.
3. Tracking inverts at the 20px line: positive below, negative above.
4. Soehne stays at weight 400; bolded body content uses Abc Diatype instead.
5. `8px` radius across buttons, cards, inputs — soft but disciplined.
6. Hairline borders (Subtle Gray `#e5e7eb`) for division — never thick lines, never shadows.

## Preview

![Apollo](https://ysxnuuuj3kqhdyj2.public.blob.vercel-storage.com/1777508417335-thumb.jpg)
