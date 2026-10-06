from simplibs.regex.base_class import Regex
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.anchors import WORD_BOUNDARY


def WHOLE_WORD(text: str) -> Regex:
    """Build a regex expression matching the given text as a complete word.

    Init Params:
        text (str): The exact text that must appear as a complete word.

    Pattern:
        1. A word boundary before `text`.
        2. The literal `text`.
        3. A word boundary after `text`.

    Notes:
        Word boundaries only exist next to word characters; `text` should start and end with one.

    Example:
        pattern = WHOLE_WORD("Python")
        # Regex: \\bPython\\b
        # Finds "Python" in "Python is great"
        # Finds "Python" in "I love Python"
        # No match in: "CPython", "Pythonic"
    """
    return WORD_BOUNDARY + Literal(text) + WORD_BOUNDARY

