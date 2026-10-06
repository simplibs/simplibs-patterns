# Patterns
from simplibs.patterns.numbers.custom.MINUTE_NUMBER import MINUTE_NUMBER


SECOND_NUMBER = MINUTE_NUMBER
"""Regex expression matching a two-digit second.

Init Params:
    (no parameters)

Pattern:
    Same expression as `MINUTE_NUMBER`; the separate name states the intended role.

Notes:
    `00`–`59`; leap seconds (`60`) are not accepted.

Example:
    SECOND_NUMBER
    # Matches: "00", "30", "59"
    # Does not match: "60", "5", "123"
"""

