from eth_account import Account  # noqa: E402,
import pkg_resources
import sys

if sys.platform == "emscripten":
    # pyodide has a built in patcher which makes the requests module work
    import pyodide_http

    pyodide_http.patch_all()
    # asynchronous connections and websockets aren't supported on
    # emscripten yet.
    # We mock the aiohttp and websockets module so that things import okay
    import micropip

    micropip.add_mock_package(
        "aiohttp",
        "1.0.0",
        modules={
            "aiohttp": """
class ClientSession:
    def __init__(self,*args,**argv):
        raise NotImplementedError("Async web3 functions aren't supported on pyodide yet")
class ClientResponse:
    def __init__(self,*args,**argv):
        raise NotImplementedError("Async web3 functions aren't supported on pyodide yet")
class ClientTimeout:
    def __init__(self,*args,**argv):
        raise NotImplementedError("Async web3 functions aren't supported on pyodide yet")
"""
        },
    )
    # mock websockets
    micropip.add_mock_package(
        "websockets",
        "1.0.0",
        modules={
            "websockets": "",
            "websockets.legacy": "",
            "websockets.legacy.client": """
class WebSocketClientProtocol:
    def __init__(self,*args,**argv):
        raise NotImplementedError("Websockets aren't supported on pyodide yet")
""",
            "websockets.client": """
def connect(*args,**argv):
        raise NotImplementedError("Websockets aren't supported on pyodide yet")
""",
            "websockets.exceptions": """
class WebSocketException:
    def __init__(self,*args,**argv):
        raise NotImplementedError("Websockets aren't supported on pyodide yet")
class ConnectionClosedOK:
    def __init__(self,*args,**argv):
        raise NotImplementedError("Websockets aren't supported on pyodide yet")
""",
        },
    )


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

__version__ = pkg_resources.get_distribution("web3").version

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
