"""Generate and maintain the English half of the Kataguru Jekyll blog.

The script uses Google Translate's public endpoint for first-pass translations.
Review generated prose before publishing. Existing English files are overwritten.
"""

from __future__ import annotations

import concurrent.futures
import json
import re
import textwrap
import time
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CACHE_PATH = ROOT / "scripts" / ".translation-cache.json"

POST_SLUGS = {
    "2026-06-27-aloitus": "a-public-workbench",
    "2026-06-27-kaapon-hammashoito": "kaapos-dental-care-and-the-cost-of-options",
    "2026-06-27-miksi-lokaalit-ai-mallit-voittavat-yrityskaytossa": "why-local-ai-models-win-in-business",
    "2026-06-27-saunan-lattia-ja-yhden-nelion-virhe": "the-sauna-floor-and-a-one-square-metre-mistake",
    "2026-06-28-ruohonleikkurin-rengas-ja-vaihdantasopimus": "the-lawnmower-tyre-and-the-trade-off",
    "2026-06-30-keskinkertaisuuden-sietaminen": "tolerating-mediocrity",
    "2026-07-06-kun-mitaan-ei-tapahtunut": "when-nothing-happened",
    "2026-07-11-rappuset-joita-en-nahnyt": "the-stairs-i-did-not-see",
    "2026-07-12-lokaali-tekoalyagentti-tyokalu-joka-tuntee-oman-aineistoni": "a-local-ai-agent-that-knows-my-material",
    "2026-07-13-kierros-jonka-sain-keskeyttaa": "the-walk-i-was-allowed-to-stop",
    "2026-07-15-arvo-joka-kasvaa-ajan-myota": "value-that-grows-over-time",
    "2026-07-21-ei-syyllisyytta-vain-mahdollisuuksia": "no-guilt-only-possibilities",
    "2026-07-21-mika-kestaa-kun-pinta-pettaa": "what-holds-when-the-surface-fails",
    "2026-07-21-parisuhteen-asennusvirhe": "the-relationship-installation-error",
    "2026-07-21-resilienssi-tarvitsee-paineventtiilin": "resilience-needs-a-pressure-relief-valve",
}

STATIC_PAGES = {
    "ohjeet.md": ("en/instructions.md", "/en/instructions/", "instructions"),
    "minusta.md": ("en/about.md", "/en/about/", "about"),
    "projektit.md": ("en/projects.md", "/en/projects/", "projects"),
    "teesit.md": ("en/theses.md", "/en/theses/", "theses"),
}


def load_cache() -> dict[str, str]:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    return {}


CACHE = load_cache()


def google_translate(text: str) -> str:
    text = text.strip()
    if not text or not re.search(r"[A-Za-zÅÄÖåäö]", text):
        return text
    if text in CACHE:
        return CACHE[text]
    params = urllib.parse.urlencode(
        {"client": "gtx", "sl": "fi", "tl": "en", "dt": "t", "q": text}
    )
    url = "https://translate.googleapis.com/translate_a/single?" + params
    last_error = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8"))
            translated = "".join(part[0] for part in payload[0] if part[0]).replace("\u200b", "").strip()
            CACHE[text] = translated
            return translated
        except Exception as error:  # network retries are intentional
            last_error = error
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Translation failed: {text[:80]!r}") from last_error


PROTECTED = re.compile(
    r"(`[^`]+`|\{[%{].*?[}%]\}|https?://\S+|/assets/[^\s\)\"']+|<[^>]+>)"
)


def translate_markup(text: str) -> str:
    protected: list[str] = []

    def hold(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"ZXQPH{len(protected) - 1}QXZ"

    masked = PROTECTED.sub(hold, text)
    translated = google_translate(masked)
    for index, value in enumerate(protected):
        translated = translated.replace(f"ZXQPH{index}QXZ", value)
        translated = translated.replace(f"ZXQPH {index} QXZ", value)
    return translated


def split_front_matter(text: str) -> tuple[list[str], str]:
    if not text.startswith("---\n"):
        return [], text
    marker = text.find("\n---\n", 4)
    if marker < 0:
        raise ValueError("Unclosed front matter")
    return text[4:marker].splitlines(), text[marker + 5 :]


def front_value(lines: list[str], key: str) -> str | None:
    prefix = key + ":"
    for line in lines:
        if line.startswith(prefix):
            return line[len(prefix) :].strip().strip('"')
    return None


def upsert_front(lines: list[str], key: str, value: str, quoted: bool = False) -> list[str]:
    rendered = f'{key}: "{value}"' if quoted else f"{key}: {value}"
    prefix = key + ":"
    for index, line in enumerate(lines):
        if line.startswith(prefix):
            lines[index] = rendered
            return lines
    lines.append(rendered)
    return lines


def translate_front(lines: list[str], translation_key: str, permalink: str) -> list[str]:
    translated: list[str] = []
    for line in lines:
        match = re.match(r'^(title|description|image_alt|location):\s*"(.*)"\s*$', line)
        if match:
            value = translate_markup(match.group(2)).replace('"', "'")
            translated.append(f'{match.group(1)}: "{value}"')
        elif line.startswith("type:"):
            translated.append("type: Article")
        elif line.startswith(("lang:", "translation_key:", "permalink:")):
            continue
        else:
            translated.append(line)
    translated.extend(["lang: en", f"translation_key: {translation_key}", f"permalink: {permalink}"])
    return translated


def translate_body(body: str) -> str:
    blocks = re.split(r"(\n\s*\n)", body)
    work: list[tuple[int, str, str]] = []
    output = list(blocks)
    for index, block in enumerate(blocks):
        if not block.strip() or block.strip() in {"---", "***"}:
            continue
        prefix = ""
        match = re.match(r"^(#{1,6}\s+|[-*+]\s+|>\s+)", block)
        if match:
            prefix = match.group(1)
            block = block[len(prefix) :]
        work.append((index, prefix, block))

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        translations = list(pool.map(lambda item: translate_markup(item[2]), work))
    for (index, prefix, original), translated in zip(work, translations):
        trailing = "\n" if original.endswith("\n") else ""
        output[index] = prefix + translated + trailing
    return "".join(output)


def add_finnish_pairing(path: Path, translation_key: str) -> None:
    text = path.read_text(encoding="utf-8")
    front, body = split_front_matter(text)
    front = upsert_front(front, "lang", "fi")
    front = upsert_front(front, "translation_key", translation_key)
    path.write_text("---\n" + "\n".join(front) + "\n---\n" + body, encoding="utf-8")


def generate_posts() -> None:
    destination = ROOT / "_posts" / "en"
    destination.mkdir(parents=True, exist_ok=True)
    for path in sorted((ROOT / "_posts").glob("*.md")):
        stem = path.stem
        slug = POST_SLUGS[stem]
        date = stem[:10]
        translation_key = stem
        source = path.read_text(encoding="utf-8")
        front, body = split_front_matter(source)
        source_date = front_value(front, "date") or f"{date} 06:00:00 +0300"
        year, month, day = date.split("-")
        permalink = f"/en/{year}/{month}/{day}/{slug}/"
        english_front = translate_front(front, translation_key, permalink)
        if not any(line.startswith("date:") for line in english_front):
            english_front.append(f"date: {source_date}")
        english = "---\n" + "\n".join(english_front) + "\n---\n\n" + translate_body(body).lstrip()
        (destination / f"{date}-{slug}.md").write_text(english, encoding="utf-8")
        add_finnish_pairing(path, translation_key)


def generate_static_pages() -> None:
    for source_name, (destination_name, permalink, key) in STATIC_PAGES.items():
        source_path = ROOT / source_name
        source = source_path.read_text(encoding="utf-8")
        front, body = split_front_matter(source)
        front = upsert_front(front, "lang", "fi")
        front = upsert_front(front, "translation_key", key)
        source_path.write_text("---\n" + "\n".join(front) + "\n---\n" + body, encoding="utf-8")
        english_front = translate_front(front, key, permalink)
        destination = ROOT / destination_name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            "---\n" + "\n".join(english_front) + "\n---\n\n" + translate_body(body).lstrip(),
            encoding="utf-8",
        )


def generate_books() -> None:
    source = (ROOT / "_data" / "books.yml").read_text(encoding="utf-8")
    lines = source.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        scalar = re.match(r'^(\s*(?:- )?(?:title|status|availability):\s*)"(.*)"\s*$', line)
        if scalar:
            value = translate_markup(scalar.group(2)).replace('"', "'")
            output.append(f'{scalar.group(1)}"{value}"')
            index += 1
            continue
        if line.strip() == "- >":
            output.append(line)
            index += 1
            paragraph: list[str] = []
            while index < len(lines) and (not lines[index].strip() or lines[index].startswith("      ")):
                if lines[index].strip():
                    paragraph.append(lines[index].strip())
                index += 1
            translated = translate_markup(" ".join(paragraph))
            for wrapped in textwrap.wrap(translated, width=100, break_long_words=False):
                output.append("      " + wrapped)
            continue
        output.append(line)
        index += 1
    (ROOT / "_data" / "books_en.yml").write_text("\n".join(output) + "\n", encoding="utf-8")


def main() -> None:
    generate_posts()
    generate_static_pages()
    generate_books()
    CACHE_PATH.write_text(json.dumps(CACHE, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated English content with {len(CACHE)} cached translations.")


if __name__ == "__main__":
    main()
