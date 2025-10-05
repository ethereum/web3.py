import pytest
import re
from typing import (
    cast,
)

from eth_typing import (
    ABI,
)
from eth_utils.toolz import (
    compose,
    curry,
)
from hexbytes import (
    HexBytes,
)

from web3.exceptions import (
    MismatchedABI,
    Web3ValueError,
)
from web3.utils.abi import (
    get_abi_element,
)

BLOCK_HASH_ABI = {
    "constant": False,
    "inputs": [{"name": "input", "type": "uint256"}],
    "name": "blockHashAmphithyronVersify",
    "outputs": [{"name": "", "type": "uint256"}],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function",
}

IDENTITY_WITH_UINT_ABI = {
    "constant": False,
    "inputs": [
        {"name": "input", "type": "uint256"},
        {"name": "uselessFlag", "type": "bool"},
    ],
    "name": "identity",
    "outputs": [{"name": "", "type": "uint256"}],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function",
}

IDENTITY_WITH_INT_ABI = {
    "constant": False,
    "inputs": [
        {"name": "input", "type": "int256"},
        {"name": "uselessFlag", "type": "bool"},
    ],
    "name": "identity",
    "outputs": [{"name": "", "type": "int256"}],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function",
}

IDENTITY_WITH_BOOL_ABI = {
    "constant": False,
    "inputs": [
        {"name": "valid", "type": "bool"},
    ],
    "name": "identity",
    "outputs": [{"name": "valid", "type": "bool"}],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function",
}

AMBIGUOUS_CONTRACT_ABI = [
    BLOCK_HASH_ABI,
    IDENTITY_WITH_UINT_ABI,
    IDENTITY_WITH_INT_ABI,
    IDENTITY_WITH_BOOL_ABI,
]


@pytest.fixture
def string_contract(w3, string_contract_factory, address_conversion_func):
    deploy_txn = string_contract_factory.constructor("Caqalai").transact()
    deploy_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert deploy_receipt is not None
    contract_address = address_conversion_func(deploy_receipt["contractAddress"])
    contract = string_contract_factory(address=contract_address)
    assert contract.address == contract_address
    assert len(w3.eth.get_code(contract.address)) > 0
    return contract


map_repr = compose(list, curry(map, repr))


@pytest.mark.parametrize(
    "method,args,repr_func,expected",
    (
        (
            "all_functions",
            (),
            map_repr,
            [
                "<Function blockHashAmphithyronVersify(uint256)>",
                "<Function identity(bool)>",
                "<Function identity(uint256,bool)>",
                "<Function identity(int256,bool)>",
            ],
        ),
        (
            "get_function_by_signature",
            ("identity(uint256,bool)",),
            repr,
            "<Function identity(uint256,bool)>",
        ),
        (
            "get_function_by_signature",
            ("identity(int256,bool)",),
            repr,
            "<Function identity(int256,bool)>",
        ),
        (
            "find_functions_by_name",
            ("identity",),
            map_repr,
            [
                "<Function identity(bool)>",
                "<Function identity(uint256,bool)>",
                "<Function identity(int256,bool)>",
            ],
        ),
        (
            "get_function_by_name",
            ("blockHashAmphithyronVersify",),
            repr,
            "<Function blockHashAmphithyronVersify(uint256)>",
        ),
        (
            "get_function_by_selector",
            (b"\x00\x00\x00\x00",),
            repr,
            "<Function blockHashAmphithyronVersify(uint256)>",
        ),
        (
            "get_function_by_selector",
            (0x00000000,),
            repr,
            "<Function blockHashAmphithyronVersify(uint256)>",
        ),
        (
            "get_function_by_selector",
            ("0x00000000",),
            repr,
            "<Function blockHashAmphithyronVersify(uint256)>",
        ),
        (
            "find_functions_by_args",
            (1, True),
            map_repr,
            ["<Function identity(uint256,bool)>", "<Function identity(int256,bool)>"],
        ),
        (
            "get_function_by_args",
            (1,),
            repr,
            "<Function blockHashAmphithyronVersify(uint256)>",
        ),
    ),
)
def test_find_or_get_functions_by_type(w3, method, args, repr_func, expected):
    contract = w3.eth.contract(abi=AMBIGUOUS_CONTRACT_ABI)
    function = getattr(contract, method)(*args)
    assert repr_func(function) == expected


def test_get_function_by_name(w3):
    FUNCTION_NAME_OVERLAP_ABI = [
        {
            "anonymous": False,
            "inputs": [],
            "name": "increment",
            "type": "function",
        },
        {
            "anonymous": False,
            "inputs": [],
            "name": "incrementCount",
            "type": "function",
        },
    ]
    contract = w3.eth.contract(abi=FUNCTION_NAME_OVERLAP_ABI)

    increment_func = contract.get_function_by_name("increment")
    increment_count_func = contract.get_function_by_name("incrementCount")
    assert repr(increment_func) == "<Function increment()>"
    assert repr(increment_count_func) == "<Function incrementCount()>"


def test_get_event_by_name(w3):
    EVENT_NAME_OVERLAP_ABI = [
        {
            "anonymous": False,
            "inputs": [],
            "name": "Deposit",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [],
            "name": "Deposited",
            "type": "event",
        },
    ]
    contract = w3.eth.contract(abi=EVENT_NAME_OVERLAP_ABI)

    deposit_event = contract.get_event_by_name("Deposit")
    deposited_event = contract.get_event_by_name("Deposited")

    assert repr(deposit_event) == "<Event Deposit()>"
    assert repr(deposited_event) == "<Event Deposited()>"


@pytest.mark.parametrize(
    "method,args,expected_message,expected_error",
    (
        (
            "get_function_by_signature",
            ("identity(uint256, bool)",),
            r"Function signature should not contain any spaces.*",
            Web3ValueError,
        ),
        (
            "get_function_by_name",
            ("identity",),
            r"Found multiple functions with matching name*",
            Web3ValueError,
        ),
        (
            "get_function_by_name",
            ("undefined_function",),
            r"Could not find any function with matching name",
            Web3ValueError,
        ),
        (
            "get_function_by_selector",
            (b"\x00" * (4 + 1),),
            f"expected value of size 4 bytes. Got: {(4 + 1)} bytes",
            Web3ValueError,
        ),
        (
            "get_function_by_args",
            (1, True),
            r"Found multiple functions with matching args*",
            Web3ValueError,
        ),
        (
            "get_function_by_args",
            (1,) * 50,
            r"Could not find any function with matching args",
            Web3ValueError,
        ),
    ),
)
def test_functions_error_messages(w3, method, args, expected_message, expected_error):
    contract = w3.eth.contract(abi=AMBIGUOUS_CONTRACT_ABI)
    with pytest.raises(expected_error, match=expected_message):
        getattr(contract, method)(*args)


def test_ambiguous_functions_abi_element_identifier(w3):
    abi = [
        {
            "name": "isValidSignature",
            "type": "function",
            "inputs": [
                {"internalType": "bytes32", "name": "id", "type": "bytes32"},
                {"internalType": "bytes", "name": "id", "type": "bytes"},
            ],
        },
        {
            "name": "isValidSignature",
            "type": "function",
            "inputs": [
                {"internalType": "bytes", "name": "id", "type": "bytes"},
                {"internalType": "bytes", "name": "id", "type": "bytes"},
            ],
        },
    ]
    contract = w3.eth.contract(abi=abi)
    fn_bytes = contract.get_function_by_signature("isValidSignature(bytes,bytes)")
    assert fn_bytes.abi_element_identifier == "isValidSignature(bytes,bytes)"
    fn_bytes32 = contract.get_function_by_signature("isValidSignature(bytes32,bytes)")
    assert fn_bytes32.abi_element_identifier == "isValidSignature(bytes32,bytes)"


def test_ambiguous_function_methods(ambiguous_function_contract):
    is_valid_signature_func = ambiguous_function_contract.get_function_by_signature(
        "isValidSignature()"
    )
    is_valid_signature_bytes_func = (
        ambiguous_function_contract.get_function_by_signature(
            "isValidSignature(bytes,bytes)"
        )
    )
    is_valid_signature_bytes32_func = (
        ambiguous_function_contract.get_function_by_signature(
            "isValidSignature(bytes32,bytes)"
        )
    )
    assert is_valid_signature_func().call() == "valid"
    assert is_valid_signature_bytes_func(b"hi", b"1").call() == 1
    assert (
        is_valid_signature_bytes32_func(
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",  # noqa: E501
            b"0",
        ).call()
        == 0
    )
    assert ambiguous_function_contract.functions.isValidSignature().call() == "valid"
    assert (
        ambiguous_function_contract.functions.isValidSignature(b"hi", b"1").call() == 1
    )


def test_ambiguous_function_methods_and_arguments(ambiguous_function_contract):
    # Raises because there exists a function without arguments
    # So the function that accepts a bytes32 argument is not set
    # for the ContractFunctions property with just the name
    with pytest.raises(
        MismatchedABI,
        match=re.escape(
            "Found multiple elements named `isValidSignature` that accept 2 "
            "argument(s)."
        ),
    ):
        ambiguous_function_contract.functions.isValidSignature(
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",  # noqa: E501
            b"0",
        )


def test_contract_function_methods(string_contract):
    set_value_func = string_contract.get_function_by_signature("setValue(string)")
    get_value_func = string_contract.get_function_by_signature("getValue()")
    assert isinstance(set_value_func("Hello").transact(), HexBytes)
    assert get_value_func().call() == "Hello"
    assert isinstance(set_value_func("Hello World").estimate_gas(), int)
    assert isinstance(set_value_func("Hello World").build_transaction(), dict)


def test_diff_between_fn_and_fn_called(string_contract):
    get_value_func = string_contract.get_function_by_signature("getValue()")
    get_value_func_called = get_value_func()
    assert get_value_func is not get_value_func_called
    assert repr(get_value_func) == "<Function getValue()>"
    assert repr(get_value_func_called) == "<Function getValue() bound to ()>"


def test_get_abi_element_for_ambiguous_functions() -> None:
    function_abi = get_abi_element(
        cast(ABI, AMBIGUOUS_CONTRACT_ABI),
        "identity",
        *[
            2**256 - 1,  # uint256 maximum
            False,
        ],
    )

    assert function_abi == IDENTITY_WITH_UINT_ABI

    function_abi = get_abi_element(
        cast(ABI, AMBIGUOUS_CONTRACT_ABI),
        "identity",
        *[
            -1,
            True,
        ],
    )

    assert function_abi == IDENTITY_WITH_INT_ABI

    function_abi = get_abi_element(
        cast(ABI, AMBIGUOUS_CONTRACT_ABI),
        "identity",
        *[
            False,
        ],
    )

    assert function_abi == IDENTITY_WITH_BOOL_ABI


def test_get_abi_element_for_ambiguous_function_arguments():
    function_abi = get_abi_element(
        cast(ABI, AMBIGUOUS_CONTRACT_ABI),
        "identity(int256,bool)",
        *[
            1,
            False,
        ],
    )

    assert function_abi == IDENTITY_WITH_INT_ABI

    function_abi = get_abi_element(
        cast(ABI, AMBIGUOUS_CONTRACT_ABI),
        "identity(uint256,bool)",
        *[
            1,
            False,
        ],
    )

    assert function_abi == IDENTITY_WITH_UINT_ABI
