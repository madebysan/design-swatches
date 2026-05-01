---
slug: the-sun
name: The Sun
url: https://www.thesun.co.uk
domain: thesun.co.uk
category: Media
styles: [Bold, Colorful, Editorial]
tagline: "Tabloid red masthead, 104px all-caps TheSun, kicker-blue links, no whitespace anywhere."
fonts: [TheSun, Arial]
primary_color: "#eb1701"
---

# Design System Inspired by The Sun

> Tabloid red masthead, 104px all-caps TheSun, kicker-blue links, no whitespace anywhere.

## 1. Visual Theme & Atmosphere

The Sun's homepage is a printed red-top tabloid that has been digitised without losing a decibel. The site sits on pure white (`#ffffff`) for the news grid but its identity lives in the screaming red masthead (`#eb1701`) — that single value is the loudest non-photographic element on the page, used not as a brand accent but as the actual nameplate background, edge-to-edge, with the white "TheSun" wordmark sitting on it like the front page of a 1960s broadsheet. Where most modern news sites have moved to whisper-quiet grayscale grids, The Sun commits to the gutter-press visual contract: ink-red masthead, hard black headlines, photo-led story cards stacked tight, and kicker-blue (`#0072ee`) inline links blazing out of body copy.

The signature typographic move is **TheSun custom display face at 104px UPPERCASE** with a `0.88` line-height — headlines so tall and tight they touch their own descenders, set across the full width of the column the way newsstand stencils stack a front-page hed. This is the only typeface in heavy use on the page. Body copy and UI rely on Arial/serif system stacks. The site doesn't try to look refined; it tries to look loud. The same restraint that drives prestige editorial brands toward four-typeface systems drives The Sun toward one big shouter and a system-font sidekick.

The third defining trait is **density of incident**. Story cards butt against one another with hairline gray (`#bebfbf`) dividers rather than card chrome — no shadows, no rounded corners on photographs, just a row-after-row stack of headlines with photos. The rare button (`4px` radius, kicker-blue background, white Arial bold UPPERCASE) reads as an interruption against the page. The semantic palette runs hot: error red `#930600`, success green `#25661f`, highlight yellow `#fef553`, accent gold `#fcb900` — these surface in WordPress block content and editorial flags. The result is a page that looks the way the printed paper sounds: red on the top, black ink in the middle, kicker links yelling, and not a wasted pixel of whitespace.

**Key Characteristics:**
- Tabloid Red masthead (`#eb1701`) — full-bleed nameplate background, the loudest pixel on the page
- Pure white (`#ffffff`) story-grid background — newsprint, never tinted
- TheSun custom display face — 104px UPPERCASE at `0.88` line-height for tabloid-stencil heds
- Kicker Blue inline link (`#0072ee`) — every clickable phrase in body copy, never decorative
- True Black (`#000000`) and Charcoal (`#222526`) for headline ink — high-contrast story type
- Hairline gray dividers (`#bebfbf`) between stories — newspaper-pica rules, never card chrome
- `4px` button radius — almost-square, with a `12px 24px` padding — printerly, not webby
- WordPress utility palette underneath — error `#930600`, success `#25661f`, highlight `#fef553`
- Subnav border `#ff7f80` — pink-coral counterpoint to the masthead red
- Magenta tabloid accent (`#b840cc`) appears on celebrity / "Page Three" sections for visual heat
- Soft sky-blue secondary (`#3a79bb`) for less-aggressive section markers
- No box-shadows on chrome — depth is via masthead block-color and hairline rules
- Story photographs square-cut, no rounded corners, packed edge-to-edge

## 2. Color Palette & Roles

### Primary Brand
- **Tabloid Red** (`#eb1701`): The Sun masthead background, edge-to-edge nameplate, subnav fill, and brand-section bars. The single most-recognisable pixel of the system. So definitional that the entire visual identity collapses without it.
- **Kicker Blue** (`#0072ee`): The inline link colour — every clickable word in body copy, plus the "BREAKING" and CTA button fills. Deeply saturated, no decoration except underline on hover. Bootstrap-ish but pushed harder.
- **True Black** (`#000000`): Headline ink, masthead text inversions on red, body text default. Pure black, no softening.

### Brand Accent
- **Subnav Coral** (`#ff7f80`): The pink-coral border used on subnav blocks — pulled from the same warm-red family as the masthead but lighter for hierarchy.
- **Tabloid Magenta** (`#b840cc`): Celebrity / showbiz / "Page Three" section accent — pushes hot when the content is gossip-led.
- **Sky Blue** (`#3a79bb`): Less-aggressive section accent for sport / news subsections.
- **Sun Gold** (`#fcb900`): Accent-exclusive WordPress utility colour — used on premium content flags and Sun Club moments.
- **Warning Red** (`#ff4c4d`): A brighter alarm-red used for "BREAKING" tickers and live-event indicators.

### Neutrals & Text
- **Headline Black** (`#000000`): Primary headline ink, masthead inverse text.
- **Charcoal** (`#222526`): Body copy and secondary headlines — slightly softened from pure black for editorial readability.
- **Slate Body** (`#585858`): Tertiary text, byline metadata.
- **Quiet Gray** (`#757777`): Secondary metadata, timestamps, photo credits — the system's most-frequent gray (480 occurrences).
- **Hairline Gray** (`#bebfbf`): Story dividers, table borders, vertical pica rules between columns.
- **Light Surface Gray** (`#f3f3f3`): Subtle alternate-row fill in tables and section banners.

### Surface & Borders
- **Page Surface** (`#ffffff`): Default story-grid background.
- **Tabloid Red Surface** (`#eb1701`): Masthead nameplate background, full-bleed.
- **Footer Ink** (`#222526`): The dark footer band — paper white text on near-black.
- **Hairline Border** (`#bebfbf`): Default 1px divider between stories and within tables.

### Functional / State
- **Sun Error Red** (`#930600`): Form errors and critical alerts (CSS var `--wp--custom--utility--color--error`). Darker than the masthead red so it doesn't compete.
- **Sun Success Green** (`#25661f`): Validation and confirmation (CSS var `--wp--custom--utility--color--success`).
- **Highlighter Yellow** (`#fef553`): Editorial highlight stripe on key content (CSS var `--wp--custom--utility--color--highlight`).
- **Premium Gold** (`#fcb900`): Sun Club exclusive content flag.
- **Button Hover Blue** (`#0056b4`): Kicker-blue button hover state.
- **Button Active Blue** (`#003e81`): Kicker-blue button pressed state.
- **Focus Ring Blue** (`#8dc3ff`): 4px keyboard-focus outline on buttons.
- **Showbiz Magenta** (`#b840cc`): Celebrity-section accent.
- **Royal Purple** (`#8a69a9`): Royal-section accent for Royal Family content.

### Gradient System
- The Sun is **gradient-free in chrome**. The masthead is solid `#eb1701` corner-to-corner. Story cards are flat. The only gradients in the system live inside photographs themselves — the page does no decorative blending.

## 3. Typography Rules

### Font Family
- **Display / Headlines**: `TheSun` custom condensed grotesque (no fallback declared in the page CSS — falls through to system serif if the brand font fails). The face that carries the masthead and every UPPERCASE headline.
- **Body / UI**: System serif stack — `serif` declared as fallback, with the page rendering Arial-equivalent stacks underneath for paragraph text.
- **OpenType Features**: Standard ligatures, lining numerals on prices and timestamps.

*Note: TheSun is a proprietary face (commissioned for News UK). For external implementations, the closest open-source matches are **Oswald**, **Bebas Neue**, or **Anton** — condensed sans-serif with tabloid stencil character. Avoid display serifs (Playfair, Bodoni) — they break the gutter-press feel.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Masthead Display | TheSun | 104px (6.50rem) | 400 | 0.88 | normal | UPPERCASE — the front-page tabloid stencil |
| Hero Headline | TheSun | 36px (2.25rem) | 400 | 1.11 | normal | Primary story head, mixed case |
| Section Title | TheSun | 32px (2.00rem) | 400 | 1.13 | normal | UPPERCASE section markers |
| Section Link | TheSun | 32px (2.00rem) | 400 | 1.13 | normal | UPPERCASE — clickable section markers |
| H1 Bold | TheSun | 30px (1.88rem) | 700 | 1.13 | normal | UPPERCASE breaking-news heds |
| H1 Bold Mixed | TheSun | 30px (1.88rem) | 700 | 1.13 | normal | Mixed-case breaking-news heds |
| H2 Caps | TheSun | 24px (1.50rem) | 400 | 1.00 | normal | UPPERCASE secondary section heads |
| H3 | TheSun | 18px (1.13rem) | 400 | 1.33 | normal | Story card headlines |
| Body | Arial / serif | 16px (1.00rem) | 400 | 1.50 | normal | Default reading copy |
| Body Bold | Arial / serif | 16px (1.00rem) | 700 | 1.50 | normal | Lead paragraphs, emphasized text |
| UI Heading | Arial / serif | 16px (1.00rem) | 700 | 1.25 | normal | Inline UI labels, button captions |
| Button Label | Arial / serif | 14px (0.88rem) | 700 | 1.21 | normal | Compact CTA labels |
| Caption / Byline | Arial / serif | 14px (0.88rem) | 400 | 1.43 | normal | Bylines, timestamps, photo credits |
| Eyebrow / Kicker | Arial / serif | 12px (0.75rem) | 700 | 1.00 | normal | UPPERCASE — story category above headline |
| Microcopy | Arial / serif | 11px (0.69rem) | 400 | 1.45 | normal | Footer legal, fine print |

### Principles
- **One shouting face, one system sidekick**: TheSun for headlines, Arial/serif for everything else. The two never trade roles. This separation is what keeps the page from feeling like a typeface dump.
- **Tight headlines, generous body**: Display type runs as tight as `0.88` line-height (touching descenders); body opens out to `1.50`. The contrast is the editorial fingerprint.
- **UPPERCASE is the masthead voice**: Every headline at 32px+ runs `text-transform: uppercase` for the front-page-stencil feel. Lowercase TheSun appears only on H3 card heads.
- **Bold is structural, not decorative**: 700-weight TheSun appears on breaking-news heds and 700-weight Arial appears on lead paragraphs and button labels. The 400 weights carry the calm.
- **No letter-spacing manipulation on display**: TheSun's native metrics carry the work — the brand never opens up large-caps with positive tracking, never tightens display with negative tracking. The face is the spacing.

## 4. Component Stylings

### Buttons

**Primary Kicker-Blue**
- Background: Kicker Blue (`#0072ee`)
- Text: Pure White (`#ffffff`)
- Padding: `12px 24px`
- Border: `0px none`
- Border-radius: `4px`
- Box-shadow: `none`
- Font: 14px Arial weight 700 UPPERCASE, mixed case allowed
- Hover: background `#0056b4`, transform `scale(1.1)`, opacity `0.7`
- Active: background `#003e81`, opacity `0.8`
- Focus: outline `4px solid #8dc3ff`, transform `scale(1.1)`, border `2px solid #000000`
- Use: Primary CTAs — "SUBSCRIBE", "READ MORE", "SIGN UP"

**Outline Inverted (Hero Overlay)**
- Background: `transparent`
- Text: Pure White (`#ffffff`)
- Padding: `6px 0px 4px`
- Border: `4px 0px solid` — top hairline only, white
- Border-radius: `0px`
- Hover: background `#8594a9` (slate blue), text `#0056b4`, opacity `0.8`
- Use: Inverted hero CTAs sitting over photography

**Black-Page Inverse**
- Background: True Black (`#000000`) on dark editorial pages
- Text: Pure White (`#ffffff`)
- Padding: `12px 24px`
- Border-radius: `4px`
- Use: Section CTAs on dark editorial backgrounds

### Cards & Containers

**Story Card**
- Background: Pure White (`#ffffff`)
- Border: `none` — depth comes from hairline `1px solid #bebfbf` dividers between cards
- Border-radius: `0px` for the photograph, `0px` for the wrapper
- Box-shadow: `none`
- Internal padding: 0 around image, 8px above headline, 4px between headline and dek
- Hover: headline underline appears in Kicker Blue (`#0072ee`)

**Masthead Block**
- Background: Tabloid Red (`#eb1701`)
- Text: Pure White (`#ffffff`)
- Padding: edge-to-edge
- Border-radius: `0px`
- Border-bottom: subnav coral `1px solid #ff7f80`
- The single most-defining surface of the brand

### Badges / Tags / Pills

**"BREAKING" Tab**
- Background: Tabloid Red (`#eb1701`) or Warning Red (`#ff4c4d`)
- Text: Pure White (`#ffffff`)
- Padding: `4px 8px`
- Border-radius: `4px`
- Font: 12px Arial weight 700 UPPERCASE
- Use: Live-news tickers and breaking-story flags

**"EXCLUSIVE" Tab**
- Background: Sun Gold (`#fcb900`)
- Text: True Black (`#000000`)
- Padding: `4px 8px`
- Border-radius: `4px`
- Font: 12px Arial weight 700 UPPERCASE
- Use: Sun Club exclusive content

**Section Tab (Sport / Showbiz / Royal)**
- Background: Sky Blue (`#3a79bb`) for sport, Magenta (`#b840cc`) for showbiz, Royal Purple (`#8a69a9`) for royal
- Text: Pure White (`#ffffff`)
- Padding: `4px 10px`
- Border-radius: `4px`
- Font: 12px Arial weight 700 UPPERCASE

### Inputs & Forms
- Background: Pure White (`#ffffff`)
- Border: `1px solid #bebfbf` default
- Border-radius: `4px`
- Font: 16px Arial weight 400
- Text colour: Charcoal (`#222526`)
- Padding: `12px 16px`
- Placeholder: Quiet Gray (`#757777`)
- Focus: outline `4px solid #8dc3ff`, border becomes `2px solid #000000`

### Navigation

**Masthead Bar**
- Background: Tabloid Red (`#eb1701`)
- Height: ~80px
- Logo: TheSun wordmark in white, ~210px wide, left-aligned at desktop, centred on mobile
- Right cluster: weather widget, search icon, account icon, hamburger menu
- Border-bottom: `1px solid #ff7f80` subnav-coral

**Primary Nav Bar (Subnav)**
- Background: Tabloid Red (`#eb1701`) or Pure White (`#ffffff`) — both variants exist
- Height: 40–48px
- Categories: "News · Sport · TV · Showbiz · Fabulous · Money · Travel · Tech · Motors · Health" — left-to-right, Arial weight 700 UPPERCASE 14px
- Hover: underline appears below text in Kicker Blue, or category background fills with darker red
- Border-bottom: `1px solid #ff7f80`

### Inline Editorial Links
- Color: Kicker Blue (`#0072ee`)
- Text-decoration: `underline`
- Font-weight: inherits from body (400 or 700)
- Hover: text shifts to `#0056b4`, underline persists
- Use: Every clickable phrase in body copy. Never used decoratively; never on non-clickable text.

## 5. Layout Principles

### Spacing System
- Base unit: 4px (with 8px and 16px as the rhythm increments for components)
- Scale: 4px, 8px, 12px, 16px, 24px, 32px, 40px, 48px, 64px, 80px
- Notable: The Sun's grid is rooted on tight 8–16px rhythm — story cards stack with `8–12px` gutters and section bands collapse to `0px` between blocks. Whitespace is rationed.

### Grid & Container
- Max content width: 1200–1280px on desktop story grid
- Masthead: full-width, edge-to-edge red, no max-width constraint
- Hero: full-width photograph + kicker + headline stack inside the 1200px container
- Story grid: 3-up or 4-up desktop, 2-up tablet, 1-up mobile — 8–16px gutters
- Footer: dense link grid in dark band (`#222526`) with paper-white type

### Whitespace Philosophy
- **Newsprint density, not magazine breath**: Story cards butt against one another with hairline `#bebfbf` dividers. Whitespace is not the structure — type weight, photographic mass, and red bands do the structural work.
- **Masthead-as-architecture**: The red `#eb1701` band sets the page's top register and announces the brand without accent or ornament. No rounded corners, no inner padding, no scrim.
- **Black-band footer**: The dark `#222526` footer block frames the bottom of every page in the same way the masthead frames the top — paper-white type, dense link grid, no shadows.

### Border Radius Scale
- Sharp (`0px`): Default for masthead, story photographs, full-bleed imagery, dividers
- Subtle (`4px`): Buttons, inputs, badges — almost-square but slightly softened
- Pill (`10%`–`50%`): Avatars, social icons, in-pager indicator dots
- No mid-range (`8–24px`): The Sun avoids the modern-app look — sharp or `4px`, nothing in between

## 6. Depth & Elevation

| Level | Box Shadow | Use Case |
|-------|-----------|---------|
| Flat (Level 0) | `none` | Default state for nearly every surface — masthead, story cards, footer |
| Hairline (Level 1) | `1px solid #bebfbf` | Story-grid dividers, footer separators, table borders |
| Block-Color (Level 2) | masthead red `#eb1701`, footer ink `#222526` | Architectural depth-by-saturation, not shadow |
| Focus Ring (Level 3) | `outline: 4px solid #8dc3ff` | Keyboard-focus on buttons and inputs |
| Hover Halo (Level 4) | `outline: 2px solid #000000` + `transform: scale(1.1)` | Button hover state — pressed-print feel |

**Shadow Philosophy**: The Sun has effectively zero box-shadows in the system — the `shadows` extraction returned an empty array. Depth is communicated entirely through colour blocks (the masthead red, the footer ink), hairline dividers (`#bebfbf`), and pressed-print transforms (`scale(1.1)` on hover). The result is a flat, paper-feeling surface that reads as front-page urgency rather than SaaS glassiness. Where competitors lean on glass-morphism and elevation, The Sun leans on ink density.

### Decorative Depth
- The masthead red against the white grid is the primary depth signal — graphic depth-by-contrast rather than shadow-based depth.
- Hover states use transform `scale(1.1)` and outline rings rather than shadow blooms — the button "presses up" mechanically.
- The black footer band creates visual depth without elevation — paper white type on near-black ink.

## 7. Do's and Don'ts

### Do
- Use Tabloid Red (`#eb1701`) only as the masthead and subnav background — full-bleed, never as accent on individual chrome
- Run TheSun custom face (or Oswald / Bebas Neue substitute) UPPERCASE at 32px+ for all headlines
- Push display line-height tight (`0.88`–`1.13`) — tabloid stencil pacing
- Use Kicker Blue (`#0072ee`) underlined for every inline editorial link — never decoratively
- Stack story cards with `1px solid #bebfbf` hairline dividers, no shadows, no card chrome
- Default to `4px` border-radius on buttons and inputs — almost-square
- Run body copy at 16px Arial regular with `1.50` line-height for paragraph readability
- Use `transform: scale(1.1)` on button hover for the pressed-print mechanical feel
- Pair the red masthead with a `#222526` footer band — top-and-bottom architectural framing
- Reserve Sun Gold (`#fcb900`) for Sun Club exclusive content flags

### Don't
- Don't soften the masthead red — `#eb1701` is the brand, no gradients, no opacity, no tinting
- Don't add box-shadows to story cards — depth is via hairline dividers and block colour, never elevation
- Don't introduce a serif display face — TheSun is a condensed grotesque; serifs break the gutter-press feel
- Don't use whitespace as the primary structuring device — type weight and red bands carry the architecture
- Don't lowercase masthead headlines — UPPERCASE TheSun at 32px+ is the front-page contract
- Don't apply mid-range radii (`8–24px`) — sharp `0px` or `4px` only
- Don't put Kicker Blue on non-clickable text — it's the inline link contract
- Don't add background colour to body paragraphs — pure white surface, ink-coloured type, hairline dividers
- Don't tint the page background — `#ffffff` is committed
- Don't soften the footer ink to a charcoal gray — `#222526` is the contract

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, masthead logo centres, hamburger nav |
| Mobile | 375–767px | Single-column, masthead 60–70px tall, 1-up story grid |
| Tablet | 768–1023px | 2-up story grid, partial inline subnav |
| Desktop | 1024–1199px | 3-up story grid, full inline subnav |
| Large | 1200–1439px | Maximum 1200px container, 4-up grid |
| XL | ≥1440px | 1280px container, 4-up grid with wider gutters |

### Touch Targets
- Primary CTAs: min 44px tap height, 24px horizontal padding on mobile
- Subnav links collapse into a full-screen hamburger menu under 768px
- Story cards: entire card is tappable, not just the headline

### Collapsing Strategy
- **Masthead**: scales proportionally; on mobile the wordmark centres and hamburger appears right
- **Subnav**: horizontal categories collapse into a horizontally-scrollable strip on tablet, then into hamburger on mobile
- **Story grid**: 4-up → 3-up → 2-up → 1-up with maintained aspect ratios
- **Hero**: photograph stays full-bleed; headline drops from 32px to 24px on mobile
- **Footer**: dense link grid collapses to accordion sections, dark band stays full-width

### Image Behavior
- Story photographs maintain a 4:3 or 16:9 crop across breakpoints
- Hero photographs use art-directed crops at mobile (often a tighter portrait of the same scene)
- The masthead nameplate scales but never simplifies to an icon — always full TheSun wordmark

## 9. Agent Prompt Guide

### Quick Reference
- Masthead Background: Tabloid Red (`#eb1701`)
- Page Background: Pure White (`#ffffff`)
- Primary Headline: TheSun face at 32–104px UPPERCASE
- Body Text: Arial 16px / 1.50 line-height
- Inline Link: Kicker Blue (`#0072ee`) underlined
- Primary Button: Kicker Blue bg, white Arial weight 700 UPPERCASE, `4px` radius
- Hairline Divider: `#bebfbf`
- Footer Band: `#222526` dark
- Sun Club Gold: `#fcb900`
- Focus Ring: `4px solid #8dc3ff`

### Example Component Prompts
- "Create a Sun-style masthead — full-bleed `#eb1701` background, `~80px` tall, white TheSun wordmark left-aligned at 210px wide, weather widget + search icon + account icon + hamburger right-aligned. Below the masthead, a 40px subnav row in `#eb1701` with white Arial weight 700 UPPERCASE 14px category links — News, Sport, TV, Showbiz, Fabulous, Money, Travel, Tech, Motors, Health. `1px solid #ff7f80` border-bottom on the subnav."
- "Build a 4-up story-card grid on `#ffffff`. Each card is a 4:3 photograph with `0px` radius, no shadow, no border. Below the image: 18px TheSun face weight 400 headline at line-height 1.33 in `#000000`, 14px Arial weight 400 dek in `#222526`, 12px Arial weight 700 UPPERCASE Kicker Blue (`#0072ee`) byline. Cards stacked with `1px solid #bebfbf` hairline dividers between rows."
- "Design a primary CTA — Kicker Blue (`#0072ee`) background, white text, 14px Arial weight 700 UPPERCASE, `12px 24px` padding, `4px` radius. On hover: background `#0056b4`, `transform: scale(1.1)`, opacity `0.7`. On focus: outline `4px solid #8dc3ff`."
- "Create a hero block — full-bleed photograph, then a `#eb1701` ribbon overlay at top-left with white 12px Arial weight 700 UPPERCASE 'BREAKING'. Below the photo: 36px TheSun weight 400 headline in `#000000` at line-height 1.11, 16px Arial body dek with Kicker Blue (`#0072ee`) underlined inline links."
- "Design a Sun Club exclusive flag — Sun Gold (`#fcb900`) background, true black `#000000` text, 12px Arial weight 700 UPPERCASE 'EXCLUSIVE', `4px 8px` padding, `4px` radius. Pair with a tabloid magenta `#b840cc` 'SHOWBIZ' tag using identical chrome."

### Iteration Guide
1. Default to pure white (`#ffffff`) story-grid background — the masthead red carries all the heat.
2. Tabloid Red (`#eb1701`) is the masthead and subnav contract — no other element on the page may use this exact red.
3. TheSun custom face (or Oswald / Bebas Neue substitute) at 32px+ UPPERCASE for every headline. Body copy stays in Arial.
4. Push display line-height tight (`0.88` on the masthead, `1.11–1.13` on heros) — tabloid-stencil pacing.
5. Kicker Blue (`#0072ee`) is the inline link contract — every clickable word in body copy carries it, underlined.
6. `4px` border-radius is the printerly default for buttons and inputs — almost-square.
7. Story cards stack with `1px solid #bebfbf` hairline dividers, no shadows, no card chrome.
8. The dark `#222526` footer band frames the bottom; the red masthead frames the top — top-and-bottom architectural framing is non-negotiable.
9. Use `transform: scale(1.1)` on button hover for the pressed-print mechanical feel.
10. Whitespace is rationed — the brand voice is gutter-press density, not magazine breath.
