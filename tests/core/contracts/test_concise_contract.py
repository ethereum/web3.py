import pytest
from unittest.mock import (
    Mock,
)

from eth_utils import (
    decode_hex,
)

from web3.contract import (
    CONCISE_NORMALIZERS,
    ConciseContract,
    ConciseMethod,
)


@pytest.fixture()
def EMPTY_ADDR():
    return '0x' + '00' * 20


@pytest.fixture()
def zero_address_contract(web3, WithConstructorAddressArgumentsContract, EMPTY_ADDR):
    deploy_txn = WithConstructorAddressArgumentsContract.deploy(args=[
        EMPTY_ADDR,
    ])
    deploy_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _address_contract = WithConstructorAddressArgumentsContract(
        address=deploy_receipt['contractAddress'],
    )
    return ConciseContract(_address_contract)


def test_concisecontract_call_default():
    mock = Mock()
    sweet_method = ConciseMethod(mock.functions.grail)
    sweet_method(1, 2)
    mock.functions.grail.assert_called_once_with(1, 2)
    # Checking in return_value, ie the function instance
    mock.functions.grail.return_value.call.assert_called_once_with({})


def test_concisecontract_custom_transact():
    mock = Mock()
    sweet_method = ConciseMethod(mock.functions.grail)
    sweet_method(1, 2, transact={'holy': 3})
    mock.functions.grail.assert_called_once_with(1, 2)
    # Checking in return_value, ie the function instance
    mock.functions.grail.return_value.transact.assert_called_once_with({'holy': 3})


def test_concisecontract_two_keywords_fail():
    mock = Mock()
    sweet_method = ConciseMethod(mock)
    with pytest.raises(TypeError):
        sweet_method(1, 2, transact={'holy': 3}, call={'count_to': 4})


def test_concisecontract_unknown_keyword_fails():
    contract = Mock()
    sweet_method = ConciseMethod(contract.functions.grail)
    with pytest.raises(TypeError):
        sweet_method(1, 2, count={'to': 5})


def test_concisecontract_returns_none_for_0addr(zero_address_contract):
    result = zero_address_contract.testAddr()
    assert result is None


def test_class_construction_sets_class_vars(web3,
                                            MATH_ABI,
                                            MATH_CODE,
                                            MATH_RUNTIME,
                                            some_address,
                                            ):
    MathContract = web3.eth.contract(
        abi=MATH_ABI,
        bytecode=MATH_CODE,
        bytecode_runtime=MATH_RUNTIME,
        ContractFactoryClass=ConciseContract,
    )

    math = MathContract(some_address)
    classic = math._classic_contract
    assert classic.web3 == web3
    assert classic.bytecode == decode_hex(MATH_CODE)
    assert classic.bytecode_runtime == decode_hex(MATH_RUNTIME)


def test_conciscecontract_keeps_custom_normalizers_on_base(web3):
    base_contract = web3.eth.contract()
    # give different normalizers to this base instance
    base_contract._return_data_normalizers = base_contract._return_data_normalizers + tuple([None])

    # create concisce contract with custom contract
    new_normalizers_size = len(base_contract._return_data_normalizers)
    concise = ConciseContract(base_contract)

    # check that concise contract includes the new normalizers
    concise_normalizers_size = len(concise._classic_contract._return_data_normalizers)
    assert concise_normalizers_size == new_normalizers_size + len(CONCISE_NORMALIZERS)
    assert concise._classic_contract._return_data_normalizers[0] is None
