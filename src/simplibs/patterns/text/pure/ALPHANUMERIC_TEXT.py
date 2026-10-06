from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.character_classes import ALPHANUMERIC


ALPHANUMERIC_TEXT = ONE_OR_MORE(ALPHANUMERIC)
"""Regex expression matching text made only of ASCII letters and digits.

Init Params:
    (no parameters)

Pattern:
    One or more characters from `a`–`z`, `A`–`Z`, `0`–`9`.
    Equivalent regex: `[a-zA-Z0-9]+`

Example:
    ALPHANUMERIC_TEXT
    # Matches: "abc123", "X"
    # Does not match: "a b", "a_b", ""
"""

