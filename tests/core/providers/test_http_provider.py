import pytest

from requests import (
    Session,
)
from requests.adapters import (
    HTTPAdapter,
)

from web3 import (
    Web3,
    __version__ as web3py_version,
)
from web3.eth import (
    Eth,
)
from web3.exceptions import (
    ProviderConnectionError,
)
from web3.geth import (
    Geth,
    GethAdmin,
    GethTxPool,
)
from web3.middleware import (
    AttributeDictMiddleware,
    BufferedGasEstimateMiddleware,
    ENSNameToAddressMiddleware,
    GasPriceStrategyMiddleware,
    ValidationMiddleware,
)
from web3.net import (
    Net,
)
from web3.providers import (
    HTTPProvider,
)

URI = "http://mynode.local:8545"


def test_no_args():
    provider = HTTPProvider()
    w3 = Web3(provider)
    assert w3.manager.provider == provider
    assert not w3.manager.provider.is_async
    assert not w3.is_connected()
    with pytest.raises(ProviderConnectionError):
        w3.is_connected(show_traceback=True)


def test_init_kwargs():
    provider = HTTPProvider(endpoint_uri=URI, request_kwargs={"timeout": 60})
    w3 = Web3(provider)
    assert w3.manager.provider == provider


def test_web3_with_http_provider_has_default_middleware_and_modules() -> None:
    adapter = HTTPAdapter(pool_connections=20, pool_maxsize=20)
    session = Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    provider = HTTPProvider(endpoint_uri=URI, session=session)
    w3 = Web3(provider)

    # assert default modules
    assert isinstance(w3.eth, Eth)
    assert isinstance(w3.net, Net)
    assert isinstance(w3.geth, Geth)
    assert isinstance(w3.geth.admin, GethAdmin)
    assert isinstance(w3.geth.txpool, GethTxPool)

    # assert default middleware

    # the following length check should fail and will need to be added to once more
    # middleware are added to the defaults
    assert len(w3.middleware_onion.middleware) == 5

    assert w3.middleware_onion.get("gas_price_strategy") == GasPriceStrategyMiddleware
    assert w3.middleware_onion.get("ens_name_to_address") == ENSNameToAddressMiddleware
    assert w3.middleware_onion.get("attrdict") == AttributeDictMiddleware
    assert w3.middleware_onion.get("validation") == ValidationMiddleware
    assert w3.middleware_onion.get("gas_estimate") == BufferedGasEstimateMiddleware


def test_user_provided_session():
    adapter = HTTPAdapter(pool_connections=20, pool_maxsize=20)
    session = Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    provider = HTTPProvider(endpoint_uri=URI, session=session)
    session = provider._request_session_manager.cache_and_return_session(URI)
    w3 = Web3(provider)
    assert w3.manager.provider == provider

    adapter = session.get_adapter(URI)
    assert isinstance(adapter, HTTPAdapter)
    assert adapter._pool_connections == 20
    assert adapter._pool_maxsize == 20


def test_get_request_headers():
    provider = HTTPProvider()
    headers = provider.get_request_headers()
    assert len(headers) == 2
    assert headers["Content-Type"] == "application/json"
    assert (
        headers["User-Agent"] == f"web3.py/{web3py_version}/"
        f"{HTTPProvider.__module__}.{HTTPProvider.__qualname__}"
    )
