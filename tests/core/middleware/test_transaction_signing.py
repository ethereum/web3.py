import pytest

from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider

from unittest.mock import (
    Mock,
)

from hexbytes import HexBytes

import eth_account
import eth_keys
from web3.middleware.signing import (
    construct_in_flight_transaction_signing_middleware,
    key_to_account,
)

KEYFILE_DATA = '{"address":"dc544d1aa88ff8bbd2f2aec754b1f1e99e1812fd","crypto":{"cipher":"aes-128-ctr","ciphertext":"52e06bc9397ea9fa2f0dae8de2b3e8116e92a2ecca9ad5ff0061d1c449704e98","cipherparams":{"iv":"aa5d0a5370ef65395c1a6607af857124"},"kdf":"scrypt","kdfparams":{"dklen":32,"n":262144,"p":1,"r":8,"salt":"9fdf0764eb3645ffc184e166537f6fe70516bf0e34dc7311dea21f100f0c9263"},"mac":"4e0b51f42b865c15c485f4faefdd1f01a38637e5247f8c75ffe6a8c0eba856f6"},"id":"5a6124e0-10f1-4c1c-ae3e-d903eacb740a","version":3}'  # noqa: E501


@pytest.fixture()
def private_key():
    return eth_account.Account.decrypt(KEYFILE_DATA, 'web3py-test')


@pytest.fixture()
def w3():
    return Web3(EthereumTesterProvider())


@pytest.fixture(
    params=[
        eth_keys.keys.PrivateKey,
        eth_account.Account.privateKeyToAccount,
        HexBytes,
    ])
def key_object(request, private_key):
    return request.param(private_key)


@pytest.fixture
def mocked_signing_middleware(private_key):
    make_request, web3 = Mock(), Mock()
    signing_middleware = construct_in_flight_transaction_signing_middleware(private_key)
    middleware = signing_middleware(make_request, web3)
    middleware.make_request = make_request
    middleware.web3 = web3
    return middleware


def test_key_to_account(w3, key_object):
    account = key_to_account(w3, key_object)
    assert isinstance(account, eth_account.local.LocalAccount)


def test_key_to_account_value_error(w3):
    with pytest.raises(ValueError):
        key_to_account(w3, 1234567890)


def test_captured_method(private_key, mocked_signing_middleware):
    method = 'eth_sendTransaction'
    params = [{
        'to': '0x0',
        'value': 1,
    }]
    mocked_signing_middleware(method, params)
    mocked_signing_middleware.web3.eth.account.privateKeyToAccount.assert_called_with(private_key)


def test_passthrough_method(private_key, mocked_signing_middleware):
    method = 'eth_call'
    params = []
    mocked_signing_middleware(method, params)
    mocked_signing_middleware.make_request.called_with(params)


def test_signed_transaction(w3, key_object):
    # fund local account
    account = key_to_account(w3, key_object)
    w3.eth.sendTransaction({
        'to': account.address,
        'from': w3.eth.accounts[0],
        'value': 10})
    assert w3.eth.getBalance(account.address) == 10
    w3.middleware_stack.add(construct_in_flight_transaction_signing_middleware(key_object))
    w3.eth.sendTransaction({
        'to': w3.eth.accounts[0],
        'value': 10})
    assert w3.eth.getBalance(account.address) == 0
