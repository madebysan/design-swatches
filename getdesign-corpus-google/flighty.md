---
version: alpha
name: "Flighty"
description: "Token-first design system reference for Flighty."

colors:
  background: "#ffffff"
  surface: "#250160"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#faf8f7"
  primary: "#010a1a"
  on-primary: "#ffffff"
  border: "#f7ab38"
  focus-ring: "#010a1a"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 50px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 25px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
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

# Flighty Design System

## Overview

Flighty's marketing site is what happens when an iOS-native app team builds the website with the same care they put into the product. The page reads as a film about flight: you scroll through chapters that alternate between bright, conversational hero sections (white canvas, oversized black headlines, hand-drawn arrows) and full-bleed cinematic dark passages where an iPhone floats over a sunset-orange tarmac or a deep-navy "departures board" night scene. There is no decorative chrome — every visual is either the product itself rendered at fidelity, a real travel photograph, or a piece of paper-stock UI texture (passport stamps, boarding pass corners, ticket-stub serifs). The brand voice is "calm authority for nervous flyers", and the page composition mirrors that: clear, uncrowded, but unafraid of dense data when data is the point.

The dominant visual move is **iPhone-as-hero**. A single hand holding a single iPhone, set against a real landscape (sunset cabin window, glowing departure board, JFK at dusk), repeats across sections like a recurring shot in a director's reel. Around the device, real Flighty UI cards float in space — gate-change notifications, baggage-belt readouts, weather chips — visually detached from the phone but rendered in the app's actual SF-Pro typography so the marketing surface and the product surface speak the same language. The cards use `rgba(255,255,255,0.08)` glass fills with subtle 1px hairlines, a treatment lifted directly from iOS 17/18 material chrome.

Where most utility apps lean blue-and-bright, Flighty leans **dusk**. The signature gradient palette runs from deep navy (`#010a1a`) through a warmed plum (`#250160`) to sunset amber (`#F7AB38`) — the actual color sequence of an evening departure. Bright white sections exist (the opening fold, FAQ, footer credits) but they're paced as breathers between the dark cinematic stretches. Even the white canvas isn't pure: it carries a slight warm tint (`#faf8f7`) that prevents the screen-glare feeling and matches the off-white of an airline boarding pass.

**Key Characteristics:**
- iPhone-as-hero composition repeated across sections — single device, hand-held, real-world background
- Dusk palette: deep navy `#010a1a` → plum `#250160` → amber `#F7AB38` mirrors evening flight light
- Inter for marketing prose, SF Pro for in-product UI cards — typographic fidelity to iOS
- EB Garamond + IBM Plex Mono used as "travel artifact" accents — passport-stamp serif and ticket-stub mono
- Floating iOS notification cards rendered with `rgba(255,255,255,0.08)` glass and 1px hairlines
- Hand-drawn red arrows and circles annotate key UI moments — designer-as-narrator energy
- Warm off-white `#faf8f7` for light sections, never pure `#ffffff`
- Pill-shaped primary CTA in deep ink with white wordmark — App Store button DNA
- Real photography only — no illustrations, no stock 3D, no abstract shapes

## Colors

### Primary
- **Flighty Ink** (`#010a1a`): The defining dark — a near-black with a navy lean. Used for hero dark backgrounds, primary CTAs, footer chrome, and the brand logo square. Reads as "night sky over the runway".
- **Flighty Plum** (`#250160`): Mid-stop in the dusk gradient — the moment between night and sunset. Used for radial gradient fills behind device hero shots.
- **Cabin White** (`#faf8f7`): The warm off-white page canvas. Carries the boarding-pass, paper-stock feeling that distinguishes Flighty from generic SaaS bright-white.
- **Pure White** (`#ffffff`): Reserved for headline text on dark surfaces and high-fidelity in-product UI cards.

### Brand Accent
- **Sunset Amber** (`#F7AB38`): The signature warm accent — pulled from the cabin-window photography that runs through the dark sections. Applied to highlight chips, priority status pills, and decorative gradient overlays. Does most of the "premium" emotional work.
- **Departure Purple** (`#977BD3`): A muted lavender used for select badge fills, chart accents, and informational status indicators. Pairs with plum for the dusk-mode palette.

### iOS Status Colors (lifted from product)
- **System Blue** (`#0099FF`): Live-tracking active state, "on time" indicators, primary in-product accent. Pulled directly from iOS system blue.
- **Alert Red** (`#D92D20`): Cancellations, gate changes, and the hand-drawn marketing annotations that circle UI moments. Always paired with white text.
- **Confirm Green** (`rgb(10, 137, 53)`): On-time confirmations, successful states, "landed" indicators.
- **Warning Amber** (`rgb(247, 144, 9)`): Delay warnings, weather advisories — distinct from Sunset Amber by being more saturated and orange-leaning.

### Neutrals & Text
- **Ink Body** (`#0a0e0c`): Primary text on light canvas — slightly warmer than pure black.
- **Mid Gray** (`#797979`): Secondary text, captions, metadata under flight cards.
- **Hairline Gray** (`#E2E2E2`): 1px borders on light surfaces, divider lines between FAQ rows.
- **Quiet Gray** (`#A4A4B8`): Secondary text on dark surfaces — readable but recessed.

### Surface & Glass
- **Cool Off-White** (`#fafafa`): Subtle alternative panel background on light sections.
- **Glass White** (`rgba(255, 255, 255, 0.08)`): The signature floating-card fill on dark hero shots — direct lift from iOS material chrome.
- **Glass Hairline** (`rgba(255, 255, 255, 0.14)`): 1px borders on glass cards.
- **Deep Surface** (`#080116`): Alternative dark panel — the "between sections" navy used for dense data backgrounds.

### Gradient System
- **Dusk Hero**: `linear-gradient(180deg, #010a1a 0%, #120036 45%, #250160 75%, #F7AB38 100%)` — the signature evening sky gradient behind device hero shots
- **Subtle Card Lift**: `linear-gradient(180deg, rgba(255,255,255,0.04) 0%, rgba(255,255,255,0) 100%)` — used inside glass cards to suggest light from above
- **Amber Glow**: `radial-gradient(circle at 50% 100%, #F7AB38 0%, transparent 60%)` — atmospheric warm wash anchoring device shots from below

## Typography

### Font Family
- **Primary (marketing prose)**: `Inter`, with `Inter Variable` for fluid weight transitions. Fallback: `-apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif`
- **In-Product UI (rendered cards)**: `SF Pro Text` at weights Regular/Medium/Semibold/Bold — never substituted, because the marketing cards mirror real iOS UI
- **Travel Artifact (accent)**: `EB Garamond` for passport-stamp serif moments — section eyebrows, decorative quotes, "Pilot's note" callouts
- **Data / Ticket-Stub**: `IBM Plex Mono` and `Fragment Mono` for flight numbers, gate codes, timestamps — anywhere the page wants to feel like it's printed on thermal paper

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Inter | 72px (4.5rem) | 700 | 1.05 | -0.025em | "Get the truth when you travel" |
| Display Large | Inter | 56px (3.5rem) | 700 | 1.08 | -0.02em | Section opener headlines |
| Display | Inter | 44px (2.75rem) | 700 | 1.10 | -0.02em | Feature section titles |
| Section Heading | Inter | 36px (2.25rem) | 700 | 1.15 | -0.015em | "Share your flying with friends and family" |
| Sub-heading | Inter | 28px (1.75rem) | 600 | 1.25 | -0.01em | Card titles, sub-section markers |
| Sub-heading Small | Inter | 22px (1.375rem) | 600 | 1.30 | -0.005em | In-card titles, FAQ questions |
| Body Large | Inter | 18px (1.125rem) | 400 | 1.55 | normal | Hero subtitle, intro paragraphs |
| Body | Inter | 16px (1rem) | 400 | 1.55 | normal | Standard reading text |
| Nav Link | Inter | 15px (0.9375rem) | 500 | 1.00 | normal | Top navigation |
| Button | Inter | 15px (0.9375rem) | 600 | 1.00 | -0.005em | Pill CTA labels |
| Caption | Inter | 13px (0.8125rem) | 500 | 1.40 | 0.01em | Metadata, footer |
| Stamp Eyebrow | EB Garamond | 14px (0.875rem) | 500 italic | 1.20 | 0.02em | "From the team" / "A note" framing |
| Flight Number | IBM Plex Mono | 14–18px | 500 | 1.00 | 0.05em | "JFK → LHR", "AA 100" |
| iOS UI Title | SF Pro Text | 17px | 600 | 1.20 | -0.022em | Floating notification card titles |
| iOS UI Body | SF Pro Text | 15px | 400 | 1.30 | -0.016em | Notification body, status text |

### Principles
- **Inter for the page, SF Pro for the product**: Whenever a marketing screen renders something that looks like the actual app (a notification card, a toast, a list row), it switches to SF Pro Text with iOS-correct sizes and tracking. This typographic honesty is the single most premium decision on the site.
- **Tight tracking on display**: Headlines run at `-0.02em` to `-0.025em` — Apple-marketing tight, not Stripe wide. Pairs with weight 700 to feel direct and confident, not airy.
- **Weight 700 ceiling for display, 600 for sub-heads**: Never goes to 800/900. The boldness comes from size and color contrast, not extreme weight.
- **EB Garamond as a stamp, not a body**: The serif appears as italic eyebrows or single-sentence callouts, never as paragraphs. It's a passport mark, not a reading face.
- **Mono for any code-shaped data**: Flight numbers, gate codes, dates, times — all mono. Reinforces "this is real data, captured precisely" without saying it.
- **Body line-height 1.55**: Generous reading rhythm. Flighty respects that travelers reading their site are often anxious — paragraphs need air.

## Layout

### Spacing System
- Base unit: 4px
- Scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128, 160px
- Inter-section spacing: 96–160px desktop, 64–96px mobile
- Card internal padding: 24–32px standard, 16px tight (dense data)
- Notification card internal padding: 14×16 — calibrated to iOS native

### Grid & Container
- Max content width: 1280px for marketing prose, 1440px for full-bleed cinematic sections
- Hero: text left (50–55%), iPhone hero right (45–50%) on desktop; stacked on mobile
- Feature sections alternate between text-left/device-right and device-left/text-right
- Full-bleed dark sections break the grid entirely — photography fills viewport edge-to-edge with text overlay
- Notification cards positioned via absolute positioning, scattered around device but never overlapping it

### Whitespace Philosophy
- **Cinematic chapters**: Each section is a self-contained scene — light hero, dark dusk, light feature breakdown, dark cinematic, light testimonials. Pacing matters as much as content.
- **Around-the-phone breathing**: The iPhone hero never gets crowded. Floating notification cards keep at least 24–48px clearance from the device edge.
- **Dense where data lives**: When a section is showing real flight data (the "Look back on your travels" passport view), spacing tightens to 12–16px to reflect the dense information of the actual app.

### Border Radius Scale
- 6px — small chips, status pills, in-product micro-elements
- 12px — input fields, App Store buttons, small cards
- 16px — primary cards, containers
- 18px — iOS notification cards (matches iOS native)
- 9999px — pill CTAs, status badges, navigation pills
- No 4px or 8px radius — Flighty's small-radius end is 6px; below that goes square

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, body text, inline content |
| Hairline (Level 1) | `1px solid #E2E2E2` border, no shadow | Light cards, FAQ row dividers |
| Lift (Level 2) | `0 1px 3px rgba(0, 0, 0, 0.04)` | Light cards, inputs, secondary buttons |
| Float (Level 3) | `0 8px 24px rgba(0, 0, 0, 0.32)` | iOS notification cards on dark scenes |
| Cinematic (Level 4) | `0 24px 80px rgba(0, 0, 0, 0.5)` | iPhone hero device, primary feature cards |
| Glow (Level 5) | `0 0 120px rgba(247, 171, 56, 0.3)` | Amber halo behind device on dusk scenes |

**Shadow Philosophy**: Flighty's depth model is photographic, not graphic. Shadows exist because the device is being lit by a real light source — usually the sunset behind it or the cabin overhead. The cinematic shadows under iPhone heroes are large and soft (80px blur, 24px offset, low opacity) to suggest the device is sitting in actual atmospheric light. The amber glow halo isn't a decorative effect; it's the visual logic of "this phone is on a tarmac at golden hour, of course it's warm-lit". Inside cards, shadows stay tiny — Flighty doesn't stack elevation; it stacks light sources.

### Decorative Depth
- iOS notification cards rely on glass blur (`backdrop-filter: blur(20px) saturate(180%)`) plus hairline borders for depth — the same recipe Apple uses
- Feature sections occasionally use a subtle inner glow (`inset 0 1px 0 rgba(255,255,255,0.04)`) on dark cards to suggest top-light pickup
- No mid-range graphic shadows (the boring SaaS `0 4px 12px rgba(0,0,0,0.1)` lift is absent) — Flighty either commits to atmospheric drama or stays flat

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

**Primary Pill (Get the App)**
- Background: Flighty Ink (`#010a1a`)
- Text: Pure White (`#ffffff`)
- Padding: 12px 20px
- Radius: `9999px` (full pill)
- Border: none
- Shadow: `0 1px 2px rgba(0, 0, 0, 0.08)` — subtle ground contact
- Font: 15px Inter weight 600, `-0.005em` tracking
- Hover: background lifts to `#0d0a14`, shadow grows to `0 2px 6px rgba(0, 0, 0, 0.12)`
- Use: Top-nav primary CTA, repeat across page

**App Store Black**
- Background: Pure Black (`#000000`)
- Text/Icon: Pure White (`#ffffff`)
- Padding: 10px 16px
- Radius: `12px`
- Includes Apple logo SVG + "Download on the App Store" two-line lockup
- Use: Hero CTA, footer download row — uses official App Store badge specs

**Sunset Amber Highlight**
- Background: Sunset Amber (`#F7AB38`)
- Text: Flighty Ink (`#010a1a`)
- Padding: 8px 14px
- Radius: `9999px`
- Font: 13px Inter weight 600, `0.01em` tracking, often uppercase
- Use: "Apple Design Award" tag, "Editor's Choice" badges — celebratory awards only

**Ghost Link**
- Background: transparent
- Text: Ink Body (`#0a0e0c`) on light, Quiet Gray (`#A4A4B8`) on dark
- Padding: 8px 12px
- Font: 15px Inter weight 500
- Hover: text shifts to full Pure White on dark, full Black on light
- Use: Nav links, secondary CTAs

### iOS Notification Card (the signature component)

- Background: `rgba(255, 255, 255, 0.08)` over dark hero, `#ffffff` over light
- Backdrop filter: `blur(20px) saturate(180%)` — full iOS material chrome
- Border: `1px solid rgba(255, 255, 255, 0.14)` on dark, `1px solid #E2E2E2` on light
- Radius: `18px` — matches iOS notification corner radius
- Padding: 14px 16px
- Shadow: `0 8px 24px rgba(0, 0, 0, 0.32)` on dark scenes for floating contact
- Font: SF Pro Text 17px weight 600 for title, 15px weight 400 for body
- Inner icon: 32×32px rounded-square app glyph, 8px gap to text
- Use: All floating-around-iPhone marketing chrome — gate changes, baggage chips, weather

### Cards & Containers
- Light card: `#ffffff` background, `1px solid #E2E2E2` border, `16px` radius, `0 1px 3px rgba(0,0,0,0.04)` shadow, 24–32px internal padding
- Dark card: `#080116` background, `1px solid rgba(255,255,255,0.08)` border, `16px` radius, no shadow (the dark eats it), 24–32px internal padding
- Glass card (over photography): `rgba(255,255,255,0.08)` fill, `rgba(255,255,255,0.14)` hairline, `18px` radius, `blur(20px)` backdrop

### Badges / Tags / Pills

**Award Tag**
- Background: Sunset Amber (`#F7AB38`) with subtle radial highlight
- Text: Flighty Ink (`#010a1a`)
- Padding: 4px 10px
- Radius: `9999px`
- Font: 12px Inter weight 600, `0.02em` tracking
- Often paired with a small SVG laurel or star glyph

**Status Pill (in-product)**
- "On Time" — Confirm Green fill, white text
- "Delayed" — Warning Amber fill, white text
- "Cancelled" — Alert Red fill, white text
- Padding: 2px 8px, radius `6px`, font SF Pro Text 11px weight 600 uppercase

**Flight Number Chip**
- Background: transparent or `rgba(0,0,0,0.04)`
- Text: Ink Body (`#0a0e0c`)
- Border: `1px solid #E2E2E2`
- Radius: `6px`
- Font: IBM Plex Mono 13px weight 500, `0.05em` tracking

### Inputs & Forms
- Background: Pure White (`#ffffff`)
- Border: `1px solid #E2E2E2`, `2px solid #0099FF` on focus
- Radius: `12px`
- Font: 16px Inter weight 400
- Padding: 12px 16px
- Focus shadow: `0 0 0 4px rgba(0, 153, 255, 0.12)`

### Navigation
- Top nav: white bar (`#ffffff` with `1px solid rgba(0,0,0,0.06)` bottom hairline), 64px tall, max-width 1280px centered
- Left: black square `Flighty` logo lockup (24×24 black tile + wordmark in Inter weight 700)
- Center: nav links (Pricing, Gift Cards, Passport, Airports, Help Center) at 15px Inter weight 500
- Right: Primary Pill CTA "Get the app" in Flighty Ink
- Sticky on scroll with subtle backdrop blur appearing after 80px

### Decorative Elements

**Hand-Drawn Annotation Arrows**
- SVG curved arrows in Alert Red (`#D92D20`), 2px stroke, slight wobble path
- Often paired with an italic EB Garamond label ("look here", "this!")
- Used in feature sections to point at specific UI elements inside the iPhone screen
- Designer-as-narrator energy — unique signature move

**Passport Stamp Frames**
- Decorative dashed-line rectangles (`2px dashed rgba(0,0,0,0.2)`)
- Wrap around special callouts ("Apple Design Award winner")
- Often paired with EB Garamond italic eyebrow text

**Glow Halo Behind Device**
- Radial gradient `#F7AB38` at 30% opacity, blurred 80px, sized larger than the device
- Sits behind iPhone shots in dark scenes — explains the warm tarmac light spilling onto the phone

## Do's and Don'ts

### Do
- Use Inter weight 700 for display headlines with `-0.02em` tracking — confident, Apple-marketing tight
- Switch to SF Pro Text whenever rendering anything that simulates the actual app — typographic fidelity is the brand
- Build hero compositions around a single iPhone in a real-world environment — never floating in abstract space
- Use the dusk gradient (`#010a1a` → `#250160` → `#F7AB38`) for cinematic dark sections
- Apply `rgba(255,255,255,0.08)` glass fill with `blur(20px)` backdrop on floating notification cards
- Include hand-drawn red arrow annotations to point at specific UI moments — designer-as-narrator energy
- Use IBM Plex Mono for any flight numbers, gate codes, or ticket-stub data
- Use EB Garamond italic only as eyebrow accent, never as body
- Pair full-bleed dark cinematic sections with bright `#faf8f7` light sections — chapter pacing
- Use `9999px` pill radius on the primary CTA — App Store button DNA
- Add a subtle amber radial glow behind iPhone hero shots — atmospheric tarmac light

### Don't
- Don't use pure white (`#ffffff`) for the page canvas — always warm off-white `#faf8f7`
- Don't use illustrations, 3D abstractions, or stock photography — only real travel photography and real product UI
- Don't apply gradient fills to text, buttons, or chrome — gradients are reserved for atmospheric backgrounds
- Don't use rounded-square device frames at the wrong corner radius — match iPhone 15 Pro chamfer (`55px` external)
- Don't use the dusk gradient on light sections — it only lives in cinematic dark passages
- Don't crowd the iPhone with notification cards — 24–48px breathing space minimum
- Don't use SF Pro outside of in-product UI simulations — the marketing prose stays Inter
- Don't use Sunset Amber (`#F7AB38`) for primary CTAs — it's an accent and award color, not an action color
- Don't use generic SaaS shadows (`0 4px 12px rgba(0,0,0,0.1)`) — Flighty either goes cinematic or stays flat
- Don't add weight 800/900 anywhere — display ceiling is 700
- Don't use mid-range corner radius (8–10px) — go 6 (chip), 12 (input), 16 (card), 18 (iOS card), or 9999 (pill)

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, hero type 36–44px, iPhone scales to 280px wide |
| Mobile Large | 640–768px | Single column, hero type 48px, two-column FAQ begins |
| Tablet | 768–1024px | Two-column hero, 56px headlines, floating cards reduce to 2–3 |
| Desktop | 1024–1280px | Full multi-column layout, 64–72px hero, all floating cards visible |
| Large Desktop | ≥1280px | Maximum scale (72px hero), 1280–1440px container, full cinematic full-bleed |

### Touch Targets
- Primary CTAs: 44px minimum height, 20px horizontal padding on mobile
- Nav links: 44×44 tap area even when label is 15px text
- iOS notification card mocks: non-interactive, but maintain 18px radius for visual consistency

### Collapsing Strategy
- **Nav**: Horizontal links collapse to hamburger at <900px, full-screen overlay menu on open with the same dark `#010a1a` background
- **Hero**: 72px → 56px → 44px → 36px progressive scaling, weight 700 maintained throughout
- **iPhone composition**: On mobile, iPhone moves below hero text and floating cards reduce from 5–6 to 2–3 most-essential ones, repositioned to sides
- **Cinematic dark sections**: Maintain full-bleed at all sizes; iPhone shrinks to 60% of viewport width on mobile rather than maintaining absolute size
- **Section spacing**: 160px desktop → 96px tablet → 64px mobile, but never tighter than 64px

### Image & Photography Behavior
- Hero photography stays art-directed across breakpoints — no crops or alternates
- iPhone device shots maintain pixel sharpness via 2x/3x asset serving
- Glass blur effects gracefully degrade on older browsers (fall back to `rgba(255,255,255,0.18)` solid)
- Dusk gradient backgrounds use CSS gradients (not images) so they scale infinitely

---

## Agent Prompt Guide

### Quick Color Reference
- Page Canvas (Light): Cabin White (`#faf8f7`)
- Page Canvas (Dark): Flighty Ink (`#010a1a`)
- Primary CTA: Flighty Ink (`#010a1a`) pill with white text
- Award Accent: Sunset Amber (`#F7AB38`)
- iOS System Blue: `#0099FF` (live tracking, on-time)
- Alert Red: `#D92D20` (cancellations, hand-drawn arrows)
- Confirm Green: `rgb(10, 137, 53)` (on-time, landed)
- Glass Card: `rgba(255, 255, 255, 0.08)` with `blur(20px)` backdrop
- Hairline (light): `1px solid #E2E2E2`
- Hairline (dark): `1px solid rgba(255, 255, 255, 0.14)`
- Dusk Gradient: `linear-gradient(180deg, #010a1a 0%, #250160 65%, #F7AB38 100%)`

### Example Component Prompts
- "Create a hero section on Cabin White (`#faf8f7`) with a headline at 72px Inter weight 700, line-height 1.05, letter-spacing -0.025em, color `#0a0e0c`. Place a single iPhone 15 Pro mockup right-aligned, 480px tall, with a `0 24px 80px rgba(0,0,0,0.5)` shadow. Surround it with 4–5 floating iOS notification cards using `rgba(255,255,255,0.08)` background, `blur(20px) saturate(180%)` backdrop filter, `1px solid rgba(255,255,255,0.14)` border, `18px` radius, SF Pro Text 17px weight 600 titles."
- "Build a primary pill CTA — Flighty Ink (`#010a1a`) background, Pure White text, `9999px` radius, padding 12px 20px, 15px Inter weight 600, `-0.005em` tracking, subtle `0 1px 2px rgba(0,0,0,0.08)` shadow. Hover lifts to `#0d0a14` background and `0 2px 6px rgba(0,0,0,0.12)` shadow."
- "Design a cinematic dark section with the dusk gradient (`linear-gradient(180deg, #010a1a 0%, #250160 65%, #F7AB38 100%)`). Center a single iPhone with a `120px` blurred amber radial glow behind it (`#F7AB38` at 30% opacity). Headline overlay in Inter 56px weight 700 in pure white at top-left, EB Garamond italic eyebrow at 14px above it."
- "Create a flight number chip — transparent background, `1px solid #E2E2E2` border, `6px` radius, IBM Plex Mono 13px weight 500, `0.05em` tracking, color `#0a0e0c`, padding 4px 8px. Display 'JFK → LHR' format."
- "Render an in-product status pill: Confirm Green `rgb(10, 137, 53)` fill, white text, SF Pro Text 11px weight 600 uppercase, `6px` radius, padding 2px 8px. Label: 'ON TIME'."
- "Build a hand-drawn annotation: 2px stroke curved SVG arrow in Alert Red (`#D92D20`) with a slight wobble path. Pair with EB Garamond italic 14px label ('look here') in the same red. Position pointing at a specific element inside an iPhone screen mockup."

### Iteration Guide
1. Default to Inter weight 700 with tight `-0.02em` tracking for any display headline — Apple-marketing precision
2. Switch to SF Pro Text the moment you render anything resembling the actual app — typographic fidelity matters
3. Hero compositions = single iPhone in real-world photography, surrounded by floating glass notification cards. Never abstract.
4. Light sections use Cabin White (`#faf8f7`), never pure white. Dark sections use Flighty Ink (`#010a1a`) or the dusk gradient.
5. Pill CTAs (`9999px` radius) for primary actions; App Store badges for download CTAs; Sunset Amber pills only for awards/honors.
6. Glass cards: `rgba(255,255,255,0.08)` fill + `blur(20px)` backdrop + hairline border + `18px` radius. Always.
7. Use IBM Plex Mono for flight data (numbers, codes, times) and EB Garamond italic for stamp-style eyebrow accents.
8. Shadow strategy: cinematic (`0 24px 80px rgba(0,0,0,0.5)`) for hero devices, `0 8px 24px rgba(0,0,0,0.32)` for floating cards, hairline-only for content cards. Skip the SaaS mid-range entirely.
9. Hand-drawn red arrows pointing at UI moments are signature — use sparingly but use them.
10. Pace the page in chapters: light → dark cinematic → light feature → dark cinematic → light close. Each section is a scene.
