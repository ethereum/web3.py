import pytest

from web3.exceptions import (
    ValidationError,
)
from web3.providers.websocket import (
    WebsocketProvider,
)


def test_restricted_websocket_kwargs():
    invalid_kwargs = {'uri': 'ws://127.0.0.1:8546'}
    re_exc_message = r'.*found: {0}*'.format(set(invalid_kwargs.keys()))
    with pytest.raises(ValidationError, match=re_exc_message):
        WebsocketProvider(websocket_kwargs=invalid_kwargs)
