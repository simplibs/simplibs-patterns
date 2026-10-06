from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.character_types import WHITESPACE
# Patterns
from simplibs.patterns.characters import AT_SIGN


_PART = ONE_OR_MORE(CharacterClass(AT_SIGN, Literal("<"), Literal(">"), WHITESPACE, negate=True))

MESSAGE_ID = Literal("<") + _PART + AT_SIGN + _PART + Literal(">")
"""Regex expression matching an email Message-ID.

Init Params:
    (no parameters)

Pattern:
    `<`, a part, `@`, a part and `>`, where parts contain no `<`, `>`, `@` or whitespace.
    Equivalent regex: `<[^@<>\\s]+@[^@<>\\s]+>`

Notes:
    The Message-ID syntax is intentionally broader than the full RFC 5322 grammar and does not
    enforce detailed `msg-id` constraints.

Example:
    MESSAGE_ID
    # Matches: "<abc123@mail.example.com>"
    # Does not match: "abc@x", "<abc>", "<a@b@c>"
"""

