from simplibs.regex.presets.quantifiers import OPTIONAL
# Patterns
from simplibs.patterns.characters import AT_SIGN
from simplibs.patterns.web.pure.URL_USERINFO import URL_USERINFO
from simplibs.patterns.web.composed.URL_FRAGMENT import URL_FRAGMENT
from simplibs.patterns.web.composed.URL_HOST import URL_HOST
from simplibs.patterns.web.composed.URL_PATH import URL_PATH
from simplibs.patterns.web.composed.URL_PORT import URL_PORT
from simplibs.patterns.web.composed.URL_QUERY import URL_QUERY


URL_LOCATION = OPTIONAL(URL_USERINFO + AT_SIGN) + URL_HOST + OPTIONAL(URL_PORT) + OPTIONAL(URL_PATH) + OPTIONAL(URL_QUERY) + OPTIONAL(URL_FRAGMENT)
"""Regex expression matching everything of a URL after the scheme and ://.

Init Params:
    (no parameters)

Pattern:
    1. An optional `URL_USERINFO` and `@`.
    2. A `URL_HOST`.
    3. An optional `URL_PORT`, `URL_PATH`, `URL_QUERY` and `URL_FRAGMENT`.

Notes:
    Shared by `URL`, `HTTP_URL` and `HTTPS_URL`.

Example:
    URL_LOCATION
    # Matches: "example.com", "user:pw@host:8080/a/b?x=1#top", "[::1]:8080/x"
    # Does not match: "", "http://x", "exa mple.com"
"""

