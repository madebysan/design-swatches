# Design System Inspired by Agora

## 1. Visual Theme & Atmosphere

Agora's website is the most counterintuitive crypto brand on the internet. The category default for "onchain governance protocol" is chrome, neon gradients, glassmorphism, and sci-fi monolith aesthetics. Agora chooses the exact opposite: a warm parchment canvas (`#fafaf9`), classical serif headlines set in a custom typeface called *Family*, and lush watercolor-style illustrations of pastoral landscapes — windmills, trees, figures walking through fields, heraldic shields bearing the marks of the protocols Agora serves (`ENS`, `.eth`, Optimism). The page reads like the cover of a 19th-century governance treatise, not a DAO dashboard.

The *Family* serif is the entire personality. Italic headlines run at 60px with tight tracking (`-0.025em`) and 1.0 line-height, set against the warm stone canvas with a deep stone-900 (`#1c1917`) — never pure black. Body copy switches to ui-sans-serif at 16px / 1.5, which creates a deliberate two-mode rhythm: serif for *ideas*, sans for *operations*. The product UI screenshots (Optimism Token House proposal lists, voter tables, delegate cards) sit on pure white panels with a single soft elevation shadow (`0 4px 20px rgba(0,0,0,0.05)`) — clinical and trustworthy where the marketing copy is romantic and humanistic.

What separates Agora from every other governance product is the **illustration system**. Hand-painted watercolor scenes — figures in silhouette walking toward a windmill, oversized flowers blooming next to data tables, a tree growing beside a feature timeline — are treated as primary content, not decoration. They're full-bleed at the edges and bleed through the structure of the page. Combined with the serif typography and the warm stone palette, the result is a visual argument: governance isn't a blockchain abstraction, it's a *commons*. The tools are modern (1px hairline borders, fully-rounded `9999px` pill buttons, an 8px spacing grid), but the soul of the brand is pre-industrial.

**Key Characteristics:**
- *Family* serif at weight 400 with italic accents — every headline is set in serif, never sans
- Warm stone canvas (`#fafaf9`) — parchment, not paper, never pure white for the page bg
- Stone-900 text (`#1c1917`) — deep warm black, never pure `#000000`
- Watercolor pastoral illustrations — full-bleed, hand-painted, anti-crypto
- Pill buttons (`9999px` radius) at compact `4px × 12px` padding — civic, low-pressure
- Single soft elevation shadow (`0 4px 20px rgba(0,0,0,0.05)`) — no hard offsets, no bevels
- Hairline borders in stone-200 (`#e5e7eb`) carry most of the structural work
- Two-mode rhythm: serif italic for ideas, ui-sans-serif for operational copy
- Heraldic shield motif — protocol partners shown as crests, not logos in a row

## 2. Color Palette & Roles

### Primary
- **Stone Canvas** (`#fafaf9`): The page background — warm off-white with a stone undertone. Not paper-white, not gray, not lavender — a neutral parchment that reads as *aged* rather than sterile.
- **Stone-900** (`#1c1917`): Primary text, headings, body copy, primary button background. Deep warm black with a brown-stone hue. Agora never uses `#000000`.
- **Pure White** (`#ffffff`): Reserved for product UI panels (proposal lists, voter cards, embedded screenshots) — the inverse of the stone canvas, signaling "this is the working surface."

### Stone Neutrals
- **Stone-700** (`#44403c`): Secondary text, muted body copy.
- **Stone-600** (`#57534e`): Link default state — links are darker than body, lower than headings.
- **Stone-300** (`#d6d3d1`): Secondary button background — warm light stone, low-pressure default.
- **Stone-200** (`#e7e5e4`): Hover background tint, hairline border accent on warmer surfaces.
- **Stone-200 Cool** (`#e5e7eb`): The structural border color — every divider, card outline, and section break.

### Brand & Accent
- Agora is **chromatic-restraint by design**. There is no signature brand color the way Cape has lavender or Stripe has indigo. The brand color *is* the warm stone palette plus the watercolor illustrations, which carry chromatic load (greens, terracotta reds, sky blues) when needed.
- **Illustration palette**: Botanical greens (`~#4a6b3a`), terracotta reds (`~#c54e3a`), sky blues (`~#7da9c8`) live inside paintings only. Never extracted into UI as accents — illustrations are chromatic, chrome is monochromatic.
- **Focus Ring Blue** (`rgba(59, 130, 246, 0.5)`): Default Tailwind focus ring — the only blue in the system, and only on keyboard focus.

### Surface, Borders & Shadow
- **Page Surface** (`#fafaf9`): Default canvas. **Product Surface** (`#ffffff`): Embedded product UI panels — proposal lists, dashboards, data tables.
- **Border Hairline** (`#e5e7eb`): Universal 1px divider — sections, cards, table rows, footer separators. **Border Warm** (`#e7e5e4`) is a less common variant on warmer card surfaces.
- **Soft Elevation** (`rgba(0, 0, 0, 0.05) 0px 4px 20px 0px`): The only shadow in the system. Applied to product UI panels to lift them off the stone canvas.

### Gradient System
- Agora is **gradient-free**. No marketing gradients, no glow effects, no glassmorphism. Watercolor illustrations carry all atmospheric chroma; UI surfaces are flat solid color.

## 3. Typography Rules

### Font Family
- **Display & Headline**: `Family` (custom serif, `font-weight: 400` and `500`, both italic and roman). Loaded via two `@font-face` declarations from `/assets/fonts/family-regular.woff2` and `/assets/public/fonts/Family-Medium.woff2`.
- **Body & UI**: `ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif` — pure system stack, no webfont. This is unusual and deliberate: the serif carries the brand, the sans is neutral infrastructure.
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New` — used in caption-size technical labels and stat tables.

*Note: "Family" is a custom proprietary serif for Agora. For external implementations, GT Sectra, Tiempos, or Editorial New are close substitutes; PP Editorial New Italic and ABC Diatype combo also approximates the brand voice.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Family (italic) | 60px (3.75rem) | 400 | 1.00 | -0.025em | Landing hero — *"Progressively decentralize with style and security."* |
| Display Large | Family (italic) | 48px (3.00rem) | 400 | 1.00 | -0.025em | Major section openers |
| Display | Family (italic) | 42px (2.625rem) | 400 | 1.05 | -0.025em | Mid-page narrative breaks |
| Heading 1 | Family | 36px (2.25rem) | 400 | 1.10 | -0.025em | Feature section heads |
| Heading 2 | Family | 32px (2.00rem) | 400 | 1.15 | -0.025em | Sub-section heads, About-page titles |
| Heading 3 | Family | 30px (1.875rem) | 400 | 1.20 | -0.025em | Card titles, embedded chart heads |
| Heading 4 | Family | 24px (1.50rem) | 400–500 | 1.20 | normal | Product UI panel titles |
| Body Large | ui-sans-serif | 20px (1.25rem) | 400 | 1.50 | normal | Hero subhead, intro paragraphs |
| Body | ui-sans-serif | 18px (1.125rem) | 400 | 1.50 | normal | Standard reading paragraph in marketing copy |
| Body Default | ui-sans-serif | 16px (1.00rem) | 400 | 1.50 | normal | Default body, About-page prose |
| UI Caption | ui-sans-serif | 14px (0.875rem) | 400–500 | 1.50 | normal | Button labels, nav links, table cells |
| Caption Small | ui-sans-serif | 12px (0.75rem) | 400 | 1.50 | normal | Metadata, timestamps in proposal lists |
| Mono Caption | ui-monospace | 14px (0.875rem) | 400 | 1.20 | normal | Technical stats, hash strings, addresses |
| Micro | ui-sans-serif | 10px (0.625rem) | 400 | 1.20 | normal | Smallest legal/footer chrome |

### Principles
- **Serif for ideas, sans for operations**: Every headline, narrative pull-quote, and brand statement is set in *Family* serif. Every functional UI label, button, table row, and caption is set in ui-sans-serif. The two never blur — there are no sans headlines and no serif buttons.
- **Italic as the brand voice**: The largest display headlines are italic, not roman. Italic serif at 48–60px is a deliberate choice that reads as *editorial confidence* rather than corporate authority. Used for hero statements and major narrative breaks.
- **Single letter-spacing token**: `-0.025em` is the only tracking value applied to display type. No size-progressive tracking like Cape does — Agora applies the same negative track to everything 24px and up.
- **System sans by design**: There is no webfont for body copy. The decision to use the OS's native sans (San Francisco on macOS/iOS, Segoe UI on Windows, Roboto on Android) keeps body copy fast and locally trustworthy — and it visually defers to the serif, which is the only typeface with personality.
- **Tight headline leading**: Display sizes run at 1.00–1.20 line-height. The italic serif is dense at this leading and reads as a single composed block, not airy editorial.
- **No uppercase chrome**: Unlike Cape, Agora does not use uppercase for buttons or labels. Everything is sentence case. The civic, calm tone forbids shouting.

## 4. Component Stylings

### Buttons

**Primary Stone (Dark)**
- Background: Stone-900 (`#1c1917`); Text: Pure White (`#ffffff`)
- Padding: `4px 12px` compact, `8px 16px` standard, `12px 24px` large CTA
- Radius: `9999px` (fully pill); Border: `0px`; Shadow: `none`
- Font: 14px ui-sans-serif weight 400, sentence case
- Hover: bg → Stone-700 (`#44403c`), text → Stone-200 warm (`#e7e5e4`)
- Use: Primary CTAs — *Talk to an expert*, *Get started*, *Read more*

**Secondary Stone (Light)**
- Background: Stone-300 (`#d6d3d1`); Text: Stone-900 (`#1c1917`)
- Padding: `4px 12px` compact, `8px 16px` standard
- Radius: `9999px`; Border: `0px`; Shadow: `none`
- Font: 14px ui-sans-serif weight 400
- Hover: bg → Stone-700, text → Stone-200 warm
- Use: Secondary actions, top-nav active state ("Product" pill)

**Ghost Nav Link**
- Transparent bg, Stone-700 text → Stone-900 on hover; `4px 12px` padding
- Use: Top-nav links — Blog, About, Careers, Contact

### Cards & Containers

**Product UI Card** — `#ffffff` bg, `1px solid #e5e7eb` hairline, `12px` radius, soft elevation `0 4px 20px rgba(0,0,0,0.05)`, 24–32px internal padding. Use: embedded product screenshots — proposal lists, voter tables, delegate cards.

**Marketing Block** — Stone Canvas (`#fafaf9`) bg same as page, `1px solid #e5e7eb` top or bottom only as section divider, `0px` radius, no shadow. Use: marketing copy sections, hero, testimonial blocks.

**Soft Card** — `#ffffff` bg, `1px solid #e5e7eb`, `8px` radius, no shadow. Use: smaller informational cards, partner crests, footer link groups.

### Badges / Tags / Pills
**Status Pill**
- Background: Stone-900 (`#1c1917`) for active, transparent with 1px stone-200 border for inactive
- Text: White on dark, Stone-700 on light
- Padding: `4px 12px`
- Radius: `9999px`
- Font: 14px ui-sans-serif weight 400 or 500
- Use: Proposal status ("Succeeded"), nav active indicator

### Inputs & Forms
- Background: Pure White (`#ffffff`)
- Border: `1px solid #e5e7eb`
- Radius: `8px`
- Font: 16px ui-sans-serif weight 400
- Text color: Stone-900 (`#1c1917`)
- Focus: `rgba(59, 130, 246, 0.5)` ring (Tailwind default blue) — the one chromatic UI moment in the system
- Padding: 8–12px vertical, 12–16px horizontal

### Navigation
- Top nav: minimal horizontal bar on stone canvas, centered or left-aligned. Small Agora wordmark/logomark (the column-capital glyph) on the left, link cluster on the right.
- Active page: dark stone-900 pill (`9999px` radius) with white text — *"Product"* in the homepage example
- Inactive links: ghost text in Stone-700, no underline, no hover background
- Hover: text shifts to Stone-900
- No sticky behavior — the nav scrolls with the page on most viewports

### Decorative Elements

**Watercolor Illustrations**
- Hand-painted pastoral scenes — figures in silhouette, windmills, trees, fields, gardens, riverside paths
- Full-bleed integration: paintings extend past the content column to the page edges
- Color palette inside paintings: muted sage greens, terracotta reds, warm earth browns, pale sky blues
- Used as primary content, not decoration: a section about "where we lose our heart" leads with a meadow scene with shields planted in it, not an icon
- Heraldic shields embedded in scenes signal partner protocols (ENS, Optimism, Uniswap, etc.) — partners are *crests*, not logos

**Hairline Section Dividers**
- `1px solid #e5e7eb` horizontal lines separate every major content block
- No decorative dividers, no SVG flourishes, no gradient lines — just the hairline
- This is the dominant structural element on the entire page

## 5. Layout Principles

### Spacing System
- Base unit: 8px (with 4px as a half-unit for tight UI chrome)
- Scale: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 128px, 320px
- Notable: Agora's spacing is heavily skewed to the small end (4–16px dominates UI components — buttons, table rows, badges) and to the very large end (128–320px for section breaks). Mid-range values (40–96px) are used sparingly.

### Grid & Container
- Max content width: ~1024px for marketing copy, ~1280px for product UI demonstrations
- Hero: centered single-column with serif headline + subhead + CTA, illustration below
- Feature sections: full-bleed product screenshots flanked by watercolor margins
- Multi-column grids appear only in the "stats" and "footer link groups" — never in the marketing narrative
- The page reads like a vertically scrolled magazine — every section is a chapter break, not a column

### Whitespace Philosophy
- **Editorial pacing**: Major sections separated by 96–128px of vertical space — the page breathes like a printed essay
- **Headline-anchored rhythm**: A 60px italic serif headline gets ~80px of air above and ~40px below, with the body copy and illustration sitting close together as a single unit
- **Hairline-led structure**: The 1px divider does most of the work that decorative spacing or background color shifts do elsewhere — the structure is *drawn*, not *spaced*

### Border Radius Scale
- Sharp (0px): Section dividers, full-bleed marketing blocks, the page itself — no chrome on the canvas
- Soft (8px): Input fields, soft informational cards
- Medium (12px): Product UI panels, embedded dashboard screenshots
- Pill (9999px): All buttons, all status badges, top-nav active state — every interactive control
- No `4px`, `16px`, `20px`, or `24px` radii: Agora's radius scale is `0 / 8 / 12 / 9999` — four values, no in-between

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border, no inset | Page canvas, marketing blocks, body text |
| Hairline (Level 1) | `1px solid #e5e7eb` border only | Section dividers, table rows, soft cards |
| Soft Lift (Level 2) | `rgba(0, 0, 0, 0.05) 0px 4px 20px 0px` + `1px solid #e5e7eb` | Product UI panels, primary cards — the only elevation in the system |
| Focus Ring (Level 3) | `rgb(255, 255, 255) none 3px` outline (or stone-900 for light buttons) | Keyboard focus on interactive elements |

**Shadow Philosophy**: Agora has *one* shadow. Where most modern web design has a 5-step elevation token system, Agora ships a single soft drop shadow — `0px 4px 20px rgba(0, 0, 0, 0.05)` — and uses it exclusively for product UI panels lifting off the stone canvas. Marketing content is *flat* and *hairline-bordered*. The contrast is the point: marketing is a printed page; product is a lifted card. Two surfaces, two treatments, no gradient between them.

### Decorative Depth
- The watercolor illustrations carry all atmospheric depth — paintings have implied perspective, light, and distance, but the UI surrounding them is pancake-flat
- No glassmorphism, no neumorphism, no inset shadows, no gradients
- Focus states use a 3px transparent outline that becomes visible only on keyboard navigation — invisible to mouse users

## 7. Do's and Don'ts

### Do
- Use *Family* serif (or GT Sectra / Tiempos as substitute) for every headline 24px and up — the serif is the brand
- Set the largest hero headlines in italic at 60px / 1.00 line-height / -0.025em tracking
- Use Stone-900 (`#1c1917`) for primary text — never pure `#000000`
- Use Stone Canvas (`#fafaf9`) for the page background — never `#ffffff` for marketing
- Use ui-sans-serif system stack for all body copy and UI — defer to the OS
- Use `9999px` radius for every button, badge, and pill — civic, friendly, low-pressure
- Use a single soft shadow (`0 4px 20px rgba(0,0,0,0.05)`) only on product UI panels
- Use 1px hairline borders (`#e5e7eb`) as the dominant structural element
- Lean on watercolor illustrations as primary content — pastoral, hand-painted, anti-crypto
- Treat partner protocols as heraldic crests embedded in scenes, not logo rows
- Keep the type scale binary: serif italic for ideas, sans for operations

### Don't
- Don't use sans-serif headlines — every headline must be set in serif
- Don't use uppercase button labels or letter-spaced UI — sentence case only
- Don't introduce gradients, glows, or glassmorphism — Agora is solid color and watercolor
- Don't use pure black (`#000000`) or pure white (`#ffffff`) for marketing surfaces — stone hues only
- Don't add accent brand colors — illustrations carry all chroma, UI is monochromatic stone
- Don't use square buttons — every button is fully pill (`9999px`)
- Don't stack multiple elevation shadows — there is one shadow in the system
- Don't replace watercolors with vector illustrations or 3D renders — hand-painted is non-negotiable
- Don't use mid-range radii (4px, 16px, 20px, 24px) — the scale is 0/8/12/9999
- Don't use roman serif at hero size — italic is the brand voice at 48–60px
- Don't use webfont sans-serif for body — system stack only

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single-column, hero drops to 36–42px italic, illustrations stack |
| Tablet | 640–768px | Single-column with wider gutters, hero at 48px |
| Small Desktop | 768–1024px | Two-column moments begin (footer, partner grid), hero at 48–60px |
| Desktop | 1024–1280px | Full layout, hero at 60px, product UI at full embedded size |
| Large Desktop | 1280–1536px | Maximum 1024px content column with watercolor margins extending into whitespace |
| XL | ≥1536px | Watercolor scenes can extend further into the bleed; type scale is locked |

### Touch Targets
- Primary CTA pills: min 32px tap height at compact size, 44px at standard — pill shape gives generous tap area
- Nav links: 4–12px padding scales up on mobile to ensure thumb-reach
- Product UI cards: full-width tap targets on mobile

### Collapsing Strategy
- **Nav**: Horizontal link cluster collapses to a hamburger or compact menu icon below 768px; logomark stays
- **Hero**: 60px → 48px → 42px → 36px italic serif progressive scale; the italic styling holds at every breakpoint
- **Product UI screenshots**: Embedded dashboard panels scroll horizontally on mobile rather than reflowing — they're treated as images, not responsive components
- **Watercolor illustrations**: Reorder above or below text on mobile; never crop the painted artwork to fit
- **Section spacing**: 128px desktop → 64px mobile — significant compression but the editorial pacing is maintained
- **Footer**: 4-column link grid on desktop collapses to single-column stacked on mobile

### Image Behavior
- Watercolor illustrations are full-bleed at all sizes — never letterboxed or cropped tightly
- Product UI screenshots maintain aspect ratio and scroll horizontally on mobile if needed
- Heraldic shields/crests scale proportionally; their placement within illustrations is preserved

## 9. Agent Prompt Guide

### Quick Color Reference
- Page Background: Stone Canvas (`#fafaf9`)
- Primary Text: Stone-900 (`#1c1917`)
- Secondary Text: Stone-700 (`#44403c`)
- Link Default: Stone-600 (`#57534e`)
- Hairline Border: Stone-200 Cool (`#e5e7eb`)
- Primary Button: Stone-900 (`#1c1917`) bg / White text
- Secondary Button: Stone-300 (`#d6d3d1`) bg / Stone-900 text
- Hover Bg: Stone-700 (`#44403c`)
- Hover Text on Dark: Stone-200 (`#e7e5e4`)
- Product UI Surface: Pure White (`#ffffff`)
- Soft Shadow: `rgba(0, 0, 0, 0.05) 0px 4px 20px 0px`
- Focus Ring: `rgba(59, 130, 246, 0.5)` (default blue)

### Example Component Prompts
- "Create a hero section on Stone Canvas (`#fafaf9`) with an italic serif headline at 60px (use *Family* / GT Sectra / Tiempos) at weight 400, line-height 1.00, letter-spacing -0.025em, color `#1c1917`. Subhead at 18px ui-sans-serif weight 400, line-height 1.50, color `#44403c`. CTA: pill button (`9999px` radius) with `#1c1917` bg, white text, 14px sans, 8px × 16px padding, sentence case (e.g. *Talk to an expert*)."
- "Design a product UI panel embedded in a marketing page — pure white background (`#ffffff`), `12px` border radius, `1px solid #e5e7eb` border, soft shadow `0 4px 20px rgba(0,0,0,0.05)`. Inside: a proposal table with stone-900 headings in serif at 24px, 14px ui-sans-serif body rows, hairline `1px solid #e5e7eb` row dividers, monospace 14px for stat columns."
- "Build a top navigation bar on stone canvas. Small Agora-style column-capital wordmark on the left. Link cluster on the right: active link is a stone-900 pill (`9999px` radius, 4px × 12px padding, white text). Inactive links are ghost stone-700 text, no underline, sentence case (Blog, About, Careers, Contact)."
- "Create a content section break: a single `1px solid #e5e7eb` horizontal hairline with 96px of vertical space above and below. No decorative elements, no SVG flourishes, no background color shift."
- "Design a partner-protocol section using heraldic shield motifs — embed protocol logos (ENS, Optimism, Uniswap) as crests inside a hand-painted watercolor pastoral scene. Use a windmill, a tree, figures in silhouette walking through a meadow. Full-bleed integration, illustration extends past the content column."

### Iteration Guide
1. Default to *Family* (or GT Sectra / Tiempos / Editorial New) italic for every headline 24px and up — serif is non-negotiable
2. Body copy and UI labels stay in `ui-sans-serif` system stack — no webfont sans, no exceptions
3. Letter-spacing is `-0.025em` for everything 24px and up; normal below 24px
4. Buttons are always pill (`9999px` radius), always sentence case, never uppercase
5. Page background is Stone Canvas (`#fafaf9`); product UI is Pure White (`#ffffff`); never blur the two
6. Stone-900 (`#1c1917`) is the darkest value — never use pure `#000000`
7. One shadow only: `0 4px 20px rgba(0,0,0,0.05)`. Apply to product UI panels exclusively. Marketing is flat.
8. 1px hairline borders (`#e5e7eb`) carry all structural separation — no thick borders, no gradient dividers
9. Watercolor illustrations are required for hero and major narrative breaks — pastoral, hand-painted, anti-crypto
10. Radius scale is binary-plus-one: `0 / 8 / 12 / 9999`. Never `4`, `16`, `20`, or `24`.
