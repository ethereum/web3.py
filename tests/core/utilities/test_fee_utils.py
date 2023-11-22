import pytest

from eth_utils import (
    is_integer,
)


@pytest.mark.parametrize(
    "fee_history_rewards,expected_max_prio_calc",
    (
        (
            [[10**20], [10**20], [10**20], [10**20]],
            15 * (10**8),
        ),
        (
            [[10**2], [10**2], [10**2], [10**2], [10**2]],
            10**9,
        ),
        (
            [[0], [0], [0], [0], [0]],
            10**9,
        ),
        (
            [[1223344455], [1111111111], [1222777777], [0], [1000222111], [0], [0]],
            round(sum([1223344455, 1111111111, 1222777777, 1000222111]) / 4),
        ),
    ),
    ids=["test-max", "test-min", "test-min-all-zero-fees", "test-non-zero-average"],
)
# Test fee_utils indirectly by mocking eth_feeHistory results
# and checking against expected output
def test_fee_utils_indirectly(
    w3, fee_history_rewards, expected_max_prio_calc, request_mocker
) -> None:
    with pytest.warns(
        UserWarning,
        match="There was an issue with the method eth_maxPriorityFeePerGas. "
        "Calculating using eth_feeHistory.",
    ):
        with request_mocker(
            w3,
            mock_errors={"eth_maxPriorityFeePerGas": {}},
            mock_results={"eth_feeHistory": {"reward": fee_history_rewards}},
        ):
            max_priority_fee = w3.eth.max_priority_fee

        assert is_integer(max_priority_fee)
        assert max_priority_fee == expected_max_prio_calc
