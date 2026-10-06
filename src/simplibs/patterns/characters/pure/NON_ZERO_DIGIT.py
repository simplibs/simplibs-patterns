from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange


NON_ZERO_DIGIT = CharacterClass(CharacterRange("1", "9"))
"""Regex expression matching a single ASCII digit from 1 to 9.

Init Params:
    (no parameters)

Pattern:
    Matches one of the characters `1` to `9`. Used to forbid leading zeros.
    Equivalent regex: `[1-9]`

Example:
    NON_ZERO_DIGIT
    # Matches: "1", "5", "9"
    # Does not match: "0", "a", "12"
"""

