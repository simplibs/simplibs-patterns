from simplibs.regex.presets.quantifiers import BETWEEN, ONE_OR_MORE
# Patterns
from simplibs.patterns.characters import EQUALS
from simplibs.patterns.formats.pure.BASE64_URL_CHARACTER import BASE64_URL_CHARACTER


BASE64_URL = ONE_OR_MORE(BASE64_URL_CHARACTER) + BETWEEN(EQUALS, 0, 2)
"""Regex expression matching a URL-safe Base64 string.

Init Params:
    (no parameters)

Pattern:
    One or more URL-safe Base64 characters followed by up to two `=` paddings.
    Equivalent regex: `[A-Za-z0-9\\-_]+={0,2}`

Notes:
    Padding is optional and its count is not checked against the length.

Example:
    BASE64_URL
    # Matches: "aGVsbG8", "a-b_c", "aGVsbG8="
    # Does not match: "a+b", "a/b", ""
"""

