# Patterns
from simplibs.patterns.characters import DOT
from simplibs.patterns.numbers import INTEGER
from simplibs.patterns.times.composed.TIME_WITH_SECONDS import TIME_WITH_SECONDS


TIME_WITH_FRACTION = TIME_WITH_SECONDS + DOT + INTEGER
"""Regex expression matching a time with seconds and a fractional part.

Init Params:
    (no parameters)

Pattern:
    A `TIME_WITH_SECONDS`, a dot and one or more digits.
    Equivalent regex: `(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]\\.[0-9]+`

Example:
    TIME_WITH_FRACTION
    # Matches: "14:30:05.123", "00:00:00.5"
    # Does not match: "14:30:05", "14:30:05."
"""

