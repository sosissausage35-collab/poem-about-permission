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


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
