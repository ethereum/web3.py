from web3.manager import (
    RequestManager,
)
from web3.middleware import (
    AttributeDictMiddleware,
    BufferedGasEstimateMiddleware,
    ENSNameToAddressMiddleware,
    GasPriceStrategyMiddleware,
    ValidationMiddleware,
)


def test_default_sync_middlewares(w3):
    expected_middlewares = [
        (GasPriceStrategyMiddleware, "gas_price_strategy"),
        (ENSNameToAddressMiddleware, "ens_name_to_address"),
        (AttributeDictMiddleware, "attrdict"),
        (ValidationMiddleware, "validation"),
        (BufferedGasEstimateMiddleware, "gas_estimate"),
    ]

    default_middlewares = RequestManager.get_default_middlewares()

    assert default_middlewares == expected_middlewares
