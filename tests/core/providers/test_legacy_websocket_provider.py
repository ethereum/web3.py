import pytest

from web3 import (
    Web3,
)
from web3.exceptions import (
    ProviderConnectionError,
    Web3ValidationError,
)
from web3.providers.legacy_websocket import (
    LegacyWebSocketProvider,
)


def test_no_args():
    provider = LegacyWebSocketProvider()
    w3 = Web3(provider)
    assert w3.manager.provider == provider
    assert not w3.manager.provider.is_async
    assert not w3.is_connected()
    with pytest.raises(ProviderConnectionError):
        w3.is_connected(show_traceback=True)


def test_restricted_websocket_kwargs():
    invalid_kwargs = {"uri": "ws://127.0.0.1:8546"}
    re_exc_message = f".*found: {set(invalid_kwargs)!r}*"
    with pytest.raises(Web3ValidationError, match=re_exc_message):
        LegacyWebSocketProvider(websocket_kwargs=invalid_kwargs)
