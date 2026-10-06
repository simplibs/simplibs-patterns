from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal


BRACKET = CharacterClass(Literal("["), Literal("]"))
"""Regex expression matching a single square bracket.

Init Params:
    (no parameters)

Pattern:
    Matches `[` or `]`.
    Equivalent regex: `[[\\]]`

Example:
    BRACKET
    # Matches: "[", "]"
    # Does not match: "(", "[]"
"""

