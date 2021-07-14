import logging
from typing import (  # noqa: F401
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    List,
    NoReturn,
    Optional,
    Sequence,
    Tuple,
    Union,
)
import uuid
from uuid import UUID

from eth_utils.toolz import (
    pipe,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.decorators import (
    deprecated_for,
)
from web3._utils.threads import (  # noqa: F401
    ThreadWithReturn,
    spawn,
)
from web3.datastructures import (
    NamedElementOnion,
)
from web3.middleware import (
    abi_middleware,
    attrdict_middleware,
    buffered_gas_estimate_middleware,
    gas_price_strategy_middleware,
    name_to_address_middleware,
    pythonic_middleware,
    request_parameter_normalizer,
    validation_middleware,
)
from web3.providers import (
    AutoProvider,
    BaseProvider,
)
from web3.types import (  # noqa: F401
    Middleware,
    MiddlewareOnion,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


NULL_RESPONSES = [None, HexBytes('0x'), '0x']


def apply_error_formatters(
    error_formatters: Callable[..., Any],
    response: RPCResponse,
) -> RPCResponse:
    if error_formatters:
        formatted_resp = pipe(response, error_formatters)
        return formatted_resp
    else:
        return response


def apply_null_result_formatters(
    null_result_formatters: Callable[..., Any],
    response: RPCResponse,
    params: Optional[Any] = None,
) -> RPCResponse:
    if null_result_formatters:
        formatted_resp = pipe(params, null_result_formatters)
        return formatted_resp
    else:
        return response


class RequestManager:
    logger = logging.getLogger("web3.RequestManager")

    def __init__(
        self,
        web3: 'Web3',
        provider: Optional[BaseProvider] = None,
        middlewares: Optional[Sequence[Tuple[Middleware, str]]] = None
    ) -> None:
        self.web3 = web3
        self.pending_requests: Dict[UUID, ThreadWithReturn[RPCResponse]] = {}

        if middlewares is None:
            middlewares = self.default_middlewares(web3)

        self.middleware_onion: MiddlewareOnion = NamedElementOnion(middlewares)

        if provider is None:
            self.provider = AutoProvider()
        else:
            self.provider = provider

    web3: 'Web3' = None
    _provider = None

    @property
    def provider(self) -> BaseProvider:
        return self._provider

    @provider.setter
    def provider(self, provider: BaseProvider) -> None:
        self._provider = provider

    @staticmethod
    def default_middlewares(
        web3: 'Web3'
    ) -> List[Tuple[Middleware, str]]:
        """
        List the default middlewares for the request manager.
        Leaving ens unspecified will prevent the middleware from resolving names.
        """
        return [
            (request_parameter_normalizer, 'request_param_normalizer'),  # Delete
            (gas_price_strategy_middleware, 'gas_price_strategy'),  # Add Async
            (name_to_address_middleware(web3), 'name_to_address'),  # Add Async
            (attrdict_middleware, 'attrdict'),  # Delete
            (pythonic_middleware, 'pythonic'),  # Delete
            (validation_middleware, 'validation'),  # Add async
            (abi_middleware, 'abi'),  # Delete
            (buffered_gas_estimate_middleware, 'gas_estimate'),
        ]

    #
    # Provider requests and response
    #
    def _make_request(
        self, method: Union[RPCEndpoint, Callable[..., RPCEndpoint]], params: Any
    ) -> RPCResponse:
        request_func = self.provider.request_func(
            self.web3,
            self.middleware_onion)
        self.logger.debug("Making request. Method: %s", method)
        return request_func(method, params)

    async def _coro_make_request(
        self, method: Union[RPCEndpoint, Callable[..., RPCEndpoint]], params: Any
    ) -> RPCResponse:
        # type ignored b/c request_func is an awaitable in async model
        request_func = await self.provider.request_func(  # type: ignore
            self.web3,
            self.middleware_onion)
        self.logger.debug("Making request. Method: %s", method)
        return await request_func(method, params)

    def formatted_response(
        self,
        response: RPCResponse,
        params: Any,
        error_formatters: Optional[Callable[..., Any]] = None,
        null_result_formatters: Optional[Callable[..., Any]] = None,
    ) -> Any:
        if "error" in response:
            apply_error_formatters(error_formatters, response)
            raise ValueError(response["error"])
        elif response['result'] in NULL_RESPONSES:
            # null_result_formatters raise either a BlockNotFound
            # or a TransactionNotFound error, depending on the method called
            apply_null_result_formatters(null_result_formatters, response, params)

        return response['result']

    def request_blocking(
        self,
        method: Union[RPCEndpoint, Callable[..., RPCEndpoint]],
        params: Any,
        error_formatters: Optional[Callable[..., Any]] = None,
        null_result_formatters: Optional[Callable[..., Any]] = None,
    ) -> Any:
        """
        Make a synchronous request using the provider
        """
        response = self._make_request(method, params)
        return self.formatted_response(response,
                                       params,
                                       error_formatters,
                                       null_result_formatters)

    async def coro_request(
        self,
        method: Union[RPCEndpoint, Callable[..., RPCEndpoint]],
        params: Any,
        error_formatters: Optional[Callable[..., Any]] = None,
        null_result_formatters: Optional[Callable[..., Any]] = None,
    ) -> Any:
        """
        Couroutine for making a request using the provider
        """
        response = await self._coro_make_request(method, params)
        return self.formatted_response(response,
                                       params,
                                       error_formatters,
                                       null_result_formatters)

    @deprecated_for("coro_request")
    def request_async(self, raw_method: str, raw_params: Any) -> UUID:
        request_id = uuid.uuid4()
        self.pending_requests[request_id] = spawn(
            self.request_blocking,
            raw_method=raw_method,
            raw_params=raw_params,
        )
        return request_id

    def receive_blocking(self, request_id: UUID, timeout: Optional[float] = None) -> Any:
        try:
            request = self.pending_requests.pop(request_id)
        except KeyError:
            raise KeyError("Request for id:{0} not found".format(request_id))
        else:
            response = request.get(timeout=timeout)

        if "error" in response:
            raise ValueError(response["error"])

        return response['result']

    def receive_async(self, request_id: UUID, *args: Any, **kwargs: Any) -> NoReturn:
        raise NotImplementedError("Callback pattern not implemented")
