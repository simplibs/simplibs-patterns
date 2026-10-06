# Patterns
from simplibs.patterns.characters import COLON
from simplibs.patterns.times.pure.HOUR import HOUR
from simplibs.patterns.times.pure.MINUTE import MINUTE


TIME = HOUR + COLON + MINUTE
"""Regex expression matching a time in HH:MM form.

Init Params:
    (no parameters)

Pattern:
    `HOUR`, colon, `MINUTE` (24-hour).
    Equivalent regex: `(?:[01][0-9]|2[0-3]):[0-5][0-9]`

Example:
    TIME
    # Matches: "00:00", "14:30", "23:59"
    # Does not match: "24:00", "7:30", "14:60", "1430"
"""

