---
slug: braun
name: Braun
url: https://www.braun.com
domain: braun.com
category: Retail
styles: [Light, Minimal, Mono]
tagline: "Dieter Rams restraint made digital — jet-black canvas, pill CTAs, and a single teal accent that earns every pixel"
fonts: [Braun Linear]
primary_color: "#04857f"
---

# Design System Inspired by Braun

> Dieter Rams restraint made digital — jet-black canvas, pill CTAs, and a single teal accent that earns every pixel

## 1. Visual Theme & Atmosphere

Braun's website is a direct-line descendant of Ulm School functionalism — a digital object that would not embarrass the TS 502 radio or the ET 66 calculator. The hero opens on a near-black cinematic canvas with warm studio photography occupying the full viewport, while product headlines sit in pure white at a confident 48px with no decorative elaboration whatsoever. The visual message is immediate: this is a German engineering company, not a lifestyle brand. Every element earns its presence through function; nothing is there for warmth.

The proprietary `Braun Linear` typeface is the typographic backbone of the entire experience — a clean geometric sans that sits comfortably in the Helvetica Neue lineage while bearing its own optical calibration. Headlines run at weight 400, which is unusual in consumer retail where bold headlines are the default demand-signal. Braun refuses that convention, trusting the typeface's structure to do the work. The result is text that reads less like advertising copy and more like product labeling — informative, authoritative, measured. At display scale (48px, line-height 1.11–1.25), the letterforms feel engineered rather than art-directed.

The signature chromatic move is a single teal-green accent — `#04857f` — used exclusively for the primary "Buy" CTA button. In a system that otherwise operates entirely in black and white, this color lands with the force of a precision instrument: a single fluorescent indicator on an otherwise matte-black control panel. The pill-shaped button radius (`128px`) is the only gesture toward softness in an otherwise rectilinear layout, and even that feels purposeful — a tactile affordance signal derived from decades of ergonomic product design. Hover states on ghost buttons shift to teal with a subtle `translateX(3px)` micro-animation — the only kinetic moment, used sparingly like a click-stop on a Braun volume dial.

**Key Characteristics:**
- Braun Linear at weight 400 for all display and heading sizes — restraint as authority, not timidity
- Pure black (`#000000`) navigation bar with white logotype — the most confident possible brand statement
- Single teal CTA accent (`#04857f`) — the only chromatic color in active UI, used exclusively for primary purchase action
- Full-pill button radius (`128px`) — ergonomic softness against an otherwise rectilinear grid
- Shadowless interface — no drop shadows anywhere; depth achieved through dark/light section contrast
- Full-bleed editorial photography on dark backgrounds, product-lit with studio precision
- `translateX(3px)` micro-animation on button hover — kinetic restraint, not spectacle
- CSS variable product color system (`--color-neo-orange`, `--color-silk-epil7`, etc.) for per-category theming
- Ghost button variants for secondary actions — transparent with solid outline, maintaining the minimal weight

## 2. Color Palette & Roles

### Primary Brand
- **Braun Black** (`#000000`): Navigation background, primary text on light surfaces, primary button fill, dark hero canvas. The dominant color — not a neutral but an active design decision.
- **Braun White** (`#ffffff`): Page background for editorial sections, primary text on dark surfaces, primary negative CTA fill. The canvas that breathes between dark sections.

### Brand Accent
- **Braun Teal** (`#04857f`): The chromatic signature — primary "Buy" CTA background, teal link color in body copy. A deep, slightly muted teal that reads as precise and clinical rather than playful. Applied to one button per hero; its restraint is the point.
- **Teal Hover** (`#099f9b`): The lightened teal variant for hover and focus states on teal-themed elements — a barely perceptible brightening that signals activation.

### Product Category Colors (CSS Variables)
- **Neo Orange** (`#ff6531`): `--color-neo-orange`. Product accent for the Neo personal care line.
- **Neo Orange Bright** (`#ff845c`): `--color-neo-orange-bright`. Lighter orange for Neo category buttons and highlights.
- **Neo Orange Bright Hover** (`#FF5E29`): `--color-neo-orange-bright-hover`. Darker accent for Neo hover states.
- **Series 3 Blue** (`#288FF7`): `--color-series3`. Electric shaver series category accent.
- **Series 5 Amber** (`#FFAA0C`): `--color-series5`. Mid-tier shaver series accent.
- **Series 6 Sky** (`#9EC3F5`): `--color-series6`. Upper-tier shaver series accent.
- **Victoria Blue** (`#4350c6`): `--color-victoria-blue`. Deep blue for premium product moments.
- **Vibrant Blue** (`#3960FD`): `--color-vibrant-blue`. Saturated blue for specific campaign moments.
- **Harmonia Gold** (`#a19486`): `--color-harmonia-gold`. Warm stone for the Harmonia hair care line.
- **Silk Epil 7 Sage** (`#CED8C2`): `--color-silk-epil7`. Sage green for the Silk Epil 7 epilator.
- **Silk Epil 5 Blush** (`#E1CAC7`): `--color-silk-epil5-silk-expert-mini-lady-shaver`. Dusty rose for the Silk Epil 5 / Lady Shaver.
- **Promo Yellow** (`#ffd635`): `--color-light-yellow`. Promotional badge accent — sale indicators and price highlights.
- **Promo Amber** (`#ea9e1c`): `--ps-background-color`. Promotional surface accent.

### Text Scale
- **Primary Text** (`#000000`): Headlines, body copy, nav labels on white surfaces.
- **Primary Text Inverse** (`#ffffff`): Headlines, body copy, nav labels on dark/black surfaces.
- **Contrast Gray** (`#707070`): `--color-contrast-color`. Secondary body text, footnotes, specifications.
- **Mid Gray** (`#9b9b9b`): `--color-dark-mid-gray`. Tertiary text, placeholder text, de-emphasized labels.
- **Hover Dim** (`rgb(86, 86, 86)`): Link hover color — text dims slightly to signal interactivity without color change.

### Surface & Borders
- **Near-White Surface** (`#f7f8fa`): Alternate card and section background — barely distinguishable from white, creates micro-layering.
- **Footer Dark** (`#595c61`): `--color-footer-light-gray`. Footer surface — dark charcoal with a hint of cool blue undertone.
- **Border Neutral** (`#979797`): `--ps-border-color`. Standard dividers, input borders, rule lines.
- **Border Black** (`#000000`): Ghost button borders, tab underlines, emphasis dividers.
- **Footer Divider** (`rgb(89, 92, 97)`): Top-rule separator for footer columns — the same color as the footer surface, rendered as a 1px solid line.

### Semantic
- **Red Alert** (`#FF0000`): `--color-red`. Error states, stock-out indicators. Pure red — no softening.
- **Body Purple** (`#6C6EA4`): `--color-body`. An anomalous purple variable, likely a legacy token not in active visible use on the current homepage.

## 3. Typography Rules

### Font Family
- **Primary**: `Braun Linear`, with fallback: `Helvetica Neue`, `Helvetica`, `Arial`, `sans-serif`
- **Registered variants**: `BraunLinear` (alternate token), `BraunLinearRegular` (regular weight explicit), `BraunLinearBold` (bold weight explicit)
- **OpenType Features**: None detected — the typeface's geometric structure is the style; no stylistic sets required.

*Note: Braun Linear is a proprietary typeface. For external implementations, Helvetica Neue Light at weight 300–400 is the closest structural equivalent. Inter at weight 400 serves as a web-safe alternative.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Braun Linear | 48px (3.00rem) | 400 | 1.11 (very tight) | normal | Full-bleed hero statements on dark photography |
| Display Hero Alt | Braun Linear | 48px (3.00rem) | 400 | 1.25 | normal | Hero statements on lighter editorial sections |
| Section Heading Large | Braun Linear | 40px (2.50rem) | 400 | 1.25 | normal | Feature section anchors, campaign titles |
| Section Heading | Braun Linear | 32px (2.00rem) | 500 | 1.25 | normal | Sub-section heads, category names (medium emphasis) |
| Section Heading Light | Braun Linear | 32px (2.00rem) | 400 | 1.25 | normal | Sub-section heads (standard) |
| Sub-heading Large | Braun Linear | 24px (1.50rem) | 500 | 1.25 | normal | Card titles, feature headings (medium emphasis) |
| Sub-heading | Braun Linear | 24px (1.50rem) | 400 | 1.25 | normal | Card titles, feature headings (standard) |
| Body Large / Button | Braun Linear | 20px (1.25rem) | 500 | 1.50 | normal | Button labels, emphasized body intro |
| Sub-heading Small | Braun Linear | 20px (1.25rem) | 400–500 | 1.25 | normal | Smaller section titles |
| Body / Link | Braun Linear | 16px (1.00rem) | 400 | 1.50 | normal | Standard reading text, navigation links |
| Body Medium | Braun Linear | 16px (1.00rem) | 500 | 1.50 | normal | Emphasized body, active nav items |
| Body Bold | BraunLinearBold | 16px (1.00rem) | 700 | 2.25 | normal | Bold links, strong inline emphasis |
| Caption Standard | Braun Linear | 14px (0.88rem) | 400 | 1.50 | normal | Product specs, metadata, image captions |
| Caption Medium | Braun Linear | 14px (0.88rem) | 500 | 1.50 | normal | Emphasized captions, badge labels |
| Caption Small | BraunLinearRegular | 13px (0.81rem) | 400 | 1.50 | normal | Fine print, footnote references |
| Micro Label | Braun Linear | 12px (0.75rem) | 400–500 | 1.50 | normal | Smallest functional labels, badge text |
| Nano | BraunLinearRegular | 11px (0.69rem) | 400 | 1.36 | normal | Legal fine print, footnote numerals |
| Button Small | Braun Linear | 12px (0.75rem) | 400 | 1.50 | normal | Compact ghost buttons, secondary actions |

### Principles
- **Weight 400 as headline voice**: Braun Linear at regular weight carries every display headline. This is the brand's defining typographic choice — where consumer electronics brands default to bold demand-signals, Braun reads more like an instruction manual than an advertisement. Authority through precision, not volume.
- **Two weights in UI**: Weight 400 for reading, weight 500 for action (buttons, emphasized labels, medium-priority headings). Weight 700 exists only in BraunLinearBold for specific link contexts. The hierarchy is controlled — no headline ever exceeds 500 except in edge-case component contexts.
- **Consistent 1.50 line-height for body**: All text at 12–16px uses line-height 1.50 regardless of context — a metronome-like consistency that reflects engineering documentation culture.
- **Tight display line-height**: 1.11 for the largest hero headlines — text blocks lock into dense, structured masses rather than floating editorial passages. This is product labeling, not poetry.
- **No letter-spacing modifications**: Unlike most premium brands that tighten tracking at display sizes or widen it for labels, Braun Linear uses normal letter-spacing throughout. The typeface's inherent spacing is considered complete as-designed.

## 4. Component Stylings

### Buttons

**Primary Teal (Buy)**
- Background: `#04857f`
- Text: `#ffffff`
- Padding: `8px 24px`
- Radius: `128px`
- Border: none
- Box Shadow: none
- Font: 16px Braun Linear weight 500, line-height 1.50
- Hover: background `#099f9b`, `translateX(3px)` transform, opacity 0.9
- Focus: background `rgb(30, 174, 219)`, border `1px solid #000000`
- Active: background `rgb(44, 100, 21)`, border `1px solid rgba(162, 192, 169, 0.5)`
- Use: Primary purchase CTA — "Buy" — the only teal element on the page

**Primary Black**
- Background: `#000000`
- Text: `#ffffff`
- Padding: `8px 24px`
- Radius: `128px`
- Border: none
- Box Shadow: none
- Font: 16px Braun Linear weight 500
- Hover: `translateX(3px)`, opacity 0.9
- Focus: background `rgb(30, 174, 219)`, border `1px solid #000000`
- Use: Primary action on white/light surfaces

**Primary Negative (White Fill)**
- Background: `#ffffff`
- Text: `#000000`
- Padding: `8px 24px`
- Radius: `128px`
- Border: none
- Font: 16px Braun Linear weight 500
- Hover: `translateX(3px)`, opacity 0.9
- Use: Light-colored CTA on dark/black backgrounds where black fill would disappear

**Ghost Black (Explore)**
- Background: `rgba(0, 0, 0, 0)` (transparent)
- Text: `#000000`
- Padding: `8px 24px`
- Radius: `128px`
- Border: `1px solid #000000`
- Font: 16px Braun Linear weight 500
- Hover: background `rgb(30, 174, 219)`, text `#ffffff`, border `1px solid var(--color-primary)`, opacity 0.9
- Focus: outline `2px solid #000000`, background `rgb(30, 174, 219)`, text `#ffffff`
- Use: Secondary action on white backgrounds — "Explore", "Learn more"

**Ghost Negative (White Outline)**
- Background: `rgba(0, 0, 0, 0)` (transparent)
- Text: `#ffffff`
- Padding: `8px 24px`
- Radius: `128px`
- Border: `1px solid #ffffff`
- Font: 16px Braun Linear weight 500
- Hover: `translateX(3px)`, opacity 0.9
- Use: Secondary action on dark/hero photography backgrounds

**Neo Orange Bright (Campaign)**
- Background: `#ff845c`
- Text: `#000000`
- Padding: `0px 36px`
- Radius: `9999px`
- Border: `1px solid #000000`
- Font: 16px Braun Linear weight 700
- Hover: `translateX(3px)`, opacity 0.9
- Use: Campaign-specific CTAs for the Neo personal care product line

### Cards
- Background: `#ffffff` (on white surfaces) or `#f7f8fa` (alternate near-white)
- Border: none by default; `0px 0px 1px solid #000000` bottom rule for list-style separators
- Radius: `4px` for small UI containers; `128px` reserved for pill button elements only
- Shadow: none — elevation is communicated through background contrast, not shadow
- Image treatment: full-bleed product photography within card, grid-locked composition
- Internal padding: 24–48px vertical, 16–24px horizontal for editorial cards

### Navigation
- Background: `#000000` (pure black)
- Logo: Braun wordmark SVG in white, 75×32px, zero safe-zone — maximum optical presence
- Nav links: Braun Linear 16px weight 400, `#ffffff`, no text decoration
- Active indicator: `0px 0px 2px solid #ffffff` bottom-border underline for active menu items
- Hover: text dims to `rgb(86, 86, 86)` — a receding grey signal, no color change
- Secondary actions (search, account, cart): icon-only, white, right-aligned cluster
- Cart badge: small circular counter on the bag icon
- Sticky: fixed at top, slides beneath hero imagery as page scrolls

### Links
- **White link** (dark surfaces): `#ffffff`, underline default, hover → `rgb(86, 86, 86)`
- **Black link** (light surfaces): `#000000`, underline default, hover → `rgb(86, 86, 86)`
- **Teal link** (body copy accent): `#04857f`, no underline, weight 500, hover → `rgb(86, 86, 86)`

### Inputs & Forms
- No input data extracted from current homepage; inferred from border tokens:
- Border: `1px solid #979797`
- Radius: `4px`
- Font: 16px Braun Linear weight 400
- Focus: likely border shifts to `#000000` based on black focus patterns in button states
- Placeholder: `#9b9b9b` (mid gray)

### Badges / Tags
- **Promotional Badge**: `#ffd635` background (promo yellow), black text, `4px` radius or `100%` circular
- **Cart Count Badge**: circular `100%` radius, small — overlay on navigation cart icon
- No structured badge component detected; product category tags use product-color variables inline

### Footer
- Background: `#595c61` (footer dark charcoal)
- Text: `#ffffff`
- Link: white, weight 400, no decoration
- Dividers: `1px solid rgb(89, 92, 97)` — near-invisible on the dark surface, structural rather than decorative
- Social icon buttons: `50%` radius (fully circular)
- Layout: multi-column grid on desktop, stacked on mobile

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Active scale: 4px, 5px, 8px, 10px, 14px, 15px, 16px, 20px, 24px, 30px, 32px, 48px, 60px, 64px, 90px, 96px
- Button internal padding: `8px 24px` — compact vertical, generous horizontal, consistent across all button variants
- Section vertical spacing: 48px–96px between major content sections
- Card internal padding: 24–48px
- Dense chrome: 4–8px for navigation item spacing and small UI chrome; generous section-level: 64–96px

### Grid & Container
- Max container width: approximately 1200–1400px, centered
- Hero: full-bleed viewport photography with content overlay bottom-left or centered
- Product grids: 3–4 column product card arrays on desktop
- Feature sections: 2-column editorial (image + text) alternating layouts
- Full-width dark cinematic sections alternate with white editorial panels — the core layout rhythm
- Braun Linear headline as primary visual anchor in each section; no decorative dividers

### Whitespace Philosophy
- **Engineering negative space**: Whitespace in Braun's system is not luxurious air — it is precise clearance, like the tolerance between machined parts. Each gap has a structural purpose, not an aesthetic one.
- **Section alternation drives pace**: The page breathes through hard cuts between full-black photography and full-white editorial panels, not through generous internal padding. Within a section, spacing is measured and compact.
- **Product first**: Layout always positions the product image as the dominant compositional element. Typography is secondary — it annotates, it does not compete.

### Border Radius Scale
- `4px`: UI containers, form elements, small chips — the default for rectangular surfaces
- `128px`: All button pill shapes — "Buy", "Explore", "Show all products" — a consistent ergonomic affordance across the entire button system
- `9999px`: Maximum pill (Neo Orange campaign buttons only — an outlier)
- `50%`: Social media icon circles, avatar elements
- `100%`: Badge overlays (cart count)
- **No mid-range values**: The system is deliberately binary — either minimal rounding (4px) or full pill (128px+). Nothing in the 8–64px range.

## 6. Depth & Elevation

| Level | Box Shadow Value | Use Case |
|-------|-----------------|----------|
| Flat (Level 0) | `none` | Everything — page background, cards, buttons, containers, navigation |
| Section Contrast | Background color shift (`#000` to `#fff`) | The primary depth mechanism — dark cinematic vs. light editorial |
| Border Rule | `0px 0px 1px solid #000000` (bottom only) | List item separators, subtle structural dividers |
| Active State | `2px solid #000000` (focus outline) | Keyboard accessibility focus rings |

**Shadow Philosophy**: Braun's system has no shadows. This is not an accident or an omission — it is a philosophical commitment to Dieter Rams' principle of "as little design as possible." Where other systems use multi-layer shadows to communicate hierarchy and elevation, Braun uses only the starkest possible mechanism: the contrast between black surfaces and white surfaces. A product card is not elevated by a shadow; it is elevated by the fact that it is white against a grey or black section. The absence of shadows also means every interactive element — every button, every link — must earn its affordance signaling through shape, color, and typography alone. The pill radius and the single teal accent carry the full weight of that communication.

## 7. Do's and Don'ts

**Do**
- Use Braun Linear at weight 400 for all display headlines — the measured lightness is the brand voice, not a gap to fill with bold
- Reserve teal (`#04857f`) for the single primary purchase CTA per hero section — its power is in scarcity
- Apply `128px` border-radius to every button without exception — the pill shape is the brand's tactile signature
- Use full-bleed, studio-lit photography on dark backgrounds for hero sections — product imagery IS the brand expression
- Alternate hard black and white sections to create layout rhythm — no gradient transitions between environments
- Apply `translateX(3px)` on button hover — the only kinetic moment, kept minimal and directional
- Use per-category CSS color variables (`--color-neo-orange`, `--color-series3`, etc.) for product-line theming
- Use `0px 0px 2px solid white` bottom underline for active navigation state

**Don't**
- Don't use drop shadows anywhere — not on cards, not on nav, not on buttons. The system is explicitly shadow-free
- Don't introduce rounded corners between 5px and 64px — the radius scale is binary: 4px or pill-shaped
- Don't use teal (`#04857f`) for decorative elements, headers, or section backgrounds — its role is primary CTA only
- Don't apply positive letter-spacing to Braun Linear at display sizes — the typeface's own spacing is complete as designed
- Don't use weight 700 in BraunLinearBold for primary headings — it exists only for specific bold link contexts
- Don't introduce warm tones (orange, amber) for primary UI outside of their assigned product-line variables
- Don't soften the navigation bar to grey — `#000000` is the non-negotiable nav surface
- Don't add gradient fills to section backgrounds — solid color contrast is the only depth tool

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Nano | 330px | Minimum supported width — compact single-column |
| Mobile S | 375px | Standard mobile single-column |
| Mobile M | 400–426px | Slightly wider mobile layout |
| Mobile L | 480–530px | Small phablet adjustments |
| Mobile XL | 550–600px | Pre-tablet adjustments |
| Tablet S | 767–769px | Two-column grids begin, nav transitions |
| Tablet | 820–896px | Medium tablet layout |
| Tablet L | 922–992px | Near-desktop layout |
| Desktop S | 1023–1074px | Full navigation, 3-column product grid |
| Desktop | 1199–1200px | Standard desktop container |
| Desktop L | 1300–1400px | Wider content at generous margins |
| Desktop XL | 1540–1600px | Maximum layout scale |

*Note: Braun ships one of the densest breakpoint lists in retail — 28 active breakpoints. This reflects the precision-engineering culture: layout adapts at every meaningful viewport increment, not at three convenient thresholds.*

### Touch Targets
- Buttons: `8px 24px` padding yields approximately 36–44px touch height — meets minimum tap target requirements
- Navigation links: generous spacing around 16px text for thumb navigation
- Social icons: `50%` circular elements at approximately 40–48px diameter
- Cart/search/account icons: clustered right-side nav with adequate inter-icon spacing

### Collapsing Strategy
- **Navigation**: Full horizontal nav with text links collapses to hamburger drawer on mobile; wordmark remains centered or left; icon cluster persists right
- **Hero**: Full-bleed photography maintained at all widths; text overlay repositions from bottom-left to centered-stacked on mobile; headline scale drops from 48px → 32px → 24px
- **Button pairs**: "Buy" + "Explore" side-by-side → stacked vertically on narrow viewports
- **Product grids**: 4-column → 3-column → 2-column → single-column
- **Editorial 2-column sections**: Image + text stacks image above text on mobile
- **Spacing compression**: 96px section gaps → 48px → 32px mobile — scale proportionally but maintain editorial air
- **Category color system**: Product-line CSS variables work identically across all breakpoints

### Image Behavior
- Hero photography maintains full-bleed treatment at every breakpoint using `object-fit: cover`
- Product grid thumbnails scale proportionally within their grid cells
- No art direction breakpoints detected — same image serves all viewport widths
- Studio photography's neutral/dark backgrounds ensure legibility at all sizes without scrims

## 9. Agent Prompt Guide

### Quick Reference
- Primary CTA: Braun Teal (`#04857f`)
- Teal Hover: (`#099f9b`)
- Page Background (light): Pure White (`#ffffff`)
- Page Background (dark/hero): Pure Black (`#000000`)
- Navigation: Pure Black (`#000000`)
- Primary Text (light bg): Black (`#000000`)
- Primary Text (dark bg): White (`#ffffff`)
- Secondary Text: Contrast Gray (`#707070`)
- Tertiary Text: Mid Gray (`#9b9b9b`)
- Button Radius: `128px`
- Border Neutral: (`#979797`)
- Footer Surface: (`#595c61`)
- Promo Yellow: (`#ffd635`)

### Example Component Prompts

- "Create a hero section on pure black (`#000000`) with a full-bleed editorial product photograph covering the entire viewport. In the lower-left quadrant, place a white headline in Braun Linear 48px weight 400, line-height 1.11. Below it, a white subtitle in Braun Linear 16px weight 400, line-height 1.50. Add two pill buttons: primary 'Buy' with background `#04857f`, white text, `128px` border-radius, `8px 24px` padding, 16px Braun Linear weight 500; secondary 'Explore' with transparent background, `1px solid white` border, white text, same radius and padding. Both buttons animate `translateX(3px)` on hover."

- "Design a product card on white (`#ffffff`) background with no shadow and `4px` border-radius. Show a product image filling the top half of the card. Below, a product name in Braun Linear 24px weight 500, line-height 1.25, color `#000000`. A feature description in 16px weight 400, color `#707070`, line-height 1.50. A teal link in Braun Linear 16px weight 500, color `#04857f`, no underline."

- "Build a top navigation bar: full-width black (`#000000`) background, 0 border-radius. Left: Braun wordmark SVG in white, 75×32px. Center: horizontal navigation links — Braun Linear 16px weight 400, white, no underline. Active item has a `0px 0px 2px solid #ffffff` bottom border. Right: search, account, and cart icons in white. Height approximately 56–64px."

- "Create a feature section alternating with a dark hero: white (`#ffffff`) background, 64px vertical padding. Left column: section heading in Braun Linear 32px weight 500, line-height 1.25, color `#000000`. Below, body copy in 16px weight 400, color `#707070`, line-height 1.50. A ghost button: transparent background, `1px solid #000000` border, `128px` radius, `8px 24px` padding, black text, 16px weight 500. Hover: background shifts to `rgb(30, 174, 219)`, text to white. Right column: full-bleed product photography."

- "Design a Neo product campaign section using the Neo color system: background `#ff845c` (Neo Orange Bright). Headline in Braun Linear 40px weight 400, line-height 1.25, color `#000000`. CTA button: background `#ff845c`, border `1px solid #000000`, `9999px` radius, `0px 36px` padding, black text, 16px Braun Linear weight 700. Hover animates `translateX(3px)` at opacity 0.9."

### Iteration Guide
1. Pill radius (`128px`) is non-negotiable on all buttons — if a rectangle appears in a button, the system identity is broken
2. Teal (`#04857f`) is restricted to the primary purchase CTA; every other action uses black, white, or a product-line variable color
3. No shadows anywhere — if depth is needed, use background color contrast between sections, not box-shadow
4. Dark and light sections must be hard cuts — no gradient transitions between the hero-black and editorial-white environments
5. Braun Linear weight 400 is the display headline weight; reach for 500 only on sub-headings and buttons, never on hero display text
6. Product-line color variables (`--color-series3`, `--color-neo-orange`, etc.) are scoped to their category campaigns — do not cross-pollinate them
7. `translateX(3px)` hover animation belongs only on buttons — apply it consistently across all pill button variants
8. For implementations without Braun Linear, use Helvetica Neue at weight 300–400 as the nearest structural equivalent; avoid any typeface with rounded apertures or humanist characteristics