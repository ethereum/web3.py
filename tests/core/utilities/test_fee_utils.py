import pytest

from eth_utils import (
    is_integer,
)

from web3.middleware import (
    construct_error_generator_middleware,
    construct_result_generator_middleware,
)
from web3.types import (
    RPCEndpoint,
)


@pytest.mark.parametrize(
    'fee_history_rewards,expected_max_prio_calc',
    (
        (
            [[10 ** 20], [10 ** 20], [10 ** 20], [10 ** 20]],
            15 * (10 ** 8),
        ),
        (
            [[10 ** 2], [10 ** 2], [10 ** 2], [10 ** 2], [10 ** 2]],
            10 ** 9,
        ),
        (
            [[0], [0], [0], [0], [0]],
            10 ** 9,
        ),
        (
            [[1223344455], [1111111111], [1222777777], [0], [1000222111], [0], [0]],
            round(sum([1223344455, 1111111111, 1222777777, 1000222111]) / 4),
        ),
    ),
    ids=[
        'test-max', 'test-min', 'test-min-all-zero-fees', 'test-non-zero-average'
    ]
)
# Test fee_utils indirectly by mocking eth_feeHistory results and checking against expected output
def test_fee_utils_indirectly(
    web3, fee_history_rewards, expected_max_prio_calc
) -> None:
    fail_max_prio_middleware = construct_error_generator_middleware(
        {RPCEndpoint("eth_maxPriorityFeePerGas"): lambda *_: ''}
    )
    fee_history_result_middleware = construct_result_generator_middleware(
        {RPCEndpoint('eth_feeHistory'): lambda *_: {'reward': fee_history_rewards}}
    )

    web3.middleware_onion.add(fail_max_prio_middleware, 'fail_max_prio')
    web3.middleware_onion.inject(fee_history_result_middleware, 'fee_history_result', layer=0)

    with pytest.warns(
        UserWarning,
        match="There was an issue with the method eth_maxPriorityFeePerGas. Calculating using "
              "eth_feeHistory."
    ):
        max_priority_fee = web3.eth.max_priority_fee
        assert is_integer(max_priority_fee)
        assert max_priority_fee == expected_max_prio_calc

    # clean up
    web3.middleware_onion.remove('fail_max_prio')
    web3.middleware_onion.remove('fee_history_result')
