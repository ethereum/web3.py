import pytest

import eth_account
import eth_keys
from hexbytes import (
    HexBytes,
)

from web3 import Web3
from web3.middleware import (
    construct_result_generator_middleware,
    construct_sign_and_send_raw_middleware,
)
from web3.middleware.signing import (
    to_account,
)
from web3.providers import (
    BaseProvider,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)

KEYFILE_DATA = '{"address":"dc544d1aa88ff8bbd2f2aec754b1f1e99e1812fd","crypto":{"cipher":"aes-128-ctr","ciphertext":"52e06bc9397ea9fa2f0dae8de2b3e8116e92a2ecca9ad5ff0061d1c449704e98","cipherparams":{"iv":"aa5d0a5370ef65395c1a6607af857124"},"kdf":"scrypt","kdfparams":{"dklen":32,"n":262144,"p":1,"r":8,"salt":"9fdf0764eb3645ffc184e166537f6fe70516bf0e34dc7311dea21f100f0c9263"},"mac":"4e0b51f42b865c15c485f4faefdd1f01a38637e5247f8c75ffe6a8c0eba856f6"},"id":"5a6124e0-10f1-4c1c-ae3e-d903eacb740a","version":3}'  # noqa: E501


@pytest.fixture(scope='session')
def private_key():
    return eth_account.Account.decrypt(KEYFILE_DATA, 'web3py-test')


class DummyProvider(BaseProvider):
    def make_request(self, method, params):
        raise NotImplementedError("Cannot make request for {0}:{1}".format(
            method,
            params,
        ))


@pytest.fixture(scope='session')
def result_generator_middleware():
    return construct_result_generator_middleware({
        'eth_sendRawTransaction': lambda *args: args,
        'net_version': lambda *_: 1,
    })


@pytest.fixture(scope='session')
def w3_base():
    return Web3(providers=[DummyProvider()], middlewares=[])


@pytest.fixture(scope='session')
def w3_dummy(w3_base, result_generator_middleware):
    w3_base.middleware_stack.add(result_generator_middleware)
    return w3_base


@pytest.mark.parametrize(
    'method,expected',
    (
        ('eth_sendTransaction', 'eth_sendRawTransaction'),
        ('eth_call', NotImplementedError),
    )
)
def test_sign_and_send_raw_middleware(w3_dummy, w3, method, expected, key_object):
    w3_dummy.middleware_stack.add(construct_sign_and_send_raw_middleware(key_object))
    account = to_account(w3, key_object)

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            w3_dummy.manager.request_blocking(
                method,
                [{
                    'to': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
                    'from': account.address,
                    'gas': 21000,
                    'gasPrice': 0,
                    'value': 1,
                    'nonce': 0
                }])
    else:
        actual = w3_dummy.manager.request_blocking(
            method,
            [{
                'to': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
                'from': account.address,
                'gas': 21000,
                'gasPrice': 0,
                'value': 1,
                'nonce': 0
            }])
        raw_txn = actual[1][0]
        actual_method = actual[0]
        assert actual_method == expected
        assert isinstance(raw_txn, bytes)


@pytest.fixture(scope='session')
def w3():
    return Web3(EthereumTesterProvider())


@pytest.fixture(
    scope='session',
    params=[
        eth_keys.keys.PrivateKey,
        eth_account.Account.privateKeyToAccount,
        HexBytes,
    ])
def key_object(request, private_key):
    return request.param(private_key)


def test_to_account(w3, key_object):
    account = to_account(w3, key_object)
    assert isinstance(account, eth_account.local.LocalAccount)


def test_to_account_type_error(w3):
    with pytest.raises(TypeError):
        to_account(w3, 1234567890)


@pytest.fixture(scope='session')
def fund_account(w3, private_key):
    # fund local account
    account = to_account(w3, private_key)
    tx_value = w3.toWei(10, 'ether')
    w3.eth.sendTransaction({
        'to': account.address,
        'from': w3.eth.accounts[0],
        'gas': 21000,
        'value': tx_value})
    assert w3.eth.getBalance(account.address) == tx_value


def test_signed_transaction_with_set_gas(w3, key_object, fund_account):
    account = to_account(w3, key_object)
    w3.middleware_stack.add(construct_sign_and_send_raw_middleware(key_object))
    start_balance = w3.eth.getBalance(account.address)
    w3.eth.sendTransaction({
        'to': w3.eth.accounts[0],
        'from': account.address,
        'gas': 21000,
        'gasPrice': 0,
        'value': 1})
    assert w3.eth.getBalance(account.address) <= start_balance - 1


def test_signed_transaction_unset_gas(w3, key_object, fund_account):
    account = to_account(w3, key_object)
    w3.middleware_stack.add(construct_sign_and_send_raw_middleware(key_object))
    start_balance = w3.eth.getBalance(account.address)
    w3.eth.sendTransaction({
        'to': w3.eth.accounts[0],
        'from': account.address,
        'value': 1})
    assert w3.eth.getBalance(account.address) <= start_balance - 1


def test_wrong_address_signed_transaction(w3, key_object):
    w3.middleware_stack.add(construct_sign_and_send_raw_middleware(key_object))
    with pytest.raises(ValueError):
        w3.eth.sendTransaction({
            'to': w3.eth.accounts[0],
            'from': w3.eth.accounts[1],
            'gas': 21000,
            'value': 10})


def test_invalid_address_signed_transaction(w3, key_object):
    w3.middleware_stack.add(construct_sign_and_send_raw_middleware(key_object))
    with pytest.raises(ValueError):
        w3.eth.sendTransaction({
            'to': w3.eth.accounts[0],
            'gas': 21000,
            'from': '!@#',
            'value': 10})


def test_missing_address_signed_transaction(w3, key_object):
    w3.middleware_stack.add(construct_sign_and_send_raw_middleware(key_object))
    with pytest.raises(ValueError):
        w3.eth.sendTransaction({
            'to': w3.eth.accounts[0],
            'gas': 21000,
            'value': 10})
