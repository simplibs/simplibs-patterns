from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.literals import NEWLINE
# Patterns
from simplibs.patterns.text.pure.LINE import LINE


MULTILINE_TEXT = LINE + ONE_OR_MORE(NEWLINE + LINE)
"""Regex expression matching text spanning two or more lines.

Init Params:
    (no parameters)

Pattern:
    A `LINE`, then one or more (newline, `LINE`) pairs.
    Equivalent regex: `.*(?:\\n.*)+`

Example:
    MULTILINE_TEXT
    # Matches: "a\\nb", "a\\n\\nb", "x\\ny\\nz"
    # Does not match: "single line", ""
"""

