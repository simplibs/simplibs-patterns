from simplibs.regex.presets.quantifiers import ONE_OR_MORE
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT


INTEGER = ONE_OR_MORE(DECIMAL_DIGIT)
"""Regex expression matching an unsigned whole number.

Init Params:
    (no parameters)

Pattern:
    One or more ASCII digits. Leading zeros are allowed.
    Equivalent regex: `[0-9]+`

Notes:
    Unsigned. For a sign use `SIGNED_INTEGER`; for zero / positive / negative checks see `ZERO`, `POSITIVE`, `NEGATIVE`.

Example:
    INTEGER
    # Matches: "0", "42", "007"
    # Does not match: "", "-5", "4.2", "abc"
"""

