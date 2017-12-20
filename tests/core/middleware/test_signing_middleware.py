import pytest
from eth_keys import keys

from eth_utils import (
    is_dict,
)
import web3
from web3 import Web3, HTTPProvider, TestRPCProvider
from web3.utils.encoding import to_bytes, to_hex
from web3.middleware import (
    construct_transaction_signing_middleware,
)

w3 = Web3(TestRPCProvider())

bytes_private_key = b'\x01' * 32
hex_str_private_key = '0xd65215905d39210e8c1aba8449d0ed3a95f2bd4b8d5f1f253135986a247d3aec'

# eth_keys method
eth_private_key = keys.PrivateKey(bytes_private_key)
eth_public_key = eth_private_key.public_key  # API is a little wonky
eth_address = eth_public_key.to_address()

# web3 account method
web3_acct = w3.eth.account.create(bytes_private_key)
web3_private_key = web3_acct.privateKey
web3_public_key = '?'
web3_address = web3_acct.address

transaction_1 = {'from': eth_address, 'to': w3.eth.accounts[0], 'value': 123}
transaction_2 = {'from': web3_address, 'to': w3.eth.accounts[0], 'value': 123}


@pytest.fixture(params=[transaction_1,
                        transaction_2,
                        ])
def transaction(request):
    return request.param


PRIVATE_KEYS = {
    'eth': eth_private_key,
    'web3': web3_private_key,
}


def _make_request(method, params):
    return {'result': 'default'}


@pytest.mark.parametrize(
    'method,params,expected',
    (
        ('eth_mining', [], 'default'),
        ('eth_sendTransaction', [], 'transaction'),
    )
)
def test_transaction_signing_middleware(method, params, expected):
    middleware = construct_transaction_signing_middleware(FIXTURES)(_make_request, None)

    actual = middleware(method, params)
    assert is_dict(actual)
    assert 'result' in actual
    assert actual['result'] == expected
