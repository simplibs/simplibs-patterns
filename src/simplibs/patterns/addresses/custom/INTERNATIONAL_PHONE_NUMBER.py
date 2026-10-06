from simplibs.regex.presets.quantifiers import BETWEEN
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT, NON_ZERO_DIGIT, PLUS_SIGN


INTERNATIONAL_PHONE_NUMBER = PLUS_SIGN + NON_ZERO_DIGIT + BETWEEN(DECIMAL_DIGIT, 6, 14)
"""Regex expression matching an international phone number in E.164 form.

Init Params:
    (no parameters)

Pattern:
    `+`, a country code starting 1–9 and further digits — 7 to 15 digits in total, no separators.
    Equivalent regex: `\\+[1-9][0-9]{6,14}`

Example:
    INTERNATIONAL_PHONE_NUMBER
    # Matches: "+420123456789", "+14155552671"
    # Does not match: "420123456789", "+0123456789", "+123", "+420 123 456 789"
"""

