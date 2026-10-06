# Patterns
from simplibs.patterns.times.pure.COMPACT_TIME import COMPACT_TIME


TIME_WITHOUT_COLONS = COMPACT_TIME
"""Regex expression matching a time written without colons.

Init Params:
    (no parameters)

Pattern:
    Same expression as `COMPACT_TIME`; the separate name states the intended role.

Example:
    TIME_WITHOUT_COLONS
    # Matches: "1430", "0000", "2359"
    # Does not match: "14:30", "2400", "143"
"""

