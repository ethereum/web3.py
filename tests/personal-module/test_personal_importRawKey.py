from testrpc.client.utils import (
    encode_32bytes,
)

from web3.utils.address import (
    is_same_address,
)
from web3.utils.formatting import (
    remove_0x_prefix,
)


def test_personal_importRawKey_as_bytes(web3, account_private_key,
                                        account_password, account_public_key):
    address = web3.personal.importRawKey(account_private_key, account_password)

    # sanity check
    assert is_same_address(address, account_public_key)

    assert web3.personal.unlockAccount(address, account_password) is True


def test_personal_importRawKey_as_hex_with_0x(web3, account_private_key,
                                              account_password,
                                              account_public_key):
    address = web3.personal.importRawKey(encode_32bytes(account_private_key), account_password)

    # sanity check
    assert is_same_address(address, account_public_key)

    assert web3.personal.unlockAccount(address, account_password) is True


def test_personal_importRawKey_as_hex_without_0x(web3,
                                                 account_private_key,
                                                 account_password,
                                                 account_public_key):
    address = web3.personal.importRawKey(remove_0x_prefix(encode_32bytes(account_private_key)), account_password)

    # sanity check
    assert is_same_address(address, account_public_key)

    assert web3.personal.unlockAccount(address, account_password) is True
