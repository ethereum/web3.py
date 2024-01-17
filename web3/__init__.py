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
    WebsocketProviderV2,
)


__all__ = [
    "__version__",
    "AsyncWeb3",
    "Web3",
    "HTTPProvider",
    "IPCProvider",
    "WebsocketProvider",
    "WebsocketProviderV2",
    "EthereumTesterProvider",
    "Account",
    "AsyncHTTPProvider",
]
