from simplibs.regex.presets.quantifiers import OPTIONAL
# Patterns
from simplibs.patterns.characters import COLON, SPACE
from simplibs.patterns.times.pure.HOUR_12 import HOUR_12
from simplibs.patterns.times.pure.MINUTE import MINUTE
from simplibs.patterns.times.composed.MERIDIEM import MERIDIEM


TWELVE_HOUR_TIME = HOUR_12 + COLON + MINUTE + OPTIONAL(SPACE) + MERIDIEM
"""Regex expression matching a time in 12-hour form with AM/PM.

Init Params:
    (no parameters)

Pattern:
    `HOUR_12`, colon, `MINUTE`, an optional space and `MERIDIEM`.
    Equivalent regex: `(?:0[1-9]|1[0-2]):[0-5][0-9]\\ ?(?:AM|PM)`

Notes:
Example:
    TWELVE_HOUR_TIME
    # Matches: "09:30 AM", "12:00PM"
    # Does not match: "13:00 PM", "09:30", "9:30 AM"
"""

_DESIGN_NOTES = """
If unpadded 12-hour times are added, keep the current zero-padded form unchanged and expose the
broader syntax as a distinct term.
"""

