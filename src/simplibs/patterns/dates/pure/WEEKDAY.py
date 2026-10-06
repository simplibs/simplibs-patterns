from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange


WEEKDAY = CharacterClass(CharacterRange("1", "7"))
"""Regex expression matching an ISO weekday number.

Init Params:
    (no parameters)

Pattern:
    `1` (Monday) to `7` (Sunday).
    Equivalent regex: `[1-7]`

Example:
    WEEKDAY
    # Matches: "1", "7"
    # Does not match: "0", "8", "12"
"""

