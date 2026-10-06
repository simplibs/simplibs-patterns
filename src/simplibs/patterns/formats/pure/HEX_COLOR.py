from simplibs.regex.presets.quantifiers import EXACTLY
from simplibs.regex.presets.character_classes import HEX_DIGIT
# Patterns
from simplibs.patterns.characters import HASH_SIGN


HEX_COLOR = HASH_SIGN + (EXACTLY(HEX_DIGIT, 6) | EXACTLY(HEX_DIGIT, 3))
"""Regex expression matching a CSS hex color.

Init Params:
    (no parameters)

Pattern:
    `#` followed by 6 or 3 hex digits.
    Equivalent regex: `\\#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})`

Notes:
    Only the 3-digit and 6-digit CSS hexadecimal color forms are matched; alpha variants are not
    included.

Example:
    HEX_COLOR
    # Matches: "#fff", "#1A2B3C"
    # Does not match: "#ffff", "fff", "#ggg"
"""

