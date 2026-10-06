# 📚 `simplibs-patterns`

**A ready-made vocabulary of regular expressions — dates, numbers, URLs, identifiers, formats and more — built on `simplibs-regex`.**

`simplibs-regex` provides the **logic**: the containers and atomic elements from which regular expressions are constructed. `simplibs-patterns` provides the **vocabulary**: named, documented patterns built on top of that logic.

The library currently contains **324 domain-specific patterns of its own**, covering areas such as dates, numbers, URLs, identifiers and formats. It also **propagates 41 foundational presets from `simplibs-regex`**, making the complete preset vocabulary available through this library as well.

```python
from simplibs.patterns.dates import ISO_DATE
from simplibs.regex.compiler import RegexPattern

pattern = RegexPattern(ISO_DATE)
pattern.search("Released on 2026-09-30.").group()   # -> "2026-09-30"
```

> `simplibs-patterns` contains no regex construction logic of its own. Its domain patterns are definitions built on `simplibs-regex`, while the foundational regex presets defined by `simplibs-regex` are propagated here as a convenient unified vocabulary.

---

## 🧩 Propagated Regex Presets

`simplibs-patterns` also exposes the foundational presets defined directly by `simplibs-regex`.

These presets are **not reimplemented or wrapped** by `simplibs-patterns`. Their functional logic remains entirely in `simplibs-regex`; this library simply propagates them so that users working with `patterns` can access the complete preset vocabulary from one place.

The propagated presets cover 41 basic building blocks from which the higher-level patterns are constructed:

* **anchors**: `ALPHANUMERIC`, `HEX_DIGIT`, `LETTER`, `LOWERCASE_LETTER`, `UPPERCASE_LETTER`
* **any_character**: `ANY`
* **character_classes**: `DIGIT`, `NON_DIGIT`, `NON_WHITESPACE`, `NON_WORD_CHARACTER`, `WHITESPACE`, `WORD_CHARACTER`
* **groups**: `ATOMIC_GROUP`, `CASE_INSENSITIVE`, `NAMED_GROUP`, `NON_CAPTURING`, `VERBOSE_GROUP`, `WITH_FLAGS`
* **literals**: `BACKSLASH`, `BELL`, `CARRIAGE_RETURN`, `FORM_FEED`, `NEWLINE`, `TAB`, `VERTICAL_TAB`
* **lookaround**: `LOOKAHEAD`, `LOOKBEHIND`, `NEGATIVE_LOOKAHEAD`, `NEGATIVE_LOOKBEHIND`
* **quantifiers**: `AT_LEAST`, `BETWEEN`, `EXACTLY`, `ONE_OR_MORE`, `OPTIONAL`, `ZERO_OR_MORE`

➡️ [README_REGEX_PRESETS](https://github.com/simplibs/simplibs-patterns/blob/main/docs/README_REGEX_PRESETS.md) — detailed reference for all propagated `simplibs-regex` presets.

---

## 🧭 The Core Philosophy

One term, one file, one docstring. Every term defined by `simplibs-patterns` is its own small file, so hovering over a name in your editor shows what it matches, which parameters it takes, the equivalent regex and examples of text that does and does not match. The folder structure doubles as a map of the vocabulary.

The patterns are **composable**. Instead of one flat list of hundreds of special cases, small terms are combined by the factories in `structured`:

```python
from simplibs.patterns.numbers import INTEGER
from simplibs.patterns.structured import LIST_OF, PAIR_OF
from simplibs.patterns.identifiers import IDENTIFIER

ids = RegexPattern(LIST_OF(INTEGER))
ids.fullmatch("1,22,333")                 # -> a re.Match object

setting = RegexPattern(PAIR_OF(IDENTIFIER, INTEGER))
setting.fullmatch("retries=3")            # -> a re.Match object
```

Language-dependent constructs take the language as a **parameter** rather than a new word per language:

```python
from simplibs.patterns.programming import COMMENT, Language

COMMENT(Language.PYTHON)       # `#` to end of line
COMMENT(Language.JAVASCRIPT)   # `//` to end of line
```

---

## 📦 Installation

```bash
pip install simplibs-patterns
```

---

## 🛠️ Architecture & Package Structure

```text
src/simplibs/patterns/
├── characters     ◄── Single characters and character classes
├── text           ◄── Runs of text
├── numbers        ◄── Numbers in text
├── identifiers    ◄── Names and identifiers
├── dates          ◄── Calendar dates and their components
├── times          ◄── Times of day and moments in time
├── structured     ◄── Building blocks for structured text
├── formats        ◄── Well-known text formats
├── addresses      ◄── Addresses of people and machines
├── communication  ◄── Communication artefacts
├── web            ◄── The web
├── programming    ◄── Source-code constructs that depend on the language
```

Inside every domain the terms are sorted into three folders:

| Folder      | What goes there                                                           | Examples                                                              |
|:------------|:--------------------------------------------------------------------------|:----------------------------------------------------------------------|
| `pure/`     | A named concept with a standalone definition.                             | `INTEGER`, `UUID`, `ISO_DATE`, `IDENTIFIER`                           |
| `composed/` | An explicit combination of other terms, or a parametrized factory.        | `SIGNED_INTEGER`, `DATE_TIME`, `IP_ADDRESS`, `LIST_OF(item)`          |
| `custom/`   | Needed a semantic decision (ranges, locales, languages) — read its notes. | `PORT_NUMBER`, `EMAIL_ADDRESS`, `STREET_ADDRESS`, `COMMENT(language)` |

File names are UPPERCASE and identical to the term they define: `numbers/pure/INTEGER.py` defines `INTEGER`.

---

## ⚠️ Good to know

* **ASCII by default.** Numeric and format terms use `DECIMAL_DIGIT` (`0`–`9`), not the Unicode-aware `DIGIT` (`\d`). Use `UNICODE_LETTER` / `WORD_CHARACTER` for human text.
* **`WORD` is a whole word** (`text.WORD`, one or more word characters). `simplibs.regex` has its own `WORD` which is a *single* `\w`; here that is `WORD_CHARACTER`.
* **Shape, not truth.** A regex cannot verify check digits (ISBN, IBAN, credit cards) or that 31 February does not exist. Each docstring says what is and is not checked.
* **Case-sensitive.** Names such as `January` or `GET` match exactly; use the `IGNORECASE` flag in `RegexPattern` to relax it.

---

## 📖 Quick Reference

The **308 terms below are defined by `simplibs-patterns` itself**. The 41 foundational presets inherited from `simplibs-regex` are listed separately above.

---

### 🔡 `characters` — 37 terms

Single characters and character classes — digits, letters, whitespace, punctuation, symbols and the escape syntax. Every other domain is built on these.

* **pure**: `DECIMAL_DIGIT`, `NON_ZERO_DIGIT`, `BINARY_DIGIT`, `OCTAL_DIGIT`, `SPACE`, `PLUS_SIGN`, `MINUS_SIGN`, `DASH`, `DOT`, `COMMA`, `COLON`, `SEMICOLON`, `SLASH`, `SINGLE_QUOTE`, `DOUBLE_QUOTE`, `UNDERSCORE`, `AT_SIGN`, `HASH_SIGN`, `DOLLAR`, `PERCENT`, `AMPERSAND`, `ASTERISK`, `EQUALS`, `PIPE`, `CARET`, `TILDE`, `QUESTION_MARK`, `PARENTHESIS`, `BRACKET`, `BRACE`, `PUNCTUATION`, `SYMBOL`, `UNICODE_LETTER`
* **composed**: `SIGN`, `QUOTE`, `SPECIAL_CHARACTER`
* **custom**: `ESCAPED_CHARACTER`

➡️ [README_PATTERNS_CHARACTERS](https://github.com/simplibs/simplibs-patterns/blob/main/docs/README_PATTERNS_CHARACTERS.md)

---

### 📝 `text` — 38 terms

Runs of text — words, lines, quoted and bracketed text, character-class texts, and parametrized helpers such as `WHOLE_WORD`, `TEXT_BETWEEN` or `TEXT_UNTIL`.

* **pure**: `EMPTY_TEXT`, `NON_EMPTY_TEXT`, `CHARACTER`, `CHARACTERS`, `WORD`, `SINGLE_WORD`, `LINE`, `SINGLE_LINE`, `WHITESPACE_TEXT`, `NON_WHITESPACE_TEXT`, `ALPHANUMERIC_TEXT`, `ALPHA_TEXT`, `DIGIT_TEXT`, `LOWERCASE_TEXT`, `UPPERCASE_TEXT`, `IDENTIFIER_LIKE_TEXT`, `SINGLE_QUOTED_TEXT`, `DOUBLE_QUOTED_TEXT`, `PARENTHESIZED_TEXT`, `BRACKETED_TEXT`, `BRACED_TEXT`
* **composed**: `QUOTED_TEXT`, `WORDS`, `SPACE_SEPARATED_WORDS`, `WORD_LIST`, `COMMA_SEPARATED_TEXT`, `MULTILINE_TEXT`, `WHOLE_WORD`, `TEXT_BETWEEN`, `PREFIXED_TEXT`, `SUFFIXED_TEXT`, `TEXT_OF_LENGTH`, `TEXT_OF_LENGTH_RANGE`
* **custom**: `MIXED_CASE_TEXT`, `CSV_LINE`, `TEXT_UNTIL`, `TEXT_AFTER`, `TEXT_BEFORE`

➡️ [README_PATTERNS_TEXT](https://github.com/simplibs/simplibs-patterns/blob/main/docs/README_PATTERNS_TEXT.md)

---

### 🔢 `numbers` — 42 terms

Numbers in text — integers, decimals, signs, bases, scientific notation, fixed-digit numbers, bounded ranges, and the number shapes used by dates, times, ports and coordinates.

* **pure**: `INTEGER`, `DECIMAL`, `INTEGER_PART`, `FRACTIONAL_PART`, `DECIMAL_SEPARATOR`, `ZERO_TO_NINE`, `BINARY`, `OCTAL`, `HEX`, `EXPONENT`, `FRACTION`
* **composed**: `NUMBER`, `SIGNED`, `SIGNED_INTEGER`, `SIGNED_NUMBER`, `NON_NEGATIVE`, `NON_POSITIVE`, `NON_ZERO`, `EXPONENT_PART`, `SCIENTIFIC`, `RATIONAL_NUMBER`, `PERCENTAGE`, `PERMILLE`, `DIGIT_NUMBER`, `ONE_DIGIT_NUMBER`, `TWO_DIGIT_NUMBER`, `THREE_DIGIT_NUMBER`, `FOUR_DIGIT_NUMBER`
* **custom**: `ZERO`, `POSITIVE`, `NEGATIVE`, `ZERO_TO_NINETY_NINE`, `ZERO_TO_TWO_HUNDRED_FIFTY_FIVE`, `PORT_NUMBER`, `YEAR_NUMBER`, `MONTH_NUMBER`, `DAY_NUMBER`, `HOUR_NUMBER`, `MINUTE_NUMBER`, `SECOND_NUMBER`, `LATITUDE`, `LONGITUDE`

➡️ [README_PATTERNS_NUMBERS](https://github.com/simplibs/simplibs-patterns/blob/main/docs/README_PATTERNS_NUMBERS.md)

---

### 🏷️ `identifiers` — 31 terms

Names and identifiers — plain and dotted identifiers, role-specific names (variable, class, module…), markup tag names, and prefix/suffix helpers.

* **pure**: `IDENTIFIER_START_CHARACTER`, `IDENTIFIER_CHARACTER`, `IDENTIFIER`, `SIMPLE_IDENTIFIER`, `NAME`, `QUALIFIED_IDENTIFIER`, `QUALIFIED_NAME`, `NAMESPACE`, `NAMESPACE_NAME`, `VARIABLE_NAME`, `CONSTANT_NAME`, `FUNCTION_NAME`, `METHOD_NAME`, `CLASS_NAME`, `TYPE_NAME`, `MODULE_NAME`, `PACKAGE_NAME`, `ATTRIBUTE_NAME`, `PROPERTY_NAME`, `PARAMETER_NAME`, `ARGUMENT_NAME`, `ENUM_NAME`, `ENUM_MEMBER_NAME`, `KEY`, `VALUE_NAME`, `LABEL`
* **composed**: `QUALIFIED_IDENTIFIER_OF`, `IDENTIFIER_WITH_PREFIX`, `IDENTIFIER_WITH_SUFFIX`
* **custom**: `TAG_NAME`, `ELEMENT_NAME`

➡️ [README_PATTERNS_IDENTIFIERS](https://github.com/simplibs/simplibs-patterns/blob/main/docs/README_PATTERNS_IDENTIFIERS.md)

---

### 📅 `dates` — 20 terms

Calendar dates and their components — year, month, day, week, weekday names, quarter, and the ISO, European, US, ordinal and week date layouts.

* **pure**: `YEAR`, `MONTH`, `DAY`, `DAY_OF_MONTH`, `WEEKDAY`, `QUARTER`, `ISO_DATE`, `DATE`, `CALENDAR_DATE`, `EUROPEAN_DATE`, `US_DATE`, `ORDINAL_DATE`, `WEEK_DATE`
* **composed**: `DATE_WITH_SEPARATOR`
* **custom**: `DAY_OF_YEAR`, `WEEK_NUMBER`, `MONTH_NAME`, `MONTH_ABBREVIATION`, `WEEKDAY_NAME`, `WEEKDAY_ABBREVIATION`

➡️ [README_PATTERNS_DATES](https://github.com/simplibs/simplibs-patterns/blob/main/docs/README_PATTERNS_DATES.md)

---

### 🕒 `times` — 26 terms

Times of day and moments in time — hours, minutes, seconds, fractions, AM/PM, time zones, ISO and 12/24-hour times, date-times and timestamps.

* **pure**: `HOUR`, `MINUTE`, `SECOND`, `HOUR_12`, `AM`, `PM`, `TIME`, `TIME_WITH_COLONS`, `TWENTY_FOUR_HOUR_TIME`, `COMPACT_TIME`, `TIME_WITHOUT_COLONS`
* **composed**: `MILLISECOND`, `MICROSECOND`, `MERIDIEM`, `TIMEZONE_OFFSET`, `UTC_OFFSET`, `TIMEZONE`, `TIME_WITH_SECONDS`, `TIME_WITH_FRACTION`, `ISO_TIME`, `TWELVE_HOUR_TIME`, `TIMEZONE_TIME`, `UTC_TIME`, `DATE_TIME`
* **custom**: `TIMESTAMP`, `UNIX_TIMESTAMP`

➡️ [README_PATTERNS_TIMES](https://github.com/simplibs/simplibs-patterns/blob/main/docs/README_PATTERNS_TIMES.md)

---

### 🧱 `structured` — 15 terms

Building blocks for structured text — lists, pairs, delimited and wrapped items — mostly as parametrized factories that take other expressions as arguments.

* **pure**: `OPENING_DELIMITER`, `CLOSING_DELIMITER`
* **composed**: `DELIMITED_BY`, `LIST_OF`, `SEQUENCE_OF`, `PAIR_OF`, `WRAPPED_BY`, `KEY_VALUE_PAIR`, `KEY_VALUE`
* **custom**: `SEPARATOR`, `DELIMITER`, `COMMA_SEPARATED_LIST`, `SEMICOLON_SEPARATED_LIST`, `SPACE_SEPARATED_LIST`, `TAB_SEPARATED_LIST`

➡️ [README_PATTERNS_STRUCTURED](https://github.com/simplibs/simplibs-patterns/blob/main/docs/README_PATTERNS_STRUCTURED.md)

---

### 🧬 `formats` — 27 terms

Well-known text formats — UUID, colors, versions, MAC and IP addresses, ISBN/ISSN, card and bank numbers, Base64, hashes, ULID and JWT.

* **pure**: `UUID`, `GUID`, `HEX_COLOR`, `VERSION`, `MAC_ADDRESS`, `IPV4_ADDRESS`, `ISBN10`, `ISBN13`, `ISSN`, `BASE64_CHARACTER`, `BASE64_URL_CHARACTER`, `HEX_STRING`, `MD5`, `SHA1`, `SHA256`
* **composed**: `RGB_COLOR`, `RGBA_COLOR`, `ISBN`, `HASH`
* **custom**: `SEMVER`, `IPV6_ADDRESS`, `CREDIT_CARD_NUMBER`, `IBAN`, `BASE64`, `BASE64_URL`, `ULID`, `JWT`

➡️ [README_PATTERNS_FORMATS](https://github.com/simplibs/simplibs-patterns/blob/main/docs/README_PATTERNS_FORMATS.md)

---

### 📬 `addresses` — 9 terms

Addresses of people and machines — IP, email, phone numbers, postal codes, street addresses and P.O. boxes.

* **pure**: `EMAIL_LOCAL_PART`
* **composed**: `IP_ADDRESS`, `PO_BOX`
* **custom**: `EMAIL_ADDRESS`, `PHONE_NUMBER`, `INTERNATIONAL_PHONE_NUMBER`, `POSTAL_CODE`, `ZIP_CODE`, `STREET_ADDRESS`

➡️ [README_PATTERNS_ADDRESSES](https://github.com/simplibs/simplibs-patterns/blob/main/docs/README_PATTERNS_ADDRESSES.md)

---

### 💬 `communication` — 16 terms

Communication artefacts — email, user names and handles, hashtags, display names, message ids and email headers.

* **pure**: `EMAIL`, `USER_HANDLE`, `MENTION`, `SOCIAL_HANDLE`, `HASHTAG`, `SUBJECT`, `REPLY_ADDRESS`, `SENDER_ADDRESS`, `RECIPIENT_ADDRESS`, `EMAIL_HEADER_NAME`, `EMAIL_HEADER_VALUE`
* **composed**: `EMAIL_HEADER`, `EMAIL_SUBJECT`
* **custom**: `USERNAME`, `DISPLAY_NAME`, `MESSAGE_ID`

➡️ [README_PATTERNS_COMMUNICATION](https://github.com/simplibs/simplibs-patterns/blob/main/docs/README_PATTERNS_COMMUNICATION.md)

---

### 🌐 `web` — 38 terms

The web — URLs and their components, domains and hosts, query strings, HTTP methods/status/headers/versions and cookies.

* **pure**: `URL_SCHEME`, `URL_CHARACTER`, `URL_USERINFO`, `DOMAIN_LABEL`, `SUBDOMAIN`, `SECOND_LEVEL_DOMAIN`, `DOMAIN`, `DOMAIN_NAME`, `HOSTNAME`, `QUERY_PARAMETER`, `HTTP_METHOD`, `HTTP_STATUS_CODE`, `HTTP_VERSION`, `HTTP_HEADER_NAME`, `HTTP_HEADER_VALUE`, `COOKIE_VALUE`, `COOKIE_NAME`
* **composed**: `HOST`, `URL_HOST`, `URL_PORT`, `URL_PATH`, `FRAGMENT_IDENTIFIER`, `URL_FRAGMENT`, `URL_QUERY`, `URL_LOCATION`, `URL`, `HTTP_URL`, `HTTPS_URL`, `WEB_ADDRESS`, `WEB_RESOURCE`, `ENDPOINT`, `API_ENDPOINT`, `QUERY_STRING`, `HTTP_HEADER`, `COOKIE`
* **custom**: `TOP_LEVEL_DOMAIN`, `URI`, `URN`

➡️ [README_PATTERNS_WEB](https://github.com/simplibs/simplibs-patterns/blob/main/docs/README_PATTERNS_WEB.md)

---

### 💻 `programming` — 9 terms

Source-code constructs that depend on the language — comments, strings, keywords, imports, literals — selected with a `Language` enum, plus a few language-neutral terms.

* **pure**: `OPERATOR`
* **composed**: `NUMBER_LITERAL`
* **custom**: `COMMENT`, `STRING_LITERAL`, `BOOLEAN_LITERAL`, `NULL_LITERAL`, `KEYWORD`, `IMPORT`
* **enums**: `Language`

➡️ [README_PATTERNS_PROGRAMMING](https://github.com/simplibs/simplibs-patterns/blob/main/docs/README_PATTERNS_PROGRAMMING.md)

---

## 🧭 Design Status

The current structure and vocabulary are a **first design of the library**, intended to establish a coherent foundation rather than freeze the final shape of the API.

Real-world use will show which domains, terms, compositions and abstractions are genuinely useful and which should evolve. Some names, groupings or individual presets may therefore still change as the library is used and its vocabulary becomes clearer.

The goal is not to predict the final structure in advance, but to let the structure emerge from actual use while keeping the vocabulary coherent and composable.

---

## ☯️ About simplibs

All libraries in the **simplibs** (Simple Libraries) ecosystem share a common
engineering philosophy:

* **Dyslexia-friendly:**
  We actively minimize cognitive load. Code is atomized into small, self-contained units,
  files are named directly after the logical task they perform, and explanations describe
  *why* something is designed, not just *what* it is.
* **Programmer's Zen:**
  Nothing should be missing, and nothing should be superfluous. We value clean execution
  paths and robust, understandable code architectures over rushed, messy feature sets.
* **Defensive Style:**
  We actively anticipate edge cases and failure modes so that only safe operational paths
  remain. Our code is built to degrade gracefully rather than crash unexpectedly.
* **Minimalism:**
  Find the most direct path to the goal in as few operational steps as possible without
  taking shortcuts on safety, readability, or completeness.
* **Code as Craft:**
  Code should be pleasant to look at, readable at a glance, and evoke structural harmony.
  We treat software engineering as a precision trade.

---

### 🤝 Contributing & Community

This is an **open-source project** built with love and care. We strongly believe in
community collaboration and welcome any feedback, bug reports, or feature ideas!

* **Want to contribute?** Feel free to open an Issue or submit a Pull Request.
* **Want to get in touch?** If you'd like to discuss the project further, collaborate,
  or just say hello, feel free to open a GitHub Issue or start a Discussion.

---

### 📝 License

This library is released under the **MIT License**. Build great things!

---

[▲ Back to Top](#-simplibs-patterns)