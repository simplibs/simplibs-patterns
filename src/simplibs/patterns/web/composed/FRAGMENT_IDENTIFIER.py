from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import QUESTION_MARK
from simplibs.patterns.web.pure.URL_CHARACTER import URL_CHARACTER


FRAGMENT_IDENTIFIER = ZERO_OR_MORE(URL_CHARACTER | QUESTION_MARK)
"""Regex expression matching the text after the # of a URL.

Init Params:
    (no parameters)

Pattern:
    Any number of `URL_CHARACTER`s or `?`.
    Equivalent regex: `(?:[a-zA-Z0-9\\-._~%/:@=!$&'()*+,;]|\\?)*`

Example:
    FRAGMENT_IDENTIFIER
    # Matches: "section-2", "top", ""
    # Does not match: "a b", "#x"
"""

