import pytest

from ens import (
    ENS,
    AsyncENSFactory,
)
from web3.middleware import (
    async_validation_middleware,
    pythonic_middleware,
)


def test_fromWeb3_inherits_web3_middlewares(w3):
    test_middleware = pythonic_middleware
    w3.middleware_onion.add(test_middleware, "test_middleware")

    ns = ENS.fromWeb3(w3)
    assert ns.w3.middleware_onion.get("test_middleware") == test_middleware


# -- async -- #

@pytest.mark.asyncio
async def test_async_ens_factory_fromWeb3_inherits_web3_middlewares(async_w3):
    test_middleware = async_validation_middleware
    async_w3.middleware_onion.add(test_middleware, 'test_middleware')

    ns = await AsyncENSFactory.fromWeb3(async_w3)
    assert ns.w3.middleware_onion.get('test_middleware') == test_middleware
