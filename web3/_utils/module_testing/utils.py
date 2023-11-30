import copy
from typing import (
    Any,
    Callable,
    Dict,
    TypeVar,
    Union,
)

from toolz import (
    merge,
)

from web3 import (
    AsyncWeb3,
    Web3,
)
from web3.exceptions import (
    Web3ValidationError,
)
from web3.types import (
    RPCEndpoint,
)

WEB3 = TypeVar("WEB3", Web3, AsyncWeb3)


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
        w3: WEB3,
        mock_results: Dict[Union[RPCEndpoint, str], Any] = None,
        mock_errors: Dict[Union[RPCEndpoint, str], Dict[str, Any]] = None,
    ):
        self.w3 = w3
        self.mock_results = mock_results or {}
        self.mock_errors = mock_errors or {}
        self._make_request = w3.provider.make_request

    def __enter__(self):
        self.w3.provider.make_request = self._mock_request_handler

        # reset request func cache to re-build request_func with mocked make_request
        self.w3.provider._request_func_cache = (None, None)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.w3.provider.make_request = self._make_request
        # reset request func cache to re-build request_func with original make_request
        self.w3.provider._request_func_cache = (None, None)

    def _mock_request_handler(self, method, params):
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
            if isinstance(mock_return, Callable):
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

    # -- async -- #
    async def __aenter__(self):
        self.w3.provider.make_request = self._async_mock_request_handler
        # reset request func cache to re-build request_func with mocked make_request
        self.w3.provider._request_func_cache = (None, None)
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        self.w3.provider.make_request = self._make_request
        # reset request func cache to re-build request_func with original make_request
        self.w3.provider._request_func_cache = (None, None)

    async def _async_mock_request_handler(self, method, params):
        if method not in self.mock_errors and method not in self.mock_results:
            return await self._make_request(method, params)

        request_id = (
            next(copy.deepcopy(self.w3.provider.request_counter))
            if hasattr(self.w3.provider, "request_counter")
            else 1
        )
        response_dict = {"jsonrpc": "2.0", "id": request_id}

        if method in self.mock_results:
            return merge(response_dict, {"result": self.mock_results[method]})
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
