from simplibs.regex.elements.Literal import Literal


MINUS_SIGN = Literal("-")
"""Regex expression matching the minus sign character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one minus sign character (`-`), taken literally.
    Equivalent regex: `\\-`

Example:
    MINUS_SIGN
    # Matches: "-"
    # Does not match: "a", "--"
"""

