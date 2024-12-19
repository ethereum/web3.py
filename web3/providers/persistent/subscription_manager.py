import logging
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Sequence,
    Union,
    cast,
    overload,
)

from eth_typing import (
    HexStr,
)

from web3.exceptions import (
    Web3TypeError,
    Web3ValueError,
)
from web3.utils.subscriptions import (
    EthSubscription,
)

if TYPE_CHECKING:
    from web3 import AsyncWeb3  # noqa: F401
    from web3.providers.persistent import PersistentConnectionProvider  # noqa: F401


class SubscriptionManager:
    logger: logging.Logger = logging.getLogger(
        "web3.providers.persistent.subscription_manager"
    )
    total_handler_calls: int = 0

    def __init__(self, w3: "AsyncWeb3") -> None:
        self._w3 = w3
        self._provider = cast("PersistentConnectionProvider", w3.provider)
        self.subscriptions: List[EthSubscription[Any]] = []
        self._subscriptions_by_id: Dict[HexStr, EthSubscription[Any]] = {}
        self._subscriptions_by_label: Dict[str, EthSubscription[Any]] = {}

    def get_by_id(self, sub_id: HexStr) -> EthSubscription[Any]:
        return self._subscriptions_by_id.get(sub_id)

    def get_by_label(self, label: str) -> EthSubscription[Any]:
        return self._subscriptions_by_label.get(label)

    @overload
    async def subscribe(self, subscriptions: EthSubscription[Any]) -> HexStr:
        ...

    @overload
    async def subscribe(
        self, subscriptions: Sequence[EthSubscription[Any]]
    ) -> List[HexStr]:
        ...

    async def subscribe(
        self, subscriptions: Union[EthSubscription[Any], Sequence[EthSubscription[Any]]]
    ) -> Union[HexStr, List[HexStr]]:
        if isinstance(subscriptions, EthSubscription):
            if subscriptions.label in self._subscriptions_by_label:
                raise Web3ValueError(
                    "Subscription label already exists. Subscriptions must have "
                    f"unique labels.\n    label: {subscriptions.label}"
                )

            subscriptions.manager = self
            sub_id = await self._w3.eth._subscribe(*subscriptions.subscription_params)
            subscriptions._id = sub_id
            self._subscriptions_by_label[subscriptions.label] = subscriptions
            self._subscriptions_by_id[subscriptions.id] = subscriptions
            self.subscriptions.append(subscriptions)
            self.logger.info(
                "Successfully subscribed to subscription:\n    "
                f"label: {subscriptions.label}\n    id: {sub_id}"
            )
            return sub_id
        elif isinstance(subscriptions, Sequence):
            if len(subscriptions) == 0:
                raise Web3ValueError("No subscriptions provided.")

            sub_ids: List[HexStr] = []
            for sub in subscriptions:
                await self.subscribe(sub)
            return sub_ids
        raise Web3TypeError("Expected a Subscription or a sequence of Subscriptions.")

    async def unsubscribe(self, subscription: EthSubscription[Any]) -> bool:
        """
        Used to unsubscribe from a subscription that is being managed by the
        subscription manager.

        :param subscription: The subscription to unsubscribe from.
        :type subscription: EthSubscription
        :return: `True` if unsubscribing was successful, `False` otherwise.
        :rtype: bool
        """
        if subscription not in self.subscriptions:
            raise Web3ValueError(
                "Subscription not found or is not being managed by the subscription "
                f"manager.\n    label: {subscription.label}\n    id: {subscription._id}"
            )
        if await self._w3.eth._unsubscribe(subscription.id):
            self.subscriptions.remove(subscription)
            self._subscriptions_by_id.pop(subscription.id)
            self._subscriptions_by_label.pop(subscription.label)
            self.logger.info(
                "Successfully unsubscribed from subscription:\n    "
                f"label: {subscription.label}\n    id: {subscription.id}"
            )
            return True
        return False

    async def unsubscribe_all(self) -> None:
        """
        Used to unsubscribe from all subscriptions that are being managed by the
        subscription manager.

        :return: None
        """
        unsubscribed = [
            await self.unsubscribe(sub) for sub in self.subscriptions.copy()
        ]
        if all(unsubscribed):
            self.logger.info("Successfully unsubscribed from all subscriptions.")
        else:
            if len(self.subscriptions) > 0:
                self.logger.warning(
                    "Failed to unsubscribe from all subscriptions. Some subscriptions "
                    f"are still active.\n    subscriptions={self.subscriptions}"
                )

    async def _handle_subscriptions(self, run_forever: bool = False) -> None:
        while run_forever or len(self.subscriptions) > 0:
            await self._w3.manager._get_next_message()

    async def handle_subscriptions(self, run_forever: bool = False) -> None:
        """
        Used to process all subscriptions. It will run until all subscriptions are
        unsubscribed from or, if `run_forever` is set to `True`, it will run
        indefinitely.

        :param run_forever: If `True`, the method will run indefinitely.
        :type run_forever: bool
        :return: None
        """
        await self._handle_subscriptions(run_forever=run_forever)
