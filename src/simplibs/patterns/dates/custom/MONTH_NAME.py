from simplibs.regex.elements.Literal import Literal


MONTH_NAME = Literal("January") | Literal("February") | Literal("March") | Literal("April") | Literal("May") | Literal("June") | Literal("July") | Literal("August") | Literal("September") | Literal("October") | Literal("November") | Literal("December")
"""Regex expression matching an English month name.

Init Params:
    (no parameters)

Pattern:
    A full English month name, capitalised: `January` … `December`.
    Equivalent regex: `January|February|March|April|May|June|July|August|September|October|November|December`

Notes:
    English and case-sensitive. Use the `IGNORECASE` flag for case-insensitive matching.

Example:
    MONTH_NAME
    # Matches: "January", "May", "December"
    # Does not match: "january", "Mar", "Sept"
"""

_DESIGN_NOTES = """
Locale-specific month names are intentionally outside this term's scope. If broader locale
support is added later, it should be represented explicitly rather than changing the meaning of
`MONTH_NAME`.
"""

