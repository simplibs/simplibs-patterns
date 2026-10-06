# Patterns
from simplibs.patterns.times.pure.AM import AM
from simplibs.patterns.times.pure.PM import PM


MERIDIEM = AM | PM
"""Regex expression matching an AM/PM marker.

Init Params:
    (no parameters)

Pattern:
    `AM` or `PM` (uppercase).
    Equivalent regex: `AM|PM`

Example:
    MERIDIEM
    # Matches: "AM", "PM"
    # Does not match: "am", "A.M.", ""
"""

