from simplibs.regex.base_class import Regex
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.containers.Repeat import RepeatMode
from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.lookaround import LOOKAHEAD
from simplibs.regex.presets.quantifiers import ONE_OR_MORE


def TEXT_BEFORE(text: str) -> Regex:
    """Build a regex expression matching the text that comes before the given text.

    Init Params:
        text (str): The literal text that must directly follow the match.

    Pattern:
        1. As few characters as possible, at least one (lazy).
        2. A lookahead requiring `text` right after the match.

    Notes:
        The following text is required but not part of the match.

    Example:
        pattern = TEXT_BEFORE("=")
        # Regex: .+?(?==)
        # Finds "key" in "key=value"
        # No match in: "nothing here"
    """
    return ONE_OR_MORE(ANY, mode=RepeatMode.LAZY) + LOOKAHEAD(Literal(text))

