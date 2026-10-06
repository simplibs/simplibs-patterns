from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.character_classes import UPPERCASE_LETTER


UPPERCASE_TEXT = ONE_OR_MORE(UPPERCASE_LETTER)
"""Regex expression matching text made only of uppercase ASCII letters.

Init Params:
    (no parameters)

Pattern:
    One or more letters `A`–`Z`.
    Equivalent regex: `[A-Z]+`

Example:
    UPPERCASE_TEXT
    # Matches: "ABC", "X"
    # Does not match: "aBC", "ABC1", ""
"""

