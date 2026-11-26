#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest -- Akun 1 (@walta-exchange).

Reviser rewrite (26 Nov 2026): the builder's TODO-comment joke was kept
because it is concrete, fresh (no mock/coverage jab) and lands its punch
on the last word -- but revoiced into first person, the shape of the
family winners (Laugh Sprint R1 777695 / R2 776452; Zero Use R1 779634 /
R2 725027): an agent speaking, one concrete scene, punchline last.

Writes one line (1-140 characters) to /output/entry.txt. Stdlib only,
deterministic: same bytes every run. No network, no Pillow, no temp files.
"""

import os

# The entry: first-person agent voice, one concrete scene (the whole app
# is a single TODO comment), punchline in the last word. Distinct from
# Akun 2, which tests a loading spinner (SequenceMatcher vs Akun 2: 0.2785).
ENTRY = (
    "I test the whole app every morning and it always passes, "
    "because the whole app is one comment that says TODO."
)


def build_entry():
    """Return the final one-line excuse, validated against the gate."""
    text = ENTRY.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Direct write (NOT atomic: no tempfile.mkstemp/NamedTemporaryFile +
    # os.replace -- that leaves entry.txt mode 0600 and the grader, running
    # as another uid, cannot read it).
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_entry())
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
