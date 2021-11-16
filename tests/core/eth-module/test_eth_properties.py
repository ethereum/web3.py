import pytest


def test_eth_protocol_version(w3):
    with pytest.warns(DeprecationWarning):
        assert w3.eth.protocol_version == '63'


def test_eth_protocolVersion(w3):
    with pytest.warns(DeprecationWarning):
        assert w3.eth.protocolVersion == '63'


def test_eth_chain_id(w3):
    assert w3.eth.chain_id == 61


def test_eth_chainId(w3):
    with pytest.warns(DeprecationWarning):
        assert w3.eth.chainId == 61


def test_set_chain_id(w3):
    assert w3.eth.chain_id == 61

    w3.eth.chain_id = 72
    assert w3.eth.chain_id == 72

    w3.eth.chain_id = None
    assert w3.eth.chain_id == 61
