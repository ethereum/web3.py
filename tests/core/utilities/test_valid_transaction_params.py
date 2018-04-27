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
    ''' baseline test for clean param dict '''
    input = {
        'from': '0x0',
        'to': '0x0',
        'gas': 21000,
        'gasPrice': 5000000,
        'data': '0x0',
        'value': 1,
        'nonce': 2,
        'chainId': 1,
    }
    valid_transaction_params = extract_valid_transaction_params(input)
    assert valid_transaction_params == input


test_data = [({'data': '0x0', 'input': '0x0'}, {'data': '0x0'}), ]
@pytest.mark.parametrize("transaction_params, expected", test_data)  # noqa E302
def test_extract_valid_transaction_params_2(transaction_params, expected):
    valid_transaction_params = extract_valid_transaction_params(transaction_params)
    assert valid_transaction_params == expected


test_data = [({'input': '0x0'}, {'data': '0x0'}), ]
@pytest.mark.parametrize("transaction_params, expected", test_data)  # noqa E302
def test_extract_valid_transaction_params_3(transaction_params, expected):
    valid_transaction_params = extract_valid_transaction_params(transaction_params)
    assert valid_transaction_params == expected


test_data = [({}, {}), ]
@pytest.mark.parametrize("transaction_params, expected", test_data)  # noqa E302
def test_extract_valid_transaction_params_4(transaction_params, expected):
    valid_transaction_params = extract_valid_transaction_params(transaction_params)
    assert valid_transaction_params == expected



@pytest.mark.xfail(raises=AttributeError, strict=True)  # noqa E302
def test_extract_valid_transaction_params_5():
    transaction_params = {'data': '0x0', 'input': '0x1'}
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
