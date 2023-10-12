from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
)

from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3.main import (  # noqa: F401
        _PersistentConnectionWeb3,
    )
    from web3.manager import (  # noqa: F401
        _AsyncPersistentRecvStream,
    )


class WebsocketConnection:
    """
    A class that houses the public API for interacting with the websocket connection
    via a `_PersistentConnectionWeb3` instance.
    """

    def __init__(self, w3: "_PersistentConnectionWeb3"):
        self._manager = w3.manager

    @property
    def subscriptions(self) -> Dict[str, Any]:
        return self._manager._request_processor.active_subscriptions

    async def send(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        return await self._manager.ws_send(method, params)

    async def recv(self) -> Any:
        return await self._manager.ws_recv()

    def listen_to_websocket(self) -> "_AsyncPersistentRecvStream":
        return self._manager._persistent_recv_stream()
