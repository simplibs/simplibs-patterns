from simplibs.regex.presets.any_character import ANY


CHARACTER = ANY
"""Regex expression matching a single character.

Init Params:
    (no parameters)

Pattern:
    Exactly one character of any kind (except a newline, unless the `DOTALL` flag is set).
    Equivalent regex: `.`

Example:
    CHARACTER
    # Matches: "a", "!", " "
    # Does not match: "", "ab"
"""

