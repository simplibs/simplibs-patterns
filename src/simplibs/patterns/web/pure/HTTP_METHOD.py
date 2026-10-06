from simplibs.regex.elements.Literal import Literal


HTTP_METHOD = Literal("GET") | Literal("POST") | Literal("PUT") | Literal("PATCH") | Literal("DELETE") | Literal("HEAD") | Literal("OPTIONS") | Literal("TRACE") | Literal("CONNECT")
"""Regex expression matching an HTTP request method.

Init Params:
    (no parameters)

Pattern:
    One of `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`, `TRACE`, `CONNECT` (uppercase).
    Equivalent regex: `GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS|TRACE|CONNECT`

Example:
    HTTP_METHOD
    # Matches: "GET", "DELETE"
    # Does not match: "get", "FETCH"
"""

