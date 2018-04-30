import pytest

from web3.exceptions import (
    MismatchedABI,
    NoABIEventsFound
)

EVENT_1_ABI = {
    "anonymous": False,
    "inputs": [
        {"indexed": False, "name": "arg0", "type": "uint256"},
        {"indexed": True, "name": "arg1", "type": "uint256"},
    ],
    "name": "Event_1",
    "type": "event",
}


def test_construct_event_filter_params_with_no_abi(web3):
    contract = web3.eth.contract()
    with pytest.raises(NoABIEventsFound):
        contract.events.thisEventDoesNotExist()


def test_construct_event_filter_params_with_no_events(web3):
    contract = web3.eth.contract(abi=[])
    with pytest.raises(NoABIEventsFound):
        contract.events.thisEventDoesNotExist()


def test_construct_event_filter_params_with_nonexistent_event(web3):
    contract = web3.eth.contract(abi=[EVENT_1_ABI])
    with pytest.raises(MismatchedABI):
        contract.events.thisEventDoesNotExist()
