from simplibs.regex.base_class import Regex
from simplibs.regex.presets.quantifiers import EXACTLY
# Patterns
from simplibs.patterns.characters import DOT
from simplibs.patterns.identifiers.pure.IDENTIFIER import IDENTIFIER


def QUALIFIED_IDENTIFIER_OF(parts: int) -> Regex:
    """Build a regex expression matching a dotted identifier with an exact number of parts.

    Init Params:
        parts (int): How many identifiers the dotted name consists of (at least 1).

    Pattern:
        An `IDENTIFIER` followed by exactly `parts - 1` (dot, `IDENTIFIER`) pairs.

    Example:
        pattern = QUALIFIED_IDENTIFIER_OF(3)
        # Regex: [a-zA-Z_][a-zA-Z0-9_]*(?:\\.[a-zA-Z_][a-zA-Z0-9_]*){2}
        # Matches: "a.b.c", "os.path.join"
        # Does not match: "a.b", "a.b.c.d", "abc"
    """
    return IDENTIFIER + EXACTLY(DOT + IDENTIFIER, parts - 1)

