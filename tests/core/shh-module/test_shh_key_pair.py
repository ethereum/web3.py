def test_shh_asymmetric_key_pair(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    # Test generating key
    key_id = web3.shh.newKeyPair()
    assert web3.shh.hasKeyPair(key_id)
    assert len(web3.shh.getPublicKey(key_id)) == 132

    private_key = web3.shh.getPrivateKey(key_id)
    assert len(private_key) == 66
    assert web3.shh.deleteKeyPair(key_id)

    # Test adding a key
    assert not web3.shh.hasKeyPair(key_id)
    key_id = web3.shh.addPrivateKey(private_key)
    assert web3.shh.hasKeyPair(key_id)
    assert web3.shh.deleteKeyPair(key_id)


def test_shh_symmetric_key_pair(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    # Test generating key
    key_id = web3.shh.newSymKey()
    assert web3.shh.hasSymKey(key_id)

    key = web3.shh.getSymKey(key_id)
    assert len(key) == 66
    assert web3.shh.deleteSymKey(key_id)

    # Test adding a key
    assert not web3.shh.hasSymKey(key_id)
    key_id = web3.shh.addSymKey(key)
    assert web3.shh.hasSymKey(key_id)
    assert web3.shh.deleteSymKey(key_id)


def test_shh_symmetric_key_pair_from_password(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    key_id = web3.shh.generateSymKeyFromPassword('shh be quiet')

    assert web3.shh.hasSymKey(key_id)
    assert len(web3.shh.getSymKey(key_id)) == 66
    assert web3.shh.deleteSymKey(key_id)
