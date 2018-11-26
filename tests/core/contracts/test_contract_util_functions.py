import pytest

from web3.contract import (
    find_matching_fn_abi,
    parse_block_identifier_int,
)


#  This tests negative block number identifiers, which behave like python
#  list slices, with -1 being the latest block and -2 being the block before that.
#  This test is necessary because transaction calls allow negative block indexes, although
#  getBlock() does not allow negative block identifiers. Support for negative block identifier
#  will likely be removed in v5.
def test_parse_block_identifier_int(web3):
    last_num = web3.eth.getBlock('latest').number
    assert 0 == parse_block_identifier_int(web3, -1 - last_num)


@pytest.mark.parametrize(
    'contract_abi, fn_name, args, kwargs, expected',
    (
        (
            [
                {
                    'inputs': [],
                    'type': 'function',
                    'name': 'a',
                },
                {
                    'inputs': [{'type': 'bytes32'}],
                    'type': 'function',
                    'name': 'a',
                },
                {
                    'inputs': [{'type': 'uint256'}],
                    'type': 'function',
                    'name': 'a',
                },
            ],
            'a',
            [1],
            None,
            {
                'inputs': [{'type': 'uint256'}],
                'type': 'function',
                'name': 'a',
            },
        ),
    ),
)
def test_find_matching_fn_abi(fn_name, contract_abi, args, kwargs, expected):
    assert expected == find_matching_fn_abi(contract_abi, fn_name, args, kwargs)
