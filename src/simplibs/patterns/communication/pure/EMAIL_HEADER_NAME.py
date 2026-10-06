from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.presets.quantifiers import ONE_OR_MORE


EMAIL_HEADER_NAME = ONE_OR_MORE(CharacterClass(CharacterRange("!", "9"), CharacterRange(";", "~")))
"""Regex expression matching an email header field name.

Init Params:
    (no parameters)

Pattern:
    One or more printable ASCII characters except space and colon.
    Equivalent regex: `[!-9;-~]+`

Example:
    EMAIL_HEADER_NAME
    # Matches: "Subject", "X-Mailer", "Content-Type"
    # Does not match: "Sub ject", "Name:", ""
"""

