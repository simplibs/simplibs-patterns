from simplibs.regex.elements.Literal import Literal


MONTH_ABBREVIATION = Literal("Jan") | Literal("Feb") | Literal("Mar") | Literal("Apr") | Literal("May") | Literal("Jun") | Literal("Jul") | Literal("Aug") | Literal("Sep") | Literal("Oct") | Literal("Nov") | Literal("Dec")
"""Regex expression matching a three-letter English month abbreviation.

Init Params:
    (no parameters)

Pattern:
    `Jan`, `Feb`, `Mar`, … `Dec`.
    Equivalent regex: `Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec`

Notes:
    English, three letters, case-sensitive.

Example:
    MONTH_ABBREVIATION
    # Matches: "Jan", "May", "Dec"
    # Does not match: "jan", "Sept", "January"
"""

