# 🌐 `patterns/web` — Detailed Reference

The web — URLs and their components, domains and hosts, query strings, HTTP methods/status/headers/versions and cookies.

Every card below is the term's full docstring. Terms are grouped by how they are defined: **pure** (a named concept), **composed** (built from other terms, or a parametrized factory) and **custom** (needed a semantic decision — read its notes).

All expressions are `simplibs.regex` objects: combine them with `+` (sequence) and `|` (alternation), wrap them with the presets (`ONE_OR_MORE`, `NAMED_GROUP`, …) and compile with `RegexPattern`.

---

## 🧭 Table of Contents

**pure**:

- [`URL_SCHEME`](#url_scheme)
- [`URL_CHARACTER`](#url_character)
- [`URL_USERINFO`](#url_userinfo)
- [`DOMAIN_LABEL`](#domain_label)
- [`SUBDOMAIN`](#subdomain)
- [`SECOND_LEVEL_DOMAIN`](#second_level_domain)
- [`DOMAIN`](#domain)
- [`DOMAIN_NAME`](#domain_name)
- [`HOSTNAME`](#hostname)
- [`QUERY_PARAMETER`](#query_parameter)
- [`HTTP_METHOD`](#http_method)
- [`HTTP_STATUS_CODE`](#http_status_code)
- [`HTTP_VERSION`](#http_version)
- [`HTTP_HEADER_NAME`](#http_header_name)
- [`HTTP_HEADER_VALUE`](#http_header_value)
- [`COOKIE_VALUE`](#cookie_value)
- [`COOKIE_NAME`](#cookie_name)

**composed**:

- [`HOST`](#host)
- [`URL_HOST`](#url_host)
- [`URL_PORT`](#url_port)
- [`URL_PATH`](#url_path)
- [`FRAGMENT_IDENTIFIER`](#fragment_identifier)
- [`URL_FRAGMENT`](#url_fragment)
- [`URL_QUERY`](#url_query)
- [`URL_LOCATION`](#url_location)
- [`URL`](#url)
- [`HTTP_URL`](#http_url)
- [`HTTPS_URL`](#https_url)
- [`WEB_ADDRESS`](#web_address)
- [`WEB_RESOURCE`](#web_resource)
- [`ENDPOINT`](#endpoint)
- [`API_ENDPOINT`](#api_endpoint)
- [`QUERY_STRING`](#query_string)
- [`HTTP_HEADER`](#http_header)
- [`COOKIE`](#cookie)

**custom**:

- [`TOP_LEVEL_DOMAIN`](#top_level_domain)
- [`URI`](#uri)
- [`URN`](#urn)

---

### `URL_SCHEME`

Regex expression matching a URL scheme.

**Init Params:**
*(no parameters)*

**Pattern:**
A letter followed by letters, digits, `+`, `-` or `.`.

```regex
[a-zA-Z][a-zA-Z0-9+\-.]*
```

**Example usage:**
```python
URL_SCHEME
# Matches: "http", "git+ssh", "a1"
# Does not match: "1http", "-x", ""
```

[▲ Back to top](#-table-of-contents)

---

### `URL_CHARACTER`

Regex expression matching a character allowed in a URL path, query or fragment.

**Init Params:**
*(no parameters)*

**Pattern:**
Letters, digits and ``- . _ ~ % / : @ = ! $ & ' ( ) * + , ;``. Excludes `?`, `#` and whitespace.

```regex
[a-zA-Z0-9\-._~%/:@=!$&'()*+,;]
```

**Example usage:**
```python
URL_CHARACTER
# Matches: "a", "/", "%", "~"
# Does not match: "?", "#", " ", "ab"
```

[▲ Back to top](#-table-of-contents)

---

### `URL_USERINFO`

Regex expression matching the user information part of a URL.

**Init Params:**
*(no parameters)*

**Pattern:**
Word characters, `-`, `.`, `:`, `~` or `%`, e.g. `user` or `user:password`.

```regex
[\w\-.:~%]+
```

**Example usage:**
```python
URL_USERINFO
# Matches: "user", "user:pass"
# Does not match: "", "a@b", "a b"
```

[▲ Back to top](#-table-of-contents)

---

### `DOMAIN_LABEL`

Regex expression matching a single label of a domain name.

**Init Params:**
*(no parameters)*

**Pattern:**
1–63 letters, digits or hyphens; it may not start or end with a hyphen.

```regex
[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?
```

**Notes:**

ASCII (punycode) labels only.

**Example usage:**
```python
DOMAIN_LABEL
# Matches: "example", "a", "my-site", "a1"
# Does not match: "-a", "a-", "", "a_b"
```

[▲ Back to top](#-table-of-contents)

---

### `SUBDOMAIN`

Regex expression matching a subdomain label.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `DOMAIN_LABEL`; the separate name states the intended role.

**Example usage:**
```python
SUBDOMAIN
# Matches: "example", "a", "my-site", "a1"
# Does not match: "-a", "a-", "", "a_b"
```

[▲ Back to top](#-table-of-contents)

---

### `SECOND_LEVEL_DOMAIN`

Regex expression matching a second-level domain label.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `DOMAIN_LABEL`; the separate name states the intended role.

**Example usage:**
```python
SECOND_LEVEL_DOMAIN
# Matches: "example", "a", "my-site", "a1"
# Does not match: "-a", "a-", "", "a_b"
```

[▲ Back to top](#-table-of-contents)

---

### `DOMAIN`

Regex expression matching a domain name with at least two labels.

**Init Params:**
*(no parameters)*

**Pattern:**
A `DOMAIN_LABEL` followed by one or more (dot, `DOMAIN_LABEL`) pairs.

```regex
[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+
```

**Example usage:**
```python
DOMAIN
# Matches: "example.com", "sub.example.co.uk"
# Does not match: "localhost", "example.", "-a.com", ".com"
```

[▲ Back to top](#-table-of-contents)

---

### `DOMAIN_NAME`

Regex expression matching a domain name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `DOMAIN`; the separate name states the intended role.

**Example usage:**
```python
DOMAIN_NAME
# Matches: "example.com", "sub.example.co.uk"
# Does not match: "localhost", "example.", "-a.com", ".com"
```

[▲ Back to top](#-table-of-contents)

---

### `HOSTNAME`

Regex expression matching a host name of one or more labels.

**Init Params:**
*(no parameters)*

**Pattern:**
A `DOMAIN_LABEL` followed by any number of (dot, `DOMAIN_LABEL`) pairs.

```regex
[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*
```

**Example usage:**
```python
HOSTNAME
# Matches: "localhost", "example.com", "my-server.local"
# Does not match: "-a", "a..b", ""
```

[▲ Back to top](#-table-of-contents)

---

### `QUERY_PARAMETER`

Regex expression matching a single key=value query parameter.

**Init Params:**
*(no parameters)*

**Pattern:**
A key, `=` and a (possibly empty) value; neither contains `&` or `=`.

```regex
[\w\-.~%+]+=[\w\-.~%+,:@/]*
```

**Example usage:**
```python
QUERY_PARAMETER
# Matches: "page=2", "q=hello+world", "flag="
# Does not match: "=x", "a b=1", "a=b&c=d"
```

[▲ Back to top](#-table-of-contents)

---

### `HTTP_METHOD`

Regex expression matching an HTTP request method.

**Init Params:**
*(no parameters)*

**Pattern:**
One of `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`, `TRACE`, `CONNECT` (uppercase).

```regex
GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS|TRACE|CONNECT
```

**Example usage:**
```python
HTTP_METHOD
# Matches: "GET", "DELETE"
# Does not match: "get", "FETCH"
```

[▲ Back to top](#-table-of-contents)

---

### `HTTP_STATUS_CODE`

Regex expression matching an HTTP status code.

**Init Params:**
*(no parameters)*

**Pattern:**
Three digits from `100` to `599`.

```regex
[1-5][0-9]{2}
```

**Example usage:**
```python
HTTP_STATUS_CODE
# Matches: "200", "404", "503"
# Does not match: "99", "600", "20", "2000"
```

[▲ Back to top](#-table-of-contents)

---

### `HTTP_VERSION`

Regex expression matching an HTTP version.

**Init Params:**
*(no parameters)*

**Pattern:**
`HTTP/` followed by `d.d` (e.g. `1.1`) or `2` / `3`.

```regex
HTTP/(?:[0-9]\.[0-9]|[23])
```

**Example usage:**
```python
HTTP_VERSION
# Matches: "HTTP/1.1", "HTTP/2", "HTTP/3"
# Does not match: "HTTP/", "HTTP 1.1", "HTTP/1"
```

[▲ Back to top](#-table-of-contents)

---

### `HTTP_HEADER_NAME`

Regex expression matching an HTTP header field name.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more token characters (letters, digits and ``! # $ % & ' * + - . ^ _ ` | ~``).

```regex
[a-zA-Z0-9!#$%&'*+\-.\^_`|~]+
```

**Example usage:**
```python
HTTP_HEADER_NAME
# Matches: "Content-Type", "X-Request-ID", "Host"
# Does not match: "Content Type", "Name:", ""
```

[▲ Back to top](#-table-of-contents)

---

### `HTTP_HEADER_VALUE`

Regex expression matching an HTTP header field value.

**Init Params:**
*(no parameters)*

**Pattern:**
Printable ASCII characters and tabs; may be empty.

```regex
[\t -~]*
```

**Example usage:**
```python
HTTP_HEADER_VALUE
# Matches: "text/html; charset=utf-8", ""
# Does not match: "a\nb"
```

[▲ Back to top](#-table-of-contents)

---

### `COOKIE_VALUE`

Regex expression matching a cookie value.

**Init Params:**
*(no parameters)*

**Pattern:**
Word characters and ``- . ~ % + / = :``; may be empty.

```regex
[\w\-.~%+/=:]*
```

**Example usage:**
```python
COOKIE_VALUE
# Matches: "abc123", "a%20b", "dGVzdA==", ""
# Does not match: "a b", "a;b", "a,b"
```

[▲ Back to top](#-table-of-contents)

---

### `COOKIE_NAME`

Regex expression matching a cookie name.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `HTTP_HEADER_NAME`; the separate name states the intended role.

**Notes:**

Cookie names are RFC 6265 tokens — the same character set as header names.

**Example usage:**
```python
COOKIE_NAME
# Matches: "Content-Type", "X-Request-ID", "Host"
# Does not match: "Content Type", "Name:", ""
```

[▲ Back to top](#-table-of-contents)

---

### `HOST`

Regex expression matching a host: IPv4, IPv6 or host name.

**Init Params:**
*(no parameters)*

**Pattern:**
`IPV4_ADDRESS`, `IPV6_ADDRESS` or `HOSTNAME`.

**Example usage:**
```python
HOST
# Matches: "example.com", "localhost", "192.168.0.1", "::1"
# Does not match: "-x", "a..b", ""
```

[▲ Back to top](#-table-of-contents)

---

### `URL_HOST`

Regex expression matching the host part of a URL.

**Init Params:**
*(no parameters)*

**Pattern:**
`IPV4_ADDRESS`, an IPv6 address in square brackets, or a `HOSTNAME`.

**Example usage:**
```python
URL_HOST
# Matches: "example.com", "localhost", "192.168.0.1", "[::1]"
# Does not match: "::1", "[::1", "a..b"
```

[▲ Back to top](#-table-of-contents)

---

### `URL_PORT`

Regex expression matching the port part of a URL.

**Init Params:**
*(no parameters)*

**Pattern:**
A colon followed by a `PORT_NUMBER`.

```regex
:(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0)
```

**Example usage:**
```python
URL_PORT
# Matches: ":80", ":8080", ":65535"
# Does not match: "80", ":65536", ":"
```

[▲ Back to top](#-table-of-contents)

---

### `URL_PATH`

Regex expression matching the path part of a URL.

**Init Params:**
*(no parameters)*

**Pattern:**
A slash followed by any number of `URL_CHARACTER`s.

```regex
/[a-zA-Z0-9\-._~%/:@=!$&'()*+,;]*
```

**Example usage:**
```python
URL_PATH
# Matches: "/", "/a/b.html", "/path/to/file"
# Does not match: "a/b", "/a?b", "/a b"
```

[▲ Back to top](#-table-of-contents)

---

### `FRAGMENT_IDENTIFIER`

Regex expression matching the text after the # of a URL.

**Init Params:**
*(no parameters)*

**Pattern:**
Any number of `URL_CHARACTER`s or `?`.

```regex
(?:[a-zA-Z0-9\-._~%/:@=!$&'()*+,;]|\?)*
```

**Example usage:**
```python
FRAGMENT_IDENTIFIER
# Matches: "section-2", "top", ""
# Does not match: "a b", "#x"
```

[▲ Back to top](#-table-of-contents)

---

### `URL_FRAGMENT`

Regex expression matching the fragment part of a URL.

**Init Params:**
*(no parameters)*

**Pattern:**
`#` followed by a `FRAGMENT_IDENTIFIER`.

```regex
\#(?:[a-zA-Z0-9\-._~%/:@=!$&'()*+,;]|\?)*
```

**Example usage:**
```python
URL_FRAGMENT
# Matches: "#top", "#section-2", "#"
# Does not match: "top", "#a b"
```

[▲ Back to top](#-table-of-contents)

---

### `URL_QUERY`

Regex expression matching the query part of a URL.

**Init Params:**
*(no parameters)*

**Pattern:**
`?` followed by any number of `URL_CHARACTER`s.

```regex
\?(?:[a-zA-Z0-9\-._~%/:@=!$&'()*+,;]|\?)*
```

**Example usage:**
```python
URL_QUERY
# Matches: "?a=1&b=2", "?"
# Does not match: "a=1", "?a b", "?#x"
```

[▲ Back to top](#-table-of-contents)

---

### `URL_LOCATION`

Regex expression matching everything of a URL after the scheme and ://.

**Init Params:**
*(no parameters)*

**Pattern:**
1. An optional `URL_USERINFO` and `@`.
2. A `URL_HOST`.
3. An optional `URL_PORT`, `URL_PATH`, `URL_QUERY` and `URL_FRAGMENT`.

**Notes:**

Shared by `URL`, `HTTP_URL` and `HTTPS_URL`.

**Example usage:**
```python
URL_LOCATION
# Matches: "example.com", "user:pw@host:8080/a/b?x=1#top", "[::1]:8080/x"
# Does not match: "", "http://x", "exa mple.com"
```

[▲ Back to top](#-table-of-contents)

---

### `URL`

Regex expression matching a URL with a scheme and ://.

**Init Params:**
*(no parameters)*

**Pattern:**
A `URL_SCHEME`, `://` and a `URL_LOCATION`.

**Notes:**

URLs without `//` (mailto:, urn:) are `URI`s, not `URL`s.

**Example usage:**
```python
URL
# Matches: "https://example.com/path?q=1#frag", "ftp://files.example.org", "git+ssh://user@host:22/repo.git"
# Does not match: "example.com", "http:/example.com", "http://"
```

[▲ Back to top](#-table-of-contents)

---

### `HTTP_URL`

Regex expression matching an http:// URL.

**Init Params:**
*(no parameters)*

**Pattern:**
`http://` followed by a `URL_LOCATION`.

**Example usage:**
```python
HTTP_URL
# Matches: "http://example.com", "http://localhost:8080/a?b=1"
# Does not match: "https://example.com", "example.com"
```

[▲ Back to top](#-table-of-contents)

---

### `HTTPS_URL`

Regex expression matching an https:// URL.

**Init Params:**
*(no parameters)*

**Pattern:**
`https://` followed by a `URL_LOCATION`.

**Example usage:**
```python
HTTPS_URL
# Matches: "https://example.com", "https://example.com/a/b?c=d#e"
# Does not match: "http://example.com", "example.com"
```

[▲ Back to top](#-table-of-contents)

---

### `WEB_ADDRESS`

Regex expression matching a web address (http or https).

**Init Params:**
*(no parameters)*

**Pattern:**
`HTTPS_URL` or `HTTP_URL`.

**Example usage:**
```python
WEB_ADDRESS
# Matches: "https://example.com", "http://example.com/a"
# Does not match: "ftp://example.com", "example.com"
```

[▲ Back to top](#-table-of-contents)

---

### `WEB_RESOURCE`

Regex expression matching a web resource.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `URL`; the separate name states the intended role.

**Notes:**

Any scheme; for http(s) only use `WEB_ADDRESS`.

**Example usage:**
```python
WEB_RESOURCE
# Matches: "https://example.com/path?q=1#frag", "ftp://files.example.org", "git+ssh://user@host:22/repo.git"
# Does not match: "example.com", "http:/example.com", "http://"
```

[▲ Back to top](#-table-of-contents)

---

### `ENDPOINT`

Regex expression matching an endpoint path.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `URL_PATH`; the separate name states the intended role.

**Example usage:**
```python
ENDPOINT
# Matches: "/", "/a/b.html", "/path/to/file"
# Does not match: "a/b", "/a?b", "/a b"
```

[▲ Back to top](#-table-of-contents)

---

### `API_ENDPOINT`

Regex expression matching an API endpoint path.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `URL_PATH`; the separate name states the intended role.

**Example usage:**
```python
API_ENDPOINT
# Matches: "/", "/a/b.html", "/path/to/file"
# Does not match: "a/b", "/a?b", "/a b"
```

[▲ Back to top](#-table-of-contents)

---

### `QUERY_STRING`

Regex expression matching a query string made of key=value parameters.

**Init Params:**
*(no parameters)*

**Pattern:**
`?` followed by `QUERY_PARAMETER`s separated by `&`.

```regex
\?[\w\-.~%+]+=[\w\-.~%+,:@/]*(?:\&[\w\-.~%+]+=[\w\-.~%+,:@/]*)*
```

**Notes:**

Use `URL_QUERY` for a looser query that is not forced into key=value form.

**Example usage:**
```python
QUERY_STRING
# Matches: "?a=1&b=2", "?x="
# Does not match: "a=1", "?", "?a"
```

[▲ Back to top](#-table-of-contents)

---

### `HTTP_HEADER`

Regex expression matching an HTTP header line.

**Init Params:**
*(no parameters)*

**Pattern:**
A `HTTP_HEADER_NAME`, `:`, optional spaces and a `HTTP_HEADER_VALUE`.

```regex
[a-zA-Z0-9!#$%&'*+\-.\^_`|~]+:\ *[\t -~]*
```

**Example usage:**
```python
HTTP_HEADER
# Matches: "Content-Type: text/html", "Host:example.com"
# Does not match: "no header", "Name value"
```

[▲ Back to top](#-table-of-contents)

---

### `COOKIE`

Regex expression matching a cookie pair.

**Init Params:**
*(no parameters)*

**Pattern:**
A `COOKIE_NAME`, `=` and a `COOKIE_VALUE`.

```regex
[a-zA-Z0-9!#$%&'*+\-.\^_`|~]+=[\w\-.~%+/=:]*
```

**Example usage:**
```python
COOKIE
# Matches: "session=abc123", "flag="
# Does not match: "=x", "name", "a b=c"
```

[▲ Back to top](#-table-of-contents)

---

### `TOP_LEVEL_DOMAIN`

Regex expression matching a top-level domain.

**Init Params:**
*(no parameters)*

**Pattern:**
2–63 ASCII letters (e.g. `com`, `cz`, `museum`).

```regex
[a-zA-Z]{2,63}
```

**Example usage:**
```python
TOP_LEVEL_DOMAIN
# Matches: "com", "cz", "museum"
# Does not match: "c", "123", "co.uk", ""
```

[▲ Back to top](#-table-of-contents)

---

### `URI`

Regex expression matching a URI: a scheme, a colon and non-whitespace text.

**Init Params:**
*(no parameters)*

**Pattern:**
A `URL_SCHEME`, `:` and one or more non-whitespace characters.

```regex
[a-zA-Z][a-zA-Z0-9+\-.]*:\S+
```

**Notes:**

Deliberately loose; the part after the colon is not validated.

**Example usage:**
```python
URI
# Matches: "mailto:a@b.com", "urn:isbn:1", "https://x.org/a"
# Does not match: "nocolon", "http:", "1http:x"
```

[▲ Back to top](#-table-of-contents)

---

### `URN`

Regex expression matching a URN.

**Init Params:**
*(no parameters)*

**Pattern:**
`urn:`, a namespace identifier, a colon and a non-whitespace specific part.

```regex
urn:[a-zA-Z0-9][a-zA-Z0-9\-]*:\S+
```

**Example usage:**
```python
URN
# Matches: "urn:isbn:0451450523", "urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66"
# Does not match: "urn:", "isbn:123", "urn:x"
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](../README.md)
