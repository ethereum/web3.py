
import pytest

from ens import (
    InvalidName,
)

# test content inspired by https://github.com/jcranmer/idna-uts46/blob/9e2ff191a8887c872ad172f2d72f8d4bf353aef8/test/test-uts46.js  # noqa: E501


def test_nameprep_basic_unicode(ens):
    assert ens.nameprep("öbb.at") == "öbb.at"
    assert ens.nameprep("Öbb.at") == "öbb.at"
    assert ens.nameprep("O\u0308bb.at") == "öbb.at"
    assert ens.nameprep("xn--bb-eka.at") == "öbb.at"
    assert ens.nameprep("faß.de") == "faß.de"
    assert ens.nameprep("fass.de") == "fass.de"
    assert ens.nameprep("xn--fa-hia.de") == "faß.de"


def test_nameprep_std3_rules(ens):
    with pytest.raises(InvalidName):
        ens.nameprep("not=std3")
