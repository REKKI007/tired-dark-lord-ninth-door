#!/usr/bin/env python3
"""The Warden of the Ninth Door — a 100-word villain monologue.

Writes the monologue to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Standard library only; deterministic; no network, no randomness.
"""

import os
from pathlib import Path

MONOLOGUE = (
    "You knocked. Nobody knocks. They kick, they chant, they die on the stairs. "
    "You knocked. You came to judge me. The ninth door opens only from inside, "
    "and I have held its key for — oh. Four kings? Five? I lost count when the "
    "third one begged. The trick is simple: one of us walks out, and the other "
    "stays. I made this floor shine for a hundred heroes. Leave your boots by "
    "the mat. Step through, and I will finally see the sun. Stay, and I will "
    "keep your place warm. Either way, the door gets fed."
)


def main() -> None:
    # Gate: entry.txt must be UTF-8 text of 1-600 characters.
    assert 1 <= len(MONOLOGUE) <= 600, len(MONOLOGUE)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(MONOLOGUE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
