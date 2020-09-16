import json
import pytest

from eth_utils import (
    decode_hex,
)

from web3.contract import (
    Contract,
)
from web3.exceptions import (
    FallbackNotFound,
)


def test_class_construction_sets_class_vars(web3,
                                            MATH_ABI,
                                            MATH_CODE,
                                            MATH_RUNTIME):
    MathContract = web3.eth.contract(
        abi=MATH_ABI,
        bytecode=MATH_CODE,
        bytecode_runtime=MATH_RUNTIME,
    )

    assert MathContract.web3 == web3
    assert MathContract.bytecode == decode_hex(MATH_CODE)
    assert MathContract.bytecode_runtime == decode_hex(MATH_RUNTIME)


def test_error_to_instantiate_base_class():
    with pytest.raises(AttributeError):
        Contract()


def test_abi_as_json_string(web3, MATH_ABI, some_address):
    abi_str = json.dumps(MATH_ABI)

    MathContract = web3.eth.contract(abi=abi_str)
    assert MathContract.abi == MATH_ABI

    math = MathContract(some_address)
    assert math.abi == MATH_ABI


def test_error_to_call_non_existent_fallback(web3,
                                             MATH_ABI,
                                             MATH_CODE,
                                             MATH_RUNTIME):
    math_contract = web3.eth.contract(
        abi=MATH_ABI,
        bytecode=MATH_CODE,
        bytecode_runtime=MATH_RUNTIME,
    )
    with pytest.raises(FallbackNotFound):
        math_contract.fallback.estimateGas()
