# Design System Inspired by HyperKit

## 1. Visual Theme & Atmosphere

HyperKit is the SaaS UI kit other SaaS UI kits get measured against — a whisper-quiet, near-monochrome system that reads like the bastard child of Vercel, Linear, and Notion. The kit's defining mood is restraint: a paper-white canvas (`#FFFFFF`), thin neutral hairlines (`#EAEAEA`), a black-tipped wordmark, and components that earn their presence through proportion and spacing rather than color or ornament. There is no brand color in the traditional sense. The "accent" is black. The "secondary" is a slightly lighter black. Status colors (green, red, amber, lavender) appear only inside data — never as decoration.

The kit is built around the assumption that the product designer adopting it wants the chrome to disappear. Every component — buttons, cards, inputs, dropdowns, command palettes, calendars, badges — is calibrated to a tight 4–8px spacing grid with 6–10px border radii that feel almost-but-not-quite-rounded. Type sits in a clear three-tier hierarchy (display, body, caption) using Inter or a near-clone, with weights pinned to 400 / 500 / 600. There is no 700, no italic flourish, no display serif. The work is done by air, alignment, and one-pixel borders.

What separates HyperKit from generic minimalist kits is the **subtle button gradient** — primary CTAs use a near-black surface with a faint top-edge highlight (visible as `linear-gradient(180deg, #2C2C2C 0%, #000 100%)` plus a 1px inner top stroke at low opacity) that gives the button a tactile, slightly-pillowed quality without ever crossing into skeuomorphism. Pair that with a soft `0 1px 2px rgba(0,0,0,0.05)` ambient drop and a `0 0 0 1px rgba(0,0,0,0.08)` inner ring, and you get a button that looks pressed-from-the-page — the same trick Vercel's primary CTA pulls. The rest of the system is flat. Only buttons and the occasional elevated card lift.

**Key Characteristics:**
- Pure white canvas (`#FFFFFF`) with thin `#EAEAEA` hairlines instead of fills for separation
- Inter (or near-clone) at 400 / 500 / 600 — no light, no bold, no italic
- Near-black primary buttons with subtle top-edge gradient and inner ring — Vercel-grade pillowing
- 6–10px border radii throughout — never sharp, never pill except for tags and avatars
- Status colors (green/red/amber/lavender) appear inside content only — not as decoration
- Dense iconography from Lucide / Phosphor — 16px stroke, 1.5–2px weight, monochrome
- Command palettes, breadcrumbs, segmented controls, toggle switches feel "stock product" — Linear/Notion DNA
- Cards use 1px border + soft `0 1px 2px rgba(0,0,0,0.05)` shadow, never heavy elevation
- Dark surfaces (`#0A0A0A` to `#171717`) appear only in dropdowns, tooltips, and the marketing chrome

## 2. Color Palette & Roles

### Primary
- **Hyperkit Black** (`#0A0A0A`): Primary text, primary button background, dark dropdown surface, marketing site background. Not pure black — a near-black that softens slightly under bright light.
- **Hyperkit White** (`#FFFFFF`): Primary canvas, card background, inverted button text, modal surface.
- **Off-Canvas** (`#FAFAFA`): Subtle panel background — sidebar fills, table row hover, kanban column base. The "second white" used to separate UI regions without introducing borders everywhere.

### Brand Accent
- HyperKit is **brand-color-free by design**. Black is the accent. The lone semi-chromatic flourish is the **AI-feature lavender** (`#8B5CF6`) that shows up on the "Ask AI" sparkle icon in command palettes and the "Assistant" entry in the editor's slash menu. It functions exactly like Cape's lavender — a single saturated hit, used surgically, never on backgrounds.
- **AI Lavender** (`#8B5CF6`): Sparkle icons, AI feature accents, occasional progress indicators.

### Neutrals & Text
- **Text Primary** (`#0A0A0A`): All body copy, headings, table content.
- **Text Secondary** (`#737373`): Labels, helper text, breadcrumb separators, metadata.
- **Text Tertiary** (`#A3A3A3`): Placeholder text, disabled states, caption metadata, "Up to 10MB, at least 500×500px"-style microcopy.
- **Text Inverse** (`#FFFFFF`): Text on black primary buttons, dark dropdown items, tooltip body.

### Surface & Borders
- **Border Default** (`#EAEAEA`): The workhorse hairline — card outlines, input borders, table dividers, sidebar separators. Visible but unassertive.
- **Border Subtle** (`#F5F5F5`): Internal dividers, lightly separated rows, secondary section breaks.
- **Border Strong** (`#D4D4D4`): Hover and focus states on inputs, selected card outlines.
- **Surface Sunken** (`#F5F5F5`): Code block, keyboard kbd badge, search input fill.
- **Surface Hover** (`#F5F5F5`): Hover background for menu items, list rows, sidebar entries.
- **Surface Selected** (`#EFEFEF`): Active sidebar item, selected list row — slightly darker than hover.

### Status Colors (used only inside content)
- **Success Green** (`#16A34A` text on `#DCFCE7` fill): "Done" status pills, success toasts.
- **In-Progress Lavender** (`#7C3AED` text on `#EDE9FE` fill): "In progress" status pills.
- **Warning Amber** (`#CA8A04` text on `#FEF3C7` fill): "Save 33%" pricing badges, attention indicators.
- **Danger Red** (`#DC2626` text on `#FEE2E2` fill): Destructive button background (`#DC2626` solid with white text), error states.
- **Info Blue** (`#2563EB` text on `#DBEAFE` fill): Informational toasts, link color when needed.

### Dark Mode Surfaces
- **Dark Surface** (`#0A0A0A`): Marketing site background, dark mode canvas.
- **Dark Surface Elevated** (`#171717`): Dark dropdown, tooltip, command palette in dark mode.
- **Dark Border** (`#262626`): Hairlines on dark surfaces.

### Gradient System
- **Primary Button Gradient**: `linear-gradient(180deg, #2C2C2C 0%, #000000 100%)` with an inner 1px top stroke at `rgba(255,255,255,0.08)` — the signature pillowed CTA.
- **Subtle Card Gradient** (rare): `linear-gradient(180deg, #FFFFFF 0%, #FAFAFA 100%)` on hero/upgrade cards. Mostly absent — the system is solid-fill-first.

## 3. Typography Rules

### Font Family
- **Primary**: `Inter`, with fallback stack `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
- **Display**: Same Inter, weight 600 — no separate display face. The wordmark uses a slightly tighter custom cut but mockup screens use Inter throughout.
- **Monospace**: `"Geist Mono"`, `"JetBrains Mono"`, `ui-monospace`, `SFMono-Regular`, monospace — for code, kbd badges, ticket IDs (`HYPE-1`, `PER-2`).
- **OpenType Features**: `cv11` (single-story 'a'), `ss03` (curved 'l'), tabular nums for tables and dates. Keeps numerals aligned in dashboards.

*Note: Hyperkit ships with Inter as the default. Geist is a strong substitute (the Vercel-screen mockups in the kit use Geist semantics). For external implementations, system-ui works as a graceful fallback.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Inter | 56–72px | 600 | 1.05 | -0.02em | Marketing landing — "The Minimal SaaS Figma UI Kit" |
| Display | Inter | 40px | 600 | 1.10 | -0.02em | Section openers — "Modern. Minimal. Easy to use." |
| Heading 1 | Inter | 32px | 600 | 1.15 | -0.01em | Page titles inside the product (e.g. "Storage", "Tasks") |
| Heading 2 | Inter | 24px | 600 | 1.20 | -0.01em | Subsection headers, modal titles |
| Heading 3 | Inter | 18px | 600 | 1.30 | -0.005em | Card titles, settings group labels |
| Heading 4 | Inter | 16px | 600 | 1.40 | 0 | Form section headers, sidebar group labels |
| Body Large | Inter | 16px | 400 | 1.50 | 0 | Primary reading body, paragraph copy |
| Body | Inter | 14px | 400 | 1.45 | 0 | Default product UI text — table cells, menu items, descriptions |
| Body Medium | Inter | 14px | 500 | 1.45 | 0 | Button labels, navigation links, emphasis |
| Caption | Inter | 13px | 400 | 1.40 | 0 | Helper text, metadata, "Sent you an invite to connect" |
| Small | Inter | 12px | 400–500 | 1.35 | 0 | Badge text, tag labels, breadcrumb crumbs, table column headers |
| Mono / Code | Geist Mono | 13px | 400 | 1.40 | 0 | Code, IDs, kbd shortcuts (`⌘K`, `HYPE-1`) |

### Principles
- **Three-weight discipline**: 400 / 500 / 600. No 300, no 700, no italic. Emphasis comes from weight bumps (400 → 500) and color shifts (`#737373` → `#0A0A0A`), never from italics or alternate cuts.
- **Negative tracking on display only**: Display sizes (≥24px) get `-0.02em` to `-0.005em`. Body and below stay at 0 for legibility — no "tight everywhere" cargo-cult.
- **Tabular numerals everywhere with data**: Pricing pages, tables, calendars, plan-usage cards all use tabular figures so columns align without manual padding.
- **Color does the hierarchy work, weight is the second pass**: A label at `#737373` reads as secondary even if it's the same size and weight as a `#0A0A0A` value next to it. The kit leans on this constantly — "Workspace name" label at gray, "Hyperkit" value at black.
- **Mono for ALL machine-generated text**: Ticket IDs, billing amounts in tables, code snippets, keyboard shortcuts. Never use mono for prose.

## 4. Component Stylings

### Buttons

**Primary Black**
- Background: `linear-gradient(180deg, #2C2C2C 0%, #000000 100%)`
- Text: `#FFFFFF`, Inter 14px weight 500
- Padding: 8px 14px (small), 10px 16px (default), 12px 20px (large)
- Radius: `8px`
- Border: inner top highlight `inset 0 1px 0 rgba(255,255,255,0.08)`
- Shadow: `0 1px 2px rgba(0,0,0,0.08), 0 0 0 1px rgba(0,0,0,0.04)`
- Hover: gradient shifts darker (`#1A1A1A` to `#000`), shadow strengthens to `0 2px 4px rgba(0,0,0,0.12)`
- Use: Primary CTA — "Buy now", "Continue", "Accept", "Create Database"

**Secondary White**
- Background: `#FFFFFF`
- Text: `#0A0A0A`, Inter 14px weight 500
- Padding: matches Primary
- Radius: `8px`
- Border: `1px solid #EAEAEA`
- Shadow: `0 1px 2px rgba(0,0,0,0.04)`
- Hover: background `#FAFAFA`, border `#D4D4D4`
- Use: Secondary actions — "Decline", "Preview", "Upload image", "Upgrade to Premium"

**Ghost / Tertiary**
- Background: transparent
- Text: `#0A0A0A`, Inter 14px weight 500
- Padding: 6px 10px
- Radius: `6px`
- Border: none
- Hover: background `#F5F5F5`
- Use: In-table actions, menu items, low-emphasis buttons in toolbars

**Destructive Red**
- Background: `#DC2626` (with the same subtle gradient treatment as primary, optional)
- Text: `#FFFFFF`, Inter 14px weight 500
- Radius: `8px`
- Use: "Delete workspace", irreversible actions

**Icon Button**
- Size: 28px or 32px square
- Background: transparent default, `#F5F5F5` hover
- Radius: `6px`
- Icon: 16px Lucide-style stroke at `#737373`, becomes `#0A0A0A` on hover

### Cards & Containers

**Default Card**
- Background: `#FFFFFF`
- Border: `1px solid #EAEAEA`
- Radius: `12px`
- Shadow: `0 1px 2px rgba(0,0,0,0.04)` ambient — barely there
- Internal padding: 20–24px standard, 32px for feature cards
- Use: Pricing tiers, dashboard widgets, settings panels, plan-usage cards

**Sunken Panel**
- Background: `#FAFAFA`
- Border: `1px solid #EAEAEA` (optional, often borderless against white parent)
- Radius: `8px`
- Use: Code blocks, sidebar regions, kanban column backgrounds, search input wells

**Empty State Card**
- Same chrome as Default Card with extra padding (48–64px)
- Centered icon (40px) above 16px heading + 14px description + CTA button
- Pattern repeats across the kit's empty-state library

### Badges / Tags / Pills

**Status Pill (filled)**
- Padding: 2px 8px
- Radius: `9999px` (pill) or `6px` (rounded rect — both used)
- Font: 12px Inter weight 500
- Pattern: tinted background + saturated text — `bg #DCFCE7 / text #16A34A` for Done, `bg #EDE9FE / text #7C3AED` for In Progress, `bg #FEF3C7 / text #CA8A04` for "Save 33%"
- Often paired with a 6px colored dot at the start

**Neutral Tag**
- Background: `#F5F5F5`
- Text: `#0A0A0A`, 12px Inter weight 500
- Border: none
- Radius: `6px`
- Use: Plan label "Hobby", section markers like "Beta", "Invite"

**Outline Tag**
- Background: transparent
- Border: `1px solid #EAEAEA`
- Same metrics as Neutral Tag
- Use: Filter chips, low-emphasis category tags

**KBD Shortcut**
- Background: `#F5F5F5`
- Border: `1px solid #EAEAEA`
- Radius: `4px`
- Padding: 1px 6px
- Font: 12px Geist Mono weight 500, color `#737373`
- Use: `⌘K`, `⌥A`, `M`, `F` shortcut hints in command palettes

### Inputs & Forms

**Text Input**
- Background: `#FFFFFF`
- Border: `1px solid #EAEAEA`
- Radius: `8px`
- Padding: 8px 12px
- Font: 14px Inter weight 400
- Placeholder: `#A3A3A3`
- Focus: border `#0A0A0A`, plus `0 0 0 3px rgba(0,0,0,0.06)` focus ring halo
- Disabled: background `#FAFAFA`, text `#A3A3A3`

**Search Input**
- Background: `#FAFAFA` or `#F5F5F5` (sunken variant)
- Border: `1px solid #EAEAEA`
- Radius: `8px`
- Leading icon: 16px magnifying glass at `#737373`, 12px from left edge

**Toggle Switch**
- Track: 32×18px, radius `9999px`
- Off state: background `#EAEAEA`
- On state: background `#0A0A0A`
- Knob: 14px white circle with `0 1px 2px rgba(0,0,0,0.15)` shadow

**Radio / Checkbox**
- Size: 16×16px
- Border: `1.5px solid #D4D4D4` unselected
- Selected radio: black ring `#0A0A0A` with 6px black inner dot
- Checkbox checked: filled `#0A0A0A` background with white checkmark

### Navigation

**Top Nav (marketing)**
- Logo left, links right ("Examples", "Pricing", "FAQ"), plus "Preview" ghost and "Buy now $37" primary
- Background: `#FFFFFF` with `1px solid #EAEAEA` bottom border
- Sticky on scroll
- Link: 14px Inter weight 500, color `#737373`, hover `#0A0A0A`

**App Sidebar**
- Background: `#FAFAFA`
- Width: 240–280px
- Item: 6px 10px padding, 6px radius, hover `#F5F5F5`, active `#EFEFEF`
- Group label: 12px uppercase weight 500 color `#737373`, padding 16px 10px 4px

**Breadcrumbs**
- Each crumb: 14px Inter weight 400 color `#737373`, last crumb `#0A0A0A` weight 500
- Separator: 14px chevron-right at `#A3A3A3`
- Trailing leaf gets a 16px icon (folder, doc, lightning bolt for "Hyperkit")

**Command Palette**
- Surface: `#FFFFFF` with `1px solid #EAEAEA`, radius `12px`
- Shadow: `0 12px 32px rgba(0,0,0,0.10), 0 0 0 1px rgba(0,0,0,0.04)`
- Search input borderless at top with 16px magnifier
- Items: 36px tall, 12px horizontal padding, hover `#F5F5F5`
- Trailing kbd shortcuts right-aligned

### Decorative Elements

**Avatar**
- Default: 24/32/40px circle, photo or initials
- Initials: `#F5F5F5` background, `#0A0A0A` text, Inter weight 500
- Border: `2px solid #FFFFFF` when stacked

**Tooltip**
- Surface: `#0A0A0A`
- Text: `#FFFFFF`, 12px Inter weight 500
- Padding: 6px 10px
- Radius: `6px`
- Tail: 6px triangle, same `#0A0A0A`
- Use: "Almost done" hint over a progress bar

**Progress Bar**
- Track: `#EAEAEA`, 4px tall, radius `9999px`
- Fill: `#0A0A0A`, same radius, animated width

**Calendar**
- Day cell: 36×36px, radius `8px` on selected, hover `#F5F5F5`
- Selected: `#0A0A0A` background, white text
- Today: `#F5F5F5` background, black text (no ring)
- Dimmed days: `#A3A3A3`
- Header: month name 14px weight 500, chevron buttons 28px ghost

## 5. Layout Principles

### Spacing System
- Base unit: 4px
- Scale: 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128
- Notable: heavy use of 8 / 12 / 16 / 24 inside components, 48 / 64 / 80 between sections. The 20px and 40px steps appear specifically for card and section padding — half-steps that prevent cramped or yawning gaps.

### Grid & Container
- Max content width: 1200px for marketing, 1280–1440px for product dashboards
- 12-column responsive grid at desktop, 4-column at tablet, single-column at mobile
- Sidebar + main pattern is the dominant product layout — 240/280px sidebar, fluid main
- Pricing: 3-column equal-width tier grid, 24px gap, all tiers same height regardless of feature list length

### Whitespace Philosophy
- **Card-density first**: Cards stack with 16–24px gaps inside sections, sections separate with 64–80px vertical air. Air sits between sections; cards stay close inside them.
- **Internal padding > external margin**: Components carry their own breathing room (20–24px internal), so the parent container can use minimal padding without feeling cramped.
- **No decorative dividers**: Borders on cards do the section work. The kit almost never uses `<hr>`-style dividers — separation comes from background shifts (`#FFFFFF` → `#FAFAFA`) or card chrome.

### Border Radius Scale
- `4px`: kbd badges, tiny indicators
- `6px`: tags, ghost buttons, icon buttons, menu items
- `8px`: inputs, buttons, dropdown surfaces, calendar cells
- `12px`: cards, modals, command palettes
- `16px`: hero / feature cards, large modals
- `9999px` (pill): toggles, progress bars, status pills, avatars, dot indicators
- No mid-large values (20px, 24px) — the system caps at 16px for rectangular surfaces.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (0) | No shadow, no border | Body text, page canvas, sidebar regions |
| Hairline (1) | `1px solid #EAEAEA` only | Cards, inputs, table rows — separation without lift |
| Resting (2) | `0 1px 2px rgba(0,0,0,0.04)` + 1px border | Default cards, segmented controls |
| Raised (3) | `0 2px 4px rgba(0,0,0,0.06), 0 0 0 1px rgba(0,0,0,0.04)` + subtle gradient | Primary buttons, pricing cards on hover |
| Floating (4) | `0 8px 24px rgba(0,0,0,0.08), 0 0 0 1px rgba(0,0,0,0.04)` | Dropdowns, popovers, calendar |
| Modal (5) | `0 16px 48px rgba(0,0,0,0.12), 0 0 0 1px rgba(0,0,0,0.06)` | Command palette, modals, dialogs |
| Tooltip (Inverted) | `#0A0A0A` surface, no shadow needed | Tooltips floating over light UI |

**Shadow Philosophy**: HyperKit's elevation system is calibrated for screens, not paper. Every shadow is subtle — `rgba(0,0,0,0.04)` to `0.12)` opacities, never above 15% — and most floating surfaces also include a hairline `0 0 0 1px rgba(0,0,0,0.04)` ring that gives crisp definition under bright light. The result is that elements feel grounded but never theatrical. The visual focus stays on content, not chrome. The one exception is the primary button gradient, which deliberately reads as a discrete, "pressable" object — that pillowed Vercel-style CTA is the whole brand.

### Decorative Depth
- Cards rest one half-step above canvas — `#EAEAEA` border + `0 1px 2px rgba(0,0,0,0.04)`. That's it.
- Dropdowns and popovers escape with a 4–8x stronger shadow but maintain the 1px ring.
- No glow effects. No blur. No backdrop-filter saturation — the system is opaque-only.

## 7. Do's and Don'ts

### Do
- Default to Inter at 14px weight 400 for body — anything more interesting needs justification
- Use the three-weight ladder (400 / 500 / 600) — every weight outside this is an exception
- Pair the subtle button gradient with a 1px `rgba(0,0,0,0.04)` ring on primary CTAs — the pillow is the whole brand
- Carry status colors in tinted-fill + saturated-text pairs, never on backgrounds wider than a pill
- Use `1px solid #EAEAEA` borders before reaching for shadows — hairline first, lift second
- Stick to the radius ladder: 6px tags, 8px inputs/buttons, 12px cards, 9999px pills
- Use color (`#737373` vs `#0A0A0A`) to do hierarchy work before bumping weights
- Apply tabular numerals to every numeric column — pricing, tables, calendars, plan usage
- Rely on `#FAFAFA` panel fills to separate UI regions instead of more borders

### Don't
- Don't introduce a brand color — black is the accent, AI lavender is the only chromatic flourish
- Don't use Inter weight 700 or 300 — the ladder stops at 600 and starts at 400
- Don't use shadow opacities above 15% — `rgba(0,0,0,0.12)` is the ceiling, not the floor
- Don't add `border-radius: 20px` or higher on rectangular surfaces — 16px is the cap
- Don't run italic for emphasis — bump weight or color instead
- Don't tile status colors as full backgrounds — they live inside pills and dots only
- Don't use horizontal rule dividers (`<hr>`) — let card borders and surface shifts do the work
- Don't decorate with iconography larger than 20px in product UI — 16px Lucide-style is the default
- Don't use the gradient button treatment on secondary or ghost actions — it's primary-CTA only

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single column, hero drops to 32px, sidebar becomes drawer |
| Mobile | 375–640px | Single column, hero 36–40px, stacked CTAs, full-width buttons |
| Tablet | 640–1024px | 2-column starts, sidebar collapsible, hero 48–56px |
| Desktop | 1024–1440px | Full sidebar, 3-column pricing, hero 56–64px |
| Large Desktop | ≥1440px | 1280–1440px max content, hero 64–72px, generous gutters |

### Touch Targets
- Buttons: minimum 36px tall on desktop, 44px on mobile
- List rows in mobile views: minimum 48px tall
- Toggle/checkbox: 16px control inside a 32px tap target
- Sidebar items: 36px tall with 8px padding for thumb comfort

### Collapsing Strategy
- **Sidebar**: 240–280px desktop → off-canvas drawer on mobile, triggered by a 16px hamburger icon in the top nav
- **Pricing tiers**: 3-column equal-width → vertical stack on mobile, "Most popular" tier surfaces first
- **Tables**: Desktop tables collapse to card lists on mobile — each row becomes a vertical stack of label/value pairs
- **Top nav**: Full link bar collapses to logo + hamburger; CTA stays visible
- **Command palette**: Full-screen on mobile (bottom-sheet pattern), centered modal on desktop
- **Section padding**: 80–96px desktop → 48–64px tablet → 32–48px mobile

### Image Behavior
- Avatars maintain pixel size across breakpoints (24/32/40px)
- Product screenshots scale fluidly within bordered card frames — never break the chrome
- Empty-state illustrations stay at fixed 80–120px regardless of viewport
- Logo wordmark scales but never collapses to icon-only — the lightning glyph is part of the lockup

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Hyperkit Black gradient (`linear-gradient(180deg, #2C2C2C 0%, #000000 100%)`)
- Page Background: Hyperkit White (`#FFFFFF`)
- Sunken Panel: Off-Canvas (`#FAFAFA`)
- Primary Text: `#0A0A0A`
- Secondary Text: `#737373`
- Tertiary Text: `#A3A3A3`
- Default Border: `#EAEAEA`
- AI Accent: `#8B5CF6` (sparkle icons only)
- Resting Shadow: `0 1px 2px rgba(0,0,0,0.04)`
- Floating Shadow: `0 8px 24px rgba(0,0,0,0.08), 0 0 0 1px rgba(0,0,0,0.04)`

### Example Component Prompts
- "Create a primary CTA button — `linear-gradient(180deg, #2C2C2C 0%, #000 100%)` background, white Inter 14px weight 500 text, 10px 16px padding, 8px radius. Add `inset 0 1px 0 rgba(255,255,255,0.08)` for the inner top highlight and `0 1px 2px rgba(0,0,0,0.08), 0 0 0 1px rgba(0,0,0,0.04)` for the resting shadow + ring."
- "Build a pricing tier card on `#FFFFFF` with `1px solid #EAEAEA`, `12px` radius, and `0 1px 2px rgba(0,0,0,0.04)` shadow. Title in Inter 18px weight 600 (`#0A0A0A`), price in Inter 32px weight 600 with tabular numerals, feature list at 14px weight 400 (`#737373`) with 16px Lucide check icons."
- "Design a status pill — `#DCFCE7` background, `#16A34A` text, 12px Inter weight 500, 2px 8px padding, `9999px` radius. Lead with a 6px `#16A34A` dot."
- "Create a command palette — `#FFFFFF` surface with `12px` radius, `1px solid #EAEAEA`, `0 12px 32px rgba(0,0,0,0.10), 0 0 0 1px rgba(0,0,0,0.04)` shadow. Borderless 16px Inter input at top with magnifier icon, 36px-tall menu items below with 12px padding, `#F5F5F5` hover, trailing `⌘K`-style kbd badges in Geist Mono 12px on `#F5F5F5` with `1px solid #EAEAEA` and 4px radius."
- "Build a kanban column — `#FAFAFA` background with no border, 12px radius, 16px padding. Header: status pill (e.g. green Done) followed by count in Inter 14px weight 400 (`#737373`). Cards inside: `#FFFFFF`, `1px solid #EAEAEA`, 8px radius, 12px padding."
- "Style a calendar — 7-column grid of 36×36px day cells with 8px radius. Hover `#F5F5F5`, selected `#0A0A0A` with white text and tabular numerals. Today is `#F5F5F5` background no ring. Dimmed-month days at `#A3A3A3`. Header has 14px Inter weight 500 month label and ghost chevron buttons."

### Iteration Guide
1. Default to Inter 14px weight 400 (`#0A0A0A` body, `#737373` secondary) — change only with reason
2. Lock the weight ladder at 400 / 500 / 600. No 300, no 700, no italic — emphasis is weight + color
3. Reach for `1px solid #EAEAEA` before adding any shadow — hairline first, lift second
4. The pillowed gradient button is sacred — only on primary CTAs, never on secondary or ghost
5. Status colors live exclusively inside pills and dots — never as section backgrounds
6. Radius ladder: 4 (kbd) → 6 (tag/ghost) → 8 (input/button) → 12 (card) → 16 (hero) → 9999 (pill). Pick a step.
7. Use `#FAFAFA` panel fills to delineate UI regions; reserve borders for component edges
8. Tabular numerals on every numeric column — pricing, tables, calendars, dashboard counters
9. AI lavender (`#8B5CF6`) is the only chromatic accent — one sparkle icon per screen, max
10. Keep shadow opacities ≤12% — anything stronger reads as a different system entirely
