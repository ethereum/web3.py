import pytest

from eth_utils import is_string


@pytest.fixture(autouse=True)
def wait_for_first_block(web3, wait_for_block):
    wait_for_block(web3)


def test_eth_getBlock_by_number(web3):
    block_1 = web3.eth.getBlock(1)
    assert block_1
    assert block_1['number'] == 1
    assert all(is_string(txn) for txn in block_1['transactions'])


def test_eth_getBlock_by_hash(web3):
    block_1 = web3.eth.getBlock(1)
    block_1_hash = block_1['hash']

    block_1_by_hash = web3.eth.getBlock(block_1_hash)
    assert block_1_by_hash
    assert block_1_by_hash['number'] == 1
    assert block_1_by_hash['hash'] == block_1_hash
    assert all(is_string(txn) for txn in block_1['transactions'])


def test_eth_getBlock_by_number_with_full_transactions(web3):
    block_1 = web3.eth.getBlock(1, True)
    assert block_1['number'] == 1
    assert all(isinstance(txn, dict) for txn in block_1['transactions'])


def test_eth_getBlock_by_hash_with_full_transactions(web3):
    block_1 = web3.eth.getBlock(1, True)
    block_1_hash = block_1['hash']

    block_1_by_hash = web3.eth.getBlock(block_1_hash)
    assert block_1_by_hash
    assert block_1_by_hash['number'] == 1
    assert block_1_by_hash['hash'] == block_1_hash
    assert all(isinstance(txn, dict) for txn in block_1['transactions'])


def test_eth_getBlock_using_latest(web3):
    current_block_number = web3.eth.blockNumber

    block = web3.eth.getBlock('latest')
    block_number = block['number']

    assert block_number >= current_block_number


def test_eth_getBlock_using_earliest(web3):
    current_block_number = web3.eth.blockNumber

    block = web3.eth.getBlock('earliest')

    assert block['number'] == 0

    block_1 = web3.eth.getBlock(0)
    assert block == block_1
