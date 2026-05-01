---
slug: things
name: Things (Cultured Code)
url: https://culturedcode.com
domain: culturedcode.com
category: Productivity
styles: [Minimal, Light, Tactile]
tagline: "Paper-cool off-white canvas, dual-layer warm shadows, one blue accent used sparingly."
fonts: [ui-sans-serif]
primary_color: "#2576eb"
---

# Design System Inspired by Things (Cultured Code)

> Paper-cool off-white canvas, dual-layer warm shadows, one blue accent used sparingly.

## 1. Visual Theme & Atmosphere

Things is the Platonic ideal of Mac-native craft — a to-do app that feels like a leather-bound notebook sitting on a walnut desk, not a productivity dashboard begging for attention. The entire surface is built on a paper-cool off-white canvas (`#f2f5f7`) that reads as premium stationery rather than screen glare, and the typography is classic San Francisco — `ui-sans-serif` with `-apple-system` fallbacks — set at calm, conversational sizes that never crowd the eye. Where most productivity apps shout with bold purples and neon checkmarks, Things whispers. Its signal is restraint, and the result is an interface that has won an Apple Design Award in three different decades because every pixel has been loved.

The defining move is the *trio* of warm neutrals — `#8e9196` (mid gray), `#55606e` (blue-gray for links and secondary UI), and `#2c3138` (deep charcoal for headings) — paired with a single saturated blue (`#2576eb`) that functions as the only chromatic accent in the system. That blue shows up exactly where it has to: the check-circle when a task is starred, the primary CTA, focus rings on inputs. Everything else is gray-on-paper, letting content breathe. Weights stay in the 400–700 range, but the composition almost never reaches for 700 at display sizes; 36px headings at weight 700 only at the very top of the page, and from there the hierarchy drops to 600 and 400 with a matter-of-fact Apple HIG rhythm. This is type treated like UI, not type treated like editorial.

What separates Things from every other "minimalist" app is its shadow system. Instead of the harsh drop shadows most web products reach for, or the flat no-shadow sterility of AI-slop 2024-2026, Things uses a signature dual-layer warm shadow: `rgba(0, 0, 0, 0.1) 0px 2px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 2px 0px`. The first layer is a whisper of lift at 2px offset with 8px blur — enough to suggest a card resting on paper. The second is a hair-thin 2px halo with zero offset that acts as a quasi-border, defining the card's edge without needing an actual stroke. Combined with generous 18px border-radius on featured cards and a 10–12.8px radius on secondary surfaces, this gives every element a tactile, light-catching presence. Things doesn't simulate paper — it inhabits it.

**Key Characteristics:**
- SF Pro / `ui-sans-serif` system stack at Apple HIG-calm sizes — 36px max display, 16–18px body
- Paper-cool canvas (`#f2f5f7`) — the definitive "not pure white" productivity background
- Dual-layer shadow signature — `0 2px 8px` soft lift paired with `0 0 2px` edge halo
- Blue accent (`#2576eb` / `#5c9cf5`) applied only to primary CTAs, focus rings, and the check-circle
- Generous border-radius spectrum (3px inline → 18px featured cards) for subtle varied rhythm
- Asymmetric button padding (`7.12px 16.96px`) — Apple-flavored, slightly wider horizontally
- Scale transform on active press (`scale(0.95)`) — the tactile "click-down" micro-interaction
- Focus halo using blue at 50% opacity (`rgba(37, 118, 235, 0.5) 0px 0px 0px 2px`) — accessibility without harshness

## 2. Color Palette & Roles

### Primary
- **Paper** (`#f2f5f7`): The primary page canvas — a cool off-white with the barest blue-green undertone. Not warm cream, not cold white; it's the shade of high-quality bond paper viewed in daylight. This is the emotional foundation of Things.
- **Things Blue** (`#2576eb`): The single chromatic accent — primary CTA background, link color, focus ring anchor. A saturated azure that reads as "signal," never decoration.
- **Sky Blue** (`#5c9cf5`): The softer variant — selected-row highlight (at 20% opacity), secondary link color, check-circle when items are starred.

### Text
- **Charcoal** (`#303336`): Primary text color — headings, body, interactive labels. Not pure black (`#000`); the slight warm-cool balance prevents screen harshness.
- **Deep Slate** (`#2c3138`): Slightly deeper alternate for emphasized headings and strong UI chrome.
- **Ink** (`#44474b`): Mid-tone for secondary headings and emphasized body content.
- **Blue-Gray** (`#55606e`): Secondary text, timestamps, tweet/quote attribution — the "quiet" content voice with a faint cool shift.
- **Stone** (`#8e9196`): Tertiary text and metadata — the quietest voice, used for muted link states and de-emphasized labels.
- **Fog** (`#8792a1`): Disabled state, inactive nav items, placeholder-adjacent content.
- **Mist** (`#9299a4`): The lightest usable gray — used sparingly for the most de-emphasized caption text.

### Surface & Borders
- **Paper Canvas** (`#f2f5f7`): Page and section background.
- **Pure White** (`#ffffff`): Card backgrounds, input fields, elevated surfaces on the paper canvas.
- **Border Cool** (`#dfe3e8`): Input borders and subtle dividers — visible but never demanding.
- **Divider Translucent** (`rgba(0, 28, 70, 0.12)`): Top-only hairline divider for list separators, carrying a faint blue tint that ties to the brand accent.

### Interactive States
- **Hover Tint** (`rgba(4, 15, 26, 0.05)`): Ultra-subtle hover background on list rows and menu items — a 5% blue-black wash.
- **Selection Tint** (`rgba(92, 156, 245, 0.2)`): Selected-state background — Sky Blue at 20% opacity, producing a soft lavender-blue cast.
- **Focus Ring Blue** (`rgba(37, 118, 235, 0.5)`): The keyboard-accessibility halo — Things Blue at 50% opacity applied as `0px 0px 0px 2px` ring shadow.
- **Active Press** (`scale(0.95)`): Buttons don't change color on press — they scale down 5%, a purely physical feedback signal borrowed from iOS.

### Shadow & Depth Tokens
- **Shadow Soft Lift** (`rgba(0, 0, 0, 0.1) 0px 2px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 2px 0px`): The signature card shadow — dual-layer, the first giving soft downward lift and the second acting as a hair-thin edge halo.
- **Shadow Ring Thin** (`rgba(0, 0, 0, 0.1) 0px 2px 10px 0px, rgba(0, 0, 0, 0.05) 0px 0px 0px 1px`): Alternate elevation — deeper blur for floating panels, with a 1px ring instead of a 2px halo.
- **Shadow Bottom Edge** (`rgba(38, 52, 74, 0.15) 0px 1px 0px 0px`): A flat 1px shadow acting as a sticky-header bottom border — purely graphic, no blur.
- **Shadow Hover Nudge** (`rgba(0, 0, 0, 0.05) 0px 2px 4px`): The lighter, tighter shadow that appears under buttons on hover — subtle but detectable, enough to signal interactivity.

### Gradient System
- Things is functionally **gradient-free**. The visual richness comes entirely from layered shadows on the paper canvas, the contrast between white cards and the `#f2f5f7` backdrop, and the single blue accent. There are no color ramps, no hero gradients, no backdrop blurs — the system trusts flat color and careful elevation.

## 3. Typography Rules

### Font Family
- **Primary**: `ui-sans-serif`, with fallbacks: `-apple-system`, `system-ui`, `Roboto`
- **Monospace**: Not present in the core marketing surface; Things uses the default system mono stack where needed (task attributes, keyboard shortcuts).
- **OpenType Features**: None enabled explicitly — the system font is allowed to use its default feature set, preserving SF Pro's native behavior.

*Note: On macOS this resolves to SF Pro Text at body sizes and SF Pro Display at headings. The design presumes Apple's native optical sizing; web substitutes should use Inter as a reasonable stand-in, though the proportional feel of SF Pro is what makes Things "feel Apple."*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display | ui-sans-serif | 36px (2.25rem) | 700 | 1.00 (tight) | normal | Maximum size — rarely used, reserved for top-of-page moments |
| Sub-heading Large | ui-sans-serif | 24px (1.50rem) | 600 | 1.00 (tight) | normal | Section heads, feature titles |
| Sub-heading Quiet | ui-sans-serif | 24px (1.50rem) | 400 | 1.25 | normal | Narrative sub-headings that don't demand weight |
| Heading Medium | ui-sans-serif | 20.25px (1.27rem) | 700 | 1.20 (tight) | normal | Card titles, emphasized list headers |
| Heading Medium Quiet | ui-sans-serif | 20.25px (1.27rem) | 400 | 1.30 | normal | Readable sub-heading, often pull-quote weight |
| Link Prominent | ui-sans-serif | 20.25px (1.27rem) | 600 | 1.30 | normal | Large CTA-adjacent links |
| Body Large | ui-sans-serif | 18px (1.13rem) | 400 | 1.35 | normal | Intro paragraphs, feature descriptions |
| Link Default | ui-sans-serif | 18px (1.13rem) | 400 | 1.20 | normal | Inline links at body-large size |
| Body Standard | ui-sans-serif | 16.96px (1.06rem) | 700 | normal | normal | Bold emphasis within body |
| Body | ui-sans-serif | 16px (1.00rem) | 400 | 1.30 | normal | Standard reading text, nav links |
| Caption | ui-sans-serif | 15.3px (0.96rem) | 400 | 1.20 | normal | Metadata, small labels |
| Caption Bold | ui-sans-serif | 15.3px (0.96rem) | 700 | 1.20 | normal | Emphasized metadata, timestamps |
| UI Small | ui-sans-serif | 15px (0.94rem) | 600 | 1.20–1.60 | normal | Button labels, small navigation |
| Micro Link | ui-sans-serif | 13.68px (0.85rem) | 400 | 1.30 | normal | Footer links, fine-print navigation |
| Micro | ui-sans-serif | 13px (0.81rem) | 400–700 | 1.20 | normal | Smallest labels, legal footer text |

### Principles
- **System-native optical sizing**: Because Things uses `ui-sans-serif`, it automatically gets SF Pro Text at small sizes and SF Pro Display at large sizes on Apple platforms. Don't fight this by loading a custom variable font — the native optical sizing IS the craft.
- **Weight restraint**: The system uses 400 / 600 / 700 only. No 300, no 500, no 800. This three-weight economy keeps the page feeling calm; there's no lightweight display type or heavy-bold aggression.
- **Tight heading line-heights**: Headings run at 1.00–1.20 line-height, which is tight enough to feel composed but not so tight that descenders collide. 1.00 at 36px looks especially composed.
- **Relaxed body**: Body text at 1.30–1.35 is the Apple HIG default — not editorial-generous like a book, not data-dense like a spreadsheet.
- **No letter-spacing tricks**: Unlike Stripe's progressive negative tracking, Things keeps letter-spacing at `normal` across the entire system. SF Pro is self-spacing.
- **Heading AA hierarchy**: 36 → 24 → 20 → 18 → 16 — roughly a 1.2–1.3 ratio ladder. No huge jumps, no tiny increments. Each level is a clean typographic step.

## 4. Component Stylings

### Buttons

**Primary Blue (Apple-flavored)**
- Background: Things Blue (`#4f91fb`) — a slightly softer variant than the link blue
- Text: Pure White (`#ffffff`)
- Padding: `7.12px 16.96px` — asymmetric, Apple-ish horizontal emphasis
- Radius: `7.6px` — the specific subtle rounding that reads as "a real macOS button"
- Border: `1px solid rgba(0, 0, 0, 0)` — transparent baseline, can intensify on focus
- Shadow: `none` at rest; on hover: `rgba(0, 0, 0, 0.05) 0px 2px 4px` (subtle lift)
- Font: 16.96px `ui-sans-serif` weight 700
- Hover: background brightens to `#649fff`
- Active: `scale(0.95)` press-down, background deepens to `#3c84f3`
- Focus: `rgba(37, 118, 235, 0.5) 0px 0px 0px 2px` ring (no outline)
- Use: Primary CTA — "Buy Things", "Download", "Start free trial"

**Ghost Link-Button**
- Background: transparent
- Text: Things Blue (`#2576eb`)
- Padding: `7.12px 16.96px`
- Radius: `7.6px` to match primary
- No shadow, no border
- Hover: underline appears
- Use: Secondary actions — "Learn more", "Watch the video"

**Subtle Panel Button**
- Background: Pure White (`#ffffff`)
- Text: Charcoal (`#303336`)
- Padding: `7.12px 16.96px`
- Radius: `6.4px`
- Shadow: Shadow Soft Lift signature
- Use: Tertiary actions on the paper canvas — "Open documentation", "See shortcuts"

### Cards & Containers
- Background: Pure White (`#ffffff`) — cards always elevate off the paper canvas
- Border: `0px` default — cards rely on shadow, not stroke
- Radius: `18px` for featured cards, `12.8px` for standard, `10.8px` for compact, `6px` for inline surfaces
- Shadow: **Shadow Soft Lift** (`rgba(0, 0, 0, 0.1) 0px 2px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 2px 0px`) — the signature treatment
- Internal padding: generous — 27px–40px for feature cards, mirroring the generous whitespace of the app itself
- Hover: shadow can shift to Shadow Ring Thin for a "picked up" sensation

### Inputs & Forms
- Background: Pure White (`#ffffff`)
- Border: `1px solid #dfe3e8` (Border Cool)
- Radius: `6.4px`
- Padding: `8px` (compact, Apple-HIG-native)
- Font: 16px `ui-sans-serif` weight 400, color Charcoal (`#303336`)
- Focus: border shifts to transparent, `rgba(37, 118, 235, 0.5) 0px 0px 0px 2px` ring shadow replaces it
- Placeholder: Stone (`#8e9196`)
- No outline — the box-shadow ring carries focus

### Links (multi-state palette)
Things has **eight distinct link treatments** across the site, reflecting an editorial discipline rare in software:
1. **Primary content link**: `#303336`, weight 600, no underline → hover: underline
2. **De-emphasized link**: `rgba(38, 52, 74, 0.5)`, weight 600 → hover: underline, color shifts to white (on dark backgrounds)
3. **Brand blue link**: `#5c9cf5`, weight 600 → hover: underline
4. **Action blue link**: `#2576eb`, weight 400 → hover: underline
5. **Legal-text link**: `rgba(0, 7, 18, 0.44)`, weight 400, underlined by default
6. **Secondary metadata link**: `#8792a1`, weight 400 → hover: underline
7. **Caption link**: `#8e9196`, weight 700 → hover: underline
8. **Cited link**: `#55606e`, weight 400 → hover: color shifts to `#1b5dbd`

This multi-link palette is how Things maintains hierarchy without ever resorting to a new color — each link "voice" communicates relative importance through gray value alone.

### Navigation
- Top nav: horizontal white bar with `rgba(38, 52, 74, 0.15) 0px 1px 0px 0px` bottom shadow acting as a divider
- Logo: Things icon (the checkbox with a check) + wordmark
- Links: 16px `ui-sans-serif` weight 400, color Charcoal (`#303336`)
- Hover: underline
- CTA: Primary Blue button right-aligned
- Sticky behavior: fixed to top with the 1px bottom shadow, no blur

### Check-Circle Micro-interaction
The signature Things UI element — the empty check-circle that fills with a blue checkmark when tapped. In documentation imagery and screenshots:
- Empty state: 16–20px circle, `1.5px` stroke in `#dfe3e8`, transparent fill
- Checked state: Things Blue (`#2576eb`) fill, white checkmark glyph, with a brief scale-bounce animation
- Starred state: Sky Blue (`#5c9cf5`) with a star-shaped check instead of the tick

### Quotes / Testimonial Cards
From the screenshot's "What People Are Saying" section:
- Background: Pure White (`#ffffff`)
- Border radius: `18px` (generous, featured-level)
- Padding: `27px` internal
- Shadow: Shadow Soft Lift signature
- Type hierarchy inside:
  - Tweet body: 15.3px weight 400, color Charcoal (`#303336`)
  - Handle: `@username` at 15.3px weight 400, color Stone (`#8e9196`)
  - Attribution name: 15.3px weight 700, color Charcoal
  - Date: 13px weight 400, color Stone
- Avatar: 32px circular, right-aligned below content

### Badges / Tags / Pills
Things doesn't heavily use traditional badges — its system prefers inline text with color-coded gray values. When pill-shaped elements appear:
- Background: Pure White with Shadow Soft Lift, or `#f2f5f7` tinted panel
- Radius: `9.6px` or `10.8px` (softly rounded, not fully pill)
- Padding: `2px 8px`
- Font: 13px weight 400, color Charcoal or Blue-Gray

## 5. Layout Principles

### Spacing System
- Base unit: 8px (with a fractional scale derived from the Apple HIG)
- Scale (px): 2, 4, 6, 9, 10, 12, 14, 18, 20, 27, 40, 81
- Notable: The scale is "Apple-fractional" — values like `4.59px`, `10.125px`, `12.8px`, `22.8px`, `27px` appear because the app is set at `0.9rem` root sizing, so everything inherits `x * 0.9` fractions. This isn't messy; it's intentional — it produces the distinctly Apple "tight but breathing" rhythm where nothing feels like it was snapped to a 16-grid.
- Generous section spacing: 81px between major sections, 40px within sections.

### Grid & Container
- Max content width: approximately 1106px (the largest of Things' breakpoints)
- Hero: centered, single-column with generous vertical padding
- Testimonial grids: 4-column on desktop, collapsing to 2-column at tablet, single column at mobile
- Dark/light section alternation is absent — Things stays on the paper canvas throughout, trusting shadow and card layering for rhythm instead

### Whitespace Philosophy
- **Breath over density**: Things deliberately uses more whitespace than comparable productivity tools. A to-do app that feels cramped would contradict its philosophy; the empty space IS the product.
- **Paper as breathing room**: The `#f2f5f7` canvas that surrounds white cards acts as visual rest — the eye can land on paper between cards just like it lands on margin between paragraphs in a book.
- **Section beats**: Generous 81px section gaps create "chapters" without requiring dividers or headline walls.

### Border Radius Scale
- Sharp (3px): Inline tags, tiny clipped images
- Subtle (4.5px–5px): Highlighted mark elements, small inline buttons
- Standard (6px): Primary buttons, action links — the "Apple-HIG-default" rounding
- Comfortable (6.4px): Input fields — slightly softer than buttons
- Apple Button (7.6px): The specific rounding of Things' primary CTA — a Goldilocks radius that reads as "real macOS button"
- Panel (9.6–10.8px): Small panels, tag pills, badges
- Card (12.8px): Standard card containers
- Featured (18px): Testimonial cards, hero content panels — the signature generous radius

Things' radius philosophy is *graduated* — unlike Cape's binary system or Stripe's narrow 4–8px band, Things uses a full ladder so different elements feel hierarchically distinct even when they share color and shadow.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Paper canvas (`#f2f5f7`), inline body text |
| Edge (Level 1) | `rgba(38, 52, 74, 0.15) 0px 1px 0px 0px` | Sticky headers, nav bottom divider — flat graphic line |
| Signature Lift (Level 2) | `rgba(0, 0, 0, 0.1) 0px 2px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 2px 0px` | Standard cards, testimonial cards, feature containers — THE Things shadow |
| Picked-Up (Level 3) | `rgba(0, 0, 0, 0.1) 0px 2px 10px 0px, rgba(0, 0, 0, 0.05) 0px 0px 0px 1px` | Hover-state elevation for cards, floating panels |
| Hover Nudge (Level 4) | `rgba(0, 0, 0, 0.05) 0px 2px 4px` | Button hover — subtle signal without over-commitment |
| Focus Halo (Level 5) | `rgba(37, 118, 235, 0.5) 0px 0px 0px 2px` | Keyboard focus on all interactive elements — blue at 50% opacity |

**Shadow Philosophy**: Things' elevation model is defined by the **dual-layer signature shadow**: a soft `0px 2px 8px` downward lift at 10% opacity paired with a `0px 0px 2px` hair-thin halo also at 10% opacity. The first layer creates the sensation of a card resting on the paper canvas — low, warm, barely there. The second layer acts as a graphic edge — it gives the card definition without needing a visible border stroke. Together they produce the distinct Things tactile feel: cards look *placed* on paper, not drawn on a screen.

The shadow colors are technically neutral black (`rgba(0, 0, 0, 0.1)`), but because they're applied over the paper-cool canvas (`#f2f5f7`), the perceived result is slightly warm — the shadow "inherits" the ambient paper tone through visual interaction. This is why swapping Things' canvas for pure white ruins the effect: the same shadow reads as harsh on `#ffffff` but feels like a soft paper-cast on `#f2f5f7`.

### Decorative Depth
- **No gradients, no blur, no glassmorphism**: Depth comes exclusively from the shadow system and card/paper layering
- **Transform-based press feedback**: `scale(0.95)` on active press replaces the "shadow deepens" pattern common on web — Things uses physical scale compression for tactile feedback, like an iOS control
- **Focus as color, not drop shadow**: Focus states use the blue ring shadow rather than increasing elevation — you can always tell what's interactive by "is it blue-ringed" rather than "is it raised"

## 7. Do's and Don'ts

### Do
- Use Paper (`#f2f5f7`) as the canvas — pure white destroys the craft
- Layer the dual signature shadow on every card — `0 2px 8px` plus `0 0 2px`, both at 10% black
- Use `ui-sans-serif` with `-apple-system` fallback — the optical sizing is doing free work
- Limit weights to 400 / 600 / 700 — the three-weight economy is the calm
- Apply the blue accent (`#2576eb`) only where it must signal action or focus
- Use graduated border-radius (3 → 6 → 10.8 → 12.8 → 18px) for hierarchy
- Pad buttons asymmetrically (`7.12px 16.96px`) — horizontal emphasis is Apple-native
- Use `scale(0.95)` transform on active press, not color darkening — physicality over palette
- Let the paper canvas breathe between cards — 81px section spacing is right, 40px is not

### Don't
- Don't use pure white (`#ffffff`) as the page background — Paper is always the backdrop
- Don't add gradient fills, glassmorphism, or backdrop blurs — Things is flat color + shadow
- Don't darken buttons on hover — use the subtle lift shadow (`0 2px 4px` at 5%) instead
- Don't use cool blue-grays like `#64748d` — the Things grays have a warmer cast (`#55606e`, `#8e9196`)
- Don't introduce a second accent color — blue is the only chromatic voice in the system
- Don't use pill (`9999px`) radius on buttons — the Apple-native 7.6px is specific and right
- Don't use heavy drop shadows (>10% opacity, >12px blur) — the signature is restraint
- Don't use custom web fonts — `ui-sans-serif` IS the font; loading Inter is a downgrade
- Don't use letter-spacing tricks — SF Pro is self-spacing, normal is correct
- Don't stack too many elevation levels — Level 0, Level 2 (signature), and Level 5 (focus) cover 90% of use cases

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile XS | <340px | Minimum layout, single column, compact padding |
| Mobile | 340–479px | Single column, 48–56px vertical section spacing |
| Mobile Large | 480–620px | Slightly roomier padding, still single column |
| Tablet | 620–899px | 2-column grids begin (testimonials), condensed nav |
| Small Desktop | 899–1002px | 3-column grids, expanded nav |
| Desktop | 1002–1106px | Full 4-column testimonial grid, 1106px max container |
| Large Desktop | ≥1106px | Centered content with generous side margins |

### Touch Targets
- Buttons use `7.12px × 16.96px` padding, yielding ~42px minimum tap height on mobile
- Nav links: 16px font at generous padding for thumb navigation
- Check-circle interactive area: always ≥ 44px hit zone even when visual circle is 20px
- Form inputs: 8px padding + 16px font = ~40px tap target

### Collapsing Strategy
- **Navigation**: Horizontal link bar → hamburger toggle below tablet breakpoint
- **Testimonial grids**: 4-column → 2-column → single column
- **Hero typography**: 36px → 28px → 24px progressive scaling, weight 700 maintained
- **Section spacing**: 81px desktop → 48px mobile (strong compression, maintains rhythm)
- **Card radius**: 18px holds at all breakpoints — no down-rounding
- **Shadows**: Signature shadow holds at all breakpoints — it's cheap and the feel is non-negotiable

### Image Behavior
- Product screenshots (the Things app UI shown in context) maintain their own rounded corners
- Testimonial avatars: always 32px circular
- No art-direction breakpoint swaps — same images served across breakpoints
- Images inside cards: often clipped to match the card radius (3–5px for thumbnails)

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: "Things Blue (`#2576eb`)" or softer "`#4f91fb`" for button fill
- Page Background: "Paper (`#f2f5f7`)"
- Card Surface: "Pure White (`#ffffff`)"
- Primary Text: "Charcoal (`#303336`)"
- Secondary Text: "Blue-Gray (`#55606e`)"
- Tertiary Text: "Stone (`#8e9196`)"
- Border: "Border Cool (`#dfe3e8`)"
- Focus Ring: "`rgba(37, 118, 235, 0.5) 0px 0px 0px 2px`"
- Signature Shadow: "`rgba(0, 0, 0, 0.1) 0px 2px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 2px 0px`"

### Example Component Prompts
- "Create a hero section on Paper (`#f2f5f7`) with a headline at 36px `ui-sans-serif` weight 700, line-height 1.00, color Charcoal (`#303336`). Subtitle at 18px weight 400, line-height 1.35, color Blue-Gray (`#55606e`). Primary CTA: background `#4f91fb`, white text, 16.96px weight 700, padding `7.12px 16.96px`, radius 7.6px, signature shadow on hover."
- "Design a testimonial card on Pure White (`#ffffff`) with 18px border-radius and the signature Things shadow (`rgba(0, 0, 0, 0.1) 0px 2px 8px 0px, rgba(0, 0, 0, 0.1) 0px 0px 2px 0px`). Internal padding 27px. Quote text at 15.3px weight 400 Charcoal, attribution name at 15.3px weight 700, date at 13px weight 400 Stone."
- "Build an input field: 1px solid `#dfe3e8` border, 6.4px radius, `8px` padding, 16px `ui-sans-serif` weight 400 Charcoal text. Focus: border becomes transparent, box-shadow `rgba(37, 118, 235, 0.5) 0px 0px 0px 2px`."
- "Create a check-circle: 20px diameter, 1.5px stroke `#dfe3e8`, transparent fill. On checked state, fill becomes Things Blue (`#2576eb`) with white checkmark glyph, scale-bounce animation."
- "Design a nav bar: white background, 1px shadow bottom (`rgba(38, 52, 74, 0.15) 0px 1px 0px 0px`). Links at 16px weight 400 Charcoal, hover: underline. Primary CTA right-aligned using the Things Blue button spec."

### Iteration Guide
1. Always start on the Paper canvas (`#f2f5f7`) — never pure white page background
2. Use the signature dual-layer shadow on every elevated card — the formula is invariant
3. Weights are 400 / 600 / 700 only — no 300, no 500, no 800 anywhere
4. Use the system font stack (`ui-sans-serif`, `-apple-system`) — custom fonts are a downgrade
5. Border-radius is graduated: 3px inline, 6–7.6px buttons, 10.8–12.8px panels, 18px featured cards
6. Button hover uses the subtle lift shadow (`0 2px 4px` at 5%), not a color change
7. Button active uses `scale(0.95)`, not background darkening
8. The blue accent (`#2576eb`) is sacred — reserve it for primary CTAs, links, focus rings, and check-circles
9. Focus states are always the blue ring shadow at 50% opacity, never outline
10. Let the paper canvas breathe — generous section spacing (81px desktop) is non-negotiable
