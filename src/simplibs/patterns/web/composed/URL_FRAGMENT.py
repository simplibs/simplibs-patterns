# Patterns
from simplibs.patterns.characters import HASH_SIGN
from simplibs.patterns.web.composed.FRAGMENT_IDENTIFIER import FRAGMENT_IDENTIFIER


URL_FRAGMENT = HASH_SIGN + FRAGMENT_IDENTIFIER
"""Regex expression matching the fragment part of a URL.

Init Params:
    (no parameters)

Pattern:
    `#` followed by a `FRAGMENT_IDENTIFIER`.
    Equivalent regex: `\\#(?:[a-zA-Z0-9\\-._~%/:@=!$&'()*+,;]|\\?)*`

Example:
    URL_FRAGMENT
    # Matches: "#top", "#section-2", "#"
    # Does not match: "top", "#a b"
"""

