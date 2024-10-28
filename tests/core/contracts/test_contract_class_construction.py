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


@pytest.mark.parametrize(
    "abi",
    ([{"type": "function", "name": "abi"}], [{"type": "function", "name": "address"}]),
)
def test_contract_init_with_reserved_name(w3, abi):
    with pytest.raises(Web3AttributeError):
        w3.eth.contract(abi=abi)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "abi",
    ([{"type": "function", "name": "abi"}], [{"type": "function", "name": "address"}]),
)
async def test_async_contract_init_with_reserved_name(async_w3, abi):
    with pytest.raises(Web3AttributeError):
        await async_w3.eth.contract(abi=abi)


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
        ([{"type": "event", "name": "AnEvent"}], "functions", NoABIFunctionsFound),
        ([{"type": "function", "name": "aFunction"}], "events", NoABIEventsFound),
        ([{"type": "function", "name": "aFunction"}], "functions", ABIFunctionNotFound),
        ([{"type": "event", "name": "AnEvent"}], "events", ABIEventNotFound),
    ),
)
def test_appropriate_exceptions_based_on_namespaces(
    w3, abi, namespace, expected_exception
):
    contract = w3.eth.contract(abi=abi)

    namespace_instance = getattr(contract, namespace)

    with pytest.raises(expected_exception):
        namespace_instance.doesNotExist()


@pytest.mark.parametrize(
    "namespace",
    ("functions", "events"),
)
def test_appropriate_exceptions_based_on_namespaces_no_abi(w3, namespace):
    contract = w3.eth.contract()

    namespace_instance = getattr(contract, namespace)

    with pytest.raises(NoABIFound):
        namespace_instance.doesNotExist()


@pytest.mark.parametrize(
    "abi,namespace,expected_exception",
    (
        ([{"type": "event", "name": "AnEvent"}], "functions", NoABIFunctionsFound),
        ([{"type": "function", "name": "aFunction"}], "events", NoABIEventsFound),
        ([{"type": "function", "name": "aFunction"}], "functions", ABIFunctionNotFound),
        ([{"type": "event", "name": "AnEvent"}], "events", ABIEventNotFound),
    ),
)
def test_async_appropriate_exceptions_based_on_namespaces(
    async_w3, abi, namespace, expected_exception
):
    contract = async_w3.eth.contract(abi=abi)

    namespace_instance = getattr(contract, namespace)

    with pytest.raises(expected_exception):
        namespace_instance.doesNotExist()


@pytest.mark.parametrize(
    "namespace",
    ("functions", "events"),
)
def test_async_appropriate_exceptions_based_on_namespaces_no_abi(async_w3, namespace):
    # Initialize without ABI
    contract = async_w3.eth.contract()

    namespace_instance = getattr(contract, namespace)

    with pytest.raises(NoABIFound):
        namespace_instance.doesNotExist()
