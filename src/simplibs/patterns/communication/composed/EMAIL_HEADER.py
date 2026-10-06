from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import COLON, SPACE
from simplibs.patterns.communication.pure.EMAIL_HEADER_NAME import EMAIL_HEADER_NAME
from simplibs.patterns.communication.pure.EMAIL_HEADER_VALUE import EMAIL_HEADER_VALUE


EMAIL_HEADER = EMAIL_HEADER_NAME + COLON + ZERO_OR_MORE(SPACE) + EMAIL_HEADER_VALUE
"""Regex expression matching an email header line.

Init Params:
    (no parameters)

Pattern:
    An `EMAIL_HEADER_NAME`, `:`, optional spaces and an `EMAIL_HEADER_VALUE`.
    Equivalent regex: `[!-9;-~]+:\\ *.*`

Notes:
    Folded (multi-line) headers are not covered.

Example:
    EMAIL_HEADER
    # Matches: "Subject: Hello", "From:x@y.com", "X-Empty:"
    # Does not match: "no header", "Name value"
"""

