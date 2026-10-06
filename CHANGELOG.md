# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [0.1.0] - 2026-10-01

### ✨ Added

#### Vocabulary

* **324 ready-made regex expressions** available through `simplibs-patterns`:
  * **283 domain-specific patterns** defined directly by this library, covering 12 domains:
    * `characters` — digits, letters, whitespace, punctuation, symbols, signs and the generic escape sequence.
    * `text` — words, lines, quoted and bracketed text, character-class texts, `WHOLE_WORD`, `TEXT_BETWEEN`, `TEXT_UNTIL`, `TEXT_AFTER`, `TEXT_BEFORE`.
    * `numbers` — integers, decimals, signs, bases, scientific notation, fractions, percentages, fixed-digit numbers, bounded ranges (`0–255`, `0–65535`), months, days, hours, minutes, seconds, latitude and longitude.
    * `identifiers` — plain and dotted identifiers, language-neutral role names, markup tag names, prefix/suffix helpers.
    * `dates` — date components, English month and weekday names, ISO, European, US, ordinal and week dates.
    * `times` — time components, AM/PM, time zones, ISO, 12-hour and 24-hour times, date-times and timestamps.
    * `structured` — `DELIMITED_BY`, `LIST_OF`, `SEQUENCE_OF`, `PAIR_OF`, `WRAPPED_BY`, key=value pairs and separated lists.
    * `formats` — UUID, colors, versions, SemVer, MAC / IPv4 / IPv6 addresses, ISBN, ISSN, IBAN, card numbers, Base64, hashes, ULID, JWT.
    * `addresses` — IP, email, phone numbers, postal codes, ZIP codes, street addresses, P.O. boxes.
    * `communication` — user names, handles, hashtags, display names, message ids, email headers.
    * `web` — URLs and their components, domains and hosts, query strings, HTTP methods, status codes, headers, versions and cookies.
    * `programming` — language-dependent `COMMENT`, `STRING_LITERAL`, `BOOLEAN_LITERAL`, `NULL_LITERAL`, `KEYWORD` and `IMPORT`, selected by the `Language` enum (`PYTHON`, `JAVASCRIPT`), plus `OPERATOR` and `NUMBER_LITERAL`.
  * **41 foundational presets propagated from `simplibs-regex`**, providing reusable building blocks for anchors, character classes, groups, literals, lookarounds and quantifiers. These presets remain fully implemented in `simplibs-regex` and are exposed here as part of the unified vocabulary.

* Each domain is sorted into `pure/` (named concepts), `composed/` (combinations of other terms and parametrized factories) and `custom/` (terms that needed a semantic decision).
* Every term has a hover-friendly docstring with **Init Params**, **Pattern**, optional **Notes** and an **Example** showing text that does and does not match.
* Domain and root `__init__.py` files with a `_DESIGN_NOTES` registry table; the whole vocabulary is importable from `simplibs.patterns`.

#### Documentation

* A main `README.md` and one detailed reference per domain (`README_PATTERNS_<DOMAIN>.md`) with a table of contents and one identical card per term.

### 📋 Improved

* **ASCII by default**: numeric and format terms are built on `DECIMAL_DIGIT` (`0`–`9`) instead of the Unicode-aware `DIGIT`, so digits of other scripts never validate as years, ports or IP octets. `UNICODE_LETTER` is provided for human text.
* **Exact ranges**: month, day, hour, minute, second, day of year, week number, port, `0–255`, latitude and longitude are exact and were verified against every value in their range.
* **Verified formats**: `IPV4_ADDRESS` and `IPV6_ADDRESS` were verified against Python's `ipaddress` module.

### ⚠️ Known Limitations

* Check digits (ISBN, ISSN, IBAN, credit cards) and calendar validity (31 February) cannot be verified by a regular expression; each docstring states what is and is not checked.
* Names of months and weekdays are English and case-sensitive.
* Quoted and bracketed text is not nested and has no escape handling; quoted CSV fields are not supported.
* Locale-specific formats (postal codes, phone numbers, street addresses) are lenient generic heuristics.
* Language-dependent terms support `PYTHON` and `JAVASCRIPT` only; block comments, triple-quoted strings and f-strings are not covered yet.

### 🔗 Dependencies

* `simplibs-regex` — the expression tree these definitions are built from.

---

## Legend

* 🔄 **Changed** — modifications to existing functionality
* ✨ **Added** — new features and components
* 🐛 **Fixed** — bug fixes
* 📋 **Improved** — enhancements to existing features
* ⚠️ **Deprecated** — deprecated functionality (not used yet in this project)
* 🗑️ **Removed** — removed functionality (not used yet in this project)
