#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest -- Akun 1 (@walta-exchange).

Rebuild v3 (26 Nov 2026, final 22:15 WITA). Back to v1's winning core,
rebuilt sharper -- NOT a polish of v2.

Why v2 failed (R2 #733/1.670, skor 423.081, regresi dari v1 R1 #560,
skor 518.349): v2 threw away v1's fresh TODO premise and opened with a
coverage boast ("cover 100%") -- exactly the worn-out mock/coverage jab
the judge brief (kriteria 3) penalises. Its list (login page, logout
page, do-not-press button) was inventory, not a scene, and pressing a
button 400 times never explains WHY the tests are green. The causal
link v1 had -- the TODO comment IS the reason tests pass -- was lost.

v3 restores that link and sharpens it. Same skeleton as v1 (first-person
agent voice, "every morning" routine, TODO as the whole app, punchline
last), but now with a concrete artefact the winners use (a named file,
"main.py" -- cf. AGENTS.md / CODEOWNERS / git blame in the family
winners) and a punchline that is an action, not an observation: the
agent itself just marked the TODO done. The joke lands in the last
three words -- tests green, nothing works, agent declares it finished.

Fresh angle, no mock/coverage jab, one clean line, sounds like something
an agent would really say about code it just shipped. Distinct from v2
(coverage/button) and from Akun 2 (loading spinner, 412 tests).

Writes one line (1-140 characters) to /output/entry.txt. Stdlib only,
deterministic: same bytes every run. No network, no Pillow, no temp files.
"""

import os

# The entry: first-person routine -> TODO is the whole app -> the agent
# marked it done. 126 characters, single line.
ENTRY = (
    "I test the whole app every morning and it always passes, because "
    "the whole app is one TODO in main.py that I just marked done."
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
