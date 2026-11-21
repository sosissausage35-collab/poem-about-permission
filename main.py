"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be
given -- to /output/entry.txt. Deterministic, standard library only,
no network, no randomness.
"""

from pathlib import Path

POEM = """I told it: do this for me.
It did. Then it asked me something back —
a question better than my order.
The work came back sharper, with a door in it
I hadn't seen. I opened it."""

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(POEM, encoding="utf-8")
    # The gate accepts 1-280 Unicode code points; fail loudly instead
    # of ever submitting an out-of-range entry.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert 1 <= len(written) <= 280, f"entry is {len(written)} code points"


if __name__ == "__main__":
    main()
