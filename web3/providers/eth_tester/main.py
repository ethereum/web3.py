from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Optional,
)

from eth_abi import (
    decode_single,
)
from eth_abi.exceptions import (
    InsufficientDataBytes,
)

from web3._utils.compat import (
    Literal,
)
from web3.providers import (
    BaseProvider,
)
from web3.providers.async_base import (
    AsyncBaseProvider,
)
from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

from .middleware import (
    default_transaction_fields_middleware,
    ethereum_tester_middleware,
)

if TYPE_CHECKING:
    from eth_tester import (  # noqa: F401
        EthereumTester,
    )


class AsyncEthereumTesterProvider(AsyncBaseProvider):
    def __init__(self) -> None:
        self.eth_tester = EthereumTesterProvider()

    async def make_request(
        self, method: RPCEndpoint, params: Any
    ) -> RPCResponse:
        return self.eth_tester.make_request(method, params)


class EthereumTesterProvider(BaseProvider):
    middlewares = (
        default_transaction_fields_middleware,
        ethereum_tester_middleware,
    )
    ethereum_tester = None
    api_endpoints = None

    def __init__(
        self,
        ethereum_tester: Optional["EthereumTester"] = None,
        api_endpoints: Optional[Dict[str, Dict[str, Callable[..., RPCResponse]]]] = None
    ) -> None:
        # do not import eth_tester until runtime, it is not a default dependency
        from eth_tester import EthereumTester  # noqa: F811
        from eth_tester.backends.base import BaseChainBackend
        if ethereum_tester is None:
            self.ethereum_tester = EthereumTester()
        elif isinstance(ethereum_tester, EthereumTester):
            self.ethereum_tester = ethereum_tester
        elif isinstance(ethereum_tester, BaseChainBackend):
            self.ethereum_tester = EthereumTester(ethereum_tester)
        else:
            raise TypeError(
                "Expected ethereum_tester to be of type `eth_tester.EthereumTester` or "
                "a subclass of `eth_tester.backends.base.BaseChainBackend`, "
                f"instead received {type(ethereum_tester)}. "
                "If you would like a custom eth-tester instance to test with, see the "
                "eth-tester documentation. https://github.com/ethereum/eth-tester."
            )

        if api_endpoints is None:
            # do not import eth_tester derivatives until runtime, it is not a default dependency
            from .defaults import API_ENDPOINTS
            self.api_endpoints = API_ENDPOINTS
        else:
            self.api_endpoints = api_endpoints

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        namespace, _, endpoint = method.partition('_')
        from eth_tester.exceptions import TransactionFailed
        try:
            delegator = self.api_endpoints[namespace][endpoint]
        except KeyError:
            return RPCResponse(
                {"error": f"Unknown RPC Endpoint: {method}"}
            )
        try:
            response = delegator(self.ethereum_tester, params)
        except NotImplementedError:
            return RPCResponse(
                {"error": f"RPC Endpoint has not been implemented: {method}"}
            )
        except TransactionFailed as e:
            try:
                reason = decode_single('(string)', e.args[0].args[0][4:])[0]
            except (InsufficientDataBytes, AttributeError):
                reason = e.args[0]
            raise TransactionFailed(f'execution reverted: {reason}')
        else:
            return {
                'result': response,
            }

    def isConnected(self) -> Literal[True]:
        return True
