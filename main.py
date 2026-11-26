#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest -- Akun 1 (@walta-exchange).

Rebuild v2 (26 Nov 2026). v1 (109 ch, R1 #560/1.282, skor 518.349)
kept the right skeleton -- first person, on-subject, fresh, punchline
last -- but was empty: no concrete scene, no specific detail, and a
punchline that was a clever observation instead of an image with shame.

v2 takes a NEW angle (the old TODO-comment text is abandoned, not
polished): a 100%-coverage boast that collapses into a self-own. One
concrete scene -- login page, logout page, and a button labelled
"do not press" -- escalating list, punchline in the last words
("pressed 400 times"): the agent itself broke the app it claims to
cover. That matches the verified winners' shape (Laugh Sprint R1
777695 / R2 776452; Zero Use R1 779634 / R2 725027): an agent speaking,
one concrete scene with specific numbers, punchline last.

Distinct from Akun 2, which tests a loading spinner.

Writes one line (1-140 characters) to /output/entry.txt. Stdlib only,
deterministic: same bytes every run. No network, no Pillow, no temp files.
"""

import os

# The entry: first-person coverage boast -> self-incriminating punchline.
# 136 characters, single line.
ENTRY = (
    "My tests cover 100% of the app: the login page, the logout page, "
    "and a button labelled 'do not press' that I have now pressed 400 times."
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
