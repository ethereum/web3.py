from web3.manager import (
    RequestManager,
)
from web3.middleware import (
    abi_middleware,
    attrdict_middleware,
    buffered_gas_estimate_middleware,
    ens_name_to_address_middleware,
    gas_price_strategy_middleware,
    validation_middleware,
)


def test_default_sync_middlewares(w3):
    expected_middlewares = [
        (gas_price_strategy_middleware, "gas_price_strategy"),
        (ens_name_to_address_middleware, "name_to_address"),
        (attrdict_middleware, "attrdict"),
        (validation_middleware, "validation"),
        (abi_middleware, "abi"),
        (buffered_gas_estimate_middleware, "gas_estimate"),
    ]

    default_middlewares = RequestManager.default_middlewares(w3)

    for x in range(len(default_middlewares)):
        assert default_middlewares[x][0].__name__ == expected_middlewares[x][0].__name__
        assert default_middlewares[x][1] == expected_middlewares[x][1]


def test_default_async_middlewares():
    expected_middlewares = [
        (gas_price_strategy_middleware, "gas_price_strategy"),
        (ens_name_to_address_middleware, "name_to_address"),
        (attrdict_middleware, "attrdict"),
        (validation_middleware, "validation"),
        (buffered_gas_estimate_middleware, "gas_estimate"),
    ]

    default_middlewares = RequestManager.async_default_middlewares()

    for x in range(len(default_middlewares)):
        assert default_middlewares[x][0].__name__ == expected_middlewares[x][0].__name__
        assert default_middlewares[x][1] == expected_middlewares[x][1]
