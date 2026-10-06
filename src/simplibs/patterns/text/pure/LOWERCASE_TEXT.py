from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.character_classes import LOWERCASE_LETTER


LOWERCASE_TEXT = ONE_OR_MORE(LOWERCASE_LETTER)
"""Regex expression matching text made only of lowercase ASCII letters.

Init Params:
    (no parameters)

Pattern:
    One or more letters `a`–`z`.
    Equivalent regex: `[a-z]+`

Example:
    LOWERCASE_TEXT
    # Matches: "abc", "x"
    # Does not match: "Abc", "abc1", ""
"""

