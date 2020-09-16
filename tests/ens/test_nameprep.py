
import pytest

from ens import (
    InvalidName,
)

# test content inspired by https://github.com/jcranmer/idna-uts46/blob/9e2ff191a8887c872ad172f2d72f8d4bf353aef8/test/test-uts46.js  # noqa: E501


def test_nameprep_basic_unicode(ens):
    assert ens.nameprep("öbb.at") == "öbb.at"
    assert ens.nameprep("Öbb.at") == "öbb.at"
    assert ens.nameprep("O\u0308bb.at") == "öbb.at"
    assert ens.nameprep("faß.de") == "faß.de"
    assert ens.nameprep("fass.de") == "fass.de"
    assert ens.nameprep("🌈rainbow.eth") == "🌈rainbow.eth"
    assert ens.nameprep("🐔🐔.tk") == "🐔🐔.tk"
    assert ens.nameprep("√.com") == "√.com"
    assert ens.nameprep("ԛәлп.com") == "ԛәлп.com"
    assert ens.nameprep("test\u200btest.com") == "testtest.com"
    assert ens.nameprep("-test.com") == "-test.com"
    assert ens.nameprep("1test.com") == "1test.com"
    assert ens.nameprep("test.1com") == "test.1com"


@pytest.mark.parametrize(
    'url', [
        ('not=std3'),
        ('not_std3.eth'),  # underscores not allowed
    ]
)
def test_nameprep_std3_rules(ens, url):
    with pytest.raises(InvalidName,
                       match=f'{url} is an invalid name'):
        ens.nameprep(url)
