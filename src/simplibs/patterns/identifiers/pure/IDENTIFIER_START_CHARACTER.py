from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
# Patterns
from simplibs.patterns.characters import UNDERSCORE


IDENTIFIER_START_CHARACTER = CharacterClass(CharacterRange("a", "z"), CharacterRange("A", "Z"), UNDERSCORE)
"""Regex expression matching a character an identifier may start with.

Init Params:
    (no parameters)

Pattern:
    A letter `a`–`z`, `A`–`Z` or an underscore.
    Equivalent regex: `[a-zA-Z_]`

Example:
    IDENTIFIER_START_CHARACTER
    # Matches: "a", "Z", "_"
    # Does not match: "1", "-", "ab"
"""

