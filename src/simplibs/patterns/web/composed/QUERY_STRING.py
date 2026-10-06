from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import AMPERSAND, QUESTION_MARK
from simplibs.patterns.web.pure.QUERY_PARAMETER import QUERY_PARAMETER


QUERY_STRING = QUESTION_MARK + QUERY_PARAMETER + ZERO_OR_MORE(AMPERSAND + QUERY_PARAMETER)
"""Regex expression matching a query string made of key=value parameters.

Init Params:
    (no parameters)

Pattern:
    `?` followed by `QUERY_PARAMETER`s separated by `&`.
    Equivalent regex: `\\?[\\w\\-.~%+]+=[\\w\\-.~%+,:@/]*(?:\\&[\\w\\-.~%+]+=[\\w\\-.~%+,:@/]*)*`

Notes:
    Use `URL_QUERY` for a looser query that is not forced into key=value form.

Example:
    QUERY_STRING
    # Matches: "?a=1&b=2", "?x="
    # Does not match: "a=1", "?", "?a"
"""

