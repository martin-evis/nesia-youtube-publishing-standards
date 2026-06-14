#!/usr/bin/env python3
"""Jednoduchá kontrola YouTube metadát pre NESIA markdown balíky.

Použitie:
    python scripts/validate_youtube_metadata.py metadata-packages/talkshow/001-video.md

Skript nerieši všetko. Kontroluje hlavne:
- dĺžku odporúčaného nadpisu,
- dĺžku popisu,
- počet hashtagov,
- prítomnosť placeholderov DOPLNIŤ / NEOVERENÉ.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

TITLE_LIMIT = 100
DESCRIPTION_LIMIT = 5000
HASHTAG_LIMIT = 60


def extract_first_codeblock_after_heading(text: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}.*?```(?:text)?\n(.*?)\n```"
    match = re.search(pattern, text, flags=re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""


def main() -> int:
    if len(sys.argv) != 2:
        print("Použitie: python scripts/validate_youtube_metadata.py <subor.md>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Súbor neexistuje: {path}")
        return 2

    text = path.read_text(encoding="utf-8")

    title = extract_first_codeblock_after_heading(text, "Odporúčaný nadpis")
    description = extract_first_codeblock_after_heading(text, "Popis videa")
    hashtags_block = extract_first_codeblock_after_heading(text, "Hashtagy")
    hashtags = re.findall(r"(?<!\w)#\S+", hashtags_block)

    warnings: list[str] = []

    if title:
        if len(title) > TITLE_LIMIT:
            warnings.append(f"Nadpis má {len(title)} znakov, limit je {TITLE_LIMIT}.")
    else:
        warnings.append("Nenašiel som odporúčaný nadpis v očakávanom code blocku.")

    if description:
        if len(description) > DESCRIPTION_LIMIT:
            warnings.append(f"Popis má {len(description)} znakov, limit je {DESCRIPTION_LIMIT}.")
    else:
        warnings.append("Nenašiel som popis videa v očakávanom code blocku.")

    if len(hashtags) > HASHTAG_LIMIT:
        warnings.append(f"Počet hashtagov je {len(hashtags)}, YouTube môže ignorovať viac ako {HASHTAG_LIMIT} hashtagov.")

    if "DOPLNIŤ" in text or "DOPLNIT" in text:
        warnings.append("Súbor obsahuje placeholder DOPLNIŤ / DOPLNIT.")

    if "NEOVERENÉ" in text or "NEOVERENE" in text:
        warnings.append("Súbor obsahuje značku NEOVERENÉ / NEOVERENE.")

    print(f"Kontrola: {path}")
    print(f"Nadpis: {len(title) if title else 0} znakov")
    print(f"Popis: {len(description) if description else 0} znakov")
    print(f"Hashtagy: {len(hashtags)}")

    if warnings:
        print("\nUpozornenia:")
        for warning in warnings:
            print(f"- {warning}")
        return 1

    print("\nOK: základné kontroly prešli.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
