import pytest

from aiohttp import (
    ClientSession,
)

from web3 import (
    AsyncWeb3,
    __version__ as web3py_version,
)
from web3.eth import (
    AsyncEth,
)
from web3.exceptions import (
    ProviderConnectionError,
)
from web3.geth import (
    AsyncGeth,
    AsyncGethAdmin,
    AsyncGethTxPool,
)
from web3.middleware import (
    AttributeDictMiddleware,
    BufferedGasEstimateMiddleware,
    ENSNameToAddressMiddleware,
    GasPriceStrategyMiddleware,
    ValidationMiddleware,
)
from web3.net import (
    AsyncNet,
)
from web3.providers.rpc import (
    AsyncHTTPProvider,
)

URI = "http://mynode.local:8545"


@pytest.mark.asyncio
async def test_async_no_args() -> None:
    provider = AsyncHTTPProvider()
    w3 = AsyncWeb3(provider)
    assert w3.manager.provider == provider
    assert w3.manager.provider.is_async
    assert not await w3.is_connected()
    with pytest.raises(ProviderConnectionError):
        await w3.is_connected(show_traceback=True)


def test_init_kwargs():
    provider = AsyncHTTPProvider(endpoint_uri=URI, request_kwargs={"timeout": 60})
    w3 = AsyncWeb3(provider)
    assert w3.manager.provider == provider


def test_web3_with_async_http_provider_has_default_middleware_and_modules() -> None:
    async_w3 = AsyncWeb3(AsyncHTTPProvider(endpoint_uri=URI))

    # assert default modules

    assert isinstance(async_w3.eth, AsyncEth)
    assert isinstance(async_w3.net, AsyncNet)
    assert isinstance(async_w3.geth, AsyncGeth)
    assert isinstance(async_w3.geth.admin, AsyncGethAdmin)
    assert isinstance(async_w3.geth.txpool, AsyncGethTxPool)

    # assert default middleware

    # the following length check should fail and will need to be added to once more
    # async middleware are added to the defaults
    assert len(async_w3.middleware_onion.middleware) == 5

    assert (
        async_w3.middleware_onion.get("gas_price_strategy")
        == GasPriceStrategyMiddleware
    )
    assert (
        async_w3.middleware_onion.get("ens_name_to_address")
        == ENSNameToAddressMiddleware
    )
    assert async_w3.middleware_onion.get("attrdict") == AttributeDictMiddleware
    assert async_w3.middleware_onion.get("validation") == ValidationMiddleware
    assert (
        async_w3.middleware_onion.get("gas_estimate") == BufferedGasEstimateMiddleware
    )


@pytest.mark.asyncio
async def test_async_user_provided_session() -> None:
    session = ClientSession()
    provider = AsyncHTTPProvider(endpoint_uri=URI)
    cached_session = await provider.cache_async_session(session)
    assert len(provider._request_session_manager.session_cache) == 1
    assert cached_session == session


def test_get_request_headers():
    provider = AsyncHTTPProvider()
    headers = provider.get_request_headers()
    assert len(headers) == 2
    assert headers["Content-Type"] == "application/json"
    assert (
        headers["User-Agent"] == f"web3.py/{web3py_version}/"
        f"{AsyncHTTPProvider.__module__}.{AsyncHTTPProvider.__qualname__}"
    )
