---
slug: criterion
name: The Criterion Collection
url: https://www.criterion.com
domain: criterion.com
category: Media
styles: [Dark, Editorial, Serif]
tagline: "Near-black slate canvas, Mercury serif authority, and gold-ink restraint in service of cinema's greatest works"
fonts: [Mercury Text G1, Gotham Narrow, GothamBook]
primary_color: "#b4841e"
---

# Design System Inspired by The Criterion Collection

> Near-black slate canvas, Mercury serif authority, and gold-ink restraint in service of cinema's greatest works

## 1. Visual Theme & Atmosphere

The Criterion Collection's website is the digital equivalent of a well-curated film archive — austere, deliberate, and completely uninterested in trend. The canvas opens on a near-black charcoal (`#252525`) that reads less as a design choice and more as a curatorial statement: this is not a streaming service competing for casual attention, this is a library. Film stills and poster art bleed edge-to-edge across a full-viewport hero, their colors allowed to breathe in the darkness without competing chromatic noise. The overall impression is of a serious institution that happens to have a website — the refinement of a Cahiers du Cinéma spread translated into pixels.

The type system is where Criterion's editorial identity crystallizes. The primary face is Mercury — H&FJ's newspaper-grade serif family, deployed across two optical variants: MercuryDisplayRegular for the largest hero moments and MercuryTextG1 for reading sizes. Mercury is a typeface associated with the New York Times and the prestige print world; its use here is a direct signal that Criterion considers itself a publishing house as much as a film label. This serif anchor is then paired with Gotham Narrow Bold and Gotham Narrow Medium — both in uppercase with expanded letter-spacing — for all structural UI chrome: navigation labels, button text, filter tags, and category markers. The effect is a clean serif/grotesk division that mirrors the hierarchies of a physical film booklet: the essay text set in a refined roman, the production notes stamped in a tight condensed sans.

The signature chromatic moment arrives in a single color: the warm, almost-amber gold of `#b4841e` — applied to the logo wordmark, the primary CTA button fill, all link underlines, and the active border on interactive elements. This isn't the bright yellow-gold of luxury hospitality brands; it's a more muted, ink-like tone that could have been mixed for letterpress. Against the charcoal canvas, it reads like gilding on a dark cloth binding. Every other chromatic impulse has been suppressed — there are no teals, no gradients, no accent palettes — which makes the gold's appearances feel meaningful rather than decorative.

**Key Characteristics:**
- Near-black charcoal canvas (`#252525`) — not pure black, a warmer-toned dark that absorbs film imagery without crushing it
- Mercury Display at 96px with tight `-0.6px` tracking for the rare major hero text moment
- Gotham Narrow Bold and Medium in uppercase with `1px` letter-spacing for all structural UI labels and navigation
- Criterion Gold (`#b4841e`) as the single chromatic accent — logo, CTA buttons, link states, active borders
- `0px` border-radius on buttons and containers — square, archival, typographic
- Hover states that transition to an unexpected teal (`rgb(30, 174, 219)`) at 0.7 opacity — the one surprise in an otherwise controlled system
- Full-viewport film-still heroes with no gradient scrims — the image stands on its own authority
- Vertical rotated text ("THE CRITERION COLLECTION") running up the left edge of the hero — a print-magazine signature device
- Mercury Italic deployed for pull quotes and captions — the cursive register separating voiced commentary from attributed fact
- `kern` and `liga` OpenType features active on all Mercury text — professional typesetting defaults, not decorative additions

## 2. Color Palette & Roles

### Primary Brand
- **Criterion Charcoal** (`#252525`): The dominant surface — header, dark sections, page backgrounds. Not pure black but a warm very-dark neutral that the dembrandt confirms as the highest-count color across the site. Holds film imagery without competing.
- **Criterion Gold** (`#b4841e`): The brand's singular chromatic anchor. Applied to the logo "C" mark and wordmark, primary button backgrounds, link underlines, and active focus borders. A muted, ink-mixed amber — authoritative without being ornamental.

### Brand Accent
- **Criterion Gold** (`#b4841e`): As above — this IS the primary_color. Its restraint across the system is the point; when it appears, it functions as a stamp of institutional authority.

### Hover / Interactive State
- **Criterion Teal** (`rgb(30, 174, 219)`): The system's surprising hover color — applied uniformly to button, link, and switch hover states at `opacity: 0.7`. It appears nowhere in default states. This single unexpected accent creates delight in the otherwise austere system without breaking it.
- **Livewire Blue** (`#2299dd`): Progress bar color via CSS variable `--livewire-progress-bar-color` — a lighter variant of the teal family, for loading indicators only.
- **Link Hover Blue** (`rgb(56, 96, 190)`): Link hover color on text links — a navy-adjacent blue that provides accessible contrast and a dignified contrast with the gold default state.

### Text Scale
- **White Primary** (`#ffffff`): Primary text on dark surfaces, hero overlay type, navigation links against the charcoal header, button text on gold backgrounds.
- **Silver Mid** (`#8e8e8e`): Secondary text, metadata, de-emphasized captions, footer footnotes. The only mid-tone gray in the text system.
- **Charcoal Body** (`#252525`): Primary text on white/light surfaces — the same charcoal that forms the dark canvas, now serving as body copy color on light sections.
- **Hover Dark** (`#272625`): Barely distinguishable from charcoal — applied in tight hover/focus contexts where the tiniest shift signals state change.

### Surface & Backgrounds
- **Charcoal Dark** (`#252525`): Primary dark surface — header, dark content sections, email input backgrounds.
- **Near-White** (`#fcfcfc`): Light surface variant — used for content sections and card faces on the light portions of the site.
- **Active Surface Dark** (`#282828`): Active state surface for dark-mode interactive elements — a 3-pixel lift from the default charcoal, perceptible only on direct comparison.

### Borders
- **Gold Border** (`rgb(180, 132, 30)`): Active/selected borders on buttons and link elements — the primary border accent.
- **Charcoal Border** (`rgb(37, 37, 37)`): Structural borders — dark surface dividers and bottom-edge container separators.
- **Light Divider** (`rgb(216, 216, 216)`): Subtle rule lines on white/light content sections.
- **Input Border** (`rgb(74, 74, 74)`): Email input default border — a mid-dark gray that lifts the input field from the charcoal surface.
- **Muted Border** (`rgb(209, 209, 209)`): Light-mode input and form field borders.
- **Toggle Blue** (`rgb(56, 96, 190)`): Toggle switch border in the cookie consent component — one of the system's few blue-family appearances.
- **Success Teal** (`rgb(50, 174, 136)`): Success state border — confirmations and positive validation feedback.

### Shadows
- **Modal Shadow** (`rgba(0, 0, 0, 0.18) 0px 16px 32px -8px, rgba(0, 0, 0, 0.08) 0px 0px 48px -8px`): Applied to floating panels and dropdowns — a two-layer shadow with a directional near component and a wide ambient halo.
- **Ambient Shadow** (`rgba(0, 0, 0, 0.2) 0px 0px 18px 0px`): Uniform ambient glow for overlapping UI elements.
- **Cookie Shadow** (`rgb(153, 153, 153) 0px 2px 10px -3px`): Consent dialog lift — a warm gray directional shadow.
- **Glow Warm** (`rgb(199, 197, 199) 0px 0px 12px 2px`): Soft focus glow for accessibility and active states.

## 3. Typography Rules

### Font Family
- **Display Serif**: `MercuryDisplayRegular`, with fallback: `Georgia`, `serif`
- **Text Serif**: `MercuryTextG1Regular` and `MercuryTextG1Italic`, with fallback: `Georgia`, `serif`
- **UI Sans (Narrow)**: `GothamNarrowBold`, `GothamNarrowMedium`, with fallback: `arial`, `sans-serif`
- **UI Sans (Book)**: `GothamBook`, with fallback: `arial`, `sans-serif`
- **System Fallback**: `Arial` — used for cookie consent dialogs and third-party form elements
- **OpenType Features**: `"kern"`, `"liga"` active on all Mercury variants — professional newspaper-grade defaults

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | MercuryDisplayRegular | 96px (6.00rem) | 400 | 1.05 | -0.6px | Maximum size — film title moments, full-bleed hero statements |
| Editorial Heading | MercuryTextG1Regular | 24px (1.50rem) | 400 | 1.30 | -0.3px | Section titles, card headings on editorial content |
| Body Serif Link | MercuryTextG1Regular | 24px (1.50rem) | 400 | 1.50 | -0.3px | In-text links within Mercury body passages |
| Italic Link | MercuryTextG1Italic | 24px (1.50rem) | 400 | 1.50 | -0.3px | Italic variant for titles and cited works in links |
| Sub-heading | MercuryTextG1Regular | 20px (1.25rem) | 400 | 1.60 | -0.3px | Sub-section markers and secondary editorial heads |
| Body Reading | MercuryTextG1Regular | 18px (1.13rem) | 400 | 1.20 | normal | Primary content body — essays, liner notes, film descriptions |
| Body Standard | MercuryTextG1Regular | 16px (1.00rem) | 400 | 1.60 | normal | UI body text, card descriptions, secondary reading |
| Body Bold | MercuryTextG1Regular | 16px (1.00rem) | 700 | 1.30 | normal | Emphasized inline body — director names, emphasized credits |
| Caption Italic | MercuryTextG1Italic | 14px (0.88rem) | 400 | 1.43 | -0.1px | Image captions, attributed quotes, italic annotations |
| Caption Regular | MercuryTextG1Regular | 14px (0.88rem) | 400 | 1.60 | normal | Standard metadata captions |
| Sub-caption | MercuryTextG1Regular | 13px (0.81rem) | 400 | 1.50 | normal | Fine-print metadata, timestamps, secondary labels |
| Micro Serif | MercuryTextG1Regular | 12px (0.75rem) | 400 | — | normal | Smallest serif text — footnotes, legal copy |
| Nav / UI Label | GothamNarrowBold | 13px (0.81rem) | 400 | 1.15 | 1px | Uppercase — primary navigation links, section headers |
| Button Label | GothamNarrowBold | 13px (0.81rem) | 400 | 1.23–1.25 | 0.6–1px | Uppercase — button text, CTA labels |
| Filter Tag | GothamNarrowMedium | 13px (0.81rem) | 600–700 | 1.00–1.40 | 0.65–1.04px | Uppercase — filter chips, category tags, pill buttons |
| Caption Upper | GothamNarrowBold | 12px (0.75rem) | 400 | 1.23 | 0.6px | Uppercase — small structural labels, image metadata |
| UI Small | GothamBook | 12px (0.75rem) | 400 | 1.40 | -0.2px | Lowercase — compact card metadata, supplementary information |
| Button Compact | MercuryTextG1Regular | 14.4px (0.90rem) | 400 | 2.64 | 0.144px | Generous line-height buttons — inline text CTAs |
| Button Heavy | MercuryTextG1Regular | 14.4px (0.90rem) | 700 | 1.00 | normal | Heavy compact action triggers |

### Principles
- **Two-register discipline**: Mercury handles all content voice — essays, film titles, descriptions. Gotham Narrow handles all structural annotation — navigation, buttons, filters, labels. These registers never blur.
- **Uppercase as institutional signal**: Every Gotham Narrow usage is uppercase with expanded letter-spacing (`0.6px–1px`). This creates a visual language that reads as "official classification" — the stamp on a library card rather than a headline competing for attention.
- **Negative tracking for Mercury at size**: All Mercury text at 20px+ carries negative letter-spacing (`-0.3px` at 24px, `-0.6px` at 96px) — standard newspaper-quality optical compensation that prevents the letterforms from opening up awkwardly at display sizes.
- **Italic as curatorial voice**: MercuryTextG1Italic appears in captions and attributed quotes — a typographic convention from print book design where the editor's voice is in italics, the filmmaker's title is in roman.
- **kern + liga everywhere**: The OpenType features `"kern"` (kerning) and `"liga"` (ligatures) are active across all Mercury contexts — a professional discipline that signals the brand's relationship with typographic craft.

## 4. Component Stylings

### Buttons

**Primary Gold (CTA)**
- Background: Criterion Gold (`#b4841e`)
- Text: Pure White (`#ffffff`)
- Padding: `12px 10px`
- Radius: `2px`
- Border: `1px solid #b4841e`
- Box Shadow: `none`
- Font: GothamNarrowBold 13px, uppercase, letter-spacing `0.6–1px`
- Hover: background `rgb(30, 174, 219)`, border `1px solid #252525`, text `#ffffff`, opacity `0.7`, transform `scale(1.03)`
- Active: background `rgb(231, 231, 231)`, opacity `0.6`, transform `scale(1)`
- Focus: background `rgb(30, 174, 219)`, outline `rgb(0, 0, 0) solid 2px`, box-shadow `rgb(0, 153, 255) 0px 0px 0px 5px`, opacity `0.7`
- Use: "WATCH NOW ON THE CHANNEL", "ADD TO CART", primary film CTAs

**Secondary White (UI Action)**
- Background: Pure White (`#ffffff`)
- Text: Criterion Charcoal (`#252525`)
- Padding: `20px`
- Radius: `0px`
- Border: `0px none #252525` (default — no border)
- Box Shadow: `none`
- Font: GothamNarrowBold 13px, uppercase
- Hover: background `rgb(30, 174, 219)`, text `#ffffff`, border `1px solid #252525`, opacity `0.7`, transform `scale(1.03)`
- Active: background `rgb(231, 231, 231)`, opacity `0.6`
- Use: Secondary actions on dark surfaces, filter toggle labels

**Ghost / Outline**
- Background: transparent
- Text: Pure White (`#ffffff`) on dark or Charcoal (`#252525`) on light
- Border: `1px solid #b4841e` (gold-bordered outline variant)
- Radius: `2px`
- Font: GothamNarrowBold 13px, uppercase, letter-spacing `1px`
- Hover: gold fill transitions to teal hover state

**Cookie Consent Button**
- Background: Criterion Gold (`#b4841e`) for "GOT IT!"
- Text: `#ffffff`
- Font: GothamNarrowBold or MercuryTextG1Regular 13–14px
- Radius: `2px`
- Use: Cookie consent acceptance — matches primary button treatment

### Cards

**Film Cover Card**
- Background: `#252525` (dark slate) or transparent over dark canvas
- Border: none in default — the cover art carries all the visual weight
- Radius: `0px` — square edges maintain the archival, printed-object quality
- Shadow: none on the card itself; hover reveals `rgba(0,0,0,0.18) 0px 16px 32px -8px, rgba(0,0,0,0.08) 0px 0px 48px -8px`
- Text: film title in MercuryTextG1Regular, director in GothamNarrowBold uppercase
- Interaction: hover scales the cover image slightly, triggers shadow elevation

**Editorial Card (Essay / Article)**
- Background: `#fcfcfc` (near-white) on light sections
- Border: `1px solid rgb(216, 216, 216)` (top rule) for section delineation
- Radius: `0px`
- Text: headline in MercuryTextG1Regular, byline in GothamNarrowBold uppercase
- Padding: `20–24px` internal

### Inputs

**Email Input (Newsletter)**
- Background: Criterion Charcoal (`#252525`)
- Text: Pure White (`#ffffff`)
- Border: `2px solid rgb(74, 74, 74)`
- Radius: `0px`
- Padding: `18px`
- Font: MercuryTextG1Regular 16px
- Placeholder: Silver Mid (`#8e8e8e`)
- Focus: border `1px solid #000000`, background `rgb(30, 174, 219)`, box-shadow `rgb(33, 150, 243) 0px 0px 1px`

**Search / Filter Input**
- Background: `#252525`
- Radius: `50px` (pill on search input) or `0px` (filter fields)
- Border: `1px solid rgb(209, 209, 209)` on light surfaces
- Font: MercuryTextG1Regular 14–16px

**Toggle Switch**
- Radius: `20px` (pill)
- Border: `1px solid rgb(56, 96, 190)`
- Use: Cookie preference toggles

### Navigation

- Container: Criterion Charcoal (`#252525`) header background, full-width
- Logo: "C" mark SVG in Criterion Gold (`#b4841e`), top-left, ~70px tall
- Primary Links: GothamNarrowBold, 13px, uppercase, letter-spacing `1px`, Pure White (`#ffffff`) text
- "Current" dropdown: inline with chevron indicator
- Utility icons: search, cart, account — white icon fills, right-aligned
- Hamburger menu: grid icon, far right
- Link hover: color shifts to Criterion Teal (`rgb(30, 174, 219)`)
- Vertical rotated text: "THE CRITERION COLLECTION" runs up the left margin of the hero in GothamNarrowBold uppercase, white, 90° rotation — a signature editorial device borrowed from magazine spines

### Links

**Gold Underlined Link (Editorial Body)**
- Default: color `#b4841e`, text-decoration `underline`
- Hover: color `rgb(56, 96, 190)`, text-decoration `none`
- Font: MercuryTextG1Regular, inherits body size

**White Nav Link**
- Default: color `#ffffff`, text-decoration `none`
- Hover: color `rgb(56, 96, 190)`, text-decoration `none`
- Font: GothamNarrowBold, 13px, uppercase

**Charcoal Body Link (Light Sections)**
- Default: color `#252525`, text-decoration `none`
- Hover: color `rgb(56, 96, 190)`, text-decoration `none`

**Muted Gray Link**
- Default: color `#8e8e8e`, text-decoration `none`
- Hover: color `rgb(56, 96, 190)`, text-decoration `none`
- Use: Footer secondary links, metadata references

### Filter Tags / Badges

**Criterion has no explicit badge system** — instead, filter tags use:
- Font: GothamNarrowMedium or GothamNarrowBold, 13px, uppercase, letter-spacing `1px`
- Background: `#252525` (dark) or `#ffffff` (light context)
- Border: `1px solid #b4841e` on active/selected states
- Radius: `17px` (pill) for filter chips, `2px` for structural labels
- Color: White text on dark, charcoal on light

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Dense scale: `1px, 5px, 6px, 8px, 10px, 12px, 15px, 16px, 18px, 20px, 24px, 25px, 32px, 40px, 48px`
- Section scale: `120px` — the dominant section-break value, appearing 8 times (generous editorial breathing room between major content blocks)
- Notable: `153.594px` appears for a specific large spacing context — likely a hero-section top padding derived from the navigation height plus breathing margin
- Button padding: `12px 10px` (primary gold) or `20px` (secondary white, uniform all-sides)
- The system uses both a dense sub-scale (5–20px for UI components) and a generous macro-scale (40–120px for section rhythm)

### Grid & Container
- Max content width: approximately 1280px centered, with full-bleed breakouts for hero imagery
- Hero: 100vw × 100vh full-viewport film stills, text overlaid without scrims
- Film grid: multi-column cover grid (5–6 columns at desktop) — the primary browsing surface, analogous to a record shop's organized shelves
- Editorial sections: single-column centered or 2-column image+text at desktop
- Footer: multi-column link organization on dark charcoal surface

### Whitespace Philosophy
- **Section breathing**: The `120px` spacing value between major sections creates the pace of a physical publication — you turn the page, there is margin, then content begins. Nothing runs into anything else.
- **Cover grid density**: The film cover grid is deliberately dense — covers tile edge-to-edge with minimal gap. This is intentional archival density, like a wall of physical DVDs; the grid's compression signals breadth of collection.
- **Hero negative space**: Full-viewport heroes use the image itself as the spatial element. Text sits sparsely within the frame — a review quote, a film title, a CTA — everything else is image.

### Border Radius Scale
- `0px`: Default for all rectangular surfaces — buttons (primary), cards, containers, hero overlays, editorial sections. The sharp corner is the system's structural identity.
- `1px`: Rare softening on inline span elements
- `2px`: Default for interactive buttons and close/back controls — barely perceptible rounding, present mostly for antialiasing
- `3px`: Occasional container softening (low confidence)
- `8px`: Floating panels, modals, dropdown containers
- `17px`: Filter pill chips
- `20px`: Toggle switch pills
- `50px`: Search input pill

## 6. Depth & Elevation

| Level | Box Shadow Value | Use Case |
|-------|-----------------|----------|
| Flat (Level 0) | `none` | Page surfaces, content cards, film grid |
| Ambient Hover (Level 1) | `rgba(0,0,0,0.2) 0px 0px 18px 0px` | Hovered interactive elements, light overlap |
| Card Elevated (Level 2) | `rgba(0,0,0,0.18) 0px 16px 32px -8px, rgba(0,0,0,0.08) 0px 0px 48px -8px` | Floating panels, hovered film cards, dropdown menus |
| Cookie / Dialog (Level 3) | `rgb(153, 153, 153) 0px 2px 10px -3px` | Cookie consent drawer, small utility overlays |
| Focus Glow (Level 4) | `rgb(0, 153, 255) 0px 0px 0px 5px` | Keyboard focus rings on interactive elements |
| Warm Glow (Level 5) | `rgb(199, 197, 199) 0px 0px 12px 2px` | Specialty focus states on light surfaces |

**Shadow Philosophy**: Criterion's shadow system is functional rather than expressive. The vast majority of the interface is flat — the darkness of the canvas provides all the necessary depth, and film imagery provides its own atmospheric dimensionality. Shadows appear only at the boundaries of interface layers: hovering a film card, opening a dropdown, displaying a cookie consent drawer. The two-layer card shadow (`rgba(0,0,0,0.18)` directional + `rgba(0,0,0,0.08)` ambient) follows a pattern structurally similar to Stripe's blue-tinted approach but executed in pure neutral black — there is no brand-color tinting in Criterion's shadows. Depth is architectural, not atmospheric.

## 7. Do's and Don'ts

**Do**
- Use Criterion Gold (`#b4841e`) exclusively — one accent color, applied to buttons, logo, link underlines, and active borders. Its power is its scarcity.
- Set all Gotham Narrow text in uppercase with `letter-spacing: 1px` — this is the structural annotation language; mixed case breaks the institutional voice.
- Apply `0px` border-radius to all rectangular UI surfaces — the square corner is non-negotiable to the archival aesthetic.
- Use Mercury with `font-feature-settings: "kern", "liga"` on all instances — professional typesetting is expected, not optional.
- Deploy Mercury Italic specifically for captions and attributed film quotes — the italic register carries editorial meaning.
- Use `120px` vertical section spacing for major content breaks — the generous breathing room creates the publication-page rhythm.
- Keep the film cover grid dense — edge-to-edge covers with minimal gap signal archival breadth.
- Maintain the two-register discipline: Mercury for content, Gotham Narrow for structural UI — never set navigation in Mercury or body text in Gotham.

**Don't**
- Don't introduce the teal hover color (`rgb(30, 174, 219)`) into default states — it belongs exclusively to hover and focus transitions.
- Don't use positive letter-spacing on Mercury headings — they require negative tracking (`-0.3px` to `-0.6px`) at 20px+.
- Don't set Gotham Narrow in mixed case for UI labels — lowercase Gotham reads as casual, undercutting the institutional register.
- Don't add gradients or scrim overlays to the film-still hero — the image stands alone on its own authority.
- Don't use border-radius values in the 4–16px range — the system is binary: near-sharp (`0–2px`) or functional-pill (`17px+`). Mid-range rounding has no place here.
- Don't use GothamBook in uppercase — it lacks the weight to carry the institutional stamp; use GothamNarrowBold or GothamNarrowMedium for uppercase contexts.
- Don't apply the modal/card shadow (`rgba(0,0,0,0.18) 0px 16px 32px -8px`) to static content — shadows in this system are reserved for interactive elevation moments.
- Don't dilute the palette with additional chromatic colors — the gold accent functions because it is singular.

## 8. Responsive Behavior

### Breakpoints
Criterion's breakpoint list is exceptionally dense — 40+ values from 0px to 1921px. Key layout-changing thresholds:

| Name | Width | Key Changes |
|------|-------|-------------|
| Micro Mobile | <320px | Minimal layout, reduced hero type, stacked navigation |
| Small Mobile | 320–425px | Single column, compressed hero typography |
| Mobile | 426–576px | Standard mobile layout, hamburger nav |
| Large Mobile | 577–650px | Slightly expanded gutters |
| Tablet Small | 651–768px | Two-column grids begin, condensed nav |
| Tablet | 769–960px | Full tablet layout, cover grid at 3–4 columns |
| Desktop Small | 961–1135px | Full nav, cover grid at 5 columns |
| Desktop | 1136–1280px | Maximum desktop layout, 6-column cover grid |
| Large Desktop | 1281–1536px | Expanded margins, full editorial width |
| Cinema | 1537–1921px+ | Ultra-wide with hero imagery at maximum scale |

### Touch Targets
- Primary CTA buttons: `12px 10px` padding — meets minimum touch height with mercury label
- Navigation links: GothamNarrowBold 13px with adequate surrounding tap area
- Film cover cards: large tap targets inherently (the cover art IS the touch target)
- Icon buttons (search, cart, account): minimum 44×44px tap area
- Filter pills: `17px` radius with adequate padding for touch accuracy

### Collapsing Strategy
- **Navigation**: Full horizontal nav with "Shop / Current / Channel" collapses to hamburger menu; logo and utility icons persist
- **Hero typography**: Mercury Display 96px hero reduces to approximately 48–60px on tablet and 36–40px on mobile — tight line-height maintained across breakpoints
- **Cover grid**: 6-column → 4-column → 3-column → 2-column across desktop → tablet → mobile
- **Editorial sections**: 2-column image+text → stacked single-column on mobile
- **Section spacing**: 120px → 60–80px on tablet → 40px on mobile — maintains proportional breathing room
- **Vertical text spine**: "THE CRITERION COLLECTION" rotated text may hide on mobile viewports where the hero height is insufficient

### Image Behavior
- Hero film stills maintain full-bleed edge-to-edge at all breakpoints
- Cover art maintains aspect ratio within grid columns; `object-fit: cover` handles crops
- No art direction swaps — the same cinematic images serve all viewports
- Lazy loading below the fold for the cover grid (high image count demands progressive loading)

## 9. Agent Prompt Guide

### Quick Reference
- Primary CTA Background: Criterion Gold (`#b4841e`)
- Primary CTA Text: Pure White (`#ffffff`)
- Page Background (Dark): Criterion Charcoal (`#252525`)
- Page Background (Light): Near-White (`#fcfcfc`)
- Primary Text (Dark Surface): Pure White (`#ffffff`)
- Primary Text (Light Surface): Criterion Charcoal (`#252525`)
- Secondary / Muted Text: Silver Mid (`#8e8e8e`)
- Link Default: Criterion Gold (`#b4841e`) with underline
- Link Hover: Link Blue (`rgb(56, 96, 190)`)
- Hover Transition Color: Criterion Teal (`rgb(30, 174, 219)`) at `opacity: 0.7`
- Active Border / Focus Gold: `1px solid #b4841e`
- Focus Ring: `rgb(0, 153, 255) 0px 0px 0px 5px`

### Example Component Prompts

- "Create a full-viewport hero section on Criterion Charcoal (`#252525`) with a full-bleed cinematic film still as the background image — no gradient scrim, no overlay. Center a film title in MercuryDisplayRegular 96px, weight 400, line-height 1.05, letter-spacing -0.6px, Pure White (`#ffffff`), font-feature-settings 'kern' 'liga'. Below it, place a review quote in MercuryTextG1Italic 20px, weight 400, line-height 1.60, letter-spacing -0.3px, white. Add a CTA button labeled 'WATCH NOW ON THE CHANNEL' — GothamNarrowBold 13px uppercase, letter-spacing 1px, background `#b4841e`, white text, `2px` border-radius, `1px solid #b4841e` border, padding `12px 10px`. On the left vertical margin, rotate 'THE CRITERION COLLECTION' 90° counterclockwise in GothamNarrowBold 11px uppercase, white, letter-spacing 1px."

- "Design a film cover grid on a `#252525` background: 6 columns at desktop, each cell containing a film cover image (aspect ratio 2:3) at `0px` border-radius with no gap or minimal 1px gap between cells. Below each cover, show the film title in MercuryTextG1Regular 14px, weight 400, line-height 1.60, white, and a director credit in GothamNarrowBold 12px uppercase, letter-spacing 0.6px, Silver Mid (`#8e8e8e`). Hover state: card shadow `rgba(0,0,0,0.18) 0px 16px 32px -8px, rgba(0,0,0,0.08) 0px 0px 48px -8px`, image scales slightly."

- "Build an editorial article card on Near-White (`#fcfcfc`) with a `1px solid rgb(216, 216, 216)` top border, `0px` radius, `24px` internal padding. Section label in GothamNarrowBold 12px uppercase, letter-spacing 0.6px, Silver Mid (`#8e8e8e`). Headline in MercuryTextG1Regular 24px, weight 400, line-height 1.30, letter-spacing -0.3px, Criterion Charcoal (`#252525`), font-feature-settings 'kern' 'liga'. Byline in MercuryTextG1Italic 14px, weight 400, line-height 1.43, letter-spacing -0.1px. Gold link at bottom: `#b4841e`, underlined, MercuryTextG1Regular 16px — hover shifts to `rgb(56, 96, 190)`, underline removed."

- "Create a newsletter email input on a `#252525` dark surface: background `#252525`, white text, `2px solid rgb(74, 74, 74)` border, `0px` border-radius, `18px` padding, MercuryTextG1Regular 16px. Placeholder text in Silver Mid (`#8e8e8e`). Adjacent submit button in Criterion Gold (`#b4841e`), white GothamNarrowBold 13px uppercase, `1px letter-spacing`, `2px` border-radius, `12px 10px` padding. Focus state for input: border `1px solid #000000`, background transitions to `rgb(30, 174, 219)`, box-shadow `rgb(33, 150, 243) 0px 0px 1px`."

- "Design a navigation header on `#252525`: left-aligned Criterion 'C' logo mark in SVG at approximately 40px tall in gold (`#b4841e`). Center or right group: 'Shop the Collection', 'Current ▾', 'The Criterion Channel' in GothamNarrowBold 13px uppercase, letter-spacing 1px, line-height 1.15, white. Far right: search icon, cart icon, user icon, hamburger menu icon — all white, 24px. Hover on any link transitions color to `rgb(30, 174, 219)`."

### Iteration Guide

1. **Two-register rule, always**: If text is navigation, button, filter, label, or UI chrome → GothamNarrowBold/Medium, uppercase, `0.6–1px` letter-spacing. If text is content, essay, film title, description, caption → Mercury family, mixed case.
2. **Gold appears once per component**: Apply `#b4841e` to the primary action only — button, link underline, or active border. Never use it decoratively or repeatedly in a single component.
3. **Sharp corners are the law**: `0px` border-radius on all rectangular containers and buttons. Use `2px` only when you need a technical softening for antialiasing. Never introduce `4–16px` radius.
4. **Teal is only for hover**: `rgb(30, 174, 219)` at `opacity: 0.7` belongs exclusively to hover and focus states — never set it as a default background or static color.
5. **120px is the section gap**: Between major content sections, use the `120px` vertical spacing. Reserve smaller values (40–48px) for intra-section spacing between related elements.
6. **Mercury needs negative tracking at size**: At 20px+, always apply negative letter-spacing (`-0.3px` at 20–24px, `-0.6px` at 96px). Body sizes (16–18px) and below track at normal.
7. **Font features are required**: Every Mercury text instance needs `font-feature-settings: "kern", "liga"` — these are professional typesetting standards, not optional decoration.
8. **Hover surprise is part of the system**: The unexpected teal hover transition on buttons and links is canonical, not a bug. It creates the system's single moment of unexpected warmth.