# Design System Inspired by Readwise / Reader

## 1. Visual Theme & Atmosphere

Readwise Reader is what happens when a reading app is designed by people who actually love books. The interface rejects the cold, blue-tinted sterility of most read-later tools and opts instead for a warm cream canvas (`#f8f4ed`) that feels less like a screen and more like the opened page of a hardback — a surface that acknowledges the eye has to spend hours here and responds with literal warmth. Every pixel is tuned for long-form ergonomics: comfortable measure, relaxed line-height, and a serif body that makes 5,000-word essays a pleasure rather than a chore.

The signature move is typographic allegiance to the serif. Where the industry default for productivity tools is a neutral sans (Inter, SF Pro, the usual suspects), Readwise commits to **Source Serif 4** — and later, Charter — for the reading surface itself. Headlines carry the gravitas of a book title; body copy has the cadence of an essay. The sans-serif (Inter) is demoted to UI chrome duty: sidebar labels, filter chips, button text. The hierarchy is unmistakable: **serif is for content, sans is for controls**. This small inversion is what makes Reader feel less like an app you tolerate and more like a reading room you inhabit.

What ties it together is a paper-like depth system that never tries to be glossy. Shadows are diffuse and amber-tinted (`rgba(45, 30, 15, 0.06)`), radii stay restrained between 6 and 10 pixels (anything more would feel app-y, anything less would feel chart-y), and the single saturated accent — a warm amber gold (`#c19a3d`) — stands in for the physical highlighter marks a reader would leave on a real page. Quotes sit on pale cream cards with a thin left rule, as if torn from the margins of a book and taped into a commonplace book. The result is a visual language that says: this is not a feed, this is not a dashboard, this is a place you come to read.

**Key Characteristics:**
- Warm cream canvas (`#f8f4ed`) evoking book paper — never pure white
- Source Serif 4 for display and body; Inter reserved for UI chrome
- Amber/gold accent (`#c19a3d`) standing in for literal highlighter strokes
- Restrained 6–10px radii — readable, not toy-like
- Paper-shadow depth: diffuse, amber-tinted, low-opacity
- Highlight cards with left-rule indent — commonplace-book DNA
- Warm dark "candle" mode for evening reading — never cold black
- Reading-ergonomic measure (62–72ch) with generous 1.65 body line-height

## 2. Color Palette & Roles

### Primary
- **Cream Paper** (`#f8f4ed`): The canonical page surface. A warm off-white with yellow-green undertone that reads unmistakably as paper rather than screen. Used for the main reading canvas and the majority of light surfaces.
- **Parchment** (`#f2ece0`): One tone darker — used for sidebar panels, subtle section dividers, and elevated-from-below containers.
- **Ink Black** (`#1c1813`): Primary body and heading ink. Never pure `#000000` — always carries a faint brown undertone, the color of pressed India ink on warm stock.

### Brand Accent
- **Amber Gold** (`#c19a3d`): The signature accent — borrowed from highlighter pens and brass bookmark clasps. Used for primary CTAs, active states, the literal highlight marker, and the hairline rule on pull quotes.
- **Amber Warm** (`#d4b15a`): A lighter variant for hover states and tinted highlight backgrounds (`rgba(193, 154, 61, 0.18)`).
- **Terracotta** (`#b85c3e`): Secondary warm accent used sparingly for annotations, tags, and error-adjacent moments. Borrowed from book cloth binding.

### Neutrals & Text
- **Ink Black** (`#1c1813`): Primary heading and body text on light surfaces.
- **Warm Graphite** (`#3d3530`): Secondary text — subheads, key labels. Think pencil-on-paper.
- **Warm Gray** (`#6b6258`): Tertiary text — metadata, timestamps, reading-time estimates.
- **Muted Stone** (`#9a9086`): Quaternary text — footnotes, disabled states, UI hints.
- **Ash** (`#c7bfb3`): Dividers, hairlines, faint borders between list items.

### Surface & Borders
- **Cream Paper** (`#f8f4ed`): Canvas.
- **Parchment** (`#f2ece0`): Elevated panels, sidebar, modal scrim.
- **Linen** (`#e8dfd0`): Hover surface for list items; subtly darker than parchment.
- **Border Cream** (`#e0d6c3`): Standard hairline border on cards and list dividers.
- **Border Warm** (`#d4c9b3`): Emphasized border for active cards and focused inputs.

### Dark Reader ("Candle" Mode)
- **Candle Dark** (`#1a1613`): Dark-reader canvas — warm near-black, the color of a lamplit room after dusk. Never `#000000`.
- **Candle Surface** (`#26201a`): Elevated panels on dark.
- **Candle Border** (`#3a3128`): Dark-mode hairlines.
- **Parchment Text** (`#e8dfd0`): Body text on dark — warm off-white, not stark.
- **Warm Silver** (`#b8ac9a`): Secondary dark-mode text.
- **Amber on Dark** (`#d4b15a`): Brand accent shifts to the lighter amber on dark surfaces for contrast.

### Semantic
- **Highlight Yellow** (`rgba(193, 154, 61, 0.22)`): The literal highlighter swipe on reading text.
- **Highlight Blue** (`rgba(88, 130, 166, 0.18)`): Secondary highlight color for shared notes.
- **Success Moss** (`#6b8e4e`): Confirmed states — moss green rather than spring green, staying within the muted earth palette.
- **Error Rust** (`#a0472c`): Error states — rust rather than red, consistent with the warm palette.

### Gradient System
Gradients are nearly absent. The only gradient work happens in the hero atmosphere — a radial cream-to-parchment (`radial-gradient(circle, #f8f4ed 0%, #f2ece0 70%)`) that mimics the faint vignette of book paper under a reading lamp. No tech-blue gradients, no neon, no animated shimmer. The palette is earthy and the treatment is flat-with-warmth.

## 3. Typography Rules

### Font Family
- **Reading & Display**: `Source Serif 4`, with fallbacks `Charter`, `Georgia`, `"Times New Roman"`, `serif`
- **Alternate Serif**: `Charter` (observed in Dembrandt data at 24px weight 600) — used interchangeably for body reading type; a slab-like transitional serif that renders cleanly at small sizes.
- **UI Chrome**: `Inter`, with fallbacks `-apple-system`, `BlinkMacSystemFont`, `"Segoe UI"`, `system-ui`, `sans-serif`
- **Monospace**: `"iA Writer Mono"`, fallback `"SF Mono"`, `Menlo`, `ui-monospace`, `monospace` — used exclusively for code blocks inside articles.

*Note: Source Serif 4 is Adobe's open-source transitional serif, available via Google Fonts. Charter is a bundled system serif on macOS. The combination is deliberate — Source Serif for display and rendered-to-screen body, Charter as a performant fallback that matches the rhythm.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display / Hero | Source Serif 4 | 58px (3.63rem) | 600 | 1.15 | -1.16px | Landing hero — book-title presence |
| Article Title (H1) | Source Serif 4 | 40px (2.50rem) | 600 | 1.15 | -0.4px | Opening headline of an article |
| Section Heading (H2) | Source Serif 4 | 28px (1.75rem) | 600 | 1.25 | -0.28px | In-article section anchors |
| Sub-heading (H3) | Source Serif 4 | 22px (1.38rem) | 600 | 1.30 | -0.22px | Minor section marks, card titles |
| Pull Quote | Source Serif 4 | 24px (1.50rem) | 400 italic | 1.45 | -0.24px | Block quotes — italic invocation |
| Body Reading | Source Serif 4 | 19px (1.19rem) | 400 | 1.65 | normal | The long-form reading size — relaxed and generous |
| Body Compact | Source Serif 4 | 16px (1.00rem) | 400 | 1.60 | normal | Article previews, feed descriptions |
| Highlight Text | Source Serif 4 | 17px (1.06rem) | 400 | 1.55 | normal | Saved highlights, daily review |
| UI Label | Inter | 13px (0.81rem) | 500 | 1.40 | 0.02em | Sidebar items, filter chips |
| UI Button | Inter | 14px (0.88rem) | 500 | 1.00 | 0.01em | Button text, tabs |
| Caption | Inter | 12px (0.75rem) | 400 | 1.50 | 0.04em | Metadata — reading time, source domain |
| Overline | Inter | 11px (0.69rem) | 600 | 1.20 | 0.12em | Uppercase category labels |

### Principles
- **Serif carries the content, sans carries the controls**: Every piece of text the reader is meant to *read* uses Source Serif 4. Every piece of text the reader is meant to *operate* uses Inter. This is the single most important typographic rule.
- **No display-weight serif**: Headlines use weight 600, not 700. The serif letterforms have enough inherent weight — pushing to bold makes them feel like marketing shout rather than editorial authority.
- **Italic for emphasis, not oblique**: Source Serif 4's italic is a true italic (structurally different letterforms), used for pull quotes, book titles within body copy, and foreign phrases. Oblique is not used.
- **Generous reading line-height (1.65)**: Body reading text breathes at 1.65 — well above the 1.4–1.5 typical of UI-centered designs. This is the single biggest lever for perceived reading comfort.
- **Letter-spacing tightens with size**: Display runs at -1.16px, body at zero, labels slightly positive (+0.02em to +0.12em). The standard inverse tracking curve.
- **Optical sizing**: Source Serif 4 supports optical size — use the `opsz` axis if available so display renders with thinner serifs and body renders with sturdier ones.

## 4. Component Stylings

### Buttons

**Primary Amber**
- Background: Amber Gold (`#c19a3d`)
- Text: Ink Black (`#1c1813`) — high contrast, deliberately not white
- Padding: 10px 20px
- Radius: 8px
- Font: Inter 14px weight 500
- Shadow: paper-lift (`0 2px 6px rgba(45, 30, 15, 0.10)`)
- Hover: Amber Warm (`#d4b15a`)
- The flagship CTA — used for "Start reading," "Save to Reader," "Add highlight"

**Ghost Serif**
- Background: transparent
- Text: Ink Black (`#1c1813`) in Source Serif 4 italic — yes, italic, because it reads like a book's "see also"
- Border: 1px solid Border Cream (`#e0d6c3`)
- Padding: 10px 20px
- Radius: 8px
- Hover: background Parchment (`#f2ece0`)

**Dark Candle**
- Background: Ink Black (`#1c1813`)
- Text: Parchment (`#f2ece0`)
- Padding: 10px 20px
- Radius: 8px
- For inverted emphasis moments — pairs well with the dark-reader preview tile

### Cards & Containers

**Reading Card (article preview)**
- Background: Cream Paper (`#f8f4ed`)
- Border: 1px solid Border Cream (`#e0d6c3`)
- Radius: 10px
- Padding: 24px
- Shadow: paper-rest (`0 1px 2px rgba(45, 30, 15, 0.04), 0 4px 12px rgba(45, 30, 15, 0.04)`)
- Used for article previews in the feed, saved-article cards, daily review items

**Highlight Card**
- Background: Parchment (`#f2ece0`)
- Border-left: 3px solid Amber Gold (`#c19a3d`)
- Border: 1px solid Border Cream (`#e0d6c3`) (top/right/bottom only)
- Radius: 8px (right side), 0px (left side, at the accent rule)
- Padding: 18px 20px 18px 22px
- Quote text in Source Serif 4 italic at 17px
- Source metadata below in Inter 12px Warm Gray
- This is the **signature component** — it's a torn page, pinned to a corkboard

**Elevated Reading Container**
- Background: `#fdfaf4` (one tick lighter than Cream Paper)
- Border: 1px solid Border Cream
- Radius: 10px
- Shadow: paper-lift (`0 6px 24px rgba(45, 30, 15, 0.08)`)
- Used for focused reading views, modal content

### Inputs & Forms
- Background: Cream Paper (`#f8f4ed`)
- Border: 1px solid Border Cream (`#e0d6c3`)
- Radius: 8px
- Padding: 10px 14px
- Font: Inter 14px weight 400
- Text color: Ink Black (`#1c1813`)
- Focus: border Amber Gold (`#c19a3d`), ring `0 0 0 3px rgba(193, 154, 61, 0.18)`
- Placeholder: Muted Stone (`#9a9086`)

### Navigation / Sidebar
- Background: Parchment (`#f2ece0`)
- Border-right: 1px solid Border Cream
- Font: Inter 13px weight 500 for items, Source Serif 4 16px for logo
- Active item: Linen background (`#e8dfd0`), Amber-Gold left rule (3px)
- Hover: Linen background, no rule
- Section labels: Inter 11px uppercase Warm Gray

### Icons
- Icon set: **Solar Linear** and **Phosphor Regular** — both have book/reading-adjacent glyphs
- Default color: Warm Graphite (`#3d3530`)
- Active / accent color: Amber Gold (`#c19a3d`)
- Size: 18px standard, 22px in navigation, 14px inline
- Stroke weight: 1.5px (linear) — keeps the editorial lightness

### Distinctive Components

**Daily Review Card**
- A dedicated card surface that surfaces 5 saved highlights per day
- Each highlight rendered as a Highlight Card, stacked with 16px gap
- Header in Source Serif 4 20px: "Your daily review"
- Progress meter below in Inter 12px

**Reading Progress Bar**
- Thin 2px Amber-Gold bar at the top of reading view
- Fills left-to-right as the reader scrolls
- The only "app-like" affordance that survives in the reading surface

**Feed List Item**
- No background, no card — just a list row with hairline divider
- Favicon-sized source icon left-aligned
- Article title in Source Serif 4 18px weight 600
- Excerpt in Source Serif 4 15px weight 400 Warm Graphite
- Source · reading time · saved-ago in Inter 12px Warm Gray

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Scale: 2px, 4px, 8px, 12px, 16px, 20px, 24px, 32px, 40px, 64px, 80px
- Card padding: 24px internal
- Reading column gap: 32px between paragraphs of metadata, 20px between body paragraphs (via `margin-block`)
- Section spacing: 64–80px between major sections

### Grid & Container
- Reading measure: **62–72 characters per line** — the single most important layout constant
- Max reading container: 680px (optimal single-column reading width)
- Dashboard max: 1200px, centered
- Sidebar: fixed 240–280px on desktop
- No 12-column grid insistence — reading-first layouts dominate

### Whitespace Philosophy
- **Reading-first**: Content containers have generous horizontal padding (32–48px on desktop) to prevent text from kissing the container edge.
- **Paragraph rhythm**: Body paragraphs separated by roughly one line-height worth of space — enough to breathe, not enough to break reading flow.
- **Card quiet**: Cards carry 24px internal padding so highlights and metadata don't feel cramped.

### Border Radius Scale
- Hairline (0px): Hairline dividers
- Subtle (4px): Tags, inline badges, faint chips
- Standard (6px): Secondary buttons, small UI controls
- Comfortable (8px): Primary buttons, inputs, standard cards
- Rounded (10px): Article cards, reading containers
- *No radius above 12px in the light UI* — reading apps should feel bookish, not toy-like

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Body copy on canvas, inline elements |
| Hairline (Level 1) | `1px solid #e0d6c3` | Feed list rows, sidebar dividers |
| Contained (Level 2) | `1px solid #e0d6c3` + shadow-rest | Standard cards (`0 1px 2px rgba(45,30,15,0.04), 0 4px 12px rgba(45,30,15,0.04)`) |
| Elevated (Level 3) | `1px solid #d4c9b3` + shadow-lift | Hover cards, modals (`0 6px 24px rgba(45,30,15,0.08)`) |
| Floating (Level 4) | shadow-float | Popovers, command palettes (`0 12px 32px rgba(45,30,15,0.12), 0 2px 6px rgba(45,30,15,0.06)`) |

**Shadow Philosophy**: Depth is communicated through **warm amber-tinted shadows** — never cool gray, never pure black. The shadow color is always derived from a deep brown-black (`rgba(45, 30, 15, X)`) to keep the palette coherent. Shadows are diffuse and low-opacity — the sensation is of a page lightly lifted from the desk, not a UI card floating in 3D space.

### Decorative Depth
- **Vignette hero**: The hero section uses a radial cream-to-parchment gradient, mimicking the faint fall-off of a page edge under lamplight.
- **Left-rule accent**: Highlight cards use a 3px solid Amber Gold left rule — a graphic depth cue without a shadow.
- **Alternation**: Sections alternate Cream Paper → Parchment → Candle Dark to create chapter-like rhythm through the page.

## 7. Do's and Don'ts

### Do
- Use Cream Paper (`#f8f4ed`) as the canonical canvas — warmth is the brand
- Use Source Serif 4 for any text the reader is meant to *read*; use Inter for controls
- Use Amber Gold (`#c19a3d`) sparingly — as a highlight marker, a CTA, an active-state rule
- Keep body line-height at 1.65 — this is the single biggest reading-comfort lever
- Use warm amber-tinted shadows (`rgba(45, 30, 15, X)`) — never `rgba(0,0,0,X)`
- Keep radii between 6 and 10 px — readable, not rounded-to-death
- Use italic (not bold) for in-body emphasis — the serif has a true italic
- Offer a warm Candle dark mode (`#1a1613`) — never pure black
- Use the Highlight Card pattern (left-rule, italic quote, source below) for all saved quotes
- Respect a 62–72ch measure in reading views

### Don't
- Don't use pure white (`#ffffff`) as a canvas — Cream Paper always
- Don't use a sans-serif for body reading text — Reader's identity is serif-led
- Don't use blue or purple accents — the palette is warm earth only
- Don't push headlines past weight 600 — the serifs carry themselves
- Don't use drop shadows larger than 32px blur — this is a reading app, not a glassmorphism demo
- Don't use pill-shaped (`border-radius: 9999px`) elements in the reading UI — too app-y
- Don't introduce any cool-gray neutrals — every gray carries a warm undertone
- Don't underline body links by default — use Amber Gold color + hover underline instead
- Don't animate scroll progress or page turns — Reader respects stillness
- Don't put UI chrome (buttons, inputs) in a serif — that's the sans's job

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, sidebar collapses to drawer, body reading at 17px |
| Tablet | 640–1024px | Sidebar persists as icon rail, reading column 600px max |
| Desktop | 1024–1440px | Full sidebar 240px, reading column 680px, dashboard grids enable |
| Wide | 1440px+ | Optional third column for highlights/notes alongside reading view |

### Touch Targets
- Minimum 40x40px for all interactive elements
- List rows in feed have generous 12px vertical padding — easy thumb targeting
- Highlight gesture: long-press on mobile, drag-select on desktop

### Collapsing Strategy
- **Sidebar**: persistent panel → icon rail → drawer (hamburger) as width decreases
- **Reading column**: 680px → 600px → 100% (with 20px horizontal padding)
- **Hero**: 58px → 40px → 32px display headline scaling
- **Highlight cards**: grid on wide views → single column on tablet/mobile

### Image Behavior
- Inline article images: 10px radius, max-width 100% of reading column
- Hero images: full-bleed within container, with 10px radius
- No art-direction changes — aspect ratios preserved across breakpoints

## 9. Agent Prompt Guide

### Quick Color Reference
- Canvas: "Cream Paper (`#f8f4ed`)"
- Panel: "Parchment (`#f2ece0`)"
- Hover: "Linen (`#e8dfd0`)"
- Primary text: "Ink Black (`#1c1813`)"
- Secondary text: "Warm Graphite (`#3d3530`)"
- Tertiary text: "Warm Gray (`#6b6258`)"
- Accent: "Amber Gold (`#c19a3d`)"
- Border: "Border Cream (`#e0d6c3`)"
- Dark canvas: "Candle Dark (`#1a1613`)"
- Dark panel: "Candle Surface (`#26201a`)"

### Example Component Prompts
- "Build a reading hero on Cream Paper (`#f8f4ed`) with a headline at 58px Source Serif 4 weight 600, line-height 1.15. Body subtitle in Source Serif 4 at 19px weight 400 line-height 1.65, color Warm Graphite (`#3d3530`). Primary CTA: Amber Gold (`#c19a3d`) background, Ink Black text, 8px radius, Inter 14px weight 500."
- "Design a highlight card on Parchment (`#f2ece0`) with a 3px solid Amber Gold left rule. Quote text in Source Serif 4 italic 17px Ink Black. Source domain and date below in Inter 12px Warm Gray. Radius 8px (0 on the left rule side), 18px padding."
- "Create an article feed row: no card background, 16px vertical padding, hairline divider Border Cream (`#e0d6c3`). Favicon left, title in Source Serif 4 18px weight 600 Ink Black, excerpt in Source Serif 4 15px weight 400 Warm Graphite, metadata in Inter 12px Warm Gray."
- "Build a dark 'Candle' reading view on Candle Dark (`#1a1613`) with Parchment Text (`#e8dfd0`) body in Source Serif 4 19px line-height 1.65. Headings in Source Serif 4 weight 600. Amber on Dark (`#d4b15a`) for the highlight accent."
- "Design a sidebar nav item — 13px Inter weight 500, Warm Graphite text, 8px 12px padding, Linen background on hover, 3px Amber Gold left rule when active."

### Iteration Guide
1. Lead with the serif — every reading surface starts from Source Serif 4
2. Reserve Inter for anything a user clicks, selects, or configures
3. Always specify Cream Paper (`#f8f4ed`) as canvas — never white
4. Use Amber Gold (`#c19a3d`) as a garnish, not a surface — primary CTA, active state, left rules
5. Shadows use warm ink (`rgba(45, 30, 15, X)`), never pure black
6. Radii stay between 6 and 10px — anything more feels consumery
7. Body reading text always at 1.65 line-height — non-negotiable
8. Italic (not bold) for emphasis within body copy
9. For dark mode, use Candle Dark (`#1a1613`), never `#000000`
10. Respect the 62–72ch reading measure — wider is not better
