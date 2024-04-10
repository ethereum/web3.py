from abc import (
    abstractmethod,
)
from typing import (
    TYPE_CHECKING,
    Any,
    Type,
    Union,
)

from web3.datastructures import (
    NamedElementOnion,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )
    from web3.types import (  # noqa: F401
        AsyncMakeRequestFn,
        MakeRequestFn,
        RPCEndpoint,
        RPCResponse,
    )


class Web3Middleware:
    """
    Base class for web3.py middleware. This class is not meant to be used directly,
    but instead inherited from.
    """

    _w3: Union["AsyncWeb3", "Web3"]

    def __init__(self, w3: Union["AsyncWeb3", "Web3"]) -> None:
        self._w3 = w3

    # -- sync -- #

    def wrap_make_request(self, make_request: "MakeRequestFn") -> "MakeRequestFn":
        def middleware(method: "RPCEndpoint", params: Any) -> "RPCResponse":
            method, params = self.request_processor(method, params)
            return self.response_processor(method, make_request(method, params))

        return middleware

    def request_processor(self, method: "RPCEndpoint", params: Any) -> Any:
        return method, params

    def response_processor(
        self, method: "RPCEndpoint", response: "RPCResponse"
    ) -> "RPCResponse":
        return response

    # -- async -- #

    async def async_wrap_make_request(
        self, make_request: "AsyncMakeRequestFn"
    ) -> "AsyncMakeRequestFn":
        async def middleware(method: "RPCEndpoint", params: Any) -> "RPCResponse":
            method, params = await self.async_request_processor(method, params)
            return await self.async_response_processor(
                method,
                await make_request(method, params),
            )

        return middleware

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
    ) -> "RPCResponse":
        return response


class Web3MiddlewareBuilder(Web3Middleware):
    @staticmethod
    @abstractmethod
    def build(
        w3: Union["AsyncWeb3", "Web3"],
        *args: Any,
        **kwargs: Any,
    ) -> Web3Middleware:
        """
        Implementation should initialize the middleware class that implements it,
        load it with any of the necessary properties that it needs for processing,
        and curry for the ``w3`` argument since it isn't initially present when building
        the middleware.

        example implementation:

        ```py
        class MyMiddleware(Web3BuilderMiddleware):
            internal_property: str = None

            @staticmethod
            @curry
            def builder(user_provided_argument, w3):
                middleware = MyMiddleware(w3)
                middleware.internal_property = user_provided_argument
                return middleware

            def request_processor(self, method, params):
                ...

            def response_processor(self, method, response):
                ...

        construct_my_middleware = MyMiddleware.builder

        w3 = Web3(provider)
        my_middleware = construct_my_middleware("my argument")
        w3.middleware_onion.inject(my_middleware, layer=0)
        ```
        """
        raise NotImplementedError("Must be implemented by subclasses")


# --- type definitions --- #

Middleware = Type[Web3Middleware]
MiddlewareOnion = NamedElementOnion[str, Middleware]
