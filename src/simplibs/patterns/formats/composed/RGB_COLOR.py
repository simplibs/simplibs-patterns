from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import EXACTLY, ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import COMMA, SPACE
from simplibs.patterns.numbers import ZERO_TO_TWO_HUNDRED_FIFTY_FIVE


RGB_COLOR = Literal("rgb(") + ZERO_TO_TWO_HUNDRED_FIFTY_FIVE + EXACTLY(COMMA + ZERO_OR_MORE(SPACE) + ZERO_TO_TWO_HUNDRED_FIFTY_FIVE, 2) + Literal(")")
"""Regex expression matching a CSS rgb() color.

Init Params:
    (no parameters)

Pattern:
    `rgb(` followed by three 0–255 components separated by commas (optional spaces), then `)`.

Example:
    RGB_COLOR
    # Matches: "rgb(255, 0, 0)", "rgb(0,0,0)"
    # Does not match: "rgb(256,0,0)", "rgb(1,2)", "rgba(0,0,0,1)"
"""

