from simplibs.regex.presets.quantifiers import EXACTLY, OPTIONAL
# Patterns
from simplibs.patterns.characters import DASH, DECIMAL_DIGIT


ZIP_CODE = EXACTLY(DECIMAL_DIGIT, 5) + OPTIONAL(DASH + EXACTLY(DECIMAL_DIGIT, 4))
"""Regex expression matching a US ZIP code.

Init Params:
    (no parameters)

Pattern:
    Five digits, optionally followed by a hyphen and four digits (ZIP+4).
    Equivalent regex: `[0-9]{5}(?:\\-[0-9]{4})?`

Example:
    ZIP_CODE
    # Matches: "90210", "90210-1234"
    # Does not match: "9021", "90210-12", "902101234"
"""

