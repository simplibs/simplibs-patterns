# Patterns
from simplibs.patterns.times.pure.HOUR import HOUR
from simplibs.patterns.times.pure.MINUTE import MINUTE


COMPACT_TIME = HOUR + MINUTE
"""Regex expression matching a time written without separators.

Init Params:
    (no parameters)

Pattern:
    `HOUR` immediately followed by `MINUTE` (`HHMM`).
    Equivalent regex: `(?:[01][0-9]|2[0-3])[0-5][0-9]`

Example:
    COMPACT_TIME
    # Matches: "1430", "0000", "2359"
    # Does not match: "14:30", "2400", "143"
"""

