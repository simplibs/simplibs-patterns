from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.quantifiers import EXACTLY


EMPTY_TEXT = EXACTLY(ANY, 0)
"""Regex expression matching an empty string.

Init Params:
    (no parameters)

Pattern:
    Matches zero characters — only an empty input.
    Equivalent regex: `.{0}`

Example:
    EMPTY_TEXT
    # Matches: ""
    # Does not match: "a", " "
"""

