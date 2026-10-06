from simplibs.regex.elements.CharacterClass import CharacterClass
# Patterns
from simplibs.patterns.characters.pure.MINUS_SIGN import MINUS_SIGN
from simplibs.patterns.characters.pure.PLUS_SIGN import PLUS_SIGN


SIGN = CharacterClass(PLUS_SIGN, MINUS_SIGN)
"""Regex expression matching a single sign character.

Init Params:
    (no parameters)

Pattern:
    `PLUS_SIGN` or `MINUS_SIGN` — one of `+` and `-`.
    Equivalent regex: `[+\\-]`

Example:
    SIGN
    # Matches: "+", "-"
    # Does not match: "a", "+-"
"""

