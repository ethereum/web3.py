import pytest

from eth_utils.toolz import (
    dissoc,
)

from web3.exceptions import (
    ValidationError,
)

# -*- coding: utf-8 -*-


@pytest.fixture()
def math_contract(web3, MathContract, address_conversion_func):
    deploy_txn = MathContract.constructor().transact()
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    math_contract_address = address_conversion_func(deploy_receipt['contractAddress'])
    _math_contract = MathContract(address=math_contract_address)
    assert _math_contract.address == math_contract_address
    return _math_contract


@pytest.fixture()
def fallback_function_contract(web3, FallbackFunctionContract, address_conversion_func):
    deploy_txn = FallbackFunctionContract.constructor().transact()
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    fallback_contract_address = address_conversion_func(deploy_receipt['contractAddress'])
    _fallback_contract = FallbackFunctionContract(address=fallback_contract_address)
    assert _fallback_contract.address == fallback_contract_address
    return _fallback_contract


@pytest.fixture()
def payable_tester_contract(web3, PayableTesterContract, address_conversion_func):
    deploy_txn = PayableTesterContract.constructor().transact()
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    payable_tester_address = address_conversion_func(deploy_receipt['contractAddress'])
    _payable_tester = PayableTesterContract(address=payable_tester_address)
    assert _payable_tester.address == payable_tester_address
    return _payable_tester


def test_build_transaction_not_paying_to_nonpayable_function(
        web3,
        payable_tester_contract,
        buildTransaction):
    txn = buildTransaction(contract=payable_tester_contract,
                           contract_function='doNoValueCall')
    assert dissoc(txn, 'gas') == {
        'to': payable_tester_contract.address,
        'data': '0xe4cb8f5c',
        'value': 0,
        'gasPrice': 1,
        'chainId': 61,
    }


def test_build_transaction_paying_to_nonpayable_function(
        web3,
        payable_tester_contract,
        buildTransaction):
    with pytest.raises(ValidationError):
        buildTransaction(contract=payable_tester_contract,
                         contract_function='doNoValueCall',
                         tx_params={'value': 1})


def test_build_transaction_with_contract_no_arguments(web3, math_contract, buildTransaction):
    txn = buildTransaction(contract=math_contract, contract_function='increment')
    assert dissoc(txn, 'gas') == {
        'to': math_contract.address,
        'data': '0xd09de08a',
        'value': 0,
        'gasPrice': 1,
        'chainId': 61,
    }


def test_build_transaction_with_contract_fallback_function(web3, fallback_function_contract):
    txn = fallback_function_contract.fallback.buildTransaction()
    assert dissoc(txn, 'gas') == {
        'to': fallback_function_contract.address,
        'data': '0x',
        'value': 0,
        'gasPrice': 1,
        'chainId': 61,
    }


def test_build_transaction_with_contract_class_method(
        web3,
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
        'gasPrice': 1,
        'chainId': 61,
    }


def test_build_transaction_with_contract_default_account_is_set(
        web3,
        math_contract,
        buildTransaction):
    txn = buildTransaction(contract=math_contract, contract_function='increment')
    assert dissoc(txn, 'gas') == {
        'to': math_contract.address,
        'data': '0xd09de08a',
        'value': 0,
        'gasPrice': 1,
        'chainId': 61,
    }


def test_build_transaction_with_gas_price_strategy_set(web3, math_contract, buildTransaction):
    def my_gas_price_strategy(web3, transaction_params):
        return 5
    web3.eth.setGasPriceStrategy(my_gas_price_strategy)
    txn = buildTransaction(contract=math_contract, contract_function='increment')
    assert dissoc(txn, 'gas') == {
        'to': math_contract.address,
        'data': '0xd09de08a',
        'value': 0,
        'gasPrice': 5,
        'chainId': 61,
    }


def test_build_transaction_with_contract_data_supplied_errors(web3,
                                                              math_contract,
                                                              buildTransaction):
    with pytest.raises(ValueError):
        buildTransaction(contract=math_contract,
                         contract_function='increment',
                         tx_params={'data': '0x000'})


def test_build_transaction_with_contract_to_address_supplied_errors(web3,
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
                'value': 0, 'gasPrice': 1, 'chainId': 61,
            }, False
        ),
        (
            {'gas': 800000}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 0, 'gasPrice': 1, 'chainId': 61,
            }, False
        ),
        (
            {'gasPrice': 21000000000}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 0, 'gasPrice': 21000000000, 'chainId': 61,
            }, False
        ),
        (
            {'nonce': 7}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 0, 'gasPrice': 1, 'nonce': 7, 'chainId': 61,
            }, True
        ),
        (
            {'value': 20000}, (5,), {}, {
                'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',  # noqa: E501
                'value': 20000, 'gasPrice': 1, 'chainId': 61,
            }, False
        ),
    ),
    ids=[
        'Standard',
        'Explicit Gas',
        'Explicit Gas Price',
        'Explicit Nonce',
        'With Value',
    ]
)
def test_build_transaction_with_contract_with_arguments(web3, skip_if_testrpc, math_contract,
                                                        transaction_args,
                                                        method_args,
                                                        method_kwargs,
                                                        expected,
                                                        skip_testrpc,
                                                        buildTransaction):
    if skip_testrpc:
        skip_if_testrpc(web3)

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
