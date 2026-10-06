# Patterns
from simplibs.patterns.numbers import NUMBER, SCIENTIFIC


NUMBER_LITERAL = SCIENTIFIC | NUMBER
"""Regex expression matching an unsigned numeric literal.

Init Params:
    (no parameters)

Pattern:
    A `SCIENTIFIC` number, a `DECIMAL` or an `INTEGER`.
    Equivalent regex: `(?:[0-9]+\\.[0-9]+|[0-9]+)[eE][+\\-]?[0-9]+|[0-9]+\\.[0-9]+|[0-9]+`

Notes:
    Unsigned: a leading minus is an operator in source code. Language-specific forms (0x, 1_000, 10n) are not covered.

Example:
    NUMBER_LITERAL
    # Matches: "42", "3.14", "1e10", "2.5E-3"
    # Does not match: "", "abc", "1.", "-5"
"""

