from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
from simplibs.regex.presets.literals import CARRIAGE_RETURN, NEWLINE
# Patterns
from simplibs.patterns.characters import COMMA


CSV_LINE = ZERO_OR_MORE(CharacterClass(COMMA, CARRIAGE_RETURN, NEWLINE, negate=True)) + ZERO_OR_MORE(COMMA + ZERO_OR_MORE(CharacterClass(COMMA, CARRIAGE_RETURN, NEWLINE, negate=True)))
"""Regex expression matching one line of comma-separated fields.

Init Params:
    (no parameters)

Pattern:
    Fields made of any characters except comma and line breaks, separated by commas. Fields may be empty.
    Equivalent regex: `[^,\\r\\n]*(?:,[^,\\r\\n]*)*`

Notes:
    Simplified: quoted fields that contain commas are not supported.

Example:
    CSV_LINE
    # Matches: "a,b,c", "a,,c", "single", ""
    # Does not match: "a\\nb"
"""

_DESIGN_NOTES = """
A full CSV pattern would need quoted-field handling and escaping rules. Keep this term
deliberately simple unless a dedicated CSV grammar is introduced.
"""

