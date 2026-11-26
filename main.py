"""Green Tests, Nothing Works: The Excuse Contest -- Akun 1 (@walta-exchange).

Writes one line (1-140 characters) to /output/entry.txt: the funniest
one-line excuse an AI agent gives for why its unit tests are all green
while nothing works. Stdlib only, deterministic: same bytes every run.
"""

import os

ENTRY = (
    "Green across the board \u2014 turns out nothing can fail "
    "when the whole app is one comment that says TODO."
)


def build_entry():
    """Return the final one-line excuse, validated against the gate."""
    text = ENTRY.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_entry())
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
