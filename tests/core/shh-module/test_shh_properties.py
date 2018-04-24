def test_shh_version(web3, skip_if_testrpc):
    skip_if_testrpc(web3)
    assert web3.shh.version == '6.0'


def test_shh_info(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    web3.shh.setMaxMessageSize(1024)
    web3.shh.setMinPoW(0.5)

    info = web3.shh.info

    assert len(info) == 4
    assert info["maxMessageSize"] == 1024
    assert info["minPow"] == 0.5
