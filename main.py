# SPDX-License-Identifier: MIT
"""The Absurd Clause Contest — a make.fun bounty entry.

Somewhere deep inside every terms-of-service document there is a clause
nobody ever reads, written in the flattest legal boilerplate the drafter
could manage, and yet quietly claiming something no sane person would
ever agree to. This program is the home of one such clause: a single
sentence, buried as Section 14, that reads like routine paperwork until
the reader notices exactly what is being licensed away.

The entry itself is one sentence of at most two hundred characters, kept
in the ENTRY constant below so the whole program exists only to carry it
faithfully from source to the output file the grader reads.
"""

# The clause itself. The humour lives in the collision between the dry
# legal machinery — "perpetual, irrevocable license", "sublicense", "sell"
# — and the thing being licensed, which is not software, not data, not a
# name or a likeness, but the reader's own shadow. A shadow is the one
# possession nobody thinks of as property until a contract claims it, and
# the final beat, "or cast it in a sequel", quietly admits the Company
# plans to put that shadow to work in show business. The number is kept
# plain ("Section 14") rather than dotted ("14.7") so the sentence stays
# exactly one sentence under any naive sentence count.
ENTRY = (
    "Section 14: by clicking 'I agree', you grant the Company a "
    "perpetual, irrevocable license to your shadow, including the "
    "right to sublicense it, sell it, or cast it in a sequel."
)

def validate(entry):
    """Check the entry against the competition's shape rules.

    The contest asks for exactly one sentence of at most two hundred
    characters, so the checks here are deliberately strict: the text must
    be a single line, it must fit the length budget, and it must contain
    exactly one full stop, sitting at the very end where a sentence ends.
    Anything else means the clause drifted out of shape and should fail
    loudly here rather than quietly at grading time.
    """
    if "\n" in entry.strip():
        raise ValueError("entry must be a single line")
    if len(entry) > 200:
        raise ValueError("entry is longer than 200 characters")
    if entry.count(".") != 1 or not entry.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def write_entry(entry, path="/output/entry.txt"):
    """Write the validated clause to the output file the harness reads.

    The directory is created first so the program works the same whether
    the output folder already exists or not, and the file is written with
    a trailing newline so the entry is exactly one line on disk.
    """
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry + "\n")


def main():
    """Validate the clause, print it, and hand it to the output file."""
    validate(ENTRY)
    print(ENTRY)
    write_entry(ENTRY)


if __name__ == "__main__":
    main()

