# Design System Inspired by MSCHF

## 1. Visual Theme & Atmosphere

MSCHF's website is anti-design as design — a deliberate refusal of the polished startup template, dressed up in stark monochrome chrome that feels closer to a 1990s BBS, an emergency broadcast screen, or a Kinko's poster than a contemporary commerce site. The homepage is one long red wall (`#f00007`, a slightly-off pure red) covered top-to-bottom in white all-caps monospace text — every drop the collective has ever released, listed as raw flat links with zero hierarchy, zero imagery, zero hand-holding. A small "[SHOP]" link sits in the top-right corner like a system notification. The whole composition reads as a manifest, a warning label, and a directory all at once.

The defining typeface is **MSCHFSansMono** — a custom monospace sans, set in uppercase at oversized scale (86.66px / 5.42rem) with crushed line-height (0.86), and used for everything: links, buttons, headings, navigation, drop names. There is no display vs body distinction. There is one type style applied at one size, and the page uses raw scroll length as its only structural device. Where contemporary brands deploy a typographic system, MSCHF deploys a typographic stamp. The flatness is the point — every drop gets the same visual weight, whether it's a $76,000 holy water shoe or a free mobile game, because MSCHF treats the catalog itself as the artwork.

What makes the system distinct is its **ugly-chic confidence**. The hover states aren't subtle tints — links flash to alternate brand colors (yellow `#ffc700`, blue `#40aaff`, white) with no transition, like clicking a 1996 web ring. The button on /shop is a pure rectangle of yellow `#ffc700` with gray text and a hard 3px outline. Border radius is essentially zero across the system. Drop shadows are absent. There are no cards, no panels, no gradients, no illustrations, no icons. The collective treats web design as another medium to subvert — the site itself is a drop.

**Key Characteristics:**
- MSCHFSansMono custom monospace, set uppercase at 86.66px weight 400 — one type style for everything
- Stark red canvas (`#f00007`) with white all-caps body — the homepage IS the artwork
- Hover states flash to alt brand colors (yellow, blue, white) with no transition curve
- 0px border radius across the system — sharp rectangles, period
- No drop shadows, no gradients, no icons, no illustrations — chrome is the antagonist
- Crushed line-height (0.86) on display type — text stacks tighter than it has any business doing
- "[SHOP]" / "[CART]" bracketed nav labels — terminal-style affordances, not buttons
- Drop catalog as homepage — a flat directory of every release, no editorial curation
- Yellow `#ffc700` shop chrome with gray `#84898e` text — deliberately wrong contrast
- Color palette feels chosen from a 16-color VGA box, not a brand workshop

## 2. Color Palette & Roles

### Primary
- **MSCHF Red** (`#f00007`): The signature canvas — homepage background, drop list, manifesto pages. A high-energy near-pure red with a 7-point green nudge that keeps it from feeling corporate. This is the brand. Use it loud, full-bleed, no compromise.
- **Pure White** (`#ffffff`): Primary text on red. All drop names, navigation, body copy on the homepage. No off-white, no warm white — clinical, untreated.
- **Pure Black** (`#000000`): Used sparingly for inverted moments — type on yellow shop chrome, footer text, occasional accent.

### Brand Accents
- **MSCHF Yellow** (`#ffc700`): The shop/CTA color — buttons on /shop, hover states, hazard-stripe energy. Not a brand-warm yellow — it's hi-vis, traffic-cone yellow, the color of a parking-lot sign. Used as a flat fill on action surfaces.
- **MSCHF Blue** (`#40aaff`): Secondary link/hover color — appears on alt navigation, drop sub-pages, and as a hover flash on certain link states. A bright sky blue that recalls early-web hyperlinks before they were tamed.

### Neutrals & Text
- **Pure White** (`#ffffff`): All primary text on the red canvas — drop list, headings, links.
- **Light Gray** (`#e5e7eb`): Default Tailwind border color carried through the build — appears on rare framed elements, dividers, form chrome.
- **MSCHF Gray** (`#84898e`): Button text on yellow CTAs, footer metadata, secondary captions. A flat mid-gray that reads as "system text" — not warm, not cool, just neutral. The deliberately mismatched gray-on-yellow combo is a signature ugly-chic move.

### Surface & Borders
- **Surface Red** (`#f00007`): Default page canvas — full-bleed, edge-to-edge.
- **Surface Yellow** (`#ffc700`): Shop section background and primary button fill.
- **Border Gray** (`rgb(193, 193, 193)`): 1px solid borders on textareas and form inputs — utilitarian, untreated.
- **Outline Stripe** (`rgba(168, 145, 65, 0.3)`): A muted gold-toned 3px solid stripe used as a 0px-0px-0px-3px asymmetric left border on certain section blocks.

### Shadow & Effects
- **System Glow** (`rgb(128, 128, 128) 0px 0px 5px 0px`): The single shadow value in the entire system — a soft gray glow used on one element. Otherwise: no shadows, no elevation.
- **Tailwind Ring** (`rgba(59, 130, 246, 0.5)`): The default Tailwind focus ring carries through unmodified — MSCHF didn't bother to override it. That's on-brand.

### Gradient System
- MSCHF is **gradient-free**. The system runs on solid blocks of saturated color stacked next to each other. No transitions, no fades, no soft surfaces. If two colors meet, they meet at a hard edge.

## 3. Typography Rules

### Font Family
- **Primary**: `MSCHFSansMono`, with fallback: `Arial`, `Helvetica`, `sans-serif`
- **OpenType Features**: None declared — the typeface ships with no stylistic sets, no ligatures, no contextual alternates. What you see is what you get.

*Note: MSCHFSansMono is a custom proprietary typeface. For external implementations, **IBM Plex Mono**, **JetBrains Mono**, or **Berkeley Mono** serve as close substitutes. **Space Mono** at weight 400 is the cheapest web-safe approximation. Whatever you pick, set it uppercase and let it crash into itself.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display / Heading 1 | MSCHFSansMono | 86.6666px (5.42rem) | 400 | 0.86 (crushed) | 0.01px | Primary drop name, manifesto headers — uppercase always |
| Link / Drop Item | MSCHFSansMono | 86.6666px (5.42rem) | 400 | 0.86 | normal | Drop list items — same size as headings, flat hierarchy |
| Button Label | MSCHFSansMono | 86.6666px (5.42rem) | 400 | 0.86 | normal | Massive button labels — buttons are hero elements |
| Sub-heading | MSCHFSansMono | ~32–48px | 400 | 0.90–1.00 | normal | Estimated — drop sub-categories, occasional second tier |
| Body | MSCHFSansMono | 16–20px | 400 | 1.20–1.30 | normal | Drop descriptions, manifesto body copy |
| UI / Nav | MSCHFSansMono | 14–16px | 400 | 1.00 | normal | "[SHOP]" / "[CART]" / footer nav, bracketed |
| Caption | MSCHFSansMono | 12–14px | 400 | 1.20 | normal | Dates, drop numbers, legal |

### Principles
- **One typeface, one weight**: MSCHFSansMono at 400 carries the entire system. There is no bold, no italic, no light. The monospace grid is the structure.
- **Uppercase as default**: Display text, links, headings, drop names — all uppercase. Mixed case appears only in body paragraphs and the rare caption.
- **Crushed line-height**: 0.86 line-height on display type. Letters in adjacent lines almost touch. This creates the dense vertical wall of text effect that defines the homepage.
- **Flat hierarchy**: Drop items and headings share the same size. The system rejects the idea that some content matters more than other content — the listing is the design.
- **Bracketed UI affordances**: Navigation and toggles wrap in square brackets — `[SHOP]`, `[CART]`, `[2024]` — borrowing terminal/CLI conventions to signal "this is interactive."
- **Letter-spacing untouched**: Tracking is essentially default (0.01px is rounding noise). The monospace grid does the spacing work — no manual tightening or loosening.
- **No italic, no bold, no underline**: Emphasis is achieved through color shift, hover flash, or all-caps repetition. Not through type variation.

## 4. Component Stylings

### Buttons

**Yellow Shop Button (Primary)**
- Background: MSCHF Yellow (`#ffc700`)
- Text: MSCHF Gray (`#84898e`)
- Padding: 13.33px 16px
- Radius: `0px` (sharp rectangle)
- Border: `0px solid #e5e7eb`
- Outline: `3px solid #84898e` (offset hard outline)
- Shadow: `none`
- Font: MSCHFSansMono 86.66px weight 400 — yes, a button label is 5.42rem
- Hover: background flips to `transparent`
- Use: Primary shop CTA, drop purchase actions

**Bracketed Link Button**
- Background: transparent
- Text: White (`#ffffff`) on red, or MSCHF Gray (`#84898e`) on yellow
- No padding, no border, no radius
- Font: MSCHFSansMono uppercase, square-bracket-wrapped (`[SHOP]`, `[CART]`)
- Hover: text color flashes to a brand alt (yellow → red, blue → white) with no transition
- Use: Navigation, internal jumps, footer links

**Drop List Link**
- Background: transparent (sits on red canvas)
- Text: White (`#ffffff`)
- Padding: vertical-only, ~13–18px line spacing
- Font: MSCHFSansMono 86.66px weight 400 uppercase, 0.86 line-height
- Hover: underline appears OR color flashes to yellow `#ffc700`
- Use: The homepage drop catalog — every product link

### Cards & Containers
- MSCHF does not use cards. There are no rounded panels, no shadow surfaces, no contained boxes.
- "Containers" are full-bleed colored sections that swap canvas colors (red → yellow → black) at section boundaries.
- When framing IS needed (form inputs), it's a 1px `#c1c1c1` solid border with `2px` radius — minimal, utilitarian, untreated.
- Internal padding: tight when present (10–18px), but most layouts use full-bleed text against the canvas with no padding wrapper.

### Badges / Tags / Pills
- Bracketed text, not pills. `[2024]`, `[SOLD OUT]`, `[NEW]` — square brackets carry the badge function.
- Where pills DO appear (rare): `2px` radius, transparent background, 1px solid border, MSCHFSansMono uppercase at 12–14px.

### Inputs & Forms
- Background: white or transparent
- Border: `1px solid #c1c1c1` (light gray, untreated)
- Radius: `0px` to `2px`
- Font: MSCHFSansMono 14–16px weight 400
- Text color: `#000000` or `#84898e`
- Focus: default Tailwind ring (`rgba(59,130,246,0.5)`) — un-customized, on-brand for the chaos
- Padding: 10–13px vertical, 16px horizontal

### Navigation
- Top nav: minimal — a small logo block (yellow `#ffc700` favicon mark, 36×41px, with 13.33/16/13.33/16 safe zone) on the left, a `[SHOP]` link on the right. That's it.
- The drop catalog IS the navigation. There is no sub-menu, no mega-menu, no breadcrumb.
- Footer: small bracketed links in a row, MSCHFSansMono ~14px gray, no border, no separator
- Sticky behavior: nav does not stick. The site scrolls as one continuous artifact.

### Decorative Elements

**Bracket Wrappers**
- Square brackets around interactive labels: `[SHOP]`, `[CART]`, `[ADD TO CART]`, `[VIEW DROP]`
- Borrowed from terminal/CLI convention — signals "this is a command, not a paragraph"
- Renders in the same MSCHFSansMono uppercase as the surrounding text

**Hard Color Section Breaks**
- When a page changes mode (catalog → shop → drop detail), the canvas color flips with no transition
- Red `#f00007` → Yellow `#ffc700` → Black `#000000` — each section is a different color block
- No gradient bridge, no fade — the sections meet at a hard pixel edge

**Drop Numbering**
- Drops are numbered (`MSCHF DROP #97`) and that numbering appears in the same MSCHFSansMono uppercase as everything else
- Numbers function as both timestamp and identity — the catalog is chronological, not categorized

## 5. Layout Principles

### Spacing System
- Base unit: 8px-ish, but with quirky monospace-grid sub-units (1.33px, 10px, 13.33px, 18.82px)
- Scale: 1.33px, 10px, 13.33px, 16px, 18.82px, 24px, 32px, 48px, 64px, 96px, 128px+
- Notable: The spacing scale carries computed monospace remainders (13.3333px = 0.83rem, 1.33332px = 0.08rem). These aren't designed values — they're what fell out of the grid math. MSCHF didn't tidy them up. That's on-brand.

### Grid & Container
- Max content width: full viewport — MSCHF rarely caps width
- Homepage: single column, full-width, drop list runs floor-to-ceiling
- Drop pages: single-column with a hero image and bracketed metadata stacked below
- Shop: gridded product list, but loose — hand-aligned more than systematized
- Pages frequently break flow with a full-bleed image, video, or solid color block that takes the entire viewport

### Whitespace Philosophy
- **Density over breath**: The homepage packs hundreds of drop links into a single scroll. Where editorial sites breathe, MSCHF crowds.
- **Crushed type rhythm**: 0.86 line-height means the text is denser than the page wants it to be. This is intentional — the wall of names is the artwork.
- **Hard color blocks for pacing**: Sections don't get whitespace separation — they get color-block separation. A red section ends and a yellow section begins.
- **Mobile maintains density**: The collective doesn't loosen up on small screens. The wall stays a wall.

### Border Radius Scale
- Sharp (0px): Default for buttons, sections, containers — the canonical value
- Minimal (2px): Form inputs, the rare framed element
- No mid-range, no pill: MSCHF does not use 4px, 8px, 12px, or 9999px radii. The system is essentially binary at zero — sharp or sharper.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no inset | Default for everything — buttons, links, sections, cards |
| Outline Stamp (Level 1) | `outline: 3px solid #84898e` | Yellow shop button — graphic outline, not elevation |
| Border Frame (Level 2) | `1px solid #c1c1c1` | Form inputs, occasional dividers |
| System Glow (Level 3) | `0px 0px 5px 0px rgb(128, 128, 128)` | One element somewhere — basically vestigial |

**Shadow Philosophy**: MSCHF rejects elevation. There are no atmospheric shadows, no Material-style depth, no `box-shadow: 0 4px 12px rgba(0,0,0,0.1)` softness anywhere. The system is graphically flat — every surface sits at z-index 0. Where depth IS expressed, it's expressed through outline strokes (3px solid) or color-block adjacency, not through light simulation. This is the visual equivalent of refusing to use Helvetica because it's polite.

### Decorative Depth
- Outline strokes (3px solid) replace traditional drop shadows on action surfaces
- Color-block adjacency (red next to yellow next to white) creates "stacking" without z-index
- The single soft glow in the system is almost certainly a leftover from an earlier build — MSCHF likely doesn't know it's there

## 7. Do's and Don'ts

### Do
- Use MSCHFSansMono (or IBM Plex Mono / Space Mono / Berkeley Mono fallback) at weight 400 uppercase for everything
- Set display type at 80–96px with 0.86 line-height — crushed, dense, wall-like
- Use MSCHF Red (`#f00007`) full-bleed as the primary canvas — no gradient, no overlay
- Wrap interactive labels in square brackets (`[SHOP]`, `[CART]`, `[ADD TO CART]`)
- Use MSCHF Yellow (`#ffc700`) only for shop/commerce surfaces — it's a CTA color, not decoration
- Keep border-radius at `0px` for everything except form inputs (max `2px`)
- Use hard outlines (3px solid) instead of drop shadows for action surfaces
- Hover-flash links to brand alts (yellow, blue, white) with no transition curve — keep the snap
- Let drop numbering carry hierarchy (`MSCHF DROP #97`) — it's the only ordering signal
- Embrace deliberately wrong contrast (gray-on-yellow, mismatched alts) — the friction is the brand

### Don't
- Don't soften the typography — MSCHFSansMono in title case or sentence case loses everything
- Don't use bold, italic, or underline for emphasis — color shift and all-caps do that work
- Don't add drop shadows, box shadows, or elevation effects — the system is graphically flat
- Don't introduce gradients, soft surfaces, or atmospheric color — solid blocks only
- Don't tame the hover states — flash to a brand alt with no transition, no easing
- Don't use cards, panels, or contained boxes — full-bleed sections meet at hard edges
- Don't tighten line-height for readability — 0.86 is the brand, not a bug
- Don't use mid-range border-radius (4–16px) — the system reads as 0px or nothing
- Don't sanitize the gray-on-yellow button contrast — the deliberate ugliness is the signal
- Don't add icons, illustrations, or hero imagery on text-only pages — the type IS the artwork
- Don't loosen mobile density — the wall of text stays a wall on small screens
- Don't use any color outside red, yellow, blue, white, gray, black — the palette IS the system

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single column, display type drops to 48–56px, line-height stays at 0.86 |
| Mobile | 375–500px | 56–64px display, drop list still floor-to-ceiling |
| Tablet | 500–1000px | 72–80px display, slight side padding (16–24px) |
| Desktop | 1000–1269px | 86.66px display (the canonical size), full-width canvas |
| Large Desktop | ≥1269px | 86.66–96px display, drop list at full scale |

The dembrandt extraction pulled a single explicit breakpoint at `500px` — MSCHF treats responsive as "make the type smaller and keep going." There is no desktop-vs-mobile redesign, no mobile-only navigation, no progressive disclosure.

### Touch Targets
- Drop links: massive — the 86.66px line-height + vertical padding gives ~100px tap regions
- Bracketed nav links: smaller (~30–44px tall), but still usable
- Yellow shop button: oversized — the button label IS 86.66px, so the tap region is enormous
- Form inputs: standard 40–48px tap height

### Collapsing Strategy
- **Nav**: There's nothing to collapse — `[SHOP]` and `[CART]` are already 2 links. They stay as-is on mobile.
- **Display type**: 86.66px → ~64px → ~48px progressive scaling. Line-height stays at 0.86 throughout.
- **Drop list**: Single column at all breakpoints. The wall remains a wall.
- **Section padding**: 64–96px desktop → 32–48px mobile. Still tight. Still dense.
- **Color blocks**: Section transitions stay hard-edged at all sizes — no responsive softening.

### Image Behavior
- Drop pages use full-bleed product imagery — no aspect ratio adjustment for mobile, the photos crop or letterbox
- Homepage has no images — it's a text wall, which scales fluidly
- Logo wordmark scales but never becomes icon-only
- No art direction changes between breakpoints — what you see on desktop is what you see on mobile, just smaller

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary Canvas: MSCHF Red (`#f00007`)
- Primary Text on Red: White (`#ffffff`)
- Shop / CTA Background: MSCHF Yellow (`#ffc700`)
- CTA Text on Yellow: MSCHF Gray (`#84898e`)
- Hover Flash Alt: Yellow (`#ffc700`) or Blue (`#40aaff`)
- Form Border: Light Gray (`#c1c1c1`)
- Outline Stamp: `3px solid #84898e`
- Section Stripe: `0px 0px 0px 3px solid rgba(168, 145, 65, 0.3)`

### Example Component Prompts
- "Create a homepage on MSCHF Red (`#f00007`) full-bleed. Stack drop names as a vertical list, each rendered in MSCHFSansMono (or IBM Plex Mono fallback) uppercase at 86.66px weight 400, line-height 0.86, color `#ffffff`. No padding wrapper, no card, no separator — just text on canvas. Hover state flips text to MSCHF Yellow (`#ffc700`) with no transition."
- "Build a primary shop button — background MSCHF Yellow (`#ffc700`), text MSCHF Gray (`#84898e`), padding 13.33px 16px, border-radius 0px, outline 3px solid #84898e, no shadow. Label in MSCHFSansMono uppercase at 86.66px weight 400. Hover: background flips to transparent."
- "Design a drop detail page with a hard color section break — top half full-bleed product photography, bottom half solid red `#f00007` with the drop name in MSCHFSansMono uppercase 86.66px white. Bracket the metadata: `[DROP #97]`, `[2024]`, `[SOLD OUT]`. No drop shadow, no card, no rounded corners."
- "Wrap nav affordances in square brackets: `[SHOP]`, `[CART]`, `[ABOUT]`. Render in MSCHFSansMono uppercase ~14–16px white on red, no underline. Hover: color flashes to MSCHF Yellow `#ffc700` with no transition curve."
- "Build a manifesto page with one massive heading — MSCHFSansMono uppercase at 86.66px weight 400, line-height 0.86, full-width on red `#f00007`. Body copy below at 16–20px in same family, mixed case OK, line-height 1.20–1.30. No imagery, no icons."

### Iteration Guide
1. Default to MSCHFSansMono uppercase at 86.66px weight 400 — one type style for nearly everything. Use IBM Plex Mono / Space Mono as fallback.
2. Keep line-height at 0.86 on display — the crushed density IS the design.
3. Use MSCHF Red (`#f00007`) full-bleed for the primary canvas — no gradient, no overlay, no soft surfaces.
4. Set border-radius to `0px` everywhere except form inputs (max `2px`). No mid-range, no pill.
5. Replace drop shadows with hard outlines (3px solid) on action surfaces — graphic, not atmospheric.
6. Wrap interactive labels in square brackets — `[SHOP]`, `[CART]` — terminal-style affordances.
7. Hover states snap to brand alts (yellow, blue, white) with no transition curve. Keep the flash.
8. Embrace gray-on-yellow contrast — the deliberate ugliness is the signal, not a bug.
9. Drop catalog as homepage — flat list of every release, equal weight, chronological numbering.
10. No icons, no illustrations, no gradients, no cards. Type and solid color only — let the chrome carry the brand.
