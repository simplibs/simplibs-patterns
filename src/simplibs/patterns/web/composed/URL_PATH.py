from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import SLASH
from simplibs.patterns.web.pure.URL_CHARACTER import URL_CHARACTER


URL_PATH = SLASH + ZERO_OR_MORE(URL_CHARACTER)
"""Regex expression matching the path part of a URL.

Init Params:
    (no parameters)

Pattern:
    A slash followed by any number of `URL_CHARACTER`s.
    Equivalent regex: `/[a-zA-Z0-9\\-._~%/:@=!$&'()*+,;]*`

Example:
    URL_PATH
    # Matches: "/", "/a/b.html", "/path/to/file"
    # Does not match: "a/b", "/a?b", "/a b"
"""

