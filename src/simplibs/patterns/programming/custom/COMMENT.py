from simplibs.regex.base_class import Regex
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import HASH_SIGN
from simplibs.patterns.programming.enums.Language import Language


_COMMENTS = {
    Language.PYTHON: HASH_SIGN + ZERO_OR_MORE(ANY),
    Language.JAVASCRIPT: Literal("//") + ZERO_OR_MORE(ANY),
}

def COMMENT(language: Language) -> Regex:
    """Build a regex expression matching a single-line comment in the given language.

    Init Params:
        language (Language): The programming language whose comment syntax is used.

    Pattern:
        From the comment marker (`#` for Python, `//` for JavaScript) to the end of the line.

    Notes:
        A `#` or `//` inside a string literal is not distinguished from a real comment marker.
        Block comments (`/* ... */`) are not covered.

    Example:
        pattern = COMMENT(Language.PYTHON)
        # Regex: \\#.*
        # Finds "# set x" in "x = 1  # set x"
        # No match in: "x = 1"
    """
    return _COMMENTS[language]


_DESIGN_NOTES = """
Block comments and docstrings need multi-line handling. If support is added, it should account
for language-specific syntax rather than turning `COMMENT` into a generic multi-line pattern.
"""

