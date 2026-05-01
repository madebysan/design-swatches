# Design System Inspired by Ghost

## 1. Visual Theme & Atmosphere

Ghost's website is editorial software design at its most disciplined: a publishing platform that looks like a well-funded indie magazine deliberately built to make WordPress feel like a 2008 forum. The page anchors on a near-black ink canvas (`#15171A`) for hero and key product sections, alternates with pure white reading panels, and punctuates the whole thing with one electric accent — a high-voltage lime (`#D1FF19`) that does double duty as primary CTA fill and as an entire chromatic section background. The design refuses gray-on-gray SaaS softness. Everything is high contrast, edge-aligned, and tuned for people whose business is words.

The typographic system carries the publisher attitude. Headlines run in a contemporary geometric sans (Ghost's stack reads as Inter / system-ui / `-apple-system`) at heavy weight and large display sizes — the hero "Turn your audience into a business" lands at roughly 54px / weight 600 with tight tracking and a 1.05 line-height. Where Cape uses 300-weight whisper and Stripe uses gradient maximalism, Ghost goes the opposite way: declarative, sans-serif, headline-as-hook, every section opening with a tight one-liner that could ship as a magazine standfirst. Body copy holds at 16–18px with comfortable 1.5+ line-height — this is a company that respects reading.

What makes Ghost unmistakable is its **chromatic section discipline**. Each major section is its own colored room: ink-black hero, pure-white feature explainers, lime-yellow callout panels, blush-pink quote sections, charcoal stats bands. There are no gradients to bridge them — sections butt up against each other in solid color blocks like a printed magazine spread changing stock. Cards use modest 6–24px radii (mostly 8/16px), modest shadows, and decisive 1px borders in a soft `#E5E5E5` neutral. The result reads as confident, owned, indie-publisher modernism — the visual equivalent of "no investors, no bullshit."

**Key Characteristics:**
- Geometric sans-serif at 600–700 weight for all display — declarative, not whispery
- Near-black ink (`#15171A`) and pure white sections alternate like magazine spreads
- Single electric lime accent (`#D1FF19`) reserved for primary CTAs and full-bleed callout panels
- Solid color block sections — no gradients, no scrim transitions between rooms
- 8/16/24px radius progression — softened but never pillowy
- Five-tier shadow ramp: from 1px hairline lifts to 25px ambient — restrained, never glassy
- Inline product screenshots dropped into context with subtle borders, no chrome wrappers
- Editorial pacing: each section opens with a one-line standfirst and a single supporting paragraph

## 2. Color Palette & Roles

### Primary
- **Ghost Ink** (`#15171A`): The signature dark — used for hero backgrounds, footer, dark feature sections, and primary text on light surfaces. A touch warmer than pure black, reads as printed ink rather than absolute zero.
- **Pure White** (`#FFFFFF`): Reading panels, content sections, card surfaces. Ghost is one of the few platforms that uses true white on its main reading sections — confidence in the type to do the work.
- **Editorial Black** (`#000000`): Reserved for borders, button fills on light surfaces, and the heaviest body type. Used distinctly from Ghost Ink — black is a frame, ink is a room.

### Brand Accent
- **Voltage Lime** (`#D1FF19`): The signature accent — applied to primary CTA buttons ("Start a free trial"), full-bleed callout sections, and pricing-tier highlights. Saturated, electric, almost neon. Used as both ink (button labels on dark) and as flood fill (entire panel backgrounds).
- **Chartreuse Lime** (`#BEF264`): Softer secondary lime for hover states, dotted patterns, and decorative accents where Voltage would overpower. Reads as the "calm" version of the brand color.

### Editorial Section Colors
Ghost's section palette is broader than most SaaS sites because each section is its own room:
- **Blush Pink** (`#FFB8E0`): Quote sections, testimonial callouts, certain feature spotlights. Soft and editorial.
- **Sky Wash** (`#A7D8F0`): Used sparingly for newsletter / membership feature panels.
- **Cream** (`#F5F0E8`): Optional warm panel background for editorial sections.

### Neutrals & Text
- **Body Ink** (`#15171A`): Primary text on white surfaces.
- **Slate** (`#64748B`): Secondary text, captions, supporting copy. The workhorse muted neutral.
- **Mist** (`#94A3B8`): Tertiary text, disabled states, very fine print.
- **Inverted Text** (`#FFFFFF`): All text on Ghost Ink surfaces.

### Surface & Borders
- **Surface White** (`#FFFFFF`): Default card and panel background on light sections.
- **Surface Ink** (`#15171A`): Default card background on dark sections.
- **Hairline Border** (`#E5E5E5`): The signature 1px border — used on cards, navigation dividers, table rows. Soft enough to disappear, present enough to define.
- **Border Strong** (`#000000`): Used selectively for emphasis frames and inverted hover states.

### Shadow Tokens
Ghost ships a five-tier shadow ramp (Tailwind's default progression, applied conservatively):
- **Hairline** (`0 0 1px rgba(0,0,0,0.1), 0 2px 6px rgba(0,0,0,0.03)`): subtle card lift
- **Soft** (`0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)`): button rest, card hover
- **Lift** (`0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1)`): floating CTAs, prominent cards
- **Float** (`0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1)`): modals, dropdowns
- **Ambient** (`0 25px 50px -12px rgba(0,0,0,0.25)`): hero product screenshots, emphasis frames

### Gradient System
- Ghost is **gradient-free across page surfaces.** No section ever uses a gradient fill — sections are always solid color blocks. The closest thing to gradient treatment is product screenshots that ship with their own UI gradients embedded; the website chrome itself never gradients.

## 3. Typography Rules

### Font Family
- **Primary**: `Inter`, with fallback: `-apple-system`, `BlinkMacSystemFont`, `"Segoe UI"`, `Roboto`, sans-serif
- **Monospace / Code**: `"SF Mono"`, `Menlo`, `Consolas`, monospace — used in code samples, API documentation, terminal references
- **OpenType Features**: Tabular figures (`tnum`) for pricing displays; standard ligatures elsewhere. No alternate stylistic sets.

*Note: Ghost's editor and marketing site lean on Inter for its strong rendering at heavy weights and tight tracking. Söhne, Founders Grotesk, or Aktiv Grotesk serve as close substitutes for premium implementations; system-ui works as a free fallback.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Inter | 54px (3.38rem) | 700 | 1.05 | -0.02em | Landing hero one-liners |
| Display Large | Inter | 48px (3.00rem) | 700 | 1.10 | -0.02em | Major section openers |
| Display | Inter | 43.2px (2.70rem) | 600 | 1.15 | -0.02em | Standard hero on inner pages |
| Section Heading | Inter | 40px (2.50rem) | 600 | 1.20 | -0.015em | Feature section titles |
| Sub-heading Large | Inter | 36px (2.25rem) | 600 | 1.20 | -0.015em | Pricing tiers, primary cards |
| Sub-heading | Inter | 32px (2.00rem) | 600 | 1.25 | -0.01em | Card titles, sub-sections |
| Sub-heading Small | Inter | 24px (1.50rem) | 600 | 1.30 | -0.01em | Feature titles, panel heads |
| Eyebrow | Inter | 20px (1.25rem) | 500 | 1.30 | -0.005em | Section eyebrows, lead-ins |
| Body Large | Inter | 18px (1.125rem) | 400 | 1.55 | normal | Intro paragraphs, lead body |
| Body | Inter | 16px (1.00rem) | 400 | 1.55 | normal | Standard reading text |
| Nav Link | Inter | 14px (0.875rem) | 500 | 1.40 | -0.005em | Top navigation, footer links |
| Button UI | Inter | 16px (1.00rem) | 600 | 1.00 | -0.005em | Button labels — sentence case |
| Caption | Inter | 14px (0.875rem) | 400 | 1.50 | normal | Supporting copy, metadata |
| Caption Small | Inter | 12px (0.75rem) | 400 | 1.40 | 0.01em | Legal text, micro labels |

### Principles
- **Heavy display, regular body**: Display sizes run weight 600–700; body text holds at 400. There is no "soft" 500 in display — Ghost commits to either bold or regular, never the in-between.
- **Tight display tracking, normal body tracking**: Headlines tighten to `-0.02em` to lock the geometric sans into dense headline blocks. Below 20px, tracking returns to normal — readability over compression.
- **Generous body line-height**: Body runs at 1.55 — well above SaaS norm. This is a publishing platform; the marketing site reads like an article on purpose.
- **Sentence case everywhere**: Buttons, headings, nav, eyebrows — all sentence case. Ghost does not use uppercase chrome. The one exception is the wordmark itself.
- **One-line headline discipline**: Hero and section headlines are written to fit on one line at desktop. Two-line hero headlines are an exception. The structure is: tight headline + supporting paragraph + CTA, repeated.

## 4. Component Stylings

### Buttons

**Primary Lime**
- Background: Voltage Lime (`#D1FF19`)
- Text: Ghost Ink (`#15171A`)
- Padding: 12px 24px (compact), 16px 32px (standard)
- Radius: `8px`
- Border: none
- Shadow: Hairline at rest, Soft on hover
- Font: 16px Inter weight 600, sentence case
- Hover: background shifts to Chartreuse (`#BEF264`), shadow lifts to Soft tier
- Use: Primary CTA — "Start a free trial", "Get started", "Sign up free"

**Dark Inverted**
- Background: Ghost Ink (`#15171A`)
- Text: Pure White (`#FFFFFF`)
- Padding: 12px 24px
- Radius: `8px`
- Shadow: none at rest, Soft on hover
- Font: 16px Inter weight 600
- Hover: background lightens to `#2B2D31`
- Use: Secondary CTAs on light surfaces, "Read docs", documentation links

**Ghost Outline**
- Background: transparent
- Text: Ghost Ink (`#15171A`) on light, Pure White (`#FFFFFF`) on dark
- Border: `1px solid #E5E5E5` on light, `1px solid rgba(255,255,255,0.2)` on dark
- Radius: `8px`
- Hover: background fills to `#F5F5F5` (light) or `rgba(255,255,255,0.05)` (dark)
- Use: Tertiary actions — "Learn more", "Pricing", "Sign in"

**Pill Tag**
- Background: transparent or `#F5F5F5`
- Text: Slate (`#64748B`)
- Border: `1px solid #E5E5E5`
- Radius: `24px`
- Padding: 4px 12px
- Font: 14px Inter weight 500
- Use: Category tags, "NEW" feature badges, navigation pills

### Cards & Containers
- Background: `#FFFFFF` on light sections; `#15171A` on dark sections
- Border: `1px solid #E5E5E5` on light surfaces; `1px solid rgba(255,255,255,0.08)` on dark
- Radius: `16px` for primary feature cards; `8px` for compact list cards; `24px` for hero/pricing emphasis
- Shadow: Hairline default, Soft on hover, Lift for floating cards, Ambient reserved for hero product screenshots
- Internal padding: 24px (compact) / 32px (standard) / 48px (feature) — Ghost respects card breathing room

### Badges / Tags / Pills

**New Badge**
- Background: Voltage Lime (`#D1FF19`)
- Text: Ghost Ink (`#15171A`)
- Padding: 2px 8px
- Radius: `6px`
- Font: 12px Inter weight 600, uppercase, letter-spacing `0.05em`
- Use: "NEW" feature flags inline next to feature names

**Pricing Tier Highlight**
- Background: Voltage Lime (`#D1FF19`) panel fill
- Text: Ghost Ink (`#15171A`)
- Border: none — the lime carries the signal
- Use: "Most Popular" pricing tier — entire card flips to lime, button inverts to dark

**Plan Pill**
- Background: `#F5F5F5`
- Text: Slate (`#64748B`)
- Border: `1px solid #E5E5E5`
- Radius: `24px`
- Padding: 6px 16px
- Use: Plan name labels at top of pricing cards

### Inputs & Forms
- Background: `#FFFFFF`
- Border: `1px solid #E5E5E5`
- Radius: `8px`
- Font: 16px Inter weight 400
- Text color: Ghost Ink (`#15171A`)
- Placeholder: Slate (`#64748B`)
- Focus: border shifts to `#15171A`, soft glow `0 0 0 3px rgba(21,23,26,0.08)`
- Padding: 12px 16px

### Navigation
- Top nav: horizontal white bar with hairline `1px solid #E5E5E5` underline
- Logo: Ghost wordmark left-aligned, sized at 28px height
- Nav links: 14px Inter weight 500, color Slate (`#64748B`), hover to Ghost Ink (`#15171A`)
- Right cluster: "Sign in" (Ghost Outline button) + "Start free trial" (Primary Lime button)
- Mega-menus: full-width drop panels on hover with multi-column feature lists, soft shadow `Float` tier
- Sticky behavior: nav fixes to top on scroll with subtle backdrop blur (`backdrop-filter: blur(8px)`) and `rgba(255,255,255,0.85)` background tint

### Decorative Elements

**Solid Section Blocks**
- Each major section uses solid color fill — Ink, White, Lime, Pink, Cream — with sharp edge-to-edge transitions
- No diagonal cuts, no SVG dividers, no gradient blends — the seam between sections IS the design
- Used for: hero (Ink), product explainers (White), pricing/CTA emphasis (Lime), testimonials (Pink/Cream), footer (Ink)

**Inline Product Screenshots**
- Browser/app screenshots embedded directly in white sections with `1px solid #E5E5E5` border and `16px` radius
- Ambient shadow tier (`0 25px 50px -12px rgba(0,0,0,0.25)`) on hero screenshots only
- No browser chrome wrappers — Ghost trusts the screenshot composition

## 5. Layout Principles

### Spacing System
- Base unit: 4px (with 8px as the primary increment)
- Scale: 2px, 4px, 8px, 12px, 16px, 20px, 24px, 32px, 36px, 40px, 48px, 54px
- Notable: The scale runs through every multiple of 4 from 8 to 48 — Ghost uses a denser, more even progression than Cape's binary tight/wide. This is a content-heavy site that needs intermediate values for editorial rhythm.

### Grid & Container
- Max content width: ~1280px for centered content; ~720px for reading-width text columns
- Hero: full-width Ink section with centered text + product screenshot below or right
- Feature sections: alternating 2-column (text + screenshot) layouts on white
- Pricing: 4-column card grid with the highlighted tier flipping to lime
- Editorial sections: single-column 720px reading width for testimonial and quote panels
- Footer: Ink section with 4-column link grid + signup form

### Whitespace Philosophy
- **Magazine-spread pacing**: Each section gets 96–128px of vertical padding — generous but not airy. The page reads like a designed publication, not a brochure.
- **Color does the chaptering**: Where competitors use horizontal rules or whitespace gaps to separate sections, Ghost uses color blocks. The transition from white to lime is the chapter break.
- **Reading-column discipline**: Body paragraphs cap at ~720px width. Even on ultrawide viewports, text never sprawls — Ghost is built by people who care about line length.

### Border Radius Scale
- Hairline (6px): Small badges, inline pills, "NEW" tags
- Standard (8px): Buttons, inputs, list cards, default surfaces — the workhorse radius
- Soft (16px): Feature cards, primary content cards, embedded screenshots
- Generous (24px): Pill buttons, hero CTAs in some contexts, pricing emphasis cards
- No pillowy radii: Ghost stays under 24px. There is no fully-pill `9999px` shape on rectangular cards — pill is reserved for the actual capsule-shaped pricing toggle.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, 1px hairline border | Section panels, footer blocks, nav bar |
| Hairline (Level 1) | `0 0 1px rgba(0,0,0,0.1), 0 2px 6px rgba(0,0,0,0.03)` | Default card lift on white sections |
| Soft (Level 2) | `0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)` | Button hover, card hover, list item active |
| Lift (Level 3) | `0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1)` | Floating CTAs, prominent feature cards |
| Float (Level 4) | `0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1)` | Dropdown menus, modal panels, mega-nav |
| Ambient (Level 5) | `0 25px 50px -12px rgba(0,0,0,0.25)` | Hero product screenshots — the one big shadow moment |

**Shadow Philosophy**: Ghost's depth system is the standard Tailwind ramp applied with restraint. Most surfaces sit at Level 0 or Level 1 — the page reads almost flat. Real elevation is reserved for two things: interaction feedback (hover lifts to Soft) and hero product moments (the ambient Level 5 shadow announces "this is the actual editor screenshot, look at it"). The five-tier system exists, but you'll rarely see more than two tiers on any given screen. Discipline is the design.

### Decorative Depth
- The 1px `#E5E5E5` hairline is doing more depth work than any shadow. It's how cards on white feel "card-like" without lifting off the page.
- Dark sections rarely use shadow at all — the contrast between Ink and white nav bar is enough separation.
- No inset shadows, no glow effects, no glassmorphism. Ghost is screen-printed, not layered.

## 7. Do's and Don'ts

### Do
- Use Inter at weight 600–700 for every display heading — heavy is the publisher voice
- Apply Voltage Lime (`#D1FF19`) only to primary CTAs and full-bleed callout panels — preserve its electric quality
- Alternate solid-color section blocks (Ink → White → Lime → White → Ink) like magazine spreads
- Keep card radius at `16px` for feature cards, `8px` for compact UI — these are the two workhorse values
- Cap body line-height at 1.55+ on reading paragraphs — this is a publishing platform
- Use the 1px `#E5E5E5` hairline border to define cards on white surfaces, not shadow
- Reserve Ambient shadow (`0 25px 50px -12px rgba(0,0,0,0.25)`) for hero product screenshots only
- Use sentence case on all buttons, headings, and nav — uppercase is reserved for "NEW" badges
- Cap reading column width at ~720px even on wide viewports
- Pair the "Most Popular" pricing tier with full lime fill — let color do the highlighting

### Don't
- Don't use weight 400–500 on display headings — the brand voice is bold, not light
- Don't introduce gradient fills on sections — Ghost is solid-color blocks
- Don't soften the dark to a navy or charcoal — Ghost Ink (`#15171A`) is exact
- Don't use lime on body text or fine UI — it's a flood/CTA color, not a text color
- Don't add glassmorphism, blur effects, or atmospheric shadows — depth is restrained
- Don't introduce additional accent colors — lime + section pinks/blues are the entire palette
- Don't use uppercase on buttons or section headings — sentence case is the rule
- Don't wrap product screenshots in fake browser chrome — embed them clean with hairline border
- Don't push hero headlines past two lines — the design is built for one-liner discipline
- Don't use `9999px` pill radius on rectangular cards — radius caps at 24px

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <400px | Single-column, hero drops to 32px, nav collapses to hamburger |
| Mobile | 400–640px | Single-column, 36–40px hero, stacked CTAs |
| Tablet Small | 640–768px | Begin 2-column for feature pairs, 40–48px hero |
| Tablet | 768–1024px | Full feature grids, 48px hero, nav still collapses |
| Desktop | 1024–1280px | Full multi-column layouts, 54px hero, full nav visible |
| Large Desktop | ≥1400px | Maximum scale (54px hero, 1280px container) |

### Touch Targets
- Primary CTAs: min 48px tap height on mobile, 16px+ horizontal padding
- Nav hamburger: 44×44px tap area
- Pricing toggle: 56px height, 32px+ tap zones per state

### Collapsing Strategy
- **Nav**: Horizontal nav collapses to hamburger below 1024px; opens as full-screen Ink overlay with stacked links at weight 600
- **Hero**: 54px → 48px → 40px → 36px → 32px progressive scaling, weight 700 maintained throughout
- **Feature sections**: 2-column text+screenshot collapses to stacked single-column with screenshot below text
- **Pricing cards**: 4-column grid → 2-column → single-column carousel-style stack on mobile
- **Section padding**: 96–128px desktop → 48–64px mobile — preserves editorial pacing at smaller scale
- **Type tracking**: `-0.02em` headline tracking holds at all breakpoints; body tracking always normal

### Image Behavior
- Hero product screenshots maintain Ambient shadow on desktop; shadow drops to Lift on mobile to save vertical space
- Inline screenshots stay full-width within their column at all breakpoints
- No art-direction switching — same images adapt with `object-fit: cover` and aspect-ratio constraints
- Logo wordmark scales to 24px height on mobile but never collapses to icon-only

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Voltage Lime (`#D1FF19`) on Ghost Ink text
- Hero Background: Ghost Ink (`#15171A`)
- Reading Background: Pure White (`#FFFFFF`)
- Primary Text on White: Ghost Ink (`#15171A`)
- Primary Text on Ink: Pure White (`#FFFFFF`)
- Secondary Text: Slate (`#64748B`)
- Tertiary Text: Mist (`#94A3B8`)
- Hairline Border: `#E5E5E5`
- Hover Lime: Chartreuse (`#BEF264`)
- Editorial Pink Section: `#FFB8E0`
- Hero Shadow: `0 25px 50px -12px rgba(0,0,0,0.25)`

### Example Component Prompts
- "Create a hero section on Ghost Ink (`#15171A`) with a centered headline at 54px Inter weight 700, line-height 1.05, letter-spacing -0.02em, color `#FFFFFF`. Below it: a single supporting paragraph at 18px weight 400, line-height 1.55, color `rgba(255,255,255,0.7)`. CTA: Voltage Lime (`#D1FF19`) button, 16px Inter weight 600, sentence case, `8px` radius, padding 16px 32px, no shadow at rest."
- "Design a feature card on white with `1px solid #E5E5E5` hairline border, `16px` radius, no shadow at rest. Title: Inter 32px weight 600, color `#15171A`, letter-spacing -0.01em. Body: Inter 16px weight 400, color `#64748B`, line-height 1.55. Padding 32px. Hover: shadow lifts to `0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)`."
- "Build a pricing card grid (4 cards). Default cards: white background, `1px solid #E5E5E5`, `16px` radius. Featured 'Most Popular' card: Voltage Lime (`#D1FF19`) background, no border, `16px` radius. Plan name as `#F5F5F5` pill at top with `24px` radius. Price at 48px Inter weight 700. Feature list at 16px weight 400 with checkmark icons in `#15171A`. CTA on default cards: Dark Inverted button (`#15171A` fill, white text). CTA on featured card: Dark Inverted (lime card needs dark CTA for contrast)."
- "Create a section transition: full-bleed Ghost Ink (`#15171A`) section ends, immediately followed by full-bleed Voltage Lime (`#D1FF19`) section. No gradient bridge, no SVG divider — sharp edge-to-edge color block transition. Each section maintains 96px vertical padding."
- "Design a 'NEW' inline badge — Voltage Lime (`#D1FF19`) background, Ghost Ink (`#15171A`) text, padding 2px 8px, `6px` radius, 12px Inter weight 600 uppercase, letter-spacing 0.05em."
- "Build a top navigation: white background with `1px solid #E5E5E5` bottom border, sticky on scroll with `rgba(255,255,255,0.85)` and `backdrop-filter: blur(8px)`. Logo left, nav links center (14px Inter weight 500, color `#64748B`, hover `#15171A`). Right cluster: ghost outline 'Sign in' button + Primary Lime 'Start free trial' button."

### Iteration Guide
1. Default to Inter weight 600–700 for all display headings — Ghost's voice is bold, not whispery
2. Use exactly one chromatic accent: Voltage Lime (`#D1FF19`). Section pinks/creams/skies are editorial decoration, not brand color.
3. Keep radius progression simple: `8px` for buttons/inputs, `16px` for cards, `24px` for emphasis. Never `9999px` on rectangular cards.
4. Section transitions are solid-color block-to-block — no gradient bridges, no divider SVGs
5. Use 1px `#E5E5E5` hairline borders to define cards on white. Save shadow for hover and hero only.
6. Cap reading column width at ~720px regardless of viewport — line length matters
7. Sentence case for all buttons and headings. Uppercase only on "NEW" inline badges.
8. Body line-height runs at 1.55+ — this is a publishing platform, type should breathe
9. Reserve Ambient shadow (`0 25px 50px -12px rgba(0,0,0,0.25)`) for hero product screenshots only — overusing it cheapens the moment
10. Pair Ghost Ink (`#15171A`) hero with white feature sections — alternate ink and white like a magazine flips between cover and editorial spreads
