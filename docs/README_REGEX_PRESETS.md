# 🧩 `patterns/regex` — Propagated Regex Presets

Core regex building blocks — anchors, character types, groups, literals, lookarounds and quantifiers provided directly by `simplibs.regex` and re-exported by `simplibs.patterns`.

These presets are **defined and implemented in `simplibs.regex`**. The `patterns` library does not redefine or wrap them; it simply propagates them so that its users can access the complete preset vocabulary from `simplibs.patterns`.

This keeps the two libraries separated by responsibility: `simplibs.regex` provides the regex construction logic and its fundamental presets, while `simplibs.patterns` builds a larger domain-oriented vocabulary on top of that foundation.

Every card below describes a preset as defined by `simplibs.regex`. The documentation is reproduced here so that the propagated presets are documented alongside the presets native to `patterns`.

All expressions are `simplibs.regex` objects: combine them with `+` (sequence) and `|` (alternation), wrap them with the presets (`ONE_OR_MORE`, `NAMED_GROUP`, …) and compile with `RegexPattern`.

---

## 🧭 Table of Contents

**anchors**:

- [`END`](#end)
- [`END_STRING`](#end_string)
- [`NON_WORD_BOUNDARY`](#non_word_boundary)
- [`START`](#start)
- [`START_STRING`](#start_string)
- [`WORD_BOUNDARY`](#word_boundary)

**any character**:

- [`ANY`](#any)

**character classes**:

- [`ALPHANUMERIC`](#alphanumeric)
- [`HEX_DIGIT`](#hex_digit)
- [`LETTER`](#letter)
- [`LOWERCASE_LETTER`](#lowercase_letter)
- [`UPPERCASE_LETTER`](#uppercase_letter)

**character types**:

- [`DIGIT`](#digit)
- [`NON_DIGIT`](#non_digit)
- [`NON_WHITESPACE`](#non_whitespace)
- [`NON_WORD_CHARACTER`](#non_word_character)
- [`WHITESPACE`](#whitespace)
- [`WORD_CHARACTER`](#word_character)

**groups**:

- [`ATOMIC_GROUP`](#atomic_group)
- [`CASE_INSENSITIVE`](#case_insensitive)
- [`NAMED_GROUP`](#named_group)
- [`NON_CAPTURING`](#non_capturing)
- [`VERBOSE_GROUP`](#verbose_group)
- [`WITH_FLAGS`](#with_flags)

**literals**:

- [`BACKSLASH`](#backslash)
- [`BELL`](#bell)
- [`CARRIAGE_RETURN`](#carriage_return)
- [`FORM_FEED`](#form_feed)
- [`NEWLINE`](#newline)
- [`TAB`](#tab)
- [`VERTICAL_TAB`](#vertical_tab)

**lookaround**:

- [`LOOKAHEAD`](#lookahead)
- [`LOOKBEHIND`](#lookbehind)
- [`NEGATIVE_LOOKAHEAD`](#negative_lookahead)
- [`NEGATIVE_LOOKBEHIND`](#negative_lookbehind)

**quantifiers**:

- [`AT_LEAST`](#at_least)
- [`BETWEEN`](#between)
- [`EXACTLY`](#exactly)
- [`ONE_OR_MORE`](#one_or_more)
- [`OPTIONAL`](#optional)
- [`ZERO_OR_MORE`](#zero_or_more)

[⬅️ Back to main README](../README.md#-propagated-regex-presets)

---

## ⚓ Anchors

### `END`

Regex expression matching the end of a line.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches the position at the end of a line (`$`), respecting multiline mode. Without `MULTILINE` it matches at the end of the string and also just before a final newline; use `END_STRING` for the strict end of the text.

```regex
$
```

**Example usage:**
```python
END
# Matches end of any line in multiline text
```

[▲ Back to top](#-table-of-contents)

---

### `END_STRING`

Regex expression matching the absolute end of the string.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches the absolute end of the entire text (`\Z`), unaffected by multiline mode.

```regex
\Z
```

**Example usage:**
```python
END_STRING
# Matches only at the very end of the string
```

[▲ Back to top](#-table-of-contents)

---

### `NON_WORD_BOUNDARY`

Regex expression matching a non-word boundary.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches a zero-width position that is not a word boundary (`\B`).

```regex
\B
```

**Example usage:**
```python
NON_WORD_BOUNDARY
# Matches positions inside words (e.g. between 'y' and 't' in 'Python')
```

[▲ Back to top](#-table-of-contents)

---

### `START`

Regex expression matching the start of a line.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches the position at the start of a line (`^`), respecting multiline mode.

```regex
^
```

**Example usage:**
```python
START
# Matches start of any line in multiline text
```

[▲ Back to top](#-table-of-contents)

---

### `START_STRING`

Regex expression matching the absolute start of the string.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches the absolute start of the entire text (`\A`), unaffected by multiline mode.

```regex
\A
```

**Example usage:**
```python
START_STRING
# Matches only at the very beginning of the string
```

[▲ Back to top](#-table-of-contents)

---

### `WORD_BOUNDARY`

Regex expression matching a word boundary.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches a zero-width position between a word character and a non-word character, or at the edge of the string next to a word character (`\b`).

```regex
\b
```

**Example usage:**
```python
WORD_BOUNDARY
# Matches boundary between a word and a non-word character or edge
```

[▲ Back to top](#-table-of-contents)

---

## 🔤 Any Character

### `ANY`

Regex expression matching any single character.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches any character except a newline (`.`); with the `DOTALL` flag it matches a newline too.

```regex
.
```

**Example usage:**
```python
ANY
# Matches: "a", "5", " ", "!"
# Does not match: "\n" (without DOTALL)
```

[▲ Back to top](#-table-of-contents)

---

## 🔡 Character Classes

### `ALPHANUMERIC`

Regex expression matching a single ASCII letter or digit.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches one ASCII letter or digit (`[a-zA-Z0-9]`); no underscore, no non-ASCII digits.

```regex
[a-zA-Z0-9]
```

**Example usage:**
```python
ALPHANUMERIC
# Matches: "a", "Z", "5"
# Does not match: "_", "-", "é"
```

[▲ Back to top](#-table-of-contents)

---

### `HEX_DIGIT`

Regex expression matching a single hexadecimal digit.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches one hexadecimal digit, case-insensitive by range (`[0-9a-fA-F]`).

```regex
[0-9a-fA-F]
```

**Example usage:**
```python
HEX_DIGIT
# Matches: "0", "9", "a", "F"
# Does not match: "g", "-"
```

[▲ Back to top](#-table-of-contents)

---

### `LETTER`

Regex expression matching a single ASCII letter.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches one lowercase or uppercase ASCII letter (`[a-zA-Z]`).

```regex
[a-zA-Z]
```

**Example usage:**
```python
LETTER
# Matches: "a", "Z"
# Does not match: "5", "_", "é"
```

[▲ Back to top](#-table-of-contents)

---

### `LOWERCASE_LETTER`

Regex expression matching a single lowercase ASCII letter.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches one character from `a` to `z` (`[a-z]`).

```regex
[a-z]
```

**Example usage:**
```python
LOWERCASE_LETTER
# Matches: "a", "z"
# Does not match: "A", "5", "é"
```

[▲ Back to top](#-table-of-contents)

---

### `UPPERCASE_LETTER`

Regex expression matching a single uppercase ASCII letter.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches one character from `A` to `Z` (`[A-Z]`).

```regex
[A-Z]
```

**Example usage:**
```python
UPPERCASE_LETTER
# Matches: "A", "Z"
# Does not match: "a", "5"
```

[▲ Back to top](#-table-of-contents)

---

## 🔠 Character Types

### `DIGIT`

Regex expression matching a single decimal digit.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches any Unicode decimal digit (`\d`): `0`-`9` and digits of other scripts. Compile with the ASCII flag to restrict it to `0`-`9`.

```regex
\d
```

**Example usage:**
```python
DIGIT
# Matches: "5", "0"
# Does not match: "a", " "
```

[▲ Back to top](#-table-of-contents)

---

### `NON_DIGIT`

Regex expression matching any character that is not a decimal digit.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches any character except decimal digits (`\D`).

```regex
\D
```

**Example usage:**
```python
NON_DIGIT
# Matches: "a", " ", "-"
# Does not match: "5"
```

[▲ Back to top](#-table-of-contents)

---

### `NON_WHITESPACE`

Regex expression matching any character that is not whitespace.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches any non-whitespace character (`\S`).

```regex
\S
```

**Example usage:**
```python
NON_WHITESPACE
# Matches: "a", "5", "!"
# Does not match: " ", "\t", "\n"
```

[▲ Back to top](#-table-of-contents)

---

### `NON_WORD_CHARACTER`

Regex expression matching any character that is not a word character.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches any non-word character (`\W`).

```regex
\W
```

**Example usage:**
```python
NON_WORD_CHARACTER
# Matches: " ", "-", "!"
# Does not match: "a", "5", "_"
```

[▲ Back to top](#-table-of-contents)

---

### `WHITESPACE`

Regex expression matching a whitespace character.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches any whitespace character like space, tab, or newline (`\s`).

```regex
\s
```

**Example usage:**
```python
WHITESPACE
# Matches: " ", "\t", "\n"
# Does not match: "a", "5"
```

[▲ Back to top](#-table-of-contents)

---

### `WORD_CHARACTER`

Regex expression matching a word character.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches any Unicode letter, digit, or underscore (`\w`). Under the ASCII flag only `a-z`, `A-Z`, `0-9` and `_`.

```regex
\w
```

**Example usage:**
```python
WORD_CHARACTER
# Matches: "a", "Z", "9", "_"
# Does not match: " ", "-", "!"
```

[▲ Back to top](#-table-of-contents)

---

## 🧩 Groups

### `ATOMIC_GROUP`

Build a regex expression matching an atomic group.

**Init Params:**
- `inner` (`Regex`): The inner regex expression to evaluate atomically.

**Pattern:**

An independent sub-expression that prevents backtracking once matched (`(?>...)`).

```regex
(?>...)
```

**Example usage:**
```python
pattern = ATOMIC_GROUP(Sequence(DIGIT, DIGIT))
# Matches: two digits, discarding intermediate backtracking states
```

[▲ Back to top](#-table-of-contents)

---

### `CASE_INSENSITIVE`

Build a regex expression matching `inner` with case-insensitive matching.

**Init Params:**
- `inner` (`Regex`): The inner regex expression the flag applies to.

**Pattern:**

A non-capturing group with the `IGNORECASE` flag scoped to `inner` only (`(?i:...)`).

```regex
(?i:...)
```

**Example usage:**
```python
pattern = CASE_INSENSITIVE(Literal("ab"))
# Matches: "ab", "AB", "aB"
```

[▲ Back to top](#-table-of-contents)

---

### `NAMED_GROUP`

Build a regex expression matching a named capturing group.

**Init Params:**
- `inner` (`Regex`): The inner regex expression to be captured.
- `name` (`str`): The name assigned to the capturing group.

**Pattern:**

A capturing group with a specific name (`(?P<name>...)`).

```regex
(?P<name>...)
```

**Example usage:**
```python
pattern = NAMED_GROUP(DIGIT, "code")
# Matches: captures decimal digit into group "code"
```

[▲ Back to top](#-table-of-contents)

---

### `NON_CAPTURING`

Build a regex expression matching a non-capturing group.

**Init Params:**
- `inner` (`Regex`): The inner regex expression to group without capturing.

**Pattern:**

A group that controls precedence without saving the matched text (`(?:...)`).

```regex
(?:...)
```

**Example usage:**
```python
pattern = NON_CAPTURING(Sequence(Literal("a"), Literal("b")))
# Matches: "ab" as a combined unit without creating a capture group
```

[▲ Back to top](#-table-of-contents)

---

### `VERBOSE_GROUP`

Build a regex expression matching `inner` in verbose mode.

**Init Params:**
- `inner` (`Regex`): The inner regex expression the flag applies to.

**Pattern:**

A non-capturing group with the `VERBOSE` flag scoped to `inner` only (`(?x:...)`).

Whitespace and `#` of a `Literal` inside are escaped, so verbose mode never swallows them.

```regex
(?x:...)
```

**Example usage:**
```python
pattern = VERBOSE_GROUP(Literal("a b"))
# Matches: "a b" (the escaped space is kept)
```

[▲ Back to top](#-table-of-contents)

---

### `WITH_FLAGS`

Build a regex expression matching `inner` with scoped inline flags.

**Init Params:**
- `inner` (`Regex`): The inner regex expression the flags apply to.
- `*flags` (`Flag`): The flags to switch on inside the group.

**Pattern:**

A non-capturing group with flags scoped to `inner` only (`(?flags:...)`).

Generic fallback for any flag combination without its own named preset.

```regex
(?flags:...)
```

**Example usage:**
```python
pattern = WITH_FLAGS(ONE_OR_MORE(DIGIT), Flag.MULTILINE, Flag.DOTALL)
# Matches: digits, with MULTILINE and DOTALL active inside the group only
```

[▲ Back to top](#-table-of-contents)

---

## 🔣 Literals

### `BACKSLASH`

Regex expression matching a literal backslash character.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches the real backslash character (`\`) exactly once — the character itself, not a two-character escape text.

```regex
\\
```

**Example usage:**
```python
BACKSLASH
# Matches: the single backslash character
# Does not match: any other character
```

[▲ Back to top](#-table-of-contents)

---

### `BELL`

Regex expression matching a bell (alert) character.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches the real bell character (`\a`) exactly once — the character itself, not a two-character escape text.

```regex
\a
```

**Example usage:**
```python
BELL
# Matches: the single bell character
# Does not match: any other character
```

[▲ Back to top](#-table-of-contents)

---

### `CARRIAGE_RETURN`

Regex expression matching a carriage return character.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches the real carriage return character (`\r`) exactly once — the character itself, not a two-character escape text.

```regex
\r
```

**Example usage:**
```python
CARRIAGE_RETURN
# Matches: the single carriage return character
# Does not match: any other character
```

[▲ Back to top](#-table-of-contents)

---

### `FORM_FEED`

Regex expression matching a form feed character.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches the real form feed character (`\f`) exactly once — the character itself, not a two-character escape text.

```regex
\f
```

**Example usage:**
```python
FORM_FEED
# Matches: the single form feed character
# Does not match: any other character
```

[▲ Back to top](#-table-of-contents)

---

### `NEWLINE`

Regex expression matching a newline character.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches the real newline character (`\n`) exactly once — the character itself, not a two-character escape text.

```regex
\n
```

**Example usage:**
```python
NEWLINE
# Matches: the single newline character
# Does not match: any other character
```

[▲ Back to top](#-table-of-contents)

---

### `TAB`

Regex expression matching a tab character.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches the real tab character (`\t`) exactly once — the character itself, not a two-character escape text.

```regex
\t
```

**Example usage:**
```python
TAB
# Matches: the single tab character
# Does not match: any other character
```

[▲ Back to top](#-table-of-contents)

---

### `VERTICAL_TAB`

Regex expression matching a vertical tab character.

**Init Params:**
*(no parameters)*

**Pattern:**

Matches the real vertical tab character (`\v`) exactly once — the character itself, not a two-character escape text.

```regex
\v
```

**Example usage:**
```python
VERTICAL_TAB
# Matches: the single vertical tab character
# Does not match: any other character
```

[▲ Back to top](#-table-of-contents)

---

## 🔎 Lookaround

### `LOOKAHEAD`

Build a regex expression matching a positive lookahead assertion.

**Init Params:**
- `inner` (`Regex`): The inner regex expression that must follow the current position.

**Pattern:**

A zero-width positive lookahead assertion (`(?=...)`).

```regex
(?=...)
```

**Example usage:**
```python
pattern = Sequence(Literal("foo"), LOOKAHEAD(Literal("bar")))
# Matches: "foo" only if it is followed by "bar"
```

[▲ Back to top](#-table-of-contents)

---

### `LOOKBEHIND`

Build a regex expression matching a positive lookbehind assertion.

**Init Params:**
- `inner` (`Regex`): The inner regex expression that must precede the current position (must have a fixed length).

**Pattern:**

A zero-width positive lookbehind assertion (`(?<=...)`).

```regex
(?<=...)
```

**Example usage:**
```python
pattern = Sequence(LOOKBEHIND(Literal("foo")), Literal("bar"))
# Matches: "bar" only if it is preceded by "foo"
```

[▲ Back to top](#-table-of-contents)

---

### `NEGATIVE_LOOKAHEAD`

Build a regex expression matching a negative lookahead assertion.

**Init Params:**
- `inner` (`Regex`): The inner regex expression that must NOT follow the current position.

**Pattern:**

A zero-width negative lookahead assertion (`(?!...)`).

```regex
(?!...)
```

**Example usage:**
```python
pattern = Sequence(Literal("foo"), NEGATIVE_LOOKAHEAD(Literal("bar")))
# Matches: "foo" only if it is NOT followed by "bar"
```

[▲ Back to top](#-table-of-contents)

---

### `NEGATIVE_LOOKBEHIND`

Build a regex expression matching a negative lookbehind assertion.

**Init Params:**
- `inner` (`Regex`): The inner regex expression that must NOT precede the current position (must have a fixed length).

**Pattern:**

A zero-width negative lookbehind assertion (`(?<!...)`).

```regex
(?<!...)
```

**Example usage:**
```python
pattern = Sequence(NEGATIVE_LOOKBEHIND(Literal("foo")), Literal("bar"))
# Matches: "bar" only if it is NOT preceded by "foo"
```

[▲ Back to top](#-table-of-contents)

---

## 🔢 Quantifiers

### `AT_LEAST`

Build a regex expression matching a minimum number of occurrences.

**Init Params:**
- `inner` (`Regex`): The inner regex expression to repeat.
- `count` (`int`): The minimum required number of repetitions.
- `mode` (`RepeatMode`): The backtracking behavior (greedy, lazy, or possessive).

**Pattern:**

A minimum number of repetitions with no upper bound (`...{count,}`).

```regex
...{count,}
```

**Example usage:**
```python
pattern = AT_LEAST(DIGIT, 2)
# Matches: "12", "12345"
# Does not match: "1"
```

[▲ Back to top](#-table-of-contents)

---

### `BETWEEN`

Build a regex expression matching a bounded range of occurrences.

**Init Params:**
- `inner` (`Regex`): The inner regex expression to repeat.
- `min_count` (`int`): The minimum number of repetitions (inclusive).
- `max_count` (`int`): The maximum number of repetitions (inclusive).
- `mode` (`RepeatMode`): The backtracking behavior (greedy, lazy, or possessive).

**Pattern:**

A bounded range of repetitions (`...{min_count,max_count}`).

```regex
...{min_count,max_count}
```

**Example usage:**
```python
pattern = BETWEEN(DIGIT, 2, 4)
# Matches: "12", "123", "1234"
# Does not match: "1", "12345"
```

[▲ Back to top](#-table-of-contents)

---

### `EXACTLY`

Build a regex expression matching an exact count of occurrences.

**Init Params:**
- `inner` (`Regex`): The inner regex expression to repeat.
- `count` (`int`): The exact number of times the inner expression must repeat.

**Pattern:**

An exact number of repetitions (`...{count}`).

```regex
...{count}
```

**Example usage:**
```python
pattern = EXACTLY(DIGIT, 3)
# Matches: "123", "999"
# Does not match: "12", "1234"
```

[▲ Back to top](#-table-of-contents)

---

### `ONE_OR_MORE`

Build a regex expression matching one or more occurrences of the inner pattern.

**Init Params:**
- `inner` (`Regex`): The inner regex expression to repeat.
- `mode` (`RepeatMode`): The backtracking behavior (greedy, lazy, or possessive).

**Pattern:**

One or more occurrences of the inner node (`...+`).

```regex
...+
```

**Example usage:**
```python
pattern = ONE_OR_MORE(DIGIT)
# Matches: "5", "12345"
# Does not match: ""
```

[▲ Back to top](#-table-of-contents)

---

### `OPTIONAL`

Build a regex expression matching zero or one occurrence of the inner pattern.

**Init Params:**
- `inner` (`Regex`): The inner regex expression to make optional.

**Pattern:**

Zero or one occurrence of the inner node (`...?`).

```regex
...?
```

**Example usage:**
```python
pattern = OPTIONAL(Literal("s"))
# Matches: "s" or an empty string
```

[▲ Back to top](#-table-of-contents)

---

### `ZERO_OR_MORE`

Build a regex expression matching zero or more occurrences of the inner pattern.

**Init Params:**
- `inner` (`Regex`): The inner regex expression to repeat.
- `mode` (`RepeatMode`): The backtracking behavior (greedy, lazy, or possessive).

**Pattern:**

Zero or more occurrences of the inner node (`...*`).

```regex
...*
```

**Example usage:**
```python
pattern = ZERO_OR_MORE(DIGIT)
# Matches: "", "5", "12345"
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](../README.md#-propagated-regex-presets)