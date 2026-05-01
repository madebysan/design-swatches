# Design System Inspired by Are.na

## 1. Visual Theme & Atmosphere

Are.na's interface is the digital equivalent of an unstyled bibliography card — pure white paper, monospaced annotations, and content laid out like specimens on a dissecting tray. Where most "research tools" pile on Notion-style chrome, Are.na reduces UI to almost nothing: a thin top bar, a tiny footer, and between them an endless field of `#ffffff` populated by image grids, link blocks, and text excerpts. The site reads like a card catalog from a 1970s architecture school — confident, disciplined, and skeptical of decoration. Nothing draws attention to itself except the work.

The defining move is the **monospaced label paired with proportional body**. Channel titles, block counts, "by [user]" attributions, and most navigation chrome run in a system mono fallback (`areal` in production, served as a monospaced grotesque). Body content — long-form text, descriptions, comments — uses Times or a humanist serif, while UI labels stay mono. This split tells you instantly which layer you're looking at: mono = system metadata, serif = human content. It's the typographic equivalent of a museum label next to a painting.

What makes Are.na unmistakable is the **complete absence of visual lift**. No drop shadows. No card chrome. No hover scale animations. No gradient overlays. Image blocks float against white with hairline `1px` borders that are almost invisible. Buttons are white-on-white with grey text and a `3px` radius that's so subtle you'd miss it. The whole system trusts the content to carry attention — a Pinterest grid stripped of every flourish, leaving only the work and a hairline of framing.

**Key Characteristics:**
- Pure white canvas (`#ffffff`) — no off-white softening, no warmth, full clinical paper
- Monospaced (`areal`) for labels, navigation, counts; serif/sans for body content
- Hairline `1px` borders at near-invisible greys (`#dedede`, `#f7f7f7`) frame everything
- `3px` border-radius across the system — present but barely perceptible
- Grey text scale (`#696969`, `#333333`, `#999999`) replaces typical black for hierarchy
- Single chromatic accent: `#00075f` deep navy for links and selection (no brand color)
- Image grids without chrome — blocks butt up against each other with whitespace as the only separator
- 4px base spacing grid — generous gaps that read as ascetic, not luxurious

## 2. Color Palette & Roles

### Primary
- **Are.na White** (`#ffffff`): The page canvas, panel backgrounds, button fills. Pure white — no warmth, no off-white. This is paper.
- **Near Black** (`#333333`): Primary text. Are.na avoids `#000000` — body copy and headings sit at `#333333` for a softer print-like feel.
- **Mid Grey** (`#696969`): Secondary text, default link color, metadata, attributions. The workhorse text tone.

### Brand Accent
- **Are.na Navy** (`#00075f`): The signature accent — applied to active links, selection states, and the "Sign up" CTA. Almost-black blue that reads as ink rather than UI color. The only saturated hue in the system.

### Neutrals & Text Hierarchy
- **Near Black** (`#333333`): Headings, body, primary text
- **Mid Grey** (`#696969`): Secondary text, links default state, "by [user]" attributions
- **Light Grey** (`#999999`): Tertiary metadata, inactive UI, placeholder text
- **Subtle Grey** (`#dedede`): Hairline borders, divider lines
- **Faint Grey** (`#f7f7f7`): Hover surfaces, alternate row backgrounds, subtle panel tint
- **White** (`#ffffff`): All primary backgrounds and surfaces

### Status & Utility Colors
- **Alert Orange** (`#e15100`): System warnings, error states, premium upgrade markers. Used sparingly — Are.na almost never displays it on the public site.
- **Success Green** (`#238020`): Confirmation states, valid input feedback
- **Pale Green** (`#b4d6b3`): Success surface tint, gentle confirmation backgrounds
- **Warning Red** (`#b93d3d`): Destructive action confirmation, delete buttons
- **Deep Navy** (`#00075f`): Primary link color, focus states, "active" selection

### Borders & Surfaces
- **Hairline Border** (`#dedede`): Standard `1px` border on inputs, channel cards, image block frames
- **Whisper Border** (`#f7f7f7`): Soft section dividers, alternate-row backgrounds
- **Border Transparent** (`rgba(0, 0, 0, 0)`): Default ghost-button state — border only appears on hover

### Gradient System
- Are.na is **gradient-free**. The system uses solid flats and hairline borders. No fades, no overlays, no scrims on imagery. Where competitors use gradient mesh backgrounds, Are.na uses a single layer of white.

## 3. Typography Rules

### Font Family
- **Mono / UI**: `areal` with fallbacks `Arial, Helvetica` — Are.na's custom monospaced grotesque used for navigation, labels, channel titles, counts, button text
- **Serif / Body**: `Times` (system serif) — used for long-form text, descriptions, block content, comments
- **Fallback chain**: `areal Fallback, Arial, Helvetica, Arial, Helvetica` — explicitly redundant for cross-platform parity
- **OpenType Features**: System defaults only — no stylistic alternates, no ligature flourishes. The mono character is enough.

*Note: `areal` is Are.na's proprietary face. For external implementations, `JetBrains Mono`, `IBM Plex Mono`, or `Söhne Mono` work as substitutes. For the serif body, fall back to `Times New Roman` or `Iowan Old Style`.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Heading 1 | areal | 16px (1.00rem) | 700 | 1.45 | normal | Page titles, channel headers — bold but small |
| Heading 1 (Serif) | Times | 16px (1.00rem) | 400 | 1.00 | normal | Editorial headers, blog posts, About copy |
| Body | areal | 16px (1.00rem) | 400 | 1.45 | normal | Standard reading text, channel descriptions |
| Link Default | areal | 16px (1.00rem) | 400 | 1.00 | normal | Clickable navigation, channel links |
| Link Bold | areal | 16px (1.00rem) | 700 | 1.45 | normal | Emphasized links, current section indicators |
| Sub-link | areal | 14.4px (0.90rem) | 700 | tight | normal | Secondary navigation, channel meta |
| Button | areal | 12.5px (0.78rem) | 700 | tight | normal | All button text — small, bold, mono |
| Caption | areal | 12.5px (0.78rem) | 400 | 1.35 | normal | Block timestamps, "X blocks" counts, attributions |

### Principles
- **Mono for chrome, serif for content**: Areal carries every UI element — nav, labels, buttons, counts, channel titles. Times appears only when human-authored prose enters the layout (descriptions, comments, About text). The split is structural, not decorative.
- **Small type, generous space**: Are.na's largest type is 16px. There is no display heading. Hierarchy comes from weight (400 vs 700), color (`#333` vs `#696969` vs `#999`), and surrounding whitespace — never from scale escalation.
- **Two weights only**: Regular (400) and bold (700). No light, no medium, no semibold. The mono face does not need intermediate weights to communicate hierarchy.
- **Tight chrome line-heights**: Buttons and small labels run at line-height 1.00 (or near-zero / tight) to lock UI into compact horizontal blocks. Body text runs at 1.35–1.45 for readability.
- **No letter-spacing tricks**: Tracking is normal at every size. The mono face's intrinsic spacing carries the rhythm — no `-0.02em` or `0.05em` adjustments.
- **No uppercase**: Are.na never uses ALL CAPS as a stylistic choice. Sentence case throughout, including buttons and nav.

## 4. Component Stylings

### Buttons

**Default Ghost (White)**
- Background: White (`#ffffff`)
- Text: Near Black (`#333333`)
- Padding: ~6px 12px (compact)
- Radius: `3px`
- Border: `1px solid rgba(0, 0, 0, 0)` default — invisible until hover
- Hover: border becomes `1px solid #dedede`, background shifts faintly to `#f7f7f7`
- Outline: `rgb(51, 51, 51) none 3px` for keyboard focus
- Font: 12.5px areal weight 700, sentence case
- Use: Most buttons in the interface — "Add", "Edit", "Filter", "Sort"

**Primary Navy CTA**
- Background: White (`#ffffff`) or transparent
- Text: Are.na Navy (`#00075f`)
- Border: `1px solid #00075f` on emphasized variants
- Radius: `3px`
- Font: 12.5px areal weight 700
- Use: "Sign up", "Subscribe to Premium", "Create channel" — the high-intent actions

**Text Link Button**
- Background: transparent
- Text: Mid Grey (`#696969`) default, Are.na Navy (`#00075f`) on hover/active
- No border, no padding, no radius
- Font: 16px areal weight 400
- Use: Inline navigation, "view all", footer links

**Destructive**
- Background: White
- Text: Warning Red (`#b93d3d`)
- Border: `1px solid #b93d3d` on hover
- Radius: `3px`
- Use: "Delete channel", "Remove block", "Disconnect"

### Cards & Containers

**Image Block**
- Background: White (`#ffffff`)
- Border: `1px solid #dedede` — hairline frame
- Radius: `3px`
- Padding: `0` — image fills to the border
- Shadow: none
- Caption: 12.5px areal weight 400 in `#696969`, sits below the block with ~6px gap

**Channel Card**
- Background: White
- Border: `1px solid #dedede`
- Radius: `3px`
- Padding: 15–20px
- Title: 16px areal weight 700 in `#333333`
- Meta: 12.5px areal weight 400 in `#696969` ("X blocks · by username")

**Text Block**
- Background: White
- Border: `1px solid #dedede`
- Radius: `3px`
- Padding: 20px
- Body: Times 16px in `#333333`
- Source attribution: 12.5px areal in `#999999`, bottom-aligned

### Badges / Tags / Pills
**Channel Privacy Tag**
- Background: White
- Text: Mid Grey (`#696969`)
- Border: `1px solid #dedede`
- Padding: 2px 6px
- Radius: `3px`
- Font: 12.5px areal weight 400
- States: "Public", "Private", "Closed"

**Premium Marker**
- Background: White
- Text: Alert Orange (`#e15100`) — the only place this color appears
- Font: 12.5px areal weight 700
- Use: "Premium" subscriber badges, system status

### Inputs & Forms
- Background: White (`#ffffff`)
- Border: `1px solid #dedede` default
- Radius: `3px`
- Font: 16px areal weight 400
- Text color: `#333333`
- Placeholder: `#999999`
- Padding: 8–12px vertical, 12px horizontal
- Focus: border shifts to `#696969` or `#00075f`, no glow ring
- Search input: identical styling — Are.na does not differentiate search inputs

### Navigation
- Top nav: thin horizontal bar, ~50px tall, `1px` bottom border in `#dedede`
- Logo: "Are.na" wordmark in areal weight 700, `#333333`, left-aligned
- Right side: "Log in" / "Sign up" links, both in areal 16px weight 400
- Profile nav (logged in): tiny avatar circle + username in mono, dropdown chevron
- Hover: text color shifts from `#696969` to `#333333` or `#00075f`
- No mega-menus. No animated drawers. Click goes to a new page.
- Footer: even thinner — small mono links to About, Premium, Terms, separated by middle dots

### Decorative Elements

**Hairline Divider**
- `1px solid #dedede` horizontal rule
- Used between sections, around blocks, as the primary "edge" of every container
- Are.na's depth system is borders, not shadows

**Block Grid**
- Image blocks arranged in flexible columns (typically 4 across desktop, 2 on tablet, 1 on mobile)
- Gap between blocks: ~15–20px
- Blocks vary in aspect ratio — Are.na does not crop to uniform tiles
- The grid breathes; it does not lock

## 5. Layout Principles

### Spacing System
- Base unit: `4px` (per dembrandt extraction)
- Common scale: `5px`, `15px`, `20px`, `29.4px`, `35px`, `100px`
- Notable: Are.na uses non-multiple-of-8 values like `15px`, `29.4px`, `35px` — the system was built on a 4px grid before that became convention. Mid-range values (`15–35px`) dominate; large gaps (`100px+`) appear only at section transitions.

### Grid & Container
- Max content width: typically full-viewport with side padding (~20–35px gutters)
- Channel index pages: flexible column grid that adapts to viewport
- Channel detail pages: 4-column block grid on desktop, 2 on tablet, 1 on mobile
- Long-form pages (About, Premium, blog): centered single-column at ~640–720px max-width
- No max-width container locks content at 1200px — Are.na lets its grids stretch

### Whitespace Philosophy
- **Ascetic, not luxurious**: Are.na's whitespace reads as restraint, not generosity. The space exists to give blocks room to be seen, not to perform "premium spacing".
- **Content density at the edges**: The top nav and footer are remarkably compact (~50px and smaller). All breathing room concentrates around the actual content.
- **No decorative gaps**: There are no `200px` empty sections between feature blocks. Sections butt up against each other with hairline borders or `~35px` of padding.

### Border Radius Scale
- Hairline (`3px`): The only radius in the system. Applied to buttons, cards, inputs, image blocks, badges. Present but barely visible.
- No `0px` sharp corners (Are.na is not aggressive)
- No `8px+` radii (Are.na is not friendly-rounded)
- No pill (`9999px`) elements anywhere — even avatars use a `3px` square crop in many places, though circular avatars do appear in some contexts

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text, top-level containers |
| Hairline (Level 1) | `1px solid #dedede` | Default frame for blocks, cards, inputs — the workhorse depth |
| Soft Tint (Level 2) | Background shifts to `#f7f7f7` | Hover states, alternate rows, subtle panel emphasis |
| Active Border (Level 3) | `1px solid #696969` or `#00075f` | Focus states on inputs, selected channels |
| Outline Focus (Level 4) | `rgb(51, 51, 51) none 3px` outline | Keyboard focus on buttons — system outline, no glow |

**Shadow Philosophy**: Are.na's depth system is **lines, not light**. There are no drop shadows anywhere on the public site. No `box-shadow: 0 4px 12px rgba(0,0,0,0.1)`. No subtle elevation. Containers are differentiated by hairline borders (`#dedede`) or background tints (`#f7f7f7`), never by simulated lift. The result is a flat, printed quality — closer to a well-designed reference book than a contemporary web app. When emphasis is needed, it comes from a slightly darker border or a slightly tinted background, never from a shadow.

### Decorative Depth
- The hairline `#dedede` border is the system's signature — appears on virtually every framed element
- Hover lifts use `#f7f7f7` tint instead of shadow growth
- Selected/focused states use color shifts (`#00075f` border) rather than glow rings
- No 3D effects, no neumorphism, no skeuomorphism

## 7. Do's and Don'ts

### Do
- Use pure white (`#ffffff`) for backgrounds — no off-white, no cream, no warmth
- Pair monospaced (`areal`) for UI/labels with serif (`Times`) for body content — the typographic split is structural
- Apply hairline `1px solid #dedede` borders on every framed element — this is the depth system
- Use `3px` border-radius across all rounded surfaces — never sharper, never softer
- Lean on grey hierarchy (`#333333` → `#696969` → `#999999`) instead of weight or scale jumps
- Reserve Are.na Navy (`#00075f`) for active links and emphasized CTAs — the only saturated hue allowed
- Keep type small (16px max for body, 12.5px for chrome) — hierarchy is structural, not scale-driven
- Use weight 400 and 700 only — no medium, no semibold
- Let image blocks butt up against each other in flexible grids — no enforced uniform crops
- Use `#f7f7f7` background tint for hover states instead of shadow lift

### Don't
- Don't use drop shadows anywhere — depth comes from hairlines, not light
- Don't use display-size headings (>24px) — Are.na's largest UI text is 16px
- Don't introduce gradient backgrounds, mesh fills, or scrim overlays — solid white only
- Don't use uppercase as a stylistic device — sentence case throughout
- Don't use rounded corners larger than `3px` — the system is restrained, not friendly
- Don't introduce additional brand colors beyond the navy — the system is monochrome plus navy
- Don't use bold weight for body text — `#333333` at weight 400 is heavy enough
- Don't add icons inside buttons — Are.na buttons are text-only
- Don't animate hover states beyond instant tint shifts — no transitions longer than 150ms
- Don't use sans-serif for body content where serif (Times) is appropriate — the split matters
- Don't crop images uniformly to enforce grid alignment — variable aspect ratios are part of the language

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <600px | Single-column block grid, stacked nav, collapsed channel list |
| Tablet | 600–960px | 2-column block grid, condensed nav, side panels collapse |
| Desktop | 960–1280px | 3–4 column block grid, full nav, sidebar visible |
| Large Desktop | ≥1280px | 4–5 column block grid, generous outer padding |

### Touch Targets
- Buttons: ~30–36px tap height (Are.na is unusually compact, but mobile padding expands)
- Nav links: ~44px tap area on mobile despite small visual size
- Image blocks: full block is tappable, no overlay required
- Form inputs: ~40px height on mobile

### Collapsing Strategy
- **Nav**: Top bar stays visible at all breakpoints; secondary nav collapses to a menu icon on mobile
- **Block grid**: 4 → 3 → 2 → 1 columns depending on viewport, with consistent ~15px gap
- **Channel sidebar**: Visible on desktop, slides up as a sheet on mobile
- **Long-form pages**: Centered column tightens to viewport width minus ~20px padding on mobile
- **Type scale**: Body type stays at 16px across all breakpoints — Are.na does not scale text by viewport
- **Images**: Block grid switches column count; individual block aspect ratios are preserved

### Image Behavior
- Block grids reflow column counts; images never crop or stretch to fit
- Featured images on channel pages compress proportionally
- No art direction swaps — desktop and mobile see the same image at different sizes
- Lazy-loading for off-screen blocks; no blur-up placeholder, just empty white space until load

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA (high intent): Are.na Navy (`#00075f`) on white
- Default Button: White (`#ffffff`) with `#333333` text and `1px solid #dedede` border on hover
- Page Background: Pure White (`#ffffff`)
- Primary Text: Near Black (`#333333`)
- Secondary Text: Mid Grey (`#696969`)
- Tertiary Text: Light Grey (`#999999`)
- Hairline Border: `1px solid #dedede`
- Hover Surface: Faint Grey (`#f7f7f7`)
- Focus Outline: `rgb(51, 51, 51) none 3px`

### Example Component Prompts
- "Create a hero section on pure white (`#ffffff`) with a heading at 16px areal (or JetBrains Mono fallback) weight 700 in `#333333`, and supporting body in Times 16px weight 400 in `#333333`. No display-size type. Add a 'Sign up' link in `#00075f` weight 700 inline."
- "Design a channel card on `#ffffff` with `1px solid #dedede` border, `3px` radius, 20px padding. Title in 16px areal weight 700 in `#333333`. Meta line below in 12.5px areal weight 400 in `#696969` reading 'X blocks · by username'. No shadow. No icon."
- "Build an image block grid — 4 columns desktop, 2 tablet, 1 mobile. Each block is a `1px solid #dedede` framed image with `3px` radius, no shadow, white background. Below the image: caption in 12.5px areal weight 400 in `#696969`."
- "Create a default button — white background, `#333333` text, 12.5px areal weight 700, 6px×12px padding, `3px` radius, `1px solid rgba(0,0,0,0)` border that becomes `1px solid #dedede` on hover. No icons."
- "Design a search input — white background, `1px solid #dedede` border, `3px` radius, 16px areal text in `#333333`, placeholder in `#999999`, 12px padding. Focus shifts border to `#00075f`. No drop shadow, no glow ring."
- "Build a long-form article page — centered Times 16px body in `#333333` at 1.45 line-height, max-width 640px, white background. Section breaks use `1px solid #dedede` hairline rules. Inline links in `#00075f` weight 400."

### Iteration Guide
1. White is the canvas — never substitute off-white, cream, or grey backgrounds
2. Mono for chrome (areal/JetBrains Mono), serif for content (Times) — never mix the assignments
3. The depth system is hairlines (`1px solid #dedede`), not shadows — refuse drop shadow requests
4. `3px` is the only border-radius — not 0, not 8, not pill
5. Type stays small: 16px ceiling for content, 12.5px for chrome — no display headings
6. Two weights: 400 and 700. No medium, no semibold, no light
7. Grey scale (`#333` → `#696969` → `#999999`) replaces typical bold/light hierarchy
8. Are.na Navy (`#00075f`) is the only chromatic accent — use it sparingly for active links and primary CTAs
9. Hover states tint backgrounds (`#f7f7f7`) or shift borders, never lift via shadow
10. Sentence case everywhere — never uppercase, never small caps
