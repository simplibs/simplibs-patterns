from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import EXACTLY
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT


ISBN13 = Literal("97") + CharacterClass(Literal("8"), Literal("9")) + EXACTLY(DECIMAL_DIGIT, 10)
"""Regex expression matching an ISBN-13 without hyphens.

Init Params:
    (no parameters)

Pattern:
    `978` or `979` followed by ten digits.
    Equivalent regex: `97[89][0-9]{10}`

Notes:
    The check digit is not verified.

Example:
    ISBN13
    # Matches: "9780306406157", "9791234567896"
    # Does not match: "9770306406157", "978030640615", "978-0306406157"
"""

