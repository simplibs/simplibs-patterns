from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal


CLOSING_DELIMITER = CharacterClass(Literal(")"), Literal("]"), Literal("}"), Literal(">"))
"""Regex expression matching a closing bracket.

Init Params:
    (no parameters)

Pattern:
    One of `)`, `]`, `}`, `>`.
    Equivalent regex: `[)\\]}>]`

Example:
    CLOSING_DELIMITER
    # Matches: ")", "]", "}", ">"
    # Does not match: "(", "a", "])"
"""

