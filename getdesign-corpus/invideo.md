# Design System Inspired by InVideo

## 1. Visual Theme & Atmosphere

InVideo's website is a confident consumer-software pitch dressed in publishing-house typography. The home page opens on pure white (`#ffffff`) — no warm tint, no off-white softening — under a saturated full-bleed royal-blue announcement bar (`#086de8`) that pins to the top of every page. The hero is dominated by a single oversized condensed-grotesk headline, set in heavy uppercase ("CREATE VIDEOS WITHOUT LIMITS"), where the word "VIDEOS" is masked with cinematic footage so the typography itself becomes the product demo. Everything else in the system — buttons, badges, nav, surfaces — is restrained and consumer-clean, designed to keep that one display moment doing the heavy lifting.

The defining typographic choice is **mediaSansSemiCondensed at weight 900, uppercase, 92px**. This is editorial billboard energy — the same compressed-bold register you'd see on a magazine cover or a film poster — and it lands on a white canvas with zero supporting illustration. Below it, everything switches to **Inter** at quiet weights (400–600) for body and UI, so the page reads as a single dramatic statement followed by clean information. The contrast between the two type families is the hierarchy: one shouts, the other organizes.

The third signature is the **fully-pill geometry**. Every actionable surface — CTAs, nav buttons, category chips, the hero prompt input — is rounded to `9999px` (the JSON reports it as `3.35544e+07px`, which is the same thing, applied 281 times across the home page). InVideo doesn't use mid-range corner radius for actions; it's either fully pill-rounded or, on content cards, gently rounded at 8–16px. Combined with the hero's centered "prompt-bar" search composition — a dark gray pill (`#3a3a3a`) with placeholder text on the left and a blue "Try invideo" CTA tucked into the right end — the site advertises its AI nature through interface form, not illustration. The composition reads "type a prompt, get a video" before you read a word of copy.

**Key Characteristics:**
- mediaSansSemiCondensed at weight 900 uppercase for the hero — compressed editorial billboard type
- Inter at 400–600 for everything else — clean, neutral, consumer-friendly
- Royal blue accent (`#086de8`, `#066de8`, `#277cee`) — three near-identical blues used across CTAs, banner, and emphasis
- Pure white (`#ffffff`) page canvas — no warm tinting, full clinical neutrality
- Full-bleed blue announcement bar pinned above the nav on every page
- Pill-radius (`9999px`) on every interactive surface — buttons, chips, the hero prompt bar
- Dark gray prompt-bar (`#3a3a3a`) hero input as the primary product hook
- Video-masked text (the word "VIDEOS" filled with footage) as a one-time hero device
- Dark sections (`/ai`) layer over the light canvas with `rgba(255,255,255,0.12)` glass buttons and white text
- Tailwind utility class system with arbitrary values throughout (`bg-[#086DE8]`, `rounded-full`)

## 2. Color Palette & Roles

### Primary
- **InVideo Blue** (`#086de8`): The signature CTA color — used on "Sign up", "Try invideo", and primary action pills. Saturated royal blue, slightly toward cobalt.
- **InVideo Blue Pressed** (`#066de8`): A near-identical sibling used on alternate primary buttons. Functionally identical to `#086de8`; presence of both suggests two design hands or ungraduated tokens.
- **InVideo Blue Light** (`#277cee`): A slightly lighter variant used on larger ad-style CTAs (e.g. the bigger "Try invideo" pills with 16/24px padding). Reads as a softer brand blue.

### Brand Accent
- **Announcement Blue** (`#086de8`): Same as primary, but applied as a full-bleed top-of-page banner ("Agent One: now live on invideo"). The banner is the brand's chrome — always-on, always blue.
- **Hot Blue** (`#3258ec`): Pricing-page variant with slightly more violet — used on plan-toggle and selected-tier surfaces.

### Neutrals & Text
- **Pure White** (`#ffffff`): Default page canvas, default light-section background. Used 786 times across the page.
- **Pure Black** (`#000000`): Hero headline, body copy, nav links. InVideo doesn't soften its black — it's `#000` everywhere primary text appears. Tracked 113 times.
- **Soft Black** (`rgba(20, 20, 20, 0.7)` → `#141414` at 70%): Secondary text, sub-headline copy, "Turn any idea into videos…" caption beneath the hero. Tracked 219 times.
- **Gray Dark** (`#222222`): CSS variable `--color-gray-dark`, used for dark-mode surface and pricing nav text.
- **Prompt Gray** (`#3a3a3a`): The hero prompt-input pill — a deliberate dark gray that signals "input field, type here" against the white canvas.

### Surface & Borders
- **Surface White** (`#ffffff`): Default content surface — cards, hero canvas, section backgrounds.
- **Glass White** (`rgba(255, 255, 255, 0.12)`): On dark sections (`/ai`), translucent glass for secondary buttons and subtle UI chrome.
- **Border Hairline** (`rgba(0, 0, 0, 0.15)` / `oklab(0 0 0 / 0.15)`): The workhorse border — `1px solid` at 15% black, used on category chips, secondary buttons, and ghost surfaces. Tracked 156 times.
- **Border Charcoal** (`rgb(55, 55, 55)`): Dark-section variant for pill chips on `/ai`.
- **Border Soft** (`lab(91.6229 -0.159115 -2.26791)` ≈ `#e6e6e8`): Cool near-white divider line for `<hr>` and section breaks.

### Shadow Colors
- **Shadow Drop** (`rgba(0, 0, 0, 0.1)`): The only shadow color in the system — used at 10% opacity for both the soft mid-shadow (`0 10px 15px -3px`) and the play-button lift (`0 20px 25px -5px`).
- **Shadow Pop** (`rgba(0, 0, 0, 0.1)`) at `0 8px 10px -6px`: Tight close-shadow paired with the drop above to compound elevation on floating play buttons.

### Gradient System
- InVideo is **near gradient-free** in the brand frame. The system relies on flat blue, flat black on white, and flat dark surfaces. The only gradient encountered is a subtle vertical wash (`rgba(177, 229, 255, 0.314)` border) on a single decorative panel — barely a gradient. The brand statement is solid blue, full stop.

## 3. Typography Rules

### Font Family
- **Display**: `mediaSansSemiCondensed`, with fallback `mediaSansSemiCondensed Fallback` — a custom compressed grotesk used only for the giant uppercase hero headline. Weight 900.
- **Display Secondary**: `mediaSans`, with fallback `mediaSans Fallback` — the non-condensed sibling, used for medium-display moments at 60px.
- **Body & UI**: `Inter` — used for everything else (sub-headlines, body, buttons, links, captions).

*Note: mediaSans / mediaSansSemiCondensed appears to be a custom or licensed family commissioned for InVideo's brand. For external implementations, Druk Wide Bold or Anton serve as close substitutes for the condensed display weight; Inter remains the open-source default for the rest.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Hero Display | mediaSansSemiCondensed | 92px (5.75rem) | 900 | 1.07 | normal | UPPERCASE | The "CREATE VIDEOS WITHOUT LIMITS" billboard |
| Hero Display Light | mediaSansSemiCondensed | 92px (5.75rem) | 400 | 1.07 | normal | UPPERCASE | Lighter variant for secondary hero treatments |
| Section Display | mediaSans | 60px (3.75rem) | 400 | 1.00 | 1px | none | Mid-page section headlines (positive tracking) |
| Page Heading | Inter | 52px (3.25rem) | 400 | 1.08 | normal | none | Sub-page hero headings |
| Heading Bold | Inter | 36px (2.25rem) | 800 | 1.11 | normal | none | Feature card titles, sub-section heads |
| Sub-heading | Inter | 20px (1.25rem) | 800 | 1.20 | normal | none | Bold callouts, emphasis blocks |
| Body Large | Inter | 20px (1.25rem) | 400 | 1.40 | normal | none | Hero caption, intro paragraphs |
| Button Large | Inter | 20px (1.25rem) | 500 | 1.20 | normal | none | Primary CTAs (`Try invideo`) |
| Section Body | Inter | 18px (1.13rem) | 400 | 1.33 | -0.4px | none | Standard body copy on feature sections |
| Button Bold | Inter | 18px (1.13rem) | 600 | 1.33 | -0.4px | none | Emphasized in-line CTAs |
| Body | Inter | 16px (1.00rem) | 400 | 1.50 | normal | none | Standard reading text, links |
| Button | Inter | 16px (1.00rem) | 500 | 1.50 | normal | none | Standard pill button labels |
| Caption | Inter | 14px (0.88rem) | 400–500 | 1.43 | -0.35px | none | Chip labels, metadata, micro-copy |

### Principles
- **One billboard, then quiet**: The 92px uppercase mediaSansSemiCondensed is a single-use device — the hero only. Don't repeat it elsewhere on the page. Once you're past the hero, Inter takes over and stays in charge.
- **Inter at 400–600 dominates**: 90% of the type on the page is Inter at weight 400 (body, links) and weight 500–600 (buttons, emphasis). Bold weight 800 is reserved for `H2`-tier section titles. There is no italic.
- **Line-height runs tight on display, comfortable on body**: 1.07–1.11 for display sizes (a publishing-style lockup), 1.33–1.50 for reading text. The jump is intentional — display blocks lock together, body text breathes.
- **Negative letter-spacing on body Inter**: Sub-section paragraphs apply `-0.4px` tracking on Inter at 16–18px — a subtle tightening that gives copy a more confident, designed feel without going into "hyper-tracked" territory.
- **Uppercase only in the billboard**: The hero headline is the only uppercase usage on the page. All buttons, labels, and chips use mixed case. This is the opposite of the convention where buttons go uppercase — InVideo reserves capitals for the brand statement.
- **No title-case eccentricity**: Headlines and buttons all use sentence case. "Try invideo" (lowercase brand-name treatment) appears throughout — consistent with the wordmark.

## 4. Component Stylings

### Buttons

**Primary Blue Pill** (the brand button)
- Background: InVideo Blue (`#086de8`)
- Text: White (`#ffffff`)
- Padding: 8px 16px (compact) or 12px 16px (standard)
- Radius: `9999px` (pure pill — JSON reports `3.35544e+07px`)
- Border: `0px`
- Shadow: `none`
- Font: 16px Inter weight 500, sentence case (e.g., "Sign up", "Try invideo")
- Outline (focus): `oklab(0.708 0 0 / 0.5) none 3px`
- Use: Primary CTA — top-nav signup, hero search, in-page conversion buttons

**Primary Blue Pill Large**
- Background: InVideo Blue Light (`#277cee`)
- Text: Off-white (`#fefefe`)
- Padding: 16px 24px
- Radius: `9999px`
- Font: 20px Inter weight 500
- Use: Hero-adjacent or section-conclusion CTAs — bigger affordance for high-attention moments

**White Pill (Login / Secondary on Light)**
- Background: White (`#ffffff`)
- Text: Black (`#000000`)
- Padding: 8px 16px
- Radius: `9999px`
- Border: `1px solid rgba(0, 0, 0, 0.19)` — a thin charcoal hairline
- Font: 16px Inter weight 500
- Use: "Login", secondary pill actions on white sections

**Glass Pill (Dark Section Secondary)**
- Background: `rgba(255, 255, 255, 0.12)` — 12% white glass
- Text: `rgba(255, 255, 255, 0.9)` — near-white at 90%
- Width: fixed `180px` for nav-tier consistency
- Padding: 8px 16px
- Radius: `9999px`
- Font: 16px Inter weight 500
- Use: Secondary CTAs on dark sections (`/ai` page) — translucent over video imagery

**Charcoal Pill (Hero Prompt Container)**
- Background: `#3a3a3a` — solid dark gray
- Text: `#ffffff`
- Radius: `22.5px` (effectively half-pill at this height) or `9999px` on taller variants
- Padding: `0px` outer (the pill *is* the input field; padding is handled by inner components)
- Inner: a blue Primary Pill ("Try invideo") tucked into the right end
- Use: The hero search/prompt bar — the signature consumer-product moment

**Floating Play Button**
- Background: `oklab(0.999994 ... / 0.95)` ≈ `rgba(255, 255, 255, 0.95)`
- Text: Black (`#000000`)
- Padding: 24px 40px (oversized, generous)
- Radius: `9999px`
- Shadow: `rgba(0,0,0,0.1) 0 20px 25px -5px, rgba(0,0,0,0.1) 0 8px 10px -6px` — compound drop + tight pop
- Hover: `scale-110` (10% grow)
- Use: Floating play button absolutely positioned over video thumbnails

### Cards & Containers
- Background: White (`#ffffff`) on light sections; `#222222` or video imagery on dark sections
- Border: `1px solid rgba(0, 0, 0, 0.15)` for outlined cards; `0px` for default content cards relying on shadow only
- Radius: `8px`, `12px`, or `16px` — InVideo uses mid-range radii on cards (unlike its actions, which are always pill)
- Shadow: `rgba(0,0,0,0.1) 0 10px 15px -3px, rgba(0,0,0,0.1) 0 4px 6px -4px` for elevated cards
- Internal padding: 16–24px standard, scaling to 32–48px on hero feature cards

### Badges / Tags / Pills

**Outline Category Chip**
- Background: transparent
- Text: Near-black (`lab(2.75381 0 0)` ≈ `#0d0d0d`)
- Border: `1px solid rgba(0, 0, 0, 0.15)`
- Radius: `9999px`
- Padding: ~8px 16px
- Font: 14px Inter weight 400–500
- Use: Below-hero category row — "Movies", "Effects", "Vision", "Money Shot", "VFX House", etc.

**Outline Chip on Dark**
- Background: transparent
- Text: White
- Border: `1px solid rgb(55, 55, 55)` — charcoal hairline
- Radius: `9999px` or `10px` for variant treatments
- Use: Pricing-page filter pills, dark-section chips

### Inputs & Forms
- Hero "prompt input" is implemented as a `textarea` with no visible border — the dark gray pill (`#3a3a3a`) wrapping it provides the visual frame
- Background: transparent inside the wrapper
- Color: `#ffffff` on dark wrapper
- Border: `0px`
- Outline (focus): `oklab(0.708 0 0 / 0.5) none 1px`
- Padding: handled by parent pill container

### Navigation
- Top bar: white background, full width, logo wordmark left, mid-aligned product/pricing nav, right-aligned "Login" (white pill) + "Sign up" (blue pill)
- Above the nav: a full-bleed `#086de8` announcement bar with a single-line message (e.g., "Agent One: now live on invideo")
- Links: Inter 16–20px, weight 400–500, color `#000000` or `rgba(20, 20, 20, 0.7)`
- Hover: subtle text-color shift; no underline
- Logo: SVG wordmark `invideo` (lowercase) with a small dot/star mark

### Decorative Elements

**Video-Masked Text**
- The word "VIDEOS" in the hero is filled with cinematic footage rather than solid color — the typography becomes a video viewport. This is a one-time signature device, not a repeating system pattern.
- Implementation: `background-clip: text; color: transparent;` over a `<video>` element

**Pill Chip Row**
- A horizontally-scrolling row of outline pill chips below the hero — categories of generated video styles. Acts as both visual rhythm and a content tease.

**Full-bleed Blue Banner**
- The persistent `#086de8` announcement bar at the top of every page — small black-and-white logo dots flank a single white line of text. Treats the brand color as page chrome rather than accent.

## 5. Layout Principles

### Spacing System
- Base unit: 8px (the most-used value at 583 occurrences in the JSON — by far the dominant gap)
- Scale: 1px, 4px, 8px, 12px, 16px, 20px, 24px, 32px, 40px, 48px, 58px, 64px, 96px, 136px, 160px, 300px
- Notable: 8px and 16px do most of the work (583 + 167 occurrences). 12px (111) handles internal padding. The big jumps (96px, 136px, 300px) handle section breaks.
- Section padding: 38px and 58px appear as recurring odd-but-deliberate values — likely tied to the design system's "section padding" tokens

### Grid & Container
- Max content width: ~1280px for centered content; 1440px viewport reference
- Hero: centered single column, full viewport height not enforced
- Below hero: full-width horizontal scroll rows of video tiles (3-up visible at desktop)
- Feature sections: 2-column or single-column long-form depending on density
- Dark sections (`/ai`): full-bleed dark, stretched edge-to-edge with content centered

### Whitespace Philosophy
- **Hero gets the air**: The hero section runs ~600px tall with significant whitespace above and below the headline — letting the 92px display type breathe
- **Content rows pack tight**: Below the hero, video tile rows compress to maximize content density — a hard switch from editorial to product-grid mode
- **No micro-spacing fussiness**: 8px, 16px, 32px do the heavy lifting; mid-range odd values are rare

### Border Radius Scale
- Pill (`9999px`): All buttons, all chips, the hero prompt bar, the play button — anything actionable
- Card Medium (`8px`, `12px`): Default for content cards and tile chrome
- Card Large (`16px`): Larger feature cards, embedded video frames
- Mid (`22.5px`, `24px`, `44px`): Specialty values for half-pill or chunky-chip variants
- Sharp (`0px`): Reserved for inputs without visible chrome (the textarea inside the prompt pill) and section-level containers

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | `box-shadow: none` | Buttons, chips, hero canvas, section backgrounds |
| Border Hairline (Level 1) | `1px solid rgba(0, 0, 0, 0.15)` | Outline pills, ghost cards, secondary buttons on white |
| Soft Lift (Level 2) | `rgba(0,0,0,0.1) 0 10px 15px -3px, rgba(0,0,0,0.1) 0 4px 6px -4px` | Default elevated card — feature cards, modal-like surfaces |
| Heavy Lift (Level 3) | `rgba(0,0,0,0.1) 0 20px 25px -5px, rgba(0,0,0,0.1) 0 8px 10px -6px` | Floating play buttons, prominent floating CTAs |
| Focus Ring (Accessibility) | `outline: oklab(0.708 0 0 / 0.5) none 3px` | All interactive elements on keyboard focus |

**Shadow Philosophy**: InVideo's depth system is restrained and Tailwind-conventional — it uses the standard `shadow-md` and `shadow-xl` patterns at 10% black opacity, no exotic colors, no inset effects, no offset stamps. The signature isn't *how* shadows are styled, it's *where they aren't* — buttons and chips get `none`, only true floating elements (play buttons, image overlays) earn elevation. This keeps the page feeling flat-but-clean and reserves elevation for moments that need to read as physically above the content layer. The double-shadow stack (one wide diffuse + one tight close) is a Tailwind/Material convention that simulates two light sources for realistic depth.

### Decorative Depth
- The hero prompt-bar pill sits flat on the white canvas — no shadow, no border, just the dark gray fill and the embedded blue CTA contrast
- Cards with imagery get the soft-lift shadow; pure-text cards stay flat with hairline borders
- No glow effects, no inner shadows, no neumorphism — strictly conventional drop shadows

## 7. Do's and Don'ts

### Do
- Use mediaSansSemiCondensed weight 900 uppercase ONLY for the hero billboard headline — one per page maximum
- Switch to Inter for everything below the hero — body, buttons, captions, nav
- Make every interactive surface a full pill (`9999px`) — buttons, chips, the prompt input
- Use InVideo Blue (`#086de8`) for primary CTAs and the announcement banner — that pairing is the brand
- Pair the hero prompt input (charcoal `#3a3a3a`) with a blue CTA pill tucked into the right end — that's the signature AI-product moment
- Keep card corner radius in the 8–16px range — only buttons go to full pill
- Use `1px solid rgba(0, 0, 0, 0.15)` hairline borders on outline pills and ghost cards
- Apply `-0.4px` letter-spacing on Inter body text at 16–18px for a slight visual tightening
- Use the standard Tailwind double-shadow stack for elevation; reserve it for genuinely floating elements
- Tuck a persistent blue announcement bar above the nav as page chrome, not a one-time promo

### Don't
- Don't use the 92px uppercase display headline more than once per page — it's a billboard, not a section style
- Don't introduce a second brand color — the system is mono + blue (with three near-identical blues that should ideally consolidate)
- Don't apply mid-range corner radius (4–6px) to buttons — actions are always full pill
- Don't apply pill radius to text content cards — content stays at 8–16px
- Don't use blurred shadows on every card — most surfaces stay flat with hairline borders
- Don't use `#000000` body text on dark sections; switch to `rgba(255, 255, 255, 0.9)` for AAA legibility
- Don't use uppercase on buttons or chips — uppercase is reserved for the hero
- Don't substitute a serif or rounded font for Inter — Inter is the system anchor
- Don't soften the white canvas to off-white — InVideo's neutrality is part of its consumer-product feel
- Don't omit the announcement bar — it's the page's most recognizable chrome element

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single-column, hero drops to 40–48px, prompt bar full-width, CTAs stack |
| Tablet | 640–1024px | 2-up tile grids, hero ~60–72px, nav still horizontal |
| Laptop | 1024–1280px | 3-up tile grids, hero ~80px, full multi-column feature sections |
| Desktop | ≥1280px | Maximum hero (92px), full content width, 4-up tile rows |

(Tailwind classes in the JSON reveal `laptop:` modifiers — InVideo uses a custom `laptop` breakpoint, not just `lg:`)

### Touch Targets
- Primary pill CTAs: 32–40px tap height min, 16–24px horizontal padding
- Category chips: ~32px tap height with 12–16px horizontal padding
- Top-nav links: generous spacing for thumb access on mobile
- Hero prompt input: full-width pill on mobile, ~600px wide on desktop

### Collapsing Strategy
- **Hero**: 92px → 60px → 40px scaling across breakpoints; uppercase and weight 900 maintained throughout
- **Prompt bar**: Always full-width of its container; on mobile becomes the most prominent element on the page
- **Category chips**: Wrap to multiple rows on tablet; horizontal-scroll on mobile if too many
- **Tile rows**: 4-up → 3-up → 2-up → horizontal-scroll on mobile
- **Nav**: Mid-nav links collapse to hamburger; logo + Login + Sign up persist
- **Announcement bar**: Stays full-bleed at all sizes; text shrinks but never disappears

### Image Behavior
- Video tiles maintain 16:9 aspect ratio across all breakpoints
- Hero "VIDEOS" text-mask video continues to play on mobile (no static fallback)
- Tile thumbnails crop center on smaller widths
- Floating play buttons scale proportionally with their tile

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: InVideo Blue (`#086de8`)
- Primary CTA Large: InVideo Blue Light (`#277cee`)
- Page Background: Pure White (`#ffffff`)
- Primary Text: Pure Black (`#000000`)
- Secondary Text: Soft Black (`rgba(20, 20, 20, 0.7)`)
- Hero Prompt Surface: Charcoal (`#3a3a3a`)
- Outline Border: Hairline (`rgba(0, 0, 0, 0.15)`)
- Glass Button on Dark: `rgba(255, 255, 255, 0.12)` bg, `rgba(255, 255, 255, 0.9)` text
- Soft Card Shadow: `rgba(0,0,0,0.1) 0 10px 15px -3px, rgba(0,0,0,0.1) 0 4px 6px -4px`

### Example Component Prompts

- "Build a hero section on white (`#ffffff`) with a centered headline at 92px in mediaSansSemiCondensed weight 900, line-height 1.07, uppercase, color `#000000`. Sub-headline below at 16–20px Inter weight 400, color `rgba(20, 20, 20, 0.7)`."

- "Create the InVideo hero prompt bar: a `#3a3a3a` pill at `9999px` border-radius, ~600px wide, ~56px tall. Inside, place a `<textarea>` with white text on the left (placeholder 'Create…') and a blue (`#086de8`) pill button labeled 'Try invideo' tucked to the right end. The right-side button is 16px Inter weight 500, white text, padding 8px 16px, also `9999px` radius."

- "Design a primary blue pill button: background `#086de8`, text `#ffffff`, padding 8px 16px (compact) or 12px 16px (standard), border-radius `9999px`, Inter 16px weight 500, no shadow, focus ring `oklab(0.708 0 0 / 0.5) none 3px`."

- "Create an outline category chip row beneath the hero: each chip is a transparent pill with `1px solid rgba(0, 0, 0, 0.15)` border, `9999px` radius, padding 8px 16px, Inter 14px weight 400–500, color near-black. Examples: 'Movies', 'Effects', 'Vision', 'Money Shot', 'VFX House'."

- "Add a full-bleed announcement bar above the nav: background `#086de8`, height ~36px, white text centered at 14px Inter weight 500. Single-line message like 'Agent One: now live on invideo' with small black-and-white pill markers flanking the text."

- "Build a floating play button overlaid on a video thumbnail: white-95% (`rgba(255,255,255,0.95)`) background, padding 24px 40px, `9999px` radius, black play icon, shadow `rgba(0,0,0,0.1) 0 20px 25px -5px, rgba(0,0,0,0.1) 0 8px 10px -6px`. On hover: `scale-110`."

### Iteration Guide
1. Default to Inter for everything except the hero — and the hero is mediaSansSemiCondensed 900 uppercase at 92px, used exactly once per page
2. Make every action a full pill (`9999px` / `rounded-full`) — buttons, chips, the prompt bar, the play button. No mid-radius on actions.
3. The brand color is `#086de8` — use it on primary CTAs, the announcement bar, and the embedded "Try invideo" button inside the hero prompt. Don't introduce other accents.
4. White is the page canvas. Pure white, not off-white. Save dark backgrounds for product-feature pages like `/ai`.
5. Cards stay at 8–16px radius with hairline `rgba(0, 0, 0, 0.15)` borders or `shadow-md` lifts. Pick one — borders or shadows, not both.
6. The hero prompt bar (`#3a3a3a` pill with embedded blue CTA) is the brand's most distinctive component — use it whenever the page sells the AI-prompt experience.
7. Apply `-0.4px` letter-spacing on Inter body at 16–18px. It's subtle but it's there.
8. Reserve uppercase for the hero only. Buttons, links, chips all use sentence case.
9. Use the announcement bar as page chrome. It's not a banner you dismiss; it's part of the brand frame.
