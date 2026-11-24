# SPDX-License-Identifier: MIT
"""Ridiculous at First Glance, Real by the Second.

Writes a single-sentence startup pitch (max 200 characters) to
/output/entry.txt. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "We rent goats in tuxedos to attend corporate layoff meetings, and HR "
    "departments pay $800 a day because nobody films themselves crying when "
    "a goat in a bow tie is eating the severance paperwork."
)


def main() -> None:
    # Gate: one sentence, 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY and ENTRY.count(".") == 1
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
