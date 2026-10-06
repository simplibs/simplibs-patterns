from simplibs.regex.presets.quantifiers import ONE_OR_MORE
# Patterns
from simplibs.patterns.characters import DOT
from simplibs.patterns.formats.pure.BASE64_URL_CHARACTER import BASE64_URL_CHARACTER


_SEGMENT = ONE_OR_MORE(BASE64_URL_CHARACTER)

JWT = _SEGMENT + DOT + _SEGMENT + DOT + _SEGMENT
"""Regex expression matching a JSON Web Token.

Init Params:
    (no parameters)

Pattern:
    Three Base64URL segments separated by dots (`header.payload.signature`).
    Equivalent regex: `[A-Za-z0-9\\-_]+\\.[A-Za-z0-9\\-_]+\\.[A-Za-z0-9\\-_]+`

Notes:
    Only the shape is checked; the segments are not decoded or verified.

    Only three non-empty Base64URL segments are matched, so a JWT with an empty signature segment is
    excluded.

Example:
    JWT
    # Matches: "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"
    # Does not match: "a.b", "a.b.c.d", "abc"
"""

