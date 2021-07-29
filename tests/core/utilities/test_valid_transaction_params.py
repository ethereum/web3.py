import pytest

from web3._utils.transactions import (
    assert_valid_transaction_params,
    extract_valid_transaction_params,
    fill_transaction_defaults,
)


def test_assert_valid_transaction_params_all_params():
    assert_valid_transaction_params({
        'chainId': 1,
        'type': '0x2',
        'from': '0x0',
        'to': '0x0',
        'gas': 21000,
        'gasPrice': 5000000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
        'value': 1,
        'data': '0x0',
        'nonce': 2,
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
    'chainId': 1,
    'type': '0x2',
    'from': '0x0',
    'to': '0x1',
    'gas': 21000,
    'gasPrice': 5000000,
    'maxFeePerGas': 2000000000,
    'maxPriorityFeePerGas': 1000000000,
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
        'chainId': 1,
        'type': '0x2',
        'from': '0x0',
        'to': '0x0',
        'gas': 21000,
        'gasPrice': 5000000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
        'value': 1,
        'tokens': 9000,
    }
    valid_transaction_params = extract_valid_transaction_params(input)
    assert valid_transaction_params == {
        'chainId': 1,
        'type': '0x2',
        'from': '0x0',
        'to': '0x0',
        'gas': 21000,
        'gasPrice': 5000000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
        'value': 1,
    }


def test_fill_transaction_defaults_for_all_params(web3):
    default_transaction = fill_transaction_defaults(web3, {})

    assert default_transaction == {
        'chainId': web3.eth.chain_id,
        'data': b'',
        'gas': web3.eth.estimate_gas({}),
        'gasPrice': web3.eth.gas_price,
        'value': 0,
    }


def test_fill_transaction_defaults_sets_type_from_1559_params_and_no_gas_price(web3):
    transaction_1559 = {
        'chainId': 1,
        'data': b'123',
        'gas': 21000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
        'value': 2,
    }
    transaction_1559_type_added = fill_transaction_defaults(web3, transaction_1559)

    assert transaction_1559_type_added == {
        'chainId': 1,
        'data': b'123',
        'gas': 21000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
        'type': '0x2',  # type is added and defaults to '0x2' when 1559 params are present
        'value': 2,
    }
