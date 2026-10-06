# 💻 `patterns/programming` — Detailed Reference

Source-code constructs that depend on the language — comments, strings, keywords, imports, literals — selected with a `Language` enum, plus a few language-neutral terms.

Every card below is the term's full docstring. Terms are grouped by how they are defined: **pure** (a named concept), **composed** (built from other terms, or a parametrized factory) and **custom** (needed a semantic decision — read its notes).

All expressions are `simplibs.regex` objects: combine them with `+` (sequence) and `|` (alternation), wrap them with the presets (`ONE_OR_MORE`, `NAMED_GROUP`, …) and compile with `RegexPattern`.

---

## 🧭 Table of Contents

**pure**:

- [`OPERATOR`](#operator)

**composed**:

- [`NUMBER_LITERAL`](#number_literal)

**custom**:

- [`COMMENT`](#comment)
- [`STRING_LITERAL`](#string_literal)
- [`BOOLEAN_LITERAL`](#boolean_literal)
- [`NULL_LITERAL`](#null_literal)
- [`KEYWORD`](#keyword)
- [`IMPORT`](#import)

**enums**:

- [`Language`](#language)

[⬅️ Back to main README](../README.md#-programming--9-terms)

---

### `OPERATOR`

Regex expression matching a common operator shared by most languages.

**Init Params:**
*(no parameters)*

**Pattern:**
`==`, `!=`, `<=`, `>=` or one of `+ - * / = < >`; two-character operators are tried first.

```regex
==|!=|<=|>=|[+\-*/=<>]
```

**Example usage:**
```python
OPERATOR
# Matches: "==", "!=", "<=", "+"
# Does not match: "=>", "a", "!", ""
```

[▲ Back to top](#-table-of-contents)

---

### `NUMBER_LITERAL`

Regex expression matching an unsigned numeric literal.

**Init Params:**
*(no parameters)*

**Pattern:**
A `SCIENTIFIC` number, a `DECIMAL` or an `INTEGER`.

```regex
(?:[0-9]+\.[0-9]+|[0-9]+)[eE][+\-]?[0-9]+|[0-9]+\.[0-9]+|[0-9]+
```

**Notes:**

Unsigned: a leading minus is an operator in source code. Language-specific forms (0x, 1_000, 10n) are not covered.

**Example usage:**
```python
NUMBER_LITERAL
# Matches: "42", "3.14", "1e10", "2.5E-3"
# Does not match: "", "abc", "1.", "-5"
```

[▲ Back to top](#-table-of-contents)

---

### `COMMENT`

Build a regex expression matching a single-line comment in the given language.

**Init Params:**
* `language` (*Language*): The programming language whose comment syntax is used.

**Pattern:**
From the comment marker (`#` for Python, `//` for JavaScript) to the end of the line.

**Notes:**

A `#` or `//` inside a string literal is not distinguished from a real comment marker.
Block comments (`/* ... */`) are not covered.

**Example usage:**
```python
pattern = COMMENT(Language.PYTHON)
# Regex: \#.*
# Finds "# set x" in "x = 1  # set x"
# No match in: "x = 1"
```

[▲ Back to top](#-table-of-contents)

---

### `STRING_LITERAL`

Build a regex expression matching a string literal in the given language.

**Init Params:**
* `language` (*Language*): The programming language whose string syntax is used.

**Pattern:**
A quoted string with backslash escapes: single or double quotes (Python), plus backticks (JavaScript).

**Notes:**

Single-line strings only; prefixes (f"", r"", b""), triple quotes and template-literal interpolation are not covered.

**Example usage:**
```python
pattern = STRING_LITERAL(Language.PYTHON)
# Regex: '(?:[^'\\n]|\\.)*'|"(?:[^"\\n]|\\.)*"
# Finds "'hi'" in "x = 'hi'"
# Finds '"a \" b"' in 'print("a \" b")'
# No match in: "x = 1", "'open"
```

[▲ Back to top](#-table-of-contents)

---

### `BOOLEAN_LITERAL`

Build a regex expression matching a boolean literal in the given language.

**Init Params:**
* `language` (*Language*): The programming language whose boolean literals are used.

**Pattern:**
`True` / `False` for Python, `true` / `false` for JavaScript, as whole words.

**Example usage:**
```python
pattern = BOOLEAN_LITERAL(Language.PYTHON)
# Regex: \bTrue\b|\bFalse\b
# Finds "True" in "flag = True"
# No match in: "flag = true", "Truely"
```

[▲ Back to top](#-table-of-contents)

---

### `NULL_LITERAL`

Build a regex expression matching the null literal of the given language.

**Init Params:**
* `language` (*Language*): The programming language whose null literal is used.

**Pattern:**
`None` for Python, `null` for JavaScript, as a whole word.

**Example usage:**
```python
pattern = NULL_LITERAL(Language.JAVASCRIPT)
# Regex: \bnull\b
# Finds "null" in "x = null"
# No match in: "x = None", "nullable"
```

[▲ Back to top](#-table-of-contents)

---

### `KEYWORD`

Build a regex expression matching a reserved keyword of the given language.

**Init Params:**
* `language` (*Language*): The programming language whose keywords are used.

**Pattern:**
Any reserved word of the language, as a whole word.

**Notes:**

Hard keywords only. Soft keywords (Python `match`, `case`, `type`) and the literals `True` / `None` are not special-cased beyond the list.

**Example usage:**
```python
pattern = KEYWORD(Language.PYTHON)
# Finds "def" in "def main():"
# Finds "lambda" in "x = lambda: 0"
# No match in: "define", "x = 1"
```

[▲ Back to top](#-table-of-contents)

---

### `IMPORT`

Build a regex expression matching an import statement in the given language.

**Init Params:**
* `language` (*Language*): The programming language whose import syntax is used.

**Pattern:**
Python: `import a.b [as c]` or `from a.b import x [as y], z` (relative dots and `*` allowed).
JavaScript: `import x from "m"`, `import { a, b as c } from "m"`, `import * as ns from "m"` or `import "m"`.

**Notes:**

Matches one statement on one line. Parenthesised multi-line Python imports and JavaScript default-plus-named forms (`import a, { b } from "m"`) are not covered.

**Example usage:**
```python
pattern = IMPORT(Language.PYTHON)
# Matches: "import os", "import os.path as p", "from os import path", "from . import x"
# Does not match: "import", "from os", "importos", "import os as"
```

[▲ Back to top](#-table-of-contents)

---

### `Language`

Programming language selector for language-dependent regex expressions.

**Members:**
* `PYTHON`
* `JAVASCRIPT`

**Example usage:**
```python
COMMENT(Language.PYTHON)       # matches "# a comment"
COMMENT(Language.JAVASCRIPT)   # matches "// a comment"
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](../README.md#-programming--9-terms)
