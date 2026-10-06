# 🏷️ `patterns/identifiers` — Detailed Reference

Names and identifiers — plain and dotted identifiers, role-specific names (variable, class, module…), markup tag names, and prefix/suffix helpers.

Every card below is the term's full docstring. Terms are grouped by how they are defined: **pure** (a named concept), **composed** (built from other terms, or a parametrized factory) and **custom** (needed a semantic decision — read its notes).

All expressions are `simplibs.regex` objects: combine them with `+` (sequence) and `|` (alternation), wrap them with the presets (`ONE_OR_MORE`, `NAMED_GROUP`, …) and compile with `RegexPattern`.

---

## 🧭 Table of Contents

**pure**:

- [`IDENTIFIER_START_CHARACTER`](#identifier_start_character)
- [`IDENTIFIER_CHARACTER`](#identifier_character)
- [`IDENTIFIER`](#identifier)
- [`SIMPLE_IDENTIFIER`](#simple_identifier)
- [`NAME`](#name)
- [`QUALIFIED_IDENTIFIER`](#qualified_identifier)
- [`QUALIFIED_NAME`](#qualified_name)
- [`NAMESPACE`](#namespace)
- [`NAMESPACE_NAME`](#namespace_name)
- [`VARIABLE_NAME`](#variable_name)
- [`CONSTANT_NAME`](#constant_name)
- [`FUNCTION_NAME`](#function_name)
- [`METHOD_NAME`](#method_name)
- [`CLASS_NAME`](#class_name)
- [`TYPE_NAME`](#type_name)
- [`MODULE_NAME`](#module_name)
- [`PACKAGE_NAME`](#package_name)
- [`ATTRIBUTE_NAME`](#attribute_name)
- [`PROPERTY_NAME`](#property_name)
- [`PARAMETER_NAME`](#parameter_name)
- [`ARGUMENT_NAME`](#argument_name)
- [`ENUM_NAME`](#enum_name)
- [`ENUM_MEMBER_NAME`](#enum_member_name)
- [`KEY`](#key)
- [`VALUE_NAME`](#value_name)
- [`LABEL`](#label)

**composed**:

- [`QUALIFIED_IDENTIFIER_OF`](#qualified_identifier_of)
- [`IDENTIFIER_WITH_PREFIX`](#identifier_with_prefix)
- [`IDENTIFIER_WITH_SUFFIX`](#identifier_with_suffix)

**custom**:

- [`TAG_NAME`](#tag_name)
- [`ELEMENT_NAME`](#element_name)

---

### `IDENTIFIER_START_CHARACTER`

Regex expression matching a character an identifier may start with.

**Init Params:**
*(no parameters)*

**Pattern:**
A letter `a`–`z`, `A`–`Z` or an underscore.

```regex
[a-zA-Z_]
```

**Example usage:**
```python
IDENTIFIER_START_CHARACTER
# Matches: "a", "Z", "_"
# Does not match: "1", "-", "ab"
```

[▲ Back to top](#-table-of-contents)

---

### `IDENTIFIER_CHARACTER`

Regex expression matching a character that may appear inside an identifier.

**Init Params:**
*(no parameters)*

**Pattern:**
A letter, a digit or an underscore (ASCII only).

```regex
[a-zA-Z0-9_]
```

**Example usage:**
```python
IDENTIFIER_CHARACTER
# Matches: "a", "Z", "5", "_"
# Does not match: "-", "ab", " "
```

[▲ Back to top](#-table-of-contents)

---

### `IDENTIFIER`

Regex expression matching a language-neutral identifier.

**Init Params:**
*(no parameters)*

**Pattern:**
A letter or underscore, followed by any number of letters, digits or underscores.

```regex
[a-zA-Z_][a-zA-Z0-9_]*
```

**Notes:**

ASCII only. Naming conventions (snake_case, PascalCase, UPPER_CASE) are not enforced.

**Example usage:**
```python
IDENTIFIER
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `SIMPLE_IDENTIFIER`

Regex expression matching a simple (unqualified) identifier.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Example usage:**
```python
SIMPLE_IDENTIFIER
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `NAME`

Regex expression matching a name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Example usage:**
```python
NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `QUALIFIED_IDENTIFIER`

Regex expression matching a dotted identifier with at least two parts.

**Init Params:**
*(no parameters)*

**Pattern:**
An `IDENTIFIER` followed by one or more (dot, `IDENTIFIER`) pairs.

```regex
[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)+
```

**Notes:**

Needs at least one dot; use `NAMESPACE` when a single part is also fine.

**Example usage:**
```python
QUALIFIED_IDENTIFIER
# Matches: "os.path", "a.b.c"
# Does not match: "os", "os.", "a..b", ".a"
```

[▲ Back to top](#-table-of-contents)

---

### `QUALIFIED_NAME`

Regex expression matching a qualified name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `QUALIFIED_IDENTIFIER`; the separate name states the intended role.

**Example usage:**
```python
QUALIFIED_NAME
# Matches: "os.path", "a.b.c"
# Does not match: "os", "os.", "a..b", ".a"
```

[▲ Back to top](#-table-of-contents)

---

### `NAMESPACE`

Regex expression matching a namespace path of one or more parts.

**Init Params:**
*(no parameters)*

**Pattern:**
An `IDENTIFIER` followed by any number of (dot, `IDENTIFIER`) pairs.

```regex
[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*
```

**Example usage:**
```python
NAMESPACE
# Matches: "std", "std.io", "a.b.c"
# Does not match: "", "a.", "1a"
```

[▲ Back to top](#-table-of-contents)

---

### `NAMESPACE_NAME`

Regex expression matching a namespace name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `NAMESPACE`; the separate name states the intended role.

**Example usage:**
```python
NAMESPACE_NAME
# Matches: "std", "std.io", "a.b.c"
# Does not match: "", "a.", "1a"
```

[▲ Back to top](#-table-of-contents)

---

### `VARIABLE_NAME`

Regex expression matching a variable name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
VARIABLE_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `CONSTANT_NAME`

Regex expression matching a constant name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
CONSTANT_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `FUNCTION_NAME`

Regex expression matching a function name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
FUNCTION_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `METHOD_NAME`

Regex expression matching a method name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
METHOD_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `CLASS_NAME`

Regex expression matching a class name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
CLASS_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `TYPE_NAME`

Regex expression matching a type name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
TYPE_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `MODULE_NAME`

Regex expression matching a module name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
MODULE_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `PACKAGE_NAME`

Regex expression matching a package name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
PACKAGE_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `ATTRIBUTE_NAME`

Regex expression matching an attribute name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
ATTRIBUTE_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `PROPERTY_NAME`

Regex expression matching a property name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
PROPERTY_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `PARAMETER_NAME`

Regex expression matching a parameter name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
PARAMETER_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `ARGUMENT_NAME`

Regex expression matching an argument name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
ARGUMENT_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `ENUM_NAME`

Regex expression matching an enumeration name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
ENUM_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `ENUM_MEMBER_NAME`

Regex expression matching an enumeration member name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
ENUM_MEMBER_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `KEY`

Regex expression matching a key name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
KEY
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `VALUE_NAME`

Regex expression matching a value name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
VALUE_NAME
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `LABEL`

Regex expression matching a label name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `IDENTIFIER`; the separate name states the intended role.

**Notes:**

Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

**Example usage:**
```python
LABEL
# Matches: "name", "_private", "snake_case_2", "X"
# Does not match: "2fast", "with-dash", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `QUALIFIED_IDENTIFIER_OF`

Build a regex expression matching a dotted identifier with an exact number of parts.

**Init Params:**
* `parts` (*int*): How many identifiers the dotted name consists of (at least 1).

**Pattern:**
An `IDENTIFIER` followed by exactly `parts - 1` (dot, `IDENTIFIER`) pairs.

**Example usage:**
```python
pattern = QUALIFIED_IDENTIFIER_OF(3)
# Regex: [a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*){2}
# Matches: "a.b.c", "os.path.join"
# Does not match: "a.b", "a.b.c.d", "abc"
```

[▲ Back to top](#-table-of-contents)

---

### `IDENTIFIER_WITH_PREFIX`

Build a regex expression matching an identifier part that follows a fixed prefix.

**Init Params:**
* `prefix` (*str*): The literal text the name must start with.

**Pattern:**
The literal `prefix`, followed by an `IDENTIFIER`.

**Notes:**

The part after the prefix must itself be a valid identifier, so `get_1` is rejected.

**Example usage:**
```python
pattern = IDENTIFIER_WITH_PREFIX("get_")
# Regex: get_[a-zA-Z_][a-zA-Z0-9_]*
# Matches: "get_value", "get_x1"
# Does not match: "get_", "value"
```

[▲ Back to top](#-table-of-contents)

---

### `IDENTIFIER_WITH_SUFFIX`

Build a regex expression matching an identifier part followed by a fixed suffix.

**Init Params:**
* `suffix` (*str*): The literal text the name must end with.

**Pattern:**
An `IDENTIFIER`, followed by the literal `suffix`.

**Example usage:**
```python
pattern = IDENTIFIER_WITH_SUFFIX("_id")
# Regex: [a-zA-Z_][a-zA-Z0-9_]*_id
# Matches: "user_id", "order_id"
# Does not match: "_id", "user"
```

[▲ Back to top](#-table-of-contents)

---

### `TAG_NAME`

Regex expression matching a markup tag name.

**Init Params:**
*(no parameters)*

**Pattern:**
A letter, then letters, digits or hyphens (e.g. `div`, `h1`, `my-element`).

```regex
[a-zA-Z][a-zA-Z0-9\-]*
```

**Notes:**

Covers HTML-style names. XML names may also contain `:`, `.` and `_`.

**Example usage:**
```python
TAG_NAME
# Matches: "div", "h1", "my-element"
# Does not match: "1div", "-x", "", "a_b"
```

[▲ Back to top](#-table-of-contents)

---

### `ELEMENT_NAME`

Regex expression matching a markup element name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `TAG_NAME`; the separate name states the intended role.

**Example usage:**
```python
ELEMENT_NAME
# Matches: "div", "h1", "my-element"
# Does not match: "1div", "-x", "", "a_b"
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](../README.md)
