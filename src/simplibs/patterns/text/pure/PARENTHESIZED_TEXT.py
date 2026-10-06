from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE


PARENTHESIZED_TEXT = Literal("(") + ZERO_OR_MORE(CharacterClass(Literal("("), Literal(")"), negate=True)) + Literal(")")
"""Regex expression matching text in parentheses.

Init Params:
    (no parameters)

Pattern:
    `(`, any characters that are not parentheses, and `)`.
    Equivalent regex: `\\([^()]*\\)`

Notes:
    Not nested: parentheses inside are not allowed (a regex cannot count nesting levels).

Example:
    PARENTHESIZED_TEXT
    # Matches: "(abc)", "()"
    # Does not match: "abc", "(a(b))", "(open"
"""

