from simplibs.regex.presets.groups import NON_CAPTURING
from simplibs.regex.presets.quantifiers import EXACTLY, ONE_OR_MORE, OPTIONAL
# Patterns
from simplibs.patterns.characters import EQUALS
from simplibs.patterns.formats.pure.BASE64_CHARACTER import BASE64_CHARACTER


_TAIL = (
    EXACTLY(BASE64_CHARACTER, 2) + EXACTLY(EQUALS, 2)
    | EXACTLY(BASE64_CHARACTER, 3) + EQUALS
)

BASE64 = ONE_OR_MORE(NON_CAPTURING(EXACTLY(BASE64_CHARACTER, 4))) + OPTIONAL(_TAIL) | _TAIL
"""Regex expression matching a padded Base64 string.

Init Params:
    (no parameters)

Pattern:
    Groups of four Base64 characters, optionally ended by a padded tail (`xx==` or `xxx=`).
    Equivalent regex: `(?:[A-Za-z0-9+/]{4})+(?:[A-Za-z0-9+/]{2}={2}|[A-Za-z0-9+/]{3}=)?|[A-Za-z0-9+/]{2}={2}|[A-Za-z0-9+/]{3}=`

Notes:
    Only standard Base64 syntax with optional `=` padding is matched; line-wrapped and unpadded
    variants are not included.

Example:
    BASE64
    # Matches: "aGVsbG8=", "aGVsbG8gd29ybGQ=", "QUJD", "YQ=="
    # Does not match: "aGVsbG8", "a", "not base64!", ""
"""

