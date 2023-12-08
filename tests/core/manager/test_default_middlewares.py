from web3.manager import (
    RequestManager,
)
from web3.middleware import (
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
        (buffered_gas_estimate_middleware, "gas_estimate"),
    ]

    default_middlewares = RequestManager.default_middlewares(w3)

    assert default_middlewares == expected_middlewares
