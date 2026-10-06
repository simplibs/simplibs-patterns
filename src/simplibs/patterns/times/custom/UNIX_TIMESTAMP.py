from simplibs.regex.presets.quantifiers import BETWEEN
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT


UNIX_TIMESTAMP = BETWEEN(DECIMAL_DIGIT, 1, 10)
"""Regex expression matching a Unix timestamp in seconds.

Init Params:
    (no parameters)

Pattern:
    One to ten digits (up to the year 2286).
    Equivalent regex: `[0-9]{1,10}`

Notes:
Example:
    UNIX_TIMESTAMP
    # Matches: "0", "1790000000", "86400"
    # Does not match: "", "-1", "17900000000", "1.5"
"""

_DESIGN_NOTES = """
If millisecond timestamps are added, use a distinct term such as `UNIX_TIMESTAMP_MS` so the unit
represented by `UNIX_TIMESTAMP` remains unambiguous.
"""

