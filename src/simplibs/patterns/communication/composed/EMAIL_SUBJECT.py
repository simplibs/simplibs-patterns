from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import SPACE
from simplibs.patterns.communication.pure.SUBJECT import SUBJECT


EMAIL_SUBJECT = Literal("Subject:") + ZERO_OR_MORE(SPACE) + SUBJECT
"""Regex expression matching an email Subject header line.

Init Params:
    (no parameters)

Pattern:
    `Subject:`, optional spaces and a `SUBJECT`.
    Equivalent regex: `Subject:\\ *.+`

Notes:
    Case-sensitive; use the `IGNORECASE` flag because header names are case-insensitive.

Example:
    EMAIL_SUBJECT
    # Matches: "Subject: Meeting tomorrow"
    # Does not match: "Subject:", "From: a"
"""

