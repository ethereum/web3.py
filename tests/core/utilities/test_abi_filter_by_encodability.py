import pytest

from web3._utils.abi import (
    filter_by_encodability,
)

FN_ABI_ONE_ADDRESS_ARG = {'inputs': [{'name': 'arg', 'type': 'address'}]}

FN_ABI_MIXED_ARGS = {
    'inputs': [
        {
            'components': [
                {'name': 'anAddress', 'type': 'address'},
                {'name': 'anInt', 'type': 'uint256'},
                {'name': 'someBytes', 'type': 'bytes'},
            ],
            'type': 'tuple'
        }
    ],
    'type': 'function'
}


@pytest.mark.parametrize(
    'arguments,contract_abi,expected_match_count,expected_first_match',
    (
        (
            ('0x' + '1' * 40,),
            [FN_ABI_ONE_ADDRESS_ARG],
            1,
            FN_ABI_ONE_ADDRESS_ARG,
        ),
        (
            ('0xffff'),  # not a valid address
            [FN_ABI_ONE_ADDRESS_ARG],
            0,
            None,
        ),
        (
            (
                {
                    'anAddress': '0x' + '0' * 40,
                    'anInt': 1,
                    'someBytes': b'\x00' * 20,
                },
            ),
            [FN_ABI_MIXED_ARGS],
            1,
            FN_ABI_MIXED_ARGS,
        ),
    )
)
def test_filter_by_encodability(
    arguments, contract_abi, expected_match_count, expected_first_match
):
    filter_output = filter_by_encodability(arguments, {}, contract_abi)
    assert len(filter_output) == expected_match_count
    if expected_match_count > 0:
        assert filter_output[0] == expected_first_match
