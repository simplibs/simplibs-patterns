# Patterns
from simplibs.patterns.times.pure.TIME import TIME


TIME_WITH_COLONS = TIME
"""Regex expression matching a time written with colons.

Init Params:
    (no parameters)

Pattern:
    Same expression as `TIME`; the separate name states the intended role.

Example:
    TIME_WITH_COLONS
    # Matches: "00:00", "14:30", "23:59"
    # Does not match: "24:00", "7:30", "14:60", "1430"
"""

