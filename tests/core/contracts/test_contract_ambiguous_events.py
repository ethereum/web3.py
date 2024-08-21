import pytest
from typing import (
    cast,
)

from eth_typing import (
    ABI,
)

from web3.contract.contract import (
    Contract,
)
from web3.exceptions import (
    MismatchedABI,
)
from web3.utils.abi import (
    get_abi_element,
    get_abi_element_by_name_and_arguments,
)

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
    ABI_FUNCTION_DEPOSIT_STRUCT,
    ABI_FUNCTION_DEPOSIT_VALUE,
]


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


def test_get_abi_element_by_name_and_arguments_for_amibguous_tuple_events() -> None:
    event_abi = get_abi_element_by_name_and_arguments(
        cast(ABI, AMBIGUOUS_EVENT_WITH_TUPLE_CONTRACT_ABI),
        "Deposit",
        ("from", "id", "value"),
        ("address", "bytes32", "(uint256,uint256)"),
    )

    assert event_abi == ABI_EVENT_DEPOSIT_WITH_TUPLE

    event_abi = get_abi_element_by_name_and_arguments(
        cast(ABI, AMBIGUOUS_EVENT_WITH_TUPLE_CONTRACT_ABI),
        "Deposit",
        ("from", "id", "value"),
        ("address", "bytes32", "uint256"),
    )

    assert event_abi == ABI_EVENT_DEPOSIT


def test_get_event_abi_with_ambiguous_events(
    ambiguous_event_contract: "Contract",
) -> None:
    event_abi_util_method = get_abi_element(
        ambiguous_event_contract.abi, "LogSingleArg", *[], **{"arg0": 1}
    )
    event_abi_util_method_args = get_abi_element_by_name_and_arguments(
        ambiguous_event_contract.abi, "LogSingleArg", ("arg0",), ("uint256",)
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

    event_abi_event_method = (
        ambiguous_event_contract.events.LogSingleArg._get_event_abi({"arg0": "uint256"})
    )
    assert event_abi_util_method == event_abi_util_method_args == event_abi_event_method


def test_get_event_abi_with_ambiguous_events_errors(
    ambiguous_event_contract: "Contract",
) -> None:
    with pytest.raises(
        MismatchedABI,
        match="Could not find an ABI for the provided argument names and types.",
    ):
        ambiguous_event_contract.events.LogSingleArg._get_event_abi({"arg0": None})

    with pytest.raises(
        MismatchedABI,
        match="Could not find an ABI with that name and number of arguments.",
    ):
        ambiguous_event_contract.events.LogSingleArg._get_event_abi()

    with pytest.raises(
        MismatchedABI,
        match="Could not find an ABI with that name and number of arguments.",
    ):
        ambiguous_event_contract._get_event_abi("NotAnEvent")

    with pytest.raises(
        MismatchedABI,
        match="Could not find an ABI with that name and number of arguments.",
    ):
        ambiguous_event_contract._get_event_abi("LogSingleArg")


def test_get_element_abi_by_name_and_arguments_errors(
    ambiguous_event_contract: "Contract",
) -> None:
    with pytest.raises(
        MismatchedABI,
        match="Could not find an ABI due to ambiguous argument matches. ABIs "
        "must have unique signatures.",
    ):
        get_abi_element_by_name_and_arguments(
            ambiguous_event_contract.abi, "LogSingleArg", ("arg0",)
        )

    with pytest.raises(
        MismatchedABI,
        match="Could not find an ABI with that name and number of arguments.",
    ):
        get_abi_element_by_name_and_arguments(
            ambiguous_event_contract.abi, "NotAnEvent"
        )
