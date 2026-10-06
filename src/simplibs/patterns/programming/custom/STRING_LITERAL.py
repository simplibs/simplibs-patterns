from simplibs.regex.base_class import Regex
from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
from simplibs.regex.presets.literals import BACKSLASH, NEWLINE
# Patterns
from simplibs.patterns.characters import DOUBLE_QUOTE, SINGLE_QUOTE
from simplibs.patterns.programming.enums.Language import Language


_SINGLE_QUOTED = (
    SINGLE_QUOTE
    + ZERO_OR_MORE(CharacterClass(SINGLE_QUOTE, BACKSLASH, NEWLINE, negate=True) | BACKSLASH + ANY)
    + SINGLE_QUOTE
)
_DOUBLE_QUOTED = (
    DOUBLE_QUOTE
    + ZERO_OR_MORE(CharacterClass(DOUBLE_QUOTE, BACKSLASH, NEWLINE, negate=True) | BACKSLASH + ANY)
    + DOUBLE_QUOTE
)
_BACKTICKED = (
    Literal("`")
    + ZERO_OR_MORE(CharacterClass(Literal("`"), BACKSLASH, negate=True) | BACKSLASH + ANY)
    + Literal("`")
)
_STRING_LITERALS = {
    Language.PYTHON: _SINGLE_QUOTED | _DOUBLE_QUOTED,
    Language.JAVASCRIPT: _SINGLE_QUOTED | _DOUBLE_QUOTED | _BACKTICKED,
}

def STRING_LITERAL(language: Language) -> Regex:
    """Build a regex expression matching a string literal in the given language.

    Init Params:
        language (Language): The programming language whose string syntax is used.

    Pattern:
        A quoted string with backslash escapes: single or double quotes (Python), plus backticks (JavaScript).

    Notes:
        Single-line strings only; prefixes (f"", r"", b""), triple quotes and template-literal interpolation are not covered.

    Example:
        pattern = STRING_LITERAL(Language.PYTHON)
        # Regex: '(?:[^'\\\\n]|\\\\.)*'|"(?:[^"\\\\n]|\\\\.)*"
        # Finds "'hi'" in "x = 'hi'"
        # Finds '"a \\" b"' in 'print("a \\" b")'
        # No match in: "x = 1", "'open"
    """
    return _STRING_LITERALS[language]


_DESIGN_NOTES = """
Triple-quoted strings, prefixed strings and template literals may require dedicated terms or a
broader language-specific string grammar. Keep `STRING_LITERAL` focused on its current single-
line forms.
"""

