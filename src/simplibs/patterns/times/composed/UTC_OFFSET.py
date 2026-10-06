# Patterns
from simplibs.patterns.times.composed.TIMEZONE_OFFSET import TIMEZONE_OFFSET


UTC_OFFSET = TIMEZONE_OFFSET
"""Regex expression matching a UTC offset.

Init Params:
    (no parameters)

Pattern:
    Same expression as `TIMEZONE_OFFSET`; the separate name states the intended role.

Example:
    UTC_OFFSET
    # Matches: "+02:00", "-05:30", "+00:00"
    # Does not match: "02:00", "+2:00", "+24:00", "+0200"
"""

