# 🔡 `patterns/characters` — Detailed Reference

Single characters and character classes — digits, letters, whitespace, punctuation, symbols and the escape syntax. Every other domain is built on these.

Every card below is the term's full docstring. Terms are grouped by how they are defined: **pure** (a named concept), **composed** (built from other terms, or a parametrized factory) and **custom** (needed a semantic decision — read its notes).

All expressions are `simplibs.regex` objects: combine them with `+` (sequence) and `|` (alternation), wrap them with the presets (`ONE_OR_MORE`, `NAMED_GROUP`, …) and compile with `RegexPattern`.

---

## 🧭 Table of Contents

**pure**:

- [`DECIMAL_DIGIT`](#decimal_digit)
- [`NON_ZERO_DIGIT`](#non_zero_digit)
- [`BINARY_DIGIT`](#binary_digit)
- [`OCTAL_DIGIT`](#octal_digit)
- [`SPACE`](#space)
- [`PLUS_SIGN`](#plus_sign)
- [`MINUS_SIGN`](#minus_sign)
- [`DASH`](#dash)
- [`DOT`](#dot)
- [`COMMA`](#comma)
- [`COLON`](#colon)
- [`SEMICOLON`](#semicolon)
- [`SLASH`](#slash)
- [`SINGLE_QUOTE`](#single_quote)
- [`DOUBLE_QUOTE`](#double_quote)
- [`UNDERSCORE`](#underscore)
- [`AT_SIGN`](#at_sign)
- [`HASH_SIGN`](#hash_sign)
- [`DOLLAR`](#dollar)
- [`PERCENT`](#percent)
- [`AMPERSAND`](#ampersand)
- [`ASTERISK`](#asterisk)
- [`EQUALS`](#equals)
- [`PIPE`](#pipe)
- [`CARET`](#caret)
- [`TILDE`](#tilde)
- [`QUESTION_MARK`](#question_mark)
- [`PARENTHESIS`](#parenthesis)
- [`BRACKET`](#bracket)
- [`BRACE`](#brace)
- [`PUNCTUATION`](#punctuation)
- [`SYMBOL`](#symbol)
- [`UNICODE_LETTER`](#unicode_letter)

**composed**:

- [`SIGN`](#sign)
- [`QUOTE`](#quote)
- [`SPECIAL_CHARACTER`](#special_character)

**custom**:

- [`ESCAPED_CHARACTER`](#escaped_character)

---

### `DECIMAL_DIGIT`

Regex expression matching a single ASCII decimal digit.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches one of the characters `0` to `9` and nothing else.

```regex
[0-9]
```

**Notes:**

Strictly ASCII, unlike `DIGIT`. All numeric vocabulary in this package is built on this term.

**Example usage:**
```python
DECIMAL_DIGIT
# Matches: "0", "7", "9"
# Does not match: "a", "42", "٣"
```

[▲ Back to top](#-table-of-contents)

---

### `NON_ZERO_DIGIT`

Regex expression matching a single ASCII digit from 1 to 9.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches one of the characters `1` to `9`. Used to forbid leading zeros.

```regex
[1-9]
```

**Example usage:**
```python
NON_ZERO_DIGIT
# Matches: "1", "5", "9"
# Does not match: "0", "a", "12"
```

[▲ Back to top](#-table-of-contents)

---

### `BINARY_DIGIT`

Regex expression matching a single binary digit.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches `0` or `1`.

```regex
[01]
```

**Example usage:**
```python
BINARY_DIGIT
# Matches: "0", "1"
# Does not match: "2", "01"
```

[▲ Back to top](#-table-of-contents)

---

### `OCTAL_DIGIT`

Regex expression matching a single octal digit.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches one of the characters `0` to `7`.

```regex
[0-7]
```

**Example usage:**
```python
OCTAL_DIGIT
# Matches: "0", "7"
# Does not match: "8", "a", "07"
```

[▲ Back to top](#-table-of-contents)

---

### `SPACE`

Regex expression matching a single space character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one space character, taken literally.

```regex
\ 
```

**Example usage:**
```python
SPACE
# Matches: " "
# Does not match: "a", "  "
```

[▲ Back to top](#-table-of-contents)

---

### `PLUS_SIGN`

Regex expression matching the plus sign character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one plus sign character (`+`), taken literally.

```regex
\+
```

**Example usage:**
```python
PLUS_SIGN
# Matches: "+"
# Does not match: "a", "++"
```

[▲ Back to top](#-table-of-contents)

---

### `MINUS_SIGN`

Regex expression matching the minus sign character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one minus sign character (`-`), taken literally.

```regex
\-
```

**Example usage:**
```python
MINUS_SIGN
# Matches: "-"
# Does not match: "a", "--"
```

[▲ Back to top](#-table-of-contents)

---

### `DASH`

Regex expression matching the dash (hyphen-minus) character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one dash (hyphen-minus) character (`-`), taken literally.

```regex
\-
```

**Notes:**

Same character as `MINUS_SIGN`; the name states the role (separator vs. sign).

**Example usage:**
```python
DASH
# Matches: "-"
# Does not match: "a", "--"
```

[▲ Back to top](#-table-of-contents)

---

### `DOT`

Regex expression matching the dot character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one dot character (`.`), taken literally.

```regex
\.
```

**Example usage:**
```python
DOT
# Matches: "."
# Does not match: "a", ".."
```

[▲ Back to top](#-table-of-contents)

---

### `COMMA`

Regex expression matching the comma character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one comma character (`,`), taken literally.

```regex
,
```

**Example usage:**
```python
COMMA
# Matches: ","
# Does not match: "a", ",,"
```

[▲ Back to top](#-table-of-contents)

---

### `COLON`

Regex expression matching the colon character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one colon character (`:`), taken literally.

```regex
:
```

**Example usage:**
```python
COLON
# Matches: ":"
# Does not match: "a", "::"
```

[▲ Back to top](#-table-of-contents)

---

### `SEMICOLON`

Regex expression matching the semicolon character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one semicolon character (`;`), taken literally.

```regex
;
```

**Example usage:**
```python
SEMICOLON
# Matches: ";"
# Does not match: "a", ";;"
```

[▲ Back to top](#-table-of-contents)

---

### `SLASH`

Regex expression matching the slash character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one slash character (`/`), taken literally.

```regex
/
```

**Example usage:**
```python
SLASH
# Matches: "/"
# Does not match: "a", "//"
```

[▲ Back to top](#-table-of-contents)

---

### `SINGLE_QUOTE`

Regex expression matching the single quote character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one single quote character (`'`), taken literally.

```regex
'
```

**Example usage:**
```python
SINGLE_QUOTE
# Matches: "'"
# Does not match: "a", "''"
```

[▲ Back to top](#-table-of-contents)

---

### `DOUBLE_QUOTE`

Regex expression matching the double quote character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one double quote character (`"`), taken literally.

```regex
"
```

**Example usage:**
```python
DOUBLE_QUOTE
# Matches: '"'
# Does not match: "a", '""'
```

[▲ Back to top](#-table-of-contents)

---

### `UNDERSCORE`

Regex expression matching the underscore character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one underscore character (`_`), taken literally.

```regex
_
```

**Example usage:**
```python
UNDERSCORE
# Matches: "_"
# Does not match: "a", "__"
```

[▲ Back to top](#-table-of-contents)

---

### `AT_SIGN`

Regex expression matching the at sign character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one at sign character (`@`), taken literally.

```regex
@
```

**Example usage:**
```python
AT_SIGN
# Matches: "@"
# Does not match: "a", "@@"
```

[▲ Back to top](#-table-of-contents)

---

### `HASH_SIGN`

Regex expression matching the hash sign character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one hash sign character (`#`), taken literally.

```regex
\#
```

**Notes:**

Named `HASH_SIGN` so that `HASH` stays free for the hash-digest term in the `formats` domain.

**Example usage:**
```python
HASH_SIGN
# Matches: "#"
# Does not match: "a", "##"
```

[▲ Back to top](#-table-of-contents)

---

### `DOLLAR`

Regex expression matching the dollar sign character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one dollar sign character (`$`), taken literally.

```regex
\$
```

**Example usage:**
```python
DOLLAR
# Matches: "$"
# Does not match: "a", "$$"
```

[▲ Back to top](#-table-of-contents)

---

### `PERCENT`

Regex expression matching the percent sign character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one percent sign character (`%`), taken literally.

```regex
%
```

**Example usage:**
```python
PERCENT
# Matches: "%"
# Does not match: "a", "%%"
```

[▲ Back to top](#-table-of-contents)

---

### `AMPERSAND`

Regex expression matching the ampersand character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one ampersand character (`&`), taken literally.

```regex
\&
```

**Example usage:**
```python
AMPERSAND
# Matches: "&"
# Does not match: "a", "&&"
```

[▲ Back to top](#-table-of-contents)

---

### `ASTERISK`

Regex expression matching the asterisk character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one asterisk character (`*`), taken literally.

```regex
\*
```

**Example usage:**
```python
ASTERISK
# Matches: "*"
# Does not match: "a", "**"
```

[▲ Back to top](#-table-of-contents)

---

### `EQUALS`

Regex expression matching the equals sign character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one equals sign character (`=`), taken literally.

```regex
=
```

**Example usage:**
```python
EQUALS
# Matches: "="
# Does not match: "a", "=="
```

[▲ Back to top](#-table-of-contents)

---

### `PIPE`

Regex expression matching the pipe character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one pipe character (`|`), taken literally.

```regex
\|
```

**Example usage:**
```python
PIPE
# Matches: "|"
# Does not match: "a", "||"
```

[▲ Back to top](#-table-of-contents)

---

### `CARET`

Regex expression matching the caret character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one caret character (`^`), taken literally.

```regex
\^
```

**Example usage:**
```python
CARET
# Matches: "^"
# Does not match: "a", "^^"
```

[▲ Back to top](#-table-of-contents)

---

### `TILDE`

Regex expression matching the tilde character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one tilde character (`~`), taken literally.

```regex
\~
```

**Example usage:**
```python
TILDE
# Matches: "~"
# Does not match: "a", "~~"
```

[▲ Back to top](#-table-of-contents)

---

### `QUESTION_MARK`

Regex expression matching the question mark character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches exactly one question mark character (`?`), taken literally.

```regex
\?
```

**Example usage:**
```python
QUESTION_MARK
# Matches: "?"
# Does not match: "a", "??"
```

[▲ Back to top](#-table-of-contents)

---

### `PARENTHESIS`

Regex expression matching a single parenthesis.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches `(` or `)`.

```regex
[()]
```

**Example usage:**
```python
PARENTHESIS
# Matches: "(", ")"
# Does not match: "[", "()"
```

[▲ Back to top](#-table-of-contents)

---

### `BRACKET`

Regex expression matching a single square bracket.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches `[` or `]`.

```regex
[[\]]
```

**Example usage:**
```python
BRACKET
# Matches: "[", "]"
# Does not match: "(", "[]"
```

[▲ Back to top](#-table-of-contents)

---

### `BRACE`

Regex expression matching a single curly brace.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches `{` or `}`.

```regex
[{}]
```

**Example usage:**
```python
BRACE
# Matches: "{", "}"
# Does not match: "(", "{}"
```

[▲ Back to top](#-table-of-contents)

---

### `PUNCTUATION`

Regex expression matching a single punctuation character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches one of `! " # % & ' ( ) * , - . / : ; ? @ [ \ ] _ { }`.

```regex
[!"#%&'()*,\-./:;?@[\\\]_{}]
```

**Notes:**

Follows the Unicode split of ASCII punctuation: characters like `$`, `+`, `<` are symbols (see `SYMBOL`).

**Example usage:**
```python
PUNCTUATION
# Matches: "!", ".", "_"
# Does not match: "$", "+", "a"
```

[▲ Back to top](#-table-of-contents)

---

### `SYMBOL`

Regex expression matching a single symbol character.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches one of ``$ + < = > ^ ` | ~``.

```regex
[$+<=>\^`|~]
```

**Example usage:**
```python
SYMBOL
# Matches: "$", "+", "~"
# Does not match: "!", "a"
```

[▲ Back to top](#-table-of-contents)

---

### `UNICODE_LETTER`

Regex expression matching a single letter of any language.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches one Unicode letter: any word character (`\w`) that is neither a digit nor an underscore (`[^\W\d_]`).

```regex
[^\W\d_]
```

**Notes:**

Use this instead of `LETTER` for names, addresses and other human text.

**Example usage:**
```python
UNICODE_LETTER
# Matches: "a", "é", "ž", "Ω"
# Does not match: "1", "_", " ", "ab"
```

[▲ Back to top](#-table-of-contents)

---

### `SIGN`

Regex expression matching a single sign character.

**Init Params:**
*(no parameters)*

**Pattern:**
`PLUS_SIGN` or `MINUS_SIGN` — one of `+` and `-`.

```regex
[+\-]
```

**Example usage:**
```python
SIGN
# Matches: "+", "-"
# Does not match: "a", "+-"
```

[▲ Back to top](#-table-of-contents)

---

### `QUOTE`

Regex expression matching a single quote character of either kind.

**Init Params:**
*(no parameters)*

**Pattern:**
`SINGLE_QUOTE` or `DOUBLE_QUOTE` — one of `'` and `"`.

```regex
['"]
```

**Example usage:**
```python
QUOTE
# Matches: "'", '"'
# Does not match: "a", "''"
```

[▲ Back to top](#-table-of-contents)

---

### `SPECIAL_CHARACTER`

Regex expression matching a single punctuation or symbol character.

**Init Params:**
*(no parameters)*

**Pattern:**
`PUNCTUATION` or `SYMBOL` — any printable ASCII character that is neither a letter, a digit nor a space.

```regex
[!"#%&'()*,\-./:;?@[\\\]_{}]|[$+<=>\^`|~]
```

**Example usage:**
```python
SPECIAL_CHARACTER
# Matches: "!", "$", "~"
# Does not match: "a", "5", " "
```

[▲ Back to top](#-table-of-contents)

---

### `ESCAPED_CHARACTER`

Regex expression matching a single backslash escape sequence.

**Init Params:**
*(no parameters)*

**Pattern:**
A backslash followed by one of:
1. `x` and 2 hex digits (`\xFF`).
2. `u` and 4 hex digits (`\u1234`).
3. `U` and 8 hex digits (`\U0001F600`).
4. any other single character (`\.`, `\n`, `\\`).

```regex
\\(?:x[0-9a-fA-F]{2}|u[0-9a-fA-F]{4}|U[0-9a-fA-F]{8}|.)
```

**Notes:**

Generic escape syntax shared by many languages. Octal and named (`\N{...}`) escapes are not special-cased; they fall under the last alternative only when a single character follows.

**Example usage:**
```python
ESCAPED_CHARACTER
# Matches: "\.", "\n", "\xFF", "\u1234"
# Does not match: "\x4", "\", "n"
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](../README.md)
