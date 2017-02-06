import pytest

from web3.contract import Contract


def test_class_construction_sets_class_vars(web3, MATH_ABI, MATH_CODE,
                                            MATH_RUNTIME, MATH_SOURCE):
    MathContract = web3.eth.contract(
        abi=MATH_ABI,
        bytecode=MATH_CODE,
        bytecode_runtime=MATH_RUNTIME,
        source=MATH_SOURCE,
    )

    assert MathContract.web3 == web3
    assert MathContract.bytecode == MATH_CODE
    assert MathContract.bytecode_runtime == MATH_RUNTIME
    assert MathContract.source == MATH_SOURCE


def test_error_to_instantiate_base_class():
    with pytest.raises(AttributeError):
        Contract()


def test_can_instantiate_without_address(web3, MATH_ABI):
    MathContract = web3.eth.contract(MATH_ABI)

    math = MathContract()
