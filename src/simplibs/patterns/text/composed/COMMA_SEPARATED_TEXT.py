from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import COMMA
from simplibs.patterns.text.pure.WORD import WORD


COMMA_SEPARATED_TEXT = WORD + ZERO_OR_MORE(COMMA + WORD)
"""Regex expression matching words separated by commas.

Init Params:
    (no parameters)

Pattern:
    A `WORD`, then any number of (comma, `WORD`) pairs, with no spaces.
    Equivalent regex: `\\w+(?:,\\w+)*`

Example:
    COMMA_SEPARATED_TEXT
    # Matches: "a", "a,b,c", "one,two"
    # Does not match: "a, b", "a,,b", "a,", ""
"""

