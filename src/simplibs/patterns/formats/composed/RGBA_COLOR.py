from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import (
    EXACTLY,
    ONE_OR_MORE,
    OPTIONAL,
    ZERO_OR_MORE,
)
# Patterns
from simplibs.patterns.characters import COMMA, DOT, SPACE
from simplibs.patterns.numbers import INTEGER, ZERO_TO_TWO_HUNDRED_FIFTY_FIVE


RGBA_COLOR = Literal("rgba(") + ZERO_TO_TWO_HUNDRED_FIFTY_FIVE + EXACTLY(COMMA + ZERO_OR_MORE(SPACE) + ZERO_TO_TWO_HUNDRED_FIFTY_FIVE, 2) + COMMA + ZERO_OR_MORE(SPACE) + (Literal("0") + OPTIONAL(DOT + INTEGER) | Literal("1") + OPTIONAL(DOT + ONE_OR_MORE(Literal("0"))) | DOT + INTEGER) + Literal(")")
"""Regex expression matching a CSS rgba() color.

Init Params:
    (no parameters)

Pattern:
    `rgba(` followed by three 0–255 components and an alpha value from 0 to 1, then `)`.

Example:
    RGBA_COLOR
    # Matches: "rgba(255, 0, 0, 0.5)", "rgba(0,0,0,1)", "rgba(0,0,0,.25)"
    # Does not match: "rgba(0,0,0)", "rgba(0,0,0,2)", "rgba(0,0,0,1.5)"
"""

