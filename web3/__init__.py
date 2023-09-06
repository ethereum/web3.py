from eth_account import Account  # noqa: E402,
import pkg_resources
import sys

if sys.platform == "emscripten":
    # pyodide has a built in patcher which makes the requests module work
    from pyodide_http import patch_all

    patch_all()
    # asynchronous connections and websockets aren't supported on
    # emscripten yet.
    # We mock the aiohttp and websockets module so that things import okay
    from micropip import add_mock_package

    add_mock_package(
        "aiohttp",
        "1.0.0",
        modules={
            "aiohttp": """
class __NotImplemented:
    def __init__(self,*args,**argv):
        raise NotImplementedError(
            "Async web3 functions aren't supported on pyodide yet"
        )
class ClientSession(__NotImplemented):
    pass
class ClientResponse(__NotImplemented):
    pass
class ClientTimeout(__NotImplemented):
    pass
"""
        },
    )
    # mock websockets
    add_mock_package(
        "websockets",
        "1.0.0",
        modules={
            "websockets": """
class __NotImplemented:
    def __init__(self,*args,**argv):
        raise NotImplementedError(
            "Async web3 functions aren't supported on pyodide yet"
        )
""",
            "websockets.legacy": "",
            "websockets.legacy.client": """
from websockets import __NotImplemented
class WebSocketClientProtocol(__NotImplemented):
    pass
""",
            "websockets.client": """
def connect(*args,**argv):
        raise NotImplementedError(
            "Websockets aren't supported on pyodide yet"
        )
""",
            "websockets.exceptions": """
from websockets import __NotImplemented
class WebSocketException(__NotImplemented):
    pass
class ConnectionClosedOK(__NotImplemented):
    pass
""",
        },
    )


from web3.main import AsyncWeb3, Web3  # noqa: E402
from web3.providers.async_rpc import AsyncHTTPProvider  # noqa: E402
from web3.providers.eth_tester import EthereumTesterProvider  # noqa: E402
from web3.providers.ipc import IPCProvider  # noqa: E402
from web3.providers.rpc import HTTPProvider  # noqa: E402
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
