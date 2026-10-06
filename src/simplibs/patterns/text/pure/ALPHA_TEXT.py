from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.character_classes import LETTER


ALPHA_TEXT = ONE_OR_MORE(LETTER)
"""Regex expression matching text made only of ASCII letters.

Init Params:
    (no parameters)

Pattern:
    One or more ASCII letters.
    Equivalent regex: `[a-zA-Z]+`

Example:
    ALPHA_TEXT
    # Matches: "abc", "Hello"
    # Does not match: "abc1", "a b", ""
"""

