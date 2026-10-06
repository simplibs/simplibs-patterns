# 📝 `patterns/text` — Detailed Reference

Runs of text — words, lines, quoted and bracketed text, character-class texts, and parametrized helpers such as `WHOLE_WORD`, `TEXT_BETWEEN` or `TEXT_UNTIL`.

Every card below is the term's full docstring. Terms are grouped by how they are defined: **pure** (a named concept), **composed** (built from other terms, or a parametrized factory) and **custom** (needed a semantic decision — read its notes).

All expressions are `simplibs.regex` objects: combine them with `+` (sequence) and `|` (alternation), wrap them with the presets (`ONE_OR_MORE`, `NAMED_GROUP`, …) and compile with `RegexPattern`.

---

## 🧭 Table of Contents

**pure**:

- [`EMPTY_TEXT`](#empty_text)
- [`NON_EMPTY_TEXT`](#non_empty_text)
- [`CHARACTER`](#character)
- [`CHARACTERS`](#characters)
- [`WORD`](#word)
- [`SINGLE_WORD`](#single_word)
- [`LINE`](#line)
- [`SINGLE_LINE`](#single_line)
- [`WHITESPACE_TEXT`](#whitespace_text)
- [`NON_WHITESPACE_TEXT`](#non_whitespace_text)
- [`ALPHANUMERIC_TEXT`](#alphanumeric_text)
- [`ALPHA_TEXT`](#alpha_text)
- [`DIGIT_TEXT`](#digit_text)
- [`LOWERCASE_TEXT`](#lowercase_text)
- [`UPPERCASE_TEXT`](#uppercase_text)
- [`IDENTIFIER_LIKE_TEXT`](#identifier_like_text)
- [`SINGLE_QUOTED_TEXT`](#single_quoted_text)
- [`DOUBLE_QUOTED_TEXT`](#double_quoted_text)
- [`PARENTHESIZED_TEXT`](#parenthesized_text)
- [`BRACKETED_TEXT`](#bracketed_text)
- [`BRACED_TEXT`](#braced_text)

**composed**:

- [`QUOTED_TEXT`](#quoted_text)
- [`WORDS`](#words)
- [`SPACE_SEPARATED_WORDS`](#space_separated_words)
- [`WORD_LIST`](#word_list)
- [`COMMA_SEPARATED_TEXT`](#comma_separated_text)
- [`MULTILINE_TEXT`](#multiline_text)
- [`WHOLE_WORD`](#whole_word)
- [`TEXT_BETWEEN`](#text_between)
- [`PREFIXED_TEXT`](#prefixed_text)
- [`SUFFIXED_TEXT`](#suffixed_text)
- [`TEXT_OF_LENGTH`](#text_of_length)
- [`TEXT_OF_LENGTH_RANGE`](#text_of_length_range)

**custom**:

- [`MIXED_CASE_TEXT`](#mixed_case_text)
- [`CSV_LINE`](#csv_line)
- [`TEXT_UNTIL`](#text_until)
- [`TEXT_AFTER`](#text_after)
- [`TEXT_BEFORE`](#text_before)

[⬅️ Back to main README](../README.md#-text--38-terms)

---

### `EMPTY_TEXT`

Regex expression matching an empty string.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches zero characters — only an empty input.

```regex
.{0}
```

**Example usage:**
```python
EMPTY_TEXT
# Matches: ""
# Does not match: "a", " "
```

[▲ Back to top](#-table-of-contents)

---

### `NON_EMPTY_TEXT`

Regex expression matching one or more characters.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more characters of any kind (except a newline, unless the `DOTALL` flag is set).

```regex
.+
```

**Example usage:**
```python
NON_EMPTY_TEXT
# Matches: "a", "Hello, world!"
# Does not match: ""
```

[▲ Back to top](#-table-of-contents)

---

### `CHARACTER`

Regex expression matching a single character.

**Init Params:**
*(no parameters)*

**Pattern:**
Exactly one character of any kind (except a newline, unless the `DOTALL` flag is set).

```regex
.
```

**Example usage:**
```python
CHARACTER
# Matches: "a", "!", " "
# Does not match: "", "ab"
```

[▲ Back to top](#-table-of-contents)

---

### `CHARACTERS`

Regex expression matching one or more characters.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `NON_EMPTY_TEXT`; the separate name states the intended role.

**Example usage:**
```python
CHARACTERS
# Matches: "a", "Hello, world!"
# Does not match: ""
```

[▲ Back to top](#-table-of-contents)

---

### `WORD`

Regex expression matching a single word.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more word characters (letters, digits, underscore) without any separator.

```regex
\w+
```

**Notes:**

A whole word, unlike `WORD_CHARACTER` (one character) and unlike `simplibs.regex` `WORD` (`\w`, one character).

**Example usage:**
```python
WORD
# Matches: "Python", "snake_case", "abc123"
# Does not match: "two words", "", "a-b"
```

[▲ Back to top](#-table-of-contents)

---

### `SINGLE_WORD`

Regex expression matching a single word.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `WORD`; the separate name states the intended role.

**Example usage:**
```python
SINGLE_WORD
# Matches: "Python", "snake_case", "abc123"
# Does not match: "two words", "", "a-b"
```

[▲ Back to top](#-table-of-contents)

---

### `LINE`

Regex expression matching one line of text, possibly empty.

**Init Params:**
*(no parameters)*

**Pattern:**
Zero or more characters that are not a line break.

```regex
.*
```

**Example usage:**
```python
LINE
# Matches: "", "one line", "a b c"
# Does not match: "a\nb"
```

[▲ Back to top](#-table-of-contents)

---

### `SINGLE_LINE`

Regex expression matching a single line of text.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `LINE`; the separate name states the intended role.

**Notes:**

Stops at a line break; use `MULTILINE_TEXT` to span several lines.

**Example usage:**
```python
SINGLE_LINE
# Matches: "", "one line", "a b c"
# Does not match: "a\nb"
```

[▲ Back to top](#-table-of-contents)

---

### `WHITESPACE_TEXT`

Regex expression matching text made only of whitespace.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more whitespace characters.

```regex
\s+
```

**Example usage:**
```python
WHITESPACE_TEXT
# Matches: " ", "\t\n "
# Does not match: "a", "", " a"
```

[▲ Back to top](#-table-of-contents)

---

### `NON_WHITESPACE_TEXT`

Regex expression matching text without any whitespace.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more non-whitespace characters.

```regex
\S+
```

**Example usage:**
```python
NON_WHITESPACE_TEXT
# Matches: "abc", "a-b!"
# Does not match: "a b", ""
```

[▲ Back to top](#-table-of-contents)

---

### `ALPHANUMERIC_TEXT`

Regex expression matching text made only of ASCII letters and digits.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more characters from `a`–`z`, `A`–`Z`, `0`–`9`.

```regex
[a-zA-Z0-9]+
```

**Example usage:**
```python
ALPHANUMERIC_TEXT
# Matches: "abc123", "X"
# Does not match: "a b", "a_b", ""
```

[▲ Back to top](#-table-of-contents)

---

### `ALPHA_TEXT`

Regex expression matching text made only of ASCII letters.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more ASCII letters.

```regex
[a-zA-Z]+
```

**Example usage:**
```python
ALPHA_TEXT
# Matches: "abc", "Hello"
# Does not match: "abc1", "a b", ""
```

[▲ Back to top](#-table-of-contents)

---

### `DIGIT_TEXT`

Regex expression matching text made only of ASCII digits.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more characters `0`–`9`.

```regex
[0-9]+
```

**Example usage:**
```python
DIGIT_TEXT
# Matches: "0", "2026", "007"
# Does not match: "1.5", "-1", "", "a1"
```

[▲ Back to top](#-table-of-contents)

---

### `LOWERCASE_TEXT`

Regex expression matching text made only of lowercase ASCII letters.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more letters `a`–`z`.

```regex
[a-z]+
```

**Example usage:**
```python
LOWERCASE_TEXT
# Matches: "abc", "x"
# Does not match: "Abc", "abc1", ""
```

[▲ Back to top](#-table-of-contents)

---

### `UPPERCASE_TEXT`

Regex expression matching text made only of uppercase ASCII letters.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more letters `A`–`Z`.

```regex
[A-Z]+
```

**Example usage:**
```python
UPPERCASE_TEXT
# Matches: "ABC", "X"
# Does not match: "aBC", "ABC1", ""
```

[▲ Back to top](#-table-of-contents)

---

### `IDENTIFIER_LIKE_TEXT`

Regex expression matching text shaped like an identifier.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Example usage:**
```python
IDENTIFIER_LIKE_TEXT
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `SINGLE_QUOTED_TEXT`

Regex expression matching text in single quotes.

**Init Params:**
*(no parameters)*

**Pattern:**
A `'`, any characters that are not `'`, and a closing `'`.

```regex
'[^']*'
```

**Notes:**

No escape handling: a quote inside the text always ends it.

**Example usage:**
```python
SINGLE_QUOTED_TEXT
# Matches: "'hello'", "''"
# Does not match: "hello", "'a'b'", "'open"
```

[▲ Back to top](#-table-of-contents)

---

### `DOUBLE_QUOTED_TEXT`

Regex expression matching text in double quotes.

**Init Params:**
*(no parameters)*

**Pattern:**
A `"`, any characters that are not `"`, and a closing `"`.

```regex
"[^"]*"
```

**Notes:**

No escape handling: a quote inside the text always ends it.

**Example usage:**
```python
DOUBLE_QUOTED_TEXT
# Matches: '"hello"', '""'
# Does not match: "hello", '"a"b"', '"open'
```

[▲ Back to top](#-table-of-contents)

---

### `PARENTHESIZED_TEXT`

Regex expression matching text in parentheses.

**Init Params:**
*(no parameters)*

**Pattern:**
`(`, any characters that are not parentheses, and `)`.

```regex
\([^()]*\)
```

**Notes:**

Not nested: parentheses inside are not allowed (a regex cannot count nesting levels).

**Example usage:**
```python
PARENTHESIZED_TEXT
# Matches: "(abc)", "()"
# Does not match: "abc", "(a(b))", "(open"
```

[▲ Back to top](#-table-of-contents)

---

### `BRACKETED_TEXT`

Regex expression matching text in square brackets.

**Init Params:**
*(no parameters)*

**Pattern:**
`[`, any characters that are not square brackets, and `]`.

```regex
\[[^[\]]*\]
```

**Notes:**

Not nested: square brackets inside are not allowed.

**Example usage:**
```python
BRACKETED_TEXT
# Matches: "[abc]", "[]"
# Does not match: "abc", "[a[b]]", "[open"
```

[▲ Back to top](#-table-of-contents)

---

### `BRACED_TEXT`

Regex expression matching text in curly braces.

**Init Params:**
*(no parameters)*

**Pattern:**
`{`, any characters that are not curly braces, and `}`.

```regex
\{[^{}]*\}
```

**Notes:**

Not nested: curly braces inside are not allowed.

**Example usage:**
```python
BRACED_TEXT
# Matches: "{abc}", "{}"
# Does not match: "abc", "{a{b}}", "{open"
```

[▲ Back to top](#-table-of-contents)

---

### `QUOTED_TEXT`

Regex expression matching text in single or double quotes.

**Init Params:**
*(no parameters)*

**Pattern:**
`SINGLE_QUOTED_TEXT` or `DOUBLE_QUOTED_TEXT`.

```regex
'[^']*'|"[^"]*"
```

**Example usage:**
```python
QUOTED_TEXT
# Matches: "'hi'", '"hi"'
# Does not match: "hi", "'hi\""
```

[▲ Back to top](#-table-of-contents)

---

### `WORDS`

Regex expression matching one or more words separated by whitespace.

**Init Params:**
*(no parameters)*

**Pattern:**
A `WORD`, then any number of (whitespace, `WORD`) pairs.

```regex
\w+(?:\s+\w+)*
```

**Example usage:**
```python
WORDS
# Matches: "hello", "hello big   world", "a\tb"
# Does not match: "", "hello,world", " hello"
```

[▲ Back to top](#-table-of-contents)

---

### `SPACE_SEPARATED_WORDS`

Regex expression matching words separated by exactly one space.

**Init Params:**
*(no parameters)*

**Pattern:**
A `WORD`, then any number of (one space, `WORD`) pairs.

```regex
\w+(?:\ \w+)*
```

**Example usage:**
```python
SPACE_SEPARATED_WORDS
# Matches: "hello", "a b c"
# Does not match: "a  b", "a\tb", ""
```

[▲ Back to top](#-table-of-contents)

---

### `WORD_LIST`

Regex expression matching a list of words.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `WORDS`; the separate name states the intended role.

**Notes:**

Separated by whitespace; for comma-separated words see `COMMA_SEPARATED_TEXT`.

**Example usage:**
```python
WORD_LIST
# Matches: "hello", "hello big   world", "a\tb"
# Does not match: "", "hello,world", " hello"
```

[▲ Back to top](#-table-of-contents)

---

### `COMMA_SEPARATED_TEXT`

Regex expression matching words separated by commas.

**Init Params:**
*(no parameters)*

**Pattern:**
A `WORD`, then any number of (comma, `WORD`) pairs, with no spaces.

```regex
\w+(?:,\w+)*
```

**Example usage:**
```python
COMMA_SEPARATED_TEXT
# Matches: "a", "a,b,c", "one,two"
# Does not match: "a, b", "a,,b", "a,", ""
```

[▲ Back to top](#-table-of-contents)

---

### `MULTILINE_TEXT`

Regex expression matching text spanning two or more lines.

**Init Params:**
*(no parameters)*

**Pattern:**
A `LINE`, then one or more (newline, `LINE`) pairs.

```regex
.*(?:\n.*)+
```

**Example usage:**
```python
MULTILINE_TEXT
# Matches: "a\nb", "a\n\nb", "x\ny\nz"
# Does not match: "single line", ""
```

[▲ Back to top](#-table-of-contents)

---

### `WHOLE_WORD`

Build a regex expression matching the given text as a complete word.

**Init Params:**
* `text` (*str*): The exact text that must appear as a complete word.

**Pattern:**
1. A word boundary before `text`.
2. The literal `text`.
3. A word boundary after `text`.

**Notes:**

Word boundaries only exist next to word characters; `text` should start and end with one.

**Example usage:**
```python
pattern = WHOLE_WORD("Python")
# Regex: \bPython\b
# Finds "Python" in "Python is great"
# Finds "Python" in "I love Python"
# No match in: "CPython", "Pythonic"
```

[▲ Back to top](#-table-of-contents)

---

### `TEXT_BETWEEN`

Build a regex expression matching text enclosed by an opening and a closing string.

**Init Params:**
* `opening` (*str*): The text that starts the enclosed part.
* `closing` (*str*): The text that ends the enclosed part.

**Pattern:**
1. The literal `opening`.
2. As few characters as possible (lazy).
3. The literal `closing`.

**Notes:**

Lazy: takes the nearest closing string, so `a <b> c <d>` yields `<b>`, not everything up to the last `>`.
The delimiters are part of the match.

**Example usage:**
```python
pattern = TEXT_BETWEEN("<", ">")
# Regex: <.*?>
# Finds "<b>" in "a <b> c <d>"
# No match in: "no brackets"
```

[▲ Back to top](#-table-of-contents)

---

### `PREFIXED_TEXT`

Build a regex expression matching text that starts with the given prefix.

**Init Params:**
* `prefix` (*str*): The literal text the match must start with.

**Pattern:**
The literal `prefix`, followed by any number of characters.

**Example usage:**
```python
pattern = PREFIXED_TEXT("log:")
# Regex: log:.*
# Matches: "log: started", "log:"
# Does not match: "info: started"
```

[▲ Back to top](#-table-of-contents)

---

### `SUFFIXED_TEXT`

Build a regex expression matching text that ends with the given suffix.

**Init Params:**
* `suffix` (*str*): The literal text the match must end with.

**Pattern:**
Any number of characters, followed by the literal `suffix`.

**Example usage:**
```python
pattern = SUFFIXED_TEXT(".py")
# Regex: .*\.py
# Matches: "main.py", ".py"
# Does not match: "main.txt"
```

[▲ Back to top](#-table-of-contents)

---

### `TEXT_OF_LENGTH`

Build a regex expression matching text of an exact length.

**Init Params:**
* `length` (*int*): The exact number of characters.

**Pattern:**
Exactly `length` characters of any kind.

**Example usage:**
```python
pattern = TEXT_OF_LENGTH(3)
# Regex: .{3}
# Matches: "abc", "123"
# Does not match: "ab", "abcd"
```

[▲ Back to top](#-table-of-contents)

---

### `TEXT_OF_LENGTH_RANGE`

Build a regex expression matching text whose length lies in an inclusive range.

**Init Params:**
* `min_length` (*int*): The minimum number of characters (inclusive).
* `max_length` (*int*): The maximum number of characters (inclusive).

**Pattern:**
Between `min_length` and `max_length` characters of any kind.

**Example usage:**
```python
pattern = TEXT_OF_LENGTH_RANGE(2, 4)
# Regex: .{2,4}
# Matches: "ab", "abcd"
# Does not match: "a", "abcde"
```

[▲ Back to top](#-table-of-contents)

---

### `MIXED_CASE_TEXT`

Regex expression matching text containing both lowercase and uppercase letters.

**Init Params:**
*(no parameters)*

**Pattern:**
Non-empty text in which at least one lowercase and at least one uppercase ASCII letter occur, in any order.

```regex
(?=.*[a-z])(?=.*[A-Z]).+
```

**Notes:**

Checks presence, not a particular style (camelCase, PascalCase…).

**Example usage:**
```python
MIXED_CASE_TEXT
# Matches: "Hello", "aB", "fooBar!"
# Does not match: "hello", "HELLO", "123", ""
```

[▲ Back to top](#-table-of-contents)

---

### `CSV_LINE`

Regex expression matching one line of comma-separated fields.

**Init Params:**
*(no parameters)*

**Pattern:**
Fields made of any characters except comma and line breaks, separated by commas. Fields may be empty.

```regex
[^,\r\n]*(?:,[^,\r\n]*)*
```

**Notes:**

Simplified: quoted fields that contain commas are not supported.

**Example usage:**
```python
CSV_LINE
# Matches: "a,b,c", "a,,c", "single", ""
# Does not match: "a\nb"
```

[▲ Back to top](#-table-of-contents)

---

### `TEXT_UNTIL`

Build a regex expression matching all text up to (not including) the given text.

**Init Params:**
* `text` (*str*): The literal text at which matching stops.

**Pattern:**
Any number of characters, each of which is not the start of `text`.

**Notes:**

The stop text itself is not consumed. Always matches (possibly empty).

**Example usage:**
```python
pattern = TEXT_UNTIL("=")
# Regex: (?:(?!=).)*
# Finds "key" in "key=value"
```

[▲ Back to top](#-table-of-contents)

---

### `TEXT_AFTER`

Build a regex expression matching the text that follows the given text.

**Init Params:**
* `text` (*str*): The literal text that must directly precede the match.

**Pattern:**
1. A lookbehind requiring `text` right before the match.
2. The rest of the line (at least one character).

**Notes:**

The preceding text is required but not part of the match.

**Example usage:**
```python
pattern = TEXT_AFTER("key=")
# Regex: (?<=key=).+
# Finds "value" in "key=value"
# No match in: "nothing here"
```

[▲ Back to top](#-table-of-contents)

---

### `TEXT_BEFORE`

Build a regex expression matching the text that comes before the given text.

**Init Params:**
* `text` (*str*): The literal text that must directly follow the match.

**Pattern:**
1. As few characters as possible, at least one (lazy).
2. A lookahead requiring `text` right after the match.

**Notes:**

The following text is required but not part of the match.

**Example usage:**
```python
pattern = TEXT_BEFORE("=")
# Regex: .+?(?==)
# Finds "key" in "key=value"
# No match in: "nothing here"
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](../README.md#-text--38-terms)
