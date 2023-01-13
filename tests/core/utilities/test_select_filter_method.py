import pytest

from web3._utils.filters import (
    _UseExistingFilter,
    select_filter_method,
)
from web3.exceptions import (
    Web3ValidationError,
)


@pytest.mark.parametrize(
    "value, expected",
    (
        ("latest", "new_block_filter"),
        ("pending", "new_pending_tx_filter"),
        ({"to": "0x" + "00" * 20}, "new_filter"),
    ),
)
def test_select_filter_method(value, expected):
    filter_method = select_filter_method(
        if_new_block_filter="new_block_filter",
        if_new_pending_transaction_filter="new_pending_tx_filter",
        if_new_filter="new_filter",
    )
    assert filter_method(value) == expected


@pytest.mark.parametrize(
    "value, error",
    (
        ("0x0", _UseExistingFilter),
        ("disallowed string", Web3ValidationError),
        (1, Web3ValidationError),  # filter id needs to be a hexstr
    ),
)
def test_select_filter_method_raises_error(value, error):
    filter_method = select_filter_method(
        if_new_block_filter="new_block_filter",
        if_new_pending_transaction_filter="new_pending_tx_filter",
        if_new_filter="new_filter",
    )
    with pytest.raises(error):
        filter_method(value)
