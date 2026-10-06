from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.presets.literals import TAB
# Patterns
from simplibs.patterns.characters import (
    COMMA,
    PIPE,
    SEMICOLON,
    SPACE,
)


SEPARATOR = CharacterClass(COMMA, SEMICOLON, PIPE, TAB, SPACE)
"""Regex expression matching a common separator character.

Init Params:
    (no parameters)

Pattern:
    One of comma, semicolon, pipe, tab or space.
    Equivalent regex: `[,;|\\t ]`

Notes:
Example:
    SEPARATOR
    # Matches: ",", ";", "|", "\\t"
    # Does not match: "a", "::", ""
"""

_DESIGN_NOTES = """
The separator character set is intentionally small. Changes to it should be driven by concrete
parsing use cases rather than by an attempt to model every possible separator convention.
"""

