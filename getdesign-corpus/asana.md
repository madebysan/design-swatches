---
slug: asana
name: Asana
url: https://asana.com
domain: asana.com
category: Productivity
styles: [Light, Editorial, Monochromatic, Warm]
tagline: "Productivity whiteboard lit by a coral lamp — authoritative black type on a breathing white field, with a warm coral flash and a deep-navy flicker to signal where action lives."
fonts: [Ghost, TWK Lausanne]
primary_color: "#646f79"
---

# Design System Inspired by Asana

> Productivity whiteboard lit by a coral lamp — authoritative black type on a breathing white field, with a warm coral flash and a deep-navy flicker to signal where action lives.

## 1. Visual Theme & Atmosphere

Asana reads as a white canvas under a coral-and-violet editorial system — generous whitespace punctuated by a near-black (`#0d0d0d`) headline weight that commands attention, then released into light gray body copy. The signature move is two coexisting type voices: Ghost at 60–72px with -0.0070em tracking for display headlines that compress letter forms into dense, authoritative blocks, and TWK Lausanne at 300–500 weight handling everything else with a humanist openness. The pairing reads like an editorial magazine spread retrofitted for a SaaS product page.

The chromatic system runs on two distinct accent families that never mix. Coral (`#ffeaec` background paired with `#690031` deep text) acts as a warm semantic accent — surfacing in active filter chips, icon illustrations, and brand-warm UI states. Asana Violet (`#222875`) is the cool informational counterpart — used for product UI frames, AI feature callouts, and trust signals. Both are restrained to small, intentional doses against an otherwise achromatic canvas. Coral signals interaction and warm brand energy; violet signals product, AI, and information architecture.

The most distinctive shape signature is the pill-on-card tension. Buttons and filter chips use a 100px+ radius (146px on the secondary CTA), floating as soft capsules against sharp-cornered cards (10–16px) and rounded product UI frames (16px outer, 10px inner). The result is a deliberate visual contrast: the softness of the button against the geometry of surrounding content. Vertical rhythm runs generous — 80–120px between sections — giving each content cluster breathing room.

**Key Characteristics:**
- White canvas (`#ffffff`) with `#f3f3f3` secondary panels — near-achromatic page texture
- Two-family typography: Ghost (display only, 60–72px, weight 500) + TWK Lausanne (everything else, 300–500)
- Pill buttons at 100px / 146px radius — the only soft elements in an otherwise angular system
- Two restricted chromatic families: Coral (warm/interaction) and Violet (cool/information)
- Coral semantic pair: `#ffeaec` background must lock with `#690031` text — never substituted
- Asana Violet (`#222875`) reserved for product UI frames and informational containers
- Cards at 10–16px radius with 1px solid `#e7e7e7` borders — no shadows
- Generous section gaps (80–120px) — each cluster breathes
- 40px circular arrow icon buttons (`#0d0d0d` active, `#e7e7e7` inactive) for carousel navigation
- TWK Lausanne weight 300 for body copy — open, non-urgent reading texture

## 2. Color Palette & Roles

### Background Surfaces
- **Pure White** (`#ffffff`): Page background, primary surface.
- **Mist** (`#f3f3f3`): Secondary section background, secondary button fill.

### Text & Content
- **Ink Black** (`#0d0d0d`): Body text, primary CTA fills, headline text.
- **Charcoal** (`#3d3d3d`): Body copy at normal reading weight.
- **Slate** (`#646f79`): Secondary body text — the primary anchor color.
- **Iron** (`#474748`): List items.
- **Graphite** (`#6e6e6`): Nav text.
- **Ash** (`#9ca6af`): Placeholder text.

### Brand & Accent — Coral Family (warm, interaction)
- **Coral Blush** (`#ffeaec`): Active filter chip background — soft warm fill.
- **Deep Coral** (`#690031`): Coral-family high-contrast text on Coral Blush. Locked semantic pair.
- **Coral Petal** (`#e1bbc7`): Icon strokes and borders.
- **Coral Ember** (`#ff584a`): Icon fills in use-case cards.
- **Coral Dark** (`#710c3a`): Hover/pressed state for coral-family elements.

### Brand & Accent — Violet Family (cool, information)
- **Asana Violet** (`#222875`): Product UI frame fills, feature container backgrounds.
- **Sky Ice** (`#cbefff`): Blue-tinted soft background for informational chips and feature callouts.

### Border & Divider
- **Cloud** (`#e7e7e7`): Card borders — the system default.
- **Stone** (`#e0dedc`): Subtle component borders.

## 3. Typography Rules

### Font Families
- **Ghost** (substitute: Neue Haas Grotesk Display, Aktiv Grotesk Ex): Display headlines only — the hero statement and major section titles. Weight 500 at 60–72px with tight -0.007em tracking compresses letter forms into dense editorial blocks. No other font on the site operates at this scale, making Ghost the unambiguous voice of authority.
- **TWK Lausanne** (substitute: Inter, DM Sans): Everything except hero display text — nav labels (weight 400, 14px), body copy (weight 300–400, 16px), subheadings (weight 500, 20–30px), section headings (weight 500, 24–36px). Weight 300 for body imparts an open, non-urgent reading texture. Weight 500 reserved for UI labels and mid-hierarchy headings. Positive letter-spacing at small sizes (+0.025–0.04em) prevents optical crowding.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display | Ghost | 72px | 500 | 1.00 | -0.50 |
| Heading-lg | Ghost | 60px | 500 | 1.00 | -0.42 |
| Heading | TWK Lausanne | 36px | 500 | 1.20 | -0.36 |
| Heading-sm | TWK Lausanne | 24px | 500 | 1.20 | normal |
| Subheading | TWK Lausanne | 20px | 500 | 1.30 | normal |
| Body | TWK Lausanne | 16px | 300 | 1.50 | normal |
| Body-emphasis | TWK Lausanne | 16px | 500 | 1.50 | normal |
| Caption | TWK Lausanne | 11px | 500 | 1.75 | +0.44 |

### Principles
- **Two voices, one rule**: Ghost speaks at display scale only (60px+). TWK Lausanne handles every other role. The split is non-negotiable — Ghost never appears below 60px, TWK Lausanne never appears at hero scale.
- **Weight 300 for body, weight 500 for action**: Body copy at TWK Lausanne 300 reads as open and unhurried. UI labels, CTAs, and subheadings step up to 500. Weight 400 sits between as a middle voice for navigation.
- **Negative tracking only at scale**: Headings 20px and above run negative or zero letter-spacing. Captions and small labels relax to positive tracking (+0.025 to +0.44) to prevent optical crowding.
- **Tight display, relaxed body**: Display at line-height 1.00 produces tightly-packed headline blocks; body at 1.50 lets reading breathe. The contrast is structural, not decorative.

## 4. Component Stylings

### Buttons

**Primary CTA Button (Pill)**
- Background: `#0d0d0d`, Text: `#ffffff`, Border: none
- Radius: `100px` (extreme pill), Padding: `16px 32px`
- Font: TWK Lausanne weight 500, 16px
- The pill against square card containers is the site's primary tension — softness of the button against geometry of surrounding content

**Secondary Outline Button (Pill)**
- Background: `#f3f3f3`, Text: `#0d0d0d`, Border: `1px solid #0d0d0d`
- Radius: `146px` (slightly larger than primary — visually paired but distinct)
- Padding: `16px 32px`. Font: TWK Lausanne weight 500, 16px
- Inverted surface from primary; near-identical radius keeps the two visually paired

**Ghost Nav Button**
- Background: transparent, Text: `#6e6e6`, Border: `1px solid #6e6e6`
- Radius: `3px` — the sharpest shape on the site, deliberately not pill-shaped
- Padding: `0 12px`, no vertical padding. Font: TWK Lausanne weight 400, 14px
- Used for navigation dropdown triggers; sharp shape distinguishes nav from CTAs

**Arrow Circle Icon Button**
- Diameter: 40px, Radius: `100px` (circle)
- Active: background `#0d0d0d`, icon `#ffffff`
- Inactive: background `#e7e7e7`, icon `#0d0d0d`
- Used for carousel prev/next and inline card-level CTA links

### Cards

**Use-Case Feature Card**
- Background: `#ffffff`, Border: `1px solid #e7e7e7`, Radius: 10–16px, Padding: 24px
- Coral stroke line illustration at top (~80px tall)
- Heading TWK Lausanne 20px weight 500 `#0d0d0d`, 16px below illustration
- Body TWK Lausanne 16px weight 300 `#3d3d3d`, 14px below heading
- 'See [X]' text link `#0d0d0d` weight 400 with a 40px circular `#0d0d0d` arrow icon button at bottom-left

**Product UI Screenshot Card**
- Outer frame: `#222875` (Asana Violet) background, Radius: 16px
- Inner app window: white background, Radius: 10px (nested 6px smaller than outer)
- The violet container makes the white app UI float as if lit from within
- Used at large scale in the hero (full-width up to 760px tall)

### Filter Chips & Badges

**Filter Chip — Active (Coral pair)**
- Background: `#ffeaec` (Coral Blush), Text: `#690031` (Deep Coral)
- Radius: `999px`, Padding: 8–12px horizontal
- Font: TWK Lausanne weight 500, 14px
- The Coral Blush + Deep Coral pair is locked — substituting either half breaks the semantic system

**Filter Chip — Inactive**
- Background: `#f3f3f3`, Text: `#0d0d0d`
- Same shape and font as active variant — only the surface flips

**Informational Tint Chip**
- Background: `#cbefff` (Sky Ice — blue tint) or `#ffeaec` (coral tint)
- Text: `#222875` or `#690031` respectively
- Radius: `999px`, Padding: `4px 12px`
- Font: TWK Lausanne weight 500, 12px, letter-spacing +0.03em
- Used for category labels inside product UI screenshots and callout blocks

### Navigation

**Sticky Navigation Bar**
- Background: `#ffffff`, Bottom border: `1px solid #e7e7e7`, Height: 56px
- Logo left-aligned. Center: nav items in Ghost Nav Button style (transparent, `#6e6e6e`)
- Right: 'Contact sales' text link (`#0d0d0d`), 'Log in' text link, 'Get started' primary pill button
- All nav text in TWK Lausanne 14px weight 400

### Logo Bar / Social Proof Strip
- White background, no border, no shadow
- Logos in grayscale at medium opacity, 32–48px column gap
- Stat text ('85% of Fortune 100') at TWK Lausanne weight 500, 30px, `#0d0d0d`

## 5. Layout Principles

### Spacing System
- **Element gap**: 16px
- **Section gap**: 80–120px — generous, gives each cluster breathing room
- **Card padding**: 24px

### Border Radius Scale
- **Tags**: `999px` (full pill)
- **Cards**: `10–16px`
- **Inputs**: `4px`
- **Modals**: `20px`
- **Buttons (primary pill)**: `100px`
- **Buttons (secondary pill)**: `146px`
- **Nav buttons**: `3px` (the sharpest shape — deliberate)

The radius range is wide because each scale corresponds to a function: 3px nav (sharp/instructional), 4px input (subtle), 10–16px card (grounded), 100–146px button (pill/interactive), 999px chip (full pill/tag).

### Grid
- Max-width: ~1200px centered for content; product UI cards bleed wider
- Hero pattern: centered headline, centered subhead at ~560px max-width, two pill buttons in a row, full-width product UI screenshot card below
- Subsequent sections alternate: full-width logo bar (no container), 2-column text + tabbed-filter + image, horizontally scrolling card rails (4 cards visible, 10px gap, overflow hinted)
- Navigation: fixed top bar at 56px, left logo + center nav + right utility links

### Layout & Composition
The page is structured as a vertical sequence of cleanly-separated content clusters, each with 80–120px of vertical breathing. The hero uses a centered-stack pattern: Ghost headline, TWK Lausanne subhead, paired pill buttons, then a full-width Asana Violet product UI screenshot card. Below alternate full-width white logo bars, 2-column splits (text + tabbed filter + image), and horizontally scrolling feature card rails with explicit prev/next circular controls. Cards never use shadows — borders alone define boundaries. The print-like surface quality is part of the brand voice.

## 6. Depth & Elevation

| Level | Hex | Name | Purpose |
|-------|-----|------|---------|
| 1 | `#ffffff` | Pure White | Page background, default card surface |
| 2 | `#f3f3f3` | Mist | Secondary section panel, inactive chip background |
| 3 | `#222875` | Asana Violet | Product UI container surface — semantic depth via brand color |

**Shadow Philosophy**: Asana refuses box-shadows on content surfaces. Cards rely on 1px solid `#e7e7e7` borders alone to define boundaries. The flat, print-like surface quality is the system's signature — adding a shadow would compromise the editorial register. Depth instead emerges from color stepping (white page → mist secondary panels → violet product frames) and from the contained inversion of the violet UI cards, which make their internal white app windows appear lit from within rather than elevated above.

## 7. Do's and Don'ts

### Do

- Use Ghost font at 60–72px with letter-spacing -0.0070em exclusively for top-level display headlines — no other element should compete at this scale.
- Apply 100px+ border-radius on all CTA buttons (primary and secondary) and filter chips — pill shapes are the only soft element in an otherwise angular component set.
- Reserve `#222875` (Asana Violet) for product UI frames and informational containers — never use it as a button fill or section background.
- Pair Coral Blush (`#ffeaec`) backgrounds exclusively with Deep Coral (`#690031`) text — they are a locked semantic pair; do not substitute either half.
- Maintain a near-achromatic page canvas (`#ffffff` primary, `#f3f3f3` secondary) and introduce coral or violet only as small contained accents, never as full-section backgrounds.
- Use TWK Lausanne weight 300 for all body copy to preserve the open, non-urgent reading texture — weight 400 is for UI labels and nav, weight 500 for subheadings and CTAs.
- Set card borders to 1px solid `#e7e7e7` with 10–16px radius — no box shadows on content cards; elevation is conveyed through color contrast alone.

### Don't

- Never use Ghost font below 60px — TWK Lausanne at weight 500 handles all sub-display heading sizes.
- Never apply the pill button radius (100px+) to cards, inputs, or modal containers — the shape language is exclusive to interactive action elements.
- Never fill a full page section with `#222875` or any saturated color — the violet and coral appear only in contained UI frames or chip-sized elements.
- Never use positive letter-spacing on headings — letter-spacing is negative or zero for all sizes 20px and above.
- Never mix the coral and violet accent families in the same component — they operate as separate semantic threads.
- Never add box-shadow elevation to feature cards — borders alone define card boundaries; shadows break the flat, print-like surface quality.
- Never set body copy weight above 400 — weight 500 is reserved for labels, CTAs, and subheading roles only.

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Hero collapses to single column, headline drops to ~40–48px |
| md | 768px+ | Two-column splits return, paired pill buttons stack tighter |
| lg | 1024px+ | Full multi-column layout, horizontally scrolling card rails activate |
| xl | 1280px+ | Max-width 1200px applies, product UI card bleeds wider than text container |

### Touch Targets
- Pill buttons at `16px 32px` padding give comfortable 48px+ touch targets at all sizes
- 40px circular arrow icon buttons meet minimum touch target without scaling
- Filter chips at `8–12px` padding need parent spacing of 8px+ for thumb separation

### Collapsing Strategy
- Hero display 72px → 60px → ~48px → ~40px on small mobile, line-height 1.00 maintained
- 4-card horizontal rails stack to single-card scroll on mobile, then to 2-up at md, full 4-up at lg
- Section gaps compress from 120px to ~64px on mobile to preserve density
- Product UI screenshot card preserves 16px outer / 10px inner radii at all sizes
- Pill buttons preserve 100px+ radius at all sizes — the shape is non-negotiable

## 9. Agent Prompt Guide

### Quick Color Reference
- Text (primary): `#0d0d0d`
- Text (body): `#3d3d3d`
- Background (page): `#ffffff`
- Background (secondary section): `#f3f3f3`
- CTA button fill: `#0d0d0d`
- CTA button text: `#ffffff`
- Brand accent (violet): `#222875`
- Brand accent (coral bg): `#ffeaec`
- Brand accent (coral text): `#690031`
- Border (cards): `#e7e7e7`

### Example Component Prompts

1. **Hero Section**: White background, max-width 1200px centered. Headline in Ghost font 72px weight 500, `#0d0d0d`, letter-spacing -0.50px, line-height 1.00, centered. Subhead in TWK Lausanne 20px weight 300, `#3d3d3d`, centered, max-width 560px, 16px below headline. Two buttons in a row centered below (24px gap): primary pill (`#0d0d0d` fill, `#ffffff` text, 100px radius, 16px 32px padding) + secondary pill (`#f3f3f3` fill, `#0d0d0d` text, 1px solid `#0d0d0d`, 146px radius, 16px 32px padding). Product UI screenshot card below buttons in a `#222875` frame with 16px radius.

2. **Use-Case Feature Card**: White background, 1px solid `#e7e7e7` border, 10px radius, 24px padding. Coral stroke line illustration at top (~80px tall). Heading TWK Lausanne 20px weight 500 `#0d0d0d`, 16px below illustration. Body TWK Lausanne 16px weight 300 `#3d3d3d`, 14px below heading. 'See [X]' text link `#0d0d0d` weight 400, with a 40px circular `#0d0d0d` arrow icon button at bottom-left of card.

3. **Filter Chip Row**: Horizontally arranged pill chips (999px radius). Active chip: `#ffeaec` background, `#690031` text, TWK Lausanne 14px weight 500. Inactive chips: `#f3f3f3` background, `#0d0d0d` text, same font. 8px horizontal gap between chips. 16px 24px padding per chip.

4. **Logo / Social Proof Bar**: White background, full-width, 80px vertical padding. Left side: stat text TWK Lausanne 30px weight 500 `#0d0d0d` ('85% of Fortune 100 companies choose Asana'). Right side: 5 company logos in a horizontal row at 48px gap, rendered flat gray (`#646f79` or desaturated). No border, no shadow.

5. **Section Header Block**: Left-aligned. Ghost font 60px weight 500 `#0d0d0d`, letter-spacing -0.42px, line-height 1.00. Below: TWK Lausanne 16–20px weight 300 `#3d3d3d`, max-width 480px, 16px margin-top. Section gap above: 96px.

### Iteration Guide
1. Ghost above 60px, TWK Lausanne everywhere else — never blur the line.
2. Pills are interactive; cards are content. Never apply 100px+ radius to cards.
3. Coral and Violet are semantic threads — coral for interaction/warmth, violet for product/information. Never mix in one component.
4. The Coral Blush + Deep Coral pair (`#ffeaec` / `#690031`) is locked. Don't substitute.
5. Body weight 300, UI weight 500 — keep the texture distinction clean.
6. Cards have borders, never shadows. Print-like flatness is the brand voice.
7. Asana Violet is for contained UI frames only — never a section background.

## Preview

![Asana](https://ysxnuuuj3kqhdyj2.public.blob.vercel-storage.com/1775934085899-thumb.jpg)
