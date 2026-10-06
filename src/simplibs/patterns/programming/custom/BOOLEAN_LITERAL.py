from simplibs.regex.base_class import Regex
# Patterns
from simplibs.patterns.text import WHOLE_WORD
from simplibs.patterns.programming.enums.Language import Language


_BOOLEAN_LITERALS = {
    Language.PYTHON: WHOLE_WORD("True") | WHOLE_WORD("False"),
    Language.JAVASCRIPT: WHOLE_WORD("true") | WHOLE_WORD("false"),
}

def BOOLEAN_LITERAL(language: Language) -> Regex:
    """Build a regex expression matching a boolean literal in the given language.

    Init Params:
        language (Language): The programming language whose boolean literals are used.

    Pattern:
        `True` / `False` for Python, `true` / `false` for JavaScript, as whole words.

    Example:
        pattern = BOOLEAN_LITERAL(Language.PYTHON)
        # Regex: \\bTrue\\b|\\bFalse\\b
        # Finds "True" in "flag = True"
        # No match in: "flag = true", "Truely"
    """
    return _BOOLEAN_LITERALS[language]

