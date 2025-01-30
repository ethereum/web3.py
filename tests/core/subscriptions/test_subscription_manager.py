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
async def test_subscription_default_labels_are_unique(subscription_manager):
    sub1 = NewHeadsSubscription()
    sub2 = NewHeadsSubscription()
    sub3 = NewHeadsSubscription()
    sub4 = NewHeadsSubscription()

    sub_ids = await subscription_manager.subscribe([sub1, sub2, sub3, sub4])
    assert sub_ids == ["0x0", "0x1", "0x2", "0x3"]

    assert sub1.label != sub2.label != sub3.label != sub4.label
    assert sub1.label == "NewHeadsSubscription('newHeads',)"
    assert sub2.label == "NewHeadsSubscription('newHeads',)#2"
    assert sub3.label == "NewHeadsSubscription('newHeads',)#3"
    assert sub4.label == "NewHeadsSubscription('newHeads',)#4"

    # assert no issues unsubscribing
    await subscription_manager.unsubscribe_all()

    assert subscription_manager.subscriptions == []
    assert subscription_manager._subscription_container.subscriptions == []
    assert subscription_manager._subscription_container.subscriptions_by_id == {}
    assert subscription_manager._subscription_container.subscriptions_by_label == {}


@pytest.mark.asyncio
async def test_subscription_manager_raises_for_new_subs_with_the_same_custom_label(
    subscription_manager,
):
    sub1 = NewHeadsSubscription(label="foo")
    sub2 = LogsSubscription(label="foo")

    with pytest.raises(
        Web3ValueError,
        match="Subscription label already exists. Subscriptions must have unique "
        "labels.\n    label: foo",
    ):
        await subscription_manager.subscribe([sub1, sub2])

    # make sure the subscription was subscribed to and not added to the manager
    assert subscription_manager.subscriptions == [sub1]
    sub_container = subscription_manager._subscription_container
    assert len(sub_container) == 1
    assert sub_container.subscriptions == [sub1]
    assert sub_container.subscriptions_by_id == {"0x0": sub1}
    assert sub_container.subscriptions_by_label == {"foo": sub1}


@pytest.mark.asyncio
async def test_subscription_manager_get_by_id(subscription_manager):
    sub = NewHeadsSubscription(label="foo")
    await subscription_manager.subscribe(sub)
    assert subscription_manager.get_by_id("0x0") == sub
    assert subscription_manager.get_by_id("0x1") is None


@pytest.mark.asyncio
async def test_subscription_manager_get_by_label(subscription_manager):
    sub = NewHeadsSubscription(label="foo")
    await subscription_manager.subscribe(sub)
    assert subscription_manager.get_by_label("foo") == sub
    assert subscription_manager.get_by_label("bar") is None


@pytest.mark.asyncio
async def test_unsubscribe_one_by_one_clears_all_subscriptions(
    subscription_manager,
):
    sub1 = NewHeadsSubscription(label="foo")
    sub2 = PendingTxSubscription(label="bar")
    await subscription_manager.subscribe(sub1)
    await subscription_manager.subscribe(sub2)

    await subscription_manager.unsubscribe(sub1)
    assert subscription_manager.subscriptions == [sub2]

    await subscription_manager.unsubscribe(sub2)
    assert subscription_manager.subscriptions == []


@pytest.mark.asyncio
async def test_unsubscribe_all_clears_all_subscriptions(subscription_manager):
    sub1 = NewHeadsSubscription(label="foo")
    sub2 = PendingTxSubscription(label="bar")
    await subscription_manager.subscribe([sub1, sub2])
    assert subscription_manager.subscriptions == [sub1, sub2]

    await subscription_manager.unsubscribe_all()
    assert subscription_manager.subscriptions == []

    sub_container = subscription_manager._subscription_container
    assert len(sub_container) == 0
    assert sub_container.subscriptions == []
    assert sub_container.subscriptions_by_id == {}
    assert sub_container.subscriptions_by_label == {}


@pytest.mark.asyncio
async def test_unsubscribe_with_hex_ids(subscription_manager):
    sub1 = NewHeadsSubscription()
    sub2 = PendingTxSubscription()
    sub3 = NewHeadsSubscription()
    sub4 = LogsSubscription()

    sub_id1, sub_id2, sub_id3, sub_id4 = await subscription_manager.subscribe(
        [sub1, sub2, sub3, sub4]
    )

    assert subscription_manager.subscriptions == [sub1, sub2, sub3, sub4]

    assert await subscription_manager.unsubscribe(sub_id1) is True
    assert subscription_manager.subscriptions == [sub2, sub3, sub4]

    assert await subscription_manager.unsubscribe([sub_id2, sub_id3]) is True
    assert subscription_manager.subscriptions == [sub4]
