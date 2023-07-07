import pytest

from ens import (
    ENS,
    AsyncENS,
)

# test content inspired by https://github.com/jcranmer/idna-uts46/blob/9e2ff191a8887c872ad172f2d72f8d4bf353aef8/test/test-uts46.js  # noqa: E501

TEST_CONTENT = (
    ("öbb.at", "öbb.at"),
    ("Öbb.at", "öbb.at"),
    ("O\u0308bb.at", "öbb.at"),
    ("faß.de", "faß.de"),
    ("fass.de", "fass.de"),
    ("🌈rainbow.eth", "🌈rainbow.eth"),
    ("🐔🐔.tk", "🐔🐔.tk"),
    ("√.com", "√.com"),
    ("ԛәлп.com", "ԛәлп.com"),
    ("test\u200btest.com", "testtest.com"),
    ("-test.com", "-test.com"),
    ("1test.com", "1test.com"),
    ("test.1com", "test.1com"),
)


@pytest.mark.parametrize("name,expected", TEST_CONTENT)
def test_nameprep_basic_unicode(name, expected):
    assert ENS.nameprep(name) == expected


# -- async -- #


@pytest.mark.parametrize("name,expected", TEST_CONTENT)
def test_async_nameprep_basic_unicode(name, expected):
    assert AsyncENS.nameprep(name) == expected
