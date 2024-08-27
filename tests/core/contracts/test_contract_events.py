from eth_typing import (
    ABIEvent,
)

from web3 import (
    Web3,
)
from web3.contract.contract import (
    Contract,
)


def test_find_events_by_identifier(w3: "Web3", event_contract: "Contract") -> None:
    def callable_check(event_abi: ABIEvent) -> bool:
        return event_abi["name"] == "LogSingleArg"

    contract_events = event_contract.find_events_by_identifier(
        event_contract.abi, w3, event_contract.address, callable_check
    )
    assert [repr(evt) for evt in contract_events] == ["<Event LogSingleArg(uint256)>"]
