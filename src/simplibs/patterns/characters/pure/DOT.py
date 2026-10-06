from simplibs.regex.elements.Literal import Literal


DOT = Literal(".")
"""Regex expression matching the dot character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one dot character (`.`), taken literally.
    Equivalent regex: `\\.`

Example:
    DOT
    # Matches: "."
    # Does not match: "a", ".."
"""

