# Patterns
from simplibs.patterns.formats.pure.ISBN10 import ISBN10
from simplibs.patterns.formats.pure.ISBN13 import ISBN13


ISBN = ISBN13 | ISBN10
"""Regex expression matching an ISBN-10 or ISBN-13.

Init Params:
    (no parameters)

Pattern:
    `ISBN13` or `ISBN10`.
    Equivalent regex: `97[89][0-9]{10}|[0-9]{9}[0-9Xx]`

Notes:
    Only unhyphenated ISBN-10 and ISBN-13 forms are matched.

Example:
    ISBN
    # Matches: "9780306406157", "0306406152"
    # Does not match: "12345", ""
"""

