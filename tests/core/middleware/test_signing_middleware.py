import pytest
from eth_keys import keys
from web3 import (
    Web3,
    EthereumTesterProvider,
    # TestRPCProvider
)
# from web3.utils.encoding import to_bytes, to_hex
from web3.middleware import (
    construct_transaction_signing_middleware,
)

bytes_private_key = b'\x01' * 32
hex_str_private_key = '0xd65215905d39210e8c1aba8449d0ed3a95f2bd4b8d5f1f253135986a247d3aec'


@pytest.fixture(scope='module', params=[
                                        # TestRPCProvider,
                                        EthereumTesterProvider,
                                        ])
def w3(request):
    instance = Web3(request.param())
    return instance


@pytest.fixture(scope='module', params=[0, ])
def testrpc_account(request, w3):
    testrpc_acct = w3.eth.accounts[request.param]

    trpc = dict(address=testrpc_acct
                )

    return trpc


@pytest.fixture(params=[bytes_private_key], ids=['bytes_pk_1'])
def web3_local_account(request, w3):
    web3_acct = w3.eth.account.create(request.param)
    w3a = dict(private_key=web3_acct.privateKey,
               public_key='',
               address=web3_acct.address
               )

    return w3a


@pytest.fixture(params=[bytes_private_key], ids=['bytes_pk_1'])
def eth_key_local_account(request):
    eth_key_acct = keys.PrivateKey(request.param)
    ek = dict(private_key=eth_key_acct.to_hex(),
              public_key=eth_key_acct.public_key,
              address=eth_key_acct.public_key.to_address()
              )

    return ek


@pytest.fixture()
def web3_account_transaction(web3_acccount, w3):
    """ Not used """
    tx = {'from': web3_acccount['address'], 'to': w3.eth.accounts[0], 'value': 123}

    return tx


@pytest.fixture()
def eth_key_account_transaction(eth_key_account, w3):
    """ Not used """
    tx = {'from': eth_key_account['address'], 'to': w3.eth.accounts[0], 'value': 123}

    return tx


@pytest.fixture(params=['web3_account', 'eth_key_account'])
def private_key(request, web3_account, eth_key_account):
    """ Not used """
    if request.param == 'web3_account':
        return web3_account['private_key']
    if request.param == 'eth_key_account':
        return eth_key_account['private_key']


def _make_request(method, params):
    return {'method': method, 'params': params}


# I wish fixtures could be passed as params :(
# https://github.com/pytest-dev/pytest/issues/349
@pytest.mark.web3
@pytest.mark.parametrize(
    'method,params,expected',
    (
        # ('eth_mining', [], 'default'),
        ('eth_sendTransaction', [], 'transaction'),
    )
)
def test_web3_local(method, params, expected, w3, testrpc_account, web3_local_account):
    tx = {'from': web3_local_account['address'], 'to': testrpc_account['address'], 'value': 123}

    middleware = construct_transaction_signing_middleware(
        web3_local_account['private_key'])(_make_request, w3)
    actual = middleware(method=method, params=[tx])

    assert actual['method'] == 'eth_sendRawTransaction'


@pytest.mark.ethkey
@pytest.mark.parametrize(
    'method,params,expected',
    (
        # ('eth_mining', [], 'default'),
        ('eth_sendTransaction', [], 'transaction'),
    )
)
def test_eth_key_local(method, params, expected, w3, testrpc_account, eth_key_local_account):
    tx = {'from': eth_key_local_account['address'], 'to': testrpc_account['address'], 'value': 123}

    middleware = construct_transaction_signing_middleware(
        eth_key_local_account['private_key'])(_make_request, w3)
    actual = middleware(method=method, params=[tx])

    assert actual['method'] == 'eth_sendRawTransaction'

# TODO:  text bytes, hex_str
# TODO:  test case where account addresses don't match
# TODO:  test case where method is not eth_sendTransaction
