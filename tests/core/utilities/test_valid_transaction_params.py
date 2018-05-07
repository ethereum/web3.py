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


def test_extract_valid_transaction_params():
    from copy import deepcopy
    base_input = {
        'from': '0x0',
        'to': '0x0',
        'gas': 21000,
        'gasPrice': 5000000,
        'value': 1,
        'nonce': 2,
        'chainId': 1,
    }

    input = deepcopy(base_input)
    input['data'] = '0x0'
    valid_transaction_params = extract_valid_transaction_params(input)
    assert valid_transaction_params == input

    in_input = deepcopy(base_input)
    in_input['input'] = '0x0'
    in_input['data'] = '0x0'
    valid_transaction_params = extract_valid_transaction_params(in_input)
    assert valid_transaction_params == input

    input['input'] = '0x1'
    with pytest.raises(AttributeError, match=r'.* You need to resolve this conflict.'):
        extract_valid_transaction_params(input)


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
