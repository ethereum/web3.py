import pytest


def test_shh_asymmetric_key_pair_deprecated(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    # Test generating key
    with pytest.warns(DeprecationWarning) as warnings:
        key_id = web3.shh.newKeyPair()
        assert web3.shh.haskeyPair(key_id)
        assert len(web3.shh.getPublicKey(key_id)) == 132
        private_key = web3.shh.getPrivateKey(key_id)
        assert len(private_key) == 66
        assert web3.shh.deleteKeyPair(key_id)

    # Test adding a key
        assert not web3.shh.hasKeyPair(key_id)

        key_id = web3.shh.addPrivateKey(private_key)
        assert web3.shh.hasKeyPair(key_id)
        assert web3.shh.deleteKeyPair(key_id)

        assert len(warnings) == 9


def test_shh_asymmetric_key_pair(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    # Test generating key

    key_id = web3.shh.new_key_pair()
    assert web3.shh.has_key_pair(key_id)
    assert len(web3.shh.get_public_key(key_id)) == 132
    private_key = web3.shh.get_private_key(key_id)
    assert len(private_key) == 66
    assert web3.shh.delete_key_pair(key_id)

    # Test adding a key
    assert not web3.shh.has_key_pair(key_id)

    key_id = web3.shh.add_private_key(private_key)
    assert web3.shh.has_key_pair(key_id)
    assert web3.shh.delete_key_pair(key_id)


def test_shh_symmetric_key_pair_deprecated(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    # Test generating key
    with pytest.warns(DeprecationWarning) as warnings:
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

        assert len(warnings) == 8


def test_shh_symmetric_key_pair(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    # Test generating key

    key_id = web3.shh.new_sym_key()
    assert web3.shh.has_sym_key(key_id)
    key = web3.shh.get_sym_key(key_id)
    assert len(key) == 66
    assert web3.shh.delete_sym_key(key_id)

    # Test adding a key
    assert not web3.shh.has_sym_key(key_id)
    key_id = web3.shh.add_sym_key(key)
    assert web3.shh.has_sym_key(key_id)
    assert web3.shh.delete_sym_key(key_id)


def test_shh_symmetric_key_pair_from_password_deprecated(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    with pytest.warns(DeprecationWarning):
        key_id = web3.shh.generate_sym_key_from_password('shh be quiet')

        assert web3.shh.hasSymKey(key_id)
        assert len(web3.shh.getSymKey(key_id)) == 66
        assert web3.shh.deleteSymKey(key_id)


def test_shh_symmetric_key_pair_from_password(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    key_id = web3.shh.generate_sym_key_from_password('shh be quiet')

    assert web3.shh.has_sym_key(key_id)
    assert len(web3.shh.get_sym_key(key_id)) == 66
    assert web3.shh.delete_sym_key(key_id)
