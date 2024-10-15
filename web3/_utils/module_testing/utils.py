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

    ************************************************************************************
    Important: When mocking results, it's important to keep in mind the types that
        clients return. For example, what we commonly translate to integers are returned
        as hex strings in the RPC response and should be mocked as such for more
        accurate testing.
    ************************************************************************************


    Example:
    -------

        def test_my_w3(w3, request_mocker):
            assert w3.eth.block_number == 0

            with request_mocker(w3, mock_results={"eth_blockNumber": "0x1"}):
                assert w3.eth.block_number == 1

            assert w3.eth.block_number == 0

    Example with async and a mocked response object:
    -----------------------------------------------

        async def test_my_w3(async_w3, request_mocker):
            def _iter_responses():
                    while True:
                        yield {"error": {"message": "transaction indexing in progress"}}
                        yield {"error": {"message": "transaction indexing in progress"}}
                        yield {"result": {"status": "0x1"}}

            iter_responses = _iter_responses()

            async with request_mocker(
                async_w3,
                mock_responses={
                    "eth_getTransactionReceipt": lambda *_: next(iter_responses)
                },
            ):
                # assert that the first two error responses are handled and the result
                # is eventually returned when present
                assert await w3.eth.get_transaction_receipt("0x1") == "0x1"


    - ``mock_results`` is a dict mapping method names to the desired "result" object of
        the RPC response.
    - ``mock_errors`` is a dict mapping method names to the desired
        "error" object of the RPC response.
    -``mock_responses`` is a dict mapping method names to the entire RPC response
        object. This can be useful if you wish to return an iterator which returns
        different responses on each call to the method.

    If a method name is not present in any of the dicts above, the request is made as
    usual.

    """

    def __init__(
        self,
        w3: Union["AsyncWeb3", "Web3"],
        mock_results: Dict[Union["RPCEndpoint", str], Any] = None,
        mock_errors: Dict[Union["RPCEndpoint", str], Any] = None,
        mock_responses: Dict[Union["RPCEndpoint", str], Any] = None,
    ):
        self.w3 = w3
        self.mock_results = mock_results or {}
        self.mock_errors = mock_errors or {}
        self.mock_responses = mock_responses or {}
        self._make_request: Union[
            "AsyncMakeRequestFn", "MakeRequestFn"
        ] = w3.provider.make_request

    def __enter__(self) -> "Self":
        # mypy error: Cannot assign to a method
        self.w3.provider.make_request = self._mock_request_handler  # type: ignore[method-assign]  # noqa: E501
        # reset request func cache to re-build request_func with mocked make_request
        self.w3.provider._request_func_cache = (None, None)

        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        # mypy error: Cannot assign to a method
        self.w3.provider.make_request = self._make_request  # type: ignore[assignment]
        # reset request func cache to re-build request_func with original make_request
        self.w3.provider._request_func_cache = (None, None)

    def _mock_request_handler(
        self, method: "RPCEndpoint", params: Any
    ) -> "RPCResponse":
        self.w3 = cast("Web3", self.w3)
        self._make_request = cast("MakeRequestFn", self._make_request)

        if all(
            method not in mock_dict
            for mock_dict in (self.mock_errors, self.mock_results, self.mock_responses)
        ):
            return self._make_request(method, params)

        request_id = (
            next(copy.deepcopy(self.w3.provider.request_counter))
            if hasattr(self.w3.provider, "request_counter")
            else 1
        )
        response_dict = {"jsonrpc": "2.0", "id": request_id}

        if method in self.mock_responses:
            mock_return = self.mock_responses[method]
            if callable(mock_return):
                mock_return = mock_return(method, params)

            if "result" in mock_return:
                mock_return = {"result": mock_return["result"]}
            elif "error" in mock_return:
                mock_return = self._create_error_object(mock_return["error"])

            mocked_response = merge(response_dict, mock_return)
        elif method in self.mock_results:
            mock_return = self.mock_results[method]
            if callable(mock_return):
                mock_return = mock_return(method, params)
            mocked_response = merge(response_dict, {"result": mock_return})
        elif method in self.mock_errors:
            error = self.mock_errors[method]
            if callable(error):
                error = error(method, params)
            mocked_response = merge(response_dict, self._create_error_object(error))
        else:
            raise Exception("Invariant: unreachable code path")

        decorator = getattr(self._make_request, "_decorator", None)
        if decorator is not None:
            # If the original make_request was decorated, we need to re-apply
            # the decorator to the mocked make_request. This is necessary for
            # the request caching decorator to work properly.
            return decorator(lambda *_: mocked_response)(
                self.w3.provider, method, params
            )
        else:
            return mocked_response

    # -- async -- #

    async def __aenter__(self) -> "Self":
        # mypy error: Cannot assign to a method
        self.w3.provider.make_request = self._async_mock_request_handler  # type: ignore[method-assign]  # noqa: E501
        # reset request func cache to re-build request_func with mocked make_request
        self.w3.provider._request_func_cache = (None, None)
        return self

    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        # mypy error: Cannot assign to a method
        self.w3.provider.make_request = self._make_request  # type: ignore[assignment]
        # reset request func cache to re-build request_func with original make_request
        self.w3.provider._request_func_cache = (None, None)

    async def _async_mock_request_handler(
        self, method: "RPCEndpoint", params: Any
    ) -> "RPCResponse":
        self.w3 = cast("AsyncWeb3", self.w3)
        self._make_request = cast("AsyncMakeRequestFn", self._make_request)

        if all(
            method not in mock_dict
            for mock_dict in (self.mock_errors, self.mock_results, self.mock_responses)
        ):
            return await self._make_request(method, params)

        request_id = (
            next(copy.deepcopy(self.w3.provider.request_counter))
            if hasattr(self.w3.provider, "request_counter")
            else 1
        )
        response_dict = {"jsonrpc": "2.0", "id": request_id}

        if method in self.mock_responses:
            mock_return = self.mock_responses[method]

            if callable(mock_return):
                mock_return = mock_return(method, params)
            elif iscoroutinefunction(mock_return):
                # this is the "correct" way to mock the async make_request
                mock_return = await mock_return(method, params)

            if "result" in mock_return:
                mock_return = {"result": mock_return["result"]}
            elif "error" in mock_return:
                mock_return = self._create_error_object(mock_return["error"])

            mocked_result = merge(response_dict, mock_return)
        elif method in self.mock_results:
            mock_return = self.mock_results[method]
            if callable(mock_return):
                # handle callable to make things easier since we're mocking
                mock_return = mock_return(method, params)
            elif iscoroutinefunction(mock_return):
                # this is the "correct" way to mock the async make_request
                mock_return = await mock_return(method, params)

            mocked_result = merge(response_dict, {"result": mock_return})

        elif method in self.mock_errors:
            error = self.mock_errors[method]
            if callable(error):
                error = error(method, params)
            elif iscoroutinefunction(error):
                error = await error(method, params)
            mocked_result = merge(response_dict, self._create_error_object(error))

        else:
            raise Exception("Invariant: unreachable code path")

        decorator = getattr(self._make_request, "_decorator", None)
        if decorator is not None:
            # If the original make_request was decorated, we need to re-apply
            # the decorator to the mocked make_request. This is necessary for
            # the request caching decorator to work properly.

            async def _coro(
                _provider: Any, _method: "RPCEndpoint", _params: Any
            ) -> "RPCResponse":
                return mocked_result

            return await decorator(_coro)(self.w3.provider, method, params)
        else:
            return mocked_result

    @staticmethod
    def _create_error_object(error: Dict[str, Any]) -> Dict[str, Any]:
        code = error.get("code", -32000)
        message = error.get("message", "Mocked error")
        return {"error": merge({"code": code, "message": message}, error)}
