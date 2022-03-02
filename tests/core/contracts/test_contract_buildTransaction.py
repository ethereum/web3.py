import pytest

from eth_utils.toolz import (
    dissoc,
)

from web3.exceptions import (
    ValidationError,
)


@pytest.fixture()
def math_contract(w3, MathContract, address_conversion_func):
    deploy_txn = MathContract.constructor().transact()
    deploy_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert deploy_receipt is not None
    math_contract_address = address_conversion_func(deploy_receipt['contractAddress'])
    _math_contract = MathContract(address=math_contract_address)
    assert _math_contract.address == math_contract_address
    return _math_contract


@pytest.fixture()
def fallback_function_contract(w3, FallbackFunctionContract, address_conversion_func):
    deploy_txn = FallbackFunctionContract.constructor().transact()
    deploy_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert deploy_receipt is not None
    fallback_contract_address = address_conversion_func(deploy_receipt['contractAddress'])
    _fallback_contract = FallbackFunctionContract(address=fallback_contract_address)
    assert _fallback_contract.address == fallback_contract_address
    return _fallback_contract


@pytest.fixture()
def payable_tester_contract(w3, PayableTesterContract, address_conversion_func):
    deploy_txn = PayableTesterContract.constructor().transact()
    deploy_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert deploy_receipt is not None
    payable_tester_address = address_conversion_func(deploy_receipt['contractAddress'])
    _payable_tester = PayableTesterContract(address=payable_tester_address)
    assert _payable_tester.address == payable_tester_address
    return _payable_tester


def test_build_transaction_not_paying_to_nonpayable_function(
        w3,
        payable_tester_contract,
        buildTransaction):
    txn = buildTransaction(contract=payable_tester_contract,
                           contract_function='doNoValueCall')
    assert dissoc(txn, 'gas') == {
        'to': payable_tester_contract.address,
        'data': '0xe4cb8f5c',
        'value': 0,
        'maxFeePerGas': 2750000000,
        'maxPriorityFeePerGas': 10 ** 9,
        'chainId': 61,
    }


def test_build_transaction_paying_to_nonpayable_function(
        w3,
        payable_tester_contract,
        buildTransaction):
    with pytest.raises(ValidationError):
        buildTransaction(contract=payable_tester_contract,
                         contract_function='doNoValueCall',
                         tx_params={'value': 1})


def test_build_transaction_with_contract_no_arguments(w3, math_contract, buildTransaction):
    txn = buildTransaction(contract=math_contract, contract_function='increment')
    assert dissoc(txn, 'gas') == {
        'to': math_contract.address,
        'data': '0xd09de08a',
        'value': 0,
        'maxFeePerGas': 2750000000,
        'maxPriorityFeePerGas': 10 ** 9,
        'chainId': 61,
    }


def test_build_transaction_with_contract_fallback_function(w3, fallback_function_contract):
    txn = fallback_function_contract.fallback.buildTransaction()
    assert dissoc(txn, 'gas') == {
        'to': fallback_function_contract.address,
        'data': '0x',
        'value': 0,
        'maxFeePerGas': 2750000000,
        'maxPriorityFeePerGas': 10 ** 9,
        'chainId': 61,
    }


def test_build_transaction_with_contract_class_method(
        w3,
        MathContract,
        math_contract,
        buildTransaction):
    txn = buildTransaction(
        contract=MathContract,
        contract_function='increment',
        tx_params={'to': math_contract.address},
    )
    assert dissoc(txn, 'gas') == {
        'to': math_contract.address,
        'data': '0xd09de08a',
        'value': 0,
        'maxFeePerGas': 2750000000,
        'maxPriorityFeePerGas': 10 ** 9,
        'chainId': 61,
    }


def test_build_transaction_with_contract_default_account_is_set(
        w3,
        math_contract,
        buildTransaction):
    txn = buildTransaction(contract=math_contract, contract_function='increment')
    assert dissoc(txn, 'gas') == {
        'to': math_contract.address,
        'data': '0xd09de08a',
        'value': 0,
        'maxFeePerGas': 2750000000,
        'maxPriorityFeePerGas': 10 ** 9,
        'chainId': 61,
    }


def test_build_transaction_with_gas_price_strategy_set(w3, math_contract, buildTransaction):
    def my_gas_price_strategy(w3, transaction_params):
        return 5
    w3.eth.set_gas_price_strategy(my_gas_price_strategy)
    txn = buildTransaction(contract=math_contract, contract_function='increment')
    assert dissoc(txn, 'gas') == {
        'to': math_contract.address,
        'data': '0xd09de08a',
        'value': 0,
        'gasPrice': 5,
        'chainId': 61,
    }


def test_build_transaction_with_contract_data_supplied_errors(w3,
                                                              math_contract,
                                                              buildTransaction):
    with pytest.raises(ValueError):
        buildTransaction(contract=math_contract,
                         contract_function='increment',
                         tx_params={'data': '0x000'})


def test_build_transaction_with_contract_to_address_supplied_errors(w3,
                                                                    math_contract,
                                                                    buildTransaction):
    with pytest.raises(ValueError):
        buildTransaction(contract=math_contract,
                         contract_function='increment',
                         tx_params={'to': '0xb2930B35844a230f00E51431aCAe96Fe543a0347'})


@pytest.mark.parametrize(
    'transaction_args,method_args,method_kwargs,expected,skip_testrpc',
    (
        (
            {}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 0, 'maxFeePerGas': 2750000000, 'maxPriorityFeePerGas': 1000000000,
                'chainId': 61,
            }, False
        ),
        (
            {'gas': 800000}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 0, 'maxFeePerGas': 2750000000, 'maxPriorityFeePerGas': 1000000000,
                'chainId': 61,
            }, False
        ),
        (  # legacy transaction, explicit gasPrice
            {'gasPrice': 22 ** 8}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 0, 'gasPrice': 22 ** 8, 'chainId': 61,
            }, False
        ),
        (
            {'maxFeePerGas': 22 ** 8, 'maxPriorityFeePerGas': 22 ** 8}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 0, 'maxFeePerGas': 22 ** 8, 'maxPriorityFeePerGas': 22 ** 8,
                'chainId': 61,
            }, False
        ),
        (
            {'nonce': 7}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 0, 'maxFeePerGas': 2750000000, 'maxPriorityFeePerGas': 1000000000,
                'nonce': 7, 'chainId': 61,
            }, True
        ),
        (
            {'value': 20000}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 20000, 'maxFeePerGas': 2750000000, 'maxPriorityFeePerGas': 1000000000,
                'chainId': 61,
            }, False
        ),
    ),
    ids=[
        'Standard',
        'Explicit Gas',
        'Explicit Gas Price',
        'Explicit Dynamic Fees',
        'Explicit Nonce',
        'With Value',
    ]
)
def test_build_transaction_with_contract_with_arguments(w3, skip_if_testrpc, math_contract,
                                                        transaction_args,
                                                        method_args,
                                                        method_kwargs,
                                                        expected,
                                                        skip_testrpc,
                                                        buildTransaction):
    if skip_testrpc:
        skip_if_testrpc(w3)

    txn = buildTransaction(contract=math_contract,
                           contract_function='increment',
                           func_args=method_args,
                           func_kwargs=method_kwargs,
                           tx_params=transaction_args)
    expected['to'] = math_contract.address
    assert txn is not None
    if 'gas' in transaction_args:
        assert txn['gas'] == transaction_args['gas']
    else:
        assert 'gas' in txn
    assert dissoc(txn, 'gas') == expected
