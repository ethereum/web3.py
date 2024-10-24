import json
import pytest

from eth_utils import (
    decode_hex,
)

from web3.contract import (
    Contract,
)
from web3.exceptions import (
    ABIEventNotFound,
    ABIFallbackNotFound,
    ABIFunctionNotFound,
    NoABIEventsFound,
    NoABIFound,
    NoABIFunctionsFound,
    Web3AttributeError,
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
    with pytest.raises(Web3AttributeError):
        Contract()


def test_abi_as_json_string(w3, math_contract_abi, some_address):
    abi_str = json.dumps(math_contract_abi)

    math_contract_factory = w3.eth.contract(abi=abi_str)
    assert math_contract_factory.abi == math_contract_abi

    math = math_contract_factory(some_address)
    assert math.abi == math_contract_abi


def test_contract_init_with_abi_function_name(
    w3,
    function_name_tester_contract_abi,
    function_name_tester_contract,
):
    # test `abi` function name does not throw when creating the contract factory
    contract_factory = w3.eth.contract(abi=function_name_tester_contract_abi)

    # re-instantiate the contract
    contract = contract_factory(function_name_tester_contract.address)

    # Contract `abi`` function should not override `web3` attribute
    assert contract.abi == function_name_tester_contract_abi

    with pytest.raises(TypeError):
        contract.functions.abi[0]

    # assert the `abi` function returns true when called
    result = contract.functions.abi().call()
    assert result is True


@pytest.mark.asyncio
async def test_async_contract_init_with_abi_function_name(
    async_w3,
    function_name_tester_contract_abi,
    async_function_name_tester_contract,
):
    # test `abi` function name does not throw when creating the contract factory
    contract_factory = async_w3.eth.contract(abi=function_name_tester_contract_abi)

    # re-instantiate the contract
    contract = contract_factory(async_function_name_tester_contract.address)

    # Contract `abi` function should not override `web3` attribute
    assert contract.abi == function_name_tester_contract_abi

    with pytest.raises(TypeError):
        contract.functions.abi[0]

    # assert the `abi` function returns true when called
    result = await contract.functions.abi().call()
    assert result is True


def test_contract_init_with_w3_function_name(
    w3,
    function_name_tester_contract_abi,
    function_name_tester_contract,
):
    # test `w3` function name does not throw when creating the contract factory
    contract_factory = w3.eth.contract(abi=function_name_tester_contract_abi)

    # re-instantiate the contract
    contract = contract_factory(function_name_tester_contract.address)

    # Contract w3 function should not override web3 instance
    with pytest.raises(AttributeError):
        contract.functions.w3.eth.get_block("latest")

    assert contract.w3.eth.get_block("latest") is not None

    # assert the `w3` function returns true when called
    result = contract.functions.w3().call()
    assert result is True


@pytest.mark.asyncio
async def test_async_contract_init_with_w3_function_name(
    async_w3,
    function_name_tester_contract_abi,
    async_function_name_tester_contract,
):
    # test `w3` function name does not throw when creating the contract factory
    contract_factory = async_w3.eth.contract(abi=function_name_tester_contract_abi)

    # re-instantiate the contract
    contract = contract_factory(async_function_name_tester_contract.address)

    # Contract w3 function should not override web3 instance
    with pytest.raises(AttributeError):
        contract.functions.w3.eth.get_block("latest")

    assert contract.w3.eth.get_block("latest") is not None

    # assert the `w3` function returns true when called
    result = await contract.functions.w3().call()
    assert result is True


def test_error_to_call_non_existent_fallback(
    w3, math_contract_abi, math_contract_bytecode, math_contract_runtime
):
    math_contract = w3.eth.contract(
        abi=math_contract_abi,
        bytecode=math_contract_bytecode,
        bytecode_runtime=math_contract_runtime,
    )
    with pytest.raises(ABIFallbackNotFound):
        math_contract.fallback.estimate_gas()


@pytest.mark.parametrize(
    "abi,namespace,expected_exception",
    (
        (None, "functions", NoABIFound),
        (None, "events", NoABIFound),
        ([{"type": "event", "name": "AnEvent"}], "functions", NoABIFunctionsFound),
        ([{"type": "function", "name": "aFunction"}], "events", NoABIEventsFound),
        ([{"type": "function", "name": "aFunction"}], "functions", ABIFunctionNotFound),
        ([{"type": "event", "name": "AnEvent"}], "events", ABIEventNotFound),
    ),
)
def test_appropriate_exceptions_based_on_namespaces(
    w3, abi, namespace, expected_exception
):
    if abi is None:
        contract = w3.eth.contract()
    else:
        contract = w3.eth.contract(abi=abi)

    namespace_instance = getattr(contract, namespace)

    with pytest.raises(expected_exception):
        namespace_instance.doesNotExist()


@pytest.mark.parametrize(
    "abi,namespace,expected_exception",
    (
        (None, "functions", NoABIFound),
        (None, "events", NoABIFound),
        ([{"type": "event", "name": "AnEvent"}], "functions", NoABIFunctionsFound),
        ([{"type": "function", "name": "aFunction"}], "events", NoABIEventsFound),
        ([{"type": "function", "name": "aFunction"}], "functions", ABIFunctionNotFound),
        ([{"type": "event", "name": "AnEvent"}], "events", ABIEventNotFound),
    ),
)
def test_async_appropriate_exceptions_based_on_namespaces(
    async_w3, abi, namespace, expected_exception
):
    if abi is None:
        contract = async_w3.eth.contract()
    else:
        contract = async_w3.eth.contract(abi=abi)

    namespace_instance = getattr(contract, namespace)

    with pytest.raises(expected_exception):
        namespace_instance.doesNotExist()
