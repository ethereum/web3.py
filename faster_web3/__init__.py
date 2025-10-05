from eth_account import Account  # noqa: E402

from importlib.metadata import version

__version__ = version("faster_web3")


from faster_web3.main import (
    AsyncWeb3,
    Web3,
)
from faster_web3.providers import (
    AsyncBaseProvider,
    AutoProvider,
    BaseProvider,
    JSONBaseProvider,
    PersistentConnection,
)
from faster_web3.providers.persistent import (  # noqa: E402
    AsyncIPCProvider,
    PersistentConnectionProvider,
    WebSocketProvider,
)
from faster_web3.providers.eth_tester import (  # noqa: E402
    AsyncEthereumTesterProvider,
    EthereumTesterProvider,
)
from faster_web3.providers.ipc import (  # noqa: E402
    IPCProvider,
)
from faster_web3.providers.rpc import (  # noqa: E402
    AsyncHTTPProvider,
    HTTPProvider,
)
from faster_web3.providers.legacy_websocket import (  # noqa: E402
    LegacyWebSocketProvider,
)


__all__ = [
    "__version__",
    "Account",
    # web3:
    "AsyncWeb3",
    "Web3",
    # providers:
    "AsyncBaseProvider",
    "AsyncEthereumTesterProvider",
    "AsyncHTTPProvider",
    "AsyncIPCProvider",
    "AutoProvider",
    "BaseProvider",
    "EthereumTesterProvider",
    "HTTPProvider",
    "IPCProvider",
    "JSONBaseProvider",
    "LegacyWebSocketProvider",
    "PersistentConnection",
    "PersistentConnectionProvider",
    "WebSocketProvider",
]
