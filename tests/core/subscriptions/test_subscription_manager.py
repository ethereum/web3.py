import itertools
import pytest
from unittest.mock import (
    AsyncMock,
)

import pytest_asyncio

from web3 import (
    AsyncWeb3,
    PersistentConnectionProvider,
)
from web3.exceptions import (
    Web3ValueError,
)
from web3.providers.persistent.subscription_manager import (
    SubscriptionManager,
)
from web3.utils.subscriptions import (
    LogsSubscription,
    NewHeadsSubscription,
    PendingTxSubscription,
)


class MockProvider(PersistentConnectionProvider):
    socket_recv = AsyncMock()
    socket_send = AsyncMock()


@pytest_asyncio.fixture
async def subscription_manager():
    countr = itertools.count()
    _w3 = AsyncWeb3(MockProvider())
    _w3.eth._subscribe = AsyncMock()
    _w3.eth._subscribe.side_effect = lambda *_: f"0x{str(next(countr))}"
    _w3.eth._unsubscribe = AsyncMock()
    _w3.eth._unsubscribe.return_value = True
    yield SubscriptionManager(_w3)


@pytest.mark.asyncio
async def test_subscription_manager_raises_for_sx_with_the_same_label(
    subscription_manager,
):
    sx1 = NewHeadsSubscription(label="foo")
    await subscription_manager.subscribe(sx1)

    with pytest.raises(
        Web3ValueError,
        match="Subscription label already exists. Subscriptions must have unique "
        "labels.\n    label: foo",
    ):
        sx2 = LogsSubscription(label="foo")
        await subscription_manager.subscribe(sx2)

    # make sure the subscription was subscribed to and not added to the manager
    assert subscription_manager.subscriptions == [sx1]
    assert subscription_manager._subscriptions_by_label == {"foo": sx1}
    assert subscription_manager._subscriptions_by_id == {"0x0": sx1}


@pytest.mark.asyncio
async def test_subscription_manager_get_by_id(subscription_manager):
    sx = NewHeadsSubscription(label="foo")
    await subscription_manager.subscribe(sx)
    assert subscription_manager.get_by_id("0x0") == sx
    assert subscription_manager.get_by_id("0x1") is None


@pytest.mark.asyncio
async def test_subscription_manager_get_by_label(subscription_manager):
    sx = NewHeadsSubscription(label="foo")
    await subscription_manager.subscribe(sx)
    assert subscription_manager.get_by_label("foo") == sx
    assert subscription_manager.get_by_label("bar") is None


@pytest.mark.asyncio
async def test_unsubscribe_one_by_one_clears_all_subscriptions(
    subscription_manager,
):
    sx1 = NewHeadsSubscription(label="foo")
    sx2 = PendingTxSubscription(label="bar")
    await subscription_manager.subscribe(sx1)
    await subscription_manager.subscribe(sx2)

    await subscription_manager.unsubscribe(sx1)
    assert subscription_manager.subscriptions == [sx2]

    await subscription_manager.unsubscribe(sx2)
    assert subscription_manager.subscriptions == []


@pytest.mark.asyncio
async def test_unsubscribe_all_clears_all_subscriptions(subscription_manager):
    sx1 = NewHeadsSubscription(label="foo")
    sx2 = PendingTxSubscription(label="bar")
    await subscription_manager.subscribe([sx1, sx2])

    await subscription_manager.unsubscribe_all()
    assert subscription_manager.subscriptions == []
    assert subscription_manager._subscriptions_by_id == {}
    assert subscription_manager._subscriptions_by_label == {}
