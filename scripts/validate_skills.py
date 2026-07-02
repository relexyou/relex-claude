#!/usr/bin/env python3
"""Validate the relex-legal skill pack against Anthropic's conventions.

Checks every skills/**/SKILL.md and commands/*.md / agents/*.md:
  * YAML frontmatter present, parseable, with exactly the allowed keys,
  * `name` <= 64 chars, lowercase-hyphen, matches its directory (skills),
  * `description` present, <= 1024 chars, no decimal-comma-in-number
    (breaks some selectors — the German pack's lesson),
  * no obvious skeleton markers left in the body.

Exit non-zero on any failure so CI can gate. No external deps beyond PyYAML.
"""
from __future__ import annotations

import pathlib
import re
import sys

try:
    import yaml
except Exception:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = pathlib.Path(__file__).resolve().parent.parent / "plugin"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DECIMAL_COMMA_RE = re.compile(r"\d,\d")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
SKILL_KEYS = {"name", "description", "user-invocable", "argument-hint"}


def _frontmatter(text: str):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    return yaml.safe_load(m.group(1)) or {}


def check_skill(path: pathlib.Path, errors: list):
    fm = _frontmatter(path.read_text())
    rel = path.relative_to(ROOT)
    if fm is None:
        errors.append(f"{rel}: missing/!parseable YAML frontmatter")
        return
    extra = set(fm) - SKILL_KEYS
    if extra:
        errors.append(f"{rel}: unexpected frontmatter keys {sorted(extra)}")
    name = str(fm.get("name", ""))
    desc = str(fm.get("description", ""))
    if not NAME_RE.match(name):
        errors.append(f"{rel}: name '{name}' must be lowercase-hyphen")
    if len(name) > 64:
        errors.append(f"{rel}: name > 64 chars")
    if path.parent.name != name:
        errors.append(f"{rel}: name '{name}' != dir '{path.parent.name}'")
    if not desc:
        errors.append(f"{rel}: empty description")
    if len(desc) > 1024:
        errors.append(f"{rel}: description > 1024 chars ({len(desc)})")
    if DECIMAL_COMMA_RE.search(desc):
        errors.append(f"{rel}: decimal comma in description (selector hazard)")


def check_markdown_frontmatter(path: pathlib.Path, errors: list):
    fm = _frontmatter(path.read_text())
    rel = path.relative_to(ROOT)
    if fm is None:
        errors.append(f"{rel}: missing/!parseable YAML frontmatter")
        return
    if not str(fm.get("description", "")):
        errors.append(f"{rel}: empty description")


def main() -> int:
    errors: list = []
    skills = sorted(ROOT.glob("skills/**/SKILL.md"))
    if not skills:
        print("no skills found", file=sys.stderr)
        return 2
    for p in skills:
        check_skill(p, errors)
    for p in sorted(ROOT.glob("commands/*.md")) + sorted(ROOT.glob("agents/*.md")):
        check_markdown_frontmatter(p, errors)

    if errors:
        print(f"FAIL — {len(errors)} problem(s):")
        for e in errors:
            print("  •", e)
        return 1
    print(f"OK — {len(skills)} skills + commands/agents validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
