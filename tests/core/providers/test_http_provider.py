import pytest

from requests import (
    Session,
)
from requests.adapters import (
    HTTPAdapter,
)

from web3 import (
    Web3,
)
from web3._utils import (
    request,
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
    GethPersonal,
    GethTxPool,
)
from web3.middleware import (
    abi_middleware,
    attrdict_middleware,
    buffered_gas_estimate_middleware,
    gas_price_strategy_middleware,
    name_to_address_middleware,
    validation_middleware,
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


def test_web3_with_http_provider_has_default_middlewares_and_modules() -> None:
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
    assert isinstance(w3.geth.personal, GethPersonal)
    assert isinstance(w3.geth.txpool, GethTxPool)

    # assert default middleware

    # the following length check should fail and will need to be added to once more
    # middlewares are added to the defaults
    assert len(w3.middleware_onion.middlewares) == 6

    assert (
        w3.middleware_onion.get("gas_price_strategy") == gas_price_strategy_middleware
    )
    assert (
        w3.middleware_onion.get("name_to_address").__name__
        == name_to_address_middleware(w3).__name__
    )
    assert w3.middleware_onion.get("attrdict") == attrdict_middleware
    assert w3.middleware_onion.get("validation") == validation_middleware
    assert w3.middleware_onion.get("gas_estimate") == buffered_gas_estimate_middleware
    assert w3.middleware_onion.get("abi") == abi_middleware


def test_user_provided_session():
    adapter = HTTPAdapter(pool_connections=20, pool_maxsize=20)
    session = Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    provider = HTTPProvider(endpoint_uri=URI, session=session)
    w3 = Web3(provider)
    assert w3.manager.provider == provider

    session = request.cache_and_return_session(URI)
    adapter = session.get_adapter(URI)
    assert isinstance(adapter, HTTPAdapter)
    assert adapter._pool_connections == 20
    assert adapter._pool_maxsize == 20
