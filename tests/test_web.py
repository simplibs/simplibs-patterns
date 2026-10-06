from simplibs.regex.testing import assert_pattern

# Pure web patterns
from simplibs.patterns.web.pure.URL_SCHEME import URL_SCHEME
from simplibs.patterns.web.pure.URL_CHARACTER import URL_CHARACTER
from simplibs.patterns.web.pure.URL_USERINFO import URL_USERINFO
from simplibs.patterns.web.pure.DOMAIN_LABEL import DOMAIN_LABEL
from simplibs.patterns.web.pure.SUBDOMAIN import SUBDOMAIN
from simplibs.patterns.web.pure.SECOND_LEVEL_DOMAIN import SECOND_LEVEL_DOMAIN
from simplibs.patterns.web.pure.DOMAIN import DOMAIN
from simplibs.patterns.web.pure.DOMAIN_NAME import DOMAIN_NAME
from simplibs.patterns.web.pure.HOSTNAME import HOSTNAME
from simplibs.patterns.web.pure.QUERY_PARAMETER import QUERY_PARAMETER
from simplibs.patterns.web.pure.HTTP_METHOD import HTTP_METHOD
from simplibs.patterns.web.pure.HTTP_STATUS_CODE import HTTP_STATUS_CODE
from simplibs.patterns.web.pure.HTTP_VERSION import HTTP_VERSION
from simplibs.patterns.web.pure.HTTP_HEADER_NAME import HTTP_HEADER_NAME
from simplibs.patterns.web.pure.HTTP_HEADER_VALUE import HTTP_HEADER_VALUE
from simplibs.patterns.web.pure.COOKIE_VALUE import COOKIE_VALUE
from simplibs.patterns.web.pure.COOKIE_NAME import COOKIE_NAME

# Composed web patterns
from simplibs.patterns.web.composed.HOST import HOST
from simplibs.patterns.web.composed.URL_HOST import URL_HOST
from simplibs.patterns.web.composed.URL_PORT import URL_PORT
from simplibs.patterns.web.composed.URL_PATH import URL_PATH
from simplibs.patterns.web.composed.FRAGMENT_IDENTIFIER import FRAGMENT_IDENTIFIER
from simplibs.patterns.web.composed.URL_FRAGMENT import URL_FRAGMENT
from simplibs.patterns.web.composed.URL_QUERY import URL_QUERY
from simplibs.patterns.web.composed.URL_LOCATION import URL_LOCATION
from simplibs.patterns.web.composed.URL import URL
from simplibs.patterns.web.composed.HTTP_URL import HTTP_URL
from simplibs.patterns.web.composed.HTTPS_URL import HTTPS_URL
from simplibs.patterns.web.composed.WEB_ADDRESS import WEB_ADDRESS
from simplibs.patterns.web.composed.WEB_RESOURCE import WEB_RESOURCE
from simplibs.patterns.web.composed.ENDPOINT import ENDPOINT
from simplibs.patterns.web.composed.API_ENDPOINT import API_ENDPOINT
from simplibs.patterns.web.composed.QUERY_STRING import QUERY_STRING
from simplibs.patterns.web.composed.HTTP_HEADER import HTTP_HEADER
from simplibs.patterns.web.composed.COOKIE import COOKIE

# Custom web patterns
from simplibs.patterns.web.custom.TOP_LEVEL_DOMAIN import TOP_LEVEL_DOMAIN
from simplibs.patterns.web.custom.URI import URI
from simplibs.patterns.web.custom.URN import URN


def test_url_scheme(subtests):
    assert_pattern(
        subtests,
        URL_SCHEME,
        r"[a-zA-Z][a-zA-Z0-9+\-.]*",
        matches=["http", "git+ssh", "a1"],
        non_matches=["1http", "-x", ""]
    )

def test_url_character(subtests):
    assert_pattern(
        subtests,
        URL_CHARACTER,
        r"[a-zA-Z0-9\-._\~%/:@=!$\&'()*+,;]",
        matches=["a", "/", "%", "~"],
        non_matches=["?", "#", " ", "ab"]
    )

def test_url_userinfo(subtests):
    assert_pattern(
        subtests,
        URL_USERINFO,
        r"[\w\-.:\~%]+",
        matches=["user", "user:pass"],
        non_matches=["", "a@b", "a b"]
    )

def test_domain_label(subtests):
    assert_pattern(
        subtests,
        DOMAIN_LABEL,
        r"[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?",
        matches=["example", "a", "my-site", "a1"],
        non_matches=["-a", "a-", "", "a_b"]
    )

def test_subdomain(subtests):
    assert_pattern(
        subtests,
        SUBDOMAIN,
        r"[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?",
        matches=["example", "a", "my-site", "a1"],
        non_matches=["-a", "a-", "", "a_b"]
    )

def test_second_level_domain(subtests):
    assert_pattern(
        subtests,
        SECOND_LEVEL_DOMAIN,
        r"[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?",
        matches=["example", "a", "my-site", "a1"],
        non_matches=["-a", "a-", "", "a_b"]
    )

def test_domain(subtests):
    assert_pattern(
        subtests,
        DOMAIN,
        r"[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+",
        matches=["example.com", "sub.example.co.uk"],
        non_matches=["localhost", "example.", "-a.com", ".com"]
    )

def test_domain_name(subtests):
    assert_pattern(
        subtests,
        DOMAIN_NAME,
        r"[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+",
        matches=["example.com", "sub.example.co.uk"],
        non_matches=["localhost", "example.", "-a.com", ".com"]
    )

def test_hostname(subtests):
    assert_pattern(
        subtests,
        HOSTNAME,
        r"[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*",
        matches=["localhost", "example.com", "my-server.local"],
        non_matches=["-a", "a..b", ""]
    )

def test_query_parameter(subtests):
    assert_pattern(
        subtests,
        QUERY_PARAMETER,
        r"[\w\-.\~%+]+=[\w\-.\~%+,:@/]*",
        matches=["page=2", "q=hello+world", "flag="],
        non_matches=["=x", "a b=1", "a=b&c=d"]
    )

def test_http_method(subtests):
    assert_pattern(
        subtests,
        HTTP_METHOD,
        r"GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS|TRACE|CONNECT",
        matches=["GET", "DELETE"],
        non_matches=["get", "FETCH"]
    )

def test_http_status_code(subtests):
    assert_pattern(
        subtests,
        HTTP_STATUS_CODE,
        r"[1-5][0-9]{2}",
        matches=["200", "404", "503"],
        non_matches=["99", "600", "20", "2000"]
    )

def test_http_version(subtests):
    assert_pattern(
        subtests,
        HTTP_VERSION,
        r"HTTP/(?:[0-9]\.[0-9]|[23])",
        matches=["HTTP/1.1", "HTTP/2", "HTTP/3"],
        non_matches=["HTTP/", "HTTP 1.1", "HTTP/1"]
    )

def test_http_header_name(subtests):
    assert_pattern(
        subtests,
        HTTP_HEADER_NAME,
        r"[a-zA-Z0-9!#$%\&'*+\-.\^_`\|\~]+",
        matches=["Content-Type", "X-Request-ID", "Host"],
        non_matches=["Content Type", "Name:", ""]
    )

def test_http_header_value(subtests):
    assert_pattern(
        subtests,
        HTTP_HEADER_VALUE,
        r"[\t -\~]*",
        matches=["text/html; charset=utf-8", ""],
        non_matches=["a\nb"]
    )

def test_cookie_value(subtests):
    assert_pattern(
        subtests,
        COOKIE_VALUE,
        r"[\w\-.\~%+/=:]*",
        matches=["abc123", "a%20b", "dGVzdA==", ""],
        non_matches=["a b", "a;b", "a,b"]
    )

def test_cookie_name(subtests):
    assert_pattern(
        subtests,
        COOKIE_NAME,
        r"[a-zA-Z0-9!#$%\&'*+\-.\^_`\|\~]+",
        matches=["Content-Type", "X-Request-ID", "Host"],
        non_matches=["Content Type", "Name:", ""]
    )

def test_host(subtests):
    assert_pattern(
        subtests,
        HOST,
        '(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:\\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3}|(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?)*',
    matches=["example.com", "localhost", "192.168.0.1", "::1"],
        non_matches=["-x", "a..b", ""]
    )

def test_url_host(subtests):
    assert_pattern(
        subtests,
        URL_HOST,
        '(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:\\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3}|\\[(?:(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:))\\]|[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?)*',        matches=["example.com", "localhost", "192.168.0.1", "[::1]"],
        non_matches=["::1", "[::1", "a..b"]
    )

def test_url_port(subtests):
    assert_pattern(
        subtests,
        URL_PORT,
        r":(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0)",
        matches=[":80", ":8080", ":65535"],
        non_matches=["80", ":65536", ":"]
    )

def test_url_path(subtests):
    assert_pattern(
        subtests,
        URL_PATH,
        r"/[a-zA-Z0-9\-._\~%/:@=!$\&'()*+,;]*",
        matches=["/", "/a/b.html", "/path/to/file"],
        non_matches=["a/b", "/a?b", "/a b"]
    )

def test_fragment_identifier(subtests):
    assert_pattern(
        subtests,
        FRAGMENT_IDENTIFIER,
        r"(?:[a-zA-Z0-9\-._\~%/:@=!$\&'()*+,;]|\?)*",
        matches=["section-2", "top", ""],
        non_matches=["a b", "#x"]
    )

def test_url_fragment(subtests):
    assert_pattern(
        subtests,
        URL_FRAGMENT,
        r"\#(?:[a-zA-Z0-9\-._\~%/:@=!$\&'()*+,;]|\?)*",
        matches=["#top", "#section-2", "#"],
        non_matches=["top", "#a b"]
    )

def test_url_query(subtests):
    assert_pattern(
        subtests,
        URL_QUERY,
        r"\?(?:[a-zA-Z0-9\-._\~%/:@=!$\&'()*+,;]|\?)*",
        matches=["?a=1&b=2", "?"],
        non_matches=["a=1", "?a b", "?#x"]
    )

def test_url_location(subtests):
    assert_pattern(
        subtests,
        URL_LOCATION,
        "(?:[\\w\\-.:\\~%]+@)?(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:\\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3}|\\[(?:(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:))\\]|[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?)*)(?::(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0))?(?:/[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]*)?(?:\\?(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?(?:\\#(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?",        non_matches=["", "http://x", "exa mple.com"]
    )

def test_url(subtests):
    assert_pattern(
        subtests,
        URL,
        "[a-zA-Z][a-zA-Z0-9+\\-.]*://(?:[\\w\\-.:\\~%]+@)?(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:\\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3}|\\[(?:(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:))\\]|[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?)*)(?::(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0))?(?:/[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]*)?(?:\\?(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?(?:\\#(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?",
        matches=["https://example.com/path?q=1#frag", "ftp://files.example.org", "git+ssh://user@host:22/repo.git"],
        non_matches=["example.com", "http:/example.com", "http://"]
    )

def test_http_url(subtests):
    assert_pattern(
        subtests,
        HTTP_URL,
        "http://(?:[\\w\\-.:\\~%]+@)?(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:\\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3}|\\[(?:(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:))\\]|[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?)*)(?::(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0))?(?:/[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]*)?(?:\\?(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?(?:\\#(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?",        matches=["http://example.com", "http://localhost:8080/a?b=1"],
        non_matches=["https://example.com", "example.com"]
    )

def test_https_url(subtests):
    assert_pattern(
        subtests,
        HTTPS_URL,
        "https://(?:[\\w\\-.:\\~%]+@)?(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:\\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3}|\\[(?:(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:))\\]|[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?)*)(?::(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0))?(?:/[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]*)?(?:\\?(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?(?:\\#(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?",        matches=["https://example.com", "https://example.com/a/b?c=d#e"],
        non_matches=["http://example.com", "example.com"]
    )

def test_web_address(subtests):
    assert_pattern(
        subtests,
        WEB_ADDRESS,
        "https://(?:[\\w\\-.:\\~%]+@)?(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:\\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3}|\\[(?:(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:))\\]|[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?)*)(?::(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0))?(?:/[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]*)?(?:\\?(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?(?:\\#(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?|http://(?:[\\w\\-.:\\~%]+@)?(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:\\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3}|\\[(?:(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:))\\]|[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?)*)(?::(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0))?(?:/[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]*)?(?:\\?(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?(?:\\#(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?",
        matches=["https://example.com", "http://example.com/a"],
        non_matches=["ftp://example.com", "example.com"]
    )

def test_web_resource(subtests):
    assert_pattern(
        subtests,
        WEB_RESOURCE,
        "[a-zA-Z][a-zA-Z0-9+\\-.]*://(?:[\\w\\-.:\\~%]+@)?(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:\\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3}|\\[(?:(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:))\\]|[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?)*)(?::(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0))?(?:/[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]*)?(?:\\?(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?(?:\\#(?:[a-zA-Z0-9\\-._\\~%/:@=!$\\&'()*+,;]|\\?)*)?",
        matches=["https://example.com/path?q=1#frag", "ftp://files.example.org", "git+ssh://user@host:22/repo.git"],
        non_matches=["example.com", "http:/example.com", "http://"]
    )

def test_endpoint(subtests):
    assert_pattern(
        subtests,
        ENDPOINT,
        r"/[a-zA-Z0-9\-._\~%/:@=!$\&'()*+,;]*",
        matches=["/", "/a/b.html", "/path/to/file"],
        non_matches=["a/b", "/a?b", "/a b"]
    )

def test_api_endpoint(subtests):
    assert_pattern(
        subtests,
        API_ENDPOINT,
        r"/[a-zA-Z0-9\-._\~%/:@=!$\&'()*+,;]*",
        matches=["/", "/a/b.html", "/path/to/file"],
        non_matches=["a/b", "/a?b", "/a b"]
    )

def test_query_string(subtests):
    assert_pattern(
        subtests,
        QUERY_STRING,
        r"\?[\w\-.\~%+]+=[\w\-.\~%+,:@/]*(?:\&[\w\-.\~%+]+=[\w\-.\~%+,:@/]*)*",
        matches=["?a=1&b=2", "?x="],
        non_matches=["a=1", "?", "?a"]
    )

def test_http_header(subtests):
    assert_pattern(
        subtests,
        HTTP_HEADER,
        r"[a-zA-Z0-9!#$%\&'*+\-.\^_`\|\~]+:\ *[\t -\~]*",
        matches=["Content-Type: text/html", "Host:example.com"],
        non_matches=["no header", "Name value"]
    )

def test_cookie(subtests):
    assert_pattern(
        subtests,
        COOKIE,
        r"[a-zA-Z0-9!#$%\&'*+\-.\^_`\|\~]+=[\w\-.\~%+/=:]*",
        matches=["session=abc123", "flag="],
        non_matches=["=x", "name", "a b=c"]
    )

def test_top_level_domain(subtests):
    assert_pattern(
        subtests,
        TOP_LEVEL_DOMAIN,
        r"[a-zA-Z]{2,63}",
        matches=["com", "cz", "museum"],
        non_matches=["c", "123", "co.uk", ""]
    )

def test_uri(subtests):
    assert_pattern(
        subtests,
        URI,
        r"[a-zA-Z][a-zA-Z0-9+\-.]*:\S+",
        matches=["mailto:a@b.com", "urn:isbn:1", "https://x.org/a"],
        non_matches=["nocolon", "http:", "1http:x"]
    )

def test_urn(subtests):
    assert_pattern(
        subtests,
        URN,
        r"urn:[a-zA-Z0-9][a-zA-Z0-9\-]*:\S+",
        matches=["urn:isbn:0451450523", "urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66"],
        non_matches=["urn:", "isbn:123", "urn:x"]
    )