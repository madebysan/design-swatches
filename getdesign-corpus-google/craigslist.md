---
version: alpha
name: "Craigslist"
description: "Browser-default brutalism: Times New Roman, hyperlink blue, and zero decorative intent since 1995"

colors:
  background: "#ffffff"
  surface: "#222222"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#dddddd"
  primary: "#0000ee"
  on-primary: "#ffffff"
  border: "#cccccc"
  focus-ring: "#0000ee"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Times New Roman, ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Times New Roman, ui-sans-serif, system-ui, sans-serif"
    fontSize: 50px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Times New Roman, ui-sans-serif, system-ui, sans-serif"
    fontSize: 19px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Times New Roman, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Times New Roman, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Times New Roman, ui-sans-serif, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Times New Roman, ui-sans-serif, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Times New Roman, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
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

# Craigslist Design System

## Overview

Craigslist is not a design system — it is a refusal of one. Where every other interface from the mid-nineties has been rebuilt, reskinned, and re-platformed into the contemporary idiom of rounded corners and gradient CTAs, Craigslist has remained exactly itself: a pure information surface where the medium is the index. The page opens on white (`#ffffff`) packed edge-to-edge with hyperlinks in the original browser blue (`#0000ee`), category headers in a warm near-black (`#222222`), and a layout governed not by a design grid but by the structural logic of HTML tables and float-based columns from a pre-flexbox world. The overall impression is of a public library card catalog that was digitized in 1996 and has refused every subsequent renovation — not out of neglect, but out of a kind of principled clarity about what a classifieds board is actually for.

The typographic foundation is a two-tier system that is, on its face, accidental and is, on deeper inspection, functionally perfect. The logotype and primary chrome ("craigslist", the post-an-ad button) are set in Times New Roman at 31px, weight 500 — a medium-weight serif that carries the blunt authority of a newspaper masthead without any of the fussiness of display type. Everything else — every link, every label, every category name — falls to Open Sans at sizes ranging from 10px to 19px, creating a utilitarian sans layer beneath the serif crown. This isn't type-pairing as aesthetic choice; it's the browser rendering the site's declared font stack before any stylesheet had a chance to intercede, preserved as tradition. The result is a voice that feels like it was composed on a typewriter and then posted on a bulletin board, which is precisely the experience it's designed to simulate.

What makes Craigslist's anti-design philosophically coherent rather than merely negligent is its absolute commitment to the hyperlink as the singular UI primitive. The `#0000ee` blue — literally the W3C default anchor color — appears 1,162 times in the raw color data, outnumbering every other color by an order of magnitude. The page is, structurally, a list of links organized by category. Section headers (`community`, `housing`, `jobs`, `for sale`, `gigs`) act as the only navigational hierarchy. Borders are `1px solid #cccccc` or `1px solid #dddddd` — the kind of border a browser draws when you don't specify one. The single shadow in the entire system — `rgba(0,0,0,0.667) 0px 0px 5.6px 0px` — appears exactly once, on the search input. Every other surface is flat.

**Key Characteristics:**
- Times New Roman at 31px weight 500 for the logo — newspaper masthead energy, zero display type pretension
- Hyperlink blue (`#0000ee`) as the singular chromatic accent — the W3C default, preserved without irony
- Open Sans as the body and link typeface — the only concession to post-nineties web design
- Pure white (`#ffffff`) canvas with no background color, tint, or texture — the browser's own default
- Near-black (`#222222`) for section header labels — warm enough to avoid pure-black harshness
- `1px solid #cccccc` as the universal border — the color of a browser's default table cell rule
- Zero box shadows on content elements — one exception only (search input, `rgba(0,0,0,0.667)`)
- Extreme information density: 9+ major category groups, 80+ subcategory links on a single viewport
- Column layout via HTML structural logic — no CSS grid, no flexbox choreography, no responsive breakpoints
- Green link variant (`#009900`) for a specific secondary link state — the only second color in the link system

## Colors

### Primary Brand
- **Hyperlink Blue** (`#0000ee`): The chromatic identity of the entire system — every navigable link, every category name, every action. Not a brand color chosen by a designer; the W3C standard browser anchor color, preserved as gospel. Appears 1,162 times. This is the design.

### Text
- **Near Black** (`#222222`): Primary text color for section headers, body labels, and non-link content. The 627-count workhorse — warmer than pure black, reads as ink on newsprint rather than screen pixel.
- **Pure Black** (`#000000`): System-level text (select menus, native form elements) where the browser asserts its own rendering.

### Surface & Background
- **Pure White** (`#ffffff`): The page background — not a design choice, a default. The browser's own document surface, unremarked upon and unchanged. Every section sits on this.
- **Light Gray** (`#eaeaea`): CTA and panel background — the "post an ad" button, the search input region, the location selector panel. A 182-count neutral that signals "interactive surface" without any visual weight.
- **Medium Gray** (`#cccccc`): Standard border color for dividers, table cells, input outlines, and section separations. The browser's own default border tone, promoted to explicit usage.
- **Warm Gray** (`#dddddd`): Heading bottom-borders (`1px solid #dddddd`) — slightly warmer than `#cccccc`, used specifically for `<h3>` and `<h5>` category header underlines.

### Interactive States
- **Hover/Focus Gray** (`#999999`): A desaturated medium gray for hover state feedback — one of only two hover colors detected.
- **Focus Blue Tint** (`#bacff2`): A pale periwinkle appearing on focus states — the browser's native focus ring color, surfacing through unoverridden default styles.
- **Craigslist Green** (`#009900`): The second link color — a pure web-safe green used for a specific link category (the charitable/nonprofit badge links, Craig's philanthropies section). Not decorative; informational.

### Borders
- **Standard Border** (`#cccccc`): `1px solid` — the universal containment rule for buttons, inputs, section dividers, table cells, and footer separators.
- **Section Divider** (`#dddddd`): `1px solid` — heading-level underlines applied as a bottom border on `<h3>` section title elements.
- **Dark Inline Border** (`#222222`): Right-side and bottom borders used for column separators and header underlines in specific structural contexts.
- **Select Border** (`#767676`): Native browser control border for `<select>` elements — the operating system's own input rendering.

### Shadows
- **Search Shadow** (`rgba(0, 0, 0, 0.667) 0px 0px 5.6px 0px`): The single shadow in the entire system. Applied exclusively to the search input. Reads more as focus reinforcement than elevation signaling — a functional remnant, not a design gesture.

## Typography

### Font Family
- **Logo / Masthead**: `Times New Roman`, with fallback: `Times`, `serif`
- **Body / Links / UI**: `Open Sans`, with fallback: `Helvetica`, `Arial`, `sans-serif`
- **Icon Font**: `icomoon` — custom icon font for the handful of icons present (post icon, star faves, account icon)
- **OpenType Features**: None declared. No `font-feature-settings`, no variable font axes, no stylistic sets. The typefaces render in their factory configurations.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Logotype / Site Title | Times New Roman | 31.33px (1.96rem) | 500 | 1.35 | normal | The newspaper masthead — only headline-scale element |
| Primary Nav / CTA | Times New Roman | 22px (1.38rem) | 400 | 0.73 | normal | "post an ad" button label — compressed line-height, reads as stamp |
| Icon Chrome | icomoon | 22px (1.38rem) | 400 | 1.00 | normal | Toolbar icons (faves, post, acct) |
| Icon Secondary | icomoon | 20px (1.25rem) | 400 | 1.00 | normal | Smaller icon chrome elements |
| Section Header Label | Open Sans | 19px (1.19rem) | 400 | normal | normal | Category headings: "community", "housing", "jobs" |
| Category Link | Open Sans | 16px (1.00rem) | 400 | 1.00 | normal | All individual subcategory hyperlinks |
| Nav Link Bold | Open Sans | 16px (1.00rem) | 700 | 1.50 | normal | Emphasized navigation items |
| UI Text | Open Sans | 16px (1.00rem) | 400 | normal | normal | General body / UI text |
| Body Standard | Open Sans | 15px (0.94rem) | 400 | 1.50 | normal | Reading text, descriptions |
| Sub-link | Open Sans | 15px (0.94rem) | 400 | 1.50 | normal | Secondary navigation links |
| Small Link | Open Sans | 14.4px (0.90rem) | 400 | 1.40 | normal | Tertiary and footer links |
| Small UI | Open Sans | 14.4px (0.90rem) | 400 | 1.40 | normal | Compact UI text |
| Caption Bold | Open Sans | 13.33px (0.83rem) | 700 | normal | normal | Emphasized small labels |
| Caption Link | Open Sans | 13.33px (0.83rem) | 400 | normal | normal | Fine-grain navigational links |
| Caption | Open Sans | 13.33px (0.83rem) | 400 | normal | normal | Metadata, annotations |
| Button Text | Open Sans | 13px (0.81rem) | 400 | 1.23 | normal | Secondary button labels |
| Caption Small | Open Sans | 13px (0.81rem) | 400 | 1.23 | normal | Compact metadata |
| Micro Button | Open Sans | 12px (0.75rem) | 400 | 1.33 | normal | Smallest button text |
| Micro Caption Bold | Open Sans | 11.2px (0.70rem) | 700 | 1.43 | normal | Small bold annotations |
| Micro Link | Open Sans | 11.2px (0.70rem) | 400 | 1.43 | normal | Sub-subcategory links, fine print |
| Nano Link | Open Sans | 10.88px (0.68rem) | 400 | normal | normal | Footer legal text, smallest links |
| Nano Caption | Open Sans | 10px (0.63rem) | 400 | normal | normal | Absolute minimum — copyright, timestamps |

### Principles
- **Serif for identity, sans for everything else**: Times New Roman appears only in the logotype and primary CTA. Its presence there is not a curated typographic choice — it's the browser's default serif font, never replaced. The accidental preservation is now the brand.
- **No letter-spacing, no tracking**: Zero declared letter-spacing anywhere in the system. Text renders at the typeface's own default metrics, unmodified. This is what browsers do when you don't tell them otherwise.
- **Compressed line-height as accident**: The 0.73 line-height on the "post an ad" button is not an intentional design choice — it's the result of font metrics and minimal padding interacting without intervention. It creates a curiously dense, stamp-like label.
- **Weight as the only hierarchy lever**: Within the Open Sans layer, weight (400 vs 700) is the only available signal of importance. No size gradations between link levels — most links are 13–16px regardless of their position in the information hierarchy.
- **Size range compressed at the bottom**: The operative range is 10–19px. There is no display type (24px+) outside the logotype. Everything is editorial density.

## Layout

### Spacing System
- Base unit: 1px — the most-used spacing value (247 instances), followed by 2px (130), 3px (61), 4px (29), 5px (29)
- The spacing scale is sub-8px-dominant: 1, 2, 3, 4, 5, 7, 8, 10 px are the operative values
- Larger jumps: 13.33px (one-third of a `<li>` line-height unit), 16px, and 53.33px (wide categorical separations)
- Padding on individual link items: approximately 1–3px — the minimum to prevent text collision
- Column gutter: achieved through HTML table cell padding or float margins, not explicit CSS gap values

### Grid & Container
- Layout is HTML-structural, not CSS-grid: the page uses a fixed-width centered container of approximately 1140px
- Three-column layout at desktop: left sidebar (help/info), center content (category groups), right sidebar (nearby cities/states)
- Within the center, category sections arrange in 3–4 columns of links using float or table-cell layout
- No max-width token, no container class — the layout width is implicit in the table structure
- Full-width header bar contains the logotype left, borough tabs center-right, toolbar icons far right

### Whitespace Philosophy
- **Information maximalism**: Whitespace is rationed. The page is a directory, not a brochure. Every pixel of vertical space is occupied by a link, a header, or a border. Negative space is not a design value here — it is wasted capacity.
- **Column density as feature**: The four-column link layout within each category section (community, housing, etc.) is not a compromise — it is the interface. Scanning columns of links is the UX paradigm.
- **Margin as separator**: Section separation is accomplished with `1px solid #dddddd` borders and 3–5px of top margin — the minimum legible gap between categorical groups.
- **Browser breathing room**: The only generous spacing is between the logotype and the start of content — approximately 10–20px — which is largely determined by default browser stylesheet margins on heading elements.

### Border Radius Scale
- `0px`: Default for all buttons, inputs, links — the overwhelming majority
- `3px`: Rare — specific div containers
- `4px`: Search input, some div panels, top-tab border-radius (`4px 4px 0px 0px`)
- `5px`: "Post an ad" button and similar panel elements — the maximum radius in the system
- `10px`: One badge element — appears to be browser-generated
- `14px`: One button — likely a specialized UI element
- `16px`: Link anchors in a specific context
- `28px`: One button element — likely account or icon button
- **The radius philosophy**: Zero is the default. Small values (3–5px) appear on interactive elements not because of a design decision but because someone added a minimal softening at some point. There is no radius system — there are radius accidents.

## Elevation & Depth

| Level | Box Shadow Value | Use Case |
|-------|-----------------|----------|
| Flat (Level 0) | `none` | Everything — the default state of all surfaces |
| Search Focus (Level 1) | `rgba(0, 0, 0, 0.667) 0px 0px 5.6px 0px` | Search input — the sole shadow in the system |

Craigslist's depth system is, in its entirety, a single box shadow on a single input. This is not an oversight — it is the logical conclusion of a philosophy where content is depth. The hierarchy of the page is communicated entirely through the visual weight of link density, category header borders, and section grouping. When you need to find "apartments / housing for rent," the depth cue is not a card shadow or a surface elevation — it is the `housing` section header underline in `#dddddd` and the visual cluster of blue links beneath it.

The "depth" of the page is architectural, not visual: sections are separated by borders, not by raised surfaces or layered planes. The `1px solid #cccccc` border between the calendar and the nearby-cities panel communicates containment as effectively as any card shadow, using one pixel of gray instead of a blurred rgba rectangle.

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

**Primary CTA ("post an ad")**
- Background: `#eaeaea`
- Text: `#0000ee`
- Padding: `3px` (effectively — minimal chrome)
- Border-radius: `5px` (top corners); `4px 4px 0px 0px` variant also detected
- Border: `0px solid #cccccc` (baseline — no visible border in default state)
- Box shadow: none
- Font: 22px Times New Roman weight 400, line-height 0.73
- Outline: `#0000ee none 3px` (browser focus outline prep)
- Hover: color shifts toward `#999999` desaturated state
- Use: The single primary action on the page — placed prominently near the logotype

**Ghost / Inline ("bd-button text-only")**
- Background: `#ffffff`
- Text: `#0000ee`
- Padding: `3px`
- Border-radius: `0px`
- Border: none
- Font: 13px Open Sans weight 400, line-height 1.23
- Outline: `#0000ee none 3px`
- Use: Inline sub-area buttons, navigation tab selectors for location (mnh, brk, que, etc.)

**Location Tab (selected state)**
- Background: `#eaeaea`
- Text: `#222222`
- Border-radius: `4px 4px 0px 0px` (top-rounded only — tab pattern)
- Border: `1px 1px 1px 0px solid #cccccc` (three sides — bottom open)
- Use: Active borough/neighborhood selector tab (e.g., "fct" highlighted)

**Yellow Star / Faves Icon Button**
- Background: transparent
- Icon: `icomoon` glyph
- Size: 22px
- Use: Saved searches/favorites — one of three toolbar icon buttons

### Navigation
- **Logotype**: `craigslist` in Times New Roman 31.33px weight 500, `#222222`, with the peace-sign emoji prefix (🕊 via CSS before-content or inline character)
- **Toolbar icons**: icomoon at 22px — faves (star), post (pencil), acct (person silhouette) — right-aligned, `#222222` fill
- **Borough tabs**: Horizontal row of short codes (mnh, brk, que, brx, stn, jsy, lgi, wch, fct) in Open Sans 13–16px, `#0000ee` links, plain text on white, tab-border on selected state
- **Section headers**: `<h3>` elements at 19px Open Sans, `#222222`, with `1px solid #dddddd` bottom border — "community", "housing", "jobs", etc.
- **No sticky behavior**: The nav scrolls off-screen naturally. No fixed positioning, no scroll-aware transforms.

### Links (the primary UI component)
- **Default**: `#0000ee`, no text-decoration in modern rendering (border-bottom `1px solid #0000ee` on some contexts)
- **Visited**: `#551a8b` (browser default purple — unoverridden)
- **Hover**: no explicit color change — cursor shifts to pointer
- **Focus**: `#bacff2` background tint via unoverridden browser focus ring
- **Green variant**: `#009900` — appears on charitable/nonprofit badge links in the footer credits section
- **Font**: Open Sans, sizes 13–16px depending on context, weight 400
- The link IS the component. No wrappers, no cards, no containers. Anchor tags arranged in columns.

### Inputs & Forms

**Search Input**
- Background: `#ffffff`
- Text: `#222222`
- Border: `1px solid #cccccc`
- Border-radius: `4px`
- Padding: minimal (~4–5px)
- Box-shadow: `rgba(0, 0, 0, 0.667) 0px 0px 5.6px 0px` — the only shadow in the system
- Font: Open Sans, inherited size
- Placeholder: browser default

**Language Select**
- Background: `#ffffff`
- Text: `#000000`
- Border: `1px solid #767676` (native OS rendering)
- Border-radius: `0px`
- Padding: `0px`
- Font: inherited system font (browser renders natively)
- Use: "english" language selector in top-right corner — entirely unrestyled OS select element

### Section Headers (pseudo-components)
- `<h3>` or `<h5>` element
- Font: Open Sans 19px weight 400 (or 16px weight 700 for subsection)
- Color: `#222222`
- Bottom-border: `1px solid #dddddd`
- Padding: minimal (2–4px below text)
- Background: none
- Text within is a plain hyperlink if the header itself is navigable

### Badges
- No formal badge component exists in the system
- The `10px` border-radius `badge` element detected is likely a browser-generated pill on a form element
- Category annotations are rendered as plain text or parenthetical inline qualifiers — "(apartments / housing for rent)" etc.

### Calendar Widget
- HTML table-based mini-calendar for "event calendar"
- `<table>` with `<td>` cells, bordered with `1px solid #cccccc`
- Current date highlighted with `#eaeaea` background
- Day numbers are `#0000ee` hyperlinks
- Header row (S M T W T F S) in `#222222`
- No styling beyond native table rendering

## Do's and Don'ts

**Do:**
- Use `#0000ee` for every hyperlink — this is not a color choice, it is the system. Any deviation requires explicit justification.
- Use Times New Roman for the logotype and primary action label — the serif presence at the masthead is the brand's only typographic personality.
- Use Open Sans at 13–16px for all category links and body content — the workhorse range that covers 90% of the interface.
- Use `#222222` for section headers and non-link text — warm near-black reads as ink, which is appropriate for a classifieds board.
- Use `1px solid #cccccc` as the universal border — for dividers, for input outlines, for section edges.
- Use `#eaeaea` as the CTA and interactive-panel surface — the only background color besides white.
- Organize content as columnar link lists grouped under plain-text category headers — the column-of-links IS the component.
- Preserve the density: put as many links as legibly possible on the primary viewport. Sparseness is inappropriate here.

**Don't:**
- Don't add box shadows to cards, panels, or buttons — the single shadow on the search input is the system's upper limit.
- Don't introduce border-radius values above 5px on any content element — and prefer 0px.
- Don't use color for anything other than `#0000ee` links, `#009900` secondary links, `#222222` text, and `#eaeaea` panels.
- Don't add hover states that change background color — the system's hover feedback is the browser cursor change and the link's visited-state purple.
- Don't use display-scale typography (24px+) outside the logotype — the directory model requires uniform small text.
- Don't add whitespace between categories for "breathing room" — density is the feature.
- Don't use custom icon sets or SVG illustrations — the icomoon icon font handles the three icons that exist, and that is sufficient.
- Don't override the visited link color (`#551a8b`) — the browser-native purple that visited links turn is important navigational information.

---

## Responsive Behavior

### Breakpoints
Craigslist has **no detected CSS breakpoints**. The layout is fixed-width HTML, approximately 1140px wide, and does not adapt to viewport size through media queries. At mobile widths, the layout compresses horizontally, requiring horizontal scrolling or column collapse through browser reflow — not through intentional responsive design.

| Name | Width | Key Changes |
|------|-------|-------------|
| Desktop (designed for) | 1024px+ | Full three-column layout, all category groups visible |
| Narrow Desktop | 800–1024px | Content begins to compress, some column wrapping |
| Tablet | 600–800px | Columns collapse, horizontal scroll begins |
| Mobile | <600px | Single-column reflow, requires horizontal scrolling — not designed for |

### Touch Targets
- Links: approximately 13–16px text with 1–3px padding — well below the 44px WCAG touch target recommendation
- "Post an ad" button: approximately 22px height — below touch target standards
- Borough tabs: small, dense — not designed for touch interaction
- The system was designed for desktop mouse interaction; touch usability is an unaddressed concern

### Collapsing Strategy
- There is no collapsing strategy — the site reflows through browser default behavior, not through authored responsive CSS
- Column groups wrap when the viewport narrows, producing a passable single-column result by accident rather than design
- The logotype and toolbar remain in the header, compressing until they stack or overflow
- No art direction, no conditional content, no mobile-specific states

### Image Behavior
- No images on the homepage — the site is purely typographic
- The peace-sign character in the logotype and the Craigslist logo are text/SVG, not raster images
- No product imagery, no photography, no illustration — the information IS the content

---

## Agent Prompt Guide

### Quick Reference
- Primary CTA Color: `#0000ee`
- Page Background: `#ffffff`
- Panel/Button Background: `#eaeaea`
- Primary Text: `#222222`
- Hyperlink: `#0000ee`
- Visited Link: `#551a8b`
- Secondary Link: `#009900`
- Border Standard: `1px solid #cccccc`
- Border Header: `1px solid #dddddd`
- Logotype Font: `Times New Roman, Times, serif`
- Body/Link Font: `Open Sans, Helvetica, Arial, sans-serif`
- Single Shadow: `rgba(0, 0, 0, 0.667) 0px 0px 5.6px 0px` (search only)

### Example Component Prompts
- "Create a Craigslist-style category section with an `<h3>` header ('housing') in Open Sans 19px weight 400, color `#222222`, with a `1px solid #dddddd` bottom border and 3px bottom margin. Below it, render a four-column list of hyperlinks at 15px Open Sans weight 400, color `#0000ee`, line-height 1.50, with 1–2px top padding between items. No cards, no borders on links, no hover backgrounds — plain anchor tags on white (`#ffffff`)."
- "Design a Craigslist homepage header: white background, full-width. Left: the text 'craigslist' in Times New Roman 31.33px weight 500, color `#222222`, preceded by the ☮ character. Center: a row of borough abbreviation links ('mnh brk que brx stn jsy lgi wch') in Open Sans 13px weight 400, color `#0000ee`, with the active tab ('fct') on `#eaeaea` background, `1px solid #cccccc` border on three sides, `border-radius: 4px 4px 0px 0px`, color `#222222`. Right: three icomoon icon labels ('faves', 'post', 'acct') at 20–22px, `#222222`."
- "Build a 'post an ad' button in Times New Roman 22px weight 400, color `#0000ee`, background `#eaeaea`, border-radius `5px`, minimal padding `3px 6px`, no border, no shadow, no hover background. Place it immediately below or beside the logotype. The label should be '📝 post an ad' with the emoji icon prepended."
- "Create a search bar: `<input type='text'>` with placeholder 'search craigslist', background `#ffffff`, border `1px solid #cccccc`, border-radius `4px`, box-shadow `rgba(0, 0, 0, 0.667) 0px 0px 5.6px 0px`, Open Sans 14px, `#222222` text. No submit button styling — plain browser default submit."
- "Render a Craigslist-style page footer: centered, white background, top `1px solid #cccccc` border. Links in Open Sans 11.2px weight 400, color `#0000ee`, arranged horizontally with pipe separators or spaces: 'help · safety · privacy · terms · about · app · sitemap'. Below, `#222222` copyright text at 10px: '© 2026 craigslist'."

### Iteration Guide
1. The link is the atom of this system — every component reduces to a styled or unstyled `<a>` tag. Start there.
2. `#0000ee` is sacred. Do not adjust it for aesthetics, contrast ratios, or brand alignment. It is the brand.
3. Add no decoration to links that isn't already in the browser default: no hover backgrounds, no transition effects, no underline customizations beyond the bottom-border pattern.
4. Open Sans at 13–16px covers the entire body type range. Resist adding sizes outside this band.
5. Times New Roman appears in exactly two places: the logotype and the primary CTA. Everything else is Open Sans.
6. Borders (`1px solid #cccccc`, `1px solid #dddddd`) are the elevation system. Use them to separate, not shadows.
7. `#eaeaea` is the only non-white surface. It signals "interactive panel" — search area, CTA button, selected tab.
8. The visited-link purple (`#551a8b`) is important navigational information — never override it.
9. Density is correct. If a layout feels sparse, add more links. The information IS the design.
10. Never introduce border-radius values above 5px. Prefer 0px. When in doubt, use 0px.
