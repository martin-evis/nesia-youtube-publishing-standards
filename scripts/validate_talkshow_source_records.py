#!/usr/bin/env python3
"""Basic validator for NESIA TALKSHOW source records.

No external dependencies. It checks only file presence and required metadata keys.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PUBLISHED = ROOT / "content" / "talkshow" / "published"
REQUIRED_FILES = [
    "source-metadata.yaml",
    "raw-input.md",
    "source-description.md",
    "source-transcript.md",
    "analysis.md",
    "performance-notes.md",
]
REQUIRED_STRINGS = [
    "schema_version:",
    "repo_version:",
    "record_type:",
    "public_repo_safe:",
    "video:",
    "publication:",
    "format:",
    "people:",
    "current_youtube_metadata:",
    "content:",
    "performance_public:",
    "missing_data:",
]


def main() -> int:
    if not PUBLISHED.exists():
        print(f"ERROR: Missing directory {PUBLISHED}")
        return 1

    dirs = [p for p in PUBLISHED.iterdir() if p.is_dir()]
    errors = []

    if not dirs:
        errors.append("No published video folders found.")

    for folder in sorted(dirs):
        for filename in REQUIRED_FILES:
            path = folder / filename
            if not path.exists():
                errors.append(f"{folder.name}: missing {filename}")
        metadata = folder / "source-metadata.yaml"
        if metadata.exists():
            text = metadata.read_text(encoding="utf-8")
            for marker in REQUIRED_STRINGS:
                if marker not in text:
                    errors.append(f"{folder.name}: source-metadata.yaml missing marker {marker}")
            if "public_repo_safe: true" not in text:
                errors.append(f"{folder.name}: public_repo_safe must be explicitly true/false")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: {len(dirs)} published TALKSHOW source records validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
