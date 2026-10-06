# Patterns
from simplibs.patterns.characters import COLON, SIGN
from simplibs.patterns.times.pure.HOUR import HOUR
from simplibs.patterns.times.pure.MINUTE import MINUTE


TIMEZONE_OFFSET = SIGN + HOUR + COLON + MINUTE
"""Regex expression matching a UTC offset such as +02:00.

Init Params:
    (no parameters)

Pattern:
    `SIGN`, `HOUR`, colon, `MINUTE`.
    Equivalent regex: `[+\\-](?:[01][0-9]|2[0-3]):[0-5][0-9]`

Example:
    TIMEZONE_OFFSET
    # Matches: "+02:00", "-05:30", "+00:00"
    # Does not match: "02:00", "+2:00", "+24:00", "+0200"
"""

