import pytest
from eth_keys import keys

from eth_utils import (
    is_dict,
)
import web3
from web3 import Web3, EthereumTesterProvider
# from web3.utils.encoding import to_bytes, to_hex
from web3.middleware import (
    construct_transaction_signing_middleware,
)

bytes_private_key = b'\x01' * 32
hex_str_private_key = '0xd65215905d39210e8c1aba8449d0ed3a95f2bd4b8d5f1f253135986a247d3aec'


@pytest.fixture(scope='module')
def w3():
    # Might want to use EthereumTesterProvider instead
    instance = Web3(EthereumTesterProvider())
    return instance


@pytest.fixture(params=[0, ])
def testrpc_account(request, w3):
    testrpc_acct = w3.eth.accounts[request.param]

    trpc = dict(address=testrpc_acct
                )

    return trpc


@pytest.fixture(params=[bytes_private_key], ids=['bytes_pk_1'])
def eth_key_account(request):
    eth_key_acct = keys.PrivateKey(bytes_private_key)
    ek = dict(private_key=eth_key_acct,
              public_key=eth_key_acct.public_key,
              address=eth_key_acct.public_key.to_address()
              )

    return ek


@pytest.fixture(params=[bytes_private_key], ids=['bytes_pk_1'])
def web3_account(request, w3):
    web3_acct = w3.eth.account.create(request.param)
    w3a = dict(private_key=web3_acct.privateKey,
               public_key='',
               address=web3_acct.address
               )

    return w3a


@pytest.fixture()
def eth_key_account_transaction(eth_key_account, w3):
    tx = {'from': eth_key_account['address'], 'to': w3.eth.accounts[0], 'value': 123}

    return tx


@pytest.fixture()
def web3_account_transaction(web3_acccount, w3):
    tx = {'from': web3_acccount['address'], 'to': w3.eth.accounts[0], 'value': 123}

    return tx


@pytest.fixture(params=['web3_account', 'eth_key_account'])
def private_key(request, web3_account, eth_key_account):
    if request.param == 'web3_account':
        return web3_account['private_key']
    if request.param == 'eth_key_account':
        return eth_key_account['private_key']


def _make_request(method, params):
    return {'result': 'default'}


# I wish fixtures could be passed as params :(
# https://github.com/pytest-dev/pytest/issues/349
@pytest.mark.parametrize(
    'method,params,expected',
    (
        ('eth_mining', [], 'default'),
        ('eth_sendTransaction', [], 'transaction'),
    )
)
def test_transaction_signing_middleware(method, params, expected, w3, private_key, testrpc_account, web3_account, eth_key_account):
    local_to_web3_tx = {'from': web3_account['address'], 'to': testrpc_account['address'], 'value': 123}
    local_to_eth_key_tx = {'from': eth_key_account['address'], 'to': testrpc_account['address'], 'value': 123}

    middleware = construct_transaction_signing_middleware(private_key)(_make_request, w3)
    # import pdb; pdb.set_trace()

    # actual = middleware(method, params)
    # assert is_dict(actual)
    # assert 'result' in actual
    # assert actual['result'] == expected
