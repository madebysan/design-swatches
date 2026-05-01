---
slug: kinfolk
name: Kinfolk
url: https://www.kinfolk.com
domain: kinfolk.com
category: Media
styles: [Light, Editorial, Serif]
tagline: "Transitional serif type on ink-ruled white canvas — slow-living editorial translated into digital stillness"
fonts: [Kinfolk-Serif-Deck, Kinfolk-Serif-Text, Kinfolk-Sans]
primary_color: "#212121"
---

# Design System Inspired by Kinfolk

> Transitional serif type on ink-ruled white canvas — slow-living editorial translated into digital stillness

## 1. Visual Theme & Atmosphere

Kinfolk's digital presence is a direct translation of its print philosophy: unhurried, considered, and defined by what is left out rather than what is added. The page opens on pure white (`#ffffff`) — not cream, not warm parchment, but the clean white of a magazine page held to good north light. Against this ground, ink-black text (`#212121`, `#000000`) lands with the weight of letterpress, and the primary structural vocabulary is the hairline rule: `1px solid rgb(33, 33, 33)` border-bottoms that divide without intruding, the way a compositor's lead slug separates columns. There is no gradient, no shadow atmosphere, no chromatic accent pulling the eye to a conversion funnel. The editorial image — a magazine cover, an architectural interior — does all of that emotional work.

The typographic system is the site's most intricate achievement. Three custom proprietary faces — `Kinfolk-Serif-Deck`, `Kinfolk-Serif-Text`, and `Kinfolk-Serif-Display` — are deployed in a hierarchy that mirrors a print publication's masthead logic. The Deck face handles all display and heading moments, running at weight 400 throughout: this is not bold-headline-as-call-to-action but serif-headline-as-title-page. At 80px it is uppercase and tracked tight (`-0.4px`), more inscription than announcement. At 50px it compresses its line-height to `1.04` — the kind of editorial density that makes a headline block feel like a designed object. Kinfolk-Sans handles UI chrome — navigation, labels, buttons, captions — in a system that clearly delineates narrative from infrastructure without ever shouting.

What makes the design genuinely distinctive is its commitment to print-media restraint in every interactive moment. Buttons are transparent-background rectangles with `2px solid rgb(0,0,0)` outlines and `2px` border-radius — almost no radius at all. Hover states shift to partial opacity (`0.8`) rather than filling with color. Section dividers are bottom borders, not ruled lines with decorative weight. The Flickity carousel that presents magazine covers uses invisible navigation controls (opacity `0` by default) that materialize only on interaction. The system trusts the photography. It trusts the serif. It trusts the reader.

**Key Characteristics:**
- Pure white canvas (`#ffffff`) — magazine page, not digital surface; no warm tint, no cool tint
- Kinfolk-Serif-Deck at weight 400 for all display sizes — the refusal of bold as an editorial stance
- Tight negative letter-spacing scaling from `-0.5px` at 50px to `-0.2px` at 40px — headlines as typographic objects
- Uppercase transforms on display headings create inscription-like authority without weight change
- Hairline ink rules (`1px solid #212121` bottom border) as the primary structural element, borrowed directly from print layout
- `2px` border-radius on buttons — barely perceptible, functionally sharp, precision over approachability
- Opacity-based hover states (`0.8` on hover, `0.6` on active) instead of color fills — restraint as interactivity
- Invisible carousel controls at default state, `170px` sidebar columns revealing section logic
- Three-face serif system (Deck for display, Text for body, Display for accent/lede) mirrors print typographic hierarchy
- No chromatic accent anywhere in the brand system — pure monochrome, every color decision is `#000`, `#212121`, or `#ffffff`

## 2. Color Palette & Roles

### Primary Brand
- **Kinfolk Ink** (`#000000`): The primary brand black — used for borders, button fills, structural dividers, heavy rules, and all maximum-contrast moments. Pure, unmixed black; the ink.
- **Kinfolk Near-Black** (`#212121`): Primary text color for body copy, navigation links, and most typographic content. Slightly lifted from pure black for comfortable reading at paragraph scale without losing depth.

### Text Scale
- **Primary Body** (`#212121`): Main reading text — all body paragraphs, navigation, link labels. The warmest of the blacks.
- **Pure Black Text** (`#000000`): Section headings, display type on white, button outlines — maximum contrast moments.
- **Pure White Text** (`#ffffff`): All text on dark or photographic surfaces — masthead overlays, subscriber bar labels, inverted components.

### Surface & Backgrounds
- **Page White** (`#ffffff`): Primary page background, card surfaces, input fields. The dominant surface.
- **Rule Light** (`#f4f4f4`): Extremely subtle light-grey used for secondary dividers and section-separating bottom borders where a hairline rule needs to recede. Also used for light modal/card borders (`1px solid rgb(244, 244, 244)`).
- **Sage Gray-Green** (`#dbded5`): The only non-monochrome neutral in the raw palette — a muted sage that appears in minor UI contexts (estimated: back-matter sections, certain pull-quote decorations). Reads as linen or aged paper.

### Borders & Rules
- **Ink Rule** (`rgb(33, 33, 33)` / `#212121`): The primary border — bottom-border hairlines on navigation, section dividers, article lists. `1px solid`.
- **Heavy Rule** (`rgb(0, 0, 0)` / `#000000`): Two-pixel rules and button outlines — the heavier structural mark. `2px solid`.
- **Ghost Rule** (`rgb(244, 244, 244)` / `#f4f4f4`): Secondary, recessive bottom borders for card separators and list item dividers.
- **White Rule** (`rgb(255, 255, 255)` / `#ffffff`): Borders on dark/photographic surfaces — subscriber bar label outlines.

### Shadows
- **Scroll Shadow** (`rgba(172, 171, 171, 0.3) 0px -1px 10px 0px`): A very soft upward ambient shadow used on sticky elements scrolling over content — barely perceptible, structural only.
- **Modal Shadow** (`rgba(0, 0, 0, 0.3) 0px 32px 68px 0px`): Deep vertical shadow for dialog overlays — the only moment of meaningful elevation in the system.

### Interactive / WordPress Admin (Non-Brand)
- **WP Admin Blue** (`#3858e9`): WordPress admin theme color — appears only in admin/cookie consent UI, not a brand color.
- **Link Blue** (`rgb(24, 99, 220)` / `#1863dc`): Hover state for cookie consent links — not a brand link color.

## 3. Typography Rules

### Font Family
- **Display / Heading**: `Kinfolk-Serif-Deck`, with fallback: `Georgia`, `'Times New Roman'`, serif
- **Body / Editorial**: `Kinfolk-Serif-Text`, with fallback: `Georgia`, serif
- **Display Accent**: `Kinfolk-Serif-Display`, with fallback: `Georgia`, serif
- **UI / Chrome**: `Kinfolk-Sans`, with fallback: `Helvetica Neue`, `Arial`, sans-serif
- **System Fallback**: `Arial` — used in cookie consent and WordPress admin components only
- **OpenType Features**: No explicit feature-settings detected; the custom faces are loaded as static fonts without variable axes.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Display Hero | Kinfolk-Serif-Deck | 80px (5.00rem) | 400 | 1.00 | -0.4px | uppercase | Magazine headline — inscription mode |
| Display Hero (editorial) | Kinfolk-Serif-Deck | 80px (5.00rem) | 400 | 1.00 | -0.4px | none | Same scale, title-case for bylined features |
| Section Hero | Kinfolk-Serif-Deck | 50px (3.13rem) | 400 | 1.04 | -0.5px | uppercase | Section title — dense editorial block |
| Section Hero (editorial) | Kinfolk-Serif-Deck | 50px (3.13rem) | 400 | 1.04 | -0.5px | none | Category heads, feature intros |
| Sub-heading Large | Kinfolk-Serif-Deck | 40px (2.50rem) | 400 | 1.15 | -0.2px | uppercase | Article headings, card headlines |
| Sub-heading Editorial | Kinfolk-Serif-Deck | 40px (2.50rem) | 400 | 1.15 | -0.2px | capitalize | Title-cased feature heads |
| Sub-heading Sans | Kinfolk-Sans | 25px (1.56rem) | 400 | 1.16 | -0.125px | none | Sans-serif sub-heading for navigation panels |
| Sub-heading Serif | Kinfolk-Serif-Deck | 25px (1.56rem) | 400 | 1.16 | -0.125px | none | Serif mid-heading for editorial contexts |
| Sub-heading Upper | Kinfolk-Serif-Deck | 25px (1.56rem) | 400 | 1.16 | -0.125px | uppercase | Section markers and categories |
| Lede / Intro Body | Kinfolk-Serif-Text | 20px (1.25rem) | 400 | 1.50 | — | none | Opening paragraphs, pull quotes |
| Display Accent | Kinfolk-Serif-Display | 20px (1.25rem) | 400 | 0.85 | — | none | Decorative display accent, drop caps |
| Display Accent Tight | Kinfolk-Serif-Display | 20px (1.25rem) | 400 | 0.85 | -0.5px | none | Tightly tracked accent display moments |
| Sans Lede | Kinfolk-Sans | 20px (1.25rem) | 400 | 1.50 | 0.4px | none | Sans intro text with open tracking |
| Bold Byline | Kinfolk-Serif-Text | 18px (1.13rem) | 700 | 1.33 | — | none | Author bylines, section anchors — only use of weight 700 |
| Body / Button | Kinfolk-Sans | 15px (0.94rem) | 400 | 1.33 | 0.15px | none | Primary UI text, button labels |
| Body Nav | Kinfolk-Sans | 15px (0.94rem) | 400 | 1.33 | -0.075px | none | Navigation links, tighter variant |
| Body UI Upper | Kinfolk-Sans | 15px (0.94rem) | 400 | 1.33 | 0.15px | uppercase | Uppercase UI labels, section nav |
| Body Serif | Kinfolk-Serif-Text | 15px (0.94rem) | 400 | 1.33 | — | none | Running body copy in articles |
| Body Serif Upper | Kinfolk-Serif-Text | 15px (0.94rem) | 400 | 1.33 | — | uppercase | Small caps substitute — category tags |
| Caption Serif | Kinfolk-Serif-Text | 14px (0.88rem) | 400 | 1.71 | — | none | Image captions, footnotes |
| Caption Button | Kinfolk-Serif-Text | 14px (0.88rem) | 500 | 1.71 | — | none | Small CTA links in caption context |
| Caption Sans | Kinfolk-Sans | 13px (0.81rem) | 400 | 1.31 | 0.39px | none | Small metadata, timestamps |
| Caption Sans Upper | Kinfolk-Sans | 13px (0.81rem) | 400 | 1.31 | 0.78px | uppercase | Uppercase micro labels — most open tracking |
| Micro | Kinfolk-Serif-Text | 12px (0.75rem) | 400 | — | — | none | Smallest running text, legal footnotes |

### Principles
- **Weight 400 is the ceiling for Kinfolk-Serif-Deck**: The display face never runs heavier than regular. Typographic authority is expressed through scale, spacing, and uppercase — never weight. Weight 700 appears once, in Kinfolk-Serif-Text for bylines, and nowhere else.
- **Scale-proportional negative tracking**: Display type tracks progressively tighter with size — `-0.5px` at 50px, `-0.4px` at 80px (fractionally tighter per em), `-0.2px` at 40px. Below 25px, tracking returns to near-zero or slightly positive.
- **Open-tracking on sans**: Kinfolk-Sans at small sizes (`13px`) uses positive letter-spacing (`0.39px`–`0.78px`) — the opposite of the serif system. This creates a clear visual distinction between narrative type (tracked tight) and navigational chrome (tracked open).
- **Line-height as editorial control**: Headlines compress to `1.00`–`1.04` for dense block presence; lede text opens to `1.50` for comfortable reading; captions breathe at `1.71`. The system uses line-height as a primary pacing tool.
- **Uppercase as register, not emphasis**: `text-transform: uppercase` on Kinfolk-Serif-Deck creates section identifiers and category markers without any weight change. It is structural, not expressive — borrowed from print masthead logic.
- **Three-face print hierarchy**: Deck for display (titles, section heads), Text for reading (body, captions, bylines), Display for accent moments (drop caps, pull quotes) — exactly the three faces a magazine art director would spec.

## 4. Component Stylings

### Buttons

**Primary Outline (Default CTA)**
- Background: `rgba(0, 0, 0, 0)` (transparent)
- Text: `rgb(0, 0, 0)` — `#000000`
- Padding: `8px`
- Radius: `2px`
- Border: `2px solid rgb(0, 0, 0)`
- Box Shadow: `none`
- Font: 14px Kinfolk-Serif-Text weight 500, line-height 1.71
- Hover: text `rgb(24, 99, 220)`, background `rgba(255,255,255,0)`, opacity `0.8`
- Active: text `rgb(24, 99, 220)`, opacity `0.6`
- Focus: color via WP admin variable (`#3858e9`), no outline
- Use: "Customise", "Buy", "Read" — all primary page actions

**Filled Black (Reject / Primary on Dark)**
- Background: `rgb(0, 0, 0)`
- Text: `rgb(255, 255, 255)`
- Padding: `8px`
- Radius: `2px`
- Border: `2px solid rgb(0, 0, 0)`
- Box Shadow: `none`
- Font: 14px weight 500
- Hover: text `rgb(24, 99, 220)`, background `rgba(255,255,255,0)`, opacity `0.8`
- Use: "Reject All", secondary confirm actions, inverted surfaces

**Accept / Accept All (White Filled)**
- Background: `rgb(255, 255, 255)`
- Text: `rgb(51, 51, 51)`
- Padding: `1px 6px`
- Radius: `0px`
- Border: `0px`
- Font: 13.3333px Arial weight 400 (cookie consent context only)
- Use: Cookie acceptance — system UI, not brand UI

**Subscriber Bar Badge-Button**
- Background: `rgba(0, 0, 0, 0)` (transparent)
- Text: `rgb(255, 255, 255)`
- Padding: `4px 8px`
- Radius: `2px`
- Border: `1px solid rgb(255, 255, 255)`
- Font: 15px Kinfolk-Sans weight 400, letter-spacing `0.15px`, line-height 20px
- Use: Subscriber tier label / CTA in announcement bar context

**Carousel Nav (Ghost Invisible)**
- Background: `rgba(255, 255, 255, 0)` to `rgba(255, 255, 255, 0.75)`
- Text: `rgb(51, 51, 51)`
- Padding: `1px 6px`
- Radius: `0px`
- Border: `0px`
- Opacity: `0` at default — only visible on interaction
- Font: 13.3333px weight 400
- Use: Flickity carousel prev/next navigation — editorial restraint, controls disappear into the layout

### Cards & Containers
- Background: `#ffffff` (page white)
- Border: bottom-only `1px solid rgb(33, 33, 33)` for list-item separation; `1px solid rgb(244, 244, 244)` for secondary divisions
- Radius: `0px` for content cards; `6px` for modal/dialog containers; `0px 0px 6px 6px` for bottom-rounded panels
- Shadow: `none` on content cards; `rgba(0, 0, 0, 0.3) 0px 32px 68px 0px` for overlay panels
- Image treatment: full-bleed within grid column, no radius on image edges, no shadow
- Internal padding: generous — estimated 25–40px for feature cards, `15px` for compact list items

### Inputs & Forms
- Background (email): `rgb(255, 255, 255)`
- Background (text/search): `rgba(0, 0, 0, 0)` (transparent)
- Text: `rgb(0, 0, 0)`
- Border: `0px` default — no visible border on standard inputs; bottom-only `1px solid rgb(0, 0, 0)` on search
- Radius: `0px` — completely sharp
- Padding: `0px` (bare inputs, styled through surrounding layout)
- Focus: borderColor `rgb(0, 0, 0)`, box-shadow `0 0 0 0.5px var(--wp-admin-theme-color, #3858e9)`
- Font: 15px Kinfolk-Sans weight 400

### Links
- **Standard editorial link**: color `rgb(33, 33, 33)`, `text-decoration: none` — text links that are invisible as links until hover
- **Underlined inline**: color `rgb(0, 0, 0)`, `text-decoration: underline rgb(137, 137, 137)` — a grey underline on black text, a whisper of a link
- **On dark surfaces**: color `rgb(255, 255, 255)`, `text-decoration: underline 1px rgb(137, 137, 137)` — white text, grey underline
- **Hover state**: opacity reduction to `0.8`, or color shift to `rgb(24, 99, 220)` only in admin/consent contexts

### Navigation
- Horizontal bar at top: KINFOLK wordmark (SVG) left-aligned, hamburger menu icon (`≡`) right-aligned
- Wordmark: ~205.5px wide SVG, pure black on white
- Menu icon: SVG, right-aligned, three horizontal lines
- Nav bar background: `#ffffff`, no border initially, scroll shadow (`rgba(172,171,171,0.3) 0px -1px 10px 0px`) on sticky scroll
- Nav links (expanded menu): Kinfolk-Sans 15px weight 400, `#212121`, letter-spacing `0.15px`, `text-transform: uppercase`
- Bottom divider: `1px solid rgb(33, 33, 33)` separating nav from content
- "Buy" and "Read" links below hero: Kinfolk-Sans 15px weight 400, separated by `|` character, horizontal center alignment

### Badges / Tags / Pills
**Subscriber Bar Label**
- Background: transparent
- Text: `rgb(255, 255, 255)`
- Padding: `4px 8px`
- Radius: `2px`
- Border: `1px solid rgb(255, 255, 255)`
- Font: 15px Kinfolk-Sans weight 400, letter-spacing `0.15px`
- Use: Tier/status indicator in announcement bars

**Category Tag**
- Inferred from typography: 13px Kinfolk-Sans weight 400, `text-transform: uppercase`, letter-spacing `0.78px`
- Background: transparent
- Border: none or bottom rule
- Use: Article category labels ("FOOD & DRINK", "INTERIORS")

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Full scale: 1px, 2px, 3px, 4px, 5px, 8px, 10px, 12px, 15px, 16px, 20px, 24px, 25px, 30px, 40px, 60px, 70px, 80px, 90px, 170px
- Notable values:
  - `15px` — the workhorse unit (89 occurrences): internal padding, text margins, small gaps
  - `25px` — comfortable component padding (15 occurrences)
  - `3px` — micro-spacing for typographic adjustments (145 occurrences — overwhelmingly the most-used fine unit)
  - `170px` — the signature large-scale value (13 occurrences): sidebar columns, section margins, the "generous air" of the editorial grid
  - `60–90px` — section vertical rhythm: generous breathing room between editorial sections

### Grid & Container
- Estimated max content width: 1440px–1600px for wide viewports, with generous interior margins
- Editorial grid: mixed — centered single-column for hero moments, 2-column (text + image) for feature sections, multi-column for article grids
- `170px` appears as a defining structural column — likely sidebar or margin width in the editorial grid, echoing the generous margins of a printed magazine spread
- Magazine cover carousel: single centered item, full-bleed width within container, Flickity-driven
- "Buy | Read" CTA: centered, inline with pipe character separator — deliberately minimal navigation

### Whitespace Philosophy
- **Generous air as editorial signal**: The `170px` spacing unit is the most distinctive structural choice in the system. Where most digital publications compress to maximize content density, Kinfolk reserves this exceptional margin as a signal of quality — the digital equivalent of a magazine with unusually wide gutters.
- **Section breathing**: 60–90px vertical padding between major editorial sections creates a reading pace that mirrors page turns rather than scroll feeds. Each section arrival feels considered.
- **Typography-first layout**: Content is organized around the type, not the grid. Whitespace exists to let the serif headings breathe and the photography hold space.
- **Rule-as-divider**: Rather than cards with background fills or shadow-based separation, Kinfolk uses hairline bottom-borders to organize content — invisible until needed, structural without decoration.

### Border Radius Scale
- `0px`: Default for all content elements — article images, input fields, content cards, standard links — the magazine grid has square corners
- `2px`: Buttons and badge/pill elements — barely perceptible rounding that softens without becoming "digital-friendly"
- `6px`: Modal and dialog containers; the `0px 0px 6px 6px` variant for bottom-rounded panels
- `50px`: Toggle switches (cookie consent) — the only fully pill-shaped element, confined to third-party UI
- The system is effectively binary: sharp (`0px`) for editorial content, barely-rounded (`2px`) for interactive chrome

## 6. Depth & Elevation

| Level | Box Shadow Value | Use Case |
|-------|-----------------|----------|
| Flat (Level 0) | `none` | All content elements, article cards, navigation, standard layout |
| Scroll (Level 1) | `rgba(172, 171, 171, 0.3) 0px -1px 10px 0px` | Sticky navigation on scroll — casts upward, almost invisible |
| Modal (Level 2) | `rgba(0, 0, 0, 0.3) 0px 32px 68px 0px` | Overlay panels, cookie consent dialogs — the only pronounced depth moment |

Kinfolk's elevation philosophy is as spare as its color system. The site is almost entirely flat — not because it lacks considered design, but because editorial hierarchy is expressed through typography and spacing rather than layered surfaces. The scroll shadow (`rgba(172,171,171,0.3) 0px -1px 10px 0px`) is upward-casting and so transparent it's barely perceptible — it merely signals that the navigation is "above" the page without dramatizing it. The modal shadow is the single genuine elevation moment: `rgba(0,0,0,0.3) 0px 32px 68px 0px` creates a deep, vertical casting shadow that pushes the consent dialog unambiguously forward. Both shadow values are instrumentally functional, never decorative. The site's depth vocabulary is: flat page, hairline rules, photography.

## 7. Do's and Don'ts

**Do:**
- Use Kinfolk-Serif-Deck at weight 400 for all display and heading text — weight 300 is unknown to this system, weight 700 is expressly forbidden at display sizes
- Apply `text-transform: uppercase` on Kinfolk-Serif-Deck headings as a structural device — it creates the inscription quality that defines the masthead voice
- Use `1px solid #212121` bottom-border rules as the primary content-separation mechanism — they are structural wallpaper, present but not prominent
- Keep button borders at `2px solid #000000` with `2px` radius — the weight of the rule matters; thinner feels cheap, any more radius feels consumer digital
- Scale letter-spacing negatively with display size: `-0.5px` at 50px, `-0.4px` at 80px, `-0.2px` at 40px — text at display sizes is a graphic object, not a readable string
- Allow `170px` margins and section spacing — the generous air is the brand voice made spatial
- Let photography hold the emotional weight — resist the urge to add graphic elements, illustrations, or iconographic decoration

**Don't:**
- Don't introduce chromatic color into the brand UI — `#dbded5` (sage gray-green) exists as a secondary neutral, but no saturated accent color belongs in this system
- Don't use hover fills or background-color changes on buttons — opacity reduction (`0.8`) is the hover convention; color fills break the transparency discipline
- Don't round image corners, card corners, or content container corners — `0px` radius for all editorial content is non-negotiable
- Don't increase heading weight beyond 400 in Kinfolk-Serif-Deck — weight 700 lives only in Kinfolk-Serif-Text for bylines; applying it to headings destroys the editorial register
- Don't add box-shadow to cards or article tiles — elevation comes from rule-borders and spacing, not lifted surfaces
- Don't use positive letter-spacing on display serif text — the compressed tracking on Kinfolk-Serif-Deck at headline sizes is definitional; loosening it breaks the headline block into a string of loose letters
- Don't use the WordPress admin blue (`#3858e9`) outside of consent/admin UI — it is a framework color, not a brand color

## 8. Responsive Behavior

### Breakpoints
Kinfolk ships with an unusually granular breakpoint system — 39 declared breakpoints reflecting fine-grained typographic and layout adjustments across every major device category.

| Name | Width | Key Changes |
|------|-------|-------------|
| Small Mobile | ≤379px | Single column, hero type scales to approximately 32–40px, stacked layout |
| Mobile | 380–549px | Single column, reduced section spacing, hero at 40–50px |
| Large Mobile | 550–739px | Wider column, hero at 50px, 2-column grids may begin |
| Tablet Small | 740–834px | 2-column editorial layout, reduced sidebar margins |
| Tablet | 835–1023px | Full 2-column, feature grids, `170px` margins compress |
| Desktop | 1024–1279px | Multi-column article grids, full sidebar margins begin |
| Large Desktop | 1280–1439px | Full editorial layout, 80px hero type, maximum grid |
| Wide Desktop | 1440–1919px | Content centered within 1440px max, generous margins |
| Cinema | 1920–4068px | Maximum typographic scale, ultra-wide photography treatment |

### Touch Targets
- Primary buttons: 8px padding (compact — may need augmentation for touch contexts)
- Navigation hamburger: adequate touch area via SVG bounding box
- Carousel navigation: arrow buttons with generous invisible tap area
- Article card links: full-card tap targets via wrapping anchor elements
- Minimum recommended: `44px` height for all interactive elements on mobile

### Collapsing Strategy
- **Navigation**: Full wordmark + hamburger maintains at all breakpoints; hamburger expands to full-screen overlay menu
- **Hero heading**: 80px → 50px → 40px → approximately 32px across breakpoints; weight 400 and uppercase maintained throughout; letter-spacing adjusts proportionally
- **Editorial grid**: Multi-column article grid → 2-column → single stacked column
- **Magazine carousel**: Flickity carousel maintains single-item display at all sizes, proportionally scaled
- **Section spacing**: `170px` sidebar/margin collapses progressively — from `170px` on wide desktop to approximately `25–40px` on mobile
- **Typography**: Serif hierarchy maintained across all sizes; only scale changes, never the typeface selection or weight philosophy

### Image Behavior
- Magazine cover imagery: centered within carousel, full container width, maintains 2:3 (portrait) aspect ratio
- Editorial photography: `object-fit: cover` within grid cells, no border-radius at any breakpoint
- Architectural and interior photography: full-bleed section treatment maintained across breakpoints
- Art direction: crops adjust for mobile portrait orientation but composition philosophy (generous negative space, single focal subject) remains consistent

## 9. Agent Prompt Guide

### Quick Reference
- Primary CTA Border: `2px solid #000000`
- Page Background: `#ffffff`
- Primary Text: `#212121`
- Display Text: `#000000`
- Border / Rule: `1px solid #212121` (bottom only)
- Link Underline: `underline 1px rgb(137, 137, 137)`
- On Dark Text: `#ffffff`
- Scroll Shadow: `rgba(172, 171, 171, 0.3) 0px -1px 10px 0px`
- Modal Shadow: `rgba(0, 0, 0, 0.3) 0px 32px 68px 0px`
- Button Radius: `2px`
- Content Radius: `0px`
- Display Font: `Kinfolk-Serif-Deck` (substitute: `Georgia`)
- Body Font: `Kinfolk-Serif-Text` (substitute: `Georgia`)
- UI Font: `Kinfolk-Sans` (substitute: `Helvetica Neue`, `Arial`)

### Example Component Prompts
- "Create a magazine hero section on pure white (`#ffffff`). Display headline at 80px Kinfolk-Serif-Deck (or Georgia), weight 400, line-height 1.00, letter-spacing -0.4px, color `#000000`, `text-transform: uppercase`. Below the headline, center a magazine cover photograph at approximately 300×400px with `0px` border-radius and no shadow. Below the image, place 'Buy | Read' navigation links in Kinfolk-Sans 15px weight 400, `#212121`, letter-spacing 0.15px, separated by a pipe character. All on white, no chromatic color."
- "Design a section heading block with a 1px solid `#212121` top rule, 40px padding above, then a category label in Kinfolk-Sans 13px weight 400 uppercase letter-spacing 0.78px color `#212121`, then a heading in Kinfolk-Serif-Deck 50px weight 400 line-height 1.04 letter-spacing -0.5px color `#000000`. Bottom of section ends with a `1px solid #212121` bottom border. No background fill, no shadow."
- "Build an article card grid — three columns on white background, `0px` gap or `15px` gap. Each card: full-bleed image (16:9 or 3:4 ratio) with `0px` radius, then a category label in Kinfolk-Sans 13px uppercase letter-spacing 0.78px, then a headline in Kinfolk-Serif-Deck 40px weight 400 line-height 1.15 letter-spacing -0.2px color `#000000`. Card separated from next by `1px solid #212121` bottom border. No card background, no shadow, no border around card."
- "Design a CTA button in outline style: transparent background, `2px solid #000000` border, `2px` border-radius, padding `8px 16px`, text in Kinfolk-Serif-Text 14px weight 500 color `#000000`. Hover state: opacity `0.8`, same border and background. On a dark photographic surface, invert: `1px solid #ffffff` border, `#ffffff` text, same radius and font."
- "Create a sticky navigation bar: white (`#ffffff`) background, KINFOLK wordmark SVG left-aligned (~205px wide), hamburger icon SVG right-aligned, `1px solid #212121` bottom border. On scroll, add `rgba(172, 171, 171, 0.3) 0px -1px 10px 0px` shadow. Nav links (on expand): Kinfolk-Sans 15px weight 400 uppercase letter-spacing 0.15px color `#212121`."

### Iteration Guide
1. Typography first — always specify which of the three faces (Deck, Text, Sans) applies to each element before touching layout
2. Resist color — if you feel the urge to add an accent color, pause. The system is monochrome by conviction, not limitation
3. Express hierarchy through scale and transform, not weight — Kinfolk-Serif-Deck is always weight 400; use `text-transform: uppercase` and size to create differentiation
4. Rules over shadows — when you need to separate content, reach for `1px solid #212121` bottom-border before any shadow or background-fill solution
5. Radius is nearly zero — `2px` on interactive elements, `0px` on everything else; never reach for 8px, 12px, or pill-shaped elements
6. Letter-spacing scales inversely with size — tighter at large sizes (negative), slightly open at small UI sizes (positive); match the proportions exactly
7. The `170px` unit is the brand's spatial voice — use it for major structural margins to achieve the magazine-quality air that distinguishes Kinfolk from compressed digital media
8. Hover states reduce opacity, they do not change color or fill — `opacity: 0.8` on hover, `opacity: 0.6` on active is the complete interaction vocabulary for buttons and links