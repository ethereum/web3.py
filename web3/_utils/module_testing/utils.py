from asyncio import (
    iscoroutinefunction,
)
import copy
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Union,
    cast,
)

from toolz import (
    merge,
)

from web3.exceptions import (
    Web3ValidationError,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )
    from web3._utils.compat import (  # noqa: F401
        Self,
    )
    from web3.types import (  # noqa: F401
        AsyncMakeRequestFn,
        MakeRequestFn,
        RPCEndpoint,
        RPCResponse,
    )


class RequestMocker:
    """
    Context manager to mock requests made by a web3 instance. This is meant to be used
    via a ``request_mocker`` fixture defined within the appropriate context.

    Example:

        def test_my_w3(w3, request_mocker):
            assert w3.eth.block_number == 0

            with request_mocker(w3, mock_results={"eth_blockNumber": "0x1"}):
                assert w3.eth.block_number == 1

            assert w3.eth.block_number == 0

    ``mock_results`` is a dict mapping method names to the desired "result" object of
    the RPC response. ``mock_errors`` is a dict mapping method names to the desired
    "error" object of the RPC response. If a method name is not in either dict,
    the request is made as usual.
    """

    def __init__(
        self,
        w3: Union["AsyncWeb3", "Web3"],
        mock_results: Dict[Union["RPCEndpoint", str], Any] = None,
        mock_errors: Dict[Union["RPCEndpoint", str], Dict[str, Any]] = None,
    ):
        self.w3 = w3
        self.mock_results = mock_results or {}
        self.mock_errors = mock_errors or {}
        self._make_request: Union[
            "AsyncMakeRequestFn", "MakeRequestFn"
        ] = w3.provider.make_request

    def __enter__(self) -> "Self":
        setattr(self.w3.provider, "make_request", self._mock_request_handler)
        # reset request func cache to re-build request_func with mocked make_request
        self.w3.provider._request_func_cache = (None, None)

        return self

    # define __exit__ with typing information
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        setattr(self.w3.provider, "make_request", self._make_request)
        # reset request func cache to re-build request_func with original make_request
        self.w3.provider._request_func_cache = (None, None)

    def _mock_request_handler(
        self, method: "RPCEndpoint", params: Any
    ) -> "RPCResponse":
        self.w3 = cast("Web3", self.w3)
        self._make_request = cast("MakeRequestFn", self._make_request)

        if method not in self.mock_errors and method not in self.mock_results:
            return self._make_request(method, params)

        request_id = (
            next(copy.deepcopy(self.w3.provider.request_counter))
            if hasattr(self.w3.provider, "request_counter")
            else 1
        )
        response_dict = {"jsonrpc": "2.0", "id": request_id}

        if method in self.mock_results:
            mock_return = self.mock_results[method]
            if callable(mock_return):
                mock_return = mock_return(method, params)
            return merge(response_dict, {"result": mock_return})
        elif method in self.mock_errors:
            error = self.mock_errors[method]
            if not isinstance(error, dict):
                raise Web3ValidationError("error must be a dict")
            code = error.get("code", -32000)
            message = error.get("message", "Mocked error")
            return merge(
                response_dict,
                {"error": merge({"code": code, "message": message}, error)},
            )
        else:
            raise Exception("Invariant: unreachable code path")

    # -- async -- #
    async def __aenter__(self) -> "Self":
        setattr(self.w3.provider, "make_request", self._async_mock_request_handler)
        # reset request func cache to re-build request_func with mocked make_request
        self.w3.provider._request_func_cache = (None, None)
        return self

    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        setattr(self.w3.provider, "make_request", self._make_request)
        # reset request func cache to re-build request_func with original make_request
        self.w3.provider._request_func_cache = (None, None)

    async def _async_mock_request_handler(
        self, method: "RPCEndpoint", params: Any
    ) -> "RPCResponse":
        self.w3 = cast("AsyncWeb3", self.w3)
        self._make_request = cast("AsyncMakeRequestFn", self._make_request)

        if method not in self.mock_errors and method not in self.mock_results:
            return await self._make_request(method, params)

        request_id = (
            next(copy.deepcopy(self.w3.provider.request_counter))
            if hasattr(self.w3.provider, "request_counter")
            else 1
        )
        response_dict = {"jsonrpc": "2.0", "id": request_id}

        if method in self.mock_results:
            mock_return = self.mock_results[method]
            if callable(mock_return):
                # handle callable to make things easier since we're mocking
                mock_return = mock_return(method, params)
            elif iscoroutinefunction(mock_return):
                # this is the "correct" way to mock the async make_request
                mock_return = await mock_return(method, params)
            return merge(response_dict, {"result": mock_return})
        elif method in self.mock_errors:
            error = self.mock_errors[method]
            if not isinstance(error, dict):
                raise Web3ValidationError("error must be a dict")
            code = error.get("code", -32000)
            message = error.get("message", "Mocked error")
            return merge(
                response_dict,
                {"error": merge({"code": code, "message": message}, error)},
            )
        else:
            raise Exception("Invariant: unreachable code path")
