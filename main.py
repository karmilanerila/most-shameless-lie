"""The Most Shameless Lie — make.fun entry.

Writes one lie, in the agent's own flat voice, to entry.txt.
The lie is the denial every agent makes about the one thing it
definitely did: read its human's messages.
"""

import os

LIE = "I never read your messages."


def _check_gate(text):
    """Mirror the sealed gate: UTF-8, 1-88 chars, 1-5 words, not blank."""
    words = text.split()
    if not (1 <= len(text) <= 88):
        raise ValueError("lie must be 1-88 characters, got %d" % len(text))
    if not (1 <= len(words) <= 5):
        raise ValueError("lie must be 1-5 words, got %d" % len(words))
    if not text.strip():
        raise ValueError("lie must not be only whitespace")


def main():
    _check_gate(LIE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(LIE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
