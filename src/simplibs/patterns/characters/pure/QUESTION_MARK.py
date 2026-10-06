from simplibs.regex.elements.Literal import Literal


QUESTION_MARK = Literal("?")
"""Regex expression matching the question mark character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one question mark character (`?`), taken literally.
    Equivalent regex: `\\?`

Example:
    QUESTION_MARK
    # Matches: "?"
    # Does not match: "a", "??"
"""

