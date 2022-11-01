import pytest

from ens import (
    ENS,
    AsyncENS,
)
from web3.middleware import (
    async_validation_middleware,
    pythonic_middleware,
)


def test_from_web3_inherits_web3_middlewares(w3):
    test_middleware = pythonic_middleware
    w3.middleware_onion.add(test_middleware, "test_middleware")

    ns = ENS.from_web3(w3)
    assert ns.w3.middleware_onion.get("test_middleware") == test_middleware


# -- async -- #


@pytest.mark.asyncio
async def test_async_from_web3_inherits_web3_middlewares(async_w3):
    test_middleware = async_validation_middleware
    async_w3.middleware_onion.add(test_middleware, "test_middleware")

    ns = AsyncENS.from_web3(async_w3)
    assert ns.w3.middleware_onion.get("test_middleware") == test_middleware
