#!/usr/bin/env python3
"""Fetch /api/styles/{id} for every NEW refero entry and convert each
designSystem object to a rich DESIGN.md.

Replaces the thin .md files written by build-refero-mds.py with the full
extended-format content refero shows on each detail page.

- Resume-safe: skips entries where {slug}-detail.json already exists.
- Polite: jitter delay 0.6-1.4s between calls.
- Mechanical: pure JSON-to-markdown formatting, no LLM.
"""
import json
import re
import time
import random
import urllib.request
import urllib.error
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path("/Users/san/Projects/_done/design-swatches")
SRC = ROOT / "research" / "refero-styles.json"
DEST = ROOT / "research" / "refero-data"
DEST.mkdir(parents=True, exist_ok=True)

domains = json.loads((ROOT / "explorer/shared/brand-domains.json").read_text())


def normalize_domain(url: str) -> str:
    try:
        d = urlparse(url).netloc.lower()
        return re.sub(r"^www\.", "", d)
    except Exception:
        return ""


sans_domains = {normalize_domain("http://" + d): slug for slug, d in domains.items()}

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"


def slugify(name: str, url: str) -> str:
    base = name.strip()
    base = re.sub(r"&", "and", base)
    base = re.sub(r"['']", "", base)
    base = re.sub(r"[^\w\s.-]", "", base)
    base = re.sub(r"\s+", "-", base).lower()
    base = re.sub(r"\.com$|\.dev$|\.io$|\.app$", "", base)
    base = re.sub(r"-+", "-", base).strip("-")
    if not base or base in {"www", "the", "an", "a"}:
        d = normalize_domain(url)
        base = d.split(".")[0] if d else "unknown"
    return base[:60]


def fetch_detail(style_id: str) -> dict:
    url = f"https://styles.refero.design/api/styles/{style_id}"
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def fmt_colors(colors: list) -> str:
    if not colors:
        return ""
    out = ["## Colors", "", "| Name | Hex | Role | Group |", "|------|-----|------|-------|"]
    for c in colors:
        n = c.get("name", "")
        h = c.get("hex", "")
        r = (c.get("role") or "").replace("|", "\\|")
        g = c.get("group", "")
        out.append(f"| {n} | `{h}` | {r} | {g} |")
    out.append("")
    return "\n".join(out)


def fmt_typography(typography: list, type_scale: list) -> str:
    out = []
    if typography:
        out.extend(["## Typography", ""])
        for t in typography:
            family = t.get("family", "")
            sub = t.get("substitute", "")
            role = (t.get("role") or "").strip()
            sizes = t.get("sizes", "")
            weights = t.get("weight") or ", ".join(str(w) for w in (t.get("weights") or []))
            lh = t.get("lineHeight", "")
            ls = t.get("letterSpacing", "")
            out.append(f"### {family}" + (f" _(substitute: {sub})_" if sub else ""))
            out.append("")
            if role:
                out.append(f"**Role:** {role}")
                out.append("")
            specs = []
            if sizes: specs.append(f"**Sizes:** {sizes}")
            if weights: specs.append(f"**Weights:** {weights}")
            if lh: specs.append(f"**Line height:** {lh}")
            if ls: specs.append(f"**Letter spacing:** {ls}")
            for s in specs:
                out.append("- " + s)
            out.append("")
    if type_scale:
        out.extend(["### Type Scale", ""])
        for s in type_scale:
            if isinstance(s, dict):
                bits = [f"`{k}: {v}`" for k, v in s.items() if k and v not in (None, "")]
                out.append("- " + " · ".join(bits))
            else:
                out.append(f"- {s}")
        out.append("")
    return "\n".join(out)


def fmt_components(components: list) -> str:
    if not components:
        return ""
    out = ["## Components", ""]
    for c in components:
        name = c.get("name", "Component")
        role = (c.get("role") or "").strip()
        desc = (c.get("description") or "").strip()
        out.append(f"### {name}")
        out.append("")
        if role: out.append(f"**Role:** {role}\n")
        if desc: out.append(f"{desc}\n")
    return "\n".join(out)


def fmt_section(title: str, value) -> str:
    if not value:
        return ""
    if isinstance(value, str):
        return f"## {title}\n\n{value.strip()}\n"
    if isinstance(value, dict):
        out = [f"## {title}", ""]
        for k, v in value.items():
            out.append(f"- **{k}:** {v}")
        return "\n".join(out) + "\n"
    if isinstance(value, list):
        out = [f"## {title}", ""]
        for v in value:
            if isinstance(v, dict):
                bits = [f"`{k}: {vv}`" for k, vv in v.items() if vv not in (None, "")]
                out.append("- " + " · ".join(bits))
            else:
                out.append(f"- {v}")
        return "\n".join(out) + "\n"
    return ""


def fmt_dos_donts(dos: list, donts: list) -> str:
    out = []
    if dos:
        out.extend(["## Do's", ""])
        for d in dos: out.append(f"- {d}")
        out.append("")
    if donts:
        out.extend(["## Don'ts", ""])
        for d in donts: out.append(f"- {d}")
        out.append("")
    return "\n".join(out)


def fmt_custom_sections(sections: list) -> str:
    out = []
    for s in sections or []:
        title = s.get("title") or s.get("name") or "Section"
        content = s.get("content") or s.get("body") or ""
        out.append(f"## {title}")
        out.append("")
        out.append(content.strip())
        out.append("")
    return "\n".join(out)


def to_markdown(slug: str, list_entry: dict, detail: dict) -> str:
    style = detail["style"]
    ds = (style.get("fullResult") or {}).get("designSystem") or {}

    site_name = style.get("siteName", list_entry.get("siteName", ""))
    url = style.get("url", list_entry.get("url", ""))
    domain = normalize_domain(url)
    refero_id = style.get("id", list_entry.get("id"))
    refero_url = f"https://styles.refero.design/style/{refero_id}"

    description = (ds.get("description") or "").strip().replace('"', "'")
    north_star = (ds.get("northStar") or "").strip().replace('"', "'")
    theme = ds.get("theme", style.get("colorScheme", ""))
    industry = ds.get("industry", style.get("industry", ""))

    # primary color: prefer first chromatic color, fallback first
    colors = ds.get("colors") or list_entry.get("colors") or []
    def is_chromatic(hexv):
        h = (hexv or "").lstrip("#").lower()
        if len(h) == 3: h = "".join(c*2 for c in h)
        if len(h) != 6: return False
        try:
            r,g,b = int(h[:2],16), int(h[2:4],16), int(h[4:6],16)
        except: return False
        return (max(r,g,b) - min(r,g,b)) >= 16
    primary_hex = None
    for c in colors:
        if is_chromatic(c.get("hex","")):
            primary_hex = c["hex"]; break
    if not primary_hex and colors:
        primary_hex = colors[0].get("hex")

    fonts = []
    seen = set()
    for t in (ds.get("typography") or []):
        f = t.get("family")
        if f and f.lower() not in seen:
            fonts.append(f); seen.add(f.lower())
    if not fonts:
        fonts = list_entry.get("fonts") or []

    fonts_yaml = "[" + ", ".join(fonts) + "]" if fonts else "[]"

    # Frontmatter
    fm = [
        "---",
        f"slug: {slug}",
        f"name: {site_name}",
        f"url: {url}",
        f"domain: {domain}",
        f"source: refero",
        f"refero_id: {refero_id}",
        f"theme: {theme}",
    ]
    if industry: fm.append(f"industry: {industry}")
    fm.append(f'tagline: "{north_star}"')
    fm.append(f"fonts: {fonts_yaml}")
    fm.append(f'primary_color: "{primary_hex}"' if primary_hex else "primary_color: null")
    fm.append("---")
    fm.append("")

    body = [
        f"# {site_name} — Style Reference",
        "",
        f"> {north_star}" if north_star else "",
        "",
        f"_Source: [Refero Styles]({refero_url}). Theme: {theme}._",
        "",
    ]
    if description:
        body += ["## Overview", "", description, ""]

    body.append(fmt_colors(colors))
    body.append(fmt_typography(ds.get("typography") or [], ds.get("typeScale") or []))
    body.append(fmt_components(ds.get("components") or []))
    body.append(fmt_section("Layout", ds.get("layout")))
    body.append(fmt_section("Spacing", ds.get("spacing")))
    body.append(fmt_section("Surfaces", ds.get("surfaces")))
    body.append(fmt_section("Elevation", ds.get("elevation")))
    body.append(fmt_section("Imagery", ds.get("imagery")))
    body.append(fmt_dos_donts(ds.get("dos") or [], ds.get("donts") or []))
    body.append(fmt_custom_sections(ds.get("customSections") or []))

    if style.get("thumbnailUrl"):
        body += ["## Preview", "", f"![{site_name}]({style['thumbnailUrl']})", ""]

    out = "\n".join(fm) + "\n".join(b for b in body if b)
    return out.rstrip() + "\n"


def main():
    raw = json.loads(SRC.read_text())
    print(f"Loaded {len(raw)} refero entries from list API")

    new_entries = [e for e in raw if normalize_domain(e["url"]) not in sans_domains]
    print(f"Filtered to {len(new_entries)} entries NOT in your corpus")
    print(f"Output dir: {DEST}\n")

    used_slugs: dict[str, int] = {}
    succeeded = 0
    failed = []
    skipped_resume = 0

    # Build slug map deterministic up front
    slug_map = {}
    for e in new_entries:
        base = slugify(e.get("siteName", ""), e.get("url", ""))
        if base in used_slugs:
            used_slugs[base] += 1
            slug = f"{base}-{used_slugs[base]}"
        else:
            used_slugs[base] = 1
            slug = base
        slug_map[e["id"]] = (slug, e)

    for i, (style_id, (slug, list_entry)) in enumerate(slug_map.items(), 1):
        detail_path = DEST / f"{slug}-detail.json"
        md_path = DEST / f"{slug}.md"

        if detail_path.exists() and md_path.exists():
            skipped_resume += 1
            if skipped_resume <= 3 or skipped_resume % 100 == 0:
                print(f"[{i}/{len(slug_map)}] {slug}: resume-skip")
            continue

        try:
            detail = fetch_detail(style_id)
        except Exception as e:
            failed.append((slug, str(e)[:120]))
            print(f"[{i}/{len(slug_map)}] {slug}: ✗ fetch failed: {e}")
            time.sleep(2 + random.random() * 2)
            continue

        # Save raw json
        detail_path.write_text(json.dumps(detail, indent=2))
        # Convert to md
        try:
            md = to_markdown(slug, list_entry, detail)
            md_path.write_text(md)
            succeeded += 1
            if i % 25 == 0 or i <= 5:
                print(f"[{i}/{len(slug_map)}] {slug}: ✓ ({len(md)//1024}KB md)")
        except Exception as e:
            failed.append((slug, f"convert: {e}"))
            print(f"[{i}/{len(slug_map)}] {slug}: ✗ convert: {e}")

        time.sleep(0.6 + random.random() * 0.8)

    print()
    print("=" * 60)
    print(f"Succeeded: {succeeded}")
    print(f"Resume-skipped: {skipped_resume}")
    print(f"Failed: {len(failed)}")
    for slug, err in failed[:10]:
        print(f"  → {slug}: {err}")


if __name__ == "__main__":
    main()
