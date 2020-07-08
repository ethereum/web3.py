from requests import (
    Session,
)
from requests.adapters import (
    HTTPAdapter,
)

from web3 import Web3
from web3._utils import (
    request,
)
from web3.providers import (
    HTTPProvider,
)

URI = "http://mynode.local:8545"


def test_no_args():
    provider = HTTPProvider()
    web3 = Web3(provider)
    assert web3.manager.provider == provider


def test_init_kwargs():
    provider = HTTPProvider(endpoint_uri=URI,
                            request_kwargs={'timeout': 60})
    web3 = Web3(provider)
    assert web3.manager.provider == provider


def test_user_provided_session():
    adapter = HTTPAdapter(pool_connections=20, pool_maxsize=20)
    session = Session()
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    provider = HTTPProvider(endpoint_uri=URI, session=session)
    web3 = Web3(provider)
    assert web3.manager.provider == provider

    session = request._get_session(URI)
    adapter = session.get_adapter(URI)
    assert isinstance(adapter, HTTPAdapter)
    assert adapter._pool_connections == 20
    assert adapter._pool_maxsize == 20
