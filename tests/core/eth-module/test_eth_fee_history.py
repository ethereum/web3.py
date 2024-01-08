import pytest
from unittest.mock import (
    MagicMock,
    patch,
)


@pytest.mark.parametrize(
    "fee_history_args, expected",
    (
        ((1, "latest"), (1, "latest", [])),
        ((1, "latest", []), (1, "latest", [])),
        ((1, "latest", None), (1, "latest", [])),
        ((1, "latest", [50]), (1, "latest", [50])),
    ),
)
@patch("web3.eth.Eth._fee_history", new=MagicMock())
def test_eth_fee_history_reward_percentiles_default_is_empty_list(
    w3, fee_history_args, expected
) -> None:
    w3.eth.fee_history(*fee_history_args)
    w3.eth._fee_history.assert_called_with(*expected)
