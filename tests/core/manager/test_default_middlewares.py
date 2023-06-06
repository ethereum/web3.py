from web3.manager import (
    RequestManager,
)
from web3.middleware import (
    abi_middleware,
    async_attrdict_middleware,
    async_buffered_gas_estimate_middleware,
    async_gas_price_strategy_middleware,
    async_validation_middleware,
    attrdict_middleware,
    buffered_gas_estimate_middleware,
    gas_price_strategy_middleware,
    name_to_address_middleware,
    pythonic_middleware,
    request_parameter_normalizer,
    validation_middleware,
)


def test_default_sync_middlwares(w3):
    expected_middlewares = [
        (request_parameter_normalizer, "request_param_normalizer"),
        (gas_price_strategy_middleware, "gas_price_strategy"),
        (name_to_address_middleware(w3), "name_to_address"),
        (attrdict_middleware, "attrdict"),
        (pythonic_middleware, "pythonic"),
        (validation_middleware, "validation"),
        (abi_middleware, "abi"),
        (buffered_gas_estimate_middleware, "gas_estimate"),
    ]

    default_middlewares = RequestManager.default_middlewares(w3)

    for x in range(len(default_middlewares)):
        assert default_middlewares[x][0].__name__ == expected_middlewares[x][0].__name__
        assert default_middlewares[x][1] == expected_middlewares[x][1]


def test_default_async_middlwares():
    expected_middlewares = [
        (async_gas_price_strategy_middleware, "gas_price_strategy"),
        (async_attrdict_middleware, "attrdict"),
        (async_validation_middleware, "validation"),
        (async_buffered_gas_estimate_middleware, "gas_estimate"),
    ]

    default_middlewares = RequestManager.async_default_middlewares()

    for x in range(len(default_middlewares)):
        assert default_middlewares[x][0].__name__ == expected_middlewares[x][0].__name__
        assert default_middlewares[x][1] == expected_middlewares[x][1]
