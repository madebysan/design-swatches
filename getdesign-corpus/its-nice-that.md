# Design System Inspired by It's Nice That

## 1. Visual Theme & Atmosphere

It's Nice That's website is a London creative-culture publication built on the editorial logic of a magazine: oversized image grids, generous typographic counter-space, and near-zero interface chrome between you and the work being celebrated. The canvas is pure white (`#ffffff`) — uncompromising, gallery-clean — and primary text sits at a soft near-black mine-shaft (`#2b2b2b`) rather than absolute black, the same convention used by serious arts and design publications to keep long-form reading temperature warm. The whole system is engineered to disappear so creative work can sit center-stage.

The typographic identity carries the entire brand. The publication pairs **Labil** (a contemporary grotesk, used for navigation, captions, eyebrow tags, and UI) with **Bradford** (a transitional serif, used for article body and select editorial moments) — a classic editorial duo that signals "this is a publication, not a product." Display headlines run at 60px Labil weight 400 with a wide 1px letter-spacing — a deliberately editorial setting that reads as confident rather than shouty. The serif drops in for long-form reading at 17–20px Bradford, line-heights between 1.47 and 1.60, restoring the warmth that grotesks alone can't deliver.

What distinguishes It's Nice That most is its **content density paired with negative-space discipline**. The homepage is a near-bezel-less image grid — full-bleed thumbnails butt against each other with hairline 1px borders (`#d6d6d6`) acting as the only separation. There's almost no card chrome, no rounded corners, no shadows on content tiles. The brand's saturated **purple accent (`#6219ff`)** appears only in editorial highlights, sponsored callouts (the "Ones to Watch" lavender wash at `#f9f5ff`), and select hover states — saved as a stamp, never used as decoration. A secondary **yellow (`#ffd519`)** appears on consent/utility chrome only, never editorial.

**Key Characteristics:**
- Pure white (`#ffffff`) canvas — gallery convention, never tinted off-white
- Mine-shaft (`#2b2b2b`) primary text — soft near-black for editorial warmth
- Labil grotesk for UI, captions, eyebrows; Bradford serif for body and headlines
- Hairline `1px solid #d6d6d6` grid borders as the only separator between image tiles
- Saturated purple (`#6219ff`) used as an editorial stamp — never as decoration
- Lavender tint surfaces (`#f9f5ff`) for sponsored / featured editorial moments
- Image grid at full bleed — content first, chrome second
- 60px display headlines with `1px` positive letter-spacing — editorial confidence over typographic bravado

## 2. Color Palette & Roles

### Primary
- **Mine-shaft** (`#2b2b2b`): Dominant text color (2,099 occurrences) — body copy, headlines, navigation, captions. The signature near-black, deliberately not pure black for reading warmth.
- **Pure White** (`#ffffff`): Page canvas — uncompromising white, the gallery convention.
- **True Black** (`#000000`): Reserved for utility chrome (cookie consent body buttons, certain form inputs) — almost never editorial.

### Brand Accent
- **Editorial Purple** (`#6219ff`): The signature stamp — sponsored callouts, "Ones to Watch" branding, certain editorial highlights, focus states. Saturated and unmissable.
- **Light Purple** (`#8147ff`): A slightly lighter interactive variant for nav-bar pill buttons. Used on filter / search chip backgrounds.
- **Lavender Wash** (`#f9f5ff`): Tinted surface for sponsored or featured editorial sections — the "softer" purple-on-paper treatment.

### Neutrals & Text
- **Mine-shaft** (`#2b2b2b`): Body text, headlines, all editorial copy.
- **Mid-Gray** (`#676767`): Secondary text — meta data, timestamps, contributor bylines, caption supplements. ~40% lightness.
- **Dim-Gray** (`#565656`): Tertiary supplementary text — even quieter than mid-gray.
- **Border Gray** (`#d6d6d6`): The hairline border color — the entire grid runs on this.

### Surface & Borders
- **White** (`#ffffff`): Default surface.
- **Soft Surface** (`#f4f4f4` at 64% opacity / rgba(244,244,244,0.64)): Subtle alternative panel for sections that want to feel slightly recessed without breaking the white canvas.
- **Dark Mine-shaft 80%** (`rgba(43, 43, 43, 0.8)`): Used for image overlay scrims and modal backdrops.
- **Border Hairline** (`#d6d6d6`): `1px solid` — the workhorse separator between cards, list items, navigation lanes.
- **Border Black** (`#141414`): Bottom-only borders on tabs and selected list items, for sharp underline emphasis.

### Utility Accents (chrome only)
- **Cookie Yellow** (`#ffd519`): Cookie banner accept button — utility chrome only, never editorial. Treated as a quarantined system color.
- **Default Link Blue** (`#0000ee`): Underlined inline links inside long-form articles — the publication respects the browser default for editorial readability.

### Gradient & Shadow Color
- **Stage Light** (`rgba(43, 43, 43, 0.376) 0px 0px 10000px 0px`): A massive blur-radius shadow used as a vignette / atmospheric stage glow on featured sections — not elevation.
- **Modal Lift** (`rgba(0, 0, 0, 0.08)`): Soft 24/38px diffuse shadow on modal/lightbox surfaces — used sparingly, only for overlays.

It's Nice That is **gradient-free in editorial surfaces**. Solid color relationships and hairline borders carry the entire system.

## 3. Typography Rules

### Font Family
- **Sans / UI / Display**: `LabilVariable`, fallback `Labil`, then `system-ui, sans-serif`. A contemporary grotesk used for navigation, eyebrow tags, captions, button labels, and most display headlines.
- **Serif / Editorial Body**: `Bradford`, no published fallback (substitute `GT Sectra`, `Tiempos Text`, or `Source Serif Pro` externally). A transitional serif used for article body, pull quotes, and select 17–20px reading moments.
- **OpenType Features**: Standard ligatures only.

*Note: Both Labil and Bradford are commercial faces. For external implementations, pair `Inter` + `Source Serif Pro`, or `Söhne` + `Tiempos Text` to approximate the editorial sans/serif duo.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Labil | 60px (3.75rem) | 400 | 1.13 | 1px | Section heads, lead story headline |
| Display Medium | Labil | 35px (2.19rem) | 400 | 1.23 | 1px | Sub-section heads, secondary editorial |
| Lead Body | Bradford | 20px (1.25rem) | 400 | 1.60 | 0.09px | Article intro paragraphs, lead body |
| Editorial Headline | Bradford | 20px (1.25rem) | 400 | 1.15 | normal | Article card titles in grids |
| Eyebrow / UI Label | Labil | 20px (1.25rem) | 400 | 1.30 | 0.8px | Category eyebrows, section labels |
| Article Body | Bradford | 17px (1.06rem) | 400 | 1.47 | 0.09px | Long-form reading |
| Article Body Wide | Bradford | 17px (1.06rem) | 400 | 1.47 | 0.4px | Pull quotes, emphasized passages |
| Nav / Inline UI | Labil | 17px (1.06rem) | 400 | 1.40 | 1px | Navigation links, button labels |
| Meta / Caption Strong | Labil | 13px (0.81rem) | 500 | 1.40 | normal | Bylines, dates, contributor names |
| Caption / Eyebrow Small | Labil | 13px (0.81rem) | 400 | 1.46 | 1px | Tag labels, micro-eyebrows |
| Footer Link | Bradford | 11px (0.69rem) | 400 | 2.91 | 0.09px | Footer column links — wide leading for browse |
| Micro Caption | Labil | 11px (0.69rem) | 400 | 1.45 | 1px | Smallest metadata, dates, footer |

### Principles
- **Sans-serif for chrome, serif for content**: Labil handles all navigation, eyebrow tags, captions, and UI; Bradford handles every long-form reading surface. The split is rigorous and signals "magazine, not product."
- **Positive letter-spacing on Labil**: Headings, eyebrows, and labels use a wide 1px (or 0.8px at smaller sizes) letter-spacing. This is the opposite of most modern brands' negative-tracking convention — it gives Labil a slightly editorial, almost classical confidence.
- **Weight 400 across the board**: Both faces stay at weight 400 for nearly everything. Weight 500 only appears for emphasized meta (bylines, contributor names). No bold (700+) anywhere — the typefaces themselves carry the hierarchy through size, not weight.
- **Generous line-height in serif**: Bradford runs at 1.47–1.60 — deliberate editorial breathing room, not the tight 1.20–1.30 favored by product UIs.
- **Wide leading on small footer links**: Footer links use 11px Bradford at 2.91 line-height — an unusual choice that turns a footer column into a browseable, almost typeset table of contents.

## 4. Component Stylings

### Buttons

**Yellow Utility (Cookie / Accept)**
- Background: Cookie Yellow (`#ffd519`)
- Text: True Black (`#000000`)
- Padding: 17px 20px
- Radius: `0px` (sharp)
- Border: `0`
- Shadow: none
- Font: 13px Labil weight 400
- Hover: background `#dbdbdb`, color `#2b2b2b` (mineshaft), opacity 0.85
- Use: Cookie consent acceptance only — quarantined to system chrome.

**Gray Secondary (Cookie / Decline)**
- Background: Light Gray (`#e8e8e8`)
- Text: Near-Black (`#141414`)
- Padding: 17px 20px
- Radius: `0px`
- Hover: background `#dbdbdb`, color mineshaft, opacity 0.85
- Use: Cookie decline / secondary utility actions.

**Purple Pill (Search / Nav)**
- Background: Light Purple (`#8147ff`)
- Text: White (`#ffffff`)
- Padding: 0 20px (vertically anchored to nav row height)
- Radius: `75px` (full pill)
- Border: `0`
- Shadow: none
- Font: 13px Labil weight 400
- Focus: removes outline cleanly — the pill itself is the focus indicator
- Use: Navigation search button — the only purple pill in the entire UI.

**Dark Inverted Icon (Feed / Action)**
- Background: Mine-shaft (`#2b2b2b`)
- Text/Icon: White (`#ffffff`)
- Padding: 0 (icon-only square)
- Radius: `0px`
- Font: 20px (icon-sized)
- Hover: background gray-100 token
- Focus: `2px solid #000` outline
- Use: Feed action buttons, follow/save toggles.

### Cards & Containers

**Editorial Image Tile (Default Grid Card)**
- Background: White
- Radius: `0px` — sharp corners are the entire grid identity
- Border: `1px solid #d6d6d6` (hairline gray) — the grid is held together by these alone
- Shadow: none
- Padding: 0 on the image; 17px–25.5px on the text caption block beneath
- Image fills full width edge-to-edge; caption sits below in 13px Labil

**Sponsored / Featured Surface**
- Background: Lavender Wash (`#f9f5ff`)
- Radius: `17px` (the editorial mid-radius)
- Border: optional `1px solid #d6d6d6`
- Padding: 25.5px–40px
- Use: Sponsored callouts, "Ones to Watch" series, featured editorial moments — the only surface that's allowed to break the white canvas.

**Soft Section Surface**
- Background: `rgba(244, 244, 244, 0.64)`
- Radius: `0px` or `17px` depending on context
- Use: Quietly-recessed section blocks (newsletter signup, secondary lists) without leaving the white canvas.

### Badges / Tags / Pills

**Category Eyebrow Tag**
- Background: transparent
- Text: Mine-shaft (`#2b2b2b`)
- Border: none (or hairline `#d6d6d6` on certain variants)
- Padding: 4.25px 8.5px
- Radius: `0px` for inline tags, `85px` for filter pills
- Font: 11–13px Labil weight 400, letter-spacing 1px

**Filter Pill**
- Background: White or Lavender Wash
- Border: `1px solid #d6d6d6`
- Radius: `85px` (full pill)
- Padding: 8.5px 17px
- Use: Topic filters, category navigation chips.

### Inputs & Forms

**Email Input**
- Background: White (`#ffffff`)
- Text: Black (`#000000`)
- Border: `0` default — the form sits inside a bordered container instead
- Radius: `0px`
- Padding: 15px 20px 16px (asymmetric — 1px less on top)
- Focus: `2px solid #000` outline replaces the borderless default state
- Font: 17px Labil

**Form Container**
- Background: white or `f9f5ff` for newsletter
- Border: `1px solid #d6d6d6`
- Padding: 25.5px–40px

### Navigation

- Top nav: white bar with Mine-shaft text, hairline `1px solid #d6d6d6` bottom border separating nav from content
- Logo: It's Nice That wordmark on the left, sans
- Right side: search (purple pill), account/feed icons (dark inverted square)
- Hover menus: drop-down panels with serif headlines and sans labels
- Links: 17px Labil weight 400, color `#2b2b2b`, no decoration default
- Hover on body links: `currentcolor` + `text-decoration: underline`
- Sticky behavior: nav fixes to top; transparent variant appears over hero imagery on certain feature articles

### Decorative Elements

**Hairline Grid Separator**
- The single most important decorative element — `1px solid #d6d6d6` separates almost every editorial unit. No shadows, no tints, just the hairline.

**Bottom Underline (Selected)**
- `0px 0px 1px` solid `#141414` — applied to active tab labels and selected list items. The system's only "active state" treatment.

**Ambient Stage Glow**
- `rgba(43, 43, 43, 0.376) 0px 0px 10000px 0px` — a single massive-radius shadow used as an atmospheric vignette around featured imagery. Not elevation, not a card lift — a stage light.

## 5. Layout Principles

### Spacing System
- Base unit: **8.5px** (the dominant value at 644 occurrences) — slightly larger than a typical 8px base, which gives the entire system a hair more breathing room
- Scale: 1px, 4.25px, 8.5px, 17px, 25.5px, 34px, 40px, 63.75px, 80px
- Notable: The scale runs on multiples of 8.5 (8.5, 17, 25.5, 34, 63.75) — an intentional 8.5px rhythm rather than a standard 8px grid. 17px does the heaviest mid-range work; 25.5px is the workhorse section spacer.

### Grid & Container
- The homepage is a **multi-column image grid** that resizes from 4 columns (desktop) → 3 → 2 → 1 (mobile) at the published breakpoints
- Maximum content width: ~1480px before content is pinned and margins balance
- Article reading width: ~660–800px (the 660px and 800px breakpoints exist specifically to control article column width)
- Images and feature heroes regularly break the container for full-bleed treatment

### Whitespace Philosophy
- **Editorial pacing, not airy minimalism**: Sections are tightly packed with content but separated by clear hairline rules and 25.5–40px gutters. The page is dense but never claustrophobic.
- **Image-first density**: Image grids run edge-to-edge with hairline borders, treating the viewport like a magazine spread rather than a product dashboard.
- **Captions hug images**: Caption blocks sit immediately below their image (17px gap), grouped tightly with the visual they describe.

### Border Radius Scale
- **Sharp (`0px`)**: The editorial workhorse — every image tile, every form input, every primary surface
- **Editorial Mid (`17px`)**: Featured/sponsored surfaces only — soft enough to read as a "callout," not a card
- **Pill (`75–85px`)**: Filter chips, search button, category navigation pills
- **No mid-range rounding**: 4–8px radii are absent. The system is editorial-binary: sharp rectangles, soft callouts, or full pills.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text, hero imagery |
| Hairline (Level 1) | `1px solid #d6d6d6` | Grid tile borders, section dividers, form container edges — the system's primary structure |
| Underline (Level 2) | `0 0 1px #141414` bottom-only | Active tabs, selected list items |
| Soft Lift (Level 3) | `rgba(0,0,0,0.08) 0 24px 38px, 0 9px 46px, 0 11px 15px` | Modal overlays, lightbox surfaces, dropdown menus |
| Stage Glow (Level 4) | `rgba(43,43,43,0.376) 0 0 10000px` | Featured editorial vignettes — atmospheric, not elevation |

**Shadow Philosophy**: It's Nice That treats elevation as a magazine treats it: borders and rules, not shadows. The system's primary structural device is the hairline `#d6d6d6` border, not the diffuse drop shadow. Soft shadows appear only on overlay surfaces (modals, lightboxes, menus) where the affordance must lift off the page. The "stage glow" massive-radius shadow is purely atmospheric — it makes featured content feel illuminated, not elevated.

### Decorative Depth
- Borders carry every structural job that shadows do in product UI
- Bottom-only underlines (`0 0 1px`) are the active-state signal across tabs and lists
- No inset shadows, no neumorphic effects, no backdrop blurs in editorial surfaces

## 7. Do's and Don'ts

### Do
- Use Labil grotesk for navigation, captions, eyebrows, and labels — every UI surface
- Use Bradford serif for article body, lead paragraphs, and editorial reading
- Apply hairline `1px solid #d6d6d6` borders as the primary structural separator
- Set headlines at 60px Labil weight 400 with `1px` positive letter-spacing
- Use `#2b2b2b` mine-shaft for all primary text — never pure black for editorial
- Reserve `#6219ff` purple for sponsored callouts, "Ones to Watch," and select editorial stamps
- Use the lavender wash (`#f9f5ff`) for featured/sponsored surfaces only
- Run Bradford body at 17px with line-height 1.47 for long-form reading
- Keep image tiles at `0px` radius — sharp grid corners are the brand
- Use `85px` pill radius for filter chips and the nav-bar search button
- Pure white (`#ffffff`) is the canvas — gallery convention, no off-white tinting

### Don't
- Don't use pure black (`#000000`) for editorial body text — it reads sterile and breaks the warmth
- Don't add box-shadows to image tiles or grid cards — the hairline border is the entire affordance
- Don't introduce mid-range border-radius (4–12px) — the system is binary (sharp / mid-17 / pill)
- Don't tighten letter-spacing on headlines — Labil headlines run with `1px` positive tracking
- Don't pair the purple accent with the cookie yellow — yellow is quarantined system chrome
- Don't use Bradford serif for navigation or button labels — it's a content typeface
- Don't use Labil grotesk for long-form article body — it's a UI typeface
- Don't introduce gradients in editorial surfaces — solid colors and hairlines only
- Don't increase weight beyond 400 for headlines — the typefaces carry hierarchy through size
- Don't tint the page background — `#ffffff` is non-negotiable

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <601px | Single-column grid, 35px headlines, stacked nav |
| Mobile | 601–767px | Single-column with select 2-col grids |
| Tablet Small | 768–900px | 2-column image grids, mid-size headlines |
| Tablet | 900–1080px | 3-column image grids begin, full nav row |
| Desktop | 1080–1280px | 4-column grids, 60px headlines |
| Wide Desktop | 1280–1480px | Full feature layout, hero takeovers |
| XL Desktop | ≥1510px | Maximum content width pinned, balanced margins |

### Touch Targets
- Nav links: 17px text with 17–25.5px padding — comfortable thumb targets
- Filter pills: 8.5px 17px padding minimum (44px+ tap height with line-height)
- Image tiles: full-tile tappable area — no separate "click target" within

### Collapsing Strategy
- **Image grid**: 4 → 3 → 2 → 1 columns as viewport narrows, maintaining hairline borders throughout
- **Headlines**: 60px → 35px → 24px (mobile) — proportional drop, weight 400 maintained
- **Navigation**: full horizontal nav collapses to hamburger below 900px; full-screen overlay on open
- **Article column**: 660–800px reading width on desktop → full-width with side margins on mobile
- **Body type**: Bradford 17px stays at 17px on mobile — never shrinks below the comfortable reading floor

### Image Behavior
- Images stay full-bleed within their tiles at every breakpoint
- Aspect ratios preserved on resize — tiles re-flow column count rather than crop
- Hero feature images compress vertically on mobile but retain editorial framing
- No art direction changes — same imagery adapts across viewports

## 9. Agent Prompt Guide

### Quick Color Reference
- Page Background: White (`#ffffff`)
- Primary Text: Mine-shaft (`#2b2b2b`)
- Secondary Text: Mid-Gray (`#676767`)
- Border Hairline: `#d6d6d6`
- Editorial Accent: Purple (`#6219ff`)
- Sponsored Surface: Lavender Wash (`#f9f5ff`)
- Nav Pill: Light Purple (`#8147ff`)
- Inline Link: Blue (`#0000ee`)
- Modal Shadow: `rgba(0,0,0,0.08) 0 24px 38px`

### Example Component Prompts
- "Build an editorial image grid on white (`#ffffff`). 4 columns desktop, 1px solid `#d6d6d6` hairline borders separating tiles, 0px corner radius. Each tile: full-bleed image, 17px caption block beneath in 13px Labil weight 400 mine-shaft (`#2b2b2b`). No shadows."
- "Create a feature article hero. Headline: 60px Labil weight 400, line-height 1.13, letter-spacing 1px, color `#2b2b2b`. Lead paragraph below: 20px Bradford serif weight 400, line-height 1.60. Caption above headline: 13px Labil weight 500, letter-spacing normal."
- "Design a sponsored callout surface. Background: Lavender Wash (`#f9f5ff`), border-radius 17px, padding 40px. Title: 35px Labil weight 400 with 1px letter-spacing. Body: 17px Bradford line-height 1.47. CTA: pill button (`75px` radius), `#8147ff` background, white text, 13px Labil."
- "Build a filter pill bar. Each pill: white background, `1px solid #d6d6d6`, `85px` radius, padding 8.5px 17px, 13px Labil weight 400 with 1px letter-spacing, color `#2b2b2b`."
- "Create an article reading column at 660–800px width. Body: 17px Bradford weight 400, line-height 1.47, color `#2b2b2b`. Inline links: `#0000ee` underlined. Pull quotes: 20px Bradford with 0.4px letter-spacing on a hairline-bordered block."

### Iteration Guide
1. Default to white (`#ffffff`) canvas and `#2b2b2b` text — never tint either
2. Hairline borders (`1px solid #d6d6d6`) carry structure — reach for them before shadows
3. Labil for chrome (UI, captions, eyebrows); Bradford for content (body, headlines, lead)
4. Headlines run at 60px Labil weight 400 with `1px` positive letter-spacing — wider, not tighter
5. Border radius is binary-ish: `0px` for grid tiles, `17px` for sponsored surfaces, `75–85px` for pills
6. Purple (`#6219ff`) is sacred — sponsored callouts and editorial stamps only, never decoration
7. Lavender wash (`#f9f5ff`) marks featured/sponsored content — the only allowed canvas break
8. Body text stays at weight 400 — let typeface and size carry hierarchy, not weight
9. Bradford line-height runs 1.47–1.60 — generous editorial breathing room, not product-tight
10. Image grids fill the viewport edge-to-edge — content first, chrome second
