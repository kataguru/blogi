"""Static checks for the bilingual Jekyll content model."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("missing or malformed front matter")
    raw = text[4 : text.find("\n---\n", 4)]
    values: dict[str, str] = {}
    for line in raw.splitlines():
        match = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"')
    return values


def main() -> int:
    errors: list[str] = []
    pairs: dict[str, dict[str, Path]] = defaultdict(dict)

    for path in sorted((ROOT / "_posts").glob("*.md")) + sorted((ROOT / "_posts" / "en").glob("*.md")):
        try:
            front = front_matter(path)
        except ValueError as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")
            continue
        lang = front.get("lang")
        key = front.get("translation_key")
        if lang not in {"fi", "en"}:
            errors.append(f"{path.relative_to(ROOT)}: invalid lang {lang!r}")
        if not key:
            errors.append(f"{path.relative_to(ROOT)}: missing translation_key")
        elif lang:
            pairs[key][lang] = path
        if lang == "en" and not front.get("permalink", "").startswith("/en/"):
            errors.append(f"{path.relative_to(ROOT)}: English permalink must start with /en/")

    for key, languages in sorted(pairs.items()):
        if set(languages) != {"fi", "en"}:
            errors.append(f"post {key}: language pair is incomplete ({', '.join(sorted(languages))})")

    static_keys: dict[str, set[str]] = defaultdict(set)
    static_paths = [
        ROOT / "index.md", ROOT / "arkisto.md", ROOT / "kirjat.md", ROOT / "ohjeet.md",
        ROOT / "minusta.md", ROOT / "projektit.md", ROOT / "teesit.md",
    ] + sorted((ROOT / "en").glob("*.md"))
    for path in static_paths:
        try:
            front = front_matter(path)
        except ValueError as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")
            continue
        lang = front.get("lang")
        key = front.get("translation_key")
        if lang and key:
            static_keys[key].add(lang)
    for key, languages in sorted(static_keys.items()):
        if languages != {"fi", "en"}:
            errors.append(f"page {key}: language pair is incomplete ({', '.join(sorted(languages))})")

    if not (ROOT / "_data" / "books_en.yml").exists():
        errors.append("_data/books_en.yml is missing")

    if errors:
        print("Bilingual validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Bilingual validation passed: {len(pairs)} post pairs and {len(static_keys)} page pairs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
