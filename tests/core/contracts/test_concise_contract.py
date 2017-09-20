
import sys

import pytest

from web3.contract import (
    ConciseContract,
    ConciseMethod,
)

if sys.version_info >= (3, 3):
    from unittest.mock import Mock


@pytest.mark.skipif(sys.version_info < (3, 3), reason="needs Mock library from 3.3")
def test_concisecontract_call_default():
    contract = Mock()
    sweet_method = ConciseMethod(contract, 'grail')
    sweet_method(1, 2)
    contract.call.assert_called_once_with({})
    contract.call().grail.assert_called_once_with(1, 2)


@pytest.mark.skipif(sys.version_info < (3, 3), reason="needs Mock library from 3.3")
def test_concisecontract_custom_transact():
    contract = Mock()
    sweet_method = ConciseMethod(contract, 'grail')
    sweet_method(1, 2, transact={'holy': 3})
    contract.transact.assert_called_once_with({'holy': 3})
    contract.transact().grail.assert_called_once_with(1, 2)


@pytest.mark.skipif(sys.version_info < (3, 3), reason="needs Mock library from 3.3")
def test_concisecontract_two_keywords_fail():
    contract = Mock()
    sweet_method = ConciseMethod(contract, 'grail')
    with pytest.raises(TypeError):
        sweet_method(1, 2, transact={'holy': 3}, call={'count_to': 4})


@pytest.mark.skipif(sys.version_info < (3, 3), reason="needs Mock library from 3.3")
def test_concisecontract_unknown_keyword_fails():
    contract = Mock()
    sweet_method = ConciseMethod(contract, 'grail')
    with pytest.raises(TypeError):
        sweet_method(1, 2, count={'to': 5})


def test_concisecontract_returns_none_for_0addr(web3, MATH_ABI):
    MathContract = web3.eth.contract(
        abi=MATH_ABI,
        ContractFactoryClass=ConciseContract,
    )

    math = MathContract()
    empty_addr = '0x' + '00' * 20

    normalize = math._classic_contract._normalize_return_data
    val = normalize(['address'], [empty_addr])
    assert val is None
    val = normalize(['address[]'], [[empty_addr] * 3])
    assert val == [None] * 3


def test_class_construction_sets_class_vars(web3,
                                            MATH_ABI,
                                            MATH_CODE,
                                            MATH_RUNTIME):
    MathContract = web3.eth.contract(
        abi=MATH_ABI,
        bytecode=MATH_CODE,
        bytecode_runtime=MATH_RUNTIME,
        ContractFactoryClass=ConciseContract,
    )

    math = MathContract()
    classic = math._classic_contract
    assert classic.web3 == web3
    assert classic.bytecode == MATH_CODE
    assert classic.bytecode_runtime == MATH_RUNTIME
