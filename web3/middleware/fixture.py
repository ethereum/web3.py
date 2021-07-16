from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
)

from web3.types import (
    AsyncMiddleware,
    Middleware,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


def construct_fixture_middleware(fixtures: Dict[RPCEndpoint, Any]) -> Middleware:
    """
    Constructs a middleware which returns a static response for any method
    which is found in the provided fixtures.
    """
    def fixture_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any], _: "Web3"
    ) -> Callable[[RPCEndpoint, Any], RPCResponse]:
        def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
            if method in fixtures:
                result = fixtures[method]
                return {'result': result}
            else:
                return make_request(method, params)
        return middleware
    return fixture_middleware


def construct_result_generator_middleware(
    result_generators: Dict[RPCEndpoint, Any]
) -> Middleware:
    """
    Constructs a middleware which intercepts requests for any method found in
    the provided mapping of endpoints to generator functions, returning
    whatever response the generator function returns.  Callbacks must be
    functions with the signature `fn(method, params)`.
    """
    def result_generator_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any], _: "Web3"
    ) -> Callable[[RPCEndpoint, Any], RPCResponse]:
        def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
            if method in result_generators:
                result = result_generators[method](method, params)
                return {'result': result}
            else:
                return make_request(method, params)
        return middleware
    return result_generator_middleware


def construct_error_generator_middleware(
    error_generators: Dict[RPCEndpoint, Any]
) -> Middleware:
    """
    Constructs a middleware which intercepts requests for any method found in
    the provided mapping of endpoints to generator functions, returning
    whatever error message the generator function returns.  Callbacks must be
    functions with the signature `fn(method, params)`.
    """
    def error_generator_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any], _: "Web3"
    ) -> Callable[[RPCEndpoint, Any], RPCResponse]:
        def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
            if method in error_generators:
                error_msg = error_generators[method](method, params)
                return {'error': error_msg}
            else:
                return make_request(method, params)
        return middleware
    return error_generator_middleware


# --- async --- #

async def async_construct_result_generator_middleware(
    result_generators: Dict[RPCEndpoint, Any]
) -> Middleware:
    """
    Constructs a middleware which returns a static response for any method
    which is found in the provided fixtures.
    """
    async def result_generator_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any], _: "Web3"
    ) -> AsyncMiddleware:
        async def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
            if method in result_generators:
                result = result_generators[method](method, params)
                return {'result': result}
            else:
                return await make_request(method, params)
        return middleware
    return result_generator_middleware


async def async_construct_error_generator_middleware(
    error_generators: Dict[RPCEndpoint, Any]
) -> Middleware:
    """
    Constructs a middleware which intercepts requests for any method found in
    the provided mapping of endpoints to generator functions, returning
    whatever error message the generator function returns.  Callbacks must be
    functions with the signature `fn(method, params)`.
    """
    async def error_generator_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any], _: "Web3"
    ) -> AsyncMiddleware:
        async def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
            if method in error_generators:
                error_msg = error_generators[method](method, params)
                return {'error': error_msg}
            else:
                return await make_request(method, params)
        return middleware
    return error_generator_middleware
