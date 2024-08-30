import pytest
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

from web3.contract.contract import (
    Contract,
)
from web3.exceptions import (
    MismatchedABI,
    Web3ValueError,
)
from web3.utils.abi import (
    get_abi_element,
)

ABI_EVENT_TRANSFER = {
    "anonymous": False,
    "inputs": [
        {
            "indexed": True,
            "internalType": "address",
            "name": "from",
            "type": "address",
        },
        {
            "indexed": True,
            "internalType": "address",
            "name": "to",
            "type": "address",
        },
        {
            "indexed": False,
            "internalType": "uint256",
            "name": "value",
            "type": "uint256",
        },
    ],
    "name": "Transfer",
    "type": "event",
}
ABI_EVENT_DEPOSIT_WITH_TUPLE = {
    "anonymous": False,
    "inputs": [
        {
            "indexed": True,
            "internalType": "address",
            "name": "from",
            "type": "address",
        },
        {
            "indexed": True,
            "internalType": "bytes32",
            "name": "id",
            "type": "bytes32",
        },
        {
            "components": [
                {"internalType": "uint256", "name": "x", "type": "uint256"},
                {"internalType": "uint256", "name": "y", "type": "uint256"},
            ],
            "indexed": False,
            "internalType": "struct DepositEventContract.T",
            "name": "value",
            "type": "tuple",
        },
    ],
    "name": "Deposit",
    "type": "event",
}

ABI_EVENT_DEPOSIT = {
    "anonymous": False,
    "inputs": [
        {
            "indexed": True,
            "internalType": "address",
            "name": "from",
            "type": "address",
        },
        {
            "indexed": True,
            "internalType": "bytes32",
            "name": "id",
            "type": "bytes32",
        },
        {
            "indexed": False,
            "internalType": "uint256",
            "name": "value",
            "type": "uint256",
        },
    ],
    "name": "Deposit",
    "type": "event",
}
ABI_FUNCTION_DEPOSIT_STRUCT = {
    "inputs": [{"internalType": "bytes32", "name": "id", "type": "bytes32"}],
    "name": "depositStruct",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function",
}
ABI_FUNCTION_DEPOSIT_VALUE = {
    "inputs": [{"internalType": "bytes32", "name": "id", "type": "bytes32"}],
    "name": "depositValue",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function",
}
AMBIGUOUS_EVENT_WITH_TUPLE_CONTRACT_ABI = [
    ABI_EVENT_DEPOSIT_WITH_TUPLE,
    ABI_EVENT_DEPOSIT,
    ABI_EVENT_TRANSFER,
    ABI_FUNCTION_DEPOSIT_STRUCT,
    ABI_FUNCTION_DEPOSIT_VALUE,
]

map_repr = compose(list, curry(map, repr))


@pytest.mark.parametrize(
    "method,args,repr_func,expected",
    (
        (
            "all_events",
            (),
            map_repr,
            [
                "<Event Deposit(address,bytes32,(uint256,uint256))>",
                "<Event Deposit(address,bytes32,uint256)>",
                "<Event Transfer(address,address,uint256)>",
            ],
        ),
        (
            "find_events_by_name",
            ("Deposit",),
            map_repr,
            [
                "<Event Deposit(address,bytes32,(uint256,uint256))>",
                "<Event Deposit(address,bytes32,uint256)>",
            ],
        ),
        (
            "get_event_by_name",
            ("Transfer",),
            repr,
            "<Event Transfer(address,address,uint256)>",
        ),
    ),
)
def test_find_or_get_events_by_type(w3, method, args, repr_func, expected):
    contract = w3.eth.contract(abi=AMBIGUOUS_EVENT_WITH_TUPLE_CONTRACT_ABI)
    contract_function = getattr(contract, method)(*args)
    assert repr_func(contract_function) == expected


@pytest.mark.parametrize(
    "method,args,expected_message,expected_error",
    (
        (
            "get_event_by_name",
            ("Deposit",),
            r"Found multiple events with matching name*",
            Web3ValueError,
        ),
    ),
)
def test_get_event_error_messages(w3, method, args, expected_message, expected_error):
    contract = w3.eth.contract(abi=AMBIGUOUS_EVENT_WITH_TUPLE_CONTRACT_ABI)
    with pytest.raises(expected_error, match=expected_message):
        getattr(contract, method)(*args)


def test_get_abi_element_for_amibguous_tuple_events() -> None:
    event_abi = get_abi_element(
        cast(ABI, AMBIGUOUS_EVENT_WITH_TUPLE_CONTRACT_ABI),
        "Deposit",
        *[
            "0xFe89cc7aBB2C4183683ab71653C4cdc9B02D44b7",
            b"0x0",
        ],
        **{"value": {"x": 1, "y": 2}},
    )

    assert event_abi == ABI_EVENT_DEPOSIT_WITH_TUPLE

    event_abi = get_abi_element(
        cast(ABI, AMBIGUOUS_EVENT_WITH_TUPLE_CONTRACT_ABI),
        "Deposit",
        *[
            "0xFe89cc7aBB2C4183683ab71653C4cdc9B02D44b7",
            b"0x0",
            1,
        ],
    )

    assert event_abi == ABI_EVENT_DEPOSIT


def test_get_abi_element_with_signature_for_amibguous_tuple_events() -> None:
    event_abi = get_abi_element(
        cast(ABI, AMBIGUOUS_EVENT_WITH_TUPLE_CONTRACT_ABI),
        "Deposit(address,bytes32,(uint256,uint256))",
    )

    assert event_abi == ABI_EVENT_DEPOSIT_WITH_TUPLE

    event_abi = get_abi_element(
        cast(ABI, AMBIGUOUS_EVENT_WITH_TUPLE_CONTRACT_ABI),
        "Deposit(address,bytes32,uint256)",
    )

    assert event_abi == ABI_EVENT_DEPOSIT


def test_get_abi_element_by_name_and_arguments_errors(
    ambiguous_event_contract: "Contract",
) -> None:
    with pytest.raises(
        MismatchedABI,
        match="Could not find an ABI with that name and number of arguments.",
    ):
        get_abi_element(ambiguous_event_contract.abi, "NotAnEvent")


def test_get_event_abi_with_ambiguous_events(
    ambiguous_event_contract: "Contract",
) -> None:
    event_abi_util_method = get_abi_element(
        ambiguous_event_contract.abi, "LogSingleArg", *[], **{"arg0": 1}
    )

    assert event_abi_util_method == {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "arg0",
                "type": "uint256",
            }
        ],
        "name": "LogSingleArg",
        "type": "event",
    }

    event_abi_event_method = ambiguous_event_contract.events.LogSingleArg._get_abi(
        abi_input_arguments=[{"name": "arg0", "type": "uint256"}]
    )
    assert event_abi_util_method == event_abi_event_method


def test_get_event_abi_with_ambiguous_events_errors(
    ambiguous_event_contract: "Contract",
) -> None:
    with pytest.raises(
        MismatchedABI,
        match="Could not identify the intended ABI with name",
    ):
        ambiguous_event_contract.events.LogSingleArg._get_abi(
            abi_input_arguments=[{"name": "arg0", "type": None}]
        )

    with pytest.raises(
        MismatchedABI,
        match="Could not identify the intended ABI with name",
    ):
        ambiguous_event_contract.events.LogSingleArg._get_abi()

    with pytest.raises(
        MismatchedABI,
        match="Could not identify the intended ABI with name",
    ):
        ambiguous_event_contract._get_event_abi("NotAnEvent")

    with pytest.raises(
        MismatchedABI,
        match="Could not identify the intended ABI with name",
    ):
        ambiguous_event_contract._get_event_abi("LogSingleArg")
