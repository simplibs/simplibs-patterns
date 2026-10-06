# Patterns
from simplibs.patterns.text import LINE


EMAIL_HEADER_VALUE = LINE
"""Regex expression matching an email header field value.

Init Params:
    (no parameters)

Pattern:
    Same expression as `LINE`; the separate name states the intended role.

Notes:
    One line of text; may be empty.

Example:
    EMAIL_HEADER_VALUE
    # Matches: "", "one line", "a b c"
    # Does not match: "a\\nb"
"""

