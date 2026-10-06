# 🧬 `patterns/formats` — Detailed Reference

Well-known text formats — UUID, colors, versions, MAC and IP addresses, ISBN/ISSN, card and bank numbers, Base64, hashes, ULID and JWT.

Every card below is the term's full docstring. Terms are grouped by how they are defined: **pure** (a named concept), **composed** (built from other terms, or a parametrized factory) and **custom** (needed a semantic decision — read its notes).

All expressions are `simplibs.regex` objects: combine them with `+` (sequence) and `|` (alternation), wrap them with the presets (`ONE_OR_MORE`, `NAMED_GROUP`, …) and compile with `RegexPattern`.

---

## 🧭 Table of Contents

**pure**:

- [`UUID`](#uuid)
- [`GUID`](#guid)
- [`HEX_COLOR`](#hex_color)
- [`VERSION`](#version)
- [`MAC_ADDRESS`](#mac_address)
- [`IPV4_ADDRESS`](#ipv4_address)
- [`ISBN10`](#isbn10)
- [`ISBN13`](#isbn13)
- [`ISSN`](#issn)
- [`BASE64_CHARACTER`](#base64_character)
- [`BASE64_URL_CHARACTER`](#base64_url_character)
- [`HEX_STRING`](#hex_string)
- [`MD5`](#md5)
- [`SHA1`](#sha1)
- [`SHA256`](#sha256)

**composed**:

- [`RGB_COLOR`](#rgb_color)
- [`RGBA_COLOR`](#rgba_color)
- [`ISBN`](#isbn)
- [`HASH`](#hash)

**custom**:

- [`SEMVER`](#semver)
- [`IPV6_ADDRESS`](#ipv6_address)
- [`CREDIT_CARD_NUMBER`](#credit_card_number)
- [`IBAN`](#iban)
- [`BASE64`](#base64)
- [`BASE64_URL`](#base64_url)
- [`ULID`](#ulid)
- [`JWT`](#jwt)

[⬅️ Back to main README](../README.md#-formats--27-terms)

---

### `UUID`

Regex expression matching a UUID in canonical form.

**Init Params:**
*(no parameters)*

**Pattern:**
Hex groups of 8-4-4-4-12 digits separated by hyphens.

```regex
[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}
```

**Notes:**

Version and variant bits are not checked.

**Example usage:**
```python
UUID
# Matches: "123e4567-e89b-12d3-a456-426614174000", "00000000-0000-0000-0000-000000000000"
# Does not match: "123e4567e89b12d3a456426614174000", "123e4567-e89b-12d3-a456-42661417400", "g23e4567-e89b-12d3-a456-426614174000"
```

[▲ Back to top](#-table-of-contents)

---

### `GUID`

Regex expression matching a GUID.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `UUID`; the separate name states the intended role.

**Example usage:**
```python
GUID
# Matches: "123e4567-e89b-12d3-a456-426614174000", "00000000-0000-0000-0000-000000000000"
# Does not match: "123e4567e89b12d3a456426614174000", "123e4567-e89b-12d3-a456-42661417400", "g23e4567-e89b-12d3-a456-426614174000"
```

[▲ Back to top](#-table-of-contents)

---

### `HEX_COLOR`

Regex expression matching a CSS hex color.

**Init Params:**
*(no parameters)*

**Pattern:**
`#` followed by 6 or 3 hex digits.

```regex
\#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})
```

**Example usage:**
```python
HEX_COLOR
# Matches: "#fff", "#1A2B3C"
# Does not match: "#ffff", "fff", "#ggg"
```

[▲ Back to top](#-table-of-contents)

---

### `VERSION`

Regex expression matching a dotted version number.

**Init Params:**
*(no parameters)*

**Pattern:**
An `INTEGER` followed by one or more (dot, `INTEGER`) pairs.

```regex
[0-9]+(?:\.[0-9]+)+
```

**Example usage:**
```python
VERSION
# Matches: "1.2", "10.0.3", "2026.9.30"
# Does not match: "1", "1.", "v1.2", "1.a"
```

[▲ Back to top](#-table-of-contents)

---

### `MAC_ADDRESS`

Regex expression matching a MAC address.

**Init Params:**
*(no parameters)*

**Pattern:**
Six pairs of hex digits separated by colons.

```regex
[0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5}
```

**Example usage:**
```python
MAC_ADDRESS
# Matches: "00:1A:2B:3C:4D:5E", "ff:ff:ff:ff:ff:ff"
# Does not match: "00-1A-2B-3C-4D-5E", "00:1A:2B:3C:4D", "00:1A:2B:3C:4D:5G"
```

[▲ Back to top](#-table-of-contents)

---

### `IPV4_ADDRESS`

Regex expression matching an IPv4 address.

**Init Params:**
*(no parameters)*

**Pattern:**
Four numbers `0`–`255` without leading zeros, separated by dots.

```regex
(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3}
```

**Example usage:**
```python
IPV4_ADDRESS
# Matches: "192.168.0.1", "0.0.0.0", "255.255.255.255"
# Does not match: "256.1.1.1", "1.2.3", "01.2.3.4", "1.2.3.4.5"
```

[▲ Back to top](#-table-of-contents)

---

### `ISBN10`

Regex expression matching an ISBN-10 without hyphens.

**Init Params:**
*(no parameters)*

**Pattern:**
Nine digits followed by a digit or `X`.

```regex
[0-9]{9}[0-9Xx]
```

**Notes:**

The check digit is not verified (a regex cannot compute it).

**Example usage:**
```python
ISBN10
# Matches: "0306406152", "080442957X"
# Does not match: "030640615", "03064061523", "0306-406152"
```

[▲ Back to top](#-table-of-contents)

---

### `ISBN13`

Regex expression matching an ISBN-13 without hyphens.

**Init Params:**
*(no parameters)*

**Pattern:**
`978` or `979` followed by ten digits.

```regex
97[89][0-9]{10}
```

**Notes:**

The check digit is not verified.

**Example usage:**
```python
ISBN13
# Matches: "9780306406157", "9791234567896"
# Does not match: "9770306406157", "978030640615", "978-0306406157"
```

[▲ Back to top](#-table-of-contents)

---

### `ISSN`

Regex expression matching an ISSN.

**Init Params:**
*(no parameters)*

**Pattern:**
`NNNN-NNNX`: four digits, a hyphen, three digits and a digit or `X`.

```regex
[0-9]{4}\-[0-9]{3}[0-9Xx]
```

**Notes:**

The check digit is not verified.

**Example usage:**
```python
ISSN
# Matches: "0317-8471", "2434-561X"
# Does not match: "03178471", "0317-847", "0317-84711"
```

[▲ Back to top](#-table-of-contents)

---

### `BASE64_CHARACTER`

Regex expression matching a character of the standard Base64 alphabet.

**Init Params:**
*(no parameters)*

**Pattern:**
`A`–`Z`, `a`–`z`, `0`–`9`, `+` or `/`.

```regex
[A-Za-z0-9+/]
```

**Example usage:**
```python
BASE64_CHARACTER
# Matches: "A", "z", "5", "+"
# Does not match: "-", "_", "="
```

[▲ Back to top](#-table-of-contents)

---

### `BASE64_URL_CHARACTER`

Regex expression matching a character of the URL-safe Base64 alphabet.

**Init Params:**
*(no parameters)*

**Pattern:**
`A`–`Z`, `a`–`z`, `0`–`9`, `-` or `_`.

```regex
[A-Za-z0-9\-_]
```

**Example usage:**
```python
BASE64_URL_CHARACTER
# Matches: "A", "z", "5", "-"
# Does not match: "+", "/", "="
```

[▲ Back to top](#-table-of-contents)

---

### `HEX_STRING`

Regex expression matching a string of hexadecimal digits.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more hex digits.

```regex
[0-9a-fA-F]+
```

**Example usage:**
```python
HEX_STRING
# Matches: "deadBEEF", "00", "1f"
# Does not match: "xyz", "", "0x1f"
```

[▲ Back to top](#-table-of-contents)

---

### `MD5`

Regex expression matching an MD5 digest in hex.

**Init Params:**
*(no parameters)*

**Pattern:**
Exactly 32 hex digits.

```regex
[0-9a-fA-F]{32}
```

**Example usage:**
```python
MD5
# Matches: "d41d8cd98f00b204e9800998ecf8427e"
# Does not match: "d41d8cd98f00b204e9800998ecf8427", "d41d8cd98f00b204e9800998ecf8427g"
```

[▲ Back to top](#-table-of-contents)

---

### `SHA1`

Regex expression matching a SHA-1 digest in hex.

**Init Params:**
*(no parameters)*

**Pattern:**
Exactly 40 hex digits.

```regex
[0-9a-fA-F]{40}
```

**Example usage:**
```python
SHA1
# Matches: "da39a3ee5e6b4b0d3255bfef95601890afd80709"
# Does not match: "da39a3ee5e6b4b0d3255bfef95601890afd8070"
```

[▲ Back to top](#-table-of-contents)

---

### `SHA256`

Regex expression matching a SHA-256 digest in hex.

**Init Params:**
*(no parameters)*

**Pattern:**
Exactly 64 hex digits.

```regex
[0-9a-fA-F]{64}
```

**Example usage:**
```python
SHA256
# Matches: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
# Does not match: "e3b0c44298fc1c14"
```

[▲ Back to top](#-table-of-contents)

---

### `RGB_COLOR`

Regex expression matching a CSS rgb() color.

**Init Params:**
*(no parameters)*

**Pattern:**
`rgb(` followed by three 0–255 components separated by commas (optional spaces), then `)`.

```regex
rgb\((?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:,\ *(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){2}\)
```

**Example usage:**
```python
RGB_COLOR
# Matches: "rgb(255, 0, 0)", "rgb(0,0,0)"
# Does not match: "rgb(256,0,0)", "rgb(1,2)", "rgba(0,0,0,1)"
```

[▲ Back to top](#-table-of-contents)

---

### `RGBA_COLOR`

Regex expression matching a CSS rgba() color.

**Init Params:**
*(no parameters)*

**Pattern:**
`rgba(` followed by three 0–255 components and an alpha value from 0 to 1, then `)`.

```regex
rgba\((?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:,\ *(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){2},\ *(?:0(?:\.[0-9]+)?|1(?:\.0+)?|\.[0-9]+)\)
```

**Example usage:**
```python
RGBA_COLOR
# Matches: "rgba(255, 0, 0, 0.5)", "rgba(0,0,0,1)", "rgba(0,0,0,.25)"
# Does not match: "rgba(0,0,0)", "rgba(0,0,0,2)", "rgba(0,0,0,1.5)"
```

[▲ Back to top](#-table-of-contents)

---

### `ISBN`

Regex expression matching an ISBN-10 or ISBN-13.

**Init Params:**
*(no parameters)*

**Pattern:**
`ISBN13` or `ISBN10`.

```regex
97[89][0-9]{10}|[0-9]{9}[0-9Xx]
```

**Example usage:**
```python
ISBN
# Matches: "9780306406157", "0306406152"
# Does not match: "12345", ""
```

[▲ Back to top](#-table-of-contents)

---

### `HASH`

Regex expression matching a common hash digest in hex.

**Init Params:**
*(no parameters)*

**Pattern:**
A `SHA256`, `SHA1` or `MD5` digest (64, 40 or 32 hex digits).

```regex
[0-9a-fA-F]{64}|[0-9a-fA-F]{40}|[0-9a-fA-F]{32}
```

**Example usage:**
```python
HASH
# Matches: "d41d8cd98f00b204e9800998ecf8427e", "da39a3ee5e6b4b0d3255bfef95601890afd80709"
# Does not match: "abc", "d41d8cd98f00b204e9800998ecf8427"
```

[▲ Back to top](#-table-of-contents)

---

### `SEMVER`

Regex expression matching a semantic version (SemVer 2.0).

**Init Params:**
*(no parameters)*

**Pattern:**
`MAJOR.MINOR.PATCH` without leading zeros, optionally followed by `-prerelease` and `+build` parts.

```regex
(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)(?:\-[a-zA-Z0-9\-]+(?:\.[a-zA-Z0-9\-]+)*)?(?:\+[a-zA-Z0-9\-]+(?:\.[a-zA-Z0-9\-]+)*)?
```

**Example usage:**
```python
SEMVER
# Matches: "1.2.3", "1.0.0-alpha.1", "1.0.0+build.5", "2.1.0-rc.1+sha.ab12"
# Does not match: "1.2", "01.2.3", "1.2.3.4", "v1.2.3"
```

[▲ Back to top](#-table-of-contents)

---

### `IPV6_ADDRESS`

Regex expression matching an IPv6 address.

**Init Params:**
*(no parameters)*

**Pattern:**
Eight groups of 1–4 hex digits separated by colons, with one run of zero groups optionally compressed to `::`.

**Notes:**

Embedded IPv4 tails (::ffff:192.0.2.1) and zone ids (fe80::1%eth0) are not covered.

**Example usage:**
```python
IPV6_ADDRESS
# Matches: "2001:db8::ff00:42:8329", "::1", "::", "fe80::1"
# Does not match: "1:2:3:4:5:6:7", "1::2::3", "12345::1", "g::1"
```

[▲ Back to top](#-table-of-contents)

---

### `CREDIT_CARD_NUMBER`

Regex expression matching a credit card number without separators.

**Init Params:**
*(no parameters)*

**Pattern:**
13 to 19 digits.

```regex
[0-9]{13,19}
```

**Notes:**

Only the length is checked — no brand prefix and no Luhn checksum.

**Example usage:**
```python
CREDIT_CARD_NUMBER
# Matches: "4111111111111111", "378282246310005"
# Does not match: "411111111111", "41111 1111 1111 1111", "41111111111111111111"
```

[▲ Back to top](#-table-of-contents)

---

### `IBAN`

Regex expression matching an IBAN without spaces.

**Init Params:**
*(no parameters)*

**Pattern:**
Two letters (country), two check digits and 11–30 uppercase letters or digits.

```regex
[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}
```

**Notes:**

Country-specific lengths and the mod-97 checksum are not verified.

**Example usage:**
```python
IBAN
# Matches: "CZ6508000000192000145399", "GB82WEST12345698765432"
# Does not match: "cz6508000000192000145399", "CZ65", "CZ65 0800 0000 1920 0014 5399"
```

[▲ Back to top](#-table-of-contents)

---

### `BASE64`

Regex expression matching a padded Base64 string.

**Init Params:**
*(no parameters)*

**Pattern:**
Groups of four Base64 characters, optionally ended by a padded tail (`xx==` or `xxx=`).

```regex
(?:[A-Za-z0-9+/]{4})+(?:[A-Za-z0-9+/]{2}={2}|[A-Za-z0-9+/]{3}=)?|[A-Za-z0-9+/]{2}={2}|[A-Za-z0-9+/]{3}=
```

**Example usage:**
```python
BASE64
# Matches: "aGVsbG8=", "aGVsbG8gd29ybGQ=", "QUJD", "YQ=="
# Does not match: "aGVsbG8", "a", "not base64!", ""
```

[▲ Back to top](#-table-of-contents)

---

### `BASE64_URL`

Regex expression matching a URL-safe Base64 string.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more URL-safe Base64 characters followed by up to two `=` paddings.

```regex
[A-Za-z0-9\-_]+={0,2}
```

**Notes:**

Padding is optional and its count is not checked against the length.

**Example usage:**
```python
BASE64_URL
# Matches: "aGVsbG8", "a-b_c", "aGVsbG8="
# Does not match: "a+b", "a/b", ""
```

[▲ Back to top](#-table-of-contents)

---

### `ULID`

Regex expression matching a ULID.

**Init Params:**
*(no parameters)*

**Pattern:**
26 characters of Crockford Base32 (no `I`, `L`, `O`, `U`); the first one is `0`–`7`.

```regex
[0-7][0-9A-HJKMNP-TV-Z]{25}
```

**Example usage:**
```python
ULID
# Matches: "01ARZ3NDEKTSV4RRFFQ69G5FAV", "7ZZZZZZZZZZZZZZZZZZZZZZZZZ"
# Does not match: "81ARZ3NDEKTSV4RRFFQ69G5FAV", "01ARZ3NDEKTSV4RRFFQ69G5FAI", "01arz3ndektsv4rrffq69g5fav", "01ARZ3NDEKTSV4RRFFQ69G5FA"
```

[▲ Back to top](#-table-of-contents)

---

### `JWT`

Regex expression matching a JSON Web Token.

**Init Params:**
*(no parameters)*

**Pattern:**
Three Base64URL segments separated by dots (`header.payload.signature`).

```regex
[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+
```

**Notes:**

Only the shape is checked; the segments are not decoded or verified.

**Example usage:**
```python
JWT
# Matches: "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"
# Does not match: "a.b", "a.b.c.d", "abc"
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](../README.md#-formats--27-terms)
