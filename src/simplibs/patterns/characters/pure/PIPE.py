from simplibs.regex.elements.Literal import Literal


PIPE = Literal("|")
"""Regex expression matching the pipe character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one pipe character (`|`), taken literally.
    Equivalent regex: `\\|`

Example:
    PIPE
    # Matches: "|"
    # Does not match: "a", "||"
"""

