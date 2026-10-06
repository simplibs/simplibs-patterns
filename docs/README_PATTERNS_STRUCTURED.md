# 🧱 `patterns/structured` — Detailed Reference

Building blocks for structured text — lists, pairs, delimited and wrapped items — mostly as parametrized factories that take other expressions as arguments.

Every card below is the term's full docstring. Terms are grouped by how they are defined: **pure** (a named concept), **composed** (built from other terms, or a parametrized factory) and **custom** (needed a semantic decision — read its notes).

All expressions are `simplibs.regex` objects: combine them with `+` (sequence) and `|` (alternation), wrap them with the presets (`ONE_OR_MORE`, `NAMED_GROUP`, …) and compile with `RegexPattern`.

---

## 🧭 Table of Contents

**pure**:

- [`OPENING_DELIMITER`](#opening_delimiter)
- [`CLOSING_DELIMITER`](#closing_delimiter)

**composed**:

- [`DELIMITED_BY`](#delimited_by)
- [`LIST_OF`](#list_of)
- [`SEQUENCE_OF`](#sequence_of)
- [`PAIR_OF`](#pair_of)
- [`WRAPPED_BY`](#wrapped_by)
- [`KEY_VALUE_PAIR`](#key_value_pair)
- [`KEY_VALUE`](#key_value)

**custom**:

- [`SEPARATOR`](#separator)
- [`DELIMITER`](#delimiter)
- [`COMMA_SEPARATED_LIST`](#comma_separated_list)
- [`SEMICOLON_SEPARATED_LIST`](#semicolon_separated_list)
- [`SPACE_SEPARATED_LIST`](#space_separated_list)
- [`TAB_SEPARATED_LIST`](#tab_separated_list)

[⬅️ Back to main README](../README.md#-structured--15-terms)

---

### `OPENING_DELIMITER`

Regex expression matching an opening bracket.

**Init Params:**
*(no parameters)*

**Pattern:**
One of `(`, `[`, `{`, `<`.

```regex
[([{<]
```

**Example usage:**
```python
OPENING_DELIMITER
# Matches: "(", "[", "{", "<"
# Does not match: ")", "a", "(["
```

[▲ Back to top](#-table-of-contents)

---

### `CLOSING_DELIMITER`

Regex expression matching a closing bracket.

**Init Params:**
*(no parameters)*

**Pattern:**
One of `)`, `]`, `}`, `>`.

```regex
[)\]}>]
```

**Example usage:**
```python
CLOSING_DELIMITER
# Matches: ")", "]", "}", ">"
# Does not match: "(", "a", "])"
```

[▲ Back to top](#-table-of-contents)

---

### `DELIMITED_BY`

Build a regex expression matching one or more items separated by a delimiter.

**Init Params:**
* `item` (*Regex*): The expression for a single item.
* `delimiter` (*Regex*): The expression that separates items.

**Pattern:**
1. One `item`.
2. Any number of (`delimiter`, `item`) pairs.

**Example usage:**
```python
pattern = DELIMITED_BY(WORD, Literal("/"))
# Regex: \w+(?:/\w+)*
# Matches: "usr", "usr/local/bin"
# Does not match: "/usr", "usr/", "usr//bin", ""
```

[▲ Back to top](#-table-of-contents)

---

### `LIST_OF`

Build a regex expression matching a list of items, comma-separated by default.

**Init Params:**
* `item` (*Regex*): The expression for a single item.
* `separator` (*Regex*): The expression between items (default `COMMA`).

**Pattern:**
One or more `item`s separated by `separator`.

**Example usage:**
```python
pattern = LIST_OF(INTEGER)
# Regex: [0-9]+(?:,[0-9]+)*
# Matches: "1", "1,2,3", "42,7"
# Does not match: "", "1,", "1,,2", "1 2"
```

[▲ Back to top](#-table-of-contents)

---

### `SEQUENCE_OF`

Build a regex expression matching one or more consecutive items without separators.

**Init Params:**
* `item` (*Regex*): The expression to repeat.

**Pattern:**
`item` repeated one or more times.

**Example usage:**
```python
pattern = SEQUENCE_OF(Literal("ab"))
# Regex: (?:ab)+
# Matches: "ab", "ababab"
# Does not match: "", "aba"
```

[▲ Back to top](#-table-of-contents)

---

### `PAIR_OF`

Build a regex expression matching a key and a value joined by a separator.

**Init Params:**
* `key` (*Regex*): The expression for the key.
* `value` (*Regex*): The expression for the value.
* `separator` (*Regex*): The expression between key and value (default `EQUALS`).

**Pattern:**
`key`, then `separator`, then `value`.

**Example usage:**
```python
pattern = PAIR_OF(IDENTIFIER, INTEGER)
# Regex: [a-zA-Z_][a-zA-Z0-9_]*=[0-9]+
# Matches: "age=42", "x=0"
# Does not match: "age:42", "age=", "=42"
```

[▲ Back to top](#-table-of-contents)

---

### `WRAPPED_BY`

Build a regex expression matching an item wrapped between an opening and a closing expression.

**Init Params:**
* `item` (*Regex*): The wrapped expression.
* `opening` (*Regex*): The expression before the item.
* `closing` (*Regex*): The expression after the item.

**Pattern:**
`opening`, then `item`, then `closing`.

**Example usage:**
```python
pattern = WRAPPED_BY(INTEGER, Literal("<"), Literal(">"))
# Regex: <[0-9]+>
# Matches: "<42>"
# Does not match: "42", "<>", "<42"
```

[▲ Back to top](#-table-of-contents)

---

### `KEY_VALUE_PAIR`

Regex expression matching a key=value pair.

**Init Params:**
*(no parameters)*

**Pattern:**
An `IDENTIFIER`, an equals sign and a value without whitespace.

```regex
[a-zA-Z_][a-zA-Z0-9_]*=\S+
```

**Example usage:**
```python
KEY_VALUE_PAIR
# Matches: "name=value", "a=1", "path=/usr/bin"
# Does not match: "name", "=value", "a= b"
```

[▲ Back to top](#-table-of-contents)

---

### `KEY_VALUE`

Regex expression matching a key=value pair.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `KEY_VALUE_PAIR`; the separate name states the intended role.

**Example usage:**
```python
KEY_VALUE
# Matches: "name=value", "a=1", "path=/usr/bin"
# Does not match: "name", "=value", "a= b"
```

[▲ Back to top](#-table-of-contents)

---

### `SEPARATOR`

Regex expression matching a common separator character.

**Init Params:**
*(no parameters)*

**Pattern:**
One of comma, semicolon, pipe, tab or space.

```regex
[,;|\t ]
```

**Example usage:**
```python
SEPARATOR
# Matches: ",", ";", "|", "\t"
# Does not match: "a", "::", ""
```

[▲ Back to top](#-table-of-contents)

---

### `DELIMITER`

Regex expression matching a delimiter character.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `SEPARATOR`; the separate name states the intended role.

**Notes:**

Same set as `SEPARATOR`. Bracket-like delimiters: `OPENING_DELIMITER`, `CLOSING_DELIMITER`.

**Example usage:**
```python
DELIMITER
# Matches: ",", ";", "|", "\t"
# Does not match: "a", "::", ""
```

[▲ Back to top](#-table-of-contents)

---

### `COMMA_SEPARATED_LIST`

Regex expression matching a list of items separated by a comma.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more items, each made of any characters except the comma, separated by a comma.

```regex
[^,]+(?:,[^,]+)*
```

**Notes:**

Items are not further restricted. For typed items use `LIST_OF(item, separator)`.

**Example usage:**
```python
COMMA_SEPARATED_LIST
# Matches: "a,b,c", "single"
# Does not match: "", "a,,b", "a,"
```

[▲ Back to top](#-table-of-contents)

---

### `SEMICOLON_SEPARATED_LIST`

Regex expression matching a list of items separated by a semicolon.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more items, each made of any characters except the semicolon, separated by a semicolon.

```regex
[^;]+(?:;[^;]+)*
```

**Notes:**

Items are not further restricted. For typed items use `LIST_OF(item, separator)`.

**Example usage:**
```python
SEMICOLON_SEPARATED_LIST
# Matches: "a;b;c", "single"
# Does not match: "", "a;;b"
```

[▲ Back to top](#-table-of-contents)

---

### `SPACE_SEPARATED_LIST`

Regex expression matching a list of items separated by a space.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more items, each made of any characters except the space, separated by a space.

```regex
[^ ]+(?:\ [^ ]+)*
```

**Notes:**

Items are not further restricted. For typed items use `LIST_OF(item, separator)`.

**Example usage:**
```python
SPACE_SEPARATED_LIST
# Matches: "a b c", "single"
# Does not match: "", "a  b"
```

[▲ Back to top](#-table-of-contents)

---

### `TAB_SEPARATED_LIST`

Regex expression matching a list of items separated by a tab.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more items, each made of any characters except the tab, separated by a tab.

```regex
[^\t]+(?:\t[^\t]+)*
```

**Notes:**

Items are not further restricted. For typed items use `LIST_OF(item, separator)`.

**Example usage:**
```python
TAB_SEPARATED_LIST
# Matches: "a\tb\tc", "single"
# Does not match: "", "a\t\tb"
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](../README.md#-structured--15-terms)
