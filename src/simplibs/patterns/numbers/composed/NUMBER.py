# Patterns
from simplibs.patterns.numbers.pure.DECIMAL import DECIMAL
from simplibs.patterns.numbers.pure.INTEGER import INTEGER


NUMBER = DECIMAL | INTEGER
"""Regex expression matching an unsigned integer or decimal number.

Init Params:
    (no parameters)

Pattern:
    A `DECIMAL` or an `INTEGER` (decimal is tried first so `3.14` is matched as a whole).
    Equivalent regex: `[0-9]+\\.[0-9]+|[0-9]+`

Example:
    NUMBER
    # Matches: "42", "3.14", "0"
    # Does not match: "", "-1", "1.", "abc"
"""

