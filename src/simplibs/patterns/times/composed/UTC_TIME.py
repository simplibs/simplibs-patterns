from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.times.composed.ISO_TIME import ISO_TIME


UTC_TIME = ISO_TIME + Literal("Z")
"""Regex expression matching an ISO time in UTC.

Init Params:
    (no parameters)

Pattern:
    An `ISO_TIME` followed by `Z`.
    Equivalent regex: `(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\\.[0-9]+)?Z`

Example:
    UTC_TIME
    # Matches: "14:30:05Z", "14:30:05.123Z"
    # Does not match: "14:30:05", "14:30:05+00:00"
"""

