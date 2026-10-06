from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal


SYMBOL = CharacterClass(Literal("$"), Literal("+"), Literal("<"), Literal("="), Literal(">"), Literal("^"), Literal("`"), Literal("|"), Literal("~"),)
"""Regex expression matching a single symbol character.

Init Params:
    (no parameters)

Pattern:
    Matches one of ``$ + < = > ^ ` | ~``.
    Equivalent regex: `[$+<=>\\^`|~]`

Example:
    SYMBOL
    # Matches: "$", "+", "~"
    # Does not match: "!", "a"
"""

