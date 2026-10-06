from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import QUESTION_MARK
from simplibs.patterns.web.pure.URL_CHARACTER import URL_CHARACTER


URL_QUERY = QUESTION_MARK + ZERO_OR_MORE(URL_CHARACTER | QUESTION_MARK)
"""Regex expression matching the query part of a URL.

Init Params:
    (no parameters)

Pattern:
    `?` followed by any number of `URL_CHARACTER`s.
    Equivalent regex: `\\?(?:[a-zA-Z0-9\\-._~%/:@=!$&'()*+,;]|\\?)*`

Example:
    URL_QUERY
    # Matches: "?a=1&b=2", "?"
    # Does not match: "a=1", "?a b", "?#x"
"""

