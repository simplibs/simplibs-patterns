from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.presets.quantifiers import EXACTLY
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT


HTTP_STATUS_CODE = CharacterClass(CharacterRange("1", "5")) + EXACTLY(DECIMAL_DIGIT, 2)
"""Regex expression matching an HTTP status code.

Init Params:
    (no parameters)

Pattern:
    Three digits from `100` to `599`.
    Equivalent regex: `[1-5][0-9]{2}`

Example:
    HTTP_STATUS_CODE
    # Matches: "200", "404", "503"
    # Does not match: "99", "600", "20", "2000"
"""

