# 💬 `patterns/communication` — Detailed Reference

Communication artefacts — email, user names and handles, hashtags, display names, message ids and email headers.

Every card below is the term's full docstring. Terms are grouped by how they are defined: **pure** (a named concept), **composed** (built from other terms, or a parametrized factory) and **custom** (needed a semantic decision — read its notes).

All expressions are `simplibs.regex` objects: combine them with `+` (sequence) and `|` (alternation), wrap them with the presets (`ONE_OR_MORE`, `NAMED_GROUP`, …) and compile with `RegexPattern`.

---

## 🧭 Table of Contents

**pure**:

- [`EMAIL`](#email)
- [`USER_HANDLE`](#user_handle)
- [`MENTION`](#mention)
- [`SOCIAL_HANDLE`](#social_handle)
- [`HASHTAG`](#hashtag)
- [`SUBJECT`](#subject)
- [`REPLY_ADDRESS`](#reply_address)
- [`SENDER_ADDRESS`](#sender_address)
- [`RECIPIENT_ADDRESS`](#recipient_address)
- [`EMAIL_HEADER_NAME`](#email_header_name)
- [`EMAIL_HEADER_VALUE`](#email_header_value)

**composed**:

- [`EMAIL_HEADER`](#email_header)
- [`EMAIL_SUBJECT`](#email_subject)

**custom**:

- [`USERNAME`](#username)
- [`DISPLAY_NAME`](#display_name)
- [`MESSAGE_ID`](#message_id)

---

### `EMAIL`

Regex expression matching an email address.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `EMAIL_ADDRESS`; the separate name states the intended role.

**Notes:**

`EMAIL_ADDRESS` lives in the `addresses` domain.

**Example usage:**
```python
EMAIL
# Matches: "john.doe@example.com", "a+b@sub.example.co.uk"
# Does not match: "john@localhost", "@example.com", "john@", "a b@x.com"
```

[▲ Back to top](#-table-of-contents)

---

### `USER_HANDLE`

Regex expression matching a user handle such as @name.

**Init Params:**
*(no parameters)*

**Pattern:**
`@` followed by an `IDENTIFIER`.

```regex
@[a-zA-Z_][a-zA-Z0-9_]*
```

**Example usage:**
```python
USER_HANDLE
# Matches: "@john", "@john_doe1"
# Does not match: "john", "@", "@1abc"
```

[▲ Back to top](#-table-of-contents)

---

### `MENTION`

Regex expression matching a mention.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `USER_HANDLE`; the separate name states the intended role.

**Example usage:**
```python
MENTION
# Matches: "@john", "@john_doe1"
# Does not match: "john", "@", "@1abc"
```

[▲ Back to top](#-table-of-contents)

---

### `SOCIAL_HANDLE`

Regex expression matching a social media handle.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `USER_HANDLE`; the separate name states the intended role.

**Example usage:**
```python
SOCIAL_HANDLE
# Matches: "@john", "@john_doe1"
# Does not match: "john", "@", "@1abc"
```

[▲ Back to top](#-table-of-contents)

---

### `HASHTAG`

Regex expression matching a hashtag.

**Init Params:**
*(no parameters)*

**Pattern:**
`#` followed by one or more word characters (Unicode-aware).

```regex
\#\w+
```

**Example usage:**
```python
HASHTAG
# Matches: "#python", "#2026", "#ahoj_světe"
# Does not match: "python", "#", "# tag"
```

[▲ Back to top](#-table-of-contents)

---

### `SUBJECT`

Regex expression matching a message subject.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `NON_EMPTY_TEXT`; the separate name states the intended role.

**Notes:**

One non-empty line of text.

**Example usage:**
```python
SUBJECT
# Matches: "a", "Hello, world!"
# Does not match: ""
```

[▲ Back to top](#-table-of-contents)

---

### `REPLY_ADDRESS`

Regex expression matching a reply-to email address.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `EMAIL_ADDRESS`; the separate name states the intended role.

**Example usage:**
```python
REPLY_ADDRESS
# Matches: "john.doe@example.com", "a+b@sub.example.co.uk"
# Does not match: "john@localhost", "@example.com", "john@", "a b@x.com"
```

[▲ Back to top](#-table-of-contents)

---

### `SENDER_ADDRESS`

Regex expression matching a sender email address.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `EMAIL_ADDRESS`; the separate name states the intended role.

**Example usage:**
```python
SENDER_ADDRESS
# Matches: "john.doe@example.com", "a+b@sub.example.co.uk"
# Does not match: "john@localhost", "@example.com", "john@", "a b@x.com"
```

[▲ Back to top](#-table-of-contents)

---

### `RECIPIENT_ADDRESS`

Regex expression matching a recipient email address.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `EMAIL_ADDRESS`; the separate name states the intended role.

**Example usage:**
```python
RECIPIENT_ADDRESS
# Matches: "john.doe@example.com", "a+b@sub.example.co.uk"
# Does not match: "john@localhost", "@example.com", "john@", "a b@x.com"
```

[▲ Back to top](#-table-of-contents)

---

### `EMAIL_HEADER_NAME`

Regex expression matching an email header field name.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more printable ASCII characters except space and colon.

```regex
[!-9;-~]+
```

**Example usage:**
```python
EMAIL_HEADER_NAME
# Matches: "Subject", "X-Mailer", "Content-Type"
# Does not match: "Sub ject", "Name:", ""
```

[▲ Back to top](#-table-of-contents)

---

### `EMAIL_HEADER_VALUE`

Regex expression matching an email header field value.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `LINE`; the separate name states the intended role.

**Notes:**

One line of text; may be empty.

**Example usage:**
```python
EMAIL_HEADER_VALUE
# Matches: "", "one line", "a b c"
# Does not match: "a\nb"
```

[▲ Back to top](#-table-of-contents)

---

### `EMAIL_HEADER`

Regex expression matching an email header line.

**Init Params:**
*(no parameters)*

**Pattern:**
An `EMAIL_HEADER_NAME`, `:`, optional spaces and an `EMAIL_HEADER_VALUE`.

```regex
[!-9;-~]+:\ *.*
```

**Notes:**

Folded (multi-line) headers are not covered.

**Example usage:**
```python
EMAIL_HEADER
# Matches: "Subject: Hello", "From:x@y.com", "X-Empty:"
# Does not match: "no header", "Name value"
```

[▲ Back to top](#-table-of-contents)

---

### `EMAIL_SUBJECT`

Regex expression matching an email Subject header line.

**Init Params:**
*(no parameters)*

**Pattern:**
`Subject:`, optional spaces and a `SUBJECT`.

```regex
Subject:\ *.+
```

**Notes:**

Case-sensitive; use the `IGNORECASE` flag because header names are case-insensitive.

**Example usage:**
```python
EMAIL_SUBJECT
# Matches: "Subject: Meeting tomorrow"
# Does not match: "Subject:", "From: a"
```

[▲ Back to top](#-table-of-contents)

---

### `USERNAME`

Regex expression matching a user name of 3–32 characters.

**Init Params:**
*(no parameters)*

**Pattern:**
A letter or digit, then 2–31 letters, digits or ``. _ -``.

```regex
[a-zA-Z0-9][a-zA-Z0-9._\-]{2,31}
```

**Example usage:**
```python
USERNAME
# Matches: "john_doe", "user.name-1", "abc"
# Does not match: "ab", "_user", "a b", ""
```

[▲ Back to top](#-table-of-contents)

---

### `DISPLAY_NAME`

Regex expression matching a person's display name.

**Init Params:**
*(no parameters)*

**Pattern:**
A letter, then letters, spaces, dots, apostrophes or hyphens (any language).

```regex
[^\W\d_](?:[^\W\d_]|[ .'\-])*
```

**Notes:**

Does not allow digits or emoji.

**Example usage:**
```python
DISPLAY_NAME
# Matches: "Jan Novák", "Mary-Jane O'Neil", "J. R. R. Tolkien"
# Does not match: "", "123", "_x"
```

[▲ Back to top](#-table-of-contents)

---

### `MESSAGE_ID`

Regex expression matching an email Message-ID.

**Init Params:**
*(no parameters)*

**Pattern:**
`<`, a part, `@`, a part and `>`, where parts contain no `<`, `>`, `@` or whitespace.

```regex
<[^@<>\s]+@[^@<>\s]+>
```

**Example usage:**
```python
MESSAGE_ID
# Matches: "<abc123@mail.example.com>"
# Does not match: "abc@x", "<abc>", "<a@b@c>"
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](../README.md)
