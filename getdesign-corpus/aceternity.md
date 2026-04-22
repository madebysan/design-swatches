# Design System Inspired by Aceternity UI

## 1. Visual Theme & Atmosphere

Aceternity UI is a design system built for **motion**. The homepage is a reel of animated components — Aurora backgrounds, 3D cards, text-generation effects, scroll-driven gradients — each demonstrating why Aceternity exists: to make Next.js landing pages look like they were shipped by a Cupertino design team at 4am. Dark canvas (`#09090b`) is the default, violet-to-pink gradients bleed through hero sections, and every interactive element ships with a framer-motion transition.

Typography is **Inter** — same as HeroUI — but used dramatically: weight 700 at 60px with `-1.5px` letter-spacing on a gradient-text fill, weight 500 at 48px for section heads, weight 400 for body. Aceternity doesn't innovate typographically; it innovates **presentationally**. Gradient text, outline text, blur effects, glow on hover — the typeface is a canvas for motion, not a voice of its own.

The distinctive radius system: **non-standard values** — `7.6px`, `9.6px`, `13.6px`. These are derived from Tailwind's arbitrary value syntax (`rounded-[9.6px]`) and compound through component composition. The result is a radius vocabulary that feels slightly off-standard — deliberately, calibrated to look premium rather than pre-made.

**Key Characteristics:**
- Dark-first (`#09090b`) with violet gradient accents — `#8b5cf6` → `#ec4899`
- Motion-driven: every component has framer-motion transitions built in
- Inter typeface with gradient-fill display treatments
- Non-standard radii (`7.6px`, `9.6px`, `13.6px`) — premium calibration
- Aurora, 3D cards, background beams, moving borders — the signature effects
- Built on Tailwind + Framer Motion + shadcn primitives underneath
- Pro tier unlocks advanced animations; free tier has the base components
- Dark mode IS the mode — light is derived, not primary

## 2. Color Palette & Roles

### Core Neutrals (dark-first)
- **Background** (`#09090b`): Primary canvas (zinc-950).
- **Surface** (`#18181b`): Card background (zinc-900).
- **Surface Elevated** (`#1c1c22`): Hover state.
- **Border** (`#27272a`): Hairline borders (zinc-800).
- **Foreground** (`#fafafa`): Primary text (zinc-50).
- **Muted Foreground** (`#a1a1aa`): Secondary text (zinc-400).
- **Disabled** (`#52525b`): Placeholder, disabled text.

### Accent Gradients (the signature)
- **Violet** (`#8b5cf6`): Primary accent (violet-500).
- **Pink** (`#ec4899`): Secondary accent (pink-500).
- **Blue** (`#3b82f6`): Tertiary accent (blue-500).
- **Aurora Gradient**: `linear-gradient(135deg, #8b5cf6 0%, #ec4899 50%, #3b82f6 100%)` — the house gradient.

### State Colors
- **Success** (`#22c55e`): Green (green-500).
- **Warning** (`#f59e0b`): Amber.
- **Error** (`#ef4444`): Red.

### Raw Color Distribution (from scan)
- `#09090b` appears 567 times — the canvas is truly dominant
- `#ffffff` appears 189 times as text/glyph color
- `#18181b` appears in hover states

## 3. Typography Rules

### Font Family
- **Primary**: `Inter`, fallback: `ui-sans-serif, system-ui, sans-serif`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, monospace`
- Aceternity often uses **`system-ui`** for smaller chrome elements — favors the native feel

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Hero | Inter | 60px | 700 | 1.00 | -1.5px |
| Display Large | Inter | 48px | 500 | 1.08 | -1.2px |
| H1 | Inter | 36px | 500 | 1.15 | -0.9px |
| H2 | Inter | 30px | 700 | 1.20 | -0.75px |
| H3 | Inter | 24px | 600 | 1.25 | -0.6px |
| Body Large | Inter | 18px | 400 | 1.56 | normal |
| Body | Inter | 16px | 400 | 1.50 | normal |
| Caption | ui-monospace | 12px | 500 | 1.40 | normal |

### Principles
- **Gradient fills at display**: Many hero titles use `background-clip: text` with Aurora gradient — the headline IS the brand color application.
- **Wide weight range**: 400, 500, 600, 700 all appear at display sizes — Aceternity uses weight as an expressive variable, not a hierarchy.
- **Negative tracking proportional to size**: -1.5px at 60px, -0.9px at 36px, -0.6px at 24px — progressive.
- **Monospace for captions**: 12px `ui-monospace` weight 500 is the branded small label treatment.

## 4. Component Stylings

### Buttons
- **Gradient**: Aurora gradient bg, white text, `7.6px` radius, `8px 20px` padding, 14px weight 500.
- **Moving Border**: Button with animated gradient-border (`background-clip` technique), transparent interior.
- **Ghost**: transparent, zinc-800 border, hover zinc-900 bg.

### Cards
- `#18181b` bg, `1px solid #27272a`, `13.6px` radius, `24px` padding.
- **3D Card**: Transforms on hover with perspective + translateZ
- **Spotlight Card**: Follows cursor with a radial gradient overlay
- **Glare Card**: CSS filter creates a moving glare effect

### Inputs
- `#18181b` bg, `1px solid #27272a`, `7.6px` radius, `8px 12px` padding.
- Focus: violet border with `0 0 0 2px rgba(139,92,246,0.3)` ring.

### Backgrounds (Aceternity's signature feature)
- **Aurora Background**: Animated gradient blobs behind content
- **Background Beams**: Animated line beams moving diagonally
- **Sparkles**: Dotted star particles with fade animations
- **Grid Pattern**: Subtle dot/grid SVG background
- **Vortex**: Conic gradient animation
- **Meteors**: Falling streak animations

### Badges / Chips
- `9999px` radius (pill), `2px 10px` padding, 12px weight 500.
- Gradient border: `1px` of gradient via `background-clip: padding-box`.

## 5. Layout Principles

### Spacing System
- Base unit: **4px**
- Dominant values: `16px` (243 uses — heavy), `8px` (84), `40px` (41), `32px` (19), `4px` (31)
- `16px` dominance suggests Aceternity's rhythm favors `4` at the small end and jumps to `16/24/32` for section breathing

### Grid
- 12-column Tailwind
- Max content width: `1280px`
- Hero sections: often full-bleed with max-width content inside
- Gutter: `24-32px` between sections

### Border Radius Scale
- Non-standard Tailwind arbitrary values define the system:
- `3px`: Small inline elements (kbd)
- `5.6px`: Small buttons, chips
- `7.6px`: Buttons, inputs — the workhorse (22 uses)
- `9.6px`: Cards, wider containers (35 uses)
- `13.6px`: Featured cards, heroes (53 uses — the signature)
- `9999px`: Pill shapes, avatars, badges

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | Background |
| Glow 1 | `0 0 20px rgba(139,92,246,0.1)` | Subtle brand glow |
| Glow 2 | `0 0 30px rgba(139,92,246,0.2)` | Hover lift |
| Glow 3 | `0 0 50px rgba(139,92,246,0.35), 0 0 80px rgba(236,72,153,0.2)` | Featured elements |
| Modal | `0 20px 60px rgba(0,0,0,0.8), 0 0 40px rgba(139,92,246,0.3)` | Dialogs |

**Shadow Philosophy**: Aceternity treats elevation as **atmospheric bloom** — gradient-tinted glows that emit from elements rather than cast shadows. This reads as premium/technological and masks the dark background beautifully. Motion-driven components often animate the glow intensity on hover/interaction — static elevation is a starting point, not the end state.

## 7. Do's and Don'ts

### Do
- Build every component with motion in mind — framer-motion is the dance partner
- Use Aurora gradients (violet → pink → blue) for hero accent moments
- Apply `background-clip: text` for gradient-filled display headlines
- Use non-standard radii (`7.6px`, `9.6px`, `13.6px`) — the off-standard look is intentional
- Pair dark canvas (`#09090b`) with brand glow shadows
- Use ui-monospace for 12px captions and technical labels

### Don't
- Don't strip motion — Aceternity without animation is Aceternity without personality
- Don't use flat solid colors for elevation — use gradient glows
- Don't use standard Tailwind radii (`0.5rem`, `0.75rem`) — break for the non-standard pixels
- Don't mix bright light-mode chrome with Aceternity components — design for dark first
- Don't use text-only buttons for primary CTAs — the gradient is the voice

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | Single column, reduced motion (media query) |
| md | `768px+` | 2-column grids, motion enabled |
| lg | `1024px+` | Full desktop, motion at full intensity |
| xl | `1280px+` | Max-width applies |

### Touch Targets
- Buttons: minimum `40px` height
- Animated components: disable transform-heavy animations on mobile (reduced motion media query)

### Collapsing Strategy
- Hero: 60px → 42px → 32px, gradient fill maintained
- 3D cards flatten on mobile (no perspective transforms)
- Aurora backgrounds simplify to static gradients on low-power devices
- Font weight variation collapses: keep 400 body, 700 display

## 9. Agent Prompt Guide

### Quick Color Reference
- Background: `#09090b` (zinc-950)
- Surface: `#18181b` (zinc-900)
- Border: `#27272a` (zinc-800)
- Text: `#fafafa` (primary), `#a1a1aa` (muted)
- Violet: `#8b5cf6`
- Pink: `#ec4899`
- Blue: `#3b82f6`
- Aurora: `linear-gradient(135deg, #8b5cf6, #ec4899, #3b82f6)`

### Example Component Prompts
- "Create a hero on #09090b with aurora gradient background (animated radial blobs of #8b5cf6, #ec4899, #3b82f6 at 25% alpha). Headline at 60px Inter weight 700 letter-spacing -1.5px, gradient text fill (background-clip: text). Subtitle 18px weight 400 color #a1a1aa. Gradient button: aurora bg, white text, 7.6px radius, 8px 20px padding, weight 500."
- "Design a card: #18181b bg, 1px solid #27272a, 13.6px radius, 24px padding, box-shadow 0 0 30px rgba(139,92,246,0.2). Title 20px Inter weight 600 color #fafafa. On hover: scale(1.02) and shadow intensifies to 0 0 50px rgba(139,92,246,0.35)."
- "Build a moving-border button: 40px height, 7.6px radius, transparent bg, 2px gradient border that animates around the perimeter (conic-gradient rotating 360deg). Interior: #18181b. Text: #fafafa 14px weight 500."

### Iteration Guide
1. Motion is the message — start with framer-motion, add static as fallback
2. Dark-first; light mode is a derivative theme
3. Use the non-standard radii (`7.6, 9.6, 13.6`) — they're intentional
4. Gradient glows (not drop shadows) for elevation
5. Aurora is the house gradient — violet → pink → blue at 135deg
6. `ui-monospace` at 12px weight 500 for technical captions/labels
