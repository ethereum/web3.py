import json
import pytest

from eth_utils import (
    keccak,
)
from hexbytes import (
    HexBytes,
)

CONTRACT_ABI = json.loads('[{"constant":false,"inputs":[],"name":"return13","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"constant":true,"inputs":[],"name":"counter","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"amt","type":"uint256"}],"name":"increment","outputs":[{"name":"result","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"int256"},{"name":"b","type":"int256"}],"name":"add","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"constant":false,"inputs":[],"name":"increment","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"int256"}],"name":"multiply7","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"value","type":"uint256"}],"name":"Increased","type":"event"}]')  # noqa: E501


def test_build_filter_topic_signature(web3):
    contract = web3.eth.contract(abi=CONTRACT_ABI)
    filter_builder = contract.events.Increased.build_filter()
    filter_builder.args['value'].match_any(100, 200, 300)
    _filter = filter_builder.deploy(web3)
    assert _filter.filter_params == {
        'topics': (
            HexBytes(keccak(text="Increased(uint256)")).hex(),)}
    assert _filter.data_filter_set == (('uint256', (100, 200, 300)),)


def test_build_filter_resetting_build_filter_properties(web3):
    contract = web3.eth.contract(abi=CONTRACT_ABI)
    filter_builder = contract.events.Increased.build_filter()
    # Address is setable from undeployed contract class
    filter_builder.address = b'\x10' * 40
    filter_builder.fromBlock = 0
    filter_builder.toBlock = 'latest'
    # Test that all filter properties can only set values once
    with pytest.raises(ValueError):
        filter_builder.address = b'\x00' * 40
    with pytest.raises(ValueError):
        filter_builder.fromBlock = 1
    with pytest.raises(ValueError):
        filter_builder.toBlock = 50


def test_build_filter_argument_match_single_can_only_be_set_once(web3):
    contract = web3.eth.contract(abi=CONTRACT_ABI)
    filter_builder = contract.events.Increased.build_filter()
    filter_builder.args['value'].match_single(100)
    with pytest.raises(ValueError):
        filter_builder.args['value'].match_single(200)


def test_build_filter_argument_match_any_can_only_be_set_once(web3):
    contract = web3.eth.contract(abi=CONTRACT_ABI)
    filter_builder = contract.events.Increased.build_filter()
    filter_builder.args['value'].match_any(100, 200)
    with pytest.raises(ValueError):
        filter_builder.args['value'].match_any(200, 300)


def test_deployed_build_filter_can_have_no_values_set(web3):
    contract = web3.eth.contract(abi=CONTRACT_ABI)
    filter_builder = contract.events.Increased.build_filter()
    filter_builder.deploy(web3)
    with pytest.raises(ValueError):
        filter_builder.address = b'\x00' * 40
    with pytest.raises(ValueError):
        filter_builder.fromBlock = 1
    with pytest.raises(ValueError):
        filter_builder.toBlock = 50
    with pytest.raises(ValueError):
        filter_builder.args['value'].match_single(200)
    with pytest.raises(ValueError):
        filter_builder.args['value'].match_any(200, 300)
