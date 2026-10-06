from simplibs.regex.base_class import Regex
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ONE_OR_MORE, OPTIONAL, ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import (
    ASTERISK,
    COMMA,
    DOT,
    SPACE,
)
from simplibs.patterns.identifiers import IDENTIFIER, NAMESPACE
from simplibs.patterns.programming.custom.STRING_LITERAL import STRING_LITERAL
from simplibs.patterns.programming.enums.Language import Language


_SPACES = ONE_OR_MORE(SPACE)
_PYTHON_ALIAS = OPTIONAL(_SPACES + Literal("as") + _SPACES + IDENTIFIER)
_PYTHON_ITEM = IDENTIFIER + _PYTHON_ALIAS
_PYTHON_SOURCE = ZERO_OR_MORE(DOT) + NAMESPACE | ONE_OR_MORE(DOT)
_JAVASCRIPT_ITEM = IDENTIFIER + OPTIONAL(_SPACES + Literal("as") + _SPACES + IDENTIFIER)
_JAVASCRIPT_STRING = STRING_LITERAL(Language.JAVASCRIPT)
_IMPORTS = {
    Language.PYTHON: (
        Literal("import") + _SPACES + NAMESPACE + _PYTHON_ALIAS
        | Literal("from") + _SPACES + _PYTHON_SOURCE + _SPACES + Literal("import") + _SPACES
        + (
            ASTERISK
            | _PYTHON_ITEM + ZERO_OR_MORE(COMMA + ZERO_OR_MORE(SPACE) + _PYTHON_ITEM)
        )
    ),
    Language.JAVASCRIPT: (
        Literal("import") + _SPACES
        + (
            IDENTIFIER
            | Literal("{") + ZERO_OR_MORE(SPACE) + _JAVASCRIPT_ITEM
            + ZERO_OR_MORE(COMMA + ZERO_OR_MORE(SPACE) + _JAVASCRIPT_ITEM)
            + ZERO_OR_MORE(SPACE) + Literal("}")
            | ASTERISK + _SPACES + Literal("as") + _SPACES + IDENTIFIER
        )
        + _SPACES + Literal("from") + _SPACES + _JAVASCRIPT_STRING
        | Literal("import") + _SPACES + _JAVASCRIPT_STRING
    ),
}

def IMPORT(language: Language) -> Regex:
    """Build a regex expression matching an import statement in the given language.

    Init Params:
        language (Language): The programming language whose import syntax is used.

    Pattern:
        Python: `import a.b [as c]` or `from a.b import x [as y], z` (relative dots and `*` allowed).
        JavaScript: `import x from "m"`, `import { a, b as c } from "m"`, `import * as ns from "m"` or `import "m"`.

    Notes:
        Matches one statement on one line. Parenthesised multi-line Python imports and JavaScript default-plus-named forms (`import a, { b } from "m"`) are not covered.

    Example:
        pattern = IMPORT(Language.PYTHON)
        # Matches: "import os", "import os.path as p", "from os import path", "from simplibs.patterns. import x"
        # Does not match: "import", "from os", "importos", "import os as"
    """
    return _IMPORTS[language]


_DESIGN_NOTES = """
Additional import forms can be added as language-specific variants. Keep the current single-line
forms narrow so that `IMPORT` does not become a language parser.
"""

