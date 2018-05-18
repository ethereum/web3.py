import pytest

import eth_account
import eth_keys
from eth_utils import (
    to_bytes,
    to_hex,
)
from hexbytes import (
    HexBytes,
)

from web3 import Web3
from web3.exceptions import (
    InvalidAddress,
)
from web3.middleware import (
    construct_result_generator_middleware,
    construct_sign_and_send_raw_middleware,
)
from web3.middleware.signing import (
    gen_normalized_accounts,
)
from web3.providers import (
    BaseProvider,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)
from web3.utils.toolz import (
    identity,
    merge,
    valfilter,
)

PRIVATE_KEY_1 = to_bytes(
    hexstr='0x6a8b4de52b288e111c14e1c4b868bc125d325d40331d86d875a3467dd44bf829')

ADDRESS_1 = '0x634743b15C948820069a43f6B361D03EfbBBE5a8'

PRIVATE_KEY_2 = to_bytes(
    hexstr='0xbf963e13b164c2100795f53e5590010f76b7a91b5a78de8e2b97239c8cfca8e8')

ADDRESS_2 = '0x91eD14b5956DBcc1310E65DC4d7E82f02B95BA46'

KEY_FUNCS = (
    eth_keys.keys.PrivateKey,
    eth_account.Account.privateKeyToAccount,
    HexBytes,
    to_hex,
    identity,
)


SAME_KEY_MIXED_TYPE = tuple(key_func(PRIVATE_KEY_1) for key_func in KEY_FUNCS)

MIXED_KEY_MIXED_TYPE = tuple(
    key_func(key) for key in [PRIVATE_KEY_1, PRIVATE_KEY_2] for key_func in KEY_FUNCS
)

SAME_KEY_SAME_TYPE = (
    eth_keys.keys.PrivateKey(PRIVATE_KEY_1),
    eth_keys.keys.PrivateKey(PRIVATE_KEY_1)
)

MIXED_KEY_SAME_TYPE = (
    eth_keys.keys.PrivateKey(PRIVATE_KEY_1), eth_keys.keys.PrivateKey(PRIVATE_KEY_2)
)


class DummyProvider(BaseProvider):
    def make_request(self, method, params):
        raise NotImplementedError("Cannot make request for {0}:{1}".format(
            method,
            params,
        ))


@pytest.fixture()
def result_generator_middleware():
    return construct_result_generator_middleware({
        'eth_sendRawTransaction': lambda *args: args,
        'net_version': lambda *_: 1,
    })


@pytest.fixture()
def w3_base():
    return Web3(providers=[DummyProvider()], middlewares=[])


@pytest.fixture()
def w3_dummy(w3_base, result_generator_middleware):
    w3_base.middleware_stack.add(result_generator_middleware)
    return w3_base


@pytest.mark.parametrize(
    'method,key_object,from_,expected',
    (
        ('eth_sendTransaction', SAME_KEY_MIXED_TYPE, ADDRESS_2, NotImplementedError),
        ('eth_sendTransaction', SAME_KEY_MIXED_TYPE, ADDRESS_1, 'eth_sendRawTransaction'),
        ('eth_sendTransaction', MIXED_KEY_MIXED_TYPE, ADDRESS_2, 'eth_sendRawTransaction'),
        ('eth_sendTransaction', MIXED_KEY_MIXED_TYPE, ADDRESS_1, 'eth_sendRawTransaction'),
        ('eth_sendTransaction', SAME_KEY_SAME_TYPE, ADDRESS_2, NotImplementedError),
        ('eth_sendTransaction', SAME_KEY_SAME_TYPE, ADDRESS_1, 'eth_sendRawTransaction'),
        ('eth_sendTransaction', MIXED_KEY_SAME_TYPE, ADDRESS_2, 'eth_sendRawTransaction'),
        ('eth_sendTransaction', MIXED_KEY_SAME_TYPE, ADDRESS_1, 'eth_sendRawTransaction'),
        ('eth_sendTransaction', SAME_KEY_MIXED_TYPE[0], ADDRESS_1, 'eth_sendRawTransaction'),
        ('eth_sendTransaction', SAME_KEY_MIXED_TYPE[1], ADDRESS_1, 'eth_sendRawTransaction'),
        ('eth_sendTransaction', SAME_KEY_MIXED_TYPE[2], ADDRESS_1, 'eth_sendRawTransaction'),
        ('eth_sendTransaction', SAME_KEY_MIXED_TYPE[3], ADDRESS_1, 'eth_sendRawTransaction'),
        ('eth_sendTransaction', SAME_KEY_MIXED_TYPE[4], ADDRESS_1, 'eth_sendRawTransaction'),
        ('eth_sendTransaction', SAME_KEY_MIXED_TYPE[0], ADDRESS_2, NotImplementedError),
        ('eth_sendTransaction', SAME_KEY_MIXED_TYPE[1], ADDRESS_2, NotImplementedError),
        ('eth_sendTransaction', SAME_KEY_MIXED_TYPE[2], ADDRESS_2, NotImplementedError),
        ('eth_sendTransaction', SAME_KEY_MIXED_TYPE[3], ADDRESS_2, NotImplementedError),
        ('eth_sendTransaction', SAME_KEY_MIXED_TYPE[4], ADDRESS_2, NotImplementedError),
        ('eth_call', MIXED_KEY_MIXED_TYPE, ADDRESS_1, NotImplementedError),
    )
)
def test_sign_and_send_raw_middleware(
        w3_dummy,
        w3,
        method,
        from_,
        expected,
        key_object):
    w3_dummy.middleware_stack.add(
        construct_sign_and_send_raw_middleware(key_object))

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            w3_dummy.manager.request_blocking(
                method,
                [{
                    'to': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
                    'from': from_,
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
                'from': from_,
                'gas': 21000,
                'gasPrice': 0,
                'value': 1,
                'nonce': 0
            }])
        raw_txn = actual[1][0]
        actual_method = actual[0]
        assert actual_method == expected
        assert isinstance(raw_txn, bytes)


@pytest.fixture()
def w3():
    return Web3(EthereumTesterProvider())


@pytest.mark.parametrize(
    'key_object',
    (
        (SAME_KEY_MIXED_TYPE),
        (MIXED_KEY_MIXED_TYPE),
        (SAME_KEY_SAME_TYPE),
        (MIXED_KEY_SAME_TYPE),
        (SAME_KEY_MIXED_TYPE[0]),
        (SAME_KEY_MIXED_TYPE[1]),
        (SAME_KEY_MIXED_TYPE[2]),
        (SAME_KEY_MIXED_TYPE[3]),
        (SAME_KEY_MIXED_TYPE[4]),
    )
)
def test_gen_normalized_accounts(key_object):
    accounts = gen_normalized_accounts(key_object)
    assert all(isinstance(account, eth_account.local.LocalAccount) for account in accounts.values())


def test_gen_normalized_accounts_type_error(w3):
    with pytest.raises(TypeError):
        gen_normalized_accounts(1234567890)


@pytest.fixture()
def fund_account(w3):
    # fund local account
    tx_value = w3.toWei(10, 'ether')
    for address in (ADDRESS_1, ADDRESS_2):
        w3.eth.sendTransaction({
            'to': address,
            'from': w3.eth.accounts[0],
            'gas': 21000,
            'value': tx_value})
        assert w3.eth.getBalance(address) == tx_value


@pytest.mark.parametrize(
    'transaction,expected,key_object,from_',
    (
        (
            #  Transaction with set gas
            {
                'gas': 21000,
                'gasPrice': 0,
                'value': 1
            },
            -1,
            MIXED_KEY_MIXED_TYPE,
            ADDRESS_1,
        ),
        (
            #  Transaction with no set gas
            {
                'value': 1
            },
            -1,
            MIXED_KEY_MIXED_TYPE,
            ADDRESS_1,
        ),
        (
            # Transaction with mismatched sender
            # expect a key error with sendTransaction + unmanaged account
            {
                'gas': 21000,
                'value': 10
            },
            KeyError,
            SAME_KEY_MIXED_TYPE,
            ADDRESS_2,
        ),
        (
            #  Transaction with invalid sender
            {
                'gas': 21000,
                'value': 10
            },
            InvalidAddress,
            SAME_KEY_MIXED_TYPE,
            '0x0000',
        )
    )
)
def test_signed_transaction(
        w3,
        fund_account,
        transaction,
        expected,
        key_object,
        from_):
    w3.middleware_stack.add(construct_sign_and_send_raw_middleware(key_object))

    # Drop any falsy addresses
    to_from = valfilter(bool, {'to': w3.eth.accounts[0], 'from': from_})

    _transaction = merge(transaction, to_from)

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            start_balance = w3.eth.getBalance(_transaction.get('from', w3.eth.accounts[0]))
            w3.eth.sendTransaction(_transaction)
    else:
        start_balance = w3.eth.getBalance(_transaction.get('from', w3.eth.accounts[0]))
        w3.eth.sendTransaction(_transaction)
        assert w3.eth.getBalance(_transaction.get('from')) <= start_balance + expected
