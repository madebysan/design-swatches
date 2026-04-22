# Design System Inspired by iOS Human Interface Guidelines

## 1. Visual Theme & Atmosphere

The iOS Human Interface Guidelines are Apple's design doctrine — the reference that governs what "iOS" looks like. The Apple Developer Documentation site serves as both reference and example: pure white canvas (`#ffffff`), Apple's specific near-black (`#1d1d1f`), System Blue (`#0071e3`) for interactive elements, and **SF Pro** — the typeface that defines Apple across iPhone, iPad, Mac, and Vision Pro. The aesthetic is restraint and deference: every pixel serves the content, every component borrowed from the system UI the user already knows.

Typography uses Apple's **SF Pro Display** for sizes 20px+ and **SF Pro Text** for sizes below 20px — a metric-matched family with optical-size-aware rendering. Weight 700 at 48px with tight `-0.144px` tracking for display. Body text at 17px weight 400 with subtle `-0.374px` tracking — the signature iOS body. Letter-spacing shifts from negative (`-0.374px` at body) to positive (`+0.216px` at 24px headings) depending on size — an unusual pattern that reflects SF's optical tuning.

The defining structural choice is **`18px` border-radius** as the dominant rounding (36 occurrences) — slightly larger than Material's 16px, much larger than shadcn's 10px. Combined with full-pill (`980px` in Apple's legacy notation, effectively `9999px`) for buttons, the system creates the soft, approachable iOS aesthetic. Colors are few: System Blue (`#0071e3`) as the one true brand, with system-defined red/green/amber/purple for semantic roles.

**Key Characteristics:**
- SF Pro Display (20px+) and SF Pro Text (<20px) — metric-matched, optical-size aware
- System Blue (`#0071e3`) as the singular brand anchor — `--sk-focus-color`
- `18px` dominant radius — the softened-card iOS signature (36 uses)
- Full-pill buttons (`980px` radius) — Apple's historical pill notation
- Mixed letter-spacing: negative at body (`-0.374px`), positive at headings (`+0.216px`)
- Restrained shadows: `0 4px 24px rgba(0,0,0,0.08)` only on cards, never on chrome
- SF Symbols for iconography — Apple's variable icon font
- Defers to system colors when possible — systemBlue, systemGreen, systemRed

## 2. Color Palette & Roles

### System Colors (Semantic)
- **System Blue** (`#0071e3`): Primary interactive — `--sk-focus-color`. Links, buttons, active states.
- **System Red** (`#ff3b30`): Destructive — delete, error.
- **System Green** (`#34c759`): Positive — success, go.
- **System Orange** (`#ff9500`): Warning, caution.
- **System Yellow** (`#ffcc00`): Attention.
- **System Pink** (`#ff2d55`): Tertiary accent, occasionally interactive.
- **System Purple** (`#af52de`): Creative, Photos accent.
- **System Teal** (`#5ac8fa`): Info, Apple TV accent.
- **System Indigo** (`#5856d6`): Alternative blue for differentiation.

### Gray Scale (System Gray)
- **System Gray 6** (`#f2f2f7`): Lightest — secondary backgrounds.
- **System Gray 5** (`#e5e5ea`): Tertiary.
- **System Gray 4** (`#d1d1d6`): Quaternary.
- **System Gray 3** (`#c7c7cc`): Separator — borders.
- **System Gray 2** (`#aeaeb2`): Placeholder.
- **System Gray** (`#8e8e93`): Secondary label.
- **System Gray (alt)** (`#515154`): Body chrome (162 occurrences).

### Label Colors
- **Label** (`#1d1d1f`): Primary label — Apple's specific dark.
- **Secondary Label** (`#515154`): Captions, muted text.
- **Tertiary Label** (`#424245`): Further muted.
- **Quaternary Label** (`#c7c7cc`): Disabled.

### Background
- **System Background** (`#ffffff`): Primary canvas.
- **System Background Secondary** (`#f5f5f7`): Grouped lists, table sections.
- **System Background Tertiary** (`#ffffff`): Nested content inside secondary.

## 3. Typography Rules

### Font Family
- **Display** (20px+): `SF Pro Display` — fallback `-apple-system, BlinkMacSystemFont, "Helvetica Neue"`
- **Text** (below 20px): `SF Pro Text` — fallback `-apple-system, BlinkMacSystemFont, "Helvetica Neue"`
- **Rounded** (display): `SF Pro Rounded` — used for accent headlines, Memoji labels
- **Mono**: `SF Mono` — fallback `ui-monospace, Menlo, monospace`
- **Web fallback**: `Inter` is often used as a web approximation since SF Pro requires Apple's font license

### Hierarchy (iOS Text Styles)

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Large Title | SF Pro Display | 34px | 700 | 1.21 | +0.374px |
| Title 1 | SF Pro Display | 28px | 700 | 1.21 | +0.364px |
| Title 2 | SF Pro Display | 22px | 700 | 1.27 | +0.352px |
| Title 3 | SF Pro Display | 20px | 600 | 1.25 | +0.38px |
| Headline | SF Pro Text | 17px | 600 | 1.29 | -0.374px |
| Body | SF Pro Text | 17px | 400 | 1.29 | -0.374px |
| Callout | SF Pro Text | 16px | 400 | 1.31 | -0.24px |
| Subhead | SF Pro Text | 15px | 400 | 1.33 | -0.24px |
| Footnote | SF Pro Text | 13px | 400 | 1.38 | -0.078px |
| Caption 1 | SF Pro Text | 12px | 400 | 1.33 | 0 |
| Caption 2 | SF Pro Text | 11px | 400 | 1.36 | +0.066px |

### Principles
- **Mixed letter-spacing**: Display sizes use POSITIVE tracking (`+0.374px`), body sizes use NEGATIVE tracking (`-0.374px`). This is counter-intuitive but reflects SF's optical tuning.
- **SF Display vs SF Text threshold at 20px**: Apple's automatic swap — SF Pro Display is drawn for large sizes, SF Pro Text for small.
- **Weight 700 at Large Title**: Apple reserves weight 700 for Large Title (navigation-scroll-expandable); standard headlines use weight 600.
- **Body at 17px is the reference size**: iOS's default body text, with `-0.374px` tracking as the signature.

## 4. Component Stylings

### Buttons
- **Filled (Primary)**: `#0071e3` bg, white text, `980px` radius (full pill — Apple's notation), `8px 20px` padding, 17px SF Pro Text weight 400.
- **Tinted**: `rgba(0,113,227,0.15)` bg, `#0071e3` text, `980px` radius.
- **Plain**: no bg, `#0071e3` text, no padding.
- **Gray**: `rgba(120,120,128,0.16)` bg, `#1d1d1f` text, `980px` radius.
- **Destructive**: `#ff3b30` variants.

### Cards / Lists
- `#ffffff` bg, `18px` radius, no border, shadow: `0 4px 24px rgba(0,0,0,0.08)`.
- **Grouped table**: `#f5f5f7` outer bg, `#ffffff` inner cards with `10-14px` radius.
- Apple uses "insets" heavily — cards have internal borders separating rows.

### Inputs (Text Field)
- `#f5f5f7` bg, no visible border, `10-12px` radius, `11px 16px` padding.
- Focus: `2px solid #0071e3` outer ring, internal bg turns `#ffffff`.

### Switches
- Track: `#e5e5ea` (off) → `#34c759` (on), `31px` height, `51px` wide
- Thumb: `27px` white circle, subtle shadow
- Radius: fully round (`9999px`)

### Navigation (Large Title)
- Top bar transitions from 96px tall (expanded Large Title) to 44px tall (collapsed Title 1) on scroll.
- Large Title in SF Pro Display weight 700 at 34px with `+0.374px` tracking.

## 5. Layout Principles

### Spacing System
- Base unit: **4pt** (rendered as px on web)
- Dominant values: `7px` (116 uses — unusual), `9px` (34), `2px` (18), `4px` (17), `5px` (18), `1px` (13)
- The `7px` prevalence is distinct — Apple's web docs use fine-grained vertical rhythm

### Grid
- Safe area insets determine layout — `16pt` margins on compact, `24pt` on regular
- Max content width on web docs: `980px` (reading), `1392px` (full layout)
- Navigation: `44pt` standard, `96pt` with Large Title

### Border Radius Scale
- Sharp (`5-6px`): Kbd, chips (4-7 uses)
- Medium (`10-12px`): Text fields, small cards
- Large (`18px`): Primary cards — the workhorse (36 uses)
- Pill (`980px` or `9999px`): Buttons, badges, search bars

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | None | Cards default |
| Subtle | `0 1px 3px rgba(0,0,0,0.04)` | Card rest |
| Card | `0 4px 24px rgba(0,0,0,0.08)` | Floating card |
| Popover | `0 8px 32px rgba(0,0,0,0.12)` | Popovers, action sheets |
| Modal | `0 16px 48px rgba(0,0,0,0.2)` | Modal dialogs |

**Shadow Philosophy**: iOS uses soft, diffused shadows — large offsets, high blur, low opacity. Rather than crisp layered shadows (like Stripe or Material), iOS shadows suggest thin floating glass. Apple's native UI also leans heavily on **materials** — translucent vibrancy effects that blur and tint content underneath — but those are system-level effects the web HIG recreates via `backdrop-filter: blur()`.

## 7. Do's and Don'ts

### Do
- Use SF Pro Display for 20px+ sizes and SF Pro Text for smaller — respect the metric split
- Use POSITIVE letter-spacing on display headings (`+0.216-0.374px`)
- Use NEGATIVE letter-spacing on body text (`-0.374px` at 17px)
- Apply `18px` radius to cards, `980px` (pill) to buttons
- Use System Blue (`#0071e3`) sparingly — it's the singular interactive color
- Apply soft diffused shadows (`0 4px 24px rgba(0,0,0,0.08)`)
- Use SF Symbols for iconography — variable axes (weight, fill, grade, opsz)

### Don't
- Don't use Inter or Roboto as primary — use SF Pro via `-apple-system` or fallback
- Don't use sharp corners — iOS is categorically rounded
- Don't use colored brand colors beyond System Blue — rely on system semantic colors
- Don't mix letter-spacing direction — Display positive, Text negative, consistent by size
- Don't override system dark mode behaviors — respect user preference
- Don't use layered multi-shadow systems — iOS is single-layer soft shadow

## 8. Responsive Behavior

### Breakpoints (iOS size classes)
| Class | Width | Changes |
|------|-------|---------|
| Compact W | `<414pt` | iPhone portrait, single-column, bottom tab bar |
| Regular W | `>414pt` | iPhone landscape / iPad, master-detail |
| Compact H | `<568pt` | iPhone landscape |
| Regular H | `>568pt` | Standard portrait orientation |

### Touch Targets
- **Minimum 44pt × 44pt** — Apple's strict accessibility floor
- Buttons: `44pt` default, scales to `50pt` for prominent CTAs
- Navigation links: `44pt` minimum with padding

### Collapsing Strategy
- Large Title: 34px → 28px on scroll (navigation collapse animation)
- Lists: grouped-table → single-column inset list on compact
- Modals: full-screen on compact, centered card on regular
- Split views: side-by-side on regular, stack on compact

## 9. Agent Prompt Guide

### Quick Color Reference
- System Blue: `#0071e3`
- Label: `#1d1d1f`
- Secondary Label: `#515154`
- Tertiary Label: `#424245`
- Separator: `#d2d2d7`
- System Background: `#ffffff`
- Secondary Background: `#f5f5f7`
- System Red: `#ff3b30`
- System Green: `#34c759`

### Example Component Prompts
- "Create a large title navigation: 96pt tall at rest, #ffffff bg. Title 34px SF Pro Display weight 700, letter-spacing +0.374px, color #1d1d1f. On scroll, collapses to 44pt with Title 1 (20px weight 600) centered. Back button in System Blue."
- "Design a grouped list: #f5f5f7 outer bg, 16pt padding. Inset cards #ffffff bg, 18px radius, shadow 0 4px 24px rgba(0,0,0,0.08). Row title 17px SF Pro Text weight 400, letter-spacing -0.374px, color #1d1d1f. Chevron 12px System Gray."
- "Build a pill button: #0071e3 bg, white text, 980px radius (full pill), 8px 20px padding, 17px SF Pro Text weight 400. Press state: 85% opacity. Disabled: System Gray 4 (#d1d1d6) bg."

### Iteration Guide
1. SF Pro Display above 20px, SF Pro Text below — the metric split matters
2. Positive letter-spacing at display, negative at body — iOS inverts the norm
3. `18px` radius on cards is the iOS signature; `980px` on buttons
4. System Blue is the only brand color — everything else is system-defined
5. Soft single-layer shadows (`0 4px 24px` at 8% opacity)
6. Respect native dark mode — don't override user system preferences
