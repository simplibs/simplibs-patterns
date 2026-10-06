from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ONE_OR_MORE
# Patterns
from simplibs.patterns.characters import BINARY_DIGIT


BINARY = Literal("0") + CharacterClass(Literal("b"), Literal("B")) + ONE_OR_MORE(BINARY_DIGIT)
"""Regex expression matching a binary number literal.

Init Params:
    (no parameters)

Pattern:
    `0b` (or `0B`) followed by one or more binary digits.
    Equivalent regex: `0[bB][01]+`

Example:
    BINARY
    # Matches: "0b101", "0B1"
    # Does not match: "0b", "0b2", "101"
"""

