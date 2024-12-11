from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Generic,
    List,
    Optional,
    Sequence,
    TypeVar,
    Union,
)

from eth_typing import (
    Address,
    ChecksumAddress,
    HexStr,
)
from hexbytes import (
    HexBytes,
)

from web3.exceptions import (
    Web3ValueError,
)
from web3.types import (
    BlockData,
    FilterParams,
    LogReceipt,
    SyncProgress,
    TxData,
)

if TYPE_CHECKING:
    from web3 import (
        AsyncWeb3,
    )
    from web3.contract.async_contract import (
        AsyncContractEvent,
    )
    from web3.providers.persistent.subscription_manager import (
        SubscriptionManager,
    )
    from web3.types import EthSubscriptionResult  # noqa: F401


TSubscriptionResult = TypeVar("TSubscriptionResult", bound="EthSubscriptionResult")
TSubscription = TypeVar("TSubscription", bound="EthSubscription[Any]")

EthSubscriptionHandler = Callable[
    ["AsyncWeb3", TSubscription, TSubscriptionResult], Coroutine[Any, Any, None]
]


def handler_wrapper(
    handler: Optional[EthSubscriptionHandler[TSubscription, TSubscriptionResult]]
) -> Optional[EthSubscriptionHandler[TSubscription, TSubscriptionResult]]:
    if handler is None:
        return None

    async def wrapped_handler(
        async_w3: "AsyncWeb3",
        sx: TSubscription,
        result: TSubscriptionResult,
    ) -> None:
        sx.handler_call_count += 1
        sx._manager.total_handler_calls += 1
        sx._manager.logger.debug(
            "Subscription handler called.\n"
            f"    label: {sx.label}\n"
            f"    call count: {sx.handler_call_count}\n"
            f"    total handler calls: {sx._manager.total_handler_calls}"
        )
        await handler(async_w3, sx, result)

    return wrapped_handler


class EthSubscription(Generic[TSubscriptionResult]):
    _id: HexStr = None
    _manager: "SubscriptionManager" = None

    def __init__(
        self: TSubscription,
        subscription_params: Optional[Sequence[Any]] = None,
        handler: Optional[
            EthSubscriptionHandler[
                "EthSubscription[TSubscriptionResult]", TSubscriptionResult
            ]
        ] = None,
        label: Optional[str] = None,
    ) -> None:
        self._subscription_params = subscription_params
        self._handler = handler_wrapper(handler)
        self._label = label
        self.handler_call_count = 0

    @classmethod
    def _create_type_aware_subscription(
        cls,
        subscription_params: Optional[Sequence[Any]],
        handler: Optional[EthSubscriptionHandler["EthSubscription[Any]", Any]] = None,
        event: Optional["AsyncContractEvent"] = None,
        label: Optional[str] = None,
    ) -> "EthSubscription[Any]":
        subscription_type = subscription_params[0]
        subscription_arg = subscription_params[1]

        if event and subscription_type != "logs":
            raise Web3ValueError(
                "Event provided without logs subscription type. "
                "Please provide a logs subscription type."
            )

        if subscription_type == "newHeads":
            return NewHeadsSubscription(handler=handler, label=label)
        elif subscription_type == "logs":
            subscription_arg = subscription_arg or {}
            return LogsSubscription(
                **subscription_arg, handler=handler, event=event, label=label
            )
        elif subscription_type == "newPendingTransactions":
            subscription_arg = subscription_arg or False
            return PendingTxSubscription(
                full_transactions=subscription_arg, handler=handler, label=label
            )
        elif subscription_type == "syncing":
            return SyncingSubscription(handler=handler, label=label)
        else:
            # don't pass in the subscription_arg, if it's ``None``, to avoid
            # client-side errors
            params = (
                (subscription_type, subscription_arg)
                if subscription_arg
                else (subscription_type,)
            )
            return cls(params, handler=handler, label=label)

    @property
    def subscription_params(self) -> Sequence[Any]:
        return self._subscription_params

    @subscription_params.setter
    def subscription_params(self, value: Optional[Sequence[Any]]) -> None:
        self._subscription_params = value

    @property
    def label(self) -> str:
        if not self._label:
            self._label = f"{self.__class__.__name__}{self.subscription_params}"
        return self._label

    @label.setter
    def label(self, value: str) -> None:
        self._label = value

    @property
    def id(self) -> HexStr:
        if not self._id:
            raise Web3ValueError(
                "No `id` found for subscription. Once you are subscribed, "
                "an `id` will be set by the server."
            )
        return self._id

    async def unsubscribe(self) -> bool:
        return await self._manager.unsubscribe(self)


LogsSubscriptionType = EthSubscription["LogReceipt"]


class LogsSubscription(LogsSubscriptionType):
    def __init__(
        self,
        address: Optional[
            Union[Address, ChecksumAddress, List[Address], List[ChecksumAddress]]
        ] = None,
        topics: Optional[List[HexStr]] = None,
        event: "AsyncContractEvent" = None,
        handler: Optional[
            EthSubscriptionHandler[LogsSubscriptionType, "LogReceipt"]
        ] = None,
        label: Optional[str] = None,
    ) -> None:
        self.event = event
        self.address = address
        self.topics = topics

        logs_filter: "FilterParams" = {}
        if self.address:
            logs_filter["address"] = self.address
        if self.topics:
            logs_filter["topics"] = self.topics
        super().__init__(
            subscription_params=("logs", logs_filter), handler=handler, label=label
        )


NewHeadsSubscriptionType = EthSubscription["BlockData"]


class NewHeadsSubscription(NewHeadsSubscriptionType):
    def __init__(
        self,
        handler: Optional[
            EthSubscriptionHandler[NewHeadsSubscriptionType, "BlockData"]
        ] = None,
        label: Optional[str] = None,
    ) -> None:
        super().__init__(
            subscription_params=("newHeads",), handler=handler, label=label
        )


PendingTxSubscriptionType = EthSubscription[Union[HexBytes, TxData]]


class PendingTxSubscription(PendingTxSubscriptionType):
    def __init__(
        self,
        full_transactions: bool = False,
        handler: Optional[
            EthSubscriptionHandler[
                EthSubscription[Union[HexBytes, TxData]], Union[HexBytes, TxData]
            ]
        ] = None,
        label: Optional[str] = None,
    ) -> None:
        self.full_transactions = full_transactions
        self.result_type = TxData if full_transactions else HexBytes
        super().__init__(
            ("newPendingTransactions", full_transactions), handler=handler, label=label
        )


SyncingSubscriptionType = EthSubscription[SyncProgress]


class SyncingSubscription(SyncingSubscriptionType):
    def __init__(
        self,
        handler: Optional[
            EthSubscriptionHandler[SyncingSubscriptionType, SyncProgress]
        ] = None,
        label: Optional[str] = None,
    ) -> None:
        super().__init__(subscription_params=("syncing",), handler=handler, label=label)
