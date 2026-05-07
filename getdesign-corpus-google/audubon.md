---
version: alpha
name: "Audubon"
description: "Field-guide cream meets midnight-navy depths, with Abril Text serif headlines and amber CTAs anchoring bird-conservation editorial gravity"

colors:
  background: "#ffffff"
  surface: "#161b26"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#252b3a"
  primary: "#3056b5"
  on-primary: "#ffffff"
  border: "#262a36"
  focus-ring: "#3056b5"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Abril Text, ui-sans-serif, system-ui, sans-serif"
    fontSize: 63px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Abril Text, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Abril Text, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Abril Text, ui-sans-serif, system-ui, sans-serif"
    fontSize: 25px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Abril Text, ui-sans-serif, system-ui, sans-serif"
    fontSize: 21px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Abril Text, ui-sans-serif, system-ui, sans-serif"
    fontSize: 19px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Abril Text, ui-sans-serif, system-ui, sans-serif"
    fontSize: 19px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Abril Text, ui-sans-serif, system-ui, sans-serif"
    fontSize: 15px
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

# Audubon Design System

## Overview

Audubon's website is a naturalist's field journal translated into pixels — an editorial system where the gravitas of nineteenth-century ornithological illustration meets the urgent practicality of a conservation campaign. The page opens on a deep navy-black canvas (`#161b26`, `#262A36`) overlaid with large-format wildlife photography that bleeds to every edge, treating the browser window the way an Audubon plate treats a folio page: as a frame for a living creature. Against this atmospheric darkness, the primary donation widget floats in semi-transparent indigo (`#252b3a`), its soft edges dissolving into the photographic background — a contained island of action within a sea of natural imagery.

The tripartite typographic system is the system's defining editorial move. `alternate-gothic-compressed` delivers the punchy, uppercase masthead moments — magazine-cover energy at 63–102px with a compressed 0.78–0.86 line-height that stacks type like the spines of field guides on a shelf. `Abril Text` then takes over for the serious editorial work: seriffed headlines at 36–41px with a warm, nineteenth-century authority that recalls the annotated captions of Audubon's own painted plates. `Gotham Narrow` handles everything functional — navigation, captions, UI labels, buttons — with the workhorse reliability of a birding field guide's index. This three-font system could feel cluttered in lesser hands; here it creates a coherent hierarchy that feels inherited from print magazine tradition rather than assembled from a component library.

The chromatic signature is a deliberate tension between warmth and cool authority. Field-guide cream (`#fff9f0`) serves as the primary light surface — aged paper rather than clinical white, evoking the yellowed pages of vintage ornithological texts. Against the deep navy backgrounds (`#161b26`, `#262A36`, `#132249`), this cream glows with the warmth of candlelight. The amber accent (`#feab01`) — the orange-yellow of a warbler's throat — functions as the system's primary CTA color: conspicuous, natural, impossible to miss. The cobalt blue (`#3056b5`) anchors interactive and informational UI, a kingfisher-blue that reads as both aquatic and authoritative. Conservation green (`#00705c`) rounds out the semantic palette as a secondary action and badge color, nodding to the habitats Audubon protects.

**Key Characteristics:**
- Triple-font hierarchy: alternate-gothic-compressed for display, Abril Text for editorial serif heads, Gotham Narrow for all functional UI
- Field-guide cream (`#fff9f0`) as primary light surface — warm parchment, never sterile white
- Deep navy layering: `#161b26` → `#252b3a` → `#262A36` creates atmospheric depth without harsh black
- Amber CTA (`#feab01`) as the single most conspicuous interactive element — warbler-yellow urgency
- Cobalt blue (`#3056b5`) for primary navigation states, badge fills, and search actions
- Conservation green (`#00705c`) for secondary actions, category tags, and ecological accent moments
- Pill-radius buttons (`30px`) as the dominant interactive shape — organic, natural, un-corporate
- Large-format editorial photography treated as page atmosphere, not decoration
- Inset shadows (`rgba(0,0,0,0.1) 0px 1px 2px 0px inset`) on inputs for tactile field-guide depth
- Uppercase with wide tracking (2.535px) on Gotham Narrow labels — field-guide annotation style

## Colors

### Primary Brand
- **Cobalt Blue** (`#3056b5`): The interactive anchor — used for primary navigation active states, donation amount selectors, search submit buttons, and badge fills. The kingfisher blue of the system.
- **Midnight Navy** (`#161b26`): The deepest primary surface — hero section backgrounds, header containers, and dark-theme primary canvas. Not quite black; always a blue-inflected navy.

### Brand Accent
- **Amber Warbler** (`#feab01`): The signature CTA accent — the primary donation button background, "Continue" button fill, background-CTA elements, and key conversion moments. Chromatic warmth in a cool-dark system. Also appears as border color on active state buttons.
- **Bootstrap Amber** (`#ffc107`): A slightly lighter warm-yellow hover-state variant used in focus and active transitions adjacent to the primary amber.

### Conservation Green
- **Teal Green** (`#00705c`): Secondary action color — green card-link buttons, category tag outlines, bordered badge text. Ecological accent; the color of marsh vegetation.
- **Bright Green** (`#00856d`): Hover-state companion to Teal Green on green button variants.

### Text Scale
- **Deep Navy Text** (`#161b26`): Primary body text on light cream surfaces — the darkest readable tone before pure black. Used for dark-on-light button labels, card titles, and link defaults.
- **Pure Black** (`#000000`): Maximum-contrast text; used for amount-box labels, form-critical text, and high-emphasis inline moments.
- **Cream White** (`#fff9f0`): Primary text on all dark/navy surfaces — the system's "warm white," never pure `#ffffff` for editorial text.
- **Warm Taupe** (`#e5e2de`): Secondary text on dark surfaces, tag and badge labels, magazine-card metadata. A parchment-tinted light gray.

### Surface & Borders
- **Block Grey** (`#262A36`): CSS variable `--block-grey-bg` — secondary dark panel background, footer sections, and dark content containers.
- **Dark Panel** (`#252b3a`): Donation widget background, semi-dark overlay panels, modal backdrops.
- **Indigo Dark** (`#132249`): Deepest navy variant for high-emphasis dark sections and deep background layering.
- **Cream Surface** (`#fff9f0`): Primary light background — field-guide cream for content panels, cards, and editorial sections.
- **Sage Tint** (`#f2f5e0`): Very light green-cream for secondary light surfaces and ecological content panels.
- **Pale Sky** (`#bbdef1`): Light blue used for hover/focus state tinting on interactive elements in dark contexts.
- **Soft Blue** (`#a6cbed`): Blue hover/focus surface on list items and category indicators.

### Semantic
- **Salad Green** (`#cbe1a7`): Filled badge background for location/pin tags — the yellow-green of new leaves.
- **Border Sage** (`rgba(60,88,78,0.31)`): Top-only divider on editorial section boundaries — a muted botanical tone.
- **Focus Azure** (`#007bc7`): Accessibility focus ring color, applied as `2px solid` outline universally across all interactive elements.

### Shadows
- **Ambient Shadow** (`rgba(0,0,0,0.1) 0px 0px 10px 0px`): Standard card and widget ambient lift.
- **Inset Shadow** (`rgba(0,0,0,0.1) 0px 1px 2px 0px inset`): Input field tactile depth.
- **Hover Lift** (`rgba(0,0,0,0.21) 0px 6px 12px -4px`): Button hover elevation — the system's most dramatic shadow.
- **Deep Hover** (`rgba(0,0,0,0.7) 0px 6px 12px -4px`): Focus/active state button shadow for maximum accessibility signal.
- **Soft Haze** (`rgba(0,0,0,0.25) 0px 0px 25px 0px`): Wide, soft haze for hero widget containment.

## Typography

### Font Family
- **Display / Masthead**: `alternate-gothic-compressed`, with fallback: `Verdana`, `sans-serif`
- **Editorial Serif**: `Abril Text`, with fallback: `Georgia`, `serif`
- **UI / Functional**: `Gotham Narrow`, with fallback: `Verdana`, `sans-serif`
- **OpenType Features**: Standard — no declared stylistic sets. The personalities of the three typefaces do the differentiation work.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Masthead / Campaign | alternate-gothic-compressed | 102px (6.38rem) | 700 | 0.78 (very tight) | 1px | Uppercase — maximum magazine-cover impact |
| Display / Magazine | alternate-gothic-compressed | 63px (3.94rem) | 700 | 0.86 (very tight) | 0.18px | Uppercase — section hero statements |
| Article Headline | Abril Text | 41px (2.56rem) | 700 | 1.22 | 0.18px | Primary editorial heading — serif authority |
| Article Headline Alt | Abril Text | 41px (2.56rem) | 700 | 1.15 | -0.55px | Tighter tracking variant for dense layouts |
| Section Heading | Abril Text | 36px (2.25rem) | 700 | 1.39 | 0.18px | Sub-section editorial heads |
| Card Heading Serif | Abril Text | 28px (1.75rem) | 700 | 1.11 | 0.18px | Article card titles in serif |
| Section Heading Sans | Gotham Narrow | 40px (2.50rem) | 300 | 1.00 | 0.18px | Functional section heads — light weight |
| Sub-heading Bold | Gotham Narrow | 33px (2.06rem) | 700 | 1.12 | 0.18px | Strong sans sub-heads |
| Sub-heading Medium | Gotham Narrow | 33px (2.06rem) | 600 | 1.12 | -0.165px | Navigation-linked headings |
| Section Mid | Gotham Narrow | 32px (2.00rem) | 600 | 1.09 | 0.18px | Mid-level section anchors |
| Card Title Medium | Gotham Narrow | 26px (1.63rem) | 500 | 1.19 | 0.18px | Card headings in sans |
| Sub-heading Condensed | Gotham Narrow | 23px (1.44rem) | 600 | 1.17 | -0.5px | Tight mid-level headings |
| Sub-heading Standard | Gotham Narrow | 23px (1.44rem) | 700 | 1.17 | 0.18px | Standard weight mid-heads |
| Section Light | Gotham Narrow | 20px (1.25rem) | 300 | 1.00 | 0.18px | Light-weight section sub-labels |
| Body Large | Gotham Narrow | 19px (1.19rem) | 400 | 1.47–1.79 | 0.18–0.19px | Lead paragraph / intro text |
| Body Standard | Gotham Narrow | 18px (1.13rem) | 400 | 1.56 | 0.18px | Main reading text |
| Body Light | Gotham Narrow | 18px (1.13rem) | 300–325 | 1.56 | 0.18px | De-emphasized body / secondary copy |
| Body Bold | Gotham Narrow | 18px (1.13rem) | 700 | 1.56 | 0.18px | Emphasized inline body weight |
| Button Primary | Gotham Narrow | 16px (1.00rem) | 500 | 1.19 | 0.8px | Primary button text — capitalize transform |
| Body Small | Gotham Narrow | 15–15.5px (0.94–0.97rem) | 325–400 | 1.40–1.42 | 0.18px | Compact body and card descriptions |
| Caption Large | Gotham Narrow | 14px (0.88rem) | 300–400 | 1.43 | 0.18px | Photo captions, metadata |
| Caption Standard | Gotham Narrow | 13px (0.81rem) | 400–500 | 1.15–1.69 | 0.13–1.17px | Category labels, small captions |
| Label Uppercase | Gotham Narrow | 13px (0.81rem) | 500 | — | 2.535px | Uppercase field-guide annotation labels |
| Nav Link | Gotham Narrow | 12px (0.75rem) | 500 | 1.10 | 0.18px | Sub-navigation and footer links |
| Micro | Gotham Narrow | 11px (0.69rem) | 500 | 1.10 | 0.18px | Smallest labels and overlines |

### Principles
- **Three-font hierarchy as editorial identity**: alternate-gothic-compressed owns display drama; Abril Text owns editorial authority; Gotham Narrow owns functional utility. Each occupies a defined territory — never interchange them.
- **Compressed display type as masthead energy**: 102px alternate-gothic at line-height 0.78 creates the compressed stacking of a magazine cover — letterforms nearly touching as they lock to the grid.
- **Serif weight consistency**: Abril Text uses weight 700 throughout — there is no light serif in this system. The bold serif headline signals seriousness about conservation; half-measures would undermine the authority.
- **Gotham Narrow's wide spacing on labels**: Uppercase Gotham Narrow captions at 2.535px letter-spacing create the feel of field-guide plate annotations — wide-tracked, authoritative, informational.
- **Capitalize transform on CTAs**: Primary buttons use `text-transform: capitalize` rather than uppercase — a softer, editorial choice that reads as a natural-language invitation ("Continue", "Donate") rather than a command.

## Layout

### Spacing System
- Base unit: 8px
- Scale: 1px, 4px, 5px, 6px, 7px, 8px, 10px, 12px, 14px, 15px, 16px, 17px, 18px, 19px, 20px, 21px, 25px, 30px, 40px, 50px
- Notable: the 18–20px band is the most-used mid-range — card padding, section gutters, and nav spacing all cluster here. The 6px and 10px values handle micro-spacing between tags and badges.
- Button padding: `6px 14px 5px` (standard pill) or `8px 14px` (slightly taller secondary)

### Grid & Container
- Max content width: approximately 1200–1400px centered
- Hero: full-bleed photography, donation widget floating right at ~60% viewport width on desktop
- Article grids: 3-column card layouts on desktop, collapsing to 2 then 1
- Magazine section: editorial 2-column (image + text block) or 3-column card grid
- Full-width dark sections with `#262A36` or `#161b26` backgrounds alternate with cream `#fff9f0` editorial sections

### Whitespace Philosophy
- **Naturalist breathing room**: Sections are given generous vertical space — the way plates in a field guide never crowd. Hero photography needs air to breathe; tightly packed editorial sections follow only for article listings.
- **Cream and dark alternation**: The page alternates between cream editorial panels and dark navy atmospheric sections, creating a rhythm like alternating spreads in a print magazine — dark for emotion and photography, light for reading and discovery.
- **Widget as focal island**: The donation widget floats as a contained card over the hero — enough internal padding (20px+) that its cream/navy surfaces feel like a premium instrument panel rather than a form.

### Border Radius Scale
| Value | Context |
|-------|---------|
| 0px | Flat-edge containers, section dividers, image crops in some contexts |
| 2px | Cards and badge micro-rounding |
| 5px | Input fields, amount boxes, small interactive elements |
| 6px | Category tags and badge pills |
| 8px | Standard card images, input containers |
| 10px | Standard content cards |
| 16px | Featured cards, image crops |
| 20px | Modal containers |
| 25px | Specific icon buttons |
| 30px | Primary pill buttons — the dominant button radius |
| 40px | Listbox bottom-rounding |
| 50% | Avatar circles, social icon buttons |

## Elevation & Depth

| Level | Box Shadow Value | Use Case |
|-------|-----------------|----------|
| Flat (0) | None | Page backgrounds, section containers, flat editorial panels |
| Inset (1) | `rgba(0,0,0,0.1) 0px 1px 2px 0px inset` | Input fields — tactile depth suggesting a filled container |
| Ambient (2) | `rgba(0,0,0,0.1) 0px 0px 10px 0px` | Cards, widgets, interactive panels in soft elevation |
| Hover Lift (3) | `rgba(0,0,0,0.21) 0px 6px 12px -4px` + `translateY(-1px)` | Button hover state — physical upward press sensation |
| Hero Haze (4) | `rgba(0,0,0,0.25) 0px 0px 25px 0px` | Wide diffuse haze for donation widget containment over photography |
| Focus Deep (5) | `rgba(0,0,0,0.7) 0px 6px 12px -4px` | Active/focus state buttons — maximum accessibility signal |

**Shadow Philosophy**: Audubon's shadow system is naturalistic rather than architectural. Rather than the precise geometric shadows of fintech or the ring-based shadows of tech brands, Audubon uses soft, diffuse drops — the way dappled light falls through a forest canopy. The inset shadow on input fields (`rgba(0,0,0,0.1) 0px 1px 2px 0px inset`) gives forms a physical, tactile quality, as if the fields are pressed into the page's surface. The dramatic hover shadow (`rgba(0,0,0,0.21) 0px 6px 12px -4px` with upward translation) gives primary CTAs a satisfying physical-press sensation. Both techniques reinforce the analogue, naturalist quality of the system without resorting to excessive decoration.

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

**Primary Amber CTA ("Continue", "Donate")**
- Background: `#feab01`
- Text: `#161b26`
- Padding: `6px 14px 5px`
- Radius: `30px` (pill)
- Border: `2px solid #feab01`
- Shadow: none (default), `rgba(0,0,0,0.21) 0px 6px 12px -4px` + `translateY(-1px)` on hover
- Font: 16px Gotham Narrow weight 500, `text-transform: capitalize`, letter-spacing 0.8px
- Hover: background `#444444`, color `#007bc7`, border `1px solid var(--azure)`
- Active: background `#fff9f0`
- Focus: background `var(--green-700)`, color `#000000`, border `2px solid #007bc7`, outline `#007bc7 solid 2px`

**Black Solid ("Near Me" button)**
- Background: `#161b26`
- Text: `#fff9f0`
- Padding: `8px 14px`
- Radius: `30px` (pill)
- Border: `2px solid #161b26`
- Font: 16px Gotham Narrow weight 500
- Hover: background transparent, color `var(--warm-200)`
- Focus: outline `#007bc7 solid 2px`, border `6px solid #007bc7`

**Ghost Cream (on dark surfaces)**
- Background: transparent
- Text: `#fff9f0`
- Padding: `8px 14px`
- Radius: `30px` (pill)
- Border: `2px solid #fff9f0`
- Font: 16px Gotham Narrow weight 500
- Hover: background `#444444`, color `#007bc7`, shadow `rgba(0,0,0,0.21) 0px 6px 12px -4px`, `translateY(-1px)`
- Active: background `#fff9f0`
- Focus: background `var(--green-700)`, color `#000000`, outline `#007bc7 solid 2px`

**Ghost Warm Green (on dark sections)**
- Background: transparent
- Text: `#ddecC6` (warm light green `rgb(221,236,198)`)
- Padding: `6px 14px 5px`
- Radius: `30px` (pill)
- Border: `2px solid rgb(221,236,198)`
- Font: 16px Gotham Narrow weight 500
- Hover: background transparent, color `var(--warm-200)`

**Green Solid (Card CTA)**
- Background: `#00856d`
- Text: `#fff9f0`
- Padding: `8px 14px`
- Radius: `30px` (pill)
- Border: `2px solid #00856d`
- Font: 16px Gotham Narrow weight 500
- Hover: background `#444444`, color `#007bc7`, shadow `rgba(0,0,0,0.21) 0px 6px 12px -4px`

**Blue Solid (Search Submit)**
- Background: `#4670d9` (rgb(70,112,217))
- Text: `#fff9f0`
- Padding: `8px 14px`
- Radius: `30px` (pill)
- Border: `2px solid #4670d9`
- Font: 16px Gotham Narrow weight 500
- Hover: background `#02071a`, color `#ffffff`

**Amount Box (Donation selector)**
- Background: transparent
- Text: `#000000`
- Padding: `1px 6px`
- Radius: `5px`
- Border: `2px solid #000000`
- Font: 18px Gotham Narrow weight 400
- Selected/Active: background `#3056b5`, color `#fff9f0`, border `2px solid #3056b5`
- Focus: outline `#007bc7 solid 2px`

### Cards
- Background: `#fff9f0` (cream) on light sections; `#262A36` on dark sections
- Border: none (default) or `1px 0px 0px solid rgba(60,88,78,0.31)` (top-only botanical divider)
- Radius: `10px` (standard content cards), `16px` (featured/promoted cards)
- Shadow: `rgba(0,0,0,0.1) 0px 0px 10px 0px` (ambient)
- Image: `border-radius: 16px 0px 0px 16px` or `16px` on card imagery
- Internal padding: 18–20px

### Badges / Tags

**Green Outline Tag (Category)**
- Background: transparent
- Text: `#00705c`
- Padding: `6px 15px`
- Radius: `6px`
- Border: `1px solid #00705c`
- Font: 13px Gotham Narrow weight 500, letter-spacing 1.17px
- Use: "News", "Policy & Advocacy", "Community Science" categories

**Salad Filled Tag (Location/Pin)**
- Background: `#cbe1a7`
- Text: `#00705c`
- Padding: `6px 15px 6px 10px`
- Radius: `6px`
- Border: `1px solid #cbe1a7`
- Font: 13px Gotham Narrow weight 500, letter-spacing 1.17px
- Use: location-tagged content with pin icon prefix

**Cream Outline Tag (on dark surfaces)**
- Background: transparent
- Text: `#e5e2de`
- Padding: `6px 15px`
- Radius: `6px`
- Border: `1px solid #e5e2de`
- Font: 13px Gotham Narrow weight 500, letter-spacing 1.17px

**Active Filter Tag (selected state)**
- Background: `#e5e2de`
- Text: `#262A36`
- Padding: `6px 15px`
- Radius: `6px`
- Border: `1px solid #262A36`
- Font: 13px Gotham Narrow weight 500

### Inputs & Forms

**Dark Panel Email Input**
- Background: `rgb(46,50,66)`
- Text: `#ffffff`
- Border: `1px solid rgb(166,166,166)` (left/bottom/top sides)
- Radius: `8px 0px 0px 8px` (left half of paired input)
- Padding: `27px 16px 8px` (generous top for floating label)
- Shadow: `rgba(0,0,0,0.1) 0px 1px 2px 0px inset`
- Focus: background `#02071a`, outline `#007bc7 solid 2px`, border-color `#d4d4d4`

**Search Input**
- Background: transparent
- Text: `#ffffff`
- Border: `0px` (borderless — contained by search wrapper)
- Radius: `7px`
- Padding: `8px 120px 8px 45px`
- Shadow: `rgba(0,0,0,0.1) 0px 1px 2px 0px inset`
- Focus: background `#02071a`, outline `#007bc7 solid 2px`

**Donation Amount Number Input**
- Background: transparent
- Text: `#000000`
- Border: `2px solid #000000`
- Radius: `5px`
- Padding: `8px 16px`
- Shadow: `rgba(0,0,0,0.1) 0px 1px 2px 0px inset`
- Focus: background `#ffffff`, outline `#007bc7 solid 2px`

### Navigation
- Top bar: two-tier structure — utility links ("Magazine", "Español") at 12–13px Gotham Narrow weight 400 against deep navy; primary nav below with dropdown mega-menus
- Nav links: Gotham Narrow weight 500, active state underlined or highlighted
- "Near Me" geo-button: black pill (`#161b26`) with location icon, `30px` radius, cream text
- "Donate" button: amber pill (`#feab01`), `30px` radius, navy text — the hero CTA even in the nav
- Active nav item: underline indicator, cobalt blue (`#3056b5`) accent
- Background: deep navy `#161b26` on dark header; `#fff9f0` cream for sub-nav panels
- Dropdowns: cream-surface panels with categorical link groupings, light botanical border separators

### Links
- **Default (on light surfaces)**: `#161b26`, `text-decoration: underline`, weight 500 → hover to `#007bc7`, no underline
- **Default (on dark surfaces)**: `#fff9f0`, no underline, weight 400 → hover to `#007bc7`
- **Taupe on dark**: `#e5e2de`, no underline, weight 500 → hover to `#007bc7`
- **Green accent links**: `#00705c`, no underline, weight 500 → hover to `#007bc7`
- **Sky blue highlight links**: `rgb(30,188,246)`, underline, weight 500 → hover to `#007bc7`

## Do's and Don'ts

**Do:**
- Use `alternate-gothic-compressed` in uppercase at 63–102px for campaign and masthead moments — compressed line-height (0.78–0.86) is mandatory for the stacked display effect
- Use `Abril Text` weight 700 for all editorial article headlines — the bold serif is non-negotiable for conservation authority
- Use `Gotham Narrow` for all UI elements, navigation, captions, buttons, and form labels — it is the functional workhorse across the entire system
- Apply `30px` border-radius (pill) to all standalone call-to-action buttons — the organic pill shape is the system's interactive signature
- Use field-guide cream (`#fff9f0`) as the primary light surface — never substitute pure white `#ffffff` for editorial content panels
- Apply amber (`#feab01`) exclusively to the highest-priority conversion CTA per screen — its power comes from restraint
- Use `text-transform: capitalize` on primary button labels for editorial softness ("Continue", "Donate Now")
- Keep letter-spacing wide (1.17px–2.535px) on uppercase Gotham Narrow labels — annotation-style tracking defines the field-guide aesthetic
- Layer dark navy surfaces (`#161b26` → `#252b3a` → `#262A36`) to create atmospheric depth beneath hero photography

**Don't:**
- Don't use `Abril Text` for UI elements, buttons, or navigation — the serif is editorial-only
- Don't use pure white (`#ffffff`) as a page background on editorial sections — cream (`#fff9f0`) is the correct warm canvas
- Don't apply the amber CTA color (`#feab01`) to decorative elements or secondary badges — amber is a conversion signal, not a theme color
- Don't use square or sharp corners (0px radius) on buttons — the pill shape (`30px`) is the system's interactive identity
- Don't use small border-radius (2–4px) on primary action buttons — reserve tight rounding for badges and inputs only
- Don't introduce cool gray neutrals without blue undertones — every "gray" in this system carries a hint of navy or sage
- Don't apply uppercase transform to Abril Text headlines — serif display text is always title-case or sentence-case
- Don't use `alternate-gothic-compressed` below 40px — at small sizes it loses its compressed drama and becomes difficult to read

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Small Mobile | ≤375px | Single column, hero full-bleed below nav, donation widget full-width |
| Mobile | 376–480px | Single column, reduced hero type scale, stacked nav |
| Large Mobile | 481–600px | Slightly wider cards, 2-column micro-grid begins |
| Tablet Small | 601–768px | 2-column article grids, hamburger nav |
| Tablet | 769–960px | Full 2-column editorial layouts, donation widget alongside hero |
| Desktop Small | 961–1080px | 3-column article cards, full horizontal nav, hero side-by-side |
| Desktop | 1081–1260px | Full layout at standard width, 3-column grids |
| Large Desktop | 1261–1440px | Maximum layout, generous gutters, full-bleed hero |
| XL | ≥1441px | Extended container, wide hero photography, full masthead type |

### Touch Targets
- Primary pill buttons: min 44px height achieved through `8px 14px` padding on 18px text
- Navigation links: adequate spacing for thumb navigation — 44×44px tap areas minimum
- Donation amount boxes: `1px 6px` padding (compact) — these are adjacent and may need larger tap areas on mobile; min 40px recommended
- Category tags: `6px 15px` padding — meets touch minimums for tap

### Collapsing Strategy
- **Navigation**: Full horizontal mega-menu → hamburger drawer on mobile, "Near Me" and "Donate" remain visible as priority actions
- **Hero**: Full-bleed photography + floating donation widget side-by-side → stacked (image above, widget below) on tablet and mobile
- **Article grids**: 3-column → 2-column → 1-column progressive collapse
- **Type scale**: alternate-gothic-compressed 102px → 63px → 41px across breakpoints; Abril Text 41px → 28px → 24px on mobile
- **Section padding**: 50px+ desktop sections → 30px → 20px mobile, maintaining the editorial breathing rhythm
- **Donation widget**: Fixed-width panel → full-width card on mobile, internal grid adjusts from 3-column amount buttons to 2×3 grid

### Image Behavior
- Hero photography is full-bleed at all breakpoints using `object-fit: cover` — the naturalist image always fills its frame
- Cards use `border-radius: 16px 0px 0px 16px` (left-side image rounding) on landscape layouts → full `16px` on stacked mobile cards
- Magazine cover imagery maintains aspect ratio within cards, never stretched
- Lazy loading for below-fold article photography via Drupal/React framework handling

---

## Agent Prompt Guide

### Quick Reference
- Primary CTA: Amber Warbler (`#feab01`)
- Page Background (light): Field-Guide Cream (`#fff9f0`)
- Page Background (dark): Midnight Navy (`#161b26`)
- Dark Panel: Block Grey (`#262A36`)
- Primary Text (light surfaces): Deep Navy (`#161b26`)
- Primary Text (dark surfaces): Cream White (`#fff9f0`)
- Secondary Text (dark): Warm Taupe (`#e5e2de`)
- Interactive Blue: Cobalt (`#3056b5`)
- Conservation Green: Teal (`#00705c`)
- Link Hover: Azure (`#007bc7`)
- Tag Background (filled): Salad Green (`#cbe1a7`)
- Focus Ring: `#007bc7 solid 2px`

### Example Component Prompts
- "Create a hero section with full-bleed bird photography as a background with a dark navy overlay (`rgba(22,27,38,0.6)`). Over the image, float a donation widget panel with background `#252b3a`, 16px border-radius, and ambient shadow `rgba(0,0,0,0.25) 0px 0px 25px 0px`. Inside: headline in Abril Text 41px weight 700 color `#fff9f0`, line-height 1.22; subtitle in Gotham Narrow 18px weight 400 color `#e5e2de`, line-height 1.56; frequency tabs (Every Month / Once a Year / Just this Once) as bordered pill buttons `30px` radius in cobalt `#3056b5`; amount grid as `2px solid #000000` amount boxes with `5px` radius; Continue button in amber `#feab01` with navy text `#161b26`, `30px` radius, `6px 14px 5px` padding, Gotham Narrow 16px weight 500."
- "Design an article card on cream `#fff9f0` with `10px` radius and `rgba(0,0,0,0.1) 0px 0px 10px 0px` ambient shadow. Image top with `16px` radius crop. Below: a green outline tag (background transparent, text `#00705c`, border `1px solid #00705c`, `6px` radius, 13px Gotham Narrow weight 500, letter-spacing 1.17px). Article headline in Abril Text 28px weight 700, color `#161b26`, line-height 1.11. Deck text in Gotham Narrow 15px weight 400, color `#161b26`, line-height 1.40. Green card-link button (`#00856d` background, `#fff9f0` text, `30px` radius, `8px 14px` padding)."
- "Build a conservation section banner on dark navy `#262A36`. Left-aligned masthead in alternate-gothic-compressed 63px weight 700, uppercase, line-height 0.86, letter-spacing 0.18px, color `#fff9f0`. Subhead in Gotham Narrow 18px weight 300, line-height 1.56, color `#e5e2de`. Ghost button (transparent background, `#fff9f0` text, `2px solid #fff9f0` border, `30px` radius, 16px Gotham Narrow weight 500). Botanical divider above section: `1px solid rgba(60,88,78,0.31)` top-border only."
- "Create a navigation bar on deep navy `#161b26`. Left: Audubon wordmark/bird logo in cream. Center: Gotham Narrow 13px weight 500 horizontal nav links in `#fff9f0`, active state underlined. Right: 'Near Me' pill button (background `#161b26`, border `2px solid #fff9f0`, text `#fff9f0`, `30px` radius, Font Awesome location icon prefix) and 'Donate' pill button (background `#feab01`, text `#161b26`, border `2px solid #feab01`, `30px` radius, 16px Gotham Narrow weight 500)."
- "Design a location badge and category tag pair. Location badge: background `#cbe1a7`, text `#00705c`, padding `6px 15px 6px 10px`, radius `6px`, border `1px solid #cbe1a7`, 13px Gotham Narrow weight 500, letter-spacing 1.17px, pin icon prefix. Category tag: background transparent, text `#00705c`, border `1px solid #00705c`, same padding and font. Arrange horizontally with 6px gap."

### Iteration Guide
1. Always establish which typographic register you're in: campaign (alternate-gothic-compressed uppercase), editorial (Abril Text bold serif), or functional (Gotham Narrow) — never mix roles within a single text block
2. Check the surface color before setting text: cream `#fff9f0` takes navy text `#161b26`; dark navy takes cream text `#fff9f0` or warm taupe `#e5e2de`
3. The amber CTA (`#feab01`) should appear once per composition — on the primary conversion action only. If a secondary CTA exists, use green `#00856d` or the ghost cream variant
4. All standalone buttons take `30px` radius (pill) — only badges/tags use `6px`, inputs use `5–8px`
5. For dark sections, the standard background rotation is: hero deep (`#161b26`) → dark panel (`#262A36`) → deep indigo (`#132249`) for layering. Never use pure `#000000` for editorial sections
6. Uppercase text in Gotham Narrow always needs wide letter-spacing: minimum 1.17px for tags, 2.535px for field-guide annotation labels
7. Apply `rgba(0,0,0,0.1) 0px 1px 2px 0px inset` to all text inputs — the inset shadow is the system's tactile signature on form elements
8. Conservation green (`#00705c`) is the ecological accent — use it for category tags, location markers, and secondary CTAs in nature/science content sections; never use it as a primary CTA competitor to amber
