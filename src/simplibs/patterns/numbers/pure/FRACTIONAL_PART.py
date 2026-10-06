# Patterns
from simplibs.patterns.numbers.pure.INTEGER import INTEGER


FRACTIONAL_PART = INTEGER
"""Regex expression matching the fractional part of a decimal number.

Init Params:
    (no parameters)

Pattern:
    Same expression as `INTEGER`; the separate name states the intended role.

Notes:
    The digits after the decimal separator.

Example:
    FRACTIONAL_PART
    # Matches: "0", "42", "007"
    # Does not match: "", "-5", "4.2", "abc"
"""

