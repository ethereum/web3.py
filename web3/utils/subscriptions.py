from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    List,
    Optional,
    Sequence,
    Union,
)

from eth_typing import (
    Address,
    ChecksumAddress,
    HexStr,
)

from web3.exceptions import (
    Web3ValueError,
)

if TYPE_CHECKING:
    from web3 import AsyncWeb3  # noqa: F401
    from web3.providers.persistent.subscription_manager import (
        SubscriptionManager,
    )
    from web3.types import (
        FilterParams,
    )

EthSubscriptionHandler = Callable[
    ["AsyncWeb3", "EthSubscription", Any], Coroutine[Any, Any, None]
]


class EthSubscription:
    """
    A base class for all eth_subscription types.
    """

    _id: HexStr = None
    _manager: "SubscriptionManager" = None

    def __init__(
        self,
        subscription_params: Optional[Sequence[Any]] = None,
        handler: Optional[EthSubscriptionHandler] = None,
        label: Optional[str] = None,
    ) -> None:
        self._handler = handler
        self._subscription_params = subscription_params
        self._label = label

    # -- properties -- #

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
                "No `id` found for subscription. Once you are subscribed to this "
                "subscription, an `id` will be set by the server."
            )

        return self._id

    # -- methods -- #

    async def unsubscribe(self) -> bool:
        """
        Unsubscribes from the subscription using the underlying manager assigned at
        subscription creation.
        """
        return await self._manager.unsubscribe(self)


class LogsSubscription(EthSubscription):
    def __init__(
        self,
        address: Optional[
            Union[Address, ChecksumAddress, List[Address], List[ChecksumAddress]]
        ] = None,
        topics: Optional[List[HexStr]] = None,
        handler: Optional[EthSubscriptionHandler] = None,
        label: Optional[str] = None,
    ) -> None:
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


class NewHeadsSubscription(EthSubscription):
    def __init__(
        self,
        handler: Optional[EthSubscriptionHandler] = None,
        label: Optional[str] = None,
    ) -> None:
        super().__init__(
            subscription_params=("newHeads",), handler=handler, label=label
        )


class PendingTxSubscription(EthSubscription):
    def __init__(
        self,
        full_transactions: bool = False,
        handler: Optional[EthSubscriptionHandler] = None,
        label: Optional[str] = None,
    ) -> None:
        self.full_transactions = full_transactions
        super().__init__(
            ("newPendingTransactions", full_transactions),
            handler=handler,
            label=label,
        )


class SyncingSubscription(EthSubscription):
    def __init__(
        self,
        handler: Optional[EthSubscriptionHandler] = None,
        label: Optional[str] = None,
    ) -> None:
        super().__init__(subscription_params=("syncing",), handler=handler, label=label)
