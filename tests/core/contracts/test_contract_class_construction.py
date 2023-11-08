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


def test_class_construction_sets_class_vars(
    w3, math_contract_abi, math_contract_bytecode, math_contract_runtime
):
    math_contract_factory = w3.eth.contract(
        abi=math_contract_abi,
        bytecode=math_contract_bytecode,
        bytecode_runtime=math_contract_runtime,
    )

    assert math_contract_factory.w3 == w3
    assert math_contract_factory.bytecode == decode_hex(math_contract_bytecode)
    assert math_contract_factory.bytecode_runtime == decode_hex(math_contract_runtime)


def test_error_to_instantiate_base_class():
    with pytest.raises(AttributeError):
        Contract()


def test_abi_as_json_string(w3, math_contract_abi, some_address):
    abi_str = json.dumps(math_contract_abi)

    math_contract_factory = w3.eth.contract(abi=abi_str)
    assert math_contract_factory.abi == math_contract_abi

    math = math_contract_factory(some_address)
    assert math.abi == math_contract_abi


def test_contract_init_with_w3_function_name(
    w3,
    function_name_tester_contract_abi,
    function_name_tester_contract,  # this is the fixture that deployed the contract
):
    # this line only fails when that second function is there, however...
    contract_factory = w3.eth.contract(abi=function_name_tester_contract_abi)

    # this will actually test that we can use the ABI and the deployed contract's
    # address to re-instantiate a new contract and interact with it
    contract = contract_factory(function_name_tester_contract.address)
    assert contract.functions.w3().call() is True


def test_error_to_call_non_existent_fallback(
    w3, math_contract_abi, math_contract_bytecode, math_contract_runtime
):
    math_contract = w3.eth.contract(
        abi=math_contract_abi,
        bytecode=math_contract_bytecode,
        bytecode_runtime=math_contract_runtime,
    )
    with pytest.raises(FallbackNotFound):
        math_contract.fallback.estimate_gas()
