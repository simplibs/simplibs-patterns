from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.presets.quantifiers import BETWEEN, OPTIONAL
from simplibs.regex.presets.character_classes import ALPHANUMERIC
# Patterns
from simplibs.patterns.characters import DASH


DOMAIN_LABEL = ALPHANUMERIC + OPTIONAL(BETWEEN(CharacterClass(CharacterRange("a", "z"), CharacterRange("A", "Z"), CharacterRange("0", "9"), DASH), 0, 61) + ALPHANUMERIC)
"""Regex expression matching a single label of a domain name.

Init Params:
    (no parameters)

Pattern:
    1–63 letters, digits or hyphens; it may not start or end with a hyphen.
    Equivalent regex: `[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?`

Notes:
    ASCII (punycode) labels only.

Example:
    DOMAIN_LABEL
    # Matches: "example", "a", "my-site", "a1"
    # Does not match: "-a", "a-", "", "a_b"
"""

