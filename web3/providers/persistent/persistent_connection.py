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
        AsyncWeb3,
    )
    from web3.manager import (  # noqa: F401
        _AsyncPersistentMessageStream,
    )


class PersistentConnection:
    """
    A class that houses the public API for interacting with the persistent connection
    via a `AsyncWeb3` instance instantiated with a `PersistentConnectionProvider` class.
    """

    def __init__(self, w3: "AsyncWeb3"):
        self._manager = w3.manager

    # -- public methods -- #
    @property
    def subscriptions(self) -> Dict[str, Any]:
        return self._manager._request_processor.active_subscriptions

    async def send(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        return await self._manager.send(method, params)

    async def recv(self) -> Any:
        return await self._manager._get_next_message()

    def process_subscriptions(self) -> "_AsyncPersistentMessageStream":
        return self._manager._persistent_message_stream()
