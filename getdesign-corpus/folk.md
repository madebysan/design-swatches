# Design System Inspired by folk

## 1. Visual Theme & Atmosphere

folk's website is the **"Notion meets boutique stationery"** end of the CRM market. Where every relationship-tool site reaches for the same blue gradient and glassy device frame, folk presents a series of pastel-paneled chapters — each feature lives in its own colored room. Baby blue (`#bee0ef`) for the hero. Butter yellow for sales research. Mint green for outreach. Soft lilac and pink (`#fab9fb`) as accent stamps. The whole identity rests on the assumption that a CRM can feel like a paper magazine instead of a SaaS dashboard.

The custom **Uxum Grotesque** typeface is the locked-in display voice — weight 500 from 72px hero down through 16px UI, comfortable 1.10 line-height. A quiet, slightly humanist grotesk paired with **Founders Grotesk** for body and **Instrument Serif** for a single italic-flavored accent ("that *works* for your team"). That serif moment is the visual signature: every other heading is grotesk, except a single verb that slips into Instrument Serif. It reads as a designer's wink.

What sets folk apart structurally is its **pastel-panel scroll architecture**. Sections don't separate by white space — they separate by changing the entire background color. You scroll from blue, into white, into yellow, into green. Each panel houses one concept and one product screenshot rendered full-bleed inside a rounded white card. The border-radius scale confirms the soft-everything ethos: 12px on cards, 20px on badges, fully-pill `1000px+` on every CTA. Sharp corners are nowhere to be found.

**Key Characteristics:**
- Pastel-paneled chapter scrolling — each feature gets its own background color (blue, yellow, green, lilac)
- Uxum Grotesque weight 500 as the display voice; Instrument Serif as the italic-flavored editorial accent
- Founders Grotesk for body and CTA labels at 19.2px — generous, readable, slightly warm
- Fully-pill CTA buttons (`borderRadius: 1000px+`) — never sharp, never rounded-rect
- Off-black text (`rgba(3, 2, 0, 0.89)` — `#030200e3`) instead of pure black — softer, paper-like
- Highlight color `#fab9fb` (sugar pink) used sparingly as a stamp / underline accent
- Layered ambient drop shadows on hero cards — soft elevation, not graphic stamps
- Product screenshots presented full-bleed inside colored panels — the panel is the frame

## 2. Color Palette & Roles

### Primary
- **folk Off-Black** (`rgba(3, 2, 0, 0.89)` / `#030200e3`): The signature text color. **Never pure black.** Adds a warm, paper-printed feel. Used for all headings, body copy, and nav links.
- **folk White** (`#ffffff`): Default content surface, form inputs, alternating section backgrounds.
- **Pure Black** (`#000000`): Reserved for inverted CTA buttons and the "Premium" pricing tier card.

### Panel Backgrounds (the chapter system)
- **Sky Blue** (`#bee0ef`): Hero panel and "trust" sections. Set as `--bg-color` CSS variable. The brand canvas.
- **Butter Yellow** (`~#f5e9b8`): Sales research / data sections.
- **Mint Green** (`~#cde8d3`): Outreach / scale sections.
- **Pale Lilac** (`~#e8e0f0`): Email / data quality sections.
- **Soft Pink** (`~#f5d6dc`): Hero illustration backdrops and warm-feature panels.

*Each panel is a saturated-but-low-chroma pastel — never neon, never primary. They sit in the LCH 85–90% lightness band so type stays legible at full off-black weight.*

### Accent / Highlight
- **Highlight Pink** (`#fab9fb`): The signature accent, set as `--highlight-color`. Sugar pink used for inline text highlights, decorative underlines, and sticker-style stamps. **Used as a stamp, not a system color** — one or two appearances per screen.

### Neutrals & Borders
- **Border Off-Black** (`rgba(3, 2, 0, 0.89)`): 1px borders on inputs, cards, dividers — matches the off-black text for tonal cohesion.
- **Hard Black Border** (`rgb(0, 0, 0)`): 1px borders on pill buttons and stronger dividers.
- **Light Gray** (`#d4d4d4`): Pricing comparison row dividers, tertiary borders.
- **Footer Gray Text** (`rgba(5, 5, 0, 0.63)` / `rgba(10, 10, 0, 0.63)`): Muted body for footer/legal copy.

### Link States
- Default link: `rgba(3, 2, 0, 0.89)` with **underline always present** — folk does not hide its links.
- Hover link: `#1a1a1a` (slightly darker), underline retained.
- Tertiary link: `rgba(10, 10, 0, 0.63)` — for footer / fine print.

### Gradient System
- folk is **almost gradient-free**. The exception is one or two product screenshots that include subtle dark→teal vertical gradients inside their cards. The page chrome uses solid pastel fills only. **Do not introduce gradient backgrounds on panels** — the chapter system is solid-color by design.

## 3. Typography Rules

### Font Family
- **Display**: `Uxum Grotesque` — custom commercial typeface. Used for all headings at weight 500.
- **Body / UI**: `Founders Grotesk` weight 400 for body, links, button labels at 19.2px.
- **Editorial Accent**: `Instrument Serif` weight 400 — italic-flavored serif used for ONE word per hero ("works") and rare pull-quote moments. The single-word serif inside a grotesk headline is the signature.
- **Tertiary / fine print**: `Inter` weight 400 — small captions, legal, footer.

*Note: For external implementations without licenses, substitute Uxum Grotesque with **Söhne** or **Neue Haas Grotesk Display** at weight 500. Founders Grotesk has a free X-Condensed variant. Instrument Serif is free on Google Fonts.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Notes |
|------|------|------|--------|-------------|-------|
| Display Hero | Uxum Grotesque | 72px (4.50rem) | 500 | 1.10 | Hero headline — single line per breakpoint |
| Display Hero Serif | Instrument Serif | 64px (4.00rem) | 400 | 1.00 | Italic-feel verb embedded inside grotesk hero |
| Display Large | Uxum Grotesque | 64px (4.00rem) | 500 | 1.20 | Section opener heads |
| Display | Uxum Grotesque | 56px (3.50rem) | 500 | 1.10 | Feature panel titles |
| Section Heading | Uxum Grotesque | 48px (3.00rem) | 500 | 1.10 | Sub-feature heads, mid-page |
| Sub-heading Large | Uxum Grotesque | 40px (2.50rem) | 500 | 1.10 | Card titles, pricing tier names |
| Sub-heading | Uxum Grotesque | 24px (1.50rem) | 500 | 1.00 | Feature card heads, pricing rows |
| Title Bold | Uxum Grotesque | 20px (1.25rem) | 700 | 1.00 | Pricing tier emphasis, table headers |
| Body Large | Founders Grotesk | 19.2px (1.20rem) | 400 | 1.60 | Hero subhead, intro paragraphs, CTA labels |
| Body / Link | Inter | 16.8–19.2px | 400 | 1.60 | Standard body copy, in-flow links |
| UI / Caption | Inter | 14–16px | 400 | 1.60 | Card body, table cells, captions |
| Eyebrow | Uxum Grotesque | 13px (0.81rem) | 500 | 1.40 | UPPERCASE, `letter-spacing: 0.5px` — section labels |
| Micro Label | Uxum Grotesque | 9px (0.56rem) | 700 | 1.00 | UPPERCASE, `0.18px` tracking — tag chrome |

### Principles
- **Weight 500 is the display ceiling** — no 700+ headlines. Quiet weight, generous size.
- **Three-family stack with intent**: Uxum Grotesque for structure, Founders Grotesk for warmth, Instrument Serif for the editorial wink. Inter only at small sizes.
- **The single-serif-word trick**: hero mixes grotesk and serif in one phrase ("The CRM that *works*"). The serif word should always be a verb or modifier — never a noun.
- **Line-height stays tight (1.00–1.20)** on display; body relaxes to **1.60**.
- **No negative letter-spacing** — folk lets Uxum Grotesque breathe at its native tracking.
- **Uppercase only at micro sizes** (9–13px) with explicit `letter-spacing` (0.18–0.5px). Never uppercase at body size.

## 4. Component Stylings

### Buttons

**Primary Pill (Black)**
- Background: Pure Black (`#000000`)
- Text: White (`#ffffff`)
- Padding: 6px 12px compact, ~14px 28px standard
- Radius: `1000px+` (fully pill — confirmed `1920px` in extraction)
- Border: `1px solid #000`
- Font: Founders Grotesk 19.2px weight 400, mixed case
- Hover: background → `rgba(255, 255, 255, 0.85)`, text → `#000`, border retained
- Focus: `box-shadow: rgba(0, 0, 0, 0.12) 0px 0px 0px 2px`
- Use: Primary CTAs — "Start your 14-day free trial", "Sign up"

**Outline Pill (Light Sections)**
- Background: White or transparent
- Text: folk Off-Black (`rgba(3, 2, 0, 0.89)`)
- Border: `1px solid rgba(3, 2, 0, 0.89)`
- Radius: `1000px+`
- Use: Secondary CTAs on white/pastel panels — "Book a demo", "Learn more"

**Inverted Pill (Dark Pricing Card)**
- Background: White
- Text: Black
- Radius: `1000px+`
- Used inside the dark "Premium" pricing tier — inversion of the primary pill
- Use: CTA-on-black-card moments

**Floating Round Action**
- Size: ~56px × 56px
- Radius: `50%` (true circle)
- Background: Black
- Shadow: `rgba(0, 0, 0, 0.06) 0px 1px 6px, rgba(0, 0, 0, 0.16) 0px 2px 32px` (layered ambient)
- Hover: `transform: scale(1.1)` + lighter shadow
- Active: `transform: scale(0.85)` (squash feedback)
- Use: Intercom launcher, floating action — bottom-right anchored

### Cards & Containers

**Feature Panel Card**
- Background: White
- Border-radius: `12px`
- Border: optional `1px solid rgba(3, 2, 0, 0.89)` for definition against pastel backgrounds
- Shadow: `rgba(0, 0, 0, 0.08) 0px 5px 12px, rgba(0, 0, 0, 0.07) 0px 21px 21px, rgba(0, 0, 0, 0.04) 0px 48px 29px, rgba(0, 0, 0, 0.01) 0px 86px 34px`
- Internal padding: 24–48px
- Use: Product screenshot containers, testimonial cards, feature highlights

**Pricing Card**
- Standard: white background, `1px solid rgba(3, 2, 0, 0.89)`, `12px` radius, 32px padding. Header in Uxum Grotesque 24px weight 500.
- Premium (featured): inverts to black background with white text and white pill CTA. The middle "recommended" tier always inverts.

**Heavy White Border Card**
- Border: `10px solid #ffffff` — chunky inset frame around dark imagery, polaroid-style

### Badges / Tags / Pills
**Pill Tag**: `20px` radius, 4–6px / 10–12px padding, Uxum Grotesque 13px weight 500 (often UPPERCASE with `0.5px` letter-spacing), `1px solid rgba(3, 2, 0, 0.89)` outline or pastel-fill variant. Use for section eyebrows, category markers, integration tags.

**Dark Highlight Tag**: `20px` radius, pure black background, white text. Use for status indicators and "New" badges.

### Inputs & Forms
- Background: `rgba(255, 255, 255, 0.9)` default, solid `#ffffff` on focus
- Border: `1px solid rgba(3, 2, 0, 0.89)`
- Radius: `0px` (sharp rectangular — the one place folk goes sharp)
- Padding: 6.4px 8px (compact) or ~12px 16px (standard)
- Text: `rgba(3, 2, 0, 0.89)` weight 400
- Focus: border → `#000`, `box-shadow: rgba(0, 0, 0, 0.12) 0px 0px 0px 2px`, no outline
- Use: Email signup, demo-request forms

### Navigation
- Top nav: white horizontal bar, left-aligned wordmark logo (SVG), right-aligned nav links + black pill CTA
- Link color: `#222222` default, `#000` on hover with underline
- Font: Founders Grotesk 19.2px weight 400 (Inter for sub-nav at 16.8px)
- Mega-menu dropdowns drop from the top nav with multi-column layouts
- Sticky behavior: nav remains fixed; pastel panels scroll beneath

### Decorative Elements

- **Pastel Chapter Panel**: full-width section, solid pastel background (blue / yellow / green / lilac / pink), 112px vertical padding desktop. Holds an eyebrow tag, headline, subhead, and a product screenshot inside a 12px-radius white card.
- **Highlight Pink Stamp**: `#fab9fb` as a sticker — circular badges, hand-drawn underlines, single-word highlights. Never on CTAs or large surfaces.
- **Layered Ambient Shadow**: `0 5px 12px / 0 21px 21px / 0 48px 29px / 0 86px 34px` (descending opacity). The signature soft lift. No hard offsets, no rubber stamps.

## 5. Layout Principles

### Spacing System
- Base unit: 8px (with 4px sub-unit for tight UI chrome)
- Scale: 4px, 6.4px, 8px, 12px, 16px, 20px, 24px, 32px, 48px, 112px, 128px, 150px, 160px
- Notable: a **big jump from 48px to 112px** for section padding — folk skips the 64–96px middle zone. Sections are either tight-internal (24–48px) or chapter-spaced (112px+). No middle ground.

### Grid & Container
- Max content width: ~1200px centered on desktop
- Hero: full-width pastel panel with two-column (text left, illustration right) interior
- Feature panels: alternating layouts — text-left/screenshot-right, then text-right/screenshot-left
- Pricing: 3-column tier comparison with a stretched comparison table beneath
- Footer: 4-column link layout with email-capture form

### Whitespace Philosophy
- **Chapter pacing**: each pastel panel acts as a chapter break — color change does the work white space does on most sites
- **Generous internal padding**: 112px top/bottom on panels lets each section breathe inside its color
- **Tight type rhythm**: within a panel, headlines and body sit close (24–32px gaps) — the air is at the panel level, not between paragraphs

### Border Radius Scale
- Sharp (0px): Form inputs only — folk's one concession to data entry
- Card (12px): Product cards, pricing tiers, panel-internal containers
- Badge (20px): Pill tags, eyebrow markers, category labels
- Pill (1000–1920px): All CTA buttons — fully rounded
- Circle (50%): Floating action buttons, avatars

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page panels, body copy, structural containers |
| Soft Lift (Level 1) | `rgba(0, 0, 0, 0.06) 0px 1px 6px, rgba(0, 0, 0, 0.16) 0px 2px 32px` | Floating action buttons, tooltips |
| Ambient Card (Level 2) | `0 5px 12px rgba(0,0,0,.08), 0 21px 21px rgba(0,0,0,.07), 0 48px 29px rgba(0,0,0,.04), 0 86px 34px rgba(0,0,0,.01)` | Feature cards, product screenshots, hero containers |
| Soft Modal (Level 3) | `rgba(0, 0, 0, 0.06) 0px 20px 20px, 0px 2px 4px, 0px 10px 10px, 0px 2px 10px rgba(0, 0, 0, 0.2)` | Modals, dropdowns, popovers |
| Focus Ring (Level 4) | `rgba(0, 0, 0, 0.12) 0px 0px 0px 2px` | Keyboard focus on inputs and buttons |

**Shadow Philosophy**: folk's depth is **atmospheric**, not graphic. Where Cape uses hard rubber-stamp offsets, folk uses 3–4 layered soft drops with descending opacity. The signature is the four-layer cascade — 5px → 21px → 48px → 86px — physics-correct, not stylized. Cards hover on real paper, not pinned by a graphic stamp.

### Decorative Depth
- White inner-borders (`10px solid white`) act as physical matting — turning a screenshot into a polaroid-style object
- Pastel panels themselves are flat; depth lives only in the cards that sit on them

## 7. Do's and Don'ts

### Do
- Use Uxum Grotesque weight 500 for every heading from 24px upward — quiet weight, generous size
- Embed Instrument Serif on a single verb in the hero ("that *works* for") — the italic-grotesk pair is the brand signature
- Use the pastel panel system to mark chapter breaks — switch background color, not just spacing
- Apply pill radius (`1000px+`) on every CTA button — full pill, never rounded-rect
- Use off-black text (`rgba(3, 2, 0, 0.89)`) instead of pure black for warmth
- Use the four-layer ambient shadow on cards that need to lift off pastel panels
- Reserve `#fab9fb` highlight pink for sticker moments — one or two per screen
- Keep underlines visible on links by default — folk doesn't hide its hyperlinks
- Use `12px` card radius and `20px` badge radius — they're distinct, not interchangeable

### Don't
- Don't use pure black (`#000000`) for body text — always off-black (`rgba(3, 2, 0, 0.89)`)
- Don't use rounded-rect buttons (4–8px radius) — folk's CTAs are fully pill or fully circle
- Don't apply the highlight pink to large surfaces, CTAs, or backgrounds — it's a stamp accent only
- Don't use heavy weights (700+) on display headlines — weight 500 is the brand voice
- Don't introduce gradient panel backgrounds — chapters are solid-color by design
- Don't use hard offset shadows or rubber-stamp effects — folk's depth is atmospheric
- Don't pair Uxum Grotesque with another grotesk for body — Founders Grotesk and Inter are the locked partners
- Don't uppercase body or sub-heading text — uppercase only at 9–13px with explicit tracking
- Don't break the 1.60 body line-height — folk's editorial pacing depends on it

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <479px | Single column, hero drops to 36–40px, panels stack |
| Mobile | 479–767px | Single column, 48px hero, CTA pills full-width |
| Tablet | 768–991px | 2-column feature panels begin, 56–64px hero |
| Desktop | 991–1440px | Full multi-column, 64–72px hero, side-by-side feature pairs |
| Large Desktop | 1440–1920px+ | Maximum type scale (72px hero), 1200px content container |

### Touch Targets
- Pill CTAs: min 44px tap height, ~28px horizontal padding on mobile
- Floating action: 56px diameter (Intercom launcher pattern)
- Nav links: ~16px vertical padding for thumb navigation

### Collapsing Strategy
- **Nav**: horizontal links collapse to hamburger; full-screen menu opens with stacked links
- **Hero**: 72px → 48px → 36px progressive scaling; serif accent word retains its proportional size
- **Pastel panels**: vertical padding 112px → 64px → 48px, but color stays solid — chapters remain
- **Feature pairs**: 2-column screenshot+text → stacked single column, text always above screenshot
- **Pricing**: 3 columns → carousel or stacked cards with scroll-snap
- **Comparison table**: collapses to per-tier accordion lists below 768px
- **Footer**: 4 columns → 2 columns at 768px → 1 column at 479px

### Image Behavior
- Product screenshots stay full-bleed inside their panels at every breakpoint
- White inner-border framing scales 10px → 6px on mobile
- Pastel panel colors preserved at all breakpoints — never collapse to white

## 9. Agent Prompt Guide

### Quick Color Reference
- Hero Panel: Sky Blue (`#bee0ef`)
- Highlight Stamp: Sugar Pink (`#fab9fb`)
- Primary Text: folk Off-Black (`rgba(3, 2, 0, 0.89)` / `#030200e3`)
- CTA Background: Pure Black (`#000000`) on white/pastel; Pure White (`#ffffff`) on black-card pricing
- Card Background: White (`#ffffff`)
- Panel Backgrounds: Sky Blue / Butter Yellow / Mint Green / Pale Lilac / Soft Pink
- Border Color: `rgba(3, 2, 0, 0.89)` for soft, `#000000` for buttons
- Focus Ring: `rgba(0, 0, 0, 0.12) 0px 0px 0px 2px`
- Ambient Shadow: `0 5px 12px rgba(0,0,0,.08), 0 21px 21px rgba(0,0,0,.07), 0 48px 29px rgba(0,0,0,.04), 0 86px 34px rgba(0,0,0,.01)`

### Example Component Prompts
- "Create a hero section on Sky Blue (`#bee0ef`) with a 72px Uxum Grotesque weight 500 headline, line-height 1.10, color `rgba(3, 2, 0, 0.89)`. Set ONE word in Instrument Serif weight 400 at 64px italic-feel — the verb. Subhead in Founders Grotesk 19.2px weight 400, line-height 1.60. CTA: black pill (`borderRadius: 1000px`, `padding: 14px 28px`, white text in Founders Grotesk 19.2px weight 400, hover inverts to white background with black text)."
- "Build a feature panel on Butter Yellow background (full-bleed, 112px top/bottom padding). Inside: Uxum Grotesque 56px headline, 24px body, then a white card (`borderRadius: 12px`, no border, layered shadow `0 5px 12px / 0 21px 21px / 0 48px 29px / 0 86px 34px`) holding a product screenshot at full bleed."
- "Design a pricing tier card — white background, `1px solid rgba(3, 2, 0, 0.89)`, `12px` border-radius, 32px padding. Tier name in Uxum Grotesque 24px weight 500. Price in 40px weight 500. CTA pill at the bottom: outline style with off-black border. Recommended tier inverts: black background, white text, white pill CTA with black text."
- "Create a pill tag — `20px` border-radius, `1px solid rgba(3, 2, 0, 0.89)`, transparent background, Uxum Grotesque 13px weight 500 UPPERCASE with `0.5px` letter-spacing, padding 4px 10px."
- "Build a floating action button — 56px circle, `borderRadius: 50%`, black background, layered shadow `rgba(0, 0, 0, 0.06) 0px 1px 6px, rgba(0, 0, 0, 0.16) 0px 2px 32px`. Hover: `scale(1.1)` and lighter shadow. Active: `scale(0.85)` for squash feedback."

### Iteration Guide
1. Start with the panel system: divide the page into pastel chapters before placing components. Color changes mark sections; spacing alone is not enough.
2. Default to Uxum Grotesque weight 500 for display, Founders Grotesk weight 400 for body. Reach for Instrument Serif only on a single verb in the hero.
3. Keep all CTAs fully pill (`borderRadius: 1000px+`). Sharp form inputs (`0px`) are the one exception.
4. Use off-black `rgba(3, 2, 0, 0.89)` for text — pure `#000000` is for button backgrounds and the featured pricing card only.
5. The four-layer ambient shadow is the only depth treatment — no hard offsets, no graphic stamps.
6. Highlight pink `#fab9fb` is a stamp accent — one or two appearances per screen, never on CTAs or panel backgrounds.
7. Underlines stay visible on links. Body line-height stays at 1.60. Display line-height stays at 1.00–1.20.
8. Section padding jumps from 48px (internal) straight to 112px (chapter breaks) — skip the 64–96px middle zone.
