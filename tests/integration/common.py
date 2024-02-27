import pytest

from websockets.exceptions import (
    ConnectionClosed,
)

from web3 import (
    Web3,
)

# use same coinbase value as in `web3.py/tests/integration/generate_fixtures/common.py`
COINBASE = "0xdc544d1aa88ff8bbd2f2aec754b1f1e99e1812fd"


class MiscWebSocketTest:
    def test_websocket_max_size_error(self, w3, endpoint_uri):
        w3 = Web3(
            Web3.LegacyWebSocketProvider(
                endpoint_uri=endpoint_uri, websocket_kwargs={"max_size": 1}
            )
        )
        with pytest.raises((OSError, ConnectionClosed)):
            w3.eth.get_block(0)
