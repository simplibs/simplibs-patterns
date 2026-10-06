from simplibs.regex.base_class import Regex
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.lookaround import NEGATIVE_LOOKAHEAD
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE


def TEXT_UNTIL(text: str) -> Regex:
    """Build a regex expression matching all text up to (not including) the given text.

    Init Params:
        text (str): The literal text at which matching stops.

    Pattern:
        Any number of characters, each of which is not the start of `text`.

    Notes:
        The stop text itself is not consumed. Always matches (possibly empty).

    Example:
        pattern = TEXT_UNTIL("=")
        # Regex: (?:(?!=).)*
        # Finds "key" in "key=value"
    """
    return ZERO_OR_MORE(NEGATIVE_LOOKAHEAD(Literal(text)) + ANY)

