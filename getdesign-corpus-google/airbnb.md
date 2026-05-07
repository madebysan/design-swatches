---
version: alpha
name: Airbnb
description: Travel-magazine consumer system — Rausch coral CTA on disciplined grayscale, full-bleed photography with 14–20px corner rounding, single-family Airbnb Cereal VF, signature stacked three-layer elevation.

colors:
  # Surface & background
  background: "#ffffff"
  surface: "#ffffff"
  surface-subtle: "#f7f7f7"
  surface-icon-button: "#f2f2f2"

  # Ink + text
  ink: "#222222"
  ink-inverted: "#ffffff"
  text-focused: "#3f3f3f"
  text-muted: "#6a6a6a"
  text-disabled: "#929292"
  text-tertiary: "#c1c1c1"

  on-background: "#222222"
  on-surface: "#222222"
  on-primary: "#ffffff"

  # Brand accents — Rausch family
  primary: "#ff385c"
  primary-deep: "#e00b41"
  plus: "#92174d"
  luxe: "#460479"

  # Semantic
  info: "#428bff"
  error: "#c13515"
  error-deep: "#b32505"
  disabled-overlay: "#3d3d3d"  # was rgba(0,0,0,0.24) — flattened for material-disabled

  # Borders & dividers
  border: "#dddddd"
  border-strong: "#222222"

  # Shadow tints
  shadow-light: "#f5f5f5"  # was rgba(0,0,0,0.04) — flattened
  shadow-medium: "#e6e6e6"  # was rgba(0,0,0,0.1) — flattened
  shadow-soft: "#fafafa"  # was rgba(0,0,0,0.02) — flattened

typography:
  heading-section:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0px
  heading-sub:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: -0.44px
  card-title:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 21px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0px
  listing-title:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.18px
  subtitle-bold:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0px
  body-medium:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  button-large:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  button-default:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0px
  caption-medium:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0px
  caption-bold:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0px
  caption-small:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0px
  micro:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  micro-bold:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0px
  badge-uppercase:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0px
  superscript:
    fontFamily: "Airbnb Cereal VF, Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif"
    fontSize: 8px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.32px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 14px
  lg: 20px
  xl: 32px
  pill: 9999px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-medium}"
    padding: 16px 24px

  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-medium}"
    padding: 8px 12px

  # Primary Rausch CTA
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-large}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
  button-primary-pressed:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"

  # Secondary outline button
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-default}"
    rounded: "{rounded.lg}"
    padding: 10px 16px

  # Circular icon button (back, share, favorite)
  button-icon-circular:
    backgroundColor: "{colors.surface-icon-button}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    size: 36px

  # Disabled state
  button-disabled:
    backgroundColor: "{colors.surface-icon-button}"
    textColor: "{colors.text-tertiary}"
    typography: "{typography.button-default}"
    rounded: "{rounded.sm}"
    padding: 14px 24px

  # Pill tab button (Homes / Experiences / Services)
  button-tab:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-medium}"
    rounded: "{rounded.none}"
    padding: 8px 14px
  button-tab-active:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Listing card — image + below-text
  card-listing:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 0px

  # Detail-page sticky booking panel
  card-booking:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px

  # Amenity grid card
  card-amenity:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-medium}"
    rounded: "{rounded.none}"
    padding: 16px 0

  # Review card
  card-review:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-medium}"
    rounded: "{rounded.none}"
    padding: 0px

  # Search pill (3-segment)
  input-search:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-medium}"
    rounded: "{rounded.xl}"
    padding: 14px 24px

  # Generic text input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-medium}"
    rounded: "{rounded.sm}"
    padding: 14px 16px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-focused}"
  input-error:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"

  # NEW pill badge (navy on tabs)
  badge-new:
    backgroundColor: "{colors.luxe}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro-bold}"
    rounded: "{rounded.xs}"
    padding: 2px 6px

  # Uppercase award badge
  badge-award:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-uppercase}"
    rounded: "{rounded.none}"
    padding: 4px 0

  # Footer / soft section block
  section-soft:
    backgroundColor: "{colors.surface-subtle}"
    textColor: "{colors.text-muted}"
    typography: "{typography.caption-medium}"
    rounded: "{rounded.none}"
    padding: 32px 24px
---

# Airbnb Design System

## Overview

Airbnb's 2026 design feels like a travel magazine that happens to be an app — pristine white canvases give way to full-bleed photography, and the interface itself disappears so the listings can breathe. The signature Rausch coral-pink (`{colors.primary}`) is used sparingly but unmistakably: search CTA, active tab indicator, primary action button, the occasional price or wishlist heart. Everything else is a disciplined grayscale, with `{colors.ink}` carrying almost every line of text.

What makes the system unmistakably Airbnb is how much *faith* it places in content. Property photos are displayed at hero scale, 4:3 with edge-to-edge radius treatment. Category switching happens through a tri-tab picker (Homes / Experiences / Services) that uses 3D rendered illustrated icons (a pitched-roof house, a hot-air balloon, a service bell) — physical, tactile, almost toy-like — paired with crisp `Airbnb Cereal VF` labels. This is the rare consumer product where 3D renders and purely typographic UI coexist without tension.

The newest surface is the **Experiences** product line — same chrome, but richer card density, more photography, and a center-anchored booking panel with sticky right-rail pricing. Listing detail pages (both rooms and experiences) follow a tight template: full-bleed hero image grid → overlapping rounded booking card (sticky on scroll) → amenities → reviews (Guest Favorite awards use a big centered `4.81` rating with a laurel-wreath lockup) → map → host profile → disclosures. The rhythm is consistent whether you're booking a room or a yacht tour.

**Key Characteristics:**
- Rausch coral-pink (`{colors.primary}`) as a single-accent brand color, used only for primary CTAs and the search button
- Full-bleed photography at 4:3 / 16:9 with gentle corner rounding (14–20px) as the primary visual vocabulary
- 3D rendered category icons paired with typographic tabs — the one place the system allows illustration
- Circular `pill` icon buttons (back arrow, share, favorite, carousel arrows) scattered throughout
- `Airbnb Cereal VF` carries every label, from 8px legal footnote to 28px section heading — a single-family system
- Product-tier color coding: Airbnb Plus (`{colors.plus}`), Airbnb Luxe (`{colors.luxe}`), Airbnb (Rausch coral)
- Guest Favorite award lockup — centered giant rating number between two laurel wreaths, one of the most recognizable moments in the system
- Sticky booking panel with a price → dates → guests stack, pinned to the right rail on desktop, transforming to a bottom-anchored "Reserve" bar on mobile
- Sticky bottom mobile navigation (Explore / Wishlists / Log in) with an active-state Rausch tint

## Colors

### Primary
- **Rausch** (`{colors.primary}`): The brand's signature coral-pink. Used for: primary "Reserve" button, search submit button, active tab underline, wishlist heart fill, pricing emphasis. The single highest-visibility color on every page.

### Secondary & Accent
- **Deep Rausch** (`{colors.primary-deep}`): A more saturated variant. Used for pressed/active button states and gradient terminal stops.
- **Plus Magenta** (`{colors.plus}`): The brand color for the Airbnb Plus product tier — a higher-end curated-listing offering.
- **Luxe Purple** (`{colors.luxe}`): The brand color for the Airbnb Luxe product tier — villa/estate-level rentals.
- **Info Blue** (`{colors.info}`): Used for legal/informational links (terms, privacy, disclosures) — the only non-monochrome link color in the system.

### Surface & Background
- **Canvas White** (`{colors.background}`): The default page background. Every card, every container, every detail page starts here.
- **Soft Cloud** (`{colors.surface-subtle}`): Subtle subsurface tint used on footer backgrounds, map-view wrappers, and "everything else" sections that want to step back from the primary white.
- **Hairline Gray** (`{colors.border}`): Ubiquitous 1px border color — separates cards, amenity rows, review panels, footer columns. The workhorse of the layout system.

### Neutrals & Text
- **Ink Black** (`{colors.ink}`): The system's near-black. Every heading, every body paragraph, every nav label, every price. Used for ~90% of all text on a page.
- **Charcoal** (`{colors.text-focused}`): Used in focused-state input text and one-step-down emphasis copy.
- **Ash Gray** (`{colors.text-muted}`): Secondary labels, subtitle-style copy under city names, muted footer links.
- **Mute Gray** (`{colors.text-disabled}`): Disabled buttons and low-priority metadata.
- **Stone Gray** (`{colors.text-tertiary}`): Tertiary dividers, icon strokes, placeholder avatars.

### Semantic & Accent
- **Error Red** (`{colors.error}`): Form validation errors, destructive-action warnings.
- **Deep Error** (`{colors.error-deep}`): Pressed/active variants of error states.
- **Disabled Overlay** (`{colors.disabled-overlay}`): Disabled material-style labels.

### Gradient System
Airbnb's brand gradient appears sparingly, typically only on the wordmark and the search-button branded moment:

```
linear-gradient(90deg, {colors.primary} 0%, {colors.primary-deep} 50%, {colors.plus} 100%)
```

This coral → magenta sweep is the "branded moment" — never used as a full surface, only as a narrow pill fill or logo treatment.

## Typography

### Font Family
- **Airbnb Cereal VF** (primary and only): The proprietary variable-weight sans-serif that carries the entire system. Fallbacks (in order): `Circular, -apple-system, system-ui, Roboto, Helvetica Neue, sans-serif`.

Weights observed: 500, 600, 700. No 400-regular — the system's "body" weight is 500, which gives every block of text a subtle extra density that reads as confident and deliberate.

OpenType features: `salt` (stylistic alternates) is used on the compact 11px and 14px 600-weight labels.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Use those tokens directly via reference rather than hardcoding values.

| Token | Use |
|---|---|
| `heading-section` | Page-level headings — "Inspiration for future getaways" |
| `heading-sub` | Content dividers — "What this place offers", "Meet the hosts" |
| `card-title` | Review panel headings, card lead titles |
| `listing-title` | Listing headlines on detail pages |
| `subtitle-bold` | Host name, city name |
| `body-medium` | Primary body copy on detail pages |
| `button-large` | "Reserve", "Become a host" |
| `button-default` | Standard button labels |
| `caption-medium` | Metadata, subtitle lines |
| `caption-bold` | `salt` feature — numeric stats, small-text emphasis |
| `caption-small` | Review dates, micro-metadata |
| `micro` | Footer disclaimers, legal micro-copy |
| `micro-bold` | "NEW" pill labels |
| `badge-uppercase` | `salt` feature — compact category/status badges |
| `superscript` | 8px uppercase — price footnotes, decimal tails |

### Principles
- **One family, many weights.** Airbnb Cereal VF handles everything from 8px legal to 28px page headings — the visual identity comes from the family itself, not from typeface mixing.
- **500 is the new 400.** The system's "regular" weight is 500, giving every paragraph a slightly more confident texture than the web default.
- **Negative tracking on display type only.** Headings 20px+ compress tracking by -0.18 to -0.44px to feel chiseled; body sizes stay at 0 tracking for readability.
- **Tight line-heights for headlines, generous for body.** Display type runs at 1.18–1.25 (tight); body and caption open up to 1.43 for long-form comfort.
- **No all-caps except at 8px.** The only uppercase transform in the system is the 8px superscript — everywhere else, sentence case with subtle weight shifts does the work.

### Note on Font Substitutes
Airbnb Cereal VF is proprietary. The closest open-source substitute is **Circular Std** (still commercial) or **Inter** (free, Google Fonts) with letter-spacing reduced by -0.01em at display sizes.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px, with off-grid values used for pixel-perfect icon alignment.

- **Section padding**: `3xl`–`4xl` top/bottom on desktop, `xl`–`2xl` on mobile
- **Card internal padding**: `xl` on booking panels and large cards, `lg` on amenity rows, `md` on listing-card metadata
- **Gutter between listing cards**: `xl` desktop, `lg` mobile
- **Between stacked text rows**: `xs`–`sm` (very tight — reinforces the "dense information" feel)

### Grid & Container
- **Max content width**: 1760–1920px on ultra-wide; 1280px on most detail pages
- **Homepage listing grid**: 6 columns at ≥1760px, 5 at ≥1440px, 4 at ≥1128px, 3 at ≥800px, 2 at ≥550px, 1 below
- **Detail page**: 2-column asymmetric — main content ~58%, sticky booking panel ~36% on the right, ~6% gutter
- **Footer**: 3-column Support / Hosting / Airbnb

### Whitespace Philosophy
Airbnb is densely informative but never cramped. Whitespace is used to *group* — listing cards have `xl` of gutter so each photograph reads as a distinct object, but the metadata under each card uses `xs`–`sm` gaps so the price/city/date feels like a single unit.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| 0 | No shadow | Listing cards, body content, text-only sections |
| 1 | Single subtle drop (`{colors.shadow-medium}` tint, ~12px blur) | Active/pressed icon buttons — subtle lift |
| 2 | Three stacked layers (1px hairline + 2px+6px + 4px+8px tints from `{colors.shadow-soft}`/`{colors.shadow-light}`/`{colors.shadow-medium}`) | Booking panel, modals, dropdown menus — signature three-layer elevation |
| Focus Ring | `0 0 0 2px {colors.border-strong}` | Active-state buttons, focused search input |
| White Separator Ring | `0 0 0 4px {colors.surface}` | Circular buttons overlaid on photographs — separates from colorful image backgrounds |

Shadow philosophy: Airbnb uses **stacked layered shadows** rather than a single drop. The three-layer booking-panel shadow reads as one cohesive lift but is actually three separate shadows at different opacity/blur values — creating subtle anti-aliasing at the shadow's perimeter that feels premium without being heavy.

### Decorative Depth
- **Photography as depth**: the system relies heavily on full-bleed photography to create visual depth
- **Laurel wreath lockup**: the Guest Favorite award uses two SVG laurel illustrations
- **3D rendered category icons**: Homes/Experiences/Services icons have soft internal lighting

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Flat sections, dividers |
| `xs` | 4px | Inline anchor tags, tag chips |
| `sm` | 8px | Text buttons, dropdowns, small utility buttons |
| `md` | 14px | Listing card photography, generic content containers, badges |
| `lg` | 20px | Primary rounded buttons (pill shape), large images, booking panel |
| `xl` | 32px | Search bar pill, extra-large containers |
| `pill` | 9999px | All circular icon buttons, all avatars, wishlist hearts |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly rather than reconstructing them.

### Buttons
- **`button-primary`** — Rausch CTA ("Reserve", "Search"). Active state adds `transform: scale(0.92)` plus a 2px Ink Black focus ring.
- **`button-secondary`** — White with Hairline Gray border, pill or rectangular.
- **`button-icon-circular`** — Back/share/favorite/carousel controls. Active adds `transform: scale(0.92)` plus a 4px white separator ring on photo backgrounds.
- **`button-disabled`** — Soft gray background, Stone Gray text.
- **`button-tab`** — Pill tab in the Homes/Experiences/Services category picker; active state shows a 2px Ink Black underline beneath the label.

### Cards & Containers
- **`card-listing`** — White background, `{rounded.md}` on the image, no container shadow. Metadata stacks below in `xs`–`sm` gaps.
- **`card-booking`** — Sticky right-rail panel with three-layer elevation, `{rounded.md}`, 24px padding, 370px width.
- **`card-amenity`** — Per-row amenity item. Hairline Gray top/bottom borders.
- **`card-review`** — 40px circular avatar + name + date row, body paragraph below.

### Inputs & Forms
- **`input-search`** — Three-segment pill (Where/When/Who) wrapped in 1px Hairline Gray, 32px radius, with a subtle floating shadow.
- **`input`** — Generic text input, focuses to Ink Black border with 2px outer ring; error switches to Error Red.
- **Date Picker** — 7-column calendar with circular `pill` day cells; selected range uses Ink Black background with white numerals.

### Navigation
- **Top Nav (Desktop)** — ~80px tall, white bg, Rausch wordmark left, tri-tab category picker center, "Become a host" + globe + avatar right.
- **Top Nav (Mobile)** — Single-row search pill full width; tri-tab picker below; bottom-fixed tab bar (Explore / Wishlists / Log in).
- **Listing Detail Secondary Nav** — Sticky horizontal anchor links (Photos · Amenities · Reviews · Location · Host).

### Image Treatment
- **Primary aspect ratios**: 4:3 for grids, 16:9 for experience hero, 1:1 for avatars
- **Radius**: `{rounded.md}` on listing-grid images, `{rounded.lg}` on detail-page hero frames, `{rounded.pill}` on avatars
- **Image grid on detail pages**: five-photo layout (1 large + 4 small)
- **Carousel**: circular 32px arrow buttons overlay the image, page-dot indicators 12px above bottom edge

### Signature Components
- **Guest Favorite Award Lockup** — Centered rating number at 44–56px 700-weight, laurel-wreath SVG illustrations flanking, "GUEST FAVORITE" label below in `{typography.badge-uppercase}`.
- **Tri-Tab Category Picker** — Three tabs (Homes / Experiences / Services) with 3D-rendered illustrated icons above 16px 500 labels; active tab has a 2px Ink Black underline; "NEW" pill on Experiences and Services.
- **Inspiration City Grid** — Text-only 6-column grid; city name 16px 600 + rental-type subtitle 14px 500 Ash Gray.
- **Reserve Sticky Card** — Pinned 120px below viewport top on desktop; collapses to a full-width bottom bar on mobile.
- **Experience Host Card** — 3:2 cover photo with circular avatar overlapping bottom edge.
- **"Things to know" Strip** — 3-column grid (House rules, Safety & property, Cancellation policy).

## Do's and Don'ts

### Do
- Reserve Rausch (`{colors.primary}`) for primary actions and the active-tab indicator — never dilute it with decorative uses.
- Let photography breathe — 4:3 crops with 14–20px rounded corners, no overlaid text, no gradient scrims.
- Use Ink Black (`{colors.ink}`) for every text layer below Rausch — this is the system's near-black, never true `#000000`.
- Pair the tri-tab category picker's 3D illustrated icons with flat typography — don't mix illustration styles within a single surface.
- Stack three low-opacity shadows to create the signature booking-panel elevation.
- Use Hairline Gray (`{colors.border}`) 1px borders for every card-to-card and row-to-row divider.
- Treat the booking panel as sticky on desktop, collapsing to a bottom-anchored reserve bar on mobile.
- Use `xs`–`sm` spacing within metadata groups and `xl` between cards — information density is intentional.

### Don't
- Don't introduce secondary accent colors outside the Rausch / Plus Magenta / Luxe Purple product-tier palette.
- Don't place text inside photographs — captions always sit below the image, never overlaid.
- Don't use all-caps labels except the single 8px superscript role.
- Don't round icon buttons to anything other than `{rounded.pill}` — circular is the system's signature geometry.
- Don't add drop shadows to listing cards — they sit on white canvas with no elevation.
- Don't use gradient backgrounds — the only gradient in the system is a narrow Rausch → magenta sweep on the wordmark.
- Don't use the 400-regular font weight — Airbnb Cereal's body weight is 500.
- Don't override Airbnb Cereal VF with a different display face — the system is intentionally single-family.

---

## Responsive Behavior

### Breakpoints

Airbnb declares ~60 breakpoints, but the meaningful layout shifts happen at a much smaller set:

| Name | Width | Key Changes |
|------|-------|-------------|
| Ultra-wide | ≥1760px | 6-column listing grid, 1760–1920px max content width |
| Desktop XL | 1440–1759px | 5-column grid, full nav visible, sticky right-rail booking panel |
| Desktop | 1128–1439px | 4-column grid, sticky booking panel persists |
| Laptop | 1024–1127px | 3–4 column grid, category nav remains horizontal |
| Tablet | 800–1023px | 3-column grid, global search may collapse to a single-row pill |
| Small tablet | 550–799px | 2-column grid, booking panel drops to full-width inline block |
| Mobile | 375–549px | 1-column stacked layout, bottom-fixed tab bar appears |
| Small mobile | <375px | Edge padding tightens to 16px; category-picker icons shrink to ~28px |

### Touch Targets
All interactive elements meet or exceed 44×44px. The circular icon button family is specifically sized 32–44px with 8–12px extended hit-area padding. The Rausch primary Reserve button is ~48px tall.

### Collapsing Strategy
- **Nav**: Top nav keeps Airbnb wordmark + tri-tab picker on tablet and above; on mobile the picker slides just below the search pill, and the globe/avatar controls move to a bottom-anchored tab bar.
- **Search bar**: Three-segment pill on desktop; collapses to a single-row "Start your search" pill on mobile.
- **Booking panel**: Sticky right-rail on ≥1128px; inline within the main content column between 800–1127px; bottom-fixed "Reserve" pill on <800px.
- **Listing grid**: Reflows 6 → 5 → 4 → 3 → 2 → 1 columns across breakpoints.
- **Detail-page image grid**: Five-image layout on desktop; swipeable full-bleed carousel on mobile.
- **Footer**: 3-column layout collapses to stacked single-column at <800px.

### Image Behavior
- `loading="lazy"` universal, with blurred preview thumbs served first
- Responsive images use Airbnb's `muscache.com` CDN with `im_w` query parameter
- No art-direction crops — same image scales up/down across breakpoints
- Carousels maintain a consistent 4:3 ratio regardless of source aspect

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Rausch (`{colors.primary}`)
- Page background: Canvas White (`{colors.background}`)
- Subsurface: Soft Cloud (`{colors.surface-subtle}`)
- Heading / body text: Ink Black (`{colors.ink}`)
- Secondary text: Ash Gray (`{colors.text-muted}`)
- Border / divider: Hairline Gray (`{colors.border}`)
- Error: Error Red (`{colors.error}`)
- Info link: Info Blue (`{colors.info}`)
- Luxe tier accent: Luxe Purple (`{colors.luxe}`)
- Plus tier accent: Plus Magenta (`{colors.plus}`)

### Example Component Prompts
- "Create a primary Reserve button: Rausch (`{colors.primary}`) background, white Airbnb Cereal 500-weight label at 16px, 14px × 24px padding, 8px border-radius, no shadow. On active/pressed add `transform: scale(0.92)` with a 2px Ink Black focus ring."
- "Build a listing card with a 4:3 full-bleed photograph at 14px border-radius, no container shadow; below the image stack three text rows with 4px gaps: city name at 16px 600 Ink Black, rental type at 14px 500 Ash Gray (`{colors.text-muted}`), and price range in 16px 500 Ink Black with a 14px `per night` suffix."
- "Design a sticky booking panel: white background, 14px border-radius, 1px Hairline Gray (`{colors.border}`) border, three-layer elevation shadow, 24px padding, 370px width, pinned 120px below viewport top on desktop. Contents: price headline, date picker, guest dropdown, Rausch primary CTA, and a 12px Ash Gray `You won't be charged yet` disclaimer."
- "Create a tri-tab category picker: three equal-width tabs labeled Homes, Experiences, Services; each tab has a ~48px 3D-rendered illustrated icon above a 16px 500 Ink Black label; active tab gets a 2px Ink Black underline; add a small 12px 700 white `NEW` pill on a dark navy background to the top-right of the Experiences and Services icons."
- "Render the Guest Favorite award lockup: a centered rating number at 52px 700-weight Ink Black, flanked left and right by hand-drawn SVG laurel wreaths at ~48px tall; below, a 12px 700 uppercase `GUEST FAVORITE` label with 0.32px tracking; sub-label at 14px 500 Ash Gray; full-width block sitting directly on white canvas with no container border."

### Iteration Guide
1. Focus on ONE component at a time.
2. Reference specific color names and hex codes from this document.
3. Use natural language descriptions alongside measurements.
4. Describe the desired "feel" ("magazine-like, photography-first" vs "dense utility").
5. Always default to Airbnb Cereal VF 500-weight for body and 600–700 for emphasis — never 400.
6. Keep Rausch pink scarce — if more than one Rausch-colored element appears per viewport, consider whether one should be neutralized.

### Known Gaps
- Homepage listing grid cards: inferred from Inspiration grid; confirm against live site for production.
- Experiences category icons: 3D illustrated icons served as raster assets; exact source-file specs not documented.
- Animation and transition timings: not captured.
- Dark mode: Airbnb does not ship a native dark mode in the extracted product surfaces.
