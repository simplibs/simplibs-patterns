from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.quantifiers import EXACTLY
from simplibs.regex.presets.character_classes import HEX_DIGIT
from simplibs.regex.presets.literals import BACKSLASH


ESCAPED_CHARACTER = BACKSLASH + (Literal("x") + EXACTLY(HEX_DIGIT, 2) | Literal("u") + EXACTLY(HEX_DIGIT, 4) | Literal("U") + EXACTLY(HEX_DIGIT, 8) | ANY)
"""Regex expression matching a single backslash escape sequence.

Init Params:
    (no parameters)

Pattern:
    A backslash followed by one of:
    1. `x` and 2 hex digits (`\\xFF`).
    2. `u` and 4 hex digits (`\\u1234`).
    3. `U` and 8 hex digits (`\\U0001F600`).
    4. any other single character (`\\.`, `\\n`, `\\\\`).
    Equivalent regex: `\\\\(?:x[0-9a-fA-F]{2}|u[0-9a-fA-F]{4}|U[0-9a-fA-F]{8}|.)`

Notes:
    Generic escape syntax shared by many languages. Octal and named (`\\N{...}`) 
    escapes are not special-cased; they fall under the last alternative only when 
    a single character follows.

Example:
    ESCAPED_CHARACTER
    # Matches: "\\.", "\\n", "\\xFF", "\\u1234"
    # Does not match: "\\x4", "\\", "n"
"""

_DESIGN_NOTES = """
Language-specific escape grammars may eventually justify dedicated patterns or a language
parameter. Keep `ESCAPED_CHARACTER` language-neutral unless such a distinction becomes
necessary.
"""

