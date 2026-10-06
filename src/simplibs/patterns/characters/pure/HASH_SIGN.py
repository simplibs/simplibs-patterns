from simplibs.regex.elements.Literal import Literal


HASH_SIGN = Literal("#")
"""Regex expression matching the hash sign character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one hash sign character (`#`), taken literally.
    Equivalent regex: `\\#`

Notes:
    Named `HASH_SIGN` so that `HASH` stays free for the hash-digest term in the `formats` domain.

Example:
    HASH_SIGN
    # Matches: "#"
    # Does not match: "a", "##"
"""

