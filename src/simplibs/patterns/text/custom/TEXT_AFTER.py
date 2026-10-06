from simplibs.regex.base_class import Regex
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.lookaround import LOOKBEHIND
# Patterns
from simplibs.patterns.text.pure.NON_EMPTY_TEXT import NON_EMPTY_TEXT


def TEXT_AFTER(text: str) -> Regex:
    """Build a regex expression matching the text that follows the given text.

    Init Params:
        text (str): The literal text that must directly precede the match.

    Pattern:
        1. A lookbehind requiring `text` right before the match.
        2. The rest of the line (at least one character).

    Notes:
        The preceding text is required but not part of the match.

    Example:
        pattern = TEXT_AFTER("key=")
        # Regex: (?<=key=).+
        # Finds "value" in "key=value"
        # No match in: "nothing here"
    """
    return LOOKBEHIND(Literal(text)) + NON_EMPTY_TEXT

