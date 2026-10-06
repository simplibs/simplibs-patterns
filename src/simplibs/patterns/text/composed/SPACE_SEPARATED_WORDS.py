from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import SPACE
from simplibs.patterns.text.pure.WORD import WORD


SPACE_SEPARATED_WORDS = WORD + ZERO_OR_MORE(SPACE + WORD)
"""Regex expression matching words separated by exactly one space.

Init Params:
    (no parameters)

Pattern:
    A `WORD`, then any number of (one space, `WORD`) pairs.
    Equivalent regex: `\\w+(?:\\ \\w+)*`

Example:
    SPACE_SEPARATED_WORDS
    # Matches: "hello", "a b c"
    # Does not match: "a  b", "a\\tb", ""
"""

