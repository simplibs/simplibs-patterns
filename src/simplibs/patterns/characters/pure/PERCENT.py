from simplibs.regex.elements.Literal import Literal


PERCENT = Literal("%")
"""Regex expression matching the percent sign character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one percent sign character (`%`), taken literally.
    Equivalent regex: `%`

Example:
    PERCENT
    # Matches: "%"
    # Does not match: "a", "%%"
"""

