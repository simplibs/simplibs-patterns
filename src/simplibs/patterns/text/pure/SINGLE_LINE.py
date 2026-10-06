# Patterns
from simplibs.patterns.text.pure.LINE import LINE


SINGLE_LINE = LINE
"""Regex expression matching a single line of text.

Init Params:
    (no parameters)

Pattern:
    Same expression as `LINE`; the separate name states the intended role.

Notes:
    Stops at a line break; use `MULTILINE_TEXT` to span several lines.

Example:
    SINGLE_LINE
    # Matches: "", "one line", "a b c"
    # Does not match: "a\\nb"
"""

