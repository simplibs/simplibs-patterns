from simplibs.regex.elements.Literal import Literal


SLASH = Literal("/")
"""Regex expression matching the slash character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one slash character (`/`), taken literally.
    Equivalent regex: `/`

Example:
    SLASH
    # Matches: "/"
    # Does not match: "a", "//"
"""

