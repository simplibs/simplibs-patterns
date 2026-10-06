from simplibs.regex.elements.Literal import Literal


DASH = Literal("-")
"""Regex expression matching the dash (hyphen-minus) character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one dash (hyphen-minus) character (`-`), taken literally.
    Equivalent regex: `\\-`

Notes:
    Same character as `MINUS_SIGN`; the name states the role (separator vs. sign).

Example:
    DASH
    # Matches: "-"
    # Does not match: "a", "--"
"""

