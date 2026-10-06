from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange


DECIMAL_DIGIT = CharacterClass(CharacterRange("0", "9"))
"""Regex expression matching a single ASCII decimal digit.

Init Params:
    (no parameters)

Pattern:
    Matches one of the characters `0` to `9` and nothing else.
    Equivalent regex: `[0-9]`

Notes:
    Strictly ASCII, unlike `DIGIT`. All numeric vocabulary in this package is built on this term.

Example:
    DECIMAL_DIGIT
    # Matches: "0", "7", "9"
    # Does not match: "a", "42", "٣"
"""

