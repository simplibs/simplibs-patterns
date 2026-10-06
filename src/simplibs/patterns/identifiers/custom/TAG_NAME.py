from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
from simplibs.regex.presets.character_classes import LETTER
# Patterns
from simplibs.patterns.characters import DASH


TAG_NAME = LETTER + ZERO_OR_MORE(CharacterClass(CharacterRange("a", "z"), CharacterRange("A", "Z"), CharacterRange("0", "9"), DASH))
"""Regex expression matching a markup tag name.

Init Params:
    (no parameters)

Pattern:
    A letter, then letters, digits or hyphens (e.g. `div`, `h1`, `my-element`).
    Equivalent regex: `[a-zA-Z][a-zA-Z0-9\\-]*`

Notes:
    Covers HTML-style names. XML names may also contain `:`, `.` and `_`.

Example:
    TAG_NAME
    # Matches: "div", "h1", "my-element"
    # Does not match: "1div", "-x", "", "a_b"
"""

_DESIGN_NOTES = """
If XML-specific naming is needed, consider a separate XML tag-name term rather than broadening
this HTML-oriented definition.
"""
