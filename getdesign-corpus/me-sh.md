# Design System Inspired by Mesh

## 1. Visual Theme & Atmosphere

Mesh's website is cinematic dark-mode editorial in service of a deeply human topic: tending personal relationships at scale. The page sits on near-black canvas (`#0f0f10`) with an off-white body color (`rgba(255, 255, 255, 0.7)`) that softens the contrast just enough to read like prestige editorial rather than tech UI. A signature peach accent (`#f2b98b`) functions as starlight — applied to primary CTA labels, key links, and the orbital glow lines that thread through the hero. The whole composition reads less like a SaaS landing page and more like the title card of a science documentary about the cosmos of someone's contact book.

The defining element is **Hoefler typography paired with literal cosmic atmosphere**. Display headlines run in `Verlag` and `VerlagCondensed` at weight 700–900 — bold, condensed, all-caps when needed, with a `0.66–0.88px` of positive tracking that's unusual for display type. Body and pull copy quietly switch to `ChronicleTextG1Roman` at 22px/1.55 line-height for the editorial moments — a literary serif that signals craft and patience. The website doesn't hedge: it commits to the H&Co stack across every level. Where every other relationship-CRM uses Inter or a generic geometric sans, Mesh uses the same typeface family The New Yorker uses for ads. That choice IS the brand.

What distinguishes Mesh most is its **light system**. Buttons and cards don't sit on the canvas — they emit light. The signature CTA wears a `rgba(255, 255, 255, 0.98) 0px 0px 4px 1px` pure-white halo glow, as if the button is a small lantern hovering above the dark page. Secondary surfaces use `rgba(255, 255, 255, 0.24) 0px 0px 0px 1px inset` — a hairline inner highlight that mimics the way light catches the rim of a glass. Combined with peach-orange accents, animated orbital paths, and full-bleed cosmic gradient washes, the site feels like the inside of a planetarium that's running a relationship graph.

**Key Characteristics:**
- Verlag / VerlagCondensed (Hoefler) display + Chronicle Text serif for editorial body — H&Co commitment top to bottom
- Near-black canvas (`#0f0f10` / `#1d1d1f`) — cosmic black, never sterile gray
- Peach-cream accent (`#f2b98b`) for primary text-CTAs and key links — the only chromatic note
- Cream-white CTA pills (`#fdfcfa`) with pure-white glow halos — buttons emit light
- Orbital glow lines and soft warm gradient washes serve as the only "illustration"
- Inset hairline shadows (`rgba(255,255,255,0.24) inset`) on tinted-glass surfaces
- Subtle press-scale interactions (`scale(0.99)` on hover) — tactile but restrained
- Body text held at `rgba(255, 255, 255, 0.7)` — never pure white, always slightly held back
- Generous border radii (8 / 12 / 14 / 16 / 36 / 50%) — Mesh is curved, never sharp

## 2. Color Palette & Roles

### Primary
- **Mesh Black** (`#0f0f10`): Primary page background — a near-pure black with the faintest blue-purple cast that reads as warm cosmic dark, not tech-OLED.
- **Mesh Carbon** (`#1d1d1f`): Secondary surface — cards, panels, raised content blocks. One step lifted from canvas.
- **Body Off-White** (`rgba(255, 255, 255, 0.7)`): Default body text. Never pure `#fff` — a 70% tint that sits gently on dark surfaces and signals "this is reading, not chrome."

### Brand Accent
- **Mesh Peach** (`#f2b98b`): The signature color — applied to text-style CTAs, primary links, default hover-from state, and the warm orbital glows in the hero. A peach-cream tone that reads as starlight or candlelight.
- **Mesh Ember** (`rgba(251, 114, 50, 0.8)`): Hover saturation step — when the peach accent is interacted with, it warms toward orange at 80% opacity. Reserved for hover/active states only.
- **Mesh Rose** (`#db9c94`): Soft skin-tone rose used in muted accent imagery, secondary glow gradients, and avatar tints. The system's quiet third color.

### Neutrals & Text
- **Pure White** (`#ffffff`): Reserved for emphasis text on dark surfaces — primary headlines, key callouts, and the inner-fill of the cream CTA button.
- **Cream White** (`#fefef7` / `#fdfcfa`): The CTA button background — warmer than pure white by a hair, which reads as paper under lamplight, not screen-white.
- **Slate Gray** (`#868f97`): Tertiary text, footnotes, low-priority links. Cool blue-gray that disappears against the dark canvas without becoming illegible.

### Surface & Borders
- **Glass Inset** (`rgba(255, 255, 255, 0.24)`): Inner-shadow hairline used as a 1px inset border on raised glass-like surfaces. The signature "rim of light" detail.
- **Border Hairline** (`rgba(255, 255, 255, 0.06)`): Almost-invisible bottom borders on dividers and section breaks — felt more than seen.
- **Border Subtle** (`rgba(151, 151, 151, 0.2)`): Slightly more visible top divider used in stacked content blocks.

### Shadow & Glow Colors
- **Lantern Halo** (`rgba(255, 255, 255, 0.98) 0px 0px 4px 1px`): The CTA's signature glow — a pure-white blur with a 1px spread that makes the button appear to emit light.
- **Soft Drop** (`rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.08) -8px 12px 22px 0px`): Floating-card shadow used on light-on-dark sections (testimonials, panels). Asymmetric offset gives it a hand-placed quality.
- **Inset Highlight** (`rgba(255,255,255,0.1) 0px -2px 3px 0px inset, rgba(255,255,255,0.06) 0px -4px 12px 0px inset`): Bottom-up inset glow on glassy buttons — reads like reflected light from below.

### Gradient System
- Mesh uses **atmospheric radial gradients** as backgrounds — warm peach/orange/rose washes radiating from the bottom or behind the hero, fading into the cosmic black canvas. These are scenic, not decorative — they replace photography. The gradients are always low-saturation, soft-radius (`0px 0px 36px 36px`-style mask radii), and never used inside components — only behind them.

## 3. Typography Rules

### Font Family
- **Display Bold**: `VerlagCondensed`, fallback `Verlag, system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue` — used for hero and section heads at 700–900 weight
- **UI / Body Sans**: `Verlag` — used for navigation, button labels, secondary heads, body copy, and most chrome
- **Editorial Serif**: `ChronicleTextG1Roman`, fallback `IBM Plex Serif` — used for pull quotes, subheads, and the literary intro paragraphs
- **System Fallback**: `system-ui, -apple-system` — only for legal/footnote chrome

*Note: Verlag and Chronicle are both commercial Hoefler & Co. typefaces. For external implementations, `Söhne` or `Neue Haas Grotesk` substitute for Verlag; `IBM Plex Serif` or `Source Serif Pro` substitute for Chronicle. The condensed-display + literary-serif pairing is the brand signature — preserve the contrast.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | VerlagCondensed | 64px (4.00rem) | 700 | 1.00 | +0.88px | "Every relationship." landing statement |
| Display Large | VerlagCondensed | 48px (3.00rem) | 900 | 1.00 | +0.66px | Section headline, all-caps emphasis |
| Editorial Lead | ChronicleTextG1Roman | 22px (1.38rem) | 400 | 1.55 | normal | Intro paragraphs, literary moments |
| Subhead | Verlag | 20px (1.25rem) | 700 | 1.00 | +0.25px | Section subheads, emphasized labels |
| Body Large | Verlag | 20px (1.25rem) | 400 | 1.40 | normal | Primary body, feature descriptions |
| Body | Verlag | 18px (1.13rem) | 400 | 1.50 | normal | Standard reading text |
| Link Bold | Verlag | 16px (1.00rem) | 700 | 1.00 | +0.22px | Nav links, emphasized inline links |
| UI Default | Verlag | 16px (1.00rem) | 400 | 1.00–1.38 | +0.22px | Buttons, form labels, chrome |
| Caption | Verlag | 14px (0.88rem) | 400–600 | 1.00–1.14 | normal | Metadata, secondary labels |
| Tiny Caps | Verlag | 12px (0.75rem) | 700 | 2.25 | +1px | Uppercase eyebrow labels, button caps |
| Micro Caps | Verlag | 12px (0.75rem) | 700 | 3.00 | +1.2px | Section eyebrows with extra air |
| Footnote | system-ui | 10px (0.63rem) | 500 | 2.00 | +1px | Uppercase legal/meta footers |

### Principles
- **H&Co commitment**: Verlag for display and UI, Chronicle for editorial body — the dual-stack is non-negotiable. Drop in a system serif and the brand collapses.
- **Positive tracking on display**: Unlike most modern brands that crank negative tracking on big type, Mesh adds +0.66–0.88px to display sizes. The condensed letterforms are tight on their own; the extra space gives them air and dignity.
- **Three-weight system**: 400 for body and UI, 700 for emphasis and bold links, 900 for the loudest section heads. No 500/600 in display contexts — Mesh is binary on weight at headline scale.
- **Body text held at 70% white**: Never `#ffffff` for paragraphs. The held-back tone is the difference between editorial and clinical.
- **Uppercase eyebrows with +1px tracking**: 12px Verlag 700 uppercase with `1px` letter-spacing and `2.25–3.0` line-height — the signature small-cap label that opens most sections.
- **Serif for the human moments**: When the page wants to slow you down (pull quotes, mission statement, intro paragraph), it switches to Chronicle. The serif IS the pause.

## 4. Component Stylings

### Buttons

**Primary Cream CTA** (the signature "Book a demo" / "Get started")
- Background: Cream White (`#fdfcfa`)
- Text: Mesh Black (`#000000`)
- Padding: `0px 27px` (text-baseline driven, height set by line-height)
- Radius: `14px` (medium pill — never sharp)
- Border: `0px none`
- Shadow: `rgba(255, 255, 255, 0.98) 0px 0px 4px 1px` — pure-white lantern halo
- Font: 18px Verlag weight 600
- Hover: `transform: translate(0px, 0px) scale(0.99)` — subtle press-in
- Use: Primary CTA across hero, footer, and pricing — the page's only "loud" interactive

**Peach Text CTA** (header / inline)
- Background: transparent
- Text: Mesh Peach (`#f2b98b`)
- Padding: 0
- Radius: `8px`
- Border: `0px`
- Shadow: `rgba(255, 255, 255, 0.24) 0px 0px 0px 1px inset` — glass hairline
- Font: 12px Verlag weight 400
- Hover: background → `rgba(251, 114, 50, 0.8)`, text → `#ffffff`, scale → 0.99
- Use: Header navigation CTA, secondary inline actions

**Peach Outlined CTA** (bottom CTA / inline)
- Background: `#ffffff` (when on dark gradient sections)
- Text: Mesh Peach (`#f2b98b`)
- Padding: standard 16–24px horizontal
- Radius: `16px`
- Border: `0px none rgb(242, 185, 139)` (color reserved as outline source)
- Hover: background → `rgba(251, 114, 50, 0.8)`, text → white, scale → 0.99
- Use: Mid-page CTAs that need to read as actionable without competing with the cream primary

### Cards & Containers
- Background: `#1d1d1f` (carbon) on dark canvas; floating cards use cream-white in testimonial sections
- Border: hairline `rgba(255, 255, 255, 0.06)` bottom or `1px solid rgb(255, 255, 255)` for hard separation
- Radius: `12px` standard, `16px` for emphasized panels, `36px` for hero/feature blocks
- Shadow: floating cards use `rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.08) -8px 12px 22px 0px` — soft 1px ring + asymmetric drop
- Internal padding: 24–36px standard, 56–64px for hero feature cards

### Badges / Tags / Pills
Mesh's extracted design has no hardened badge component — labels and tags are rendered as small uppercase Verlag captions (12px / weight 700 / +1px tracking) inline rather than in chromed pills. When pill containers ARE used, they inherit the medium radii (`6–14px`) and the inset hairline glass treatment.

### Inputs & Forms
The marketing page exposes minimal form chrome — primary form fields appear in the product UI screenshots. Inferred styling for the brand:
- Background: `rgba(255, 255, 255, 0.04)` — barely-there glass
- Border: `1px solid rgba(255, 255, 255, 0.06)` hairline
- Radius: `8–12px`
- Font: 16px Verlag weight 400
- Text color: `rgba(255, 255, 255, 0.7)` body, white on focus
- Focus: peach accent (`#f2b98b`) outline + intensified inset glow

### Navigation
- Top nav: dark transparent bar, left-aligned Mesh logo (114×26 SVG wordmark), center pill nav, right-aligned `Log in` link + Cream CTA `Book a demo`
- Links: Verlag 16px weight 400, color `rgba(255, 255, 255, 0.7)`
- Hover: text → pure white, no underline (Mesh never underlines links)
- Logo: 114×26 white wordmark on black — never inverted, always the dark canvas

### Decorative Elements

**Orbital Glow Paths**
- Animated thin curved lines (1px peach `#f2b98b` at low opacity) tracing arcs through the hero
- Combined with bright "starburst" points at intersections — the only graphic illustration in the system
- Reads as celestial — the visual metaphor for relationships orbiting the user

**Atmospheric Gradient Washes**
- Soft radial gradients in peach/rose/orange fade from bottom-of-section into black
- Used as scene-setters between major content blocks
- Never inside a card — gradients are for the world behind components, not the components themselves

**Mask-Radius Backgrounds**
- Image / video panels use heavy corner masks — `0px 0px 36px 36px` on bottom corners — that round the bottom of inset media
- The 36px radius is unusually large; it's a deliberate visual softening signal

## 5. Layout Principles

### Spacing System
- Base unit: 8px, with frequent 6/9px sub-units for tight UI (badges, button padding)
- Scale: 6px, 9px, 12px, 16px, 18px, 24px (most-used), 36px, 56px, 64px, 150px+, 408px (max section)
- Notable: 24px is the workhorse value (25 occurrences in the extracted data). Mesh either sits at 24px or jumps to 56–64px for major sections — there's no 32px or 40px mid-range.

### Grid & Container
- Max content width: ~1200px for centered editorial content
- Hero: full-bleed gradient-and-orbital section, with text and product UI screenshot stacked or side-by-side
- Feature sections: alternating editorial-text-only and product-screenshot moments
- Full-bleed cosmic backgrounds extend edge-to-edge — content sits within them, never against a hard frame

### Whitespace Philosophy
- **Cosmic pacing**: Sections breathe at a planetarium scale — 150–200px between majors. The dark canvas absorbs whitespace better than light backgrounds, and Mesh leans into that.
- **Editorial rhythm**: Eyebrow caps (12px) → bold display headline (48px+) → editorial serif paragraph (22px Chronicle) — three discrete typographic registers, paced with generous gaps.
- **Product UI as illustration**: Where the hero needs visual interest, Mesh drops in a cropped screenshot of the actual product on a soft floating panel. The product is the illustration.

### Border Radius Scale
- Tight (4–8px): Buttons, small inputs, tight UI chrome
- Medium (12–16px): Cards, panels, primary CTAs — the workhorse range
- Generous (24–36px): Feature cards, hero panels, image containers
- Circle (50%): Avatars, orbital nodes, decorative dots
- No 0px: Mesh has zero sharp corners on interactive elements. Everything is curved. Sharpness would break the cosmic-soft language.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Body copy, structural containers, gradient backgrounds |
| Glass Hairline (Level 1) | `rgba(255, 255, 255, 0.24) 0px 0px 0px 1px inset` | Header CTA, glass buttons — rim-of-light effect |
| Soft Lift (Level 2) | `rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.08) -8px 12px 22px 0px` | Floating testimonial cards, content panels |
| Lantern Halo (Level 3) | `rgba(255, 255, 255, 0.98) 0px 0px 4px 1px` | Primary cream CTA — the "this button emits light" moment |
| Inset Glow (Level 4) | `rgba(255,255,255,0.1) 0px -2px 3px 0px inset, rgba(255,255,255,0.06) 0px -4px 12px 0px inset` | Specialty buttons with bottom-up reflected light |

**Shadow Philosophy**: Mesh's depth system is **luminous, not gravitational**. Where most dark-mode sites simulate elevation with downward drop shadows (mimicking a light source above), Mesh flips it: surfaces glow outward. The CTA halo emits light in all directions; inset shadows reflect light up from below; the cosmic background gradients glow from the floor of each section. Combined, these create a sense that the dark canvas is space and the components are luminous bodies floating in it. Hard offset shadows, sharp drop shadows, and atmospheric blur fog are all absent. The only "downward" shadow is the asymmetric `-8px 12px 22px` on floating cards, which reads more like a hand-placed paper than a stack of UI.

### Decorative Depth
- Glow halos pair with the cream-paper button surface to read as paper-under-lamplight, not glass-on-OLED
- Inset glass hairlines are reserved for transparent surfaces — they signal "this is glass, not solid"
- The orbital line paths in the hero have their own subtle bloom — they're rendered with a 1–2px glow that ties them to the same light system as the buttons

## 7. Do's and Don'ts

### Do
- Use Verlag / VerlagCondensed for all display and UI; Chronicle for editorial pull copy — preserve the H&Co commitment
- Hold body text at `rgba(255, 255, 255, 0.7)` on dark canvas — never pure white
- Apply Mesh Peach (`#f2b98b`) only to text-CTAs, key links, and orbital glow accents — preserve its starlight quality
- Use the lantern halo (`rgba(255,255,255,0.98) 0px 0px 4px 1px`) on primary cream CTAs — buttons should emit light
- Apply positive letter-spacing (+0.66 to +0.88px) on display sizes — Verlag Condensed needs the air
- Use uppercase eyebrow labels at 12px Verlag 700 with +1px tracking and 2.25–3.0 line-height
- Lean into atmospheric radial gradients (peach / rose / orange) behind sections, not inside components
- Use 12 / 14 / 16 / 36px curve radii — Mesh is curved, not sharp
- Use Chronicle serif for the slow human moments — pull quotes, mission lines, intro paragraphs
- Subtle press-scale `transform: scale(0.99)` for hover/active interactive feedback — tactile but quiet

### Don't
- Don't use system sans (SF, Inter, Helvetica) for headlines — Verlag is the brand
- Don't use 0px border-radius on interactive elements — Mesh has zero sharp corners
- Don't use pure `#000000` for background — Mesh Black `#0f0f10` carries the cosmic warmth
- Don't use pure `#ffffff` for body text — `rgba(255,255,255,0.7)` is the signature held-back white
- Don't introduce additional brand colors — peach, rose, cream are the entire palette
- Don't use hard offset shadows or material-style elevation — depth is luminous, not gravitational
- Don't use negative letter-spacing on display headlines — VerlagCondensed needs positive tracking
- Don't underline links — color and weight do the work
- Don't decorate with stock illustration or icons — orbital paths, gradient washes, and product screenshots are the visual language
- Don't crank saturation on the peach — it should always read as candlelight, not neon

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <479px | Single-column, hero drops to 36–40px, stacked CTAs |
| Mobile | 479–754px | Single-column editorial flow, 48px hero, full-width CTAs |
| Tablet | 755–991px | 2-column begins on feature pairs, 56px hero |
| Desktop | 992–1215px | Full multi-column layout, 64px hero, side-by-side product UI |
| Large Desktop | ≥1216px | Maximum scale, 64px hero, 1200px content container |

### Touch Targets
- Cream Primary CTA: min 48px tap height (height set by 18px Verlag at 1.35 line-height + 27px horizontal padding)
- Header peach CTA: min 40px tap height with comfortable 12px padding around the text
- Nav links: 16px Verlag with generous vertical padding for thumb access

### Collapsing Strategy
- **Nav**: Center pill nav collapses to hamburger menu on mobile; primary cream CTA stays visible
- **Hero**: 64px → 56px → 48px → 36px display headline, condensed weight maintained at every breakpoint
- **Editorial paragraphs**: Chronicle serif scales down to 18px on mobile but never converts to sans
- **Orbital decoration**: Simplifies to 1–2 arcs on mobile rather than the full multi-orbit cosmic field
- **Product UI screenshots**: Scale down proportionally, then stack below text on narrow widths
- **Section spacing**: 150–200px desktop → 64–96px mobile — compresses but still feels editorial

### Image Behavior
- Product UI screenshots maintain the soft cream-white card framing on all viewports
- Cosmic gradient backgrounds reflow with the viewport, never crop awkwardly
- Logo wordmark stays as wordmark — never reduces to a glyph
- Avatar circles in testimonials stay perfectly round (50% radius) at every size

## 9. Agent Prompt Guide

### Quick Color Reference
- Page Background: Mesh Black (`#0f0f10`)
- Card Background: Mesh Carbon (`#1d1d1f`)
- Primary Body Text: `rgba(255, 255, 255, 0.7)`
- Headline / Emphasis Text: `#ffffff`
- Brand Accent (links, text-CTAs): Mesh Peach (`#f2b98b`)
- Hover Saturation: Mesh Ember (`rgba(251, 114, 50, 0.8)`)
- Cream CTA Surface: `#fdfcfa`
- Cream CTA Halo: `rgba(255, 255, 255, 0.98) 0px 0px 4px 1px`
- Glass Inset: `rgba(255, 255, 255, 0.24) 0px 0px 0px 1px inset`
- Hairline Border: `rgba(255, 255, 255, 0.06)`

### Example Component Prompts
- "Create a hero section on Mesh Black (`#0f0f10`) with a soft radial peach-to-black gradient wash behind. Headline at 64px VerlagCondensed weight 700, line-height 1.00, letter-spacing +0.88px, color `#ffffff`. Below it, a 22px Chronicle Text serif paragraph at line-height 1.55 in `rgba(255, 255, 255, 0.7)`. Primary CTA: cream white (`#fdfcfa`) pill at `14px` radius, 18px Verlag weight 600, `0px 27px` padding, with `rgba(255, 255, 255, 0.98) 0px 0px 4px 1px` lantern halo shadow. Hover: scale to 0.99."
- "Design a header peach text CTA — transparent background, 12px Verlag weight 400 in `#f2b98b`, `8px` radius, `rgba(255, 255, 255, 0.24) 0px 0px 0px 1px inset` glass hairline. Hover: background to `rgba(251, 114, 50, 0.8)`, text to white, scale 0.99."
- "Build a floating testimonial card on cream white (`#fdfcfa`) at `12px` radius, with shadow `rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.08) -8px 12px 22px 0px`. Title 20px Verlag weight 700 with +0.25px letter-spacing, body 18px Verlag weight 400 line-height 1.50."
- "Create an uppercase eyebrow label — 12px Verlag weight 700, color `rgba(255, 255, 255, 0.7)`, letter-spacing +1px, line-height 2.25, transform uppercase."
- "Design an editorial pull quote in 22px ChronicleTextG1Roman weight 400, line-height 1.55, color `#ffffff`, no italic, no quote marks — let the typeface carry the literary weight."

### Iteration Guide
1. Default to Verlag / VerlagCondensed for everything — Chronicle ONLY for editorial body, never UI
2. Body text lives at `rgba(255, 255, 255, 0.7)` — pure white is reserved for headline emphasis only
3. Peach (`#f2b98b`) is precious — text-CTAs and key links only, never as a background fill
4. Curve radii are binary at the high end: `12–16px` workhorse, `36px` for feature panels, `50%` for circles. Never `0px`.
5. Display tracking is positive (+0.66 to +0.88px) — VerlagCondensed needs the air
6. Buttons emit light — every primary CTA gets the `rgba(255, 255, 255, 0.98) 0 0 4px 1px` halo
7. Backgrounds get atmospheric gradient washes; components do not — keep gradients OUTSIDE the box
8. Subtle press feedback only — `scale(0.99)` is the entire interaction vocabulary. No bounce, no rotate, no slide.
