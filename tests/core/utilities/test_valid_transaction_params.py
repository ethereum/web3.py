import pytest

from web3.utils.transactions import (
    assert_valid_transaction_params,
    extract_valid_transaction_params,
)


def test_assert_valid_transaction_params_all_params():
    assert_valid_transaction_params({
        'from': '0x0',
        'to': '0x0',
        'gas': 21000,
        'gasPrice': 5000000,
        'value': 1,
        'data': '0x0',
        'nonce': 2,
        'chainId': 1,
    })


def test_assert_valid_transaction_params_some_params():
    assert_valid_transaction_params({
        'from': '0x0',
        'to': '0x0',
        'value': 1,
    })


def test_assert_valid_transaction_params_invalid_param():
    with pytest.raises(ValueError):
        assert_valid_transaction_params({
            'from': '0x0',
            'to': '0x0',
            'value': 1,
            'tokens': 9000,
        })


FULL_TXN_DICT = {
    'from': '0x0',
    'to': '0x1',
    'gas': 21000,
    'gasPrice': 5000000,
    'data': '0x2',
    'value': 3,
    'nonce': 2,
    'chainId': 1,
}


@pytest.mark.parametrize(
    "transaction_params, expected",
    ((FULL_TXN_DICT, FULL_TXN_DICT),
     ({'data': '0x0', 'input': '0x0'}, {'data': '0x0'}),
     ({'input': '0x0'}, {'data': '0x0'}),
     ({}, {}),
     )
)
def test_extract_valid_transaction_params(transaction_params, expected):
    valid_transaction_params = extract_valid_transaction_params(transaction_params)
    assert valid_transaction_params == expected


INVALID_TXN_PARAMS = {'data': '0x0', 'input': '0x1'}
EXPECTED_EXC_MSG = r'.* "input:(.*)" and "data:(.*)" .*'


@pytest.mark.parametrize(
    "transaction_params, expected_exc_msg",
    ((INVALID_TXN_PARAMS, EXPECTED_EXC_MSG),)
)
def test_extract_valid_transaction_params_invalid(transaction_params, expected_exc_msg):
    with pytest.raises(AttributeError, match=expected_exc_msg):
        extract_valid_transaction_params(transaction_params)


def test_extract_valid_transaction_params_includes_invalid():
    input = {
        'from': '0x0',
        'to': '0x0',
        'gas': 21000,
        'gasPrice': 5000000,
        'value': 1,
        'tokens': 9000,
    }
    valid_transaction_params = extract_valid_transaction_params(input)
    assert valid_transaction_params == {
        'from': '0x0',
        'to': '0x0',
        'gas': 21000,
        'gasPrice': 5000000,
        'value': 1,
    }
