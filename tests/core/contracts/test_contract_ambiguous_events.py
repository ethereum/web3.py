from web3.contract.contract import (
    Contract,
)


def test_get_abi_from_event(ambiguous_event_contract: "Contract") -> None:
    expected_event_abi = {
        "anonymous": False,
        "inputs": [],
        "name": "LogNoArguments",
        "type": "event",
    }

    event_get_abi_result = ambiguous_event_contract.events.LogSingleArg._get_event_abi()
    assert expected_event_abi == event_get_abi_result
