from enum import Enum


class Language(Enum):
    """Programming language selector for language-dependent regex expressions.

    Members:
        PYTHON: The Python language.
        JAVASCRIPT: The JavaScript language.

    Example:
        COMMENT(Language.PYTHON)
        # Matches: "# a comment"
        COMMENT(Language.JAVASCRIPT)
        # Matches: "// a comment"
    """

    PYTHON = "python"
    JAVASCRIPT = "javascript"

