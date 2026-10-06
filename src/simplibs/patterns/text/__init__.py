# Pure:
from .pure.EMPTY_TEXT import EMPTY_TEXT
from .pure.NON_EMPTY_TEXT import NON_EMPTY_TEXT
from .pure.CHARACTER import CHARACTER
from .pure.CHARACTERS import CHARACTERS
from .pure.WORD import WORD
from .pure.SINGLE_WORD import SINGLE_WORD
from .pure.LINE import LINE
from .pure.SINGLE_LINE import SINGLE_LINE
from .pure.WHITESPACE_TEXT import WHITESPACE_TEXT
from .pure.NON_WHITESPACE_TEXT import NON_WHITESPACE_TEXT
from .pure.ALPHANUMERIC_TEXT import ALPHANUMERIC_TEXT
from .pure.ALPHA_TEXT import ALPHA_TEXT
from .pure.DIGIT_TEXT import DIGIT_TEXT
from .pure.LOWERCASE_TEXT import LOWERCASE_TEXT
from .pure.UPPERCASE_TEXT import UPPERCASE_TEXT
from .pure.IDENTIFIER_LIKE_TEXT import IDENTIFIER_LIKE_TEXT
from .pure.SINGLE_QUOTED_TEXT import SINGLE_QUOTED_TEXT
from .pure.DOUBLE_QUOTED_TEXT import DOUBLE_QUOTED_TEXT
from .pure.PARENTHESIZED_TEXT import PARENTHESIZED_TEXT
from .pure.BRACKETED_TEXT import BRACKETED_TEXT
from .pure.BRACED_TEXT import BRACED_TEXT
# Composed:
from .composed.QUOTED_TEXT import QUOTED_TEXT
from .composed.WORDS import WORDS
from .composed.SPACE_SEPARATED_WORDS import SPACE_SEPARATED_WORDS
from .composed.WORD_LIST import WORD_LIST
from .composed.COMMA_SEPARATED_TEXT import COMMA_SEPARATED_TEXT
from .composed.MULTILINE_TEXT import MULTILINE_TEXT
from .composed.WHOLE_WORD import WHOLE_WORD
from .composed.TEXT_BETWEEN import TEXT_BETWEEN
from .composed.PREFIXED_TEXT import PREFIXED_TEXT
from .composed.SUFFIXED_TEXT import SUFFIXED_TEXT
from .composed.TEXT_OF_LENGTH import TEXT_OF_LENGTH
from .composed.TEXT_OF_LENGTH_RANGE import TEXT_OF_LENGTH_RANGE
# Custom:
from .custom.MIXED_CASE_TEXT import MIXED_CASE_TEXT
from .custom.CSV_LINE import CSV_LINE
from .custom.TEXT_UNTIL import TEXT_UNTIL
from .custom.TEXT_AFTER import TEXT_AFTER
from .custom.TEXT_BEFORE import TEXT_BEFORE


_DESIGN_NOTES = """
# Text Patterns Sub-Package

## Purpose
Runs of text — words, lines, quoted and bracketed text, character-class texts, and parametrized helpers such as `WHOLE_WORD`, `TEXT_BETWEEN` or `TEXT_UNTIL`.

## Layout
`pure/` named concepts · `composed/` combinations of other terms and parametrized factories · `custom/` terms that needed a semantic decision

## Internal Components Registry

| Component               | Type             | Description                                              |
| :---------------------- | :--------------- | :------------------------------------------------------- |
| `EMPTY_TEXT`            | Regex Expression | An empty string.                                         |
| `NON_EMPTY_TEXT`        | Regex Expression | One or more characters.                                  |
| `CHARACTER`             | Regex Expression | A single character.                                      |
| `CHARACTERS`            | Regex Expression | One or more characters.                                  |
| `WORD`                  | Regex Expression | A single word.                                           |
| `SINGLE_WORD`           | Regex Expression | A single word.                                           |
| `LINE`                  | Regex Expression | One line of text, possibly empty.                        |
| `SINGLE_LINE`           | Regex Expression | A single line of text.                                   |
| `WHITESPACE_TEXT`       | Regex Expression | Text made only of whitespace.                            |
| `NON_WHITESPACE_TEXT`   | Regex Expression | Text without any whitespace.                             |
| `ALPHANUMERIC_TEXT`     | Regex Expression | Text made only of ASCII letters and digits.              |
| `ALPHA_TEXT`            | Regex Expression | Text made only of ASCII letters.                         |
| `DIGIT_TEXT`            | Regex Expression | Text made only of ASCII digits.                          |
| `LOWERCASE_TEXT`        | Regex Expression | Text made only of lowercase ASCII letters.               |
| `UPPERCASE_TEXT`        | Regex Expression | Text made only of uppercase ASCII letters.               |
| `MIXED_CASE_TEXT`       | Regex Expression | Text containing both lowercase and uppercase letters.    |
| `IDENTIFIER_LIKE_TEXT`  | Regex Expression | Text shaped like an identifier.                          |
| `SINGLE_QUOTED_TEXT`    | Regex Expression | Text in single quotes.                                   |
| `DOUBLE_QUOTED_TEXT`    | Regex Expression | Text in double quotes.                                   |
| `QUOTED_TEXT`           | Regex Expression | Text in single or double quotes.                         |
| `PARENTHESIZED_TEXT`    | Regex Expression | Text in parentheses.                                     |
| `BRACKETED_TEXT`        | Regex Expression | Text in square brackets.                                 |
| `BRACED_TEXT`           | Regex Expression | Text in curly braces.                                    |
| `WORDS`                 | Regex Expression | One or more words separated by whitespace.               |
| `SPACE_SEPARATED_WORDS` | Regex Expression | Words separated by exactly one space.                    |
| `WORD_LIST`             | Regex Expression | A list of words.                                         |
| `COMMA_SEPARATED_TEXT`  | Regex Expression | Words separated by commas.                               |
| `CSV_LINE`              | Regex Expression | One line of comma-separated fields.                      |
| `MULTILINE_TEXT`        | Regex Expression | Text spanning two or more lines.                         |
| `WHOLE_WORD`            | Factory          | Builds the given text as a complete word.                |
| `TEXT_BETWEEN`          | Factory          | Builds text enclosed by an opening and a closing string. |
| `PREFIXED_TEXT`         | Factory          | Builds text that starts with the given prefix.           |
| `SUFFIXED_TEXT`         | Factory          | Builds text that ends with the given suffix.             |
| `TEXT_OF_LENGTH`        | Factory          | Builds text of an exact length.                          |
| `TEXT_OF_LENGTH_RANGE`  | Factory          | Builds text whose length lies in an inclusive range.     |
| `TEXT_UNTIL`            | Factory          | Builds all text up to (not including) the given text.    |
| `TEXT_AFTER`            | Factory          | Builds the text that follows the given text.             |
| `TEXT_BEFORE`           | Factory          | Builds the text that comes before the given text.        |
"""
