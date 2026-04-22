# Design System Inspired by Ivory (Tapbots)

## 1. Visual Theme & Atmosphere

Tapbots has been carving dimensional iOS buttons since iPhone OS 2 — Paul Haddad and Mark Jardine have spent nearly two decades insisting that software should feel like a physical object. Tweetie, Twitterrific-adjacent, Tweetbot, Pastebot, Calcbot — every one of their apps has shipped with the same quiet philosophy: the screen is a surface, not a window. Buttons have backs. Icons have weight. Toggles click. When you pull-to-refresh, the r2-d2-meets-Atari sound isn't a gimmick — it's a reminder that you just did something physical. Ivory, their post-Twitter Mastodon client, is the purest expression of that legacy they've ever shipped. It carries the entire Tapbots craft signature into the federated timeline.

The Ivory homepage (tapbots.com/ivory) is a dark, warm, almost cinematic stage built around the product. The background is an off-black `#1a1a1a` — never pure `#000`, because Tapbots treats pure black as clinical and Ivory is *warm*. A muted lavender-periwinkle mist (`#cdd4f8`) bleeds through the hero as ambient atmosphere. The mascot — the iconic red-outlined Tapbots bird, descended from the original "bot" robot face — sits in the footer like a signature. Iconography is custom-drawn, not licensed. Every screen shown is a real iOS screenshot with SF Pro Display text kerned to iOS defaults. The site doesn't try to look like a website; it tries to look like an iOS app someone tilted into landscape.

What sets Ivory apart from every other "we made a dark website" moment in 2026 is its commitment to **tactile button construction.** Every primary CTA — "Download on the App Store," "Need Help with Ivory?" — is a miniature object: a rounded capsule with a pill-gradient fill (warm purple `#ba94ff` → soft lavender `#deccff`), an inset top-edge highlight simulating a light source overhead, a drop shadow pooling below, and a subtle ring of border color holding the whole thing together. This is the same button recipe Tapbots has been refining since Tweetbot 1.0 in 2011. It is the opposite of flat design. It is the opposite of "clean." It is *crafted* — and that word, overused everywhere else, is load-bearing here.

**Key Characteristics:**
- Off-black warm dark background (`#1a1a1a`) — never pure black
- SF Pro Display/Text native Apple stack — `-apple-system` first, no webfont downloads
- Dimensional CTA buttons with inset highlights + drop shadows + gradient fills
- Tapbots red mascot bird (`color(display-p3 1 0.302 0.302)` ≈ `#FF4D4D`) as brand signature
- Purple-lavender accent spectrum (`#ba94ff` → `#deccff` → `#cdd4f8`) borrowed from Ivory's app icon
- Pill geometry: 40px border-radius on CTAs, 18px on feature cards
- Light weight 300 on large SF Pro Display headings, 600 on product-name moments
- Native iOS screenshots embedded as product hero — no mockups, no illustrations
- Small footer type (16px) with uppercase section headers — mirrors iOS Settings app
- Hand-crafted iconography — the Tapbots "mascot" bird is never outsourced

## 2. Color Palette & Roles

Ivory's palette lives almost entirely in the dark-mode register, but Tapbots has historically shipped their apps with both a light (Ivory) and dark (Ebony-equivalent) theme — the product name itself is a nod to the piano-key duality. The marketing site leans into the dark treatment to showcase the app's atmosphere, but the purple accents carry over identically to the light theme with tuned contrast. Warmth is the common thread: neutrals are cool-white gray scaled down, not blue-gray or true neutral.

### Primary
- **Off-Black Warm** (`#1a1a1a`): Page background, section surfaces. The foundational dark — never `#000`, always slightly warmer to prevent clinical harshness.
- **Paper White** (`#ffffff`): Primary body text on dark, button text on CTAs, headings. Pure white reads cleanly against the off-black warmth.
- **Ivory Purple** (`#ba94ff`): Primary CTA gradient start, link accent, hero glow. The brand purple — saturated but soft, more periwinkle than royal.

### Purple Accent Spectrum
- **Lavender Light** (`#deccff`): Button gradient terminus, soft highlight tint. Pairs with `#ba94ff` to make the signature CTA gradient.
- **Periwinkle Mist** (`#cdd4f8`): Hero atmospheric glow, decorative background washes. The most atmospheric tone in the palette — light blue-violet.
- **Purple Deep** (`#4c278e`): Active/visited link on certain dark surfaces (`rgb(76, 39, 142)` weight 600). A denser purple for visited or tapped states.

### Signature Accent
- **Tapbots Red** (`#FF4D4D` — display-P3 `color(display-p3 1 0.302 0.302)`): The mascot bird outline, key hover links ("Mastodon," "Contact Us"), brand punctuation. Display-P3 gauged — on a wide-gamut display this red is noticeably more saturated than sRGB would allow.

### Neutral Scale (all warm-tuned)
- **Text Strong** (`#ffffff`): Headlines on dark backgrounds, product names.
- **Text Primary** (`#c3c3c3`): Body copy on dark, readable at reading distance.
- **Text Secondary** (`#999999`): Secondary paragraph text, descriptions, ancillary info.
- **Text Tertiary** (`#666666`): Metadata, copyright lines, fine print.
- **Border Subtle** (`rgba(255, 255, 255, 0.08)`): Card edges, divider hairlines on dark surfaces.

### Surface Variants
- **Surface Elevated** (`#222222` approx): Feature cards, testimonial blocks on `#1a1a1a` base — a single step of elevation.
- **Surface Glow** (`#cdd4f8` at 8-12% alpha): Ambient glow behind the hero phone mockup and any product-showcase moment.

### Button Gradient
The Ivory CTA gradient is the single most important color pairing in the system:
- **Gradient Top** (`#c9a6ff`): Lighter purple — catches the simulated overhead light.
- **Gradient Bottom** (`#a07ff0`): Slightly darker purple — the "shadow" side of the pill.
- **Inset Highlight** (`rgba(255, 255, 255, 0.25)`): The 1px white line at the top of every button, simulating a rounded glass edge.
- **Drop Shadow** (`rgba(186, 148, 255, 0.35)`): Purple-tinted glow pooling below — the pill is "lit from above."

## 3. Typography Rules

Tapbots uses the Apple system font stack exclusively. There are no custom webfonts, no variable fonts, no Google Fonts. The stack is `-apple-system, "helvetica-neue", helvetica, arial` — which resolves to **SF Pro Display** on modern Apple devices and degrades gracefully elsewhere. This is a deliberate identity choice: Tapbots ships native iOS and macOS apps, and their marketing site wants to *feel* like it was rendered by UIKit. Every typographic decision reinforces that native-native identity.

### Font Family
- **Primary**: `-apple-system`, fallbacks: `helvetica-neue, helvetica, arial, sans-serif`
- **No web fonts**: deliberate — the site wants to render in SF Pro (Apple) or Roboto (Android) or Segoe (Windows) at zero latency.
- **No OpenType features**: no `ss01`, no `liga`, no `tnum` — SF Pro's default optical sizing handles the work.

### Hierarchy

| Role | Size | Weight | Line Height | Notes |
|------|------|--------|-------------|-------|
| Display Hero | 36px (2.25rem) | 300 | 1.20 | Top of hero, Ivory product name moment — whisper-weight for luxury |
| Heading Bold | 32px (2.00rem) | 600 | 1.10 | Feature section headings — commanding but native-iOS-tuned |
| Heading Regular | 28px (1.75rem) | 600 | 1.10 | Sub-section headings |
| Sub-heading Light | 24px (1.50rem) | 300 | 1.40 | Airy sub-headings, quote moments |
| Sub-heading Bold | 24px (1.50rem) | 600 | 1.10 | Card titles with emphasis |
| Body Large | 24px (1.50rem) | 400 | 1.40 | Feature descriptions |
| Feature Heading | 21px (1.31rem) | 600 | 1.29 | In-card titles, footer column headers |
| Body | 20px (1.25rem) | 400 | 1.70 | Primary reading text — relaxed 1.7 leading |
| Body Light | 21px (1.31rem) | 300 | 1.40 | Lighter-weight body for spacious passages |
| Nav / Footer Link | 20px (1.25rem) | 600 | 1.70 | Footer section links — readable at arm's length |
| Fine Print | 18px (1.13rem) | 300-400 | 1.40-1.50 | Caption, secondary info |
| Uppercase Label | 16px (1.00rem) | 400 | 1.80 | All-caps metadata ("SYSTEM REQUIREMENTS", "©2008-2026 TAPBOTS, LLC.") |

### Principles
- **Native optical sizing**: SF Pro Display automatically swaps to SF Pro Text below 19px — no manual switching needed because the stack is just `-apple-system`. Trust the system.
- **Light 300 for "atmosphere" headings, bold 600 for "product" headings**: whisper-light is reserved for tagline and hero moments; 600 anchors the product name "Ivory" and feature titles.
- **Relaxed body leading (1.70-1.80)**: body copy at 20px with line-height 1.70 is unusually airy for a dark-mode site, creating a reading comfort that stands out against the density.
- **No negative letter-spacing**: Ivory trusts SF Pro's native metrics. This is *the* sign of a native-respecting designer — you don't need to fight SF Pro with `letter-spacing: -0.5px`.
- **Uppercase metadata at 16px with 1.8 line-height**: the "SYSTEM REQUIREMENTS" and copyright treatments echo iOS Settings screen labels — a tiny, tactile detail.

## 4. Component Stylings

### Buttons — THE Signature Component

Ivory's CTA button is the single most-studied thing on the page. It's a masterwork of dimensional stacking. Read this recipe like a pastry formula:

**Primary CTA (Purple Gradient Pill) — "Need Help with Ivory?", "Download on the App Store"**
- **Shape**: Pill / capsule — border-radius: 40px
- **Padding**: 12px 20px (inset for the pill-hug)
- **Background**: linear-gradient(180deg, `#c9a6ff` 0%, `#a07ff0` 100%) — lighter at top, denser at bottom, simulating a light source overhead
- **Border**: 1px solid `rgba(255,255,255,0.15)` — a hairline rim catching the virtual edge light
- **Inset highlight** (top edge glow): `box-shadow: inset 0 1px 0 rgba(255,255,255,0.25)` — a 1px white stripe along the top inside edge, simulating beveled glass
- **Drop shadow** (elevation): `box-shadow: 0 2px 4px rgba(0,0,0,0.2), 0 8px 16px rgba(186,148,255,0.25)` — dual shadow: a crisp near-shadow for contact and a wide purple-tinted halo for ambient glow
- **Full box-shadow stack** (combined):
  ```
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.25),
    0 1px 2px rgba(0,0,0,0.15),
    0 4px 10px rgba(186,148,255,0.25);
  ```
- **Text**: 16px weight 600, color `#ffffff`, letter-spacing 0, with a tiny icon left (12px chat bubble or Mastodon bird)
- **Hover**: gradient shifts `#d4b5ff` → `#a984ff`, outer shadow intensifies, inset highlight brightens to `rgba(255,255,255,0.35)`
- **Active (pressed)**: `transform: translateY(1px)`, inner shadow inverts — ON pressing, the button sinks 1px and shows an inset dark shadow (the "pressed-in" state)
- **Use**: All primary marketing CTAs

**App Store Badge (Apple-provided)**
- Apple's standard black "Download on the App Store" badge — not reskinned, used as-is per App Store guidelines
- Tapbots always pairs it with a contextual icon of the app they're promoting (Ivory's mascot bird sits to the left)

**Footer Text Link — "Mastodon", "Contact Us"**
- Background: transparent
- Text: `color(display-p3 1 0.302 0.302)` (Tapbots red), weight 400
- Hover: text color transitions to pure white `#ffffff`
- No underline at rest, no underline on hover — color shift does the work
- Small iconify-style icon preceding text ("@" for Mastodon, envelope for Contact)

**Tertiary Ghost Link — inline text "Paul, Mark & Todd"**
- Text only, inline
- Color: `color(display-p3 1 0.302 0.302)` (red)
- Hover: `#ffffff`
- No box, no border — just a color-shift on the characters themselves. Tapbots' signature for "people" links.

### Cards & Containers
- Background: `#1a1a1a` with a subtle `rgba(255,255,255,0.04)` inner tint for elevated surfaces
- Border: `1px solid rgba(255,255,255,0.08)` — hairline white at 8% alpha
- Border-radius: 18px (smaller feature cards), 40px (hero CTAs and capsule chips)
- Padding: generous — 30px-48px interior
- Shadow: soft ambient `0 8px 24px rgba(0,0,0,0.3)` on floating cards; nothing on flat sections
- Hover: subtle border brighten `rgba(255,255,255,0.12)`, no lift

### Inputs (Form fields — adapted Tapbots style)
- Background: `#1a1a1a` matching the surface
- Border: `1px solid rgba(255,255,255,0.1)`
- Border-radius: 10px
- Padding: 12px 16px
- Focus: border shifts to `#ba94ff` with `0 0 0 3px rgba(186,148,255,0.18)` ring
- Placeholder: `#666666`

### Navigation / Footer
- Footer columns: each app family (Ivory, Tweetbot, Pastebot, Calcbot) gets a column with a weight-600 title and weight-400 children
- Column title: 21px weight 600 `#ffffff`
- Column link: 20px weight 400 `#c3c3c3`, hover to `#ffffff`
- Bottom bar: uppercase 16px "©2008-2026 TAPBOTS, LLC. ALL RIGHTS RESERVED." centered — the only uppercase text on the page

### Distinctive Components

**Mascot Bird (Tapbots logomark)**
- SVG silhouette of a stylized songbird — round body, twin "antennae" on the head (a nod to the original Tapbots robot/bot logo)
- Stroke color: `color(display-p3 1 0.302 0.302)` (display-P3 red) — on wide-gamut screens, this red is brighter than sRGB allows
- Size: ~40px in the footer, larger in app icon contexts
- Treatment: outline-only (no fill), 2px stroke weight — rendered like a minimalist tattoo

**Product Hero Mockup**
- Real iOS screenshot of Ivory embedded inside a realistic iPhone bezel (no generic "floating phone" template)
- Purple periwinkle radial glow (`#cdd4f8` at 10-18% alpha) centered behind the phone — ambient light source
- No fake highlights, no isometric rotation — shot flat and centered

## 5. Layout Principles

### Spacing System
- Base unit: 8px (extrapolated from the 8px/16px/24px/32px/48px rhythm in the extracted scale)
- Observed scale values (px): 4, 10, 12, 16.8, 20, 25.2, 27, 28.8, 29.4, 30, 32, 33.6, 40, 48, 60, 80
- Notable: Ivory uses *odd* pixel values (16.8, 25.2, 28.8, 33.6) — these are `1rem × 1.05`, `1rem × 1.575`, `1rem × 1.8`, `1rem × 2.1`. Type-driven spacing scaled from the font system, not a strict 8px grid.

### Grid & Container
- Max content width: ~960px for text-heavy sections, up to 1612px on the hero (very wide but centered)
- Responsive breakpoints: 414px (iPhone), 500px (small tablet), 700px (large tablet)
- Footer columns: 4-column grid on desktop (Ivory / Tweetbot / Pastebot / Calcbot), collapsing to stacked 1-column on mobile

### Whitespace Philosophy
- **Breathing room around the product**: the hero iPhone mockup has 80px+ of dark space on all sides — the product is the subject
- **Section separation via dark voids**: there are no background color swaps between sections; instead, 60-80px of vertical padding separates content blocks
- **Tight in-column density**: inside a footer column, link rows are stacked 8-12px apart — the columns themselves are dense, the spaces between them are vast

### Border Radius Scale
- Subtle (10px): input fields, small tags
- Medium (18px): feature cards, product hero containers
- Pill (40px): CTA buttons, capsule highlights — the signature Ivory shape
- Badge/circular: 50% for avatar circles and icon chips

## 6. Depth & Elevation — THE DIMENSIONAL BUTTON STACK

This section is the core of Tapbots' craft legacy. Every button on the Ivory site is built from a multi-layer shadow and gradient stack that simulates a physical, light-lit object. Below is the exact recipe, annotated.

### The Five-Layer Button Recipe

Every primary CTA assembles **five distinct visual layers**, rendered in this order (bottom to top in the CSS paint order):

| Layer | CSS | Purpose |
|-------|-----|---------|
| 1. Ambient glow | `0 8px 24px rgba(186,148,255,0.25)` drop shadow | Wide, soft purple halo — the object "lights up" its surroundings |
| 2. Contact shadow | `0 1px 2px rgba(0,0,0,0.2)` drop shadow | Sharp, tight shadow directly below — anchors the object to the surface |
| 3. Gradient fill | `linear-gradient(180deg, #c9a6ff, #a07ff0)` background | The "body" of the button — lighter at top, denser at bottom |
| 4. Rim light | `1px solid rgba(255,255,255,0.15)` border | Hairline rim catching the virtual edge light |
| 5. Inset highlight | `inset 0 1px 0 rgba(255,255,255,0.25)` box-shadow | The 1px white line along the top inside edge — the signature "beveled glass" effect |

### Full CSS Implementation

```css
.btn-ivory {
  /* Shape */
  border-radius: 40px;
  padding: 12px 20px;

  /* Layer 3: Gradient fill */
  background: linear-gradient(180deg, #c9a6ff 0%, #a07ff0 100%);

  /* Layer 4: Rim light */
  border: 1px solid rgba(255, 255, 255, 0.15);

  /* Layers 1, 2, 5: The dimensional shadow stack */
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.25),  /* Inset highlight (top) */
    0 1px 2px rgba(0, 0, 0, 0.2),              /* Contact shadow */
    0 8px 24px rgba(186, 148, 255, 0.25);     /* Ambient glow */

  /* Typography */
  color: #ffffff;
  font: 600 16px -apple-system;

  /* Interaction */
  transition: transform 0.08s ease-out, box-shadow 0.15s ease;
}

.btn-ivory:hover {
  background: linear-gradient(180deg, #d4b5ff 0%, #a984ff 100%);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.35),
    0 2px 4px rgba(0, 0, 0, 0.25),
    0 12px 32px rgba(186, 148, 255, 0.35);
}

.btn-ivory:active {
  transform: translateY(1px);
  box-shadow:
    inset 0 2px 4px rgba(0, 0, 0, 0.2),  /* Pressed-in inset */
    0 0 0 rgba(0, 0, 0, 0);
}
```

### Elevation Table

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (L0) | No shadow, flat surface | Body copy backgrounds, text sections |
| Card Elevation (L1) | `0 4px 12px rgba(0,0,0,0.2)`, border 1px white 8% alpha | Feature cards, product preview tiles |
| CTA (L2) | Full five-layer stack (above) | All primary buttons |
| Hero (L3) | `0 24px 60px rgba(0,0,0,0.4)` + purple ambient glow behind | Hero iPhone mockup |
| Pressed (L-1) | `inset 0 2px 4px rgba(0,0,0,0.2)`, no drop | Active button state — the "sunken" look |

### Shadow Philosophy

Tapbots shadows are never neutral. Every drop shadow has a **tint** that matches the element's color:
- Purple buttons cast purple-tinted halos (`rgba(186,148,255,0.25)`)
- The bird mascot can cast a red-tinted halo (`rgba(255,77,77,0.2)`) in hover states
- Dark cards cast warm-black shadows (`rgba(0,0,0,0.3)`) — never `rgba(0,0,0,1)`

This is the inheritance from 15 years of iOS dimensional buttons: the world is lit, and light passes through the object's color on its way to the surface below.

## 7. Do's and Don'ts — Tactility is the North Star

### Do
- Build every CTA from the full five-layer stack — gradient + border + inset highlight + contact shadow + ambient glow. Anything less is an impostor button.
- Use purple-tinted shadows on purple buttons, red-tinted shadows on red elements. Shadows should *inherit* the element's hue.
- Use off-black `#1a1a1a` backgrounds — never pure `#000`. Warmth is the inheritance.
- Use SF Pro Display (via `-apple-system`) — never substitute Inter or Helvetica. The site's native-iOS feel depends on it.
- Embed real iOS screenshots of Ivory, not mockups or illustrations. If you can't ship a real screenshot, ship no screenshot.
- Keep the mascot bird visible but quiet — footer-sized, outline-only, Tapbots red. Never animate, never enlarge.
- Respect `color(display-p3 ...)` — on wide-gamut displays, the Tapbots red is P3-specific. Use the display-P3 syntax in CSS.
- Use 40px pill radius for CTAs and 18px rounded-square for cards. Two radii, clear roles.
- Use weight 300 for whisper headings, weight 600 for product names. Never use weight 400 for a hero.
- Animate pressed buttons with `translateY(1px)` and inset-dark shadow — simulate the button being pushed *into* the surface.

### Don't
- Don't use flat buttons. A flat button on an Ivory page reads as a broken element.
- Don't use neutral gray drop shadows. Tint shadows to match the element's hue — this is the signature Tapbots craft move.
- Don't use pure `#000` anywhere. The dark is warm.
- Don't add a webfont. `-apple-system` is the entire typographic decision.
- Don't use rounded-square buttons (4-8px radius). CTAs are pills. Cards are soft-squares.
- Don't put the mascot bird in the hero. It's a footer-only signature — treating it like a logo breaks the quietness.
- Don't use generic lucide/heroicons for product UI. Icons should feel custom, weighted, dimensional. Solar Bold, Phosphor Fill, or SF Symbols.
- Don't animate with long durations. Tapbots interactions are snappy — 80-150ms ease-out, never longer.
- Don't use Material ripples or ink splashes. The pressed state is a 1px sink with inset-dark shadow. Anything else feels Android.
- Don't letter-space SF Pro. SF Pro's native tracking is the work. Leave it alone.

## 8. Responsive Behavior

### Breakpoints (extracted)
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <414px | Single-column footer, hero stacks, CTAs full-width |
| Mobile Large | 414-500px | iPhone-comfortable, footer stacks 2x2 |
| Tablet | 500-700px | Footer transitions to 4-column, hero side-by-side |
| Desktop | >700px | Full 4-column footer, max-width 960px content |

### Touch Targets
- Primary CTAs: 44px minimum height (native iOS touch target guideline) — achieved via 12px vertical padding on 16px text
- Footer links: 20px type with 1.70 line-height creates ~34px row — just shy of 44px, but adequate for pointer targeting on desktop
- The mascot bird in the footer is non-interactive (no hover state) — just a brand signature

### Collapsing Strategy
- Hero: iPhone mockup scales down and stacks above copy on mobile; desktop shows copy-left, phone-right
- Footer: 4 equal columns on ≥700px, 2x2 grid on tablet, single-column stack on mobile
- CTA buttons: width fills container on mobile, auto-width on desktop
- Type scale: 36px hero → 28px on mobile; 32px heading → 24px on mobile
- Button dimensionality is preserved at all sizes — the shadow stack never flattens on mobile

## 9. Agent Prompt Guide

### Quick Color Reference
- Page background: `#1a1a1a` (warm off-black — never `#000`)
- Text primary: `#ffffff` (body on dark)
- Text secondary: `#c3c3c3`
- Text tertiary: `#999999`
- Text metadata: `#666666`
- Ivory Purple: `#ba94ff` (gradient start), `#deccff` (gradient light end)
- Button gradient: `linear-gradient(180deg, #c9a6ff 0%, #a07ff0 100%)`
- Tapbots Red: `color(display-p3 1 0.302 0.302)` or fallback `#FF4D4D`
- Ambient glow: `rgba(186, 148, 255, 0.25)` for purple, `rgba(255, 77, 77, 0.2)` for red
- Surface borders: `rgba(255, 255, 255, 0.08)`

### The Button Recipe (copy-paste ready)

```css
.btn-primary {
  border-radius: 40px;
  padding: 12px 20px;
  background: linear-gradient(180deg, #c9a6ff 0%, #a07ff0 100%);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #ffffff;
  font: 600 16px -apple-system, helvetica-neue, helvetica, arial;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.25),
    0 1px 2px rgba(0, 0, 0, 0.2),
    0 8px 24px rgba(186, 148, 255, 0.25);
  transition: all 0.12s ease-out;
}
```

### Example Component Prompts
- "Build an Ivory CTA button: pill shape 40px radius, 12px×20px padding, purple gradient (#c9a6ff top → #a07ff0 bottom), inset white highlight on top edge (inset 0 1px 0 rgba(255,255,255,0.25)), contact shadow (0 1px 2px rgba(0,0,0,0.2)), purple ambient halo (0 8px 24px rgba(186,148,255,0.25)), 1px rgba(255,255,255,0.15) border, white text 16px weight 600 SF Pro."
- "Design an Ivory product hero: full-bleed #1a1a1a background, radial purple glow (#cdd4f8 at 12% alpha) centered behind a real iOS screenshot framed in an iPhone bezel. Headline 36px SF Pro Display weight 300 white, tagline below at 20px weight 400 #c3c3c3. Two CTAs: App Store badge left, Ivory Purple gradient pill right."
- "Build the Tapbots footer: four columns (Ivory / Tweetbot / Pastebot / Calcbot), each with a 21px weight 600 title in white and 20px weight 400 links in #c3c3c3 (hover → #ffffff). Centered Tapbots red mascot bird (outline only, 40px) above the intro copy. Bottom row centered uppercase 16px '©2008-2026 TAPBOTS, LLC. ALL RIGHTS RESERVED.'"
- "Create a feature card: #1a1a1a background with rgba(255,255,255,0.04) inner tint, 1px rgba(255,255,255,0.08) border, 18px radius, 30px padding. Heading 24px weight 600 white, body 20px weight 400 #c3c3c3 line-height 1.70. Hover: border brightens to 0.12 alpha, no lift."

### Iteration Guide

1. **Every button gets the five-layer stack.** No exceptions. A flat button fails the "Tapbots test."
2. **Shadows inherit hue.** Purple things cast purple shadows. Red things cast red halos. Never use `rgba(0,0,0,0.x)` as a universal shadow — tint it.
3. **Use `-apple-system` only.** Don't substitute Inter, Helvetica, or a Google Font. The native-iOS feel is non-negotiable.
4. **Off-black, not pure black.** `#1a1a1a` is the only correct page background. `#000` is forbidden.
5. **Pill 40px for CTAs, rounded 18px for cards, 10px for inputs.** Three radii, clear roles.
6. **Icons should have weight.** Use Solar Bold, Phosphor Fill, or SF Symbols — not lucide or heroicons (too linear).
7. **Whisper-light 300 for atmosphere, bold 600 for products.** Never weight 400 for a hero.
8. **Embed real iOS screenshots.** No mockups, no illustrations, no 3D-rendered phones.
9. **The mascot bird belongs in the footer.** Outline-only, Tapbots red, small. Never in the hero, never animated.
10. **Pressed state: `translateY(1px)` + inset dark shadow.** The button sinks into the surface. Simulate physicality.
