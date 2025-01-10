import pytest

from web3.utils.subscriptions import (
    LogsSubscription,
    NewHeadsSubscription,
    PendingTxSubscription,
    SyncingSubscription,
)


@pytest.fixture
def handler():
    pass


def test_new_heads_subscription_properties(handler):
    new_heads_subscription = NewHeadsSubscription(
        handler=handler, label="new heads label"
    )
    assert new_heads_subscription._handler is handler
    assert new_heads_subscription.label == "new heads label"
    assert new_heads_subscription.subscription_params == ("newHeads",)


def test_pending_tx_subscription_properties_default(handler):
    pending_tx_subscription = PendingTxSubscription(
        handler=handler, label="pending tx label"
    )
    assert pending_tx_subscription._handler is handler
    assert pending_tx_subscription.label == "pending tx label"
    assert pending_tx_subscription.full_transactions is False
    assert pending_tx_subscription.subscription_params == (
        "newPendingTransactions",
        False,
    )


def test_pending_tx_subscription_properties_full_transactions(handler):
    pending_tx_subscription = PendingTxSubscription(
        full_transactions=True, handler=handler, label="pending tx label"
    )
    assert pending_tx_subscription._handler is handler
    assert pending_tx_subscription.label == "pending tx label"
    assert pending_tx_subscription.full_transactions is True
    assert pending_tx_subscription.subscription_params == (
        "newPendingTransactions",
        True,
    )


def test_logs_subscription_properties_default(handler):
    logs_subscription = LogsSubscription(handler=handler, label="logs label")
    assert logs_subscription._handler is handler
    assert logs_subscription.label == "logs label"
    assert logs_subscription.subscription_params == ("logs", {})
    assert logs_subscription.address is None
    assert logs_subscription.topics is None


def test_logs_subscription_properties(handler):
    address = "0x1234567890123456789012345678901234567890"
    topics = [
        "0x0000000000000000000000000000000000000000000000000000000000000001",
        "0x0000000000000000000000000000000000000000000000000000000000000002",
    ]
    logs_subscription = LogsSubscription(
        address=address, topics=topics, handler=handler, label="logs label"
    )
    assert logs_subscription._handler is handler
    assert logs_subscription.label == "logs label"
    assert logs_subscription.subscription_params == (
        "logs",
        {"address": address, "topics": topics},
    )
    assert logs_subscription.address == address
    assert logs_subscription.topics == topics


def test_syncing_subscription_properties(handler):
    syncing_subscription = SyncingSubscription(handler=handler, label="syncing label")
    assert syncing_subscription._handler is handler
    assert syncing_subscription.label == "syncing label"
    assert syncing_subscription.subscription_params == ("syncing",)
