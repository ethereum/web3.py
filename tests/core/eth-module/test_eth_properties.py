import pytest


def test_eth_protocol_version(web3):
    assert web3.eth.protocol_version == '63'


def test_eth_protocolVersion(web3):
    with pytest.warns(DeprecationWarning):
        assert web3.eth.protocolVersion == '63'


def test_eth_chainId(web3):
    assert web3.eth.chainId == 61
