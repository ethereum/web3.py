import pytest

from eth_utils import (
    keccak,
)
from hexbytes import (
    HexBytes,
)

from web3.exceptions import (
    Web3ValueError,
)


def test_build_filter_topic_signature(w3, math_contract_abi):
    contract = w3.eth.contract(abi=math_contract_abi)
    filter_builder = contract.events.Increased.build_filter()
    filter_builder.args["value"].match_any(100, 200, 300)
    _filter = filter_builder.deploy(w3)
    assert _filter.filter_params == {
        "topics": (HexBytes(keccak(text="Increased(uint256)")).to_0x_hex(),)
    }
    assert _filter.data_filter_set == (("uint256", (100, 200, 300)),)


def test_build_filter_resetting_build_filter_properties(w3, math_contract_abi):
    contract = w3.eth.contract(abi=math_contract_abi)
    filter_builder = contract.events.Increased.build_filter()
    # Address is setable from undeployed contract class
    filter_builder.address = b"\x10" * 40
    filter_builder.from_block = 0
    filter_builder.to_block = "latest"
    # Test that all filter properties can only set values once
    with pytest.raises(Web3ValueError):
        filter_builder.address = b"\x00" * 40
    with pytest.raises(Web3ValueError):
        filter_builder.from_block = 1
    with pytest.raises(Web3ValueError):
        filter_builder.to_block = 50


def test_build_filter_argument_match_single_can_only_be_set_once(w3, math_contract_abi):
    contract = w3.eth.contract(abi=math_contract_abi)
    filter_builder = contract.events.Increased.build_filter()
    filter_builder.args["value"].match_single(100)
    with pytest.raises(Web3ValueError):
        filter_builder.args["value"].match_single(200)


def test_build_filter_argument_match_any_can_only_be_set_once(w3, math_contract_abi):
    contract = w3.eth.contract(abi=math_contract_abi)
    filter_builder = contract.events.Increased.build_filter()
    filter_builder.args["value"].match_any(100, 200)
    with pytest.raises(Web3ValueError):
        filter_builder.args["value"].match_any(200, 300)


def test_deployed_build_filter_can_have_no_values_set(w3, math_contract_abi):
    contract = w3.eth.contract(abi=math_contract_abi)
    filter_builder = contract.events.Increased.build_filter()
    filter_builder.deploy(w3)
    with pytest.raises(Web3ValueError):
        filter_builder.address = b"\x00" * 40
    with pytest.raises(Web3ValueError):
        filter_builder.from_block = 1
    with pytest.raises(Web3ValueError):
        filter_builder.to_block = 50
    with pytest.raises(Web3ValueError):
        filter_builder.args["value"].match_single(200)
    with pytest.raises(Web3ValueError):
        filter_builder.args["value"].match_any(200, 300)
