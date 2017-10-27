def test_shh_new_identity(web3, skip_if_testrpc):
    skip_if_testrpc(web3)
    new_identity = web3.shh.newIdentity()
    assert isinstance(new_identity, bytes)
    assert len(new_identity) == 60
