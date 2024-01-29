import pytest

from web3 import (
    AsyncWeb3,
    EthereumTesterProvider,
    Web3,
)
from web3.datastructures import (
    AttributeDict,
)
from web3.middleware import (
    AttributeDictMiddleware,
)
from web3.providers.eth_tester import (
    AsyncEthereumTesterProvider,
)

GENERATED_NESTED_DICT_RESULT = {
    "a": 1,
    "b": {
        "b1": 1,
        "b2": {"b2a": 1, "b2b": {"b2b1": 1, "b2b2": {"test": "fin"}}},
    },
}


def _assert_dict_and_not_attrdict(value):
    assert not isinstance(value, AttributeDict)
    assert isinstance(value, dict)


def test_attrdict_middleware_default_for_ethereum_tester_provider():
    w3 = Web3(EthereumTesterProvider())
    assert w3.middleware_onion.get("attrdict") == AttributeDictMiddleware


def test_attrdict_middleware_is_recursive(w3, request_mocker):
    with request_mocker(
        w3,
        mock_results={"fake_endpoint": GENERATED_NESTED_DICT_RESULT},
    ):
        result = w3.manager.request_blocking("fake_endpoint", [])

    assert isinstance(result, AttributeDict)

    assert isinstance(result["b"], AttributeDict)
    assert result.b == result["b"]
    assert isinstance(result.b["b2"], AttributeDict)
    assert result.b.b2 == result.b["b2"]
    assert isinstance(result.b.b2["b2b"], AttributeDict)
    assert result.b.b2.b2b == result.b.b2["b2b"]
    assert isinstance(result.b.b2.b2b["b2b2"], AttributeDict)
    assert result.b.b2.b2b.b2b2 == result.b.b2.b2b["b2b2"]


def test_no_attrdict_middleware_does_not_convert_dicts_to_attrdict(request_mocker):
    w3 = Web3(EthereumTesterProvider())
    # remove attrdict middleware
    w3.middleware_onion.remove("attrdict")

    with request_mocker(
        w3,
        mock_results={"fake_endpoint": GENERATED_NESTED_DICT_RESULT},
    ):
        result = w3.manager.request_blocking("fake_endpoint", [])

    _assert_dict_and_not_attrdict(result)
    _assert_dict_and_not_attrdict(result["b"])
    _assert_dict_and_not_attrdict(result["b"]["b2"])
    _assert_dict_and_not_attrdict(result["b"]["b2"]["b2b"])
    _assert_dict_and_not_attrdict(result["b"]["b2"]["b2b"]["b2b2"])


# --- async --- #


@pytest.mark.asyncio
async def test_async_attrdict_middleware_default_for_async_eth_tester_provider():
    async_w3 = AsyncWeb3(AsyncEthereumTesterProvider())
    assert async_w3.middleware_onion.get("attrdict") == AttributeDictMiddleware


@pytest.mark.asyncio
async def test_async_attrdict_middleware_is_recursive(async_w3, request_mocker):
    async with request_mocker(
        async_w3,
        mock_results={"fake_endpoint": GENERATED_NESTED_DICT_RESULT},
    ):
        result = await async_w3.manager.coro_request("fake_endpoint", [])

    assert isinstance(result, AttributeDict)

    assert isinstance(result["b"], AttributeDict)
    assert result.b == result["b"]
    assert isinstance(result.b["b2"], AttributeDict)
    assert result.b.b2 == result.b["b2"]
    assert isinstance(result.b.b2["b2b"], AttributeDict)
    assert result.b.b2.b2b == result.b.b2["b2b"]
    assert isinstance(result.b.b2.b2b["b2b2"], AttributeDict)
    assert result.b.b2.b2b.b2b2 == result.b.b2.b2b["b2b2"]


@pytest.mark.asyncio
async def test_no_async_attrdict_middleware_does_not_convert_dicts_to_attrdict(
    request_mocker,
):
    async_w3 = AsyncWeb3(AsyncEthereumTesterProvider())

    # remove attrdict middleware
    async_w3.middleware_onion.remove("attrdict")

    async with request_mocker(
        async_w3,
        mock_results={"fake_endpoint": GENERATED_NESTED_DICT_RESULT},
    ):
        result = await async_w3.manager.coro_request("fake_endpoint", [])

    _assert_dict_and_not_attrdict(result)
    _assert_dict_and_not_attrdict(result["b"])
    _assert_dict_and_not_attrdict(result["b"]["b2"])
    _assert_dict_and_not_attrdict(result["b"]["b2"]["b2b"])
    _assert_dict_and_not_attrdict(result["b"]["b2"]["b2b"]["b2b2"])
