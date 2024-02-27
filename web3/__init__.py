from eth_account import Account  # noqa: E402
import sys

if sys.version_info.major == 3 and sys.version_info.minor < 8:
    import pkg_resources

    __version__ = pkg_resources.get_distribution("web3").version
else:
    from importlib.metadata import version

    __version__ = version("web3")


from web3.main import (
    AsyncWeb3,
    Web3,
)
from web3.providers.persistent import (  # noqa: E402
    AsyncIPCProvider,
    PersistentConnectionProvider,
    WebSocketProvider,
)
from web3.providers.eth_tester import (  # noqa: E402
    EthereumTesterProvider,
)
from web3.providers.ipc import (  # noqa: E402
    IPCProvider,
)
from web3.providers.rpc import (  # noqa: E402
    AsyncHTTPProvider,
    HTTPProvider,
)
from web3.providers.legacy_websocket import (  # noqa: E402
    LegacyWebSocketProvider,
)


__all__ = [
    "__version__",
    "AsyncWeb3",
    "Web3",
    "HTTPProvider",
    "IPCProvider",
    "LegacyWebSocketProvider",
    "WebSocketProvider",
    "EthereumTesterProvider",
    "Account",
    "AsyncHTTPProvider",
    "AsyncIPCProvider",
]
