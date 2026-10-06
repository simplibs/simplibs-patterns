from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.times.composed.TIMEZONE_OFFSET import TIMEZONE_OFFSET


TIMEZONE = Literal("Z") | TIMEZONE_OFFSET
"""Regex expression matching an ISO 8601 time zone designator.

Init Params:
    (no parameters)

Pattern:
    `Z` (UTC) or a `TIMEZONE_OFFSET`.
    Equivalent regex: `Z|[+\\-](?:[01][0-9]|2[0-3]):[0-5][0-9]`

Example:
    TIMEZONE
    # Matches: "Z", "+02:00", "-05:00"
    # Does not match: "z", "UTC", "+2"
"""

