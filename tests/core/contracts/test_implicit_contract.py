import pytest

from eth_utils import (
    is_integer,
)

from web3.contract import (
    ImplicitContract,
)


@pytest.fixture()
def math_contract(web3, MATH_ABI, MATH_CODE, MATH_RUNTIME, address_conversion_func):
    # Deploy math contract
    # NOTE Must use non-specialized contract factory or else deploy() doesn't work
    MathContract = web3.eth.contract(
        abi=MATH_ABI,
        bytecode=MATH_CODE,
        bytecode_runtime=MATH_RUNTIME,
    )
    tx_hash = MathContract.constructor().transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    math_address = address_conversion_func(tx_receipt['contractAddress'])
    # Return interactive contract instance at deployed address
    # TODO Does parent class not implement 'deploy()' for a reason?
    MathContract = web3.eth.contract(
        abi=MATH_ABI,
        bytecode=MATH_CODE,
        bytecode_runtime=MATH_RUNTIME,
        ContractFactoryClass=ImplicitContract,
    )
    contract = MathContract(math_address)
    assert contract.address == math_address
    return contract


@pytest.fixture()
def get_transaction_count(web3):
    def get_transaction_count(blocknum_or_label):
        block = web3.eth.getBlock(blocknum_or_label)
        # Return the blocknum if we requested this via labels
        # so we can directly query the block next time (using the same API call)
        # Either way, return the number of transactions in the given block
        if blocknum_or_label in ["pending", "latest", "earliest"]:
            return block.number, len(block.transactions)
        else:
            return len(block.transactions)
    return get_transaction_count


def test_implicitcontract_call_default(math_contract, get_transaction_count):
    # When a function is called that defaults to call
    blocknum, starting_txns = get_transaction_count("pending")
    start_count = math_contract.counter()
    assert is_integer(start_count)
    # Check that a call was made and not a transact
    # (Auto-mining is enabled, so query by block number)
    assert get_transaction_count(blocknum) == starting_txns
    # Check that no blocks were mined
    assert get_transaction_count("pending") == (blocknum, 0)


def test_implicitcontract_transact_default(web3, math_contract, get_transaction_count):
    # Use to verify correct operation later on
    start_count = math_contract.counter()
    assert is_integer(start_count)  # Verify correct type
    # When a function is called that defaults to transact
    blocknum, starting_txns = get_transaction_count("pending")
    math_contract.increment(transact={})
    # Check that a transaction was made and not a call
    assert math_contract.counter() - start_count == 1
    # (Auto-mining is enabled, so query by block number)
    assert get_transaction_count(blocknum) == starting_txns + 1
    # Check that only one block was mined
    assert get_transaction_count("pending") == (blocknum + 1, 0)


def test_implicitcontract_call_override(math_contract, get_transaction_count):
    # When a function is called with transact override that defaults to call
    blocknum, starting_txns = get_transaction_count("pending")
    math_contract.counter(transact={})
    # Check that a transaction was made and not a call
    # (Auto-mining is enabled, so query by block number)
    assert get_transaction_count(blocknum) == starting_txns + 1
    # Check that only one block was mined
    assert get_transaction_count("pending") == (blocknum + 1, 0)


def test_implicitcontract_transact_override(math_contract, get_transaction_count):
    # Use to verify correct operation later on
    start_count = math_contract.counter()
    assert is_integer(start_count)  # Verify correct type
    # When a function is called with call override that defaults to transact
    blocknum, starting_txns = get_transaction_count("pending")
    math_contract.increment(call={})
    # Check that a call was made and not a transact
    assert math_contract.counter() - start_count == 0
    # (Auto-mining is enabled, so query by block number)
    assert get_transaction_count(blocknum) == starting_txns
    # Check that no blocks were mined
    assert get_transaction_count("pending") == (blocknum, 0)
