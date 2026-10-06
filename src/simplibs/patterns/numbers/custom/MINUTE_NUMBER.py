from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT


MINUTE_NUMBER = CharacterClass(CharacterRange("0", "5")) + DECIMAL_DIGIT
"""Regex expression matching a two-digit minute.

Init Params:
    (no parameters)

Pattern:
    `00`–`59`, always two digits.
    Equivalent regex: `[0-5][0-9]`

Example:
    MINUTE_NUMBER
    # Matches: "00", "30", "59"
    # Does not match: "60", "5", "123"
"""

