from simplibs.regex.base_class import Regex
from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.quantifiers import EXACTLY


def TEXT_OF_LENGTH(length: int) -> Regex:
    """Build a regex expression matching text of an exact length.

    Init Params:
        length (int): The exact number of characters.

    Pattern:
        Exactly `length` characters of any kind.

    Example:
        pattern = TEXT_OF_LENGTH(3)
        # Regex: .{3}
        # Matches: "abc", "123"
        # Does not match: "ab", "abcd"
    """
    return EXACTLY(ANY, length)

