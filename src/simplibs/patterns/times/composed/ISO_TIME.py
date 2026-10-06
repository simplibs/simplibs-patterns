from simplibs.regex.presets.quantifiers import OPTIONAL
# Patterns
from simplibs.patterns.characters import DOT
from simplibs.patterns.numbers import INTEGER
from simplibs.patterns.times.composed.TIME_WITH_SECONDS import TIME_WITH_SECONDS


ISO_TIME = TIME_WITH_SECONDS + OPTIONAL(DOT + INTEGER)
"""Regex expression matching a time in ISO 8601 form.

Init Params:
    (no parameters)

Pattern:
    A `TIME_WITH_SECONDS`, optionally followed by a dot and fraction digits.
    Equivalent regex: `(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\\.[0-9]+)?`

Example:
    ISO_TIME
    # Matches: "14:30:05", "14:30:05.123"
    # Does not match: "14:30", "14:30:05."
"""

