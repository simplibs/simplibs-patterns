from simplibs.regex.presets.quantifiers import BETWEEN
from simplibs.regex.presets.character_classes import LETTER


TOP_LEVEL_DOMAIN = BETWEEN(LETTER, 2, 63)
"""Regex expression matching a top-level domain.

Init Params:
    (no parameters)

Pattern:
    2–63 ASCII letters (e.g. `com`, `cz`, `museum`).
    Equivalent regex: `[a-zA-Z]{2,63}`

Notes:
    Only ASCII-letter TLDs are matched; Unicode TLDs and punycode forms such as `xn--...` are not
    supported.

Example:
    TOP_LEVEL_DOMAIN
    # Matches: "com", "cz", "museum"
    # Does not match: "c", "123", "co.uk", ""
"""

