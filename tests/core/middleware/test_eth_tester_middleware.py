import pytest
from unittest.mock import (
    Mock,
)

from web3.providers.eth_tester.middleware import (
    default_transaction_fields_middleware,
)
from web3.types import (
    BlockData,
)

SAMPLE_ADDRESS_LIST = [
    "0x0000000000000000000000000000000000000001",
    "0x0000000000000000000000000000000000000002",
    "0x0000000000000000000000000000000000000003",
]
SAMPLE_ADDRESS = "0x0000000000000000000000000000000000000004"


@pytest.mark.parametrize("block_number", {0, "0x0", "earliest"})
def test_get_transaction_count_formatters(w3, block_number):
    tx_counts = w3.eth.get_transaction_count(w3.eth.accounts[-1], block_number)
    assert tx_counts == 0


def test_get_block_formatters(w3):
    all_block_keys = BlockData.__annotations__.keys()
    all_non_poa_block_keys = {k for k in all_block_keys if k != "proofOfAuthorityData"}

    latest_block = w3.eth.get_block("latest")
    latest_block_keys = set(latest_block.keys())
    assert all_non_poa_block_keys == latest_block_keys


@pytest.mark.parametrize(
    "w3_accounts, method, from_field_added, from_field_value",
    (
        (SAMPLE_ADDRESS_LIST, "eth_gasPrice", False, None),
        (SAMPLE_ADDRESS_LIST, "eth_blockNumber", False, None),
        (SAMPLE_ADDRESS_LIST, "meow", False, None),
        (SAMPLE_ADDRESS_LIST, "eth_call", True, SAMPLE_ADDRESS_LIST[0]),
        (SAMPLE_ADDRESS_LIST, "eth_estimateGas", True, SAMPLE_ADDRESS_LIST[0]),
        (
            SAMPLE_ADDRESS_LIST,
            "eth_sendTransaction",
            True,
            SAMPLE_ADDRESS_LIST[0],
        ),
        (SAMPLE_ADDRESS_LIST, "eth_gasPrice", False, None),
        (SAMPLE_ADDRESS_LIST, "eth_blockNumber", False, None),
        (SAMPLE_ADDRESS_LIST, "meow", False, None),
    ),
)
def test_default_transaction_fields_middleware(
    w3_accounts, method, from_field_added, from_field_value
):
    def mock_request(_method, params):
        return params

    mock_w3 = Mock()
    mock_w3.eth.accounts = w3_accounts

    middleware = default_transaction_fields_middleware(mock_w3)
    base_params = {"chainId": 5}
    inner = middleware.wrap_make_request(mock_request)
    filled_transaction = inner(method, [base_params])

    filled_params = filled_transaction[0]

    assert ("from" in filled_params.keys()) == from_field_added
    if "from" in filled_params.keys():
        assert filled_params["from"] == from_field_value

    filled_transaction[0].pop("from", None)
    assert filled_transaction[0] == base_params


# -- async -- #


@pytest.mark.parametrize(
    "w3_accounts, method, from_field_added, from_field_value",
    (
        (SAMPLE_ADDRESS_LIST, "eth_gasPrice", False, None),
        (SAMPLE_ADDRESS_LIST, "eth_blockNumber", False, None),
        (SAMPLE_ADDRESS_LIST, "meow", False, None),
        (SAMPLE_ADDRESS_LIST, "eth_call", True, SAMPLE_ADDRESS_LIST[0]),
        (SAMPLE_ADDRESS_LIST, "eth_estimateGas", True, SAMPLE_ADDRESS_LIST[0]),
        (
            SAMPLE_ADDRESS_LIST,
            "eth_sendTransaction",
            True,
            SAMPLE_ADDRESS_LIST[0],
        ),
        (SAMPLE_ADDRESS_LIST, "eth_gasPrice", False, None),
        (SAMPLE_ADDRESS_LIST, "eth_blockNumber", False, None),
        (SAMPLE_ADDRESS_LIST, "meow", False, None),
    ),
)
@pytest.mark.asyncio
async def test_async_default_transaction_fields_middleware(
    w3_accounts,
    method,
    from_field_added,
    from_field_value,
):
    async def mock_request(_method, params):
        return params

    async def mock_async_accounts():
        return w3_accounts

    mock_w3 = Mock()
    mock_w3.eth.accounts = mock_async_accounts()

    middleware = default_transaction_fields_middleware(mock_w3)
    base_params = {"chainId": 5}
    inner = await middleware.async_wrap_make_request(mock_request)
    filled_transaction = await inner(method, [base_params])

    filled_params = filled_transaction[0]
    assert ("from" in filled_params.keys()) == from_field_added
    if "from" in filled_params.keys():
        assert filled_params["from"] == from_field_value

    filled_transaction[0].pop("from", None)
    assert filled_transaction[0] == base_params

    # clean up
    mock_w3.eth.accounts.close()
