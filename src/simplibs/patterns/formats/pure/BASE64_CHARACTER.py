from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
# Patterns
from simplibs.patterns.characters import PLUS_SIGN, SLASH


BASE64_CHARACTER = CharacterClass(CharacterRange("A", "Z"), CharacterRange("a", "z"), CharacterRange("0", "9"), PLUS_SIGN, SLASH)
"""Regex expression matching a character of the standard Base64 alphabet.

Init Params:
    (no parameters)

Pattern:
    `A`–`Z`, `a`–`z`, `0`–`9`, `+` or `/`.
    Equivalent regex: `[A-Za-z0-9+/]`

Example:
    BASE64_CHARACTER
    # Matches: "A", "z", "5", "+"
    # Does not match: "-", "_", "="
"""

