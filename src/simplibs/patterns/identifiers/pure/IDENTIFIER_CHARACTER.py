from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
# Patterns
from simplibs.patterns.characters import UNDERSCORE


IDENTIFIER_CHARACTER = CharacterClass(CharacterRange("a", "z"), CharacterRange("A", "Z"), CharacterRange("0", "9"), UNDERSCORE)
"""Regex expression matching a character that may appear inside an identifier.

Init Params:
    (no parameters)

Pattern:
    A letter, a digit or an underscore (ASCII only).
    Equivalent regex: `[a-zA-Z0-9_]`

Example:
    IDENTIFIER_CHARACTER
    # Matches: "a", "Z", "5", "_"
    # Does not match: "-", "ab", " "
"""

