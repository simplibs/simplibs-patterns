# Patterns
from simplibs.patterns.times.composed.ISO_TIME import ISO_TIME
from simplibs.patterns.times.composed.TIMEZONE import TIMEZONE


TIMEZONE_TIME = ISO_TIME + TIMEZONE
"""Regex expression matching an ISO time with a time zone.

Init Params:
    (no parameters)

Pattern:
    An `ISO_TIME` followed by a `TIMEZONE`.
    Equivalent regex: `(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\\.[0-9]+)?(?:Z|[+\\-](?:[01][0-9]|2[0-3]):[0-5][0-9])`

Example:
    TIMEZONE_TIME
    # Matches: "14:30:05Z", "14:30:05+02:00"
    # Does not match: "14:30:05", "14:30Z"
"""

