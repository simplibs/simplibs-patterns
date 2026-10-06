# Patterns
from simplibs.patterns.characters import DOT
from simplibs.patterns.numbers.pure.INTEGER import INTEGER


DECIMAL = INTEGER + DOT + INTEGER
"""Regex expression matching an unsigned decimal number with a dot.

Init Params:
    (no parameters)

Pattern:
    An `INTEGER`, a dot and another `INTEGER`.
    Equivalent regex: `[0-9]+\\.[0-9]+`

Notes:
Example:
    DECIMAL
    # Matches: "3.14", "0.5", "10.000"
    # Does not match: "3", ".5", "3.", "3,14"
"""

_DESIGN_NOTES = """
If locale-aware decimal syntax is introduced, prefer an explicit separate term or parameter so
that `DECIMAL` keeps its current dot-based meaning.
"""

