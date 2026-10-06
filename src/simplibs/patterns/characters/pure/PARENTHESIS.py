from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal


PARENTHESIS = CharacterClass(Literal("("), Literal(")"))
"""Regex expression matching a single parenthesis.

Init Params:
    (no parameters)

Pattern:
    Matches `(` or `)`.
    Equivalent regex: `[()]`

Example:
    PARENTHESIS
    # Matches: "(", ")"
    # Does not match: "[", "()"
"""

