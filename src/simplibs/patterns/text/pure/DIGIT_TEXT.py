from simplibs.regex.presets.quantifiers import ONE_OR_MORE
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT


DIGIT_TEXT = ONE_OR_MORE(DECIMAL_DIGIT)
"""Regex expression matching text made only of ASCII digits.

Init Params:
    (no parameters)

Pattern:
    One or more characters `0`–`9`.
    Equivalent regex: `[0-9]+`

Example:
    DIGIT_TEXT
    # Matches: "0", "2026", "007"
    # Does not match: "1.5", "-1", "", "a1"
"""

