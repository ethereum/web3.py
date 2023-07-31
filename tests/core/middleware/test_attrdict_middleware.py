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
    async_attrdict_middleware,
    async_construct_result_generator_middleware,
    attrdict_middleware,
    construct_result_generator_middleware,
)
from web3.providers.eth_tester import (
    AsyncEthereumTesterProvider,
)
from web3.types import (
    RPCEndpoint,
)

GENERATED_NESTED_DICT_RESULT = {
    "result": {
        "a": 1,
        "b": {
            "b1": 1,
            "b2": {"b2a": 1, "b2b": {"b2b1": 1, "b2b2": {"test": "fin"}}},
        },
    }
}


def _assert_dict_and_not_attrdict(value):
    assert not isinstance(value, AttributeDict)
    assert isinstance(value, dict)


def test_attrdict_middleware_default_for_ethereum_tester_provider():
    w3 = Web3(EthereumTesterProvider())
    assert w3.middleware_onion.get("attrdict") == attrdict_middleware


def test_attrdict_middleware_is_recursive(w3):
    w3.middleware_onion.inject(
        construct_result_generator_middleware(
            {RPCEndpoint("fake_endpoint"): lambda *_: GENERATED_NESTED_DICT_RESULT}
        ),
        "result_gen",
        layer=0,
    )
    response = w3.manager.request_blocking("fake_endpoint", [])

    result = response["result"]
    assert isinstance(result, AttributeDict)
    assert response.result == result

    assert isinstance(result["b"], AttributeDict)
    assert result.b == result["b"]
    assert isinstance(result.b["b2"], AttributeDict)
    assert result.b.b2 == result.b["b2"]
    assert isinstance(result.b.b2["b2b"], AttributeDict)
    assert result.b.b2.b2b == result.b.b2["b2b"]
    assert isinstance(result.b.b2.b2b["b2b2"], AttributeDict)
    assert result.b.b2.b2b.b2b2 == result.b.b2.b2b["b2b2"]

    # cleanup
    w3.middleware_onion.remove("result_gen")


def test_no_attrdict_middleware_does_not_convert_dicts_to_attrdict():
    w3 = Web3(EthereumTesterProvider())

    w3.middleware_onion.inject(
        construct_result_generator_middleware(
            {RPCEndpoint("fake_endpoint"): lambda *_: GENERATED_NESTED_DICT_RESULT}
        ),
        "result_gen",
        layer=0,
    )

    # remove attrdict middleware
    w3.middleware_onion.remove("attrdict")

    response = w3.manager.request_blocking("fake_endpoint", [])

    result = response["result"]

    _assert_dict_and_not_attrdict(result)
    _assert_dict_and_not_attrdict(result["b"])
    _assert_dict_and_not_attrdict(result["b"]["b2"])
    _assert_dict_and_not_attrdict(result["b"]["b2"]["b2b"])
    _assert_dict_and_not_attrdict(result["b"]["b2"]["b2b"]["b2b2"])


# --- async --- #


@pytest.mark.asyncio
async def test_async_attrdict_middleware_default_for_async_ethereum_tester_provider():
    async_w3 = AsyncWeb3(AsyncEthereumTesterProvider())
    assert async_w3.middleware_onion.get("attrdict") == async_attrdict_middleware


@pytest.mark.asyncio
async def test_async_attrdict_middleware_is_recursive(async_w3):
    async_w3.middleware_onion.inject(
        await async_construct_result_generator_middleware(
            {RPCEndpoint("fake_endpoint"): lambda *_: GENERATED_NESTED_DICT_RESULT}
        ),
        "result_gen",
        layer=0,
    )
    response = await async_w3.manager.coro_request("fake_endpoint", [])

    result = response["result"]
    assert isinstance(result, AttributeDict)
    assert response.result == result

    assert isinstance(result["b"], AttributeDict)
    assert result.b == result["b"]
    assert isinstance(result.b["b2"], AttributeDict)
    assert result.b.b2 == result.b["b2"]
    assert isinstance(result.b.b2["b2b"], AttributeDict)
    assert result.b.b2.b2b == result.b.b2["b2b"]
    assert isinstance(result.b.b2.b2b["b2b2"], AttributeDict)
    assert result.b.b2.b2b.b2b2 == result.b.b2.b2b["b2b2"]

    # cleanup
    async_w3.middleware_onion.remove("result_gen")


@pytest.mark.asyncio
async def test_no_async_attrdict_middleware_does_not_convert_dicts_to_attrdict():
    async_w3 = AsyncWeb3(AsyncEthereumTesterProvider())

    async_w3.middleware_onion.inject(
        await async_construct_result_generator_middleware(
            {RPCEndpoint("fake_endpoint"): lambda *_: GENERATED_NESTED_DICT_RESULT}
        ),
        "result_gen",
        layer=0,
    )

    # remove attrdict middleware
    async_w3.middleware_onion.remove("attrdict")

    response = await async_w3.manager.coro_request("fake_endpoint", [])

    result = response["result"]

    _assert_dict_and_not_attrdict(result)
    _assert_dict_and_not_attrdict(result["b"])
    _assert_dict_and_not_attrdict(result["b"]["b2"])
    _assert_dict_and_not_attrdict(result["b"]["b2"]["b2b"])
    _assert_dict_and_not_attrdict(result["b"]["b2"]["b2b"]["b2b2"])
