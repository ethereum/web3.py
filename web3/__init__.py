from eth_account import Account  # noqa: E402,
import pkg_resources

from web3.main import (
    AsyncWeb3,
    Web3,
)
from web3.providers.async_rpc import (  # noqa: E402
    AsyncHTTPProvider,
)
from web3.providers.eth_tester import (  # noqa: E402
    EthereumTesterProvider,
)
from web3.providers.ipc import (  # noqa: E402
    IPCProvider,
)
from web3.providers.rpc import (  # noqa: E402
    HTTPProvider,
)
from web3.providers.websocket import (  # noqa: E402
    WebsocketProvider,
)

__version__ = pkg_resources.get_distribution("web3").version

__all__ = [
    "__version__",
    "AsyncWeb3",
    "Web3",
    "HTTPProvider",
    "IPCProvider",
    "WebsocketProvider",
    "EthereumTesterProvider",
    "Account",
    "AsyncHTTPProvider",
]
