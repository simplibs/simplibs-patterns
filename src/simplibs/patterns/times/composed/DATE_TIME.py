from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.characters import SPACE
from simplibs.patterns.dates import ISO_DATE
from simplibs.patterns.times.composed.ISO_TIME import ISO_TIME


DATE_TIME = ISO_DATE + CharacterClass(Literal("T"), SPACE) + ISO_TIME
"""Regex expression matching a date and a time together.

Init Params:
    (no parameters)

Pattern:
    An `ISO_DATE`, a `T` or a space, and an `ISO_TIME`.

Notes:
Example:
    DATE_TIME
    # Matches: "2026-09-30T14:30:05", "2026-09-30 14:30:05.5"
    # Does not match: "2026-09-30", "14:30:05", "2026-09-30T14:30"
"""

_DESIGN_NOTES = """
If both `DATE_TIME` and `DATETIME` are introduced, their relationship should be settled at the
naming/API level rather than allowing overlapping aliases to evolve accidentally.
"""

