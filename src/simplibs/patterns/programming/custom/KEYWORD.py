from simplibs.regex.base_class import Regex
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.containers.Alternation import Alternation
from simplibs.regex.presets.anchors import WORD_BOUNDARY
# Patterns
from simplibs.patterns.programming.enums.Language import Language


_PYTHON_KEYWORDS = ("False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield")
_JAVASCRIPT_KEYWORDS = ("async", "await", "break", "case", "catch", "class", "const", "continue", "debugger", "default", "delete", "do", "else", "export", "extends", "finally", "for", "function", "if", "import", "in", "instanceof", "let", "new", "return", "static", "super", "switch", "this", "throw", "try", "typeof", "var", "void", "while", "with", "yield")
_KEYWORDS = {
    Language.PYTHON: WORD_BOUNDARY + Alternation(*(Literal(word) for word in _PYTHON_KEYWORDS)) + WORD_BOUNDARY,
    Language.JAVASCRIPT: WORD_BOUNDARY + Alternation(*(Literal(word) for word in _JAVASCRIPT_KEYWORDS)) + WORD_BOUNDARY,
}

def KEYWORD(language: Language) -> Regex:
    """Build a regex expression matching a reserved keyword of the given language.

    Init Params:
        language (Language): The programming language whose keywords are used.

    Pattern:
        Any reserved word of the language, as a whole word.

    Notes:
        Hard keywords only. Soft keywords (Python `match`, `case`, `type`) and the literals `True` / `None` are not special-cased beyond the list.

    Example:
        pattern = KEYWORD(Language.PYTHON)
        # Finds "def" in "def main():"
        # Finds "lambda" in "x = lambda: 0"
        # No match in: "define", "x = 1"
    """
    return _KEYWORDS[language]


_DESIGN_NOTES = """
Keyword tables are version-sensitive. If broader language/version coverage is added, keep the
source of the keyword set explicit rather than embedding version assumptions in the pattern
itself.
"""

