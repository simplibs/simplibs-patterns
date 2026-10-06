from simplibs.regex.base_class import Regex
# Patterns
from simplibs.patterns.text import WHOLE_WORD
from simplibs.patterns.programming.enums.Language import Language


_NULL_LITERALS = {
    Language.PYTHON: WHOLE_WORD("None"),
    Language.JAVASCRIPT: WHOLE_WORD("null"),
}

def NULL_LITERAL(language: Language) -> Regex:
    """Build a regex expression matching the null literal of the given language.

    Init Params:
        language (Language): The programming language whose null literal is used.

    Pattern:
        `None` for Python, `null` for JavaScript, as a whole word.

    Example:
        pattern = NULL_LITERAL(Language.JAVASCRIPT)
        # Regex: \\bnull\\b
        # Finds "null" in "x = null"
        # No match in: "x = None", "nullable"
    """
    return _NULL_LITERALS[language]

