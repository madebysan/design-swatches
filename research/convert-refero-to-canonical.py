#!/usr/bin/env python3
"""Mechanically convert a refero rich .md into the canonical 9-section DESIGN.md format.

Input:  research/refero-data/{slug}.md (refero shape)
Output: research/refero-converted/{slug}.md (canonical shape)

This is a structural pass — sections get renamed, reordered, and reshaped.
It does NOT rewrite voice. The result is structurally compliant with the
canonical format but reads more spec-like than the hand-written corpus.
"""
import re
import sys
from pathlib import Path

RESEARCH = Path("/Users/san/Projects/_done/design-swatches/research")
SRC = RESEARCH / "refero-data"
DEST = RESEARCH / "refero-converted"
DEST.mkdir(parents=True, exist_ok=True)

# refero industry -> canonical category
INDUSTRY_TO_CATEGORY = {
    "ai": "AI Lab",
    "agency": "Agency",
    "design": "Design Studio",
    "portfolio": "Portfolio",
    "saas": "SaaS",
    "tech": "SaaS",
    "ecommerce": "Ecommerce",
    "shopify": "Ecommerce",
    "editorial": "Editorial",
    "publication": "Editorial",
    "magazine": "Editorial",
    "music": "Music",
    "type-foundry": "Type Foundry",
    "typography": "Type Foundry",
    "fintech": "Fintech",
    "developer-tools": "Developer Tools",
    "devtools": "Developer Tools",
    "productivity": "Productivity",
    "fashion": "Fashion",
    "lifestyle": "Lifestyle",
    "food": "Food & Beverage",
    "beverage": "Food & Beverage",
    "travel": "Travel",
    "wellness": "Wellness",
    "beauty": "Beauty",
    "education": "Education",
    "media": "Media",
    "news": "News",
    "non-profit": "Non-profit",
    "sports": "Sports",
    "gaming": "Gaming",
    "fitness": "Fitness",
    "automotive": "Automotive",
    "real-estate": "Real Estate",
    "finance": "Finance",
}


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body) from a markdown file."""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    fm_raw, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_raw.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    return fm, body


def split_sections(body: str) -> dict[str, str]:
    """Split markdown body by `## ` headings into a dict {heading: content}."""
    sections = {}
    current = "PREAMBLE"
    buf: list[str] = []
    for line in body.splitlines():
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            sections[current] = "\n".join(buf).strip()
            current = m.group(1).strip()
            buf = []
        else:
            buf.append(line)
    sections[current] = "\n".join(buf).strip()
    return sections


def parse_color_table(colors_md: str) -> list[dict]:
    """Parse refero's `| Name | Hex | Role | Group |` table."""
    rows = []
    for line in colors_md.splitlines():
        line = line.strip()
        if not line.startswith("|") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4 or cells[0].lower() == "name":
            continue
        rows.append({
            "name": cells[0],
            "hex": cells[1].strip("`"),
            "role": cells[2],
            "group": cells[3],
        })
    return rows


def emit_color_palette(colors: list[dict]) -> str:
    """Group colors by 'group' and emit canonical-style bulleted lists."""
    if not colors:
        return "_(No color data extracted.)_\n"
    groups: dict[str, list[dict]] = {}
    for c in colors:
        groups.setdefault(c["group"] or "neutral", []).append(c)
    out = []
    group_titles = {
        "neutral": "Core Neutrals",
        "accent": "Accent Colors",
        "primary": "Primary",
        "secondary": "Secondary",
        "state": "State Colors",
        "brand": "Brand Colors",
        "semantic": "State Colors",
    }
    for grp, items in groups.items():
        title = group_titles.get(grp.lower(), grp.title())
        out.append(f"### {title}")
        for c in items:
            role_short = c["role"].split(".")[0].split(",")[0].strip()
            if role_short:
                out.append(f"- **{c['name']}** (`{c['hex']}`): {role_short}.")
            else:
                out.append(f"- **{c['name']}** (`{c['hex']}`)")
        out.append("")
    return "\n".join(out)


def emit_typography_table(typo_md: str) -> str:
    """Convert refero's per-family typography blocks + Type Scale into canonical format."""
    families = []
    cur = None
    in_type_scale = False
    for line in typo_md.splitlines():
        m = re.match(r"^###\s+(.+?)(?:\s+_\(substitute:\s*(.+?)\)_)?$", line.strip())
        if m:
            heading = m.group(1).strip()
            if heading.lower() == "type scale":
                if cur:
                    families.append(cur)
                    cur = None
                in_type_scale = True
                continue
            in_type_scale = False
            if cur:
                families.append(cur)
            cur = {"name": heading, "substitute": (m.group(2) or "").strip(), "role": "", "specs": {}}
            continue
        if in_type_scale:
            continue
        if cur is None:
            continue
        rm = re.match(r"^\*\*Role:\*\*\s+(.+)$", line.strip())
        if rm:
            cur["role"] = rm.group(1).strip()
            continue
        sm = re.match(r"^-\s+\*\*(.+?):\*\*\s+(.+)$", line.strip())
        if sm:
            cur["specs"][sm.group(1).strip().lower()] = sm.group(2).strip()
    if cur:
        families.append(cur)

    # Type Scale rows
    scale_rows = []
    for line in typo_md.splitlines():
        if not line.strip().startswith("- "):
            continue
        parts = re.findall(r"`([^`]+)`", line)
        row = {}
        for p in parts:
            if ":" in p:
                k, _, v = p.partition(":")
                row[k.strip()] = v.strip()
        if row:
            scale_rows.append(row)

    out = ["### Font Families"]
    for f in families:
        sub = f" (substitute: {f['substitute']})" if f["substitute"] else ""
        out.append(f"- **{f['name']}**{sub}: {f['role']}")
    out.append("")

    if scale_rows:
        out.append("### Hierarchy")
        out.append("")
        out.append("| Role | Size | Line Height | Letter Spacing |")
        out.append("|------|------|-------------|----------------|")
        for r in scale_rows:
            role = r.get("role", "")
            size = r.get("size", "")
            lh = r.get("lineHeight") or r.get("lineheight", "")
            ls = r.get("letterSpacing") or r.get("letterspacing", "")
            out.append(f"| {role} | {size}px | {lh} | {ls or 'normal'} |")
        out.append("")

    return "\n".join(out)


def parse_inline_dict(s: str) -> dict | None:
    """Parse `{'cards': '8px', 'badges': '0px'}` -> dict. Returns None if not a dict literal."""
    s = s.strip()
    if not (s.startswith("{") and s.endswith("}")):
        return None
    try:
        import ast
        return ast.literal_eval(s)
    except (ValueError, SyntaxError):
        return None


def emit_layout(layout_md: str, spacing_md: str) -> str:
    """Combine refero Layout (prose) + Spacing (key/value) into canonical Layout Principles."""
    out = []
    radius_dict = None
    spacing_pairs = []
    if spacing_md:
        for line in spacing_md.splitlines():
            line = line.strip()
            m = re.match(r"^-\s+\*\*(.+?):\*\*\s+(.+)$", line)
            if not m:
                continue
            k, v = m.group(1), m.group(2)
            if k.lower() == "radius":
                d = parse_inline_dict(v)
                if d:
                    radius_dict = d
                    continue
            spacing_pairs.append((k, v))

    if spacing_pairs:
        out.append("### Spacing System")
        out.append("")
        for k, v in spacing_pairs:
            out.append(f"- **{k}**: {v}")
        out.append("")

    if radius_dict:
        out.append("### Border Radius Scale")
        out.append("")
        for k, v in radius_dict.items():
            out.append(f"- **{k}**: `{v}`")
        out.append("")

    if layout_md:
        out.append("### Layout & Composition")
        out.append("")
        out.append(layout_md.strip())
        out.append("")
    return "\n".join(out)


def emit_elevation(surfaces_md: str, elevation_md: str) -> str:
    """Build a minimal elevation section from refero surfaces / elevation if present."""
    out = []
    if surfaces_md:
        out.append("### Surface Levels")
        out.append("")
        for line in surfaces_md.splitlines():
            line = line.strip()
            if line.startswith("- "):
                out.append(line)
        out.append("")
    if elevation_md:
        out.append("### Elevation")
        out.append("")
        out.append(elevation_md.strip())
        out.append("")
    if not out:
        out = ["_(No explicit elevation system documented; refero brands often rely on surface contrast and borders rather than shadows.)_\n"]
    return "\n".join(out)


def emit_components(components_md: str) -> str:
    """Pass refero's named-tile components through; canonical format prefers type-grouped components but mechanical conversion can't re-bucket without an LLM. Keep as-is with H3 titles intact."""
    if not components_md:
        return "_(No component data extracted.)_\n"
    return components_md.strip() + "\n"


def emit_dos_donts(dos_md: str, donts_md: str) -> str:
    out = []
    if dos_md:
        out.append("### Do")
        out.append("")
        out.append(dos_md.strip())
        out.append("")
    if donts_md:
        out.append("### Don't")
        out.append("")
        out.append(donts_md.strip())
        out.append("")
    return "\n".join(out)


def derive_category(industry: str) -> str:
    return INDUSTRY_TO_CATEGORY.get((industry or "").lower(), industry.title() if industry else "Other")


def derive_styles(theme: str, body_text: str) -> list[str]:
    """Derive styles[] from theme + simple keyword scan over the overview."""
    styles = []
    if theme.lower() == "dark":
        styles.append("Dark")
    elif theme.lower() == "light":
        styles.append("Light")
    keywords = {
        "Editorial": ["editorial", "broadsheet", "research journal", "magazine"],
        "Minimalist": ["minimal", "restraint", "stripped"],
        "Bold": ["bold", "high-contrast", "dramatic"],
        "Brutalist": ["brutalist", "raw", "industrial"],
        "Gradient": ["gradient", "aurora", "blur"],
        "Monochromatic": ["monochrome", "achromatic", "monochromatic"],
        "Warm": ["warm", "ivory", "parchment", "terracotta", "earthy"],
        "Cool": ["cool", "slate", "icy", "cyan"],
        "Playful": ["playful", "whimsical", "rounded"],
    }
    lower = body_text.lower()
    for label, words in keywords.items():
        if any(w in lower for w in words) and label not in styles:
            styles.append(label)
        if len(styles) >= 4:
            break
    return styles


def convert(slug: str) -> str:
    src_path = SRC / f"{slug}.md"
    text = src_path.read_text()
    fm, body = parse_frontmatter(text)
    sections = split_sections(body)

    name = fm.get("name", slug)
    url = fm.get("url", "")
    domain = fm.get("domain", "")
    tagline = fm.get("tagline", "").strip().strip('"')
    fonts_raw = fm.get("fonts", "[]")
    primary_color = fm.get("primary_color", "").strip().strip('"')
    theme = fm.get("theme", "")
    industry = fm.get("industry", "")

    overview = sections.get("Overview", "").strip()
    category = derive_category(industry)
    styles = derive_styles(theme, overview)

    # Canonical frontmatter
    out_fm = ["---"]
    out_fm.append(f"slug: {slug}")
    out_fm.append(f"name: {name}")
    out_fm.append(f"url: {url}")
    out_fm.append(f"domain: {domain}")
    out_fm.append(f"category: {category}")
    out_fm.append(f"styles: [{', '.join(styles) if styles else 'Light'}]")
    out_fm.append(f'tagline: "{tagline}"')
    out_fm.append(f"fonts: {fonts_raw}")
    if primary_color and primary_color != "null":
        out_fm.append(f'primary_color: "{primary_color}"')
    else:
        out_fm.append("primary_color: null")
    out_fm.append("---")
    out_fm.append("")

    # Body
    body_out = [f"# Design System Inspired by {name}", "", f"> {tagline}", ""]

    # 1. Visual Theme & Atmosphere
    body_out.append("## 1. Visual Theme & Atmosphere")
    body_out.append("")
    body_out.append(overview if overview else f"_({name} — visual theme analysis pending.)_")
    body_out.append("")
    # Pull a bullet list of "Key Characteristics" from refero's first sentence + tagline
    chars = []
    if primary_color:
        chars.append(f"Primary anchor color: `{primary_color}`")
    if theme:
        chars.append(f"Theme: {theme}")
    fonts_clean = re.findall(r"[A-Za-z][A-Za-z0-9 .'-]+", fonts_raw)
    if fonts_clean:
        chars.append(f"Typeface set: {', '.join(fonts_clean[:3])}")
    if chars:
        body_out.append("**Key Characteristics:**")
        for c in chars:
            body_out.append(f"- {c}")
        body_out.append("")

    # 2. Color Palette & Roles
    body_out.append("## 2. Color Palette & Roles")
    body_out.append("")
    colors = parse_color_table(sections.get("Colors", ""))
    body_out.append(emit_color_palette(colors))

    # 3. Typography Rules
    body_out.append("## 3. Typography Rules")
    body_out.append("")
    body_out.append(emit_typography_table(sections.get("Typography", "")))

    # 4. Component Stylings
    body_out.append("## 4. Component Stylings")
    body_out.append("")
    body_out.append(emit_components(sections.get("Components", "")))

    # 5. Layout Principles
    body_out.append("## 5. Layout Principles")
    body_out.append("")
    body_out.append(emit_layout(sections.get("Layout", ""), sections.get("Spacing", "")))

    # 6. Depth & Elevation
    body_out.append("## 6. Depth & Elevation")
    body_out.append("")
    body_out.append(emit_elevation(sections.get("Surfaces", ""), sections.get("Elevation", "")))

    # 7. Do's and Don'ts
    body_out.append("## 7. Do's and Don'ts")
    body_out.append("")
    body_out.append(emit_dos_donts(sections.get("Do's", ""), sections.get("Don'ts", "")))

    # 8. Responsive Behavior — refero doesn't capture this; emit placeholder
    body_out.append("## 8. Responsive Behavior")
    body_out.append("")
    body_out.append("_(Responsive specs not captured by source extraction. Defaults: mobile single-column, md (768px+) two-column, lg (1024px+) full-width composition; touch targets ≥40px; reduce motion at low-power.)_")
    body_out.append("")

    # 9. Agent Prompt Guide
    body_out.append("## 9. Agent Prompt Guide")
    body_out.append("")
    apg = sections.get("Agent Prompt Guide", "").strip()
    body_out.append(apg if apg else "_(No agent guide extracted.)_")
    body_out.append("")

    # Surface any extra refero sections that didn't map
    extras = []
    keep_known = {"PREAMBLE", "Overview", "Colors", "Typography", "Components", "Layout",
                  "Spacing", "Surfaces", "Elevation", "Imagery", "Do's", "Don'ts",
                  "Agent Prompt Guide", "Preview"}
    for k, v in sections.items():
        if k not in keep_known and v.strip():
            extras.append((k, v))
    if sections.get("Imagery", "").strip():
        body_out.append("## Imagery (refero supplemental)")
        body_out.append("")
        body_out.append(sections["Imagery"].strip())
        body_out.append("")
    for k, v in extras:
        body_out.append(f"## {k} (refero supplemental)")
        body_out.append("")
        body_out.append(v.strip())
        body_out.append("")

    # Preview
    if sections.get("Preview", "").strip():
        body_out.append("## Preview")
        body_out.append("")
        body_out.append(sections["Preview"].strip())
        body_out.append("")

    return "\n".join(out_fm) + "\n".join(body_out).rstrip() + "\n"


def main():
    slugs = sys.argv[1:] if len(sys.argv) > 1 else [
        "anthropic", "ableton", "adidas", "allbirds", "asana",
        "astro", "1password", "atlassian", "apollo", "arcade",
    ]
    for slug in slugs:
        try:
            md = convert(slug)
            out = DEST / f"{slug}.md"
            out.write_text(md)
            kb = len(md) // 1024
            print(f"✓ {slug:<15} → {out.name} ({kb}KB)")
        except FileNotFoundError:
            print(f"✗ {slug}: source missing in refero-data/")
        except Exception as e:
            print(f"✗ {slug}: {e}")


if __name__ == "__main__":
    main()
