from abc import abstractmethod
from typing import (
    Sequence,
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )
    from web3.types import (
        RPCEndpoint,
        RPCResponse,
    )


WEB3 = TypeVar("WEB3", "AsyncWeb3", "Web3")


class Web3Middleware:
    """
    Base class for web3.py middleware. This class is not meant to be used directly,
    but instead inherited from.
    """

    _w3: WEB3

    def __init__(self, w3: WEB3) -> None:
        self._w3 = w3

    def _wrap_make_request(self, make_request):
        def middleware(method: "RPCEndpoint", params: Any) -> "RPCResponse":
            method, params = self.request_processor(method, params)
            return self.response_processor(method, make_request(method, params))

        return middleware

    # -- sync -- #

    def request_processor(self, method: "RPCEndpoint", params: Any) -> Any:
        return method, params

    def response_processor(self, method: "RPCEndpoint", response: "RPCResponse") -> Any:
        return response

    # -- async -- #

    async def async_request_processor(
        self,
        method: "RPCEndpoint",
        params: Any,
    ) -> Any:
        return method, params

    async def async_response_processor(
        self,
        method: "RPCEndpoint",
        response: "RPCResponse",
    ) -> Any:
        return response


class Web3MiddlewareBuilder(Web3Middleware):
    @staticmethod
    @abstractmethod
    def build_middleware(
        w3: Union["AsyncWeb3", "Web3"],
        *args: Any,
        **kwargs: Any,
    ):
        """
        Implementation should initialize the middleware class that implements it,
        load it with any of the necessary properties that it needs for processing,
        and curry for the ``w3`` argument since it isn't initially present when building
        the middleware.

        example implementation:

        ```py
        class MyMiddleware(Web3BuilderMiddleware):

            @staticmethod
            @curry
            def build_middleware(w3, request_formatters=None, response_formatters=None):
                middleware = MyMiddleware(w3)
                middleware.request_formatters = request_formatters
                middleware.response_formatters = response_formatters

                return middleware
        ```
        """
        raise NotImplementedError("Must be implemented by subclasses")
