from simplibs.regex.elements.Literal import Literal


WEEKDAY_NAME = Literal("Monday") | Literal("Tuesday") | Literal("Wednesday") | Literal("Thursday") | Literal("Friday") | Literal("Saturday") | Literal("Sunday")
"""Regex expression matching an English weekday name.

Init Params:
    (no parameters)

Pattern:
    A full English weekday name, capitalised: `Monday` … `Sunday`.
    Equivalent regex: `Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday`

Notes:
    English and case-sensitive.

Example:
    WEEKDAY_NAME
    # Matches: "Monday", "Sunday"
    # Does not match: "monday", "Mon"
"""

