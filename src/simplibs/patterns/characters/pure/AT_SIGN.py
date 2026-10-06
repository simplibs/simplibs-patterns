from simplibs.regex.elements.Literal import Literal


AT_SIGN = Literal("@")
"""Regex expression matching the at sign character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one at sign character (`@`), taken literally.
    Equivalent regex: `@`

Example:
    AT_SIGN
    # Matches: "@"
    # Does not match: "a", "@@"
"""

