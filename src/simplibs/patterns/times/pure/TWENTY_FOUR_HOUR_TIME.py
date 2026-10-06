# Patterns
from simplibs.patterns.times.pure.TIME import TIME


TWENTY_FOUR_HOUR_TIME = TIME
"""Regex expression matching a time in 24-hour form.

Init Params:
    (no parameters)

Pattern:
    Same expression as `TIME`; the separate name states the intended role.

Example:
    TWENTY_FOUR_HOUR_TIME
    # Matches: "00:00", "14:30", "23:59"
    # Does not match: "24:00", "7:30", "14:60", "1430"
"""

