from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
# Patterns
from simplibs.patterns.characters import DASH, UNDERSCORE


BASE64_URL_CHARACTER = CharacterClass(CharacterRange("A", "Z"), CharacterRange("a", "z"), CharacterRange("0", "9"), DASH, UNDERSCORE)
"""Regex expression matching a character of the URL-safe Base64 alphabet.

Init Params:
    (no parameters)

Pattern:
    `A`–`Z`, `a`–`z`, `0`–`9`, `-` or `_`.
    Equivalent regex: `[A-Za-z0-9\\-_]`

Example:
    BASE64_URL_CHARACTER
    # Matches: "A", "z", "5", "-"
    # Does not match: "+", "/", "="
"""

