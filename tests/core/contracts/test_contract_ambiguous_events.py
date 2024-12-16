import pytest
from typing import (
    cast,
)

from eth_typing import (
    ABI,
)

from web3.contract.async_contract import (
    AsyncContract,
)
from web3.contract.contract import (
    Contract,
    ContractEvent,
)
from web3.exceptions import (
    MismatchedABI,
)
from web3.main import (
    AsyncWeb3,
    Web3,
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


def test_get_abi_from_event_signature(ambiguous_event_contract: "Contract") -> None:
    expected_event_abi = {
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

    event_get_abi_result = ambiguous_event_contract.events["LogSingleArg(uint256)"].abi
    assert expected_event_abi == event_get_abi_result


def test_get_abi_from_event_call_without_args(ambiguous_event_contract: "Contract"):
    expected_event_abi = {
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

    event_get_abi_result = ambiguous_event_contract.events.LogSingleArg.abi
    assert expected_event_abi == event_get_abi_result


def test_get_abi_from_event_call_with_any_args(ambiguous_event_contract: "Contract"):
    expected_event_abi = {
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

    event_get_abi_result = ambiguous_event_contract.events.LogSingleArg().abi
    assert expected_event_abi == event_get_abi_result

    event_get_abi_result = ambiguous_event_contract.events.LogSingleArg(1).abi
    assert expected_event_abi == event_get_abi_result

    event_get_abi_result = ambiguous_event_contract.events.LogSingleArg(
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",  # noqa: E501
    ).abi
    assert expected_event_abi == event_get_abi_result

    event_get_abi_result = ambiguous_event_contract.events.LogSingleArg("hi").abi
    assert expected_event_abi == event_get_abi_result


def test_async_get_abi_from_event(
    async_ambiguous_event_contract: "AsyncContract",
) -> None:
    expected_event_abi = {
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

    event_get_abi_result = async_ambiguous_event_contract.events[
        "LogSingleArg(uint256)"
    ].abi
    assert expected_event_abi == event_get_abi_result


def test_get_abi_element_for_ambiguous_tuple_events() -> None:
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


def test_get_abi_element_with_signature_for_ambiguous_tuple_events() -> None:
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
        match=r"ABI Not Found!\nNo element named `NotAnEvent` with 0 argument\(s\).",
    ):
        get_abi_element(ambiguous_event_contract.abi, "NotAnEvent")


def test_contract_event_methods(
    w3: "Web3", ambiguous_event_contract: "Contract"
) -> None:
    log_arg_event = cast(
        ContractEvent, ambiguous_event_contract.events["LogSingleArg(uint256)"]
    )

    assert log_arg_event.abi == {
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
    assert log_arg_event.name == "LogSingleArg"
    assert log_arg_event.abi_element_identifier == "LogSingleArg(uint256)"
    assert log_arg_event.get_logs() == []

    filter_builder = log_arg_event.build_filter()
    filter_builder.from_block = "latest"
    filter_builder.to_block = "latest"
    filter_builder.args.arg0.match_single(1)
    filter_instance = filter_builder.deploy(w3)

    assert filter_instance.filter_params == {
        "fromBlock": "latest",
        "toBlock": "latest",
        "address": ambiguous_event_contract.address,
        "topics": (
            "0x56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4",
        ),
    }

    log_filter = log_arg_event.create_filter(from_block="latest")
    log_entry = {
        "address": ambiguous_event_contract.address,
        "topics": (
            "0x56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4",
        ),
        "data": "0x0000000000000000000000000000000000000000000000000000000000000005",
        "logIndex": 0,
        "transactionIndex": 0,
        "transactionHash": "0x0",
        "blockHash": "0x0",
        "blockNumber": 0,
    }
    assert log_filter.log_entry_formatter(log_entry) == {
        "args": {"arg0": 5},
        "event": "LogSingleArg",
        "logIndex": 0,
        "transactionIndex": 0,
        "transactionHash": "0x0",
        "address": ambiguous_event_contract.address,
        "blockHash": "0x0",
        "blockNumber": 0,
    }


@pytest.mark.asyncio
async def test_async_contract_event_methods(
    async_w3: "AsyncWeb3", async_ambiguous_event_contract: "AsyncContract"
) -> None:
    log_arg_event = cast(
        ContractEvent, async_ambiguous_event_contract.events["LogSingleArg(uint256)"]
    )

    assert log_arg_event.abi == {
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
    assert log_arg_event.event_name == "LogSingleArg"
    assert log_arg_event.name == "LogSingleArg"
    assert log_arg_event.abi_element_identifier == "LogSingleArg(uint256)"
    assert await log_arg_event.get_logs() == []

    filter_builder = log_arg_event.build_filter()
    filter_builder.from_block = "latest"
    filter_builder.to_block = "latest"
    filter_builder.args.arg0.match_single(1)
    filter_instance = await filter_builder.deploy(async_w3)

    assert filter_instance.filter_params == {
        "fromBlock": "latest",
        "toBlock": "latest",
        "address": async_ambiguous_event_contract.address,
        "topics": (
            "0x56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4",
        ),
    }

    log_filter = await log_arg_event.create_filter(from_block="latest")
    log_entry = {
        "address": async_ambiguous_event_contract.address,
        "topics": (
            "0x56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4",
        ),
        "data": "0x0000000000000000000000000000000000000000000000000000000000000005",
        "logIndex": 0,
        "transactionIndex": 0,
        "transactionHash": "0x0",
        "blockHash": "0x0",
        "blockNumber": 0,
    }
    assert log_filter.log_entry_formatter(log_entry) == {
        "args": {"arg0": 5},
        "event": "LogSingleArg",
        "logIndex": 0,
        "transactionIndex": 0,
        "transactionHash": "0x0",
        "address": async_ambiguous_event_contract.address,
        "blockHash": "0x0",
        "blockNumber": 0,
    }
