from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import EXACTLY


ULID = CharacterClass(CharacterRange("0", "7")) + EXACTLY(CharacterClass(CharacterRange("0", "9"), CharacterRange("A", "H"), Literal("J"), Literal("K"), Literal("M"), Literal("N"), CharacterRange("P", "T"), CharacterRange("V", "Z"),), 25,)
"""Regex expression matching a ULID.

Init Params:
    (no parameters)

Pattern:
    26 characters of Crockford Base32 (no `I`, `L`, `O`, `U`); the first one is `0`–`7`.
    Equivalent regex: `[0-7][0-9A-HJKMNP-TV-Z]{25}`

Notes:
    Only uppercase Crockford Base32 characters are accepted; lowercase ULIDs are not matched.

Example:
    ULID
    # Matches: "01ARZ3NDEKTSV4RRFFQ69G5FAV", "7ZZZZZZZZZZZZZZZZZZZZZZZZZ"
    # Does not match: "81ARZ3NDEKTSV4RRFFQ69G5FAV", "01ARZ3NDEKTSV4RRFFQ69G5FAI", "01arz3ndektsv4rrffq69g5fav", "01ARZ3NDEKTSV4RRFFQ69G5FA"
"""

