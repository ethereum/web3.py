import pytest

from eth_account import (
    Account,
)
from eth_account.signers.local import (
    LocalAccount,
)
import eth_keys
from eth_tester.exceptions import (
    ValidationError,
)
from eth_utils import (
    ValidationError as EthUtilsValidationError,
    is_hexstr,
    to_bytes,
    to_hex,
)
from eth_utils.toolz import (
    assoc,
    dissoc,
    identity,
    merge,
    valfilter,
)
from hexbytes import (
    HexBytes,
)
import pytest_asyncio

from web3 import (
    AsyncWeb3,
    Web3,
)
from web3.exceptions import (
    InvalidAddress,
)
from web3.middleware import (
    SignAndSendRawMiddlewareBuilder,
)
from web3.middleware.signing import (
    gen_normalized_accounts,
)
from web3.providers import (
    AsyncBaseProvider,
    BaseProvider,
)
from web3.providers.eth_tester import (
    AsyncEthereumTesterProvider,
    EthereumTesterProvider,
)

PRIVATE_KEY_1 = to_bytes(
    hexstr="0x6a8b4de52b288e111c14e1c4b868bc125d325d40331d86d875a3467dd44bf829"
)

ADDRESS_1 = "0x634743b15C948820069a43f6B361D03EfbBBE5a8"

PRIVATE_KEY_2 = to_bytes(
    hexstr="0xbf963e13b164c2100795f53e5590010f76b7a91b5a78de8e2b97239c8cfca8e8"
)

ADDRESS_2 = "0x91eD14b5956DBcc1310E65DC4d7E82f02B95BA46"

KEY_FUNCS = (
    eth_keys.keys.PrivateKey,
    Account.from_key,
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
    eth_keys.keys.PrivateKey(PRIVATE_KEY_1),
)

MIXED_KEY_SAME_TYPE = (
    eth_keys.keys.PrivateKey(PRIVATE_KEY_1),
    eth_keys.keys.PrivateKey(PRIVATE_KEY_2),
)


class DummyProvider(BaseProvider):
    def make_request(self, method, params):
        raise NotImplementedError(f"Cannot make request for {method}: {params}")


@pytest.fixture
def w3_dummy(request_mocker):
    w3_base = Web3(provider=DummyProvider(), middleware=[])
    with request_mocker(
        w3_base,
        mock_results={
            "eth_sendRawTransaction": lambda *args: args,
            "net_version": lambda *_: 1,
            "eth_chainId": lambda *_: "0x02",
        },
    ):
        yield w3_base


def hex_to_bytes(s):
    return to_bytes(hexstr=s)


TEST_SIGN_AND_SEND_RAW_MIDDLEWARE_PARAMS = (
    ("eth_sendTransaction", SAME_KEY_MIXED_TYPE, ADDRESS_2, NotImplementedError),
    (
        "eth_sendTransaction",
        SAME_KEY_MIXED_TYPE,
        ADDRESS_1,
        "eth_sendRawTransaction",
    ),
    (
        "eth_sendTransaction",
        MIXED_KEY_MIXED_TYPE,
        ADDRESS_2,
        "eth_sendRawTransaction",
    ),
    (
        "eth_sendTransaction",
        MIXED_KEY_MIXED_TYPE,
        ADDRESS_1,
        "eth_sendRawTransaction",
    ),
    ("eth_sendTransaction", SAME_KEY_SAME_TYPE, ADDRESS_2, NotImplementedError),
    (
        "eth_sendTransaction",
        SAME_KEY_SAME_TYPE,
        ADDRESS_1,
        "eth_sendRawTransaction",
    ),
    (
        "eth_sendTransaction",
        MIXED_KEY_SAME_TYPE,
        ADDRESS_2,
        "eth_sendRawTransaction",
    ),
    (
        "eth_sendTransaction",
        MIXED_KEY_SAME_TYPE,
        ADDRESS_1,
        "eth_sendRawTransaction",
    ),
    (
        "eth_sendTransaction",
        SAME_KEY_MIXED_TYPE[0],
        ADDRESS_1,
        "eth_sendRawTransaction",
    ),
    (
        "eth_sendTransaction",
        SAME_KEY_MIXED_TYPE[1],
        ADDRESS_1,
        "eth_sendRawTransaction",
    ),
    (
        "eth_sendTransaction",
        SAME_KEY_MIXED_TYPE[2],
        ADDRESS_1,
        "eth_sendRawTransaction",
    ),
    (
        "eth_sendTransaction",
        SAME_KEY_MIXED_TYPE[3],
        ADDRESS_1,
        "eth_sendRawTransaction",
    ),
    (
        "eth_sendTransaction",
        SAME_KEY_MIXED_TYPE[4],
        ADDRESS_1,
        "eth_sendRawTransaction",
    ),
    ("eth_sendTransaction", SAME_KEY_MIXED_TYPE[0], ADDRESS_2, NotImplementedError),
    ("eth_sendTransaction", SAME_KEY_MIXED_TYPE[1], ADDRESS_2, NotImplementedError),
    ("eth_sendTransaction", SAME_KEY_MIXED_TYPE[2], ADDRESS_2, NotImplementedError),
    ("eth_sendTransaction", SAME_KEY_MIXED_TYPE[3], ADDRESS_2, NotImplementedError),
    ("eth_sendTransaction", SAME_KEY_MIXED_TYPE[4], ADDRESS_2, NotImplementedError),
    ("eth_call", MIXED_KEY_MIXED_TYPE, ADDRESS_1, NotImplementedError),
    (
        "eth_sendTransaction",
        SAME_KEY_SAME_TYPE,
        hex_to_bytes(ADDRESS_1),
        "eth_sendRawTransaction",
    ),
)
TEST_SIGNED_TRANSACTION_PARAMS = (
    (
        {"gas": 21000, "gasPrice": 10**9, "value": 1},
        -1,
        MIXED_KEY_MIXED_TYPE,
        ADDRESS_1,
    ),
    (
        {"value": 1},
        -1,
        MIXED_KEY_MIXED_TYPE,
        ADDRESS_1,
    ),
    # expect validation error + unmanaged account
    (
        {"gas": 21000, "value": 10},
        ValidationError,
        SAME_KEY_MIXED_TYPE,
        ADDRESS_2,
    ),
    (
        {"gas": 21000, "value": 10},
        InvalidAddress,
        SAME_KEY_MIXED_TYPE,
        "0x0000",
    ),
    (
        {"gas": 21000, "gasPrice": 0, "value": 1},
        EthUtilsValidationError,
        MIXED_KEY_MIXED_TYPE,
        ADDRESS_1,
    ),
    (
        {
            "type": "0x2",
            "value": 22,
            "maxFeePerGas": 2000000000,
            "maxPriorityFeePerGas": 10**9,
        },
        -1,
        SAME_KEY_MIXED_TYPE,
        ADDRESS_1,
    ),
    (
        {
            "value": 22,
            "maxFeePerGas": 20**9,
            "maxPriorityFeePerGas": 10**9,
        },
        -1,
        SAME_KEY_MIXED_TYPE,
        ADDRESS_1,
    ),
)


@pytest.mark.parametrize(
    "method,key_object,from_,expected",
    TEST_SIGN_AND_SEND_RAW_MIDDLEWARE_PARAMS,
)
def test_sign_and_send_raw_middleware(w3_dummy, method, from_, expected, key_object):
    w3_dummy.middleware_onion.add(SignAndSendRawMiddlewareBuilder.build(key_object))

    legacy_transaction = {
        "to": "0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf",
        "from": from_,
        "gas": 21000,
        "gasPrice": 10**9,
        "value": 1,
        "nonce": 0,
    }
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            w3_dummy.manager.request_blocking(method, [legacy_transaction])
    else:
        # assert with legacy txn params
        actual = w3_dummy.manager.request_blocking(method, [legacy_transaction])
        assert_method_and_txn_signed(actual, expected)

        # assert with dynamic fee transaction params and explicit type
        dynamic_fee_transaction = dissoc(legacy_transaction, "gasPrice")
        dynamic_fee_transaction = assoc(
            dynamic_fee_transaction, "maxFeePerGas", 2000000000
        )
        dynamic_fee_transaction = assoc(
            dynamic_fee_transaction, "maxPriorityFeePerGas", 1000000000
        )
        dynamic_fee_transaction = assoc(dynamic_fee_transaction, "type", "0x2")

        actual_dynamic_fee_call = w3_dummy.manager.request_blocking(
            method, [dynamic_fee_transaction]
        )
        assert_method_and_txn_signed(actual_dynamic_fee_call, expected)

        # assert with dynamic fee transaction params and no explicit type
        dynamic_fee_transaction_no_type = dissoc(dynamic_fee_transaction, "type")

        actual_dynamic_fee_call_no_type = w3_dummy.manager.request_blocking(
            method, [dynamic_fee_transaction_no_type]
        )
        assert_method_and_txn_signed(actual_dynamic_fee_call_no_type, expected)


def assert_method_and_txn_signed(actual, expected):
    raw_txn = actual[1][0]
    actual_method = actual[0]
    assert actual_method == expected
    assert is_hexstr(raw_txn)


@pytest.fixture()
def w3():
    _w3 = Web3(EthereumTesterProvider())
    _w3.eth.default_account = _w3.eth.accounts[0]
    return _w3


@pytest.mark.parametrize(
    "key_object",
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
    ),
)
def test_gen_normalized_accounts(key_object):
    accounts = gen_normalized_accounts(key_object)
    assert all(isinstance(account, LocalAccount) for account in accounts.values())


def test_gen_normalized_accounts_type_error(w3):
    with pytest.raises(TypeError):
        gen_normalized_accounts(1234567890)


@pytest.fixture
def fund_account(w3):
    # fund local account
    tx_value = w3.to_wei(10, "ether")
    for address in (ADDRESS_1, ADDRESS_2):
        w3.eth.send_transaction(
            {
                "to": address,
                "from": w3.eth.default_account,
                "gas": 21000,
                "value": tx_value,
            }
        )
        assert w3.eth.get_balance(address) == tx_value


@pytest.mark.parametrize(
    "transaction,expected,key_object,from_",
    TEST_SIGNED_TRANSACTION_PARAMS,
    ids=[
        "with set gas",
        "with no set gas",
        "with mismatched sender",
        "with invalid sender",
        "with gasPrice lower than base fee",
        "with txn type and dynamic fee txn params",
        "with dynamic fee txn params and no type",
    ],
)
def test_signed_transaction(w3, fund_account, transaction, expected, key_object, from_):
    w3.middleware_onion.add(SignAndSendRawMiddlewareBuilder.build(key_object))

    # Drop any falsy addresses
    to_from = valfilter(bool, {"to": w3.eth.default_account, "from": from_})

    _transaction = merge(transaction, to_from)

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            w3.eth.send_transaction(_transaction)
    else:
        start_balance = w3.eth.get_balance(
            _transaction.get("from", w3.eth.default_account)
        )
        w3.eth.send_transaction(_transaction)
        assert w3.eth.get_balance(_transaction.get("from")) <= start_balance + expected


@pytest.mark.parametrize(
    "from_converter,to_converter",
    (
        (identity, identity),
        (hex_to_bytes, identity),
        (identity, hex_to_bytes),
        (hex_to_bytes, hex_to_bytes),
    ),
)
def test_sign_and_send_raw_middleware_with_byte_addresses(
    w3_dummy, from_converter, to_converter
):
    private_key = PRIVATE_KEY_1
    from_ = from_converter(ADDRESS_1)
    to_ = to_converter(ADDRESS_2)

    w3_dummy.middleware_onion.add(SignAndSendRawMiddlewareBuilder.build(private_key))

    actual = w3_dummy.manager.request_blocking(
        "eth_sendTransaction",
        [
            {
                "to": to_,
                "from": from_,
                "gas": 21000,
                "gasPrice": 0,
                "value": 1,
                "nonce": 0,
            }
        ],
    )
    raw_txn = actual[1][0]
    actual_method = actual[0]
    assert actual_method == "eth_sendRawTransaction"
    assert is_hexstr(raw_txn)


# -- async -- #


class AsyncDummyProvider(AsyncBaseProvider):
    async def coro_request(self, method, params):
        raise NotImplementedError(f"Cannot make request for {method}:{params}")


@pytest_asyncio.fixture
async def async_w3_dummy(request_mocker):
    w3_base = AsyncWeb3(provider=AsyncDummyProvider(), middleware=[])
    async with request_mocker(
        w3_base,
        mock_results={
            "eth_sendRawTransaction": lambda *args: args,
            "net_version": 1,
            "eth_chainId": "0x02",
        },
    ):
        yield w3_base


@pytest_asyncio.fixture
async def async_w3():
    _async_w3 = AsyncWeb3(AsyncEthereumTesterProvider())
    accounts = await _async_w3.eth.accounts
    _async_w3.eth.default_account = accounts[0]
    return _async_w3


@pytest_asyncio.fixture
async def async_fund_account(async_w3):
    # fund local account
    tx_value = async_w3.to_wei(10, "ether")
    for address in (ADDRESS_1, ADDRESS_2):
        await async_w3.eth.send_transaction(
            {
                "to": address,
                "from": async_w3.eth.default_account,
                "gas": 21000,
                "value": tx_value,
            }
        )
        acct_bal = await async_w3.eth.get_balance(address)
        assert acct_bal == tx_value


@pytest.mark.parametrize(
    "method,key_object,from_,expected",
    TEST_SIGN_AND_SEND_RAW_MIDDLEWARE_PARAMS,
)
@pytest.mark.asyncio
async def test_async_sign_and_send_raw_middleware(
    async_w3_dummy,
    method,
    from_,
    expected,
    key_object,
):
    async_w3_dummy.middleware_onion.add(
        SignAndSendRawMiddlewareBuilder.build(key_object)
    )

    legacy_transaction = {
        "to": "0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf",
        "from": from_,
        "gas": 21000,
        "gasPrice": 10**9,
        "value": 1,
        "nonce": 0,
    }
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            await async_w3_dummy.manager.coro_request(
                method,
                [legacy_transaction],
            )
    else:
        # assert with legacy txn params
        actual = await async_w3_dummy.manager.coro_request(
            method,
            [legacy_transaction],
        )
        assert_method_and_txn_signed(actual, expected)

        # assert with dynamic fee transaction params and explicit type
        dynamic_fee_transaction = dissoc(legacy_transaction, "gasPrice")
        dynamic_fee_transaction = assoc(
            dynamic_fee_transaction, "maxFeePerGas", 2000000000
        )
        dynamic_fee_transaction = assoc(
            dynamic_fee_transaction, "maxPriorityFeePerGas", 1000000000
        )
        dynamic_fee_transaction = assoc(dynamic_fee_transaction, "type", "0x2")

        actual_dynamic_fee_call = await async_w3_dummy.manager.coro_request(
            method, [dynamic_fee_transaction]
        )
        assert_method_and_txn_signed(actual_dynamic_fee_call, expected)

        # assert with dynamic fee transaction params and no explicit type
        dynamic_fee_transaction_no_type = dissoc(dynamic_fee_transaction, "type")

        actual_dynamic_fee_call_no_type = await async_w3_dummy.manager.coro_request(
            method, [dynamic_fee_transaction_no_type]
        )
        assert_method_and_txn_signed(actual_dynamic_fee_call_no_type, expected)


@pytest.mark.parametrize(
    "transaction,expected,key_object,from_",
    TEST_SIGNED_TRANSACTION_PARAMS,
    ids=[
        "with set gas",
        "with no set gas",
        "with mismatched sender",
        "with invalid sender",
        "with gasPrice lower than base fee",
        "with txn type and dynamic fee txn params",
        "with dynamic fee txn params and no type",
    ],
)
@pytest.mark.asyncio
async def test_async_signed_transaction(
    async_w3,
    async_fund_account,
    transaction,
    expected,
    key_object,
    from_,
):
    async_w3.middleware_onion.add(SignAndSendRawMiddlewareBuilder.build(key_object))

    # Drop any falsy addresses
    to_from = valfilter(bool, {"to": async_w3.eth.default_account, "from": from_})

    _transaction = merge(transaction, to_from)

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            await async_w3.eth.send_transaction(_transaction)
    else:
        start_balance = await async_w3.eth.get_balance(
            _transaction.get("from", async_w3.eth.default_account)
        )
        await async_w3.eth.send_transaction(_transaction)
        assert (
            await async_w3.eth.get_balance(_transaction.get("from"))
            <= start_balance + expected
        )


@pytest.mark.parametrize(
    "from_converter,to_converter",
    (
        (identity, identity),
        (hex_to_bytes, identity),
        (identity, hex_to_bytes),
        (hex_to_bytes, hex_to_bytes),
    ),
)
@pytest.mark.asyncio
async def test_async_sign_and_send_raw_middleware_with_byte_addresses(
    async_w3_dummy, from_converter, to_converter
):
    private_key = PRIVATE_KEY_1
    from_ = from_converter(ADDRESS_1)
    to_ = to_converter(ADDRESS_2)

    async_w3_dummy.middleware_onion.add(
        SignAndSendRawMiddlewareBuilder.build(private_key)
    )

    actual = await async_w3_dummy.manager.coro_request(
        "eth_sendTransaction",
        [
            {
                "to": to_,
                "from": from_,
                "gas": 21000,
                "gasPrice": 0,
                "value": 1,
                "nonce": 0,
            }
        ],
    )
    raw_txn = actual[1][0]
    actual_method = actual[0]
    assert actual_method == "eth_sendRawTransaction"
    assert is_hexstr(raw_txn)
