from simplibs.regex.elements.Literal import Literal


WEEKDAY_ABBREVIATION = Literal("Mon") | Literal("Tue") | Literal("Wed") | Literal("Thu") | Literal("Fri") | Literal("Sat") | Literal("Sun")
"""Regex expression matching a three-letter English weekday abbreviation.

Init Params:
    (no parameters)

Pattern:
    `Mon`, `Tue`, `Wed`, … `Sun`.
    Equivalent regex: `Mon|Tue|Wed|Thu|Fri|Sat|Sun`

Notes:
    English, three letters, case-sensitive.

Example:
    WEEKDAY_ABBREVIATION
    # Matches: "Mon", "Sun"
    # Does not match: "mon", "Monday"
"""

