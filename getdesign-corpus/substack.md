# Design System Inspired by Substack

## 1. Visual Theme & Atmosphere

Substack is editorial calm dressed up as a publishing platform. The system is built on a paper-white canvas (`#ffffff`), deep near-black ink (`#1a1a1a`), and a single saturated flame-orange (`#FF6719`) that does all the conversion work. Where social platforms shout with gradients, ambient glows, and chromatic clutter, Substack reads like a newsstand: thin rules, calm cards, generous reading column, and one bold accent that always means the same thing — "subscribe" or "start your Substack." The atmosphere is anti-feed-algorithm by design. Posts breathe. The interface gets out of the way.

The typographic identity splits cleanly in two. The product chrome — navigation, buttons, metadata, dashboard — runs on a humanist sans-serif (system-equivalent to `Söhne` / `Inter`) at modest weights. The reading surface — every post on every publication — flips to a transitional serif (system-equivalent to `Source Serif Pro` / `Charter` / Substack's house serif) at 18–20px with comfortable 1.6 line-height. This split is the brand's most defining mechanism: the platform speaks in sans, but the writers speak in serif. Readers always know which one they're hearing.

What sets Substack apart visually is its **restraint with elevation**. Cards do not float on dramatic shadows. Borders are thin (`1px solid #e6e6e6`) and the radii are gentle (4–6px). There are no gradients, no glassmorphism, no decorative blobs. The interface is closer to a well-set magazine page than to a SaaS dashboard. The orange CTA is the only place the system raises its voice, and that voice carries because everything around it stays quiet.

**Key Characteristics:**
- Substack Orange (`#FF6719`) used exclusively for CTAs, subscribe states, and brand moments
- Paper-white canvas (`#ffffff`) with near-black ink (`#1a1a1a`) — newsstand neutrality
- Sans-serif for product chrome, serif for reading — the platform-vs-publication signal
- Three-column app shell on desktop: left rail nav, center feed, right rail (suggested reads, profile)
- Cards with thin `1px` borders, gentle 4–6px radius, no offset shadows
- Avatar-led metadata: every card opens with a circular author avatar + name + publication
- Generous reading-column max-width (~640–720px) on post pages
- No gradients, no decorative illustrations — typography and photography only

## 2. Color Palette & Roles

### Primary
- **Substack Orange** (`#FF6719`): The signature flame accent — applied to primary CTAs ("Start your Substack", "Subscribe"), brand mark, active nav states, and notification dots. The only saturated color in the system.
- **Substack Ink** (`#1a1a1a`): Primary text on light backgrounds. A deep near-black that reads as ink, not OLED black.
- **Paper White** (`#ffffff`): Default page background and card surface.

### Brand Accent Variants
- **Orange Hover** (`#E55A14`): A 10% darker orange for button hover states.
- **Orange Tint** (`#FFF4ED`): A pale orange wash for selected states, info banners, and subscribe-success moments. Used sparingly.

### Neutrals & Text
- **Substack Ink** (`#1a1a1a`): All primary headings and body copy.
- **Reading Gray** (`#404040`): Body copy on long-form posts when softer than ink is desired.
- **Metadata Gray** (`#737373`): Bylines, timestamps, post stats, and secondary nav labels.
- **Disabled Gray** (`#b3b3b3`): Inactive icons and placeholder text.

### Surface & Borders
- **Card Surface** (`#ffffff`): Default card and modal background — matches page canvas.
- **Section Tint** (`#fafafa`): A barely-perceptible warm gray for alternating sections, sidebars, and the right-rail "Up next" panel.
- **Hairline Border** (`#e6e6e6`): The workhorse 1px border around feed cards, post cards, and input fields.
- **Strong Border** (`#d4d4d4`): A slightly darker rule used on hover and for active separators.

### Status & Utility
- **Like Red** (`#dc2626`): Heart/like states only — never used for CTAs.
- **Restack Green** (`#16a34a`): Restack confirmations and success toasts.
- **Lock Yellow** (`#eab308`): Paywalled content indicators.

### Gradient System
- Substack is **functionally gradient-free**. The system relies on solid orange + neutral relationships, thin borders, and typography. The only place a soft gradient appears is the optional cover-image scrim on publication headers, which is a low-opacity black-to-transparent overlay (`rgba(0,0,0,0) → rgba(0,0,0,0.4)`) for legibility — never a brand decoration.

## 3. Typography Rules

### Font Family
- **Product Sans (chrome)**: `Söhne`, `Inter`, system-ui sans fallback — for navigation, buttons, metadata, dashboard.
- **Reading Serif (publications)**: `Source Serif Pro`, `Charter`, `Georgia` fallback — for post bodies, post titles, pull quotes, and any author-authored prose.
- **Monospace (rare)**: `Söhne Mono`, `JetBrains Mono`, `ui-monospace` — for code blocks inside posts only.
- **OpenType Features**: Standard ligatures, old-style figures inside reading copy, lining figures inside chrome. No exotic stylistic sets.

*Note: Substack uses commercial typefaces in its production system. For external implementations, `Inter` (sans) and `Source Serif Pro` (serif, free via Google Fonts) are the closest open substitutes. `Charter` ships free with macOS and is an excellent reading-serif backup.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Marketing Hero | Sans | 56px (3.50rem) | 700 | 1.05 | -0.02em | Homepage and landing-page headlines |
| Marketing H2 | Sans | 40px (2.50rem) | 700 | 1.10 | -0.01em | Section heads on marketing pages |
| Post Title (article) | Serif | 36–44px | 700 | 1.15 | -0.01em | The article H1 on a publication post |
| Post Title (card) | Serif | 22–24px | 700 | 1.25 | normal | Title shown in feed cards |
| Section Heading | Sans | 20px (1.25rem) | 600 | 1.30 | normal | "Up next", "Discussions", dashboard sections |
| Subscribe Form Heading | Sans | 24px (1.50rem) | 700 | 1.20 | -0.01em | "Sign up to..." subscribe prompts |
| Body (reading) | Serif | 19–20px | 400 | 1.60 | normal | The reading column — comfortable for long-form |
| Body (chrome) | Sans | 15px (0.94rem) | 400 | 1.45 | normal | UI body text, dashboard prose |
| Card Body | Sans | 14px (0.88rem) | 400 | 1.40 | normal | Excerpts and descriptions in feed cards |
| Metadata | Sans | 13px (0.81rem) | 400 | 1.30 | normal | Bylines, timestamps, post stats |
| Button (primary) | Sans | 15px (0.94rem) | 600 | 1.00 | normal | "Subscribe", "Start your Substack" |
| Button (small) | Sans | 13px (0.81rem) | 600 | 1.00 | normal | Inline subscribe, restack |
| Caption | Sans | 12px (0.75rem) | 400 | 1.30 | 0.01em | Image credits, footnotes |

### Principles
- **Sans for chrome, serif for content**: This is the most important typographic rule. Anywhere a writer's voice appears (post body, post title, pull quote, author bio prose), use serif. Anywhere the platform speaks (nav, buttons, dashboards, metadata), use sans. Mixing them collapses the brand's central tension.
- **Reading column over chrome density**: Post bodies use 19–20px serif at 1.60 line-height, even on desktop. Substack errs toward magazine-comfort over screen-density.
- **Weight 700 for emphasis, 400 for prose**: Substack uses a tight two-weight palette in its serif (400 regular, 700 bold) and adds 600 in the sans for buttons and section heads. No 300, no 800/900 — the stack stays calm.
- **Title case on marketing, sentence case in product**: Marketing pages use Title Case headlines. The product UI (dashboards, settings, modals) uses sentence case to feel like reading rather than shouting.
- **Negative tracking only at display sizes**: Headlines 36px and up tighten to `-0.01em` to `-0.02em`. Anything 24px and below stays at normal tracking. Reading copy never gets tracked.

## 4. Component Stylings

### Buttons

**Primary Orange**
- Background: Substack Orange (`#FF6719`)
- Text: Pure White (`#ffffff`)
- Padding: 10px 20px standard, 12px 28px large
- Radius: `4px`
- Border: none
- Shadow: none in default state
- Font: 15px Sans weight 600
- Hover: background shifts to `#E55A14`, no transform
- Active: background shifts to `#CC4F12`
- Use: Primary CTA — "Subscribe", "Start your Substack", "Sign up", "Publish"

**Secondary Outline**
- Background: transparent
- Text: Substack Ink (`#1a1a1a`)
- Border: `1px solid #d4d4d4`
- Radius: `4px`
- Padding: 10px 20px
- Font: 15px Sans weight 600
- Hover: border darkens to `#1a1a1a`, background tints to `#fafafa`
- Use: Secondary actions — "Sign in", "Learn more", "Get app"

**Ghost Text Button**
- Background: transparent
- Text: Substack Ink (`#1a1a1a`)
- Border: none
- Padding: 6px 8px
- Font: 14px Sans weight 500
- Hover: text shifts to `#737373`
- Use: Inline secondary actions, tertiary nav

**Subscribe (inline, on cards)**
- Background: transparent
- Text: Substack Orange (`#FF6719`)
- Border: none
- Padding: 4px 0
- Font: 13px Sans weight 600
- Hover: text darkens to `#E55A14`, optional underline
- Use: The "Subscribe" link that appears on every feed card next to the publication name

### Cards & Containers

**Feed Card**
- Background: Paper White (`#ffffff`)
- Border: `1px solid #e6e6e6`
- Radius: `6px`
- Shadow: none
- Padding: 16–20px
- Composition: avatar (32px circle) + author name + Subscribe link + post title (serif) + excerpt (sans, gray) + image (full-bleed within card) + reaction row
- Hover: border darkens to `#d4d4d4`

**Post Card (publication grid)**
- Background: `#ffffff`
- Border: `1px solid #e6e6e6` or borderless on white sections
- Radius: `4px`
- Cover image: 16:9 aspect, `4px` top radius, full bleed of card width
- Padding below image: 16px
- Title in serif weight 700, byline + date in sans 13px gray

**Right-Rail Panel**
- Background: Section Tint (`#fafafa`)
- Border: `1px solid #e6e6e6`
- Radius: `6px`
- Padding: 16px
- Use: "Log in or sign up", "Up next", "Get app" promo block

### Badges / Tags / Pills
**Category Pill**
- Background: `#f5f5f5`
- Text: `#404040`
- Border: none
- Padding: 4px 10px
- Radius: `9999px`
- Font: 13px Sans weight 500

**Paid Badge**
- Background: `#fef9c3`
- Text: `#854d0e`
- Padding: 2px 6px
- Radius: `3px`
- Font: 11px Sans weight 600 uppercase, `0.04em` tracking
- Use: "PAID" indicator on premium posts

### Inputs & Forms
- Background: `#ffffff`
- Border: `1px solid #d4d4d4`
- Radius: `4px`
- Font: 15px Sans weight 400
- Text color: `#1a1a1a`
- Placeholder: `#b3b3b3`
- Focus: border shifts to `#FF6719`, no glow, no shadow
- Padding: 10px 12px
- Used heavily for the email-capture subscribe input — often inline with an orange Subscribe button

### Navigation

**Left Rail (App Shell)**
- Width: ~64px (icons) or ~220px (expanded with labels)
- Background: `#ffffff`
- Border: `1px solid #e6e6e6` on the right edge
- Items: Home, Subscriptions, Chat, Activity, Explore, Profile, Create
- Icon size: 20–22px, weight 1.5 stroke
- Active state: orange icon (`#FF6719`) + bold sans label
- Inactive state: ink icon (`#1a1a1a`) + regular sans label
- "Create" button at the bottom: filled orange pill

**Top Bar (Publication)**
- Height: 64px
- Background: `#ffffff` with bottom `1px solid #e6e6e6`
- Logo/wordmark left-aligned (publication-controlled, often serif)
- Right side: search, "Sign in" ghost, "Subscribe" primary orange

### Decorative Elements

**Author Avatar Stack**
- Circular avatars (32–40px) with `2px solid #ffffff` separator when overlapped
- Used for "X subscribers" social-proof rows on subscribe modals

**Cover Image Treatment**
- Full-bleed at top of post; no scrim unless headline overlays the image
- Inside cards: 16:9 ratio, gentle radius matching the card

## 5. Layout Principles

### Spacing System
- Base unit: `4px`
- Scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 96px
- Notable: Substack favors mid-range spacing (16–32px) over the extremes. Sections breathe at 64–96px between majors, but cards stay tight at 16–20px internal.

### Grid & Container
- Reading column max-width: 640–720px on post pages — explicit magazine measure
- Feed/dashboard max-width: ~1200px three-column shell (left rail ~64–220px, center feed ~600px, right rail ~320px)
- Marketing pages: ~1100px centered, with hero sections that occasionally break to full-width
- Gutters: 24px between cards in feed, 32px between rail and feed
- Mobile: single column, all rails collapse, bottom tab bar replaces left rail

### Whitespace Philosophy
- **Magazine pacing on posts**: Post pages use generous top space (96–128px above title) and a narrow column to mimic print reading — the reader gets one column of attention.
- **Dashboard density on chrome**: The app shell is denser, closer to Twitter or Notion in feel, where 16–20px gutters dominate.
- **Section breaks via tint, not rule**: Where most sites use a `1px` divider, Substack switches background to `#fafafa` for the next section — softer, more editorial.

### Border Radius Scale
- Sharp (`0px`): Full-bleed cover images, top edge of card images
- Soft (`4px`): Buttons, inputs, small cards, badges with corners
- Card (`6px`): Feed cards, panels, modals
- Pill (`9999px`): Category pills, avatar circles, toggle indicators
- No mid-range above 8px: Substack stays under 8px for rectangular surfaces — no chunky 12–20px radii.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body prose, structural sections |
| Hairline (Level 1) | `1px solid #e6e6e6` | Default card and panel separation — the workhorse |
| Strong Hairline (Level 2) | `1px solid #d4d4d4` | Hover states, active separators, focused inputs |
| Drop (Level 3) | `0 4px 12px rgba(0, 0, 0, 0.08)` | Modals, dropdowns, popovers |
| Modal Backdrop (Level 4) | `rgba(0, 0, 0, 0.5)` overlay + Drop shadow | Subscribe modals, settings dialogs |

**Shadow Philosophy**: Substack's depth system is essentially flat. The platform achieves separation through hairline borders and background tint shifts, not through atmospheric shadows. When shadows do appear (modals, dropdowns), they are soft, near-imperceptible, and never decorative. There are no offset shadows, no neumorphism, no inset effects. The interface looks closer to a well-printed page than to a Material Design layout — and that's the point.

### Decorative Depth
- Cover images sit flush inside cards with a sharp top edge meeting the card's rounded corners — the image clips to the card's `6px` radius on top
- Avatar circles use a `2px solid #ffffff` ring when stacked on tinted backgrounds
- No glow, no glassmorphism, no parallax depth — the only "z" cue is the modal scrim

## 7. Do's and Don'ts

### Do
- Reserve Substack Orange (`#FF6719`) for CTAs, subscribe actions, and brand moments — the orange should always mean "subscribe" or "publish"
- Use serif for any text authored by a writer (post titles, post bodies, quotes); use sans for UI chrome
- Default to `1px solid #e6e6e6` borders for separation — shadows are a last resort
- Keep card radius at `4–6px` — calm, not chunky
- Set reading copy at 19–20px serif with 1.60 line-height — magazine comfort wins over screen density
- Use `#fafafa` section tints for chapter-like breaks instead of horizontal rules
- Lead every feed card with a 32px circular avatar — the author is the unit of trust
- Stay near sentence case in product UI; Title Case is for marketing pages
- Pair the orange "Subscribe" button with a calm white email input for inline capture forms

### Don't
- Don't use orange for non-CTA decoration — it dilutes the action signal
- Don't mix serif and sans inside a single block of running prose — switch only at the chrome/content boundary
- Don't use offset shadows, neumorphism, or glassmorphism — Substack is flat by design
- Don't use radii above 8px on rectangular containers — chunky pills break the editorial feel
- Don't introduce additional saturated brand colors — orange + neutrals only
- Don't use light weights (300) anywhere — the stack lives at 400/600/700
- Don't crowd post pages with chrome — the reading column is sacred and the rails should feel optional
- Don't use heavy drop shadows on cards — hairline borders carry the same job calmer
- Don't replace the avatar-first card composition with a logo or thumbnail-first layout — the writer is the brand

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, bottom tab bar, full-width cards, hero type drops to 32–36px |
| Tablet | 640–1024px | Two-column shell (collapse right rail), left rail compresses to icons-only |
| Desktop | 1024–1280px | Full three-column shell, expanded left rail labels appear |
| Large Desktop | ≥1280px | Maximum reading column, comfortable rail spacing, hero up to 56px |

### Touch Targets
- Primary buttons: min 44px tap height, 16–20px horizontal padding on mobile
- Bottom tab bar items: 56px tall with icon + label
- Subscribe inputs: 48px tall on mobile to clear keyboard accessibility minimum
- Card hit targets: full card is tappable; subscribe links inside cards expand their hit area

### Collapsing Strategy
- **Left rail**: Desktop expanded → tablet icons-only → mobile bottom tab bar with 5 items
- **Right rail**: Desktop visible → tablet hidden → mobile only as a "More" sheet
- **Hero type**: 56px → 40px → 32px progressive scaling, weight 700 maintained
- **Reading column**: 720px desktop → 100% width with 16–20px page padding on mobile
- **Card padding**: 20px desktop → 16px mobile, never below 12px
- **Three-column feed**: collapses to single column under 1024px

### Image Behavior
- Cover images preserve 16:9 aspect across breakpoints
- Avatars stay circular at all sizes; never become square thumbnails
- Cards with images keep image at top on mobile (no side-by-side reflow)
- Inline post images get full reading-column width on desktop, full viewport width on mobile

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Substack Orange (`#FF6719`)
- Hover Orange: `#E55A14`
- Page Background: Paper White (`#ffffff`)
- Section Tint: `#fafafa`
- Primary Text: Substack Ink (`#1a1a1a`)
- Reading Body: `#404040`
- Metadata Gray: `#737373`
- Hairline Border: `#e6e6e6`
- Strong Border: `#d4d4d4`
- Modal Shadow: `0 4px 12px rgba(0, 0, 0, 0.08)`

### Example Component Prompts
- "Build a Substack-style feed card on a `#ffffff` background with `1px solid #e6e6e6` border, `6px` radius, 20px padding. Lead with a 32px circular author avatar, name in 14px Sans weight 600, then an inline orange `#FF6719` 'Subscribe' link in 13px weight 600. Title in serif (Source Serif Pro) 22px weight 700, line-height 1.25. Excerpt in 14px Sans `#737373`. Cover image 16:9 with sharp top edge meeting the card radius."
- "Create a Substack subscribe form: 48px-tall white input with `1px solid #d4d4d4` border, `4px` radius, 15px Sans placeholder in `#b3b3b3`. Pair with an orange `#FF6719` 'Subscribe' button, 15px Sans weight 600 white text, `4px` radius, 10px 20px padding, no shadow. Below: small metadata in 13px `#737373` — terms-of-service line."
- "Design a Substack post page reading column: max-width 720px, centered. Title in 40px serif weight 700, line-height 1.15, color `#1a1a1a`. Byline row in 14px Sans `#737373` with circular avatar. Body in 19px serif weight 400, line-height 1.60, color `#404040`. Generous 96px top padding above title."
- "Build a three-column app shell: 64px left icon rail (`#ffffff` with `1px solid #e6e6e6` right border), centered 600px feed column, 320px right rail with `#fafafa` tinted panels in `6px` radius. Active nav icon in orange `#FF6719`, inactive in ink `#1a1a1a`."
- "Design a category pill — `#f5f5f5` background, `#404040` text, `9999px` radius, 4px 10px padding, 13px Sans weight 500. Use for post tags and topic chips."

### Iteration Guide
1. Default to sans for product chrome and serif for any author-authored prose — this split is non-negotiable
2. Use orange `#FF6719` only for primary CTAs and subscribe states — never for decoration or non-action accents
3. Reach for `1px solid #e6e6e6` borders before drop shadows — Substack is flat by design
4. Keep radii in the 4–6px range for rectangles, `9999px` for circular elements — no chunky mid-range
5. Reading column at 19–20px serif with 1.60 line-height — magazine comfort over screen density
6. Avatar-led card composition: every feed card opens with a circular author avatar — the writer is the unit
7. Section tint (`#fafafa`) for chapter breaks instead of horizontal rules — softer separation
8. Stay in the 400/600/700 weight band — no 300, no 800 — the stack stays calm
