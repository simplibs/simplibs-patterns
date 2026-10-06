from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.characters import (
    ASTERISK,
    EQUALS,
    MINUS_SIGN,
    PLUS_SIGN,
    SLASH,
)


OPERATOR = Literal("==") | Literal("!=") | Literal("<=") | Literal(">=") | CharacterClass(PLUS_SIGN, MINUS_SIGN, ASTERISK, SLASH, EQUALS, Literal("<"), Literal(">"))
"""Regex expression matching a common operator shared by most languages.

Init Params:
    (no parameters)

Pattern:
    `==`, `!=`, `<=`, `>=` or one of `+ - * / = < >`; two-character operators are tried first.
    Equivalent regex: `==|!=|<=|>=|[+\\-*/=<>]`

Notes:
Example:
    OPERATOR
    # Matches: "==", "!=", "<=", "+"
    # Does not match: "=>", "a", "!", ""
"""

_DESIGN_NOTES = """
Language-specific operator sets may eventually be exposed through a language-aware pattern
rather than expanding the common `OPERATOR` definition.
"""

