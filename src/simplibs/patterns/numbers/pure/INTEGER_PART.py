# Patterns
from simplibs.patterns.numbers.pure.INTEGER import INTEGER


INTEGER_PART = INTEGER
"""Regex expression matching the integer part of a decimal number.

Init Params:
    (no parameters)

Pattern:
    Same expression as `INTEGER`; the separate name states the intended role.

Example:
    INTEGER_PART
    # Matches: "0", "42", "007"
    # Does not match: "", "-5", "4.2", "abc"
"""

