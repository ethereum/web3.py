

def test_filtering_sequential_blocks_with_bounded_range(
        web3,
        emitter,
        Emitter,
        wait_for_transaction):
    builder = emitter.events.LogNoArguments.build_filter()
    builder.fromBlock = "latest"

    initial_block_number = web3.eth.blockNumber

    builder.toBlock = initial_block_number + 100
    filter_ = builder.deploy(web3)
    for i in range(100):
        emitter.functions.logNoArgs(which=1).transact()
    assert web3.eth.blockNumber == initial_block_number + 100
    assert len(filter_.get_new_entries()) == 100


def test_filtering_starting_block_range(
        web3,
        emitter,
        Emitter,
        wait_for_transaction):
    for i in range(10):
        emitter.functions.logNoArgs(which=1).transact()
    builder = emitter.events.LogNoArguments.build_filter()
    filter_ = builder.deploy(web3)
    initial_block_number = web3.eth.blockNumber
    for i in range(10):
        emitter.functions.logNoArgs(which=1).transact()
    assert web3.eth.blockNumber == initial_block_number + 10
    assert len(filter_.get_new_entries()) == 10


def test_requesting_results_with_no_new_blocks(web3, emitter):
    builder = emitter.events.LogNoArguments.build_filter()
    filter_ = builder.deploy(web3)
    assert len(filter_.get_new_entries()) == 0
