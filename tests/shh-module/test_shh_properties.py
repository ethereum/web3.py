def test_shh_version(web3, skip_if_testrpc):
    skip_if_testrpc(web3)
    assert web3.shh.version == 2
