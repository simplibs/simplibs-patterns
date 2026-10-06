# Patterns
from simplibs.patterns.characters import COLON
from simplibs.patterns.times.pure.SECOND import SECOND
from simplibs.patterns.times.pure.TIME import TIME


TIME_WITH_SECONDS = TIME + COLON + SECOND
"""Regex expression matching a time in HH:MM:SS form.

Init Params:
    (no parameters)

Pattern:
    A `TIME`, colon, `SECOND`.
    Equivalent regex: `(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]`

Example:
    TIME_WITH_SECONDS
    # Matches: "00:00:00", "14:30:05"
    # Does not match: "14:30", "14:30:60"
"""

