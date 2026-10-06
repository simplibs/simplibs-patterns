from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.quantifiers import ONE_OR_MORE


NON_EMPTY_TEXT = ONE_OR_MORE(ANY)
"""Regex expression matching one or more characters.

Init Params:
    (no parameters)

Pattern:
    One or more characters of any kind (except a newline, unless the `DOTALL` flag is set).
    Equivalent regex: `.+`

Example:
    NON_EMPTY_TEXT
    # Matches: "a", "Hello, world!"
    # Does not match: ""
"""

