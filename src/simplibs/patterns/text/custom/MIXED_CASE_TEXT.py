from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.lookaround import LOOKAHEAD
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
from simplibs.regex.presets.character_classes import LOWERCASE_LETTER, UPPERCASE_LETTER
# Patterns
from simplibs.patterns.text.pure.NON_EMPTY_TEXT import NON_EMPTY_TEXT


MIXED_CASE_TEXT = LOOKAHEAD(ZERO_OR_MORE(ANY) + LOWERCASE_LETTER) + LOOKAHEAD(ZERO_OR_MORE(ANY) + UPPERCASE_LETTER) + NON_EMPTY_TEXT
"""Regex expression matching text containing both lowercase and uppercase letters.

Init Params:
    (no parameters)

Pattern:
    Non-empty text in which at least one lowercase and at least one uppercase ASCII letter occur, in any order.
    Equivalent regex: `(?=.*[a-z])(?=.*[A-Z]).+`

Notes:
    Checks presence, not a particular style (camelCase, PascalCase…).

Example:
    MIXED_CASE_TEXT
    # Matches: "Hello", "aB", "fooBar!"
    # Does not match: "hello", "HELLO", "123", ""
"""

