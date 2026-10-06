from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import COLON, SPACE
from simplibs.patterns.web.pure.HTTP_HEADER_NAME import HTTP_HEADER_NAME
from simplibs.patterns.web.pure.HTTP_HEADER_VALUE import HTTP_HEADER_VALUE


HTTP_HEADER = HTTP_HEADER_NAME + COLON + ZERO_OR_MORE(SPACE) + HTTP_HEADER_VALUE
"""Regex expression matching an HTTP header line.

Init Params:
    (no parameters)

Pattern:
    A `HTTP_HEADER_NAME`, `:`, optional spaces and a `HTTP_HEADER_VALUE`.
    Equivalent regex: `[a-zA-Z0-9!#$%&'*+\\-.\\^_`|~]+:\\ *[\\t -~]*`

Example:
    HTTP_HEADER
    # Matches: "Content-Type: text/html", "Host:example.com"
    # Does not match: "no header", "Name value"
"""

