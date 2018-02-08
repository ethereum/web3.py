import json
import pytest

from web3.exceptions import (
    ValidationError,
)
from web3.utils.abi import (
    get_abi_input_types,
)
from web3.utils.function_identifiers import (
    FallbackFn,
)

SINGLE_FN_NO_ARGS = json.loads('[{"constant":false,"inputs":[],"name":"a","outputs":[],"type":"function"}]')  # noqa: E501
SINGLE_FN_ONE_ARG = json.loads('[{"constant":false,"inputs":[{"name":"","type":"uint256"}],"name":"a","outputs":[],"type":"function"}]')  # noqa: E501
MULTIPLE_FUNCTIONS = json.loads('[{"constant":false,"inputs":[],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"bytes32"}],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"uint256"}],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"uint8"}],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"int8"}],"name":"a","outputs":[],"type":"function"}]')  # noqa: E501
FALLBACK_FUNCTION = json.loads('[{"constant": false, "inputs": [], "name": "getData", "outputs": [{"name": "r", "type": "uint256"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"payable": false, "stateMutability": "nonpayable", "type": "fallback"}]')  # noqa: E501


def test_finds_single_function_without_args(web3):
    Contract = web3.eth.contract(abi=SINGLE_FN_NO_ARGS)

    abi = Contract._find_matching_fn_abi('a', [])
    assert abi['name'] == 'a'
    assert abi['inputs'] == []


def test_finds_single_function_with_args(web3):
    Contract = web3.eth.contract(abi=SINGLE_FN_ONE_ARG)

    abi = Contract._find_matching_fn_abi('a', [1234])
    assert abi['name'] == 'a'
    assert len(abi['inputs']) == 1
    assert abi['inputs'][0]['type'] == 'uint256'


def test_finds_fallback_function(web3):
    Contract = web3.eth.contract(abi=FALLBACK_FUNCTION)

    abi = Contract._find_matching_fn_abi(FallbackFn, [])
    assert abi['type'] == 'fallback'


def test_error_when_no_function_name_match(web3):
    Contract = web3.eth.contract(abi=SINGLE_FN_NO_ARGS)

    with pytest.raises(ValidationError):
        Contract._find_matching_fn_abi('no_function_name', [1234])


@pytest.mark.parametrize(
    'arguments,expected_types',
    (
        ([], []),
        ([b'arst'], ['bytes32']),
        (['0xf00b47'], ['bytes32']),
        ([1234567890], ['uint256']),
        # ([255], ['uint8']),  # TODO: enable
        ([-1], ['int8']),
    )
)
def test_finds_function_with_matching_args(web3, arguments, expected_types):
    Contract = web3.eth.contract(abi=MULTIPLE_FUNCTIONS)

    abi = Contract._find_matching_fn_abi('a', arguments)
    assert abi['name'] == 'a'
    assert len(abi['inputs']) == len(expected_types)
    assert set(get_abi_input_types(abi)) == set(expected_types)


def test_error_when_duplicate_match(web3):
    Contract = web3.eth.contract(abi=MULTIPLE_FUNCTIONS)

    with pytest.raises(ValidationError):
        Contract._find_matching_fn_abi('a', [100])
