from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
from simplibs.regex.presets.literals import TAB


HTTP_HEADER_VALUE = ZERO_OR_MORE(CharacterClass(TAB, CharacterRange(" ", "~")))
"""Regex expression matching an HTTP header field value.

Init Params:
    (no parameters)

Pattern:
    Printable ASCII characters and tabs; may be empty.
    Equivalent regex: `[\\t -~]*`

Notes:
    Only printable ASCII characters and tabs are matched; obsolete line folding and non-ASCII header
    bytes are not supported.

Example:
    HTTP_HEADER_VALUE
    # Matches: "text/html; charset=utf-8", ""
    # Does not match: "a\\nb"
"""

