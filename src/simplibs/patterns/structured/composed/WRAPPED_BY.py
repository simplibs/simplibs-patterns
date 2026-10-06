from simplibs.regex.base_class import Regex


def WRAPPED_BY(item: Regex, opening: Regex, closing: Regex) -> Regex:
    """Build a regex expression matching an item wrapped between an opening and a closing expression.

    Init Params:
        item (Regex): The wrapped expression.
        opening (Regex): The expression before the item.
        closing (Regex): The expression after the item.

    Pattern:
        `opening`, then `item`, then `closing`.

    Example:
        pattern = WRAPPED_BY(INTEGER, Literal("<"), Literal(">"))
        # Regex: <[0-9]+>
        # Matches: "<42>"
        # Does not match: "42", "<>", "<42"
    """
    return opening + item + closing

