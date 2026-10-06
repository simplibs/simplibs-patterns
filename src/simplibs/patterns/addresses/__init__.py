# Pure:
from .pure.EMAIL_LOCAL_PART import EMAIL_LOCAL_PART
# Composed:
from .composed.IP_ADDRESS import IP_ADDRESS
from .composed.PO_BOX import PO_BOX
# Custom:
from .custom.EMAIL_ADDRESS import EMAIL_ADDRESS
from .custom.PHONE_NUMBER import PHONE_NUMBER
from .custom.INTERNATIONAL_PHONE_NUMBER import INTERNATIONAL_PHONE_NUMBER
from .custom.POSTAL_CODE import POSTAL_CODE
from .custom.ZIP_CODE import ZIP_CODE
from .custom.STREET_ADDRESS import STREET_ADDRESS


_DESIGN_NOTES = """
# Addresses Patterns Sub-Package

## Purpose
Addresses of people and machines — IP, email, phone numbers, postal codes, street addresses and P.O. boxes.

## Layout
`pure/` named concepts · `composed/` combinations of other terms and parametrized factories · `custom/` terms that needed a semantic decision

## Internal Components Registry

| Component                    | Type             | Description                                    |
| :--------------------------- | :--------------- | :--------------------------------------------- |
| `IP_ADDRESS`                 | Regex Expression | An IPv4 or IPv6 address.                       |
| `EMAIL_LOCAL_PART`           | Regex Expression | The part of an email address before the @.     |
| `EMAIL_ADDRESS`              | Regex Expression | An email address.                              |
| `PHONE_NUMBER`               | Regex Expression | A phone number in a lenient written form.      |
| `INTERNATIONAL_PHONE_NUMBER` | Regex Expression | An international phone number in E.164 form.   |
| `POSTAL_CODE`                | Regex Expression | A postal code in a generic international form. |
| `ZIP_CODE`                   | Regex Expression | A US ZIP code.                                 |
| `STREET_ADDRESS`             | Regex Expression | A street address line in a lenient form.       |
| `PO_BOX`                     | Regex Expression | A P.O. box line.                               |
"""
