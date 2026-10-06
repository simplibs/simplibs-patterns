from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.character_types import WORD_CHARACTER
# Patterns
from simplibs.patterns.characters import HASH_SIGN


HASHTAG = HASH_SIGN + ONE_OR_MORE(WORD_CHARACTER)
"""Regex expression matching a hashtag.

Init Params:
    (no parameters)

Pattern:
    `#` followed by one or more word characters (Unicode-aware).
    Equivalent regex: `\\#\\w+`

Example:
    HASHTAG
    # Matches: "#python", "#2026", "#ahoj_světe"
    # Does not match: "python", "#", "# tag"
"""

