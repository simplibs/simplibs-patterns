# 📬 `patterns/addresses` — Detailed Reference

Addresses of people and machines — IP, email, phone numbers, postal codes, street addresses and P.O. boxes.

Every card below is the term's full docstring. Terms are grouped by how they are defined: **pure** (a named concept), **composed** (built from other terms, or a parametrized factory) and **custom** (needed a semantic decision — read its notes).

All expressions are `simplibs.regex` objects: combine them with `+` (sequence) and `|` (alternation), wrap them with the presets (`ONE_OR_MORE`, `NAMED_GROUP`, …) and compile with `RegexPattern`.

---

## 🧭 Table of Contents

**pure**:

- [`EMAIL_LOCAL_PART`](#email_local_part)

**composed**:

- [`IP_ADDRESS`](#ip_address)
- [`PO_BOX`](#po_box)

**custom**:

- [`EMAIL_ADDRESS`](#email_address)
- [`PHONE_NUMBER`](#phone_number)
- [`INTERNATIONAL_PHONE_NUMBER`](#international_phone_number)
- [`POSTAL_CODE`](#postal_code)
- [`ZIP_CODE`](#zip_code)
- [`STREET_ADDRESS`](#street_address)
- 
---

### `EMAIL_LOCAL_PART`

Regex expression matching the part of an email address before the @.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more letters, digits or ``. _ % + -``.

```regex
[a-zA-Z0-9._%+\-]+
```

**Example usage:**
```python
EMAIL_LOCAL_PART
# Matches: "john.doe", "user+tag", "a"
# Does not match: "a@b", "", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `IP_ADDRESS`

Regex expression matching an IPv4 or IPv6 address.

**Init Params:**
*(no parameters)*

**Pattern:**
`IPV4_ADDRESS` or `IPV6_ADDRESS`.

**Notes:**

`IPV4_ADDRESS`, `IPV6_ADDRESS` and `MAC_ADDRESS` live in the `formats` domain.

**Example usage:**
```python
IP_ADDRESS
# Matches: "192.168.0.1", "::1", "2001:db8::ff00:42:8329"
# Does not match: "256.1.1.1", "1.2.3", ""
```

[▲ Back to top](#-table-of-contents)

---

### `PO_BOX`

Regex expression matching a P.O. box line.

**Init Params:**
*(no parameters)*

**Pattern:**
`P.O. Box` (dots optional) followed by a number.

```regex
P\.?O\.?\ Box\ [0-9]+
```

**Notes:**

Case-sensitive; use the `IGNORECASE` flag to relax it.

**Example usage:**
```python
PO_BOX
# Matches: "P.O. Box 123", "PO Box 45", "P.O Box 7"
# Does not match: "Box 123", "P.O. Box", "po box 5"
```

[▲ Back to top](#-table-of-contents)

---

### `EMAIL_ADDRESS`

Regex expression matching an email address.

**Init Params:**
*(no parameters)*

**Pattern:**
An `EMAIL_LOCAL_PART`, `@` and a `DOMAIN` (at least two labels).

```regex
[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+
```

**Notes:**

A practical subset of RFC 5322: no quoted local parts, no comments, no IP-literal domains.

**Example usage:**
```python
EMAIL_ADDRESS
# Matches: "john.doe@example.com", "a+b@sub.example.co.uk"
# Does not match: "john@localhost", "@example.com", "john@", "a b@x.com"
```

[▲ Back to top](#-table-of-contents)

---

### `PHONE_NUMBER`

Regex expression matching a phone number in a lenient written form.

**Init Params:**
*(no parameters)*

**Pattern:**
An optional `+`, then digits mixed with spaces, hyphens and parentheses, ending in a digit (about 7–20 characters).

```regex
\+?[0-9(][0-9 \-()]{5,18}[0-9]
```

**Notes:**

Lenient on purpose: the count of digits and the country rules are not checked.

**Example usage:**
```python
PHONE_NUMBER
# Matches: "+420 123 456 789", "(555) 123-4567", "555-1234"
# Does not match: "12345", "abc", "+"
```

[▲ Back to top](#-table-of-contents)

---

### `INTERNATIONAL_PHONE_NUMBER`

Regex expression matching an international phone number in E.164 form.

**Init Params:**
*(no parameters)*

**Pattern:**
`+`, a country code starting 1–9 and further digits — 7 to 15 digits in total, no separators.

```regex
\+[1-9][0-9]{6,14}
```

**Example usage:**
```python
INTERNATIONAL_PHONE_NUMBER
# Matches: "+420123456789", "+14155552671"
# Does not match: "420123456789", "+0123456789", "+123", "+420 123 456 789"
```

[▲ Back to top](#-table-of-contents)

---

### `POSTAL_CODE`

Regex expression matching a postal code in a generic international form.

**Init Params:**
*(no parameters)*

**Pattern:**
3–10 characters: letters, digits, spaces or hyphens, starting and ending with a letter or digit.

```regex
[a-zA-Z0-9][a-zA-Z0-9 \-]{1,8}[a-zA-Z0-9]
```

**Notes:**

Generic; it cannot reject malformed codes of a particular country.

**Example usage:**
```python
POSTAL_CODE
# Matches: "110 00", "SW1A 1AA", "90210", "10115"
# Does not match: "1", "12", "-1234", "12 "
```

[▲ Back to top](#-table-of-contents)

---

### `ZIP_CODE`

Regex expression matching a US ZIP code.

**Init Params:**
*(no parameters)*

**Pattern:**
Five digits, optionally followed by a hyphen and four digits (ZIP+4).

```regex
[0-9]{5}(?:\-[0-9]{4})?
```

**Example usage:**
```python
ZIP_CODE
# Matches: "90210", "90210-1234"
# Does not match: "9021", "90210-12", "902101234"
```

[▲ Back to top](#-table-of-contents)

---

### `STREET_ADDRESS`

Regex expression matching a street address line in a lenient form.

**Init Params:**
*(no parameters)*

**Pattern:**
Text of word characters, spaces and ``. , ' - /`` that contains at least one letter (any language) and at least one digit.

```regex
(?=.*\d)(?=.*[^\W\d_])[\w .,'\-/]+
```

**Notes:**

Locale-independent heuristic: it recognises the shape 'letters + a number', not a real address grammar.

**Example usage:**
```python
STREET_ADDRESS
# Matches: "Václavské náměstí 1", "221B Baker Street", "5 Main St.", "Hlavní 12/3"
# Does not match: "Main Street", "12345", "", "12 @ home"
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](../README.md)
