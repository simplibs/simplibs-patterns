from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange


OCTAL_DIGIT = CharacterClass(CharacterRange("0", "7"))
"""Regex expression matching a single octal digit.

Init Params:
    (no parameters)

Pattern:
    Matches one of the characters `0` to `7`.
    Equivalent regex: `[0-7]`

Example:
    OCTAL_DIGIT
    # Matches: "0", "7"
    # Does not match: "8", "a", "07"
"""

