import pytest

from eth_utils.toolz import (
    compose,
    curry,
)
from hexbytes import (
    HexBytes,
)

from web3.exceptions import (
    Web3ValueError,
)

AMBIGUOUS_CONTRACT_ABI = [
    {
        "constant": False,
        "inputs": [{"name": "input", "type": "uint256"}],
        "name": "blockHashAmphithyronVersify",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
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
    },
    {
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
    },
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
            "find_functions_by_name",
            ("identity",),
            map_repr,
            ["<Function identity(uint256,bool)>", "<Function identity(int256,bool)>"],
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
