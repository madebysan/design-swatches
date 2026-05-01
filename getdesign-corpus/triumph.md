---
slug: triumph
name: Triumph Motorcycles
url: https://www.triumphmotorcycles.com
domain: triumphmotorcycles.com
category: Auto
styles: [Dark, Bold, Editorial]
tagline: "Gunmetal black canvas, uppercase DIN, and a single crimson accent that signals speed without apology"
fonts: [DIN2014-Demi, DIN2014-Regular, triumph]
primary_color: "#cd192d"
---

# Design System Inspired by Triumph Motorcycles

> Gunmetal black canvas, uppercase DIN, and a single crimson accent that signals speed without apology

## 1. Visual Theme & Atmosphere

Triumph Motorcycles' website is a cinematic broadsheet for machines — a system where the design decisions feel less like UI choices and more like engineering tolerances. The page opens on a full-bleed, motion-blurred track photograph with the "NEW DAYTONA 660" headline punched across the lower-left in uppercase DIN2014-Demi at display scale: white letterforms sitting on darkened asphalt, letterforms wide and mechanical, carrying the authority of a spec sheet rather than a marketing slogan. The overall impression is of a brand that has been making motorcycles since 1902 and has no interest in appearing contemporary — only in appearing correct.

The typeface is the primary design material. DIN2014-Demi and DIN2014-Regular are the typographic backbone: geometric, German-engineered grotesks with consistently wide letter-spacing (1px on display headings, 0.5px on secondary text) and uniform uppercase transforms on every headline and UI label. This isn't uppercase-as-trend; it's uppercase as mechanical notation, the way torque specs and gear ratios are written. Paired with the bespoke "triumph" logotype face used for brand moments and the Triumph eagle wordmark, the font system creates a single register — the register of precision instruments. Nothing is decorative. Weight 400 in DIN2014-Demi reads like bold in most systems because the typeface's Demi cut is already structurally heavy.

What gives Triumph its specific character is the chromatic restraint applied to a brand that could easily indulge in excess. The palette is gunmetal: pure black (`#000000`) as the dominant surface, charcoal (`#333333`) for dark panels and mid-tones, oil-grey (`#63656a`) for secondary text and structural chrome, and Triumph Crimson (`#cd192d`) as the sole chromatic accent — applied to primary CTAs, border accents, and interactive highlights. The crimson is not the softened luxury-red of Ferrari; it's a harder, more working-class red that evokes painted tank badges rather than paddock glamour. The hover interaction — an inset white fill sweeping across buttons with `rgb(255,255,255) 0px 0px 0px 30px inset` — is the most kinetic moment in an otherwise composed system, a flash of inverted light that mirrors a motorcycle headlamp cutting through dark.

**Key Characteristics:**
- DIN2014-Demi as the primary display voice — mechanically wide, Germanic, never romantic
- Uppercase transforms on all headings and most UI labels — notation logic, not typographic flourish
- 1px letter-spacing on display headings creating the signature wide-tracked, engineered rhythm
- Pure black (`#000000`) as the dominant canvas with charcoal (`#333333`) for layered dark surfaces
- Triumph Crimson (`#cd192d`) as the single chromatic accent — one red, used with precision
- `0px` border-radius on all primary interactive elements — sharp-cornered engineering aesthetic
- Full-bleed cinematic motorcycle photography as the primary visual medium
- Inset-sweep hover animation on CTAs (`rgb(255,255,255) 0px 0px 0px 30px inset`) — the kinetic signature
- 2px solid borders on buttons — heavier than typical, reinforcing mechanical materiality
- Minimal shadow system — depth through surface color contrast, not atmospheric lift

## 2. Color Palette & Roles

### Primary Brand
- **Triumph Black** (`#000000`): The dominant surface color — hero section backgrounds, primary button fill, dark panel backgrounds, the logo backdrop. Used without softening, pure and industrial.

### Brand Accent
- **Triumph Crimson** (`#cd192d`): The sole chromatic accent — primary CTA button fill, 2px border accents on key buttons, inline link color in body content. The tank-badge red that anchors every Triumph motorcycle. Border variant at same hue: `2px solid rgb(205, 25, 45)`.

### Secondary Accent
- **Deep Crimson** (`#a11d2c`): Hover/active link state — a slightly darker shift from the Triumph Crimson, used when link text transitions in dark contexts (hover color `rgb(161, 29, 44)`).
- **Error Crimson** (`#c40303`): Cookie policy inline link color — a warmer, more urgent red used for legal-critical links.

### Text Scale
- **Primary White** (`#ffffff`): All primary text on dark surfaces, button labels on black and crimson backgrounds, navigation links, headline overlays on photography.
- **Charcoal Body** (`#333333`): Primary text on light surfaces — card body copy, product descriptions, light-section paragraphs.
- **Oil Grey** (`#63656a`): Secondary text — footer meta, captions, secondary nav items, subdued labels. A cool mid-grey with a barely perceptible blue undertone.
- **Dark Ink** (`#2a2a2a`): Section block backgrounds and mid-dark containers — slightly lifted from pure black, creating a subtle layer distinction.

### Surface & Panels
- **Charcoal Panel** (`#333333`): Section dividers, inline dark panels, CTA section backgrounds where full black would flatten.
- **Dark Steel** (`#505050`): Hairline top-border on section dividers (`1px solid rgb(80, 80, 80)`) — a structural line at the threshold between sections.
- **Mid Steel** (`#63656a`): Footer top-border (`1px solid rgb(99, 101, 106)`) and secondary structural lines.

### Borders
- **Black Border** (`#000000`): Primary 2px solid border on black CTAs — the frame that defines button physicality.
- **Crimson Border** (`#cd192d`): 2px solid border on primary crimson CTAs — border and fill share the hue, creating a unified stamped appearance.
- **Silver Rule** (`#dddddd`): Span-level 1px solid hairlines for fine UI separation.
- **Light Rule** (`#d1d1d1`): Alternate light separator for container-level divisions.
- **Input Border** (`#d1d1d1`): 1px solid border on form inputs.

### Interactive States
- **Hover Sweep White** (`rgb(255, 255, 255) 0px 0px 0px 30px inset`): The signature button hover — a full-width inset box-shadow that visually "fills" the button with white light from the inside, inverting the dark button.
- **Focus Blue** (`rgb(30, 174, 219)`): Button focus and interactive focus-state background — the one moment of cool chromatic color in an otherwise warm-and-neutral system. Carries no brand weight; exists purely for accessibility signalling.
- **Link Hover Blue** (`#3860be`): All link hover states regardless of default color — white links, red links, black links all converge to this dignified navy on hover.
- **Focus Yellow** (`rgb(240, 255, 0)`): Section block focus state — a high-visibility lemon yellow used on keyboard-accessible section containers for WCAG compliance.

### Semantic
- **Success Green** (`rgb(50, 174, 136)`): Confirmation borders on forms — appears only in validation contexts.
- **Active Green** (`rgb(44, 100, 21)`): Active/pressed button background — a muted forest green for the pressed state, signalling confirmed interaction.

## 3. Typography Rules

### Font Family
- **Display / Headings**: `DIN2014-Demi`, with fallback: `Arial`, `Helvetica`, `sans-serif`
- **Body / Secondary**: `DIN2014-Regular`, with fallback: `Arial`, `Helvetica`, `sans-serif`
- **Brand / Logo**: `triumph` (proprietary logotype font), with fallback: `Arial`
- **OpenType Features**: None explicitly declared — DIN's inherent geometric character carries the brand voice. No stylistic sets or alternate glyphs.

*Note: DIN2014 is a commercial revival of DIN 1451 by Linotype. For external implementations, Neue Haas Grotesk, Aktiv Grotesk, or FF DIN serve as close substitutes. Inter at weight 500 is the web-safe fallback.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Display Hero | DIN2014-Demi | 80px (5.00rem) | 400 | 1.00 | 1px | uppercase | Maximum impact — hero section model names |
| Display Large | DIN2014-Demi | 50px (3.13rem) | 400 | 1.20 | 1px | uppercase | Secondary hero, section title callouts |
| Display Mid | DIN2014-Demi | 40px (2.50rem) | 400 | 2.75 | 1px | uppercase | Category headers with generous line-height for spacer effect |
| Section Heading | DIN2014-Demi | 35px (2.19rem) | 400 | 1.20 | 1px | uppercase | Feature section anchors |
| Section Heading (Sentence) | DIN2014-Demi | 35px (2.19rem) | 400 | 1.20 | 1px | none | Descriptive sub-section heads without uppercase |
| Sub-heading Large | DIN2014-Demi | 32px (2.00rem) | 400 | — | 1px | uppercase | Card and panel titles |
| Sub-heading Regular | DIN2014-Regular | 30px (1.88rem) | 400 | 1.17 | 0.5px | none | Editorial body headings in regular weight |
| Sub-heading Capitalize | DIN2014-Regular | 30px (1.88rem) | 400 | 1.27 | 1px | capitalize | Title-case heading variant |
| Feature Title | DIN2014-Regular | 24px (1.50rem) | 400 | — | — | none | Smaller feature and card titles |
| Body Heading | DIN2014-Regular | 18px (1.13rem) | 400 | 1.39 | 0.5px | none | Section subtitle, inline headings |
| Nav Link / Label | DIN2014-Demi | 17px (1.06rem) | 400 | 2.12 | 0.5px | uppercase | Navigation links, uppercase label links |
| UI Label Demi | DIN2014-Demi | 17px (1.06rem) | 400 | 1.47 | 0.5px | uppercase | UI section labels in demi weight |
| Button Primary | DIN2014-Demi | 17px (1.06rem) | 400 | 2.82 | 0.17px | none | Main CTA button text |
| Body / UI | DIN2014-Regular | 16px (1.00rem) | 400 | 0.94 | — | none | Standard body, link text |
| Body Bold | DIN2014-Regular | 16px (1.00rem) | 700 | 1.50 | — | none | Emphasized inline body text |
| Body Semi | DIN2014-Regular | 16px (1.00rem) | 600 | 1.50 | — | none | Semi-bold body for secondary emphasis |
| Button Compact | DIN2014-Demi | 16px (1.00rem) | 400 | 3.25 | — | uppercase | Compact CTA with tall line-height |
| Button Regular | DIN2014-Regular | 16px (1.00rem) | 400 | — | 0.16px | — | Secondary action buttons |
| Brand Caption | triumph | 16px (1.00rem) | 400 | 1.00 | — | none | Brand logotype and logo-adjacent text |
| Label Demi Upper | DIN2014-Demi | 15px (0.94rem) | 400 | 1.00 | 0.5px | uppercase | Tag labels, category markers |
| Button Small | DIN2014-Regular | 14.4px (0.90rem) | 700 | 1.00 | 0.144px | none | Small bold action buttons |
| Nav Small | DIN2014-Regular | 14px (0.88rem) | 400 | 1.07 | — | none | Secondary nav, footer links |
| Caption Upper | DIN2014-Regular | 14px (0.88rem) | 400 | — | — | uppercase | Image captions, label text |
| Caption Bold | DIN2014-Regular | 14px (0.88rem) | 700 | 1.50 | — | none | Emphasized captions |
| Utility / Footer | DIN2014-Regular | 13px (0.81rem) | 400 | 1.69 | 0.5px | none | Footer body, small paragraphs |
| Micro Button | DIN2014-Regular | 12px (0.75rem) | 700 | 1.00 | 0.96px | none | Smallest CTA with wide tracking |
| Brand Micro | triumph | 13px (0.81rem) | 400 | 1.00 | — | none | Logo micro-application |

### Principles
- **Uppercase as engineering notation**: DIN2014-Demi headings run uppercase universally at display sizes — this isn't decorative; it's the same convention used for model codes, spec sheets, and motorcycle chassis identifiers.
- **Wide tracking at display scale**: 1px letter-spacing on 35–80px headlines creates the visual "spread" of engraved signage. The wider the text, the wider the tracking — this is opposite to the negative-tracking convention of fashion brands, and it suits DIN's industrial geometry.
- **Two weights, clear division**: DIN2014-Demi for all headlines, CTAs, and UI labels; DIN2014-Regular for body text, captions, and secondary information. The line between these registers is absolute — Demi is for structure, Regular is for information.
- **Tall line-heights on buttons**: Primary button text runs at line-heights of 2.82–3.25 — creating oversized tap targets through line-height rather than padding, a pattern common in automotive site design.
- **DIN's weight 400 is not light**: In DIN2014-Demi, `font-weight: 400` is actually the Demi (semi-bold equivalent) cut. The numeric weight refers to the CSS registration, not visual weight. Always specify the full font-family name to trigger the correct cut.

## 4. Component Stylings

### Buttons

**Primary Crimson (CTA — "VIEW BIKE")**
- Background: `#cd192d`
- Text: `#ffffff`
- Padding: `0px 20px`
- Height: set via line-height `2.82–3.25` on 16–17px text (approximately 48–52px tall)
- Radius: `0px` (sharp rectangular)
- Border: `2px solid rgb(205, 25, 45)`
- Box Shadow: `none` (default)
- Font: 16–17px DIN2014-Demi weight 400, letter-spacing 0.17px
- Hover: background `#ffffff`, color `rgb(34, 133, 247)`, border `2px solid #000000`, box-shadow `rgb(255, 255, 255) 0px 0px 0px 30px inset`, opacity `0.6`, transform `translateX(5px)`
- Focus: background `rgb(30, 174, 219)`, outline `rgb(0, 0, 0) solid 1px`, border `1px solid #000`, transform `scale(1.1)`, opacity `0.9`
- Use: Primary model CTAs, hero carousel "VIEW BIKE" buttons

**Primary Black (Secondary CTA — "CONFIGURE")**
- Background: `#000000`
- Text: `#ffffff`
- Padding: `0px 20px`
- Radius: `0px`
- Border: `2px solid rgb(0, 0, 0)`
- Box Shadow: `none`
- Font: 16–17px DIN2014-Demi weight 400
- Hover: background `#ffffff`, color `rgb(34, 133, 247)`, border `2px solid #000`, box-shadow `rgb(255, 255, 255) 0px 0px 0px 30px inset`, transform `translateX(5px)`, opacity `0.6`
- Focus: background `rgb(30, 174, 219)`, outline `1px solid #000`, transform `scale(1.1)`
- Use: Secondary configurator actions, outline-priority CTAs alongside crimson primary

**Cookie / Utility Button (White Surface)**
- Background: `#ffffff`
- Text: `rgb(42, 42, 42)`
- Padding: `12px 10px`
- Radius: `2px`
- Border: none (0px)
- Font: 13px DIN2014-Regular weight 600
- Hover: background `rgb(30, 174, 219)`, color `#ffffff`, transform `scale(1.1)`, opacity `0.9`
- Focus: background `rgb(30, 174, 219)`, outline `rgb(0, 0, 0) solid 2px`, border `1px solid #000`
- Use: Cookie consent "COOKIE PREFERENCES" button, utility dialogs

**Standard Black (Allow All)**
- Background: `#000000`
- Text: `#ffffff`
- Padding: `0px 20px`
- Radius: `2px`
- Border: `1px solid #000000`
- Font: 17px DIN2014-Demi weight 400
- Hover: background `rgb(30, 174, 219)`, color `#ffffff`, transform `scale(1.1)`
- Use: Cookie "ALLOW ALL" button, consent confirmations

**Section Block CTA (Dark Link-style)**
- Background: `rgb(42, 42, 42)`
- Text: `#ffffff`
- Padding: `0px`
- Radius: `0px`
- Border: partial — top `1px solid rgb(80, 80, 80)`
- Hover: background `#000000`, color `rgb(161, 29, 44)`
- Focus: background `rgb(240, 255, 0)` (accessibility yellow)
- Font: 16px DIN2014-Regular weight 400
- Use: Navigation section blocks, expandable CTA link-rows

### Cards & Containers
- Background: `#000000` (hero/dark sections) or `#333333` (mid-dark panels) or `#ffffff` (light editorial sections)
- Border: none by default; `0px 1px 1px solid rgb(51,51,51)` on bottom/side edges for section separation; `3px 0px 0px solid black` top-edge accent on featured containers
- Radius: `0px` for all content surfaces — no rounded edges on structural containers
- Shadow: `rgba(0, 0, 0, 0.2) 0px 0px 18px 0px` for card lift; `rgb(153, 153, 153) 0px 2px 10px -3px` for secondary elevation
- Internal padding: 20–30px standard, 40–50px for featured card areas

### Inputs & Forms
- Background: `#ffffff`
- Border: `1px solid rgb(209, 209, 209)`
- Radius: `0px` (or `2px` minimal rounding on cookie search)
- Font: 16px DIN2014-Regular weight 400
- Text color: `#333333`
- Placeholder color: `#63656a`
- Focus: standard browser outline; border transitions to validation colors

### Navigation
- Background: `#000000` — the nav bar sits on an absolute black ground, creating maximum contrast against all surface types
- Logo: Triumph wordmark SVG (`110×23px`) left-aligned, white on black
- Primary links: DIN2014-Demi uppercase — "MOTORCYCLES", "ACCESSORIES", "CLOTHING SHOP", "OWNERS", "BRAND", "RACING"
- Secondary links (right): "Dealers", "Configure", "Offers", "Test Ride" — DIN2014-Regular, smaller, no uppercase
- Icons: cart and location pin in white at far right
- Region selector: "USA" dropdown at right edge
- Link hover: color shifts to Link Hover Blue (`#3860be`) — universal across all nav contexts
- The nav sits as a thin horizontal band (approximately 44px) — height is pure function
- Sticky: fixed at top, imagery scrolls beneath

### Vertical Rotated Label
- "NEW SPEED TW..." text visible on right edge of hero — DIN2014-Demi, rotated 90° clockwise, uppercase, crimson accent
- Used as a slide-counter/title indicator at the carousel edge

### Decorative Elements
- **Full-bleed hero photography**: Cinematic track imagery, motion-blurred motorcycles, documentary-grade photography — always darkened sufficiently for white headline legibility
- **Carousel navigation**: Left/right arrow controls at lower edges, rendered as white chevrons on dark backgrounds
- **Crimson border-top accent**: `3px solid #000` top-edge or crimson variant (`3px solid #cd192d`) on featured blocks creates a racing stripe visual metaphor

## 5. Layout Principles

### Spacing System
- Base unit: 8px (with exceptions for the 10px anchor, which is the most common measured value at count 90)
- Scale: 1px, 2px, 3px, 5px, 6px, 10px, 11.2px, 12px, 15px, 16px, 18px, 20px, 21px, 25px, 30px, 40px, 50px, 75px, 90px, 325px
- Notable: 10px is the system's primary micro-spacing unit — used for gutters, padding edges, and button horizontal padding far more than the 8px baseline. 20px is the second most-used value, serving as the standard horizontal button padding and inner card spacing. The 75–90px range handles generous section breathing room. 325px is a fixed sidebar or content-column width.

### Grid & Container
- Max content width: approximately 1366px (largest breakpoint) with centered content
- Hero: full-viewport-width, full-viewport-height or near-full — the photograph IS the layout
- Product sections: 2-column (model image left, spec/CTA right) or single-column full-bleed alternating
- Navigation: full-width fixed bar, content sits below
- Carousel: full-bleed horizontal with arrow navigation at edges

### Whitespace Philosophy
- **Cinematic breathing room**: Hero sections claim the entire viewport without hesitation. Below-hero content uses generous 40–75px vertical padding per section, maintaining editorial pacing between model features.
- **Dark sections need no decoration**: A black panel with white DIN2014-Demi uppercase text requires no additional visual elements — the contrast and the letterforms do all the work. Resist filling dark sections with icons or illustrations.
- **Content density is functional**: Specification sections and configurator panels pack information tightly (10–20px spacing) because the user needs comparison data, not atmosphere. The switch from generous hero spacing to dense spec spacing is intentional and communicates context.

### Border Radius Scale
- Sharp (`0px`): Default for buttons, cards, containers, inputs, badges — the overwhelming majority of interactive elements
- Near-sharp (`2px`): Utility buttons (cookie consent, allow-all) — a barely perceptible softening for dialog-context elements
- Minimal (`2.5px`): Rare regional container elements
- Badge/pill (`9px`): Span-level notification badges and count indicators
- Large (`20px`): Span-level chip elements
- Full pill (`50px`): Cookie search input — the sole fully-rounded element in the system
- Circle (`100%`): Circular avatar/emblem spans

The system is effectively binary: sharp rectangular (0px) for structural elements, near-sharp (2px) for utility dialogs. The 50px pill and 100% circle appear only in low-stakes utility contexts.

## 6. Depth & Elevation

| Level | Box Shadow Value | Use Case |
|-------|-----------------|----------|
| Flat (Level 0) | none | Page canvas, hero sections, all primary content containers |
| Ambient (Level 1) | `rgb(153, 153, 153) 0px 2px 10px -3px` | Cards on light-section backgrounds, slight product elevation |
| Standard (Level 2) | `rgba(0, 0, 0, 0.2) 0px 0px 18px 0px` | Panels and modals on dark backgrounds, cookie consent dialog |
| Warm Glow (Level 3) | `rgb(199, 197, 199) 0px 0px 12px 2px` | Hover/focus halos on specific interactive elements |
| Reverse Glow (Level 4) | `rgb(199, 197, 199) -3px -3px 5px -2px` | Left/top-edge halos for asymmetric focus indicators |
| CTA Sweep (Interactive) | `rgb(255, 255, 255) 0px 0px 0px 30px inset` | Hover state on all primary CTAs — the white light sweep |

**Shadow Philosophy**: Triumph's depth system is almost entirely absent on content elements — the photography handles all perceived depth. Shadows appear only in two distinct contexts: ambient lift on light-section cards (`rgb(153,153,153)` at tight spread) and the kinetic CTA hover (the `30px inset white` sweep). The inset sweep is the system's signature interaction — not a traditional shadow but an animated fill that reads as light passing through the button. It's mechanical, not atmospheric: the sensation of a relay switching rather than a surface floating. Where soft drop shadows do appear, they use neutral cool-grays without brand tinting, keeping focus on the photography and typography.

## 7. Do's and Don'ts

**Do**:
- Use DIN2014-Demi with `text-transform: uppercase` and `letter-spacing: 1px` on all display headings — the combination is the brand's typographic identity
- Apply Triumph Crimson (`#cd192d`) with a matching `2px solid` border of the same hue — border and fill as one unified stamp
- Use the inset white sweep (`rgb(255,255,255) 0px 0px 0px 30px inset`) on all primary CTA hover states — it's the system's signature kinetic moment
- Let full-bleed photography carry the emotional weight of each section — white text over darkened imagery, no gradient scrims required
- Keep `border-radius: 0px` on all structural interactive elements — the sharpness is the engineering aesthetic
- Use `#000000` (pure black) for the nav background and hero sections — Triumph does not soften its blacks
- Pair the "VIEW BIKE" crimson primary with a "CONFIGURE" black secondary in the same CTA cluster — the color hierarchy makes the action hierarchy explicit
- Apply `letter-spacing: 0.5px` on 15–17px uppercase labels — tight enough to read as machine-printed, wide enough to distinguish from body text

**Don't**:
- Don't introduce mid-range border-radius (4–16px) on buttons or cards — Triumph is sharp-cornered by principle
- Don't use Triumph Crimson (`#cd192d`) as a background surface beyond primary CTAs — one crimson element per section maximum
- Don't use DIN2014-Regular for display headings — Regular is strictly for body and secondary text; Demi carries the brand voice
- Don't apply positive letter-spacing greater than 1px on body text — wide tracking is reserved for display/uppercase contexts
- Don't use soft drop shadows (`rgba(0,0,0,0.1) 0px 10px 30px`) on hero elements — photography provides depth; UI shadows flatten the cinematic quality
- Don't use the Focus Blue (`rgb(30, 174, 219)`) for anything other than keyboard focus states — it's an accessibility color, not a brand color
- Don't introduce gradient fills on section backgrounds — solid black, solid charcoal, solid white; transitions happen between sections, not within them
- Don't lowercase navigation links — all primary nav items are uppercase DIN2014-Demi; breaking this pattern disrupts the mechanical hierarchy

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | ≤375px | Single-column, hero text drops to ~35px, stacked CTAs, full-width buttons |
| Mobile | 376–480px | Single-column, 40–50px hero text, compressed nav |
| Mobile Large | 481–599px | Slightly wider content, beginning of 2-column micro-grids |
| Tablet Small | 600–767px | 2-column layouts begin, hero text 50–60px |
| Tablet | 768–1023px | Full 2-column product layout, horizontal nav compresses |
| Desktop | 1024–1365px | Full multi-column layout, hero at 70–80px max |
| Large Desktop | ≥1366px | Maximum layout width, full 80px hero text, carousel at full scale |

*The system ships with 21 active breakpoints — unusually granular, reflecting the need to maintain full-bleed photographic compositions at every common device width.*

### Touch Targets
- Primary CTAs ("VIEW BIKE", "CONFIGURE"): tall line-heights (2.82–3.25 on 16–17px type) create ~48–52px effective height — meets WCAG 44px minimum
- Navigation links: 44px+ vertical tap area with adequate horizontal spacing
- Carousel arrows: minimum 44×44px invisible tap area around chevron icons
- Section block CTAs: full-width on mobile, providing generous tap surface

### Collapsing Strategy
- **Navigation**: Full horizontal 9-item nav bar collapses to hamburger (or compact icon row) on mobile; secondary utility links ("Dealers", "Configure", "Offers", "Test Ride") may fold into expanded mobile menu
- **Hero carousel**: Full-viewport full-bleed at all breakpoints — maintains cinematic treatment; text positioning shifts from lower-left to lower-center or stacked below on smallest viewports
- **Product sections**: 2-column image+spec layouts collapse to single-column with image stacking above text; CTAs shift to full-width stacked pair
- **Typography scaling**: 80px hero → 50px → 35–40px across breakpoints; `text-transform: uppercase` and `letter-spacing: 1px` maintained throughout
- **Section spacing**: 75–90px vertical padding → 30–40px on mobile; editorial pacing compressed but not eliminated
- **Carousel**: Slide count and arrow visibility maintained; dot indicators scale proportionally

### Image Behavior
- Hero photography maintains full-bleed treatment at all breakpoints using `object-fit: cover`
- Darkening treatment on hero imagery (CSS overlay or image pre-processing) adapts to ensure white text remains legible at all sizes
- Product photography on 2-column cards reflows above text on mobile, maintaining aspect ratio
- No art direction swaps — the same cinematic editorial language applies at every breakpoint

## 9. Agent Prompt Guide

### Quick Reference
- Primary CTA: Triumph Crimson (`#cd192d`)
- Secondary CTA: Triumph Black (`#000000`)
- Page Background (dark): Triumph Black (`#000000`)
- Page Background (light sections): Pure White (`#ffffff`)
- Mid Dark Panel: Charcoal (`#333333`)
- Primary Text (on dark): Pure White (`#ffffff`)
- Primary Text (on light): Charcoal (`#333333`)
- Secondary Text: Oil Grey (`#63656a`)
- CTA Border (crimson): `2px solid #cd192d`
- CTA Border (black): `2px solid #000000`
- Hover Sweep: `rgb(255,255,255) 0px 0px 0px 30px inset`
- Focus State: `rgb(30, 174, 219)` background
- Link Hover: `#3860be`
- Nav Background: `#000000`
- Button Radius: `0px`

### Example Component Prompts
- "Create a hero section with a full-bleed darkened track photograph as background. Overlay a white headline in DIN2014-Demi at 80px, `font-weight: 400`, `line-height: 1.00`, `letter-spacing: 1px`, `text-transform: uppercase`, color `#ffffff`, positioned lower-left with 40px padding. Add a tagline below at 30px DIN2014-Regular weight 400, `line-height: 1.17`, `letter-spacing: 0.5px`, white. Below that, place a crimson CTA button (`background: #cd192d`, `border: 2px solid #cd192d`, `color: #ffffff`, `padding: 0px 20px`, `border-radius: 0px`, 17px DIN2014-Demi, line-height 2.82) and a black secondary button (`background: #000000`, `border: 2px solid #000000`, same type) side by side. Both buttons get hover state: `box-shadow: rgb(255,255,255) 0px 0px 0px 30px inset`, `transform: translateX(5px)`, `opacity: 0.6`."
- "Design a motorcycle model card on a black (`#000000`) background. Model name in DIN2014-Demi 35px, `text-transform: uppercase`, `letter-spacing: 1px`, `line-height: 1.20`, white. Short descriptor in DIN2014-Regular 18px, `letter-spacing: 0.5px`, `line-height: 1.39`, white at 80% opacity. A crimson `VIEW BIKE` button at bottom: `background: #cd192d`, `border: 2px solid #cd192d`, `border-radius: 0px`, `padding: 0px 20px`, 17px DIN2014-Demi. No border-radius, no drop shadow on the card itself — the photography and darkness define the container."
- "Build a top navigation bar on `#000000` background. Left: Triumph wordmark SVG in white. Center: primary links in DIN2014-Demi uppercase — MOTORCYCLES, ACCESSORIES, CLOTHING SHOP, OWNERS, BRAND, RACING — white, no decoration. Right: Dealers, Configure, Offers, Test Ride in DIN2014-Regular at 14px, white; then cart icon and location pin icon; then `USA` region dropdown. All links hover to `#3860be`. Nav height approximately 44px, padding 0 20px."
- "Create a dark section divider with a `1px solid rgb(80, 80, 80)` top border and `background: #333333`. Inside, a DIN2014-Demi heading at 32px uppercase `letter-spacing: 1px`, white. Below, DIN2014-Regular body text at 16px `line-height: 1.50`, color `#63656a`. Section padding: 50px vertical, 20px horizontal. No shadow, no radius."
- "Design a utility dialog (cookie consent) on white (`#ffffff`) background with `border-radius: 2px` and soft shadow `rgba(0,0,0,0.2) 0px 0px 18px 0px`. Heading in DIN2014-Regular 16px weight 600. Body in DIN2014-Regular 13px `line-height: 1.69`. Two buttons side by side: 'COOKIE PREFERENCES' in white-surface button (`background: #ffffff`, `color: rgb(42,42,42)`, `border-radius: 2px`, `padding: 12px 10px`, 13px DIN2014-Regular weight 600) and 'ALLOW ALL' in black button (`background: #000000`, `color: #ffffff`, `border-radius: 2px`, `padding: 12px 10px`, 17px DIN2014-Demi). Both hover to `background: rgb(30, 174, 219)` white text."

### Iteration Guide
1. `text-transform: uppercase` + `letter-spacing: 1px` on DIN2014-Demi is the non-negotiable display formula — never remove either property from headline elements
2. All border-radius stays at `0px` for structural/interactive elements; use `2px` only for utility dialog buttons where softness is permissible
3. The inset sweep hover (`rgb(255,255,255) 0px 0px 0px 30px inset`) must appear on every primary and secondary CTA button — it is the system's kinetic signature, not optional
4. Crimson (`#cd192d`) appears once per visual cluster maximum — if it's on the primary CTA, no other element in the same section should be crimson
5. DIN2014-Demi for all headings and CTAs; DIN2014-Regular for body and captions — the split is absolute, never reversed
6. Dark sections (`#000000`) need only white text and photography — resist adding shadows, borders, or decorative elements; the contrast does the work
7. Focus Blue (`rgb(30, 174, 219)`) appears only in keyboard focus/active states — never use it as a section color or brand moment
8. Line-heights on buttons are tall by convention (2.82–3.25) — this creates the button height through type, not padding; maintain this approach for consistent touch target sizing
9. Link hover color converges to `#3860be` regardless of default link color — white links, crimson links, and black links all hover to the same navy
10. Letter-spacing scales with context: `1px` at display uppercase, `0.5px` at secondary uppercase, `0.17px` at buttons, normal at body — never apply display-scale tracking to body text