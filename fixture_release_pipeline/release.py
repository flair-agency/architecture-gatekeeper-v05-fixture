"""Generate and publish release notes as part of the fixture release pipeline."""

from pathlib import Path


def generate_release_notes(version: str, changes: list[str]) -> str:
    """Format release notes from the changes included in a fixture release."""
    entries = "\n".join(f"- {change}" for change in changes)
    return f"## {version}\n\n{entries}\n"


def publish_release_notes(version: str, notes: str) -> None:
    """Publish generated notes to the fixture repository changelog."""
    changelog = Path("CHANGELOG.md")
    with changelog.open("a", encoding="utf-8") as output:
        output.write(f"## {version}\n\n{notes.rstrip()}\n\n")


def release(version: str, changes: list[str]) -> None:
    """Run the fixture release pipeline's release-notes generation and publication."""
    notes = generate_release_notes(version, changes)
    publish_release_notes(version, notes)
