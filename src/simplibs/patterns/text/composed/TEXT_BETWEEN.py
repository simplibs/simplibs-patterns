from simplibs.regex.base_class import Regex
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.containers.Repeat import RepeatMode
from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE


def TEXT_BETWEEN(opening: str, closing: str) -> Regex:
    """Build a regex expression matching text enclosed by an opening and a closing string.

    Init Params:
        opening (str): The text that starts the enclosed part.
        closing (str): The text that ends the enclosed part.

    Pattern:
        1. The literal `opening`.
        2. As few characters as possible (lazy).
        3. The literal `closing`.

    Notes:
        Lazy: takes the nearest closing string, so `a <b> c <d>` yields `<b>`, not everything up to the last `>`.
        The delimiters are part of the match.

    Example:
        pattern = TEXT_BETWEEN("<", ">")
        # Regex: <.*?>
        # Finds "<b>" in "a <b> c <d>"
        # No match in: "no brackets"
    """
    return Literal(opening) + ZERO_OR_MORE(ANY, mode=RepeatMode.LAZY) + Literal(closing)

