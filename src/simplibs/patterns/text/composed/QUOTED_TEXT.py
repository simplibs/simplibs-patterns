# Patterns
from simplibs.patterns.text.pure.DOUBLE_QUOTED_TEXT import DOUBLE_QUOTED_TEXT
from simplibs.patterns.text.pure.SINGLE_QUOTED_TEXT import SINGLE_QUOTED_TEXT


QUOTED_TEXT = SINGLE_QUOTED_TEXT | DOUBLE_QUOTED_TEXT
"""Regex expression matching text in single or double quotes.

Init Params:
    (no parameters)

Pattern:
    `SINGLE_QUOTED_TEXT` or `DOUBLE_QUOTED_TEXT`.
    Equivalent regex: `'[^']*'|"[^"]*"`

Example:
    QUOTED_TEXT
    # Matches: "'hi'", '"hi"'
    # Does not match: "hi", "'hi\\""
"""

