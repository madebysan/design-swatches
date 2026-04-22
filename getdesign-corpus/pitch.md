# Design System Inspired by Pitch

## 1. Visual Theme & Atmosphere

Pitch is what happens when presentation software stops apologizing for being software. The homepage opens onto a violet-lavender gradient wash — a painterly, atmospheric backdrop that refuses to be a flat hex value — and then places a single, enormous Mark Pro headline (`#2b2a35`, weight 800, tight line-height) across it. The effect is immediately theatrical: the marketing surface behaves less like a SaaS landing page and more like the inside of a deck itself, where color is a stage and typography is the performer. Pitch's craft is about dimensional depth on a surface most tools leave flat — frosted navigation chrome, floating product dashboards with soft violet-tinted shadows, and panel stacks that suggest a deep z-axis rather than a single plane.

Where Linear and Stripe render restraint, Pitch renders **confidence**. The palette is narrow but saturated: a near-black charcoal-violet (`#2b2a35`) for type, a signature electric violet (`#6b53ff`) for interactive moments, and a deeper display purple (`#8d49f7`) that appears as the brand's louder voice. Layered behind all of it are soft lavender-to-periwinkle gradient meshes — never hard stops, always blended — that give the page an ambient, lit-from-within quality. Mark Pro at 90px / weight 800 / -1.8px tracking dominates the hero; Eina01 handles body, links, and buttons at a quieter 16–18px with generous 2.00 line-height for breathing room. The contrast between heavy display type and airy body copy is deliberate: it's how decks work — a big claim, then space to absorb it.

The glassmorphic treatment shows up in the second fold, where the live product UI (Links overview, Sales Proposal) is rendered as a **frosted floating panel** on top of the violet gradient: a translucent white-ish background around `rgba(255, 255, 255, 0.72)`, a whisper-thin `1px solid rgba(255,255,255,0.4)` border, a soft 8–14px radius, and a diffuse `rgba(0,0,0,0.15) 0px 3px 10px` shadow that grounds it without anchoring it. The panel doesn't sit *on* the page — it hovers over the gradient, which bleeds through subtly from behind. This is the defining Pitch move: **glass as a product surface, not just a decorative flourish**. Every floating card, nav bar, modal, and hover state inherits this treatment. Presentation tools are about what's in front and what's behind; Pitch's UI makes the z-axis visible.

**Key Characteristics:**
- Dark-violet primary text (`#2b2a35`) on lavender-gradient backgrounds — never pure black on white
- Brand electric violet (`#6b53ff`) as interactive accent, display purple (`#8d49f7`) for marketing emphasis
- Mark Pro at weight 800 for display (90px / 60px / 42px) with aggressive negative tracking (-1.8px at 90px)
- Eina01 at weight 400–700 for body, buttons, links, and UI (13px–22px)
- Button text treatment: uppercase, weight 700, 14px, 1.4px letter-spacing — a stamp-like confidence
- Glassmorphic floating panels: `backdrop-filter: blur(20px)`, `rgba(255,255,255,0.72)` fill, 8–14px radius
- Gradient meshes as ambient background, never as fill — radial violet/lavender bloom behind hero content
- Soft layered shadows in violet-tinted rgba: `rgba(0,0,0,0.15) 0px 3px 10px` (standard), `rgba(43,42,53,0.25) 0px 6px 27px` (elevated)
- Yellow accent `#ffd02c` as highlight stamp (9px solid border on callout divs) — playful punctuation in an otherwise violet system
- 8px base spacing, 12px / 20px / 28px / 30px / 40px / 60px / 120px rhythm
- Radius scale: 3px (inline tags), 6px (buttons), 8px (cards), 12–14px (panels), 20–26px (featured cards), 50% (pill/circle)

## 2. Color Palette & Roles

### Brand & Accent
- **Pitch Violet** (`#6b53ff`): The signature brand color. Primary CTA backgrounds, active states, interactive accents, selected items. Electric, confident, unmistakably Pitch.
- **Display Purple** (`#8d49f7`): The louder voice — marketing graphics, gradient stops, link hover highlights. Warmer and more saturated than Pitch Violet, used for emphasis rather than action.
- **Violet Hover** (`#586ee0`): Pressed/active variant of Pitch Violet — slightly shifted blue.
- **Lavender Wash** (`rgb(240, 239, 244)`): The atmospheric background tint — not a surface color, a *field* color. Logos and image safe zones use this as their canvas.

### Text & Ink
- **Charcoal Violet** (`#2b2a35`): Primary text and ink color. A near-black with a purple-cool undertone — never use pure `#000`. Headlines, body text, solid UI chrome.
- **Deep Violet Panel** (`#1e1d28`): Dark panel background — marginally deeper than charcoal violet for stacked dark surfaces.
- **Pure White** (`#ffffff`): Card surfaces, reversed text on dark sections, glass panel fill base (before transparency).
- **True Black** (`#000000`): Reserved for extreme contrast moments — not the default ink color.

### Accent & Highlight
- **Highlight Yellow** (`#ffd02c`): Playful accent — used as 9px solid border strokes on callout divs, highlight swashes on key words. The unexpected warm note in an otherwise cool palette.
- **Warm Alert** (`#ffa000`): Dashed-border warning treatment for emphasis states.

### Neutrals & Borders
- **Border Soft** (`rgb(221, 223, 229)`): Default 1px border on images, cards, and dividers.
- **Border Cool** (`rgb(215, 216, 224)`): Slightly cooler card border variant.
- **Border Ink** (`#2b2a35`): Solid dark border used for high-contrast dividers (tab bottoms, sidebar edges).

### Glass & Atmosphere
- **Glass White** (`rgba(255, 255, 255, 0.72)`): The glass panel fill. Pair with `backdrop-filter: blur(20px)`.
- **Glass Border** (`rgba(255, 255, 255, 0.4)`): The characteristic frost-edge border on glass panels.
- **Glass Dark** (`rgba(30, 29, 40, 0.6)`): Dark-mode glass — deep panel at 60% opacity with blur.
- **Gradient Stop Top** (`#b9a7ff`): Lavender starting stop for background mesh.
- **Gradient Stop Bottom** (`#6b53ff`): Violet ending stop — the mesh resolves into brand.

### Quick Reference Matrix
| Role | Token | Hex |
|------|-------|-----|
| Primary CTA | Pitch Violet | `#6b53ff` |
| Marketing emphasis | Display Purple | `#8d49f7` |
| Primary ink | Charcoal Violet | `#2b2a35` |
| Dark panel | Deep Violet Panel | `#1e1d28` |
| Highlight | Highlight Yellow | `#ffd02c` |
| Glass fill | Glass White | `rgba(255,255,255,0.72)` |
| Atmospheric field | Lavender Wash | `rgb(240,239,244)` |

## 3. Typography Rules

### Font Families
- **Display**: `Mark Pro`, fallback `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`
- **Body / UI**: `Eina01`, same fallbacks
- **Emoji**: `"Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"`
- **No variable fonts, no OpenType feature flags** — Pitch runs classic static weights

### Hierarchy

| Role | Font | Size | Weight | Line Height | Tracking | Transform |
|------|------|------|--------|-------------|----------|-----------|
| Display XL | Mark Pro | 90px (5.63rem) | 800 | 1.00 | -1.8px | — |
| Display Large | Mark Pro | 60px (3.75rem) | 800 | 1.00 | -1.2px | — |
| Display | Mark Pro | 42px (2.63rem) | 800 | 1.40 | -0.84px | — |
| Heading 1 | Eina01 | 28px (1.75rem) | 800 | 1.20 | — | — |
| Heading 2 | Eina01 | 28px (1.75rem) | 700 | 1.40 | — | — |
| Heading 3 | Mark Pro | 27px (1.69rem) | 800 | 1.40 | -0.54px | — |
| Intro Large | Eina01 | 22px (1.38rem) | 400 | 2.00 (airy) | — | — |
| Body Large | Eina01 | 18px (1.13rem) | 400 | 1.30 | — | — |
| Body Large Bold | Eina01 | 18px (1.13rem) | 700 | 1.30 | — | — |
| Link / Body | Eina01 | 16px (1.00rem) | 400 | 2.00 | — | — |
| Link Bold | Eina01 | 16px (1.00rem) | 700 | 1.10 | — | — |
| Button | Eina01 | 14px (0.88rem) | 700 | normal | 1.4px | UPPERCASE |
| Caption | Eina01 | 13px (0.81rem) | 400 | 1.00 | — | — |
| Label | Mark Pro | 13px (0.81rem) | 700 | 1.85 | 1.3px | UPPERCASE |

### Principles
- **Mark Pro 800 is the stage voice.** Headlines use weight 800 at every display size. Mark Pro only appears at weight 800 — it's a "make a statement" weight.
- **Eina01 is the conversation.** Body, links, buttons, captions — Eina01 runs the UI at weights 400 and 700. The contrast between heavy Mark Pro display and lighter Eina01 body is the signature typographic rhythm.
- **Airy body line-heights.** 2.00 line-height on 16–22px body text gives paragraphs breathing room — Pitch is a pitch tool, and pitches need space between beats.
- **Tight display tracking.** Tracking scales negatively with size: -1.8px at 90px, -1.2px at 60px, -0.84px at 42px, -0.54px at 27px. Below 22px, tracking is neutral or positive for labels.
- **Uppercase buttons and labels.** Button text uses uppercase with +1.4px tracking — a small-caps signature that reads as stamp-like, confident, press-worthy.

## 4. Component Stylings

### Buttons

**Primary CTA (Violet)**
- Background: `#6b53ff`
- Text: `#ffffff`, Eina01 14px weight 700 UPPERCASE, 1.4px tracking
- Padding: `12px 20px`
- Radius: `6px`
- Hover: background `#8d49f7` (display purple shift) or lightens with rgba overlay
- Use: "Sign up for free", "Get a demo" — all primary actions

**Secondary (Ghost)**
- Background: transparent
- Text: `#2b2a35`, same typography as primary
- Border: `1px solid #2b2a35`
- Padding: `12px 20px`
- Radius: `6px`
- Hover: background `rgba(43,42,53,0.08)`

**Nav Carousel Button (Circular)**
- Background: `#ffffff`
- Color: `#000000`
- Padding: `1px 6px`
- Radius: `50%`
- Shadow: `rgba(43,42,53,0.25) 0px 6px 27px 0px` or `rgba(43,42,53,0.5) 0px 6px 27px 0px`
- Hover: `rgba(0,0,0,0.1)` overlay
- Active: fills with `#6b53ff`

### Cards & Containers

**Standard Card**
- Background: `#ffffff`
- Border: `1px solid rgb(221, 223, 229)`
- Radius: `8px` (default), `12–14px` (featured), `20–26px` (large hero cards)
- Shadow: `rgba(0,0,0,0.15) 0px 3px 10px 0px`
- Padding: `20px` to `40px` depending on scale

**Glass Panel (Signature Treatment)**
- Background: `rgba(255, 255, 255, 0.72)`
- Backdrop filter: `blur(20px) saturate(140%)`
- Border: `1px solid rgba(255, 255, 255, 0.4)`
- Radius: `12px` or `14px`
- Shadow: `rgba(0, 0, 0, 0.15) 0px 4px 30px 0px` + `rgba(107, 83, 255, 0.12) 0px 0px 0px 1px` (violet ambient rim)
- Use: Floating product dashboards, modals, toolbar overlays, navigation on gradient backgrounds
- **Always requires a gradient or image behind it** — the blur is the point

**Dark Glass Panel**
- Background: `rgba(30, 29, 40, 0.6)`
- Backdrop filter: `blur(24px)`
- Border: `1px solid rgba(255, 255, 255, 0.08)`
- Shadow: `rgba(43, 42, 53, 0.5) 0px 6px 27px 0px`

### Inputs & Forms

**Text Input**
- Background: `#ffffff`
- Text: `#2b2a35`, Eina01 16px weight 400
- Border: `1px solid rgb(221, 223, 229)`
- Padding: `12px 14px`
- Radius: `6px`
- Focus: border `#6b53ff`, shadow `0 0 0 3px rgba(107, 83, 255, 0.18)`

### Badges & Chips

**Violet Badge**
- Background: `rgba(107, 83, 255, 0.12)`
- Text: `#6b53ff`
- Padding: `4px 10px`
- Radius: `20px` (pill)
- Font: Eina01 12px weight 700 uppercase, 1.2px tracking

**Yellow Callout Stamp**
- 9px solid `#ffd02c` border on a `<div>`, often skewed or rotated
- Use: Playful emphasis, onboarding highlights, "new" stamps

### Navigation

- Pitch logo left, horizontal nav center (Product, Use Cases, Templates, Resources, Pricing), CTAs right
- Links: Eina01 16px weight 400, color `#2b2a35`, hover `#6b53ff`
- "Sign up" CTA is filled violet, "Log in" is ghost
- Mega-menu dropdowns on hover: **glass panel treatment** — `rgba(255,255,255,0.96)` with `blur(20px)`, 12px radius, soft shadow

## 5. Layout Principles

### Spacing System
- Base unit: 4px (effective grid runs on 4px multiples)
- Primary rhythm: 12px, 20px, 28px, 30px, 40px, 60px, 120px
- Micro-adjustments: 2px, 6px, 10px for optical tuning
- Large sections: 120px vertical padding — Pitch breathes

### Grid
- Max content width: approximately 1280px
- Hero: centered single-column, headline max-width ~900px
- Feature rows: 2-column (image + copy) or 3-column cards
- Product demo sections: full-bleed gradient background with floating glass UI centered

### Whitespace Philosophy
- **The gradient IS the whitespace.** Pitch's violet-lavender mesh is ambient, atmospheric — empty space isn't white, it's colored air. Content floats on top of it via glass panels and shadow-lifted cards.
- **Enormous display type + airy body.** 90px headlines followed by 22px intro copy with 2.00 line-height: a rhythm of punch and pause.
- **Generous vertical breaks.** 120px between major sections, 60–80px between subsections.

### Border Radius Scale
- Micro (3px): Inline tags, badge corners on pills
- Button (6px): Standard buttons, inputs, select dropdowns
- Card (8px): Default cards, images, videos
- Panel (12–14px): Featured cards, images with rounded tops, product panels
- Feature (20–26px): Hero illustration cards, large floating dashboards
- Jumbo (56px): Hero illustration frames
- Full (50%): Circular nav buttons, avatars, status dots

## 6. Depth & Elevation — Glass, Gradient, and Layered Frost

Pitch's depth language is **atmospheric, not architectural**. Linear stacks background luminance. Stripe uses blue-tinted drop shadows. Pitch layers *frosted panels over gradient air*, using backdrop-filter blur as the depth cue. Below the visible layer of product UI, a gradient mesh drifts; above it, a semi-transparent glass surface catches light. The combination creates the illusion of depth on a 2D canvas — not through shadow alone, but through **optical parallax**: the blur reveals what's behind without showing it sharply.

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, gradient background `linear-gradient(180deg, #b9a7ff 0%, #6b53ff 100%)` or lavender wash `rgb(240,239,244)` | Page background, section backdrops |
| Whisper (Level 1) | `rgba(0,0,0,0.15) 0px 3px 10px 0px` | Standard cards, images, small components |
| Lifted (Level 2) | `rgba(0,0,0,0.15) 0px 4px 30px 0px` | Featured cards, hover states on product tiles |
| Floating (Level 3) | `rgba(103, 110, 144, 0.2) 0px 8px 26px 0px` | Modals, tooltips — shadow has cool gray tint |
| Deep Float (Level 4) | `rgba(43, 42, 53, 0.25) 0px 6px 27px 0px` | Nav controls, floating carousel buttons |
| Theatrical (Level 5) | `rgba(43, 42, 53, 0.5) 0px 6px 27px 0px` | Dark-section elevated elements, dramatic CTAs |

### The Glass Recipe (Signature)

```css
.glass-panel {
  background: rgba(255, 255, 255, 0.72);
  backdrop-filter: blur(20px) saturate(140%);
  -webkit-backdrop-filter: blur(20px) saturate(140%);
  border: 1px solid rgba(255, 255, 255, 0.4);
  border-radius: 14px;
  box-shadow:
    rgba(0, 0, 0, 0.15) 0px 4px 30px 0px,
    rgba(107, 83, 255, 0.08) 0px 0px 0px 1px inset;
}
```

**Blur values by use:**
- `blur(12px)` — subtle frost, reads almost opaque, use on busy photo backgrounds
- `blur(20px)` — **the default Pitch blur**, use on gradient or lavender backgrounds
- `blur(24px)` — heavier frost for modals and dark-mode glass, higher occlusion
- `blur(40px)` — atmospheric obscuration, for full-screen overlay scrims

**Translucent background fills:**
- Light glass: `rgba(255, 255, 255, 0.72)` — the hero panel value
- Lighter glass: `rgba(255, 255, 255, 0.88)` — nav bars on busy backgrounds
- Dark glass: `rgba(30, 29, 40, 0.6)` — dark-mode product chrome
- Ultra-dark glass: `rgba(30, 29, 40, 0.8)` — modals over gradients

### Gradient Meshes as Depth

Behind every glass panel, there should be something worth blurring. Pitch uses radial or linear gradient meshes:

```css
/* Ambient lavender-violet hero mesh */
background:
  radial-gradient(circle at 20% 30%, rgba(185, 167, 255, 0.6) 0%, transparent 50%),
  radial-gradient(circle at 80% 70%, rgba(141, 73, 247, 0.4) 0%, transparent 55%),
  linear-gradient(180deg, #e9e2ff 0%, #b9a7ff 100%);
```

The mesh is never a hard-stop gradient — it's at least two radial blooms layered over a soft linear base. Colors are always in the violet/lavender/periwinkle family, sometimes warming toward peach at the edges for playfulness.

### Shadow Philosophy

Shadows on Pitch are **soft, diffuse, and slightly violet-tinted** when they appear on dark elements. The `rgba(43, 42, 53, ...)` family of shadow colors — charcoal violet with transparency — carries the brand's cool cast into the shadow itself. On light surfaces, `rgba(0, 0, 0, 0.15)` with generous blur radii (10px, 30px) keeps shadows hazy and atmospheric rather than crisp and defined. Nothing on Pitch casts a hard shadow.

## 7. Do's and Don'ts

### Do
- Pair Mark Pro (weight 800) display with Eina01 (weight 400/700) body — the typographic rhythm is non-negotiable
- Use violet-tinted charcoal (`#2b2a35`) as your primary ink instead of pure black
- Layer glass panels over gradient meshes — the blur needs something worth blurring
- Apply `backdrop-filter: blur(20px)` generously on floating UI chrome over colored backgrounds
- Use `rgba(255, 255, 255, 0.72)` as the glass fill — not solid white, never fully opaque
- Reserve `#6b53ff` for interactive/CTA moments, `#8d49f7` for marketing emphasis
- Uppercase button text at 14px/700 weight with +1.4px tracking — Pitch's button-as-stamp signature
- Use airy line-heights (2.00) on body copy 16–22px to create presentation-like pacing
- Frame product screenshots with `1px solid rgba(255,255,255,0.4)` borders and 8–14px radius
- Add yellow `#ffd02c` 9px border strokes sparingly for playful emphasis — it's the system's punctuation

### Don't
- Don't use pure `#000000` as primary ink — `#2b2a35` carries the cool violet cast that unifies the palette
- Don't stack glass panels without something colored or gradient behind them — clear glass on white reads like a broken render
- Don't use solid fills for floating product chrome — the translucency IS the product feel
- Don't skip backdrop-filter polyfills — include `-webkit-backdrop-filter` for Safari support
- Don't pair Mark Pro at light weights — it only lives at 800; lighter UI work belongs to Eina01
- Don't use warm neutrals or cream tones in body surfaces — the palette is cool violet throughout
- Don't render hard-edged drop shadows — Pitch shadows are always diffuse (10–30px blur radius)
- Don't use gradients with hard color stops — always feather the transitions with radial blooms
- Don't use `#6b53ff` decoratively — it's reserved for CTAs, selections, and active product states
- Don't introduce more than one warm accent (`#ffd02c`) per section — it's a spice, not a sauce

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Single column, hero at 42–48px, glass panels edge-to-edge |
| Tablet | 768–1082px | Two-column starts, nav collapses to hamburger |
| Desktop Small | 1082–1399px | Full nav, standard card grids |
| Desktop | 1399–1667px | Default design viewport |
| Large Desktop | >1667px | Expanded margins, hero max-width constraint |

Observed breakpoints from the source: 1082px, 1123px, 1399px, 1667px, 1670px, 1820px.

### Collapsing Strategy
- Hero display: 90px → 60px → 42px (tracking adjusts proportionally from -1.8px to -0.84px)
- Glass panels: maintain blur at all sizes, but reduce radius from 14px → 8px on mobile
- Two-column image+copy: stacks vertically on mobile, image above
- Navigation: full links → hamburger at 1082px
- Gradient meshes: simplify from 3-radial to single-radial on mobile for performance

### Touch Targets
- All buttons: minimum 40px tall at 14px type + 12px vertical padding
- Circular nav buttons: 36–44px diameter
- Glass panels on mobile: min-height 200px to stay tappable

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Pitch Violet (`#6b53ff`)
- Marketing emphasis: Display Purple (`#8d49f7`)
- Ink: Charcoal Violet (`#2b2a35`)
- Dark panel: Deep Violet (`#1e1d28`)
- Glass fill: `rgba(255, 255, 255, 0.72)`
- Glass border: `rgba(255, 255, 255, 0.4)`
- Lavender field: `rgb(240, 239, 244)`
- Highlight: Yellow (`#ffd02c`)
- Standard shadow: `rgba(0,0,0,0.15) 0px 3px 10px 0px`
- Elevated shadow: `rgba(43,42,53,0.25) 0px 6px 27px 0px`

### Example Component Prompts
- "Create a hero section with a layered gradient mesh: `radial-gradient(circle at 20% 30%, rgba(185,167,255,0.6) 0%, transparent 50%), radial-gradient(circle at 80% 70%, rgba(141,73,247,0.4) 0%, transparent 55%), linear-gradient(180deg, #e9e2ff 0%, #b9a7ff 100%)`. Headline in Mark Pro weight 800, 90px, line-height 1.00, letter-spacing -1.8px, color `#2b2a35`. Intro copy in Eina01 weight 400, 22px, line-height 2.00. Primary CTA: `#6b53ff` background, white text, Eina01 14px weight 700 UPPERCASE, 1.4px tracking, 6px radius, 12x20px padding."
- "Build a glass product panel: `background: rgba(255,255,255,0.72); backdrop-filter: blur(20px) saturate(140%); border: 1px solid rgba(255,255,255,0.4); border-radius: 14px; box-shadow: rgba(0,0,0,0.15) 0px 4px 30px 0px`. Place over a violet gradient mesh. Inside: Eina01 14px labels, charcoal-violet `#2b2a35` text, circular nav buttons at 36px with `rgba(43,42,53,0.25) 0px 6px 27px 0px` shadow."
- "Design a pricing card: white background, 1px solid `rgb(221, 223, 229)` border, 12px radius, `rgba(0,0,0,0.15) 0px 3px 10px` shadow. Plan name in Eina01 28px weight 800. Price in Mark Pro 60px weight 800 with -1.2px tracking. Feature list in Eina01 16px weight 400 with 2.00 line-height. CTA violet `#6b53ff` full-width bottom."
- "Create a glassmorphic nav bar floating above a gradient hero: position fixed top, background `rgba(255,255,255,0.88)`, backdrop-filter blur 20px, border-bottom `1px solid rgba(255,255,255,0.4)`. Logo left, nav links Eina01 16px `#2b2a35`, Sign up CTA right in `#6b53ff`."
- "Build a testimonial with yellow-stamp highlight: quote in Mark Pro 42px weight 800, letter-spacing -0.84px. Author line in Eina01 14px weight 700 UPPERCASE with 1.4px tracking. Wrap the emphasized word in a `<mark>` with 9px solid `#ffd02c` border, slight rotation `transform: rotate(-1deg)`."

### Iteration Guide
1. Always layer glass on gradient — backdrop-filter with no colored background behind is invisible
2. Mark Pro 800 for any display moment; Eina01 400/700 for everything else — mixing them within the same role breaks the rhythm
3. Shadows should have 10–30px blur radius and low opacity (0.15–0.25) — nothing crisp, nothing black
4. Use `#2b2a35` not `#000000` — the cool violet cast is what unifies Pitch's light and dark surfaces
5. Reserve `#6b53ff` for action and `#8d49f7` for attention — they're not interchangeable
6. Button text is UPPERCASE weight 700 with +1.4px tracking — it's a press-stamp, not body copy
7. When building a glass panel, always ask: "What's behind this?" If the answer is "plain white", remove the glass treatment
