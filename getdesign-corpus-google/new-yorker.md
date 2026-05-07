---
version: alpha
name: "The New Yorker"
description: "Token-first design system reference for The New Yorker."

colors:
  background: "#ffffff"
  surface: "#db3334"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#121212"
  primary: "#ffffff"
  on-primary: "#ffffff"
  border: "#e5e5e5"
  focus-ring: "#ffffff"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 42px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 29px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 23px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 21px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 21px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  4xl: 96px

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 16px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.background}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    borderColor: "{colors.focus-ring}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  badge:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
---

# The New Yorker Design System

## Overview

The New Yorker's website is a century of typographic discipline ported, faithfully, to a screen. The page reads as a magazine spread — pure white canvas (`#ffffff`), deep ink-black text (`#000000`), and a single editorial red (`#db3334`) that functions as the masthead's nameplate ribbon and not much else. Where most editorial sites have softened toward Helvetica or geometric sans, the New Yorker holds the line: every headline runs in **Irvin** (the 1925 hand-lettered display face Rea Irvin drew for the original masthead) or **Adobe Caslon Pro** (the body workhorse since the magazine's founding). The result is the most-imitated editorial system in American media, and the only one whose visual vocabulary is unchanged at the level of the letterform itself.

The defining move is the typographic stack. Three serif faces do nearly all the talking — Irvin Heading Pro for display, Irvin Text for sub-deck rubrics in small caps, and TNY Adobe Caslon Pro for the entire reading column. A grotesk (`Graphik`) handles UI chrome and metadata, but it never touches an article's body or a section title. The voice is set by the type itself before a word is read: this is a magazine, not a blog, and the typography is treating you accordingly.

What separates the New Yorker from other heritage editorial brands is restraint everywhere except type. Cards have no shadows. Borders are 1px hairlines (`#e5e5e5`). Buttons are flat black or flat white with a 1px outline. There are no gradients, no accent colors beyond the masthead red, no hover animations beyond a simple underline. The signature single-panel cartoon — sized at the same column width as the article that surrounds it — is the only illustration the system permits. Eustace Tilley, the dandy with the monocle, appears on the print cover annually but rarely on the web. The web design trusts the print system to do the work.

**Key Characteristics:**
- Three-serif stack: Irvin Heading Pro (display), Irvin Text (rubrics, small caps), TNY Adobe Caslon Pro (body)
- Pure white canvas (`#ffffff`) — magazine paper, not warm off-white
- Editorial red (`#db3334`) reserved for masthead nameplate and rubric accents only
- Drop caps in Caslon at the opening of every long-form feature — 4-line height, no embellishment
- Hairline 1px borders (`#e5e5e5`) as the primary structural device — no shadows, no fills
- Section rubrics in Irvin Text small-caps at 14px — the magazine's department labels (Talk of the Town, Profiles, Letter From…)
- Single-panel cartoons treated as editorial content, not decoration — captioned in Caslon italic
- Strict 12-column magazine grid with generous white space and dense text columns
- Dark hero blocks (`#121212`) for cinematic features, with reverse type set in Caslon

## Colors

### Primary
- **Ink Black** (`#000000`): Primary text, headlines, masthead, body type. The New Yorker uses pure black — no softened off-blacks.
- **Newsprint White** (`#ffffff`): Primary page background. Crisp magazine-paper white, not warm.
- **Hero Black** (`#121212`): Cinematic dark sections — long-form features, video heroes, signed-sealed-delivered-style standouts. Slightly warmer than pure black to read as ink rather than void.

### Brand Accent
- **New Yorker Red** (`#db3334`): The masthead nameplate red — the only chromatic color in the system. Appears on the homepage masthead bar, "Subscribe" CTA accents, breaking-news flags, and section dividers in print-emulation moments. Used roughly once per screen. Never on body type, never as a fill behind reading content.

### Neutrals & Text
- **Ink Black** (`#000000`): All headlines, all body type, all primary navigation.
- **Caption Slate** (`#333333`): Footer secondary text, copyright, fine print. A single dark-gray step below ink for tertiary information.
- **Metadata Gray** (`#a2a2a2`): Bylines, timestamps, kicker labels in some contexts. Mid-gray neutral.
- **Hairline Gray** (`#e5e5e5`): Border and divider color across the entire system. Never used for text.
- **Surface Gray** (`#f5f5f5`): Tinted panel background — used sparingly for newsletter signup blocks and "Recommended Reading" rails.

### Surface & Borders
- **Page Surface** (`#ffffff`): Default canvas.
- **Tinted Surface** (`#f5f5f5`): Subscription blocks, footer, rare panel insets.
- **Hairline** (`#e5e5e5`): 1px solid borders on cards, dividers between articles, table-of-contents rules.
- **Hero Surface** (`#121212`): Dark editorial features.

### Link Colors
- **Default link**: `#000000` with underline
- **Hover link**: `#000000` (color does not change), underline persists
- **External / brand link**: `#0879bf` (a single use of editorial blue for off-site links and certain article sponsorships)
- **Visited**: no distinct visited state — the magazine treats every link as fresh

### Gradient System
- The New Yorker is **gradient-free**. Solid black, solid white, solid red, solid hairline. Photography and illustration carry all chromatic richness; the layout itself stays mono.

## Typography

### Font Family
- **Display**: `IrvinHeadingPro`, fallbacks: `Helvetica Neue, Helvetica, Arial` — the digitization of Rea Irvin's 1925 masthead lettering. Used for major headlines, section titles, and the masthead nameplate itself.
- **Rubric / Small Caps**: `IrvinText`, fallbacks: `IrvinHeadingPro, Georgia, Times New Roman, Times` — used at 14px in uppercase for department labels (Talk of the Town, Daily Shouts, Letter From, Profiles).
- **Body / Reading**: `TNYAdobeCaslonPro`, fallbacks: `Times New Roman, Times` — Adobe Caslon Pro custom-tuned for The New Yorker. The reading face. Carries every article body, every drop cap, every byline.
- **UI / Chrome**: `Graphik`, fallbacks: `Helvetica Neue, Helvetica, Arial` — small UI labels, button text, navigation chrome, breadcrumbs.
- **Forms / Auxiliary**: `Inter` — newsletter signup, form fields, certain captions.
- **Sub-Display**: `NeutrafaceNewYorker`, fallbacks: `Helvetica Neue, Helvetica, Arial` — occasional sans display in 15px weight 600 for sub-section markers.
- **OpenType Features**: `oldstyle-nums` enabled in Caslon body, `lining-nums` in Graphik UI. Standard ligatures everywhere.

*Note: IrvinHeadingPro and TNYAdobeCaslonPro are proprietary to Condé Nast / The New Yorker. For external implementations, ITC Caslon No. 224 or Adobe Caslon Pro substitute for body Caslon; for Irvin display, Anton, Bodoni Moda Display at heavy weight, or a hand-lettered alternative like Saol Display approximate the feel. Graphik substitutes cleanly with Inter or GT America.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Transform | Notes |
|------|------|------|--------|-------------|-----------|-------|
| Masthead Nameplate | IrvinHeadingPro | 60–96px | 400 | 1.00 | none | The New Yorker logo rendered at scale |
| Display Hero | IrvinHeadingPro | 48–60px | 400 | 1.10 | none | Section-front cover headlines |
| Headline Large | IrvinHeadingPro | 36px (2.25rem) | 400 | 1.11 | none | Lead article on homepage / section front |
| Headline | IrvinHeadingPro | 28px (1.75rem) | 400 | 1.14 | none | Standard article hed in feed |
| Sub-headline | TNYAdobeCaslonPro | 22px (1.38rem) | 400 | 1.27 | none | Article dek / sub-deck below hed |
| Body Lead | TNYAdobeCaslonPro | 21px (1.31rem) | 400 | 1.50 | none | Opening graf, pull-quote body |
| Body | TNYAdobeCaslonPro | 17px (1.06rem) | 400 | 1.41 | none | Standard reading column |
| Rubric / Department | IrvinText | 14px (0.88rem) | 400 | 1.30 | uppercase | "TALK OF THE TOWN", "DAILY SHOUTS" |
| Byline | Graphik | 14px (0.88rem) | 500 | 1.71 | none | "By Author Name" — always Graphik, never Caslon |
| Caption | Inter | 14px (0.88rem) | 400 | 1.40 | none | Photo captions, image credits |
| UI Button | Graphik | 13px (0.81rem) | 500 | 1.00 | uppercase | Subscribe, Newsletter, Listen |
| Metadata | Graphik | 12–13px | 500 | 1.00 | uppercase | Timestamps, kickers, section pills |
| Drop Cap | TNYAdobeCaslonPro | ~64–80px (4 lines) | 400 | 1.00 | none | Feature article opener |

### Principles
- **Three-serif system, not one**: Irvin for display because it carries the brand's visual signature; Caslon for reading because it is the most-tuned reading serif in English-language publishing; Graphik for UI because metadata should not pretend to be editorial.
- **Caslon does the heavy lifting**: Every word a reader actually reads — body, dek, drop cap, photo caption italic, pull quote — is set in Caslon at weight 400. There is no bold body; emphasis is italic.
- **Irvin is sacred**: Reserve Irvin Heading Pro for headlines and the masthead nameplate. Never use Irvin for body text, captions, or UI. The face is too distinctive to dilute.
- **Small caps for departments**: Section rubrics ("Talk of the Town", "Profiles", "The Critics") are Irvin Text uppercase at 14px — never Caslon, never sentence case. This is the print magazine's table-of-contents convention rendered for screen.
- **No bold body Caslon**: Emphasis in body copy is italic Caslon, never bold. The print magazine has not used bold serif body in its history.
- **Tight display line-height**: Irvin Heading Pro at 36px runs at 1.11 line-height — magazine-tight, not airy. Headlines are blocks, not paragraphs.
- **Generous body line-height**: Caslon body at 17px runs at 1.41–1.50 — long-form reading comfort, the inverse of display tightness.
- **Old-style numerals in body**: Caslon body uses old-style figures so numbers sit on the baseline like lowercase letters; UI Graphik uses lining figures.

## Layout

### Spacing System
- Base unit: 8px (with 4px sub-unit for tight UI)
- Scale: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 56px, 64px
- Most-used: 8px (UI gap), 16px (small section), 32px (card padding), 56–64px (section break)
- Vertical column rhythm: paragraphs separated by 16px; sub-sections by 32px; articles by 64px hairline-ruled gap

### Grid & Container
- Max content width: ~1200px for the homepage / section fronts
- Article reading column: ~640–720px max — narrow, magazine-style for long-form comfort
- Homepage: 12-column responsive grid, with feature article spanning 8 columns and rail spanning 4
- Section fronts: 3-column or 4-column card grids
- Long-form articles: single centered column with full-bleed photography breaking the column for cinematic moments
- Cartoons sit at column width — never break out, never inset

### Whitespace Philosophy
- **Magazine pacing**: Each article in a feed is separated by a 1px hairline and 32–48px of vertical air. The page reads as a table of contents.
- **Reading column air**: Caslon body at 17px / 1.41 line-height with 16–24px paragraph spacing — denser than blog convention, looser than print. Tuned for screens that are read like pages.
- **Hero breathing room**: Display headlines at 36px get 48–64px of air above and 32px below. The masthead always gets its own band.
- **No filler**: Empty rails are left empty. The grid does not invent content to balance itself.

### Border Radius Scale
- Sharp (`0px`): Default for every rectangular element — buttons, cards, inputs, badges, image containers. Magazines do not have rounded corners.
- Pill (`9999px`): Reserved exclusively for the "Listen" audio button and circular avatar crops. Nothing else.
- No mid-range radii: The system is binary — sharp or fully circular. 4–16px values do not exist.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text, structural blocks |
| Hairline (Level 1) | `1px solid #e5e5e5` | Card edges, dividers between feed items, section rules |
| Ink Border (Level 2) | `1px solid #000000` | Form inputs, ghost buttons, primary outlined elements |
| Inverted Block (Level 3) | `#121212` background panel | Cinematic features, video heroes — depth via tonal shift, not shadow |
| Focus Outline (Level 4) | `2px solid #000000` outline, `0px` offset | Keyboard accessibility on inputs and links |

**Shadow Philosophy**: The New Yorker has no drop shadows. Anywhere. Depth is communicated by hairlines, ink borders, and tonal alternation between white and `#121212` blocks. The system is consciously print — paper has no shadow, only ink and absence of ink. When an element needs to feel "raised", it gets a 1px black border. When a section needs gravity, it inverts to a dark panel. There is no ambient elevation, no atmospheric blur, no gradient surface. This is the most rigorous flat system in editorial media, and it has been flat since before "flat design" was a phrase.

### Decorative Depth
- The dark hero (`#121212`) is the only true "elevation" the system uses — it functions as a chapter shift
- Hairlines are structural, not decorative — every rule serves to separate content
- Focus rings are black, hard, and 2px — accessibility is not softened with color glow

## Shapes

The complete radius scale is declared in the `rounded:` token block above.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Hard-edged brand moments and flush layouts |
| `sm` | 4px | Small controls and tight UI details |
| `md` | 8px | Inputs and compact interface elements |
| `lg` | 16px | Cards and larger containers |
| `pill` | 9999px | CTAs, chips, and rounded badges |

## Components

### Buttons

**Primary Black**
- Background: `#000000`
- Text: `#ffffff`
- Padding: 12px 24px
- Radius: `0px` (sharp rectangular)
- Border: none
- Shadow: none
- Font: 13px Graphik weight 500, uppercase, letter-spacing `0.05em`
- Hover: background shifts to `#333333`
- Use: "Subscribe", "Save", "Listen" — primary CTAs throughout

**Outline Ghost**
- Background: transparent
- Text: `#000000`
- Border: `1px solid #000000`
- Padding: 12px 24px
- Radius: `0px`
- Font: 13px Graphik weight 500, uppercase
- Hover: background `#000000`, text `#ffffff`
- Use: Secondary actions — "Newsletter", "Sign In"

**Inverted (on dark hero)**
- Background: `#ffffff`
- Text: `#000000`
- Border: none
- Padding: 12px 24px
- Radius: `0px`
- Use: CTAs sitting on `#121212` cinematic blocks

**Audio Pill ("Listen")**
- Background: transparent
- Text: `#000000` (or white on dark)
- Border: `1px solid currentColor`
- Radius: `9999px` (pill — the sole use of full radius in the system)
- Padding: 6px 14px
- Icon: headphones glyph at 14px, 8px gap from label
- Font: 13px Graphik weight 500
- Use: "Listen to this article" — the only pill-shaped element in the New Yorker UI

### Cards & Containers

**Article Card**
- Background: `#ffffff`
- Border: `1px solid #e5e5e5` (often only top/bottom — `1px 0 0` rule between feed items)
- Radius: `0px`
- Shadow: none
- Padding: 24–32px vertical between siblings
- Internal: image (full-width or 4:3), Irvin headline, Caslon dek, Graphik byline

**Dark Feature Card**
- Background: `#121212`
- Text: `#ffffff` headline (Irvin), `#e5e5e5` body (Caslon)
- Radius: `0px`
- Padding: 64px 48px
- Border: none
- Use: Cinematic long-form features — "Signed, Sealed, Delivered" style

**Quote / Pull Quote Block**
- Background: `#ffffff`
- Border: none — flanked by 1px hairline rules above and below
- Font: 28–36px Caslon italic, weight 400, line-height 1.30
- Indentation: full column or generous left rule
- Decoration: optional opening curly-quote glyph at 64px in Caslon

### Badges / Tags / Pills

**Section Rubric**
- Background: transparent
- Text: `#000000` (or `#db3334` for breaking)
- Font: 14px IrvinText uppercase, weight 400, letter-spacing `0.05em`
- No border, no fill — pure typographic
- Use: "DAILY SHOUTS", "PROFILES", "LETTER FROM PARIS"

**Breaking / Updated Flag**
- Background: `#db3334`
- Text: `#ffffff`
- Padding: 4px 8px
- Radius: `0px`
- Font: 12px Graphik uppercase weight 500
- Use: Live news, "JUST IN" indicators

### Inputs & Forms
- Background: `#ffffff`
- Border: `1px solid #000000` (full ink border, not hairline gray)
- Radius: `0px`
- Font: 16px Inter weight 400, color `#000000`
- Padding: 12px 16px
- Focus: border thickens to `2px solid #000000`, no glow, no halo
- Newsletter input pairs with adjacent black submit button — flush, no gap

### Navigation
- Top bar: black masthead band (`#000000`) with the Irvin nameplate centered in white
- Below masthead: horizontal section nav in Graphik 13px uppercase weight 500 — News, Books & Culture, Fiction & Poetry, Humor, Magazine, Puzzles & Games, Video, Podcasts, Archive
- Nav links: `#ffffff` on black band; `#000000` on white drop-down
- Hover: subtle 1px underline appears below the link
- Sticky behavior: masthead and section nav both stick on scroll
- Mobile: hamburger reveals full-screen takeover with sections stacked in 22px Caslon

### Decorative Elements

**Drop Cap**
- Caslon roman, 4-line height (~64–80px depending on body size)
- Color: `#000000`
- No box, no fill, no decoration — just the letterform at scale
- Float: left, with 8–12px right margin so the body wraps tight
- Use: Opening of every long-form feature

**Cartoon Block**
- Single-panel cartoon embedded inline with the article
- Caption: Caslon italic 17px, centered below the image
- Border: none — the cartoon's own line work is its frame
- Treated as editorial content, not advertising or decoration

**Hairline Rule**
- 1px solid `#e5e5e5` horizontal divider
- Used between articles in feeds, before/after pull quotes, separating bylines from body
- The system's primary structural device — replaces the role shadows or fills play in modern UI

**Section Divider Ornament**
- A small centered glyph (sometimes a Tilley silhouette, sometimes a typographic dingbat) flanked by hairline rules
- Used at major editorial breaks — between essay sections, before "Continue Reading"

## Do's and Don'ts

### Do
- Use Irvin Heading Pro for headlines and the masthead nameplate only — never for body, never for UI
- Use Adobe Caslon Pro (or TNYAdobeCaslonPro) for every word the reader will actually read
- Use Irvin Text uppercase at 14px for department rubrics — the print magazine's TOC convention
- Set drop caps in Caslon at 4-line height at the opening of every long-form feature
- Use 1px hairlines (`#e5e5e5`) as the primary structural device between feed items
- Keep the page background pure white (`#ffffff`) — magazine paper, not warm off-white
- Use New Yorker red (`#db3334`) only on the masthead nameplate and breaking-news flags
- Use italic Caslon for emphasis in body copy — never bold
- Inset single-panel cartoons at column width with Caslon italic captions centered below
- Invert to `#121212` panels for cinematic features — the only "elevation" the system uses
- Use old-style numerals in Caslon body, lining numerals in Graphik UI
- Use `0px` radius on every rectangular element — magazines don't round corners

### Don't
- Don't set body type in Irvin or any sans — Caslon is non-negotiable for reading
- Don't use bold Caslon for emphasis — italic is the only emphasis in the body
- Don't introduce drop shadows or atmospheric elevation — the system is flat by century-long convention
- Don't use mid-range border-radius (4–16px) — only `0px` rectangular or `9999px` pill (and pill is reserved for the Listen button)
- Don't saturate with red — one application per screen at most
- Don't use accent colors beyond `#db3334` — the system is mono plus red
- Don't use Inter or Graphik for headlines — those faces serve UI and forms only
- Don't use ALL CAPS Caslon — small caps belong to Irvin Text
- Don't introduce gradients anywhere — solid colors only
- Don't use a warm off-white canvas — the New Yorker is crisp white paper
- Don't compress display line-height below 1.10 or stretch body line-height above 1.55
- Don't replace single-panel cartoons with stock illustration — if you can't license a real cartoon, use no illustration

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single column, masthead nameplate scales to 32px, body 16px |
| Mobile | 375–667px | Single column, headline drops to 24px, body 17px maintained |
| Tablet | 768–1023px | 2-column feed grid, headline 28px |
| Desktop | 1024–1599px | 3-column feed grid, headline 36px, full nav bar |
| Large Desktop | ≥1600px | Maximum scale, 1200px container, 36–60px display |

### Touch Targets
- Primary CTAs: min 44px tap height, 24px horizontal padding on mobile
- Section nav links: 44px minimum row height in mobile drawer
- Article cards: full row tappable, no nested clickable regions

### Collapsing Strategy
- **Masthead**: Centered Irvin nameplate stays centered at all widths; subscribe CTA collapses to icon below tablet
- **Section Nav**: Horizontal row collapses to hamburger drawer below 768px; drawer reveals stacked Caslon 22px section names
- **Feed Grid**: 3-column → 2-column → single column; hairline dividers persist at all widths
- **Article column**: Reading column maintains ~640–720px max even on large desktop — the magazine never lets the line measure stretch
- **Drop caps**: Maintained at 4-line height across breakpoints, proportional to body size
- **Cartoons**: Always at column width — they shrink with the column, never break out
- **Dark hero panels**: Maintain `#121212` background; padding compresses 64px → 32px on mobile

### Image Behavior
- Photography full-bleed within the article column, occasionally breaking out for cinematic features
- Cartoons are never cropped or full-bleed — they always sit at column width with margin around the panel
- Image captions in Caslon italic 14px, color `#333333`, no background tint
- No art-direction shifts between breakpoints — the same composition adapts proportionally

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Text / Background Inversion: Ink Black (`#000000`)
- Page Background: Newsprint White (`#ffffff`)
- Cinematic Hero Background: Hero Black (`#121212`)
- Masthead / Breaking Accent: New Yorker Red (`#db3334`)
- Tinted Surface: Surface Gray (`#f5f5f5`)
- Hairline Borders: `#e5e5e5`
- Caption / Footer Text: `#333333`
- Metadata / Tertiary: `#a2a2a2`
- External Link: `#0879bf`

### Quick Type Reference
- Display headlines: IrvinHeadingPro 36px / 1.11 line-height / weight 400
- Body reading: TNYAdobeCaslonPro 17px / 1.41 line-height / weight 400
- Rubric labels: IrvinText 14px uppercase / weight 400
- UI buttons: Graphik 13px uppercase / weight 500
- Bylines: Graphik 14px / weight 500

### Example Component Prompts
- "Create a New Yorker–style article card on `#ffffff` with a `1px solid #e5e5e5` rule above and below. Headline in IrvinHeadingPro 28px weight 400, line-height 1.14, color `#000000`. Dek in TNYAdobeCaslonPro 22px weight 400, line-height 1.27. Byline in Graphik 14px weight 500 uppercase 'BY AUTHOR NAME'. No shadow, no background tint, `0px` radius."
- "Build a long-form feature opener: full-bleed photo above the fold, then a centered 720px reading column. Headline at 36px IrvinHeadingPro, dek at 22px Caslon italic. Body opens with a 4-line drop cap in Caslon roman, no decoration. Body text at 17px Caslon, 1.41 line-height, paragraphs separated by 16px."
- "Design a section rubric: 'TALK OF THE TOWN' in IrvinText 14px weight 400, uppercase, `0.05em` letter-spacing, color `#000000`, with a `1px solid #e5e5e5` rule beneath at 8px gap."
- "Create a cinematic dark feature panel: `#121212` background, 64px padding, IrvinHeadingPro 48px white headline, Caslon italic dek at 21px in `#e5e5e5`, white outline 'Listen' pill button (`9999px` radius, 1px white border, 13px Graphik uppercase)."
- "Build a newsletter signup block on `#f5f5f5` surface: 32px padding, Caslon 22px headline 'Sign up for The Daily', Inter 14px body, full-width email input (`1px solid #000`, `0px` radius), flush-attached black submit button with white Graphik 13px uppercase 'SIGN UP'."

### Iteration Guide
1. Default to the three-serif stack: Irvin for display, Caslon for body, Graphik only for UI chrome
2. Keep radius binary: `0px` for everything, `9999px` only for the Listen pill and avatar crops
3. Use 1px hairlines (`#e5e5e5`) instead of shadows for separation — the system is flat by design
4. Red (`#db3334`) is sacred — masthead nameplate and breaking flags only, one per screen max
5. Italic Caslon is the only body emphasis — never bold serif
6. Drop caps open every long-form feature — Caslon roman, 4 lines tall, no decoration
7. Department rubrics in Irvin Text uppercase 14px — never sentence case, never Caslon
8. Pure white canvas (`#ffffff`); invert to `#121212` only for cinematic features
9. Reading column maxes at ~720px even on large desktop — line measure is sacred
10. Single-panel cartoons sit at column width with Caslon italic captions — treat as editorial content, not decoration
