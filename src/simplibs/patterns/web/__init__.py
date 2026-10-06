# Pure:
from .pure.URL_SCHEME import URL_SCHEME
from .pure.URL_CHARACTER import URL_CHARACTER
from .pure.URL_USERINFO import URL_USERINFO
from .pure.DOMAIN_LABEL import DOMAIN_LABEL
from .pure.SUBDOMAIN import SUBDOMAIN
from .pure.SECOND_LEVEL_DOMAIN import SECOND_LEVEL_DOMAIN
from .pure.DOMAIN import DOMAIN
from .pure.DOMAIN_NAME import DOMAIN_NAME
from .pure.HOSTNAME import HOSTNAME
from .pure.QUERY_PARAMETER import QUERY_PARAMETER
from .pure.HTTP_METHOD import HTTP_METHOD
from .pure.HTTP_STATUS_CODE import HTTP_STATUS_CODE
from .pure.HTTP_VERSION import HTTP_VERSION
from .pure.HTTP_HEADER_NAME import HTTP_HEADER_NAME
from .pure.HTTP_HEADER_VALUE import HTTP_HEADER_VALUE
from .pure.COOKIE_VALUE import COOKIE_VALUE
from .pure.COOKIE_NAME import COOKIE_NAME
# Composed:
from .composed.HOST import HOST
from .composed.URL_HOST import URL_HOST
from .composed.URL_PORT import URL_PORT
from .composed.URL_PATH import URL_PATH
from .composed.FRAGMENT_IDENTIFIER import FRAGMENT_IDENTIFIER
from .composed.URL_FRAGMENT import URL_FRAGMENT
from .composed.URL_QUERY import URL_QUERY
from .composed.URL_LOCATION import URL_LOCATION
from .composed.URL import URL
from .composed.HTTP_URL import HTTP_URL
from .composed.HTTPS_URL import HTTPS_URL
from .composed.WEB_ADDRESS import WEB_ADDRESS
from .composed.WEB_RESOURCE import WEB_RESOURCE
from .composed.ENDPOINT import ENDPOINT
from .composed.API_ENDPOINT import API_ENDPOINT
from .composed.QUERY_STRING import QUERY_STRING
from .composed.HTTP_HEADER import HTTP_HEADER
from .composed.COOKIE import COOKIE
# Custom:
from .custom.TOP_LEVEL_DOMAIN import TOP_LEVEL_DOMAIN
from .custom.URI import URI
from .custom.URN import URN


_DESIGN_NOTES = """
# Web Patterns Sub-Package

## Purpose
The web — URLs and their components, domains and hosts, query strings, HTTP methods/status/headers/versions and cookies.

## Layout
`pure/` named concepts · `composed/` combinations of other terms and parametrized factories · `custom/` terms that needed a semantic decision

## Internal Components Registry

| Component             | Type             | Description                                           |
| :-------------------- | :--------------- | :---------------------------------------------------- |
| `URL_SCHEME`          | Regex Expression | A URL scheme.                                         |
| `URL_CHARACTER`       | Regex Expression | A character allowed in a URL path, query or fragment. |
| `URL_USERINFO`        | Regex Expression | The user information part of a URL.                   |
| `DOMAIN_LABEL`        | Regex Expression | A single label of a domain name.                      |
| `SUBDOMAIN`           | Regex Expression | A subdomain label.                                    |
| `SECOND_LEVEL_DOMAIN` | Regex Expression | A second-level domain label.                          |
| `TOP_LEVEL_DOMAIN`    | Regex Expression | A top-level domain.                                   |
| `DOMAIN`              | Regex Expression | A domain name with at least two labels.               |
| `DOMAIN_NAME`         | Regex Expression | A domain name.                                        |
| `HOSTNAME`            | Regex Expression | A host name of one or more labels.                    |
| `HOST`                | Regex Expression | A host: IPv4, IPv6 or host name.                      |
| `URL_HOST`            | Regex Expression | The host part of a URL.                               |
| `URL_PORT`            | Regex Expression | The port part of a URL.                               |
| `URL_PATH`            | Regex Expression | The path part of a URL.                               |
| `FRAGMENT_IDENTIFIER` | Regex Expression | The text after the # of a URL.                        |
| `URL_FRAGMENT`        | Regex Expression | The fragment part of a URL.                           |
| `URL_QUERY`           | Regex Expression | The query part of a URL.                              |
| `URL_LOCATION`        | Regex Expression | Everything of a URL after the scheme and ://.         |
| `URL`                 | Regex Expression | A URL with a scheme and ://.                          |
| `HTTP_URL`            | Regex Expression | An http:// URL.                                       |
| `HTTPS_URL`           | Regex Expression | An https:// URL.                                      |
| `WEB_ADDRESS`         | Regex Expression | A web address (http or https).                        |
| `WEB_RESOURCE`        | Regex Expression | A web resource.                                       |
| `ENDPOINT`            | Regex Expression | An endpoint path.                                     |
| `API_ENDPOINT`        | Regex Expression | An API endpoint path.                                 |
| `URI`                 | Regex Expression | A URI: a scheme, a colon and non-whitespace text.     |
| `URN`                 | Regex Expression | A URN.                                                |
| `QUERY_PARAMETER`     | Regex Expression | A single key=value query parameter.                   |
| `QUERY_STRING`        | Regex Expression | A query string made of key=value parameters.          |
| `HTTP_METHOD`         | Regex Expression | An HTTP request method.                               |
| `HTTP_STATUS_CODE`    | Regex Expression | An HTTP status code.                                  |
| `HTTP_VERSION`        | Regex Expression | An HTTP version.                                      |
| `HTTP_HEADER_NAME`    | Regex Expression | An HTTP header field name.                            |
| `HTTP_HEADER_VALUE`   | Regex Expression | An HTTP header field value.                           |
| `HTTP_HEADER`         | Regex Expression | An HTTP header line.                                  |
| `COOKIE_VALUE`        | Regex Expression | A cookie value.                                       |
| `COOKIE_NAME`         | Regex Expression | A cookie name.                                        |
| `COOKIE`              | Regex Expression | A cookie pair.                                        |
"""
