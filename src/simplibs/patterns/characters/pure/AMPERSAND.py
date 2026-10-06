from simplibs.regex.elements.Literal import Literal


AMPERSAND = Literal("&")
"""Regex expression matching the ampersand character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one ampersand character (`&`), taken literally.
    Equivalent regex: `\\&`

Example:
    AMPERSAND
    # Matches: "&"
    # Does not match: "a", "&&"
"""

