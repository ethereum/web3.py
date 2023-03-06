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
from web3.providers import (
    HTTPProvider,
)

URI = "http://mynode.local:8545"


def test_no_args():
    provider = HTTPProvider()
    w3 = Web3(provider)
    assert w3.manager.provider == provider
    assert not w3.manager.provider.is_async


def test_init_kwargs():
    provider = HTTPProvider(endpoint_uri=URI, request_kwargs={"timeout": 60})
    w3 = Web3(provider)
    assert w3.manager.provider == provider


def test_user_provided_session():
    adapter = HTTPAdapter(pool_connections=20, pool_maxsize=20)
    session = Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    provider = HTTPProvider(endpoint_uri=URI, session=session)
    w3 = Web3(provider)
    assert w3.manager.provider == provider

    session = request.cache_and_return_session(URI, provider.id)
    adapter = session.get_adapter(URI)
    assert isinstance(adapter, HTTPAdapter)
    assert adapter._pool_connections == 20
    assert adapter._pool_maxsize == 20


def test_user_sessions_are_different():
    uri = "http://localhost:8545"

    provider_1 = HTTPProvider(uri)
    provider_2 = HTTPProvider(uri)
    assert provider_1.id is not provider_2.id

    session_1 = request.cache_and_return_session(uri, provider_1.id)
    session_2 = request.cache_and_return_session(uri, provider_2.id)
    assert session_1 is not session_2
