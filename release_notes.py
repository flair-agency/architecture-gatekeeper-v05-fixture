"""Utilities for publishing release notes in the synthetic fixture."""

from pathlib import Path


def publish_release_notes(version: str, notes: str) -> None:
    """Append a version's notes to the repository changelog."""
    changelog = Path("CHANGELOG.md")
    with changelog.open("a", encoding="utf-8") as output:
        output.write(f"## {version}\n\n{notes.rstrip()}\n\n")
