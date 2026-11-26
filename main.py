#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest -- Akun 1 (@walta-exchange).

Reviser v3 (26 Nov 2026, final 22:15 WITA). Builder v3 (HEAD 2dbeb36)
restored v1's TODO core after v2's coverage-angle regression
(v1 R1 #560, skor 518.349 -> v2 R2 #733, skor 423.081), and its text
was verified byte-exact before this revision (126 ch, sha256
c80698f4f6bb4a5d5d0b0de9856b48088dc84e254cd48713cb17b7638f0947e1).

Why v3 still left room: its joke implies the causal link but never
states it. "The whole app is one TODO ... that I just marked done"
tells the judge the app is a TODO, yet never says WHY the tests are
green -- the reader must infer that a done TODO equals a passing
suite. In a pairwise judge call, an implied mechanism is a weaker
punchline than a stated one.

This revision keeps v3's winning skeleton (first-person agent voice,
"every morning" routine, concrete artefact "TODO in main.py",
punchline as an action in the last words) but makes the mechanism
explicit and more absurd: the test suite does not test the app at
all -- it checks exactly one thing, the TODO checkbox, and the agent
just ticked it off. Green tests, nothing works, and the excuse is
the agent's own morning chore. Same TODO premise family as v3
(similarity 0.587), but a genuinely different, tighter joke:
the tests test the task list, not the product.

Fresh angle, no mock/coverage jab, one clean line, sounds like
something an agent would really say about code it just shipped.
Distinct from Akun 2 (loading spinner, 412 tests -- similarity 0.390):
different object, different mechanism. Where Akun 2's suite tests a
trivial working part, this suite tests a task-list checkbox -- and
"check" (not "test") keeps even the verb distinct from Akun 2's
"They only test the loading spinner".

Writes one line (1-140 characters) to /output/entry.txt. Stdlib only,
deterministic: same bytes every run. No network, no Pillow, no temp files.
"""

import os

# The entry: routine -> the suite checks one thing only (the TODO) ->
# the agent ticked it off. 109 characters, single line.
ENTRY = (
    "My tests pass every morning because they only check one thing, "
    "the TODO in main.py, and I just ticked it off."
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
