# Pure:
from .pure.UUID import UUID
from .pure.GUID import GUID
from .pure.HEX_COLOR import HEX_COLOR
from .pure.VERSION import VERSION
from .pure.MAC_ADDRESS import MAC_ADDRESS
from .pure.IPV4_ADDRESS import IPV4_ADDRESS
from .pure.ISBN10 import ISBN10
from .pure.ISBN13 import ISBN13
from .pure.ISSN import ISSN
from .pure.BASE64_CHARACTER import BASE64_CHARACTER
from .pure.BASE64_URL_CHARACTER import BASE64_URL_CHARACTER
from .pure.HEX_STRING import HEX_STRING
from .pure.MD5 import MD5
from .pure.SHA1 import SHA1
from .pure.SHA256 import SHA256
# Composed:
from .composed.RGB_COLOR import RGB_COLOR
from .composed.RGBA_COLOR import RGBA_COLOR
from .composed.ISBN import ISBN
from .composed.HASH import HASH
# Custom:
from .custom.SEMVER import SEMVER
from .custom.IPV6_ADDRESS import IPV6_ADDRESS
from .custom.CREDIT_CARD_NUMBER import CREDIT_CARD_NUMBER
from .custom.IBAN import IBAN
from .custom.BASE64 import BASE64
from .custom.BASE64_URL import BASE64_URL
from .custom.ULID import ULID
from .custom.JWT import JWT


_DESIGN_NOTES = """
# Formats Patterns Sub-Package

## Purpose
Well-known text formats — UUID, colors, versions, MAC and IP addresses, ISBN/ISSN, card and bank numbers, Base64, hashes, ULID and JWT.

## Layout
`pure/` named concepts · `composed/` combinations of other terms and parametrized factories · `custom/` terms that needed a semantic decision

## Internal Components Registry

| Component              | Type             | Description                                  |
| :--------------------- | :--------------- | :------------------------------------------- |
| `UUID`                 | Regex Expression | A UUID in canonical form.                    |
| `GUID`                 | Regex Expression | A GUID.                                      |
| `HEX_COLOR`            | Regex Expression | A CSS hex color.                             |
| `RGB_COLOR`            | Regex Expression | A CSS rgb() color.                           |
| `RGBA_COLOR`           | Regex Expression | A CSS rgba() color.                          |
| `VERSION`              | Regex Expression | A dotted version number.                     |
| `SEMVER`               | Regex Expression | A semantic version (SemVer 2.0).             |
| `MAC_ADDRESS`          | Regex Expression | A MAC address.                               |
| `IPV4_ADDRESS`         | Regex Expression | An IPv4 address.                             |
| `IPV6_ADDRESS`         | Regex Expression | An IPv6 address.                             |
| `ISBN10`               | Regex Expression | An ISBN-10 without hyphens.                  |
| `ISBN13`               | Regex Expression | An ISBN-13 without hyphens.                  |
| `ISBN`                 | Regex Expression | An ISBN-10 or ISBN-13.                       |
| `ISSN`                 | Regex Expression | An ISSN.                                     |
| `CREDIT_CARD_NUMBER`   | Regex Expression | A credit card number without separators.     |
| `IBAN`                 | Regex Expression | An IBAN without spaces.                      |
| `BASE64_CHARACTER`     | Regex Expression | A character of the standard Base64 alphabet. |
| `BASE64_URL_CHARACTER` | Regex Expression | A character of the URL-safe Base64 alphabet. |
| `BASE64`               | Regex Expression | A padded Base64 string.                      |
| `BASE64_URL`           | Regex Expression | A URL-safe Base64 string.                    |
| `HEX_STRING`           | Regex Expression | A string of hexadecimal digits.              |
| `MD5`                  | Regex Expression | An MD5 digest in hex.                        |
| `SHA1`                 | Regex Expression | A SHA-1 digest in hex.                       |
| `SHA256`               | Regex Expression | A SHA-256 digest in hex.                     |
| `HASH`                 | Regex Expression | A common hash digest in hex.                 |
| `ULID`                 | Regex Expression | A ULID.                                      |
| `JWT`                  | Regex Expression | A JSON Web Token.                            |
"""
