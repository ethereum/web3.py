import itertools
import pytest
import threading
import uuid

from web3 import Web3
from web3._utils.caching import (
    SimpleCache,
    generate_cache_key,
)
from web3.middleware import (
    construct_error_generator_middleware,
    construct_result_generator_middleware,
    construct_simple_cache_middleware,
)
from web3.middleware.async_cache import (
    async_construct_simple_cache_middleware,
)
from web3.middleware.fixture import (
    async_construct_error_generator_middleware,
    async_construct_result_generator_middleware,
)
from web3.providers.base import (
    BaseProvider,
)
from web3.providers.eth_tester import (
    AsyncEthereumTesterProvider,
)
from web3.types import (
    RPCEndpoint,
)


@pytest.fixture
def w3_base():
    return Web3(provider=BaseProvider(), middlewares=[])


@pytest.fixture
def result_generator_middleware():
    return construct_result_generator_middleware(
        {
            RPCEndpoint("fake_endpoint"): lambda *_: str(uuid.uuid4()),
            RPCEndpoint("not_whitelisted"): lambda *_: str(uuid.uuid4()),
        }
    )


@pytest.fixture
def w3(w3_base, result_generator_middleware):
    w3_base.middleware_onion.add(result_generator_middleware)
    return w3_base


def dict_cache_class_return_value_a():
    # test dictionary-based cache
    return {
        generate_cache_key(f"{threading.get_ident()}:{('fake_endpoint', [1])}"): {
            "result": "value-a"
        },
    }


def simple_cache_class_return_value_a():
    # test `SimpleCache` class cache
    _cache = SimpleCache()
    _cache.cache(
        generate_cache_key(f"{threading.get_ident()}:{('fake_endpoint', [1])}"),
        {"result": "value-a"},
    )
    return _cache


@pytest.mark.parametrize(
    "cache_class",
    (
        dict_cache_class_return_value_a,
        simple_cache_class_return_value_a,
    ),
)
def test_simple_cache_middleware_pulls_from_cache(w3, cache_class):

    w3.middleware_onion.add(
        construct_simple_cache_middleware(
            cache_class=cache_class,
            rpc_whitelist={RPCEndpoint("fake_endpoint")},
        )
    )

    assert w3.manager.request_blocking("fake_endpoint", [1]) == "value-a"


@pytest.mark.parametrize("cache_class", (dict, SimpleCache))
def test_simple_cache_middleware_populates_cache(w3, cache_class):
    w3.middleware_onion.add(
        construct_simple_cache_middleware(
            cache_class=cache_class,
            rpc_whitelist={RPCEndpoint("fake_endpoint")},
        )
    )

    result = w3.manager.request_blocking("fake_endpoint", [])

    assert w3.manager.request_blocking("fake_endpoint", []) == result
    assert w3.manager.request_blocking("fake_endpoint", [1]) != result


@pytest.mark.parametrize("cache_class", (dict, SimpleCache))
def test_simple_cache_middleware_does_not_cache_none_responses(w3_base, cache_class):
    counter = itertools.count()
    w3 = w3_base

    def result_cb(_method, _params):
        next(counter)
        return None

    w3.middleware_onion.add(
        construct_result_generator_middleware(
            {
                RPCEndpoint("fake_endpoint"): result_cb,
            }
        )
    )

    w3.middleware_onion.add(
        construct_simple_cache_middleware(
            cache_class=cache_class,
            rpc_whitelist={RPCEndpoint("fake_endpoint")},
        )
    )

    w3.manager.request_blocking("fake_endpoint", [])
    w3.manager.request_blocking("fake_endpoint", [])

    assert next(counter) == 2


@pytest.mark.parametrize("cache_class", (dict, SimpleCache))
def test_simple_cache_middleware_does_not_cache_error_responses(w3_base, cache_class):
    w3 = w3_base
    w3.middleware_onion.add(
        construct_error_generator_middleware(
            {
                RPCEndpoint("fake_endpoint"): lambda *_: f"msg-{uuid.uuid4()}",
            }
        )
    )

    w3.middleware_onion.add(
        construct_simple_cache_middleware(
            cache_class=cache_class,
            rpc_whitelist={RPCEndpoint("fake_endpoint")},
        )
    )

    with pytest.raises(ValueError) as err_a:
        w3.manager.request_blocking("fake_endpoint", [])
    with pytest.raises(ValueError) as err_b:
        w3.manager.request_blocking("fake_endpoint", [])

    assert str(err_a) != str(err_b)


@pytest.mark.parametrize("cache_class", (dict, SimpleCache))
def test_simple_cache_middleware_does_not_cache_endpoints_not_in_whitelist(
    w3,
    cache_class,
):
    w3.middleware_onion.add(
        construct_simple_cache_middleware(
            cache_class=cache_class,
            rpc_whitelist={RPCEndpoint("fake_endpoint")},
        )
    )

    result_a = w3.manager.request_blocking("not_whitelisted", [])
    result_b = w3.manager.request_blocking("not_whitelisted", [])

    assert result_a != result_b


# -- async -- #


async def _async_simple_cache_middleware_for_testing(make_request, async_w3):
    middleware = await async_construct_simple_cache_middleware(
        cache_class=SimpleCache,
        rpc_whitelist={RPCEndpoint("fake_endpoint")},
    )
    return await middleware(make_request, async_w3)


@pytest.fixture
def async_w3():
    return Web3(
        provider=AsyncEthereumTesterProvider(),
        middlewares=[
            (_async_simple_cache_middleware_for_testing, "simple_cache"),
        ],
    )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "cache_class",
    (
        dict_cache_class_return_value_a,
        simple_cache_class_return_value_a,
    ),
)
async def test_async_simple_cache_middleware_pulls_from_cache(async_w3, cache_class):
    async def _properly_awaited_middleware(make_request, _async_w3):
        middleware = await async_construct_simple_cache_middleware(
            cache_class=cache_class,
            rpc_whitelist={RPCEndpoint("fake_endpoint")},
        )
        return await middleware(make_request, _async_w3)

    async_w3.middleware_onion.inject(
        _properly_awaited_middleware,
        layer=0,
    )

    _result = await async_w3.manager.coro_request("fake_endpoint", [1])
    assert _result == "value-a"


@pytest.mark.asyncio
async def test_async_simple_cache_middleware_populates_cache(async_w3):
    async_w3.middleware_onion.inject(
        await async_construct_result_generator_middleware(
            {
                RPCEndpoint("fake_endpoint"): lambda *_: str(uuid.uuid4()),
            }
        ),
        "result_generator",
        layer=0,
    )

    result = await async_w3.manager.coro_request("fake_endpoint", [])

    _empty_params = await async_w3.manager.coro_request("fake_endpoint", [])
    _non_empty_params = await async_w3.manager.coro_request("fake_endpoint", [1])

    assert _empty_params == result
    assert _non_empty_params != result


@pytest.mark.asyncio
async def test_async_simple_cache_middleware_does_not_cache_none_responses(async_w3):
    counter = itertools.count()

    def result_cb(_method, _params):
        next(counter)
        return None

    async_w3.middleware_onion.inject(
        await async_construct_result_generator_middleware(
            {
                RPCEndpoint("fake_endpoint"): result_cb,
            },
        ),
        "result_generator",
        layer=0,
    )

    await async_w3.manager.coro_request("fake_endpoint", [])
    await async_w3.manager.coro_request("fake_endpoint", [])

    assert next(counter) == 2


@pytest.mark.asyncio
async def test_async_simple_cache_middleware_does_not_cache_error_responses(async_w3):
    async_w3.middleware_onion.inject(
        await async_construct_error_generator_middleware(
            {
                RPCEndpoint("fake_endpoint"): lambda *_: f"msg-{uuid.uuid4()}",
            }
        ),
        "error_generator",
        layer=0,
    )

    with pytest.raises(ValueError) as err_a:
        await async_w3.manager.coro_request("fake_endpoint", [])
    with pytest.raises(ValueError) as err_b:
        await async_w3.manager.coro_request("fake_endpoint", [])

    assert str(err_a) != str(err_b)


@pytest.mark.asyncio
async def test_async_simple_cache_middleware_does_not_cache_non_whitelist_endpoints(
    async_w3,
):
    async_w3.middleware_onion.inject(
        await async_construct_result_generator_middleware(
            {
                RPCEndpoint("not_whitelisted"): lambda *_: str(uuid.uuid4()),
            }
        ),
        layer=0,
    )

    result_a = await async_w3.manager.coro_request("not_whitelisted", [])
    result_b = await async_w3.manager.coro_request("not_whitelisted", [])

    assert result_a != result_b
