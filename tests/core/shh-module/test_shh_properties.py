import pytest


def test_shh_version(web3, skip_if_testrpc):
    skip_if_testrpc(web3)
    assert web3.shh.version == '6.0'


def test_shh_info_deprecated(web3, skip_if_testrpc):
    skip_if_testrpc(web3)
    with pytest.warns(DeprecationWarning) as warnings:
        web3.shh.setMaxMessageSize(1024)
        web3.shh.setMinPoW(0.5)

        info = web3.shh.info

        assert len(warnings) == 2
        assert len(info) == 4
        assert info["maxMessageSize"] == 1024
        assert info["minPow"] == 0.5


def test_shh_info(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    web3.shh.set_max_message_size(1024)
    web3.shh.set_min_pow(0.5)

    info = web3.shh.info

    assert len(info) == 4
    assert info["maxMessageSize"] == 1024
    assert info["minPow"] == 0.5
