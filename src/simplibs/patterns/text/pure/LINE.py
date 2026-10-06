from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE


LINE = ZERO_OR_MORE(ANY)
"""Regex expression matching one line of text, possibly empty.

Init Params:
    (no parameters)

Pattern:
    Zero or more characters that are not a line break.
    Equivalent regex: `.*`

Example:
    LINE
    # Matches: "", "one line", "a b c"
    # Does not match: "a\\nb"
"""

