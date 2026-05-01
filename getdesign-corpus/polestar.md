# Design System Inspired by Polestar

## 1. Visual Theme & Atmosphere

Polestar's website is Scandinavian minimalism applied to a luxury electric car brand — and it's the cleanest car configurator on the web. The page opens on a pure white canvas (`#ffffff`) that runs uninterrupted from edge to edge, with no gradient backdrops, no atmospheric glows, no decorative chrome. Everything is built around oversized product photography, a confident grotesk in three sizes, and a deep black-and-white type system that lets the cars themselves carry the visual weight. Where every other automotive site reaches for cinematic video loops, neon accent colors, and racetrack imagery, Polestar reaches for negative space.

The custom `Polestar Unica77` typeface is the defining element of the brand's visual identity. Display headlines run at a confident weight 400 (regular) — never bold, never italic — at sizes that scale from 32px on cards up to 72–96px on hero statements. Tracking is consistently tight and slightly negative on display sizes (`-0.02em`), and line-height locks to 1.0–1.1 so headlines read as architectural blocks rather than airy editorial passages. Body copy drops to 16px regular with normal tracking and 1.5 line-height — a Swiss-modernist pairing that feels closer to a museum exhibition catalogue than a car website.

What distinguishes Polestar most is its **commitment to chromatic restraint**. The system is functionally monochrome: black, white, and a tight family of cool grays. There is no signature accent color — no blue, no green, no electric-vehicle cliché. The cars themselves provide the only color on the page (Snow white, Stratus gray, Space black, Electron silver, Gold Matte). Every UI element — buttons, links, dividers, badges — is rendered in pure black or pure white. Borders are 1px hairlines. Corners are uniformly sharp at 0px or barely-rounded at 2–4px. The result is an interface that feels less like marketing and more like a calibrated instrument panel.

**Key Characteristics:**
- Polestar Unica77 at weight 400 for all display, heading, and body text — single-weight discipline
- Pure white page canvas (`#ffffff`) — no off-whites, no warm tints, no gradients
- Functionally monochrome system — black, white, and cool gray scale only
- Hairline 1px borders in black or `rgba(0,0,0,0.12)` — no thick rules, no shadows
- Sharp 0–4px corner radii — buttons, cards, and inputs all sit on a near-rectilinear grid
- Tight negative tracking (`-0.02em`) on display sizes; normal on body
- Full-bleed product photography on neutral seamless backgrounds — no environments, no scenery
- Generous vertical whitespace (96–160px between sections) with type-anchored rhythm
- The car IS the color — every chromatic moment on the page comes from product imagery

## 2. Color Palette & Roles

### Primary
- **Polestar Black** (`#000000`): Primary text, headings, body copy, primary button backgrounds, icon strokes, borders. Pure unsoftened black.
- **Polestar White** (`#ffffff`): Primary page background, button text on dark, inverted surfaces. Pure unsoftened white — never off-white, never warm.

### Brand Accent
- Polestar deliberately has **no chromatic brand accent**. Where competitors use electric blue, racing red, or eco green, Polestar uses none. The cars supply the color.

### Neutrals & Text
- **Polestar Black** (`#000000`): All primary text and headings.
- **Body Gray** (`#3d3d3d`): Long-form body copy in dense paragraph blocks (terms, sustainability text) — softens slightly from pure black for reading comfort.
- **Caption Gray** (`#6e6e6e`): Secondary metadata, captions, footnote markers, helper text.
- **Disabled Gray** (`#a8a8a8`): Disabled states, inactive nav items, low-emphasis labels.

### Surface & Borders
- **Surface White** (`#ffffff`): Default page and card surface — flat, unmodulated.
- **Surface Mist** (`#f4f4f4`): Subtle alternating section background for visual rhythm without introducing warmth.
- **Surface Stone** (`#e6e6e6`): Tertiary panel surface for sustainability charts, comparison tables.
- **Border Black** (`#000000`): Full-weight 1px borders on outlined buttons, dividers between major sections.
- **Border Hairline** (`rgba(0, 0, 0, 0.12)`): 1px subtle dividers between cards, table rows, footer columns.

### Product Color Reference (drawn from the cars)
These appear ONLY on product imagery, never as UI fills:
- **Snow** (`#f5f5f5`) — exterior white paint
- **Stratus** (`#bfbfbf`) — exterior light gray
- **Space** (`#1a1a1a`) — exterior near-black
- **Electron** (`#888888`) — exterior medium silver
- **Gold Matte** (`#a89368`) — exterior matte gold (rare accent)

### Gradient System
- Polestar is **gradient-free**. Every fill is a flat solid. The only tonal transitions on the page come from product photography lighting on the cars themselves. No CSS gradients, no overlay scrims, no atmospheric fades.

## 3. Typography Rules

### Font Family
- **Primary**: `Polestar Unica77`, with fallback: `Helvetica`, `Arial`, `sans-serif`
- **Monospace / Numeric**: Same `Polestar Unica77` — no mono variant. Tabular figures used for spec tables.
- **OpenType Features**: Tabular figures (`tnum`) for spec tables and pricing. No stylistic alternates.

*Note: Polestar Unica77 is a custom-licensed cut of Lineto's Unica77. For external implementations, **Söhne** by Klim Type Foundry is the closest substitute, **Inter** at weight 400 works as a free web alternative, and **Neue Haas Grotesk Display** captures the same Swiss-grotesk character.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Unica77 | 96px (6.00rem) | 400 | 1.00 | -0.02em | Maximum size — landing hero statements ("Choose better.") |
| Display Large | Unica77 | 72px (4.50rem) | 400 | 1.05 | -0.02em | Section openers, full-width statements |
| Display | Unica77 | 56px (3.50rem) | 400 | 1.10 | -0.02em | Primary feature section titles |
| Heading 1 | Unica77 | 40px (2.50rem) | 400 | 1.10 | -0.01em | Page-level headings |
| Heading 2 | Unica77 | 32px (2.00rem) | 400 | 1.15 | -0.01em | Card titles, sub-section heads |
| Heading 3 | Unica77 | 24px (1.50rem) | 400 | 1.20 | normal | Feature titles, comparison labels |
| Heading 4 | Unica77 | 20px (1.25rem) | 400 | 1.30 | normal | Small section heads, tile titles |
| Body Large | Unica77 | 18px (1.13rem) | 400 | 1.40 | normal | Intro paragraphs, sustainability statements |
| Body | Unica77 | 16px (1.00rem) | 400 | 1.50 | normal | Standard reading text |
| Body Small | Unica77 | 14px (0.88rem) | 400 | 1.50 | normal | Secondary copy, helper text |
| Nav Link | Unica77 | 14px (0.88rem) | 400 | 1.00 | normal | Top navigation, footer columns |
| Button UI | Unica77 | 14px (0.88rem) | 400 | 1.00 | normal | Button labels — sentence case, never uppercase |
| Caption | Unica77 | 12px (0.75rem) | 400 | 1.40 | normal | Footnotes, legal text, image credits |
| Spec Number | Unica77 (tnum) | 32–48px | 400 | 1.00 | -0.01em | Performance specs (range, 0–60, hp) |

### Principles
- **Single-weight discipline**: The entire system runs on weight 400. No bold, no light, no italic. Visual hierarchy comes exclusively from size and spacing, not weight contrast. This is the most defining rule of the system.
- **Sentence case everywhere**: Headlines, buttons, and nav items all use sentence case ("Book a test drive" — not "BOOK A TEST DRIVE"). Polestar never shouts.
- **Tight display tracking**: Letter-spacing tightens to `-0.02em` at 56px+ and `-0.01em` at 24–40px, returning to normal at 20px and below. The negative tracking is subtle but consistent.
- **Locked display line-height**: Headlines run at 1.00–1.15 line-height. This produces dense architectural type blocks rather than open editorial passages — fitting for a brand that builds cars on a grid.
- **Body copy breathes at 1.5**: Where headlines lock tight, paragraph copy opens up to 1.5 line-height for sustained reading on terms, sustainability, and ownership pages.
- **Numerals for specs**: Performance figures (range, kWh, 0–60 mph) use tabular figures at large display sizes for direct visual comparison across cars.

## 4. Component Stylings

### Buttons

**Primary Black**
- Background: Polestar Black (`#000000`)
- Text: Polestar White (`#ffffff`)
- Padding: 14px 24px standard, 18px 32px large
- Radius: `2px` (nearly sharp — barely-rounded edge)
- Border: `0px`
- Shadow: none
- Font: 14px Unica77 weight 400, sentence case, normal tracking
- Hover: background shifts to `#1a1a1a`, no transform
- Use: Primary CTA — "Shop available cars", "Book a test drive", "View offers"

**Outlined Black**
- Background: transparent
- Text: Polestar Black (`#000000`)
- Border: `1px solid #000000`
- Padding: 13px 23px (1px shy to compensate for border)
- Radius: `2px`
- Hover: background fills to `#000000`, text inverts to `#ffffff`
- Use: Secondary CTA — "Find a retailer", "Read more"

**Ghost Link Button**
- Background: transparent
- Text: Polestar Black (`#000000`)
- Border: `0px`
- Padding: 14px 0px
- Underline: `1px solid #000000` on hover (slides in from left)
- Trailing arrow icon: 16px line-style chevron
- Use: Tertiary actions, footer links, "Read more" tail links

**Inverted Primary (on dark hero)**
- Background: Polestar White (`#ffffff`)
- Text: Polestar Black (`#000000`)
- Padding: 14px 24px
- Radius: `2px`
- Hover: background shifts to `#f0f0f0`
- Use: CTAs that sit on dark product imagery or photography backgrounds

### Cards & Containers
- Background: `#ffffff` on light sections; `#f4f4f4` for alternating tonal blocks
- Border: `0px` default — cards rely on whitespace and 1px dividers, not frames
- Radius: `4px` for car-card containers; `0px` for full-width content blocks
- Shadow: none — Polestar uses zero box-shadow across the entire system
- Internal padding: 24–32px for car cards, 48–96px for feature containers
- Image treatment: cars sit on flat seamless backgrounds, never composited into environments

### Badges / Tags / Pills
**Hairline Tag**
- Background: transparent
- Text: Polestar Black (`#000000`)
- Border: `1px solid rgba(0, 0, 0, 0.12)`
- Padding: 4px 10px
- Radius: `2px`
- Font: 12px Unica77 weight 400
- Use: Spec category labels, filter pills

**Solid Black Badge**
- Background: Polestar Black (`#000000`)
- Text: Polestar White (`#ffffff`)
- Padding: 4px 10px
- Radius: `2px`
- Font: 12px Unica77 weight 400
- Use: New-arrival markers, status badges (sparingly used)

### Inputs & Forms
- Background: `#ffffff`
- Border: `1px solid #000000` (full weight) or `1px solid rgba(0,0,0,0.24)` (resting)
- Border on focus: `1px solid #000000` + `0 0 0 1px #000000` outer ring
- Radius: `2px`
- Font: 16px Unica77 weight 400
- Text color: `#000000`, placeholder `#a8a8a8`
- Padding: 14px 16px
- Labels: 14px above the field, normal tracking, `#3d3d3d`
- Use: Newsletter signup, retailer location lookup, configurator selection

### Navigation
- Top nav: horizontal white bar, left-aligned Polestar wordmark (SVG, all caps but in the logotype itself), right-aligned model links and account/cart icons
- Hover menus: full-width drop panels with car renders and link columns — same white background, hairline 1px black divider above the panel
- Links: Unica77 14px weight 400, `#000000`, normal tracking
- Hover: 1px underline slides in below the link from left to right (200ms ease)
- Sticky behavior: nav remains fixed at top with hairline `rgba(0,0,0,0.12)` bottom border on scroll
- Mobile: hamburger collapses to full-screen white overlay menu, large 32px link list

### Decorative Elements

**Hairline Dividers**
- 1px solid `rgba(0, 0, 0, 0.12)` horizontal rules separate footer columns, table rows, and adjacent sections
- Never thicker than 1px; no double rules; no vertical dividers except in spec comparison tables

**Full-Bleed Product Photography**
- Hero shots and feature imagery fill the viewport edge-to-edge
- Cars are always photographed on flat seamless gray or white sweeps — never roads, never landscapes, never people unless intentional cabin shots
- Text overlays rare — when they appear, they're black on white panels adjacent to imagery, not over it

**Spec Block**
- Large tabular figure (32–48px) paired with a 14px caption beneath
- Used for range, 0–60 mph, kWh, hp — direct numeric comparison, no decoration

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Scale: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px, 160px
- Notable: The scale is linear and predictable — Polestar uses every step, not just the extremes. Mid-range values (24–48px) appear constantly for component padding and small section gaps; large values (96–160px) handle major section breaks.

### Grid & Container
- Max content width: 1440px on large desktop, 1200px standard
- Hero: full-bleed, with text content constrained to a 1200px inner column
- Feature sections: 12-column grid, content typically fills 8–12 columns
- Car showcase: 2-column or 3-column grid of car cards with consistent aspect ratios
- Spec tables: 4–5 column tabular layouts for cross-model comparison
- Full-bleed product imagery breaks the container regularly for cinematic moments

### Whitespace Philosophy
- **Architectural pacing**: Each section gets significant vertical breathing room (96–160px between majors) — the page reads like a museum wall layout
- **Type-anchored rhythm**: A 96px hero needs 128–160px of air above and below; a 16px paragraph only needs 24–32px
- **Tonal alternation**: Pure white sections alternate with `#f4f4f4` mist sections to chapter the page without requiring decorative dividers or color changes
- **No filler chrome**: Polestar will leave a section 50% empty rather than fill it with secondary content — emptiness is a deliberate design tool

### Border Radius Scale
- Sharp (0px): Default for full-width blocks, dividers, hero containers
- Near-Sharp (2px): Buttons, inputs, badges, small cards — the workhorse radius
- Soft (4px): Car cards, feature tiles — very subtle softening
- No mid-range radii: Polestar does not use 8–24px radii. The system stays close to rectilinear at all times. No fully-rounded pills.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text, structural containers, cards |
| Hairline (Level 1) | `1px solid rgba(0, 0, 0, 0.12)` | Section dividers, table rows, footer column splits |
| Outline (Level 2) | `1px solid #000000` | Outlined buttons, focused inputs, emphasized cards |
| Focus Ring (Level 3) | `0 0 0 1px #000000` outer + `1px solid #000000` border | Keyboard focus on interactive elements |
| Inverted Tonal (Level 4) | Background swap to `#000000` | Dark sections — full-bleed black panels for product hero |

**Shadow Philosophy**: Polestar's depth system is **graphic and tonal, not atmospheric**. There is no `box-shadow` anywhere in the system. Where every other car brand reaches for soft elevation shadows under cards and buttons, Polestar refuses entirely. Depth comes from three sources only — (1) hairline 1px borders, (2) tonal background shifts between white and `#f4f4f4`, and (3) full-tonal inversions to pure black sections. This produces a flat, printed quality that echoes Swiss exhibition design and reinforces the brand's commitment to material honesty. If you need an element to feel "lifted," you give it more whitespace, not a shadow.

### Decorative Depth
- Hairline borders pair with the near-sharp 2px radii to create a precise, instrumented feel
- Tonal alternation (white and mist) creates chapter breaks without decoration
- Pure black sections function as the deepest "elevation" — full inversions used sparingly for product hero moments
- No glow, no inner shadow, no gradient overlays, no atmospheric mist

## 7. Do's and Don'ts

### Do
- Use Unica77 weight 400 for every size — single-weight discipline is the brand
- Keep the page canvas pure `#ffffff` — never warm white, never off-white
- Let product photography supply the color — every UI element stays monochrome
- Use 1px hairline borders for dividers — never thicker rules
- Keep corner radius at `0–4px` — sharp is the default
- Use sentence case for all buttons, headlines, and nav — never uppercase
- Apply tight negative tracking (`-0.02em`) on display sizes 56px and up
- Photograph cars on flat seamless backgrounds — no environments, no scenery
- Leave sections 50% empty when emptiness is the point — whitespace is a deliberate tool
- Pair tabular figures with small captions for performance specs

### Don't
- Don't use bold or light weights on Unica77 — weight 400 is the only weight
- Don't introduce a brand accent color — Polestar has none
- Don't use `box-shadow` anywhere — the system is flat by mandate
- Don't use mid-range corner radii (8–24px) — stay near-rectilinear
- Don't compose cars into landscapes, roads, or environments — flat backgrounds only
- Don't use uppercase or all-caps for UI chrome — sentence case is non-negotiable
- Don't add gradient fills or atmospheric overlays — the system is solid-color only
- Don't soften pure black or pure white — `#000` and `#fff` stay unsoftened
- Don't use thick borders or double rules — 1px hairlines only
- Don't reach for cinematic video loops or motion-heavy hero treatments — stillness is the brand

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero type drops to 36–40px |
| Mobile | 375–600px | Single-column, 40–48px hero, full-width buttons |
| Tablet | 600–960px | 2-column grids begin, 56–64px hero |
| Desktop | 960–1280px | 3-column grids, 72–80px hero, 1200px container |
| Large Desktop | ≥1280px | Maximum type scale (96px hero), 1440px container |

### Touch Targets
- Primary CTAs: min 48px tap height, full-width on mobile
- Nav links: 44px tap height in mobile overlay menu
- Configurator selectors: 56–64px tap targets for color and wheel selection

### Collapsing Strategy
- **Nav**: Horizontal model bar collapses to hamburger on mobile; opens to full-screen white overlay with 32px sentence-case link list
- **Hero**: 96px → 72px → 56px → 40px progressive scaling, weight 400 maintained
- **Car showcase**: 3-column grid → 2-column → single-column stacked
- **Spec tables**: Horizontal 4-column comparison transforms to vertically stacked spec groups on mobile
- **Section spacing**: 160px desktop → 64–80px mobile — reduces but maintains architectural pace
- **Imagery**: Full-bleed product photography preserved at every breakpoint; aspect ratios shift from 16:9 desktop to 4:5 mobile

### Image Behavior
- Product imagery maintains seamless flat background treatment on mobile
- Hero car renders crop tighter on mobile but keep the same studio lighting
- No art direction changes between breakpoints — the same visual language scales down
- Logo wordmark scales but never becomes icon-only

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Polestar Black (`#000000`) on white, or Polestar White (`#ffffff`) on dark
- Page Background: Polestar White (`#ffffff`)
- Alternate Section: Surface Mist (`#f4f4f4`)
- Primary Text: Polestar Black (`#000000`)
- Body Text: Body Gray (`#3d3d3d`)
- Caption Text: Caption Gray (`#6e6e6e`)
- Disabled Text: Disabled Gray (`#a8a8a8`)
- Hairline Border: `rgba(0, 0, 0, 0.12)`
- Solid Border: `#000000`
- Brand Accent: NONE — Polestar has no accent color

### Example Component Prompts
- "Create a hero section on Polestar White (`#ffffff`) with a headline at 96px Unica77 weight 400, line-height 1.00, letter-spacing -0.02em, color `#000000`. Use a Polestar Black (`#000000`) primary CTA — 14px Unica77 weight 400, sentence case, `2px` radius, no shadow, 14px 24px padding."
- "Design a car card on `#ffffff` with `4px` border-radius, no border, no shadow. Inside: full-width product render on `#f4f4f4` seamless background, then 24px padding with title at 24px Unica77 weight 400 and a single-line spec at 14px in `#3d3d3d`."
- "Build a full-bleed black hero section (`#000000`). Overlay text left-aligned: headline at 72px Unica77 weight 400 in pure white, body at 18px weight 400. Add an inverted primary CTA — `#ffffff` background, `#000000` text, `2px` radius, no shadow."
- "Create a hairline divider — full-width `1px solid rgba(0, 0, 0, 0.12)`. No spacing on the rule itself; let the surrounding sections supply 96–128px of vertical breathing room."
- "Design a spec block — large tabular figure at 48px Unica77 weight 400 with `tnum` enabled (e.g. '300'), then a 14px Unica77 caption directly beneath ('miles of range'). Stack vertically with 8px gap, left-aligned."
- "Build a newsletter input — `#ffffff` background, `1px solid rgba(0, 0, 0, 0.24)` resting border, `2px` radius, 14px 16px padding, 16px Unica77 weight 400 placeholder in `#a8a8a8`. Focus state: border darkens to `#000000` plus a `0 0 0 1px #000000` outer ring."

### Iteration Guide
1. Default to Unica77 weight 400 for every size — never reach for bold or light
2. Keep the page canvas pure `#ffffff` — never warm white, never off-white, never gradient
3. Refuse to introduce a brand accent color — the cars supply all the color
4. Never apply `box-shadow` — the system is flat by mandate; use 1px hairlines instead
5. Keep corner radius at `0–4px` — sharp is the brand voice
6. Use sentence case for every UI label — uppercase is forbidden
7. Negative tracking (`-0.02em`) at 56px+, normal at body — subtle but consistent
8. When in doubt, add whitespace, not chrome — emptiness is a deliberate tool
9. Photograph cars on flat seamless backgrounds — no environments, no scenery, no people
10. Hairline borders, tonal alternation, and full inversions are the only depth tools — there is nothing else
