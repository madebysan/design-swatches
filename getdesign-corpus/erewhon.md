# Design System Inspired by Erewhon

## 1. Visual Theme & Atmosphere

Erewhon's website is the digital equivalent of walking into one of their Los Angeles stores: pared-back, almost monastic, but with every surface, edge, and shadow tuned for quiet luxury. The page sits on a stack of soft neutrals — a cream canvas (`#f4eee4`) under cards, a warm off-white (`#faf7f2`) for product surfaces, and a near-black (`#0d0d0d`) header that runs edge-to-edge like a gallery banner. The wordmark sets the tone: a refined, generously-tracked sans-serif rendered at modest size and centered in the nav, refusing the size-and-shout posture of typical e-commerce. There is no accent color, no hero illustration, no badge confetti. The single chromatic note is a small "Sold Out" sticker in muted ink — and even that reads as editorial caption rather than promotional shout.

What makes Erewhon's interface feel premium is **photographic restraint**, not graphic flourish. Every product card uses the same warm cream backdrop (`#f4eee4`) and the same daylight-soft tonal photography — shadows fall but never cut, highlights bloom but never blow out. A bag of granola, a $20 smoothie, a $9 spring water sushi roll — all photographed with the same calm, ambient lighting that flattens product hierarchy and turns inventory into still-life. There are no lifestyle stagings, no gradient overlays, no sale ribbons. The grid is the gallery. This is the aesthetic mechanism that lets Erewhon charge $20 for a smoothie: visual silence as price justification.

The third defining trait is **graphic minimalism through omission**. Cards have no borders. Buttons have no shadows. Sections have no dividers. The system relies almost entirely on negative space and tonal shifts (`#faf7f2` against `#f4eee4` against `#ffffff`) to articulate structure — differences of two or three percentage points in luminance, doing the work that borders and shadows do on lesser sites. Only the dark header (`#0d0d0d`) breaks the cream tonality, and it does so with conviction: a single hard band of near-black that frames the entire experience like a museum plinth.

**Key Characteristics:**
- Cream-on-cream tonal palette — `#faf7f2` page, `#f4eee4` cards, `#ffffff` surface accents
- Near-black header band (`#0d0d0d`) — the only chromatic anchor, edge-to-edge gallery banner
- Refined geometric sans wordmark, generously tracked (`0.16em+`), centered with restraint
- Soft daylight product photography on uniform cream backdrops — every product, same light
- Sharp 0–2px radii throughout — borders are the exception, tonal shifts do structural work
- No accent color, no gradients, no decorative shadows — silence as luxury signal
- Editorial product cards — image dominant, label small, price smaller, no chrome
- Single muted "ink" sticker (`#a23a3a`) for status states ("Sold Out") — caption tone, not alert tone

## 2. Color Palette & Roles

### Primary
- **Erewhon Cream** (`#f4eee4`): Card and tile backgrounds — the warm beige that defines product surfaces. The single most-seen color on the site.
- **Erewhon Paper** (`#faf7f2`): Page canvas — a half-step lighter than cream, used for the body and footer. Visible only as the negative space between cards.
- **Pure White** (`#ffffff`): Reserved for cookie modals, dropdown panels, and elevated content surfaces. Never the page background.
- **Erewhon Ink** (`#0d0d0d`): Top navigation bar, primary text, button fills. A near-black, slightly warmed, never pure `#000`.

### Brand Accent
- Erewhon is **deliberately accent-free**. There is no signature brand color in the UI. The only chromatic moment is the muted `#a23a3a` "Sold Out" sticker on product cards — and even that reads as printed-tag, not interactive accent.
- **Sold Out Ink** (`#a23a3a`): Faded brick red on cream — used exclusively for inventory status stickers. Never a CTA color.

### Neutrals & Text
- **Ink** (`#0d0d0d`): Headers, body copy, product names, button labels — the only text color in the system.
- **Soft Ink** (`#3a3a3a`): Secondary text — product descriptions, footer link labels, fine print.
- **Mute Ink** (`rgba(13, 13, 13, 0.55)`): Disabled states, captions, "Add to bag" hover dimming.
- **Hairline Gray** (`#e8e2d6`): The barely-there border tone used on the rare bordered surface (newsletter input, dropdown chrome). Sits one shade darker than cream.

### Surface & Borders
- **Card Cream** (`#f4eee4`): Default product card background — the workhorse surface.
- **Footer Paper** (`#faf7f2`): Footer background — matches page canvas, no visible boundary.
- **Header Ink** (`#0d0d0d`): Top nav bar — the single dark band in the system, full-width.
- **Border Hairline** (`1px solid #e8e2d6`): Reserved for inputs and the cookie-banner action buttons.

### Photographic Tonality
- **Product Backdrop Cream** (`#f4eee4` → `#ece4d4`): Photo backgrounds harmonize with card surfaces — products appear to float on the page rather than sit in framed photos. The transition between photo and card is intentionally near-invisible.
- **Highlight Bloom** (`#fbf5e9`): The lightest cream tone, present in product photography highlights — never used in UI.

### Gradient System
- Erewhon is **gradient-free**. The system relies on flat tonal relationships between three creams and one near-black. Any apparent gradient on the page is photographic, not CSS.

## 3. Typography Rules

### Font Family
- **Wordmark / Display**: A refined geometric sans-serif with humanist proportions. Likely a custom cut or a commercial face such as `Söhne`, `Neue Haas Grotesk`, or `GT America`. Generously tracked at display sizes.
- **Body / UI**: A modern grotesk in the same family lineage, used at lighter weights for product names, prices, and captions. Falls back to `system-ui, -apple-system, "Helvetica Neue", Arial, sans-serif`.
- **Open Source Substitute**: For external implementations, `Inter` at weight 400/500 or `Söhne` (commercial) approximate the feel; `Söhne Schmal` works for the wordmark wide-track treatment.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Wordmark | Geometric Sans | 22–28px | 500 | 1.00 | 0.16em | All-caps logotype, centered in header |
| Section Heading | Geometric Sans | 32–40px | 500 | 1.10 | 0.04em | "CURATED BY EREWHON", section eyebrows |
| Eyebrow Label | Geometric Sans | 11–12px | 500 | 1.20 | 0.12em | "VIEW COLLECTION", uppercase chrome |
| Product Name | Modern Grotesk | 14px | 500 | 1.30 | 0.01em | Card titles — title case, restrained |
| Product Description | Modern Grotesk | 13px | 400 | 1.45 | normal | Subtitle line under product name |
| Price | Modern Grotesk | 13–14px | 500 | 1.30 | normal | Same scale as product name, tabular figures |
| Body | Modern Grotesk | 14–16px | 400 | 1.55 | normal | Cookie banner copy, footer text |
| Footer Heading | Geometric Sans | 13px | 500 | 1.30 | 0.10em | "Newsletter", "Main menu", "Contact" — uppercase |
| Footer Link | Modern Grotesk | 13px | 400 | 1.60 | normal | Title case footer navigation |
| Caption | Modern Grotesk | 11–12px | 400 | 1.40 | normal | Legal text, copyright, fine print |
| Status Sticker | Geometric Sans | 11px | 500 | 1.00 | 0.08em | "Sold Out" tag — uppercase, tight |

### Principles
- **Restraint over hierarchy**: Erewhon refuses dramatic size jumps. Section heads are 32–40px, product names are 14px — there is no 80px hero, no tabloid display. The site reads at one calm volume.
- **Tracked uppercase as ornament**: The few uppercase moments (wordmark, eyebrows, "VIEW COLLECTION") are heavily tracked (`0.10em–0.16em`). Tracking is the only typographic flourish — bold weights, italics, and serifs are absent.
- **Title case for content, uppercase for chrome**: Product names, descriptions, and prices are title or sentence case. Uppercase is reserved for navigational and structural elements only.
- **Weight 400/500 only**: No 700, no 800. The system runs on regular and medium — and the medium is reserved for wordmark, headings, prices, and section heads. Body copy is 400.
- **Tabular figures for prices**: Prices use lining/tabular figures so `$8.50` and `$20.00` align cleanly in the grid. Critical for the side-by-side product comparison effect.

## 4. Component Stylings

### Buttons

**Primary Ink Button**
- Background: Erewhon Ink (`#0d0d0d`)
- Text: Pure White (`#ffffff`)
- Padding: 14px 28px
- Radius: `2px` (effectively sharp)
- Border: `0`
- Shadow: none
- Font: 13px geometric sans, weight 500, letter-spacing `0.06em`, uppercase
- Hover: background shifts to `#1f1f1f`, no transform
- Use: Newsletter "Join", cookie "Accept", primary checkout flows

**Inverted Cream Button**
- Background: Pure White (`#ffffff`) or Cream (`#f4eee4`)
- Text: Erewhon Ink (`#0d0d0d`)
- Padding: 14px 28px
- Radius: `2px`
- Border: `1px solid #e8e2d6`
- Hover: border darkens to `#0d0d0d`, no fill change
- Use: Cookie "Manage preferences" / "Decline", secondary actions

**Eyebrow Link Button**
- Background: transparent
- Text: Erewhon Ink (`#0d0d0d`)
- Padding: 0 (inline)
- Font: 11–12px geometric sans, weight 500, uppercase, letter-spacing `0.12em`
- Treatment: underline appears on hover (`text-decoration-thickness: 1px`, offset 4px)
- Use: "VIEW COLLECTION", "About", inline navigational links

**Add to Bag (Card Hover)**
- Background: Erewhon Ink (`#0d0d0d`)
- Text: Pure White (`#ffffff`)
- Appears: on card hover, slides up from card bottom edge
- Padding: 12px 0 (full card width)
- Font: 12px, weight 500, uppercase, `0.08em` tracking

### Cards & Containers
- Background: Card Cream (`#f4eee4`)
- Border: `0` — cards never use borders
- Radius: `0px` for image area, `0px` for the surrounding tile — the system is uniformly sharp
- Shadow: none — cards rely on tonal contrast against the page (`#faf7f2`)
- Internal padding: 0 around photo, 12–16px below for label and price
- Aspect ratio: 1:1 square, enforced across all product cards regardless of source image
- Hover: subtle cream darkening (`#ece4d4`) on the card surface, optional slide-up "Add to bag" bar

### Badges / Tags / Stickers
**Sold Out Sticker**
- Background: Pure White (`#ffffff`)
- Text: Sold Out Ink (`#a23a3a`)
- Border: `0`
- Position: absolute, top: 12px, left: 12px (overlay on product image)
- Padding: 6px 10px
- Radius: `0px`
- Font: 11px geometric sans, weight 500, uppercase, `0.08em` tracking
- Treatment: feels like a printed paper tag, not a UI badge

**Inventory Pill** (rare)
- Background: transparent
- Text: Mute Ink (`rgba(13, 13, 13, 0.55)`)
- Border: `1px solid #e8e2d6`
- Radius: `9999px`
- Use: only for low-stock or pre-order indicators

### Inputs & Forms
- Background: Pure White (`#ffffff`) or transparent
- Border: `1px solid #e8e2d6` default, `1px solid #0d0d0d` on focus
- Radius: `2px`
- Font: 14px modern grotesk, weight 400
- Text color: `#0d0d0d`
- Placeholder: Mute Ink (`rgba(13, 13, 13, 0.55)`)
- Focus: border darkens to ink, no box-shadow ring
- Padding: 12px 14px
- Newsletter input: bottom-bordered only (`border-bottom: 1px solid #0d0d0d`), no top/side borders — editorial newsletter feel

### Navigation
- Top header: full-width band, background `#0d0d0d`, height ~48px desktop / ~52px mobile
- Logo: centered geometric-sans wordmark in white, 22–28px, `0.16em` tracking
- Left side: hamburger menu icon (white, 20×20px stroke icon)
- Right side: account icon, search icon, cart icon (all white, 20×20px)
- Hover: icon opacity shifts from `1.0` to `0.7`
- Sticky: header remains fixed on scroll, content slides beneath
- Sub-nav (when present): white background, ink text, `0.10em` tracked uppercase categories

### Decorative Elements

**Ink Header Band**
- The single most distinctive UI element: a continuous `#0d0d0d` bar across the top of every page
- No logo color shift, no transparency, no scroll behavior beyond fixed-position
- Functions as a frame for the cream content below — the gallery plinth

**Tonal Card Grid**
- 4-column desktop, 2-column tablet, 1.5-column mobile (peek-scroll)
- 16–24px gutters, no row dividers
- Cards are tonally near-identical — variation comes from photography, not from chrome

**Cookie / Modal Overlay**
- Background: Pure White (`#ffffff`), no scrim behind (or a 20% black scrim at most)
- Border: `0`
- Shadow: very soft `0 8px 24px rgba(0, 0, 0, 0.06)` — the only blurred shadow in the system
- Padding: 24–32px
- Buttons inside follow the inverted-cream pattern

## 5. Layout Principles

### Spacing System
- Base unit: 4px
- Scale: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px
- Card grid gutter: 16–24px desktop, 12px mobile
- Section vertical rhythm: 64–96px between major content blocks
- Generous use of 96px+ to separate hero, grid, and footer — the page breathes

### Grid & Container
- Max content width: ~1440px on desktop, with 32–48px side padding
- Product grid: 4 columns desktop, 2 columns tablet, 1.5 columns mobile (horizontal scroll snap)
- Hero / featured imagery: full-width, no container constraint
- Footer: 4-column desktop layout (Brand / Newsletter / Main menu / Contact), stacks to single column under 768px
- Content alignment: left-aligned by default; centered only for the wordmark and primary CTAs in modals

### Whitespace Philosophy
- **Air as luxury signal**: Every section has 64–128px of vertical breathing room. The page never feels packed.
- **Tonal pacing instead of dividers**: Sections separate via shifts between `#faf7f2` and `#f4eee4` — no horizontal rules, no separators
- **Photo-first composition**: Imagery occupies 60–70% of any given fold. Type and chrome wrap around photographs, never compete with them.
- **Empty cells are intentional**: When the grid has fewer products than columns, the grid does not collapse — empty space remains, preserving the rhythm

### Border Radius Scale
- Sharp (0px): Default for all cards, image containers, header band, status stickers
- Near-sharp (2px): Buttons, inputs — a one-pixel concession to softness
- Pill (9999px): Reserved for inventory pills, dropdown chevrons, and rare badge moments
- No mid-range radii: 4px, 8px, 12px do not exist in the system

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Cards, buttons, inputs, header band — the system default |
| Tonal Lift (Level 1) | `#faf7f2` page → `#f4eee4` card — implied depth via tone | Product cards, content tiles |
| Hairline Frame (Level 2) | `1px solid #e8e2d6` | Inputs, secondary buttons, dropdown chrome |
| Soft Modal (Level 3) | `0 8px 24px rgba(0, 0, 0, 0.06)` | Cookie banner, search dropdown, account modal — the only blurred shadow |
| Ink Band (Level 4) | Solid `#0d0d0d` against cream — chromatic depth | Top header, primary CTA fills |

**Shadow Philosophy**: Erewhon almost entirely refuses elevation. The system reads as flat printed material — like a hand-set catalogue rather than a dimensional UI. Where most e-commerce sites use card shadows to indicate clickability, Erewhon uses tonal shift: the half-step between `#faf7f2` (page) and `#f4eee4` (card) is enough. Only floating modal surfaces (cookie banner, search overlay) earn a softly diffused shadow, and even then it's barely perceptible (`6%` opacity, `24px` blur). The visual logic is: if you have to add a shadow, you've already failed at composition.

### Decorative Depth
- Photographic shadows do the work UI shadows would do — every product is photographed with daylight-soft floor shadows that anchor it without graphic intervention
- The dark header band (`#0d0d0d`) creates implicit depth by chromatic contrast — the cream below feels lifted relative to the ink above
- Hover states avoid translation/scale — interactive feedback is tonal (slight darken) rather than dimensional (lift)

## 7. Do's and Don'ts

### Do
- Use cream-on-cream tonality (`#faf7f2` page, `#f4eee4` cards) for tonal depth without borders
- Anchor every page with the `#0d0d0d` ink header — the single chromatic frame
- Track uppercase moments at `0.10em–0.16em` — heavy tracking is the typographic signature
- Use weight 500 for headings/wordmark, weight 400 for body — never 700+
- Photograph products on uniform cream backdrops with soft daylight — consistency is the luxury signal
- Use `0px` or `2px` radius universally — the system is sharp
- Reserve `9999px` pill radius only for genuinely small/circular elements
- Let tonal shifts and whitespace articulate structure — borders are an exception
- Keep section vertical rhythm at 64–128px — generous air is non-negotiable

### Don't
- Don't introduce accent colors — Erewhon has no brand color in the UI, only photographic tones
- Don't use bold weights (700, 800) — the system tops out at 500
- Don't use blurred drop shadows on cards or buttons — flat is the default
- Don't pure-white the page background — always `#faf7f2` or `#f4eee4`
- Don't use serif type — the system is grotesk-only despite the luxury positioning
- Don't enlarge headlines past 40px — restraint is the volume
- Don't add gradients, glows, or overlays — chromatic flatness is the rule
- Don't use sale ribbons, pricing slashes, or promotional badges — the only sticker is "Sold Out"
- Don't tighten letter-spacing on body type — Erewhon stays at normal tracking below 14px
- Don't introduce dividers or hairline rules — let tonal shifts separate sections

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single column, cards 1.5 visible (peek-scroll horizontal), 32px hero type |
| Mobile | 375–768px | 2-column product grid, 32px section heads, hamburger menu |
| Tablet | 768–1024px | 3-column grid, section heads scale to 36px |
| Desktop | 1024–1440px | 4-column grid, full nav visible, max content width |
| Large Desktop | ≥1440px | 4-column grid persists, max width caps at ~1440px, side padding grows |

### Touch Targets
- Header icons: 44×44px tap area (icon itself 20×20px)
- Cards: full card is tappable, 1:1 aspect preserved
- "Add to bag" hover bar becomes a persistent footer-bar on touch devices
- Newsletter input: 48px tap height

### Collapsing Strategy
- **Header**: All icons remain visible on mobile (hamburger / wordmark / account / cart). The nav band height drops slightly (52px → 48px desktop)
- **Product grid**: 4 → 3 → 2 → 1.5 columns. The 1.5-column mobile layout uses scroll-snap to suggest more inventory beyond the fold
- **Section headings**: 40px → 32px → 28px progressively, tracking maintained
- **Footer**: 4-column to single-column stack under 768px, with section headings retained
- **Modals**: Cookie banner becomes a bottom-anchored sheet on mobile (full-width, 16px padding, slide-up)
- **Type scale**: Body stays at 14–16px regardless of breakpoint — the system does not scale body type

### Image Behavior
- Product images maintain 1:1 aspect ratio at all breakpoints
- Hero / lifestyle imagery shifts from full-bleed desktop to edge-to-edge mobile (no margin)
- No art-direction swap between breakpoints — the same crop scales
- Photographic tonality and lighting remain consistent across viewports

## 9. Agent Prompt Guide

### Quick Color Reference
- Page Canvas: Erewhon Paper (`#faf7f2`)
- Card Surface: Erewhon Cream (`#f4eee4`)
- Header / Primary CTA: Erewhon Ink (`#0d0d0d`)
- Body Text: Erewhon Ink (`#0d0d0d`)
- Secondary Text: Soft Ink (`#3a3a3a`)
- Muted Text: Mute Ink (`rgba(13, 13, 13, 0.55)`)
- Hairline Border: Hairline Gray (`#e8e2d6`)
- Sold Out Sticker: Sold Out Ink (`#a23a3a`) on white
- Modal Surface: Pure White (`#ffffff`)

### Example Component Prompts
- "Create a product card on Erewhon Cream (`#f4eee4`) with `0px` radius, no border, no shadow. Square 1:1 image area filling card width. Below: product name in 14px modern grotesk weight 500 (`#0d0d0d`), then price in 13px weight 500. Padding 12px below image. On hover, slide a `#0d0d0d` 'ADD TO BAG' bar (12px uppercase, weight 500, `0.08em` tracking, white text) up from the bottom edge."
- "Design a top navigation header — full-width `#0d0d0d` band, 48px tall on desktop. Center a geometric sans wordmark 'EREWHON' at 24px weight 500, white, with `0.16em` letter-spacing, uppercase. Place 20×20px white icons (hamburger left; account, search, cart right) with 44px tap targets and hover opacity 0.7."
- "Build a 4-column product grid on Erewhon Paper (`#faf7f2`) with 24px gutters and 96px vertical breathing room above and below. No dividers, no row separators — let the page tone show through. Product cards in `#f4eee4`. On scroll, the `#0d0d0d` header stays sticky."
- "Create a 'Sold Out' sticker — white background, `#a23a3a` text, 11px geometric sans weight 500, uppercase, `0.08em` tracking. Padding 6px 10px, `0px` radius, no border. Position absolute, 12px from the top-left of the product image."
- "Design a newsletter input — no top/side borders, `1px solid #0d0d0d` on the bottom only. Inside: 14px modern grotesk weight 400, placeholder in `rgba(13, 13, 13, 0.55)`. To the right, a 'JOIN' button — `#0d0d0d` background, white text, 13px weight 500 uppercase, `0.06em` tracking, padding 14px 28px, `2px` radius."
- "Style a section heading — 'CURATED BY EREWHON' in 36px geometric sans weight 500, color `#0d0d0d`, line-height 1.10, letter-spacing `0.04em`, uppercase. Pair with a small 'VIEW COLLECTION' link to its right — 12px weight 500 uppercase, `0.12em` tracking, underline on hover only."

### Iteration Guide
1. Default to cream-on-cream tonality — `#faf7f2` for page, `#f4eee4` for cards. Tonal shift replaces borders.
2. Anchor every layout with the `#0d0d0d` ink header band — it is the system's only chromatic frame.
3. Keep weight 400/500 only — never 700+. Restraint is the brand voice.
4. Use `0px` or `2px` radius universally. Pill radius only for genuinely circular UI.
5. Track uppercase at `0.10em–0.16em` — heavy tracking is the typographic ornament.
6. Photographic consistency is the luxury signal — every product on the same cream backdrop, same daylight tonality.
7. Refuse drop shadows on cards and buttons. Reserve a soft `0 8px 24px rgba(0,0,0,0.06)` only for floating modals.
8. Generous vertical rhythm (64–128px between sections) is non-negotiable — the page must breathe.
9. No accent color, no gradients, no badges except the muted "Sold Out" sticker — silence is the signature.
10. Body type stays at 14–16px regardless of viewport. The system does not scale body copy.
