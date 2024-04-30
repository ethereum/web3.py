from copy import (
    copy,
)
from types import (
    TracebackType,
)
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Dict,
    Generic,
    List,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
)

from web3._utils.compat import (
    Self,
)
from web3.contract.async_contract import (
    AsyncContractFunction,
)
from web3.contract.contract import (
    ContractFunction,
)
from web3.method import (
    Method,
)
from web3.types import (
    TFunc,
    TReturn,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )
    from web3.providers import (  # noqa: F401
        PersistentConnectionProvider,
    )
    from web3.providers.async_base import (  # noqa: F401
        AsyncJSONBaseProvider,
    )
    from web3.types import (  # noqa: F401
        RPCEndpoint,
        RPCResponse,
    )

BatchRequestInformation = Tuple[Tuple["RPCEndpoint", Any], Sequence[Any]]


class BatchRequestContextManager(Generic[TFunc]):
    def __init__(self, web3: Union["AsyncWeb3", "Web3"]) -> None:
        self.web3 = web3
        self._requests_info: List[BatchRequestInformation] = []
        self._async_requests_info: List[
            Coroutine[Any, Any, BatchRequestInformation]
        ] = []

    def add(self, batch_payload: TReturn) -> None:
        # When batching, we don't make a request. Instead, we will get the request
        # information and store it in the `_requests_info` list. So we have to cast the
        # apparent "request" into the BatchRequestInformation type.
        if isinstance(batch_payload, (ContractFunction, AsyncContractFunction)):
            batch_payload = batch_payload.call()  # type: ignore

        if self.web3.provider.is_async:
            self._async_requests_info.append(
                cast(Coroutine[Any, Any, BatchRequestInformation], batch_payload)
            )
        else:
            self._requests_info.append(cast(BatchRequestInformation, batch_payload))

    def add_mapping(
        self, batch_payload: Dict[Method[Callable[..., Any]], List[Any]]
    ) -> None:
        for method, params in batch_payload.items():
            for param in params:
                self.add(method(param))

    def __enter__(self) -> Self:
        self.web3.provider._is_batching = True
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException],
        exc_val: BaseException,
        exc_tb: TracebackType,
    ) -> None:
        self.web3.provider._is_batching = False

    def execute(self) -> List["RPCResponse"]:
        return self.web3.manager.make_batch_request(self._requests_info)

    # -- async -- #

    async def __aenter__(self) -> Self:
        provider = cast("AsyncJSONBaseProvider", self.web3.provider)
        provider._is_batching = True
        if provider.has_persistent_connection:
            provider = cast("PersistentConnectionProvider", provider)
            provider._batch_request_counter = next(copy(provider.request_counter))
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException],
        exc_val: BaseException,
        exc_tb: TracebackType,
    ) -> None:
        provider = cast("AsyncJSONBaseProvider", self.web3.provider)
        provider._is_batching = False
        if provider.has_persistent_connection:
            provider = cast("PersistentConnectionProvider", provider)
            provider._batch_request_counter = None

    async def async_execute(self) -> List["RPCResponse"]:
        return await self.web3.manager.async_make_batch_request(
            self._async_requests_info
        )
