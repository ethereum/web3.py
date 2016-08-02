from eth_tester_client.utils import (
    normalize_address,
    encode_32bytes,
    strip_0x,
)


reset_chain = True


def test_personal_importRawKey_as_bytes(web3, account_private_key, account_password,
                               account_public_key):
    address = web3.personal.importRawKey(account_private_key, account_password)

    # sanity check
    assert normalize_address(address) == normalize_address(account_public_key)

    assert web3.personal.unlockAccount(address, account_password) is True


def test_personal_importRawKey_as_hex_with_0x(web3, account_private_key, account_password,
                               account_public_key):
    address = web3.personal.importRawKey(encode_32bytes(account_private_key), account_password)

    # sanity check
    assert normalize_address(address) == normalize_address(account_public_key)

    assert web3.personal.unlockAccount(address, account_password) is True


def test_personal_importRawKey_as_hex_without_0x(web3, account_private_key, account_password,
                               account_public_key):
    address = web3.personal.importRawKey(strip_0x(encode_32bytes(account_private_key)), account_password)

    # sanity check
    assert normalize_address(address) == normalize_address(account_public_key)

    assert web3.personal.unlockAccount(address, account_password) is True
