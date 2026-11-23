"""One-line joke for the make.fun One-Line Laugh Sprint.

Writes a single original line about everyday life to entry.txt in the
output directory named by the MAKEFUN_OUTPUT_DIR environment variable,
or "output" when that variable is unset or empty. The entry is one line
of 95 characters, inside the 1-200 character limit, written as UTF-8
with one trailing newline. Standard library only, deterministic,
no network, no randomness, no clock.
"""

import os
from pathlib import Path

JOKE = "My phone died mid-sentence, so I finished the argument out loud, alone, and somehow still lost."


def resolve_output_dir() -> Path:
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if raw:
        return Path(raw)
    return Path("output")


def write_entry() -> Path:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("joke must be 1-200 characters, got %d" % len(JOKE))
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("joke must be a single line")
    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    data = (JOKE + "\n").encode("utf-8")
    entry.write_bytes(data)
    return entry


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
