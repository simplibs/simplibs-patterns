from simplibs.regex.presets.quantifiers import BETWEEN
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT


CREDIT_CARD_NUMBER = BETWEEN(DECIMAL_DIGIT, 13, 19)
"""Regex expression matching a credit card number without separators.

Init Params:
    (no parameters)

Pattern:
    13 to 19 digits.
    Equivalent regex: `[0-9]{13,19}`

Notes:
    Only the length is checked — no brand prefix and no Luhn checksum.

    Only the numeric length is checked; card-brand prefixes, checksums and separator characters are
    not validated.

Example:
    CREDIT_CARD_NUMBER
    # Matches: "4111111111111111", "378282246310005"
    # Does not match: "411111111111", "41111 1111 1111 1111", "41111111111111111111"
"""

