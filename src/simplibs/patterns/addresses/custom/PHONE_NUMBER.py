from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import BETWEEN, OPTIONAL
# Patterns
from simplibs.patterns.characters import (
    DASH,
    DECIMAL_DIGIT,
    PLUS_SIGN,
    SPACE,
)


PHONE_NUMBER = OPTIONAL(PLUS_SIGN) + CharacterClass(CharacterRange("0", "9"), Literal("(")) + BETWEEN(CharacterClass(CharacterRange("0", "9"), SPACE, DASH, Literal("("), Literal(")")), 5, 18) + DECIMAL_DIGIT
"""Regex expression matching a phone number in a lenient written form.

Init Params:
    (no parameters)

Pattern:
    An optional `+`, then digits mixed with spaces, hyphens and parentheses, ending in a digit (about 7–20 characters).
    Equivalent regex: `\\+?[0-9(][0-9 \\-()]{5,18}[0-9]`

Notes:
    Lenient on purpose: the count of digits and the country rules are not checked.

    Country-specific phone-number grouping and exact digit counts are not validated; the pattern
    accepts a broad written form instead.

Example:
    PHONE_NUMBER
    # Matches: "+420 123 456 789", "(555) 123-4567", "555-1234"
    # Does not match: "12345", "abc", "+"
"""

