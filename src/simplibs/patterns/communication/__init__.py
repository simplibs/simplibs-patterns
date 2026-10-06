# Pure:
from .pure.EMAIL import EMAIL
from .pure.USER_HANDLE import USER_HANDLE
from .pure.MENTION import MENTION
from .pure.SOCIAL_HANDLE import SOCIAL_HANDLE
from .pure.HASHTAG import HASHTAG
from .pure.SUBJECT import SUBJECT
from .pure.REPLY_ADDRESS import REPLY_ADDRESS
from .pure.SENDER_ADDRESS import SENDER_ADDRESS
from .pure.RECIPIENT_ADDRESS import RECIPIENT_ADDRESS
from .pure.EMAIL_HEADER_NAME import EMAIL_HEADER_NAME
from .pure.EMAIL_HEADER_VALUE import EMAIL_HEADER_VALUE
# Composed:
from .composed.EMAIL_HEADER import EMAIL_HEADER
from .composed.EMAIL_SUBJECT import EMAIL_SUBJECT
# Custom:
from .custom.USERNAME import USERNAME
from .custom.DISPLAY_NAME import DISPLAY_NAME
from .custom.MESSAGE_ID import MESSAGE_ID


_DESIGN_NOTES = """
# Communication Patterns Sub-Package

## Purpose
Communication artefacts — email, user names and handles, hashtags, display names, message ids and email headers.

## Layout
`pure/` named concepts · `composed/` combinations of other terms and parametrized factories · `custom/` terms that needed a semantic decision

## Internal Components Registry

| Component            | Type             | Description                     |
| :------------------- | :--------------- | :------------------------------ |
| `EMAIL`              | Regex Expression | An email address.               |
| `USERNAME`           | Regex Expression | A user name of 3–32 characters. |
| `USER_HANDLE`        | Regex Expression | A user handle such as @name.    |
| `MENTION`            | Regex Expression | A mention.                      |
| `SOCIAL_HANDLE`      | Regex Expression | A social media handle.          |
| `HASHTAG`            | Regex Expression | A hashtag.                      |
| `DISPLAY_NAME`       | Regex Expression | A person's display name.        |
| `SUBJECT`            | Regex Expression | A message subject.              |
| `MESSAGE_ID`         | Regex Expression | An email Message-ID.            |
| `REPLY_ADDRESS`      | Regex Expression | A reply-to email address.       |
| `SENDER_ADDRESS`     | Regex Expression | A sender email address.         |
| `RECIPIENT_ADDRESS`  | Regex Expression | A recipient email address.      |
| `EMAIL_HEADER_NAME`  | Regex Expression | An email header field name.     |
| `EMAIL_HEADER_VALUE` | Regex Expression | An email header field value.    |
| `EMAIL_HEADER`       | Regex Expression | An email header line.           |
| `EMAIL_SUBJECT`      | Regex Expression | An email Subject header line.   |
"""
