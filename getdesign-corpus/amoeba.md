---
slug: amoeba
name: Amoeba Music
url: https://www.amoeba.com
domain: amoeba.com
category: Retail
styles: [Bold, Tactile, Editorial]
tagline: "Hi-vis sticker yellow on black, LasVegasOTJackpot display, dotted underlines and 6px chunky sleeve corners."
fonts: [LasVegasOTJackpot, BurbankBigMedium]
primary_color: "#fff200"
---

# Design System Inspired by Amoeba Music

> Hi-vis sticker yellow on black, LasVegasOTJackpot display, dotted underlines and 6px chunky sleeve corners.

## 1. Visual Theme & Atmosphere

Amoeba.com is the homepage equivalent of an actual record-store wall — overstuffed, hand-priced, and proud of it. The site refuses every chrome convention of modern e-commerce: no frosted hero, no soft shadows, no whitespace as a luxury signal. The page is a kraft-board collage of black panels (`#000000`), pure-white inserts (`#ffffff`), and a single high-vis sticker yellow (`#fff200`) doing the work of a price tag, neon sign, and warning stripe at once. There is no gradient anywhere. The atmosphere is independent-record-store, 1990s flyer wall, deep-fried-by-the-sun-on-Sunset-Blvd.

The typographic signature is **LasVegasOTJackpot at 30–38px for the page H1s** — a chunky display face that reads like a casino marquee filtered through a photocopier. Below it, **BurbankBigMedium uppercase** carries the link/nav voice (18px, all-caps, weight 400) — a comic-book sans that screams "vinyl crate label." Body text falls back to Verdana and Arial 11–16px. There is no custom UI sans, no variable font, no Inter, no Helvetica. The two display faces ARE the brand — everything else is plain web type from the early-2000s playbook.

What makes Amoeba feel *unmistakably tactile* is the **dotted-underline link convention** and the **black drop-shadows on every yellow button**. Links use `border-bottom: 1px dotted #404040` instead of the standard underline — a typewriter-receipt cue that no other major retailer uses. Buttons sit on `rgb(102, 102, 102) 1px 1px 3px 0px` shadows — sharp 1px black drops, not soft Material lifts. The 6px border radius on cards and tabs is the workhorse — chunky enough to feel like a sleeve corner, sharp enough not to feel "designed." Combined with the red `#ed1c24` 1px borders that wrap genre lists, the page feels stickered, taped, and Sharpie-priced rather than rendered.

**Key Characteristics:**
- LasVegasOTJackpot at 30–38px for page H1s — chunky photocopied marquee display
- BurbankBigMedium uppercase at 18px for nav/links — comic-book grotesk in all-caps
- Sticker Yellow (`#fff200`) on Black (`#000000`) — the page's only chromatic conversation
- Yellow CTA buttons with `1px solid #ffffff` borders and `1px 1px 3px` black drop shadows
- Dotted-underline links — `border-bottom: 1px dotted rgb(64, 64, 64)`, 23 instances on the homepage
- Red border accent (`#ed1c24`) — 1px solid borders wrapping genre lists, 12 occurrences
- 6px workhorse border radius — 45 instances; 5px for `<ul>`, 10px for `<a>`, 50% for one circle
- Hard-edged drop shadows: `rgb(102, 102, 102) 0px 0px 4px 0px` and `rgb(0, 0, 0) 2px 2px 6px 0px`
- Inset retro borders — `2px inset rgb(118, 118, 118)` on inputs, signaling 90s OS chrome
- Scale-skewed-compact spacing: 2/3/4/5/7/10/11/13px values dominate

## 2. Color Palette & Roles

### Primary Brand
- **Sticker Yellow** (`#fff200`): The brand-defining accent. Used on every primary CTA fill, the wordmark backplate, sale badges, and yellow-link surfaces. Hi-vis pure yellow — no warm cream, no mustard. This is the parking-lot-cone yellow of an actual Amoeba sleeve sticker.
- **Hover Yellow** (`#ffd200`): The hover/active variant — a single-step warmer yellow used for `:hover` on yellow CTAs. The shift is small but the page is so saturated already that even one hue-step lands.
- **Amoeba Black** (`#000000`): Pure black, used as the page-anchor surface for navs, tab-bar fills, and bold panel backdrops. Never softened to `#222` — Amoeba uses the actual ink.

### Brand Accent
- **Vinyl-Sleeve Red** (`#ed1c24`): The 1px border color that wraps genre lists and category lists. Twelve occurrences on the homepage. A blood-red signal flag, not a CTA color — used purely as a chrome accent on `<ul>` borders.
- **Marquee White** (`#ffffff`): Pure white — used as content surface, button border, and text-on-black. The white is doing both "negative space" and "active surface" duty.

### Text
- **Amoeba Black** (`#000000`): Primary text on yellow and white surfaces. The page's default ink.
- **Charcoal Slate** (`#404040`): Secondary text and dotted-underline color — `27% lightness` LCH gray. Used for caption text and the dotted-link border-bottom.
- **Mid Gray** (`#7c7e7d`): Tertiary text, divider hairlines, muted form labels.
- **Border Gray** (`#c1c1c1`): 1px solid border on `<textarea>` — the only soft-gray border in the system.

### Surface
- **Amoeba Black** (`#000000`): Top nav, footer, hero panels — the page's structural ink.
- **Marquee White** (`#ffffff`): Editorial content surface, card fills, tab panels.
- **Inset Wash** (`rgb(118, 118, 118)`): The 2px inset border color on `<input>` fields — a deliberate retro 90s-OS chrome.

### Status & Highlight
- **Sticker Yellow** (`#fff200`): Doubles as the highlight/sale color. There is no separate "on-sale" tint.
- **Vinyl-Sleeve Red** (`#ed1c24`): The only red on the site — not a CTA, just a list-border accent.

### Gradient System
- Amoeba is **gradient-free**. There is not a single gradient on the homepage. All depth comes from solid-color blocks, 1px dotted borders, and hard-edged drop shadows. The visual "gradient" is the implicit one created by black backdrops cradling yellow sticker buttons cradling white-bordered inserts.

## 3. Typography Rules

### Font Family
- **Display**: `LasVegasOTJackpot`, fallback: `Verdana`, `Geneva`. The chunky photocopied-marquee face used for every page H1 from 30–38px.
- **UI / Link**: `BurbankBigMedium`, fallback: `Verdana`, `Geneva`. Comic-book grotesk used for nav, link labels, and uppercase chrome at 11–18px.
- **Body**: `Verdana`, fallback: `Geneva`, `sans-serif`. The classic web sans for body copy at 11–16px.
- **Body alt**: `Arial`, fallback: `Helvetica`. Used for `<caption>` runs at 12–14px in weights 400 and 700.
- **Times** (`Times`): A single 16px H1 occurrence — likely a CMS default escaping the design system. Treat as an anti-pattern.

*Note: LasVegasOTJackpot is a custom Amoeba typeface; for external implementations, **Lobster** or **Limelight** approximate the chunky-marquee feel. For BurbankBigMedium, **Bebas Neue** or **Anton** in uppercase serve as substitutes. Body should fall back to **Verdana** for the workhorse 1996-internet feel — do not sub Inter.*

### Hierarchy

| Role | Font | Size | Weight | Transform | Notes |
|------|------|------|--------|-----------|-------|
| Page H1 (XL) | LasVegasOTJackpot | 38px (2.38rem) | 400 | none | The biggest moment — section anchors, "Vinyl", "Now Playing" |
| Page H1 (L) | LasVegasOTJackpot | 30px (1.88rem) | 400 | none | Secondary section heads |
| H1 / CMS Default | Verdana / Times | 16px (1rem) | 400 | none | Fallback CMS heading — the system breaks here, treat as a one-off |
| Nav Link | BurbankBigMedium | 18px (1.13rem) | 400 | uppercase | The primary nav link voice — chunky grotesk in caps |
| Link Inline | BurbankBigMedium | 18px / 16px | 400 | none | Title-cased link variant |
| Body Link | Verdana | 16px (1rem) | 400 | none | Body-copy link in workhorse sans |
| Body | Verdana | 16px (1rem) | 400 | none | Standard reading body |
| Bold Body | BurbankBigMedium | 16px (1rem) | 700 | none | Emphasized track titles, "now playing" labels |
| Eyebrow Caption | BurbankBigMedium | 14px (0.88rem) | 400 | uppercase | Genre tag eyebrows above album rows |
| Bold Caption | Arial | 14px (0.88rem) | 700 | none | Emphasized inline caption |
| Caption | Arial | 12px (0.75rem) | 400 | none | Standard metadata, byline |
| Micro Bold | Verdana | 11px (0.69rem) | 700 | none | Track counts, "supported by" |
| Micro | Verdana | 11px (0.69rem) | 400 | none | Footer microcopy, legal text |

### Principles
- **Two custom display faces, two fallback bodies.** LasVegasOTJackpot for H1s, BurbankBigMedium for nav/links — these two carry the brand voice. Verdana and Arial do all the body and caption work.
- **No line-height in the data.** The system relies on browser defaults — about 1.20 for body, 1.10 for headlines. There is no explicit leading control, which contributes to the "raw web 2002" feel.
- **No letter-spacing.** Every typography rule omits `letter-spacing` — type runs at default tracking, even at 11px micro sizes. This is part of why the page reads "unstyled" in a deliberate way.
- **Uppercase as a structural cue.** BurbankBigMedium uppercase at 18px is the nav voice; uppercase 14px Burbank is the eyebrow voice. Title case appears almost exclusively in body.
- **Sub-1rem sizes everywhere.** Most utility text lands at 11px or 12px — Amoeba does not pad chrome with 14px+ "comfortable" sizes. The page is dense by 2024 standards.

## 4. Component Stylings

### Buttons

**Primary — Yellow Sticker**
- Background: Sticker Yellow (`#ffd300`) — note: the live variant uses `#ffd300` for buttons, not the brighter `#fff200` of the wordmark
- Text: Amoeba Black (`#000000`)
- Padding: `2px 8px`
- Radius: `6px`
- Border: `1px solid #ffffff`
- Shadow: `rgb(102, 102, 102) 1px 1px 3px 0px` — sharp 1px gray drop
- Outline (focus): `3px` outline (defaults to black, not yellow)
- Font: 7–14px, weight 400 (yes — the on-page yellow sticker buttons run as small as 7px in the data; treat 12–14px as the safe minimum for new work)
- Hover: background shifts to `#ffd200` (single-step warmer)
- Use: All primary CTAs — "Buy", "Add to Cart", "Shop Now"

**Tab Button — White on Black**
- Background: Pure White (`#ffffff`)
- Text: Amoeba Black (`#000000`)
- Padding: `11px`
- Radius: `0px 0px 6px 6px` — bottom-only chunky corners (sleeve-edge cue)
- Border: `0px none`
- Shadow: `rgb(0, 0, 0) 2px 2px 6px 0px` — hard 2px black drop
- Font: 16px Verdana / BurbankBigMedium weight 400
- Use: Tab panels — "New Releases", "Vinyl", "Used"

**Black Outline (Inverse)**
- Background: `rgb(255, 255, 255)`
- Text: `rgb(0, 0, 0)`
- Border: `2px solid #ffffff` on dark; `1px solid #ffffff` on yellow
- Radius: `6px` or `3px`
- Shadow: `rgb(0, 0, 0) 1px 1px 1px 0px`
- Use: Secondary CTAs, "Sign Up", "More Info"

### Cards & Containers

- Background: `#ffffff` (default content) or `#000000` (anchor panels)
- Border: `1px solid #ed1c24` (red sleeve-frame on `<ul>` genre lists), `1px solid #ffffff` on dark, or `0` for default cards
- Radius: `6px` (workhorse), `5px` for `<ul>`, `10px` for `<a>`, `2px` for `<span>` badges, `0px 0px 6px 6px` for tab panels (bottom-only chunky)
- Shadow: `rgb(102, 102, 102) 0px 0px 4px 0px` for the standard panel lift; `rgb(0, 0, 0) 2px 2px 6px 0px` for hard-edged "stickered" drops
- Internal padding: tight — 2/4/8/11/13px values dominate. There is no 24px or 32px luxury padding here.

### Badges / Tags / Pills

**Yellow Sticker Badge**
- Background: `#ffd300`
- Text: `#000000`
- Border: `1px solid #ffffff`
- Radius: `2px` (small, pill-square hybrid)
- Font: 11px BurbankBigMedium weight 700
- Use: "On Sale", "Used", price stickers

**Red Border Tag**
- Background: `#ffffff`
- Text: `#000000`
- Border: `1px solid #ed1c24`
- Radius: `5px`
- Font: 12px Verdana weight 400
- Use: Genre list framing, category chips

### Inputs & Forms

**Text Input (Retro Inset)**
- Background: `#ffffff`
- Text: `#000000`
- Border: `2px inset rgb(118, 118, 118)` — a deliberate retro inset, 14 instances
- Radius: `0` (browser default)
- Padding: ~5px 8px
- Font: 13–14px Verdana
- Use: Search, email, account fields — the inset border is sacred 90s-chrome cue

**Textarea**
- Background: `#ffffff`
- Border: `1px solid #c1c1c1`
- Radius: `3px`
- Padding: 8–12px
- Font: 14px Arial weight 400

**Select**
- Background: `#ffffff`
- Border: `1px solid rgb(118, 118, 118)`
- Radius: `0`
- Padding: 4–6px

### Navigation

- Top nav: black `#000000` bar, ~48–56px tall, white wordmark left, BurbankBigMedium uppercase 18px nav links centered
- Link hover: white text shifts to yellow `#fff200`
- Bottom border: `1px solid rgb(64, 64, 64)` dotted — the same dotted convention as inline links
- Sticky: nav stays pinned on scroll
- Sub-nav: yellow strip with black uppercase BurbankBigMedium links, 14–16px

### Links (Distinctive)

- Default: `#000000` text with `border-bottom: 1px dotted rgb(64, 64, 64)` — NOT `text-decoration: underline`. This is the Amoeba signature.
- Hover: text shifts to yellow `#fff200`, dotted border stays
- Yellow links on black: text `#fff200`, no border, hover white `#ffffff`
- White links on black: text `#ffffff`, hover yellow `#fff200`

### Decorative Elements

**Wordmark / Logo**
- "Amoeba" displayed in custom hand-lettering logotype on yellow `#fff200` plate
- Sized roughly 120–180px wide depending on viewport
- Always on yellow — the brand identity is the yellow chip

**Price Sticker**
- Yellow `#ffd300` filled rectangle with 1px white border
- 6px radius
- Black BurbankBigMedium 700 caps inside
- Hard 1px gray drop shadow — looks pasted on

## 5. Layout Principles

### Spacing System
- Base unit: nominal 8px, but Amoeba uses a sub-grid heavily: 2/3/4/5/7/10/11/13/15/17px
- Scale: 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17, 19, 20, 22, 30px
- Notable: The scale skews extremely compact. 2px is the most-used spacing value (67 occurrences). Most inline padding lands between 2–13px. Generous values (20px+) only appear in section spacing.

### Grid & Container
- No declared breakpoints in the extracted data — Amoeba's site uses fixed-width containers around `~1024–1200px`
- Album-cover grids: 4–6 columns desktop, 3 columns tablet, 2 columns mobile
- Genre list rails: dense vertical stacks with 1px red sleeve-frame borders
- Side-by-side panel layouts dominate over single-column scroll

### Whitespace Philosophy
- **Density-first, sticker-collage chrome.** Sections butt against each other with 8–13px between rows and 20–30px between major panels. The page is not "calm" — it is a flyer wall.
- **Black/white panel alternation.** Sections alternate black-anchored and white-anchored, with yellow sticker buttons crossing the boundary as the visual hinge.
- **No editorial breathing room.** There are no 80px+ section gutters. Amoeba does not space-as-luxury; the density IS the personality.

### Border Radius Scale
- Sharp (0px): Inputs, default elements
- Tight (2–3px): Span badges, buttons (small)
- Compact (5–6px): The workhorse — cards, buttons, tabs, list rails (45 instances at 6px alone)
- Mid (10px): Anchor / link wrappers
- Half-rounded (`6px 6px 0px 0px` or `0px 0px 6px 6px`): Tab panels — top-only or bottom-only corners signaling "this is a sleeve edge"
- Pill (50%): One isolated circular button — likely the "play" affordance

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, 0px border | Default content surfaces |
| Sticker Lift (Level 1) | `rgb(102, 102, 102) 0px 0px 4px 0px` (18 instances) | Yellow CTA buttons, sticker badges |
| Hard Drop (Level 2) | `rgb(102, 102, 102) 1px 1px 3px 0px` (11 instances) | Tab buttons, sticker chips |
| Inkwell (Level 3) | `rgb(0, 0, 0) 1px 1px 1px 0px` (10 instances) | Hard-edged contrast drops on yellow surfaces |
| Heavy Drop (Level 4) | `rgb(0, 0, 0) 2px 2px 6px 0px` (7 instances) | Tab panels, white insets on black |
| Inset Punch (Level 5) | `rgba(0, 0, 0, 0.3) 2px 2px 2px -1px inset` (4 instances) | Pressed state on buttons, retro chrome |
| Outline Focus (Level 6) | `rgb(0, 0, 0) none 3px` outline | Keyboard focus on interactive elements |

**Shadow Philosophy**: Amoeba's depth system is **hard-edged and pasted-on**. Where modern design uses soft 0.05–0.10 opacity blurs to suggest physics, Amoeba uses 1–2px gray and black drops at 100% opacity that look like the elements were photocopied and taped to the page. There is no diffused Material-style shadow. The page is uniformly hard-cut — nothing floats softly, everything is stuck flat against the surface beneath it.

### Decorative Depth
- The dotted-underline links create their own micro-depth — a perforated edge that reads as "physically detached from the page"
- The 2px inset borders on inputs deliberately evoke 90s OS chrome — a system control, not a designed object
- The 6px sleeve-corner radius on tab panels (`0px 0px 6px 6px`) signals "this is a record-sleeve flap, not a card"
- No glow, blur, or atmospheric effects — Amoeba is all hard edges

## 7. Do's and Don'ts

### Do
- Use Sticker Yellow (`#fff200`) for the wordmark/logo and `#ffd300` for button fills — both belong to the system
- Pair yellow CTAs with `1px solid #ffffff` borders and a `1px 1px 3px` gray drop shadow
- Use LasVegasOTJackpot at 30–38px for page H1s — chunky display is the voice
- Use BurbankBigMedium uppercase at 18px for nav links and 14px for eyebrows
- Style links with `border-bottom: 1px dotted rgb(64, 64, 64)` — never `text-decoration: underline`
- Wrap genre lists in `1px solid #ed1c24` red borders — this is the sleeve-frame cue
- Use 6px border-radius on cards, 5px on `<ul>`, 10px on `<a>` — and `0px 0px 6px 6px` for tab panels
- Pack density — 8–13px row spacing, 20–30px section spacing, no 80px luxuries
- Use hard 1–2px drop shadows in solid colors, never blurred 24px Material lifts

### Don't
- Don't soften the yellow to mustard, gold, or amber — Amoeba yellow is hi-vis pure (`#fff200` / `#ffd300`)
- Don't use solid `text-decoration: underline` on links — Amoeba uses dotted borders, not underlines
- Don't introduce new chromatic colors beyond yellow, red, black, white — the palette is locked at four
- Don't use blurred drop shadows or diffused glow effects — the system is hard-cut, photocopier-flat
- Don't use Inter, Helvetica Neue, or any modern grotesk for body — Verdana and Arial are the workhorse
- Don't add 24–32px luxury padding around buttons — Amoeba CTAs are tight (`2px 8px` to `11px`)
- Don't alphabetize, normalize, or "modernize" the type scale — the 7px / 11px / 12px / 14px / 18px chunky jumps are intentional
- Don't use sentence-case for nav — nav is BurbankBigMedium UPPERCASE
- Don't redesign the dotted underline. It is the brand.

## 8. Responsive Behavior

### Breakpoints
The extracted data shows no declared breakpoints — Amoeba's site uses implicit fixed-width layouts. The estimated responsive behavior:

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single-column rails, 2-col album grid, stacked nav |
| Tablet | 640–1024px | 3–4 col album grid, condensed BurbankBigMedium nav |
| Desktop | 1024px+ | Full multi-column layout, fixed-width container ~1100–1200px |
| Large Desktop | ≥1280px | Container caps; outer margins absorb extra width |

### Touch Targets
- Yellow CTA buttons: ~32–40px tall — below modern WCAG AAA but in line with the dense web-2003 aesthetic
- Nav links: ~36–44px tap area through line-height and padding
- Tab buttons: 11px padding gives ~36–44px tap height

### Collapsing Strategy
- Nav: BurbankBigMedium uppercase nav collapses to a hamburger on mobile
- Album grids: 6-col → 4-col → 3-col → 2-col progression
- Genre lists: stack vertically below 768px
- Type scale: 38px → 30px → ~24px progressive heading scale

### Image Behavior
- Album covers: square aspect, lazy-loaded
- Hero banners: 16:9 with hard 6px corners
- Sticker artwork: yellow rectangles with 1px white border — preserved at all sizes

## 9. Agent Prompt Guide

### Quick Color Reference
- Sticker Yellow: `#fff200` (logo plate)
- Button Yellow: `#ffd300` (CTA fill)
- Hover Yellow: `#ffd200` (one-step warmer)
- Black: `#000000`
- White: `#ffffff`
- Vinyl-Sleeve Red: `#ed1c24` (genre list borders only)
- Charcoal Slate: `#404040` (dotted-link border-bottom)
- Mid Gray: `#7c7e7d`
- Inset Border: `rgb(118, 118, 118)`

### Example Component Prompts

1. *"Create a primary yellow CTA: `#ffd300` background, `#000000` text in BurbankBigMedium uppercase 14px weight 700, `2px 8px` padding, `6px` border-radius, `1px solid #ffffff` border, drop shadow `rgb(102, 102, 102) 1px 1px 3px 0px`. Hover background shifts to `#ffd200`."*

2. *"Build the page H1: LasVegasOTJackpot at 38px weight 400 in `#000000` on white, or `#fff200` on black. No letter-spacing, default line-height. Below it, place a BurbankBigMedium uppercase 14px eyebrow caption."*

3. *"Style a body link: `#000000` text with `border-bottom: 1px dotted rgb(64, 64, 64)`. On hover, text shifts to `#fff200`, dotted border stays. Do NOT use `text-decoration: underline` — Amoeba uses dotted borders."*

4. *"Create a genre list: `<ul>` with `1px solid #ed1c24` border, `5px` border-radius, white background. Each `<li>` is BurbankBigMedium uppercase 14px in `#000000` with `border-bottom: 1px dotted #404040` between items."*

5. *"Build a tab panel: white `#ffffff` content surface with `0px 0px 6px 6px` border-radius (bottom-only chunky corners), `rgb(0, 0, 0) 2px 2px 6px 0px` drop shadow. Tab labels in 16px BurbankBigMedium weight 400."*

6. *"Style a retro text input: `#ffffff` background, `2px inset rgb(118, 118, 118)` border, no border-radius, ~5px 8px padding, 13px Verdana text. The inset is mandatory — modern flat inputs break the voice."*

### Iteration Guide

1. **Audit the yellow.** Buttons are `#ffd300`, the wordmark is `#fff200`. If you see `#ffeb3b`, `#fffd54`, or any other yellow, correct it.
2. **Audit link decoration.** Every text link should have `border-bottom: 1px dotted rgb(64, 64, 64)`. If you see `text-decoration: underline`, replace it.
3. **Audit display type.** Page H1s should be LasVegasOTJackpot at 30–38px. Nav links should be BurbankBigMedium uppercase 18px. If you see Inter, Helvetica Neue, or Lato, correct it.
4. **Audit drop shadows.** Shadows should be hard-edged 1–2px solid-color drops. If you see `0 4px 24px rgba(0,0,0,0.05)` Material-style blurs, replace them with `1px 1px 3px rgb(102, 102, 102)`.
5. **Audit spacing.** If you see 24px or 32px luxury padding around buttons or rows, tighten to 2/4/8/11px. Amoeba is dense, not airy.
6. **Audit color sprawl.** Only yellow, red, black, white, and the declared grays should appear. No blue, no green, no purple — and especially no gradients.
7. **Audit border style.** Genre lists wrap in `1px solid #ed1c24`. Inputs have `2px inset` borders. If you see `1px solid #e5e5e5`, replace with the correct retro/sleeve-frame value.
8. **Audit casing.** Nav and eyebrow labels are UPPERCASE in BurbankBigMedium. Body is title or sentence case. If you see lowercase nav, fix it.
9. **When in doubt, ask: "would this fit on a Sunset Blvd flyer wall in 2003?"** If yes, ship it. If it screams "redesigned in 2024," reconsider.
