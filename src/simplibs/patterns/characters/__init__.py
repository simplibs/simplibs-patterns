# Pure:
from .pure.DECIMAL_DIGIT import DECIMAL_DIGIT
from .pure.NON_ZERO_DIGIT import NON_ZERO_DIGIT
from .pure.BINARY_DIGIT import BINARY_DIGIT
from .pure.OCTAL_DIGIT import OCTAL_DIGIT
from .pure.SPACE import SPACE
from .pure.PLUS_SIGN import PLUS_SIGN
from .pure.MINUS_SIGN import MINUS_SIGN
from .pure.DASH import DASH
from .pure.DOT import DOT
from .pure.COMMA import COMMA
from .pure.COLON import COLON
from .pure.SEMICOLON import SEMICOLON
from .pure.SLASH import SLASH
from .pure.SINGLE_QUOTE import SINGLE_QUOTE
from .pure.DOUBLE_QUOTE import DOUBLE_QUOTE
from .pure.UNDERSCORE import UNDERSCORE
from .pure.AT_SIGN import AT_SIGN
from .pure.HASH_SIGN import HASH_SIGN
from .pure.DOLLAR import DOLLAR
from .pure.PERCENT import PERCENT
from .pure.AMPERSAND import AMPERSAND
from .pure.ASTERISK import ASTERISK
from .pure.EQUALS import EQUALS
from .pure.PIPE import PIPE
from .pure.CARET import CARET
from .pure.TILDE import TILDE
from .pure.QUESTION_MARK import QUESTION_MARK
from .pure.PARENTHESIS import PARENTHESIS
from .pure.BRACKET import BRACKET
from .pure.BRACE import BRACE
from .pure.PUNCTUATION import PUNCTUATION
from .pure.SYMBOL import SYMBOL
from .pure.UNICODE_LETTER import UNICODE_LETTER
# Composed:
from .composed.SIGN import SIGN
from .composed.QUOTE import QUOTE
from .composed.SPECIAL_CHARACTER import SPECIAL_CHARACTER
# Custom:
from .custom.ESCAPED_CHARACTER import ESCAPED_CHARACTER


_DESIGN_NOTES = """
# Characters Patterns Sub-Package

## Purpose
Single characters and character classes — digits, letters, whitespace, punctuation, symbols and the escape syntax. Every other domain is built on these.

## Layout
`pure/` named concepts · `composed/` combinations of other terms and parametrized factories · `custom/` terms that needed a semantic decision

## Internal Components Registry

| Component            | Type             | Description                                        |
| :------------------- | :--------------- | :------------------------------------------------- |
| `DECIMAL_DIGIT`      | Regex Expression | A single ASCII decimal digit.                      |
| `NON_ZERO_DIGIT`     | Regex Expression | A single ASCII digit from 1 to 9.                  |
| `BINARY_DIGIT`       | Regex Expression | A single binary digit.                             |
| `OCTAL_DIGIT`        | Regex Expression | A single octal digit.                              |
| `SPACE`              | Regex Expression | A single space character.                          |
| `PLUS_SIGN`          | Regex Expression | The plus sign character.                           |
| `MINUS_SIGN`         | Regex Expression | The minus sign character.                          |
| `DASH`               | Regex Expression | The dash (hyphen-minus) character.                 |
| `DOT`                | Regex Expression | The dot character.                                 |
| `COMMA`              | Regex Expression | The comma character.                               |
| `COLON`              | Regex Expression | The colon character.                               |
| `SEMICOLON`          | Regex Expression | The semicolon character.                           |
| `SLASH`              | Regex Expression | The slash character.                               |
| `BACKSLASH`          | Regex Expression | The backslash character.                           |
| `SINGLE_QUOTE`       | Regex Expression | The single quote character.                        |
| `DOUBLE_QUOTE`       | Regex Expression | The double quote character.                        |
| `UNDERSCORE`         | Regex Expression | The underscore character.                          |
| `AT_SIGN`            | Regex Expression | The at sign character.                             |
| `HASH_SIGN`          | Regex Expression | The hash sign character.                           |
| `DOLLAR`             | Regex Expression | The dollar sign character.                         |
| `PERCENT`            | Regex Expression | The percent sign character.                        |
| `AMPERSAND`          | Regex Expression | The ampersand character.                           |
| `ASTERISK`           | Regex Expression | The asterisk character.                            |
| `EQUALS`             | Regex Expression | The equals sign character.                         |
| `PIPE`               | Regex Expression | The pipe character.                                |
| `CARET`              | Regex Expression | The caret character.                               |
| `TILDE`              | Regex Expression | The tilde character.                               |
| `QUESTION_MARK`      | Regex Expression | The question mark character.                       |
| `PARENTHESIS`        | Regex Expression | A single parenthesis.                              |
| `BRACKET`            | Regex Expression | A single square bracket.                           |
| `BRACE`              | Regex Expression | A single curly brace.                              |
| `PUNCTUATION`        | Regex Expression | A single punctuation character.                    |
| `SYMBOL`             | Regex Expression | A single symbol character.                         |
| `UNICODE_LETTER`     | Regex Expression | A single letter of any language.                   |
| `SIGN`               | Regex Expression | A single sign character.                           |
| `QUOTE`              | Regex Expression | A single quote character of either kind.           |
| `SPECIAL_CHARACTER`  | Regex Expression | A single punctuation or symbol character.          |
| `ESCAPED_CHARACTER`  | Regex Expression | A single backslash escape sequence.                |
"""
